# 历史校准轮：跨领域预测—结果记录（2026-10）

> **证据边界：** 本文件是结果已知后整理的 `CALIBRATION` 记录，不是相对 `holdout`，也不是未来样本外证据。它用于把可复核的历史失准与明确缺口放在同一张桌面上，不能计算准确率、Brier 分数或跨领域判别增量。
>
> **本轮没有新增未来判断。** 科技方向当前仍没有满足严格门槛的合格配对；保留 `unknown/unverified` 是交付结果，不用相近指标凑数。

> **计数范围：** 本文件是“历史校准轮”记录，**本轮**合格配对为 2 条；它不是仓库全量档案（全量为 6 条），也不是方法论当前摘要（两份最新记录合计 3 条配对 + 1 条未知候选）。

## 1. 记录规则与分类

本轮统一记录：预测日期或信息截止点、结果日期与观察窗、预测与结果指标、单位、人口／对象分母或基期、原始材料定位、结果材料定位、逐字摘录或明确缺失项。分类只能是：

- `CALIBRATION`：结果已经可见后才选择或整理；可用来发现规则边界。
- `CONTAMINATED_RELATIVE_HOLDOUT`：只有在候选总体、T 前材料、分配、同输入基线与揭晓顺序预先冻结后才可使用；本轮没有这样的案例。
- `GENUINE_FUTURE_OOS`：预先登记的未来判断卡到期后复核；本轮没有这样的案例。
- `UNKNOWN/UNVERIFIED`：至少一项关键材料、同口径结果或定位尚未闭合；不得计入合格案例或准确率分母。

所有案例在 2026-10-02 选择／整理，因而本文件中的已配对案例均只能是 `CALIBRATION`。

## 2. 案例总表

| case_id | 领域 | 预测—结果 | 证据分类 | 观察窗 | 结论 |
|---|---|---|---|---|---|
| `P-04` | 宏观经济／公共政策 | FOMC 预测 2008 年实际 GDP 正增长；BEA 结果为负增长 | `CALIBRATION` | 2008 Q4/Q4；预测点至 2009-03-26 发布 | 合格的同口径方向失准案例；不支持准确率结论 |
| `B-WEBVAN` | 商业 | 1999 年披露的 2000 年收入／净亏损 projection；2000 10-K 结果 | `CALIBRATION` | 1999-12-10 至 2000-12-31 | 合格的数值规模失准案例；不等同于社会扩散规则失效 |
| `T-SHUTTLE` | 科技／航天 | 1972 年航天飞机飞行规划；结果子集尚未由原件重建 | `UNKNOWN/UNVERIFIED` | 1979–1990（候选目标窗） | 不计入合格案例；缺逐任务结果与同窗分母 |

**计数规则：** 本轮合格配对为 2（`P-04`、`B-WEBVAN`），但二者都是 calibration；科技合格配对为 0。计数不表示总体准确率，也不表示方法已验证。

## 3. P-04 · FOMC 对 2008 年实际 GDP 的预测

### 身份与时间

- **预测主体：** Federal Reserve Board，FOMC participants。
- **预测材料：** *Summary of Economic Projections, October 30–31, 2007*。
- **预测原件：** [`politics-artifacts/P-04/prediction.html`](politics-artifacts/P-04/prediction.html)，HTTP 200，SHA-256 `cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`；来源：<https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>。
- **预测日期／信息截止点：** 2007-10-30/31 会议日期。副本没有独立发布日期，因此不把 2007-10-31 写成已核实发布日期。
- **结果主体：** Bureau of Economic Analysis。
- **结果材料：** [`politics-artifacts/P-04/outcome.html`](politics-artifacts/P-04/outcome.html)，页面标明 2009-03-26 08:30 EST，HTTP 200，SHA-256 `25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`；来源：<https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>。
- **结果日期／观察结束：** 2009-03-26 最终估值发布；目标窗为 2008 Q4/Q4 实际 GDP 增长。

### 指标、分母与摘录

- **预测指标／单位：** 美国实际 GDP，2008 Q4/Q4，percent growth rate；区间 `+1.8%–+2.5%`。
- **预测对象／基期：** 美国实际 GDP；2007 Q4 为基期，2008 Q4 为目标期。这里的分母是增长率定义中的实际 GDP 基期，不是人口。
- **预测摘录：** `prediction.html` 字节区间 `[8275,8558)`；摘录 SHA-256 `d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`：
  > “central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent”
- **结果指标／单位：** 同一 Q4/Q4 实际 GDP 增长率，`−0.8%`。
- **结果摘录：** `outcome.html` 字节区间 `[33844,34200)`；摘录 SHA-256 `484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`：
  > “During 2008 ... real GDP decreased 0.8 percent.”

### 判定与缺口

- **判定：** 预测区间全部为正，结果为负，记为 `direction miss`；结果比预测下沿低 2.6 个百分点，比上沿低 3.3 个百分点。
- **可比性：** 预测脚注和结果原件都使用 Q4/Q4 实际 GDP 增长；没有用年度平均值、名义 GDP 或人均 GDP 替换。
- **缺失／未验证：** 完整参与者级分布、概率、预测时点的实时数据 vintage、之后的修订路径、同输入基线和预先指定评分规则均未知。因此不能算 Brier、对数评分、相对判别增量或总体命中率。
- **方法边界：** 平滑的宏观基线可能覆盖不了尾部传导／危机转折；未来宏观判断应分别写基准情景、尾部风险、触发条件和数据 vintage。该案没有单独证伪任何普及闸。

## 4. B-WEBVAN · Webvan 2000 年财务 projection

### 身份与时间

- **预测主体：** Goldman Sachs 代表在投资者电话会议中的 projection，由 Webvan 的 S-1 在结果前披露；本案使用的是披露文本，不把它扩写成 Goldman Sachs 的完整概率预测。
- **预测材料：** Webvan S-1，filed 1999-12-10；原件：<https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt>；仓库中的来源定位、页码、行号和 SHA-256 见 [`business-forecast-calibration-2026-09.md`](business-forecast-calibration-2026-09.md) 第 8–21 行。
- **预测日期／信息点：** 1999-12-10；目标为 2000 财年。
- **结果材料：** Webvan Group, Inc. 2000 Form 10-K，filed 2001-04-02；原件：<https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt>；来源定位、页码、行号和 SHA-256 见同一证据包第 23–37 行。
- **结果日期／观察窗：** 2000 财年结果在 2001-04-02 文件中披露；预测点至财年结束约 12 个月。

### 指标、分母与摘录

- **预测指标／单位：** 2000 年收入 `$120.0m`，2000 年净亏损 `$154.3m`；货币单位为美元。2001 年数字保留在原件中，但不作为本案观察窗。
- **预测对象／分母：** Webvan 公司 2000 财年收入与净亏损；不是用户数、市场总额或社会采用率。
- **预测摘录：**
  > “The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.”
- **结果指标／单位：** 2000 年 Net Sales `$178.456m`，Net Loss `$453.289m`；原件表格单位是 thousands。
- **结果摘录：**
  > “Net Sales $178,456”
  >
  > “Net Loss $ (453,289)”
  >
  > “Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.”

### 判定与缺口

- **收入规模：** 实际约为预测的 1.49 倍，约高 48.7%。
- **净亏损规模：** 实际约为预测的 2.94 倍，绝对差约 `$298.989m`；主分类为 `scale miss`。
- **可比性：** 本案主指标使用双方均明确列出的 `net loss`；`revenue` 与 `Net Sales` 只作辅助指标，不把术语差异隐藏成完全同名。
- **缺失／未验证：** 预测原件只披露 projection 及其假设，不提供概率分布、基线预测或预先评分规则；不能从单案推出商业预测总体准确率。
- **方法边界：** 收入方向接近不覆盖损失规模错误；商业预测必须分开记录收入、损失、部署节奏和机制假设。该案不单独证伪五道社会扩散闸。

## 5. T-SHUTTLE · 科技方向的未验证候选

### 已定位的预测材料

- **预测主体／材料：** Mathematica, Inc. 为 NASA 编写的 *Economic Analysis of the Space Shuttle System: Executive Summary*（NASA-CR-129570）。
- **预测材料：** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>；标题页日期 1972-01-31；§0.2.2 p. 0-7、Table 0.1 p. 0-8。
- **预测摘录：** “from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year”。
- **预测指标／单位：** 1979–1990 共 12 年的 Space Shuttle flights；点值 514，年均 43 次；材料明确它是 NASA／DoD mission model 的规划／经济分析情景，不是概率预测。

### 结果材料与缺失

- **目前能定位的结果来源：** NASA 历史资源页 <https://www.nasa.gov/history/space-shuttle-history-resources/> 只确认全项目 1981-04-12 至 2011-07-21 共 135 次任务。
- **为什么不能配对：** 135 次是全项目总数，不是 1979–1990（或明确处理 1979–1980 无发射年份后的同窗子集）；该页面没有逐年／逐任务原始表。
- **缺失项：** NASA 逐任务汇编或官方逐年清单、每项任务的日期与定位、预先固定的 1979–1990 分母处理规则。未经这些材料核对的“1981–1990 为 38 次”不计入结果。
- **分类：** `UNKNOWN/UNVERIFIED`；没有结果摘录可合法填写，不能写成“514 对 38”的确定失准，也不计入本轮合格案例。
- **下一步停止条件：** 只有取得同窗官方任务清单并能逐项复核预测窗口内任务数，才可把它升级为 calibration 配对；否则保留缺口，不继续用记忆或二手转述填洞。

## 6. 本轮能支持与不能支持什么

**能支持：**

1. 跨领域记录必须同时保留预测时间、结果观察窗、指标、单位、分母／基期、原件定位、摘录和缺失项。
2. FOMC 案说明宏观中心区间可能漏掉危机转折；Webvan 案说明收入方向接近不等于损失规模校准。
3. 科技案例必须先解决同窗结果和分母，再谈“预测失准”；能力、规划情景、融资门槛、市场估计和概率预测不可混称。

**不能支持：**

- 不能计算本项目或某领域的准确率、Brier 分数、总体命中率。
- 不能把 calibration 改写成相对 holdout；本轮没有冻结候选总体、T 前包、分配盐、同输入基线和一次揭晓。
- 不能据此宣称五道普及闸已验证或某一道已被证伪。
- 不能把现有历史材料转写成新的未来判断；真正样本外证据仍由未来登记判断卡到期后提供。

## 7. 可复核入口与双语一致性

- 方法边界：[历史伪样本外验证协议](../zh/02-historical-validation-protocol.md)。
- 政治材料：[政治校准证据包](politics-calibration.md) 与 `politics-artifacts/P-04/`。
- 商业材料：[商业预测校准证据包](business-forecast-calibration-2026-09.md)。
- 科技缺口：[科技史校准补录](technology-calibration-addendum-2026-10.md)。
- 英文镜像：[Historical Calibration Round 2026-10](historical-calibration-round-2026-10.en.md)。两份文件共用 case_id、分类和结论；英文不是独立计数。

**本轮交付结论：** 2 个可重建的 `CALIBRATION` 配对、1 个明确的科技 `UNKNOWN/UNVERIFIED` 缺口；没有 holdout、未来样本外证据或准确率结论。