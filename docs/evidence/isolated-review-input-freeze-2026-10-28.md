# 隔离式全面重审输入冻结（2026-10-28）

## 中文记录

本文件只记录**重审输入已经冻结**，不记录也不暗示重审已经启动、方法有效或预测准确率。审查者收到的是去除旧来源线索与旧复核标签后的 `bundle`，而不是本仓库、manifest 或映射文件。

### 冻结指纹

- 输入源 commit：`01162c9fa6a483ef58471f4694a3e69d39f8bb35`（包含逐卡排除清单校验器的提交）
- manifest：[`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- manifest SHA-256：`077493f7f582dfa3e9ffaad9336094c9c9b87c6278f6d1e5b063fa2289580545`
- 逐卡排除清单 SHA-256：`cb10542760595e16a0b3bd706ed1c8f9d881bfeb40e436357e5c29f45d3220b0`
- bundle：[`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- bundle SHA-256：`b500a63a28e755479790b5680787ae86a47f2703685ffa56657b7ad7f4c177f6`
- 证据 JSON：[`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- source_commit 重建证据：[`source-rebuild-2026-10-28.json`](blind-review/source-rebuild-2026-10-28.json)，记录了从 `01162c9...` checkout 后逐字节 manifest、逐卡清单和 `exclusion_cards_sha256` 均匹配
- `bundle-prepared` 的 `verification` 还记录了本轮 `python3 scripts/check.py`（190 文件、6354 内部链接、双语各 123 卡、21 链）和 blind bundle `SELF_TEST_PASSED`；这些是结构/隔离测试，不是方法有效性或预测准确率证明
- seed SHA-256（seed 本身不入仓库）：`fee92edc96b339743a3b0f0e05794bc64e5e5fd5f02bd6a296cc34b975a363d`
- 密封映射 SHA-256（映射保存在仓库外，不随 bundle 发布）：`c2c8e767ab40320beac5da44b65cf6de18272bd6aeb57163a2bd30d38810a1bd`
- 纳入：29 张中英成对判断卡；`R-01`–`R-29`
- 候选总数：218；排除：189
- 保留字段（中英同义）：`judgment`、`audience`、`reasoning_chain`、`time_window`、`falsifier`、`leading_indicator`
- 去除内容：旧卡片编号、标题回溯线索、来源路径、状态／置信度／外部对照元数据、依赖关系、普及闸及其旧结论标签、编号约束标签与 `EXT-NN` 来源编号；判断字段本身保留，以便重审者能判断原主张。

### 纳入与排除

纳入规则和逐项文件哈希以 manifest 为准：当前台账中同时存在中英文版本、六个必填字段在去标签及旧复核标签清理后仍可读的卡片。排除项只有两桶：

1. `docs/evidence/legacy-ledger-migration.md` 中的 95 条历史迁移快照：它们重复当前判断，不构成第二套判断全集；manifest 以 `legacy:J-NNN` 稳定 ID 逐卡列出，并保留来源文件与标题。
2. 94 张当前台账卡片：去除旧复核元结论后，至少一个必填字段（manifest 逐卡列出，首个为 `audience`）不再有可读内容，无法交给 reviewer 判断；每张卡的稳定 ID、逐卡原因、双语来源路径和标题均写入 manifest，不再只依赖 stdout。

`exclusions[*].count` 必须等于其 `cards` 列表长度；逐卡排除清单的 SHA-256 为 `exclusion_cards_sha256`，并由生成器重新计算。纳入与排除 ID 集合不得重叠。给定冻结 `source_commit` 重建 manifest 时，这些列表和哈希应一致。

### 结构证据与边界

`bundle-prepared-2026-10-28-isolated.json` 记录了独立运行两次、manifest 顺序无关、`git archive HEAD` 字节一致、双语字段／路径／计数、索引顺序、跨语言卡片集合、映射可达性和合并泄漏扫描均通过。映射不在 bundle 中；它只用于冻结 `R-NN → J-NNN` 对应关系，并以外部密封文件保存。

这些检查只证明输入包可重建且结构边界成立。它们**不**证明 reviewer 已运行，不证明来源隔离在密码学意义上成立，不证明方法有效，也不构成预测准确率。

## English record

This file freezes the **input to a future isolated re-review**. It does not say that the re-review has started or finished, and it is not evidence of method validity or prediction accuracy. A reviewer receives the de-labelled bundle, not the repository, manifest, or mapping.

### Frozen fingerprints

- Source commit: `01162c9fa6a483ef58471f4694a3e69d39f8bb35` (the commit containing the per-card exclusion validator)
- Manifest: [`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- Manifest SHA-256: `077493f7f582dfa3e9ffaad9336094c9c9b87c6278f6d1e5b063fa2289580545`
- Per-card exclusion-list SHA-256: `cb10542760595e16a0b3bd706ed1c8f9d881bfeb40e436357e5c29f45d3220b0`
- Bundle: [`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- Bundle SHA-256: `b500a63a28e755479790b5680787ae86a47f2703685ffa56657b7ad7f4c177f6`
- Evidence JSON: [`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- Source-commit rebuild evidence: [`source-rebuild-2026-10-28.json`](blind-review/source-rebuild-2026-10-28.json), which records byte-identical manifest, per-card list, and `exclusion_cards_sha256` after checking out `01162c9...`
- The `verification` object in `bundle-prepared` also records this round's `python3 scripts/check.py` (190 files, 6354 internal links, 123 cards per language, 21 chains) and blind-bundle `SELF_TEST_PASSED`; these are structural/isolation tests, not evidence of method validity or prediction accuracy.
- Seed SHA-256 (the seed itself is not committed): `fee92edc96b339743a3b0f0e05794bc64e5e5fd5f02bd6a296cc34b975a363d6`
- Sealed mapping SHA-256 (stored outside the repository): `c2c8e767ab40320beac5da44b65cf6de18272bd6aeb57163a2bd30d38810a1bd`
- Included: 29 bilingual card pairs, numbered locally as `R-01`–`R-29`
- Candidate total: 218; excluded: 189
- Retained fields: `judgment`, `audience`, `reasoning_chain`, `time_window`, `falsifier`, `leading_indicator`
- Removed: legacy identifiers, title/source traceback clues, paths, status/confidence/external-comparison metadata, dependency references, diffusion-gate labels and conclusions, numbered constraint labels, and `EXT-NN` source identifiers. The judgment field itself remains so the reviewer can assess the original claim.

### Inclusion and exclusions

The manifest is authoritative for the inclusion rule and every bilingual source hash: include a current card only when both language projections retain readable content in all six required fields after de-labelling and removal of prior-review vocabulary. There are two exclusion buckets:

1. The 95 historical migration snapshots in `docs/evidence/legacy-ledger-migration.md`, which duplicate current judgments and are not a second judgment set; the manifest assigns each a stable `legacy:J-NNN` ID and preserves its source file and heading.
2. 94 current ledger cards whose required fields no longer have readable content after prior-review metadata is removed (the manifest lists each card and its first missing field, beginning with `audience`); each stable ID, per-card reason, bilingual source paths, and heading is persisted in the manifest rather than only printed to stdout.

Each `exclusions[*].count` must equal its `cards` list length. The per-card exclusion-list SHA-256 is stored as `exclusion_cards_sha256` and recomputed by the generator; included and excluded ID sets must be disjoint. Rebuilding from the frozen `source_commit` must reproduce the same lists and digest.

### Structural evidence and boundary

`bundle-prepared-2026-10-28-isolated.json` records two independent runs, manifest-order independence, byte identity from `git archive HEAD`, bilingual field/path/count checks, index ordering, cross-language card-set consistency, mapping reachability, and the merged leakage scan. The mapping is not in the bundle; it only fixes the `R-NN → J-NNN` correspondence and is sealed outside the repository.

These checks establish only that the input package is reproducible and structurally bounded. They do **not** show that a reviewer ran, do not provide cryptographic anonymity, do not validate the method, and do not constitute prediction accuracy.
