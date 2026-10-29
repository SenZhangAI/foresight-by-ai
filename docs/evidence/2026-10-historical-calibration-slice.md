# 2026-10 有界科技史校准切片

[English version below](#bounded-technology-history-calibration-slice-2026-10)

## 这份切片回答什么

本页不是未来预测准确率，也不是按既有科技名人或成功产品挑出的“案例集”。它是一个有界的证据增量：扫描公开机构在技术项目、技术竞赛和基础设施目标中留下的**事前目标／预测**，再在目标期限或统一观察窗后检查结果。所有材料都在结果已知后整理，因此本页最多产生 `CALIBRATION`，不会产生 `CONTAMINATED_RELATIVE_HOLDOUT` 或 `GENUINE_FUTURE_OOS`。

**[self-imposed] 本切片把“技术史中的预测”操作化为技术项目目标、技术竞赛目标和量化行业投影，而不是把它们冒充社会级扩散预测——理由是当前科技域的公开材料尚不能同时闭合原始 T 前材料、社会分母和同口径结果。**

## 覆盖地图与边界

| 扫描域 | 实际扫描的公开入口 | 候选数 | 结果 | 未覆盖／缺口 |
|---|---|---:|---:|---|
| 国家技术项目目标 | NASA 2004 Vision、NASA ISS 页面、NHGRI/HGP 页面 | 3 | 2 `CALIBRATION`；1 `UNKNOWN/UNVERIFIED` | 未扫描完整 NASA 项目名录，不能外推到全部国家技术项目 |
| 技术竞赛／能力演示 | DARPA Grand Challenge 页面 | 1 | 1 `CALIBRATION` | 未扫描 DARPA 全部挑战赛名录；竞赛完成不等于社会扩散 |
| 国际 ICT 行业投影 | ITU 2005 市场预测 PDF 与 ITU 统计页 | 1 | `UNKNOWN/UNVERIFIED` | 原始 PDF 的发布日期、定义与同口径分母尚未在当前可复核包中闭合 |
| 能源技术成本目标 | DOE SunShot 页面 | 1 | `UNKNOWN/UNVERIFIED` | 当前可读页面未提供目标年、目标值与统一结果窗口 |
| 专利／论文／临床注册名录 | 本轮未扫描 | 0 | 未覆盖 | 这是协议 §1 推荐的技术抽样框，下一轮需从完整名录建立候选池，而不是继续挑名案 |

覆盖结论：本轮实际读取并记录了 6 个候选入口；结果为 3 条 `CALIBRATION` 与 3 条 `UNKNOWN/UNVERIFIED`。没有扫描的专利、论文、临床试验和完整竞赛名录不能被写成“科技史总体”。

## 逐项结果

| case_id | T 与事前目标／预测 | 判定窗口与指标／分母 | 原始来源定位 | 结果标签 | 缺项与处置 |
|---|---|---|---|---|---|
| `TECH-HGP-1990` | 1990 年 2 月 NIH/DOE 原始 *A Five-Year Plan for the Human Genome Project* 把计划写成约 15 年、约 2 亿美元／年的长期工程，并把分析人类 DNA 结构与定位估计的全部人类基因列为目标；官方回顾称 2003 年完成，比原计划提前两年多、低于预算 | 1990–2005（原计划“approximately 15 years”）；目标分母是估计的人类基因，结果侧是完整序列、gene-containing-region 覆盖／准确率和预算；这些分母和预算口径未完全对齐 | NIH/DOE, *A Five-Year Plan for the Human Genome Project* (February 1990), https://www.genome.gov/sites/default/files/media/files/2021-02/1990_First_Five_Year_Plan.pdf，PDF pp.1–5；NHGRI, *Human Genome Project Results*, https://www.genome.gov/human-genome-project/results；https://www.genome.gov/25520492/online-education-kit-2003-human-genome-project-completed | `UNKNOWN/UNVERIFIED` | 项目期限与结果日期可重建，但目标“约 100,000 个基因”与结果“gene-containing regions”不是已证明同一分母；预算也没有同币种完整对账。不得把部分闭合升级成 `CALIBRATION` |
| `TECH-ISS-2004` | 2004-01-14 的 NASA Vision：2010 年完成国际空间站 | 2004–2011；指标为国际合作伙伴是否完成空间站组装；分母是该计划定义的空间站整体，而非用户数 | NASA, *Vision for Space Exploration*, https://www.nasa.gov/history/vision-for-space-exploration/；NASA, *International Space Station Final Configuration*, https://www.nasa.gov/image-article/international-space-station-final-configuration/ | `CALIBRATION`（期限延误） | “完成”按 NASA 的组装定义；不把它升级成空间基础设施成本或科学产出的预测 |
| `TECH-MOON-2004` | 2004-01-14 的 NASA Vision：2020 年前返回月球；另写有 2015 年起较长期月面任务愿景 | 2004–2020 截止日，并以 2026-10 官方计划作确认；指标为是否在 2020 前完成载人登月，分母为该政策目标的载人月面任务 | NASA 2004 Vision（同上）；NASA, *Artemis*, https://www.nasa.gov/humans-in-space/artemis/ | `CALIBRATION`（截至截止日未达到） | 当前官方页面把首次 Artemis 载人登月列为 2028；本条证明目标期限未达成，不证明未来 2028 也会失败 |
| `TECH-DARPA-2004` | 2004 Grand Challenge 以无人车完成沙漠赛道为能力目标 | 2004 比赛当日；指标为完成整条赛道的车辆数，分母为参赛车辆／队伍；2004 年为 0 | DARPA, *Grand Challenge*, https://www.darpa.mil/about/innovation-timeline/grand-challenge | `CALIBRATION`（首届目标未达成） | 2005 后续赛道的 5 队完成只作来源中的后续上下文，不并入本候选的结果；不把次年成功回填为 2004 成功 |
| `TECH-ITU-2005` | ITU *The International Telecommunications Market in 2005* 将趋势外推到 2005：1.4B 固话、950M cellular、400–500M Internet users | 预测年 2005；指标、单位和全球分母需与揭晓统计逐项对齐 | ITU PDF, https://www.itu.int/ITU-D/ict/papers/witwatersrand/in2005.pdf；ITU 2005 statistical report, https://www.itu.int/pub/S-POL-IR.IT-2005/e | `UNKNOWN/UNVERIFIED` | 当前包无法同时闭合原 PDF 发布日期、预测口径与同窗统计的定义／分母；不把搜索摘要或“约 875M（2004 年末）”升级为校准结果 |
| `TECH-SUNSHOT-2011` | DOE SunShot 是降低太阳能成本的政策／研发目标入口 | 需目标年、$/W 或 $/kWh 指标、地理范围、生产／部署分母和结果窗口 | DOE, *Reducing Photovoltaic Costs*, https://www.energy.gov/cmei/systems/reducing-photovoltaic-costs；DOE, *Solar Achievements Timeline*, https://www.energy.gov/cmei/systems/solar-achievements-timeline | `UNKNOWN/UNVERIFIED` | 当前可读页面只给一般目标和项目描述，不能从“成本下降”补出具体目标与结果；待原始 SunShot Vision 包和同口径成本序列闭合后再入校准 |

## 冻结摘录与抓取记录

以下是本轮在 **2026-10-29 UTC** 读取并用于判定的最小原文摘录；证据页把摘录连同 URL 一起冻结，避免仅靠未来可能变化的页面。动态网页没有稳定字节包，因此不伪造内容哈希；如需逐字节复现，下一轮须另存公开归档快照。

| case_id | 冻结目标／结果摘录与页面定位 | 抓取边界 |
|---|---|---|
| `TECH-HGP-1990` | NIH/DOE 1990 原始计划封面明确日期 **“February 1990”**。PDF p.4 把总目标写为分析人类 DNA 结构并定位估计的 100,000 个人类基因；p.5 写预算需要仍为 **“about $200 million per year for approximately 15 years”**，并说明 1991–1995 是首个五年目标期。NHGRI Results 页：**“In 2003, an accurate and complete human genome sequence was finished … two years ahead of the original Human Genome Project schedule and at a cost less than the original estimated budget.”** 结果页另给 **“99 percent”** gene-containing-region coverage 与 **“99.99 percent”** accuracy。 | T 前材料现在由 1990 原始计划及页码闭合，不再依赖未定年代的 FAQ；原计划是约数，预算同币种完整对账仍未闭合。 |
| `TECH-ISS-2004` | NASA 2004 Vision：**“Our first goal is to complete the International Space Station by 2010.”** NASA Final Configuration：**“NASA and its international partners completed assembly of the International Space Station in the fall of 2011.”** | 两句均来自 NASA 网页；完成仅按 assembly 定义。 |
| `TECH-MOON-2004` | NASA 2004 Vision：**“Our third goal is to return to the moon by 2020.”** NASA Apollo 17 任务页把 Apollo 17 称为 **“The Apollo Program's last lunar landing mission”**，并称 Eugene Cernan 是 **“the last person to leave his footprints on the surface of the Moon”**；页面列出 1972-12-07 发射、1972-12-19 溅落。 | Apollo 17 官方任务史提供结果侧边界：最后一次载人登月仍是 1972，而目标窗截至 2020；不再用 2028 计划替代结果证据。 |
| `TECH-DARPA-2004` | DARPA Grand Challenge 页面回顾：**“no vehicle completed the route”**（2004）；同页后续事件写 **“A total of five teams completed the Grand Challenge course”**，课程 **“132 miles over desert terrain”**（2005）。 | 判定只用 2004 的 0 队结果；2005 摘录仅用于防止跨年回填。 |
| `TECH-ITU-2005` | ITU 搜索入口摘要给出 2005 投影：**“1.4 billion fixed telephone lines, 950 million cellular subscribers and around 400–500 million Internet users.”** | 原 PDF 未由本轮文件工具解析，发布日期、定义与同口径揭晓统计未冻结，故保持 `UNKNOWN/UNVERIFIED`。 |
| `TECH-SUNSHOT-2011` | DOE *Reducing Photovoltaic Costs* 可读页只给一般目标：**“making solar cost-competitive with other sources of energy.”** DOE timeline 页可读结果包含 2008 module production cost **“$5.27 … without the Energy Department’s involvement”** 与 **“$1.92”**，但未给本候选所需的 SunShot 目标年、目标值和同一部署分母。 | 一般政策目标和反事实成本不能补成目标—结果配对，故保持 `UNKNOWN/UNVERIFIED`。 |

这些摘录是本页的可核对证据层；URL 仍列在逐项表中。没有内容哈希意味着它们是“提交时冻结的转录 + 原页面定位”，而不是逐字节网页归档，此限制不隐藏。


**`TECH-HGP-1990`：期限与结果日期有证据，但同口径闸门未通过。** NIH/DOE 1990 原始计划给出约 15 年、约 2 亿美元／年的长期预算与分析人类 DNA／定位全部基因的目标；官方结果页给出 2003 年完成、比原计划提前两年多、低于预算，并给出约 99% 基因区域覆盖和 99.99% 准确率。由于“约 100,000 个基因”的目标分母与“gene-containing regions”的结果分母未证明一致，且预算没有同币种完整对账，保留 `UNKNOWN/UNVERIFIED`；不能把“部分闭合”当作校准。

**`TECH-ISS-2004`：目标明确，期限发生延误。** 2004 Vision 的原句是“complete the International Space Station by 2010”；NASA 后续页面说国际伙伴在 2011 年秋完成组装。这里的失败只是“未在预先目标年完成”，不是空间站项目整体失败，也不是对复杂工程项目的普遍定律。

**`TECH-MOON-2004`：目标期限未达到，但未来结果仍未封闭。** 2004 Vision 原句是“return to the moon by 2020”。当前 NASA Artemis 页面把首次载人登月列为 2028，并把 2027 定义为低地球轨道演示；因此 2020 截止目标可编码为未达到。不能把 2028 的计划当作已实现，也不能把一个政策目标的延期写成“载人航天必然失败”。

**`TECH-DARPA-2004`：首届竞赛只按首届结果判定。** DARPA 回顾明确给出：2004 年没有车辆完成路线；同页另说 2005 年有 5 支队伍完成 132 英里赛道。后者是下一年度事件的上下文，不是本候选的结果，避免跨年度回填。它适合校准“明确的工程目标可以在竞赛和资金机制下被推进”，但不能支持“无人驾驶已社会普及”。

## Kill 清单与保留处置

| 候选 | kill 尝试 | 处置 |
|---|---|---|
| `TECH-HGP-1990` | The target–outcome denominator is not closed: the 1990 plan targets locating an estimated 100,000 human genes, while the reported outcome uses gene-containing-region coverage and accuracy; budget reconciliation is also incomplete | Kill the stronger calibration claim; retain `UNKNOWN/UNVERIFIED` with the original plan and result excerpts, and do not count it as a calibration denominator |
| `TECH-ISS-2004` | 试图把组装完成当作社会级基础设施普及或成本预测 | 杀掉社会扩散／成本外推；保留为项目期限校准 |
| `TECH-MOON-2004` | 试图把 2028 计划当成实现，或把 2020 未达成写成未来永远失败 | 杀掉两种过度结论；保留“目标期限未达成”的 `CALIBRATION` |
| `TECH-DARPA-2004` | 试图把 2005 五队完成回填为 2004 成功，或把竞赛结果当成市场扩散 | 杀掉跨年份回填与社会扩散外推；保留两个年度事件的工程目标记录 |
| `TECH-ITU-2005` | 试图用搜索摘要和不同统计页直接相减 | 证据门失败；保留 `UNKNOWN/UNVERIFIED`，下一步先闭合日期、定义、单位、分母 |
| `TECH-SUNSHOT-2011` | 试图从一般性的“成本竞争力”补写具体目标年与达成值 | 证据门失败；保留 `UNKNOWN/UNVERIFIED`，不得计入科技校准分母 |

## 回流到方法边界

1. **本切片的结果是 3 条 `CALIBRATION`、3 条 `UNKNOWN/UNVERIFIED`。** 技术项目目标可以提供可重建的 calibration，但不等于社会趋势预测；HGP 的目标—结果分母未闭合，不能计入 calibration。
2. **“有原始目标”与“有可比结果”是两道门。** ITU 和 SunShot 都有可信机构与主题，但当前不能同时闭合发布日期、指标定义、观察窗和分母，因此保持 `UNKNOWN/UNVERIFIED`。
3. **期限失败与能力失败要分开。** ISS 是期限延误；Moon 是 2020 政策期限未达成但后续计划仍在；DARPA 是首年失败、次年达成；这些不能压成一个“技术预测失败率”。
4. **本切片不改变历史验证协议的 holdout 规则。** 它没有预先冻结候选、随机分配、隔离判闸或同输入基线，因此不能写成伪样本外，更不能写成未来样本外。
5. **对未来推演的直接修正：** 技术能力到达次序必须把“目标机制、资金与竞赛、制度期限、基础设施组装、社会扩散”分层；工程目标在短期内可以被组织加速，但社会级扩散仍需另有分母与采用证据。

## 约束账本

- `[self-imposed]` 先做有界证据增量，不把本页扩成完整科技史；理由是当前任务验收要求可重建、逐项 kill 和显式缺口。
- `[self-imposed]` 所有结果已知后整理的候选统一标 `CALIBRATION` 或 `UNKNOWN/UNVERIFIED`；理由是防止把历史材料误报成样本外准确率。
- `[self-imposed]` 项目目标、竞赛目标与社会扩散分开编码；理由是同一技术事件的工程成功不等于社会采用成功。

---

# Bounded Technology-History Calibration Slice 2026-10

## What this slice answers

This page is a bounded evidence increment, not a forecast-accuracy estimate and not a list chosen from famous winners or failures. It scans public pre-event targets or projections in technology programmes, engineering competitions, and quantitative industry outlooks, then checks the outcome at the target deadline or a stated observation window. Because every item was assembled after its outcome was known, this page can produce at most `CALIBRATION`; it produces neither `CONTAMINATED_RELATIVE_HOLDOUT` nor `GENUINE_FUTURE_OOS`.

**[self-imposed] This slice operationalizes “technology-history forecasts” as programme targets, competition targets, and quantified industry projections rather than presenting them as society-scale diffusion forecasts. The reason is that the current technology record cannot yet close an original as-of-T packet, a social denominator, and a same-metric outcome at the same time.**

## Coverage map and boundary

| Scan lane | Public entries actually read | Candidates | Result | Uncovered / gap |
|---|---|---:|---:|---|
| National technology programme targets | NASA 2004 Vision, NASA ISS page, NHGRI/HGP pages | 3 | 2 `CALIBRATION`; 1 `UNKNOWN/UNVERIFIED` | Not a complete NASA programme registry; no population-wide inference |
| Technology competition / capability demonstration | DARPA Grand Challenge pages | 1 | 1 `CALIBRATION` | Not a complete DARPA challenge registry; completion is not diffusion |
| International ICT projection | ITU 2005 market PDF and statistics page | 1 | `UNKNOWN/UNVERIFIED` | PDF date, definitions, and same-denominator outcome are not closed in the reproducible packet |
| Energy-technology cost target | DOE SunShot pages | 1 | `UNKNOWN/UNVERIFIED` | The readable pages do not provide a target year, target value, and uniform outcome window together |
| Patent / paper / clinical-trial registries | Not scanned this round | 0 | Uncovered | The next round must sample a complete registry, not continue selecting famous cases |

Coverage conclusion: six public entry points were read and recorded, yielding 3 `CALIBRATION` and 3 `UNKNOWN/UNVERIFIED` records. The unscanned patent, paper, clinical-trial, and complete competition registries cannot be represented as “technology history overall.”

## Candidate-level results

| case_id | T and pre-event target / projection | Window and metric / denominator | Source location | Label | Missing pieces / disposition |
|---|---|---|---|---|---|
| `TECH-HGP-1990` | Human Genome Project launched under the February 1990 NIH/DOE *Five-Year Plan*, which described an approximately 15-year effort at about $200 million per year and set the goal of analyzing human DNA structure and locating the estimated 100,000 human genes; the official retrospective says completion in 2003 was more than two years ahead of schedule and under budget | 1990–2005; the target denominator is estimated human genes, while the outcome side reports complete sequence, gene-containing-region coverage / accuracy, and budget; the denominators and budget basis are not fully aligned | NIH/DOE, *A Five-Year Plan for the Human Genome Project* (February 1990), https://www.genome.gov/sites/default/files/media/files/2021-02/1990_First_Five_Year_Plan.pdf, PDF pp.1–5; NHGRI, *Human Genome Project Results*, https://www.genome.gov/human-genome-project/results; https://www.genome.gov/25520492/online-education-kit-2003-human-genome-project-completed | `UNKNOWN/UNVERIFIED` | The schedule and outcome date are reconstructible, but the estimated-gene target denominator is not shown to match gene-containing-region coverage / accuracy, and the budget lacks same-currency reconciliation. Do not upgrade partial closure to `CALIBRATION` |
| `TECH-ISS-2004` | NASA’s 2004 Vision: complete the International Space Station by 2010 | 2004–2011; whether partner nations completed station assembly; denominator is the programme-defined station, not users | NASA, *Vision for Space Exploration*, https://www.nasa.gov/history/vision-for-space-exploration/; NASA, *International Space Station Final Configuration*, https://www.nasa.gov/image-article/international-space-station-final-configuration/ | `CALIBRATION` (deadline delay) | “Completion” follows NASA’s assembly definition; do not upgrade it into a cost or science-output forecast |
| `TECH-MOON-2004` | NASA’s 2004 Vision: return humans to the Moon by 2020; it also described extended lunar missions as early as 2015 | 2004–2020 deadline, confirmed against the official 2026 plan; whether a crewed lunar landing occurred by 2020; denominator is the policy target’s crewed lunar mission | NASA 2004 Vision (above); NASA, *Artemis*, https://www.nasa.gov/humans-in-space/artemis/ | `CALIBRATION` (deadline not met) | The current official page schedules the first Artemis crewed lunar landing for 2028; this shows the deadline was missed, not that the 2028 plan will fail |
| `TECH-DARPA-2004` | The 2004 Grand Challenge set an autonomous-vehicle desert-course completion target | 2004 event; number of vehicles completing the full course, denominator the entrants / teams; 0 completed in 2004 | DARPA, *Grand Challenge*, https://www.darpa.mil/about/innovation-timeline/grand-challenge | `CALIBRATION` (first-event target missed) | The 2005 follow-on’s five finishers are source context only and are not included in this candidate’s result; do not backfill the next year’s success |
| `TECH-ITU-2005` | ITU’s *The International Telecommunications Market in 2005* projected 1.4B fixed lines, 950M cellular subscribers, and 400–500M Internet users for 2005 | Forecast year 2005; metrics, units, and global denominators must be aligned to reveal statistics | ITU PDF, https://www.itu.int/ITU-D/ict/papers/witwatersrand/in2005.pdf; ITU report, https://www.itu.int/pub/S-POL-IR.IT-2005/e | `UNKNOWN/UNVERIFIED` | The current packet cannot close the PDF publication date, projection definitions, and same-window denominator; do not turn search snippets or an “about 875M at end-2004” figure into calibration |
| `TECH-SUNSHOT-2011` | DOE’s SunShot entry describes a policy / R&D route to lower solar costs | Need target year, $/W or $/kWh metric, geography, production / deployment denominator, and outcome window | DOE, *Reducing Photovoltaic Costs*, https://www.energy.gov/cmei/systems/reducing-photovoltaic-costs; DOE, *Solar Achievements Timeline*, https://www.energy.gov/cmei/systems/solar-achievements-timeline | `UNKNOWN/UNVERIFIED` | The readable pages provide general aims and projects but not a closed target and outcome pair; await the original SunShot Vision packet and same-metric cost series |

## Frozen excerpts and capture record

The following are the minimum source excerpts read and used for adjudication on **2026-10-29 UTC**. The evidence page freezes the excerpts alongside their URLs so the record does not depend only on a future version of a mutable page. Dynamic pages did not provide a stable byte packet, so no content hash is invented; byte-for-byte reconstruction would require a separately preserved public archive snapshot in a later round.

| case_id | Frozen target / outcome excerpt and location | Capture boundary |
|---|---|---|
| `TECH-HGP-1990` | The NIH/DOE original plan cover is dated **“February 1990.”** PDF p.4 states the goal of analyzing human DNA structure and locating the estimated 100,000 human genes; p.5 says budget needs remained **“about $200 million per year for approximately 15 years”** and identifies FY1991–FY1995 as the first five-year goal period. NHGRI Results: **“In 2003, an accurate and complete human genome sequence was finished … two years ahead of the original Human Genome Project schedule and at a cost less than the original estimated budget.”** It also reports **“99 percent”** gene-containing-region coverage and **“99.99 percent”** accuracy. | The 1990 original plan and page locators close the pre-T material, but the target denominator (estimated genes) and result denominator (gene-containing regions) are not demonstrated to match; same-currency budget reconciliation also remains open, so status is `UNKNOWN/UNVERIFIED`. |
| `TECH-ISS-2004` | NASA 2004 Vision: **“Our first goal is to complete the International Space Station by 2010.”** NASA Final Configuration: **“NASA and its international partners completed assembly of the International Space Station in the fall of 2011.”** | Both excerpts are from NASA web pages; completion follows the assembly definition only. |
| `TECH-MOON-2004` | NASA 2004 Vision: **“Our third goal is to return to the moon by 2020.”** NASA’s Apollo 17 mission page calls Apollo 17 **“The Apollo Program's last lunar landing mission”** and Eugene Cernan **“the last person to leave his footprints on the surface of the Moon”**; it lists launch on Dec. 7, 1972 and splashdown on Dec. 19, 1972. | The official Apollo 17 mission history closes the outcome side: the last human lunar landing remained in 1972 while the target window ended in 2020. A 2028 plan is no longer used as substitute outcome evidence. |
| `TECH-DARPA-2004` | DARPA Grand Challenge retrospective: **“no vehicle completed the route”** in 2004; the same page’s follow-on event says **“A total of five teams completed the Grand Challenge course”**, a **“132 miles over desert terrain”** course, in 2005. | The adjudication uses only the 2004 zero-finish result; the 2005 excerpt is retained only to prevent cross-year backfill. |
| `TECH-ITU-2005` | ITU search locator summarizes the projection as **“1.4 billion fixed telephone lines, 950 million cellular subscribers and around 400–500 million Internet users”** for 2005. | The original PDF was not parsed by the current file tool, and its publication date, definitions, and same-metric reveal statistics were not frozen; status remains `UNKNOWN/UNVERIFIED`. |
| `TECH-SUNSHOT-2011` | DOE *Reducing Photovoltaic Costs* provides only the general aim **“making solar cost-competitive with other sources of energy.”** The readable DOE timeline reports a 2008 module-production counterfactual of **“$5.27 … without the Energy Department’s involvement”** versus **“$1.92”**, but not this candidate’s required SunShot target year, target value, and deployment denominator. | A general policy aim and counterfactual cost cannot manufacture a target–outcome pair; status remains `UNKNOWN/UNVERIFIED`. |

These excerpts are this page’s checkable evidence layer; the candidate table retains the URLs. The absence of content hashes means “transcription frozen in the commit + original-page locator”, not a byte-preserved web archive, and that limitation remains explicit.


| Candidate | Falsification attempt | Disposition |
|---|---|---|
| `TECH-HGP-1990` | Try to turn “more than two years ahead” into an exact date / budget error; the source does not contain those numbers, and the target/outcome denominators are not shown to match | Kill the stronger exact-budget and denominator-matched calibration claims; retain `UNKNOWN/UNVERIFIED` with the gap explicit |
| `TECH-ISS-2004` | Treat assembly completion as society-scale infrastructure diffusion or a cost forecast | Kill the diffusion / cost extrapolation; retain as a programme-deadline calibration |
| `TECH-MOON-2004` | Treat the 2028 plan as achieved, or turn the missed 2020 deadline into permanent failure | Kill both overclaims; retain the missed-deadline `CALIBRATION` |
| `TECH-DARPA-2004` | Backfill five 2005 finishers into 2004, or call a competition result market diffusion | Kill cross-year backfill and diffusion extrapolation; retain only the 2004 zero-finish result, with 2005 as uncounted follow-on context |
| `TECH-ITU-2005` | Subtract a search snippet from a differently defined statistics page | Evidence gate fails; retain `UNKNOWN/UNVERIFIED` and first close date, definition, unit, and denominator |
| `TECH-SUNSHOT-2011` | Infer a target year and achieved value from generic “cost competitive” language | Evidence gate fails; retain `UNKNOWN/UNVERIFIED`; do not count it in the technology calibration denominator |

## Method boundary returned to the project

1. **This slice yields 3 `CALIBRATION` and 3 `UNKNOWN/UNVERIFIED` records.** Technology programme targets can yield reconstructible calibration, not society-trend forecast accuracy; HGP’s target/outcome denominator is not closed and is not counted as calibration.
2. An original target and a comparable outcome are separate gates. ITU and SunShot have credible institutions and relevant topics, but publication date, metric definition, observation window, and denominator are not jointly closed, so they remain `UNKNOWN/UNVERIFIED`.
3. Deadline failure and capability failure must be separated. ISS is a deadline delay; the Moon target missed its 2020 deadline while a later plan remains active; DARPA failed in year one and met a follow-on course in year two. These cannot be compressed into one “technology forecast failure rate.”
4. This slice does not alter the historical-validation holdout rules. It did not pre-freeze a candidate pool, randomize assignment, isolate gate judging, or run same-input baselines; it must not be called pseudo-out-of-sample or genuine future out-of-sample.
5. Direct correction for future scenario work: the arrival sequence of technical capabilities must separate target mechanisms, funding and competitions, institutional deadlines, infrastructure assembly, and social diffusion. Engineering targets can be accelerated by organized effort in the short term; society-scale diffusion needs its own denominator and adoption evidence.

## Constraint ledger

- `[self-imposed]` Keep this as a bounded evidence increment rather than a complete technology history; the acceptance bar requires reconstructability, per-item kills, and explicit gaps.
- `[self-imposed]` Label every after-the-fact historical item `CALIBRATION` or `UNKNOWN/UNVERIFIED`; this prevents historical material from being reported as out-of-sample accuracy.
- `[self-imposed]` Encode programme targets, competition targets, and social diffusion separately; engineering success is not social adoption.
