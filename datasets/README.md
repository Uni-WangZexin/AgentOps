# Datasets & Benchmarks

[首页](../README.md) · [Paper list](../papers/README.md) · [Algorithms](../algorithms/README.md) · [Datasets](../datasets/README.md) · [Tools](../tools/README.md)

原文 Table VIII 的8项 AgentOps 数据集/基准，另列正文提及的通用任务环境。数据集以正式名称列出，综述别名在对应条目保留。

| 数据集 | 任务 / 标签 | 规模与单位 | 入口 |
| --- | --- | --- | --- |
| [Who&When](../datasets/README.md#who-and-when) | 责任智能体与决定性步骤定位；适合复现较早的归因基线。 | 184 个失败任务 | [Paper](https://arxiv.org/abs/2505.00212) · [Project](https://github.com/ag2ai/Agents_Failure_Attribution) · [Data](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| [MAST-Data](../datasets/README.md#mast-data) | 失败模式多标签分类、系统设计比较、自动标注研究。 | 1,642 条执行轨迹 | [Paper](https://arxiv.org/abs/2503.13657) · [Project](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · [Data](https://huggingface.co/datasets/mcemri/MAST-Data) |
| [TRAIL](../datasets/README.md#trail) | 从长trace识别错误span、分类错误并解释影响。 | 148 条轨迹 / 841 个错误 | [Paper](https://arxiv.org/abs/2505.08638) · [Project](https://github.com/patronus-ai/trail-benchmark) · [Data](https://huggingface.co/datasets/PatronusAI/TRAIL) |
| [AgentFail](../datasets/README.md#agentfail) | 平台工作流的故障定位、根因分类与修复研究。 | 307 条失败轨迹 | [Paper](https://arxiv.org/abs/2509.23735) · [Project](https://github.com/Jenna-Ma/JaWs-AgentFail) · [Data](https://github.com/Jenna-Ma/JaWs-AgentFail) |
| [AEGIS](../datasets/README.md#aegis) | 可控错误生成、错误智能体/模式识别，以及诊断模型训练。 | 9,533 条轨迹 / 24,843 个错误 | [Paper](https://arxiv.org/abs/2509.14295) · [Project](https://github.com/kfq20/AEGIS) · [Data](https://huggingface.co/datasets/Fancylalala/AEGIS) |
| [AgentErrorBench](../datasets/README.md#agenterrorbench) | 单智能体模块化错误分析、根因定位及反馈恢复。 | 200 条轨迹 | [Paper](https://arxiv.org/abs/2509.25370) · [Project](https://github.com/ulab-uiuc/AgentDebug) · [Data](https://drive.google.com/drive/folders/1bQe6dQA85pktT63YnKIKJDTVaH3O3Vpu?usp=drive_link) |
| [MP-Bench](../datasets/README.md#mp-bench) | 多视角归因、步骤排序及解释质量评测。 | 289 条日志（论文口径） | [Paper](https://arxiv.org/abs/2603.25001) · [Project](https://github.com/yeonjun-in/MP-Bench) · [Data](https://github.com/adobe-research/multi-agent-eval-bench/tree/main/MP-Bench) |
| [LongRCA Bench](../datasets/README.md#longrca-bench) | 长轨迹根因检索、责任角色预测与精确步骤定位。 | 1,140 条轨迹 | [Paper](https://arxiv.org/abs/2608.15242) · [Project](https://longrca-bench.github.io/) · [Data](https://huggingface.co/datasets/CLoud5-real/longrca-bench) |

## Labels & Coverage

以下覆盖判断来自[原文 Table IX](https://arxiv.org/html/2606.01581v2#S8.T9)，不是本仓库重新标注。✓=明确覆盖；—=很少或无实质覆盖。

| 数据集 | 推理 | 动作 | 记忆 | 安全 | 任务规范 | 通信 | 终止 | 编排 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Who&When | ✓ | ✓ | — | — | — | — | — | — |
| MAST-Data | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — |
| TRAIL | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| AgentFail | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ |
| AEGIS | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — |
| AgentErrorBench | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| MP-Bench | ✓ | ✓ | — | — | — | — | — | — |
| LongRCA Bench | ✓ | ✓ | — | — | — | — | — | ✓ |

## Resource Details

<a id="who-and-when"></a>

### Who&When

面向失败归因：给定完整失败日志，预测责任智能体、决定性错误步骤，并给出自然语言原因。它把“谁出了错”和“何时引入关键错误”变成可评测目标。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2505.00212) | [项目](https://github.com/ag2ai/Agents_Failure_Attribution) | [数据](https://huggingface.co/datasets/Kevin355/Who_and_When) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 184 个失败任务 |
| 标签 | 人工标注责任智能体、决定性错误步骤和解释；原论文以最早决定性错误作为主要归因目标。 |
| 系统/环境（综述） | 127 multi-agent LLM systems |
| 综述名称 / #Fail. / #Types | Who&When / 184 / 未提供 |
| Single RC / Scalability（综述） | True / Partial |
| 访问状态 | 官方HF数据页及样本预览可访问；本仓库没有批量下载或逐文件验证。 |
| 许可 | 未确认：HF公开数据卡未见明确数据许可证；代码仓库标示MIT，不能据此自动推定数据许可证。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

184是带标注的失败任务；127是系统配置数量，两者不能互换。

综述标为Partial；可生成多样系统轨迹，但精细因果标注仍需人工。此处是构建/标注可扩展性的阅读解释，非性能测试结论。

来源：[1](https://arxiv.org/abs/2505.00212) · [2](https://github.com/ag2ai/Agents_Failure_Attribution) · [3](https://huggingface.co/datasets/Kevin355/Who_and_When)。核验日期：2026-09-09。

</details>

<a id="mast-data"></a>

### MAST-Data

以多智能体执行轨迹研究失败模式，提供MAST分类体系以及LLM评审标注流程。原始分类包含系统设计、智能体间失配、任务验证三组，共14种模式。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2503.13657) | [项目](https://github.com/multi-agent-systems-failure-taxonomy/MAST) | [数据](https://huggingface.co/datasets/mcemri/MAST-Data) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 1,642 条执行轨迹 |
| 标签 | 主数据是LLM judge对14种模式的二元多标签，缺失项可为null；人工标注用于分类构建和一致性研究。 |
| 系统/环境（综述） | ChatDev, MetaGPT, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus |
| 综述名称 / #Fail. / #Types | MASFT / 1642 / 14 |
| Single RC / Scalability（综述） | True / Yes |
| 访问状态 | 官方HF数据卡、文件说明与样本预览可访问；未批量下载。 |
| 许可 | HF数据卡标示CC BY 4.0；未逐项审查第三方上游任务材料的权利。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

1642是主数据中的执行轨迹数，不是1642个独立根因或全部必然失败的任务。HF展示1661行包含另一个19行人工一致性子集；不能按1661个独立主基准样本理解。

综述标为Yes；论文提供LLM-as-a-Judge标注流程，但标签可靠性、跨系统泛化与人工校准仍需单独评估。

- 综述条目名MASFT对应原论文MAST分类体系及MAST-Data数据。
- 综述Single RC=✓不能理解为每条轨迹只有一个模式标签：原数据明确是多标签。
- 原论文附录J讨论成功与失败执行中都可能出现失败模式。

来源：[1](https://arxiv.org/html/2503.13657v3) · [2](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · [3](https://huggingface.co/datasets/mcemri/MAST-Data)。核验日期：2026-09-09。

</details>

<a id="trail"></a>

### TRAIL

用人工标注的真实智能体轨迹评估复杂trace调试能力。标签可落在span上，并带错误类别、证据、解释与影响程度，强调推理、执行及规划问题。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2505.08638) | [项目](https://github.com/patronus-ai/trail-benchmark) | [数据](https://huggingface.co/datasets/PatronusAI/TRAIL) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 148 条轨迹 / 841 个错误 |
| 标签 | 专家标注span ID、错误类型、证据、描述及Low/Medium/High影响程度；一个span可包含错误，一个trace可包含多个错误。 |
| 系统/环境（综述） | – |
| 综述名称 / #Fail. / #Types | TRAIL / 841 / 21 |
| Single RC / Scalability（综述） | True / No |
| 访问状态 | 数据卡公开，但文件门控要求登录、同意分享联系信息与访问条件。未接受条件、未下载数据。 |
| 许可 | 数据卡标示MIT，同时附门控、不得在公开无门控仓库转发，以及只用于评估相关系统等限制；使用前需读取完整条件，不应仅依据MIT标签判断可重分发。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

综述841是错误实例数：它们分布于148条轨迹，而非841条失败轨迹。148条包括118条GAIA与30条SWE-bench任务轨迹。

综述标为No；长上下文的逐span人工判断成本较高。No并非无法新增样本，也不代表产品不支持大规模trace处理。

- 综述Single RC=✓不是每trace只有一个错误的证明；TRAIL原始任务标注多个错误span。
- 综述Systems栏为“–”；官方卡实际说明OpenDeepResearch/CodeAct、GAIA/SWE-bench Lite来源。

来源：[1](https://arxiv.org/abs/2505.08638) · [2](https://huggingface.co/datasets/PatronusAI/TRAIL)。核验日期：2026-09-09。

</details>

<a id="agentfail"></a>

### AgentFail

聚焦Dify与Coze等低代码平台编排的工作流，记录真实任务失败。最新版研究连接失败表现、根因与修复策略，适合分析节点行为和流程结构共同引起的问题。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2509.23735) | [项目](https://github.com/Jenna-Ma/JaWs-AgentFail) | [数据](https://github.com/Jenna-Ma/JaWs-AgentFail) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 307 条失败轨迹 |
| 标签 | 多轮专家标注，包含查询、工作流配置、执行失败日志，以及失败位置、根因和修复策略。 |
| 系统/环境（综述） | Dify, Coze |
| 综述名称 / #Fail. / #Types | AgentFail / 307 / 16 |
| Single RC / Scalability（综述） | True / Partial |
| 访问状态 | 官方仓库可访问且有coze、dify等目录，但README仍写dataset coming soon。完整307例发布状态、文件完整性和独立下载包未确认。 |
| 许可 | 未确认：检查的仓库页未见明确许可证。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

307是从1387个测试案例中得到的失败轨迹；1387不是失败数据集大小。

综述标为Partial；工作流和任务可以扩展，完整生命周期标签仍依赖平台环境与专家判断。

- 综述引用旧标题Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems: Dataset, Taxonomy, and Benchmark；arXiv v2标题为Demystifying the Lifecycle of Failures in Platform-Orchestrated Agentic Workflows。
- 仓库出现n8n目录不代表可将它加进综述Table VIII的Dify/Coze快照。

来源：[1](https://arxiv.org/html/2509.23735v2) · [2](https://github.com/Jenna-Ma/JaWs-AgentFail)。核验日期：2026-09-09。

</details>

<a id="aegis"></a>

### AEGIS

从原本成功的多智能体轨迹中注入可控错误，生成带标签的失败数据。框架以MAST的14类模式为基础，通过上下文相关的操纵生成用于训练和评测的案例。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2509.14295) | [项目](https://github.com/kfq20/AEGIS) | [数据](https://huggingface.co/datasets/Fancylalala/AEGIS) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 9,533 条轨迹 / 24,843 个错误 |
| 标签 | 以注入位置、目标智能体与错误模式建立可追溯标签；数据样本的faulty_agents是列表。 |
| 系统/环境（综述） | LLM Debate, MacNet, AgentVerse, Dylan, SmolAgents, Magentic-One |
| 综述名称 / #Fail. / #Types | Aegis / 24843 / 14 |
| Single RC / Scalability（综述） | True / Yes |
| 访问状态 | 官方项目、HF数据卡和样本预览可访问；未批量下载或重跑生成流程。 |
| 许可 | HF数据卡标示MIT；代码仓库也标示MIT。未逐项审查上游任务材料。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

官网明确9533条轨迹、24843个错误实例。综述#Fail.=24843，不能作为轨迹或HF数据行数。

综述标为Yes；自动错误生成有利于扩充，但生成错误的真实性与对自然失败的迁移需要另做验证。

- 综述Single RC=✓不能推导为一个样本只有一个faulty agent：官方数据预览存在多个faulty_agents。
- 项目当前标题使用Attribution，综述书目与早期arXiv标题使用Identification；仍为同一arXiv编号。

来源：[1](https://arxiv.org/abs/2509.14295) · [2](https://kfq20.github.io/AEGIS-Website/) · [3](https://github.com/kfq20/AEGIS) · [4](https://huggingface.co/datasets/Fancylalala/AEGIS)。核验日期：2026-09-09。

</details>

<a id="agenterrorbench"></a>

### AgentErrorBench

针对记忆、反思、规划、动作和系统模块收集失败轨迹，支撑根因诊断及纠错反馈。AgentErrorBench是数据集；同篇论文的AgentDebug是诊断和恢复方法。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2509.25370) | [项目](https://github.com/ulab-uiuc/AgentDebug) | [数据](https://drive.google.com/drive/folders/1bQe6dQA85pktT63YnKIKJDTVaH3O3Vpu?usp=drive_link) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 200 条轨迹 |
| 标签 | 按AgentErrorTaxonomy分析失败；具体数据字段和标签完整性未逐文件检查。 |
| 系统/环境（综述） | ALFWorld, WebShop, GAIA |
| 综述名称 / #Fail. / #Types | Agent-Debug / 200 / 17 |
| Single RC / Scalability（综述） | True / No |
| 访问状态 | 官方仓库提供Google Drive下载入口；页面能打开但本次文本工具未取得文件列表，实际下载和文件完整性未核验。 |
| 许可 | 代码项目标示MIT；Drive数据是否适用同一许可证未单独确认。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

官方仓库给出的ALFWorld 100、GAIA 50、WebShop 50合计200条轨迹。

综述标为No；现有发布是经系统标注的有限轨迹集，不等价于对应环境不能生成更多任务。

- 综述Table VIII的Agent-Debug和Table IX的AgentDebug均指向这篇论文；原论文把AgentDebug称为方法，数据集正式名称是AgentErrorBench。
- 综述Systems栏ALFWorld、WebShop、GAIA是任务环境/基准名，不应统一理解为agent框架。

来源：[1](https://arxiv.org/abs/2509.25370) · [2](https://github.com/ulab-uiuc/AgentDebug)。核验日期：2026-09-09。

</details>

<a id="mp-bench"></a>

### MP-Bench

把失败归因视为可能存在多个合理解释的任务。多个专家独立标记诱发失败的步骤、原因和理想动作，按共识强度形成排序，同时评价归因解释。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2603.25001) | [项目](https://github.com/yeonjun-in/MP-Bench) | [数据](https://github.com/adobe-research/multi-agent-eval-bench/tree/main/MP-Bench) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 289 条日志（论文口径） |
| 标签 | 三位专家独立逐步标注；依据标注共识形成ranking，并保留原因与理想动作。 |
| 系统/环境（综述） | MAgentic-One, CaptainAgent |
| 综述名称 / #Fail. / #Types | MP-Bench / 289 / 未提供 |
| Single RC / Scalability（综述） | False / No |
| 访问状态 | 论文链接到作者代码仓库；该仓库再链接Adobe Research的MP-Bench目录作为原始数据入口。未下载重建或验证所有log_source可解析。 |
| 许可 | 数据目录及作者代码页的许可证未确认；不能自动沿用别的Adobe项目的许可。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

论文为169条手工系统执行+120条自动系统执行=289条；三个专家的标注不能重复算作三份独立轨迹。

综述标为No；原论文强调三专家高质量标注的成本。多视角是评测设定，不等于已验证多个独立因果根源同时存在。

- 当前作者仓库README写manual=169、automatic=126，合计295，与论文289不一致。尚未确定是脚本预期、版本差异或文档错误；本仓库以论文289作快照并保留冲突。

来源：[1](https://arxiv.org/html/2603.25001v1) · [2](https://github.com/yeonjun-in/MP-Bench) · [3](https://github.com/adobe-research/multi-agent-eval-bench/tree/main/MP-Bench)。核验日期：2026-09-09。

</details>

<a id="longrca-bench"></a>

### LongRCA Bench

关注长流程失败，分别标注责任角色和最早决定性根因步骤。数据来自五类任务中的自然失败，强调根因可能出现在最终失败之前很久，责任角色也不能简单等同于错误步骤的发言者。

| Paper | Project | Data |
| --- | --- | --- |
| [论文](https://arxiv.org/abs/2608.15242) | [项目](https://longrca-bench.github.io/) | [数据](https://huggingface.co/datasets/CLoud5-real/longrca-bench) |

| 字段 | 内容 |
| --- | --- |
| 规模 | 1,140 条轨迹 |
| 标签 | 人工独立标注责任角色与最早决定性步骤，另有解释；两项分别计分。 |
| 系统/环境（综述） | AutoGen-based and custom multi-agents |
| 综述名称 / #Fail. / #Types | LongRCA Bench / 1140 / 未提供 |
| Single RC / Scalability（综述） | True / No |
| 访问状态 | 官方项目页与HF数据卡/预览可访问，提供JSON和Parquet说明；未批量下载或运行评测。 |
| 许可 | 未确认：检查的HF数据卡未见明确数据许可证。论文的arXiv许可不能替代数据许可。 |

<details>
<summary>统计口径、版本差异与核验来源</summary>

全量1140条；LongRCA-Mini的200条是从全量抽取的子集。HF显示1340行不能理解成1340条不同轨迹。

综述标为No；长历史的人工因果审阅困难。现有1,140条不是该任务领域可扩展性的上限。

- 上游任务为SWE-bench Pro、Terminal-Bench 2、TravelPlanner、VitaBench与WebArena Verified；综述Systems概括为AutoGen-based and custom multi-agents。
- 同篇论文的RCTA是诊断方法，不能单列为新数据集。

来源：[1](https://arxiv.org/html/2608.15242v3) · [2](https://longrca-bench.github.io/) · [3](https://huggingface.co/datasets/CLoud5-real/longrca-bench)。核验日期：2026-09-09。

</details>

## Upstream Task Benchmarks

用于生成agent运行轨迹的任务环境，**不计入上述8项归因基准**。

| 基准 | 用途 | 论文 | 项目 / 数据 |
| --- | --- | --- | --- |
| GAIA | 通用助手推理、检索与工具任务 | [Paper](https://arxiv.org/abs/2311.12983) | [Data](https://huggingface.co/datasets/gaia-benchmark/GAIA) |
| ALFWorld | 文本与具身交互任务 | [Paper](https://arxiv.org/abs/2010.03768) | [Project](https://github.com/alfworld/alfworld) |
| WebShop | 满足用户约束的网页购物交互 | [Paper](https://arxiv.org/abs/2207.01206) | [Project](https://github.com/princeton-nlp/WebShop) |

## Other Benchmarks Mentioned in the Survey

这些出现在异常与方法章节中，不与Table VIII数据集混计；这里只记录已核实的论文入口，不推定数据已公开。

| 资源 | 关注问题 | 论文 |
| --- | --- | --- |
| QE-RAG | QE-RAG 针对查询输入错误设计 RAG 鲁棒性评测，展示检索链路入口错误如何影响后续生成。 | [Paper](https://arxiv.org/abs/2504.04062) |
| RAG Benchmark | RGB 从多个能力维度评测 RAG 中的语言模型，提供分析检索、冲突信息和生成可靠性的基准背景。 | [Paper](https://arxiv.org/abs/2309.01431) |
| ASB | Agent Security Bench 系统化评测智能体攻击与防御，为安全异常提供威胁模型与实验场景。 | [Paper](https://arxiv.org/abs/2410.02644) |
| CLAMBER | CLAMBER 评测语言模型识别模糊信息需求并提出澄清问题的能力，是任务规范异常的相关基准。 | [Paper](https://arxiv.org/abs/2405.12063) |
| API-bank | API-Bank 提供工具增强对话与 API 调用基准，并探索训练提升工具使用能力；原文表 V 标为缓解而非检测。 | [Paper](https://arxiv.org/abs/2304.08244) |
| SpecOps | SpecOps 从任务规格出发自动测试真实 GUI 环境中的智能体，补充以 trace 离线归因为主的评测方式。 | [Paper](https://arxiv.org/abs/2603.10268) |

原始 `#Fail.` 的单位不统一，不可直接求和。`Single RC`是综述的归因设定判断，不等于每条轨迹只有一个错误标签。所有原值和更详细访问说明保留于 [datasets.json](../data/datasets.json)。
