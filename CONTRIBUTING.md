# Contributing

本仓库维护按AgentOps综述分类的paper、算法、数据集与工具清单。

- 提供原论文或官方项目链接，以及归入该类别的依据。
- 保留原文编号；同一论文的跨类关联不重复计入总数。
- 区分研究论文、工具、方法与数据集；数据规模写清单位。
- 只补充有来源的Project / Data链接，未确认字段留空。
- 更新`data/`和`scripts/build_catalog.py`后重新生成目录并校验。

```bash
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

详细规则见 [Collection Rules](docs/collection-rules.md)。
