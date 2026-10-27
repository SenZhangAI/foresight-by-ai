# 隔离式全面重审输入冻结（2026-10-28）

## 中文记录

本文件只记录**重审输入已经冻结**，不记录也不暗示重审已经启动、方法有效或预测准确率。审查者收到的是去除旧来源线索与旧复核标签后的 `bundle`，而不是本仓库、manifest 或映射文件。

### 冻结指纹

- 输入源 commit：`018977bce046743036602ea99f63ea2dc18f2ef8`（清理器变更所在提交）
- manifest：[`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- manifest SHA-256：`0814d828c4694ecb8e7417f7ef8600eb2cebcc27a779f8ff2660584a819233a1`
- bundle：[`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- bundle SHA-256：`aaf60a038b487087f55db0c807427bfc3b4acc0cd8f7387e2218304f966d7f31`
- 证据 JSON：[`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- seed SHA-256（seed 本身不入仓库）：`266195e5d9223267726d6eedc3a3d561c3e4540448ca90590dd928e5cd1dc98a`
- 密封映射 SHA-256（映射保存在仓库外，不随 bundle 发布）：`bbd380d401266eb0e20940b535e4dd52059a74e4c13ab6b9ba4e52f8c045f136`
- 纳入：35 张中英成对判断卡；`R-01`–`R-35`
- 候选总数：218；排除：183
- 保留字段（中英同义）：`judgment`、`audience`、`reasoning_chain`、`time_window`、`falsifier`、`leading_indicator`
- 去除内容：旧卡片编号、标题回溯线索、来源路径、状态／置信度／外部对照元数据、依赖关系、普及闸及其旧结论标签、编号约束标签与 `EXT-NN` 来源编号；判断字段本身保留，以便重审者能判断原主张。

### 纳入与排除

纳入规则和逐项文件哈希以 manifest 为准：当前台账中同时存在中英文版本、六个必填字段在去标签及旧复核标签清理后仍可读的卡片。排除项只有两桶：

1. `docs/evidence/legacy-ledger-migration.md` 中的 95 条历史迁移快照：它们重复当前判断，不构成第二套判断全集。
2. 88 张当前台账卡片：去除旧复核元结论后，至少一个必填字段（manifest 逐卡列出，首个为 `audience`）不再有可读内容，无法交给 reviewer 判断；这些卡没有被静默丢弃，逐卡原因已写入 manifest。

卡片集合、双语路径、源文件哈希、纳入理由与排除桶均被冻结；后续改变必须另起 manifest 和 commit，不能覆盖本指纹。

### 结构证据与边界

`bundle-prepared-2026-10-28-isolated.json` 记录了独立运行两次、manifest 顺序无关、`git archive HEAD` 字节一致、双语字段／路径／计数、索引顺序、跨语言卡片集合、映射可达性和合并泄漏扫描均通过。映射不在 bundle 中；它只用于冻结 `R-NN → J-NNN` 对应关系，并以外部密封文件保存。

这些检查只证明输入包可重建且结构边界成立。它们**不**证明 reviewer 已运行，不证明来源隔离在密码学意义上成立，不证明方法有效，也不构成预测准确率。

## English record

This file freezes the **input to a future isolated re-review**. It does not say that the re-review has started or finished, and it is not evidence of method validity or prediction accuracy. A reviewer receives the de-labelled bundle, not the repository, manifest, or mapping.

### Frozen fingerprints

- Source commit: `018977bce046743036602ea99f63ea2dc18f2ef8` (the commit containing the cleaner change)
- Manifest: [`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- Manifest SHA-256: `0814d828c4694ecb8e7417f7ef8600eb2cebcc27a779f8ff2660584a819233a1`
- Bundle: [`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- Bundle SHA-256: `aaf60a038b487087f55db0c807427bfc3b4acc0cd8f7387e2218304f966d7f31`
- Evidence JSON: [`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- Seed SHA-256 (the seed itself is not committed): `266195e5d9223267726d6eedc3a3d561c3e4540448ca90590dd928e5cd1dc98a`
- Sealed mapping SHA-256 (stored outside the repository): `bbd380d401266eb0e20940b535e4dd52059a74e4c13ab6b9ba4e52f8c045f136`
- Included: 35 bilingual card pairs, numbered locally as `R-01`–`R-35`
- Candidate total: 218; excluded: 183
- Retained fields: `judgment`, `audience`, `reasoning_chain`, `time_window`, `falsifier`, `leading_indicator`
- Removed: legacy identifiers, title/source traceback clues, paths, status/confidence/external-comparison metadata, dependency references, diffusion-gate labels and conclusions, numbered constraint labels, and `EXT-NN` source identifiers. The judgment field itself remains so the reviewer can assess the original claim.

### Inclusion and exclusions

The manifest is authoritative for the inclusion rule and every bilingual source hash: include a current card only when both language projections retain readable content in all six required fields after de-labelling and removal of prior-review vocabulary. There are two exclusion buckets:

1. 95 historical migration snapshots from `docs/evidence/legacy-ledger-migration.md`, which duplicate current cards and are not a second judgment set.
2. 88 current ledger cards whose required fields no longer have readable content after prior-review metadata is removed (the manifest lists each card and its first missing field, beginning with `audience`); they are explicitly excluded rather than silently dropped.

The card set, bilingual paths, source hashes, inclusion reasons, and exclusion buckets are frozen. Any later change requires a new manifest and commit rather than overwriting this fingerprint.

### Structural evidence and boundary

`bundle-prepared-2026-10-28-isolated.json` records two independent runs, manifest-order independence, byte identity from `git archive HEAD`, bilingual field/path/count checks, index ordering, cross-language card-set consistency, mapping reachability, and the merged leakage scan. The mapping is not in the bundle; it only fixes the `R-NN → J-NNN` correspondence and is sealed outside the repository.

These checks establish only that the input package is reproducible and structurally bounded. They do **not** show that a reviewer ran, do not provide cryptographic anonymity, do not validate the method, and do not constitute prediction accuracy.
