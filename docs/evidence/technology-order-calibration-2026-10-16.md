# 科技次序排序规律校准（2026-10-16）：校准未通过，T-PV 窗口内系统成本未闭合

[English version](technology-order-calibration-2026-10-16.en.md) · [方法论 §2](../zh/00-method.md#2-透镜工具箱) · [冻结包](technology-order-calibration-freeze-2026-10-16.md)

> **状态边界：** 本页是 `CALIBRATION`，不是 `HOLDOUT`，也不是 `GENUINE_FUTURE_OOS`。案例是在结局已知后选出的。冻结候选包是本判定记录的祖先；下列数字与结果材料在冻结之后才收集。因此本页只能记录一次未通过的历史校准，不能支持透镜纳入、方法准确率主张或样本外证据。

## 1. 冻结规则与入库判定（未通过）

冻结的 R-T1 是：在时点 `T`，标准化的可重复单元越能并行制造，跨场址部署时需要的场地专属接口、逐案审批和不可逆责任越少，就越应更早同时达到可持续的可比单位成本下降与跨场址扩散。强场址耦合、漫长审批／建设周期或不可逆物理责任，是把系统排后并对「会最先到达」判**否**的理由。

R-T2 要求阶段分离：原型或组件价格下降不算系统成功；只有在定义窗口内，同一对象的可比单位成本指标与跨场址扩散证据同时闭合，才算系统成功。

**决定：校准不通过；这一缺口目前补不上。** T-PV 在截至 2010 年的冻结窗口内没有闭合同一对象、同一系统边界的可比单位成本与跨场址扩散。冻结包的 R-T2 明确禁止用原型或组件价格冒充系统成功；本轮找到的 IRENA 2010–2023 比较跨出窗口，只能作为窗口外补充。按排除规则，不能把四案写成 2 个成功 + 2 个负例，也不能把 L11 纳入方法论。

### 冻结包内部矛盾与本轮取舍

冻结包的 T-PV 检验列字面写的是「截至 2010：可比组件价格下降 + 跨场址累计装机扩散」。如果只按这一列读取，当前记录中的 OWID 组件价格和累计装机数据会让 T-PV 闭合，并把结果推向 2(a)。但冻结包同一文件的 R-T2 又明确写着「下降的组件价格不算系统级成功」，要求同一对象的可比单位成本与跨场址扩散同时闭合；两处规定不能在不加解释的情况下同时适用。

本页采用 R-T2 的更严格读法：组件价格不是系统级成本，因此 T-PV 仍为 `UNKNOWN/UNVERIFIED`，校准走 2(b)。这不是在取数前冻结的规则，而是在结果显现后作出的保守取舍：先前的 1b83337 曾按组件价格使 T-PV 闭合，ca8dfc8 又尝试用窗口外的 IRENA 系统成本，随后均在复审中被否定；本页才收口为当前判法。选择更严格方向，是为了不把口径不一致的材料升级为第二个成功案例，但读者应把这视为冻结包设计缺陷下的事后裁决，而不是规则已被干净校准。冻结包不得在本轮改写；若未来重新冻结，必须先修正 T-PV 检验列，使它与 R-T2 明确一致。

## 2. 案例矩阵

| 编号 | T 与冻结排序 | 结果及与规则的关系 | 证据状态 |
|---|---|---|---|
| T-CONT | 1956-04-26 Ideal X 首航；预测为本组最早「是」 | 现代集装箱化从 Ideal X 装载 58 个拖车车厢开始。里士满联储 2012 年《The Voyage to Containerization》原文报告，传统货物装卸约 5.83 美元／吨，而 McLean 专家估算 Ideal-X 装船成本为 15.8 美分／吨；同一文还记载 1962 年集装箱仅占纽约港货运 8%、西海岸货运 2%。窗口内的跨场址扩散：鹿特丹港史料记载 1966-05-03 Sea-Land 的 Fairland 首抵鹿特丹，每周跨大西洋全集装箱航线挂靠 Elizabeth、Rotterdam、Bremen、Grangemouth。IICL 所称「每年数亿集装箱货物单元」是当代规模，属窗口外补充，不用于闭合截至 1966 的检验。**窗口内可闭合，作为成功候选保留。** | 成本对比是装卸成本，不是全航程社会成本；扩散证据是港口史料的定性记录。里士满联储原文引述 Levinson，成本数字仍不是独立的全系统成本序列。 |
| T-PV | 1954-04-25 贝尔实验室展示；预测为「是」，但晚于 T-CONT | Bell System Memorial 报告早期硅电池效率约 6%。OWID 世界序列给出的光伏组件成本为：1975 年 132.3757、2010 年 2.5118067、2024 年 0.26518628（单位沿用图表定义）；累计装机 CSV 给出：2000 年 0.756669 GW、2010 年 39.84921 GW、2020 年 710.7258 GW、2024 年 1866.8978 GW。IRENA 的可比全系统 LCOE 比较为 2010 年对 2023 年，超出截至 2010 的冻结窗口；因此窗口内没有同一系统口径的成本下降序列。**`UNKNOWN/UNVERIFIED`：不能计入成功案例；冻结包检验列与 R-T2 的冲突及本页的事后取舍见 §1。** | 组件价格与累计装机是补充材料；窗口外 IRENA 数字不能闭合 R-T2。IEA-PVPS《Germany 2010 National Survey Report》页面确认报告存在，但本运行时无法取回 PDF 正文和其中的 turnkey 价格表，故不得把未读取的数字当作证据。 |
| T-NUC | 1954-06-27《原子能法》签署；预测对「最先低价规模扩散」判**否** | 可取得的 OECD NEA 2020 年研究摘要称，第三代反应堆在若干地区出现延期和建设成本超支，挑战核电竞争力；并把统一法规、标准、许可、融资，以及 SMR／先进反应堆列为仍需解决的降本工作。IAEA 的 2023 数据显示核电约占全球发电量 10%，发电量同比增加 2.6%；该数据晚于截至 2020 的冻结窗口，只作窗口外补充，且本身也不是最先、广泛低价复制的证据。**负例方向一致，但证据偏弱：** 这只能依据窗口内 NEA 2020 研究中关于延期、成本超支和仍需降本工作的论述；本页没有直接读到 NEA 正文的完整部署结论，也没有窗口内「地理上广泛部署」的同口径证据。 | 「低价」不是单一全球电价；窗口内证据是成本超支与仍需降本的定性研究，不是全系统价格序列。这是有边界的负结果，不是「核电失败」。 |
| T-SST | 1962-11-05 SST 计划阶段；预测对「最先低价大众客运扩散」判**否** | Smithsonian 记录协和式飞机 1976 年开始服务、16 架量产机（共造 20 架）、最多 100 名乘客、平均往返票价超过 12,000 美元、高运营成本、航线收缩，并于 2003 年退役；许多航班只有半满。GAO 1978 年报告称机场地方选择权可能不是可行的协和噪声监管方式，并认为需要明确的联邦标准。**负例对照与判否一致。** | 目标是低价大众复制，不是技术飞行或高价服务；事故、制造商停止支持和 2001 年后需求下降是混杂因素，但不抹去成本／监管证据。 |

由于 T-PV 未能在冻结窗口内闭合，不能得出「集装箱运输 → 光伏系统扩散」已通过校准的结论。T-CONT 是当前唯一可继续保留的成功候选；T-NUC 与 T-SST 仍是判否对照，但不足以满足 2 个成功案例的最低要求。

## 3. 候选规则原本打算承载与不承载什么（未纳入，仅作记录）

以下是冻结候选的设计范围，保留是为了让未来的重新校准有起点；由于本轮校准未通过，它们**都不是**现行方法论的一部分，任何判断卡不得据此主张透镜背书。

**原拟承载：**

- 「哪类技术先达到可重复降本与跨场址扩散」这一排序问题；
- 当候选是强耦合、审批密集、责任不可逆的系统，而目标是低价大众复制时，作出负面判断；
- 区分可复制的组件与可部署的系统：光伏组件是模块化的，但并网项目仍需场址、电网、融资和许可接口。

**原拟不承载：**

- 突破或达到可签约单位成本的精确日期；
- 把模块化相对于补贴、公共研发、地缘政治、融资和标准的贡献量化为因果效应；
- 「模块化总会胜出」，或「核电、超音速飞行技术上不可能」；
- 纯数字能力排序；本透镜针对的是部署接口可以被检查的物理或社会技术系统。

## 4. 证伪条件与领先指标

（未纳入，仅作记录：以下是候选规则若将来重新校准并通过时应携带的证伪条件。）若一个冻结为**否**的类型在同一目标窗口内先于模块化、低耦合替代方案达到低价大众扩散，或一个强模块化案例反复因场址耦合压倒标准接口而失败，就应判该候选规则错误。领先指标包括：产品成本中可在工厂重复制造的模块占比；场址专属工程改动数量；审批时长及其方差；从首个单元到第二个、到第十个场址的时间；含融资与集成成本的可比单位成本；以及复用同一接口和维护流程的部署占比。

若将来重新校准通过，使用该规则的判断卡必须说明预测的是组件成本、全系统成本还是交付服务成本，并点明可能逆转排序的部署接口与责任。本轮未通过，因此目前没有判断卡可以使用它。

## 5. 外部对照（一致／分歧／为何仍坚持）

- **一致：** 这与既有学习曲线和标准化研究相交；上列来源也明确讨论学习、许可、融资与标准化。不把它包装成独立发现。
- **分歧：** 「技术按能力次序到达」的通俗叙事把原型、组件、系统和大众采用压成一个日期。四个案例拒绝这种压缩：贝尔实验室的可工作电池不等于光伏系统扩散，协和式的可工作服务不等于大众客运扩散。
- **为何没有坚持：** 增量主张更窄且可证伪：部署耦合与不可逆责任应影响可比降本和跨场址扩散的次序，并且必须能够判**否**。但本轮只能在窗口内闭合一个成功案例（T-CONT），T-PV 未闭合，达不到 2 个成功案例的最低要求，因此不入库；与外部文献一致这一点不能替代窗口内证据。

## 6. 本轮新找到的失准预测案例

**0 个新的合格预测失准案例。** 本页四案是历史规则校准案例，不是本轮新发现的、带有明确预测日期并与同指标结果配对的失准预测。既有科技史校准补录也记录合格预测—结果配对为零。因此本轮不宣称某一位预测者犯错；本页记录新规则在哪些案例通过、判否，以及哪些测量仍有缺口。

## 7. 处置与重审后果

本轮不纳入 L11。冻结规则未被改写；由于 T-PV 的窗口内系统成本缺口，校准按 2(b) 收口为「这一缺口目前补不上」。本页不改任何判断卡的结论、状态、置信度或时间窗字段，也不产生 holdout；未来若要补入此类透镜，必须另行冻结候选、修复同一系统口径的窗口内证据，并按 §1.3 触发重审。

## 8. 来源与抓取说明

- Richmond Federal Reserve，*The Voyage to Containerization*：<https://www.richmondfed.org/-/media/richmondfedorg/publications/research/econ_focus/2012/q2-3/pdf/economic_history.pdf>（本轮直接取回 PDF 正文核对：原文写传统装卸约 5.83 美元／吨、Ideal-X 装船成本 15.8 美分／吨，并记载 1962 年集装箱占纽约港货运 8%、西海岸货运 2%；原文引述 Levinson，成本比较仍是装卸成本而非全系统成本）。
- Institute of International Container Lessors，*History of Containerization*：<https://www.iicl.org/about/history-of-containerization/>（1956 年 Ideal X／58 个拖车车厢；全球多式联运规模是当代数字，属窗口外补充）。
- SuperSummary，*The Box* by Marc Levinson 摘要：<https://www.supersummary.com/the-box-marc-levinson/summary/>（1956 年 Ideal X 装船约 15.8 美分／吨对传统散货 5.83 美元／吨；二手摘要，作为窗口内成本证据并记为限制）。
- Port of Rotterdam 史料（docslib 转载）：<https://docslib.org/doc/9660426/port-of-rotterdam-brief-history-of-container-transport-forty-years-ago-on-3-may-1966-sea-lands-container-ship-fairland-a>（1966-05-03 Sea-Land 的 Fairland 首抵鹿特丹，每周跨大西洋全集装箱航线挂靠 Elizabeth、Rotterdam、Bremen、Grangemouth；窗口内跨场址扩散证据）。
- Bell System Memorial，*Bell Labs—Photovoltaics*：<https://memorial.bellsystem.com/belllabs_photovoltaics.html>（1954 年展示；约 6% 效率）。
- Our World in Data，*Solar PV module cost* CSV：<https://ourworldindata.org/grapher/solar-pv-prices.csv>（冻结后直接抓取；数字见上）。
- Our World in Data，*Solar photovoltaic cumulative capacity* CSV：<https://ourworldindata.org/grapher/solar-pv-cumulative-capacity.csv>（冻结后直接抓取；数字见上）。
- IRENA，*Renewable Power Generation Costs in 2023*：<https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023>（2010 与 2023 光伏 LCOE 的比较；2023 年在冻结窗口之外，不能用于闭合截至 2010 的检验）。
- IEA-PVPS，*National Survey Report Germany – 2010*：<https://iea-pvps.org/national_survey/national-survey-report-germany-2010/>；PDF：<https://iea-pvps.org/wp-content/uploads/2020/01/nsr_2010_DEU.pdf>（页面确认报告身份与下载地址；本运行时无法取回 PDF 正文和 turnkey 价格表，因此未将其作为已取得的窗口内数字证据）。
- 美国能源部，*Solar Achievements Timeline*：<https://www.energy.gov/cmei/systems/solar-achievements-timeline>（2008 年实际与反事实组件成本估计；反事实数字不是市场价格）。
- OECD Nuclear Energy Agency，*Unlocking Reductions in the Construction Costs of Nuclear*：<https://www.oecd.org/en/publications/unlocking-reductions-in-the-construction-costs-of-nuclear_33ba86e1-en.html>（2020 年成本／标准／许可／融资研究；本运行时页面保护限制了直接抓取）。
- IAEA，*Nuclear Power Data and Operating Experience for 2023*：<https://www.iaea.org/newscenter/news/iaea-releases-nuclear-power-data-and-operating-experience-for-2023>（2023 年规模与发电量；晚于截至 2020 的冻结窗口，只作窗口外补充；本运行时页面保护限制了直接抓取）。
- Smithsonian National Air and Space Museum，*Concorde, Fox Alpha, Air France*：<https://airandspace.si.edu/collection-objects/concorde-fox-alpha-air-france/nasm_A20030139000>（服务、机队、票价、上座率与退役事实）。
- 美国 GAO，*Concorde Monitoring and Noise Regulation*, CED-78-52：<https://www.gao.gov/products/ced-78-52>（1978 年噪声监管与公众接受度证据）。
