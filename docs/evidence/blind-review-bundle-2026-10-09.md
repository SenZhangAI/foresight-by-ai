# 盲判材料准备证据：2026-10-09

## 结论边界

本记录的交付状态是 **`BUNDLE_PREPARED`**，不是重审结果。它证明冻结输入已经被转成去标签、重编号和乱序的材料；**尚无可核验的重审启动证据**。没有独立 reviewer 的原始输出和运行时间，因此不得声称重审已启动、执行或完成，也不得把本记录升级为方法有效性、预测准确率或历史 holdout 证据。

去标签材料只对拿不到本仓库的重审者成立，不是密码学隔离：保留字段仍是判断正文的文字。若同一人同时持有 bundle 和公开仓库，仍可能靠内容比对恢复对应关系。因此 `bundle.json`、原始 seed 和 `R-NN → J-NNN` 映射均不进入 git；本次证据只保留 seed 哈希、输入哈希和输出哈希。

## 本轮修正：按语言与索引一致性检查，以及它发现的缺陷

上一轮（提交 `66db88f`）的生成器把中英两份记录**合并成一个字符串**做泄漏扫描。独立核验指出，验收所要求的「中英分别执行语义、路径、索引和映射可达性检查」并未实现。本轮补齐六个独立检查分支，每条都会点名语言与 `R-NN`：

| 分支 | 判什么 | 为什么合并扫描做不到 |
|---|---|---|
| `lang_semantic` | 单一语言投影的保留字段白名单、必填字段是否仍有可读内容 | 合并扫描找的是「出现了禁止文本」；字段**被清空或缺失**时它什么也看不到 |
| `lang_path` | 单一语言投影里残留的标题锚点与裸文件名 | `LINK_RE` 要方括号、`URL_RE` 要协议头、`PATH_RE` 要目录前缀；`#锚点` 与 `02.md` 三者全不匹配 |
| `lang_count` | 单一语言的记录数与冻结 manifest 卡数 | 旧实现的 `zh_count`／`en_count` 是同一循环里各加一，恒等，不可能判否 |
| `index_order` | 编号必须是 `R-01…R-NN` 无缺号，且该顺序等于按 seed 重算的内容序 | 这是序列的性质，不属于任何单条记录 |
| `cross_language` | 中英逻辑卡集合相同，且每条记录两种语言承载相同字段含义 | 同上，合并后看不出是哪一侧缺字段 |
| `mapping_reachability` | 每个 `R-NN` 必须唯一对应一张来源卡，反之亦然 | 两条记录正文相同时映射虽能写出但不可用，扫描不出任何泄漏 |

**这些检查立刻判否了上一轮实际发出的材料。** 在冻结提交 `0eb7474` 的树上复算 102 张卡：**28 张卡的「一句话判断」字段在去标签后被清空**——其中 **15 张只在中文失败、0 张只在英文失败、13 张中英皆空**。根因是这些卡把一句话判断同时用作 `### J-NNN · <标题>` 的标题，而当时的去标签把标题一律删除，于是判断正文一并被删。合并扫描对此结构性失明：空字段不泄漏任何线索。

已复核这是**既有缺陷而非本轮引入**：用提交 `66db88f` 的原版 `redact_traceback_clues`（不含本轮新增的锚点／裸文件名剥离）在同一棵树上复算，得到完全相同的 41 个被清空字段 / 28 张卡。因此上一轮公布的 bundle（`a2fdc9db…`）确实含有 28 张没有论点的记录，而当时没有任何检查会报错。

> ⚠ **下面这段「显式排除」的处理方式已被取代，保留只为留痕。** 它与本项目验收所要求的「bundle 只保留原始主张」「每条既有判断给出结论」相抵触：那 28 张卡确有一句话判断，只是与卡片标题同文而被一并删除；排除一张有判断的卡，等于让它永远拿不到结论。现行处理方式见本文件[最后一节「第二轮」](#第二轮改为修掉去标签缺陷取代上面的排除决定)。

~~处理方式是按**同一条纳入规则**显式排除，而不是放宽检查：纳入规则原本就是「中英双卡具备六个必填保留字段」，本轮只是把它改为在**去标签之后**求值——保留一张没有论点的卡比排除它更糟。选择逻辑放在 `scripts/blind_manifest.py`，不进生成器。~~

## 冻结输入

- 冻结器：`scripts/blind_manifest.py`（选择逻辑在此，生成器只负责「冻结输入 → bundle」）
- manifest：`docs/evidence/blind-review/manifest-2026-10-09.json`
- `source_commit`：`b0e025a40037058ee7c56678705cb48b447db64c`
- 纳入规则：中英文当前台账卡均具备 `judgment`、`audience`、`reasoning_chain`、`time_window`、`falsifier`、`leading_indicator` 六个必填保留字段，**且去标签后每一项仍有可读内容**。
- 覆盖：候选 197；纳入 74；排除 123 = 95 迁移快照 + 28 去标签后失去论点的卡。
- manifest SHA-256：`404acac527338ca8ef11b3d3a775c22af9fe78d6a26ff40632f5e3220f723107`

```sh
# 实际执行的冻结命令
python3 scripts/blind_manifest.py --repo . \
  --out docs/evidence/blind-review/manifest-2026-10-09.json
# exit code: 0
# source_commit=b0e025a40037058ee7c56678705cb48b447db64c
# candidate=197 included=74 excluded=123
```

## 运行记录

生产运行使用仓库外临时目录；seed 由 `secrets.token_hex(32)` 生成，原文不记录，只记录哈希 `080c2d1cc05dfd1b4f6e333d97647465fba3b4418ebf7016e97ba7c2a0cfc48f`。

```sh
# 实际执行的命令（seed 原文只存在于本地 shell 变量）
tmpdir=$(mktemp -d /tmp/foresight-blind-bundle.XXXXXX)
seed=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
python3 scripts/blind_bundle.py \
  --repo . \
  --manifest docs/evidence/blind-review/manifest-2026-10-09.json \
  --output-dir "$tmpdir/bundle" \
  --mapping-out "$tmpdir/mapping.json" \
  --seed "$seed" \
  --verify-determinism \
  --evidence docs/evidence/blind-review/bundle-prepared-2026-10-09.json
# exit code: 0
```

生产结果：

- 状态：`BUNDLE_PREPARED`
- bundle SHA-256：`7bfc5ffcdf9cdf37a81c0d7024017c58010c453c66c340e655b2a210d3418b3d`
- 记录数：74；中文 74；英文 74
- 按语言检查：中、英各自的 `semantic_fields`／`path_and_anchor`／`count_against_manifest` 均 `passed`（见证据 JSON 的 `per_language_checks`，分语言分别记录）。
- 结构检查：`index_order`、`cross_language_card_set_and_field_meanings`、`mapping_reachability`、`merged_leakage_scan` 均 `passed`。
- 两个独立临时目录：逐字节一致；两次哈希均为上述 bundle 哈希。
- 反转 manifest 卡片顺序：输出逐字节一致。
- 普通 checkout 与 `git archive HEAD`：`archive_same_bytes=true`。
- 不同 seed：`seed_changes_assignment=true`。
- mapping：仅写入仓库外临时目录；bundle 不含 mapping，生成器不读取 mapping。

## 自测与边界攻击

`python3 scripts/blind_bundle.py --self-test` 退出码为 0，输出 `SELF_TEST_PASSED`：fixture 4 张卡，**18 个负例、18 个 mutation**（上一轮为 9／9）。

既有 9 个合并扫描负例全部回归通过：旧编号、status、修订理由、普及闸、原文件路径、原始标题、依赖标识、同形旧编号、跨行拆分旧编号；每个非零退出并点名 `R-NN`，逐个禁用对应分支后恰好放行。

本轮新增 9 个负例，每个都先确认**由自己的分支报错**，再单独禁用该分支确认缺陷得以通过——因此没有一个是靠已有合并扫描间接报错的：

| 负例 | 分支 | 实际报错（节选） |
|---|---|---|
| `zh_required_field_emptied` | `lang_semantic` | `R-02 (zh): required field 'falsifier' carries no readable content after de-labelling` |
| `en_required_field_emptied` | `lang_semantic` | `R-01 (en): required field 'falsifier' carries no readable content after de-labelling` |
| `zh_bare_heading_anchor` | `lang_path` | `R-02 (zh): field 'leading_indicator' keeps a heading anchor … #锚点二` |
| `en_bare_source_filename` | `lang_path` | `R-02 (en): field 'leading_indicator' keeps a bare source file name: 02.md` |
| `en_field_meaning_dropped` | `cross_language` | `R-02: … (zh-only: ['opposing_mechanism']; en-only: -)` |
| `duplicate_record_body` | `mapping_reachability` | `R-01 = R-02 share one record body, so neither resolves to a single source card` |
| `index_order_permuted` | `index_order` | `index/order inconsistency at position 1: R-01 sits where R-02 belongs …` |
| `language_count_short` | `lang_count` | `zh projection carries 3 records but the frozen manifest pins 4 cards` |
| `card_set_unpaired` | `cross_language` | `the zh and en logical card sets differ: 1 card(s) only in zh, 0 only in en` |

前两例是**只在一种语言失败**的直接证据：自测断言中文失败的消息必须含 `(zh)` 且不含 `(en)`，英文失败的反之。若两种语言仍被合并判定，这对断言无法同时成立。

后三例（`index_order_permuted`、`language_count_short`、`card_set_unpaired`）由测试专用注入点触发，因为**任何合法的冻结 manifest 都无法产生这些缺陷**——它们是生成器内部不变量，注入是唯一能证明该闸有牙的办法。该注入点不在 CLI 上暴露。

另外已验证：`refused_run_exit_code=1`（拒绝路径与进程退出码是同一件事）、`mapping_pairs_match_bundle=true`、manifest 哈希闸、mapping 仓内写入被拒、`archive_same_bytes=true`、`seed_changes_assignment=true`。

这些全是结构与隔离证据。它们不证明历史规则有效、不证明预测准确、不证明重审已经开始，也不证明对同时拥有 bundle 和仓库的人具有密码学不可逆性。

## 检查记录

- `npm run check`：退出码 0；输出为 `all automated pre-publication checks pass`。这只是机械结构证据，不是方法有效性或预测准确率证据。
- `git diff --check`：退出码 0，无输出。
- 提交内容：生成器、冻结器、重新冻结的 manifest、哈希证据、双语 protocol 与本证据包；bundle、seed、mapping 不进入仓库。

## 第二轮：改为修掉去标签缺陷（取代上面的排除决定）

上面那条「把 28 张卡显式排除」的处理方式已被取代。取代它的理由不是口味问题，是它违反本项目自己的验收条文：「bundle 只保留原始主张」要求保留主张，「每条既有判断给出保留、REVISED、FALSIFIED 或明确降级结论」要求每条都有结论——排除一张确实写有判断的卡，两条都做不到。

**用一手诊断把猜测换成了事实。** 用仓库自己的 `blind_bundle` 与 `blind_manifest` 模块在真实台账上跑逐卡逐字段诊断（即上面那种「一刀切删标题」的行为），28 条被排除卡的死因分布是 `Counter({'judgment': 41})`：**41 个 (卡, 语言) 失败实例全部且仅落在 `judgment` 字段**，其余五个必填字段（受众、推理链、时间窗、证伪条件、领先指标）无一受损。所以这不是「这些卡字段不全」，而是「去标签把标题删得太宽」。

**窄豁免，且对称。** 现在只有**本卡自己的标题**、只在**本卡自己的 `judgment` 字段内**可以留存。别卡的标题出现在任何字段、本卡的标题出现在其他任何字段，仍一律判否——那仍然是可反查旧编号的线索。代价明写而非隐藏：主张原文因此可被同时持有 bundle 与公开仓库的人反查，但这与推理链、时间窗、证伪条件已经逐字出现在 bundle 里是同一级的暴露；隔离本来就是流程隔离（重审者按角色被禁入仓库），不是密码学隔离。

**豁免是载重的，由三个用例守住**（都在 `--self-test` 内）：

| 用例 | 类型 | 它证明什么 |
|---|---|---|
| 主张 == 本卡标题的卡必须纳入 | 回归正例 | 双语逐字保留，`blank_claim_fields: 0`；若豁免失效此例立刻失败 |
| `foreign_title_in_claim` | 结构注入负例 | 别卡标题注入 `judgment` 必须由 `title` 分支判否，且只禁用该分支时必须放行——证明不是靠别的分支间接拦住 |
| `drop_claim_exemption` | TEST_FAULT（撤回豁免） | 撤回豁免后主张再次被清空，并且只由 `lang_semantic` 报告——证明豁免确实是那 41 个字段存活的原因 |

`python3 scripts/blind_bundle.py --self-test` 当前为 `SELF_TEST_PASSED`、`negative_cases=20`、`mutation_cases=20`、`regression_cases=1`、`refused_run_exit_code=1`、`mapping_pairs_match_bundle=true`。

### 重新冻结的输入与 bundle

```sh
# 冻结（逐字）
python3 scripts/blind_manifest.py --repo . \
  --out docs/evidence/blind-review/manifest-2026-10-09b.json
# candidate=197 included=102 excluded=95

# 生产（bundle / mapping / seed 全在仓库外临时目录）
python3 scripts/blind_bundle.py --repo . \
  --manifest docs/evidence/blind-review/manifest-2026-10-09b.json \
  --output-dir "$tmpdir/bundle" --mapping-out "$tmpdir/mapping.json" \
  --seed "$seed" --verify-determinism \
  --evidence docs/evidence/blind-review/bundle-prepared-2026-10-09b.json
```

- `source_commit`：`98fd95701da3bacef4d43e304db6b82e3f4d3b9b`
- manifest SHA-256：`181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1`
- 覆盖：候选 197；纳入 **102**；排除 **95**（只剩历史迁移快照，`claim_lost` 排除桶已空）
- bundle SHA-256：`e15b0e36d427432aeddb436f6fe205f53af691c04c0a58083b51647e34f43360`；记录数 102（中 102 / 英 102）；**双语 judgment 字段空值数 0**
- seed SHA-256：`a18ea18e3a88ffd865b44d3ca93555a7ac60f91f2e8cc3a4e22df6f5b2c775e0`（原文不入仓库）
- 确定性：`same_bytes=true`、`order_independent=true`、`archive_same_bytes=true`、`seed_changes_assignment=true`
- 分语言检查：中、英各自 `semantic_fields`／`path_and_anchor`／`count_against_manifest` 均 `passed`
- 结构检查：`index_order`、`cross_language_card_set_and_field_meanings`、`mapping_reachability`、`merged_leakage_scan` 均 `passed`

**旧轮证据一律未被覆盖**：`manifest-2026-10-09.json`（纳入 74）与 `bundle-prepared-2026-10-09.json` 原样保留，第二轮用 `-b` 新文件名。这意味着仓库里现在有三套冻结输入（`7c06add3…` 102 条、`404acac5…` 74 条、`181b35ec…` 102 条），读者必须按本节的轮次上下文区分，**不得把三者的计数混用**。

### 这一节不证明什么

它不证明预测准确、不证明方法有效、不证明隔离是密码学的。它只证明：去标签不再吃掉主张，而且这件事由一个会在豁免被撤回时失败的测试守着。28 张卡在这份 bundle 上的重判结果见[隔离盲判复审第 11 节](blind-review-reaudit-2026-10-09.md#11-第二轮28-张卡在修复后的-bundle-上的重判)。
