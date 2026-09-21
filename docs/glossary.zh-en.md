# 术语对照 · Glossary

## 一、核心概念 · Core concepts

| 中文 | English | 用法 |
|---|---|---|
| 丰富 | abundance | 某种能力、供给或资源变得更多、更便宜、更容易获得 |
| 稀缺 | scarcity | 相对于需求仍受约束、因而价值上升的要素 |
| 判断 | judgment | 带推理链、时间窗、证伪条件、领先指标和置信度的可检验主张 |
| 仅图景 | landscape only | 有助于理解未来但缺少完整判断字段、暂不作为可下注主张的内容 |
| 商机候选 | opportunity candidate | 通过丰富→稀缺闸门、且有明确付费者和硬约束支撑的方向（出口 A） |
| 窗口机会 | window opportunity | 目前可获利但预计会被同一股力量自动化、只能短期下注的方向，必须注明预计关闭年份 |
| 结构性后果 | structural consequence | 通过硬约束检验但没有明确付费者的可检验社会、组织或关系推论（出口 B） |
| 临床级因果证明 | clinical-grade causal proof | 能支持特定医疗使用场景并接受监管、伦理与结果追责的前瞻性证据，不等同于模型生成的相关性或候选解释 |
| 连续照护 | continuity of care | 跨时间持续观察、干预并在异常时升级的照护闭环，不只是一次问答 |
| 可验证掌握 | verifiable mastery | 在不依赖生成帮助的受控或迁移任务中，能重复表现出的知识或技能 |
| 过程证据 | process evidence | 能把成品与本人真实练习、版本演进或现场表现连接起来的可复核记录 |
| 透镜 | lens | 用于观察未来的推理角度；本项目使用 L1–L9 |
| 约束迁移 | constraint migration | 一个瓶颈解除后，系统瓶颈跳到另一个环节 |
| 关系不对称 | relational asymmetry | 互动双方在记忆、耐心、可复制性或专属性等方面存在结构性差异 |

## 二、闸门与硬约束 · The gate and hard constraints

| 中文 | English | 用法 |
|---|---|---|
| 闸门 | gate | 进入商机候选的必过检验：新稀缺能否被制造丰富的同一股力量自动化 |
| 三问 | the three questions | 丰富什么 → 因此稀缺什么 → 该新稀缺能否再次被同一股力量丰富 |
| 硬约束 | hard constraint | 挡住「同一股力量把新稀缺也自动化」的结构性限制，只认下列五类白名单 |
| 物理 | physical | 必须在现实世界移动质量、消耗能量、等待时间流逝或进行身体操作 |
| 法律／责任 | law / liability | 需要能被起诉、赔偿、许可或承担责任的主体 |
| 信任／关系 | trust / relationship | 依赖长期重复博弈、声誉和关系积累，不能一次生成 |
| 产权／私有性 | ownership / private property | 关键输入由他人合法持有，不能仅靠算力复制或强取 |
| 身体在场 | embodied presence | 需求本身要求有人真实地到场、触碰或共同经历 |
| 不可逆性 | irreversibility | **辅助透镜，不是第六类硬约束**：用于检验上述约束的后果代价，须在推理链与反方中单独说明，不得据此单独过闸 |
| 出口 A | Exit A | 通过硬约束闸门且能指出付费者的商机候选 |
| 出口 B | Exit B | 通过硬约束闸门但没有付费者的结构性后果 |
| 出口 C | Exit C | 缺少完整判断字段或置信度过低的仅图景内容 |

## 三、判断卡片字段 · Judgment-card fields

| 中文 | English | 用法 |
|---|---|---|
| 推理链 | reasoning chain | 卡片字段：从底层规律经过中间环节到判断的可复核路径 |
| 时间窗 | time window | 判断预期发生并接受检验的时间区间 |
| 证伪条件 | falsifier | 一旦观察到就承认判断错误的具体事件或指标 |
| 领先指标 | leading indicator | 在判断结果出现前会先发生变化、可用于跟踪的信号 |
| 置信度 | confidence | 对判断成立概率与证据强度的分档表达，只用高／中／低三档，不是修辞强度 |
| depends-on | depends-on | 卡片字段名，不翻译：本判断踩在哪几条上游判断之上 |
| 依赖链 | dependency chain | 由 `depends-on` 连接的判断关系；远期判断建立在近期判断之上 |
| 最强反方 | strongest counterargument | 能推翻本判断的最有力机制，而不是最容易反驳的弱化版本 |
| 与共识 | consensus comparison | 与主流共识的一致／分歧，以及为何仍坚持或据此降低置信度 |
| 外部对照来源 | external comparison source | 独立推演完成后才引入的外部材料编号（EXT-N） |
| 出处 | source | 本判断的论证正文所在文件 |
| 下次检查日 | next review | 到期检查的计划日期 |
| 判断状态 | judgment status | `ACTIVE`／`HIT`／`FALSIFIED`／`REVISED`，不翻译 |
| 我会撤回的信号 | retraction signal | 机会候选专用：出现即撤回或降级该候选的具体观察 |
| 观察这个指标 | watch this indicator | 机会候选专用：可持续跟踪的领先信号 |

## 四、文档结构 · Document structure

| 中文 | English | 用法 |
|---|---|---|
| 判断台账 | judgment ledger | 判断卡片的唯一住所（`90-ledger.md`）；正文不复制卡片内容 |
| 推演链 | reasoning-chain document | 编号 `C1`、`C2`…（不是 `C-N`）的长论证文件：沿一条因果线纵向讲到底，区别于卡片字段「推理链」；编号只在 [推演链登记](../README.md#推演链登记) 分配 |
| 时间层 | time layer | 近期／中期／远期三篇正文；粗粒度容器，不是严格日历 |
| 近期／中期／远期 | near / mid / far term | 2026–2028 / 2029–2032 / 2033–2040；精度由每条判断自己的时间窗承担 |
| 判断编号 | judgment identifier | `J-NNN`，全项目唯一、中英共用、不复用、不翻译 |
| 机会编号 | opportunity identifier | `O-NNN`，商机候选专用，与判断编号同规则 |
| 到期检查 | expiry review | 按卡片「下次检查日」逐条复核证伪条件是否触发，并记入检查日志 |
| 显式缺口 | explicit gap | 已知未覆盖的维度，以条目形式保留在台账，不因首轮有产出而删除 |
| 发布前自检清单 | pre-publication checklist | 台账末节的跨文件不变量清单，每次发布前逐项过一遍 |

## 五、历史验证协议 · Historical validation protocol

| 中文 | English | 用法 |
|---|---|---|
| 校准集 | calibration set | 可以看结局并用于改规则的历史案例；不得再作为验证样本 |
| 历史伪样本外留存集 | historical pseudo-out-of-sample holdout | 规则与材料先冻结、判闸后一次性揭晓的历史子集；只能支持共同泄漏下的相对比较 |
| 截点资料包 | as-of packet | 只含判定时点 T 及更早信息的标准化案例材料 |
| 识别探针 | identification probe | 判闸前提交的案例身份猜测、结局猜测与置信度，用于测量记忆泄漏 |
| 判闸者 | gate judge | 不接入仓库与揭晓来源、只依据截点资料包逐闸判定的独立角色 |
| 结局判定者 | outcome adjudicator | 判闸和基线提交后，依据预登记来源独立编码历史结局的角色 |
| 分歧／解锁裁决者 | disagreement / unlocking arbiter | 在结局编码冻结后裁定定义争议或预写解锁条件是否出现的独立角色 |
| 基线臂 | baseline arm | 与判闸臂使用同一模型和输入、但使用不同规则的比较条件 |
| 判别力 | discrimination | `P(S \| PASS) − P(S \| VETO)`，比较放行组与否决组实际社会级普及率的差 |
| 致命漏判 | fatal false veto | 五道闸给出 `VETO`、但历史结局为 S 的高代价错误；是否进一步触发判断卡自身证伪条件由台账另行裁定 |
| 弃权 | abstention | 材料不足时拒绝判定；必须计入覆盖率，不能靠多弃权提高分数 |
| 中间态 | intermediate outcome | 持续采用但既未成为定义人群多数、也未退出的历史结局 |
| 解锁条件 | unlocking condition | 速度层否决时预先写下的、可观察且有主体与时点的翻案条件 |
| 相对判别增量 | relative incremental discrimination | 五道闸判别力减去最强同输入基线判别力；不是绝对准确率 |

## 六、能源与许可 · Energy and permitting

C3 推演链引入的术语，中英文档须照此一一对应。

| 中文 | English | 用法 |
|---|---|---|
| 并网许可 | interconnection permit | 授权主体批准某一负载或电源接入电网的行政许可 |
| 并网排队 | interconnection queue | 等待并网审批与容量分配的项目序列；排队位置本身具有价值 |
| 大负荷接入 | large-load interconnection | 数据中心类大容量用电主体的接入申请，区别于发电侧排队 |
| 可交付电力 | deliverable power | 不是发电能力，而是能在承诺日期真正送到某一位置的电力 |
| 投产日期担保 | in-service date guarantee | 合同条款：承诺通电日期并为延迟负赔偿责任 |
| 容量预留费 | capacity reservation fee | 为锁定尚未使用的变电容量而支付的费用 |
| 过桥供电 | bridge power | 在并网完成前用自备发电或储能临时供电的安排 |
| 可调度负荷 | schedulable load | 可暂停、可延后、可跨区迁移的算力负荷，与延迟敏感负荷相对 |
| 需求响应 | demand response | 电网付费购买用户侧减载或移负荷的机制 |
| 可中断电价 | interruptible tariff | 以接受被中断为条件换取更低电价的安排 |
| 社会许可 | social licence | 本地居民与地方政治对项目的默认容忍；失去它会变成真实选址成本 |
| 本地外部性 | local externality | 成本落在本地、收益归于外部股东的部分 |
| 使用侧管制 | use-side control | 管制对象从硬件实物转向主体、用途与场址授权 |
| 权重转移 | weight transfer | 模型权重的跳转与跨境传递，已成为管制客体 |
| 东道国 | host state | 提供场址与电力以换取算力投资的国家 |
| 能力主权 | capability sovereignty | 对能力本身的处置权，区别于仅获得租金与就业 |

术语在中文与英文文档中保持一一对应；判断编号与机会编号不翻译、不重新编号。
