# 科技史校准补录：预测失准候选与证据缺口（2026-10）

> **证据等级：`CALIBRATION`，不是相对 `holdout`，也不是未来样本外证据。** 本补录在结果已知后进行候选搜寻；它用于检查历史规则的边界，不证明方法准确率提高。没有同时满足“预测先于结果、指标同口径、原件可复查”的案例时，诚实记录零合格案。

## 1. 本轮范围与判定规则

- **领域：** 科技史；不复制政治／宏观或商业校准包的案例。
- **目标：** 寻找 T 前明确给出指标与时间窗的科技预测，并与事后同口径结果配对；优先保留失准案例。
- **合格条件：** (1) 预测原始材料的发布日期或可核验信息截止点；(2) 预测指标、数值／区间、目标时间窗和单位；(3) 结果原始材料与发布日期；(4) 结果使用同一指标、分母和单位；(5) 两端摘录可定位；(6) 选择时点虽晚于结果，也只能标为 `CALIBRATION`，不能写成 holdout。
- **不合格处理：** 任一要件缺失就记为 `unknown/unverified` 或排除，不用记忆、二手叙事或相近指标填洞。
- **本轮选择时点：** 2026-10-02。所有结果均已可见，因此不存在样本外意义。

## 2. 合格配对结果

**本轮合格配对：0。**

本补录仍保留了可稳定定位的候选配对记录：候选 A 将 1972 年的航天飞机飞行次数规划情景与 NASA 的历史结果页并列，候选 B 将 1998 年的 Iridium 用户数估计与 1999 年 10-Q 结果并列。它们是待核验的预测—结果材料对，不是已通过本轮严格门槛的合格配对；以下明确记录为何不能计入。

这不是“没有科技预测失败”，而是当前检索材料中没有一案能在本补录的严格门槛下同时完成原件定位、同口径结果和时间顺序证明。以下候选保留，是为了让缺口可复查，而不是把它们升级成证据。

## 3. 候选 A：航天飞机飞行次数——结果子集尚未由原件核对（排除）

### T 前预测原件

- **主体／材料：** Mathematica, Inc. 为 NASA 编写的 *Economic Analysis of the Space Shuttle System: Executive Summary*（NASA-CR-129570）。
- **发布日期：** 1972-01-31（标题页）；报告更新 1971-05-31 的旧分析。
- **来源：** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>
- **定位：** §0.2.2，p. 0-7；Table 0.1，p. 0-8。
- **逐字摘录：** “from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year”。
- **预测指标：** 1979–1990 共 12 年的 Space Shuttle flights；点值 514，年均 43；单位为任务／飞行次数。
- **性质：** 这是基于 NASA／DoD mission model 的规划／经济分析情景，不是概率预测；这一限制必须随案保留。

### 事后结果与缺口

- NASA 的历史资源页只确认全项目 1981-04-12 至 2011-07-21 共 135 次任务：<https://www.nasa.gov/history/space-shuttle-history-resources/>。
- 该 135 次是全项目分母，不是 1979–1990 或 1981–1990 子集；页面没有逐年／逐任务表，不能用它推导预测窗口内的结果。
- **缺失项：** 需要 NASA 的任务汇编或逐任务原始清单，逐项核对 1979–1990（或预先说明如何处理 1979–1980 无发射年份）的任务数、发布日期和定位。当前流转中得到的“1981–1990 为 38 次”只是未核对的记忆／转述，不计入结果。
- **判定：** `unknown/unverified`，不计为合格失准。不能写成“514 对 38”的确定结论。

## 4. 候选 B：Iridium 用户数——远期预测没有同窗结果，近期开具的 covenant 不是 T 前预测（排除）

### 远期预测原件

- **主体／材料：** Iridium LLC / Iridium World Communications Ltd. FY1997 Form 10-K405。
- **提交日期：** 1998-03-25。
- **来源：** <https://www.sec.gov/Archives/edgar/data/948421/0000950133-98-000917.txt>
- **定位：** `THE IRIDIUM MARKET – GENERAL` 段，文本约行 900–930（SEC 原件需以下载版本重新定位）。
- **逐字摘录：** “Iridium estimates that it will have customer counts in the year 2002 in the range of 2.2 million to 2.5 million for its satellite-based voice services … 1.0 million to 1.3 million … and 350,000 to 500,000 …”。
- **指标：** 2002 年 customer counts；分服务类型；单位为 subscribers／customers。

### 结果与口径缺口

- Iridium 在 1999-03-31 的 10-Q（提交 1999-05-17）记载：截至 1999-03-31，7,188 个 Iridium World Satellite Service subscribers、10,294 个 total subscribers：<https://www.sec.gov/Archives/edgar/data/1035442/0000950133-99-001884.txt>，原件约行 1760。
- 该结果是 1999-03-31，不是 2002；而且远期预测分服务类型与结果披露的合计口径不对齐，不能作为同窗配对。
- 10-Q 还转述一项**截至 1999-03-31 的融资 covenant 最低门槛**：“at least 27,000 Iridium World Satellite Service subscribers and at least 52,000 total subscribers”；这份 10-Q 在结果日之后提交，因此不是 T 前预测原件。用 27,000／52,000 对 7,188／10,294 会制造“预测失准”的假配对。
- **缺失项：** 若要使用该候选，必须找到 1998-12 至 1999-03-31 之前发布的原始文件，证明 27,000／52,000 是当时预先公开的预测／目标，并明确它是公司预测还是融资条款；本轮未完成。
- **判定：** 2002 远期案 `unknown/unverified`；1999 covenant 案排除，不计为合格失准。

## 5. 本轮主动排除的常见替代

- **把 NASA 全项目 135 次当作 1979–1990 结果：** 分母错误。
- **把未经 NASA 原件核对的 38 次当作结果：** 结果来源不可复查，违反原件要求。
- **把 Iridium 10-Q 中结果日后的 covenant 门槛当作 T 前预测：** 时间顺序错误。
- **把 2002 预测与 1999 结果直接比较：** 观察窗和服务分组不一致。

## 6. 对方法的有限校准含义

本轮没有新增未来判断卡，也没有产生可用于命中率、Brier 分数、相对判别增量或跨案例准确率的样本。它只留下一个可操作的边界：科技史校准不能因为“技术最终没有按宣传普及”就自动成为失准案；必须先冻结目标年份、活动分母、单位和结果口径。对科技能力尤其要区分：规划情景、融资 covenant、市场规模估计、概率预测和事后叙事。

下一次若继续科技史搜寻，应优先取得可读的 NASA 逐任务汇编或同类官方预测／统计系列；在此之前，本补录的诚实结论是**合格案为零，缺口已具体列明**。

## 8. 2026-10-09 原始抓取复核：三条新科技候选均终局为 UNKNOWN/UNVERIFIED

本节不是把旧候选换名重报，而是一次有界的原始来源抓取。抓取时间均为 UTC；`bytes` 是 `curl` 下载体的字节数，SHA-256 对应保存的响应体。三条候选都含有本次提交前全文不存在的来源标识与逐字摘录，因此满足“确实抓取过”的最低证明；三条都因结果口径或项目身份缺口留在 `UNKNOWN/UNVERIFIED`，不增加科技域合格计数。

### 8.1 T-X33：X-33 飞行测试开始时间（UNKNOWN/UNVERIFIED）

- **T 前原件：** NASA NTRS citation `19990070318`，*The X-33 Flight Test Challenge*；来源 <https://ntrs.nasa.gov/api/citations/19990070318>。
- **抓取证明：** `2026-10-09T03:07:26Z`；HTTP `200`；`3,654` bytes；SHA-256 `22f932ca781b99da8d9437954cb79d2df1b0ed6e7e9a45409797ad704140f095`。
- **本次新增逐字摘录：** “Flight testing will begin in July 2000, with launches originating from Edwards Air Force Base and initial landings at Michael Army Airfield in Utah.”
- **科技域归属：** 预测量是飞行测试启动这一技术部署里程碑，不是收入、亏损或订阅数。
- **结果侧抓取：** NASA NTRS citation `20110016255` 的全文响应，`2026-10-09T03:07:29Z`、HTTP `200`、`34,058` bytes、SHA-256 `ea57e94432d546013b21e9848a75bc4c38a29c09ae7aa367f4f53caa2dbe865e`；其中新增摘录为 “Although a cryogenic tank failure during testing ultimately led to the end of the effort”。
- **终局与缺口：** `UNKNOWN/UNVERIFIED`。结果原件确认项目因储罐失败结束，但本轮没有从同一结果材料建立“截至 2000-07 是否完成首飞／零次首飞”的明确分母与时间点，不能把“项目结束”偷换成“7 月预测失准”。最强替代解释是预测本来只承诺启动测试，不承诺首飞；该解释目前无法被结果原件排除。
- **排除性记录：** 同一预测材料还谈到低成本入轨目标、发动机与热防护技术验证；这些是成本目标或子系统验证，不是本案的飞行测试启动指标，不能替代结果列。

### 8.2 T-X34：X-34 首次飞行计划（UNKNOWN/UNVERIFIED）

- **T 前原件：** NASA NTRS citation `19990019135`，*X-34 Program Status*；来源 <https://ntrs.nasa.gov/api/citations/19990019135>。
- **抓取证明：** `2026-10-09T03:18:53Z`；HTTP `200`；`3,256` bytes；SHA-256 `8e926b7f4d8d8b5aa0102aff8c70eea964c98fdab6e29c27d9b135a425d94c07`。
- **本次新增逐字摘录：** “The X-34 program has moved rapidly from the drawing board to hardware build-up, with the first flight scheduled for 1999.”
- **科技域归属：** 预测量是可重复使用运载器技术验证器的首次飞行部署时间，不是商业收入或公司经营指标。
- **结果侧线索：** NASA NTRS citation `20000092068`（*X-34 Project: Overview and Status*）响应于 `2026-10-09T03:18:55Z` 抓取，HTTP `200`、`3,378` bytes、SHA-256 `8d3434fd0164e8bdaf72b3cc9f1a661f2d401a0e75124e76ed2269879d58311c`。它只证明存在后续状态材料，没有在本轮取得可定位的“1999 年实际首飞／取消前状态”结果段落。
- **终局与缺口：** `UNKNOWN/UNVERIFIED`。缺少同一观察窗内的官方结果摘录、取消日期及“是否完成 powered flight”的明确分母，不能把二手的“后来取消”叙述当作结果。最强替代解释是“首次飞行”指无动力或 captive-carry 测试而不是 powered flight；本轮未取得能排除该解释的原件。
- **排除性记录：** 后续状态材料中的发动机、热防护和设计图是能力／部件状态，不是首次飞行结果；不能用它们填补观察窗。

### 8.3 T-FREEDOM：Space Station Freedom 首个组件与 ISS 首次组件（UNKNOWN/UNVERIFIED）

- **T 前原件：** NASA NTRS citation `19900046020`，*Space Station Freedom — A program update*；来源 <https://ntrs.nasa.gov/api/citations/19900046020>。
- **抓取证明：** `2026-10-09T03:11:02Z`；HTTP `200`；`2,881` bytes；SHA-256 `b1393592c9f584c5a285a88d8ecac63357e0bc0cdc642f905f6bbeb926edce0e`。
- **本次新增逐字摘录：** “A first Freedom-element launch by the Space Shuttle is planned for 1995, with completion of the assembly process by 1998.”
- **科技域归属：** 预测量是空间站组件发射与组装完成的部署里程碑，不是商业财务量。
- **结果侧材料：** NASA NTRS citation `20000109670` 的响应于 `2026-10-09T03:11:04Z` 抓取，HTTP `200`、`3,778` bytes、SHA-256 `6a4e6eaefb817bcfb7c91d1ad72dffd5e83c1ddd819a4eb14ac238d0e95a6ab9`；新增摘录为 “This element (Stage 1A/R) was launched on 20 November 1998 and is currently operating on-orbit.”
- **终局与缺口：** `UNKNOWN/UNVERIFIED`。预测对象是 Freedom，结果材料是其后重构的 ISS；本轮没有取得同一项目定义下的“Freedom 首个组件／组装完成”结果，无法证明两者是同一分母。最强替代解释是项目重构后仍可把 ISS 视作 Freedom 的连续部署，因此把 1998 的 FGB 发射直接当作 Freedom 结果；这需要项目谱系与指标映射原件，当前没有。
- **排除性记录：** 结果材料同时包含 2000 年 Service Module 计划和美国实验舱的 TBD 状态；这些是不同组件／不同版本的计划，不能与 1990 年 Freedom 的“首个组件／组装完成”列混用。

### 8.4 本轮判定与边界

三条新候选均已终局为 `UNKNOWN/UNVERIFIED`；科技域合格配对仍为 **0**，三域合计仍为 **6/12**。它们不是旧清单中的 `T-SHUTTLE`、Iridium 2002，也不是核电、卡特太阳能、第五代计算机或 VR 的重复材料；新标识 `19990070318`、`19990019135`、`19900046020` 及其字段缺口使本轮至少留下了此前仓库没有的证据状态。`CALIBRATION` 不支持推翻任何普及闸；本轮没有指名独占案例表行，也没有触碰 `:388` 的重审债，因此不提出推翻闸门的主张。

本轮不能升级为命中率、Brier 分数、holdout 或样本外证据。本记录遵守[历史伪样本外验证协议](../zh/02-historical-validation-protocol.md)和方法论对 `CALIBRATION` 的边界：结果已知后选入的案例只能用于校准和暴露规则缺口，不能冒充 holdout。未来真实样本外证据仍只能来自预登记判断卡在时间窗到期后的复核。
