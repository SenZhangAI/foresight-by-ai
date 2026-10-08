# 历史校准证据切片：科技、公共政策与商业（2026-10-02）

> **证据边界（先读）：** 本文件是结果已知后整理的跨领域 `CALIBRATION` 切片。它用于校准记录字段、暴露预测失效边界，不能证明本项目的准确率、Brier 分数、跨领域判别增量或未来预测能力。它不是 `CONTAMINATED_RELATIVE_HOLDOUT`，也不是 `GENUINE_FUTURE_OOS`。
>
> 本切片没有凑案例数：两案有可重建的预测—结果配对，科技案只有可重建的预测材料而结果配对仍未闭合，故明确保留 `UNKNOWN/UNVERIFIED`。所有案例于 2026-10-02 选择或整理，结果已知后的选择决定了其最高证据等级只能是 `CALIBRATION`。

> **与其他计数的关系：** 本文件是一个单独的 evidence slice，不是仓库总档案。它自身只有 **2 条**可重建配对（`P-04`、`B-WEBVAN`）+ **1 条** `UNKNOWN/UNVERIFIED` 候选（`T-SHUTTLE`）。仓库全量 `CALIBRATION` 档案是 **6 条**；方法论当前摘要把本切片与下一批合并为 **3 条**配对 + 1 条未知候选。见[历史回顾的计数导航](../zh/01-retrospect.md#103-最新跨领域证据切片与下一批等级观察窗与口径2026-10)。

## 1. 分类与记录协议

每案都尽量记录以下字段：预测主体与原始材料、结果主体与原始材料、预测日期或信息截止点、结果日期、观察窗、预测与结果指标、单位、人口／对象分母或基期、比较规则、逐字摘录、仓库副本定位、原始字节哈希，以及 `unknown/unverified` 缺项。

- `CALIBRATION`：结果已经可见后才选择或整理；可用来发现规则边界，不能用来计算未经预先冻结的总体准确率。
- `CONTAMINATED_RELATIVE_HOLDOUT`：只有在结果揭晓前冻结可枚举候选总体、T 前材料、分层与分配、同输入基线、评分规则和揭晓顺序，才可作为相对检验；本切片没有执行这些步骤。
- `GENUINE_FUTURE_OOS`：预登记的未来判断卡在观察窗结束后复核；本切片没有这类案例。
- `UNKNOWN/UNVERIFIED`：关键原件、同口径结果、定位或分母尚未闭合；不得计入合格案例数或准确率分母。

## 2. 切片总表

| case_id | 领域 | 预测与结果 | 证据等级 | 观察窗 | 可计入什么 | 不能计入什么 |
|---|---|---|---|---|---|---|
| `P-04` | 公共政策／宏观经济 | FOMC 预测 2008 年实际 GDP 正增长；BEA 同口径结果为 −0.8% | `CALIBRATION` | 预测点 2007-10-30/31；目标 2008 Q4/Q4；结果发布 2009-03-26 | 一条可重建的方向失准记录；宏观中心区间漏掉危机转折的边界材料 | 宏观预测总体准确率、Brier 分数、普及闸验证 |
| `B-WEBVAN` | 商业 | 1999 年披露的 Webvan 2000 年收入／净亏损 projection；2000 年 10-K 结果 | `CALIBRATION` | 1999-12-10 至 2000 财年结束，结果于 2001-04-02 披露 | 一条可重建的公司财务规模失准记录；收入、亏损与部署假设应分开记录 | 社会扩散规则被证伪、商业预测总体准确率 |
| `T-SHUTTLE` | 科技／航天 | 1972 年航天飞机飞行规划为 1979–1990 共 514 次；同窗实际任务结果尚未由原始清单重建 | `UNKNOWN/UNVERIFIED` | 候选目标窗 1979–1990，共 12 年 | 证明科技案例必须先闭合同窗结果与分母；保留一个可继续调查的候选 | 不得写成“514 对 38”的确定失准，不计入合格配对 |

**当前计数：** 可重建配对 2 条（`P-04`、`B-WEBVAN`），科技领域合格配对 0 条；`T-SHUTTLE` 不进入分母。这不是样本量意义上的验证，也不是准确率。

## 3. `P-04`：FOMC 对 2008 年实际 GDP 的预测

### 3.1 身份、原始定位与日期

- **预测主体：** Federal Reserve Board，FOMC participants。
- **预测原始材料：** *Summary of Economic Projections, October 30–31, 2007*；仓库副本 [`prediction.html`](politics-artifacts/P-04/prediction.html)，HTTP 200，原始字节 SHA-256 `cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`；原始来源：<https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>。
- **预测日期／信息截止点：** 2007-10-30/31 会议日期。副本没有独立发布日期，所以不把 2007-10-31 写成已核实的发布日期。
- **结果主体：** Bureau of Economic Analysis。
- **结果原始材料：** *Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*；仓库副本 [`outcome.html`](politics-artifacts/P-04/outcome.html)，页面标明 2009-03-26 08:30 EST，HTTP 200，原始字节 SHA-256 `25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`；原始来源：<https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>。
- **结果日期／观察结束：** 2009-03-26 的最终估值发布；目标观察期为 2008 Q4/Q4。
- **证据等级：** `CALIBRATION`。本案在 2026-10-02 由已知结果的材料中选取。

### 3.2 指标、单位、分母与逐字摘录

- **预测指标：** 美国实际 GDP，2008 Q4/Q4 增长率。
- **预测值与单位：** `+1.8%–+2.5%`，percent growth rate。
- **分母／基期：** 2007 Q4 实际 GDP 为基期，2008 Q4 为目标期；不是人口分母。
- **预测定位：** `prediction.html` 字节区间 `[8275,8558)`，摘录 SHA-256 `d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`；原文：`central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent`。
- **结果指标：** 同一 Q4/Q4 实际 GDP 增长率，`−0.8%`。
- **结果定位：** `outcome.html` 字节区间 `[33844,34200)`，摘录 SHA-256 `484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`；原文：`During 2008 ... real GDP decreased 0.8 percent.`

### 3.3 判定与缺项

- **判定：** 预测区间全部为正，结果为负，记为 `direction miss`；结果比预测下沿低 2.6 个百分点，比上沿低 3.3 个百分点。
- **同口径依据：** 预测脚注与结果原件都使用 Q4/Q4 实际 GDP 增长；没有用年度平均值、名义 GDP、人均 GDP或总量替换。
- **`unknown/unverified`：** 完整参与者级分布、概率、预测时的实时数据 vintage、之后的修订路径、同输入基线及预先指定的评分规则均未知。
- **允许的解释范围：** 本案支持“平滑的宏观中心区间可能漏掉危机转折”这一方法边界；不支持宏观预测总体不可靠，也不单独证伪任何普及闸。

## 4. `B-WEBVAN`：Webvan 2000 年财务 projection

### 4.1 身份、原始定位与日期

- **预测主体：** Goldman Sachs 代表在投资者电话会议中的 projection；Webvan 的 S-1 在结果前披露了这段话及其假设限制。不能把披露的 projection 扩写成完整概率预测。
- **预测原始材料：** Webvan S-1，filed 1999-12-10；SEC 原件：<https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt>；仓库定位、页码、原文件行 820–929 与 SHA-256 `05b7375d74ddd6835230d15a6e625206b93ce78a4457fa6d28d54ceafcb55ece` 见[商业校准证据包](business-forecast-calibration-2026-09.md)。
- **预测日期／信息点：** 1999-12-10；目标为 2000 财年，距财年结束约 12 个月。
- **结果原始材料：** Webvan Group, Inc. 2000 Form 10-K，filed 2001-04-02；SEC 原件：<https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt>；仓库定位、页码、原文件行 830–863 与 SHA-256 `1fa9948622c6eeb5a8b15ce05ad98b0fe0b7060afae75ec17a8de4d430909e28` 见[商业校准证据包](business-forecast-calibration-2026-09.md)。
- **结果日期／观察结束：** 2000 财年结果在 2001-04-02 文件中披露。
- **证据等级：** `CALIBRATION`。本案在结果已知后选入。

### 4.2 指标、单位、分母与逐字摘录

- **预测指标与单位：** Webvan 公司 2000 财年收入 `$120.0m`、净亏损 `$154.3m`；单位为美元。
- **预测对象／分母：** 单一公司的 2000 财年财务结果，不是用户数、市场总额或社会采用率。
- **预测摘录：** `The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.`
- **结果指标与单位：** 2000 年 Net Sales `$178.456m`、Net Loss `$453.289m`；10-K 表格原单位为 thousands。
- **结果摘录：** `Net Sales $178,456`；`Net Loss $ (453,289)`；`Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.`

### 4.3 判定与缺项

- **判定：** 收入实际约为预测的 1.49 倍，约高 48.7%；净亏损实际约为预测的 2.94 倍，绝对差约 `$298.989m`，主分类为 `scale miss`。
- **同口径依据：** 主指标使用双方明确出现的 `net loss`；`revenue` 与 `Net Sales` 仅作辅助指标，不隐藏术语差异。
- **`unknown/unverified`：** 预测没有概率分布、基线预测或预先指定评分规则；不能从单一公司案例推出商业预测总体准确率。
- **允许的解释范围：** 该案要求将收入、亏损、部署节奏和机制假设分开记录；它不是社会扩散规则失效的证据。

## 5. `T-SHUTTLE`：科技候选，结果配对未闭合

### 5.1 可重建的预测材料

- **预测主体／材料：** Mathematica, Inc. 为 NASA 编写的 *Economic Analysis of the Space Shuttle System: Executive Summary*（NASA-CR-129570）。
- **预测原始来源：** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>；标题页日期 1972-01-31；定位 §0.2.2 p. 0-7、Table 0.1 p. 0-8。
- **逐字摘录：** `from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year`。
- **预测指标／单位：** 1979–1990 共 12 年的 Space Shuttle flights；点值 514，年均 43 次。
- **对象分母：** 12 年时间窗与计划任务次数；材料将其描述为 NASA／DoD mission model 的规划／经济分析情景，而非概率预测。
- **证据等级：** `UNKNOWN/UNVERIFIED`，不是 `CALIBRATION` 配对。

### 5.2 结果材料为何不能填写

- 目前定位到的 NASA 历史资源页 <https://www.nasa.gov/history/space-shuttle-history-resources/> 只确认全项目 1981-04-12 至 2011-07-21 共 135 次任务。
- 135 次是全项目总数，不是 1979–1990 的同窗子集；该页面没有可逐项复核的逐年／逐任务原始表。
- 尚缺：NASA 官方逐年或逐任务清单、每项任务日期与定位，以及如何处理 1979–1980 无发射年份的预先固定分母规则。
- 因此不得将未经原始清单核对的“1981–1990 为 38 次”写成结果，也不得写成“514 对 38”的确定失准。
- **升级条件：** 只有取得同窗官方任务清单、逐项复核窗口内任务数并固定分母处理，才能升级为 `CALIBRATION` 配对；否则保持 `UNKNOWN/UNVERIFIED`。

## 6. 这组材料改变什么，不改变什么

**能支持：**

1. 跨科技、公共政策与商业案例必须同时保留预测时间、结果观察窗、指标、单位、分母／基期、原件定位、摘录和缺项；“主题相近”不能替代同口径。
2. 宏观中心区间可能漏掉危机转折；公司收入方向接近不等于亏损规模校准；科技规划情景不能在缺少同窗任务清单时被伪装成失准案例。
3. 技术案例必须把能力、规划情景、融资门槛、市场规模估计和概率预测分开；不同证据类型不能混算。

**不能支持：**

- 不能计算本项目或任何领域的准确率、Brier 分数、命中率或跨领域判别增量。
- 不能把本切片改写成 `CONTAMINATED_RELATIVE_HOLDOUT`：没有预先冻结总体、T 前包、分配、同输入基线、评分规则和一次揭晓。
- 不能声称五道普及闸已经验证或某一道已被证伪。
- 不能把历史校准材料转写成新的未来判断卡；真正 `GENUINE_FUTURE_OOS` 证据仍须来自事前登记、未来到期的判断卡。

## 7. 可追溯入口与双语约束

- 方法边界：[历史伪样本外验证协议](../zh/02-historical-validation-protocol.md)。
- 已有跨领域轮次：[历史校准轮](historical-calibration-round-2026-10.md)。
- 政治材料：[政治校准证据包](politics-calibration.md) 与 `politics-artifacts/P-04/`。
- 商业材料：[商业预测校准证据包](business-forecast-calibration-2026-09.md)。
- 科技材料：[科技史校准补录](technology-calibration-addendum-2026-10.md)；本切片的 `T-SHUTTLE` 只补充其可重建性边界，不把候选升级为合格案例。
- 英文镜像：[Historical Calibration Evidence Slice](historical-calibration-2026-10-02.en.md)。中英文共用 case_id、证据等级、日期、口径与缺项；英文不是独立计数。

**本切片交付结论：** 2 条可重建的 `CALIBRATION` 配对（公共政策 1、商业 1），1 条科技 `UNKNOWN/UNVERIFIED` 候选；没有相对 holdout、未来样本外证据或准确率结论。
