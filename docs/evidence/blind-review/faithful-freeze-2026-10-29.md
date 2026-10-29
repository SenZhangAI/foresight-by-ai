# 严格字段保真盲审冻结 / Strict source-field-fidelity freeze

## 中文

本轮把旧的“清洗后稳定生成”路径改为**源字段保真冻结**。盲审包只从 `source_commit` 的 Git 快照读取；不读取当前工作树。manifest 为每个纳入卡片的六个字段记录：中英文源文件、字段名、完整字段定位（包括 bullet、label、冒号、空白、换行和值）、原始 label/value 子定位和完整字段字节 SHA-256。包内字段只允许进行 manifest 明确的 `J-NNN → R-NNN` 精确字节别名替换。

任何 NFKC、换行或空白归一化、链接／来源清洗、标签删除、状态／评审文字替换、未登记卡片 ID 的变换都不会发生：必填字段一旦需要这些操作，卡片进入 manifest 的逐卡 exclusion ledger。`fidelity-evidence.json` 逐字段记录源定位、源 hash、输出 hash、别名替换列表和 `exact_except_explicit_id_alias` 结论；它不是同一清洗流程的 hash 自证，因为重建步骤先从 Git 快照按 locator 读取原始字节，再逐字段做允许变换比较。

- 冻结源提交：`609ce7601a872040011f50c41f94136c02cec7da`
- manifest：[`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- manifest SHA-256：`0dc19cf09d1fd856bf4f3f06c9fb13e862b8d8919d10f7ba052f963dfabbb473`
- 纳入：71 张双语卡片；排除：52 张；每张纳入卡片 12 个字段（中英六字段），共 852 个字段
- bundle：[`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- bundle SHA-256：`355b9e78cec19eed82fb74584a3a829920061cf7e7955a5408c75b3ae547f0aa`
- 逐字段证据：[`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- 密封 `R-NNN → J-NNN` 映射保存在仓库外；仓库只保存其 hash，不把映射交给盲审者

可重建命令：

```bash
python3 scripts/blind_fidelity.py \
  --repo . \
  --source-commit 609ce7601a872040011f50c41f94136c02cec7da \
  --manifest-out docs/evidence/blind-review/manifest-2026-10-29-faithful.json
python3 scripts/blind_fidelity.py \
  --repo . \
  --manifest docs/evidence/blind-review/manifest-2026-10-29-faithful.json \
  --output-dir docs/evidence/blind-review/faithful-bundle-2026-10-29 \
  --mapping-out /absolute/path/outside/repository/mapping.json
```

`source_commit` 更新后，必须重新冻结 manifest；旧 manifest 不得指向新工作树。这个包证明的是输入字段的可重建保真边界，不证明盲审已运行、方法有效或预测准确。

## English

This round replaces “stable cleaned text” with a **source-field-fidelity freeze**. The package reads only the Git snapshot named by `source_commit`; it never reads the working tree. For every included card and each of the six required fields in both languages, the manifest records the source file, complete field locator (bullet, label, colon, whitespace, newlines, and value), label/value sub-locators, and complete field-byte SHA-256. A bundled field may differ only through the manifest’s explicit exact-byte `J-NNN → R-NNN` alias replacement.

No NFKC, newline or whitespace normalization, link/source cleaning, label deletion, status/review-text replacement, or implicit card-ID rewrite is performed. If a required field would need one of those operations, the card is placed in the manifest’s per-card exclusion ledger. `fidelity-evidence.json` records, field by field, the source locator, source hash, emitted hash, alias replacements, and the `exact_except_explicit_id_alias` verdict. This is not a hash of two outputs from one cleaning pipeline: reconstruction reads raw bytes from the Git snapshot at each locator and then applies only the permitted alias operation.

- Frozen source commit: `609ce7601a872040011f50c41f94136c02cec7da`
- Manifest: [`manifest-2026-10-29-faithful.json`](manifest-2026-10-29-faithful.json)
- Manifest SHA-256: `0dc19cf09d1fd856bf4f3f06c9fb13e862b8d8919d10f7ba052f963dfabbb473`
- Included: 71 bilingual cards; excluded: 52; 852 fields across the included cards
- Bundle: [`faithful-bundle-2026-10-29/bundle.json`](faithful-bundle-2026-10-29/bundle.json)
- Bundle SHA-256: `355b9e78cec19eed82fb74584a3a829920061cf7e7955a5408c75b3ae547f0aa`
- Field evidence: [`faithful-bundle-2026-10-29/fidelity-evidence.json`](faithful-bundle-2026-10-29/fidelity-evidence.json)
- The sealed `R-NNN → J-NNN` mapping is kept outside the repository; only its hash is recorded, so it is not given to the blind reviewer

Rebuild with the two commands shown in the Chinese section. When `source_commit` changes, freeze a new manifest; an old manifest must never silently read a new working tree. This package proves a reproducible input-field fidelity boundary only. It does not prove that a review ran, that the method is valid, or that predictions are accurate.
