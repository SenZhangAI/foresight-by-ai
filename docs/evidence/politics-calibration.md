# 政治预测失准校准：可复核证据包（2026-09）

> **范围：`CALIBRATION`，不是样本外准确率。** 本文件只保存结果发生前已公开的预测与其后同口径结果。它用于检查既有规则在历史案例中的失效边界，不生成未来预测卡，也不能推出通用命中率。
>
> **合格案例数：4。** 每案都给出原始摘录、结果摘录、日期、观察窗、指标／单位、唯一失准分类以及与既有方法规则的关系。链接是稳定来源；页面若改版，定位文字仍可用于核验。另保留 2 个 `unverified` 候选，明确说明缺口，不凑数。

## 计数规则与字段

- 合格案例必须同时有：`T` 前原始预测逐字摘录及稳定定位；`T` 后同口径结果逐字摘录及定位；预测日期、观察窗、指标和单位；且只能使用 `direction`、`timing`、`scale`、`mechanism` 之一作为主分类。
- “预测错误”不是“结果令人意外”的同义词。分类只描述预测与结果在哪一维不一致。
- 本轮把选举民调／模型、公共政策宏观预测和战争后果预测放在同一证据包中，但不把它们合并成一个准确率分母；跨案例比较只用于规则校准。

## 合格案例

### P-01 · 英国脱欧公投：YouGov 临场民调把方向判反

**预测主体与 T 前材料**

- **预测日期：** 2016-06-23；发布时点为投票日、正式结果公布前。
- **观察窗：** 投票日结束至官方计票结果公布。
- **指标与单位：** 英国公投中 `Remain` 与 `Leave` 的有效投票比例（百分比）。
- **原始摘录：** “Remain are on 52% with Leave on 48%.”
- **稳定定位：** YouGov, *On-the-day recontact poll shows YouGov's final figures as Remain 52% and Leave 48%*，结果段落（第二个正文段）；页面日期 2016-06-23。来源：<https://yougov.com/en-gb/articles/15778-yougov-day-poll>。

**后续结果**

- **结果日期：** 2016-06-24（对 2016-06-23 投票的官方公布结果）。
- **结果摘录：** “There were 17,410,742 votes cast for leaving the European Union (51.9%) and 16,141,241 votes cast for remaining in the European Union (48.1%).”
- **稳定定位：** Office for National Statistics, *EU referendum results*，2016-06-24，结果正文段落；来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/elections/electoralregistration/bulletins/eureferendumresults/2016-06-24>。官方政府页面同时明确写为 “their decision to leave the European Union”，见 *The result of the EU Referendum: Ambassador's Statement*，2016-06-24，首个正文段：<https://www.gov.uk/government/news/the-result-of-the-eu-referendum-ambassadors-statement>。

- **唯一分类：** `direction`。预测给出 Remain 第一、Leave 第二；结果为 Leave 第一、Remain 第二。两者比较的是同一投票问题和百分比单位，不把 0.1 个百分点的数值差异另算成 `scale`。
- **对既有方法规则的关系：** **支持“不要把共识或单一模型当作确定性结论”，削弱“临近结果时民意已足够稳定”的隐含假设。** 它不证明所有民调都无效，也不证明方向永远不可判；它显示在竞争接近、临界选民和 turnout 结构未被充分观测时，必须把方向不确定性保留到结果揭晓。

### P-02 · 2017 英国大选：YouGov 对保守党多数政府的判断失准

**预测主体与 T 前材料**

- **预测日期：** 2017-06-06/07（6 月 8 日投票前的 final-call poll）。
- **观察窗：** 2017-06-07 预测发布至 2017-06-08 选举结果；指标是下院是否出现保守党多数政府。
- **指标与单位：** 下院多数政府（定性二元结果；同时记录投票意向百分比）。
- **原始摘录：** “For now, YouGov’s final call for the 2017 election is for a seven point Conservative lead, leading to an increased Conservative majority in the Commons.” 同文给出投票意向：`CON 42%, LAB 35%, LDEM 10%, UKIP 5%`。
- **稳定定位：** YouGov, *Labour won the battles of the election campaign, but the Conservatives still look almost certain to win the war*，结尾主文段及投票意向段：<https://yougov.com/en-gb/articles/18339-final-call-poll-tories-seven-points-and-set-increa>。

**后续结果**

- **结果日期：** 2017-06-08。
- **结果摘录：** “The election resulted in a hung Parliament, with no single party winning an overall majority.” “The Conservative Party … won 317 seats and 42.3% of the vote … The Labour Party … won 262 seats, and 40.0% of the vote.”
- **稳定定位：** House of Commons Library, *General Election 2017: results and analysis*，摘要／开头结果段：<https://commonslibrary.parliament.uk/research-briefings/cbp-7979/>；同一结果的 Electoral Commission 数据报告为 PDF 第 1 页第 1.3 段：<https://www.electoralcommission.org.uk/sites/default/files/pdf_file/UKPGE-2017-electoral-data-report.pdf>。

- **唯一分类：** `direction`。T 前明确预测“increased Conservative majority”；T 后明确为无任何政党多数的悬浮议会（hung Parliament）。投票意向的 42% 与实际 42.3% 接近，但本案判定的是制度结果而非把投票误差另算一次。
- **对既有方法规则的关系：** **支持把选票份额、席位转换和制度结果拆开，并削弱把领先百分点直接外推为多数政府的做法。** 本案也提醒预测必须写清“谁赢”与“能否执政”是两个不同指标。

### P-03 · 美国撤出阿富汗：总统对快速全面接管的判断在观察窗内失准

**预测主体与 T 前材料**

- **预测日期：** 2021-07-08。
- **观察窗：** 2021-07-08 至 2021-08-15；指标为阿富汗塔利班是否在短期内“overrunning everything and owning the whole country”。
- **指标与单位：** 在观察窗内是否发生全国性接管（方向性二元结果；不是伤亡数或控制区百分比）。
- **原始摘录：** “The jury is still out. But the likelihood there's going to be the Taliban overrunning everything and owning the whole country is highly unlikely.”
- **稳定定位：** American Presidency Project, *Remarks on United States Military Operations in Afghanistan and an Exchange With Reporters*，2021-07-08，标题下的 “Taliban/Reconciliation Efforts” 段落。来源：<https://www.presidency.ucsb.edu/documents/remarks-united-states-military-operations-afghanistan-and-exchange-with-reporters>。

**后续结果**

- **结果日期：** 2021-08-15。
- **结果摘录：** Congressional Research Service, *Taliban Establishes Control Over Afghanistan Amid U.S. Withdrawal* 的摘要写明：“On August 15, 2021, Taliban fighters entered Afghanistan's capital, Kabul, effectively reestablishing the group's rule over the country after a nearly two-decade-long insurgency against U.S. and international forces and the former Afghan government.”
- **稳定定位：** CRS 产品 IN11725，摘要首段／PDF 第 1 页：<https://www.congress.gov/crs-product/IN11725>；PDF：<https://www.congress.gov/crs_external_products/IN/PDF/IN11725/IN11725.2.pdf>。

- **唯一分类：** `direction`。预测的可判定内容是“全国性接管高度不可能”；结果是在五周左右发生了全国性接管。原始摘录没有给出一个独立的精确时间承诺，因此不把本案伪装成 `timing` 失准。
- **对既有方法规则的关系：** **支持“必须登记观察窗与领先指标”，并削弱只写长期结构方向而不记录制度脆弱性与转折条件的做法。** 该材料并不能单独确定失败机制是军队凝聚力、政治谈判、撤军执行或情报误判；机制因果应另建证据链，不能从结果摘录倒推。

### P-04 · 美国 2008 年经济增长：FOMC 预测正增长，实际出现收缩

**预测主体与 T 前材料**

- **预测日期：** 2007-10-30/31（FOMC 会议预测）。
- **观察窗：** 2007 年第四季度至 2008 年第四季度。
- **指标与单位：** 美国实际 GDP 同比增长（Q4/Q4，百分比）。
- **原始摘录：** “However, the central tendency of participants’ projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent, notably below the 2-1/2 to 2-3/4 percent central tendency in June.” 表下注释：“Projections of real GDP growth, PCE inflation, and core PCE inflation are fourth-quarter-to-fourth-quarter growth rates, that is, percentage changes from the fourth quarter of the prior year to the fourth quarter of the indicated year.”
- **稳定定位：** Federal Reserve Board, *Summary of Economic Projections, October 30–31, 2007*，正文 “Economic Outlook” 段及 Table 1 “Economic Projections of Federal Reserve Governors and Reserve Bank Presidents”，2008 Real GDP Growth / Central Tendencies 1.8–2.5：<https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>。

**后续结果**

- **结果日期：** 2009-03-27（BEA 对 2008 Q4 的最终估计）。
- **结果摘录：** “During 2008 (that is, measured from the fourth quarter of 2007 to the fourth quarter 2008), real GDP decreased 0.8 percent.”
- **稳定定位：** Bureau of Economic Analysis, *Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*，页面 “2008 GDP” 小节、以 “During 2008 (that is…” 开头的段落：<https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>。该段明确这是 Q4 2007 到 Q4 2008 的变化，不是年度平均增长。

- **唯一分类：** `direction`。FOMC 对 Q4/Q4 实际 GDP 给出正增长区间（1.8–2.5%），最终 BEA 同口径结果为 −0.8%。
- **对既有方法规则的关系：** **支持“预测与结果必须固定指标、观察窗和单位”，并证伪把金融传导风险压缩成平滑的单一基线增长区间。** 该案例仍不能推出普遍准确率，但清楚显示尾部传导和相关性断裂会使机构基线方向翻转。
### P-05 · 英国脱欧经济冲击：官方宏观预测的规模与实际短期结果不匹配（`unverified`）

**预测主体与 T 前材料**

- **预测日期：** 2016-05-23（公投前）。
- **观察窗：** 公投后两年，预测基准为“投票留欧”情景。
- **指标与单位：** 英国实际 GDP 水平相对留欧基准的差异（百分比）；同时报告失业人数和英镑价值，但本案只判 GDP 主指标。
- **原始摘录：** “The central conclusion of the analysis is that the effect of this profound shock would be to push the UK into recession and lead to a sharp rise in unemployment.” 报告的 “shock” 情景进一步写明：“GDP would be around 3.6% lower in the shock scenario compared with a vote to remain.”
- **稳定定位：** HM Treasury, *HM Treasury analysis: the immediate economic impact of leaving the EU*，2016-05-23，Executive Summary，PDF 约第 5–6 页（以 PDF 印刷页码为准）；来源：<https://www.gov.uk/government/publications/hm-treasury-analysis-the-immediate-economic-impact-of-leaving-the-eu>；PDF：<https://assets.publishing.service.gov.uk/media/5a80772140f0b62305b8b510/hm_treasury_analysis_the_immediate_economic_impact_of_leaving_the_eu_web.pdf>。

**后续结果**

- **结果日期／观察点：** 2018-10-31 发布的 ONS 2018 年度国民账户，覆盖 2016–2017 年；2017 是公投后第一个完整年度。
- **结果摘录：** “The UK economy grew by 1.7% in 2017 in volume terms, which followed growth of 1.8% in 2016.” 同一节进一步写道：“While the UK economy did slow in 2017, the 1.7% growth recorded was not as weak as many had forecasted.”
- **稳定定位：** Office for National Statistics, *UK National Accounts, The Blue Book: 2018 edition*, “National accounts at a glance”，开头 GDP 段落及 “GDP after the EU referendum” 段落；发布日期 2018-10-31：<https://www.ons.gov.uk/economy/grossdomesticproductgdp/compendium/unitedkingdomnationalaccountsthebluebook/2018/nationalaccountsataglance>。

- **唯一分类：** `direction`。预测的主判定是“push the UK into recession”；同一 GDP 指标在后续官方序列中仍为正增长（2017 年 1.7%），不是衰退。Treasury 的 −3.6% 是相对留欧反事实的量级预测，但本案不把它与实际增长率混成同口径 `scale` 误差。
- **对既有方法规则的关系：** **支持“预测必须预先定义指标、基准与观察窗”，并削弱把市场冲击、衰退和 GDP 反事实差值写成一个不可拆分判断的做法。** 本案不能推出“脱欧没有长期成本”；它只校准“公投后两年内进入衰退”这一可判定方向命题。

### P-06 · 伊拉克大规模杀伤性武器：战前评估与战后发现（`unverified`）

- **保留理由：** 这是一个有明确战前文本入口、但当前运行环境无法把 PDF 原件及战后同口径原件稳定落入仓库的候选；不计入合格案例。
- **可检索的战前摘录：** 2002 年美国情报社区公开材料 *Iraq's Weapons of Mass Destruction Programs* 的摘要写道：“Iraq has stockpiles of CW and BW agents and munitions, is rebuilding its dual-use production facilities, and is aggressively pursuing delivery platforms—including UAVs—for chemical and biological agents.”
- **来源与缺口：** National Security Archive 的原始 PDF 入口：<https://nsarchive2.gwu.edu/NSAEBB/NSAEBB254/doc02.pdf>。当前环境能确认该原件的标题与搜索摘录，但不能可靠抽取 PDF 页码／段落并把文件作为仓库内证据附件保存。
- **预期结果入口：** Iraq Survey Group / Duelfer Report，2004，官方 CIA Reading Room 与可访问 HTML 镜像均存在入口，但本轮不能从稳定可读页面取得战后“无库存”原文及页码。仅有新闻二手转述不得计入。
- **分类：** `unverified`；不能在缺失同口径战后原文时擅自选择 `direction` 或 `mechanism`。
- **方法关系：** 候选提示“能力／意图／库存／可部署性”必须拆成不同指标；但在证据包补齐前，不支持或证伪任何规则。


- 合格案例：**4**（P-01 英国脱欧民调、P-02 2017 英国大选、P-03 阿富汗、P-04 美国 GDP）。
- `unverified`：**2**（P-05 脱欧宏观反事实 GDP；P-06 伊拉克 WMD；两案均缺当前包内可独立重建的同口径结果原件）。
- 因此，本文件达到四个合格案例要求，同时诚实保留两个未验证候选；未验证材料不进入合格计数，也不用于推出通用命中率。

## 停止条件与证据边界

只有在补齐下列材料后，P-05 或 P-06 才能从 `unverified` 改为合格案例：

1. P-05 的留欧反事实 GDP 序列、发布时间和表格定位；
2. P-05 明确的留欧反事实基准与同一单位；
3. P-05 可由 fresh-context 读者从来源重建相对差值；
4. P-06 战前 PDF 的页码／段落和战后同口径库存结果原件；
5. P-06 对能力、意图、库存和可部署性指标的预先拆分。

这是 `CALIBRATION`，不是样本外准确率。即使未来补足四个案例，也只能用于检查、削弱或修订既有规则，不能由本文件推出通用命中率。真正的样本外证据仍只能来自事前登记、未来揭晓的判断卡。
