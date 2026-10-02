# 历史证据补录：FOMC 对 2008 年实际 GDP 的预测

> **证据等级：`CALIBRATION`，不是相对 `holdout`，也不是未来样本外证据。** 本案是在结果已经发生且可见之后，从仓库已有政治校准包中选取的配对。它可以作为方法边界的可复核历史材料，但不能证明本项目的相对判别力或未来准确率提高。

## 1. 案例身份与选择时点

- **case_id：** `P-04`
- **领域：** 宏观经济／公共政策
- **预测主体：** Federal Reserve Board，FOMC participants
- **预测材料：** *Summary of Economic Projections, October 30–31, 2007*
- **预测材料仓库副本：** [`prediction.html`](politics-artifacts/P-04/prediction.html)；原始响应状态 `HTTP 200`；SHA-256：`cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`
- **预测来源：** <https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>
- **预测日期／时间点：** 2007-10-30/31（会议日期与信息截止点）。副本没有独立的发布日期，不能把 2007-10-31 伪写成已核实的发布日期。
- **结果材料：** Bureau of Economic Analysis，*Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*
- **结果材料仓库副本：** [`outcome.html`](politics-artifacts/P-04/outcome.html)；页面标为 2009-03-26 08:30 EST 发布；原始响应状态 `HTTP 200`；SHA-256：`25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`
- **结果来源：** <https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>
- **结果日期／观察结束：** 2009-03-26 的最终估值发布；目标观测期为 2008 年 Q4/Q4 实际 GDP 增长。
- **本补录的选择时点：** 2026-10-02。选择晚于结果，故分类只能是 `CALIBRATION`。

## 2. 预测与结果的同口径配对

### 预测

仓库副本的可定位摘录为：

> “central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent”

- **forecast_metric：** 美国实际 GDP 增长率，2008 Q4/Q4。
- **forecast_value：** 1.8%–2.5%（参与者预测的 central tendency 区间）。
- **unit：** percent growth rate。
- **population/base：** 美国实际 GDP；基期为 2007 Q4，目标期为 2008 Q4。
- **阈值／比较规则：** 预测区间全部大于 0；若结果小于 0，则方向判断为未命中。
- **原件定位：** `prediction.html` 字节区间 `[8275,8558)`；摘录 SHA-256：`d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`。

### 结果

仓库副本的可定位摘录为：

> “During 2008 ... real GDP decreased 0.8 percent.”

- **outcome_metric：** 美国实际 GDP 增长率，2008 Q4/Q4。
- **outcome_value：** −0.8%。
- **unit：** percent growth rate。
- **population/base：** 美国实际 GDP；与预测相同，比较 2007 Q4 至 2008 Q4。
- **原件定位：** `outcome.html` 字节区间 `[33844,34200)`；摘录 SHA-256：`484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`。

**可比性结论：** 预测脚注和结果原件均采用 Q4/Q4 实际 GDP 增长口径；本配对不以年度平均增长替换 Q4/Q4，也不把 GDP 总量、名义 GDP 或人均 GDP 当作结果。因而可以判定为同一指标的方向与区间比较。这里的“分母”不是人口，而是增长率定义中的 2007 Q4 实际 GDP 基期；预测材料没有提供可用于重建每位参与者概率或加权平均的完整分布，因此这些字段保持未知。

## 3. 判定

- **方向：** 预测给出正增长区间（+1.8% 至 +2.5%），结果为 −0.8%；方向相反，记为 `direction miss`。
- **区间误差：** 结果比预测区间下沿低 2.6 个百分点，比上沿低 3.3 个百分点。该数值只描述本案，不能转换为总体准确率。
- **时间：** 预测点在 2007-10-30/31；目标期为 2008 Q4/Q4；结果材料发布于 2009-03-26。预测先于目标结果，时间顺序成立。
- **观察窗口：** 2008 Q4/Q4；结果材料是 final release，但不能据此声称所有历史数据修订已经被穷尽。
- **缺失／未验证：** `unknown/unverified`：完整参与者级预测分布、预测概率、预测时的实时 GDP 数据 vintage、事后修订路径、同一时点其他基线预测的完整输入与预先指定的比较规则。没有这些字段，不能计算 Brier、对数评分、相对判别增量或跨案例命中率。

## 4. 它能支持什么，不能支持什么

**能支持：** 这是一个原件可定位、时间顺序清楚、预测与结果口径可比的历史失准案例。它具体攻击“平滑的宏观基线足以覆盖尾部传导／危机转折”的乐观假设：正增长区间并没有覆盖 2008 年的负增长结果。今后的宏观判断应单独记录基准情景、尾部风险、触发条件与数据 vintage，而不能只记录一个中心区间。

**不能支持：** 本案是结果已知后选入的单案 `CALIBRATION`。它不是冻结总体后分配到的相对 `holdout`，没有同输入基线，也没有预先封存的评分规则与批次分母；因此不能推出“方法准确率提高”“宏观预测总体不可靠”或“某一道普及闸已被证伪”。它也没有新增未来趋势判断。

## 5. 与历史验证协议的关系

本记录遵守[历史伪样本外验证协议](../zh/02-historical-validation-protocol.md)所要求的边界：结果已知后选入的案例只能用于 `CALIBRATION`，不能冒充 holdout。要升级为相对 holdout，必须另行从未揭晓的可枚举候选总体冻结 T 前材料、分层与分配、同输入基线、评分规则和结果揭晓顺序；本补录没有执行这些步骤。

**本轮结论：** 新增的是一条可重建的校准记录与一个方法边界，不是预测准确率结论。未来样本外证据仍需等待预登记判断卡在时间窗到期后复核。
