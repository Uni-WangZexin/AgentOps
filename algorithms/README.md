# Algorithms & Methods

[首页](../README.md) · [Paper list](../papers/README.md) · [Algorithms](../algorithms/README.md) · [Datasets](../datasets/README.md) · [Tools](../tools/README.md)

按论文的方法分类整理。检测、缓解、根因定位与处置机制分表列出，不将工具、训练方法和数据集混称为检测算法。

**[Detection / Mitigation](#detection) · [Root Cause Localization](#localization) · [Resolution](#resolution)**

<a id="detection"></a>

## Detection & Mitigation

29 项，按[原文 Table V](https://arxiv.org/html/2606.01581v2#S5.T5)。D = 检测；M = 缓解。输入与输出为原文概括，代码复现前仍需检查原论文的实际依赖。

### 推理异常 · Reasoning

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| SAPLMA | White-box | LLM Parameters → Anomaly Probability | ✓ / — | SAPLMA 利用模型内部状态训练真假判断分类器，代表能够读取内部信息的幻觉检测路线。 | [Paper](https://arxiv.org/abs/2304.13734) · [73](../docs/references.md#ref-73) |
| OPERA | White-box | Attention Map → Penalty-regenerated Response | ✓ / ✓ | OPERA 从注意力中的过度信任现象出发施加惩罚与回溯重分配，缓解多模态模型的幻觉输出。 | [Paper](https://arxiv.org/abs/2311.17911) · [72](../docs/references.md#ref-72) |
| Honesty | White-box | LLM Parameters (Finetuning) → Revised Response | ✓ / ✓ | Alignment for Honesty 研究模型如何承认知识边界，通过评测与训练降低超出知识范围时的无依据回答。 | [Paper](https://arxiv.org/abs/2312.07000) · [19](../docs/references.md#ref-19) |
| LURE | Grey-box | Token Logits, Revisor Model → Revised Response | ✓ / ✓ | LURE 分析视觉语言模型的对象幻觉并训练修订器，针对输出进行检测和纠正。 | [Paper](https://arxiv.org/abs/2310.00754) · [76](../docs/references.md#ref-76) |
| Conformal | Grey-box | Token Logits → High-quality Response | ✓ / ✓ | Conformal Language Modeling 通过校准与停止规则选择生成集合，研究受统计约束的生成质量控制。 | [Paper](https://arxiv.org/abs/2306.10193) · [77](../docs/references.md#ref-77) |
| Debate | Black-box | Multiple Agents → Debated Response | ✓ / ✓ | Multiagent Debate 让多个模型实例反复评议答案，以交叉检查改善事实性与推理；不应把投票一致当作真实正确。 | [Paper](https://arxiv.org/abs/2305.14325) · [78](../docs/references.md#ref-78) |
| CoK | Black-box | Multiple Data Sources → High-quality Response | ✓ / ✓ | Chain-of-Knowledge 在推理过程中整合异构外部知识并调整推理链，用外部证据改善回答依据。 | [Paper](https://arxiv.org/abs/2305.13269) · [79](../docs/references.md#ref-79) |

### 动作异常 · Action

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| AI-Infra-Guard | MCP | AI Component → MCP Risks | ✓ / — | 腾讯 AI-Infra-Guard 是安全扫描工具；综述特别引用其 MCP 风险检查能力，不将项目文档当作同行评议论文。 | [Project / Docs](https://github.com/Tencent/AI-Infra-Guard) · [22](../docs/references.md#ref-22) |
| MCP Guardian | MCP | AI Component → MCP Risks | ✓ / — | MCP Guardian 在 MCP 通信中增加鉴权、限流、日志和检查机制，是围绕工具协议的安全防护路线。 | [Paper](https://arxiv.org/abs/2504.12757) · [80](../docs/references.md#ref-80) |

### 记忆异常 · Memory

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| PI | Short-term Memory | Long Context → Response | — / ✓ | Positional Interpolation 通过位置插值扩展上下文窗口；原文将其标为缓解方法，并不把它列作异常检测器。 | [Paper](https://arxiv.org/abs/2306.15595) · [81](../docs/references.md#ref-81) |
| CoA | Short-term Memory | Long Context → Response | — / ✓ | Chain of Agents 让多个工作智能体分块处理长上下文，再由管理智能体汇总，缓解长文本处理限制。 | [Paper](https://arxiv.org/abs/2406.02818) · [82](../docs/references.md#ref-82) |
| ReDeep | Long-term Memory / RAG | Attention, LLM Parameters → Hallucination Results | ✓ / ✓ | ReDeEP 区分外部上下文与参数知识的利用以检测 RAG 幻觉；同文的 AARF 承担缓解作用，二者功能应分开理解。 | [Paper](https://arxiv.org/abs/2410.11414) · [27](../docs/references.md#ref-27) |
| LRP4RAG | Long-term Memory / RAG | Token Logits → Anomaly Probability | ✓ / — | LRP4RAG 使用逐层相关性传播的信号分类 RAG 幻觉，原文将它列为检测而非直接纠正方法。 | [Paper](https://arxiv.org/abs/2408.15533) · [83](../docs/references.md#ref-83) |

### 安全异常 · Security

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| GUARDIAN | Graph-based | Agent Graph → Anomalous Position | ✓ / — | GUARDIAN 以时序图刻画多智能体依赖并用重建信号识别异常协作，避免忽视智能体之间的相关性。 | [Paper](https://arxiv.org/abs/2505.19234) · [84](../docs/references.md#ref-84) |
| SentinelAgent | Graph-based | Agent Graph → Anomalous Position | ✓ / — | SentinelAgent 以交互图表示多智能体系统，在多个粒度识别异常协作模式；异常节点不应自动等同于已证实根因。 | [Paper](https://arxiv.org/abs/2505.24201) · [33](../docs/references.md#ref-33) |

### 任务规范异常 · Task Specification

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| SpecValidator | Classifier-based | Task Description → Defect Type / Probability | ✓ / — | SpecValidator 判断代码生成任务描述是否存在缺陷并预测缺陷类型或概率，用于执行前检查输入质量。 | [Paper](https://arxiv.org/abs/2604.24703) · [85](../docs/references.md#ref-85) |
| Ambig-SWE | Classifier-based | Task Instruction → Underspecification Label / Clarification Questions | ✓ / ✓ | Ambig-SWE 把软件工程指令欠明确问题分为识别、提问和利用答复三个环节，评测交互澄清的价值。 | [Paper](https://arxiv.org/abs/2502.13069) · [86](../docs/references.md#ref-86) |
| CLAMBER | Classifier-based | User Query → Ambiguity Label / Clarifying Question | ✓ / ✓ | CLAMBER 评测语言模型识别模糊信息需求并提出澄清问题的能力，是任务规范异常的相关基准。 | [Paper](https://arxiv.org/abs/2405.12063) · [87](../docs/references.md#ref-87) |
| Ask-or-Assume | Uncertainty-based | Task Instruction, Agent State → Ask-or-Execute Decision | ✓ / ✓ | Ask or Assume? 利用任务与状态中的不确定性决定何时提问澄清，研究编码智能体的执行与询问权衡。 | [Paper](https://arxiv.org/abs/2603.26233) · [88](../docs/references.md#ref-88) |
| Semantic Entropy | Uncertainty-based | Sampled Interpretations → Semantic Uncertainty Score | ✓ / — | Semantic Uncertainty 将语义等价的回答归组估计不确定性；综述借用该信号辅助判断可能的任务歧义。 | [Paper](https://arxiv.org/abs/2302.09664) · [89](../docs/references.md#ref-89) |
| SelfCheckGPT | Uncertainty-based | Sampled Responses → Consistency Score | ✓ / — | SelfCheckGPT 比较多次采样回答的一致性以检测可能的幻觉；一致性信号对任务歧义的使用是综述层面的延伸讨论。 | [Paper](https://arxiv.org/abs/2303.08896) · [90](../docs/references.md#ref-90) |

### 编排异常 · Orchestration

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| Introspective | Single-step | Token Logits → High-quality Plan | ✓ / ✓ | Introspective Planning 结合不确定性估计、任务歧义和反馈来改进规划，原文将其归入单步编排问题的处理路线。 | [Paper](https://arxiv.org/abs/2402.06529) · [91](../docs/references.md#ref-91) |
| API-bank | Single-step | LLM Parameters (Finetuning) → High-quality Plan | — / ✓ | API-Bank 提供工具增强对话与 API 调用基准，并探索训练提升工具使用能力；原文表 V 标为缓解而非检测。 | [Paper](https://arxiv.org/abs/2304.08244) · [92](../docs/references.md#ref-92) |
| ReAct | Single-step | Prompt → High-quality Plan | ✓ / ✓ | ReAct 交替进行推理、行动和环境观察，使智能体能够据反馈调整计划；综述在规划与运行时纠错中引用它。 | [Paper](https://arxiv.org/abs/2210.03629) · [14](../docs/references.md#ref-14) |
| ToolLLM | Multi-step | LLM Parameters (Finetuning) → High-quality Plan | — / ✓ | ToolLLM 围绕大规模真实 API 构建指令与调用路径训练资源；综述将其作为多步工具规划的能力增强方法。 | [Paper](https://arxiv.org/abs/2307.16789) · [4](../docs/references.md#ref-4) |
| Reflexion | Multi-step | External Feedback → High-quality Plan | ✓ / ✓ | Reflexion 把执行反馈转为语言反思并保留到后续尝试中，在不更新模型参数的情况下改善行为。 | [Paper](https://arxiv.org/abs/2303.11366) · [93](../docs/references.md#ref-93) |
| CodeAct | Multi-step | Tool Description → Code | — / ✓ | CodeAct 将行动表示为可执行代码，以编程语言表达复杂工具操作；原文将其列为多步编排的缓解方法。 | [Paper](https://arxiv.org/abs/2402.01030) · [94](../docs/references.md#ref-94) |

### 通信异常 · Communication

| 方法 | 路线 | 输入 → 输出 | D / M | 主要思想 | 资源 |
| --- | --- | --- | --- | --- | --- |
| AgentPrune | Redundancy | Agent Graph → Optimized Agent Graph | ✓ / ✓ | AgentPrune 对消息传递图进行剪枝，降低冗余通信及其成本；综述将其放在通信异常检测与缓解中。 | [Paper](https://arxiv.org/abs/2410.02506) · [41](../docs/references.md#ref-41) |
| G-Designer | Redundancy | Agent Graph → Optimized Agent Graph | ✓ / ✓ | G-Designer 用图模型生成任务相关的通信拓扑，减少不必要的通信并改善多智能体协作效率。 | [Paper](https://arxiv.org/abs/2410.11782) · [95](../docs/references.md#ref-95) |

### 终止异常 · Termination

原文 Table V 未单列终止检测算法，提到任务成功状态和执行步数等规则；相关失败研究见 [Termination papers](../papers/README.md#termination)。

<a id="localization"></a>

## Root Cause Localization

按[原文 §VI](https://arxiv.org/html/2606.01581v2#S6)分为轨迹回放/谱分析、结构化轨迹、LLM 归因。表内方法可与数据集同名，二者角色分别维护。

### Trajectory Replay & Spectrum Analysis

| 方法 | 输入 | 输出 | 核心思路 | 资源 |
| --- | --- | --- | --- | --- |
| FAMAS | 成败轨迹 / state–action–agent 元组 | 可疑智能体与动作排序 | 结合失败频率、重复程度和动作中心性计算可疑度。 | [Paper](https://arxiv.org/abs/2509.13782) |

### Structured Trace Modeling

| 方法 | 输入 | 输出 | 核心思路 | 资源 |
| --- | --- | --- | --- | --- |
| GraphTracer | 信息依赖图 | 上游错误节点 | 沿信息流反向追踪下游错误的来源。 | [Paper](https://arxiv.org/abs/2510.10581) |
| AgenTracer | 故障注入与反事实回放轨迹 | 责任智能体与步骤 | 用可控生成的失败轨迹训练归因模型。 | [Paper](https://arxiv.org/abs/2509.03312) |
| Causal attribution | 结构化因果图 | 责任主体与关键动作 | 以因果结构和反事实推断进行归因。 | [Paper](https://arxiv.org/abs/2509.08682) |
| SentinelAgent | 智能体交互图与执行动态 | 异常协作与行为模式 | 以图结构与分层监测支持异常位置分析。 | [Paper](https://arxiv.org/abs/2505.24201) |
| StepFinder | 轨迹的时序语义特征 | 根因步骤 | 语义特征与时序建模结合，处理跨步骤依赖。 | [Paper](https://arxiv.org/abs/2606.03467) |

### LLM-based Attribution

| 方法 | 输入 | 输出 | 核心思路 | 资源 |
| --- | --- | --- | --- | --- |
| Who&When | 失败日志 | 责任智能体、决定性步骤 | All-at-once、Step-by-step、Binary Search三种归因方式。 | [Paper](https://arxiv.org/abs/2505.00212) · [Project](https://github.com/ag2ai/Agents_Failure_Attribution) · [Data](https://huggingface.co/datasets/Kevin355/Who_and_When) |
| AgentFail | 工作流日志与故障分类知识 | 故障位置、根因 | 用细粒度故障分类引导语义归因。 | [Paper](https://arxiv.org/abs/2509.23735) · [Project](https://github.com/Jenna-Ma/JaWs-AgentFail) · [Data](https://github.com/Jenna-Ma/JaWs-AgentFail) |
| AgentDebug | 执行轨迹与错误分类 | 诊断反馈与修复指导 | 将分类感知诊断与轨迹重规划衔接。 | [Paper](https://arxiv.org/abs/2509.25370) · [Project](https://github.com/ulab-uiuc/AgentDebug) · [Data](https://drive.google.com/drive/folders/1bQe6dQA85pktT63YnKIKJDTVaH3O3Vpu?usp=drive_link) |

<a id="resolution"></a>

## Resolution

以下是[原文 §VII](https://arxiv.org/html/2606.01581v2#S7)的10类**处置机制**，每类链接对应方法论文/实现文档；机制数量不等于独立算法数量。

### Pre-execution · 执行前预防

| 机制 | 作用 | 代表方法 / 论文 |
| --- | --- | --- |
| 任务重述与细化 | 补充目标、约束、成功判据与子任务。 | [CoT](https://arxiv.org/abs/2201.11903) · [ReAct](https://arxiv.org/abs/2210.03629) · [Tree of Thoughts](https://arxiv.org/abs/2305.10601) |
| 计划验证 | 执行前验证计划的可行性、依赖和约束。 | [AutoGen](https://arxiv.org/abs/2308.08155) |
| 动作空间约束 | 限制工具、接口、参数与执行环境。 | [Toolformer](https://arxiv.org/abs/2302.04761) · [SWE-agent](https://arxiv.org/abs/2405.15793) |

### In-execution · 执行中纠正

| 机制 | 作用 | 代表方法 / 论文 |
| --- | --- | --- |
| 观察驱动重规划 | 利用新观察调整后续行动。 | [ReAct](https://arxiv.org/abs/2210.03629) |
| 自我修正 | 通过批评、反馈、反思改进中间结果。 | [Self-Refine](https://arxiv.org/abs/2303.17651) · [Reflexion](https://arxiv.org/abs/2303.11366) |
| 运行时约束与修复 | 拦截不合法动作，修复格式和接口集成错误。 | [AgentSpec](https://arxiv.org/abs/2503.18666) · [Comfrey](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/319/Comfrey-Mitigating-Integration-Failures-in-LLM-enabled-Software-at-Run-Time) |
| 冗余执行与选择 | 生成多个候选，通过一致性、投票或验证器选择。 | [Self-Consistency](https://arxiv.org/abs/2203.11171) · [Debate](https://arxiv.org/abs/2305.14325) · [AutoGen](https://arxiv.org/abs/2308.08155) |

### Post-execution · 执行后恢复

| 机制 | 作用 | 代表方法 / 论文 |
| --- | --- | --- |
| 回滚与重执行 | 恢复到已保存状态，从修正点继续执行。 | [ARC](https://arxiv.org/abs/2602.13723) · [LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence) |
| 记忆与技能更新 | 保存经验、反思与可复用技能。 | [Reflexion](https://arxiv.org/abs/2303.11366) · [Voyager](https://arxiv.org/abs/2305.16291) |
| 策略与提示修订 | 持久改进后续运行的提示和策略。 | [AutoPrompt](https://arxiv.org/abs/2010.15980) · [P-Tuning v2](https://arxiv.org/abs/2110.07602) · [DePT](https://arxiv.org/abs/2309.05173) · [Promptbreeder](https://arxiv.org/abs/2309.16797) |

## 实现入口

`Project`仅在已有核验记录提供原始项目时列出，未列出不表示作者没有开源。本文不提供重写算法或复现性能声明。输入数据与标签应对照[数据集目录](../datasets/README.md)选择。
