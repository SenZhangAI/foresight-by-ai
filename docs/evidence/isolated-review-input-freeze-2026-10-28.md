# 隔离式全面重审输入冻结（2026-10-28）

## 中文记录

本文件只记录**重审输入已经冻结**，不记录也不暗示重审已经启动、方法有效或预测准确率。审查者收到的是去除旧来源线索与旧复核标签后的 `bundle`，而不是本仓库、manifest 或映射文件。

### 冻结指纹

- 输入源 commit：`0317c0adaecc4c725caeb6b9fd35b9e2109679ce`
- manifest：[`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- manifest SHA-256：`f942a6d40f4113243905180a8df4e53995d5f0557a9f3431609c95e3931b5482`
- bundle：[`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- bundle SHA-256：`7135af58447d31d35e500ad3c79f341ee83e63d82f5c1edd73e272d0bd2c3291`
- 证据 JSON：[`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- seed SHA-256（seed 本身不入仓库）：`60f654795f233f69ab4e3db4df46dd10de6c014b582d0b497fc7b9b50ecd0cda`
- 密封映射 SHA-256（映射保存在仓库外，不随 bundle 发布）：`cbb0d439050ab43fb06f1c5116fbbe30f1876e7adaf1950b7ba546ca8f6e6177`
- 纳入：121 张中英成对判断卡；`R-01`–`R-121`
- 候选总数：218；排除：97
- 保留字段（中英同义）：`judgment`、`audience`、`reasoning_chain`、`time_window`、`falsifier`、`leading_indicator`
- 去除内容：旧卡片编号、标题回溯线索、来源路径、状态／置信度／外部对照元数据、依赖关系、普及闸及其旧结论标签、编号约束标签与 `EXT-NN` 来源编号；判断字段本身保留，以便重审者能判断原主张。

### 纳入与排除

纳入规则和逐项文件哈希以 manifest 为准：当前台账中同时存在中英文版本、六个必填字段在去标签及旧复核标签清理后仍可读的卡片。排除项只有两桶：

1. `docs/evidence/legacy-ledger-migration.md` 中的 95 条历史迁移快照：它们重复当前判断，不构成第二套判断全集。
2. `J-071`、`J-072`：清理后 `reasoning_chain` 不再有可读内容，无法交给 reviewer 判断；这两张没有被静默丢弃，排除原因已写入 manifest。

卡片集合、双语路径、源文件哈希、纳入理由与排除桶均被冻结；后续改变必须另起 manifest 和 commit，不能覆盖本指纹。

### 结构证据与边界

`bundle-prepared-2026-10-28-isolated.json` 记录了独立运行两次、manifest 顺序无关、`git archive HEAD` 字节一致、双语字段／路径／计数、索引顺序、跨语言卡片集合、映射可达性和合并泄漏扫描均通过。映射不在 bundle 中；它只用于冻结 `R-NN → J-NNN` 对应关系，并以外部密封文件保存。

这些检查只证明输入包可重建且结构边界成立。它们**不**证明 reviewer 已运行，不证明来源隔离在密码学意义上成立，不证明方法有效，也不构成预测准确率。

## English record

This file freezes the **input to a future isolated re-review**. It does not say that the re-review has started or finished, and it is not evidence of method validity or prediction accuracy. A reviewer receives the de-labelled bundle, not the repository, manifest, or mapping.

### Frozen fingerprints

- Source commit: `0317c0adaecc4c725caeb6b9fd35b9e2109679ce`
- Manifest: [`manifest-2026-10-28-isolated.json`](blind-review/manifest-2026-10-28-isolated.json)
- Manifest SHA-256: `f942a6d40f4113243905180a8df4e53995d5f0557a9f3431609c95e3931b5482`
- Bundle: [`bundle-2026-10-28-isolated.json`](blind-review/bundle-2026-10-28-isolated.json)
- Bundle SHA-256: `7135af58447d31d35e500ad3c79f341ee83e63d82f5c1edd73e272d0bd2c3291`
- Evidence JSON: [`bundle-prepared-2026-10-28-isolated.json`](blind-review/bundle-prepared-2026-10-28-isolated.json)
- Seed SHA-256 (the seed itself is not committed): `60f654795f233f69ab4e3db4df46dd10de6c014b582d0b497fc7b9b50ecd0cda`
- Sealed mapping SHA-256 (stored outside the repository): `cbb0d439050ab43fb06f1c5116fbbe30f1876e7adaf1950b7ba546ca8f6e6177`
- Included: 121 bilingual card pairs, numbered locally as `R-01`–`R-121`
- Candidate total: 218; excluded: 97
- Retained fields: `judgment`, `audience`, `reasoning_chain`, `time_window`, `falsifier`, `leading_indicator`
- Removed: legacy identifiers, title/source traceback clues, paths, status/confidence/external-comparison metadata, dependency references, diffusion-gate labels and conclusions, numbered constraint labels, and `EXT-NN` source identifiers. The judgment field itself remains so the reviewer can assess the original claim.

### Inclusion and exclusions

The manifest is authoritative for the inclusion rule and every bilingual source hash: include a current card only when both language projections retain readable content in all six required fields after de-labelling and removal of prior-review vocabulary. There are two exclusion buckets:

1. 95 historical migration snapshots from `docs/evidence/legacy-ledger-migration.md`, which duplicate current cards and are not a second judgment set.
2. `J-071` and `J-072`, whose `reasoning_chain` became unreadable after cleaning; their exclusion is explicit in the manifest rather than silent.

The card set, bilingual paths, source hashes, inclusion reasons, and exclusion buckets are frozen. Any later change requires a new manifest and commit rather than overwriting this fingerprint.

### Structural evidence and boundary

`bundle-prepared-2026-10-28-isolated.json` records two independent runs, manifest-order independence, byte identity from `git archive HEAD`, bilingual field/path/count checks, index ordering, cross-language card-set consistency, mapping reachability, and the merged leakage scan. The mapping is not in the bundle; it only fixes the `R-NN → J-NNN` correspondence and is sealed outside the repository.

These checks establish only that the input package is reproducible and structurally bounded. They do **not** show that a reviewer ran, do not provide cryptographic anonymity, do not validate the method, and do not constitute prediction accuracy.
