# 商业预测失准校准：可复核证据包（2026-09）

> **用途**：本文件是 `docs/zh/01-retrospect.md` 第二轮历史校准的证据包。以下只使用随仓库交付的逐字摘录与稳定来源定位；它们是 `CALIBRATION`，不是样本外预测准确率，也不进入 holdout。
>
> **证据规则**：预测必须发生在目标结果之前；结果必须使用同一指标或明确说明不可比；二手转述不能替代原始申报。SEC 全文原件的 SHA-256 写在每个来源下，便于读者重新下载后核对。

## 案例 A · Webvan：收入方向接近，但亏损规模严重失准

### T 前预测原件

- **预测主体／来源**：Goldman Sachs 代表在面向投资者的电话会议中给出的 projection；Webvan 的 S-1 在 T 前披露该原话并记录其来源与限制。
- **预测／披露日期**：1999-12-10（S-1 filed）；预测段落所在小节为 `OUR LIMITED OPERATING HISTORY MAKES FINANCIAL FORECASTING DIFFICULT FOR US AND FOR FINANCIAL ANALYSTS THAT MAY PUBLISH ESTIMATES OF OUR FINANCIAL RESULTS`，并在其后以 `The article also referred to...` 段落披露 Goldman Sachs 代表的数字。
- **稳定来源**：[SEC full submission 0000891618-99-004914](https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt)
- **原件定位**：SEC 文本印刷页 13（`<PAGE> 13`），上述 `Risk Factors` 段落及其 `The article also referred to...` 段落，原文件行 820–929；SHA-256 `05b7375d74ddd6835230d15a6e625206b93ce78a4457fa6d28d54ceafcb55ece`。

**逐字摘录（保留原文措辞与数字）**：

> “The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.”
>
> “These projections are based upon a number of estimates and assumptions and are inherently subject to significant uncertainties and contingencies, including the timing and cost of our distribution center roll-out, the volume and size of customer orders, market penetration and competition.”

**冻结的 T 前指标**：2000 年收入 `$120.0m`；2000 年净亏损 `$154.3m`；2001 年收入 `$518.2m`；2001 年净亏损 `$302m`。本案把 2000 年作为同口径结果观察窗，预测至年末约 12 个月。

### 结果原件

- **结果来源**：Webvan Group, Inc. 2000 Form 10-K filed 2001-04-02。
- **稳定来源**：[SEC full submission 0001012870-01-001485](https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt)
- **原件定位**：SEC 文本印刷页 12，`ITEM 6. SELECTED CONSOLIDATED FINANCIAL DATA` 下的 `Consolidated Statements of Operations Data` 表（`Net Sales`／`Net Loss` 行），原文件行 830–863；SHA-256 `1fa9948622c6eeb5a8b15ce05ad98b0fe0b7060afae75ec17a8de4d430909e28`。

**逐字摘录**：

> “Net Sales                                                            $    178,456    $     13,305   $         -”
>
> “Net Loss                                                             $   (453,289)   $   (144,569)  $   (12,004)”
>
> “Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.”

表格单位是 `(In thousands, except share and per share data)`，因此 2000 实际净销售额为 `$178.456m`，实际净亏损为 `$453.289m`。

### 判定与分类

- **主要同口径指标**：本案以 `net loss` 为主指标（预测与结果均逐字使用该名称）；`revenue`／`Net Sales` 只作为辅助指标，因术语不同不承担核心失准判定。
- **收入规模**：预测 `$120.0m`，实际 `$178.456m`；实际为预测的约 1.49 倍，偏差约 +48.7%。这是可量化的规模误差，但不是“需求方向完全相反”。
- **亏损规模**：预测净亏损 `$154.3m`，实际 `$453.289m`；实际亏损约为预测的 2.94 倍，绝对差约 `$298.989m`。这是 `scale` 失准，且方向为低估损失。
- **机制／时点**：预测原件自己列出的 rollout timing、订单量、市场渗透和竞争假设，正是需要在预测时显式拆开的变量；结果不能仅归因于“技术不行”。本案不声称这些变量中哪一个单独造成偏差。
- **独立性**：该案是电子商务基础设施与组织扩张的商业预测；与既有 Forrester 美国线上零售总额系列不是同一预测主体、指标或来源。

### 规则影响

本案**不推翻五道普及闸中的任何一道**：它检验的是一家公司财务 projection 的数值校准，而不是某项能力能否成为社会风气。它反而给方法增加一个边界：商业预测必须把“收入规模”“损失规模”“部署节奏”和“机制假设”分开记账；不能因为收入方向正确，就把成本结构和利润结果一并写成命中。

## 案例 B · eToys：同一季度的销售预测在两个月内大幅下修，实际仍低于下修后的上沿

### T 前预测原件

- **预测主体／来源**：eToys 公司在 Form 8-K 的 Exhibit 99.1 新闻稿中披露其对当季经营结果的明确 forward estimate；这是公司自己的预测，不是融资契约或二手转述。
- **预测／披露日期**：2000-12-15；观察目标为截至 2000-12-31 的 fiscal third quarter。该文件是本案实际冻结的 T 前预测原件；它同时提到 10 月 30 日的旧区间，但本案不把未交付的 10 月 30 日文件或旧区间计入误差计算。
- **稳定来源**：[SEC full submission 0000912057-00-053869](https://www.sec.gov/Archives/edgar/data/1052245/000091205700053869/a2033537zex-99_1.txt)
- **原件定位**：Exhibit 99.1 印刷页 1，标题 `ETOYS EXPECTS LOWER THAN ESTIMATED FISCAL THIRD QUARTER OPERATING RESULTS` 下的 `Specifically, the company's new estimates...` 段落，原文件行 14–47；SHA-256 `71d6a22b0921fb49b23496abe3ece877c6a443aeaa5efc8bed7030f808ba8a87`。

**逐字摘录**：

> “LOS ANGELES, December 15, 2000 -- As a result of weaker-than-expected holiday sales, eToys Inc. (NASDAQ: ETYS) today announced that it expects to report operating results for its fiscal third quarter ending December 31 that are lower than the estimates the company provided on October 30 of this year.”
>
> “Net sales are expected to be between $120 million and $130 million, rather than the $210 million to $240 million previously estimated.”
>
> “Operating losses are expected to be between 55 percent and 65 percent of revenue, rather than the 22 percent to 28 percent of revenue previously estimated...”

**冻结的 T 前指标**：2000 Q3（季度截至 12 月 31 日）收入区间 `$120m–$130m`，经营亏损率区间 `55%–65%`。`$210m–$240m` 与 `22%–28%` 只作为 12 月 15 日文件中的历史引用，不作为本案可计量预测原件；本案的 interval-miss 规则是：实际值落在 T 前发布区间之外即记为 `scale` miss，再单独记录偏离幅度。本案主要观察窗为 12 月 15 日到 12 月 31 日的 16 天。

### 结果原件

- **结果来源**：eToys Inc.，2000 Q3 Form 10-Q，filed 2001-02-14，结果为截至 2000-12-31 的同一季度。
- **稳定来源**：[SEC full submission 0000912057-01-005726](https://www.sec.gov/Archives/edgar/data/1052245/000091205701005726/a2034712z10-q.txt)
- **原件定位**：印刷页 3，`ITEM 1. CONSOLIDATED FINANCIAL STATEMENTS` 下的 `CONSOLIDATED STATEMENTS OF OPERATIONS` 表，原文件行 130–180；另有 `NET SALES` 小节对原始估计与实际结果的明确说明，原文件行 973–1006；SHA-256 `17e484b5e00d06ebeaee13f5303e5a21c58173a000973fd9dc6e0a832cab06f3`。

**逐字摘录**：

> “Net sales.......................................    $131,166     $ 106,751     $ 182,004     $ 128,032”
>
> “(IN THOUSANDS, EXCEPT PER SHARE AMOUNTS)”
>
> “It should be noted that net sales for the quarter ended December 31, 2000 were substantially below our original estimate of $210 million to $240 million, due to a harsh retail climate and dampened enthusiasm for Internet retailing.”
>
> “...in fact net sales for the quarter were only $131.2 million due to a harsh retail climate and dampened enthusiasm for Internet retailing.”

表格列为 quarter ended December 31, 2000 / 1999 与 nine months ended；因此同口径实际季度净销售额为 `$131.166m`。

### 判定与分类

- **收入规模**：相对于 12 月 15 日冻结的 `$120m–$130m` 区间，实际 `$131.166m` 高出上沿 `$1.166m`（约 +0.9%），因此按预先写明的 interval-miss 规则记为边界性的 `scale` miss。10 月 30 日旧区间只作为未计入的背景引用，不能用来扩大本案误差。
- **方向／时点**：同一季度内公司在结果揭晓前承认旧估计失效；就本案冻结的 12 月 15 日版本而言，实际结果在 16 天后略越过区间上沿，这是 `timing + scale` 的 forecast revision 案例。
- **机制**：原件把短缺归因于 harsh retail climate、对 Internet retailing 的兴趣下降和总统选举后的注意力分散；证据支持这些是公司披露的解释，不足以证明唯一因果。
- **独立性**：eToys 是在线玩具零售商自己的季度财务预测，与 Webvan 的 Goldman Sachs 预测不同主体、不同业务公司、不同披露文件；失准机制也不同：Webvan 的核心边界是配送中心 rollout 与固定成本／亏损规模，eToys 的核心边界是节日需求短缺与预测区间修订。两者也都不是 Forrester 美国线上零售总额系列。

### 规则影响

本案不推翻五道普及闸，但明确补强一条记录规则：**同一指标若在结果前发生预测修订，必须冻结每一版的日期与区间，并按版本分别计算误差；若预测以区间给出，区间覆盖与偏离幅度分开记**。

本案的 `unverified` 项是 2000-10-30 的旧 `$210m–$240m` 原始公告：12 月 15 日文件只对它作了引用，本证据包没有把它计入案例指标；因此本案不声称旧版本的精确误差，只检验已交付的 12 月 15 日区间。


## 附录 · Iridium：商业融资契约门槛失准（不计入两例 forecast miss）

### T 前原件（商业目标，不是普通概率性预测）

- **来源**：Iridium World Communications Ltd.，本案唯一采用的 T 前原件是其 `424B4` prospectus，filed 1999-01-25；该来源不是 Forrester 系列，披露其 secured bank facility 在未来日期要求达到的最低收入和订户水平。这是可在结果发生前读取的、带具体日期和数值的融资契约目标；本案将其作为可检验的商业目标门槛，不把它冒充成普通概率性预测。
- **稳定来源**：[SEC full submission 000095013399000162](https://www.sec.gov/Archives/edgar/data/948421/000095013399000162/0000950133-99-000162.txt)
- **原件定位**：SEC 文本第 17–18 页（`<PAGE> 17`–`<PAGE> 18`），`IRIDIUM MAY BE UNABLE TO SATISFY OR MAY BE ADVERSELY CONSTRAINED BY THE COVENANTS IN ITS BANK FACILITIES AND DEBT SECURITIES` 风险因素／契约段落，原文件行 1258–1272；SHA-256 `762d4dac8b26a55cddf805c3e135df51b3173ad956ac72576f1ec33e02956109`。

**逐字摘录**：

> “IRIDIUM MAY BE UNABLE TO SATISFY OR MAY BE ADVERSELY CONSTRAINED BY THE COVENANTS IN ITS BANK FACILITIES AND DEBT SECURITIES”
>
> “at March 31, 1999 it have cumulative cash revenues of at least $4 million, cumulative accrued revenues of at least $30 million, at least 27,000 Iridium World Satellite Service subscribers and at least 52,000 total subscribers;”
>
> “at June 30, 1999 it have cumulative cash revenues of at least $50 million, cumulative accrued revenues of at least $150 million, at least 88,000 Iridium World Satellite Service subscribers and at least 213,000 total subscribers; and”
>
> “at September 30, 1999 it have cumulative cash revenues of at least $220 million, cumulative accrued revenues of at least $470 million, at least 173,000 Iridium World Satellite Service subscribers and at least 454,000 total subscribers.”

**冻结的 T 前指标**：截至 1999-03-31 的累计现金收入 `$4m`、累计应计收入 `$30m`、Iridium World Satellite Service 订户 `27,000`、总订户 `52,000`。

### 结果原件

- **结果来源**：Iridium LLC，1999 Q1 Form 10-Q filed 1999-05-17；结果截至 1999-03-31，仍在上述目标期限内，且文件明确解释了 waiver。
- **稳定来源**：[SEC full submission 000095013399001884](https://www.sec.gov/Archives/edgar/data/948421/000095013399001884/0000950133-99-001884.txt)
- **原件定位**：SEC 文本第 24 页（`<PAGE> 24`），小节标题 `Iridium Expects that it Will Not Satisfy the Secured Bank Facility Revenue and Subscriber Covenants`，原文件行 1729–1760；SHA-256 `ce3e246e41856e395be0c36ed39419a6e566fc02eacb14c5153811c15fd0b8c8`。

**逐字摘录**：

> “As a result of various factors, Iridium's subscriber levels and revenues have been significantly below its prior estimates.”
>
> “As of March 31, 1999, Iridium had $195,000 of cumulative cash revenues, $1.637 million of cumulative accrued revenues, 7,188 Iridium World Satellite Service subscribers and 10,294 total subscribers.”
>
> “Iridium now expects that it will not satisfy the secured bank facility's May 31, 1999 (extended from March 31, 1999) minimum subscriber and revenue covenants and also expects that it will not be able to satisfy the June 30, 1999 and September 30, 1999 covenants.”

### 判定与分类

- **现金收入**：`$0.195m / $4m = 4.875%`；达到目标的约 4.9%。
- **累计应计收入**：`$1.637m / $30m ≈ 5.46%`；达到目标的约 5.5%。
- **服务订户**：`7,188 / 27,000 ≈ 26.6%`。
- **总订户**：`10,294 / 52,000 ≈ 19.8%`。
- **分类**：`scale`（收入与订户目标相对实际结果严重高估）+ `timing`（首个约束日期即未达标）+ `mechanism`（商业 rollout、设备分销、服务商和营销协调未按先前估计形成；本案只引用文件明确写出的“below prior estimates”，不把后续解释扩写成单因果）。

### 规则影响

本案同样**不推翻五道普及闸**。它不能单独判定卫星电话被闸一、闸三或闸四中的哪一道挡住，因为该目标同时受商业融资契约、设备供应、服务商和市场采用影响。它暴露的是另一条方法边界：**预测必须记录“目标／契约门槛”与“概率性预测”的来源性质**；两者都可以检验，但不能混称为同一种预测证据。它也提醒我们，技术系统完整可用不等于商业采用曲线会按资本计划到达。

## 交叉结论：本轮改什么、不改什么

1. **改写证据要求，不改五闸结论**：商业预测必须同时记录指标、单位、目标日期、预测主体、预测版本、T 前披露位置和结果原件；收入方向正确不覆盖亏损规模错误，预测下修也不能抹掉上一版。
2. **不把 Webvan 与 eToys 当 holdout**：两案都是看到历史结局后选入本轮的 `CALIBRATION`，不能声称方法准确率提高。
3. **不把“商业预测失准”偷换成“社会扩散规则被证伪”**：Webvan 与 eToys 没有隔离出五闸中某一闸的独占失败机制；诚实结论是增加边界与记录纪律，暂不修改闸一至闸五。
4. **Iridium 不计入两例 forecast miss**：它是融资契约最低门槛，保留为“商业目标门槛未达”的附录与 `unverified-as-forecast` 边界，不用来凑足预测案例数量。
5. **后续可检验方向**：从 SEC 初始 S-1／F-1／8-K 总体中预先冻结普通案例，分别编码 revenue、loss、subscriber／customer、deployment milestone 与 forecast revision；在看结果前固定误差阈值，才能进入历史伪样本外协议，而不是继续挑选名人失败故事。
