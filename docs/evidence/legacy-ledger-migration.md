# Legacy ledger migration: J-001–J-095 / 旧判断卡完整迁移清单

> **Closed set / 闭集**：J-001–J-095。历史源为分片前 Git 快照 `1f99c832be8cbc82631beb7679d82994a2b7e0fb^`；当前卡位于 `docs/{zh,en}/ledger/`。本文件是逐卡双语审计清单，不替代台账。

## Scope and reading rules / 范围与阅读规则

- 历史快照 `1f99c832be8cbc82631beb7679d82994a2b7e0fb^` 的中英文总台账各含目标 95 张卡；每张卡在下方有文件/行锚点。
- 当前分片每张 J-001–J-095 卡均链接回本清单；当前卡中的新证据、收窄或状态变化不倒填进历史值。
- **Unknown / unverified**：历史正文没有的字段明确写未知/未验证，不从当前继任卡推回。
- 历史独立受众规模字段为 0/86；历史 schema 把规模放在普及闸复核内，因此单独字段记为未知而不臆造。
- **[self-imposed] 可删除约束**：逐字快照字段和锚点不等于语义等价；语义等价须 fresh-context reviewer 复核。

## Coverage summary / 覆盖摘要

- 历史卡：中文 95 + 英文 95；当前配对卡：中文 95 + 英文 95。
- 历史字段（提出日期、一句话命题、普及闸复核、透镜、推理链、时间窗、证伪条件、领先指标、置信度、depends-on、最强反方、与共识、外部对照来源、出处、下次检查日、状态）：两种语言均 95/95。
- 独立 Audience scale / 受众规模：J-001–J-086 两种语言均 0/86（历史 schema 将规模放在普及闸复核内）；J-087–J-095 两种语言均 9/9；当前 J-001–J-095 配对卡均 95/95。

## Per-card inventory / 逐卡清单

## J-001

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L5–L24`；`docs/en/ledger/01-10.md:L5–L24`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L520–L538`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L5–L24`
- **原始标题**：同等能力的单位推理成本继续下降
- **原始一句话命题**：同等能力的单位推理成本到 2029 年底再降一个数量级。
- **原始推理链**：推理是可并行的确定性计算 → 累计产量与工程优化带来学习曲线 → 硬件能效、模型效率、调度复用三条相对独立的下降通道共同降低单位成本 → 同等能力可以被更频繁地调用。
- **原始时间窗**：2026-01 至 2029-12。
- **原始证伪条件**：出现连续 18 个月以上，达到同等能力的最低公开单位价格不降反升，且该上升不能由需求侧临时挤兑或一次性能源价格冲击解释。
- **原始领先指标**：达到固定基准分数所需的最低公开单位价格、单位算力能耗、开源模型追平当时最强闭源模型的滞后月数；每半年观察。
- **原始置信度**：高。
- **原始 depends-on**：—。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：与方向一致，但“2029 年再降十倍”证据不足；来源支持下降通道，不支持具体数量级。仍坚持：三条下降通道（硬件能效、模型效率、调度复用）相对独立，来源只是没有测量到具体倍数，并未给出反向证据；数量级风险由「最低公开单位价格连续 18 个月上升」的证伪条件承担。
- **原始外部对照来源**：EXT-1（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L520–L538`
- **Current card anchor**: `docs/en/ledger/01-10.md:L5–L24`
- **Original title**: Unit reasoning cost keeps falling
- **Original one-sentence judgment**: The unit cost of reasoning at equal capability falls another order of magnitude by the end of 2029.
- **Original reasoning chain**: Reasoning is parallelizable deterministic computation → cumulative production and engineering optimization create a learning curve → hardware efficiency, model efficiency, and scheduling/reuse provide relatively independent cost-decline paths → equal capability can be called more frequently.
- **Original time window**: 2026-01 to 2029-12.
- **Original falsifier**: For 18 consecutive months, the lowest public unit price for equal capability rises rather than falls, and the rise cannot be explained by temporary demand congestion or a one-off energy shock.
- **Original leading indicator**: Lowest public price for a fixed benchmark score, energy per unit of compute, and months for open models to catch the strongest closed model at the time; observe twice yearly.
- **Original confidence**: High.
- **Original depends-on**: —.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude. Retained: the three decline channels (hardware efficiency, model efficiency, scheduling reuse) are relatively independent, and the sources simply do not measure the specific multiple rather than contradicting it; the magnitude risk is carried by the falsification condition on lowest public unit price.
- **Original external comparison source**: EXT-1 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-001` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-002

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L25–L45`；`docs/en/ledger/01-10.md:L25–L45`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L539–L558`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L25–L45`
- **原始标题**：「从海量产出中筛出客观高质量」不是持久稀缺，只是 2~4 年的窗口
- **原始一句话命题**：「从海量产出中筛出客观高质量」不是持久稀缺，只是 2~4 年的窗口。
- **原始推理链**：客观质量在多数领域可形式化 → 可形式化即可被自动检验 → 生成模型可自我采样并自评 → 筛选内化为生成过程的一部分，不再是独立需求
- **原始时间窗**：窗口在 2029 年底前基本关闭
- **原始证伪条件**：到 2030 年，仍有一个规模可观的独立市场，其产品的核心价值就是「替用户从 AI 产出中挑出更好的那个」，且该市场没有被模型厂商内化
- **原始领先指标**：模型厂商是否把「多方案生成 + 自动择优」做成默认行为；第三方「AI 产出质检」类产品的收入是在扩大还是被挤压
- **原始置信度**：中
- **原始 depends-on**：J-001
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：仍坚持但机制不同：客观择优可能部分内置，责任型和领域型质检仍可能保留。
- **原始外部对照来源**：EXT-2, EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L539–L558`
- **Current card anchor**: `docs/en/ledger/01-10.md:L25–L45`
- **Original title**: “Selecting objectively high quality from abundant output” is not a durable scarcity, but merely a 2–4 year window
- **Original one-sentence judgment**: Selecting objectively high quality from abundant output is not a durable scarcity; it is merely a 2–4 year window.
- **Original reasoning chain**: Objective quality is formalizable in most domains → anything formalizable can be checked automatically → generative models can sample and self-evaluate → selection is internalized as part of generation and is no longer an independent need
- **Original time window**: The window will be basically closed by the end of 2029
- **Original falsifier**: In 2030, a sizable independent market still exists whose core value is “picking the better one from AI output for the user,” and that market has not been internalized by model vendors
- **Original leading indicator**: Whether model vendors make “generate multiple options + automatically select the best” the default behavior; whether revenue from third-party “AI output quality assurance” products is expanding or being squeezed
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Retain with a different mechanism: objective selection may be partly internalized, while liability- and domain-sensitive QA may persist.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-002` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-003

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L46–L66`；`docs/en/ledger/01-10.md:L46–L66`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L559–L578`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L46–L66`
- **原始标题**：真正持久的稀缺是「关于你的私有上下文」的所有权与可用形态
- **原始一句话命题**：真正持久的稀缺是「关于你的私有上下文」的所有权与可用形态。
- **原始推理链**：客观质量可自动化，主观适配不可 → 主观适配的关键输入是个人/组织的历史取舍 → 该输入私有、未被结构化、且本人无法自述 → 硬约束（产权 + 私有性）阻止同一股力量自动获取
- **原始时间窗**：2027 年起需求可见，2033 年前不会消失
- **原始证伪条件**：出现一种方法，仅凭少量公开可得的交互就能稳定复现某个体/组织的取舍偏好（达到本人认可度 80% 以上），使得私有历史不再必要
- **原始领先指标**：① 企业是否开始为「我们的语境／调性／禁区」建立专门的资产而不是散在提示词里；② 个人是否出现导出并携带自己偏好档案的行为；③ 「不像我们」这类否决理由是否开始被显式记录
- **原始置信度**：中
- **原始 depends-on**：J-001, J-002
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：仍坚持但证据边界更窄：外部材料支持私有上下文治理权重要，不证明其必然成为持久稀缺。
- **原始外部对照来源**：EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L559–L578`
- **Current card anchor**: `docs/en/ledger/01-10.md:L46–L66`
- **Original title**: The genuinely durable scarcity is ownership of “private context about you” and its usable form
- **Original one-sentence judgment**: The genuinely durable scarcity is ownership of private context about you and its usable form.
- **Original reasoning chain**: Objective quality can be automated, subjective fit cannot → the key input to subjective fit is an individual’s/organization’s history of choices → that input is private, unstructured, and impossible for the person to articulate → hard constraints (ownership + privacy) prevent the same force from acquiring it automatically
- **Original time window**: Demand becomes visible from 2027 and will not disappear before 2033
- **Original falsifier**: A method appears that can stably reproduce an individual’s/organization’s choice preferences using only a small amount of publicly available interaction (reaching over 80% approval by the person), making private history unnecessary
- **Original leading indicator**: ① Whether companies begin building dedicated assets for “our context / sensibility / boundaries” rather than leaving them scattered in prompts; ② whether individuals begin exporting and carrying their own preference profiles; ③ whether rejection reasons such as “this doesn’t feel like us” begin to be explicitly recorded
- **Original confidence**: Medium
- **Original depends-on**: J-001, J-002
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Retain with a narrower evidence boundary: sources support governance of private context, not that it must become durable scarcity.
- **Original external comparison source**: EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-003` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-004

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L67–L87`；`docs/en/ledger/01-10.md:L67–L87`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L579–L598`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L67–L87`
- **原始标题**：随着 AI 从「生成内容」转向「执行动作」，稀缺项是「让行动可撤销」的基础设施
- **原始一句话命题**：随着 AI 从「生成内容」转向「执行动作」，稀缺项是「让行动可撤销」的基础设施。
- **原始推理链**：生成便宜 → 试错策略普及 → 但试错的前提是结果可撤销 → AI 开始触碰不可逆动作（支付、部署、发送、签约）→ 不可逆性让物理与法律／责任约束显现，不会因模型变强而消失 → 「可撤销化」成为使用 AI 的前置条件而非可选项
- **原始时间窗**：2027 起需求显性化，2032 前成为标配
- **原始证伪条件**：到 2031 年，主流做法仍是让 AI 直接对生产环境/真实账户执行不可逆动作，且事故率低到无人要求隔离层
- **原始领先指标**：① 企业采购清单里是否出现「AI 动作沙盘／影子环境／回滚」这类独立条目；② 保险公司是否开始为「AI 自主执行动作」定价；③ 重大 AI 执行事故的公开案例频率
- **原始置信度**：中
- **原始 depends-on**：J-001
- **原始状态与谱系**：`REVISED` —— 2026-09-19 的机会耐久闸第三问复核发现本卡把「可撤销基础设施」整体当作稀缺项，却没有回答「制造丰富的同一股力量为何不能复制它」；已由 `J-065` 收窄取代。按第一节规则，本卡原文保留、编号不复用，不再作为商机依据。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：部分一致：隔离、监督与恢复机制已有依据；可撤销基础设施的独立稀缺性与时间窗仍证据不足。仍坚持：不可逆动作触发的是物理与法律／责任约束，不随模型变强消失；可撤销基础设施的独立稀缺性未获外部证实，因此置信度保持「中」而非上调。
- **原始外部对照来源**：EXT-2, EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L579–L598`
- **Current card anchor**: `docs/en/ledger/01-10.md:L67–L87`
- **Original title**: As AI shifts from “generating content” to “executing actions,” the scarce item is infrastructure that “makes actions reversible”
- **Original one-sentence judgment**: As AI shifts from generating content to executing actions, the scarce item is infrastructure that makes actions reversible.
- **Original reasoning chain**: Generation becomes cheap → trial-and-error strategies spread → but trial and error presupposes reversible outcomes → AI begins touching irreversible actions (payments, deployment, sending, signing) → irreversibility exposes physical and legal/liability constraints that will not disappear as models improve → “reversibilization” becomes a prerequisite for using AI rather than an option
- **Original time window**: Demand becomes explicit from 2027 and becomes standard before 2032
- **Original falsifier**: By 2031, mainstream practice still lets AI directly execute irreversible actions in production environments/real accounts, and the incident rate is low enough that no one demands an isolation layer
- **Original leading indicator**: ① Whether enterprise procurement lists begin to include standalone items such as “AI action sandboxes / shadow environments / rollback”; ② whether insurers begin pricing “AI autonomous action”; ③ the public frequency of major AI execution incidents
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` — the opportunity-durability review of 2026-09-19 found that this card treated “reversible infrastructure” as a single scarce item without ever answering why the same force that makes generation abundant cannot copy it; it has been narrowed and superseded by `J-065`. Per the section-1 rule the card is kept verbatim, its ID is not reused, and it is no longer a basis for any opportunity candidate.
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified. Retained: irreversible actions trigger physical and legal/liability constraints that do not dissolve as models improve; the independent scarcity of reversible infrastructure is unconfirmed externally, so confidence stays Medium rather than rising.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-004` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.
- **出生攻击 / Boundary attack**：J-004 must retain the historical “reversible infrastructure” proposition. Replacing it with J-065’s “cross-party reversal right” while retaining only J-004 fails this ledger; both historical text and successor relation remain independently visible.
- **J-004 → J-065**：historical status explicitly records narrowing/supersession by J-065; current J-065 reasoning separately links back to J-004.

## J-005

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L88–L108`；`docs/en/ledger/01-10.md:L88–L108`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L618–L637`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L88–L108`
- **原始标题**：生成丰富之后，价值向三类不可重组的输入集中：原始信号、可追责承诺、被验证因果
- **原始一句话命题**：生成丰富之后，价值向三类不可重组的输入集中：原始信号、可追责承诺、被验证因果。
- **原始推理链**：生成 = 对已有模式的重组 → 不能由重组得到的东西不会变丰富 → 供需铁律：与丰富品互补而未同步变丰富者升值 → 三类输入分别由物理在场、法律责任、干预实验三种硬约束保护
- **原始时间窗**：2029–2033 期间在定价上明显可见
- **原始证伪条件**：出现可靠的合成数据／模拟推理，在需要新观测的领域（如新药、新材料）系统性替代真实实验，且被监管接受
- **原始领先指标**：① 一手数据（传感器、现场、专有流水）的授权价格走势；② 带赔偿承诺的 AI 服务是否出现并能溢价；③ 实验与中试环节在研发预算中的占比
- **原始置信度**：中
- **原始 depends-on**：J-001
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：与机制一致但需收窄到高责任领域：可追溯信号与现实因果验证重要，不推出三类输入普遍升值。仍坚持：三类输入分别被物理在场、法律责任与干预实验三种硬约束保护，无法由重组得到；按外部证据边界把适用范围收窄到高责任领域，不再主张三类输入普遍升值。
- **原始外部对照来源**：EXT-7（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L618–L637`
- **Current card anchor**: `docs/en/ledger/01-10.md:L88–L108`
- **Original title**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality
- **Original one-sentence judgment**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality.
- **Original reasoning chain**: Generation = recombination of existing patterns → what cannot be obtained through recombination will not become abundant → supply-and-demand law: what complements abundant goods without becoming abundant in parallel appreciates → the three kinds of input are respectively protected by the hard constraints of physical presence, legal liability, and experimental intervention
- **Original time window**: Clearly visible in pricing during 2029–2033
- **Original falsifier**: Reliable synthetic data/simulation-based reasoning systematically replaces real experiments in fields requiring new observations (such as new drugs and new materials), and regulators accept it
- **Original leading indicator**: ① Price trends for licensing first-party data (sensors, field sites, proprietary workflows); ② whether AI services with compensation commitments appear and command a premium; ③ the share of experiments and pilot production in R&D budgets
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate. Retained: the three input classes are protected by physical presence, legal liability, and interventional experiment, and cannot be produced by recombination; following the external evidence boundary, the claim is narrowed to high-liability domains rather than broad appreciation.
- **Original external comparison source**: EXT-7 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-005` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-006

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L109–L128`；`docs/en/ledger/01-10.md:L109–L128`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L658–L676`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L109–L128`
- **原始标题**：推理吞吐先于长程自主性
- **原始一句话命题**：到 2028 年，单位任务可承受的并行推理次数将显著增加，生成—比较—修正会先于长程自主执行成为默认工作流。
- **原始推理链**：J-001 的单位成本下降 → 同一预算可运行更多候选路径 → 调度器可把简单步骤并行化并把困难步骤升级 → 工作流从单次回答变成候选搜索。
- **原始时间窗**：2026–2028。
- **原始证伪条件**：到 2028 年底，同等质量任务的主流系统仍只能承受单一路径，且成本下降没有转化为并行尝试。
- **原始领先指标**：公开系统的每任务采样数、端到端延迟与质量的联合曲线；每半年观察。
- **原始置信度**：高。
- **原始 depends-on**：J-001。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：方向一致但顺序尚未证实：能力与吞吐扩张早于可靠长程代理仍是可检验假设。仍坚持：并行候选搜索只需要单位成本下降与调度可行，不依赖外部对顺序的确认；顺序风险已写入 2028 年底的证伪条件。
- **原始外部对照来源**：EXT-1, EXT-3（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L658–L676`
- **Current card anchor**: `docs/en/ledger/01-10.md:L109–L128`
- **Original title**: Reasoning throughput precedes long-horizon autonomy
- **Original one-sentence judgment**: By 2028, the number of parallel reasoning paths affordable per task will rise substantially, making generate–compare–revise workflows common before long-horizon autonomous execution.
- **Original reasoning chain**: J-001 lowers unit cost → the same budget runs more candidate paths → a scheduler parallelizes simple steps and upgrades difficult ones → workflows shift from one answer to candidate search.
- **Original time window**: 2026–2028.
- **Original falsifier**: By the end of 2028, mainstream systems still support only one path per comparable task, and cost declines have not translated into parallel attempts.
- **Original leading indicator**: Per-task sample count, end-to-end latency, and quality curves for public systems; observe twice yearly.
- **Original confidence**: High.
- **Original depends-on**: J-001.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable. Retained: parallel candidate search requires only falling unit cost and feasible scheduling, not external confirmation of ordering; the ordering risk is carried by the end-2028 falsification condition.
- **Original external comparison source**: EXT-1, EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-006` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-007

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L129–L148`；`docs/en/ledger/01-10.md:L129–L148`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L677–L695`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L129–L148`
- **原始标题**：可接续上下文先于可靠长期记忆
- **原始一句话命题**：2026–2029 年，任务级检索上下文会先成为跨轮次协作的普遍底座，而带来源、可修正的长期记忆随后才成熟。
- **原始推理链**：并行尝试增加状态量 → 单一上下文窗口无法容纳全部历史 → 任务、证据和未决问题必须被检索 → 可检索上下文先解决“找回来”，来源与版本再解决“是否可信”。
- **原始时间窗**：2026–2029。
- **原始证伪条件**：到 2029 年，主流长任务仍主要依靠无结构聊天回放，且检索上下文没有带来可测的续接收益。
- **原始领先指标**：长任务恢复成功率、检索命中率、上下文窗口外信息的引用比例；按季度观察。
- **原始置信度**：高。
- **原始 depends-on**：J-006。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：与方向一致但机制不同：可检索上下文常与长窗口组合，不能据此断言固定产业先后。仍坚持：「先找回来、再判断是否可信」是能力依赖关系，与长窗口并存并不冲突；产业先后的部分按外部边界下调为可检验假设。
- **原始外部对照来源**：EXT-8（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L677–L695`
- **Current card anchor**: `docs/en/ledger/01-10.md:L129–L148`
- **Original title**: Resumable context precedes reliable long-term memory
- **Original one-sentence judgment**: From 2026 to 2029, task-level retrieval context will become a common base for multi-session collaboration before sourced, revisable long-term memory matures.
- **Original reasoning chain**: More parallel attempts create more state → one context window cannot hold the full history → tasks, evidence, and open questions must be retrieved → retrieval first solves “bring it back,” while provenance and versions solve “can it be trusted.”
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, mainstream long tasks still rely mainly on unstructured chat replay, and retrieval context produces no measurable continuation gain.
- **Original leading indicator**: Long-task recovery rate, retrieval hit rate, and the share of citations from outside the active context window; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order. Retained: “retrieve first, then establish trustworthiness” is a capability dependency that coexists with long windows; following the external boundary, the industry-ordering part is downgraded to a testable hypothesis.
- **Original external comparison source**: EXT-8 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-007` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-008

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L149–L168`；`docs/en/ledger/01-10.md:L149–L168`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L696–L714`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L149–L168`
- **原始标题**：有来源的长期记忆成为可靠协作前提
- **原始一句话命题**：2028–2031 年，要求来源、时间和置信边界的长期记忆会成为高价值连续协作的必要能力，而非聊天产品的附加功能。
- **原始推理链**：可接续上下文让历史可取回 → 历史中包含过时和互相矛盾的事实 → 需要事件来源、更新时间和撤回关系 → 只有可修正记忆才能支撑较长自主任务。
- **原始时间窗**：2028–2031。
- **原始证伪条件**：到 2031 年，高价值连续任务在没有来源、版本和撤回机制的记忆上仍能保持同等错误率与追责能力。
- **原始领先指标**：企业系统对记忆来源、时间戳和撤回接口的采购要求；事故复盘中由错误记忆导致的比例；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-007。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：仍坚持但机制不同：来源、版本与可修正性提高审计能力，尚未证明是所有高价值协作的必要条件。
- **原始外部对照来源**：EXT-4, EXT-8（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L696–L714`
- **Current card anchor**: `docs/en/ledger/01-10.md:L149–L168`
- **Original title**: Sourced long-term memory becomes a prerequisite for reliable collaboration
- **Original one-sentence judgment**: From 2028 to 2031, long-term memory with sources, dates, and confidence boundaries will become necessary for high-value continuous collaboration rather than a chat-product extra.
- **Original reasoning chain**: Resumable context makes history retrievable → history contains stale and conflicting facts → events need sources, update times, and retraction relations → only revisable memory can support longer autonomous tasks.
- **Original time window**: 2028–2031.
- **Original falsifier**: By 2031, high-value continuous tasks using memory without provenance, versioning, or retraction maintain the same error rate and accountability as sourced memory.
- **Original leading indicator**: Enterprise requirements for memory provenance, timestamps, and retraction APIs; the share of incidents caused by bad memory; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain with a different mechanism: provenance, versioning, and revisability improve auditability, but are not proven necessary for every high-value collaboration.
- **Original external comparison source**: EXT-4, EXT-8 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-008` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-009

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L169–L188`；`docs/en/ledger/01-10.md:L169–L188`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L715–L733`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L169–L188`
- **原始标题**：受限工作流中的连续执行先成熟
- **原始一句话命题**：2027–2030 年，权限有限、输入输出可检查的受限工作流会先实现稳定连续执行，开放世界自主性不会同步成熟。
- **原始推理链**：有来源记忆减少重复错误 → 封闭环境提供有限状态空间 → 权限与退出条件可预先写明 → 系统可连续完成多步动作并在失败处停止。
- **原始时间窗**：2027–2030。
- **原始证伪条件**：到 2030 年，开放世界任务的可靠性与受限工作流无显著差异，且权限边界与停止条件不再影响部署。
- **原始领先指标**：无人工接管完成的连续步骤数、受限环境的任务成功率、权限拒绝后的安全停止率；按季度观察。
- **原始置信度**：高。
- **原始 depends-on**：J-008。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：与共识一致：受限、可检查工作流先于开放世界自主执行，外部材料支持约束迁移而非替代原链。仍坚持：外部材料支持的是约束迁移本身，而受限工作流先稳定源于状态空间有限、权限与停止条件可预先写明，不是对共识的复述。
- **原始外部对照来源**：EXT-2, EXT-3（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L715–L733`
- **Current card anchor**: `docs/en/ledger/01-10.md:L169–L188`
- **Original title**: Continuous execution in constrained workflows matures first
- **Original one-sentence judgment**: From 2027 to 2030, constrained workflows with checkable inputs and outputs and limited permissions will achieve stable continuous execution before open-world autonomy matures.
- **Original reasoning chain**: Sourced memory reduces repeated errors → closed environments provide a limited state space → permissions and exits can be specified in advance → systems can complete multiple actions and stop at a known failure.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, open-world tasks have reliability indistinguishable from constrained workflows, and permission boundaries and stop conditions no longer affect deployment.
- **Original leading indicator**: Consecutive steps completed without intervention, constrained-environment success rate, and safe-stop rate after permission denial; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-008.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain. Retained: the sources support the constraint transition itself, while constrained workflows stabilize first because their state space is bounded and permissions and stop conditions can be specified in advance — not a restatement of consensus.
- **Original external comparison source**: EXT-2, EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-009` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-010

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L189–L207`；`docs/en/ledger/01-10.md:L189–L207`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L734–L752`
- **当前卡锚点**：`docs/zh/ledger/01-10.md:L189–L207`
- **原始标题**：长程自主执行晚于受限连续执行
- **原始一句话命题**：2029–2033 年，跨较长时间、较少人工确认的自主执行才会在部分高价值场景达到可接受可靠性。
- **原始推理链**：受限工作流先积累状态和失败样本 → 长任务暴露更多未预见状态 → 系统需要在不确定时暂停并请求证据 → 可靠的长程执行依赖环境观测和评估回路，而非只依赖更长计划。
- **原始时间窗**：2029–2033。
- **原始证伪条件**：到 2033 年，长程任务仍只能靠逐步人工确认，或其事故率没有比 2029 年显著下降。
- **原始领先指标**：单次授权覆盖的平均动作跨度、长任务中主动暂停比例、人工接管与不可逆事故率；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-009。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：方向一致但时间窗证据不足：长程能力在增长，可靠部署仍受任务时长与成功率约束。仍坚持：长程可靠性受环境观测与评估回路约束，外部长任务曲线与该机制一致；时间窗风险由 2033 年的证伪条件承担。
- **原始外部对照来源**：EXT-3（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L734–L752`
- **Current card anchor**: `docs/en/ledger/01-10.md:L189–L207`
- **Original title**: Long-horizon autonomy follows constrained continuous execution
- **Original one-sentence judgment**: From 2029 to 2033, autonomous execution across longer horizons with fewer human confirmations will reach acceptable reliability in some high-value settings.
- **Original reasoning chain**: Constrained workflows accumulate state and failure data → long tasks expose more unanticipated states → the system must pause and request evidence under uncertainty → reliable long-horizon execution depends on environment observation and evaluation loops, not simply longer plans.
- **Original time window**: 2029–2033.
- **Original falsifier**: By 2033, long-horizon tasks still require step-by-step human confirmation, or their incident rate has not materially fallen from 2029.
- **Original leading indicator**: Average action span per authorization, proactive pause rate, human takeover rate, and irreversible incident rate; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited. Retained: long-horizon reliability is bounded by environment observation and evaluation loops, which matches the external task-horizon curves; the window risk is carried by the 2033 falsification condition.
- **Original external comparison source**: EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-010` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-011

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L26–L45`；`docs/en/ledger/11-20.md:L26–L45`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L753–L771`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L26–L45`
- **原始标题**：跨媒介一致性先于长时连贯性
- **原始一句话命题**：2027–2030 年，跨文字、图像、音频的局部角色与格式一致性会先成为可复用能力，跨长时段的因果连贯性随后出现。
- **原始推理链**：推理吞吐增加 → 可以对同一任务采样多个媒介版本 → 共享表示和约束检查先解决局部一致 → 长时连贯还需要持续状态与反复验证。
- **原始时间窗**：2027–2030。
- **原始证伪条件**：到 2030 年，长时段交互世界的因果、空间和动作连贯性已普遍稳定，而局部跨媒介一致性仍非默认能力。
- **原始领先指标**：跨媒介实体保持率、镜头或音色连续性、长时段状态漂移率；按季度观察。
- **原始置信度**：中。
- **原始 depends-on**：J-006, J-007。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：仍坚持但证据不足：研究支持长时一致性困难，不证明跨媒介一致性必然先到。
- **原始外部对照来源**：EXT-5（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L753–L771`
- **Current card anchor**: `docs/en/ledger/11-20.md:L26–L45`
- **Original title**: Cross-media consistency precedes long-range coherence
- **Original one-sentence judgment**: From 2027 to 2030, local consistency of entities and formats across text, images, and audio will become reusable before causal coherence across long time spans.
- **Original reasoning chain**: More reasoning throughput → multiple media versions can be sampled for one task → shared representations and constraint checks solve local consistency first → long-range coherence still needs persistent state and repeated evaluation.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, causal, spatial, and action coherence in long interactive worlds is broadly stable while local cross-media consistency is not a default capability.
- **Original leading indicator**: Cross-media entity retention, shot or timbre continuity, and long-horizon state drift; observe quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain but with insufficient evidence: research supports long-range coherence difficulty, not that cross-media consistency must arrive first.
- **Original external comparison source**: EXT-5 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-011` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-012

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L46–L65`；`docs/en/ledger/11-20.md:L46–L65`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L772–L790`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L46–L65`
- **原始标题**：跨时间连贯生成依赖状态与验证
- **原始一句话命题**：2029–2034 年，长故事、持续交互环境和多轮设计中的跨时间连贯性，会在状态记忆和反复验证成熟后才达到生产级。
- **原始推理链**：局部跨媒介一致减少单帧错误 → 长任务仍会积累角色、空间和因果漂移 → 有来源记忆保存状态 → 自动反例与回放验证才允许持续修正。
- **原始时间窗**：2029–2034。
- **原始证伪条件**：到 2034 年，生产级长时生成仍不依赖状态追踪和回放验证，且漂移率已与短片段相同。
- **原始领先指标**：长时生成的状态漂移率、回放重现率、跨轮次修改的局部保持率；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-008, J-011。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：与机制一致但时间窗不足：长时连贯生成依赖状态保持、时空表示与持续评估。仍坚持：跨时间连贯依赖状态保持与回放验证，外部综述指出的正是同一难题；时间窗未获外部支持，因此置信度保持「中」。
- **原始外部对照来源**：EXT-5（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L772–L790`
- **Current card anchor**: `docs/en/ledger/11-20.md:L46–L65`
- **Original title**: Cross-time coherence depends on state and evaluation
- **Original one-sentence judgment**: From 2029 to 2034, cross-time coherence in long stories, persistent interactive environments, and multi-round design will reach production quality only after state memory and repeated evaluation mature.
- **Original reasoning chain**: Local cross-media consistency reduces frame-level errors → long tasks still accumulate drift in entities, space, and causality → sourced memory preserves state → automatic counterexamples and replay evaluation permit ongoing correction.
- **Original time window**: 2029–2034.
- **Original falsifier**: By 2034, production-grade long-generation neither depends on state tracking and replay evaluation nor has drift comparable to short segments.
- **Original leading indicator**: Long-generation state drift, replay reproducibility, and local-retention rate after cross-round edits; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-008, J-011.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation. Retained: long-range coherence depends on state retention and replay validation, which is the same difficulty the external review identifies; the window has no external support, so confidence stays Medium.
- **Original external comparison source**: EXT-5 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-012` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-013

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L66–L85`；`docs/en/ledger/11-20.md:L66–L85`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L791–L809`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L66–L85`
- **原始标题**：可检查的工具调用先于开放环境行动
- **原始一句话命题**：2027–2030 年，带参数、前置条件、权限和结果结构的工具调用会先普及，系统才会扩大到复杂环境中的连续行动。
- **原始推理链**：受限连续执行需要明确边界 → 自然语言工具调用难以检查 → typed 接口把动作和结果结构化 → 结构化调用先在少数工具上积累可靠性，再扩展工具面。
- **原始时间窗**：2027–2030。
- **原始证伪条件**：到 2030 年，高价值工具普遍接受无结构自然语言调用，且错误率与可检查接口无差异。
- **原始领先指标**：工具 schema 覆盖率、前置条件拒绝率、参数错误率、调用结果可回放比例；按季度观察。
- **原始置信度**：高。
- **原始 depends-on**：J-009。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：与共识一致：结构化、可检查工具调用已有产品化依据，但严格先后仍是项目判断。仍坚持：结构化接口的可检查性带来的先后是机制推论，产品化证据与之一致；严格先后仍由 2030 年的证伪条件承担。
- **原始外部对照来源**：EXT-6（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L791–L809`
- **Current card anchor**: `docs/en/ledger/11-20.md:L66–L85`
- **Original title**: Checkable tool calls precede open-environment action
- **Original one-sentence judgment**: From 2027 to 2030, tool calls with parameters, preconditions, permissions, and structured results will spread before systems expand into continuous action in complex environments.
- **Original reasoning chain**: Constrained continuous execution needs explicit boundaries → natural-language tool calls are hard to check → typed interfaces structure actions and results → structured calls first accumulate reliability on a few tools and then expand the tool surface.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, high-value tools broadly accept unstructured natural-language calls, with no error-rate difference from checkable interfaces.
- **Original leading indicator**: Tool-schema coverage, precondition rejection rate, parameter error rate, and replayable-result ratio; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment. Retained: the ordering follows from the checkability of structured interfaces, and productization evidence is consistent with it; the strict ordering is carried by the 2030 falsification condition.
- **Original external comparison source**: EXT-6 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-013` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-014

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L86–L105`；`docs/en/ledger/11-20.md:L86–L105`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L810–L828`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L86–L105`
- **原始标题**：可演练环境晚于单工具接入
- **原始一句话命题**：2028–2032 年，快照、影子运行、权限边界和回滚点组合成的可演练环境，会晚于单个工具接入但先于高价值自主行动普及。
- **原始推理链**：typed 工具能表达单个动作 → 多个动作会共享外部状态 → 真实状态不可随意试错 → 需要隔离、快照、影子运行和回滚来扩大尝试空间。
- **原始时间窗**：2028–2032。
- **原始证伪条件**：到 2032 年，高价值自主行动仍普遍直接写入真实环境，且隔离与回滚没有降低事故成本或采购门槛。
- **原始领先指标**：AI 工作流采购中影子环境和回滚条目；可恢复动作比例；自主行动保险或责任定价；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-009, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：仅保留为证据不足的景观：可演练、可恢复环境有治理依据，但统一市场顺序与时间窗未证实。
- **原始外部对照来源**：EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L810–L828`
- **Current card anchor**: `docs/en/ledger/11-20.md:L86–L105`
- **Original title**: Rehearsable environments follow single-tool integration
- **Original one-sentence judgment**: From 2028 to 2032, environments combining snapshots, shadow execution, permission boundaries, and rollback points will arrive after single-tool integration but before high-value autonomous action becomes common.
- **Original reasoning chain**: Typed tools express one action → multiple actions share external state → real state cannot be freely trialed → isolation, snapshots, shadow execution, and rollback expand the safe attempt space.
- **Original time window**: 2028–2032.
- **Original falsifier**: By 2032, high-value autonomous action still writes directly to real environments, and isolation and rollback have not reduced incident cost or procurement barriers.
- **Original leading indicator**: Shadow-environment and rollback line items in AI-workflow procurement; recoverable-action ratio; autonomous-action insurance or liability pricing; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain only as an evidence-limited landscape: governance supports rehearsable, recoverable environments, not a market order or window.
- **Original external comparison source**: EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-014` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-015

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L106–L125`；`docs/en/ledger/11-20.md:L106–L125`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L829–L847`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L106–L125`
- **原始标题**：形式化验证先于开放世界评估
- **原始一句话命题**：2026–2029 年，测试、schema、静态检查和反例搜索等形式化验证会先被生成系统内化，独立的现实结果评估随后成熟。
- **原始推理链**：并行生成增加候选数 → 可形式化性质能被程序快速判定 → 生成—测试—淘汰闭环降低错误输出 → 开放世界结果仍需等待观测与干预，不能由自评即时替代。
- **原始时间窗**：2026–2029。
- **原始证伪条件**：到 2029 年，开放世界结果评估已普遍可靠，而形式化测试仍未进入生成默认流程。
- **原始领先指标**：默认开启的自动测试比例、反例搜索覆盖率、schema 违规率、形式化验证对最终采纳率的影响；每季度观察。
- **原始置信度**：高。
- **原始 depends-on**：J-006, J-009。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：与方向一致但机制更宽：可执行测试通常先于开放世界结果评估，未证明所有系统默认内置。仍坚持：可形式化性质能被程序即时判定，开放世界结果必须等待观测，这一非对称不因外部材料而改变。
- **原始外部对照来源**：EXT-2, EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L829–L847`
- **Current card anchor**: `docs/en/ledger/11-20.md:L106–L125`
- **Original title**: Formal verification precedes open-world evaluation
- **Original one-sentence judgment**: From 2026 to 2029, tests, schemas, static checks, and counterexample search will be absorbed by generation systems before independent evaluation of real-world outcomes matures.
- **Original reasoning chain**: Parallel generation increases candidate count → formal properties can be judged quickly by programs → generate–test–discard loops lower output error → open-world outcomes still require waiting for observation and intervention and cannot be replaced immediately by self-evaluation.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, open-world outcome evaluation is broadly reliable while formal testing has not entered the default generation loop.
- **Original leading indicator**: Default-on automated-test ratio, counterexample-search coverage, schema-violation rate, and formal-verification impact on final adoption; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-006, J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration. Retained: formalizable properties can be decided immediately by programs while open-world outcomes must await observation, and that asymmetry is unchanged by the external material.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-015` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-016

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L126–L147`；`docs/en/ledger/11-20.md:L126–L147`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L848–L869`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L126–L147`
- **原始标题**：开放世界评估是自主边界扩张的最后门槛
- **原始一句话命题**：2029–2035 年，独立观测、因果干预和持续监控组成的开放世界评估，会成为长程自主行动扩大授权范围的最后技术门槛。
- **原始推理链**：形式化验证只能覆盖可预先写明的性质 → 长任务会遇到未建模状态和延迟副作用 → 外部观测与干预产生独立证据 → 持续监控把一次性测试变成运行时反馈 → 授权边界才可逐步扩大。
- **原始时间窗**：2029–2035。
- **原始证伪条件**：到 2035 年，长程自主系统在开放环境中无需独立观测、干预或持续监控，仍能达到与受限环境相当的事故率。
- **原始领先指标**：长任务中外部证据占比、因果实验触发率、运行时暂停与回滚率、授权范围随评估结果扩张的幅度；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-010, J-012, J-014, J-015。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`技术能力演进链`。
- **原始外部对照判断**：仅保留为证据不足的景观：开放世界反馈可能限制自主授权扩张，但不是已证实的最后门槛。
- **原始外部对照来源**：EXT-3, EXT-4（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L848–L869`
- **Current card anchor**: `docs/en/ledger/11-20.md:L126–L147`
- **Original title**: Open-world evaluation is the final gate for expanding autonomy
- **Original one-sentence judgment**: From 2029 to 2035, independent observation, causal intervention, and continuous monitoring will become the final technical gate for widening the authorization of long-horizon autonomous action.
- **Original reasoning chain**: Formal verification covers only pre-specified properties → long tasks encounter unmodeled states and delayed side effects → external observation and intervention create independent evidence → continuous monitoring turns one-off tests into runtime feedback → authorization boundaries can expand incrementally.
- **Original time window**: 2029–2035.
- **Original falsifier**: By 2035, long-horizon autonomous systems reach open environments without independent observation, intervention, or continuous monitoring and still match constrained-environment incident rates.
- **Original leading indicator**: Share of external evidence in long tasks, causal-experiment trigger rate, runtime pause and rollback rate, and authorization expansion following evaluation results; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-010, J-012, J-014, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain only as an evidence-limited landscape: open-world feedback may constrain autonomous authority, but is not established as the final gate.
- **Original external comparison source**: EXT-3, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-016` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-017

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L5–L25`；`docs/en/ledger/11-20.md:L5–L25`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L638–L657`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L5–L25`
- **原始标题**：AI 中介会比强关系更快扩大弱关系协调
- **原始一句话命题**：2027–2033 年，AI 中介会比强关系更快扩大弱关系协调，但不会同步扩大人能长期在场的强关系数量。
- **原始推理链**：J-006 降低多方协调与信息压缩成本 → J-007 让共同背景和历史更容易被接续 → 弱关系的联系、翻译、介绍与约时间可以规模化 → 强关系仍受共同经历、互相承担、冲突修复和有限注意力约束 → 连接数量增长不会自动变成可依赖的承诺数量。
- **原始时间窗**：2027–2033。
- **原始证伪条件**：到 2033 年，AI 中介普及后，纵向研究显示个人可长期维持的强关系数量与可承担共同后果的关系数量同步显著上升，且不存在新的注意力或在场瓶颈。
- **原始领先指标**：工作、教育和交易中 AI 中介协调的比例；每次协调所需的人类时间；近关系网络规模与关系修复频率；每年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-006, J-007。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：与方向一致但因果仍待验证：外部材料支持弱／强关系分层，不直接证明 AI 中介造成容量差异。仍坚持：强关系受共同经历、互相承担与有限注意力约束，弱关系协调可规模化；因果缺口由纵向研究型领先指标承担，置信度不上调。
- **原始外部对照来源**：EXT-17, EXT-18（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L638–L657`
- **Current card anchor**: `docs/en/ledger/11-20.md:L5–L25`
- **Original title**: AI mediation expands weak-tie coordination faster than strong relationships
- **Original one-sentence judgment**: From 2027 to 2033, AI mediation will expand weak-tie coordination faster than strong relationships, without expanding the number of relationships in which a person can remain present over time.
- **Original reasoning chain**: J-006 lowers the cost of multi-party coordination and information compression → J-007 makes shared context and history easier to resume → contact, translation, introductions, and scheduling for weak ties can scale → strong ties remain constrained by shared experience, mutual responsibility, conflict repair, and finite attention → more connections do not automatically become more commitments that people can rely on.
- **Original time window**: 2027–2033.
- **Original falsifier**: By 2033, longitudinal evidence after widespread AI mediation shows that the number of strong relationships a person can sustain and the number of relationships in which they can bear shared consequences both rise materially, without a new attention or presence bottleneck.
- **Original leading indicator**: Share of work, education, and transactions coordinated through AI mediation; human time per coordination; close-network size and relationship-repair frequency; measured annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect. Retained: strong ties are bounded by shared experience, mutual exposure, and finite attention while weak-tie coordination scales; the causal gap is carried by longitudinal leading indicators, and confidence is not raised.
- **Original external comparison source**: EXT-17, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-017` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-018

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L148–L167`；`docs/en/ledger/11-20.md:L148–L167`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L870–L888`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L148–L167`
- **原始标题**：并行推理先于长程自主执行
- **原始一句话命题**：到 2028 年，生成—比较—修正会先于长程自主执行成为默认工作流。
- **原始推理链**：J-006 的并行吞吐增加 → 候选搜索先变便宜 → 可靠的长程环境控制仍需 J-009 的边界与验证 → 并行推理先普及。
- **原始时间窗**：2026–2028。
- **原始证伪条件**：到 2028 年底，主流高价值工作流已主要依赖少确认的长程自主执行，而非候选搜索。
- **原始领先指标**：每任务采样数、自动比较比例与无人工接管动作跨度；每半年观察。
- **原始置信度**：高。
- **原始 depends-on**：J-006, J-009。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与共识一致：并行的生成—比较—修正可能先于长程自主成为常态，但时间窗仍是项目推断。仍坚持：候选搜索先变便宜是 J-006 的直接推论；时间窗仍是本项目推断，由 2028 年底的证伪条件承担。
- **原始外部对照来源**：EXT-1（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L870–L888`
- **Current card anchor**: `docs/en/ledger/11-20.md:L148–L167`
- **Original title**: Parallel reasoning before long-horizon autonomy
- **Original one-sentence judgment**: By 2028, generate–compare–revise becomes the default workflow before long-horizon autonomy.
- **Original reasoning chain**: J-006 raises parallel throughput → candidate search becomes cheap first → reliable long-horizon environmental control still requires J-009 boundaries and evaluation → parallel reasoning spreads first.
- **Original time window**: 2026–2028.
- **Original falsifier**: By end-2028, high-value workflows mainly rely on low-confirmation long-horizon autonomy rather than candidate search.
- **Original leading indicator**: Samples per task, automatic comparison share, and action span without human takeover; semiannual.
- **Original confidence**: High.
- **Original depends-on**: J-006, J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference. Retained: cheaper candidate search follows directly from J-006; the window remains this project’s inference and is carried by the end-2028 falsification condition.
- **Original external comparison source**: EXT-1 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-018` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-019

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L168–L187`；`docs/en/ledger/11-20.md:L168–L187`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L889–L907`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L168–L187`
- **原始标题**：节省 token 只是窗口
- **原始一句话命题**：2026–2028 年，节省 token 的价值会被更强模型和更低成本的多次尝试压缩，主要是窗口而非持久稀缺。
- **原始推理链**：J-001 降低单位成本 → J-006 允许多采样 → 废案的 token 代价下降 → 省 token 的独立溢价缩小。
- **原始时间窗**：2026–2028。
- **原始证伪条件**：到 2028 年，买方仍持续为减少模型调用次数支付结构性溢价，且不是供给受限导致。
- **原始领先指标**：单位任务调用次数、每次调用价格与 token 优化服务的留存溢价；每季度观察。
- **原始置信度**：中。
- **原始 depends-on**：J-001, J-006。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：仍坚持但机制不同：成本下降同时来自推理效率与硬件调度；公开价格尚不足以证明优化溢价消失。
- **原始外部对照来源**：EXT-1, EXT-12（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L889–L907`
- **Current card anchor**: `docs/en/ledger/11-20.md:L168–L187`
- **Original title**: Token saving is a window
- **Original one-sentence judgment**: From 2026–2028, stronger models and cheaper repeated attempts compress the value of saving tokens; it is a window, not durable scarcity.
- **Original reasoning chain**: J-001 lowers unit cost → J-006 enables sampling → dud token cost falls → the independent premium for token saving shrinks.
- **Original time window**: 2026–2028.
- **Original falsifier**: By 2028, buyers still pay a structural premium for fewer model calls, without supply constraints explaining it.
- **Original leading indicator**: Calls per task, call price, and retention premium for token-optimization services; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Retain with a different mechanism: cost decline can come from inference efficiency and hardware scheduling; public prices do not prove optimization premiums vanish.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-019` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-020

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L188–L206`；`docs/en/ledger/11-20.md:L188–L206`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L908–L926`
- **当前卡锚点**：`docs/zh/ledger/11-20.md:L188–L206`
- **原始标题**：可复制内容的价格继续下降
- **原始一句话命题**：到 2028 年，可复制内容的边际价格继续下降，客观择优逐步成为生成流程内置能力。
- **原始推理链**：J-002 的可形式化质量被自动测试 → J-015 的生成—验证闭环扩大 → 同质内容供给增加 → 单纯交付内容的价格下降。
- **原始时间窗**：2026–2028。
- **原始证伪条件**：到 2028 年，通用可复制内容仍普遍保持稀缺溢价，且不是版权或算力限制造成。
- **原始领先指标**：同类内容生成成本、交付价格与自动筛选覆盖率；每季度观察。
- **原始置信度**：中。
- **原始 depends-on**：J-002, J-015。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与内容供给增加方向一致，但责任型筛选未必消失；检测、标注与来源机制仍需专门层。仍坚持：可复制内容供给增加压低边际价格这一供需推论成立；本卡不主张责任型筛选层消失，检测与来源机制仍按 J-022 处理。
- **原始外部对照来源**：EXT-1, EXT-4, EXT-11（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L908–L926`
- **Current card anchor**: `docs/en/ledger/11-20.md:L188–L206`
- **Original title**: Reproducible content keeps falling in price
- **Original one-sentence judgment**: By 2028, reproducible content keeps falling in marginal price as objective selection becomes part of generation.
- **Original reasoning chain**: J-002 formalizable quality is tested automatically → J-015 expands the generate–verify loop → homogeneous supply increases → mere content delivery loses price.
- **Original time window**: 2026–2028.
- **Original falsifier**: By 2028, generic reproducible content retains broad scarcity premiums without copyright or compute constraints.
- **Original leading indicator**: Generation cost, delivery price, and automatic-selection coverage; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-002, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers. Retained: the supply-demand inference that copyable content depresses marginal price holds; this card does not claim liability-sensitive selection disappears, and detection and provenance remain handled under J-022.
- **Original external comparison source**: EXT-1, EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-020` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-021

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L5–L24`；`docs/en/ledger/21-30.md:L5–L24`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L927–L945`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L5–L24`
- **原始标题**：一手现场信号先获得溢价
- **原始一句话命题**：2026–2029 年，未经记录的现场观测和可追溯来源会比二手表达更早获得溢价。
- **原始推理链**：J-005 的原始信号不可由重组生成 → J-015 让二手表达更易自动筛选 → 买方把溢价转向现场、来源与责任。
- **原始时间窗**：2026–2029。
- **原始证伪条件**：到 2029 年，买方对可验证现场与高保真重组不再支付差异化价格。
- **原始领先指标**：带时间地点来源的资料成交溢价、现场数据采购合同数；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-005, J-015。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：仍坚持但机制不同：可追溯的一手来源可能先升值；尚无普遍现场溢价的价格证据。
- **原始外部对照来源**：EXT-4, EXT-11（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L927–L945`
- **Current card anchor**: `docs/en/ledger/21-30.md:L5–L24`
- **Original title**: First-hand field signals earn a premium first
- **Original one-sentence judgment**: From 2026–2029, unrecorded field observations and traceable sources earn a premium earlier than second-hand expression.
- **Original reasoning chain**: J-005’s raw signals cannot be recombined → J-015 makes second-hand expression easier to screen → buyers shift premiums to field reality, sources, and accountability.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, buyers pay no differential for verifiable field reality over high-fidelity recombination.
- **Original leading indicator**: Premium for sourced material and field-data contracts; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Retain with a different mechanism: traceable first-hand sources may gain value first; broad field-premium pricing is unproven.
- **Original external comparison source**: EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-021` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-022

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L25–L44`；`docs/en/ledger/21-30.md:L25–L44`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L946–L964`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L25–L44`
- **原始标题**：可伪造信号推动凭据升级
- **原始一句话命题**：2026–2029 年，可伪造的个性化信号增加后，重要判断会转向更昂贵的身份、履约和责任凭据。
- **原始推理链**：J-005 使可追责主体升值 → J-017 使弱关系协调变便宜 → 表面互动更难区分 → 高价值决策提高凭据门槛。
- **原始时间窗**：2026–2029。
- **原始证伪条件**：高价值交易中，低成本生成身份信号的接受率上升且没有额外责任或验证要求。
- **原始领先指标**：多因素凭据采用率、保证金与责任条款的交易占比；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-005, J-017。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与“信任更重要”方向一致，但机制偏向来源、身份与责任凭据升级；采用率和成本仍未知。仍坚持：可伪造信号增加必然抬高高价值判断的验证门槛，这由信号伪造机制决定；采用率与成本未知，因此置信度保持「中」。
- **原始外部对照来源**：EXT-4, EXT-11（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L946–L964`
- **Current card anchor**: `docs/en/ledger/21-30.md:L25–L44`
- **Original title**: Forgable signals drive credential upgrades
- **Original one-sentence judgment**: From 2026–2029, more forgable personalized signals push important decisions toward costlier identity, fulfillment, and liability credentials.
- **Original reasoning chain**: J-005 raises accountable entities → J-017 cheapens weak-tie coordination → surface interaction is harder to distinguish → high-value decisions raise credential thresholds.
- **Original time window**: 2026–2029.
- **Original falsifier**: Acceptance of low-cost generated identity signals rises in high-value transactions without added liability or verification.
- **Original leading indicator**: Multifactor credential adoption, guarantees, and liability clauses; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-017.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown. Retained: more forgeable signals necessarily raise the verification threshold for high-value judgments, which follows from the forgery mechanism; adoption and cost are unknown, so confidence stays Medium.
- **Original external comparison source**: EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-022` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-023

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L45–L64`；`docs/en/ledger/21-30.md:L45–L64`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L965–L983`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L45–L64`
- **原始标题**：注意力转向兑现承诺
- **原始一句话命题**：2027–2030 年，重要注意力分配会从表达质量转向关系持续性与承诺兑现率。
- **原始推理链**：J-017 的协调供给增加 → J-022 的表面信号更易伪造 → 单次表达区分度下降 → 重复关系中的兑现记录获得更大权重。
- **原始时间窗**：2027–2030。
- **原始证伪条件**：到 2030 年，重要选择仍主要由单次生成表达预测，而非历史兑现记录。
- **原始领先指标**：平台与组织对兑现率、复购关系和违约记录的使用比例；每年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-017, J-022, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：证据不足，方向可保留：表达供给增加后履约记录可能更重要，但现有使用数据不能直接证明注意力转移。仍坚持：方向由「单次表达区分度下降 + 重复关系留痕」推出，现有使用数据既不能证明也不能否证；注意力转移风险由 2030 年的证伪条件承担。
- **原始外部对照来源**：EXT-16（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L965–L983`
- **Current card anchor**: `docs/en/ledger/21-30.md:L45–L64`
- **Original title**: Attention shifts toward fulfilled commitments
- **Original one-sentence judgment**: From 2027–2030, important attention allocation shifts from expression quality toward relationship continuity and fulfilled commitments.
- **Original reasoning chain**: J-017 expands coordination supply → J-022 makes surface signals easier to forge → one-off expression loses distinction → repeated fulfillment records gain weight.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, important choices are still predicted mainly by one-off generated expression rather than fulfillment records.
- **Original leading indicator**: Use of fulfillment, repeat relationships, and breach records; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-017, J-022, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift. Retained: the direction follows from declining discriminability of one-off expression plus durable records in repeated relationships, which current usage data can neither prove nor refute; the attention-shift risk is carried by the 2030 falsification condition.
- **Original external comparison source**: EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-023` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-024

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L65–L84`；`docs/en/ledger/21-30.md:L65–L84`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L984–L1002`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L65–L84`
- **原始标题**：身份凭据重新分层（仅图景）
- **原始一句话命题**：2027–2032 年，身份凭据可能围绕持续履约、责任和在场重新分层，但制度形式尚不确定。
- **原始推理链**：J-022 提高验证成本 → J-023 提高长期记录价值 → 不同风险场景采用不同凭据层级，但制度结果受平台与法律选择影响。
- **原始时间窗**：2027–2032。
- **原始证伪条件**：到 2032 年，高风险交易仍普遍只依赖单一低成本身份信号，且没有场景分层。
- **原始领先指标**：高风险服务的保证、审计和在场证明组合；每年观察。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-022, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：边界证据支持“凭据分层可能出现”，制度落点仍不确定，继续标为仅图景。仍坚持：仅作为图景保留，置信度不上调；升级为可下注判断需要制度落点的证据（法律或平台明确采用分层凭据）。
- **原始外部对照来源**：EXT-4, EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L984–L1002`
- **Current card anchor**: `docs/en/ledger/21-30.md:L65–L84`
- **Original title**: Credentials re-layer (landscape only)
- **Original one-sentence judgment**: From 2027–2032, credentials may re-layer around fulfillment, liability, and presence, but the institutional form is uncertain.
- **Original reasoning chain**: J-022 raises verification cost → J-023 raises the value of long records → risk contexts adopt different credential layers, subject to platform and legal choices.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, high-risk transactions still rely on one low-cost identity signal without contextual layers.
- **Original leading indicator**: Guarantees, audits, and presence proofs in high-risk services; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-022, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only. Retained as landscape only, with confidence not raised; upgrading to a bettable judgment requires evidence of an institutional endpoint (law or platforms explicitly adopting stratified credentials).
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-024` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-025

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L85–L104`；`docs/en/ledger/21-30.md:L85–L104`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1003–L1021`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L85–L104`
- **原始标题**：小团队产出能力上升
- **原始一句话命题**：2027–2030 年，小团队能以更少步骤完成更多可验证产出。
- **原始推理链**：J-009 的受限连续执行 → J-013 的可检查工具调用 → 重复知识步骤被代理化 → 人数不变时可验证产出增加。
- **原始时间窗**：2027–2030。
- **原始证伪条件**：到 2030 年，采用受限代理的同规模团队在可比任务上没有更高的可验证产出。
- **原始领先指标**：每位员工完成的可审计任务数、人工接管率和单位产出；每季度观察。
- **原始置信度**：中。
- **原始 depends-on**：J-009, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与知识工作自动化方向一致，但小团队净产出的因果证据仍不足。仍坚持：重复知识步骤被代理化后可验证产出上升是机制推论；因果缺口由同规模团队对照型领先指标承担。
- **原始外部对照来源**：EXT-16（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1003–L1021`
- **Current card anchor**: `docs/en/ledger/21-30.md:L85–L104`
- **Original title**: Small-team output rises
- **Original one-sentence judgment**: From 2027–2030, small teams complete more verifiable output with fewer steps.
- **Original reasoning chain**: J-009 constrained continuity → J-013 inspectable tools → repeated knowledge steps become agent-mediated → verifiable output rises at constant headcount.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, comparable teams using constrained agents do not produce more verifiable output.
- **Original leading indicator**: Auditable tasks per employee, takeover rate, and output per unit; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient. Retained: rising verifiable output once repeated knowledge steps are delegated follows from the mechanism; the causal gap is carried by leading indicators comparing equally sized teams.
- **Original external comparison source**: EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-025` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-026

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L105–L124`；`docs/en/ledger/21-30.md:L105–L124`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1022–L1040`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L105–L124`
- **原始标题**：责任边界不会同步消失
- **原始一句话命题**：2027–2032 年，责任边界不会与知识工作步骤的自动化同步消失。
- **原始推理链**：J-009 扩大可执行步骤 → J-013 使权限更可编程 → 事故仍需法律主体承担 → 授权、审查和异常升级位置保持稀缺。
- **原始时间窗**：2027–2032。
- **原始证伪条件**：到 2032 年，高价值场景普遍没有明确的人或组织承担 AI 行动后果。
- **原始领先指标**：AI 系统责任条款、异常升级岗位和保险赔付记录；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-009, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与共识一致：执行步骤自动化不会同步消除监督与责任边界；法规要求不等于岗位数量预测。仍坚持：事故需法律主体承担这一约束不随自动化消失；本卡不预测岗位数量，因此法规证据与之无冲突。
- **原始外部对照来源**：EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1022–L1040`
- **Current card anchor**: `docs/en/ledger/21-30.md:L105–L124`
- **Original title**: Responsibility boundaries remain
- **Original one-sentence judgment**: From 2027–2032, responsibility boundaries do not disappear at the same rate as knowledge-work steps.
- **Original reasoning chain**: J-009 expands executable steps → J-013 makes permissions programmable → accidents still need a legal entity → authorization, review, and escalation remain scarce.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, high-value AI actions routinely have no identifiable person or organization bearing consequences.
- **Original leading indicator**: Liability clauses, escalation roles, and insurance claims; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts. Retained: the constraint that incidents require a legal subject does not dissolve with automation; this card forecasts no job counts, so the regulatory evidence does not conflict with it.
- **Original external comparison source**: EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-026` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-027

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L125–L144`；`docs/en/ledger/21-30.md:L125–L144`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1041–L1059`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L125–L144`
- **原始标题**：租用算力扩大能力扩散
- **原始一句话命题**：2026–2029 年，租用算力会扩大小组织获得 AI 能力的范围，但不会平均分配收益。
- **原始推理链**：J-001 降低调用成本 → J-006 提高可承受尝试数 → 按需租用降低固定资本门槛 → 数据、入口和责任能力仍造成收益差异。
- **原始时间窗**：2026–2029。
- **原始证伪条件**：到 2029 年，小组织无法通过租用获得可比的通用推理能力，或能力扩散同步消除收益差异。
- **原始领先指标**：小组织 AI 调用占比、固定算力资本支出与租用价格；每季度观察。
- **原始置信度**：中。
- **原始 depends-on**：J-001, J-006。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与能力扩散方向一致，但收益不均的机制更具体地落在能源、数据与组织能力约束。仍坚持：能力可租用与收益不均来自两组不同约束（资本门槛 vs 数据、入口与责任能力），外部扩散证据只支持前者。
- **原始外部对照来源**：EXT-1, EXT-12（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1041–L1059`
- **Current card anchor**: `docs/en/ledger/21-30.md:L125–L144`
- **Original title**: Rented compute spreads capability
- **Original one-sentence judgment**: From 2026–2029, rented compute spreads access to AI capability for small organizations without distributing gains evenly.
- **Original reasoning chain**: J-001 lowers call cost → J-006 raises affordable attempts → renting lowers fixed-capital barriers → data, access, and liability capacity still differentiate gains.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, small organizations cannot obtain comparable general reasoning by renting, or diffusion eliminates gain differences.
- **Original leading indicator**: Small-organization call share, fixed compute capex, and rental price; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity. Retained: rentable capability and uneven gains arise from two different constraint sets (capital thresholds versus data, distribution, and liability capacity), and the diffusion evidence supports only the first.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-027` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-028

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L145–L164`；`docs/en/ledger/21-30.md:L145–L164`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1060–L1078`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L145–L164`
- **原始标题**：入口成为议价节点（仅图景）
- **原始一句话命题**：2027–2032 年，专有数据、用户分发和责任承接可能成为比模型本身更重要的议价节点。
- **原始推理链**：J-027 扩大模型可得性 → J-005 使真实输入与责任升值 → 可复制模型的差异下降 → 控制输入、出口和损失吸收能力可能获得租金。
- **原始时间窗**：2027–2032。
- **原始证伪条件**：到 2032 年，入口控制者相对无入口者没有持续溢价，且差异不是监管限制造成。
- **原始领先指标**：数据许可、分发抽成、AI 责任保险和渠道独占条款；每年观察。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-005, J-013。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：仅有边界证据：能源、数据与责任入口可能成为议价点，但持续租金尚未证实。仍坚持：仅作为图景保留，置信度不上调；升级需要持续租金的价格证据，而不是入口存在本身。
- **原始外部对照来源**：EXT-4, EXT-12（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1060–L1078`
- **Current card anchor**: `docs/en/ledger/21-30.md:L145–L164`
- **Original title**: Access becomes a bargaining node (landscape only)
- **Original one-sentence judgment**: From 2027–2032, proprietary data, distribution, and liability capacity may become more important bargaining nodes than models.
- **Original reasoning chain**: J-027 expands model access → J-005 raises the value of real inputs and responsibility → models become more reproducible → control of inputs, exits, and losses may earn rent.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, access controllers have no persistent premium over non-controllers absent regulatory constraints.
- **Original leading indicator**: Data licenses, distribution take rates, AI liability insurance, and channel exclusivity; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-005, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven. Retained as landscape only, with confidence not raised; upgrading requires price evidence of persistent rents, not merely the existence of gatekeeping positions.
- **Original external comparison source**: EXT-4, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-028` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-029

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L165–L184`；`docs/en/ledger/21-30.md:L165–L184`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1079–L1097`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L165–L184`
- **原始标题**：需求侧锚点保持
- **原始一句话命题**：2026–2030 年，地位、确定性、真实在场和责任归属仍是需求侧锚点，尽管表达与选择变丰富。
- **原始推理链**：J-017 扩大协调接触 → J-011 扩大可试身份与表达 → 选择数量增加不等于共同后果增加 → 需求仍围绕地位、确定性、在场和责任组织。
- **原始时间窗**：2026–2030。
- **原始证伪条件**：到 2030 年，跨群体行为显示这些需求不再预测重要选择，且不是测量或制度变化造成。
- **原始领先指标**：高价值消费、关系维持和承诺决策中对在场与责任的偏好；每年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-017, J-011。
- **原始状态与谱系**：ACTIVE。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：与保守方向一致：现实社交、福祉与责任仍是合理需求锚点，但不能证明 2030 年偏好不变。仍坚持：需求侧锚点由地位、确定性、在场与责任归属的稳定性推出；2030 年偏好不变无法被外部证实，风险由证伪条件承担。
- **原始外部对照来源**：EXT-17, EXT-18（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1079–L1097`
- **Current card anchor**: `docs/en/ledger/21-30.md:L165–L184`
- **Original title**: Demand-side anchors persist
- **Original one-sentence judgment**: From 2026–2030, status, certainty, embodied presence, and responsibility remain demand-side anchors despite richer expression and choice.
- **Original reasoning chain**: J-017 expands coordination → J-011 expands trial identities and expression → more options do not create shared consequences → demand remains organized around status, certainty, presence, and responsibility.
- **Original time window**: 2026–2030.
- **Original falsifier**: By 2030, these needs no longer predict important choices across groups, independent of measurement or institutional change.
- **Original leading indicator**: Preferences for presence and responsibility in high-value consumption, relationship, and commitment decisions; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-017, J-011.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven. Retained: the demand-side anchors follow from the stability of status, certainty, presence, and responsibility attribution; unchanged preferences through 2030 cannot be externally confirmed, and that risk is carried by the falsification condition.
- **Original external comparison source**: EXT-17, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-029` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-030

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L185–L203`；`docs/en/ledger/21-30.md:L185–L203`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1098–L1118`
- **当前卡锚点**：`docs/zh/ledger/21-30.md:L185–L203`
- **原始标题**：AI 代理协调而非共同经历（仅图景）
- **原始一句话命题**：2027–2032 年，AI 能代理背景同步与关系协调，但不能代理需要身体在场和共同承担的经历。
- **原始推理链**：J-017 使弱关系协调变便宜 → J-011 使多模态表达更丰富 → 共同经历仍要求身体、时间和互惠后果 → 协调代理不会自动增加强关系容量。
- **原始时间窗**：2027–2032。
- **原始证伪条件**：到 2032 年，代理互动在长期关系中稳定替代共同经历，且当事人报告与行为结果都无差异。
- **原始领先指标**：关系维护中代理消息与真实共同活动的比例、冲突修复结果和留存率；每年观察。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-017, J-011。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`近期图景`。
- **原始外部对照判断**：仅有边界证据：AI 已能代理协调，但能否替代共同经历尚无充分因果与代际证据。仍坚持：仅作为图景保留；共同经历要求身体、时间与互惠后果这一硬约束仍成立，但替代效应缺因果与代际证据，置信度不上调。
- **原始外部对照来源**：EXT-9, EXT-17（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1098–L1118`
- **Current card anchor**: `docs/en/ledger/21-30.md:L185–L203`
- **Original title**: AI mediates coordination, not shared experience (landscape only)
- **Original one-sentence judgment**: From 2027–2032, AI mediates context synchronization and relationship coordination but not experiences requiring embodied presence and shared consequences.
- **Original reasoning chain**: J-017 cheapens weak-tie coordination → J-011 enriches multimodal expression → shared experience still requires bodies, time, and reciprocal consequences → coordination agents do not expand strong-relationship capacity automatically.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, agent-mediated interaction reliably replaces shared experience in long relationships with no behavioral or reported difference.
- **Original leading indicator**: Agent messages versus shared activities, conflict-repair results, and retention; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-017, J-011.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient. Retained as landscape only: the hard constraint that shared experience requires bodies, time, and reciprocal consequences still holds, while substitution effects lack causal and generational evidence, so confidence is not raised.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-030` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-031

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L5–L25`；`docs/en/ledger/31-40.md:L5–L25`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1119–L1138`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L5–L25`
- **原始标题**：可暂停、可回放、可回滚的行动环境成为长程 AI 执行的准入条件
- **原始一句话命题**：可暂停、可回放、可回滚的行动环境成为长程 AI 执行的准入条件
- **原始推理链**：组织把长程任务交给代理 → 失败状态与责任成本累积 → 可观察、可暂停、可回滚降低不可逆损失 → 高价值部署把行动环境列为准入条件
- **原始时间窗**：2026–2032
- **原始证伪条件**：到 2032 年高价值代理执行仍普遍直接连接生产系统，且事故成本没有推动独立隔离环境采购
- **原始领先指标**：企业采购中沙盘、影子环境和回滚条目；代理事故复盘频率；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-010
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：仍坚持但机制不同：日志、监督与风险控制已有制度依据，完整可回滚准入条件及时间窗未证实。
- **原始外部对照来源**：EXT-4, EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1119–L1138`
- **Current card anchor**: `docs/en/ledger/31-40.md:L5–L25`
- **Original title**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Original one-sentence judgment**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Original reasoning chain**: Organizations delegate long-horizon tasks → failure states and liability accumulate → observable, pausable, rollback-capable environments reduce irreversible loss → high-value deployments make the environment an admission condition
- **Original time window**: 2026–2032
- **Original falsifier**: By 2032, high-value agent execution still commonly connects directly to production systems without incident costs driving separate isolation procurement
- **Original leading indicator**: Sandbox, shadow-environment, and rollback items in procurement; agent incidents; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-010
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: logging, oversight, and risk control have institutional support; a complete rollback gate and its window are unverified.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-031` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-032

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L26–L46`；`docs/en/ledger/31-40.md:L26–L46`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1139–L1158`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L26–L46`
- **原始标题**：授权审查与异常升级比执行步骤更稀缺
- **原始一句话命题**：授权审查与异常升级比执行步骤更稀缺
- **原始推理链**：可检查工具调用扩散 → 执行步骤被模板化 → 跨边界授权、异常升级和最终责任仍需判断 → 审查岗位相对执行步骤升值
- **原始时间窗**：2027–2032
- **原始证伪条件**：到 2032 年授权审查工时与执行工时同步下降，且事故率不因审查减少而上升
- **原始领先指标**：权限拒绝率、人工升级工时、责任岗位招聘；季度观察
- **原始置信度**：中
- **原始 depends-on**：J-013
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：与共识一致但相对稀缺性不足：授权审查和异常升级已制度化，供给比较仍缺数据。仍坚持：跨边界授权、异常升级与最终责任需要判断，不会被模板化吃掉；相对稀缺性缺供给数据，因此置信度保持「中」。
- **原始外部对照来源**：EXT-4, EXT-10, EXT-13（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1139–L1158`
- **Current card anchor**: `docs/en/ledger/31-40.md:L26–L46`
- **Original title**: Authorization review and exception escalation become scarcer than execution steps
- **Original one-sentence judgment**: Authorization review and exception escalation become scarcer than execution steps
- **Original reasoning chain**: Inspectable tool calls spread → execution steps become templated → cross-boundary authorization, exception escalation, and final responsibility still require judgment → review roles appreciate relative to execution steps
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, authorization-review hours fall at the same rate as execution hours without increased incidents
- **Original leading indicator**: Permission-denial rate, human escalation hours, responsibility-role hiring; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-013
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing. Retained: cross-boundary authorization, escalation, and final responsibility require judgment and are not absorbed by templating; relative scarcity lacks supply data, so confidence stays Medium.
- **Original external comparison source**: EXT-4, EXT-10, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-032` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-033

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L47–L67`；`docs/en/ledger/31-40.md:L47–L67`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1159–L1178`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L47–L67`
- **原始标题**：真实干预的可验证记录比解释本身更有价值
- **原始一句话命题**：真实干预的可验证记录比解释本身更有价值
- **原始推理链**：生成解释变便宜 → 解释供给过剩 → 真实干预产生不可复制结果 → 可验证记录连接因果与责任 → 记录获得溢价
- **原始时间窗**：2029–2033
- **原始证伪条件**：到 2033 年高责任市场不再为带现场证据的干预记录支付溢价
- **原始领先指标**：一手干预记录许可价、审计要求、带证据服务续约率；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-005
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：仍坚持但机制不同：合规证据、模型风险与现实干预记录的价值上升有依据，尚未证明必高于解释。
- **原始外部对照来源**：EXT-7, EXT-13（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1159–L1178`
- **Current card anchor**: `docs/en/ledger/31-40.md:L47–L67`
- **Original title**: Verifiable records of real interventions become more valuable than explanation itself
- **Original one-sentence judgment**: Verifiable records of real interventions become more valuable than explanation itself
- **Original reasoning chain**: Generated explanations become cheap → explanation supply becomes abundant → real interventions produce non-recombinable outcomes → verifiable records connect causality and responsibility → records earn a premium
- **Original time window**: 2029–2033
- **Original falsifier**: By 2033, high-liability markets no longer pay a premium for intervention records with field evidence
- **Original leading indicator**: First-hand intervention-license prices, audit requirements, evidence-backed renewal rates; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: compliance evidence, model risk controls, and intervention records are gaining value; superiority to explanation is unproven.
- **Original external comparison source**: EXT-7, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-033` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-034

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L68–L88`；`docs/en/ledger/31-40.md:L68–L88`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1179–L1198`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L68–L88`
- **原始标题**：合成证据先在低责任场景获准，高责任场景仍要求现实试验
- **原始一句话命题**：合成证据先在低责任场景获准，高责任场景仍要求现实试验
- **原始推理链**：合成资料降低探索成本 → 低责任场景可容忍模型误差 → 高责任场景承担身体、法律和赔偿后果 → 监管保留现实试验
- **原始时间窗**：2028–2033
- **原始证伪条件**：到 2033 年高责任领域普遍以合成证据取代现实试验且事故率不升
- **原始领先指标**：监管文件中合成证据采纳范围、试验预算、保险条款；年度观察
- **原始置信度**：中
- **原始 depends-on**：J-005
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：与共识一致但时间窗不足：低责任场景较易采用合成证据，高责任场景保留现实验证。仍坚持：高责任场景承担身体、法律与赔偿后果，监管因此保留现实试验；时间窗未获外部支持，由 2033 年的证伪条件承担。
- **原始外部对照来源**：EXT-7, EXT-9（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1179–L1198`
- **Current card anchor**: `docs/en/ledger/31-40.md:L68–L88`
- **Original title**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Original one-sentence judgment**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Original reasoning chain**: Synthetic material lowers exploration cost → low-liability contexts tolerate model error → high-liability contexts bear bodily, legal, and compensation consequences → regulators retain real trials
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, high-liability fields broadly replace real trials with synthetic evidence without higher incident rates
- **Original leading indicator**: Regulatory acceptance scope, trial budgets, insurance clauses; annual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation. Retained: high-liability settings carry bodily, legal, and compensation consequences, which is why regulators preserve real trials; the window has no external support and is carried by the 2033 falsification condition.
- **Original external comparison source**: EXT-7, EXT-9 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-034` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-035

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L89–L109`；`docs/en/ledger/31-40.md:L89–L109`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1199–L1218`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L89–L109`
- **原始标题**：责任抵押进入重要 AI 输出的交易结构
- **原始一句话命题**：责任抵押进入重要 AI 输出的交易结构
- **原始推理链**：复制表达增加 → 错误损失更难归因 → 买方要求谁承担后果 → 保险、赔付准备金和审计进入合同 → 责任抵押成为交易条件
- **原始时间窗**：2028–2033
- **原始证伪条件**：到 2033 年高价值 AI 服务仍无责任定价、赔付条款或审计要求
- **原始领先指标**：AI 责任保险保费、合同赔付上限、审计采购；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-005
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：仍坚持但机制不同：责任治理、保险与赔付安排正在进入交易结构，尚未普遍形成“责任抵押”。
- **原始外部对照来源**：EXT-14, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1199–L1218`
- **Current card anchor**: `docs/en/ledger/31-40.md:L89–L109`
- **Original title**: Responsibility collateral enters the transaction structure for consequential AI output
- **Original one-sentence judgment**: Responsibility collateral enters the transaction structure for consequential AI output
- **Original reasoning chain**: Reproducible expression increases → error losses become harder to attribute → buyers ask who bears consequences → insurance, reserves, and audits enter contracts → responsibility collateral becomes a transaction condition
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, high-value AI services still lack liability pricing, compensation clauses, or audit requirements
- **Original leading indicator**: AI liability premiums, contractual caps, audit procurement; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: liability governance, insurance, and compensation are entering transactions, but universal “liability collateral” is unproven.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-035` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-036

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L110–L130`；`docs/en/ledger/31-40.md:L110–L130`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1219–L1238`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L110–L130`
- **原始标题**：长期履约记录比一次自然表达更能分配注意力
- **原始一句话命题**：长期履约记录比一次自然表达更能分配注意力
- **原始推理链**：表达生成变便宜 → 表面可信度难区分 → 重复履约留下可核验记录 → 注意力转向长期一致性与兑现率
- **原始时间窗**：2027–2032
- **原始证伪条件**：到 2032 年重要选择仍主要由一次性表达而非履约记录预测
- **原始领先指标**：带历史表现的推荐采用率、复购与违约率；年度观察
- **原始置信度**：中
- **原始 depends-on**：J-017
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：证据不足，方向可保留：长期履约记录可能支持可信度判断，但没有注意力分配的直接证据。仍坚持：表达变便宜使表面可信度失效、重复履约留下可核验记录，机制不依赖注意力数据；缺口由领先指标承担。
- **原始外部对照来源**：EXT-13, EXT-14（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1219–L1238`
- **Current card anchor**: `docs/en/ledger/31-40.md:L110–L130`
- **Original title**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Original one-sentence judgment**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Original reasoning chain**: Expression generation becomes cheap → surface credibility becomes hard to distinguish → repeated fulfillment leaves verifiable records → attention shifts to longitudinal consistency and delivery rate
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, important choices are still driven mainly by one-off expression rather than fulfillment records
- **Original leading indicator**: Adoption of performance-history recommendations, repeat and default rates; annual
- **Original confidence**: Medium
- **Original depends-on**: J-017
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence. Retained: cheap expression voids surface credibility while repeated fulfillment leaves verifiable records, a mechanism that does not depend on attention data; the gap is carried by leading indicators.
- **Original external comparison source**: EXT-13, EXT-14 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-036` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-037

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L131–L151`；`docs/en/ledger/31-40.md:L131–L151`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1239–L1258`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L131–L151`
- **原始标题**：同规模小团队的可验证产出提高
- **原始一句话命题**：同规模小团队的可验证产出提高
- **原始推理链**：受限工作流稳定 → 工具调用可检查 → 少数人编排更多代理步骤 → 单位团队产出与可验证记录增加
- **原始时间窗**：2027–2031
- **原始证伪条件**：到 2031 年采用代理的小团队相对基线没有可重复的产出提升
- **原始领先指标**：团队人均交付量、返工率、可审计产出比例；季度观察
- **原始置信度**：中
- **原始 depends-on**：J-009
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：与共识一致但因果证据不足：AI 扩散支持可能性，不能单独证明同规模小团队产出提高。仍坚持：少数人编排更多可检查步骤是机制推论；同规模产出的因果缺口由对照型领先指标承担，置信度不上调。
- **原始外部对照来源**：EXT-1, EXT-16（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1239–L1258`
- **Current card anchor**: `docs/en/ledger/31-40.md:L131–L151`
- **Original title**: Comparable small teams produce more verifiable output
- **Original one-sentence judgment**: Comparable small teams produce more verifiable output
- **Original reasoning chain**: Constrained workflows stabilize → tool calls become inspectable → a few people orchestrate more agent steps → per-team output and audit records increase
- **Original time window**: 2027–2031
- **Original falsifier**: By 2031, agent-using small teams show no repeatable output gain over baseline
- **Original leading indicator**: Per-person delivery, rework, auditable-output share; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-009
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams. Retained: fewer people orchestrating more checkable steps follows from the mechanism; the causal gap on same-size output is carried by comparative leading indicators, and confidence is not raised.
- **Original external comparison source**: EXT-1, EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-037` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-038

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L152–L172`；`docs/en/ledger/31-40.md:L152–L172`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1259–L1278`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L152–L172`
- **原始标题**：授权、异常升级和责任岗位不会与执行步骤同速减少
- **原始一句话命题**：授权、异常升级和责任岗位不会与执行步骤同速减少
- **原始推理链**：工具调用可检查 → 权限边界更清晰 → 正常步骤自动化 → 异常与跨界后果不可预先穷尽 → 责任岗位保留
- **原始时间窗**：2027–2032
- **原始证伪条件**：到 2032 年责任岗位占比与执行岗位同步下降，且高风险事故没有增加
- **原始领先指标**：异常升级量、责任岗位招聘、事故后人工介入；季度观察
- **原始置信度**：中
- **原始 depends-on**：J-013
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：与共识一致：监督、验证、异常升级与责任不会随自动化同步消失，但岗位数量与时间窗未证实。仍坚持：异常与跨界后果不可预先穷尽，责任岗位因此保留；岗位数量与时间窗不是外部材料能给出的，由证伪条件承担。
- **原始外部对照来源**：EXT-10, EXT-13（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1259–L1278`
- **Current card anchor**: `docs/en/ledger/31-40.md:L152–L172`
- **Original title**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Original one-sentence judgment**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Original reasoning chain**: Inspectable tool calls spread → permission boundaries clarify → normal steps automate → exceptions and cross-boundary consequences cannot be fully precomputed → responsibility roles remain
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, responsibility-role share falls at the same rate as execution roles without more high-risk incidents
- **Original leading indicator**: Exception volume, responsibility-role hiring, post-incident human intervention; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-013
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven. Retained: exceptions and cross-boundary consequences cannot be enumerated in advance, which is why accountability roles persist; job counts and timing are not something the sources can supply and are carried by the falsification condition.
- **Original external comparison source**: EXT-10, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-038` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-039

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L173–L193`；`docs/en/ledger/31-40.md:L173–L193`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1279–L1298`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L173–L193`
- **原始标题**：模型租用更丰富，但能源、数据和渠道控制形成准入租金
- **原始一句话命题**：模型租用更丰富，但能源、数据和渠道控制形成准入租金
- **原始推理链**：单位推理成本下降 → 模型能力可租用 → 模型差异收窄 → 能源接入、独家数据和渠道仍受物理与产权约束 → 控制者获得准入租金
- **原始时间窗**：2027–2033
- **原始证伪条件**：到 2033 年控制能源、数据和渠道者相对非控制者没有持续溢价
- **原始领先指标**：租用模型价格、数据许可费、渠道抽成和能源接入价差；年度观察
- **原始置信度**：中
- **原始 depends-on**：J-001
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：仍坚持但机制不同：模型租用可能丰富，能源与基础设施接入的约束较实，数据和渠道租金仍未证实。
- **原始外部对照来源**：EXT-1, EXT-12（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1279–L1298`
- **Current card anchor**: `docs/en/ledger/31-40.md:L173–L193`
- **Original title**: Rented models become abundant, while energy, data, and channel control create access rents
- **Original one-sentence judgment**: Rented models become abundant, while energy, data, and channel control create access rents
- **Original reasoning chain**: Unit reasoning cost falls → model capability becomes rentable → model differences narrow → energy access, exclusive data, and channels remain constrained by physics and ownership → controllers earn access rents
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, controllers of energy, data, and channels have no persistent premium over non-controllers
- **Original leading indicator**: Rented-model prices, data-license fees, channel take rates, energy-access spreads; annual
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: model rental may become abundant, while energy and infrastructure constraints are real; data and channel rents remain unproven.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-039` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-040

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L194–L213`；`docs/en/ledger/31-40.md:L194–L213`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1299–L1318`
- **当前卡锚点**：`docs/zh/ledger/31-40.md:L194–L213`
- **原始标题**：能吸收 AI 事故的资产负债表成为独立稀缺
- **原始一句话命题**：能吸收 AI 事故的资产负债表成为独立稀缺
- **原始推理链**：真实干预和承诺升值 → AI 事故损失可量化 → 合同要求赔付能力 → 资本与保险把偿付能力定价 → 大资产负债表获得准入优势
- **原始时间窗**：2028–2033
- **原始证伪条件**：到 2033 年赔付能力不影响 AI 合同价格、融资或部署资格
- **原始领先指标**：责任保险保费、赔付准备金、合同资产要求；年度观察
- **原始置信度**：中
- **原始 depends-on**：J-005
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：证据不足但有现实锚点：保险与责任治理存在，资产负债表成为独立稀缺的未来溢价尚未证实。仍坚持：赔付能力被合同与保险定价，是现行治理的延伸；独立稀缺溢价未被证实，因此置信度保持「中」。
- **原始外部对照来源**：EXT-14, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1299–L1318`
- **Current card anchor**: `docs/en/ledger/31-40.md:L194–L213`
- **Original title**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Original one-sentence judgment**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Original reasoning chain**: Real interventions and commitments appreciate → AI accident losses become measurable → contracts require compensation capacity → capital and insurance price solvency → large balance sheets gain admission advantage
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, compensation capacity does not affect AI contract prices, financing, or deployment eligibility
- **Original leading indicator**: Liability premiums, reserves, contract asset requirements; annual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven. Retained: pricing solvency through contracts and insurance extends current governance; the independent scarcity premium is unproven, so confidence stays Medium.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-040` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-041

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L5–L25`；`docs/en/ledger/41-50.md:L5–L25`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1319–L1338`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L5–L25`
- **原始标题**：AI 先扩大弱关系的协调半径
- **原始一句话命题**：AI 先扩大弱关系的协调半径
- **原始推理链**：沟通与背景同步成本下降 → 翻译、介绍、约时可规模化 → 弱关系连接半径扩大 → 强关系仍受共同承担约束
- **原始时间窗**：2027–2033
- **原始证伪条件**：到 2033 年 AI 中介不提高跨组织弱关系连接数量或降低协调时间
- **原始领先指标**：AI 中介协调比例、跨组织联系数、单次协调人时；年度观察
- **原始置信度**：中
- **原始 depends-on**：J-017
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：方向一致但证据不足：AI 扩大沟通与协调范围，尚无足够数据区分弱关系与强关系的因果变化。仍坚持：协调成本下降先扩大弱关系半径，强关系仍受共同承担约束；因果区分缺口由弱／强关系分项领先指标承担。
- **原始外部对照来源**：EXT-16, EXT-18（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1319–L1338`
- **Current card anchor**: `docs/en/ledger/41-50.md:L5–L25`
- **Original title**: AI first expands the coordination radius of weak ties
- **Original one-sentence judgment**: AI first expands the coordination radius of weak ties
- **Original reasoning chain**: Communication and context-sync costs fall → translation, introductions, and scheduling scale → weak-tie connection radius expands → strong ties remain constrained by shared consequences
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, AI mediation neither increases cross-organization weak-tie connections nor reduces coordination time
- **Original leading indicator**: AI-mediated coordination share, cross-organization contacts, human time per coordination; annual
- **Original confidence**: Medium
- **Original depends-on**: J-017
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects. Retained: falling coordination cost widens weak-tie radius first while strong ties remain bounded by shared exposure; the causal-separation gap is carried by weak-/strong-tie leading indicators.
- **Original external comparison source**: EXT-16, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-041` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-042

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L26–L46`；`docs/en/ledger/41-50.md:L26–L46`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1339–L1358`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L26–L46`
- **原始标题**：共同经历与身体在场仍是强关系容量上限（仅图景）
- **原始一句话命题**：共同经历与身体在场仍是强关系容量上限（仅图景）
- **原始推理链**：多模态表达变丰富 → 代理陪伴与提醒普及 → 共同经历仍要求身体、时间和互惠后果 → 强关系容量受在场约束
- **原始时间窗**：2027–2033
- **原始证伪条件**：到 2033 年代理互动在长期关系中稳定替代共同经历，且报告与行为结果无差异
- **原始领先指标**：代理互动与共同活动比例、冲突修复、关系留存；年度观察
- **原始置信度**：低
- **原始 depends-on**：J-011
- **原始状态与谱系**：ACTIVE。
- **原始出处**：`中期图景`。
- **原始外部对照判断**：证据不足：伦理与照护治理保留人的主体性，但不能替代强关系容量与替代效应研究。仍坚持：仅作为图景保留，置信度不上调；升级需要长期关系中替代效应的行为与自述双重证据。
- **原始外部对照来源**：EXT-9（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1339–L1358`
- **Current card anchor**: `docs/en/ledger/41-50.md:L26–L46`
- **Original title**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Original one-sentence judgment**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Original reasoning chain**: Multimodal expression becomes abundant → mediated companionship and reminders spread → shared experience still requires bodies, time, and reciprocal consequences → strong-tie capacity remains presence-constrained
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, agent-mediated interaction reliably replaces shared experience in long relationships with no reported or behavioral difference
- **Original leading indicator**: Agent interaction versus shared activity, conflict repair, relationship retention; annual
- **Original confidence**: Low
- **Original depends-on**: J-011
- **Original status and lineage**: ACTIVE.
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects. Retained as landscape only, with confidence not raised; upgrading requires both behavioral and self-reported evidence of substitution in long-term relationships.
- **Original external comparison source**: EXT-9 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-042` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-043

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L47–L66`；`docs/en/ledger/41-50.md:L47–L66`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1554–L1573`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L47–L66`
- **原始标题**：高价值代理执行可能转向边界授权，而非逐步操作（仅图景）
- **原始一句话命题**：高价值代理执行可能转向边界授权，而非逐步操作（仅图景）。
- **原始推理链**：可回滚环境降低监督成本 → 代理承担更多步骤 → 监督转向权限边界与异常升级 → 高价值部署采用边界授权。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年仍普遍逐步审批且回滚未降低监督成本。
- **原始领先指标**：边界授权合同占比、逐步审批次数、演练采购；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-031, J-032, J-014。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：现行治理支持权限边界设计，但不能外推从逐步操作转为边界授权的长期界面。仍坚持：仅作为图景保留，置信度不上调；升级需要边界授权合同占比等实际采用证据，而不是现行权限设计本身。
- **原始外部对照来源**：EXT-4, EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1554–L1573`
- **Current card anchor**: `docs/en/ledger/41-50.md:L47–L66`
- **Original title**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only)
- **Original one-sentence judgment**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only).
- **Original reasoning chain**: Rollback-capable environments lower supervision cost → agents take more steps → supervision shifts to boundaries and escalation → high-value deployment uses boundary grants.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, high-value agents still require step approval and rollback has not lowered supervision cost.
- **Original leading indicator**: Boundary-grant share, step approvals, rehearsal procurement; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-031, J-032, J-014.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants. Retained as landscape only, with confidence not raised; upgrading requires adoption evidence such as the share of boundary-grant contracts, not the existence of current permission design.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-043` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-044

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L67–L86`；`docs/en/ledger/41-50.md:L67–L86`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1574–L1593`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L67–L86`
- **原始标题**：可吸收事故的责任位置成为代理基础设施的承重墙（仅图景）
- **原始一句话命题**：可吸收事故的责任位置成为代理基础设施的承重墙（仅图景）。
- **原始推理链**：执行扩大 → 尾部损失难由单一使用者承担 → 责任抵押成为准入 → 可赔付主体支撑基础设施。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年赔付能力不影响部署、价格或融资。
- **原始领先指标**：责任保费、合同准备金、偿付条款；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-032, J-040。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：责任与保险已被制度讨论，但偿付能力成为代理基础设施瓶颈尚未成立。仍坚持：仅作为图景保留，置信度不上调；升级需要赔付能力影响部署、价格或融资的直接证据。
- **原始外部对照来源**：EXT-14, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1574–L1593`
- **Current card anchor**: `docs/en/ledger/41-50.md:L67–L86`
- **Original title**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only)
- **Original one-sentence judgment**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only).
- **Original reasoning chain**: Execution scales → tail losses exceed one user’s capacity → collateral and balance sheets become admission conditions → solvent entities support infrastructure.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, solvency does not affect deployment, pricing, or financing.
- **Original leading indicator**: Liability premiums, reserves, solvency clauses; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-032, J-040.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished. Retained as landscape only, with confidence not raised; upgrading requires direct evidence that solvency affects deployment, pricing, or financing.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-044` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-045

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L87–L106`；`docs/en/ledger/41-50.md:L87–L106`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1594–L1613`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L87–L106`
- **原始标题**：合成表达越丰富，未经安排的现实观察越稀缺（仅图景）
- **原始一句话命题**：合成表达越丰富，未经安排的现实观察越稀缺（仅图景）。
- **原始推理链**：可回放内容增长 → 叙事失去区分度 → 未安排的现场观察成为稀缺信号 → 原始条件与因果责任升值。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年高责任决策不区分现场与合成，且价格、采纳和结果无差异。
- **原始领先指标**：现场证据溢价、原始记录要求、合成替代率；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-033, J-034。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：仍坚持但证据不足：来源标准的发展支持原始记录相对重要，不能证明未经安排观察必成稀缺品。
- **原始外部对照来源**：EXT-11（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1594–L1613`
- **Current card anchor**: `docs/en/ledger/41-50.md:L87–L106`
- **Original title**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only)
- **Original one-sentence judgment**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only).
- **Original reasoning chain**: Replayable supply grows → narrative loses distinctiveness → unarranged field observation becomes scarce → preserving conditions and causality gains value.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, high-liability decision-makers do not distinguish field from synthetic evidence.
- **Original leading indicator**: Field-evidence premium, raw-record requirements, synthetic substitution; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-033, J-034.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: provenance standards support the relative importance of original records, not inevitable scarcity of unarranged observation.
- **Original external comparison source**: EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-045` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-046

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L107–L126`；`docs/en/ledger/41-50.md:L107–L126`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1614–L1633`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L107–L126`
- **原始标题**：高责任场景仍为现场因果记录保留溢价（仅图景）
- **原始一句话命题**：高责任场景仍为现场因果记录保留溢价（仅图景）。
- **原始推理链**：解释变便宜 → 责任方区分建议与干预 → 现场记录连接行为、结果和赔付 → 高责任交易支付溢价。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年合成替代现场后事故率、保险价和合同价无差异。
- **原始领先指标**：现场记录许可价、保险折扣、试验要求；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-033, J-034。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：高责任场景要求来源与验证，但现场因果记录溢价尚无价格证据。仍坚持：仅作为图景保留，置信度不上调；升级需要现场因果记录带来的价格或保险费率差异证据。
- **原始外部对照来源**：EXT-7, EXT-11（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1614–L1633`
- **Current card anchor**: `docs/en/ledger/41-50.md:L107–L126`
- **Original title**: High-liability settings retain a premium for field causal records (landscape only)
- **Original one-sentence judgment**: High-liability settings retain a premium for field causal records (landscape only).
- **Original reasoning chain**: Cheap explanations → liable parties distinguish advice from intervention → field records connect action, outcome and compensation → high-liability transactions pay.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, replacing field records with synthetic evidence changes neither accidents nor prices.
- **Original leading indicator**: Record licensing, insurance discounts, trial requirements; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-033, J-034.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence of price or insurance-rate differences attributable to field causal records.
- **Original external comparison source**: EXT-7, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-046` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-047

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L127–L146`；`docs/en/ledger/41-50.md:L127–L146`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1634–L1653`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L127–L146`
- **原始标题**：AI 关系的复制性扩大陪伴供给，但不可复制互惠成为稀缺（仅图景）
- **原始一句话命题**：AI 关系的复制性扩大陪伴供给，但不可复制互惠成为稀缺（仅图景）。
- **原始推理链**：记忆、耐心和人格可复制 → 陪伴随时可用 → 复制削弱专属感与共同风险 → 不可复制互惠稀缺。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年复制式陪伴稳定替代人类互惠且行为无差异。
- **原始领先指标**：陪伴复制率、退出率、留存与修复；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-041, J-042。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：可复制 AI 陪伴可能扩大供给，但互惠稀缺与长期替代没有数据。仍坚持：仅作为图景保留，置信度不上调；升级需要复制式陪伴与人类互惠的长期行为对照证据。
- **原始外部对照来源**：EXT-9, EXT-17（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1634–L1653`
- **Current card anchor**: `docs/en/ledger/41-50.md:L127–L146`
- **Original title**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only)
- **Original one-sentence judgment**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only).
- **Original reasoning chain**: Copyable memory, patience and style → companionship scales → copyability reduces exclusivity and shared risk → non-copyable reciprocity is scarce.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, copyable companionship replaces human reciprocity with no behavioral difference.
- **Original leading indicator**: Copy rate, exit rate, retention and repair outcomes; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-042.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence. Retained as landscape only, with confidence not raised; upgrading requires long-term behavioral comparisons between copyable companionship and human reciprocity.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-047` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-048

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L147–L166`；`docs/en/ledger/41-50.md:L147–L166`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1654–L1673`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L147–L166`
- **原始标题**：人与 AI 的授权、退出与主体边界成为关系规范议题（仅图景）
- **原始一句话命题**：人与 AI 的授权、退出与主体边界成为关系规范议题（仅图景）。
- **原始推理链**：关系可复制、暂停和迁移 → 记忆与承诺边界分离 → 数据、退出和责任冲突增加 → 制度定义主体边界。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年相关争议不持续且普通合同足够。
- **原始领先指标**：数据纠纷、退出条款、专门规范或判例；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-041, J-042。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：与规范问题存在的共识一致，但预测证据不足：授权、退出与主体边界仍未形成稳定制度终点。仍坚持：仅作为图景保留，置信度不上调；升级需要争议持续且普通合同不足以处理的制度证据。
- **原始外部对照来源**：EXT-9, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1654–L1673`
- **Current card anchor**: `docs/en/ledger/41-50.md:L147–L166`
- **Original title**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only)
- **Original one-sentence judgment**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only).
- **Original reasoning chain**: Copyable, pausable relationships → memory and commitment boundaries diverge → data, exit and liability conflicts grow → institutions define subjects.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, relationship-data and exit disputes do not persist and ordinary contracts suffice.
- **Original leading indicator**: Data disputes, exit clauses, dedicated rules or cases; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-042.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint. Retained as landscape only, with confidence not raised; upgrading requires institutional evidence that disputes persist and ordinary contracts are insufficient.
- **Original external comparison source**: EXT-9, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-048` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-049

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L167–L186`；`docs/en/ledger/41-50.md:L167–L186`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1674–L1693`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L167–L186`
- **原始标题**：AI 协调越丰富，共同承担不可逆承诺越稀缺（仅图景）
- **原始一句话命题**：AI 协调越丰富，共同承担不可逆承诺越稀缺（仅图景）。
- **原始推理链**：协调成本下降 → 候选增加 → 选择不等于承诺，承诺要求承担失败 → 共同承担者稀缺。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年协调增加同步提高共同承担长期失败的比例。
- **原始领先指标**：承诺持续率、退出率、修复时间；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-041, J-038。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：建议供给增长可观察，共同承担不可逆承诺没有可比数据。仍坚持：仅作为图景保留，置信度不上调；升级需要协调增加与共同承担比例之间的可比数据。
- **原始外部对照来源**：EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1674–L1693`
- **Current card anchor**: `docs/en/ledger/41-50.md:L167–L186`
- **Original title**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only)
- **Original one-sentence judgment**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only).
- **Original reasoning chain**: Coordination costs fall → candidates multiply → choosing is not commitment; commitment bears failure → willing groups are scarce.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, more coordination also raises joint bearing of long-term failure and repair is no bottleneck.
- **Original leading indicator**: Commitment retention, exit rate, repair time; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-038.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent. Retained as landscape only, with confidence not raised; upgrading requires comparable data linking increased coordination to the share of jointly borne commitments.
- **Original external comparison source**: EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-049` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-050

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L187–L205`；`docs/en/ledger/41-50.md:L187–L205`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1694–L1713`
- **当前卡锚点**：`docs/zh/ledger/41-50.md:L187–L205`
- **原始标题**：人类协作的价值从共同做步骤转向共同选择承诺（仅图景）
- **原始一句话命题**：人类协作的价值从共同做步骤转向共同选择承诺（仅图景）。
- **原始推理链**：代理吸收协调 → 人类介入减少 → 介入集中于不可逆选择与共同担责 → 以承诺质量衡量协作。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年协作价值仍主要来自共同执行步骤。
- **原始领先指标**：共同确认事件、不可逆决策、兑现率；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-041, J-038。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：仍坚持但证据不足：治理把人类确认保留在关键节点，但不能证明协作价值整体迁移。
- **原始外部对照来源**：EXT-4, EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1694–L1713`
- **Current card anchor**: `docs/en/ledger/41-50.md:L187–L205`
- **Original title**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only)
- **Original one-sentence judgment**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only).
- **Original reasoning chain**: Agents absorb coordination → human intervention shrinks → it concentrates on irreversible choices and joint liability → commitment quality measures collaboration.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, collaboration value remains step execution rather than commitment choice.
- **Original leading indicator**: Human-confirmed commitments, irreversible decisions, fulfillment; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-038.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: governance preserves human confirmation at key points, but does not prove a wholesale shift in collaboration value.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-050` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-051

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L125–L144`；`docs/en/ledger/51-60.md:L125–L144`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1714–L1733`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L125–L144`
- **原始标题**：建议供给丰富不会自动分散真实行动权（仅图景）
- **原始一句话命题**：建议供给丰富不会自动分散真实行动权（仅图景）。
- **原始推理链**：建议廉价生成 → 信息增加 → 许可、资源接入和赔付仍集中 → 建议不等于行动权。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年建议增加同步造成关键入口广泛分散。
- **原始领先指标**：资源集中度、授权主体数、转化分布；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-039, J-040, J-035。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过；十亿量级是受影响人群的构造式上限，不等于十亿个不同个人每周重复执行同一动作；本卡判断的是制度与资源分配安排，因此保留为低置信度仅图景／制度性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：基础设施、责任与资源控制可能集中，但建议丰富与行动权的关系未证实。仍坚持：仅作为图景保留，置信度不上调；升级需要许可、资源接入与赔付这些关键入口分散程度的证据。
- **原始外部对照来源**：EXT-12, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1714–L1733`
- **Current card anchor**: `docs/en/ledger/51-60.md:L125–L144`
- **Original title**: Abundant advice does not automatically disperse real action rights (landscape only)
- **Original one-sentence judgment**: Abundant advice does not automatically disperse real action rights (landscape only).
- **Original reasoning chain**: Advice is cheap → information grows → permissions, resources and compensation remain concentrated → advice does not disperse action rights.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, advice growth coincides with broad dispersion of energy, data, licensing, and compensation access.
- **Original leading indicator**: Resource concentration, authorization holders, advice-to-action distribution; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-039, J-040, J-035.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: Gate 1 fails; the billion-scale figure is an upper bound for affected people, not a count of distinct weekly actors; this card remains a low-confidence landscape/institutional judgment and is no longer a society-wide trend claim; original card text retained, identifier not reused, basis: `Retrospect · Gate 1`).
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence on how dispersed the key gates of licensing, resource access, and compensation actually are.
- **Original external comparison source**: EXT-12, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-051` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-052

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L145–L164`；`docs/en/ledger/51-60.md:L145–L164`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1734–L1753`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L145–L164`
- **原始标题**：能源、现实数据、授权与赔付形成远期制度入口（仅图景）
- **原始一句话命题**：能源、现实数据、授权与赔付形成远期制度入口（仅图景）。
- **原始推理链**：模型扩张 → 控制点迁移到现实输入、许可和损失 → 四类入口被定价 → 控制形成议价位置。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年四类入口不产生持续价格、许可或融资优势。
- **原始领先指标**：能源价差、数据费、审查费、保险准备金；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-039, J-040, J-035。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：仍坚持但证据不足：能源、现实数据、授权与赔付已有现实入口，远期组合仍属推演。
- **原始外部对照来源**：EXT-12, EXT-14, EXT-15（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1734–L1753`
- **Current card anchor**: `docs/en/ledger/51-60.md:L145–L164`
- **Original title**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only)
- **Original one-sentence judgment**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only).
- **Original reasoning chain**: Model supply expands → control migrates to real inputs, permissions and losses → institutions price four access points → control creates bargaining power.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, four access points create no persistent price, licensing, or financing advantage.
- **Original leading indicator**: Energy spreads, data fees, review fees, insurance reserves; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-039, J-040, J-035.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: energy, real-world data, authorization, and compensation have present-day entry points; the long-term combination remains an inference.
- **Original external comparison source**: EXT-12, EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-052` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-053

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L165–L184`；`docs/en/ledger/51-60.md:L165–L184`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1754–L1773`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L165–L184`
- **原始标题**：当可生成物普遍丰富，个人承担过什么可能成为意义信号（仅图景）
- **原始一句话命题**：当可生成物普遍丰富，个人承担过什么可能成为意义信号（仅图景）。
- **原始推理链**：作品、身份和成就可生成 → 输出区分度下降 → 真实时间、身体风险和责任留下成本信号 → 承担成为意义来源。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年真实承担不再影响信任、地位或长期选择。
- **原始领先指标**：长期承诺溢价、经历验证、叙事与结果脱钩；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-042, J-029。
- **原始状态与谱系**：ACTIVE。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：人的主体性与责任有现实依据，但“亲自承担”成为意义信号尚无跨代证据。仍坚持：仅作为图景保留，置信度不上调；升级需要跨代的信任、地位或长期选择数据。
- **原始外部对照来源**：EXT-9, EXT-17（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1754–L1773`
- **Current card anchor**: `docs/en/ledger/51-60.md:L165–L184`
- **Original title**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only)
- **Original one-sentence judgment**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only).
- **Original reasoning chain**: Generatable output loses distinction → real time, bodily risk and responsibility leave cost signals → personal burden becomes meaning/status signal.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, real responsibility no longer affects trust, status, or long-term choices.
- **Original leading indicator**: Trust premium for commitments, experience verification, narrative/outcome coupling; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-042, J-029.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence. Retained as landscape only, with confidence not raised; upgrading requires generational data on trust, status, or long-term choices.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-053` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-054

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L185–L203`；`docs/en/ledger/51-60.md:L185–L203`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1774–L1829`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L185–L203`
- **原始标题**：不可委托的时间、身体风险与长期承诺保持需求侧稀缺（仅图景）
- **原始一句话命题**：不可委托的时间、身体风险与长期承诺保持需求侧稀缺（仅图景）。
- **原始推理链**：即时安慰增加 → 选择增加但生命时间不增加 → 身体风险与长期承诺仍需本人承担 → 稀缺转向不可委托经历。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年代理替代经历后相关偏好与结果无差异。
- **原始领先指标**：经历投入、承诺完成率、身体在场溢价；年度。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-042, J-029。
- **原始状态与谱系**：ACTIVE。
- **原始出处**：`远期图景`。
- **原始外部对照判断**：证据不足的景观：身体、照护与现实风险仍是治理对象，但 2033–2040 的需求侧稀缺未证实。仍坚持：仅作为图景保留，置信度不上调；升级需要代理替代经历之后偏好与结果差异的研究。
- **原始外部对照来源**：EXT-9, EXT-10（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1774–L1879`
- **Current card anchor**: `docs/en/ledger/51-60.md:L185–L203`
- **Original title**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only)
- **Original one-sentence judgment**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only).
- **Original reasoning chain**: Choice grows but lifetime does not → bodily risk and long commitments remain personal → scarcity moves to non-delegable experience.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, agent substitution leaves no observable difference in preferences or outcomes around time and risk.
- **Original leading indicator**: Non-delegable time, long-commitment completion, embodied premium; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-042, J-029.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven. Retained as landscape only, with confidence not raised; upgrading requires studies on differences in preferences and outcomes after delegated experience substitutes for direct experience.
- **Original external comparison source**: EXT-9, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-054` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-055

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L5–L24`；`docs/en/ledger/51-60.md:L5–L24`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1359–L1377`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L5–L24`
- **原始标题**：高责任任务中的现实信号以合同资产形式获得溢价
- **原始一句话命题**：在高责任任务中，带来源、许可、校准与责任链的现实信号比数据文件本身更可能获得结构性溢价。
- **原始推理链**：C1 使二手表达和合成样本丰富 → 普通数据文件的边际价格下降 → 高责任任务仍需要现实观测、来源证明和可追索主体 → 采集许可、校准、使用边界与赔付义务被写入合同 → 数据从文件变成带责任链的合同资产。
- **原始时间窗**：2029–2033。
- **原始证伪条件**：到 2033 年，在多个高责任领域，合成证据被监管、保险与买方普遍接受，事故率不高于现实信号，且来源、校准与责任链不再带来可观察溢价。
- **原始领先指标**：高责任审批中合成证据的占比、带来源与校准条款的数据合同溢价、现实试验预算占比、数据责任保险费率；每半年观察。
- **原始置信度**：中。
- **原始 depends-on**：J-005, J-033, J-034, J-039。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C2：现实信号如何变成合同资产`。
- **原始外部对照判断**：与“数据治理、来源和可信度更重要”的方向一致，但本项目把范围收窄到高责任任务；现实信号是否形成独立溢价仍未证实。仍坚持：高责任任务需要现实观测、来源证明与可追索主体，这三者不能由重组生成；独立溢价未被证实，因此置信度保持「中」。
- **原始外部对照来源**：EXT-7, EXT-10, EXT-14（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1359–L1377`
- **Current card anchor**: `docs/en/ledger/51-60.md:L5–L24`
- **Original title**: Real-world signals earn a premium as contract assets in high-liability tasks
- **Original one-sentence judgment**: In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium.
- **Original reasoning chain**: C1 makes second-hand expression and synthetic samples abundant → ordinary data files lose marginal price → high-liability tasks still require real observations, provenance, and an accountable party → collection permission, calibration, usage boundaries, and compensation duties enter contracts → data becomes a contract asset with a liability chain.
- **Original time window**: 2029–2033.
- **Original falsifier**: By 2033, across multiple high-liability fields, regulators, insurers, and buyers broadly accept synthetic evidence with no worse incident rate than real signals, while provenance, calibration, and liability chains carry no observable premium.
- **Original leading indicator**: Synthetic-evidence share in high-liability approvals, premium for data contracts with provenance and calibration clauses, real-trial budget share, and data-liability insurance rates; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-033, J-034, J-039.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C2: How Real-World Signals Become Contract Assets`.
- **Original external comparison**: Directionally consistent with stronger data governance, provenance, and trust, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven. Retained: high-liability tasks require real observation, provenance, and a recourse-bearing subject, none of which recombination can produce; the independent premium is unproven, so confidence stays Medium.
- **Original external comparison source**: EXT-7, EXT-10, EXT-14 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-055` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-056

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L25–L44`；`docs/en/ledger/51-60.md:L25–L44`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1378–L1396`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L25–L44`
- **原始标题**：算力扩张的绑定约束从芯片供给迁移到电力交付与并网许可
- **原始一句话命题**：算力扩张的绑定约束在本窗口内从芯片供给迁移到电力交付与并网许可。
- **原始推理链**：芯片是可量产、可运输、可全球再分配的工业品，扩产弹性随投资上升 → 变压器、高压设备与线路受重型制造与施工周期约束，几乎不能靠增加订单提速，且不可跨区域调剂 → 并网、环评与用地许可的周期由行政流程与地方政治决定，与技术进步解耦 → 三条供给曲线的斜率相差一个量级 → 资本集中涌入时，先耗尽的是许可与并网队列，而不是晶圆。
- **原始时间窗**：2026–2031。
- **原始证伪条件**：到 2031 年，主要市场新建算力项目的上线延迟中，归因于芯片交付的仍多于归因于电力交付与并网许可的；或主要市场的大负荷接入平均等待时长较 2026 年下降。
- **原始领先指标**：大负荷接入与并网排队时长、变压器与高压开关设备交货期、项目宣布到通电的平均时长、电力合同签约早于硬件订单的比例；每半年。
- **原始置信度**：中。
- **原始 depends-on**：J-001, J-027。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：与“AI 用电增长构成现实约束”的方向一致；本项目的主张更窄也更可证伪——绑定约束是交付与许可的**时序**，不是发电总量。外部对照本轮只取得发电侧排队证据（EXT-19 明确不覆盖负荷侧），负荷侧排队数据未取得，因此一致性只到机制层。我为何仍坚持：负荷侧统计虽缺，机制的两条腿已分别被佐证——DOE 记录超大规模设施（300–1000MW+）的接入前置期为 1–3 年，并因此转向与现有电厂共址以更快取电（EXT-29）；ERCOT 的大负荷排队积压持续扩大，是唯一公开的负荷侧 ISO 级数据（EXT-30）。置信度维持「中」不上调，因为跨市场的负荷侧排队统计仍不存在。
- **原始外部对照来源**：EXT-12, EXT-19, EXT-29, EXT-30（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1378–L1396`
- **Current card anchor**: `docs/en/ledger/51-60.md:L25–L44`
- **Original title**: The binding constraint on compute expansion moves from chip supply to power delivery and interconnection permits
- **Original one-sentence judgment**: Within this window the binding constraint on compute expansion moves from chip supply to power delivery and interconnection permitting.
- **Original reasoning chain**: Chips are a mass-produced, shippable, globally reallocatable industrial good whose expansion elasticity rises with investment → transformers, high-voltage equipment, and lines are bound by heavy-manufacturing and construction cycles, can barely be accelerated by more orders, and cannot be reallocated across regions → interconnection, environmental, and land permits run on administrative and local-political cycles decoupled from technical progress → the three supply curves differ in slope by an order of magnitude → when capital concentrates, permits and interconnection queues are exhausted before wafers.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, among delays to new compute projects in major markets, those attributable to chip delivery still outnumber those attributable to power delivery and interconnection permitting; or average large-load interconnection wait times in major markets fall below their 2026 level.
- **Original leading indicator**: Large-load interconnection queue times, transformer and high-voltage switchgear lead times, average time from project announcement to energization, share of deals where power contracts are signed before hardware orders; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-027.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: Directionally consistent with "AI electricity growth is a real constraint," but this project's claim is narrower and more falsifiable — the binding constraint is the **timing** of delivery and permitting, not total generation. The comparison obtained this round covers generation-side queues only (EXT-19 explicitly excludes load-side queues), so the agreement holds at the mechanism level only. Why the judgment is retained: load-side statistics are still missing, but both legs of the mechanism are separately corroborated — DOE records connection lead times of 1–3 years for hyperscale facilities of 300–1000 MW+ and the resulting shift toward co-location with existing generation to get power faster (EXT-29), and ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30). Confidence stays at Medium rather than rising, because cross-market load-side queue statistics still do not exist.
- **Original external comparison source**: EXT-12, EXT-19, EXT-29, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-056` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-057

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L45–L64`；`docs/en/ledger/51-60.md:L45–L64`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1397–L1415`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L45–L64`
- **原始标题**：被定价的不是电量而是可交付时间的确定性
- **原始一句话命题**：在算力的电力交易中，被定价的主要不是电量，而是“在承诺日期一定通电”的确定性。
- **原始推理链**：J-056 使队列成为绑定约束 → 模型代际窗口短，晚十八个月投产的容量在竞争上大幅贬值 → 买方对投产日期的支付意愿高于对平均电价的支付意愿 → 合同结构长出容量预留费、投产日期担保、延迟赔偿与自备发电、储能过桥条款 → 同一地区“带许可、带并网”的场址与裸地形成远超土建成本的价差。
- **原始时间窗**：2027–2032。
- **原始证伪条件**：到 2032 年，大型算力电力合同的价格差异主要由每度电价格解释，而与交付日期担保相关的条款（容量预留费、提前期溢价、延迟赔偿）未成为普遍条款。
- **原始领先指标**：电力与容量合同中出现投产日期担保与延迟赔偿的比例、同一地区带许可场址与裸地的成交价差、自备发电与储能作为过桥方案的采用率；每半年。
- **原始置信度**：中。
- **原始 depends-on**：J-056。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**部分一致，但一致点不落在本卡的主张上。** 一致：监管核准的大负荷合同确实围绕「承诺与期限」而非每度电价格分层——FERC 要求 PJM 为共址负荷设立按容量承诺等级区分的三档服务（EXT-21）；PUCO 核准的 AEP Ohio 关税以 85% 最低付费、12 年期、4 年爬坡、退出费与财务担保构成价格保护（EXT-22）。**分歧**：这些条款保护的是**供方**不被弃单套牢，而本卡主张的是**买方**为「按期通电」付溢价；两者都指向「时间与承诺被定价」，但方向相反，不能互相替代。**证据边界**：本卡的证伪条件要求比较合同条款的普遍性，而大负荷合同的商业条款几乎全部保密，公开统计不存在——该证伪条件目前**不可计算**。我为何仍坚持：机制方向获得两个司法辖区的独立支持，判断保留，置信度维持「中」不上调；同时把领先指标的重心从「合同条款比例」移到可公开查证的代理——监管备案中最低付费与退出费条款的出现数量，以及同一地区带许可场址与裸地的成交价差。
- **原始外部对照来源**：EXT-21, EXT-22（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1397–L1415`
- **Current card anchor**: `docs/en/ledger/51-60.md:L45–L64`
- **Original title**: What gets priced is not energy but certainty of delivery date
- **Original one-sentence judgment**: In compute-related power transactions, what is mainly priced is not energy but the certainty of being live on the promised date.
- **Original reasoning chain**: J-056 makes the queue the binding constraint → model generations turn over quickly, so capacity that arrives eighteen months late loses much of its competitive value → willingness to pay for an in-service date exceeds willingness to pay for a lower average tariff → contracts grow capacity reservation fees, in-service date guarantees, delay damages, and on-site generation or storage as a bridge → within one region, permitted and interconnected sites trade above bare land by far more than construction cost.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, price differences in large compute power contracts are mainly explained by per-kilowatt-hour price, and terms tied to delivery-date guarantees (reservation fees, lead-time premiums, delay damages) have not become common.
- **Original leading indicator**: Share of power and capacity contracts carrying in-service date guarantees and delay damages; price gap between permitted sites and bare land in the same region; adoption of on-site generation and storage as bridging; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Partly consistent, but the agreement does not sit where this card lands.** Agreement: regulator-approved large-load contracts are indeed tiered by commitment and term rather than by per-kilowatt-hour price — FERC directed PJM to create three tiers of co-located load service distinguished by capacity commitment (EXT-21), and the AEP Ohio tariff approved by PUCO builds its price protection from an 85% minimum take, a 12-year term, a 4-year ramp, exit fees and collateral (EXT-22). **Divergence**: those terms protect the **seller** against being stranded, whereas this card claims the **buyer** pays a premium for energization on date; both point at time and commitment being priced, but from opposite sides, and one does not substitute for the other. **Evidence boundary**: this card's falsifier asks how common such contract terms are, and commercial terms in large-load contracts are almost entirely confidential, so no public statistics exist and the falsifier is currently **not computable**. Why the judgment is retained: the direction of the mechanism has independent support in two jurisdictions, so the judgment stands with confidence at Medium rather than rising; and the leading indicator shifts from "share of contracts" to a publicly checkable proxy — the count of minimum-take and exit-fee provisions appearing in regulatory filings, and the price gap between permitted and raw sites in the same region.
- **Original external comparison source**: EXT-21, EXT-22 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-057` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-058

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L65–L84`；`docs/en/ledger/51-60.md:L65–L84`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1416–L1434`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L65–L84`
- **原始标题**：AI 负荷分裂为延迟敏感与可调度两类，可调度部分成为电网的灵活性资源
- **原始一句话命题**：AI 负荷分裂为延迟敏感与可调度两类，可调度的那部分成为电网可付费购买的灵活性资源，而不只是负担。
- **原始推理链**：交互式推理延迟敏感、不可中断、不可迁移 → 训练、批量推理与评估可暂停、可延后、可跨时区迁移 → 后者的中断成本主要是时间而非报废，与电解铝等传统重工业负荷性质不同 → 电网最缺的是灵活性，且需求响应、可中断电价与容量市场是现成的付费通道 → 可调度算力同时是负荷与资源，其真实电力成本可低于名义电价。
- **原始时间窗**：2027–2033。
- **原始证伪条件**：到 2033 年，主要市场数据中心在可中断／需求响应合同中的签约容量仍可忽略（不足其签约容量的 5%），且大型算力用户普遍拒绝可中断条款。
- **原始领先指标**：数据中心参与需求响应的签约容量与占比、可中断电价合同比例、跨区域调度训练作业的公开实践、容量市场中数据中心的报价；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-056, J-018。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**机制一致，规模未知。** 一致：可调度性已从推断变为实测——EPRI DCFlex 在 Phoenix 的现场示范中，一个 AI 计算集群在 3 小时电网高峰事件里削减 25% 用电功率且未影响核心服务（EXT-24）；杜克 Nicholas Institute 的建模给出规模上限，若新增大负荷接受年 0.25%–1.0% 的限时削减，全美 22 个最大平衡区可多容纳近 100GW（EXT-23）。**分歧与证据边界**：这两者都是**潜力**而非**签约**。本卡的证伪条件以「签约容量是否不足 5%」为准，而 PJM 已出清的约 8,064.7 MW 需求响应容量（EXT-25）与 ERCOT 的灵活负荷估计均不按行业拆分，数据中心专项的签约容量没有任何权威机构公布——该证伪条件目前**不可计算**。我为何仍坚持：机制侧证据比提出时更强（推断变实测），判断保留、置信度维持「中」；并补一条领先指标——PJM 或 ERCOT 是否开始按行业披露数据中心的需求响应注册容量，这是本卡重新可证伪的前置条件。
- **原始外部对照来源**：EXT-23, EXT-24, EXT-25, EXT-30（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1416–L1434`
- **Current card anchor**: `docs/en/ledger/51-60.md:L65–L84`
- **Original title**: AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a grid flexibility resource
- **Original one-sentence judgment**: AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a flexibility resource the grid pays for rather than merely a burden.
- **Original reasoning chain**: Interactive inference is latency-sensitive, non-interruptible, and immobile → training, batch inference, and evaluation can be paused, deferred, and moved across time zones → for the latter the cost of interruption is time rather than spoilage, unlike aluminium smelting and similar heavy industrial load → what grids are shortest of is flexibility, and demand response, interruptible tariffs, and capacity markets are existing payment channels → schedulable compute is load and resource at once, and its real power cost can sit below its nominal tariff.
- **Original time window**: 2027–2033.
- **Original falsifier**: By 2033, contracted data-centre capacity in interruptible or demand-response programs in major markets remains negligible (under 5% of their contracted capacity) and large compute users broadly refuse interruptibility terms.
- **Original leading indicator**: Contracted data-centre demand-response capacity and its share, share of interruptible tariff contracts, public practice of cross-region scheduling of training jobs, data-centre bids in capacity markets; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056, J-018.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, scale unknown.** Agreement: schedulability has moved from inference to measurement — in EPRI's DCFlex demonstration in Phoenix an AI compute cluster cut 25% of its power through a three-hour grid peak without affecting core services (EXT-24), and Duke's Nicholas Institute puts an upper bound on the scale: if new large loads accept 0.25–1.0% annual curtailment, the 22 largest US balancing areas could host nearly 100 GW more load (EXT-23). **Divergence and evidence boundary**: both are **potential**, not **contracted**. This card's falsifier turns on whether contracted interruptible capacity stays below 5%, yet neither PJM's roughly 8,064.7 MW of cleared demand-response capacity (EXT-25) nor ERCOT's flexible-load estimates are broken out by industry, and no authority publishes data-centre-specific contracted capacity — so the falsifier is currently **not computable**. Why the judgment is retained: the mechanism side is better evidenced than when the card was written (inference became measurement), so the judgment stands with confidence at Medium; and one leading indicator is added — whether PJM or ERCOT begins disclosing data-centre demand-response registrations by industry, which is the precondition for this card becoming falsifiable again.
- **Original external comparison source**: EXT-23, EXT-24, EXT-25, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-058` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-059

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L85–L104`；`docs/en/ledger/51-60.md:L85–L104`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1435–L1453`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L85–L104`
- **原始标题**：算力管制的抓手从硬件出口转向使用侧
- **原始一句话命题**：当租用架构使能力越境而硬件不动，算力管制的抓手会从硬件出口转向使用侧的主体、用途与场址授权。
- **原始推理链**：芯片离散、可点数、跨境须过关，因而是理想的管制对象 → 租用算力使能力扩散而硬件不移动（J-027）→ 只管“谁拥有”无法约束“谁在用” → 管制者要么接受管制失效，要么把义务移到使用侧：主体实名与用途申报、远程访问限制、模型权重转移规则、场址与运营方认证 → 管制对象从物转向主体与合同。
- **原始时间窗**：2026–2031。
- **原始证伪条件**：到 2031 年，主要管制体系仍只锚定硬件与实体清单，对模型权重转移、远程访问或数据中心运营方认证没有可执行义务，也没有执行案例。
- **原始领先指标**：管制文本中关于权重、远程访问、云服务与数据中心认证的条款及其修订；算力提供方的实名与用途申报要求；跨境算力合同中的合规条款；执法与处罚案例；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-001, J-027。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**部分一致，且有一处明确分歧。** 一致：管制确已越出“芯片实体”，扩展到最先进闭源模型权重与数据中心运营方授权（EXT-20）。分歧：本项目独立推演预期抓手主要落在账户与远程访问许可，而已观察到的落点是权重门槛与场址／运营方认证，并不存在独立的云访问许可制度。我为何仍坚持：机制（租用架空实体管制 → 义务向主体与合同迁移）与观察到的落点方向一致，差别在接口而非方向；因此把可证伪部分收窄为“是否出现可执行的使用侧义务与执行案例”，而不是“是否出现云访问许可证”。
- **原始外部对照来源**：EXT-20（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1435–L1453`
- **Current card anchor**: `docs/en/ledger/51-60.md:L85–L104`
- **Original title**: The handle of compute control moves from hardware export to the use side
- **Original one-sentence judgment**: Once rental architectures let capability cross borders while hardware stays put, the handle of compute control moves from hardware export to use-side control of parties, purposes, and site authorization.
- **Original reasoning chain**: Chips are discrete, countable, traceable, and must clear customs, making them an ideal control object → rented compute diffuses capability while hardware does not move (J-027) → governing "who owns" cannot constrain "who uses" → a regulator either accepts failed control or moves duties to the use side: identity and purpose declaration, remote-access restrictions, model-weight transfer rules, site and operator authorization → the object of control shifts from things to parties and contracts.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, major control regimes remain anchored only in hardware and entity lists, with no enforceable duties on weight transfer, remote access, or data-centre operator authorization, and no enforcement cases.
- **Original leading indicator**: Provisions and revisions covering weights, remote access, cloud services, and data-centre authorization; identity and purpose-declaration requirements imposed on compute providers; compliance clauses in cross-border compute contracts; enforcement and penalty cases; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-027.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Partly consistent, with one explicit divergence.** Agreement: control has already moved beyond the chip as a physical object, reaching the most advanced closed model weights and data-centre operator authorization (EXT-20). Divergence: this project's independent reasoning expected the handle to land mainly on accounts and remote-access licensing, whereas the observed landing point is weight thresholds plus site and operator authorization, with no standalone cloud-access licensing regime. Why the judgment is retained: the mechanism (rental hollows out entity control → duties migrate to parties and contracts) matches the observed direction, and the difference is the interface rather than the direction; the falsifiable part is therefore narrowed to "do enforceable use-side duties and enforcement cases appear," not "does a cloud-access licence appear."
- **Original external comparison source**: EXT-20 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-059` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-060

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L105–L124`；`docs/en/ledger/51-60.md:L105–L124`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1454–L1472`
- **当前卡锚点**：`docs/zh/ledger/51-60.md:L105–L124`
- **原始标题**：能源富余国以场址换算力，获得租金而非能力主权（仅图景）
- **原始一句话命题**：能源富余、审批快的东道国以场址与电力换取算力投资，获得的是租金、就业与税收，而不是对能力本身的处置权（仅图景）。
- **原始推理链**：电力与场址不可搬运，芯片可搬运但受出口管制，模型权重可瞬时迁移 → 三类要素的地理与管辖权分离 → 东道国能提供的恰是最不可移动的一项 → 其手中的筹码（断电、征用）是一次性且代价极高的手段 → 议价所得表现为租金与就业，而非能力主权。
- **原始时间窗**：2028–2035。
- **原始证伪条件**：到 2035 年，东道国普遍在跨境算力合同中取得权重托管、本地使用配额或独立审计权；或主要新增算力仍集中在同时拥有芯片供应与管辖权的国家，跨境“主权算力场址”未形成可观察的合同类别。
- **原始领先指标**：跨境数据中心投资中东道国取得的条款（本地使用配额、权重托管、审计权）、以能源补贴换算力配额的安排、按国别的算力上限与认证制度；每年。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-056, J-059。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：部分与已观察到的制度一致——按国别的算力分配上限与数据中心运营方认证已经存在（EXT-20），弗吉尼亚 JLARC 审计也显示，即使在数据中心位于本地的情况下，东道辖区实际留住的价值仍然很少（EXT-28）。但本卡关于东道国长期议价地位的推论证据不足，我为何仍坚持：仅作图景保留，置信度不上调；升级需要跨境合同条款的可核查证据，包括权重托管、本地使用配额或独立审计权。
- **原始外部对照来源**：EXT-20, EXT-28（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1454–L1472`
- **Current card anchor**: `docs/en/ledger/51-60.md:L105–L124`
- **Original title**: Energy-rich hosts trade sites for compute and gain rent rather than capability sovereignty (landscape only)
- **Original one-sentence judgment**: Host states with surplus energy and fast permitting trade sites and power for compute investment and obtain rent, employment, and tax revenue rather than any right of disposal over the capability itself (landscape only).
- **Original reasoning chain**: Power and sites cannot be moved, chips can be moved but are export-controlled, and model weights move instantly → the three factors separate geographically and jurisdictionally → what a host state supplies is precisely the least movable factor → its leverage (cutting power, expropriation) is one-shot and extremely costly → what it gains shows up as rent and employment, not capability sovereignty.
- **Original time window**: 2028–2035.
- **Original falsifier**: By 2035, host states broadly obtain weight escrow, local usage quotas, or independent audit rights in cross-border compute contracts; or most new compute remains concentrated in states that hold both chip supply and jurisdiction, with no observable contract class for cross-border "sovereign compute sites."
- **Original leading indicator**: Terms obtained by host states in cross-border data-centre investment (local usage quotas, weight escrow, audit rights); arrangements trading energy subsidies for compute quotas; country-level compute caps and authorization regimes; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-056, J-059.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: Partly consistent with observed institutions — country-level compute allocation caps and data-centre operator authorization already exist (EXT-20), and Virginia's JLARC audit shows how little of the value a host jurisdiction retains even inside its own borders (EXT-28). But the inference about host states' long-run bargaining position lacks evidence. Why the judgment is retained: it is kept as landscape only and confidence is not raised; upgrading it requires verifiable evidence from cross-border contract terms — weight escrow, local usage quotas, or independent audit rights.
- **Original external comparison source**: EXT-20, EXT-28 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-060` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-061

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L25–L44`；`docs/en/ledger/61-70.md:L25–L44`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1473–L1491`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L25–L44`
- **原始标题**：数据中心的本地外部性显性化，社会许可成为选址的真实约束
- **原始一句话命题**：数据中心的本地外部性显性化，社会许可从隐性前提变成选址的真实成本项。
- **原始推理链**：数据中心投资巨大但就业稀少，用电与用水显著 → 成本落在本地，收益集中在外部股东 → 可见性不对称：居民每月看到电费账单，看不到 AI 收益 → 按损失厌恶，本地政治会做出反应：暂停令、超大用户专用费率、用水限制、以税收与就业为条件的协议 → 选址成本中出现过去几乎不计价的社会许可项。
- **原始时间窗**：2026–2031。
- **原始证伪条件**：到 2031 年，主要市场几乎没有出现针对数据中心的地方暂停令、超大负荷专用费率或用水限制，且居民电价争议没有形成政策后果。
- **原始领先指标**：地方暂停或否决案例数、超大负荷专用费率条款的出台、用水许可条件、以就业与税收换电力的协议条款；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-056。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**一致，且其中一半已提前落地。** 一致：本卡预期的「大负荷专属费率」不是远期图景而是已发生的制度事实——PUCO 于 2025 年 7 月核准 AEP Ohio 的数据中心专属关税，明确以隔离居民费率为目的（EXT-22）；佐治亚 PSC 于 2025 年 1 月对 100MW 以上负荷确立按项目风险定价的最低账单规则（EXT-32）。两个司法辖区独立做出同方向选择，早于本卡 2031 年的窗口。**分歧与证据边界**：另一半缺证据——没有任何政府或学术机构对地方暂停令与选址被拒案例做全国系统统计，现存追踪器为商业／众包性质且方法论不透明；水资源冲突目前只有个案诉讼（佐治亚居民指控数据中心损害水源，尚未判决），不构成规律。我为何仍坚持：判断保留、置信度维持「中」不上调——上调需要暂停令的系统计数，而不是更多个案；同时明确本卡的证伪条件应先按「专属费率」这一有证据的半边检验，暂停令与用水限制在统计口径出现前只能作为边界证据。
- **原始外部对照来源**：EXT-22, EXT-32（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1473–L1491`
- **Current card anchor**: `docs/en/ledger/61-70.md:L25–L44`
- **Original title**: Local externalities of data centres become explicit and social licence becomes a real siting constraint
- **Original one-sentence judgment**: The local externalities of data centres become explicit, turning social licence from an implicit premise into a real cost line in siting.
- **Original reasoning chain**: Data centres are very large investments with few jobs and conspicuous power and water use → costs land locally while returns accrue to external shareholders → visibility is asymmetric: residents see a monthly electricity bill and never see the AI revenue → under loss aversion, local politics responds with moratoria, special tariff classes for very large customers, water restrictions, and agreements conditioned on tax and employment → siting costs acquire a line item that was previously priced at roughly zero.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, major markets show almost no local moratoria, large-load tariff classes, or water restrictions aimed at data centres, and residential power-price disputes produce no policy consequences.
- **Original leading indicator**: Count of local moratoria or rejections, introduction of large-load tariff classes, water-permit conditions, terms trading employment and tax for power; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Consistent, and half of it has already happened early.** Agreement: the dedicated large-load tariff this card expected is not a future landscape but an accomplished institutional fact — PUCO approved AEP Ohio's data-centre-specific tariff in July 2025 with the explicit purpose of shielding residential ratepayers (EXT-22), and the Georgia PSC established risk-priced minimum-billing rules for loads above 100 MW in January 2025 (EXT-32). Two jurisdictions moved the same way independently, ahead of this card's 2031 window. **Divergence and evidence boundary**: the other half lacks evidence — no government or academic body systematically counts local moratoria or rejected siting applications, and the trackers that exist are commercial or crowdsourced with opaque methodology; water conflicts so far exist as individual undecided lawsuits (Georgia residents alleging harm to their water), not as an established pattern. Why the judgment is retained: kept with confidence at Medium rather than raised — raising it needs a systematic count of moratoria, not more anecdotes; and this card's falsifier should first be evaluated on the tariff half, where evidence exists, with moratoria and water restrictions treated as boundary evidence until a counting standard appears.
- **Original external comparison source**: EXT-22, EXT-32 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-061` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-062

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L45–L64`；`docs/en/ledger/61-70.md:L45–L64`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1492–L1510`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L45–L64`
- **原始标题**：重资产可课税而价值层可迁移，地方获得的份额结构性偏低（仅图景）
- **原始一句话命题**：能被课税的是不可移动的重资产，能创造利润的是可瞬时迁移的价值层，地方获得的份额因此结构性偏低（仅图景）。
- **原始推理链**：课税需要管辖区内可见且不可移动的存在 → 数据中心不可移动，而利润与模型权重可移动 → 地方能抓住电价、地税与少量就业，抓不住利润 → 地方不断提高对重资产的要求，企业以选址竞争对冲 → 形成“重资产纳税、价值层避税”的结构性错配。
- **原始时间窗**：2028–2035。
- **原始证伪条件**：到 2035 年，主要市场对算力服务的征税从资产端转向使用端（如覆盖 AI 服务的使用税或目的地征税普遍落地），使地方税基与其承担的负荷规模相称。
- **原始领先指标**：数据中心税收优惠的撤回或条件化、以电力消费为基数的地方费、AI 服务征税的立法进程、地方与企业的收益分享条款；每年。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-061, J-039。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**机制一致，但只被证到一半。** 一致：弗吉尼亚 JLARC 对全美最大数据中心市场的官方审计量化了本卡的第一步——销售与使用税豁免使州级每年放弃约 9.28 亿美元（FY23）而约 90% 行业适用，地方留存以财产税为主，经济影响中的岗位大量集中在建设期而非永久运营（EXT-28）；跨州层面，36 个州设有数据中心专项优惠而仅 11 州披露受益企业，被追踪超巨额交易的每岗位补贴成本平均超 26.2 万美元（EXT-31，⚠ 倡导型机构，非全样本）。**分歧与证据边界**：被证到的只是「重资产可课税且地方留存偏低」，本卡的另一半——利润与模型权重可移动使价值层逃逸——没有任何政府或跨州研究直接处理；本卡的证伪条件指向「征税是否从资产端转向使用端」，而针对云与 AI 服务的目的地征税至今只有各州零散税务裁定，不存在系统研究。我为何仍坚持：仅作图景保留，置信度不上调；升级为可下注判断需要两样东西——地方留存收入与其承担负荷规模的对照口径，以及使用端征税的立法进展。
- **原始外部对照来源**：EXT-28, EXT-31（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1492–L1510`
- **Current card anchor**: `docs/en/ledger/61-70.md:L45–L64`
- **Original title**: Heavy assets are taxable while the value layer is mobile, so local shares stay structurally low (landscape only)
- **Original one-sentence judgment**: What can be taxed is the immovable heavy asset while what earns the profit is the instantly mobile value layer, so the share captured locally stays structurally low (landscape only).
- **Original reasoning chain**: Taxation requires a visible, immovable presence inside the jurisdiction → data centres are immovable while profit and model weights are mobile → localities can reach power prices, property tax, and a little employment, but not profit → localities keep raising demands on the heavy asset while firms hedge through siting competition → a structural mismatch forms between the taxed asset and the untaxed value layer.
- **Original time window**: 2028–2035.
- **Original falsifier**: By 2035, taxation of compute services in major markets shifts from the asset side to the use side (for example broadly adopted usage or destination-based taxes covering AI services), giving localities a tax base commensurate with the load they carry.
- **Original leading indicator**: Withdrawal or conditioning of data-centre tax abatements, local levies based on electricity consumption, legislative progress on taxing AI services, revenue-sharing terms between localities and firms; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-061, J-039.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, but only half of it.** Agreement: Virginia's JLARC audit of the largest US data-centre market quantifies this card's first step — the sales and use tax exemption forgoes roughly $928 million of state revenue a year (FY23) with about 90% of the industry claiming it, local retention rests mainly on property tax, and the jobs in the economic-impact figures are heavily concentrated in the construction phase rather than permanent operations (EXT-28). Across states, 36 offer data-centre-specific tax breaks while only 11 disclose which companies receive them, and subsidy per job in tracked megadeals averages over $262,000 (EXT-31 — ⚠ advocacy organization, not a full sample). **Divergence and evidence boundary**: what is evidenced is only that heavy assets are taxable and the local share is low; the other half — profits and model weights being mobile so the value layer escapes — is addressed by no government or cross-state study, and this card's falsifier points at whether taxation shifts from the asset side to the usage side, where cloud and AI services are covered only by scattered state tax rulings with no systematic research. Why the judgment is retained: kept as landscape only, confidence not raised; upgrading it to a bettable judgment needs two things — a comparable measure of local retained revenue against the load borne, and legislative movement on usage-side taxation.
- **Original external comparison source**: EXT-28, EXT-31 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-062` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-063

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L65–L84`；`docs/en/ledger/61-70.md:L65–L84`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1511–L1529`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L65–L84`
- **原始标题**：算力的地理分布由并网排队与审批速度决定，而不是由电价决定
- **原始一句话命题**：在电网扩容完成之前，算力的地理分布主要由接入排队与审批速度解释，而不是由电价解释。
- **原始推理链**：新建发电与输电的周期以年计，短期内不可压缩 → 谁有现成的冗余变电容量与快审批，谁先拿到算力投资 → 队列位置的价值高于电价差（J-057）→ 电价高但排队短的地区可能胜过电价低但排队长的地区 → 新增容量的地理分布与“最便宜的电”不一致。
- **原始时间窗**：2026–2030。
- **原始证伪条件**：到 2030 年，新增算力容量的地区分布与地区电价的相关性强于与接入等待时长的相关性。
- **原始领先指标**：新增容量按地区分布，与各地区排队时长、电价的对照；企业公开的选址理由；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-056, J-057。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**机制一致，比较口径缺失，并含一处必须更正的来源误用。** 一致：DOE 记录超大规模设施（300–1000MW+）的接入前置期为 1–3 年，并因此转向与现有电厂共址以更快取电，这正是本卡「接入速度而非电价决定落点」的机制（EXT-29）；ERCOT 的大负荷排队积压持续扩大，是唯一公开的负荷侧 ISO 级数据（EXT-30）；弗吉尼亚 JLARC 记录了北弗吉尼亚这一全美最大集群因变电与输电容量受限而出现开发受阻（EXT-28）。**更正**：EXT-19（LBNL *Queued Up*）只覆盖发电与储能并网，**不覆盖负荷侧**，不得用作数据中心选址证据——这是本领域最易发生的来源误用，已在来源索引中标注。**证据边界**：本卡的证伪条件要求比较「地区电价」与「接入等待时长」对新增容量分布的解释力，而没有任何机构发布过这类定量对照，公开数据无法计算该检验。我为何仍坚持：机制侧证据一致且来自官方文件，判断保留、置信度维持「中」；补一条领先指标——ERCOT 式的负荷侧排队披露是否扩散到 PJM、MISO 等市场，这决定本卡何时重新可证伪。
- **原始外部对照来源**：EXT-28, EXT-29, EXT-30（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1511–L1529`
- **Current card anchor**: `docs/en/ledger/61-70.md:L65–L84`
- **Original title**: The geography of compute is decided by interconnection queues and permitting speed, not by electricity price
- **Original one-sentence judgment**: Until grid expansion catches up, the geography of compute is explained mainly by interconnection queues and permitting speed rather than by electricity price.
- **Original reasoning chain**: New generation and transmission run in years and cannot be compressed in the short term → whoever has existing spare substation capacity and fast approvals receives compute investment first → the value of queue position exceeds the tariff differential (J-057) → a region with higher power prices but a short queue can beat a region with cheap power and a long queue → the geographic distribution of new capacity diverges from the cheapest power.
- **Original time window**: 2026–2030.
- **Original falsifier**: By 2030, the regional distribution of new compute capacity correlates more strongly with regional electricity prices than with interconnection wait times.
- **Original leading indicator**: Regional distribution of new capacity compared against regional queue times and tariffs; publicly stated siting rationales; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056, J-057.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, the comparison is unavailable, and one source misuse must be corrected.** Agreement: DOE records connection lead times of 1–3 years for hyperscale facilities (300–1000 MW+) and the resulting shift toward co-location with existing generation to get power faster — exactly this card's mechanism that access speed rather than price decides where compute lands (EXT-29); ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30); and Virginia's JLARC records development constrained by substation and transmission capacity in Northern Virginia, the largest US cluster (EXT-28). **Correction**: EXT-19 (LBNL *Queued Up*) covers generation and storage interconnection only and **does not cover load**, so it must not be used as evidence about data-centre siting — this is the most common source misuse in this area and is now flagged in the source index. **Evidence boundary**: this card's falsifier asks which better explains the regional distribution of new capacity, local electricity price or interconnection wait time, and no institution has published such a quantitative comparison, so the test cannot be computed from public data. Why the judgment is retained: the mechanism-side evidence is consistent and comes from official documents, so the judgment stands with confidence at Medium; one leading indicator is added — whether ERCOT-style load-side queue disclosure spreads to PJM, MISO and other markets, which determines when this card becomes falsifiable again.
- **Original external comparison source**: EXT-28, EXT-29, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-063` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-064

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L85–L104`；`docs/en/ledger/61-70.md:L85–L104`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1530–L1553`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L85–L104`
- **原始标题**：若能效增速持续高于负荷增速，这条链的约束将在远期解除（仅图景）
- **原始一句话命题**：若单位服务能耗的下降速度持续高于负荷增长速度，且可调度负荷能大范围跨区迁移，本链的电力与许可约束会在远期自行解除（仅图景）。
- **原始推理链**：本链的约束成立依赖“负荷增速高于电网可交付容量增速” → 若能效提升与跨区调度同时生效，峰值负荷增长被削平 → 队列不再是绑定约束 → 确定性溢价与场址租金随之消失。
- **原始时间窗**：2033–2040。
- **原始证伪条件**：到 2040 年，主要市场算力相关负荷的增速仍持续高于可交付容量增速，且接入等待时长没有系统性下降。
- **原始领先指标**：单位服务能耗下降速度与算力服务量增长速度之比、峰值负荷增速、跨区调度作业占比；每年。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-056, J-058。
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C3：电子落地`。
- **原始外部对照判断**：**对手假设在历史上成立，但当前数据指向相反方向。** 一致（对本卡有利的一侧）：效率跑赢负荷并非空想——2010–2018 年全球数据中心计算实例增长 550%，能耗仅增约 6%，这是同行评审记录的八年解耦窗口（EXT-27）。**分歧与证据边界**：当前阶段数据反向——LBNL 测得美国数据中心用电占比自 2023 年约 4.4% 升向 2028 年 6.7%–12%（EXT-26）；IEA 给出 2024–2030 年数据中心用电年均约 15% 的增速，为其他所有行业增速之和的四倍以上（EXT-12）。也就是说，解耦在大模型阶段已明显减弱。此外没有任何权威机构发布过专门针对「效率转折点」的分析，本卡 2033–2040 的窗口更远在所有被引来源的预测边界之外。我为何仍坚持：作为本链最重要的对手假设保留，不作为行动依据，置信度不上调；它的价值在于指明本链约束的解除条件，而不在于预测解除会发生。
- **原始外部对照来源**：EXT-12, EXT-26, EXT-27（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1530–L1553`
- **Current card anchor**: `docs/en/ledger/61-70.md:L85–L104`
- **Original title**: If efficiency gains keep outpacing load growth, the constraint in this chain dissolves in the long run (landscape only)
- **Original one-sentence judgment**: If energy per unit of service keeps falling faster than load grows, and schedulable load can migrate freely across regions, this chain's power and permitting constraint dissolves on its own in the long run (landscape only).
- **Original reasoning chain**: The constraint holds only while load growth exceeds deliverable-capacity growth → if efficiency gains and cross-region scheduling both take effect, peak load growth flattens → the queue stops being the binding constraint → the certainty premium and site rents disappear with it.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, compute-related load in major markets still grows faster than deliverable capacity and interconnection wait times show no systematic decline.
- **Original leading indicator**: Ratio between the decline in energy per unit of service and the growth of compute service volume, peak load growth, share of cross-region scheduled jobs; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-056, J-058.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **The counter-hypothesis is historically real, but current data points the other way.** Agreement (the side that favours this card): efficiency outrunning load is not wishful — between 2010 and 2018 global data-centre compute instances grew 550% while energy use rose only about 6%, a peer-reviewed eight-year decoupling window (EXT-27). **Divergence and evidence boundary**: the current phase runs the other way — LBNL measures US data centres at about 4.4% of national electricity in 2023 heading to 6.7–12% by 2028 (EXT-26), and the IEA puts data-centre electricity growth at roughly 15% a year over 2024–2030, more than four times the combined growth of all other sectors (EXT-12); decoupling has clearly weakened in the large-model phase. Beyond that, no authority has published a dedicated analysis of an efficiency turning point, and this card's 2033–2040 window lies past the forecast boundary of every source cited here. Why the judgment is retained: kept as this chain's most important counter-hypothesis and not as a basis for action, with confidence not raised; its value is in naming the condition under which this chain's constraint dissolves, not in predicting that it will.
- **Original external comparison source**: EXT-12, EXT-26, EXT-27 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-064` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-065

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L5–L24`；`docs/en/ledger/61-70.md:L5–L24`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L599–L617`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L5–L24`
- **原始标题**：AI 跨主体执行动作后，真正稀缺的不是回滚软件，而是跨主体撤销权
- **原始一句话命题**：真正稀缺的不是沙盘与回滚软件，而是把状态从对方账本里收回来的跨主体撤销权。
- **原始推理链**：`J-004` 把「可撤销基础设施」整体当作稀缺项 → 按机会耐久闸第三问逐层拆开 → 动作不跨所有权边界时（自有库、自有云资源、测试沙盘），回滚是纯软件，恰是制造丰富的同一股力量最擅长造的东西，且被操作的系统由平台自己持有、有动机内置并免费发放 → 这一半有付费者而过不了机会耐久闸，出口是窗口机会 → 动作跨所有权边界时（付款、发货、签约、权利转让），状态落在对方账本与对方取得的法律权利上，撤销必须由对方同意并执行 → 而对方的默认利益是终局：它出售的正是终局性，撤销额度被配额化并单独计价（争议手续费、托管费、开证费）→ 历史上跨主体回退只在少数封闭网络里被真正建起来（卡组织拒付、证券结算撤销、托管与信用证），每一个都是会员规则、保证金与长期重复博弈的产物 → 算力可以无限复制沙盘代码，复制不出对方同意回退的义务 → 硬约束落在产权／私有性与信任／关系，而不是不可逆性（后者只是辅助透镜）→ 物理上不可逆的动作（已消耗、已损害、已投药）根本没有可撤销产品，残余归赔付主体，见 `J-005`
- **原始时间窗**：2027–2033，需求随代理跨主体执行放量而显性化
- **原始证伪条件**：到 2033 年，面向机器发起动作的跨主体撤销（延迟终局结算、可编程托管、单方撤销窗口）已成为主要支付与结算网络的默认规则且不单独计价，接入层没有形成可辨认的独立供给方
- **原始领先指标**：① 是否出现面向代理的可编程托管／延迟终局结算产品并单独计价；② 拒付与争议窗口是否被扩展到机器发起的交易；③ 合同模板中是否出现「AI 执行条款的单方撤销窗口」；④ 边界内沙盘／回滚是否被平台内置为默认能力（该项变真只确认窗口清单那一行关闭，不构成对本判断的支持）；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-001
- **原始状态与谱系**：`REVISED`（2026-09-20 普及闸复核：闸一不过，受众天花板即上述职业／组织规模，本卡降级为职业／组织性判断，不再作社会级趋势判断；原卡正文一字未删，编号不复用，判据见 `历史回顾 · 闸一`）。
- **原始出处**：`C1 · 生成变得免费之后`。
- **原始外部对照判断**：本轮未完成外部对照：未知。本判断由 2026-09-19 的机会耐久闸复核当场产生，尚未与任何外部判断对照；按 `00-method.md` 第 1.1 节第 4 条显式标注为未知，不得当作已对照使用，下一轮补齐三要素。
- **原始外部对照来源**：本轮未完成对照。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L599–L617`
- **Current card anchor**: `docs/en/ledger/61-70.md:L5–L24`
- **Original title**: Once AI executes across ownership boundaries, the scarce item is not rollback software but the right to reverse
- **Original one-sentence judgment**: What is scarce is not sandbox and rollback software but the right to pull state back out of the counterparty’s ledger.
- **Original reasoning chain**: `J-004` treated “reversible infrastructure” as one scarce item → taken apart layer by layer under opportunity-durability gate’s third question → when the action does not cross an ownership boundary (your own database, your own cloud resources, a test sandbox), rollback is pure software, exactly what the force making generation abundant is best at producing, and the system being operated on is held by the platform itself, which has every incentive to bundle it and give it away → that half has payers but fails the opportunity-durability gate, so its exit is a window opportunity → when the action does cross an ownership boundary (payment, shipping, signing, transfer of rights), the state lands in the counterparty’s ledger and in legal rights the counterparty has acquired, so reversal must be consented to and executed by that party → whose default interest is finality: what it sells is finality, and reversal capacity is rationed and separately priced (dispute fees, escrow fees, issuance fees) → historically, cross-party unwind has actually been built only inside a handful of closed networks (card-scheme chargebacks, securities settlement reversal, escrow and letters of credit), each a product of membership rules, collateral, and long-running repeated games → compute can copy sandbox code without limit; it cannot copy the counterparty’s obligation to unwind → the hard constraint therefore lands on ownership/privacy and trust/relationship, not on irreversibility (which is only a supporting lens) → for physically irreversible actions (consumed, harmed, injected) no reversibility product exists at all and the residue belongs to the compensating party, see `J-005`
- **Original time window**: 2027–2033, as demand becomes explicit with the volume of cross-party agent execution
- **Original falsifier**: By 2033, cross-party reversal for machine-initiated actions (delayed-finality settlement, programmable escrow, unilateral rescission windows) has become a default rule of the major payment and settlement networks, is not priced separately, and the access layer has produced no identifiable independent supplier
- **Original leading indicator**: ① Whether programmable escrow / delayed-finality settlement products aimed at agents appear and are separately priced; ② whether chargeback and dispute windows are extended to machine-initiated transactions; ③ whether contract templates begin to carry a “unilateral rescission window for AI-executed clauses”; ④ whether platforms bundle within-boundary sandbox / rollback as a default capability (that one turning true only confirms that the Window List row has closed and is not evidence for this judgment); observed every six months
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Comparison not completed this round: unknown. This judgment was produced on the spot by the opportunity-durability review of 2026-09-19 and has not yet been compared against any external judgment; it is explicitly marked unknown per `00-method.md` §1.1 item 4, must not be used as if compared, and the three elements will be completed in the next round.
- **Original external comparison source**: Comparison not completed this round.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-065` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-066

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L105–L124`；`docs/en/ledger/61-70.md:L105–L124`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1830–L1848`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L105–L124`
- **原始标题**：五道普及闸是必要条件，不是充分条件
- **原始一句话命题**：一项能力若有任一道普及闸不通过，它不会成为社会级风气；但五道全过只说明它有资格参赛，不保证它会发生。
- **原始推理链**：先立三道自我攻击锁 → 第三把锁要求举出「五闸全过却仍失败」的案例 → 1985 年 New Coke 逐条过闸：规模（每天喝可乐的人以十亿计）、替代（替掉旧可乐，同一动作、同一价格、同一货架）、承载（同一条生产线与分销网络，边际部署成本为零）、决策（可口可乐单方生产，消费者单方购买）、代价（零学习、零身体、零社会代价，且盲测中更好喝）→ 1985-07-11，79 天后宣布旧配方回归 → 漏掉的是需求侧：人买的不总是那个东西本身，可乐卖的是身份符号，而符号的价值恰恰来自它不变 → 因此这套闸只能证否，不能证是 → 正确用法是「不过闸 ⇒ 基本不会成为社会风气」，而非「全过闸 ⇒ 会发生」
- **原始时间窗**：2026-01 至 2036-12（作为推演规则的适用与检验期）
- **原始证伪条件**：出现一项在五道闸中**至少一道明确不通过**、却仍在十年内达到社会级普及（十亿人日频，或亿级人周频）的能力，且其普及无法由本文写明的解锁条件解释
- **原始领先指标**：① 每半年清点当期新达到社会级的能力，逐条回填五闸判定，记录有无「不过闸却普及」的反例；② 本项目新写的每条社会级判断是否都能通过五闸检验；③ 是否出现第二个「全过闸仍失败」的案例（该项变真只加强本卡，不削弱）；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-067, J-068, J-069, J-070, J-071
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：Rogers 1962 的创新五属性（EXT-33）与本文闸二、闸五分别重合于 relative advantage 与 complexity；Moore 1991（EXT-35）同样主张技术成功不等于跨越到大众市场。**分歧与证据边界**：Rogers 的五属性是打分式（越高扩散越快），本文改写为否决式必要条件并要求指名具体对象（替掉哪个动作、承载物由谁付、决定权在谁手上）；打分式框架几乎不可证伪，否决式清单可以。**我为何仍坚持**：否决式读法的代价是把全部判否押在闸集合的完备性上，这一代价已由 New Coke 反例显式承认并写进本卡与正文第六节，因此置信度停在「中」，不上调。
- **原始外部对照来源**：EXT-33, EXT-35（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1880–L1898`
- **Current card anchor**: `docs/en/ledger/61-70.md:L105–L124`
- **Original title**: The five gates are necessary, not sufficient
- **Original one-sentence judgment**: If a capability fails any one of the five diffusion gates it will not become the way a whole society does things; passing all five only means it qualifies to compete, and guarantees nothing.
- **Original reasoning chain**: Three self-attack locks are set up first → the third lock demands a case that passes all five gates and still fails → New Coke, 1985, gate by gate: scale (people who drink cola daily number in the billions), substitution (replaces the old Coke — same act, same price, same shelf), carrier (same production line and distribution network, zero marginal deployment cost), decision rights (Coca-Cola decides to produce unilaterally, consumers buy unilaterally), cost (zero learning, zero bodily, zero social cost, and it won blind taste tests) → launched 1985-07-11, the old formula announced back 79 days later → what the gates missed is on the demand side: what people buy is not always the thing itself, Coke sells an identity symbol, and a symbol's value comes precisely from not changing → therefore this gate set can only disprove, never prove → the correct use is "fails a gate ⇒ will essentially not become society-wide," never "passes all gates ⇒ will happen."
- **Original time window**: 2026-01 to 2036-12 (the period over which this rule is applied and tested).
- **Original falsifier**: A capability that **clearly fails at least one** of the five gates nevertheless reaches society-wide diffusion within ten years (billions of people daily, or hundreds of millions weekly), and its diffusion cannot be explained by an unlock condition already written into this document.
- **Original leading indicator**: (1) Every six months, enumerate the capabilities that newly reached society-wide scale in that period, back-fill the five-gate verdict for each, and record whether any counter-example diffused while failing a gate; (2) whether every new society-level judgment written in this project can pass the five-gate test; (3) whether a second "passes all gates, still fails" case appears (that turning true strengthens this card rather than weakening it); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: J-067, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: Rogers 1962's five attributes of an innovation (EXT-33) overlap with this document's Gate 2 and Gate 5 at relative advantage and complexity respectively; Moore 1991 (EXT-35) likewise argues technical success is not the same as crossing into a mass market. **Divergence and evidence boundary**: Rogers's five attributes are scored (higher means faster diffusion); this document rewrites them as veto-style necessary conditions and requires naming a concrete object (which act is replaced, who pays for the carrier, whose hands the decision sits in). A scored framework is nearly unfalsifiable; a veto checklist can be falsified. **Why the judgment is retained**: the cost of the veto-style reading is that every negative verdict rides on the gate set being complete, a cost explicitly acknowledged through the New Coke counter-example and written into both this card and section 6 of the prose, so confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-33, EXT-35 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-066` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-067

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L125–L144`；`docs/en/ledger/61-70.md:L125–L144`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1849–L1867`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L125–L144`
- **原始标题**：一项能力的受众天花板等于它所服务动作的人数与频次，不等于技术能力的上限
- **原始一句话命题**：一项能力能影响的人数上限，由它所服务的那个动作有多少人做、多久做一次决定，而不由技术能力的上限决定。
- **原始推理链**：清点达到社会级的能力，它们服务的动作在普及前已是十亿量级日频——智能手机（联系人、看东西、找路、付钱；2023 年 43 亿人持有，占世界人口 54%）、健康码（进入一个场所）、移动支付（付一笔钱）→ 再清点技术完全成功却停在小众的案例，其服务动作的人数在普及前就不够：协和式客机（愿为省三四小时付数倍票价的跨大西洋旅客，年以十万人次计，27 年只造 20 架、商用 14 架）、铱星（无蜂窝信号处打电话，破产时用户 5.5 万而保本需百万以上）、世界语（1887 年绝大多数人一生不会遇到跨母语日常交谈的场合）→ 三者的技术全部可用，差别只在动作的人数 → 因此必须在技术评估之前先数人 → 并追问一层：它是提高既有专业者的上限（天花板＝该职业人数），还是让原本不会的人也能做（可能把动作本身做大）
- **原始时间窗**：2026-01 至 2036-12
- **原始证伪条件**：出现一项能力，其所服务的动作在普及前只有百万量级人口在做，却在五年内达到十亿人日频使用，且该增长不能由「它让原本不会做的人也能做、从而把动作人数本身扩大」来解释
- **原始领先指标**：① 本项目每条新写的社会级断言是否都给出了动作的人数量级与频次；② 每半年观察当期新达到十亿量级的能力，其服务动作在普及前的人数量级；③ 是否出现「动作人数未变而受众暴涨」的反例；每半年观察
- **原始置信度**：中
- **原始 depends-on**：—
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：扩散研究普遍承认采用有上限。**分歧与证据边界**：这是一处真实的文献空白——本轮检索未找到任何既有扩散框架把「所服务动作的人数与频次」作为前置筛选变量：Rogers 的五属性刻画创新自身的属性（EXT-33），Bass 1969 把市场潜力 m 当作**外生给定的参数**（EXT-38），两者都不问「这个动作到底有多少人在做」，而这正是闸一问的量。**我为何仍坚持**：三组失败案例（协和、铱星、世界语）的技术全部成功，唯一共同点是动作人数不足，这个共同点足以支撑判断；但因为没有任何外部框架校准过它，置信度不高于「中」。
- **原始外部对照来源**：EXT-33, EXT-38（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1899–L1917`
- **Current card anchor**: `docs/en/ledger/61-70.md:L125–L144`
- **Original title**: The audience ceiling of a capability is the headcount and frequency of the activity it serves
- **Original one-sentence judgment**: The upper bound on how many people a capability can affect is set by how many people perform the activity it serves and how often they perform it, not by the ceiling of the technology.
- **Original reasoning chain**: Enumerate the capabilities that reached society-wide scale, and the activities they serve were already billions-scale and daily before diffusion — smartphones (contacts, looking things up, finding the way, paying; 4.3 billion owners in 2023, 54% of world population), health codes (entering a venue), mobile payment (paying for something) → then enumerate the cases where the technology fully succeeded and still stalled at a niche, and the headcount of the activity served was already insufficient: Concorde (transatlantic passengers willing to pay several times the fare to save three or four hours, hundreds of thousands of trips a year; 20 aircraft built over 27 years, 14 in commercial service), Iridium (calling from places without cellular coverage; 55,000 subscribers at bankruptcy against a break-even in the millions), Esperanto (since 1887 the vast majority of people never once encounter a cross-native-language everyday conversation) → the technology worked in all three; the difference is only the headcount of the activity → therefore you must count people before assessing the technology → and ask one layer deeper: does it raise the ceiling of existing professionals (ceiling = the size of that occupation), or let people who previously could not do it do it (which may enlarge the activity itself).
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability whose served activity was performed by only millions of people before diffusion nevertheless reaches billions of daily users within five years, and that growth cannot be explained by "it let people who previously could not do it do it, thereby enlarging the activity's headcount itself."
- **Original leading indicator**: (1) Whether every new society-level assertion in this project states the order of magnitude and frequency of the activity's headcount; (2) every six months, observe the capabilities newly reaching billions scale and the pre-diffusion headcount of the activity they serve; (3) whether a counter-example appears in which the activity's headcount did not change while the audience exploded; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: diffusion research broadly accepts that adoption has a ceiling. **Divergence and evidence boundary**: this is a genuine gap in the literature — this round's search found no existing diffusion framework that uses "the headcount and frequency of the activity served" as a prior screening variable: Rogers's five attributes characterize the innovation itself (EXT-33), and Bass 1969 treats market potential m as an **exogenously given parameter** (EXT-38); neither asks how many people actually perform the activity, which is exactly the quantity Gate 1 asks about. **Why the judgment is retained**: three failure cases (Concorde, Iridium, Esperanto) all succeeded technically and share exactly one feature — insufficient headcount for the activity — and that shared feature is enough to support the judgment; but because no external framework has ever calibrated it, confidence is no higher than Medium.
- **Original external comparison source**: EXT-33, EXT-38 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-067` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-068

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L145–L164`；`docs/en/ledger/61-70.md:L145–L164`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1868–L1886`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L145–L164`
- **原始标题**：能普及的能力都替掉了一个已在发生的动作，而不是在它之上再加一件事
- **原始一句话命题**：能普及的能力都替掉了用户今天已经在做的某一个具体动作；不替任何东西、只是多一件事的，天花板是爱好者。
- **原始推理链**：采用一项新能力要付学习、购置、改流程的固定代价 → 这笔代价只有在有旧动作可抵扣时才划算 → 不替任何东西，收益就得自证，采用只能靠好奇心，而好奇心的存量就是爱好者的人数 → 通过侧：集装箱替掉散货装卸（1956 年每吨 5.83 美元 → 每吨 15.8 美分，降幅约 97%）、家庭联产承包替掉记工分（同一块地同一批人，变的只是监督成本的归属）、二维码支付替掉掏钱找零对账 → 被挡住侧：Google Glass 不替代任何动作而是在脸上加一件事（2013 年 1500 美元，2015 年 1 月停售）、3D 电视给「看电视」加一个要额外付代价的属性（ESPN 3D 2010-06-11 开播，2013-09-30 关闭）、MOOC **替错了对象**——它替掉「听课」，而学生买的是文凭，文凭一点没被替掉（同行评议完成率中位数 12.6%）→ 判否条件因此只有一条：不替任何东西；成本降幅不是及格线而是速度变量
- **原始时间窗**：2026-01 至 2036-12
- **原始证伪条件**：出现一项**不替代任何既有具体动作、纯粹新增**的能力，在五年内达到社会级普及（十亿人日频或亿级人周频），且其采用不由强制或单一主体补贴驱动
- **原始领先指标**：① 每条新判断是否都能指名它替掉的那个具体、可数、当时已在发生的动作；② 观察当期高增长产品中「纯新增型」与「替代型」的构成；③ 是否出现替错对象的新案例（替了表层动作而没替掉用户真正在买的东西）；每半年观察
- **原始置信度**：中
- **原始 depends-on**：—
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：与 Rogers 1962 五属性中的 relative advantage 高度重合（EXT-33），扩散研究早已承认相对优势是扩散速度的解释变量。**分歧与证据边界**：本文把它从打分维度改写为判否条件，并且把判否条件收窄到「替代 vs 附加」这一项——成本降幅被明确降级为速度变量，理由是本文自己的通过案例（家庭联产承包）并没有把单位成本降一个数量级，若把数量级写进及格线，这道闸会被自己的案例证伪。**我为何仍坚持**：这次收窄是落地前的主动更正，代价是闸二的判否力变弱（它现在只能挡住「纯新增型」），这一点已在正文第三节写明，置信度因此停在「中」。
- **原始外部对照来源**：EXT-33（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1918–L1936`
- **Current card anchor**: `docs/en/ledger/61-70.md:L145–L164`
- **Original title**: What diffuses replaces an activity already happening, not something added on top
- **Original one-sentence judgment**: Capabilities that diffuse all replace one concrete activity the user already performs today; anything that replaces nothing and merely adds one more thing is capped at hobbyists.
- **Original reasoning chain**: Adopting a new capability costs a fixed price in learning, purchase and process change → that price only pays off when there is an old activity to offset it against → replace nothing and the benefit must justify itself from scratch, so adoption runs on curiosity alone, and the stock of curiosity is exactly the headcount of hobbyists → passing side: containerization replaced break-bulk loading ($5.83 per ton in 1956 → 15.8 cents per ton, roughly a 97% drop), China's household responsibility system replaced work-point accounting (same land, same people; what changed was who bore the monitoring cost), QR-code payment replaced pulling out cash, making change and reconciling → blocked side: Google Glass replaced no activity and instead added a thing on your face ($1,500 in 2013, withdrawn January 2015), 3D television added an extra-cost attribute to "watching television" (ESPN 3D launched 2010-06-11, closed 2013-09-30), MOOCs **replaced the wrong object** — they replaced attending lectures, while what students buy is the credential, and the credential was not replaced at all (median completion rate of 12.6% in peer-reviewed work) → the veto condition is therefore exactly one: replaces nothing; the size of the cost drop is not a pass mark but a speed variable.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability that **replaces no existing concrete activity and is purely additive** reaches society-wide diffusion within five years (billions daily or hundreds of millions weekly), and its adoption is driven neither by coercion nor by a single subsidizing party.
- **Original leading indicator**: (1) Whether every new judgment can name the concrete, countable activity, already happening at the time, that it replaces; (2) the split between "purely additive" and "substitutive" among the period's fast-growing products; (3) whether new cases of replacing the wrong object appear (the surface activity replaced while what the user actually buys is not); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: heavily overlapping with relative advantage among Rogers 1962's five attributes (EXT-33); diffusion research has long accepted relative advantage as an explanatory variable for diffusion speed. **Divergence and evidence boundary**: this document rewrites it from a scored dimension into a veto condition, and narrows the veto condition to the single item of substitution versus addition — the size of the cost drop is explicitly demoted to a speed variable, because this document's own passing case (the household responsibility system) did not cut unit cost by an order of magnitude, and writing an order of magnitude into the pass mark would have this gate falsified by its own evidence. **Why the judgment is retained**: this narrowing is a proactive correction made before landing, at the cost of weakening Gate 2's power to say no (it can now only block the purely additive), which is stated in section 3 of the prose; confidence therefore stays at Medium.
- **Original external comparison source**: EXT-33 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-068` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-069

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L165–L184`；`docs/en/ledger/61-70.md:L165–L184`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1887–L1905`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L165–L184`
- **原始标题**：专用基础设施若只为这一件事存在，它不会被建起来；能力要等到承载物因别的理由已经存在
- **原始一句话命题**：若一项能力所需的新基础设施除了它没有第二个用途、也没有独立收入来源，那么这套基础设施要么不会被建起来，要么必须等别人因为别的理由把它建好。
- **原始推理链**：1964 年可视电话需要专用宽带环路与专用终端，这套东西除了可视电话没有第二用途 → AT&T 必须独家承担全部成本，再靠一个尚不存在的用户群回收 → 匹兹堡峰值 32 台、芝加哥峰值 453 台，合计不到 500 台 → 2020 年的视频通话什么专用基础设施都不需要：前置摄像头、宽带、屏幕全都因为**别的理由**早已在几十亿人口袋里，采用者的边际硬件成本为零 → Zoom 日均会议参与人数三个月内 1000 万 → 3 亿 → 需求没变、技术没变，变的是承载物的出资人 → 对照：美国电视的广播塔确实是新建专用基础设施，但它有独立收入来源（广告），于是被建起来（家庭拥有率 1948 年约 1% → 1955 年约 75%）；健康码跑在已装好的支付宝与微信里，没让任何人装新 App → 反例侧：铱星 66 颗卫星加专用话机约 50 亿美元只为一件事存在；Better Place 换电既要站网又要车厂改设计，融资约 8.5 亿美元后于 2013 年 5 月破产
- **原始时间窗**：2026-01 至 2036-12
- **原始证伪条件**：出现一项需要全新专用基础设施、且该基础设施既无第二用途又无独立收入来源、也无单一主体全额买单的能力，仍在十年内达到社会级普及
- **原始领先指标**：① 每条带时间窗的判断是否都回答了「承载物由谁付」；② 观察当期受阻能力中，阻力是否可归到承载物缺失；③ 是否出现「承载物因别的理由建好」从而解锁某条既有判断的事件（这类事件是时间窗修正的触发器）；每半年观察
- **原始置信度**：中
- **原始 depends-on**：—
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：文献中有相邻概念——Teece 1986 的互补性资产、网络效应文献中的 installed base、Zittrain 2006 的 generativity（EXT-37）。**分歧与证据边界**：它们回答的是「谁能从创新中获利」与「为什么通用平台能长出未预期的应用」，而闸三问的是一个更前置的存在性问题：这件专用基础设施到底会不会被建起来。本轮未找到把这个问题单独提出的既有框架。**我为何仍坚持**：可视电话 1964 vs 2020 这一对是同一需求、同一技术、不同承载物的天然对照，机制足够清楚；但因为闸三与闸四 (b) 存在合并风险尚未排除，置信度不高于「中」。
- **原始外部对照来源**：EXT-37（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1937–L1955`
- **Current card anchor**: `docs/en/ledger/61-70.md:L165–L184`
- **Original title**: Infrastructure that serves only one capability does not get built
- **Original one-sentence judgment**: If the new infrastructure a capability requires has no second use and no independent revenue source, that infrastructure either does not get built, or the capability must wait until someone else builds it for other reasons.
- **Original reasoning chain**: The 1964 Picturephone needed dedicated broadband loops and dedicated terminals, and that equipment had no second use beyond Picturephone → AT&T had to bear the entire cost alone and recover it from a user base that did not yet exist → Pittsburgh peaked at 32 sets and Chicago at 453, under 500 in total → video calling in 2020 required no dedicated infrastructure whatsoever: front cameras, broadband and screens were already in billions of pockets **for other reasons**, and the adopter's marginal hardware cost was zero → Zoom's daily meeting participants went from 10 million to 300 million in three months → the demand had not changed and the technology had not changed; what changed was who paid for the carrier → contrast: US television broadcast towers genuinely were newly built dedicated infrastructure, but they had an independent revenue source (advertising), so they got built (household ownership roughly 1% in 1948 → roughly 75% in 1955); health codes ran inside the already-installed Alipay and WeChat and made nobody install a new app → counter-example side: Iridium's 66 satellites plus dedicated handsets cost roughly $5 billion and existed for one thing only; Better Place's battery swapping needed both a station network and redesigned cars, and went bankrupt in May 2013 after raising about $850 million.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability requiring wholly new dedicated infrastructure that has neither a second use nor an independent revenue source, and for which no single party pays in full, nevertheless reaches society-wide diffusion within ten years.
- **Original leading indicator**: (1) Whether every judgment with a time window answers "who pays for the carrier"; (2) among the capabilities currently blocked, whether the resistance can be attributed to a missing carrier; (3) whether events of the form "the carrier got built for other reasons" unlock an existing judgment (such events are the trigger for revising time windows); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: the literature has adjacent concepts — Teece 1986's complementary assets, installed base in the network-effects literature, and Zittrain 2006's generativity (EXT-37). **Divergence and evidence boundary**: those answer "who can profit from an innovation" and "why general platforms grow unanticipated applications," whereas Gate 3 asks a prior existence question: will this dedicated infrastructure be built at all. This round found no existing framework that poses that question on its own. **Why the judgment is retained**: Picturephone 1964 versus 2020 is a natural control pair — same demand, same technology, different carrier — and the mechanism is clear enough; but because the merger risk between Gate 3 and Gate 4(b) has not been ruled out, confidence is no higher than Medium.
- **Original external comparison source**: EXT-37 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-069` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-070

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L185–L203`；`docs/en/ledger/61-70.md:L185–L203`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1906–L1924`
- **当前卡锚点**：`docs/zh/ledger/61-70.md:L185–L203`
- **原始标题**：多方必须同时改变时，只有存在既能强制又能观测执行的一方、或单一主体补贴、或局部闭环，改变才会发生
- **原始一句话命题**：若采用必须多方同时改变，则只有在「能强制且执行可被观测的一方」「能一次性补贴各方启动成本的单一主体」「无须等全社会的局部闭环」三者之一成立时，改变才会越出试点。
- **原始推理链**：单方即可决定的采用自动过闸（ATM：银行单方部署、储户单方使用，1967-06-27 巴克莱 Enfield 第一台）→ 需多方同时改变时，各方的最优策略是等待，于是停在试点 → 解锁路径 (a) 强制且可观测：健康码既能强制，执行又在每个场所入口被看见，数月全国铺开；家庭联产承包 1978 年小岗村 18 户 → 1979 年底安徽 51% 生产队 → 1982 年中央一号文件 → 1983 年全面推行 → 反证 (a) 的另一半：禁酒令能强制但**看不见**，约 1520 名联邦探员对应 1.06 亿人口（约每七万人一名），仅纽约就有三万到十万家地下酒吧，1933 年废除 → 解锁路径 (b) 单一主体补贴：1958 年 BankAmericard 弗雷斯诺空投，向居民无申请邮寄约 6 万张已激活卡，用自己的资产负债表一次性买单整座城市的启动成本 → 解锁路径 (c) 局部闭环：1975 年美国《米制转换法》明文「完全自愿」、无期限无处罚，1982 年米制委员会被撤销，日常生活没普及，**但科学界、医药界、军队完全使用公制**——同一案例里 (c) 的正反两面同时出现
- **原始时间窗**：2026-01 至 2036-12
- **原始证伪条件**：出现一例必须多方同时改变的采用，在三条解锁路径**都不成立**的情况下仍达到社会级普及
- **原始领先指标**：① 每条涉及协同的判断是否都指名了决定权持有方与解锁路径；② 观察当期停在试点的协同型能力，其卡点是否可归到三条路径的缺失；③ 是否出现纯由网络效应自发完成的大规模协同（该项变真直接触发证伪条件）；每半年观察
- **原始置信度**：中
- **原始 depends-on**：—
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：与 Olson 1965《集体行动的逻辑》一致——理性自利的个体不会自动为共同利益行动，除非群体很小或存在强制与选择性激励（EXT-36）；本文三条解锁路径与 Olson 的强制、选择性激励、小群体一一对应。同时与路径依赖、网络外部性文献一致（EXT-34）：采用价值取决于他人是否也采用，这正是多方协同型采用的困难来源。**分歧与证据边界**：本文的增量是 (a) 里「执行必须可被观测」这半截——Olson 讲强制，不讲强制的可观测性；这半截来自禁酒令（能强制、看不见、失败）与美国米制转换（不强制、无处罚、失败）两个案例的对照。**我为何仍坚持**：该半截有两个方向相反的案例支撑，但「可观测性」尚未被任何外部框架单独检验过，且三条路径的完备性存疑（见最强反方），置信度停在「中」。
- **原始外部对照来源**：EXT-34, EXT-36（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1956–L1974`
- **Current card anchor**: `docs/en/ledger/61-70.md:L185–L203`
- **Original title**: When many parties must change together, change needs enforceable and observable authority, a single subsidizing party, or a local closed loop
- **Original one-sentence judgment**: If adoption requires many parties to change at once, change moves beyond pilots only when one of three holds: a party that can both compel and observe compliance, a single party able to subsidize everyone's start-up cost at once, or a local closed loop that need not wait for the whole society.
- **Original reasoning chain**: Adoption decidable by one party passes automatically (ATMs: the bank deploys unilaterally, the depositor uses unilaterally; Barclays Enfield, 1967-06-27) → when many parties must change at once, each party's optimal strategy is to wait, so it stalls at pilots → unlock path (a) enforceable and observable: health codes could both be compelled and be seen being enforced at every venue entrance, rolled out nationwide in months; the household responsibility system went from 18 households in Xiaogang in 1978 → 51% of production teams in Anhui by end-1979 → the 1982 Central Document No. 1 → full rollout in 1983 → the other half of (a), by contradiction: Prohibition could compel but could **not see** — roughly 1,520 federal agents for a population of 106 million (about one per 70,000), with 30,000 to 100,000 speakeasies in New York City alone; repealed in 1933 → unlock path (b) a single subsidizing party: the 1958 BankAmericard Fresno drop mailed roughly 60,000 pre-activated cards to residents who had not applied, buying an entire city's start-up cost outright off its own balance sheet → unlock path (c) a local closed loop: the 1975 US Metric Conversion Act said in so many words that conversion was "wholly voluntary," with no deadline and no penalty; the Metric Board was abolished in 1982 and everyday life never converted, **yet science, medicine and the military use metric completely** — both sides of (c) appear inside the same case.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A case of adoption requiring many parties to change at once reaches society-wide diffusion while **none** of the three unlock paths holds.
- **Original leading indicator**: (1) Whether every judgment involving coordination names the holder of decision rights and the unlock path; (2) among coordination-type capabilities stalled at pilots, whether the blockage can be attributed to the absence of all three paths; (3) whether large-scale coordination is ever completed spontaneously by network effects alone (that turning true triggers the falsifier directly); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: consistent with Olson 1965, *The Logic of Collective Action* — rational self-interested individuals do not automatically act for a common interest unless the group is small or coercion and selective incentives exist (EXT-36); this document's three unlock paths map one-to-one onto Olson's coercion, selective incentives and small groups. Also consistent with the path-dependence and network-externality literature (EXT-34): the value of adopting depends on whether others adopt, which is exactly the source of difficulty in multi-party coordination. **Divergence and evidence boundary**: this document's increment is the half-clause inside (a) that enforcement must be observable — Olson discusses coercion, not the observability of coercion; that half comes from contrasting Prohibition (could compel, could not see, failed) with US metrication (no compulsion, no penalty, failed). **Why the judgment is retained**: that half-clause is supported by two cases pointing in opposite directions, but observability has never been tested on its own by any external framework, and the completeness of the three paths is in doubt (see the opposing mechanism), so confidence stays at Medium.
- **Original external comparison source**: EXT-34, EXT-36 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-070` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-071

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L5–L28`；`docs/en/ledger/71-80.md:L5–L28`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1925–L1947`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L5–L28`
- **原始标题**：持续净负担而非毛摩擦决定自愿采用天花板
- **原始一句话命题**：在自愿采用下，应比较相对真实 incumbent 的**持续净负担**：新增身体／社会／学习／金钱负担，减去节省的等待、价格、时间与流程成本；只有净负担为正、可观且随频次累积时，才会把天花板压到远低于动作人数。
- **原始推理链**：原规则把每次使用摩擦直接当负担 → Piggly Wiggly 1916 年自助商店要求顾客每次自行走过货架、比较和取货，却很快扩张并使 self-service 成为超市基本形态（EXT-55）→ 所以「存在重复劳动」不能判否，必须减去旧流程的等待、价格、时间与选择成本 → 失败侧仍成立：隐形眼镜相对框架眼镜增加每次戴取与护理，3D 电视增加每次佩戴与视角约束，Google Glass 增加持续社会摩擦 → 安全带说明强制可绕过自愿采用的净负担 → 当前规则只在**自愿采用且持续净负担为正、可观**时判不过。
- **原始时间窗**：2026-01 至 2036-12
- **原始证伪条件**：出现一项在自愿采用条件下（无强制、无持续补贴）的能力，相对真实 incumbent 每次都带来经同口径核算的显著正净负担，却在十年内达到所服务动作人口多数（>50%）；或 calibration 无法找到只由持续净负担判否、而非由闸二替代判否的独占案例。
- **原始领先指标**：① 新判断是否同时登记新增摩擦与被节省的等待／价格／时间／流程成本；② 失败案例的净负担能否在采用前材料中计算；③ 是否出现高留存产品长期承担显著正净负担；每半年观察。
- **原始置信度**：中
- **原始 depends-on**：—
- **原始状态与谱系**：REVISED（2026-09-21 闸五收窄；v1 快照保留并计入 calibration 分母）
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：**一致**：与 Rogers 1962 的 complexity 和 relative advantage 都部分重合（EXT-33）。**分歧与证据边界**：本卡把「每次净负担」写成可判否的必要条件，而 Rogers 是打分式属性；自助零售只证明毛摩擦写法错误，不单独证明净负担版本正确。**我为何仍坚持**：成功侧自助零售与失败侧隐形眼镜／3D 电视／Google Glass 给出相反方向，足以要求净额核算，但不足以上调置信度。
- **原始外部对照来源**：EXT-33, EXT-39, EXT-40, EXT-55, EXT-65, EXT-66（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1975–L1997`
- **Current card anchor**: `docs/en/ledger/71-80.md:L5–L28`
- **Original title**: Recurring net burden, not gross friction, sets the voluntary-adoption ceiling
- **Original one-sentence judgment**: Voluntary adoption must compare **recurring net burden relative to the real incumbent**: added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost. Only a positive, material burden that accumulates with frequency pushes the ceiling far below the activity population.
- **Original reasoning chain**: The old rule treated any per-use friction as burden → Piggly Wiggly's 1916 self-service store made shoppers repeatedly walk the aisles, compare, and pick goods, yet expanded rapidly and helped make self-service the supermarket's basic form (EXT-55) → therefore recurring labor alone cannot veto adoption; the ledger must subtract waiting, price, time, and process savings from it → the failure side remains: contact lenses add repeated insertion and care relative to frames, 3D television adds glasses and viewing-position constraints, and Google Glass adds recurring social friction → seat belts show that compulsion can bypass voluntary net burden → the current rule vetoes only when **voluntary adoption carries a positive, material recurring net burden**.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: Under voluntary adoption (no compulsion, no ongoing subsidy), a capability with a materially positive recurring net burden versus the real incumbent reaches majority adoption (>50%) of the population performing the activity within ten years; or calibration cannot find a case stopped only by recurring net burden rather than Gate 2 replacement.
- **Original leading indicator**: (1) whether new judgments record both added friction and saved waiting / price / time / process cost; (2) whether failure cases' net burden can be computed from as-of evidence; (3) whether high-retention products sustain a materially positive recurring net burden; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: REVISED (2026-09-21 Gate 5 narrowed; v1 snapshot retained and counted in the calibration denominator).
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: partly overlaps Rogers 1962's complexity and relative advantage (EXT-33). **Divergence and evidence boundary**: this card turns per-use net burden into a necessary-condition veto, whereas Rogers uses scored attributes; self-service retail refutes the gross-friction version but does not by itself prove the net-burden version. **Why the judgment is retained**: success-side self-service retail and failure-side contact lenses / 3D television / Google Glass force net accounting, but do not justify raising confidence.
- **Original external comparison source**: EXT-33, EXT-39, EXT-40, EXT-55, EXT-65, EXT-66 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-071` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-072

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L29–L50`；`docs/en/ledger/71-80.md:L29–L50`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1948–L1972`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L29–L50`
- **原始标题**：「从几十套候选方案中择一」是一条职业性判断，其受众天花板在百万量级
- **原始一句话命题**：「面对一批已生成好的候选方案，选定一个并为结果负责」这个动作的全球从业人数在百万量级、频次为周频，因此由它推出的稀缺性是职业性判断，不得以社会级口吻书写。
- **原始推理链**：定义动作——面对一批已经生成好的候选方案，选定一个并为结果负责 → 谁在做这个动作须同时满足三条：职业上要求批量产出候选（广告与营销创意、设计与产品、建筑与工程方案、咨询方案）、本人有拍板权而非执行者、频次至少每周一次 → 三条同时满足的人集中在上述岗位的决策层，按岗位结构推算全球量级在 10⁶、周频 → 逐闸判定：闸二过（替掉「先做三版再从三版里选」）、闸三过（搭在已普及的生成工具上）、闸四过（一个人单方决定）、闸五边界（要看的候选从 3 个变成 60 个，注意力代价上升）、**闸一不过**（百万级周频，对照社会级门槛十亿人日频或亿级人周频差两到三个数量级）→ 同一条链上真正过闸一的不是「选」而是「做」：「需要一份能用的材料、图、文案或程序」十亿人偶尔要做，且此前大多数人做不了，属于「让原本不会的人也能做」那一类
- **原始时间窗**：2026-01 至 2031-12
- **原始证伪条件**：到 2031 年底，出现可引用的统计显示「从批量候选中择一并担责」的人群达到亿级且为周频以上，或该动作被证明已扩散到非职业人群的日常决策中
- **原始领先指标**：① 是否出现可引用的全球岗位统计以替换本卡的构造式推算；② 消费级产品中「一次生成数十个候选供用户挑选」是否成为默认交互（该项变真会把动作人数做大，直接冲击本卡）；③ 本项目 C1 链中依赖「选择稀缺」的下游判断，其受众口吻是否已按本卡收窄；每半年观察
- **原始置信度**：中
- **原始 depends-on**：J-066, J-067
- **原始状态与谱系**：ACTIVE
- **原始出处**：`历史回顾：什么才能成为整个社会的风气`。
- **原始外部对照判断**：本轮未完成外部对照：未知。本卡的受众量级来自构造式推算，本轮未取得可引用的全球岗位统计，也未与任何外部判断对照；按 `00-method.md` 第 1.1 节第 4 条显式标注为未知，不得当作已对照使用，下一轮补齐三要素。
- **原始外部对照来源**：本轮未完成对照。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1998–L2022`
- **Current card anchor**: `docs/en/ledger/71-80.md:L29–L50`
- **Original title**: Choosing one from dozens of generated candidates is an occupational judgment, not a society-level trend
- **Original one-sentence judgment**: The activity "faced with a batch of already-generated candidates, pick one and own the outcome" is performed by a global population in the millions at weekly frequency, so any scarcity derived from it is an occupational judgment and must not be written in a society-level voice.
- **Original reasoning chain**: Define the activity — faced with a batch of already-generated candidates, pick one and own the outcome → whoever performs it must satisfy three conditions at once: an occupation that requires producing candidates in batches (advertising and marketing creative, design and product, architectural and engineering schemes, consulting proposals), personal authority to decide rather than to execute, and a frequency of at least once a week → people satisfying all three concentrate in the decision layer of those roles, and by role structure the global order of magnitude is 10⁶ at weekly frequency → gate by gate: Gate 2 passes (replaces "make three versions first, then choose among the three"), Gate 3 passes (rides on already-diffused generation tools), Gate 4 passes (one person decides unilaterally), Gate 5 is borderline (candidates to review go from 3 to 60, so the attention cost rises), **Gate 1 fails** (millions at weekly frequency, two to three orders of magnitude below the society-wide threshold of billions daily or hundreds of millions weekly) → what actually passes Gate 1 on the same chain is not choosing but making: "needing a usable document, diagram, copy or program" is something billions of people occasionally need, and most of them previously could not do it, which belongs to the "lets people who previously could not do it do it" class.
- **Original time window**: 2026-01 to 2031-12.
- **Original falsifier**: By the end of 2031, citable statistics show that the population who "pick one from batch candidates and own the outcome" has reached hundreds of millions at weekly-or-higher frequency, or the activity is shown to have spread into the everyday decisions of non-professionals.
- **Original leading indicator**: (1) Whether citable global role statistics appear that could replace this card's constructed estimate; (2) whether "generate dozens of candidates at once for the user to pick from" becomes the default interaction in consumer products (that turning true enlarges the activity's headcount and strikes this card directly); (3) whether downstream judgments in this project's C1 chain that depend on "choice becoming scarce" have had their audience voice narrowed per this card; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: J-066, J-067.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: Comparison not completed this round: unknown. This card's audience magnitude comes from a constructed estimate; no citable global role statistics were obtained this round and it was not compared against any external judgment. Per `00-method.md` §1.1 item 4 it is explicitly marked unknown, must not be used as compared, and the three elements are to be completed next round.
- **Original external comparison source**: Comparison not completed this round.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-072` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-073

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L51–L70`；`docs/en/ledger/71-80.md:L51–L70`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1973–L1991`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L51–L70`
- **原始标题**：具身智能是 AI 触及物理劳动人口的必要补足，不是普及的充分条件
- **原始一句话命题**：只要 AI 只能动信息，它的受众天花板就被闸一按在「以屏幕为工作面的那部分人」上；能在现实中移动质量、停留现场、触碰身体是换掉这个分母的**必要补足**，但换掉分母只解开闸一——闸二到闸五一道都不随模型能力自动打开，因此具身能力**不是**社会级普及的充分条件。
- **原始推理链**：闸一的判据只有一句——这项能力服务的动作有多少人在做、多久做一次 → 以屏幕为工作面、以信息为产出物的人在全球就业里是少数（付费能力最强的一批岗位，但不是多数人口），真正的人口分布在必须移动质量、停留现场、触碰身体的地方：农业就业仍以数亿人计（EXT-41）、家政工人是一个以千万计的单列群体（EXT-42）、仅美国一国口径下手工搬运与居家健康助理各以百万计（EXT-43）→ 因此只能动信息的 AI，天花板被按在屏幕职业者上，在那以内可以是一门极好的生意，但按普及闸的读法永远不会成为整个社会的风气 → 换掉分母的唯一路径是让 AI 能动的东西从比特扩展到质量 → **但换掉分母只解开闸一**：闸二要替掉一个今天已经在做的动作（转移机器人替掉「搬动」，没有替掉「陪着」，而买方买的是后者），闸三的承载物是现实空间本身（通道宽度、地面平整度、插接标准、工位改造、田间行距，没有任何人因为别的理由替它建好），闸四要护士、家属、保险与监管同时点头，闸五的准备、监督、清洁、故障处理与社会性尴尬每次都付、不随次数摊薄 → 再看两条曲线：感知与策略沿软件曲线下降（快变量），执行器、减速器、力矩传感器、电池、部署工时与责任定价沿工业与制度曲线下降（慢变量，年降幅通常是个位数百分比）→ 绑定约束因此从「模型能力」迁移到「单位任务成本 + 责任定价 + 部署工时」 → **何时单位任务成本穿越人工**：只在结构化、高频、对象半配合或无生命的格子里先穿越（挤奶、托盘搬运、货到人、固定工位的焊接与喷涂，2026–2030）；非结构化但环境可被改造的格子在 2028–2034；触碰人体与一次性现场在 2032–2040，且先在机构与工地、不在家庭；开放的家庭柔性任务在本窗口内不穿越 → 而穿越只意味着采购部门开始算这笔账，不意味着普及：**局部算得过账 ≠ 社会级普及** → **硬约束**：**物理**（必须移动质量、消耗时间与能量）叠加**产权／私有性**（每个仓库、每块地、每户住宅都是私有且各不相同的现场输入，不能靠算力复制）；这两类都不可能被产生丰富的同一股力量复制掉。
- **原始时间窗**：2026–2040。
- **原始证伪条件**：到 2035 年底，出现可引用的统计显示某项**纯信息型**能力（不移动质量、不到场、不触碰身体）的重复使用者主体已不是以屏幕为工作面的职业人群，并达到十亿人日频或亿级人周频——则「具身是必要补足」这半句被证伪。另一半句另有一条：若到 2033 年底，具身系统的单位任务成本与模型能力同步下降（不再与软件曲线脱钩）、单台部署工时随累计装机量显著下降，且出现覆盖具身作业的通行险种与可查费率，则「不是充分条件」这半句应被收窄。
- **原始领先指标**：① 具身系统的单位任务成本（元／件、元／有效作业小时）时间序列，是否与模型能力的进步曲线脱钩；② 具身作业的专门险种、可查费率与第一批赔付判例；③ 单台部署工时随累计装机量的学习曲线，以及集成商服务收入占设备收入的比例；④ 职业口径（EXT-43 的 53-7062 与 31-1121）的岗位数与工资，在采用密集地区是否先于全国口径出现分化——仅美国观测窗，不可当作全球指标；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-006, J-066, J-067, J-068, J-069, J-070, J-071。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**机制一致，但外部来源只证到两端，中间的到达次序没有任何来源校准。** 一致：IFR 口径显示工厂对机器人的需求在十年里翻了一倍（EXT-45），证明具身能力**可以**真的扩散；Abundant Robotics 在技术做到能下地作业之后仍停掉业务（EXT-46），证明**技术可行不等于商业可行**——第二点与本链的独立推演高度一致，必须诚实标注：**它不是本卡的发现，本卡的增量是给出这类失败的结构性解释（利用率 × 碎片化）与可观察的领先指标。** **分歧与证据边界**：外部材料多数讨论**装机总量**或**单个案例**，本卡讨论的是**到达次序**与**约束位置**，前者推不出后者；本轮未取得的关键数据已逐条记为缺口——各场景的单位任务成本时间序列、具身作业的保险费率与赔付判例、单台部署工时的学习曲线、照护场景的全球部署规模与留存率，四项均无公开可核查口径，本卡因此**不使用**任何精确全球数字。**我为何仍坚持**：核心论证不依赖上述任何一个缺失的数字，它依赖的是一个客观的结构性差异——感知与策略沿软件曲线下降，执行器、部署与责任沿工业与制度曲线下降，两条曲线的斜率差可以被观察；但因为中间的到达次序无人校准，置信度停在「中」，不上调。
- **原始外部对照来源**：EXT-41, EXT-42, EXT-43, EXT-45, EXT-46（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2023–L2041`
- **Current card anchor**: `docs/en/ledger/71-80.md:L51–L70`
- **Original title**: Embodied intelligence is the necessary complement for AI to reach the physical-labour population, not a sufficient condition for diffusion
- **Original one-sentence judgment**: As long as AI can only move information, Gate 1 holds its audience ceiling down to "the share of people whose work surface is a screen"; being able to move mass, be present on site, and touch a human body is the **necessary complement** that changes that denominator, but changing the denominator only opens Gate 1 — Gates 2 through 5 do not open automatically as model capability improves, so embodiment is **not** a sufficient condition for society-level diffusion.
- **Original reasoning chain**: Gate 1's test is a single sentence — how many people perform the activity this capability serves, and how often → people whose work surface is a screen and whose output is information are a **minority** of global employment (the best-paying roles, but not most of the population); the population sits where someone must move mass, stay on site, or touch another person's body: agricultural employment is still **hundreds of millions** (EXT-41), domestic workers are a separately counted group in the **tens of millions** (EXT-42), and in the United States alone hand material movers and home health aides are each **millions**-scale occupations (EXT-43) → therefore an AI that can only move information has its ceiling pinned to screen professionals; inside that ceiling it can be an excellent business, but by the diffusion-gate reading it will never become the way a whole society does things → the only route to a different denominator is to extend what AI can move from bits to mass → **but changing the denominator only opens Gate 1**: Gate 2 demands replacing an activity already performed today (the transfer robot replaced "lifting," not "being there," and what the buyer buys is the latter); Gate 3's carrier is physical space itself (corridor widths, floor flatness, connector standards, workcell retrofits, row spacing — nobody has built any of it for other reasons); Gate 4 requires nurses, families, insurers and regulators to nod at once; Gate 5's preparation, supervision, cleaning, fault handling and social awkwardness are paid on every use and never amortize → then the two curves: perception and policy fall along the software curve (fast variable), while actuators, reducers, torque sensors, batteries, deployment hours and priced liability fall along industrial and institutional curves (slow variables, typically single-digit percent per year) → the binding constraint therefore migrates from "model capability" to **cost per task + priced liability + deployment hours** → **when cost per task crosses labour**: only in squares that are structured, high-frequency, and whose object is semi-cooperative or inanimate does it cross first (milking, pallet handling, goods-to-person, fixed-station welding and painting; 2026–2030); squares that are unstructured but whose environment can be rebuilt cross at 2028–2034; touching human bodies and one-off sites cross at 2032–2040, and first in institutions and on job sites rather than in homes; open-ended household tasks do not cross inside this window → and crossing only means procurement departments start doing the arithmetic, not that the practice diffuses: **beating labour cost locally ≠ society-level diffusion** → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (every warehouse, plot and dwelling is a private, non-identical on-site input that compute cannot copy); neither can be copied away by the same force that produced the abundance.
- **Original time window**: 2026–2040.
- **Original falsifier**: By the end of 2035, citable statistics show that the repeat users of some **purely informational** capability (moving no mass, never present on site, never touching a body) are no longer mainly people whose work surface is a screen, and that they number a billion daily or hundreds of millions weekly — that falsifies the "embodiment is the necessary complement" half. The other half has its own test: if by the end of 2033 cost per task for embodied systems falls in step with model capability (no longer decoupled from the software curve), deployment hours per unit fall markedly with cumulative installed base, and a generally available insurance product with quotable rates covers embodied work, then the "not a sufficient condition" half should be narrowed.
- **Original leading indicator**: (1) the time series of cost per task for embodied systems (per piece, per effective operating hour) and whether it is decoupled from the model-capability curve; (2) dedicated insurance products, quotable rates, and the first liability rulings for embodied work; (3) the learning curve of deployment hours per unit against cumulative installed base, and the ratio of integrator service revenue to equipment revenue; (4) whether headcount and wages in occupational series (EXT-43's 53-7062 and 31-1121) diverge in adoption-dense regions ahead of the national series — a US-only observation window that must not be used as a global indicator; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-066, J-067, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **The mechanism agrees, but external sources only reach the two ends; nothing calibrates the arrival order in between.** Agreement: IFR reports that factory demand for robots doubled over ten years (EXT-45), which proves embodied capability **can** genuinely diffuse; Abundant Robotics shut its business down after reaching field-capable apple harvesting (EXT-46), which proves **technical feasibility is not commercial feasibility** — the second point coincides closely with this chain's independent reasoning and must be labelled honestly: **it is not this card's discovery; this card's increment is a structural explanation of such failures (utilization × fragmentation) plus observable leading indicators.** **Divergence and evidence boundary**: most external material discusses **installed totals** or **single cases**, while this card is about **arrival order** and **where the constraint sits**, and the former does not imply the latter; the key data not obtained this round is recorded as explicit gaps — cost-per-task time series by scene, insurance rates and liability rulings for embodied work, the learning curve of deployment hours per unit, and deployment scale and retention in care — none of which has a publicly checkable definition, so this card **uses** no precise global figure at all. **Why the judgment is retained**: the core argument depends on none of those missing numbers; it depends on an objective structural difference — perception and policy fall along the software curve while actuators, deployment and liability fall along industrial and institutional curves — and the gap between those slopes can be observed. But because nobody has calibrated the arrival order in between, confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-41, EXT-42, EXT-43, EXT-45, EXT-46 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-073` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-074

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L71–L90`；`docs/en/ledger/71-80.md:L71–L90`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L1992–L2010`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L71–L90`
- **原始标题**：照护里的接触式转移先在机构穿越，居家在本窗口内不构成社会级普及
- **原始一句话命题**：照护是需求最确定的一格，但挡住它的不是「能不能抱起来」，而是「抱起来的全过程里人是活的」与每一次使用都要重新付出的持续代价；接触式床椅转移成为机构常规配置不早于 2032–2038，且先出现在人力成本与护理工伤赔付压力最高的少数国家，居家场景在本窗口（到 2040）内不构成社会级普及。
- **原始推理链**：人口结构把照护推成需求最确定的一格（需要被照护的人在增加，愿意做这份工作的人在减少），且这个缺口无法靠信息处理填补——没有人能在屏幕上把一位老人从床上抱到轮椅上 → 技术瓶颈不在负载而在「人是活的」：同一转移动作对不同体重、肌张力、疼痛耐受需要完全不同的力矩轨迹，被照护者会中途改变姿势、会抗拒、会突然放松，要求毫米级位置精度与牛顿级力控在同一回路里并以人体安全裕度为约束 → 理研 ROBEAR 在 2015 年已经把能力侧的可行性演示清楚（EXT-44），十年过去它仍不是病房里的常规设备，**十年的空白本身就是证据：挡住这一格的不是能力** → 挡住它的是闸五：准备、监督、清洁、解释、安抚每次都要付且不随次数摊薄（链文第一节那台被退回的机器，试用第一周十二次转移零夹伤，退回理由里一个字也没提价格）→ 叠加闸三：居家还需要门宽、地面与卫生间改造，没有人因为别的理由替它建好 → 叠加闸四：一台机器人进病房要护士、家属、保险公司与监管方同时点头 → **何时单位任务成本穿越人工**：完全可以想象某个高工资国家的大型机构把单次转移成本压到低于两名护工的工时成本，那一刻账算得过来，但闸五与闸三仍然横着——**穿越只意味着机构采购部门开始算这笔账，不意味着这件事普及到大多数被照护的人身上** → **硬约束**：**身体在场**（需求本身要求有人真实地到场与触碰）叠加**法律／责任**（一次转移事故的赔付主体必须存在且可被起诉）；把护理排班、用药核对、跌倒风险评分全部自动化，也不会减少一次必须发生的身体转移。
- **原始时间窗**：2026–2038。
- **原始证伪条件**：到 2031 年底，接触式床椅转移机器人已在任一主要照护市场成为机构常规配置（以保险报销编码、人力配置折算或该国机构装机覆盖率可核实）——则本卡的时间窗下沿被证伪；或到 2040 年前，居家接触式转移达到亿级家庭的日频使用——则本卡的居家判断被证伪。
- **原始领先指标**：① 监管侧是否出现「接触式转移机器人」的独立审批路径与保险报销编码——没有报销编码，机构只能用自有预算买，采用曲线会一直平；② 护理人力配置标准里设备能否被折算为人力（决定 ROI 的是这一行，不是设备价格）；③ 采用密集机构的护理人员腰背工伤赔付率是否下降——最难伪造的指标，因为它由保险公司而非厂商统计；④ ROBEAR 一类原型是否出现进入量产的后继型号；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-073, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**一致**：ROBEAR 一类原型（EXT-44）证明接触式转移在能力侧的可行性十年前已被演示，这正是「空白不能用能力解释」的前提；美国职业口径把居家健康助理列为增长最快的一批岗位（EXT-43），与「需求最确定」一致。**分歧与证据边界**：外部材料只证明单个原型与单国岗位前景，不覆盖**到达次序**；本轮未查到 ROBEAR 之后是否存在量产后继型号，也没有照护场景的全球部署规模与留存率的可核查来源，两项均记为缺口；EXT-43 只覆盖美国，不可外推全球。**我为何仍坚持**：本卡的论证不依赖部署规模数字，它依赖的是持续代价不摊薄与赔付主体必须可被起诉这两条，二者都不随模型能力打开；但因为缺少部署与留存数据，置信度停在「中」。
- **原始外部对照来源**：EXT-43, EXT-44（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2042–L2060`
- **Current card anchor**: `docs/en/ledger/71-80.md:L71–L90`
- **Original title**: Contact transfer in care crosses inside institutions first, and homes reach no society-level diffusion inside this window
- **Original one-sentence judgment**: Care is the square with the most certain demand, but what blocks it is not "can it lift" — it is "the person is alive throughout" plus the cost paid afresh on every single use; contact bed-to-chair transfer becomes standard institutional equipment no earlier than 2032–2038, and first in the handful of countries with the highest labour costs and heaviest nursing-injury compensation exposure, while home settings reach no society-level diffusion inside this window (to 2040).
- **Original reasoning chain**: Demographics make care the most certain demand (the number of people needing care rises, the number willing to do the work falls), and the gap cannot be closed by processing information — nobody lifts an elderly person from a bed into a wheelchair through a screen → the technical bottleneck is not load but that the person is alive: the same transfer needs a completely different torque trajectory for different weights, muscle tone and pain tolerance, and the person shifts posture, resists, or suddenly goes slack, which demands millimetre-scale position accuracy and newton-scale force control in one loop bounded by a human safety margin → Riken's ROBEAR demonstrated the capability side clearly in 2015 (EXT-44), and a decade later it is still not standard ward equipment: **the decade of silence is itself the evidence that what blocks this square is not capability** → what blocks it is Gate 5: preparation, supervision, cleaning, explaining and reassuring are paid every time and never amortize (the machine sent back in the chain's opening section completed twelve transfers in its first week with no pinch injury, and price appears nowhere in the reason it was returned) → compounded by Gate 3: a home additionally needs door widths, floors and bathrooms rebuilt, and nobody has built them for other reasons → compounded by Gate 4: putting a robot in a ward needs nurses, families, insurers and regulators to nod at once → **when cost per task crosses labour**: it is entirely plausible that a large institution in a high-wage country pushes the per-transfer cost below the wage cost of two aides, and at that moment the numbers work — while Gates 5 and 3 still stand in the way, so **crossing only means the procurement department starts doing the arithmetic, not that the practice reaches most of the people receiving care** → **Hard constraints**: **embodied presence** (the need itself requires someone to be physically there and to touch) compounded by **law / liability** (a party capable of being sued must carry a transfer accident); automating rostering, medication checks and fall-risk scoring completely removes not one transfer that must physically happen.
- **Original time window**: 2026–2038.
- **Original falsifier**: By the end of 2031, contact bed-to-chair transfer robots are standard institutional equipment in any major care market (verifiable through a reimbursement code, counting equipment against required staffing, or national installed-base coverage) — that falsifies this card's lower bound; or, before 2040, home contact transfer reaches daily use in hundreds of millions of households — that falsifies this card's home judgment.
- **Original leading indicator**: (1) whether regulators open a distinct approval pathway for contact transfer robots and whether a reimbursement code exists — without reimbursement, institutions buy from their own budget and the adoption curve stays flat; (2) whether staffing standards allow equipment to be counted against required headcount (that is the line that decides ROI, not the purchase price); (3) whether back-injury compensation rates fall in institutions with dense adoption — the hardest indicator to fake, because insurers rather than vendors produce it; (4) whether a production successor to a ROBEAR-class prototype ever appears; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: a ROBEAR-class prototype (EXT-44) proves the capability side of contact transfer was demonstrated a decade ago, which is the premise for "the silence cannot be explained by capability"; US occupational data lists home health aides among the fastest-growing occupations (EXT-43), consistent with "the most certain demand." **Divergence and evidence boundary**: the external material establishes one prototype and one country's occupational outlook, and covers no **arrival order**; this round found no checkable source on whether a production successor to ROBEAR exists, and none on deployment scale or retention in care worldwide — both recorded as gaps; EXT-43 covers the United States only and cannot be extrapolated globally. **Why the judgment is retained**: the argument depends on no deployment-scale figure; it depends on recurring costs that do not amortize and on a compensable party that must be suable, neither of which opens as model capability improves. But with deployment and retention data missing, confidence stays at Medium.
- **Original external comparison source**: EXT-43, EXT-44 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-074` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-075

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L91–L110`；`docs/en/ledger/71-80.md:L91–L110`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2011–L2029`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L91–L110`
- **原始标题**：仓储的瓶颈已从移动移到抓取，非结构化拣选先到，门到门交付在本窗口内不成立
- **原始一句话命题**：仓储是具身智能最先算得过账的地方（货物不会疼、仓库归一个法人所有、地面是平的），真正卡住的是非结构化拣选的长尾失败代价；受控大仓的规模化单件拣选保守放在 2028–2033，而门到门的最后一公里交付在本窗口内不成立，因为它同时踩中闸三与闸四。
- **原始推理链**：结构化仓库里的自主移动基本是解决过的问题（地面平整、路径可标定、异常可停机）→ 真正卡住的是**非结构化拣选**：混杂 SKU、透明与反光包装、柔性袋装、堆叠遮挡、料箱底部的最后一件 → 难点不在平均成功率，而在**长尾失败的代价**：一次抓空只是慢几秒，一次抓漏导致错发，成本是整条履约链的返工与信誉 → 因此这一格的工程目标不是「能抓」，是每小时多少件、错误率多少、失败后谁来接手 → 结构化搬运、托盘作业与「货到人」已经在扩散（2026–2028 继续），非结构化单件拣选在受控大仓的规模化保守放在 2028–2033 → 门到门交付要面对楼梯、门禁、雨天、狗与无人看管的包裹：承载物是别人的楼道（闸三），且要物业、住户、平台同时改变（闸四），在本窗口内不成立 → **何时单位任务成本穿越人工**：单个高吞吐、单班次稳定、SKU 规整的大仓，ROI 现在就能算过来；判据是**按件计费**合同（元／拣选件，含错误率赔付）是否出现——厂商自己愿意为长尾失败定价，是成熟最诚实的信号 → 但全球仓储的长尾是中小仓库：低吞吐、货品混杂、季节性波动大、停机一天就影响全部订单，**资本开支摊不薄、停机风险摊不掉，而这恰恰是绝大多数搬运岗位所在的地方**；把大仓的账当成行业的账，就是把闸一算反了——算的是设备能进多少个仓，不是能替掉多少人的动作 → **硬约束**：**物理**（必须移动质量、消耗时间与能量）叠加**产权／私有性**（仓库布局、SKU 主数据与订单流是私有资产，任何改造都要业主同意，而谈判成本不随模型能力下降）。
- **原始时间窗**：2026–2033。
- **原始证伪条件**：到 2028 年底，非结构化单件拣选已在受控大仓规模化（按件计费加错误率赔付条款成为该细分的主流商业模式）——则本卡的中段时间窗被证伪；或到 2033 年底，门到门的机器人交付在任一主要市场成为主流配送方式（占该市场包裹量的多数）——则本卡的最后一公里判断被证伪。
- **原始领先指标**：① 商业模式是否从「卖设备」转向**按件计费**（含错误率赔付）；② 第三方物流的保险条款是否为「机器人拣选」单列费率；③ 单仓的部署工时是否随累计装机量下降；④ 在采用密集地区，O\*NET 53-7062（EXT-43）一类岗位的招聘量与工资是否先于全国口径出现分化；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-073, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**一致**：美国职业口径证明「手工搬运货物、库存与物料」确实是以百万计的大类岗位且有官方口径可查（EXT-43），支撑本卡分母的存在性，也支撑把岗位数与工资当作领先指标。**分歧与证据边界**：EXT-43 只覆盖美国一国，不可外推全球；本轮未取得非结构化拣选的装机量、按件计费合同渗透率与单仓部署工时的公开口径，本卡因此不给出任何精确数字，只给到达次序与可观察指标。**我为何仍坚持**：长尾失败的代价与逐个业主的谈判成本这两条都不随模型能力下降，机制清楚；但因为关键指标目前没有公开数据，置信度停在「中」。
- **原始外部对照来源**：EXT-43（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2061–L2079`
- **Current card anchor**: `docs/en/ledger/71-80.md:L91–L110`
- **Original title**: Warehousing's bottleneck has moved from moving to grasping: unstructured picking arrives first and door-to-door delivery does not hold inside this window
- **Original one-sentence judgment**: Warehousing is where embodied intelligence pencils out first (goods feel no pain, the building belongs to one legal entity, the floor is flat), and what is actually stuck is the cost of the failure tail in unstructured picking; scaled single-item picking in controlled large warehouses sits conservatively at 2028–2033, while door-to-door last-mile delivery does not hold inside this window because it trips Gate 3 and Gate 4 at once.
- **Original reasoning chain**: Autonomous mobility inside a structured warehouse is largely a solved problem (flat floors, mappable paths, stop-on-anomaly) → what is stuck is **unstructured picking**: mixed SKUs, transparent and reflective packaging, soft polybags, occluded stacks, the last item at the bottom of a tote → the difficulty is not average success rate but **the cost of the failure tail**: a missed grasp costs seconds, a mis-pick costs a rework of the whole fulfilment chain plus reputation → so the engineering target is not "can it pick" but picks per hour, error rate, and who takes over after a failure → structured movement, pallet handling and goods-to-person are already diffusing (continuing through 2026–2028), while scaled unstructured single-item picking in controlled large warehouses sits conservatively at 2028–2033 → door-to-door delivery faces stairs, entry systems, rain, dogs and unattended parcels: the carrier is someone else's stairwell (Gate 3) and building management, residents and platforms must all change (Gate 4), so it does not hold inside this window → **when cost per task crosses labour**: a single high-throughput, single-shift, tidy-SKU warehouse already pencils out, and the test is whether **per-pick pricing** appears (per picked item, with error-rate damages) — a vendor willing to price its own failure tail is the most honest signal of maturity → but the tail of global warehousing is small and mid-sized sites: low throughput, mixed goods, seasonal swings, a day of downtime hitting every order, so **capex does not amortize and downtime risk cannot be spread — and that is exactly where most material-handling jobs are**; treating the large-warehouse case as the sector's case inverts Gate 1, counting how many warehouses a machine can enter rather than how many people's activity it can replace → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (layout, SKU master data and order flow are private assets, any retrofit needs the owner's consent, and negotiation cost does not fall with model capability).
- **Original time window**: 2026–2033.
- **Original falsifier**: By the end of 2028, unstructured single-item picking is operating at scale in controlled large warehouses (per-pick pricing with error-rate damages having become the mainstream commercial model in that segment) — that falsifies this card's mid-segment window; or by the end of 2033 robotic door-to-door delivery is the mainstream delivery mode in any major market (a majority of that market's parcels) — that falsifies this card's last-mile judgment.
- **Original leading indicator**: (1) whether the commercial model shifts from selling machines to **per-pick pricing** with error-rate damages; (2) whether third-party logistics insurance quotes a separate rate for robotic picking; (3) whether deployment hours per site fall as the installed base grows; (4) whether hiring volumes and wages in occupations like O\*NET 53-7062 (EXT-43) diverge in adoption-dense regions ahead of the national series; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: US occupational data proves that "hand laborers and freight, stock and material movers" really is a millions-scale occupation with an official definition to cite (EXT-43), which supports the existence of this card's denominator and the use of headcount and wages as leading indicators. **Divergence and evidence boundary**: EXT-43 covers the United States only and cannot be extrapolated globally; this round obtained no public figures on the installed base of unstructured picking, the penetration of per-pick contracts, or deployment hours per site, so this card gives no precise numbers at all — only arrival order and observable indicators. **Why the judgment is retained**: the cost of the failure tail and the per-owner negotiation cost are both independent of model capability, and the mechanism is clear; but with no public data on the key indicators, confidence stays at Medium.
- **Original external comparison source**: EXT-43 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-075` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-076

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L111–L130`；`docs/en/ledger/71-80.md:L111–L130`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2030–L2048`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L111–L130`
- **原始标题**：制造业已经发生的规模化过的是闸四的局部闭环，柔性装配与小批量多品种仍在闸外
- **原始一句话命题**：制造业是唯一能直接引用「机器人已经规模化」的场景，但那次规模化过的是闸四的第 (c) 条局部闭环，且只发生在重复动作、刚性工件、可标定位置、固定节拍这组边界条件之内；柔性装配在大批量产线的常规化保守放在 2028–2034，小批量多品种的中小制造企业在本窗口内只在集成商生态密集的少数产业带局部成立，不构成社会级普及。
- **原始推理链**：IFR 口径显示工厂对机器人的需求在十年里翻了一倍（EXT-45）→ 这条事实必须被两面使用：它既证明具身能力可以真的扩散，也**画出了扩散发生的边界条件** → 扩散发生在焊接、喷涂、上下料、码垛（动作重复、工件刚性、位置可标定、节拍固定），没有发生在柔性装配（线束要顺着形变走、连接器插不进去时要知道回退多少再试、软胶件的公差每件不同；人靠手上的即时反馈，机器要靠力控加容差补偿，而这套东西目前的成本与调试工时都高得不成比例）→ 更隐蔽的瓶颈是**换线**：大批量单一产品的产线摊得起一次示教，小批量多品种摊不起——每次产品变更都要重新编程、重新标定、重新验证安全 → 这就是为什么机器人密度与**批量规模**的相关性远强于它与工资水平的相关性 → **何时单位任务成本穿越人工**：在批量足够大、节拍固定的产线上早已穿越（这正是 IFR 曲线的含义）；在小批量多品种处不穿越，因为同一次示教能被摊薄的件数太少 → 但要看清那次规模化过的是**闸四第 (c) 条局部闭环**：一个工厂内部就能先跑通，不必等全社会；**工厂之所以能局部闭环，是因为它是一个有围墙、有单一决策者、有统一标准的空间，而照护、农业、建筑、家庭都没有这堵墙** → 用工厂的扩散速度推断其他四格，等于假设那堵墙免费存在 → **硬约束**：**物理**叠加**产权／私有性**（产线是特定业主的私有资产，改造由业主决定，且改造期间的停产损失由业主独自承担）。
- **原始时间窗**：2026–2034。
- **原始证伪条件**：到 2030 年底，IFR 一类口径中新装机的**结构**显示「装配／精密操作」占比已超过搬运码垛类，且小批量多品种的中小制造企业同步扩散（以换型时间系统性下降、集成商服务收入占设备收入比例下降为证）——则「柔性装配 2028–2034、小批量多品种更慢」被证伪。
- **原始领先指标**：① IFR 这类口径里新装机的**结构**是否向装配／精密操作倾斜——只看总量会把码垛的增长误读成装配的突破；② 单条产线的换型时间是否系统性下降；③ 集成商的服务收入占设备收入的比例（居高不下说明部署成本仍由现场人工承担，规模效应没有出现）；④ 二手工业机器人的残值曲线（残值高说明可再部署性强，是碎片化被克服的信号）；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-073, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**一致**：IFR 是本链唯一能直接引用的规模化证据（EXT-45），它支持「具身能力可以真的扩散」这一前提的存在性。**分歧与证据边界**：IFR 口径是**装机总量**，本卡讨论的是**到达次序与边界条件**，总量推不出结构；本轮未取得按应用类型拆分的新装机结构、换型时间序列与二手残值曲线，三项均记为缺口。**我为何仍坚持**：边界条件（重复动作、刚性工件、可标定、固定节拍、单一决策者）可以从扩散发生与未发生的两侧对照读出，机制清楚；但因为缺少结构拆分数据，置信度停在「中」，不上调。
- **原始外部对照来源**：EXT-45（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2080–L2098`
- **Current card anchor**: `docs/en/ledger/71-80.md:L111–L130`
- **Original title**: Manufacturing's one real scaling passed through Gate 4's local closed loop; flexible assembly and high-mix low-volume are still outside the gate
- **Original one-sentence judgment**: Manufacturing is the only scene where "robots already scaled" can be cited directly, but that scaling passed through Gate 4's clause (c), the local closed loop, and happened only inside one set of boundary conditions — repetitive motions, rigid workpieces, calibratable positions, fixed takt; flexible assembly becoming routine on high-volume lines sits conservatively at 2028–2034, and high-mix low-volume small and mid-sized manufacturers hold inside this window only locally, in the few industrial clusters with dense integrator ecosystems, which is not society-level diffusion.
- **Original reasoning chain**: IFR reports that factory demand for robots doubled over ten years (EXT-45) → that fact must be used in both directions: it proves embodied capability really can diffuse, and it **draws the boundary conditions under which the diffusion happened** → diffusion happened in welding, painting, machine tending and palletizing (repetitive motions, rigid workpieces, calibratable positions, fixed takt) and did not happen in flexible assembly (a wire harness must be routed as it deforms, a connector must know how far to back off and retry when it will not seat, every soft gasket has a different tolerance; humans work on immediate tactile feedback while machines need force control plus tolerance compensation, and today that stack costs disproportionately in both hardware and commissioning hours) → the subtler bottleneck is **changeover**: a high-volume single-product line amortizes one teaching pass, a high-mix low-volume shop does not, because every product change means reprogramming, recalibrating and re-validating safety → which is why robot density correlates far more strongly with **batch size** than with wage levels → **when cost per task crosses labour**: it crossed long ago on lines with large enough batches and fixed takt (that is what the IFR curve means), and it does not cross in high-mix low-volume work because too few pieces amortize one teaching pass → but look at which gate that scaling passed: **Gate 4's clause (c), the local closed loop** — a single factory can make it work internally without waiting for society; **a factory can close the loop because it is a walled space with one decision-maker and one standard, and care, agriculture, construction and homes have no such wall** → extrapolating the factory's diffusion rate to the other four squares assumes that wall is free → **Hard constraints**: **physical** compounded by **ownership / privacy** (a production line is a specific owner's private asset, the retrofit is theirs to authorize, and the lost output during the retrofit is theirs alone to absorb).
- **Original time window**: 2026–2034.
- **Original falsifier**: By the end of 2030, the **composition** of new installations in IFR-class series shows assembly and precision manipulation exceeding handling and palletizing, and high-mix low-volume small and mid-sized manufacturers diffuse in step (evidenced by systematically falling changeover time and a falling ratio of integrator service revenue to equipment revenue) — that falsifies "flexible assembly at 2028–2034, high-mix low-volume slower."
- **Original leading indicator**: (1) whether the **composition** of new installations in series like IFR's tilts toward assembly and precision manipulation — reading totals alone mistakes palletizing growth for an assembly breakthrough; (2) whether line changeover time falls systematically; (3) the ratio of integrator service revenue to equipment revenue (a ratio that stays high says deployment cost is still carried by on-site labour and the scale effect has not arrived); (4) the residual-value curve for used industrial robots (high residuals signal redeployability, the signal that fragmentation is being overcome); annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: IFR is the only directly citable evidence of scaling in this chain (EXT-45), and it supports the existence of the premise that embodied capability can genuinely diffuse. **Divergence and evidence boundary**: IFR's series is an **installed total**, while this card is about **arrival order and boundary conditions**, and a total does not imply a composition; this round obtained no public series for new-installation composition by application type, changeover time, or used-robot residual values — all three recorded as gaps. **Why the judgment is retained**: the boundary conditions (repetitive motion, rigid workpiece, calibratable, fixed takt, one decision-maker) can be read off by contrasting where diffusion happened with where it did not, and the mechanism is clear; but with the composition breakdown missing, confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-45 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-076` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-077

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L131–L150`；`docs/en/ledger/71-80.md:L131–L150`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2049–L2067`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L131–L150`
- **原始标题**：农业里穿越的是挤奶不是采摘，季节性与碎片化把单位任务成本卡在人工之上
- **原始一句话命题**：自动挤奶已在高工资国家的中大型牧场成为常规设备，因为动作每天重复、地点固定、对象会自己走进设备、产出可计量、失败可控；选择性采摘在本窗口内仍以局部试点与单一作物为主、2030 年前不构成主流作业方式，因为季节性把分母压到极小、碎片化又把适配成本抬高。
- **原始推理链**：先看已经穿越的挤奶，把条件列出来才知道有多苛刻——动作每天重复两到三次、地点固定、**对象会自己走进设备**、产出物可计量可定价、失败后果可控（一次失败就是少挤一头）；**奶牛是半配合的对象，这一条几乎是免费的补贴** → 再看已经失败的选择性采摘：Abundant Robotics 把苹果采摘做到能下地作业的程度，公司仍然停掉了这块业务（EXT-46）→ 这不是能力故事，是**利用率**故事：一台采摘机一年只在几周的收获窗口里工作，资本开支要摊到那几周的作业小时上；而果园的行距、树形、品种各不相同，每换一个果园就要重新适配 → **季节性把分母压到极小，碎片化又把分子的适配成本抬高——两头夹击，单位任务成本降不下来** → 技术瓶颈另有三条：自然光照与遮挡下的感知鲁棒性、末端执行器对易损产物的处理（苹果碰伤就降级，草莓更甚）、生物变异（同一棵树上没有两个果实的位置与成熟度相同）→ **何时单位任务成本穿越人工**：只在高频、固定、对象半配合的结构化作业上穿越（挤奶、导航播种施肥、行内机械除草；2026–2030 是规模化窗口）；选择性采摘只有在年有效作业小时数显著上升（跨作物、跨季节复用）之后才可能穿越 → 全球尺度上，农业具身化的绝大部分潜在对象并不在高工资国家的资本密集农场里（EXT-41），这决定了社会级普及的时间窗要比设备可行性的时间窗晚一代人 → 因此「农业机器人已被证明可行」是一句危险的话：**被证明的是挤奶，不是采摘** → **硬约束**：**物理**（必须在田间移动、受天气与季节窗口约束，能量与时间不可压缩）叠加**产权／私有性**（每块地、每个果园的物理布局是私有且各不相同的输入，不能靠算力复制）。
- **原始时间窗**：2026–2030。
- **原始证伪条件**：到 2030 年底，选择性采摘在任一主要产区的主要作物上成为主流作业方式——以机器采摘占该作物该产区采收量的多数，或按亩／按产量计费的采摘服务出现规模化复购为证。
- **原始领先指标**：① 采摘设备是否以按亩或按产量收费的服务模式获得**复购**（复购比首单更能说明账算得过来）；② 设备的**年有效作业小时数**是否上升（跨作物、跨季节复用是唯一能救利用率的路径）；③ 农忙季短期工工资在采用密集产区是否先于全国口径出现分化；④ 保险与农协是否为机器作业的减产风险提供产品；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-073, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**一致**：Abundant Robotics 在技术可行之后仍停掉业务（EXT-46），支持「技术可行不等于商业可行」；FAO 就业指标支持农业就业仍以数亿人计、且在中低收入国家占比显著更高（EXT-41），支持本卡关于分母位置的判断。**分歧与证据边界**：EXT-46 是单个公司案例，不构成整类技术的统计；FAO 只取**量级**不取精确数值，其口径、年份与统计边界以来源本身为准；本轮未取得采摘设备的装机量与复购数据。**我为何仍坚持**：挤奶与采摘是同一产业内部、同一时期的天然对照，穿越条件（高频、固定、对象半配合）可以被逐条检验；但失败侧只有单案例支撑，置信度停在「中」。
- **原始外部对照来源**：EXT-41, EXT-46（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2099–L2117`
- **Current card anchor**: `docs/en/ledger/71-80.md:L131–L150`
- **Original title**: In agriculture what crossed is milking, not harvesting: seasonality and fragmentation hold cost per task above labour
- **Original one-sentence judgment**: Automatic milking is already standard equipment on mid-to-large dairy farms in high-wage countries because the action repeats daily, the location is fixed, the animal walks into the machine by itself, the output is measurable and failure is contained; selective harvesting stays at local pilots on single crops inside this window and does not become a mainstream practice before 2030, because seasonality crushes the denominator while fragmentation inflates the adaptation cost.
- **Original reasoning chain**: Start with milking, which crossed, and list the conditions to see how strict they are — the action repeats two or three times a day, the location is fixed, **the animal walks into the machine by itself**, the output is measurable and priceable, and failure is contained (one missed cow); **a cow is a semi-cooperative object, and that condition is close to a free subsidy** → then selective harvesting, which failed: Abundant Robotics took apple harvesting to the point of working in orchards and still shut the business down (EXT-46) → this is not a capability story but a **utilization** story: a harvester works a few weeks a year and its capex must amortize over those weeks' operating hours, while row spacing, tree architecture and variety differ between orchards so every new customer means re-adaptation → **seasonality crushes the denominator, fragmentation inflates the adaptation cost in the numerator — squeezed from both ends, cost per task does not fall** → three further technical bottlenecks: perception robustness under natural light and occlusion, end effectors handling damageable produce (a bruised apple is downgraded, a strawberry more so), and biological variation (no two fruits on one tree share a position or a ripeness) → **when cost per task crosses labour**: only on structured operations that are high-frequency, fixed and semi-cooperative (milking, guided seeding and fertilizing, intra-row mechanical weeding; 2026–2030 is the scaling window); selective harvesting can cross only after annual effective operating hours rise markedly through cross-crop, cross-season reuse → globally, most of the potential object of agricultural embodiment is not on capital-intensive farms in high-wage countries at all (EXT-41), which puts society-level diffusion a generation behind equipment feasibility → so "agricultural robotics is proven" is a dangerous sentence: **what is proven is milking, not harvesting** → **Hard constraints**: **physical** (the machine must move through a field, bounded by weather and a seasonal window; energy and time are incompressible) compounded by **ownership / privacy** (each plot and orchard is a private, unique physical layout that compute cannot copy).
- **Original time window**: 2026–2030.
- **Original falsifier**: By the end of 2030, selective harvesting is the mainstream practice for a major crop in any major growing region — evidenced either by machine harvesting taking a majority of that crop's harvested volume in that region, or by per-acre or per-yield harvesting services earning repeat business at scale.
- **Original leading indicator**: (1) whether harvesting equipment earns **repeat business** under a per-acre or per-yield service model (repeat orders say more than first orders about whether the numbers work); (2) whether **annual effective operating hours** per machine rise (cross-crop, cross-season reuse is the only route that rescues utilization); (3) whether seasonal wages diverge in adoption-dense growing regions ahead of the national series; (4) whether insurers or grower cooperatives offer products covering yield loss from machine operation; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: Abundant Robotics shutting down after the technology worked (EXT-46) supports "technical feasibility is not commercial feasibility"; FAO's employment indicators support agricultural employment still being hundreds of millions with a markedly higher share in low- and middle-income countries (EXT-41), which supports where this card places the denominator. **Divergence and evidence boundary**: EXT-46 is a single company case and constitutes no statistic over the class; FAO is used for **orders of magnitude** only, with its definitions, years and statistical boundaries as given in the source; this round obtained no installed-base or repeat-purchase data for harvesting equipment. **Why the judgment is retained**: milking versus harvesting is a natural control pair inside one industry in one period, and the crossing conditions (high frequency, fixed location, semi-cooperative object) can be checked one by one; but with only a single case on the failure side, confidence stays at Medium.
- **Original external comparison source**: EXT-41, EXT-46 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-077` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-078

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L151–L170`；`docs/en/ledger/71-80.md:L151–L170`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2068–L2090`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L151–L170`
- **原始标题**：建筑与家政被一次性现场与别人的家挡住，本窗口内只以单工序设备与单任务切片到达
- **原始一句话命题**：建筑与家政共享同一个最难的性质——作业环境每一次都不同，而且不归执行者所有；到 2040 年，现场建筑机器人仍以单工序设备为主、不构成对工地整体流程的替代，家庭的开放柔性任务不构成社会级普及，家庭具身化会继续以单任务切片（扫地、洗碗、割草）的形式推进。
- **原始推理链**：**建筑**——工地是一次性的：每个项目的几何、地质、工序交叉与天气都不重复，公差以厘米计而不是毫米计，且多工种在同一空间里互相等待 → FBR 的 Hadrian 砌砖机是这一格最诚实的标本（EXT-47）：这个方向已经推进了十年量级的时间，仍处在单点作业与示范项目阶段 → 挡住它的不只是砌砖速度：**一台机器砌得再快，也要等前道工序、等验收、等许可、等天气** → 建筑真正的结构性路径是绕过工地——把作业搬进工厂化预制车间，也就是把「一次性现场」改造成「结构化空间」，那样它就退化成 J-076 的制造问题 → **家政**——最难的一格，难点甚至不在执行，在**任务定义**：「收拾一下」包含物品归类、价值判断（哪件是垃圾、哪件是纪念品）、隐私边界与家庭内部的约定 → ILO 口径下家政工人是一个以千万计的群体（EXT-42），说明需求真实存在且已经在被付费购买——但被购买的从来不只是动作，还包括判断力、可信度和不需要交代细节的默契 → 失败还不可逆：打碎的不是杯子，是「这个杯子」（L6）→ **何时单位任务成本穿越人工**：即便 Hadrian 一类设备在某些标准化住宅上把砌筑的单位成本压到人工以下，社会级普及要求的是**整条工地流程、保险费率与验收制度同时改变**——那是闸四的多方协同，不是设备性能问题；家政同理，一台机器在演示视频里叠好衣服，与一亿个家庭愿意让它每天进卧室之间，隔着产权、信任与每一次使用的持续代价 → **硬约束**：建筑——**法律／许可**（施工许可、验收、工伤责任必须落在可被起诉的主体上）叠加**物理**；家政——**产权／私有性**（别人的家是私有空间，进入需要授权）叠加**信任／关系**（把钥匙交给谁，是长期重复博弈的结果，不能一次生成）。
- **原始时间窗**：2026–2040。
- **原始证伪条件**：到 2040 年前，现场建筑机器人替代的已不是单工序而是工地整体流程（以总承包合同中由机器人承担的工序数与工期占比可核实）——则本卡的建筑判断被证伪；或通用家用机器人在任一国家达到多数家庭日频执行**开放柔性任务**（而不是扫地、洗碗、割草这类单任务切片）——则本卡的家政判断被证伪。
- **原始领先指标**：建筑——① 总承包商的保险费率是否为机器人作业单列；② 工期合同中是否出现机器人设备的违约与停工条款；③ 预制率（工厂完成的工序占比）是否持续上升。家政——④ 通用家用机器人的价格是否跌入耐用消费品区间**并且**单次任务的持续代价足够低（不需要事前收拾、不需要全程监督）；⑤ 高采用国家的家政工人规模与工资是否出现分化；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-073, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C4：具身智能`。
- **原始外部对照判断**：**一致**：FBR Hadrian 推进十年量级仍停在单点作业与示范项目（EXT-47），支持「挡住现场建筑的不是砌砖速度」；ILO 把家政工人单列为一个以千万计、且很大一部分处于非正规就业的群体（EXT-42），支持需求真实存在且已被付费购买。**分歧与证据边界**：两者都是**单个案例或单个群体口径**，不覆盖到达次序；ILO 的统计边界与年份以来源本身为准，本卡只取量级；本轮未取得预制率、机器人作业保险费率与家用机器人单次任务持续代价的可核查序列。**我为何仍坚持**：本卡依赖的是两条不随模型能力打开的约束——许可与责任必须落在可被起诉的主体上，以及进入私有空间需要授权与长期信任；但作为一条到 2040 年的否定性判断，它的可检验性弱于本链中段的判断，置信度因此停在「中」，不上调。
- **原始外部对照来源**：EXT-42, EXT-47（见上方来源索引）。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2118–L2140`
- **Current card anchor**: `docs/en/ledger/71-80.md:L151–L170`
- **Original title**: Construction and domestic work are blocked by the one-off site and somebody else's home: inside this window they arrive only as single-operation equipment and single-task slices
- **Original one-sentence judgment**: Construction and domestic work share the hardest property — the work environment is different every time and does not belong to whoever is working in it; through 2040 on-site construction robots remain single-operation equipment and do not substitute for the site process as a whole, open-ended household tasks reach no society-level diffusion, and home embodiment continues as single-task slices (vacuuming, dishwashing, mowing).
- **Original reasoning chain**: **Construction** — a site is one-off: geometry, ground conditions, trade sequencing and weather never repeat, tolerances are in centimetres rather than millimetres, and multiple trades wait on each other in one space → FBR's Hadrian bricklaying machine is the most honest specimen here (EXT-47): a direction pushed for something on the order of a decade, still at single-operation and demonstration-project scale → what blocks it is not laying speed: **however fast a machine lays brick, it still waits on the preceding trade, on inspection, on permits and on weather** → construction's real structural path is to bypass the site — move the work into a prefabrication plant, converting the one-off site into structured space, at which point it degenerates into the manufacturing problem of J-076 → **Domestic work** — the hardest square, and the difficulty is not even execution but **task definition**: "tidy up" contains classification, value judgment (which object is rubbish and which is a keepsake), privacy boundaries and household-specific conventions → on ILO's count domestic workers are a group in the tens of millions (EXT-42), so the demand is real and already being paid for — but what is bought was never only the motions; it includes judgment, trustworthiness and the tacit understanding that saves the employer from specifying anything → and failure is irreversible: what breaks is not *a* cup, it is *that* cup (L6) → **when cost per task crosses labour**: even if a Hadrian-class machine pushes the unit cost of bricklaying below manual labour on some standardized houses, society-level diffusion requires **the site process, insurance rates and the inspection regime to change together** — Gate 4 multi-party coordination, not equipment performance; domestic work is the same, since between a machine folding laundry in a demo video and a hundred million households letting it into the bedroom daily sit ownership, trust and the cost paid on every use → **Hard constraints**: construction — **law / permitting** (building permits, inspection and injury liability must land on a party that can be sued) compounded by **physical**; domestic — **ownership / privacy** (someone's home is private space and entry requires authorization) compounded by **trust / relationship** (who gets a key is the product of repeated interaction over time and cannot be generated in one pass).
- **Original time window**: 2026–2040.
- **Original falsifier**: Before 2040, on-site construction robots substitute not for single operations but for the site process as a whole (verifiable through the number of trades and the share of schedule carried by robots in general contracts) — that falsifies this card's construction judgment; or a general-purpose home robot reaches daily performance of **open-ended household tasks** (not single-task slices such as vacuuming, dishwashing or mowing) in a majority of households in any country — that falsifies its domestic-work judgment.
- **Original leading indicator**: construction — (1) whether general contractors' insurance quotes a separate rate for robotic work; (2) whether schedule contracts start carrying default and stoppage clauses for robotic equipment; (3) whether the prefabrication share of work keeps rising. Domestic — (4) whether a general-purpose home robot falls into the durable-goods price band **and** carries a low enough recurring cost per task (no tidying beforehand, no supervision throughout); (5) whether domestic-worker headcount and wages diverge in high-adoption countries; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: FBR's Hadrian, pushed for something on the order of a decade, is still at single-operation and demonstration scale (EXT-47), supporting "what blocks on-site construction is not laying speed"; ILO counts domestic workers as a separate group in the tens of millions with a large informal share (EXT-42), supporting that the demand is real and already paid for. **Divergence and evidence boundary**: both are **a single case or a single group definition** and cover no arrival order; ILO's statistical boundaries and years are as given in the source and this card takes orders of magnitude only; this round obtained no checkable series for prefabrication share, insurance rates for robotic work, or the recurring per-task cost of home robots. **Why the judgment is retained**: the card depends on two constraints that do not open as model capability improves — permitting and liability must land on a party that can be sued, and entering private space requires authorization and long-run trust. But as a negative judgment running to 2040 it is less checkable than this chain's mid-segment judgments, so confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-42, EXT-47 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-078` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-079

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L171–L191`；`docs/en/ledger/71-80.md:L171–L191`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2091–L2110`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L171–L191`
- **原始标题**：生物医学候选生成与临床级因果证明会分叉
- **原始一句话命题**：2026–2034 年，生物医学候选生成与排序成本显著下降，但临床级因果证明不会按同一比例提速。
- **原始推理链**：候选可复制、搜索与排序成本下降 → 可信因果仍需真实样本、时间与受试者保护 → 瓶颈移到前瞻验证。
- **原始时间窗**：2026–2034。
- **原始证伪条件**：2030 年前，至少三个高责任医疗类别在不增加真实样本和随访强度时，把候选到获批有效干预的中位周期压缩一半以上且安全性撤回率不升。
- **原始领先指标**：每个获批干预对应的候选数、进入人体试验比例、各期历时、上市后安全性补充与撤回率；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-005, J-034, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C5：生物与医疗`。
- **原始外部对照判断**：**一致**：FDA 按 Context of Use 与风险评估 AI 可信度，支持“生成不等于证明”。**边界**：不证明时间窗或提速上限。**我为何仍坚持**：真实结局与受试者保护不随候选复制而复制。
- **原始外部对照来源**：EXT-49, EXT-50。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2141–L2160`
- **Current card anchor**: `docs/en/ledger/71-80.md:L171–L191`
- **Original title**: Biomedical candidate generation and clinical-grade causal proof diverge
- **Original one-sentence judgment**: From 2026 to 2034, biomedical candidate generation and ranking get much cheaper, while clinical-grade causal proof does not accelerate proportionally.
- **Original reasoning chain**: Candidates are copyable and ranking costs fall → trustworthy causality still needs real samples, time, and subject protection → the bottleneck moves to prospective validation.
- **Original time window**: 2026–2034.
- **Original falsifier**: Before 2030, at least three high-liability categories halve median candidate-to-approved-intervention time without increasing real samples or follow-up intensity, while safety withdrawals do not rise.
- **Original leading indicator**: candidates per approval, share entering human trials, phase duration, post-market safety supplements, and withdrawals; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-034, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA evaluates AI credibility by Context of Use and risk, supporting “generation is not proof.” **Boundary**: it does not establish the window or acceleration ceiling. **Why retained**: real outcomes and subject protection do not copy with candidates.
- **Original external comparison source**: EXT-49, EXT-50.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-079` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-080

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L192–L211`；`docs/en/ledger/71-80.md:L192–L211`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2111–L2130`
- **当前卡锚点**：`docs/zh/ledger/71-80.md:L192–L211`
- **原始标题**：低责任医疗工作流先于无专业复核的自主诊疗扩散
- **原始一句话命题**：2026–2031 年，摘要、编码、排程和复核型决策支持先于无专业复核的自主诊疗成为常规配置。
- **原始推理链**：低责任工具替换已有动作、嵌入现有载体且可复核 → 自主诊疗跨越执业权、责任和不可逆处置 → 前者先扩散。
- **原始时间窗**：2026–2031。
- **原始证伪条件**：到 2031 年，至少两个大型司法辖区中无人工复核的自主诊疗患者人次持续高于 AI 辅助文书与复核型支持，且不依赖一次性强制采购。
- **原始领先指标**：FDA 授权用途分布、医院“建议—复核”与“自主执行”比例、保险责任条款、临床留存率；每半年。
- **原始置信度**：中。
- **原始 depends-on**：J-079, J-066, J-068, J-069。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C5：生物与医疗`。
- **原始外部对照判断**：**一致**：FDA 清单证明受监管产品已获授权。**边界**：清单不穷尽全部设备，也不证明部署规模或自主程度。**我为何仍坚持**：复核型工具可利用机构闭环，自主诊疗必须额外获得行动权。
- **原始外部对照来源**：EXT-48, EXT-50。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2161–L2180`
- **Current card anchor**: `docs/en/ledger/71-80.md:L192–L211`
- **Original title**: Low-liability medical workflows diffuse before autonomous care without professional review
- **Original one-sentence judgment**: From 2026 to 2031, summarization, coding, scheduling, and review-based decision support become routine before autonomous diagnosis and treatment without professional review.
- **Original reasoning chain**: Low-liability tools replace existing work, fit current carriers, and remain reviewable → autonomous care crosses licensing, liability, and irreversible treatment → the former diffuses first.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, in at least two large jurisdictions, encounters covered by care without human review persistently exceed AI-assisted documentation and review-based support without one-off mandated procurement.
- **Original leading indicator**: FDA intended-use distribution, hospital recommend-review versus autonomous-action shares, insurance/liability terms, and clinical retention; twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-079, J-066, J-068, J-069.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA's list proves authorized regulated products exist. **Boundary**: it is not exhaustive and proves neither deployment scale nor autonomy. **Why retained**: review-based tools use an institutional loop; autonomous care needs additional action rights.
- **Original external comparison source**: EXT-48, EXT-50.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-080` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-081

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L5–L25`；`docs/en/ledger/81-90.md:L5–L25`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2131–L2150`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L5–L25`
- **原始标题**：药物候选更丰富，不等于人体试验时间同步缩短
- **原始一句话命题**：到 2034 年，AI 增加进入实验室的药物候选，但候选增长不会等比例转化为获批药物。
- **原始推理链**：搜索空间扩大 → 更多候选争夺没有同比扩张的湿实验、受试者、站点与监管容量 → 淘汰率或排队上升。
- **原始时间窗**：2026–2034。
- **原始证伪条件**：2028–2034 年，AI 起源候选从首次人体试验到获批的中位历时与失败率同时下降 50% 以上，并在至少三个治疗领域复现。
- **原始领先指标**：AI 起源候选的 Phase I 数量、各期转化率、站点启动与招募完成时间、每个获批药对应的临床候选数；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-079, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C5：生物与医疗`。
- **原始外部对照判断**：**一致**：FDA 要求按风险建立 AI 可信度。**边界**：不支持周期或成功率预测。**我为何仍坚持**：候选计算与人体时间属于不同生产函数。
- **原始外部对照来源**：EXT-49。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2181–L2200`
- **Current card anchor**: `docs/en/ledger/81-90.md:L5–L25`
- **Original title**: More drug candidates do not proportionally shorten human trial time
- **Original one-sentence judgment**: By 2034, AI increases drug candidates reaching laboratories, but candidate growth does not translate proportionally into approvals.
- **Original reasoning chain**: Search expands → more candidates compete for wet-lab, participant, site, and regulatory capacity that has not expanded proportionally → attrition or queues rise.
- **Original time window**: 2026–2034.
- **Original falsifier**: Between 2028 and 2034, AI-origin candidates cut both median first-in-human-to-approval time and failure rates by more than 50%, replicated in at least three therapeutic areas.
- **Original leading indicator**: Phase I AI-origin candidates, phase conversion, site start and recruitment completion time, and clinical candidates per approval; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-079, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA requires risk-linked AI credibility. **Boundary**: it supports no timeline or success-rate forecast. **Why retained**: candidate computation and human time follow different production functions.
- **Original external comparison source**: EXT-49.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-081` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-082

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L26–L46`；`docs/en/ledger/81-90.md:L26–L46`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2151–L2174`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L26–L46`
- **原始标题**：解释变多后，医疗稀缺移向获授权的干预与连续照护（仅图景）
- **原始一句话命题**：2027–2034 年，慢病、老龄和基层医疗的瓶颈从标准解释移向获授权干预、连续观察和异常升级。
- **原始推理链**：问答可复制 → 解释与提醒边际成本下降 → 采样、给药、转移、复诊与异常判断仍需本地资源和责任链 → 无载体时建议变成未兑现需求。
- **原始时间窗**：2027–2034。
- **原始证伪条件**：多个国家在 AI 问答广泛使用五年内，可干预工时、随访完成率和异常响应速度同步增长，且人力与机构容量不再是主要排队原因。
- **原始领先指标**：建议后复诊完成率、异常升级时延、每位照护者负担、基层空缺岗位、远程项目十二个月留存；每年。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-079, J-080, J-032, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C5：生物与医疗`。
- **原始外部对照判断**：**一致**：WHO 支持卫生人力、问责和安全是现实约束。**边界**：不证明 AI 会加剧照护排队。**我为何仍坚持**：本地干预与责任链不会由更多解释自动生成。
- **原始外部对照来源**：EXT-50, EXT-51。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2201–L2224`
- **Current card anchor**: `docs/en/ledger/81-90.md:L26–L46`
- **Original title**: Once explanation is abundant, medical scarcity moves to authorized intervention and continuity of care (landscape only)
- **Original one-sentence judgment**: From 2027 to 2034, the bottleneck in chronic disease, ageing, and primary care moves from standard explanation to authorized intervention, continuous observation, and exception escalation.
- **Original reasoning chain**: Q&A is copyable → explanation and reminder costs fall → sampling, medication, transfer, follow-up, and exception judgment still need local resources and liability chains → advice becomes unmet demand without a carrier.
- **Original time window**: 2027–2034.
- **Original falsifier**: Across several countries, within five years of widespread AI Q&A, intervention hours, follow-up completion, and exception response speed rise together while staff and institutional capacity cease to be principal queue causes.
- **Original leading indicator**: post-advice follow-up, escalation latency, load per caregiver, primary-care vacancies, and twelve-month remote-program retention; annually.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-079, J-080, J-032, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: WHO supports workforce, accountability, and safety as real constraints. **Boundary**: it does not prove AI worsens care queues. **Why retained**: local intervention and liability chains do not emerge automatically from more explanation.
- **Original external comparison source**: EXT-50, EXT-51.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-082` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-083

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L47–L67`；`docs/en/ledger/81-90.md:L47–L67`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2175–L2194`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L47–L67`
- **原始标题**：个性化讲解先于可验证掌握变丰富
- **原始一句话命题**：2026–2030 年，个性化解释、例题和即时反馈成为常规能力，但可验证掌握不同比增长。
- **原始推理链**：讲解可复制 → 生成与翻译成本下降 → 练习仍要求注意、时间与行为改变 → “看懂”与“独立完成”分叉。
- **原始时间窗**：2026–2030。
- **原始证伪条件**：多国、多年龄、多学科中，广泛使用生成式辅导两年后，受控迁移测试与长期保持率按使用强度同比提高且无需课程重设。
- **原始领先指标**：AI 辅导周活、独立迁移成绩、三至六个月保持率、完成率与帮助依赖度；每学期。
- **原始置信度**：中。
- **原始 depends-on**：J-001, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C6：教育与技能形成`。
- **原始外部对照判断**：**一致**：UNESCO 要求人本、年龄适配、隐私和教学设计。**边界**：不证明学习成果不会同比提高。**我为何仍坚持**：练习时间不可由解释替学员承担。
- **原始外部对照来源**：EXT-52。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2225–L2244`
- **Current card anchor**: `docs/en/ledger/81-90.md:L47–L67`
- **Original title**: Personalized explanation becomes abundant before verifiable mastery
- **Original one-sentence judgment**: From 2026 to 2030, personalized explanations, examples, and immediate feedback become routine, but verifiable mastery does not grow proportionally.
- **Original reasoning chain**: Explanations are copyable → generation and translation costs fall → practice still requires attention, time, and behavioural change → understanding and independent performance diverge.
- **Original time window**: 2026–2030.
- **Original falsifier**: Across countries, ages, and subjects, after two years of widespread generative tutoring, controlled transfer and long-term retention rise proportionally with use without curriculum redesign.
- **Original leading indicator**: weekly AI-tutoring use, independent transfer scores, three- to six-month retention, completion, and dependence on assistance; each term.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: UNESCO requires human-centred, age-appropriate, private, pedagogically designed use. **Boundary**: it does not prove outcomes fail to rise proportionally. **Why retained**: explanation cannot bear practice time for the learner.
- **Original external comparison source**: EXT-52.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-083` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-084

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L68–L88`；`docs/en/ledger/81-90.md:L68–L88`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2195–L2214`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L68–L88`
- **原始标题**：AI 辅导先嵌入教师与机构，而不是替代学校
- **原始一句话命题**：2026–2031 年，AI 辅导先在教师布置、课程对齐和机构监督中稳定扩散，而非大规模替代学校。
- **原始推理链**：独立聊天增加新动作 → 机构内辅导替换答疑、练习与反馈 → 学校提供身份、课程、同伴、评价和资格载体 → 局部闭环先扩散。
- **原始时间窗**：2026–2031。
- **原始证伪条件**：到 2031 年，至少三个大型教育系统中，脱离学校／雇主的 AI 路径获得的普遍认可资格持续多于机构内路径。
- **原始领先指标**：教师布置型与个人直购型使用占比、课程系统集成、十二个月留存、教师工作量、独立 AI 资格认可范围；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-083, J-066, J-068, J-069, J-070, J-071。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C6：教育与技能形成`。
- **原始外部对照判断**：**一致**：OECD 强调治理、生态和教师能力。**边界**：不证明学校保持当前边界。**我为何仍坚持**：学校绑定了学习之外的身份、评价与资格出口。
- **原始外部对照来源**：EXT-53。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2245–L2264`
- **Current card anchor**: `docs/en/ledger/81-90.md:L68–L88`
- **Original title**: AI tutoring enters teacher and institutional workflows before replacing schools
- **Original one-sentence judgment**: From 2026 to 2031, AI tutoring diffuses first through teacher assignment, curriculum alignment, and institutional supervision rather than large-scale school replacement.
- **Original reasoning chain**: Stand-alone chat adds a new action → embedded tutoring replaces Q&A, practice, and feedback → schools carry identity, curriculum, peers, assessment, and credentials → local loops diffuse first.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, in at least three large education systems, broadly recognized qualifications from AI pathways outside schools/employers persistently outnumber those from institution-embedded pathways.
- **Original leading indicator**: teacher-assigned versus direct purchase use, learning-system integration, twelve-month retention, teacher workload, and recognition breadth of independent AI credentials; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-083, J-066, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: OECD emphasizes governance, ecosystems, and teacher capacity. **Boundary**: it does not prove schools retain current boundaries. **Why retained**: schools bind learning to identity, assessment, and credential exits.
- **Original external comparison source**: EXT-53.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-084` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-085

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L89–L109`；`docs/en/ledger/81-90.md:L89–L109`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2215–L2234`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L89–L109`
- **原始标题**：居家成品信号变弱，受控表现与过程证据增值
- **原始一句话命题**：2027–2034 年，高风险升学和招聘降低无过程验证居家成品的权重，增加受控表现与过程证据。
- **原始推理链**：成品生成成本下降 → 成品与本人能力相关性变弱 → 选择者转向更贵但更难转包的身份、现场和长期记录。
- **原始时间窗**：2027–2034。
- **原始证伪条件**：到 2032 年，主要大学与大型雇主仍扩大无过程验证居家成品的独立权重，且其对后续表现的预测效度不降。
- **原始领先指标**：口试和现场任务占比、身份验证支出、作品集版本史要求、实习／学徒记录权重；每年。
- **原始置信度**：中。
- **原始 depends-on**：J-022, J-083, J-084, J-066。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C6：教育与技能形成`。
- **原始外部对照判断**：**一致**：UNESCO 支持重设评价。**边界**：不证明何种评价增值。**我为何仍坚持**：选择制度不能长期依赖与能力失去相关性的代理量。
- **原始外部对照来源**：EXT-52。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2265–L2284`
- **Current card anchor**: `docs/en/ledger/81-90.md:L89–L109`
- **Original title**: Take-home artifact signals weaken while controlled performance and process evidence gain weight
- **Original one-sentence judgment**: From 2027 to 2034, high-stakes admissions and hiring reduce the weight of take-home artifacts without process verification and increase controlled performance and process evidence.
- **Original reasoning chain**: Artifact-generation costs fall → artifacts correlate less with personal capability → selectors move toward costlier but harder-to-outsource identity, live performance, and longitudinal records.
- **Original time window**: 2027–2034.
- **Original falsifier**: By 2032, leading universities and large employers keep increasing the independent weight of take-home artifacts without process verification while their predictive validity does not decline.
- **Original leading indicator**: oral and live-task share, identity-verification spending, portfolio version-history requirements, and internship/apprenticeship weight; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-022, J-083, J-084, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: UNESCO supports assessment redesign. **Boundary**: it does not establish which assessment gains weight. **Why retained**: selection systems cannot indefinitely rely on a proxy that has lost correlation with capability.
- **Original external comparison source**: EXT-52.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-085` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-086

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L115–L135`；`docs/en/ledger/81-90.md:L115–L135`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2235–L2258`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L115–L135`
- **原始标题**：解释鸿沟缩小，但练习与验证鸿沟可能扩大（仅图景）
- **原始一句话命题**：2027–2034 年，AI 缩小优质解释获取差距，但无承载机构时技能与机会差距可能不降反升。
- **原始推理链**：边际解释变便宜 → 有设备与自律者先获益 → 掌握仍依赖时间、反馈与实践环境 → 资格依赖机构承认 → 新供给按既有资源差异被吸收。
- **原始时间窗**：2027–2034。
- **原始证伪条件**：在无新增教师、设备、评价或社会支持投入而广泛提供低成本 AI 辅导的地区，低收入与高收入学习者的独立掌握和资格差距连续五年显著缩小。
- **原始领先指标**：设备与连接、按收入分组的使用强度、独立测评差距、教师接触时间、完成率、资格与就业转化；每年。
- **原始置信度**：低（仅图景）。
- **原始 depends-on**：J-083, J-084, J-066, J-069, J-070。
- **原始状态与谱系**：ACTIVE
- **原始出处**：`C6：教育与技能形成`。
- **原始外部对照判断**：**一致**：世界银行证明基础学习缺口规模巨大。**边界**：不支持 AI 对不平等的方向。**我为何仍坚持**：解释只是学习生产函数的一项投入，且不是资格授予者。
- **原始外部对照来源**：EXT-54。
- **原始独立受众规模**：未知/未验证：历史卡没有独立「受众规模」字段；规模信息只在「普及闸复核」中，未把后来字段倒填。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2285–L2308`
- **Current card anchor**: `docs/en/ledger/81-90.md:L115–L135`
- **Original title**: The explanation gap narrows while practice and verification gaps may widen (landscape only)
- **Original one-sentence judgment**: From 2027 to 2034, AI narrows access gaps in explanation, but without carrier institutions skill and opportunity gaps may fail to fall or may widen.
- **Original reasoning chain**: Marginal explanation becomes cheap → people with devices and self-direction benefit first → mastery still needs time, feedback, and practice environments → credentials need institutional recognition → new supply is absorbed through existing resource differences.
- **Original time window**: 2027–2034.
- **Original falsifier**: Where low-cost AI tutoring is widespread without added teachers, devices, assessment, or social support, low- versus high-income gaps in independent mastery and qualifications shrink significantly for five consecutive years.
- **Original leading indicator**: device/connectivity access, use by income, independent assessment gaps, teacher contact, completion, qualifications, and employment conversion; annually.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-083, J-084, J-066, J-069, J-070.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: the World Bank establishes the enormous scale of foundational learning deficits. **Boundary**: it does not support AI's direction of effect on inequality. **Why retained**: explanation is only one input to learning and is not the authority granting qualifications.
- **Original external comparison source**: EXT-54.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-086` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.



## J-087

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L137–L158`；`docs/en/ledger/81-90.md:L137–L158`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2259–L2278`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L137–L158`
- **提出日期**：2026-09-21
- **一句话判断**：2026–2031 年，采用生成与工具调用的组织先把工作拆成机器默认执行、人类处理例外、责任人设定边界，而不是普遍形成无人组织。
- **受众规模**：知识工作者、运营人员与管理者为构造式亿量级影响面；主要**提高既有专业者上限**，工作单元改造的主体是组织。
- **普及闸复核**：影响面不是同一动作的可引用行为统计，且组织必须完成工作流替换与局部闭环；闸一不过，按组织性判断书写。
- **透镜**：技术次序 + 组织载体 + 普及闸二至闸四。
- **推理链**：生成和工具调用先成熟 → 边界清楚、可复核任务先被嵌入 → 例外与责任仍需主体 → 最小生产单元先变成人类责任人监督多次机器执行。
- **时间窗**：2026–2031。
- **证伪条件**：到 2031 年，在至少三个大型知识工作行业，持续十二个月的生产级 AI 部署中，采用“机器默认执行／人类处理例外／责任人设定边界”工作单元的比例仍不足一半；无论另一半由端到端无人执行占据，还是部署普遍停在演示与失败阶段，均触发本卡证伪。
- **领先指标**：默认执行占比、人工接管率、每名责任人监督的执行数、部署前流程重构时数、十二个月留存；每半年。
- **置信度**：中。
- **depends-on**：J-006, J-007, J-009, J-066, J-068。
- **最强反方**：端到端可靠性可能跃升，使组织跳过监督单元而直接委托完整结果。
- **与共识**：**一致**：NIST 要求治理、测量、监测与人类监督。**边界**：不证明监督单元是主流组织形态或本卡时间窗。**我为何仍坚持**：既有责任主体和工作流是已存在的载体，逐任务替换比一次性重建企业边界更容易过普及闸。
- **外部对照来源**：EXT-4。
- **出处**：[C7：技术先到，权力后到](../zh/chains/70-capability-to-social-consequences.md)。
- **下次检查日**：2027-06-30。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2309–L2328`
- **Current card anchor**: `docs/en/ledger/81-90.md:L137–L158`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2031, organizations adopting generation and tool use first split work into machine-default execution, human exception handling, and accountable boundary setting rather than broadly becoming staffless.
- **Audience scale**: constructed hundred-millions-scale reach across knowledge workers, operations staff, and managers; mainly **raises existing professionals' ceiling**, while organizations perform the work-unit redesign.
- **Diffusion-gate review**: The reach is not a citable same-action behaviour statistic, and organizations must complete workflow substitution and a local closed loop; Gate 1 **FAIL**, an organizational judgment.
- **Lens**: technology sequence + organizational carrier + diffusion Gates 2–4.
- **Reasoning chain**: Generation and tool use mature first → bounded reviewable tasks enter workflows first → exceptions and liability still need a principal → the minimum production unit becomes one accountable person supervising multiple machine executions.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, across at least three large knowledge-work industries, fewer than half of production AI deployments that persist for twelve months use a work unit combining machine-default execution, human exception handling, and accountable boundary setting. The card fails whether the remainder is end-to-end staffless execution or deployment broadly stalls in demonstrations and failures.
- **Leading indicator**: machine-default share, human takeover rate, executions per accountable owner, pre-deployment workflow-redesign hours, and twelve-month retention; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007, J-009, J-066, J-068.
- **Strongest opposing mechanism**: End-to-end reliability may jump enough for organizations to delegate complete outcomes without passing through supervisory units.
- **Against consensus**: **Agreement**: NIST calls for governance, measurement, monitoring, and human oversight. **Boundary**: it does not establish this organizational form or time window. **Why retained**: existing accountable principals and workflows are already-built carriers, so task-by-task substitution clears the diffusion gates more easily than rebuilding firm boundaries at once.
- **External comparison source**: EXT-4.
- **Source**: [C7：技术先到，权力后到：能力出现次序如何穿过组织，才变成社会后果](../zh/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-087` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.
- **J-086/J-087 boundary attack**：J-086 remains a separate historical card and J-087 begins the next source section; replacing either historical proposition with the other’s current wording would fail this migration boundary.

## J-088

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L159–L180`；`docs/en/ledger/81-90.md:L159–L180`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2279–L2298`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L159–L180`
- **提出日期**：2026-09-21
- **一句话判断**：2027–2034 年，在生成密集职业中，初级产出席位和例行工时的相对收缩先于职业总人数下降，受监督实战成为技能形成瓶颈。
- **受众规模**：初级知识工作者、求职者与专业训练者为构造式千万量级；主要**提高既有专业者上限**，但收窄新人的职业入口。
- **普及闸复核**：职业入口是低频制度安排，不是社会成员反复执行的同一动作；闸一不过，按劳动市场与技能形成判断书写。
- **透镜**：任务束 + 技能形成 + 信号博弈。
- **推理链**：初级产出最易验证并自动化 → 资深者用更少初级工时维持产量 → 新人失去以真实任务练习的载体 → 学徒、模拟与受监督实战的稀缺上升。
- **时间窗**：2027–2034。
- **证伪条件**：到 2032 年，在至少五个生成密集职业中，初级席位占比没有先于职业总人数下降；或虽先下降，但可验证的学徒、模拟、轮岗或受监督实战容量同步扩张到足以维持采用前的专业者补充率。初级席位与职业总人数同步下降或晚于整体收缩，也触发本卡证伪。
- **领先指标**：初级／资深招聘比、入职任务结构、学徒席位、监督时数、晋升周期、外部候选人的受控表现；每年。
- **置信度**：中。
- **depends-on**：J-087, J-083, J-066。
- **最强反方**：AI 辅导与高保真模拟可能同时降低训练成本，使更多新人获得比旧工作更密集的反馈。
- **与共识**：**部分一致**：ILO 2025 的全球职业暴露指数发现全球约四分之一劳动者处于某种 GenAI 暴露中，并判断多数职业更可能被转化而非整岗替代。**边界**：该指数不提供初级招聘、学徒载体、净就业或本卡时间窗。**我为何仍坚持**：被替掉的例行产出同时是旧职业的练习载体，而新载体不会由生成能力自动建立。
- **外部对照来源**：EXT-60。
- **出处**：[C7：技术先到，权力后到](../zh/chains/70-capability-to-social-consequences.md)。
- **下次检查日**：2027-06-30。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2329–L2348`
- **Current card anchor**: `docs/en/ledger/81-90.md:L159–L180`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, in generation-intensive occupations junior production seats and routine hours shrink relatively before total occupational headcount, making supervised practice a skill-formation bottleneck.
- **Audience scale**: constructed tens-of-millions-scale reach across junior knowledge workers, applicants, and professional trainees; mainly **raises existing professionals' ceiling** while narrowing entry routes.
- **Diffusion-gate review**: Occupational entry is a low-frequency institutional arrangement, not one repeated action performed across society; Gate 1 **FAIL**, a labour-market and skill-formation judgment.
- **Lens**: task bundles + skill formation + signalling game.
- **Reasoning chain**: Junior production is easiest to verify and automate → seniors sustain output with fewer junior hours → entrants lose the carrier for real-task practice → apprenticeship, simulation, and supervised fieldwork become scarcer.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, across at least five generation-intensive occupations, junior-seat share does not decline before total occupational headcount; or it declines first but verifiable apprenticeship, simulation, rotation, or supervised-fieldwork capacity expands enough to preserve the pre-adoption replenishment rate of professionals. Junior seats falling at the same time as or after total occupational contraction also falsifies the card.
- **Leading indicator**: junior-to-senior hiring ratio, entry-task mix, apprenticeship places, supervised hours, time to promotion, and controlled performance of external candidates; annually.
- **Confidence**: Medium.
- **depends-on**: J-087, J-083, J-066.
- **Strongest opposing mechanism**: AI tutoring and high-fidelity simulation may lower training cost simultaneously, giving more entrants denser feedback than old jobs did.
- **Against consensus**: **Partial agreement**: the ILO's 2025 global occupational-exposure index finds about one in four workers in occupations with some GenAI exposure and judges transformation more likely than whole-job replacement for most occupations. **Boundary**: the index provides no evidence about junior hiring, apprenticeship carriers, net employment, or this card's time window. **Why retained**: the routine production being removed was also the old occupation's practice carrier, and generation does not automatically build a replacement carrier.
- **External comparison source**: EXT-60.
- **Source**: [C7：技术先到，权力后到：能力出现次序如何穿过组织，才变成社会后果](../zh/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-088` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-089

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L181–L202`；`docs/en/ledger/81-90.md:L181–L202`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2299–L2318`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L181–L202`
- **提出日期**：2026-09-21
- **一句话判断**：2026–2032 年，能持续调用工具的 AI 广泛获得高责任自主权之前，身份、权限、日志、暂停、审计与申诉进入核心生产系统。
- **受众规模**：受高责任自动化影响的员工、客户与公民为构造式亿量级；主要**提高既有专业者上限**，控制动作由组织与公共机构执行。
- **普及闸复核**：影响面不是控制动作的执行人数，且多方授权依赖可强制、可观测的制度协调；闸一不过，按制度性判断书写。
- **透镜**：行动权 + 法律责任 + 普及闸四。
- **推理链**：工具调用扩大可造成的后果 → 资产所有者要求最小权限与可暂停性 → 争议要求日志、责任签名与申诉 → 控制面从合规附件变成生产依赖。
- **时间窗**：2026–2032。
- **证伪条件**：到 2030 年，在至少三个高责任行业，大多数生产级自主系统在取得广泛高责任权限时仍未把主体级授权、不可篡改操作记录、人工暂停和争议申诉入口作为前置生产依赖。若系统先广泛取得权限、事故后才被监管或买方收紧，仍因次序相反触发本卡证伪。
- **领先指标**：细粒度权限覆盖率、日志留存、人工暂停率、外部审计条款、申诉时延、因缺控制面被拒的采购；每半年。
- **置信度**：中。
- **depends-on**：J-007, J-009, J-031, J-055, J-070。
- **最强反方**：低事故率和平台级保险可能让组织接受黑箱自治，以事后赔偿替代逐项控制。
- **与共识**：**一致**：NIST 与 EU AI Act 支持治理、日志、人类监督和风险管理。**边界**：不证明申诉控制面的普及次序或跨行业一致性。**我为何仍坚持**：可执行系统会触碰他人资产与权利，现有责任主体需要可观测的授权与中止路径才能委托。
- **外部对照来源**：EXT-4, EXT-10。
- **出处**：[C7：技术先到，权力后到](../zh/chains/70-capability-to-social-consequences.md)。
- **下次检查日**：2027-06-30。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2349–L2368`
- **Current card anchor**: `docs/en/ledger/81-90.md:L181–L202`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2032, identity, permission, logging, pause, audit, and appeal enter core production systems before tool-using AI broadly receives high-liability autonomous authority.
- **Audience scale**: constructed hundred-millions-scale reach across employees, customers, and citizens affected by high-liability automation; mainly **raises existing professionals' ceiling**, while organizations and public institutions operate the controls.
- **Diffusion-gate review**: Affected reach is not the headcount executing the control action, and multi-party authorization depends on enforceable and observable coordination; Gate 1 **FAIL**, an institutional judgment.
- **Lens**: action rights + legal liability + diffusion Gate 4.
- **Reasoning chain**: Tool use enlarges possible consequences → asset owners require least privilege and interruptibility → disputes require logs, accountable signatures, and appeal → the control plane moves from compliance attachment to production dependency.
- **Time window**: 2026–2032.
- **Falsifier**: By 2030, across at least three high-liability industries, most production autonomous systems receive broad high-liability authority without principal-level authorization, tamper-evident action records, human pause, and dispute appeal as prior production dependencies. If systems receive broad authority first and regulators or buyers tighten only after accidents, the reversed order still falsifies the card.
- **Leading indicator**: fine-grained permission coverage, log retention, human pause rate, external-audit clauses, appeal latency, and procurements rejected for missing controls; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-007, J-009, J-031, J-055, J-070.
- **Strongest opposing mechanism**: Low accident rates and platform-level insurance may make black-box autonomy acceptable, replacing per-action control with ex-post compensation.
- **Against consensus**: **Agreement**: NIST and the EU AI Act support governance, logging, human oversight, and risk management. **Boundary**: they do not establish the diffusion order of appeal controls or consistency across industries. **Why retained**: execution touches other parties' assets and rights, so existing accountable principals need observable authorization and interruption paths before delegating.
- **External comparison source**: EXT-4, EXT-10.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-089` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-090

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L203–L223`；`docs/en/ledger/81-90.md:L203–L223`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2319–L2338`
- **当前卡锚点**：`docs/zh/ledger/81-90.md:L203–L223`
- **提出日期**：2026-09-21
- **一句话判断**：2027–2035 年，通用模型价格下降后的早期生产率收益优先流向拥有客户、专有工作流数据、牌照、渠道、责任资本、算力或电力的主体，而非按技术可得性自动均分。
- **受众规模**：企业、劳动者与消费者为构造式十亿量级影响面；主要**提高既有专业者上限**，收益分配由资产所有者与制度决定。
- **普及闸复核**：十亿量级是分配影响面而非同一动作行为统计，判断对象是资产与制度安排；闸一不过，按资本与权力判断书写。
- **透镜**：互补资产 + 资本收益 + 竞争制度。
- **推理链**：模型和调用价格下降 → 核心能力租金受压 → 商业化仍需稀缺互补资产与固定改造成本 → 既有资产拥有者先吸收收益 → 开放标准、竞争与再分配决定后续扩散。
- **时间窗**：2027–2035。
- **证伪条件**：到 2032 年，在至少五个高采用行业中，控制客户、专有数据、牌照、渠道或基础设施的既有企业并未获得相对利润率、市场份额或议价权改善；无论收益转向新进入者、模型供应商、劳动者还是消费者，均触发本卡证伪。
- **领先指标**：行业利润率、并购与集中度、AI 供应链各层收益、工资份额、价格下降、数据可携带性与渠道迁移率；每年。
- **置信度**：中。
- **depends-on**：J-001, J-039, J-056, J-087。
- **最强反方**：模型商品化、开放权重与低代码分发可能使互补资产快速可复制，小团队直接夺走既有渠道和利润。
- **与共识**：**一致于机制、未知于结果**：Teece 的互补资产理论支持创新收益取决于稀缺互补资产；Brynjolfsson、Rock 与 Syverson 的生产率 J 曲线支持通用技术需要业务流程、人力资本与组织共发明等互补无形投资。**边界**：两者都不支持 AI 收益分配、集中期长度或本卡具体时间窗。**我为何仍坚持**：模型可得不等于客户、牌照、电力、责任资本和工作流改造能力同时可得。
- **外部对照来源**：EXT-37, EXT-61。
- **出处**：[C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md)。
- **下次检查日**：2027-12-31。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2369–L2388`
- **Current card anchor**: `docs/en/ledger/81-90.md:L203–L223`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, early productivity gains after general-model prices fall flow first to parties owning customers, proprietary workflow data, licences, channels, liability-bearing capital, compute, or power rather than spreading automatically with technical access.
- **Audience scale**: constructed billion-scale reach across firms, workers, and consumers; mainly **raises existing professionals' ceiling**, while asset owners and institutions determine distribution.
- **Diffusion-gate review**: Billion-scale is distributional reach, not a same-action behaviour statistic, and the subject is an asset and institutional arrangement; Gate 1 **FAIL**, a capital-and-power judgment.
- **Lens**: complementary assets + capital returns + competition institutions.
- **Reasoning chain**: Model and call prices fall → scarcity rents on core capability compress → commercialization still needs scarce complementary assets and fixed redesign cost → incumbent asset owners absorb gains first → open standards, competition, and redistribution determine later spread.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five high-adoption industries, incumbent firms controlling customers, proprietary data, licences, channels, or infrastructure gain no relative margin, market share, or bargaining power. The card fails whether gains move to entrants, model suppliers, labour, or consumers.
- **Leading indicator**: industry margins, merger activity and concentration, returns by AI supply-chain layer, labour share, price decline, data portability, and channel switching; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-039, J-056, J-087.
- **Strongest opposing mechanism**: Model commoditization, open weights, and low-code distribution may make complementary assets rapidly replicable, letting small teams take incumbent channels and profits directly.
- **Against consensus**: **Agreement on mechanism, unknown on outcome**: Teece's complementary-assets theory supports value capture depending on scarce complements; Brynjolfsson, Rock, and Syverson's Productivity J-Curve supports general-purpose technologies requiring complementary intangible investment in business processes, human capital, and organizational co-invention. **Boundary**: neither establishes AI's distribution, the duration of concentration, or this card's time window. **Why retained**: model access does not simultaneously supply customers, licences, power, liability capital, and workflow-redesign capacity.
- **External comparison source**: EXT-37, EXT-61.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-090` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-091

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L5–L26`；`docs/en/ledger/91-95.md:L5–L26`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2339–L2358`
- **当前卡锚点**：`docs/zh/ledger/91-95.md:L5–L26`
- **提出日期**：2026-09-21
- **一句话判断**：2027–2035 年，AI 密集行业同时出现单位产出工时下降与品类、频次或客群扩张；净就业方向由需求弹性和未自动化硬约束共同决定。
- **受众规模**：劳动者与消费者为构造式十亿量级影响面；能力既**提高既有专业者上限**，也可能在低价服务中让原本不会的人也能做部分消费或生产动作。
- **普及闸复核**：影响面不是单一重复动作，且就业是行业层净结果；闸一不过，按需求与劳动结构判断书写。
- **透镜**：供需弹性 + 任务束 + 物理／制度硬约束。
- **推理链**：单位任务工时下降 → 价格、等待或定制成本下降 → 原本不经济的需求进入市场 → 未自动化环节吸收部分新增量 → 需求扩张与任务节省的相对幅度决定净就业。
- **时间窗**：2027–2035。
- **证伪条件**：到 2032 年，在至少五个采用密集行业中，单位服务工时显著下降后三年内，品类、频次、客群和总产出均无扩张。就业是否还能被宏观周期、监管或其他因素解释，不影响“需求扩张与任务节省同时发生”这一主张被证伪。
- **领先指标**：单位产出工时、价格、等待时间、SKU／服务品类、每客频次、新客占比、总产出、未自动化环节岗位；每年。
- **置信度**：中。
- **depends-on**：J-001, J-037, J-073, J-087。
- **最强反方**：需求已饱和或收入约束不变时，成本下降可能只转化为利润和岗位减少，不产生足够新增量。
- **与共识**：**部分一致**：ILO 2025 认为多数职业更可能发生任务转化而非整岗替代，并明确暴露指数本身不能给出净就业结果。**边界**：不提供需求弹性、产量扩张或净就业方向。**我为何仍坚持**：供需关系决定成本下降后数量是否扩张，身体、牌照和场址决定新增量落在哪个环节，单凭能力曲线无法推出净值。
- **外部对照来源**：EXT-60。
- **出处**：[C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md)。
- **下次检查日**：2027-12-31。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2389–L2412`
- **Current card anchor**: `docs/en/ledger/91-95.md:L5–L26`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, AI-intensive industries see both lower labour hours per unit and expansion in variety, frequency, or customer segments; demand elasticity and non-automated hard constraints jointly determine net employment.
- **Audience scale**: constructed billion-scale reach across workers and consumers; the capability both **raises existing professionals' ceiling** and, in low-cost services, may let people who could not do it do it now for some consumption or production actions.
- **Diffusion-gate review**: The reach is not one repeated action and employment is an industry-level net result; Gate 1 **FAIL**, a demand-and-labour-structure judgment.
- **Lens**: supply-and-demand elasticity + task bundles + physical and institutional hard constraints.
- **Reasoning chain**: Labour hours per task fall → price, waiting, or customization costs fall → previously uneconomic demand enters → non-automated steps absorb part of the new volume → the relative size of expansion and savings determines net employment.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five adoption-intensive industries, significant labour-hour reductions per service are followed for three years by no expansion in variety, frequency, customer segments, or total output. Whether employment can also be explained by macroeconomic cycles, regulation, or other factors does not prevent falsification of the card's claim that demand expansion and task savings occur together.
- **Leading indicator**: labour hours per unit, price, wait time, SKU or service variety, frequency per customer, new-customer share, total output, and jobs in non-automated steps; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-037, J-073, J-087.
- **Strongest opposing mechanism**: Where demand is saturated or income constraints do not move, cost reduction may become profit and job reduction without enough new volume.
- **Against consensus**: **Partial agreement**: the ILO's 2025 index judges task transformation more likely than whole-job replacement for most occupations and makes clear that exposure alone does not yield a net-employment outcome. **Boundary**: it provides no demand elasticity, output expansion, or net employment direction. **Why retained**: supply and demand determine whether lower cost expands quantity, while bodies, licences, and sites determine where that quantity lands; capability curves alone cannot yield the net result.
- **External comparison source**: EXT-60.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

## 18. Judgment cards for the C8 upstream-materials and climate-coupling chain

> These four cards come from [C8：芯片之前的晶圆厂：为什么气候风险咬住的是「已验证瓶颈」](../zh/chains/80-fab-materials-and-climate.md). They separate mineral stock and nominal supplier count from a qualified conversion path that can actually switch, and judge climate coupling through event–exposure–transmission rather than a single incident.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-091` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-092

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L27–L48`；`docs/en/ledger/91-95.md:L27–L48`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2363–L2382`
- **当前卡锚点**：`docs/zh/ledger/91-95.md:L27–L48`
- **提出日期**：2026-09-22
- **一句话判断**：2026–2032 年，先进半导体的韧性投入从增加原料和成品库存，转向提前验证替代精炼、电子级转化、设备服务、配方与工艺转移路径。
- **受众规模**：实际执行者为构造式百万量级的半导体采购、工艺、设备、供应链、政策与基础设施专业者，主要**提高既有专业者上限**；消费者只间接受价格和供给影响。
- **普及闸复核**：这是低频产业配置而非同一动作在社会中扩散；闸一不过，按职业／组织性判断书写。
- **透镜**：供给弹性 + L2 约束迁移 + L4 扩散滞后 + 地理硬约束。
- **推理链**：算力扩张推动先进半导体产能与韧性需求 → 部分关键材料是其他矿业加工的副产品，增量供给不只响应本品价格 → 电子级纯度、配方、设备与客户批准把同名材料变成工艺专用品 → 库存只能缓冲中断，不能替代未验证转化节点 → 单一企业难为闲置备用链独自买单，需由大买方、公共支持或集群闭环协调 → 企业把边际韧性预算移向替代路径的提前验证与实际切换。
- **时间窗**：2026–2032。
- **证伪条件**：到 2030 年，在至少三个先进半导体制造集群或十家主要制造／材料／设备企业中，韧性投入仍主要增加原料或成品库存；替代来源的预验证、双重工艺资格、可转移配方、备件／服务冗余与跨场址切换时间均无可观察增长。只增加名义供应商数量而没有验证，不算命中。
- **领先指标**：双重验证材料占比、替代来源验证周期、可移植配方／掩模覆盖、设备备件与服务冗余、跨场址切换演练、库存预算与验证预算之比；每年。
- **置信度**：中。
- **depends-on**：J-056, J-069, J-070。
- **最强反方**：材料标准化、开放设备接口、可信仿真与更快客户批准可能把验证周期压到足以让库存和名义多来源重新成为主要工具。
- **与共识**：**一致于暴露，未知于响应**：OECD、USGS 与 DOE 支持关键投入的区域集中、副产品耦合和环节脆弱性。**边界**：这些来源不证明企业韧性预算的迁移方向或验证周期。**我为何仍坚持**：未通过验证的物料和场址无法在中断时承接同一规格产出，名义供给不等于可切换供给。
- **外部对照来源**：EXT-67, EXT-68, EXT-69, EXT-70, EXT-72, EXT-73。
- **出处**：[C8：芯片之前的晶圆厂](../zh/chains/80-fab-materials-and-climate.md)。
- **下次检查日**：2027-06-30。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2413–L2432`
- **Current card anchor**: `docs/en/ledger/91-95.md:L27–L48`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2026 to 2032, resilience investment for advanced semiconductors shifts from larger raw-material and finished-goods inventories toward pre-qualified alternate refining, electronic-grade conversion, tool service, recipes, and process-transfer paths.
- **Audience scale**: a constructed million-scale set of semiconductor procurement, process, equipment, supply-chain, policy, and infrastructure professionals performs the work; this mainly **raises existing professionals' ceiling**, while consumers encounter indirect price and availability effects.
- **Diffusion-gate review**: This is low-frequency industrial configuration, not one activity diffusing across society; Gate 1 **FAIL**, so it remains an occupational/organizational judgment.
- **Lens**: supply elasticity + L2 constraint migration + L4 diffusion lag + geographic hard constraints.
- **Reasoning chain**: compute expansion raises demand for advanced-semiconductor capacity and resilience → some critical materials are by-products of other ore-processing systems, so incremental supply does not respond only to their own price → electronic-grade purity, recipes, tools, and customer approval turn chemically identical material into a process-specific input → inventory buffers disruption but cannot replace an unqualified conversion node → one firm rarely funds idle backup paths alone, so large buyers, public support, or cluster-level closed loops must coordinate them → firms move marginal resilience spending toward advance qualification and exercised switching.
- **Time window**: 2026–2032.
- **Falsifier**: By 2030, across at least three advanced-semiconductor clusters or ten major manufacturing, materials, or equipment firms, resilience spending still mainly increases raw or finished inventory, while pre-qualification of alternatives, dual process qualification, portable recipes, parts/service redundancy, and cross-site transfer time show no observable growth. Merely increasing nominal supplier count without qualification does not count as a hit.
- **Leading indicator**: share of dual-qualified materials, alternate-source qualification duration, portable recipe/mask coverage, parts and service redundancy, cross-site failover exercises, and inventory-to-qualification budget ratio; annually.
- **Confidence**: Medium.
- **depends-on**: J-056, J-069, J-070.
- **Strongest opposing mechanism**: material standardization, open tool interfaces, trusted simulation, and faster customer approval may compress qualification enough that inventory and nominal multi-sourcing regain primacy.
- **Against consensus**: **Agreement on exposure, unknown on response**: OECD, USGS, and DOE support regional concentration, by-product coupling, and segment vulnerability. **Boundary**: they do not establish the direction of resilience budgets or qualification duration. **Why retained**: unqualified materials and sites cannot carry the same specified output during disruption, so nominal supply is not switchable supply.
- **External comparison source**: EXT-67, EXT-68, EXT-69, EXT-70, EXT-72, EXT-73.
- **Source**: [C8：芯片之前的晶圆厂：为什么气候风险咬住的是「已验证瓶颈」](../zh/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-092` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-093

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L49–L70`；`docs/en/ledger/91-95.md:L49–L70`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2383–L2402`
- **当前卡锚点**：`docs/zh/ledger/91-95.md:L49–L70`
- **提出日期**：2026-09-22
- **一句话判断**：2026–2033 年，先进晶圆厂选址与公共支持越来越按稳定电力、电能质量、进水水质、水回用、排放与气候适应的组合能力定价，而不是分别比较土地、税率和平均公用事业价格。
- **受众规模**：直接决策者为十万至百万量级的晶圆厂、材料、公用事业、政府与社区专业者；集群周边百万量级居民可能受资源分配影响，能力主要**提高既有专业者上限**。
- **普及闸复核**：受影响人口不是同一周频动作的执行者，选址是低频组织决策；闸一不过，按产业／制度判断书写。
- **透镜**：互补资产 + 场址不可移动性 + L7 制度滞后。
- **推理链**：先进工艺同时需要稳定电力、超纯水、气体化学品与排放能力 → 任一公用工程不合格都会把廉价土地变成不可用场址 → 气候风险提高公共系统供给方差 → 专用处理、回用、储备与电力质量进入选址总成本和补贴条件。
- **时间窗**：2026–2033。
- **证伪条件**：到 2031 年，在至少十个新建或大扩建先进晶圆厂项目中，选址、补贴和公用事业合同仍主要由土地、税率与平均电／水价格解释；电能质量、取排水权、回用率、干旱／洪水适应和专用设施既不改变排名，也不形成实质合同或资本开支。
- **领先指标**：项目水电专用设施资本开支、单位晶圆取水与回收率、电能质量条款、取排水许可周期、气候适应附带条件、场址因公用工程退出或延期次数；每半年。
- **置信度**：中。
- **depends-on**：J-061, J-069。
- **最强反方**：高回收率、闭式冷却、场内处理、自备电力与灵活工艺可能把晶圆厂从公共系统解耦，使组合约束退化为普通资本成本。
- **与共识**：**一致于运营约束，未知于定价权重**：IEA、LBNL、DOE 与 ERCOT 支持大型负荷的电力交付和接入约束，DOE 与 TSMC 支持水、能源和韧性是半导体运营问题。**边界**：它们不证明一束公用工程会超过税率与土地成为晶圆厂选址决定项。**我为何仍坚持**：这些投入互为补充品，缺一项就无法把其他低价投入转成已验证产出。
- **外部对照来源**：EXT-12, EXT-26, EXT-29, EXT-30, EXT-69, EXT-71。
- **出处**：[C8：芯片之前的晶圆厂](../zh/chains/80-fab-materials-and-climate.md)。
- **下次检查日**：2027-06-30。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2433–L2452`
- **Current card anchor**: `docs/en/ledger/91-95.md:L49–L70`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2026 to 2033, advanced-fab siting and public support increasingly price firm power, power quality, inlet-water quality, reuse, discharge, and climate adaptation as a bundle rather than comparing land, tax, and average utility prices separately.
- **Audience scale**: direct decision makers are a million-scale-or-smaller set of fab, materials, utility, government, and community professionals; millions around major clusters may be affected by allocation, while the capability mainly **raises existing professionals' ceiling**.
- **Diffusion-gate review**: affected residents are not performers of one weekly action, and siting is a low-frequency organizational choice; Gate 1 **FAIL**, an industrial/institutional judgment.
- **Lens**: complementary assets + site immobility + L7 institutional lag.
- **Reasoning chain**: advanced processes jointly require firm power, ultrapure water, gases and chemicals, and discharge capacity → failure of one utility makes cheap land unusable → climate risk increases variance in public systems → dedicated treatment, reuse, reserves, and power quality enter total siting cost and subsidy conditions.
- **Time window**: 2026–2033.
- **Falsifier**: By 2031, across at least ten new or substantially expanded advanced fabs, siting, subsidies, and utility contracts remain explained mainly by land, tax, and average water/power prices; power quality, withdrawal/discharge rights, reuse, drought/flood adaptation, and dedicated facilities neither change rankings nor create material contracts or capital spending.
- **Leading indicator**: project capital spending on dedicated water/power systems, withdrawal per wafer and recovery rate, power-quality clauses, withdrawal/discharge permitting time, climate-adaptation conditions, and projects exited or delayed for utility reasons; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-061, J-069.
- **Strongest opposing mechanism**: high recovery, closed-loop cooling, on-site treatment, dedicated generation, and flexible processes may decouple fabs from public systems and reduce the bundle to ordinary capital cost.
- **Against consensus**: **Agreement on operating constraints, unknown on pricing weight**: IEA, LBNL, DOE, and ERCOT support power-delivery and interconnection constraints for large loads, while DOE and TSMC support water, energy, and resilience as semiconductor operating issues. **Boundary**: they do not show a utility bundle outranking tax and land in fab siting. **Why retained**: these inputs are complements; a missing one prevents the others from becoming qualified output.
- **External comparison source**: EXT-12, EXT-26, EXT-29, EXT-30, EXT-69, EXT-71.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-093` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-094

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L71–L92`；`docs/en/ledger/91-95.md:L71–L92`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2403–L2422`
- **当前卡锚点**：`docs/zh/ledger/91-95.md:L71–L92`
- **提出日期**：2026-09-22
- **一句话判断**：2027–2034 年，半导体采购、保险、融资与选址会把气候风险系统性纳入定价，但可被检验的传导单位不是风险区厂房数量，而是至少一种无法由库存或已验证替代路径吸收的多场址已验证产出损失、替代路径验证周期延长或相关供应商中断；若窗口结束前没有这类传导却已仅按风险地图或披露监管定价，本判断证伪。
- **受众规模**：直接执行者为百万量级的制造、采购、保险、融资、设备与公共基础设施专业者，主要**提高既有专业者上限**；下游消费者为更大的间接受影响面。
- **普及闸复核**：这是机构定价与风险配置，不是亿级不同个人每周执行同一动作；闸一不过。
- **透镜**：事件—暴露—传导 + 保险定价 + 资格验证。
- **推理链**：气候事件不等于停产 → 暴露只有穿过水、电、物流、设备服务或供应商节点才损伤产出 → 库存与已验证替代路径可吸收部分冲击 → 只有重复且不可吸收的已验证传导才可能改变保费、合同、库存和选址；**当前没有来源证明这类传导会在窗口内出现，窗口尚未结束时不构成命中或证伪并保持 `ACTIVE`；到期复核时只有预登记量无法计算才记 `INDETERMINATE`；若损失触发器未出现却已有风险地图／披露监管先行定价，则按对称证伪条件判错**。
- **时间窗**：2027–2034。
- **证伪条件**：在 2032 年前，至少三个制造区域都出现了重复、气候相关、且无法由库存或已验证替代路径吸收的已验证产出损失；若在此前提下半导体保险条款、供应合同、资格验证、库存结构、融资成本和选址标准仍无系统变化，或变化只跟风险地图走、与实际产出损失和替代路径无关，则本卡证伪。**若到 2034 年窗口结束前，上述损失从未出现，却已有保险条款、融资成本或选址标准仅按风险地图或披露监管系统性变化，本卡同样证伪。**反复发生但被完全吸收的水、电、物流或场址中断，以及触发器从未出现且没有这类先行定价，均不触发证伪。
- **领先指标**：气候相关停机小时与损失晶圆、保险免赔额与除外条款、气候附加审计、替代来源验证周期、相关节点共同暴露、事件后选址或合同变化；每年。
- **置信度**：中。
- **depends-on**：J-092, J-093。
- **最强反方**：长期合同、库存、快速修复和需求替代可能持续吸收气候冲击，使暴露升高但产出与金融条款不变。
- **与共识**：**一致于暴露，分歧于证据单位**：UNU-EHS 支持台湾干旱与用水限制的暴露层，FERC/NERC 支持寒潮电力系统中断，NXP 只支持一家公司的一次停产传导。**边界**：这些材料不证明多场址重复减产或保险、融资如何响应。**我为何仍坚持**：只有事件穿过共同节点形成不可吸收损失，才会改变经济行为；这也使一次事故不足以支撑趋势。
- **外部对照来源**：EXT-69, EXT-71, EXT-74, EXT-75, EXT-76。
- **出处**：[C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md)。
- **下次检查日**：2027-12-31。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2453–L2472`
- **Current card anchor**: `docs/en/ledger/91-95.md:L71–L92`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2027 to 2034, semiconductor procurement, insurance, finance, and siting will systematically price climate risk, but the testable transmission unit is not the number of facilities in hazard zones: it is at least one multi-site qualified-output loss, longer alternate-path qualification, or related supplier interruption that inventory or qualified alternate paths cannot absorb; if the window ends without that transmission but pricing has changed based only on hazard maps or disclosure regulation, the judgment is falsified.
- **Audience scale**: a million-scale set of manufacturing, procurement, insurance, finance, equipment, and infrastructure professionals performs the work; this mainly **raises existing professionals' ceiling**; downstream consumers are a larger indirect reach.
- **Diffusion-gate review**: This is institutional risk pricing, not a weekly action by hundreds of millions of distinct people; Gate 1 **FAIL**.
- **Lens**: event–exposure–transmission + insurance pricing + qualification.
- **Reasoning chain**: a climate event is not a production loss → exposure damages output only through water, power, logistics, equipment service, or supplier nodes → inventory and qualified alternatives absorb part of the shock → only repeated, unabsorbed qualified transmission can change premiums, contracts, inventory, and siting; **no current source establishes that this transmission will occur inside the window, so its absence before expiry is neither a HIT nor automatically a falsification and must be reviewed against the preregistered conditions; if the loss trigger is absent but hazard-map or disclosure-regulation prior pricing appears, the symmetric falsifier applies**.
- **Time window**: 2027–2034.
- **Falsifier**: Before 2032, at least three manufacturing regions have each experienced repeated climate-related qualified-output loss that inventory or qualified alternate paths could not absorb; if, under that condition, semiconductor insurance terms, supplier contracts, qualification, inventory structure, financing cost, and siting standards show no systematic change, or changes follow hazard maps alone and remain unrelated to output loss and alternate-path qualification, the card fails. **If the loss trigger never occurs by the end of the 2034 window, but insurance terms, financing cost, or siting standards have systematically changed based only on hazard maps or disclosure regulation, the card also fails.** Repeated water, power, logistics, or site interruptions that are fully absorbed, and a trigger that never occurs without this kind of prior pricing, do not trigger falsification.
- **Leading indicator**: climate-related downtime and lost wafers, insurance deductibles and exclusions, climate audit clauses, alternate-source qualification time, common-node exposure, and post-event contract or siting changes; annually.
- **Confidence**: Medium.
- **depends-on**: J-092, J-093.
- **Strongest opposing mechanism**: long-term contracts, inventory, rapid repair, and demand substitution may keep absorbing climate shocks, allowing exposure to rise while output and financial terms remain unchanged.
- **Against consensus**: **Agreement on exposure, divergence on evidence unit**: UNU-EHS supports the exposure layer of Taiwan drought and water restrictions, FERC/NERC supports freeze-driven power-system interruption, and NXP supports only one firm's single shutdown transmission. **Boundary**: these materials do not establish repeated multi-site output loss or insurance and financing response. **Why retained**: only an event transmitted through a common node into unabsorbed loss changes economic behaviour; one incident is therefore insufficient evidence of a trend.
- **External comparison source**: EXT-69, EXT-71, EXT-74, EXT-75, EXT-76.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-094` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-095

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L93–L113`；`docs/en/ledger/91-95.md:L93–L113`

### 中文历史快照

- **历史锚点**：`1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/zh/90-ledger.md:L2423–L2441`
- **当前卡锚点**：`docs/zh/ledger/91-95.md:L93–L113`
- **提出日期**：2026-09-22
- **一句话判断**：2027–2034 年，大型晶圆厂项目越来越会在批准、补贴与公用事业合同中显式约定专用水电与适应设施由谁付费，以及资源紧缺时晶圆厂、居民和其他产业谁先被限供。
- **受众规模**：主要半导体集群周边为构造式千万量级受影响人口，直接执行者为百万量级以内的政府、公用事业、企业与社区代表；这是分配影响面，主要**提高既有专业者上限**，**不是**社会级重复动作。
- **普及闸复核**：合同与审批是低频制度动作，受影响人口不能冒充行动者；闸一不过，按制度／分配判断书写。
- **透镜**：本地外部性 + 集体行动 + 不可移动基础设施。
- **推理链**：晶圆厂韧性需要专用电力、水处理、回用、储备与应急恢复 → 资本与国家收益可跨区分配，而基础设施成本和短缺风险留在本地 → 资源稀缺时，模糊优先级变成政治与财务风险 → 出资、限供与恢复次序被写入批准和合同。
- **时间窗**：2027–2034。
- **证伪条件**：到 2032 年，在至少十个大型新建或扩建项目中，项目继续使用普通无差别公用事业服务；专用设施出资、短缺限供、应急恢复和社区补偿既未成为审批争议，也未进入公开决定或合同条款。
- **领先指标**：专用公用工程出资比例、工业与居民限供规则、优先恢复条款、社区收益协议、取水争议、费率交叉补贴、地方暂停或附条件批准；每半年。
- **置信度**：中。
- **depends-on**：J-061, J-070, J-093。
- **最强反方**：闭环水系统、专用发电与全额企业出资可能让项目与公共资源分配解耦，从而避免持续政治谈判。
- **与共识**：**机制相邻、结果未知**：J-061 及公共基础设施材料支持大型负荷会显化本地成本。**边界**：当前来源不证明晶圆厂项目的分摊与限供条款会成为常态。**我为何仍坚持**：不可移动公用工程把全国性收益与本地成本放在不同主体账本上，短缺时必须有人决定次序。
- **外部对照来源**：EXT-69, EXT-71。
- **出处**：[C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md)。
- **下次检查日**：2027-12-31。
- **状态**：ACTIVE
- **历史源未单独记录的迁移字段**：未知/未验证：冻结源卡片未记录当前分片入口、本清单的迁移审计状态或后续继任关系；这些字段仅由本清单登记，不从当前卡倒填为历史判断。

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2473–L2491`
- **Current card anchor**: `docs/en/ledger/91-95.md:L93–L113`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2027 to 2034, major fab projects increasingly specify in approvals, subsidies, and utility contracts who funds dedicated water, power, and adaptation assets and whether fabs, residents, or other industry are curtailed first during scarcity.
- **Audience scale**: major clusters create a constructed ten-million-scale affected population, while a million-scale-or-smaller set of governments, utilities, firms, and community representatives performs the decisions; this mainly **raises existing professionals' ceiling** and is distributional reach, **not** society-wide repeated action.
- **Diffusion-gate review**: contracting and approval are low-frequency institutional actions, and affected population cannot substitute for actor count; Gate 1 **FAIL**.
- **Lens**: local externalities + collective action + immovable infrastructure.
- **Reasoning chain**: fab resilience requires dedicated power, treatment, reuse, reserves, and emergency restoration → capital and national benefits travel while infrastructure cost and shortage risk stay local → under scarcity, ambiguous priority becomes political and financial risk → funding, curtailment, and restoration order enter approvals and contracts.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, across at least ten major new or expanded projects, fabs continue to take ordinary undifferentiated utility service, while dedicated-facility funding, scarcity curtailment, emergency restoration, and community compensation create neither approval disputes nor public decisions or contract terms.
- **Leading indicator**: sponsor share of dedicated-utility cost, industrial-versus-residential curtailment rules, priority-restoration clauses, community-benefit agreements, withdrawal disputes, rate cross-subsidy, and local moratoria or conditional approvals; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-061, J-070, J-093.
- **Strongest opposing mechanism**: closed-loop water, dedicated generation, and full sponsor funding may decouple projects from public resource allocation and avoid persistent bargaining.
- **Against consensus**: **Adjacent mechanism, unknown outcome**: J-061 and infrastructure material support large loads making local costs visible. **Boundary**: current sources do not establish fab allocation and curtailment clauses becoming standard. **Why retained**: immovable utilities place national benefits and local costs on different ledgers, forcing someone to choose an order under scarcity.
- **External comparison source**: EXT-69, EXT-71.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage / 双语配对与谱系

- **双语配对 / Bilingual pairing**：`J-095` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## Verification checklist / 复核清单

- **Closed-set**：exactly J-001 through J-095, once each; J-096 and later current cards are outside this historical closed set.
- **Historical preservation**：each of the 95 cards has a frozen-source Git anchor, original fields in both languages, and a current Chinese/English shard entry.
- **Unknown semantics**：unknown/unverified is used only for absent standalone fields or unstated lineage; it does not erase information inside a broader field.
- **Bilingual anchors**：each of the 95 cards has paired Chinese/English current-shard and historical-snapshot anchors; J-086/J-087 and J-095 are explicit boundary checks.
- **Mechanical checks are structural evidence only**：the repository checker cannot prove semantic equivalence or detect a birth-time semantic replacement; fresh-context review must attack those boundaries.
