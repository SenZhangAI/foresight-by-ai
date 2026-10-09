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

**这些检查立刻判否了上一轮实际发出的材料。** 在冻结提交 `0eb7474` 的树上复算 102 张卡：**28 张卡的「一句话判断」字段在去标签后被清空**——其中 **15 张只在中文失败、0 张只在英文失败、13 张中英皆空**。根因是这些卡把一句话判断同时用作 `### J-NNN · <标题>` 的标题，而隔离要求必须删除标题，于是判断正文一并被删。合并扫描对此结构性失明：空字段不泄漏任何线索。

已复核这是**既有缺陷而非本轮引入**：用提交 `66db88f` 的原版 `redact_traceback_clues`（不含本轮新增的锚点／裸文件名剥离）在同一棵树上复算，得到完全相同的 41 个被清空字段 / 28 张卡。因此上一轮公布的 bundle（`a2fdc9db…`）确实含有 28 张没有论点的记录，而当时没有任何检查会报错。

处理方式是按**同一条纳入规则**显式排除，而不是放宽检查：纳入规则原本就是「中英双卡具备六个必填保留字段」，本轮只是把它改为在**去标签之后**求值——保留一张没有论点的卡比排除它更糟。选择逻辑放在 `scripts/blind_manifest.py`，不进生成器。

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
