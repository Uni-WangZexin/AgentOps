#!/usr/bin/env python3
"""Validate the local knowledge catalog. No network or third-party packages."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read_json(name: str):
    path = ROOT / "data" / f"{name}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return []


def items(value, *keys: str) -> list:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        for key in (*keys, "items", "records"):
            if isinstance(value.get(key), list):
                return value[key]
    errors.append(f"Expected a list, or a catalog object with a list: {keys}")
    return []


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
    seen: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\s\-]", "", heading.lower()).replace(" ", "-")
        suffix = seen.get(slug, 0)
        seen[slug] = suffix + 1
        result.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return result


refs = items(read_json("references"), "references")
taxonomy = items(read_json("taxonomy"), "taxonomy")
methods = items(read_json("detection-methods"), "methods")
datasets = items(read_json("datasets"), "datasets")
tools = items(read_json("monitoring-tools"), "tools")
source = read_json("source")
papers = items(read_json("papers"), "papers")
algorithms = read_json("algorithms")
catalog_rules = read_json("catalog-rules")

for label, records, expected in [
    ("references", refs, 125),
    ("taxonomy", taxonomy, 8),
    ("detection-methods", methods, 29),
    ("datasets", datasets, 8),
    ("monitoring-tools", tools, 17),
    ("papers", papers, 98),
]:
    check(len(records) == expected, f"{label}: expected {expected}, found {len(records)}")

numbers = [r.get("number") for r in refs]
check(sorted(n for n in numbers if isinstance(n, int)) == list(range(1, 126)),
      "Reference numbers must cover 1..125 exactly once")
for ref in refs:
    n = ref.get("number")
    for field in ("title", "url", "summary_zh", "source_type", "verification"):
        check(bool(ref.get(field)), f"Reference {n}: missing {field}")
    check(urlsplit(ref.get("url", "")).scheme in {"http", "https"},
          f"Reference {n}: invalid primary link")

for method in methods:
    check(method.get("reference_number") in numbers,
          f"Unknown method reference: {method.get('name')}")
    for field in ("detection_as_survey", "mitigation_as_survey"):
        check(type(method.get(field)) is bool,
              f"Method {method.get('name')}: {field} must be boolean")

for category in taxonomy:
    check(category.get("structural_level") in {"intra-agent", "inter-agent"},
          f"Unknown structural level: {category.get('id')}")
    check(all(n in numbers for n in category.get("reference_numbers", [])),
          f"Unknown taxonomy reference: {category.get('id')}")
check(isinstance(source, dict) and source.get("version") == "v2", "Source must be pinned to v2")

scholarly_types = {"preprint", "conference_paper", "journal_article",
                   "research_paper_unspecified", "doctoral_thesis"}
scholarly_numbers = {r["number"] for r in refs if r.get("source_type") in scholarly_types}
paper_numbers = [n for p in papers for n in p.get("reference_numbers", [])]
check(set(paper_numbers) == scholarly_numbers, "Paper list must cover every scholarly reference")
check(len(paper_numbers) == len(set(paper_numbers)) == 99,
      "Each scholarly reference must belong to exactly one canonical paper record")
check(len({p.get("id") for p in papers}) == 98, "Canonical paper IDs must be unique")
check(any(p.get("reference_numbers") == [16, 104] for p in papers),
      "The known CoT duplicate must retain both original reference numbers")
group_ids = {g["id"] for g in catalog_rules.get("groups", [])}
for paper in papers:
    check(paper.get("primary_category") in group_ids,
          f"Unknown primary paper category: {paper.get('id')}")
    check(all(c in group_ids for c in paper.get("related_categories", [])),
          f"Unknown related paper category: {paper.get('id')}")
    check(bool(paper.get("survey_contexts")), f"Missing paper provenance: {paper.get('id')}")
if isinstance(algorithms, dict):
    check(algorithms.get("detection_and_mitigation") == methods,
          "Algorithm detection registry must preserve Table V records")
    for key, expected in (("root_cause_localization", 9), ("resolution_mechanisms", 10)):
        entries = algorithms.get(key, [])
        check(len(entries) == expected, f"{key}: expected {expected} entries")
        for entry in entries:
            check(all(n in numbers for n in entry.get("reference_numbers", [])),
                  f"Unknown algorithm reference: {entry.get('name', entry.get('id'))}")

markdown_files = sorted(ROOT.rglob("*.md"))
texts = {path: path.read_text(encoding="utf-8") for path in markdown_files}
for path, text in texts.items():
    # Ignore fenced examples when checking actual document navigation.
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
        destination = raw.strip().strip("<>")
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            continue
        relative, _, fragment = destination.partition("#")
        target = (path.parent / unquote(relative)).resolve() if relative else path
        check(target.is_relative_to(ROOT), f"{path.name}: link escapes repository: {destination}")
        check(target.exists(), f"{path.relative_to(ROOT)}: missing local target {destination}")
        if fragment and target in texts:
            check(unquote(fragment) in anchors(texts[target]),
                  f"{path.relative_to(ROOT)}: missing anchor {destination}")

ref_doc = texts.get(ROOT / "docs" / "references.md", "")
for n in range(1, 126):
    check(f"ref-{n}" in anchors(ref_doc), f"Missing reference anchor ref-{n}")

bib_path = ROOT / "references.bib"
if bib_path.exists():
    bib = bib_path.read_text(encoding="utf-8")
    keys = re.findall(r"^@\w+\{([^,]+),", bib, re.M)
    check(len(keys) == len(set(keys)), "Duplicate BibTeX keys")
    check("wang2026agentops" in keys, "Missing main paper BibTeX key wang2026agentops")
    check(len(keys) >= 126, "Expected main paper plus 125 source-numbered BibTeX entries")
else:
    errors.append("Missing references.bib")

if errors:
    print("Catalog validation FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"PASS: {len(papers)} paper records / {len(refs)} reference entries, {len(taxonomy)} anomaly categories, "
      f"{len(methods)} detection/mitigation methods, {len(datasets)} datasets, "
      f"{len(tools)} tools, {len(markdown_files)} Markdown files.")
print("Local metadata and navigation checks only; external availability and experimental reproduction are not tested.")
