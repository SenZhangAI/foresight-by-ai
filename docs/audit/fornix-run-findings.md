# Defects in this repo found by fornix run audits

These were found by fornix's 2026-10-13 review of the 2026-10-08..10 runs. A fresh-eye reviewer with no audit context found them, and the main session re-measured each one.

**This file is the SoT for these defects.** When one is fixed, move it to "Fixed" and record the fixing commit.

---

## Still open

### RA-1013-1 · P1 · The blind-review bundle rewrites the claims reviewers judge

- **Behaviour**: `de_label_value` (`scripts/blind_bundle.py:297-311` @ `6d5756e`) makes four changes to retained prose:
  - it deletes METADATA / GATE / DEPENDENCY tokens anywhere in the prose ("状态", "status", "confidence", "置信度", "出处", "普及闸", …);
  - it rewrites every `J-NNN` as the English phrase "the preceding judgment", including inside zh fields;
  - it folds look-alike characters;
  - it squeezes the space after `, ; :`.
- **Measured** on the 2026-10-09b corpus: **1,272 of 2,040** retained fields altered. Examples:
  - J-066's claim lost its subject (普及闸);
  - J-012's falsifier lost 状态 ("不依赖状态追踪" → "不依赖追踪");
  - two different upstream cards both became "the preceding judgment".
- **Consequence**: both published review rounds (`bundle-2026-10-09a/b`) were run on altered text. That needs a disclosure, and the reviews of cards whose judgment or falsifier text changed should be redone.
- **A worked fix exists, unmerged**, on branch `audit/run-defects-2026-10-13` (`88510b3`, WIP):
  - prose ships verbatim; only card ids become per-record aliases ⟨A⟩/⟨B⟩, shared by zh and en;
  - the scan refuses instead of deleting;
  - a new `fidelity` check undoes the aliases and compares byte-for-byte;
  - `--self-test` passes;
  - metadata in prose is moved into non-whitelisted bullets at source (86 audience-provenance clauses, 37 dated lens annotations, J-066, J-094).
- **Why it is not merged**:
  1. After those moves, `scripts/check.py`'s audience "identity floor" fails 107 cards. Those cards passed only because the provenance prefix sat in front of the magnitude; their group is written as "magnitude（group）". The floor needs to accept that form. That is a judgment for this project.
  2. J-106 (in `docs/zh/ledger/103-110.md`, which has uncommitted edits in the main tree) carries another card's title in its falsifier. The new scan refuses it, by design.
- **Falsify**: build a bundle on a fresh freeze; every retained field is byte-identical to its source except for card-id aliases.

### RA-1013-2 · obs · Uncommitted edits left by a stopped run

- `git status` shows 10 modified files with mtimes 2026-10-10 11:35–11:51: README, `scripts/check.py`, `docs/zh/00-method.md`, `01-retrospect.md`, `03-evolution.md`, `90-ledger.md`, `chains/130-…`, `ledger/103-110.md`, `docs/en/90-ledger.md`, `docs/evidence/social-regularity-calibration-2026-10-10.md`.
- The last fornix LLM call in this project was 2026-10-10 11:51:36, so these are a stopped cluster's half-done edits (an L10-lens rewrite). Nobody owns them.
- **Falsify**: they are committed or deliberately discarded. (fornix-side card: Session500/fornix#1002.)

### RA-1013-3 · P2 · A lens was used before its falsifier existed

- `ee8d9ed` admitted lens L10 with no defined falsification window, and `44c543f` built J-106 on it before `c9188d9` defined one.
- The uncommitted tree above suggests L10 was falsified the same day.
- **Falsify**: J-106's premise is re-checked against L10's current status.

### RA-1013-4 · obs · Two chains' "unused lenses" lines don't follow the format the lens-contradiction check assumes

- C12 (`docs/zh/chains/120-…:22`) lists lenses without `（名称）`.
- C13 (`docs/zh/chains/130-…:35`) has no colon or list on that line.
- A literal implementation of the audit work unit's criteria would go red on a clean HEAD.

## Fixed

(none yet)
