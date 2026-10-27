# 历史预测—结果候选可行性清单（2026-10）

[English version](historical-candidate-feasibility-2026-10.en.md)

> **范围与结论。** 本页承接历史先行方向，审计下一批跨科技、政治与商业的历史预测—结果候选。它是候选可行性清单，不是回测、不是 holdout，也不是方法有效性证明。所有候选都是结果已知后发现；即使日后补齐，也最多进入 `CALIBRATION`，不能进入 `CONTAMINATED_RELATIVE_HOLDOUT` 或 `GENUINE_FUTURE_OOS`。
>
> **本批结论：** 宽搜得到 24 个疑似候选；逐案反证后，没有新增案例满足“独立重建所需字段”而可冻结为合格候选。22 个保留为 `UNKNOWN/UNVERIFIED` 储备项，2 个因不属于本批可评分的 forecast 单元而排除（`T-APOLLO-1961` 是政策承诺而非概率 forecast；`B-WEWORK-RUNRATE-2019` 是没有未来目标日期的状态指标）。没有新增 `CALIBRATION`，也不声称预测准确率、`GENUINE_FUTURE_OOS` 或方法已验证。

## 1. 记录协议与字段

每个候选都分开记录：

- 事前材料及其日期／信息截止点 `T`；
- 判定时点或目标日期；
- 观察窗口；
- 结果指标、单位与分母；
- 预测原件与结果原件的稳定来源定位；
- 是否可以由第三方独立重建；
- 缺项与证据等级。

本批沿用[历史伪样本外验证协议](../zh/02-historical-validation-protocol.md) §0–§2：预测对象、结果对象、指标、单位、分母、观察窗或原始定位任一项无法闭合，就不能进入冻结候选池，必须保留 `UNKNOWN/UNVERIFIED` 或明确排除。结果已知后收集的材料不能被重命名为 holdout。

### 证据等级

| 等级 | 本页含义 |
|---|---|
| `UNKNOWN/UNVERIFIED` | 宽搜找到预测线索和／或结果线索，但至少一项承重字段仍无法独立重建；不计入合格 calibration。 |
| `EXCLUDED` | kill pass 证明该项不是本批可评分的 forecast 单元：它是政策承诺而非概率 forecast，或是没有未来目标日期的状态指标。 |
| `CALIBRATION` | 本批没有新增。只有结果已知后仍能以同口径原件重建的候选，未来才可按此标签登记；不能升级为样本外证据。 |

## 2. 候选总表

### 按领域快速索引

- **科技／科技治理（8）**：`Y2K-FEDERAL-COST-1999`、`CONCORDE-BA-PROFIT-1974`、`T-HGP-1990`、`T-APOLLO-1961`、`T-EV-EVERYWHERE-2012`、`T-UGV-2000`、`T-BROADBAND-2010`、`T-MOORE-1965`
- **政治／公共政策（6）**：`P-2015-UK-GE`、`P-2014-SCOTLAND`、`P-2012-US-ELECTION`、`P-YUGOSLAVIA-1990`、`P-ACA-COVERAGE-2010`、`P-OMB-FY2001`
- **商业／金融市场（10）**：`DOW-36000-1999`、`B-NETFLIX-2011-Q3`、`B-TESLA-2016-BUILD`、`B-TESLA-2016-DELIVERIES`、`B-PELOTON-SUBSCRIPTIONS-FY2022`、`B-PELOTON-REVENUE-FY2022`、`B-MOVIEPASS-2018`、`B-BEYONDMEAT-2019`、`B-WEWORK-RUNRATE-2019`、`B-QUIBI-FIRST-YEAR`

总表与 §3 kill pass 使用完全相同的 `case_id`；阅读单案时可用 `case_id` 搜索两处，避免把不同指标或不同证据级别拼成一个案例。

| case_id | 领域 | 一线预测／结果主张 | T 与目标／观察窗 | 指标与分母 | 原始来源定位 | kill pass 后状态 | 关键缺项或排除理由 |
|---|---|---|---|---|---|---|---|
| `Y2K-FEDERAL-COST-1999` | 科技治理／公共部门 | GAO 1999 报告给出 24 个联邦机构 Y2K 累计成本估计约 $7.5bn；最终成本／故障结果尚未同口径闭合 | T：1999-04-28；目标／观察窗需以最终成本或故障指标另定 | 预防成本、实际支出与故障数不能互换；分母为 24 个机构 | [GAO AIMD-99-154](https://www.govinfo.gov/content/pkg/GAOREPORTS-AIMD-99-154/html/GAOREPORTS-AIMD-99-154.htm)；结果材料见[跨域扩展](cross-domain-forecast-outcome-expansion-2026-10-26.md) | `UNKNOWN/UNVERIFIED` | 报告明确多数仍是估计；缺 24 机构最终实际支出／义务和统一观察窗，不能用“没有灾难”替代成本结果 |
| `DOW-36000-1999` | 商业／金融市场 | Glassman/Hassett 书名提出 DJIA 36,000 点，但目标年份和条件未恢复 | T：1999 原版／2000 版本；目标日期未知；观察窗未冻结 | DJIA 每日收盘点位；不能换成总回报、股息或通胀调整财富 | [Internet Archive](https://archive.org/details/dow36000newstrat00jame)；[FRED DJIA](https://fred.stlouisfed.org/series/DJIA/) | `UNKNOWN/UNVERIFIED` | 书名不是完整预测原件；缺正文时间条件、目标定义和结果规则，不能事后挑高点判定 |
| `CONCORDE-BA-PROFIT-1974` | 科技商业化／大型工程 | 1974 Hansard 确认当时存在 Concorde 运营亏损／盈利影响 forecast，但没有数值预测 | T：1974-04-03 议事录；目标财年／观察窗未知 | 年度／累计盈利或亏损；金额、财年、客流分母均缺 | [House of Lords Hansard](https://api.parliament.uk/historic-hansard/lords/1974/apr/03/concorde-project-and-loss-forecasts)；结果线索见[跨域扩展](cross-domain-forecast-outcome-expansion-2026-10-26.md) | `UNKNOWN/UNVERIFIED` | 缺原始数值、同口径财报和观察窗；不能因后来停飞就判商业预测失败 |
| `T-HGP-1990` | 科技 | HGP 计划约 2005 年完成；后来 2003 年宣布完成 | T：1990 计划；目标约 2005（另有 1998 修订为 2003）；观察至 2003 | 参考序列完成；约 30 亿碱基；质量／覆盖阈值未定 | 计划：[First Five-Year Plan](https://www.genome.gov/sites/default/files/media/files/2021-02/1990_First_Five_Year_Plan.pdf)；结果：[DOE timeline](https://doe-humangenomeproject.ornl.gov/human-genome-project-timeline/)、[NIH overview](https://www.genome.gov/human-genome-project) | `UNKNOWN/UNVERIFIED` | 1990 原计划的最终验收日期、覆盖／质量阈值及与 2003 结果的同口径映射未闭合；1998 修订不能替代 1990 版本 |
| `T-APOLLO-1961` | 科技 | Kennedy 要求在 1960 年代结束前载人登月并安全返回；Apollo 11 在 1969 完成 | T：1961-05-25；目标：1969-12-31 前；观察至 1969-07-24 | 是否登月、是否安全返回；“安全”无预先量化阈值 | 预测：[Kennedy speech](https://www.presidency.ucsb.edu/documents/special-message-the-congress-urgent-national-needs)；结果：[NASA Apollo 11](https://www.nasa.gov/mission/apollo-11/) | `EXCLUDED` | 它是国家政策目标／承诺而非本批要比较的概率 forecast；若未来研究政策目标，应另设“承诺兑现”单元，不把它混入预测方法样本 |
| `T-EV-EVERYWHERE-2012` | 科技 | DOE 目标到 2022 年电池包约 125 美元/kWh；DOE 2022 估算为 139 美元/kWh | T：2012 倡议／2014 blueprint；目标：2022；观察：2022 成本估计 | pack $/kWh；目标与结果均需币值、模型产量和 pack/cell 边界一致 | 预测：[DOE blueprint](https://www.energy.gov/sites/default/files/2014/02/f8/eveverywhere_blueprint.pdf)；结果：[DOE 2022 estimate](https://www.energy.gov/eere/vehicles/articles/fotw-1308-august-14-2023-electric-vehicle-battery-pack-costs-2022-are-87-lower) | `UNKNOWN/UNVERIFIED` | 目标与结果的币值年、估计模型、年产 100,000 假设和实际市场价格边界未闭合；不能直接写成“125 对 139”的失准 |
| `T-UGV-2000` | 科技／政策 | 法律目标到 2015 年三分之一现役地面作战车辆为无人系统；GAO 后来称未实现 | T：约 2000-10-01；目标：2015；观察至 GAO-15-342 | 无人 operational vehicles / 全部 operational ground combat vehicles；分子、分母和 autonomous 定义未定 | 预测：[P.L. 106-398](https://www.govinfo.gov/content/pkg/PLAW-106publ398/pdf/PLAW-106publ398.pdf)；结果：[GAO-15-342](https://www.gao.gov/products/gao-15-342) | `UNKNOWN/UNVERIFIED` | GAO 的精确页码、2015 分子／分母和“无人”边界未恢复；法律中的 `goal` 是否作为可评分预测也未裁定 |
| `T-BROADBAND-2010` | 科技／基础设施 | FCC 目标 2020 年至少 1 亿家庭可负担地获得实际 100/50 Mbps | T：2010-03-16 左右；目标：2020；观察至 2020 报告 | 家庭数、实际速度、可负担性；结果报告主要是 25/3 Mbps 人口覆盖 | 预测：[FCC plan](https://www.fcc.gov/sites/default/files/national-broadband-plan.pdf)；结果：[2020 report](https://www.fcc.gov/reports-research/reports/broadband-progress-reports/2020-broadband-deployment-report) | `UNKNOWN/UNVERIFIED` | 结果侧没有原目标的 1 亿家庭／100/50／可负担性同口径数据；人口与家庭、advertised 与 actual 不能替换 |
| `T-MOORE-1965` | 科技 | Moore 预计 1975 年最低成本集成电路约 65,000 components | T：1965-04-19；目标：1975；观察至 1975 回顾／芯片数据 | minimum-cost complexity；components 与 transistors 的分母定义未闭合 | 预测：[1965 article](https://www.worldradiohistory.com/Archive-Electronics/60s/65/Electronics-1965-04-19.pdf)；结果：[1975 DOI](https://doi.org/10.1109/IEDM.1975.189170)、[Intel history](https://www.intel.com/content/www/us/en/history/museum-gordon-moore-law.html) | `UNKNOWN/UNVERIFIED` | 预测原刊未在本轮核页；“最低成本”类别和 components/transistors 等价性未证；单一 8080 不能替代总体结果 |
| `P-2015-UK-GE` | 政治 | 最终民调把 Conservative/Labour 视为接近持平或略有领先；实际 Conservative 单党多数 | T：2015-05-04–07；目标：2015-05-07；观察至官方结果 | 全国有效票份额／第一名／议席多数必须拆开 | 预测：[YouGov PDF](https://cdn.yougov.com/cumulus_uploads/document/prq13gslk4/FINALCALL_GB_May2015_WedPM_W.pdf)、[Survation PDF](https://survation.com/wp-content/uploads/2015/05/Final-Phone-Poll-2.pdf)、[Populus archive](https://web.archive.org/web/20150514004946/http://www.populus.co.uk/wp-content/uploads/OmOnline_Vote_Final_BPC.pdf)；结果：[Commons Library](https://commonslibrary.parliament.uk/research-briefings/cbp-7186/) | `UNKNOWN/UNVERIFIED` | 官方结果页本轮返回 403，原件未保存；民调分母、是否预测席位和 ICM 数值未闭合，不能把“多数”替换“份额” |
| `P-2014-SCOTLAND` | 政治 | 最终民调显示 No 领先；实际 No 55.3%、Yes 44.7% | T：2014-09-15–18；目标：2014-09-18；观察至官方结果 | Yes/No 有效票比例与方向；undecided 处理需预先冻结 | 预测：[YouGov](https://yougov.co.uk/news/2014/09/18/yougov-referendum-prediction/)、[Survation PDF](https://survation.com/wp-content/uploads/2014/09/24-hour-scottish-referendum-poll.pdf)、[Ipsos archive](https://web.archive.org/web/20140924042744/http://www.ipsos-mori.com/Assets/Docs/Polls/scotland-referendum-18-september-tables.pdf)；结果：Electoral Commission 原件 URL 本轮未恢复 | `UNKNOWN/UNVERIFIED` | 官方结果原件、调查分母与 undecided 规则未闭合；且需与已有 `P-01` 题型重复性分开登记 |
| `P-2012-US-ELECTION` | 政治 | Gallup final poll 给 Romney 50%、Obama 49%；实际 popular vote 由 Obama 获胜 | T：2012-11-01–04；目标：2012-11-06；观察至认证结果 | likely-voter 民调与全国有效票的份额／第一名；不得换成 Electoral College | 预测：[Gallup](http://www.gallup.com/poll/158519/romney-obama-gallup-final-election-survey.aspx)；结果：FEC／National Archives 官方结果（本轮未恢复稳定 URL） | `UNKNOWN/UNVERIFIED` | 官方认证结果原件、Gallup 模式（两党或全体）及分母未闭合 |
| `P-YUGOSLAVIA-1990` | 政治／地缘 | 疑似 CIA NIE 对南斯拉夫稳定／解体作过事前判断 | T：疑似 1990，具体日未知；目标窗与阈值未知 | 联邦持续、共和国独立或国际承认的具体指标未定 | 预测：NIE 15-90 原件本轮未取得；结果线索：[UN members](https://www.un.org/en/members/index.shtml#serbia)、[UNSC Resolution 721](https://www.nato.int/ifor/un/u911127a.htm) | `UNKNOWN/UNVERIFIED` | 核心预测原件、确切主张、目标窗和统一分母均缺；不能写成“CIA 预测失败” |
| `P-ACA-COVERAGE-2010` | 政治／公共政策 | CBO 2010 对 ACA exchange/Medicaid/无保险人数作覆盖预测；CMS 后来发布 enrollment | T：2010-03-18–20；可能目标 2014–16；观察窗需按原表冻结 | exchange、Medicaid、无保险人数不能与 CMS effectuated enrollment 混用 | 预测：[CBO HR 4872](http://www.cbo.gov/ftpdocs/113xx/doc11355/hr4872.pdf)、[CBO update](https://www.cbo.gov/publication/43472)；结果：[CMS 2015 snapshot](https://www.cms.gov/Newsroom/MediaReleaseDatabase/Fact-sheets/2016-Fact-sheets-items/2016-03-11.html) | `UNKNOWN/UNVERIFIED` | CBO 原表数字、目标年、定义与 CMS 同口径结果未恢复；后续 CBO 不能反向替代 T 前预测 |
| `P-OMB-FY2001` | 政治／财政 | FY2001 预算材料疑似预计 receipts 约 2.019 万亿美元；实际 receipts／surplus 较低 | T：2000 预算发布；目标：2001-09-30；观察至财政年度结果 | unified-budget receipts/outlays/surplus；口径与修订版本未定 | 预测：[OMB Budget 2001](https://www.gpo.gov/fdsys/pkg/BUDGET-2001-BUD/pdf/BUDGET-2001-BUD.pdf)；结果：[OMB historical tables](https://www.gpo.gov/fdsys/pkg/BUDGET-2016-TAB/pdf/BUDGET-2016-TAB.pdf) | `UNKNOWN/UNVERIFIED` | 原预算页码、预测表、完整 outlays/surplus 数值及预算口径未闭合 |
| `B-NETFLIX-2011-Q3` | 商业 | Netflix 对 Q3 美国订户作 guidance，调价后下修，季末 unique US subscribers 约 23.79m | T：2011-07-25 初版／2011-09-15 修订；目标：2011-09-30；结果 2011-10-24 | Total Unique US Subscribers；DVD/streaming subscriptions 不可相加 | 预测：[July 8-K](https://www.sec.gov/Archives/edgar/data/1065280/000119312511196126/dex991.htm)、[Sept revision](https://www.sec.gov/Archives/edgar/data/1065280/000119312511248698/d231910dex991.htm)；结果：[Oct 8-K](https://www.sec.gov/Archives/edgar/data/1065280/000119312511278716/d246709dex991.htm) | `UNKNOWN/UNVERIFIED` | guidance 关键数字在图形中未转录；必须按版本冻结，且 unique 与 subscriptions 分母不同 |
| `B-TESLA-2016-BUILD` | 商业／科技商业化 | Tesla 把 500,000 辆总产量 build plan 提前至 2018；2018 production 254,530 | T：2016-05-04；目标：2018-12-31；结果 2019-02-19 | annual total production；不可换成交付、预订或 Model 3 | 预测：[2016 Q1 update](https://www.sec.gov/Archives/edgar/data/1318605/000119312516577582/d158845dex991.htm)；结果：[2018 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459019003165/tsla-10k_20181231.htm) | `UNKNOWN/UNVERIFIED` | “build plan”是计划还是 forecast，以及是否指年产 run-rate 而非全年产量，原文语义需先闭合 |
| `B-TESLA-2016-DELIVERIES` | 商业 | Tesla guidance 2016 年交付 80,000–90,000 辆 Model S/X；年末结果待配对 | T：2016-05-04；目标：2016-12-31；观察至 2017-01-03／10-K | 两车型全球 deliveries；不得换 production | 预测：[2016 Q1 update](https://www.sec.gov/Archives/edgar/data/1318605/000119312516577582/d158845dex991.htm)；结果：[2017 8-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459017000024/tsla-8k_20170103.htm)、[2016 10-K](https://www.sec.gov/Archives/edgar/data/1318605/000156459017003118/tsla-10k_20161231.htm) | `UNKNOWN/UNVERIFIED` | 本轮未转录官方最终交付数字，且未搜集年内所有下修／重申版本 |
| `B-PELOTON-SUBSCRIPTIONS-FY2022` | 商业 | Peloton 预计 FY2022 末订户 3.35–3.45m；年末订户约 2.966m | T：2021-11-04；目标：2022-06-30；结果 2022-08-25 | ending subscriptions；不能与收入指标合并 | 预测：[Q1 letter](https://www.sec.gov/Archives/edgar/data/1639825/000163982521000320/shareholderletter2022q1.htm)；结果：[Q4 letter](https://www.sec.gov/Archives/edgar/data/1639825/000163982522000100/a4q2022shareholderletter.htm) | `UNKNOWN/UNVERIFIED` | “updated” guidance 后还有修订版本，不能择最后版本而不建版本链 |
| `B-PELOTON-REVENUE-FY2022` | 商业 | Peloton 预计 FY2022 全年收入 $4.4–4.8bn；同口径全年结果尚未转录 | T：2021-11-04；目标：2022-06-30；结果 2022-08-25 | FY revenue；不能与 ending subscriptions 合并 | 预测：[Q1 letter](https://www.sec.gov/Archives/edgar/data/1639825/000163982521000320/shareholderletter2022q1.htm)；结果：[Q4 letter](https://www.sec.gov/Archives/edgar/data/1639825/000163982522000100/a4q2022shareholderletter.htm) | `UNKNOWN/UNVERIFIED` | 收入结果未转录，且 guidance 修订链未闭合 |
| `B-MOVIEPASS-2018` | 商业 | MoviePass 预计 2018 年末超过 5m 付费订户；同口径年末结果未找到 | T：2018-06-13；目标：2018-12-31；观察约 201 天 | year-end paying subscribers；不能用峰值、下载或停运替代 | 预测：[Business Wire](https://www.businesswire.com/news/home/20180613005595/en/MoviePass%E2%84%A2-Surpasses-3-Million-Paying-Subscribers)；结果：Helios SEC filings（稳定年末同口径 URL 本轮未锁定） | `UNKNOWN/UNVERIFIED` | 付费订户定义在套餐变更／暂停服务后可能变化，缺同口径结果原件 |
| `B-BEYONDMEAT-2019` | 商业 | Beyond Meat 年内更新 2019 net revenue guidance $265–275m；10-K 有全年 net revenues | T：疑似 2019 Q3 release；目标：2019-12-31；观察约两个月 | same-year net revenue；不能换 gross profit 或 sell-through | 预测：SEC filings index（附件 accession 尚未锁定）；结果：[2019 10-K](https://www.sec.gov/Archives/edgar/data/1655210/000162828020003841/bynd201910k.htm) | `UNKNOWN/UNVERIFIED` | 预测原件 accession、发布日期和最终数字尚未恢复；所有 guidance 版本未冻结 |
| `B-WEWORK-RUNRATE-2019` | 商业 | WeWork S-1 给出 run-rate revenue/backlog，但未给未来目标日期 | T：2019-08-14；目标日期缺失；观察窗缺失 | run-rate/backlog 不是 GAAP 年度 revenue | 预测／披露：[S-1 index](https://www.sec.gov/Archives/edgar/data/1533523/000119312519220499/0001193125-19-220499-index.htm)；后续：[2021 S-1](https://www.sec.gov/Archives/edgar/data/1813756/000119312521326238/d148532ds1.htm) | `EXCLUDED` | kill pass 证实这是当时状态指标而非带目标日期的 forecast；不能把 backlog 偷换成收入预测 |
| `B-QUIBI-FIRST-YEAR` | 商业 | 疑似 Quibi 预测首年约 7m 付费订户；服务约六个月后关闭 | T：疑似 2019，具体日缺失；目标：首年日期缺失；观察窗未定义 | paid subscribers；不能用 downloads/trials/停运替代 | 预测 investor deck 原件未取得；结果线索：[CNBC](https://www.cnbc.com/2020/10/22/quibi-co-founders-katzenberg-whitman-explain-what-went-wrong.html) | `UNKNOWN/UNVERIFIED` | 原始 deck、日期、同口径官方订户结果均缺；停运不是订户结果 |

### 2.1 逐案可重建性索引

为避免让读者从状态和缺项反推，本索引把可重建性单独作为字段记录：

| case_id 集合 | 独立可重建性 | 证据等级与解释 |
|---|---|---|
| `Y2K-FEDERAL-COST-1999`、`DOW-36000-1999`、`CONCORDE-BA-PROFIT-1974`、`T-HGP-1990`、`T-EV-EVERYWHERE-2012`、`T-UGV-2000`、`T-BROADBAND-2010`、`T-MOORE-1965`、`P-2015-UK-GE`、`P-2014-SCOTLAND`、`P-2012-US-ELECTION`、`P-YUGOSLAVIA-1990`、`P-ACA-COVERAGE-2010`、`P-OMB-FY2001`、`B-NETFLIX-2011-Q3`、`B-TESLA-2016-BUILD`、`B-TESLA-2016-DELIVERIES`、`B-PELOTON-SUBSCRIPTIONS-FY2022`、`B-PELOTON-REVENUE-FY2022`、`B-MOVIEPASS-2018`、`B-BEYONDMEAT-2019`、`B-QUIBI-FIRST-YEAR` | 否（至少一个承重字段未闭合） | `UNKNOWN/UNVERIFIED`；保留为储备项，不进入冻结或 calibration 分母。 |
| `T-APOLLO-1961`、`B-WEWORK-RUNRATE-2019` | 不适用（不是本批可评分 forecast 单元） | `EXCLUDED`；保留排除理由，不进入冻结或 calibration 分母。 |

该索引不把“有预测线索”误写成“可重建”：本批独立可重建且可冻结的数量为 0。
## 3. 逐案 kill pass

本节的“kill”不是把未知案例判为预测失败，而是尝试证明候选不能作为可重建案例进入冻结池。每行保留一个可追溯理由；未能杀掉但字段不足的候选留在 `UNKNOWN/UNVERIFIED`。

| case_id | 反证动作 | 结果 |
|---|---|---|
| `Y2K-FEDERAL-COST-1999` | 用 GAO 估计的累计成本对比“没有全球灾难”或应急拨款 | 反证成功：预防成本、拨款和故障结果不是同一指标；留 UNKNOWN |
| `DOW-36000-1999` | 用 FRED 后来触及的点位代替原书未恢复的时间条件 | 反证成功：没有目标窗不能判按期命中或失准；留 UNKNOWN |
| `CONCORDE-BA-PROFIT-1974` | 用后来停飞或“项目昂贵”替代缺失的数值预测和财报 | 反证成功：停飞不是盈利结果；留 UNKNOWN |
| `T-HGP-1990` | 用 1998 修订目标和 2003 宣布完成反向替代 1990 原计划，并检查覆盖／质量阈值是否同口径 | 未能杀掉“存在候选”的事实；但杀掉“可直接判定 1990 目标已命中”的说法，留 UNKNOWN |
| `T-APOLLO-1961` | 检查原文是否是概率预测及“安全返回”是否可量化 | 杀掉本批 forecast 单元资格；排除，保留为可能的政策承诺研究对象 |
| `T-EV-EVERYWHERE-2012` | 尝试用 DOE 2022 的模型估计直接对比 blueprint 的 $125 | 发现币值、pack/cell、产量假设未闭合；不能判 miss，留 UNKNOWN |
| `T-UGV-2000` | 尝试用 GAO “未实现”叙述代替 2015 分子／分母 | 反证成功：叙述不能提供同口径结果；留 UNKNOWN |
| `T-BROADBAND-2010` | 尝试用 FCC 25/3 Mbps 人口指标替代原目标 100/50 Mbps 家庭指标 | 反证成功：对象、速度和分母均不同；留 UNKNOWN |
| `T-MOORE-1965` | 尝试用单一 8080 transistor 数或 1975 回顾代替最低成本 components 总体 | 反证成功：定义和总体不等价；留 UNKNOWN |
| `P-2015-UK-GE` | 尝试把全国民调份额直接当作下院多数结果 | 反证成功：制度结果与票份额不同；留 UNKNOWN |
| `P-2014-SCOTLAND` | 尝试用搜索摘要和已知 55.3/44.7 代替官方结果原件、调查分母与 undecided 规则 | 反证成功：尚不能独立重建；留 UNKNOWN |
| `P-2012-US-ELECTION` | 尝试用 Gallup popular-vote poll 对比 Electoral College 或无认证结果的摘要 | 反证成功：指标偷换；留 UNKNOWN |
| `P-YUGOSLAVIA-1990` | 尝试用解体后的百科／承认事实反推 CIA 预测内容 | 反证成功：没有事前原件和阈值；留 UNKNOWN |
| `P-ACA-COVERAGE-2010` | 尝试用 2016 CBO 回顾或 CMS effectuated enrollment 填补 2010 CBO 原表 | 反证成功：后续估计和结果定义不能代替 T 前预测；留 UNKNOWN |
| `P-OMB-FY2001` | 尝试用历史表的实际 receipts/surplus 反推预算原件的完整 forecast | 反证成功：缺原预算表和 unified-budget 口径；留 UNKNOWN |
| `B-NETFLIX-2011-Q3` | 尝试从结果 23.79m 反推 7 月或 9 月 guidance 图形中的数字 | 反证成功：关键预测数值未恢复，且两个版本不能择一；留 UNKNOWN |
| `B-TESLA-2016-BUILD` | 尝试把“500,000 build plan”直接当作 2018 年全年 production forecast | 反证成功：run-rate/全年与计划/预测性质未闭合；留 UNKNOWN |
| `B-TESLA-2016-DELIVERIES` | 尝试用常见“约 76,000”叙述代替官方最终 deliveries 与修订链 | 反证成功：未定位同口径官方数字；留 UNKNOWN |
| `B-PELOTON-SUBSCRIPTIONS-FY2022` | 用年末 2.966m 直接对比 2021-11 guidance，忽略中途 updated guidance | 版本链未闭合，不能判定；留 UNKNOWN |
| `B-PELOTON-REVENUE-FY2022` | 用订户结果或媒体收入数字替代同口径 FY revenue 结果 | 指标偷换且结果未转录；留 UNKNOWN |
| `B-MOVIEPASS-2018` | 尝试用服务停运、峰值 3m 或媒体叙述替代年末 paid subscribers | 反证成功：事件和峰值不是同口径结果；留 UNKNOWN |
| `B-BEYONDMEAT-2019` | 尝试用 10-K 年收入倒推未定位的 Q3 guidance | 反证成功：预测原件与版本尚未闭合；留 UNKNOWN |
| `B-WEWORK-RUNRATE-2019` | 尝试把 run-rate/backlog 作为未来年度收入预测 | 反证成功：没有目标日期，且指标不是 GAAP 年收入；排除 |
| `B-QUIBI-FIRST-YEAR` | 尝试用停运或媒体订户数替代首年 paid subscribers 结果 | 反证成功：原始 forecast 和同口径结果均缺；留 UNKNOWN |

## 4. 可冻结候选边界

### 4.1 本批没有新增可冻结候选

“候选冻结”要求第三方不依赖本页作者记忆即可重建：预测原件身份与日期、T 前数值／区间、目标日期、结果原件、同一指标／单位／分母、统一观察窗和稳定定位必须全部存在。本批每一项至少有一个字段未闭合，因此冻结数量为 **0**。

这不是“历史上没有预测失败”，也不是“方法被证明无效”。它只表示本轮宽搜尚未形成可独立重建的新增材料。已有仓库案例（如 `P-04`、`B-WEBVAN`、`B-ETOYS`）不在本批重复计数。

### 4.2 储备项的下一步闭合动作

| case_id | 最小闭合动作 |
|---|---|
| `T-HGP-1990` | 取得 1990 原计划页码、完成阈值与最终序列验收原件；把 1998 修订另立版本。 |
| `T-EV-EVERYWHERE-2012` | 固定币值年、pack/cell、模型产量与结果估计边界。 |
| `T-UGV-2000` | 读取 GAO 页码并取得 2015 分子、分母、operational／autonomous 定义。 |
| `T-BROADBAND-2010` | 找到 2020 年原目标同口径的家庭、100/50、actual speed 和 affordability 结果；否则维持 UNKNOWN。 |
| `T-MOORE-1965` | 保存 1965 原刊页码／摘录和 1975 同定义的总体测量；不能用单芯片填补。 |
| 政治三项选举／公投 | 保存官方结果原件、固定调查分母和 undecided 规则，拆票份额与制度结果。 |
| `P-YUGOSLAVIA-1990` | 取得 NIE 原件、确切主张和时间窗；找不到则排除而非用事后史补洞。 |
| `P-ACA-COVERAGE-2010` | 从 CBO 2010 原表逐项恢复目标年、定义、数字，再匹配 CMS 同口径结果。 |
| `P-OMB-FY2001` | 读取 OMB 原预算表并固定 unified-budget 口径、修订版本和年度结果。 |
| 商业候选 | 先保存 T 前 guidance 原件的数值／版本，再取同口径官方结果；任何计划、run-rate、停运事件都不能代替 forecast。 |

## 5. 覆盖地图

| 领域／材料族 | 本轮扫描内容 | 结果 | 未扫描或剩余缺口 |
|---|---|---|---|
| 科技史 | `technology-calibration*`、`historical-calibration*`、`picturephone*`、`cross-domain*`、科技相关 chains 与 NASA／DOE／FCC／GAO／Kennedy／Moore 来源指针 | 8 个新疑似候选（含 Y2K 与 Concorde）；1 个排除，7 个 UNKNOWN；无新增冻结 | 未逐项下载所有 PDF／原始页，尤其 Moore、UGV、HGP 的页码与结果分母待闭合；ITER、SunShot、IPv4 耗尽仅作零产出线索 |
| 政治／公共政策 | `politics-calibration*`、`historical-misfit*`、`historical-calibration*`、跨域页、政治／地缘 chains；2015 UK、2014 Scotland、2012 US、Yugoslavia、ACA、OMB 指针 | 6 个新疑似候选；无新增冻结；全为 UNKNOWN | 政治原件的逐页下载与官方结果复核未完成；YouGov／Commons Library／Electoral Commission 等部分页面需后续保存 |
| 商业 | `business-forecast-calibration*`、`business-regularity*`、`cross-domain*`、`picturephone*`、SEC／公司披露指针 | 10 个新疑似候选（含 Dow 36,000；Peloton 按指标拆为两案）；1 个排除，9 个 UNKNOWN；无新增冻结 | Netflix 图形 guidance、Tesla 修订链、Peloton 收入、MoviePass／Quibi 私营公司结果仍待原件闭合；Groupon、Blue Apron、Snap、Roku、Sirius XM、Ford EV 搜索未形成数字对 |
| 既有档案与方法边界 | `02-historical-validation-protocol.md`、已有 calibration 与 blind-review 证据 | 重复项被识别并未计数；分类边界沿用 | 本页不是全面重审，不触碰既有 holdout／独立重审状态 |

**覆盖结论：** 三个指定领域均有独立 harvest leg；没有静默遗漏一个指定领域。零产出搜索区已命名，不能被读者误读为已完成全面检索。

## 6. 本批形成的校准材料吗？

**没有。** 本批形成的是候选可行性审计材料：宽搜产生 24 个疑似候选，kill pass 阻止不完整配对进入冻结池，最终新增冻结数为 0。它收紧了下一轮应保存的字段和偷换边界，但没有形成可计入的 `CALIBRATION` 配对，更不形成 `CONTAMINATED_RELATIVE_HOLDOUT`、`GENUINE_FUTURE_OOS`、准确率或方法验证。

## 7. 自我约束台账

以下约束是本轮执行者为满足可重建性而加的，不把它们归于用户：

- `[self-imposed]` 只有预测原件、结果原件、同口径指标／单位／分母、观察窗和稳定定位全部可独立重建，才进入冻结候选；**理由：** 防止用故事数量代替证据闭合。
- `[self-imposed]` 计划、政策目标、run-rate、backlog、停运事件与概率 forecast 分开编码；**理由：** 它们的承诺强度和结果对象不同。
- `[self-imposed]` 预测版本必须逐版本冻结，不能选择最有利的修订版；**理由：** 防止事后择时。
- `[self-imposed]` 宽搜阶段保留疑似候选，证据门放在 kill pass；**理由：** 本轮是候选枚举，漏掉候选的代价高于事后杀掉一个假候选。

**如需放宽任何一条，必须在下一轮明确写出“删除哪条自我约束及原因”；本页不会用降低门槛来凑数。**

## 8. 来源与可复核入口

本页候选来源均已在各表逐案列出。仓库内方法边界见：

- [历史伪样本外验证协议](../zh/02-historical-validation-protocol.md)
- [历史回顾](../zh/01-retrospect.md)
- [下一批历史预测—结果证据记录](historical-calibration-next-batch-2026-10-02.md)
- [跨领域历史预测—结果证据扩展](cross-domain-forecast-outcome-expansion-2026-10-26.md)
- [科技史校准补录](technology-calibration-addendum-2026-10.md)
