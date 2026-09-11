# Monitoring Tools

[首页](../README.md) · [Paper list](../papers/README.md) · [Algorithms](../algorithms/README.md) · [Datasets](../datasets/README.md) · [Tools](../tools/README.md)

17项观测/评估工具，按[论文 Table IV](https://arxiv.org/html/2606.01581v2#S4.T4)收录。列表是论文快照，入口状态核验截至2026-09-09。

| 工具 | 用途 | 官方入口 | 状态说明 |
| --- | --- | --- | --- |
| LangDB | 综述强调Rust实现、路由优化与成本控制；适合作为网关式观测的例子。 | [Project / Docs](https://github.com/vllora/vllora) | 原文仓库链接重定向到vllora/vllora；保留旧名称以对应综述，当前项目名称已不同。 |
| LangFuse | 综述强调OpenTelemetry集成，并结合trace、评估及开发流程。 | [Project / Docs](https://github.com/langfuse/langfuse) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| MLFlow | 从机器学习实验管理扩展到GenAI，综述提到可为agent系统定义自定义指标。 | [Project / Docs](https://mlflow.org/genai) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| Helicone | 综述将可观测性与缓存、网关fallback相联系，用于延迟与资源管理。 | [Project / Docs](https://github.com/Helicone/helicone) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| LangWatch | 综述归纳为观测、评估和开发能力，并提到MCP服务入口。 | [Project / Docs](https://github.com/langwatch) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| LlamaTrace | 书目将其定义为托管Phoenix的LLM tracing与评估平台。 | [Project / Docs](https://phoenix.arize.com/llamatrace/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| OpenLLMetry | 基于OpenTelemetry的LLM插桩工具；综述认为prompt优化和评估支持较有限。 | [Project / Docs](https://github.com/traceloop/openllmetry) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| Arize Phoenix | 书目将其定位为开源LLM tracing与评估平台。 | [Project / Docs](https://arize.com/phoenix/) | 原文域名重定向到arize.com/phoenix/；页面可访问。 |
| Literal AI | 综述列入协作观测、评估与开发平台；现有官方迁移公告另见下方。 | [Project / Docs](https://docs.literalai.com/more/migration-guide) | 原文官网链接读取返回404；官方迁移文档公告服务仅持续至2025-10-31，故保留为历史条目。 |
| Opik | 书目将其定位为开源LLM评估平台，同时进入该表的观测能力比较。 | [Project / Docs](https://www.comet.com/site/products/opik/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| OpenInference | 面向AI可观测性的OpenTelemetry插桩与语义规范生态；属于采集层而非单一托管后台。 | [Project / Docs](https://github.com/Arize-ai/openinference) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| TruLens | 综述强调Python包、LlamaIndex等集成，以及人类反馈支持的迭代优化。 | [Project / Docs](https://www.trulens.org/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| HoneyHive | 综述强调分布式trace、多模态系统与自定义span。 | [Project / Docs](https://www.honeyhive.ai/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| PromptLayer | 从prompt管理与优化出发，综述强调prompt ranking等观测功能。 | [Project / Docs](https://www.promptlayer.com/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| AgentOpsMonitor | 综述除可观测性之外还强调运行管理；此名称对应AgentOps.ai产品。 | [Project / Docs](https://www.agentops.ai/) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| DeepEval | 综述指出其重心是评估；不要仅依据表格将其当作完整生产监控后端。 | [Project / Docs](https://github.com/confident-ai/deepeval) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |
| LangSmith | 综述归纳tracing、评估与数据集管理，以及LangChain工作流调试与优化。 | [Project / Docs](https://www.langchain.com/langsmith-platform) | 原文链接页面可访问；未安装、试用或逐项测试产品能力。 |

## Capability Matrix

六列能力按原文快照保存，未对当前版本重新实测。✓/✗不可用于断言某产品现有版本必然支持或不支持某能力。

| 工具 | System | Cost | RAG | Performance | Log | Trace |
| --- | --- | --- | --- | --- | --- | --- |
| LangDB | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ |
| LangFuse | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| MLFlow | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Helicone | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| LangWatch | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| LlamaTrace | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| OpenLLMetry | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ |
| Arize Phoenix | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Literal AI | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Opik | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| OpenInference | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ |
| TruLens | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| HoneyHive | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| PromptLayer | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| AgentOpsMonitor | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| DeepEval | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| LangSmith | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Runtime / Protocol / State Tools

这些是正文提及的支持工具，不计入上方17项。

| 资源 | 用途 | 入口 |
| --- | --- | --- |
| Ai-infra-guard | 腾讯 AI-Infra-Guard 是安全扫描工具；综述特别引用其 MCP 风险检查能力，不将项目文档当作同行评议论文。 | [Project / Docs](https://github.com/Tencent/AI-Infra-Guard) |
| OpenTelemetry: a cloud native observability framework | OpenTelemetry 提供通用遥测规范和采集基础，是统一 trace、span、指标与日志的重要基础设施。 | [Project / Docs](https://opentelemetry.io) |
| LangGraph: persistence and time travel | LangGraph 的持久化与时间旅行文档介绍检查点、恢复和分叉执行，为回滚重执行提供工程实现参考。 | [Project / Docs](https://docs.langchain.com/oss/python/langgraph/persistence) |

Literal AI 按历史条目保留；LangDB 原链接已重定向至 vLLora。原链接、当前入口和核验说明存于 [monitoring-tools.json](../data/monitoring-tools.json)。
