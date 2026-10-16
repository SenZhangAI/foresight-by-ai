# 科技次序排序规律校准（2026-10-16）：模块化与耦合以中低置信度纳入 L11

[English version](technology-order-calibration-2026-10-16.en.md) · [方法论 §2](../zh/00-method.md#2-透镜工具箱) · [冻结包](technology-order-calibration-freeze-2026-10-16.md)

> **状态边界：** 本页是 `CALIBRATION`，不是 `HOLDOUT`，也不是 `GENUINE_FUTURE_OOS`。案例是在结局已知后选出的。冻结候选包是本判定记录的祖先；下列数字与结果材料在冻结之后才收集。因此本页只支持一条有边界的透镜，不支持方法准确率主张。

## 1. 冻结规则与入库决定

冻结的 R-T1 是：在时点 `T`，标准化的可重复单元越能并行制造，跨场址部署时需要的场地专属接口、逐案审批和不可逆责任越少，就越应更早同时达到可持续的可比单位成本下降与跨场址扩散。强场址耦合、漫长审批／建设周期或不可逆物理责任，是把系统排后并对「会最先到达」判**否**的理由。

R-T2 要求阶段分离：原型或组件价格下降不算系统成功；只有在定义窗口内，同一对象的可比单位成本指标与跨场址扩散证据同时闭合，才算系统成功。

**决定：以中低置信度、范围收窄为排序／否决透镜，纳入 L11。** 四个案例满足 2 个成功 + 2 个负例对照的校准形状，且规则确实能判「否」。它不产生命中率、准确率或样本外证据。

## 2. 案例矩阵

| 编号 | T 与冻结排序 | 结果及与规则的关系 | 证据状态 |
|---|---|---|---|
| T-CONT | 1956-04-26 Ideal X 首航；预测为本组最早「是」 | 现代集装箱化从 Ideal X 装载 58 个拖车车厢开始。里士满联储的历史材料报告，传统装卸约 5.83 美元／吨，而集装箱装船低于 0.16 美元／吨；IICL 记录其后来成为每年涉及数亿集装箱货物单元的全球多式联运系统。**成功案例，与预测一致。** | 成本对比是装卸成本，不是全航程社会成本；扩散来源是定性证据。 |
| T-PV | 1954-04-25 贝尔实验室展示；预测为「是」，但晚于 T-CONT | Bell System Memorial 报告早期硅电池效率约 6%。OWID 世界序列给出的光伏组件成本为：1975 年 132.3757、2010 年 2.5118067、2024 年 0.26518628（单位沿用图表定义）；累计装机 CSV 给出：2000 年 0.756669 GW、2010 年 39.84921 GW、2020 年 710.7258 GW、2024 年 1866.8978 GW。**成功案例，与预测一致，但保留组件／系统边界。** | 价格和装机序列分别是组件与累计装机，不是全项目发电成本；1954 原型不算系统成功。 |
| T-NUC | 1954-06-27《原子能法》签署；预测对「最先低价规模扩散」判**否** | OECD NEA 2020 年研究称，第三代反应堆在若干地区出现延期和建设成本超支，挑战核电竞争力；并把统一法规、标准、许可、融资，以及 SMR／先进反应堆列为仍需解决的降本工作。IAEA 的 2023 数据显示核电约占全球发电量 10%，发电量同比增加 2.6%；这是实际规模，但不是最先、广泛低价复制的证据。**负例对照与判否一致。** | 「低价」不是单一全球电价；IAEA 的规模数字也不是全系统价格序列。这是有边界的负结果，不是「核电失败」。 |
| T-SST | 1962-11-05 SST 计划阶段；预测对「最先低价大众客运扩散」判**否** | Smithsonian 记录协和式飞机 1976 年开始服务、16 架量产机（共造 20 架）、最多 100 名乘客、平均往返票价超过 12,000 美元、高运营成本、航线收缩，并于 2003 年退役；许多航班只有半满。GAO 1978 年报告称机场地方选择权可能不是可行的协和噪声监管方式，并认为需要明确的联邦标准。**负例对照与判否一致。** | 目标是低价大众复制，不是技术飞行或高价服务；事故、制造商停止支持和 2001 年后需求下降是混杂因素，但不抹去成本／监管证据。 |

预测排序是 **集装箱运输 → 光伏系统扩散**，核电与 SST 明确排除在「最先低价大众扩散」之外。结果支持这一排序，也支持两个负例判定；没有冻结为「否」的案例最先达到目标。

## 3. 规则能承载与不能承载什么

**能承载：**

- 「哪类技术先达到可重复降本与跨场址扩散」这一排序问题；
- 当候选是强耦合、审批密集、责任不可逆的系统，而目标是低价大众复制时，作出负面判断；
- 区分可复制的组件与可部署的系统：光伏组件是模块化的，但并网项目仍需场址、电网、融资和许可接口。

**不能承载：**

- 突破或达到可签约单位成本的精确日期；
- 把模块化相对于补贴、公共研发、地缘政治、融资和标准的贡献量化为因果效应；
- 「模块化总会胜出」，或「核电、超音速飞行技术上不可能」；
- 纯数字能力排序；本透镜针对的是部署接口可以被检查的物理或社会技术系统。

## 4. 证伪条件与领先指标

若一个冻结为**否**的类型在同一目标窗口内先于模块化、低耦合替代方案达到低价大众扩散，或一个强模块化案例反复因场址耦合压倒标准接口而失败，就应标记 L11 错误。领先指标包括：产品成本中可在工厂重复制造的模块占比；场址专属工程改动数量；审批时长及其方差；从首个单元到第二个、到第十个场址的时间；含融资与集成成本的可比单位成本；以及复用同一接口和维护流程的部署占比。

未来使用 L11 的判断卡必须说明预测的是组件成本、全系统成本还是交付服务成本，并点明可能逆转排序的部署接口与责任。

## 5. 外部对照（一致／分歧／为何仍坚持）

- **一致：** 这与既有学习曲线和标准化研究相交；上列来源也明确讨论学习、许可、融资与标准化。不把它包装成独立发现。
- **分歧：** 「技术按能力次序到达」的通俗叙事把原型、组件、系统和大众采用压成一个日期。四个案例拒绝这种压缩：贝尔实验室的可工作电池不等于光伏系统扩散，协和式的可工作服务不等于大众客运扩散。
- **为何仍坚持：** 增量主张更窄且可证伪：部署耦合与不可逆责任应影响可比降本和跨场址扩散的次序，并且必须能够判**否**。两个成功案例和两个负例对照只足以支持中低置信度入库。

## 6. 本轮新找到的失准预测案例

**0 个新的合格预测失准案例。** 本页四案是历史规则校准案例，不是本轮新发现的、带有明确预测日期并与同指标结果配对的失准预测。既有科技史校准补录也记录合格预测—结果配对为零。因此本轮不宣称某一位预测者犯错；本页记录新规则在哪些案例通过、判否，以及哪些测量仍有缺口。

## 7. 处置与重审后果

L11 作为当前透镜纳入，但本轮校准不产生 holdout。任何此前以无条件技术次序作推理的判断，仍受方法论的规则变更重审协议约束；本页不改任何判断卡的结论、状态、置信度或时间窗字段。未来使用 L11 必须明确目标指标与系统边界。

## 8. 来源与抓取说明

- Richmond Federal Reserve，*The Voyage to Containerization*：<https://www.richmondfed.org/-/media/richmondfedorg/publications/research/econ_focus/2012/q2-3/pdf/economic_history.pdf>（本运行时未能取回 PDF；装卸成本数字保留为委托研究证据，并明确记为限制）。
- Institute of International Container Lessors，*History of Containerization*：<https://www.iicl.org/about/history-of-containerization/>（1956 年 Ideal X／58 个拖车车厢；全球多式联运规模）。
- Bell System Memorial，*Bell Labs—Photovoltaics*：<https://memorial.bellsystem.com/belllabs_photovoltaics.html>（1954 年展示；约 6% 效率）。
- Our World in Data，*Solar PV module cost* CSV：<https://ourworldindata.org/grapher/solar-pv-prices.csv>（冻结后直接抓取；数字见上）。
- Our World in Data，*Solar photovoltaic cumulative capacity* CSV：<https://ourworldindata.org/grapher/solar-pv-cumulative-capacity.csv>（冻结后直接抓取；数字见上）。
- 美国能源部，*Solar Achievements Timeline*：<https://www.energy.gov/cmei/systems/solar-achievements-timeline>（2008 年实际与反事实组件成本估计；反事实数字不是市场价格）。
- OECD Nuclear Energy Agency，*Unlocking Reductions in the Construction Costs of Nuclear*：<https://www.oecd.org/en/publications/unlocking-reductions-in-the-construction-costs-of-nuclear_33ba86e1-en.html>（2020 年成本／标准／许可／融资研究；本运行时页面保护限制了直接抓取）。
- IAEA，*Nuclear Power Data and Operating Experience for 2023*：<https://www.iaea.org/newscenter/news/iaea-releases-nuclear-power-data-and-operating-experience-for-2023>（2023 年规模与发电量；本运行时页面保护限制了直接抓取）。
- Smithsonian National Air and Space Museum，*Concorde, Fox Alpha, Air France*：<https://airandspace.si.edu/collection-objects/concorde-fox-alpha-air-france/nasm_A20030139000>（服务、机队、票价、上座率与退役事实）。
- 美国 GAO，*Concorde Monitoring and Noise Regulation*, CED-78-52：<https://www.gao.gov/products/ced-78-52>（1978 年噪声监管与公众接受度证据）。
