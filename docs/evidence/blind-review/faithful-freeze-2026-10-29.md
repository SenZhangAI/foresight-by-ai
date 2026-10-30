# 严格字段保真盲审冻结 / Strict source-field-fidelity freeze

## 中文

本轮把旧的“清洗后稳定生成”路径改为**源字段保真冻结**。盲审包只从 `source_commit` 的 Git 快照读取；不读取当前工作树。manifest 为每个纳入卡片的六个字段记录：中英文源文件、字段名、完整字段定位（包括 bullet、label、冒号、空白、换行和值）、原始 label/value 子定位和完整字段字节 SHA-256；这份完整 manifest 保存在仓库外。仓库内同名文件只是去标识化 receipt，不含源 ID、alias、路径、locator、label 或映射。包内字段只允许进行 private manifest 明确的 `J-NNN → R-NNN` 精确字节别名替换。

任何 NFKC、换行或空白归一化、链接／来源清洗、标签删除、状态／评审文字替换、未登记卡片 ID 的变换都不会发生：必填字段一旦需要这些操作，卡片进入 private manifest 的逐卡 exclusion ledger。`fidelity-evidence.json` 是不含映射的公开逐字段证据；`exclusion-evidence.json` 逐个列出排除字段的 opaque ref、语言、字段、原因、源字段哈希和排除结论；公开证据不发布 source_id、路径、locator、label 或 `from` ID。它不是同一清洗流程的 hash 自证，因为私有重建步骤先从 Git 快照按 locator 读取原始字节，再逐字段做允许变换比较。

- 冻结源提交：`ed8b0cb89a94113f20272443b85a8ec67de83775`
- 生成器提交：`8339088aab3dda97e38cfdfa5e7da669575e13ab`（`scripts/blind_fidelity.py`）
- 生成器 SHA-256：`13430291bdad4022b48292e96fbdc36c7ee8167aa7b5b4724655220690cd68e8`
- manifest：[`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- manifest receipt SHA-256：`490cd58f2bf5a20a994c0698196199d4a1ce90d92dab73b3608dd735a0552d28`
- private manifest SHA-256（仓库外）：`7c211fa4020e8d1559e22b3446303129822e0289d106f688e72b5629f0475418`
- 纳入：8 张双语卡片；排除：115 张；每张纳入卡片 12 个字段（中英六字段），共 96 个字段
- bundle：[`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- bundle SHA-256：`bebd90e6cb53001f331da38e01aeac3ab634598143ae34df576b1d9f93427c81`
- 逐字段证据：[`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- 逐字段证据 SHA-256：`7dd5c5d494a1911bac357b769ab1f7fdec3925434759415459c889fa9a4255b8`
- 排除字段证据：[`faithful-bundle-2026-10-29/exclusion-evidence.json`](faithful-bundle-2026-10-29/exclusion-evidence.json)，SHA-256：`19e0c439b55414229316fa13c10c74abeda178fecbbebebb74ac798253210f5a`
- 密封 `R-NNN → J-NNN` 映射文件保存在仓库外；映射 SHA-256：`428709c322f88cd3e83defb466b64195cbf8c3bef4e35ead82b7f91bdc0d3d54`。仓库不直接交付该映射文件，但由于公开 bundle 同时提供 `source_commit` 与完整字段原文，能读取同一源仓库的审查者仍可能通过逐字段匹配重建映射；因此这里是“不交付映射文件”，不是信息论意义上的匿名隔离。

可重建命令：

```bash
python3 scripts/blind_fidelity.py \
  --repo . \
  --source-commit ed8b0cb89a94113f20272443b85a8ec67de83775 \
  --manifest-out /absolute/path/outside/repository/manifest-private.json
python3 scripts/blind_fidelity.py \
  --repo . \
  --manifest /absolute/path/outside/repository/manifest-private.json \
  --output-dir docs/evidence/blind-review/faithful-bundle-2026-10-29 \
  --mapping-out /absolute/path/outside/repository/mapping.json
python3 scripts/blind_fidelity.py \
  --repo . \
  --manifest /absolute/path/outside/repository/manifest-private.json \
  --receipt-out docs/evidence/blind-review/manifest-2026-10-29-faithful.json
```

`source_commit` 更新后，必须重新冻结 manifest；旧 manifest 不得指向新工作树。这个包证明的是输入字段的可重建保真边界，不证明盲审已运行、方法有效或预测准确。

## English

This round replaces “stable cleaned text” with a **source-field-fidelity freeze**. The package reads only the Git snapshot named by `source_commit`; it never reads the working tree. For every included card and each of the six required fields in both languages, the private manifest records the source file, complete field locator (bullet, label, colon, whitespace, newlines, and value), label/value sub-locators, and complete field-byte SHA-256. The repository receipt intentionally omits those source details. A bundled field may differ only through the private manifest’s explicit exact-byte `J-NNN → R-NNN` alias replacement.

No NFKC, newline or whitespace normalization, link/source cleaning, label deletion, status/review-text replacement, or implicit card-ID rewrite is performed. If a required field would need one of those operations, the card is placed in the private manifest’s per-card exclusion ledger. Public `fidelity-evidence.json` records included fields; public `exclusion-evidence.json` records each excluded field with an opaque reference, language, field, reason, source-field hash, and exclusion verdict, while withholding source IDs, paths, labels, locators, and mappings. This is not a hash of two outputs from one cleaning pipeline: private reconstruction reads raw bytes from the Git snapshot at each locator and then applies only the permitted alias operation.

- Frozen source commit: `ed8b0cb89a94113f20272443b85a8ec67de83775`
- Generator commit: `8339088aab3dda97e38cfdfa5e7da669575e13ab` (`scripts/blind_fidelity.py`)
- Generator SHA-256: `13430291bdad4022b48292e96fbdc36c7ee8167aa7b5b4724655220690cd68e8`
- Manifest: [`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- Manifest receipt SHA-256: `490cd58f2bf5a20a994c0698196199d4a1ce90d92dab73b3608dd735a0552d28`
- Private manifest SHA-256 (outside the repository): `7c211fa4020e8d1559e22b3446303129822e0289d106f688e72b5629f0475418`
- Included: 8 bilingual cards; excluded: 115; 96 fields across the included cards
- Bundle: [`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- Bundle SHA-256: `bebd90e6cb53001f331da38e01aeac3ab634598143ae34df576b1d9f93427c81`
- Field evidence: [`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- Field evidence SHA-256: `7dd5c5d494a1911bac357b769ab1f7fdec3925434759415459c889fa9a4255b8`
- Excluded-field evidence: [`faithful-bundle-2026-10-29/exclusion-evidence.json`](faithful-bundle-2026-10-29/exclusion-evidence.json), SHA-256: `19e0c439b55414229316fa13c10c74abeda178fecbbebebb74ac798253210f5a`
- The sealed `R-NNN → J-NNN` mapping file is kept outside the repository; mapping SHA-256: `428709c322f88cd3e83defb466b64195cbf8c3bef4e35ead82b7f91bdc0d3d54`. The repository does not directly deliver that file, but because the public bundle includes both `source_commit` and complete field text, a reviewer who can read the same source repository may still reconstruct the mapping by field matching; this is withholding the mapping artifact, not information-theoretic anonymity.

Rebuild with the three commands shown in the Chinese section. When `source_commit` changes, freeze a new manifest; an old manifest must never silently read a new working tree. This package proves a reproducible input-field fidelity boundary only. It does not prove that a review ran, that the method is valid, or that predictions are accurate.
