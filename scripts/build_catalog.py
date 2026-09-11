#!/usr/bin/env python3
"""Build the paper/resource catalogs from local source metadata. No network."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
refs=json.loads((R/'data/references.json').read_text()); by={r['number']:r for r in refs}
methods=json.loads((R/'data/detection-methods.json').read_text())
datasets=json.loads((R/'data/datasets.json').read_text())
GROUPS=[
 ('reasoning','推理异常 · Reasoning',[1,9,15,16,17,18,19,72,73,76,77,78,79,90,110],'S2.SS2.SSS1'),
 ('action','动作异常 · Action',[4,20,21,80,92,94,103,106],'S2.SS2.SSS2'),
 ('memory','记忆异常 · Memory',[23,24,25,26,27,28,81,82,83,112],'S2.SS2.SSS3'),
 ('security','安全异常 · Security',[10,30,32,33,71,84,108],'S2.SS2.SSS4'),
 ('task-specification','任务规范异常 · Task Specification',[31,34,36,85,86,87,88,89],'S2.SS3.SSS1'),
 ('orchestration','编排异常 · Orchestration',[14,37,38,39,91,93,105],'S2.SS3.SSS2'),
 ('communication','通信异常 · Communication',[41,95],'S2.SS3.SSS3'),
 ('termination','终止异常 · Termination',[43,44,45],'S2.SS3.SSS4'),
 ('monitoring','监控与可观测性 · Monitoring',[51,52,53,74,75],'S4'),
 ('root-cause','根因定位与失败归因 · Root Cause Localization',[7,12,96,97,98,99,100,101,102],'S6'),
 ('resolution','纠错与恢复 · Resolution',[107,109,113,114,115,116],'S7'),
 ('benchmarks','数据与评测 · Datasets & Benchmarks',[13,117,118,119,120,121,122,123,124,125],'S8'),
 ('background','背景与应用 · Background',[3,5,6,8,11,46,47,48],'S1')]
# Primary groups are an editorial navigation placement; all additional relations retain their own source.
CROSS={14:['reasoning','resolution'],16:['resolution'],19:['reasoning'],21:['security'],25:['benchmarks'],27:['reasoning'],28:['benchmarks'],30:['benchmarks'],31:['termination'],33:['task-specification','root-cause'],38:['resolution'],43:['orchestration'],72:['monitoring'],73:['monitoring'],74:['resolution'],78:['resolution'],85:['action'],86:['benchmarks'],87:['benchmarks'],88:['resolution'],89:['reasoning'],90:['task-specification'],92:['orchestration','benchmarks'],93:['resolution','memory'],94:['orchestration'],96:['root-cause'],99:['benchmarks'],102:['benchmarks','resolution'],103:['resolution'],105:['resolution'],106:['resolution'],110:['resolution'],112:['resolution'],12:['termination','benchmarks'],117:['task-specification','communication','termination'],118:['root-cause'],119:['root-cause'],120:['root-cause'],121:['root-cause']}
# Corrections to navigation assignments must never be confused with the survey's dataset-coverage matrix.
ALIAS={1:'DeepSeek-R1',4:'ToolLLM',12:'Who&When',14:'ReAct',16:'CoT',19:'Honesty',23:'Lost in the Middle',24:'PI-LLM',25:'QE-RAG',26:'Astute RAG',27:'ReDeEP',28:'RAG Benchmark',30:'ASB',31:'MAST workshop',33:'SentinelAgent',36:'AgentFM',38:'AutoGen',39:'CAMEL',41:'AgentPrune',43:'Smurfs',44:'ReDel',45:'Neural Howlround',51:'AgentOps Observability',52:'CHANGE',53:'AgentOps Automation',72:'OPERA',73:'SAPLMA',74:'ARC',75:'WebTestPilot',76:'LURE',77:'Conformal',78:'Debate',79:'CoK',80:'MCP Guardian',81:'PI',82:'CoA',83:'LRP4RAG',84:'GUARDIAN',85:'SpecValidator',86:'Ambig-SWE',87:'CLAMBER',88:'Ask-or-Assume',89:'Semantic Entropy',90:'SelfCheckGPT',91:'Introspective',92:'API-bank',93:'Reflexion',94:'CodeAct',95:'G-Designer',96:'FAMAS',97:'GraphTracer',98:'AgenTracer',99:'AgentFail',101:'StepFinder',102:'AgentDebug',103:'SWE-agent',105:'Tree of Thoughts',106:'Toolformer',107:'Self-Refine',108:'AgentSpec',109:'Comfrey',110:'Self-Consistency',112:'Voyager',113:'AutoPrompt',114:'P-Tuning v2',115:'DePT',116:'Promptbreeder',117:'MAST',118:'TRAIL',119:'AEGIS',120:'MP-Bench',121:'LongRCA Bench',122:'GAIA',123:'ALFWorld',124:'WebShop',125:'SpecOps'}
project={d['survey_reference_number']:d['project_url'] for d in datasets['datasets']}
data_urls={d['survey_reference_number']:d['data_url'] for d in datasets['datasets']}
# Official environment links have already been checked in the source dataset catalog.
for n,url in [(122,'https://huggingface.co/datasets/gaia-benchmark/GAIA'),(123,'https://github.com/alfworld/alfworld'),(124,'https://github.com/princeton-nlp/WebShop')]:project[n]=url
primary={n:g[0] for g in GROUPS for n in g[2]}
assert len(primary)==98
scholarly={r['number'] for r in refs if r['source_type'] in {'preprint','conference_paper','journal_article','research_paper_unspecified','doctoral_thesis'}}
assert scholarly==set(primary)|{104},scholarly.symmetric_difference(set(primary)|{104})
papers=[]
for n in sorted(primary):
 r=by[n]; ids=[n,104] if n==16 else [n]
 contexts=[c for k in ids for c in by[k]['cited_contexts']]
 papers.append({'id':f'paper-{n}','reference_numbers':ids,'name':ALIAS.get(n),'title':r['title'],'year':r['year'],'venue_as_cited':r['venue_as_cited'],'source_type':r['source_type'],'paper_url':r['url'],'project_url':project.get(n),'data_url':data_urls.get(n),'summary_zh':r['summary_zh'],'primary_category':primary[n],'related_categories':CROSS.get(n,[]),'classification_basis':'editorial_navigation_from_survey_contexts; formal method categories remain in detection-methods.json','survey_contexts':contexts,'verification_status':r['verification']['status'],'notes':r['notes']})
(R/'data/papers.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2)+'\n')
rules={'baseline':'arXiv:2606.01581v2','updated':'2026-09-10','source_check_date':'2026-09-09','paper_count':98,'scholarly_reference_count':99,'bibliography_entry_count':125,'duplicate_merges':[{'canonical':16,'aliases':[104],'reason':'Same CoT paper and same direct paper URL'}],'groups':[{'id':i,'title':t,'references':n,'source_section':s} for i,t,n,s in GROUPS],'related_categories':{str(k):v for k,v in CROSS.items()},'paper_inclusion_types':sorted({p['source_type'] for p in papers})}
(R/'data/catalog-rules.json').write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n')
# Algorithm registry keeps methods, diagnostic strategies and resolution mechanisms separate.
rca=[('FAMAS',[96],'trajectory-spectrum','成败轨迹 / state–action–agent 元组','可疑智能体与动作排序','结合失败频率、重复程度和动作中心性计算可疑度。'),('GraphTracer',[97],'structured-trace','信息依赖图','上游错误节点','沿信息流反向追踪下游错误的来源。'),('AgenTracer',[98],'structured-trace','故障注入与反事实回放轨迹','责任智能体与步骤','用可控生成的失败轨迹训练归因模型。'),('Causal attribution',[100],'structured-trace','结构化因果图','责任主体与关键动作','以因果结构和反事实推断进行归因。'),('SentinelAgent',[33],'structured-trace','智能体交互图与执行动态','异常协作与行为模式','以图结构与分层监测支持异常位置分析。'),('StepFinder',[101],'structured-trace','轨迹的时序语义特征','根因步骤','语义特征与时序建模结合，处理跨步骤依赖。'),('Who&When',[12],'llm-attribution','失败日志','责任智能体、决定性步骤','All-at-once、Step-by-step、Binary Search三种归因方式。'),('AgentFail',[99],'llm-attribution','工作流日志与故障分类知识','故障位置、根因','用细粒度故障分类引导语义归因。'),('AgentDebug',[102],'llm-attribution','执行轨迹与错误分类','诊断反馈与修复指导','将分类感知诊断与轨迹重规划衔接。')]
resolution=[('task-respecification','任务重述与细化','pre-execution',[16,14,105],'补充目标、约束、成功判据与子任务。'),('plan-verification','计划验证','pre-execution',[38],'执行前验证计划的可行性、依赖和约束。'),('action-restriction','动作空间约束','pre-execution',[106,103],'限制工具、接口、参数与执行环境。'),('observation-replanning','观察驱动重规划','in-execution',[14],'利用新观察调整后续行动。'),('self-correction','自我修正','in-execution',[107,93],'通过批评、反馈、反思改进中间结果。'),('runtime-enforcement','运行时约束与修复','in-execution',[108,109],'拦截不合法动作，修复格式和接口集成错误。'),('redundant-selection','冗余执行与选择','in-execution',[110,78,38],'生成多个候选，通过一致性、投票或验证器选择。'),('rollback-reexecution','回滚与重执行','post-execution',[74,111],'恢复到已保存状态，从修正点继续执行。'),('memory-skill-update','记忆与技能更新','post-execution',[93,112],'保存经验、反思与可复用技能。'),('policy-prompt-revision','策略与提示修订','post-execution',[113,114,115,116],'持久改进后续运行的提示和策略。')]
algo={'detection_and_mitigation':methods,'root_cause_localization':[{'name':n,'reference_numbers':rs,'category':c,'input':i,'output':o,'summary_zh':s,'source':'https://arxiv.org/html/2606.01581v2#S6'} for n,rs,c,i,o,s in rca],'resolution_mechanisms':[{'id':i,'name_zh':n,'phase':p,'reference_numbers':rs,'summary_zh':s,'source':'https://arxiv.org/html/2606.01581v2#S7'} for i,n,p,rs,s in resolution]}
(R/'data/algorithms.json').write_text(json.dumps(algo,ensure_ascii=False,indent=2)+'\n')

def cell(s):return str(s or '—').replace('|','\\|').replace('\n',' ')
def table(headers, rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(cell(c) for c in row)+' |' for row in rows])+'\n'
def link(label,url):return f'[{label}]({url})' if url else '—'
def source(anchor):return 'https://arxiv.org/html/2606.01581v2#'+anchor
def venue(r):
 v=r['venue_as_cited'] or ''
 if r['source_type']=='preprint':return 'arXiv'
 for key,value in [('Workshop','ICLR Workshop'),('Learning Representations','ICLR'),('Forty-first International Conference on Machine Learning','ICML'),('Forty-second International Conference on Machine Learning','ICML'),('41st International Conference on Machine Learning','ICML'),('neural information processing','NeurIPS'),('Findings of the Association','Findings EMNLP'),('System Demonstrations','EMNLP Demo'),('Nations of the Americas','NAACL'),('31st International Conference on Computational Linguistics','COLING'),('Empirical Methods','EMNLP'),('Association for Computational Linguistics','ACL'),('AdNLP 2025','AdNLP'),('International Symposium on Leveraging','ISoLA'),('CVPR','CVPR'),('computer vision and pattern recognition','CVPR'),('AAAI','AAAI'),('Foundations of Software Engineering','FSE'),('First conference on language modeling','COLM'),('Transactions on Information Systems','ACM TOIS'),('Computing Surveys','ACM CSUR'),('Transactions of the Association','TACL'),('Proceedings of the ACM on Software Engineering','PACMSE'),('Companion Proceedings','WWW Companion')]:
  if key.lower() in v.lower():
   if v.startswith('Transactions of the Association'):return 'TACL'
   return value
 return v or ('学位论文' if r['source_type']=='doctoral_thesis' else '未标明')
def reflink(n,prefix=''):
 return link(str(n),prefix+'docs/references.md#ref-'+str(n))
def resource_links(n):
 out=[link('Paper' if n in scholarly else 'Project / Docs',by[n]['url'])]
 if n in project:out.append(link('Project',project[n]))
 if n in data_urls:out.append(link('Data',data_urls[n]))
 return ' · '.join(out)
def paper_table(ns,prefix='',full=True):
 rows=[]
 for n in sorted(ns,key=lambda x:(-(by[x]['year'] or 0),x)):
  r=by[n]
  label=ALIAS.get(n)
  title=(f'**{label}** — ' if label else '')+link(r['title'],r['url'])
  metadata=f"{r['year'] or '—'} / {venue(r)}"
  extra=[reflink(n,prefix)]
  if n==16:extra.append(reflink(104,prefix))
  if n in project:extra.append(link('Project',project[n]))
  if n in data_urls:extra.append(link('Data',data_urls[n]))
  rows.append([metadata,title,r['summary_zh'],' · '.join(extra)])
 return table(['年份 / 来源¹','论文','简介 / 在该领域的用途','资源'],rows)
def header(name):return f'# {name}\n\n[首页](../README.md) · [Paper list](../papers/README.md) · [Algorithms](../algorithms/README.md) · [Datasets](../datasets/README.md) · [Tools](../tools/README.md)\n\n'

dataset_scale={'who-and-when':'184 个失败任务','mast-data':'1,642 条执行轨迹','trail':'148 条轨迹 / 841 个错误','agentfail':'307 条失败轨迹','aegis':'9,533 条轨迹 / 24,843 个错误','agenterrorbench':'200 条轨迹','mp-bench':'289 条日志（论文口径）','longrca-bench':'1,140 条轨迹'}
dataset_name={'who-and-when':'Who&When','mast-data':'MAST-Data','trail':'TRAIL','agentfail':'AgentFail','aegis':'AEGIS','agenterrorbench':'AgentErrorBench','mp-bench':'MP-Bench','longrca-bench':'LongRCA Bench'}
def ds_table(prefix=''):
 return table(['数据集','任务 / 标签','规模与单位','入口'],[[link(dataset_name[d['id']],prefix+'datasets/README.md#'+d['id']),d['purpose'],dataset_scale[d['id']],' · '.join([link('Paper',d['paper_url']),link('Project',d['project_url']),link('Data',d['data_url'])])] for d in datasets['datasets']])

root='''# AgentOps — Papers, Datasets & Algorithms

围绕论文 **[Agent System Operations: Categorization, Challenges, and Future Directions](https://arxiv.org/abs/2606.01581v2)** 整理的资源清单。按异常类别、运维阶段和方法路线收录论文、数据集、算法与工具。

**[Paper list](papers/README.md) · [Algorithms](algorithms/README.md) · [Datasets](datasets/README.md) · [Tools](tools/README.md) · [BibTeX](references.bib)**

98 条研究文献记录 · 29 项检测/缓解方法 · 9 项根因定位方法 · 10 类处置机制 · 8 个 AgentOps 基准 · 17 个监控工具。

> 整理基线：arXiv v2，2026-09-06。资源链接核验：2026-09-09；目录更新：2026-09-10。98 条研究记录对应原文 99 条研究类引用，合并了 CoT [16]/[104] 的明确重复；全部 125 条原始书目保留在[引用索引](docs/references.md)。¹年份、会议与期刊默认沿用综述，预印本和最终会议版本差异见引用索引。

## Contents

- **Intra-agent anomalies**：[Reasoning](#reasoning) · [Action](#action) · [Memory](#memory) · [Security](#security)
- **Inter-agent anomalies**：[Task Specification](#task-specification) · [Orchestration](#orchestration) · [Communication](#communication) · [Termination](#termination)
- **AgentOps stages**：[Monitoring](#monitoring) · [Root Cause Localization](#root-cause) · [Resolution](#resolution)
- **Evaluation**：[Datasets](#datasets) · [Benchmark papers](#benchmarks)
- **Supporting resources**：[Background](#background) · [Algorithms](algorithms/README.md) · [Tools](tools/README.md)

## Paper List

下面按主要研究主题陈列，每条研究记录只出现一次；跨类别关联及论文中的引用位置见[交叉分类索引](papers/README.md)。主类是便于检索的目录位置，方法的正式类别仍按论文 Table V / §VI / §VII 保存。

'''
for gid,title,ns,anchor in GROUPS:
 root+=f'<a id="{gid}"></a>\n\n### {title}\n\n[综述对应章节]({source(anchor)}) · [相关类别交叉索引](papers/README.md#{gid})\n\n'+paper_table(ns)+'\n'
root+='''<a id="datasets"></a>

## Datasets & Benchmarks

以 **Paper / Project / Data** 区分论文、项目和数据入口。下表统一标明计数单位；原文 `#Fail.`、标签覆盖和访问条件见[数据集目录](datasets/README.md)。

'''+ds_table()+'''
## Algorithms & Tools

| 目录 | 组织规则 | 主要内容 |
| --- | --- | --- |
| [Detection & Mitigation](algorithms/README.md#detection) | 异常类型 → 方法类别 | 白盒/灰盒/黑盒、MCP、记忆、图模型、任务澄清、单步/多步规划、通信优化 |
| [Root Cause Localization](algorithms/README.md#localization) | 轨迹谱分析 / 结构化轨迹 / LLM 归因 | FAMAS、GraphTracer、AgenTracer、StepFinder、Who&When、AgentFail 等 |
| [Resolution](algorithms/README.md#resolution) | 执行前 / 执行中 / 执行后 | 任务细化、计划验证、自我修正、运行时修复、回滚、记忆技能更新 |
| [Monitoring Tools](tools/README.md) | 工具类型与观测能力 | 17 项工具、官方入口、Table IV 能力矩阵 |

## Maintain This List

数据源在 `data/`；修改后运行：

```bash
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

收录范围、分类关系和去重规则见 [Collection Rules](docs/collection-rules.md)。完整引用见 [references.bib](references.bib)，更正方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
'''
(R/'README.md').write_text(root)

pdoc=header('Paper List')+'''按综述的分类与叙述建立交叉索引。**同一文献可以出现在多个相关类别**，因为异常类别、检测方法和运维阶段是不同维度。

- 首页提供按主类排列的98条研究记录；本页增加跨类关联。
- 每行的 [编号] 可查看作者、原文引用位置和核验说明。
- 工具文档、博客、模型卡与白皮书不计入研究论文总数，单列在末尾。
- ¹年份和来源采用综述记录，不能据此把所有年份理解为首次公开年份。

'''
for gid,title,ns,anchor in GROUPS:
 allns=sorted(set(ns)|{n for n,gs in CROSS.items() if gid in gs})
 pdoc+=f'<a id="{gid}"></a>\n\n## {title}\n\n'+paper_table(allns,'../')+'\n'
nonpapers=[r for r in refs if r['number'] not in scholarly]
pdoc+='## 非研究论文来源\n\n工具/官方文档、模型卡、博客和白皮书分别标注，不与论文混计。\n\n'+table(['类型','条目','说明','原文编号'],[[r['source_type'],link(r['title'],r['url']),r['summary_zh'],reflink(r['number'],'../')] for r in nonpapers])
(R/'papers/README.md').write_text(pdoc)

adoc=header('Algorithms & Methods')+'''按论文的方法分类整理。检测、缓解、根因定位与处置机制分表列出，不将工具、训练方法和数据集混称为检测算法。

**[Detection / Mitigation](#detection) · [Root Cause Localization](#localization) · [Resolution](#resolution)**

<a id="detection"></a>

## Detection & Mitigation

29 项，按[原文 Table V](https://arxiv.org/html/2606.01581v2#S5.T5)。D = 检测；M = 缓解。输入与输出为原文概括，代码复现前仍需检查原论文的实际依赖。

'''
anomap={'Reasoning Anomalies':'reasoning','Action Anomalies':'action','Memory Anomalies':'memory','Security Anomalies':'security','Task Specification Anomalies':'task-specification','Orchestration Anomalies':'orchestration','Communication Anomalies':'communication'}
for gid,title,_,_ in GROUPS[:8]:
 ms=[m for m in methods if anomap[m['anomaly_type_as_survey']]==gid]
 adoc+=f'### {title}\n\n'
 if not ms:
  adoc+='原文 Table V 未单列终止检测算法，提到任务成功状态和执行步数等规则；相关失败研究见 [Termination papers](../papers/README.md#termination)。\n\n';continue
 adoc+=table(['方法','路线','输入 → 输出','D / M','主要思想','资源'],[[m['name'],m['category_as_survey'],m['input_as_survey']+' → '+m['output_as_survey'],('✓' if m['detection_as_survey'] else '—')+' / '+('✓' if m['mitigation_as_survey'] else '—'),by[m['reference_number']]['summary_zh'],resource_links(m['reference_number'])+' · '+reflink(m['reference_number'],'../')] for m in ms])+'\n'
adoc+='''<a id="localization"></a>

## Root Cause Localization

按[原文 §VI](https://arxiv.org/html/2606.01581v2#S6)分为轨迹回放/谱分析、结构化轨迹、LLM 归因。表内方法可与数据集同名，二者角色分别维护。

'''
for category,title in [('trajectory-spectrum','Trajectory Replay & Spectrum Analysis'),('structured-trace','Structured Trace Modeling'),('llm-attribution','LLM-based Attribution')]:
 adoc+='### '+title+'\n\n'+table(['方法','输入','输出','核心思路','资源'],[[a['name'],a['input'],a['output'],a['summary_zh'],resource_links(a['reference_numbers'][0])] for a in algo['root_cause_localization'] if a['category']==category])+'\n'
adoc+='''<a id="resolution"></a>

## Resolution

以下是[原文 §VII](https://arxiv.org/html/2606.01581v2#S7)的10类**处置机制**，每类链接对应方法论文/实现文档；机制数量不等于独立算法数量。

'''
for phase,title in [('pre-execution','Pre-execution · 执行前预防'),('in-execution','In-execution · 执行中纠正'),('post-execution','Post-execution · 执行后恢复')]:
 adoc+='### '+title+'\n\n'+table(['机制','作用','代表方法 / 论文'],[[a['name_zh'],a['summary_zh'],' · '.join(link(ALIAS.get(n,'LangGraph' if n==111 else by[n]['title']),by[n]['url']) for n in a['reference_numbers'])] for a in algo['resolution_mechanisms'] if a['phase']==phase])+'\n'
adoc+='## 实现入口\n\n`Project`仅在已有核验记录提供原始项目时列出，未列出不表示作者没有开源。本文不提供重写算法或复现性能声明。输入数据与标签应对照[数据集目录](../datasets/README.md)选择。\n'
(R/'algorithms/README.md').write_text(adoc)

# Dataset list: emphasize resource links and comparable units, move long notes into collapsible details.
ddoc=header('Datasets & Benchmarks')+'''原文 Table VIII 的8项 AgentOps 数据集/基准，另列正文提及的通用任务环境。数据集以正式名称列出，综述别名在对应条目保留。

'''+ds_table('../')+'\n## Labels & Coverage\n\n以下覆盖判断来自[原文 Table IX](https://arxiv.org/html/2606.01581v2#S8.T9)，不是本仓库重新标注。✓=明确覆盖；—=很少或无实质覆盖。\n\n'
keys=['reasoning','action','memory','security','task_specification','communication','termination','orchestration']
ddoc+=table(['数据集','推理','动作','记忆','安全','任务规范','通信','终止','编排'],[[dataset_name[d['id']]]+['✓' if d['survey_taxonomy_coverage'][k]=='explicit' else '—' for k in keys] for d in datasets['datasets']])
ddoc+='\n## Resource Details\n\n'
for d in datasets['datasets']:
 ddoc+=f'<a id="{d["id"]}"></a>\n\n### {dataset_name[d["id"]]}\n\n'+d['introduction']+'\n\n'
 ddoc+=table(['Paper','Project','Data'],[[link('论文',d['paper_url']),link('项目',d['project_url']),link('数据',d['data_url'])]])+'\n'
 ddoc+=table(['字段','内容'],[['规模',dataset_scale[d['id']]],['标签',d['annotation']],['系统/环境（综述）',d['survey_statistics']['systems_as_reported']],['综述名称 / #Fail. / #Types',f"{d['survey_name']} / {d['survey_statistics']['failure_count_as_reported']} / {d['survey_statistics']['type_count_as_reported'] or '未提供'}"],['Single RC / Scalability（综述）',f"{d['survey_statistics']['single_rc_as_reported']} / {d['survey_statistics']['scalability_as_reported']}"],['访问状态',d['data_access']],['许可',d['dataset_license']]])+'\n'
 ddoc+='<details>\n<summary>统计口径、版本差异与核验来源</summary>\n\n'+d['quantity_note']+'\n\n'+d['scalability_note']+'\n\n'
 if d['differences']:ddoc+='\n'.join('- '+v for v in d['differences'])+'\n\n'
 ddoc+='来源：'+' · '.join(link(str(i+1),u) for i,u in enumerate(d['sources']))+'。核验日期：'+d['checked_at']+'。\n\n</details>\n\n'
ddoc+='''## Upstream Task Benchmarks

用于生成agent运行轨迹的任务环境，**不计入上述8项归因基准**。

'''+table(['基准','用途','论文','项目 / 数据'],[['GAIA','通用助手推理、检索与工具任务',link('Paper',by[122]['url']),link('Data',project[122])],['ALFWorld','文本与具身交互任务',link('Paper',by[123]['url']),link('Project',project[123])],['WebShop','满足用户约束的网页购物交互',link('Paper',by[124]['url']),link('Project',project[124])]])+'\n'
ddoc+='## Other Benchmarks Mentioned in the Survey\n\n这些出现在异常与方法章节中，不与Table VIII数据集混计；这里只记录已核实的论文入口，不推定数据已公开。\n\n'+table(['资源','关注问题','论文'],[[ALIAS[n],by[n]['summary_zh'],link('Paper',by[n]['url'])] for n in [25,28,30,87,92,125]])+'\n'
ddoc+='原始 `#Fail.` 的单位不统一，不可直接求和。`Single RC`是综述的归因设定判断，不等于每条轨迹只有一个错误标签。所有原值和更详细访问说明保留于 [datasets.json](../data/datasets.json)。\n'
(R/'datasets/README.md').write_text(ddoc)

tools=json.loads((R/'data/monitoring-tools.json').read_text())['tools']
tdoc=header('Monitoring Tools')+'''17项观测/评估工具，按[论文 Table IV](https://arxiv.org/html/2606.01581v2#S4.T4)收录。列表是论文快照，入口状态核验截至2026-09-09。

'''+table(['工具','用途','官方入口','状态说明'],[[t['name'],t['introduction_from_survey'],link('Project / Docs',t.get('resolved_url') or t['cited_url']),t['endpoint_status']] for t in tools])+'\n## Capability Matrix\n\n六列能力按原文快照保存，未对当前版本重新实测。✓/✗不可用于断言某产品现有版本必然支持或不支持某能力。\n\n'+table(['工具','System','Cost','RAG','Performance','Log','Trace'],[[t['name']]+['✓' if t['capabilities_snapshot'][k] else '✗' for k in ['system','cost','rag','performance','log','trace']] for t in tools])+'\n'
tdoc+='## Runtime / Protocol / State Tools\n\n这些是正文提及的支持工具，不计入上方17项。\n\n'+table(['资源','用途','入口'],[[by[n]['title'],by[n]['summary_zh'],link('Project / Docs',by[n]['url'])] for n in [22,50,111]])+'\n'
tdoc+='Literal AI 按历史条目保留；LangDB 原链接已重定向至 vLLora。原链接、当前入口和核验说明存于 [monitoring-tools.json](../data/monitoring-tools.json)。\n'
(R/'tools/README.md').write_text(tdoc)
print('Built resource-first README, paper cross-index, algorithm list, dataset list and tools list.')
