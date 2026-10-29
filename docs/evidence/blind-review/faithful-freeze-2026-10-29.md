# 严格字段保真盲审冻结 / Strict source-field-fidelity freeze

## 中文

本轮把旧的“清洗后稳定生成”路径改为**源字段保真冻结**。盲审包只从 `source_commit` 的 Git 快照读取；不读取当前工作树。manifest 为每个纳入卡片的六个字段记录：中英文源文件、字段名、完整字段定位（包括 bullet、label、冒号、空白、换行和值）、原始 label/value 子定位和完整字段字节 SHA-256；这份完整 manifest 保存在仓库外。仓库内同名文件只是去标识化 receipt，不含源 ID、alias、路径、locator、label 或映射。包内字段只允许进行 private manifest 明确的 `J-NNN → R-NNN` 精确字节别名替换。

任何 NFKC、换行或空白归一化、链接／来源清洗、标签删除、状态／评审文字替换、未登记卡片 ID 的变换都不会发生：必填字段一旦需要这些操作，卡片进入 private manifest 的逐卡 exclusion ledger。`fidelity-evidence.json` 是不含映射的公开逐字段证据；公开 evidence 只发布 alias、language、field、source/emitted hash、替换计数和差异结论；不发布 source_id、路径、locator、label 或 `from` ID。它不是同一清洗流程的 hash 自证，因为私有重建步骤先从 Git 快照按 locator 读取原始字节，再逐字段做允许变换比较。

- 冻结源提交：`fa4e65750f15f75ebf90737faaa9218f3d81be74`
- manifest：[`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- manifest receipt SHA-256：`9bb3d0a3235996d5b4def20ca6c1576d27593f64d6d61488b1418de527d279ba`
- private manifest SHA-256（仓库外）：`f942db710797f7ca61d5a5268a6d3ddfddf52afcab743857da6efbee7ccb0c43`
- 纳入：8 张双语卡片；排除：115 张；每张纳入卡片 12 个字段（中英六字段），共 96 个字段
- bundle：[`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- bundle SHA-256：`677d05e6090b73e9c7b4a13bf6ee8153a806c373f76f1da057d8fe2a78617d26`
- 逐字段证据：[`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- 密封 `R-NNN → J-NNN` 映射保存在仓库外；映射 SHA-256：`a9e666def9996b2c699425c34a4d602937e0fa35943a30d9bc041017d8f757e6`；仓库不把映射交给盲审者

可重建命令：

```bash
python3 scripts/blind_fidelity.py \
  --repo . \
  --source-commit fa4e65750f15f75ebf90737faaa9218f3d81be74 \
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

No NFKC, newline or whitespace normalization, link/source cleaning, label deletion, status/review-text replacement, or implicit card-ID rewrite is performed. If a required field would need one of those operations, the card is placed in the private manifest’s per-card exclusion ledger. Public `fidelity-evidence.json` records, field by field, only opaque alias, language, field, source/emitted hashes, replacement counts, and the `exact_except_explicit_id_alias` verdict; each private excluded field records its language, field, reason, source path, locator, source hash, and `excluded_before_projection`. This is not a hash of two outputs from one cleaning pipeline: private reconstruction reads raw bytes from the Git snapshot at each locator and then applies only the permitted alias operation.

- Frozen source commit: `fa4e65750f15f75ebf90737faaa9218f3d81be74`
- Manifest: [`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- Manifest receipt SHA-256: `9bb3d0a3235996d5b4def20ca6c1576d27593f64d6d61488b1418de527d279ba`
- Private manifest SHA-256 (outside the repository): `f942db710797f7ca61d5a5268a6d3ddfddf52afcab743857da6efbee7ccb0c43`
- Included: 8 bilingual cards; excluded: 115; 96 fields across the included cards
- Bundle: [`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- Bundle SHA-256: `677d05e6090b73e9c7b4a13bf6ee8153a806c373f76f1da057d8fe2a78617d26`
- Field evidence: [`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- The sealed `R-NNN → J-NNN` mapping is kept outside the repository; mapping SHA-256: `a9e666def9996b2c699425c34a4d602937e0fa35943a30d9bc041017d8f757e6`; the mapping is not given to the blind reviewer

Rebuild with the three commands shown in the Chinese section. When `source_commit` changes, freeze a new manifest; an old manifest must never silently read a new working tree. This package proves a reproducible input-field fidelity boundary only. It does not prove that a review ran, that the method is valid, or that predictions are accurate.
