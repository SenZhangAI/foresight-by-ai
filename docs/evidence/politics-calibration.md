# 政治预测失准校准：可保存证据包（2026-09）

> **证据等级：`CALIBRATION`，不是样本外准确率。** 本文件只用于在已知结果的历史材料上识别方法规则的失效边界；不能由它推出通用命中率，也不生成未来预测卡。
>
> **本文件的四案计数由候选登记表派生。** P-01–P-06 是固定候选登记；只有状态为 `qualified` 的案例计入四案。任何候选都不得为了维持数量而删除。每个 `qualified` 案例同时提供仓库内可读取的 `prediction_artifact` 与 `outcome_artifact` 原始字节副本、身份链、来源日期、抓取日期、HTTP/文件状态、原始字节哈希和摘录定位／哈希。

## 证据包清单

- **Canonical manifest hash：** `80ec916729e3b669fe7d9b1da66c254be70b9747c275ce958f9ad3bc20723a63`（manifest 内容见文末；版本标识 `politics-calibration-2026-09-v2`）
- **Artifact root：** [`politics-artifacts/`](politics-artifacts/)
- **抓取日期：** 2026-09-29（UTC 日期；来源文件本身的发布日期另列）
- HTML 副本保留原始响应字节；PDF/TXT 副本保留下载文件或文本文件字节。摘录是副本的派生物，不是原件替代品。
- `raw_bytes_sha256` 对应仓库内副本本身；`excerpt_sha256` 对应 `byte_offset_start` 至 `byte_offset_end`（结束位置不含）之间的字节。读者可用 `dd` 或脚本按定位复算。

## 固定候选登记（不得从文件中删除）

| case_id | 候选 | status | 计数 | 原因 |
|---|---|---|---:|---|
| P-01 | 2016 英国脱欧公投临场民调 | `qualified` | 1 | 预测与结果同为公投方向／百分比；两份 HTML 原始副本可读，日期先后和摘录可重建。 |
| P-02 | 2017 英国大选多数政府预测 | `qualified` | 1 | 预测是多数政府制度结果；结果原件明确为悬浮议会；不能把席位多数与投票份额互换。 |
| P-03 | 2021 阿富汗撤军后全国接管预测 | `unverified` | 0 | 预测副本已保存，但本轮无法把 CRS 结果原件保存到仓库；仅有 URL／搜索摘要不能计入。 |
| P-04 | FOMC 对 2008 年实际 GDP 的预测 | `qualified` | 1 | 预测与结果均为 2008 Q4/Q4 实际 GDP 增长，单位为百分比；两份 HTML 原始副本可读。 |
| P-05 | 脱欧后的英国 GDP 反事实冲击预测 | `unverified` | 0 | 预测是“相对留欧基准的两年后水平差”；保存的结果是实际年度增长率，缺少同一反事实基准序列，不能伪装成同口径。 |
| P-06 | 伊拉克 WMD 库存预测 | `qualified` | 1 | 战前预测与战后 ISG 结果都直接涉及 stockpiles；PDF/TXT 原始副本及摘录定位可重建。 |

**合格案例数（由上表 `status=qualified` 派生）：4。** `P-03` 与 `P-05` 的存在、编号、状态和原因必须保留；它们不是失败的计数填充物。

## 统一字段与分类规则

每案必须记录：`forecast_metric`、`outcome_metric`、`unit`、`population/base`、`forecast_date`、`outcome_date`、`observation_window`、`threshold_or_comparison_rule`，且只使用一个主分类：`direction`、`timing`、`scale`、`mechanism`。如果预测与结果不是完全同字段，必须写出 `derived/comparable_with_rule`；主题相近不等于同口径。

## Qualified cases

### P-01 · 英国脱欧公投：YouGov 临场民调把方向判反

- **预测主体／原件：** YouGov，*YouGov on the day poll: Remain 52%, Leave 48%*，发布日期 2016-06-23。副本：[`prediction.html`](politics-artifacts/P-01/prediction.html)，媒体类型 `text/html`，抓取 HTTP `200`，`raw_bytes_sha256=b7167d06dafb7f1f52e7939d6ea2499798c661d80cadb072490a5ddabe04ad1f`，来源 URL：<https://yougov.com/en-gb/articles/15778-yougov-day-poll>。
- **预测摘录：** `Remain are on 52% with Leave on 48%.`；原始副本字节区间 `[231946,231986)`；`excerpt_sha256=64bbba25935acc518678156eab4ec408dd013acd3893422517686651efcaf643`。
- **结果主体／原件：** UK Prime Minister’s Office, *The result of the EU Referendum: Ambassador's Statement*，发布日期 2016-06-24。副本：[`outcome.html`](politics-artifacts/P-01/outcome.html)，`text/html`，抓取 HTTP `200`，`raw_bytes_sha256=d774df6ad02ba3c0ec6420f760c279ead9b88f12539f847f8070b5ee3c71e8ad`，来源 URL：<https://www.gov.uk/government/news/the-result-of-the-eu-referendum-ambassadors-statement>。
- **结果摘录：** `their decision to leave the European Union is respected.`；副本包含 GOV.UK 的原始 JSON/HTML 响应；区间 `[4093,4389)`（该段为 JSON 转义 HTML，区间可直接复算）；`excerpt_sha256=693ba6f3814ba35f901e894c9a30d5123736718f46f3ea956df2bde05f434015`。
- **forecast_metric：** Leave/Remain 有效投票比例及第一名方向；**outcome_metric：** Leave/Remain 公投结果方向；**unit：** percent／ordinal winner；**population/base：** UK EU membership referendum voters；**forecast_date：** 2016-06-23；**outcome_date：** 2016-06-24；**observation_window：** 投票日发布至结果公布；**threshold_or_comparison_rule：** 预测把 Remain 排第一，官方结果把 Leave 排第一；**derived/comparable_with_rule：** 同一公投问题，比较第一名方向，不把百分比差异另算 `scale`。
- **唯一分类：** `direction`。

### P-02 · 2017 英国大选：多数政府预测失准

- **预测主体／原件：** YouGov，*Final call poll: Tories lead by seven points and set to increase majority*，发布日期 2017-06-07。副本：[`prediction.html`](politics-artifacts/P-02/prediction.html)，`text/html`，HTTP `200`，`raw_bytes_sha256=e47041289e141fcc3b013e67cddf112fd1b4d2b67d340d3f3ebdb5ed9d64be26`，来源 URL：<https://yougov.com/en-gb/articles/18339-final-call-poll-tories-seven-points-and-set-increa>。
- **预测摘录：** `increased Conservative majority in the Commons.`；区间 `[360124,360175)`；`excerpt_sha256=39ebee32d1b50ba3ce97aa1d83aec05143407ac09d58ffaee168ca7bbda71756`。
- **结果主体／原件：** House of Commons Library，*General Election 2017: results and analysis*，发布日期 2017-06-09。副本：[`outcome.html`](politics-artifacts/P-02/outcome.html)，`text/html`，HTTP `200`，`raw_bytes_sha256=555b715c8417cb1c717f26ecd5033fef4cf7ef89fa6aaa50943c31128fcbb5d1`，来源 URL：<https://commonslibrary.parliament.uk/research-briefings/cbp-7979/>。
- **结果摘录：** `The 2017 General Election resulted in a hung Parliament, with no party winning an overall majority.`；同一原始段同时给出 Conservative 317 seats / 42.3% vote、Labour 262 seats / 40.0%；区间 `[46194,46576)`；`excerpt_sha256=f0ec768ff5d77a54adab4176db5860a943de290ddd8eeff661a6c34c67a3bd38`。
- **forecast_metric：** 是否形成 Conservative majority government；**outcome_metric：** 是否有任何党派取得下院整体多数；**unit：** binary institutional outcome；**population/base：** UK House of Commons election；**forecast_date：** 2017-06-07；**outcome_date：** 2017-06-08；**observation_window：** 选前 final call 至选举结果；**threshold_or_comparison_rule：** `increased Conservative majority` 与 `no party winning an overall majority` 互为否定结果；**derived/comparable_with_rule：** 只比较制度结果，不用 42% 投票份额替换席位多数，也不把席位与投票份额混算。
- **唯一分类：** `direction`。

### P-04 · 美国 2008 年经济增长：FOMC 预测正增长，结果收缩

- **预测主体／原件：** Federal Reserve Board，*Summary of Economic Projections, October 30–31, 2007*，发布日期 2007-10-31。副本：[`prediction.html`](politics-artifacts/P-04/prediction.html)，`text/html`，HTTP `200`，`raw_bytes_sha256=cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`，来源 URL：<https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>。
- **预测摘录：** `central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent`；区间 `[8275,8558)`；`excerpt_sha256=d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`。
- **结果主体／原件：** Bureau of Economic Analysis，*Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*，发布日期 2009-03-27。副本：[`outcome.html`](politics-artifacts/P-04/outcome.html)，`text/html`，HTTP `200`，`raw_bytes_sha256=25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`，来源 URL：<https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>。
- **结果摘录：** `During 2008 ... real GDP decreased 0.8 percent.`；区间 `[33844,34200)`；`excerpt_sha256=484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`。
- **forecast_metric：** US real GDP growth, Q4/Q4；**outcome_metric：** US real GDP growth, Q4/Q4；**unit：** percent；**population/base：** United States real GDP, fourth-quarter-to-fourth-quarter；**forecast_date：** 2007-10-31；**outcome_date：** 2009-03-27 release of final estimate；**observation_window：** 2008 Q4/Q4；**threshold_or_comparison_rule：** 预测区间全为正（1.8–2.5%），最终同口径值为 −0.8%；**derived/comparable_with_rule：** 预测脚注和结果原件均指 Q4/Q4，不用年度平均值替代。
- **唯一分类：** `direction`。

### P-06 · 伊拉克 WMD：战前库存断言与战后调查结果相反

- **预测主体／原件：** US Intelligence Community，*Iraq’s Weapons of Mass Destruction Programs*，September 2002。副本：[`prediction.pdf`](politics-artifacts/P-06/prediction.pdf)，媒体类型 `application/pdf`，文件状态 `200`，`raw_bytes_sha256=336043a37c995baa80e4b01c0d9310fb4450fab886d2ffbc7cc785338c9b7b6a`；可读文本派生副本：[`prediction.txt`](politics-artifacts/P-06/prediction.txt)，`text/plain`，`raw_bytes_sha256=5df02216a31f30d9aafee76933993895b0c6df3a618b9eb2a7d4a668426b56e1`，来源档案 URL：<https://archive.org/details/cia-readingroom-document-0005479946>。
- **预测摘录：** `Iraq has stockpiles of CW and BW agents and munitions`；TXT 副本字节区间 `[549,634)`；`excerpt_sha256=b5f5a0607f2cc52ac217bac6ff76d2ff0ee4660fec082371598d5dee2dbcc64b`。PDF 是扫描件；TXT 是同一档案的 OCR/文本派生物，不能冒充 PDF 字节哈希。
- **结果主体／原件：** Charles A. Duelfer / Iraq Survey Group，*The Iraq Survey Group and the Search for WMD*，最终报告于 2004-09-30 发布；本仓库副本来自 CIA Reading Room 的公开档案条目（档案发布／解密元数据日期 2018-11-20），报告正文讨论战后搜索。副本：[`outcome.pdf`](politics-artifacts/P-06/outcome.pdf)，`application/pdf`，文件状态 `200`，`raw_bytes_sha256=83d697983426fbccc5e858bde29704261e8d3ad308b3df86c4c4ce50701d80f0`；可读文本派生副本：[`outcome.txt`](politics-artifacts/P-06/outcome.txt)，`text/plain`，`raw_bytes_sha256=83bd2b6c8198bde45999392d4c06b55d9401a94cc7d38b0a48477dff7262f6c5`，来源档案 URL：<https://archive.org/details/cia-readingroom-document-05618006>。
- **结果摘录：** `ISG teams found no stockpiles of weapons`；TXT 副本字节区间 `[11805,12061)`；`excerpt_sha256=c6f5e144394c769dfb79cebd8ac0bbb8445af77d364d3f19ba26f627e6dc077c`。该摘录保留 OCR 换行和断词；PDF 是结果原始文件，TXT 仅用于稳定文本定位。
- **forecast_metric：** Iraq stockpiles of chemical/biological warfare agents and munitions；**outcome_metric：** ISG 搜索发现的 WMD weapon stockpiles；**unit：** binary existence claim；**population/base：** Iraq WMD stockpiles；**forecast_date：** 2002-09-01（报告月份）；**outcome_date：** 2004-09-30（Duelfer Report 发布；仓库副本的 CIA 档案元数据日期为 2018-11-20）；**observation_window：** 战前评估至 ISG 战后搜索报告；**threshold_or_comparison_rule：** 预测断言存在库存，结果报告没有发现库存；**derived/comparable_with_rule：** 两者都比较库存是否存在，不把“能力／意图／活动”替换成库存。
- **唯一分类：** `direction`。

## 未验证候选的停止条件

- **P-03：** 必须把 CRS/官方结果原始文件保存进仓库，记录媒体类型、发布者、标题／编号、日期、文件状态、原始字节哈希和摘录定位；仅有搜索摘要、URL 或手写摘录不够。结果还必须明确“全国性接管”而不是把“进入首都”偷换成全国控制。
- **P-05：** 必须保存与预测相同的“相对留欧反事实 GDP 水平”结果序列，或者明确、可重建的同一基准映射；实际年度增长率不能直接替代两年后相对反事实水平。

## 方法边界

四个合格案例都来自结果已知后的历史选择，因此是 `CALIBRATION`。它们可以削弱“临近结果方向稳定”“选票份额可直接推出制度结果”“平滑基线能覆盖尾部传导”“能力／意图等同于库存”等规则，但不能证明跨领域预测准确率。真实样本外证据仍只能来自事前登记、未来揭晓的判断卡。

## Manifest

下列 manifest 是中英文镜像共享的身份索引；英文镜像必须使用相同的 case_id、状态、artifact 路径和哈希，不得独立改数：

```yaml
manifest_id: politics-calibration-2026-09-v2
candidate_ids: [P-01, P-02, P-03, P-04, P-05, P-06]
qualified_case_ids: [P-01, P-02, P-04, P-06]
unverified_case_ids: [P-03, P-05]
raw_artifacts_root: docs/evidence/politics-artifacts
count_rule: count rows whose status is exactly qualified
calibration_only: true
```
