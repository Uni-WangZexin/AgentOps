# AgentOps — Papers, Datasets & Algorithms

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

<a id="reasoning"></a>

### 推理异常 · Reasoning

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS2.SSS1) · [相关类别交叉索引](papers/README.md#reasoning)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / arXiv | **DeepSeek-R1** — [Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning](https://arxiv.org/abs/2501.12948) | DeepSeek-R1 以强化学习提升推理能力，是综述讨论智能体推理能力及其异常的背景模型。 | [1](docs/references.md#ref-1) |
| 2025 / ACM CSUR | [Hallucination detection in foundation models for decision-making: a flexible definition and review of the state of the art](https://arxiv.org/abs/2403.16527) | 该综述从决策任务出发讨论基础模型幻觉的定义与检测，支撑推理异常的概念边界。 | [9](docs/references.md#ref-9) |
| 2024 / PLOS digital health | [Peer review of gpt-4 technical report and systems card](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000417) | 针对 GPT-4 技术报告与系统卡进行学术评议，涉及模型报告与可靠性证据的充分性。 | [18](docs/references.md#ref-18) |
| 2024 / NeurIPS | **Honesty** — [Alignment for honesty](https://arxiv.org/abs/2312.07000) | Alignment for Honesty 研究模型如何承认知识边界，通过评测与训练降低超出知识范围时的无依据回答。 | [19](docs/references.md#ref-19) |
| 2024 / CVPR | **OPERA** — [Opera: alleviating hallucination in multi-modal large language models via over-trust penalty and retrospection-allocation](https://arxiv.org/abs/2311.17911) | OPERA 从注意力中的过度信任现象出发施加惩罚与回溯重分配，缓解多模态模型的幻觉输出。 | [72](docs/references.md#ref-72) |
| 2024 / ICLR | **LURE** — [Analyzing and mitigating object hallucination in large vision-language models](https://arxiv.org/abs/2310.00754) | LURE 分析视觉语言模型的对象幻觉并训练修订器，针对输出进行检测和纠正。 | [76](docs/references.md#ref-76) |
| 2024 / ICLR | **Conformal** — [Conformal language modeling](https://arxiv.org/abs/2306.10193) | Conformal Language Modeling 通过校准与停止规则选择生成集合，研究受统计约束的生成质量控制。 | [77](docs/references.md#ref-77) |
| 2024 / ICLR | **CoK** — [Chain-of-knowledge: grounding large language models via dynamic knowledge adapting over heterogeneous sources](https://arxiv.org/abs/2305.13269) | Chain-of-Knowledge 在推理过程中整合异构外部知识并调整推理链，用外部证据改善回答依据。 | [79](docs/references.md#ref-79) |
| 2023 / arXiv | [A survey of hallucination in large foundation models](https://arxiv.org/abs/2309.05922) | 系统讨论大型基础模型的幻觉现象、成因与处理方法，为推理异常提供已有研究背景。 | [17](docs/references.md#ref-17) |
| 2023 / Findings EMNLP | **SAPLMA** — [The internal state of an llm knows when it’s lying](https://arxiv.org/abs/2304.13734) | SAPLMA 利用模型内部状态训练真假判断分类器，代表能够读取内部信息的幻觉检测路线。 | [73](docs/references.md#ref-73) |
| 2023 / ICML | **Debate** — [Improving factuality and reasoning in language models through multiagent debate](https://arxiv.org/abs/2305.14325) | Multiagent Debate 让多个模型实例反复评议答案，以交叉检查改善事实性与推理；不应把投票一致当作真实正确。 | [78](docs/references.md#ref-78) |
| 2023 / EMNLP | **SelfCheckGPT** — [Selfcheckgpt: zero-resource black-box hallucination detection for generative large language models](https://arxiv.org/abs/2303.08896) | SelfCheckGPT 比较多次采样回答的一致性以检测可能的幻觉；一致性信号对任务歧义的使用是综述层面的延伸讨论。 | [90](docs/references.md#ref-90) |
| 2023 / ICLR | **Self-Consistency** — [Self-consistency improves chain of thought reasoning in language models](https://arxiv.org/abs/2203.11171) | Self-Consistency 通过采样多条推理路径并汇总答案改善推理可靠性，是冗余执行与结果选择的例子。 | [110](docs/references.md#ref-110) |
| 2022 / ICLR | [Finetuned language models are zero-shot learners](https://arxiv.org/abs/2109.01652) | FLAN 研究指令微调带来的零样本迁移能力，作为智能体推理基础能力的背景。 | [15](docs/references.md#ref-15) |
| 2022 / NeurIPS | **CoT** — [Chain-of-thought prompting elicits reasoning in large language models](https://arxiv.org/abs/2201.11903) | Chain-of-Thought 通过显式中间推理步骤改善复杂任务表现；与原文 [104] 是同一论文的重复书目条目。 | [16](docs/references.md#ref-16) · [104](docs/references.md#ref-104) |

<a id="action"></a>

### 动作异常 · Action

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS2.SSS2) · [相关类别交叉索引](papers/README.md#action)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / 未标明 | [Function calling in large language models: industrial practices, challenges, and future directions](https://openreview.net/forum?id=LNxVGPedFW) | 从工业实践梳理函数调用的流程、挑战与方向，为行动异常中的调用错误、接口约束等问题提供背景。 | [20](docs/references.md#ref-20) |
| 2025 / COLING | [The dark side of function calling: pathways to jailbreaking large language models](https://aclanthology.org/2025.coling-main.39/) | 研究函数调用能力暴露的越狱路径，说明工具接口也可能成为安全风险入口。 | [21](docs/references.md#ref-21) |
| 2025 / AdNLP | **MCP Guardian** — [MCP guardian: a security-first layer for safeguarding mcp-based ai system](https://arxiv.org/abs/2504.12757) | MCP Guardian 在 MCP 通信中增加鉴权、限流、日志和检查机制，是围绕工具协议的安全防护路线。 | [80](docs/references.md#ref-80) |
| 2024 / ICLR | **ToolLLM** — [ToolLLM: facilitating large language models to master 16000+ real-world apis](https://arxiv.org/abs/2307.16789) | ToolLLM 围绕大规模真实 API 构建指令与调用路径训练资源；综述将其作为多步工具规划的能力增强方法。 | [4](docs/references.md#ref-4) |
| 2024 / ICML | **CodeAct** — [Executable code actions elicit better llm agents](https://arxiv.org/abs/2402.01030) | CodeAct 将行动表示为可执行代码，以编程语言表达复杂工具操作；原文将其列为多步编排的缓解方法。 | [94](docs/references.md#ref-94) |
| 2024 / arXiv | **SWE-agent** — [SWE-agent: agent-computer interfaces enable automated software engineering](https://arxiv.org/abs/2405.15793) | SWE-agent 研究面向编码任务的智能体—计算机接口，说明工具与行动空间设计如何影响执行可靠性。 | [103](docs/references.md#ref-103) |
| 2023 / EMNLP | **API-bank** — [API-bank: a comprehensive benchmark for tool-augmented llms](https://arxiv.org/abs/2304.08244) | API-Bank 提供工具增强对话与 API 调用基准，并探索训练提升工具使用能力；原文表 V 标为缓解而非检测。 | [92](docs/references.md#ref-92) |
| 2023 / NeurIPS | **Toolformer** — [Toolformer: language models can teach themselves to use tools](https://arxiv.org/abs/2302.04761) | Toolformer 研究模型自学工具调用，说明可用工具和调用接口的设计会影响智能体行动质量。 | [106](docs/references.md#ref-106) |

<a id="memory"></a>

### 记忆异常 · Memory

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS2.SSS3) · [相关类别交叉索引](papers/README.md#memory)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / arXiv | **PI-LLM** — [Unable to forget: proactive interference reveals working memory limits in llms beyond context length](https://arxiv.org/abs/2506.08184) | 研究主动干扰对 LLM 工作记忆的影响，说明上下文长度增加不等于记忆能力无限扩展。 | [24](docs/references.md#ref-24) |
| 2025 / arXiv | **QE-RAG** — [QE-rag: a robust retrieval-augmented generation benchmark for query entry errors](https://arxiv.org/abs/2504.04062) | QE-RAG 针对查询输入错误设计 RAG 鲁棒性评测，展示检索链路入口错误如何影响后续生成。 | [25](docs/references.md#ref-25) |
| 2025 / ICLR | **ReDeEP** — [ReDeEP: detecting hallucination in retrieval-augmented generation via mechanistic interpretability](https://arxiv.org/abs/2410.11414) | ReDeEP 区分外部上下文与参数知识的利用以检测 RAG 幻觉；同文的 AARF 承担缓解作用，二者功能应分开理解。 | [27](docs/references.md#ref-27) |
| 2024 / TACL | **Lost in the Middle** — [Lost in the middle: how language models use long contexts](https://arxiv.org/abs/2307.03172) | Lost in the Middle 检验信息位置如何影响长上下文利用能力，是短期记忆异常的重要证据。 | [23](docs/references.md#ref-23) |
| 2024 / arXiv | **Astute RAG** — [Astute rag: overcoming imperfect retrieval augmentation and knowledge conflicts for large language models](https://arxiv.org/abs/2410.07176) | Astute RAG 研究不完美检索和知识冲突下的生成，强调外部检索内容并不天然可靠。 | [26](docs/references.md#ref-26) |
| 2024 / AAAI | **RAG Benchmark** — [Benchmarking large language models in retrieval-augmented generation](https://arxiv.org/abs/2309.01431) | RGB 从多个能力维度评测 RAG 中的语言模型，提供分析检索、冲突信息和生成可靠性的基准背景。 | [28](docs/references.md#ref-28) |
| 2024 / NeurIPS | **CoA** — [Chain of agents: large language models collaborating on long-context tasks](https://arxiv.org/abs/2406.02818) | Chain of Agents 让多个工作智能体分块处理长上下文，再由管理智能体汇总，缓解长文本处理限制。 | [82](docs/references.md#ref-82) |
| 2024 / arXiv | **LRP4RAG** — [LRP4RAG: detecting hallucinations in retrieval-augmented generation via layer-wise relevance propagation](https://arxiv.org/abs/2408.15533) | LRP4RAG 使用逐层相关性传播的信号分类 RAG 幻觉，原文将它列为检测而非直接纠正方法。 | [83](docs/references.md#ref-83) |
| 2023 / arXiv | **PI** — [Extending context window of large language models via positional interpolation](https://arxiv.org/abs/2306.15595) | Positional Interpolation 通过位置插值扩展上下文窗口；原文将其标为缓解方法，并不把它列作异常检测器。 | [81](docs/references.md#ref-81) |
| 2023 / arXiv | **Voyager** — [Voyager: an open-ended embodied agent with large language models](https://arxiv.org/abs/2305.16291) | Voyager 在开放环境中积累可复用技能库，支撑综述关于执行后记忆和技能更新的讨论。 | [112](docs/references.md#ref-112) |

<a id="security"></a>

### 安全异常 · Security

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS2.SSS4) · [相关类别交叉索引](papers/README.md#security)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / ACM CSUR | [Ai agents under threat: a survey of key security challenges and future pathways](https://arxiv.org/abs/2406.02630) | 总结 AI 智能体的安全威胁与研究方向，为综述的安全异常类别提供背景。 | [10](docs/references.md#ref-10) |
| 2025 / ICLR | **ASB** — [Agent security bench (asb): formalizing and benchmarking attacks and defenses in llm-based agents](https://arxiv.org/abs/2410.02644) | Agent Security Bench 系统化评测智能体攻击与防御，为安全异常提供威胁模型与实验场景。 | [30](docs/references.md#ref-30) |
| 2025 / arXiv | **SentinelAgent** — [SentinelAgent: graph-based anomaly detection in multi-agent systems](https://arxiv.org/abs/2505.24201) | SentinelAgent 以交互图表示多智能体系统，在多个粒度识别异常协作模式；异常节点不应自动等同于已证实根因。 | [33](docs/references.md#ref-33) |
| 2025 / arXiv | **GUARDIAN** — [GUARDIAN: safeguarding llm multi-agent collaborations with temporal graph modeling](https://arxiv.org/abs/2505.19234) | GUARDIAN 以时序图刻画多智能体依赖并用重建信号识别异常协作，避免忽视智能体之间的相关性。 | [84](docs/references.md#ref-84) |
| 2025 / arXiv | **AgentSpec** — [Agentspec: customizable runtime enforcement for safe and reliable llm agents](https://arxiv.org/abs/2503.18666) | AgentSpec 用可定制规则约束运行中的智能体行为，在危险或不合规行动执行前进行拦截。 | [108](docs/references.md#ref-108) |
| 2024 / ISoLA | [Emergence in multi-agent systems: a safety perspective](https://arxiv.org/abs/2408.04514) | 从安全角度讨论多智能体涌现行为，强调单体行为正常仍可能形成系统层面的危险结果。 | [32](docs/references.md#ref-32) |
| 2021 / CVPR | [Mlcapsule: guarded offline deployment of machine learning as a service](https://arxiv.org/abs/1808.00590) | MLCapsule 研究受保护的离线模型服务部署，为模型内部信息的可访问性与可观测性约束提供背景。 | [71](docs/references.md#ref-71) |

<a id="task-specification"></a>

### 任务规范异常 · Task Specification

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS3.SSS1) · [相关类别交叉索引](papers/README.md#task-specification)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2026 / arXiv | **SpecValidator** — [Defective task descriptions in llm-based code generation: detection and analysis](https://arxiv.org/abs/2604.24703) | SpecValidator 判断代码生成任务描述是否存在缺陷并预测缺陷类型或概率，用于执行前检查输入质量。 | [85](docs/references.md#ref-85) |
| 2026 / ICLR | **Ambig-SWE** — [Ambig-swe: interactive agents to overcome underspecificity in software engineering](https://arxiv.org/abs/2502.13069) | Ambig-SWE 把软件工程指令欠明确问题分为识别、提问和利用答复三个环节，评测交互澄清的价值。 | [86](docs/references.md#ref-86) |
| 2026 / arXiv | **Ask-or-Assume** — [Ask or assume? uncertainty-aware clarification-seeking in coding agents](https://arxiv.org/abs/2603.26233) | Ask or Assume? 利用任务与状态中的不确定性决定何时提问澄清，研究编码智能体的执行与询问权衡。 | [88](docs/references.md#ref-88) |
| 2025 / ICLR Workshop | **MAST workshop** — [Why do multiagent systems fail?](https://openreview.net/forum?id=wM521FqPvI) | 该 ICLR 工作坊论文分析多智能体失效模式与协作缺陷；与 [117] 属相关研究版本，保留原始独立编号。 | [31](docs/references.md#ref-31) |
| 2025 / FSE | **AgentFM** — [Agentfm: role-aware failure management for distributed databases with llm-driven multi-agents](https://arxiv.org/abs/2504.06614) | AgentFM 通过角色感知的多智能体协作管理分布式数据库故障，体现智能体在传统系统运维中的用途。 | [36](docs/references.md#ref-36) |
| 2024 / ACL | **CLAMBER** — [CLAMBER: a benchmark of identifying and clarifying ambiguous information needs in large language models](https://arxiv.org/abs/2405.12063) | CLAMBER 评测语言模型识别模糊信息需求并提出澄清问题的能力，是任务规范异常的相关基准。 | [87](docs/references.md#ref-87) |
| 2023 / arXiv | **Semantic Entropy** — [Semantic uncertainty: linguistic invariances for uncertainty estimation in natural language generation](https://arxiv.org/abs/2302.09664) | Semantic Uncertainty 将语义等价的回答归组估计不确定性；综述借用该信号辅助判断可能的任务歧义。 | [89](docs/references.md#ref-89) |
| 2007 / 学位论文 | [Modeling exception management in multi-agent systems.](https://ir.soken.ac.jp/records/865) | 这篇学位论文研究多智能体异常管理的建模问题，提供早于 LLM 智能体的异常处理背景。 | [34](docs/references.md#ref-34) |

<a id="orchestration"></a>

### 编排异常 · Orchestration

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS3.SSS2) · [相关类别交叉索引](papers/README.md#orchestration)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2024 / Vicinagearth | [A survey on llm-based multi-agent systems: workflow, infrastructure, and challenges](https://doi.org/10.1007/s44336-024-00009-2) | 按工作流、基础设施和挑战梳理 LLM 多智能体系统，为编排问题提供系统背景。 | [37](docs/references.md#ref-37) |
| 2024 / COLM | **AutoGen** — [Autogen: enabling next-gen llm applications via multi-agent conversations](https://arxiv.org/abs/2308.08155) | AutoGen 以多智能体会话构建应用，支持规划、执行与审查等角色协作，是编排与纠错框架的例子。 | [38](docs/references.md#ref-38) |
| 2024 / arXiv | **Introspective** — [Introspective planning: guiding language-enabled agents to refine their own uncertainty](https://arxiv.org/abs/2402.06529) | Introspective Planning 结合不确定性估计、任务歧义和反馈来改进规划，原文将其归入单步编排问题的处理路线。 | [91](docs/references.md#ref-91) |
| 2023 / ICLR | **ReAct** — [ReAct: synergizing reasoning and acting in language models](https://arxiv.org/abs/2210.03629) | ReAct 交替进行推理、行动和环境观察，使智能体能够据反馈调整计划；综述在规划与运行时纠错中引用它。 | [14](docs/references.md#ref-14) |
| 2023 / NeurIPS | **CAMEL** — [Camel: communicative agents for” mind” exploration of large language model society](https://arxiv.org/abs/2303.17760) | CAMEL 用角色设定驱动智能体通信与任务协作，为理解角色对齐和编排机制提供背景。 | [39](docs/references.md#ref-39) |
| 2023 / NeurIPS | **Reflexion** — [Reflexion: language agents with verbal reinforcement learning](https://arxiv.org/abs/2303.11366) | Reflexion 把执行反馈转为语言反思并保留到后续尝试中，在不更新模型参数的情况下改善行为。 | [93](docs/references.md#ref-93) |
| 2023 / NeurIPS | **Tree of Thoughts** — [Tree of thoughts: deliberate problem solving with large language models](https://arxiv.org/abs/2305.10601) | Tree of Thoughts 显式探索与评估多个思路分支，为执行前规划和备选方案检查提供机制。 | [105](docs/references.md#ref-105) |

<a id="communication"></a>

### 通信异常 · Communication

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS3.SSS3) · [相关类别交叉索引](papers/README.md#communication)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / ICLR | **AgentPrune** — [Cut the crap: an economical communication pipeline for llm-based multi-agent systems](https://arxiv.org/abs/2410.02506) | AgentPrune 对消息传递图进行剪枝，降低冗余通信及其成本；综述将其放在通信异常检测与缓解中。 | [41](docs/references.md#ref-41) |
| 2025 / ICML | **G-Designer** — [G-designer: architecting multi-agent communication topologies via graph neural networks](https://arxiv.org/abs/2410.11782) | G-Designer 用图模型生成任务相关的通信拓扑，减少不必要的通信并改善多智能体协作效率。 | [95](docs/references.md#ref-95) |

<a id="termination"></a>

### 终止异常 · Termination

[综述对应章节](https://arxiv.org/html/2606.01581v2#S2.SS3.SSS4) · [相关类别交叉索引](papers/README.md#termination)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / NAACL | **Smurfs** — [Smurfs: multi-agent system using context-efficient dfsdt for tool planning](https://arxiv.org/abs/2405.05955) | Smurfs 用多个智能体和上下文高效的搜索机制分解工具规划任务，为多步协作与编排研究提供例子。 | [43](docs/references.md#ref-43) |
| 2025 / arXiv | **Neural Howlround** — [’Neural howlround’in large language models: a self-reinforcing bias phenomenon, and a dynamic attenuation solution](https://arxiv.org/abs/2504.07992) | Neural howlround 讨论自我强化偏置及动态衰减机制，帮助理解反馈循环可能导致的异常持续行为。 | [45](docs/references.md#ref-45) |
| 2024 / EMNLP Demo | **ReDel** — [ReDel: a toolkit for llm-powered recursive multi-agent systems](https://arxiv.org/abs/2408.02248) | ReDel 支持递归任务委派、事件日志与执行回放，便于检查动态多智能体的组织和终止行为。 | [44](docs/references.md#ref-44) |

<a id="monitoring"></a>

### 监控与可观测性 · Monitoring

[综述对应章节](https://arxiv.org/html/2606.01581v2#S4) · [相关类别交叉索引](papers/README.md#monitoring)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2026 / arXiv | **CHANGE** — [Architecting agentops needs change](https://arxiv.org/abs/2601.06456) | 从软件架构视角讨论 AgentOps 所需能力与变化，补充仅依赖日志追踪的运维视角。 | [52](docs/references.md#ref-52) |
| 2026 / arXiv | **ARC** — [ARC: compiling large multi-modal requirement documents into runnable software systems](https://arxiv.org/abs/2602.13723) | ARC 将大型多模态需求文档转为可运行软件；综述还以其 Git 历史说明检查点和回滚的工程实现背景。 | [74](docs/references.md#ref-74) |
| 2026 / PACMSE | **WebTestPilot** — [Webtestpilot: agentic end-to-end web testing against natural language specification by inferring oracles with symbolized gui elements](https://arxiv.org/abs/2602.11724) | WebTestPilot 从自然语言规格与符号化 GUI 元素推导测试判断依据，展示对网页智能体结果进行系统检查的思路。 | [75](docs/references.md#ref-75) |
| 2025 / arXiv | **AgentOps Automation** — [Taming uncertainty via automation: observing, analyzing, and optimizing agentic ai systems](https://arxiv.org/abs/2507.11277) | 围绕观察、分析与优化构建自动化思路，强调处理智能体系统中的不确定性。 | [53](docs/references.md#ref-53) |
| 2024 / arXiv | **AgentOps Observability** — [Agentops: enabling observability of llm agents](https://arxiv.org/abs/2411.05285) | 讨论如何让 LLM 智能体获得可观测性，是以监控为核心的早期 AgentOps 工作。 | [51](docs/references.md#ref-51) |

<a id="root-cause"></a>

### 根因定位与失败归因 · Root Cause Localization

[综述对应章节](https://arxiv.org/html/2606.01581v2#S6) · [相关类别交叉索引](papers/README.md#root-cause)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2026 / arXiv | [Trajaudit: automated failure diagnosis for agentic coding systems](https://arxiv.org/abs/2605.26563) | TrajAudit 研究编码智能体执行轨迹的自动失败诊断，补充综述对真实工程智能体故障分析的讨论。 | [7](docs/references.md#ref-7) |
| 2026 / arXiv | **StepFinder** — [StepFinder: a temporal semantic framework for failure attribution in multi-agent systems](https://arxiv.org/abs/2606.03467) | StepFinder 先用语言模型构造语义特征，再以时序模型捕捉跨步骤依赖，实现步骤级归因。 | [101](docs/references.md#ref-101) |
| 2025 / ICML | **Who&When** — [Which agent causes task failures and when? on automated failure attribution of LLM multi-agent systems](https://arxiv.org/abs/2505.00212) | Who&When 将失败归因拆为责任智能体和关键错误步骤，并比较整段判断、逐步判断与二分查找三种策略。 | [12](docs/references.md#ref-12) · [Project](https://github.com/ag2ai/Agents_Failure_Attribution) · [Data](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| 2025 / arXiv | **FAMAS** — [Who is introducing the failure? automatically attributing failures of multi-agent systems via spectrum analysis](https://arxiv.org/abs/2509.13782) | FAMAS 将轨迹抽象为状态、行动和智能体元组，通过成功/失败差异及可疑度评分定位责任行为。 | [96](docs/references.md#ref-96) |
| 2025 / arXiv | **GraphTracer** — [GraphTracer: graph-guided failure tracing in llm agents for robust multi-turn deep search](https://arxiv.org/abs/2510.10581) | GraphTracer 通过信息依赖图追踪上游错误如何传播，适用于多轮深度搜索智能体的失败分析。 | [97](docs/references.md#ref-97) |
| 2025 / arXiv | **AgenTracer** — [AgenTracer: who is inducing failure in the llm agentic systems?](https://arxiv.org/abs/2509.03312) | AgenTracer 利用反事实回放与故障注入构建训练轨迹，训练模型识别责任智能体与关键错误步骤。 | [98](docs/references.md#ref-98) |
| 2025 / arXiv | **AgentFail** — [Diagnosing failure root causes in platform-orchestrated agentic systems: dataset, taxonomy, and benchmark](https://arxiv.org/abs/2509.23735) | AgentFail 结合平台智能体失败数据、细粒度分类和诊断基准，研究复杂轨迹中的根因识别。 | [99](docs/references.md#ref-99) · [Project](https://github.com/Jenna-Ma/JaWs-AgentFail) · [Data](https://github.com/Jenna-Ma/JaWs-AgentFail) |
| 2025 / arXiv | [Automatic failure attribution and critical step prediction method for multi-agent systems based on causal inference](https://arxiv.org/abs/2509.08682) | 基于因果图与反事实推理，将多智能体系统失败关联到责任智能体和关键行动步骤。 | [100](docs/references.md#ref-100) |
| 2025 / arXiv | **AgentDebug** — [Where llm agents fail and how they can learn from failures](https://arxiv.org/abs/2509.25370) | 该工作提出 AgentErrorTaxonomy、AgentErrorBench 和 AgentDebug，把分类、错误轨迹评测与纠错反馈连接起来。 | [102](docs/references.md#ref-102) · [Project](https://github.com/ulab-uiuc/AgentDebug) · [Data](https://drive.google.com/drive/folders/1bQe6dQA85pktT63YnKIKJDTVaH3O3Vpu?usp=drive_link) |

<a id="resolution"></a>

### 纠错与恢复 · Resolution

[综述对应章节](https://arxiv.org/html/2606.01581v2#S7) · [相关类别交叉索引](papers/README.md#resolution)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2026 / 未标明 | **Comfrey** — [Comfrey: mitigating integration failures in llm-enabled software at run-time](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/319/Comfrey-Mitigating-Integration-Failures-in-LLM-enabled-Software-at-Run-Time) | Comfrey 在 LLM 与确定性软件组件之间检查和修复接口不兼容，针对格式、语法等集成失败进行运行时处理。 | [109](docs/references.md#ref-109) |
| 2024 / ICLR | **DePT** — [Dept: decomposed prompt tuning for parameter-efficient fine-tuning](https://arxiv.org/abs/2309.05173) | DePT 将提示调优分解以提高参数效率，属于执行后更新提示或策略的相关优化技术。 | [115](docs/references.md#ref-115) |
| 2024 / ICML | **Promptbreeder** — [Promptbreeder: self-referential self-improvement via prompt evolution](https://arxiv.org/abs/2309.16797) | Promptbreeder 以演化方式联合优化提示及其变异过程，展示从任务反馈持续改进指令的路线。 | [116](docs/references.md#ref-116) |
| 2023 / NeurIPS | **Self-Refine** — [Self-refine: iterative refinement with self-feedback](https://arxiv.org/abs/2303.17651) | Self-Refine 让同一语言模型生成反馈并迭代修订输出，是运行时自我纠错的代表方法。 | [107](docs/references.md#ref-107) |
| 2022 / ACL | **P-Tuning v2** — [P-tuning: prompt tuning can be comparable to fine-tuning universally across scales and tasks](https://arxiv.org/abs/2110.07602) | P-Tuning v2 研究可训练连续提示在不同规模与任务上的适用性，为持久化提示调整提供背景。 | [114](docs/references.md#ref-114) |
| 2020 / EMNLP | **AutoPrompt** — [Autoprompt: eliciting knowledge from language models with automatically generated prompts](https://arxiv.org/abs/2010.15980) | AutoPrompt 自动寻找离散提示以激发模型知识，作为长期提示修订与自动优化的相关方法。 | [113](docs/references.md#ref-113) |

<a id="benchmarks"></a>

### 数据与评测 · Datasets & Benchmarks

[综述对应章节](https://arxiv.org/html/2606.01581v2#S8) · [相关类别交叉索引](papers/README.md#benchmarks)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2026 / ICLR | [Holistic agent leaderboard: the missing infrastructure for ai agent evaluation](https://arxiv.org/abs/2510.11977) | HAL 讨论统一、可复现的智能体评测基础设施，帮助理解为什么孤立的任务分数不足以支撑运维评估。 | [13](docs/references.md#ref-13) |
| 2026 / arXiv | **MP-Bench** — [Rethinking failure attribution in multi-agent systems: a multi-perspective benchmark and evaluation](https://arxiv.org/abs/2603.25001) | 该多视角基准重新审视失败归因的标注与评价方式，提醒读者归因答案可能依赖观察视角。 | [120](docs/references.md#ref-120) · [Project](https://github.com/yeonjun-in/MP-Bench) · [Data](https://github.com/adobe-research/multi-agent-eval-bench/tree/main/MP-Bench) |
| 2026 / 未标明 | **LongRCA Bench** — [LongRCA bench: diagnosing responsible roles and root causes in long-horizon agent failures](https://arxiv.org/abs/2608.15242) | LongRCA Bench 面向长程智能体失败，同时考察责任角色与根因诊断，补充长轨迹带来的归因挑战。 | [121](docs/references.md#ref-121) · [Project](https://longrca-bench.github.io/) · [Data](https://huggingface.co/datasets/CLoud5-real/longrca-bench) |
| 2026 / arXiv | **SpecOps** — [Specops: a fully automated ai agent testing framework in real-world gui environments](https://arxiv.org/abs/2603.10268) | SpecOps 从任务规格出发自动测试真实 GUI 环境中的智能体，补充以 trace 离线归因为主的评测方式。 | [125](docs/references.md#ref-125) |
| 2025 / arXiv | **MAST** — [Why do multi-agent llm systems fail?](https://arxiv.org/abs/2503.13657) | MAST 对真实多智能体轨迹建立失效分类与标注资源；应使用对应版本的类别数和数据统计。 | [117](docs/references.md#ref-117) · [Project](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · [Data](https://huggingface.co/datasets/mcemri/MAST-Data) |
| 2025 / arXiv | **TRAIL** — [TRAIL: trace reasoning and agentic issue localization](https://arxiv.org/abs/2505.08638) | TRAIL 将执行 trace 的推理与问题定位组织为评测任务，关注复杂工具交互中错误的识别和解释。 | [118](docs/references.md#ref-118) · [Project](https://github.com/patronus-ai/trail-benchmark) · [Data](https://huggingface.co/datasets/PatronusAI/TRAIL) |
| 2025 / arXiv | **AEGIS** — [AEGIS: automated error generation and identification for multi-agent systems](https://arxiv.org/abs/2509.14295) | AEGIS 从成功轨迹注入可追踪错误，构建具有明确错误标签的数据以训练和评测多智能体失败归因。 | [119](docs/references.md#ref-119) · [Project](https://github.com/kfq20/AEGIS) · [Data](https://huggingface.co/datasets/Fancylalala/AEGIS) |
| 2023 / ICLR | **GAIA** — [Gaia: a benchmark for general ai assistants](https://arxiv.org/abs/2311.12983) | GAIA 评测通用助手完成现实问题的能力；它是任务环境/基准，不自动提供专门的失败根因标签。 | [122](docs/references.md#ref-122) · [Project](https://huggingface.co/datasets/gaia-benchmark/GAIA) |
| 2022 / NeurIPS | **WebShop** — [Webshop: towards scalable real-world web interaction with grounded language agents](https://arxiv.org/abs/2207.01206) | WebShop 提供基于网页购物的交互任务，可作为工具使用、规划和错误轨迹采集的环境。 | [124](docs/references.md#ref-124) · [Project](https://github.com/princeton-nlp/WebShop) |
| 2020 / arXiv | **ALFWorld** — [Alfworld: aligning text and embodied environments for interactive learning](https://arxiv.org/abs/2010.03768) | ALFWorld 将文本与具身家庭任务对齐，常用于生成和分析多步智能体执行轨迹。 | [123](docs/references.md#ref-123) · [Project](https://github.com/alfworld/alfworld) |

<a id="background"></a>

### 背景与应用 · Background

[综述对应章节](https://arxiv.org/html/2606.01581v2#S1) · [相关类别交叉索引](papers/README.md#background)

| 年份 / 来源¹ | 论文 | 简介 / 在该领域的用途 | 资源 |
| --- | --- | --- | --- |
| 2025 / WWW Companion | [Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis](https://arxiv.org/abs/2502.08224) | Flow-of-Action 用标准操作流程约束多智能体诊断过程；诊断对象是微服务故障，是“用智能体运维系统”的应用例子。 | [5](docs/references.md#ref-5) |
| 2025 / ACM TOIS | [Recommender ai agent: integrating large language models for interactive recommendations](https://arxiv.org/abs/2308.16505) | InteRecAgent 结合语言模型与推荐工具，借助记忆、规划和反思实现交互式推荐。 | [6](docs/references.md#ref-6) |
| 2025 / arXiv | [Towards trustworthy gui agents: a survey](https://arxiv.org/abs/2503.23434) | 梳理 GUI 智能体的可信性问题，是界面操作场景下可靠性与安全研究的参考。 | [11](docs/references.md#ref-11) |
| 2025 / Information | [Transitioning from mlops to llmops: navigating the unique challenges of large language models](https://www.mdpi.com/2078-2489/16/2/87) | 讨论从 MLOps 到 LLMOps 的变化，为解释语言模型应用在部署、监测与维护上的特殊要求提供背景。 | [48](docs/references.md#ref-48) |
| 2024 / 未标明 | [Econagent: large language model-empowered agents for simulating macroeconomic activities](https://arxiv.org/abs/2310.10436) | EconAgent 用具有感知、记忆与决策能力的语言模型智能体模拟宏观经济活动，展示多智能体的应用范围。 | [3](docs/references.md#ref-3) |
| 2024 / arXiv | [Agent ai: surveying the horizons of multimodal interaction](https://arxiv.org/abs/2401.03568) | Agent AI 综述多模态交互智能体的发展，用于说明已有综述覆盖能力与交互，却未完全覆盖系统运维链路。 | [8](docs/references.md#ref-8) |
| 2023 / arXiv | [Ai for it operations (aiops) on cloud platforms: reviews, opportunities and challenges](https://arxiv.org/abs/2304.04661) | 梳理云平台 AIOps 的研究、机会与挑战，是传统运维对象和智能体运维对象之间的比较背景。 | [47](docs/references.md#ref-47) |
| 2015 / International conference on agile software development | [DevOps: a definition and perceived adoption impediments](https://link.springer.com/chapter/10.1007/978-3-319-18612-2_14) | 通过定义与采用障碍讨论 DevOps，为综述比较 DevOps、AIOps、LLMOps 与 AgentOps 提供参照。 | [46](docs/references.md#ref-46) |

<a id="datasets"></a>

## Datasets & Benchmarks

以 **Paper / Project / Data** 区分论文、项目和数据入口。下表统一标明计数单位；原文 `#Fail.`、标签覆盖和访问条件见[数据集目录](datasets/README.md)。

| 数据集 | 任务 / 标签 | 规模与单位 | 入口 |
| --- | --- | --- | --- |
| [Who&When](datasets/README.md#who-and-when) | 责任智能体与决定性步骤定位；适合复现较早的归因基线。 | 184 个失败任务 | [Paper](https://arxiv.org/abs/2505.00212) · [Project](https://github.com/ag2ai/Agents_Failure_Attribution) · [Data](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| [MAST-Data](datasets/README.md#mast-data) | 失败模式多标签分类、系统设计比较、自动标注研究。 | 1,642 条执行轨迹 | [Paper](https://arxiv.org/abs/2503.13657) · [Project](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · [Data](https://huggingface.co/datasets/mcemri/MAST-Data) |
| [TRAIL](datasets/README.md#trail) | 从长trace识别错误span、分类错误并解释影响。 | 148 条轨迹 / 841 个错误 | [Paper](https://arxiv.org/abs/2505.08638) · [Project](https://github.com/patronus-ai/trail-benchmark) · [Data](https://huggingface.co/datasets/PatronusAI/TRAIL) |
| [AgentFail](datasets/README.md#agentfail) | 平台工作流的故障定位、根因分类与修复研究。 | 307 条失败轨迹 | [Paper](https://arxiv.org/abs/2509.23735) · [Project](https://github.com/Jenna-Ma/JaWs-AgentFail) · [Data](https://github.com/Jenna-Ma/JaWs-AgentFail) |
| [AEGIS](datasets/README.md#aegis) | 可控错误生成、错误智能体/模式识别，以及诊断模型训练。 | 9,533 条轨迹 / 24,843 个错误 | [Paper](https://arxiv.org/abs/2509.14295) · [Project](https://github.com/kfq20/AEGIS) · [Data](https://huggingface.co/datasets/Fancylalala/AEGIS) |
| [AgentErrorBench](datasets/README.md#agenterrorbench) | 单智能体模块化错误分析、根因定位及反馈恢复。 | 200 条轨迹 | [Paper](https://arxiv.org/abs/2509.25370) · [Project](https://github.com/ulab-uiuc/AgentDebug) · [Data](https://drive.google.com/drive/folders/1bQe6dQA85pktT63YnKIKJDTVaH3O3Vpu?usp=drive_link) |
| [MP-Bench](datasets/README.md#mp-bench) | 多视角归因、步骤排序及解释质量评测。 | 289 条日志（论文口径） | [Paper](https://arxiv.org/abs/2603.25001) · [Project](https://github.com/yeonjun-in/MP-Bench) · [Data](https://github.com/adobe-research/multi-agent-eval-bench/tree/main/MP-Bench) |
| [LongRCA Bench](datasets/README.md#longrca-bench) | 长轨迹根因检索、责任角色预测与精确步骤定位。 | 1,140 条轨迹 | [Paper](https://arxiv.org/abs/2608.15242) · [Project](https://longrca-bench.github.io/) · [Data](https://huggingface.co/datasets/CLoud5-real/longrca-bench) |

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
