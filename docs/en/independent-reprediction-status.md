# Independent Re-prediction After Historical Calibration: Current Status

[中文版](../zh/independent-reprediction-status.md)

[Back to README / document map](../../README.en.md)

> **Bottom line first:** two historical rounds completed their prior per-card procedure, and a separate 2026-10-28 repaired-bundle run reviewed 29 frozen records. The latter is **input-incomplete**: all 29 are `UNKNOWN/UNVERIFIED`, so this is not a forecasting system whose accuracy has been established. The public evidence lets readers distinguish the frozen input, procedural execution, completed re-judgement, and still-open evidence boundaries. It does not support treating reproducibility, an input-boundary result, or structure checks as forecast correctness or claiming that the method has been validated.

## Why this page exists

After historical calibration, the project followed the stated sequence for reviewing the old forecast material in isolation. It did not simply give a new instance a ledger containing old statuses. It froze the input, generated a de-labelled, renumbered, shuffled bundle, sent records to fresh-context batches for item-by-item re-judgement, and only then unsealed the mapping.

This is the public reader's status entrance. It creates no new future judgment and does not replace the [Judgment Ledger](90-ledger.md), the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md), or the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md). It is a navigation page for the current evidence state, not a certificate that upgrades the historical review into a future out-of-sample forecast.

## From historical calibration to independent re-prediction: four status steps

These four steps use the same link set and order as the bilingual README. Each current status is separate evidence; a structural green light at a later step cannot replace an earlier one:

| Step | Entry | Current status |
|---|---|---|
| 1. Historical retrospect | [Retrospect](01-retrospect.md) | **Partial calibration completed**: cases explain known outcomes, expose counterexamples, and narrow rules; they do not produce future accuracy. |
| 2. Method validation | [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md) | **Protocol public; historical holdout not run**: freezing, retention, baselines, and leakage boundaries are specified; no pseudo-out-of-sample hit rate is reportable. |
| 3. Isolated re-prediction | [This independent re-prediction status](independent-reprediction-status.md) · [Isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md) · [2026-10-27 five-card gate-screening record](../evidence/independent-reprediction-supplement-2026-10-27.en.md) · [2026-10-28 repaired-bundle report](../evidence/blind-review/independent-rereview-2026-10-28.en.md) | **Two historical rounds completed; the five-card supplement remains protocol debugging because R2>50%; the 2026-10-28 run reviewed 29/29 records but is input-incomplete**: all 29 are `UNKNOWN/UNVERIFIED`, with no gate result. These records support an auditable input-boundary finding, not independent correctness or a completed protocol-level re-review. |
| 4. Genuine out-of-sample result | [Ledger review log](90-ledger.md#8-review-log) | **Unverified**: no future card has both reached its observation window and been registered with a `GENUINE_FUTURE_OOS` result, so accuracy cannot be reported. |

A passing `python3 scripts/check.py` or `npm run check` proves only the structural and link contract; it does not prove method validity, forecast correctness, or a genuine out-of-sample result. For the full reading path, return to the [same four-step entrance in the English README](../../README.en.md).

## Read four statuses separately

| Status | Currently verifiable fact | What it must not be read as |
|---|---|---|
| **Frozen input** | The second-round baseline was frozen at commit `98fd95701da3bacef4d43e304db6b82e3f4d3b9b`; the manifest is `docs/evidence/blind-review/manifest-2026-10-09b.json`, SHA-256 `181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1`; 102 bilingual card pairs were frozen under the same inclusion rule. The 2026-10-27 supplement uses commit `30876ab9cbbdff898d82697e392f06042542d9a0` as its source, freezes only J-103–J-107, includes 5, and explicitly excludes the other 118. | Not every current ledger card entered a review: the 2026-10-09 historical round has no J-103–J-107 record, and the supplement does not cover the other 118. |
| **Isolation from old documents** | The bundle retained only the judgment, audience scale, reasoning chain, time window, falsifier, leading indicator, lenses, strongest counterargument, “what can be done now,” and proposal date. It removed card IDs, statuses, confidence, `REVISED` reasons, dependency graphs, source links, original paths, and explicit review passages, then renumbered and shuffled records by seed. | Not cryptographic isolation. Someone holding both the bundle and the public repository may still match records by text, and de-labelling cannot remove the same model's training memory. More importantly, the audience field still carried Gate 1's prior conclusion, so it is not valid to claim that every old-answer leak was removed. |
| **Independent re-judgement** | Two rounds were completed on 2026-10-09: round one used six mutually isolated batches for 102 records; after the de-labelling defect was fixed, round two re-judged the 28 records affected by the input defect. Results, hashes, mappings, and raw outputs have public evidence; round-two outputs are in `docs/evidence/blind-review/raw/round2/`. | This is procedural independent re-judgement, not proof of independent correctness. The re-reviewer was the same model as the original author; agreement measures reproducibility, not correctness. |
| **Current result** | The 2026-10-09 historical round gave each record entering the review a `VETO` or `ABSTAIN` disposition; round two repaired the input defect affecting 28 cards. The public report records `VETO 37 / ABSTAIN 65` for the 102-record accounting, alongside a separate accounting for the intact bilingual subset; the only new public status change triggered and retained by the historical round was the downgrade of J-029's society-scale wording. The 2026-10-27 supplement connects J-103–J-107 to de-labeled records, recognition probes, and raw gate outputs, but R2=3/5 downgrades it to protocol debugging: J-103, J-105, J-106, and J-107 are raw `ABSTAIN`, and J-104 is raw `VETO`. | `ABSTAIN` is not a pass, and zero falsifications does not mean that no judgment was falsified; the historical rounds and the five-card debugging batch do not check future facts or produce a hit rate or accuracy estimate. |

## What this round actually completed

1. **A reproducible frozen input**: the source commit, manifest, inclusion rule, card count, bilingual projections, and hashes were recorded so cards could not be added or removed after seeing results.
2. **Material procedural isolation**: results were submitted before the mapping was unsealed; batches could not see one another or the full repository. Negative tests for the generator are recorded in the bundle evidence page.
3. **A repaired input defect and a second re-judgement**: the first round exposed that the one-sentence judgment of 28 cards had been erased by the title de-labelling rule. The project repaired the generator and re-judged them in round two rather than excluding them permanently; the first-round dispositions remain historical records only.
4. **Explicit limits rather than concealed limits**: the audience-field leak, missing run timestamp, owner-backed ordering of the round-two hash evidence, and same-model training-memory limitation remain publicly recorded.

The full per-card reasons, two historical rounds, the five-card debugging batch, open gaps, and prohibited claims are in the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md) and the [supplemental gate-screening record](../evidence/independent-reprediction-supplement-2026-10-27.en.md). Evidence labels and the conditions for the next step are in the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md).

## 2026-10-27 supplement: J-103–J-107

This batch froze **exactly five cards, J-103–J-107**: source commit `30876ab9cbbdff898d82697e392f06042542d9a0`, with manifest coverage of 123 candidates, 5 included, and 118 explicitly excluded. The mapping is `R-02→J-103`, `R-05→J-104`, `R-04→J-105`, `R-03→J-106`, `R-01→J-107`. The de-labeled bundle, recognition probes, raw gate JSON, hashes, and exclusion reasons are in the [supplemental gate-screening record](../evidence/independent-reprediction-supplement-2026-10-27.en.md) and its `blind-review/supplement-2026-10-27/` evidence directory. Probe counts are `R0=0 / R1=2 / R2=3`; the batch is therefore downgraded to protocol debugging/calibration and cannot be called a completed protocol-level independent re-review.

| Card | Raw overall | Batch status | How readers should understand it |
|---|---|---|---|
| J-103 | `ABSTAIN` | Debugging record, not independent re-review | Gate 5 lacks per-use net burden and an enforceable actor; R2 high-confidence S guess |
| J-104 | `VETO` | Debugging record, not independent re-review | Gates 1 and 4 veto; R2 high-confidence D guess |
| J-105 | `ABSTAIN` | Debugging record, not independent re-review | Five-gate mapping for institutional action is missing; R1 |
| J-106 | `ABSTAIN` | Debugging record, not independent re-review | Budget action, scale, and net-burden evidence is missing; R1 |
| J-107 | `ABSTAIN` | Debugging record, not independent re-review | Replacement action, carrying conditions, and net burden are missing; R2 high-confidence D guess |

The other 118 cards are explicitly excluded from this batch. They are neither marked “reviewed” nor turned into results by the exclusion. The raw outputs must not be written as forecast accuracy or `GENUINE_FUTURE_OOS`; a protocol-level independent re-review would require a new batch frozen before any of these records are revealed. Evidence labels and the conditions for the next step are in the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md).

## 2026-10-28 repaired-bundle run: 29 records, all input-incomplete

The [public report](../evidence/blind-review/independent-rereview-2026-10-28.en.md) and its [machine-readable record](../evidence/blind-review/independent-rereview-2026-10-28.json) consume only the repaired frozen bundle, SHA-256 `b500a63a28e755479790b5680787ae86a47f2703685ffa56657b7ad7f4c177f6`. Its freeze provenance is `source_commit 01162c9fa6a483ef58471f4694a3e69d39f8bb35`, manifest SHA-256 `077493f7f582dfa3e9ffaad9336094c9c9b87c6278f6d1e5b063fa2289580545`, with 218 candidates, 29 included, and 189 excluded at the candidate-pool layer. Those 189 exclusions precede bundle construction; the 29 records in the bundle have no internal exclusions. The bundle contains exactly 29 bilingual records, and all 29 were reviewed: `R-01` through `R-29`. Each record has the six retained fields and a Chinese/English pair; no old `J-NNN` identifier, status, source label, or external method text was imported.

| Per-card scope | Status for every listed record | Disposition | Evidence limit |
|---|---|---|---|
| `R-01`–`R-29` (29/29; the report lists each ID) | `UNKNOWN/UNVERIFIED` | `retain-unverified-boundary` | The frozen input lacks the five diffusion-gate definitions, applicability rules, thresholds, execution instructions, and out-of-sample protocol; no gate result can be produced without importing outside text |

This is an explicit per-card result, not an aggregate pass/fail. The bundle has no exclusions within its 29 records. Conversely, records outside `R-01`–`R-29` are outside this run, not negative cases and not silently reviewed; because the bundle deliberately restores no external mapping, no claim about which current `J-NNN` cards are covered is allowed. The result therefore supports only an input-boundary failure and traceable retention. It does **not** produce `PASS`, `VETO`, `ABSTAIN`, reproducibility, falsification, accuracy, `CALIBRATION`, `CONTAMINATED_RELATIVE_HOLDOUT`, or `GENUINE_FUTURE_OOS` evidence. The complete per-card bases are in the linked report and JSON, not in an inferred aggregate count.


- “The blind re-review passed, therefore the judgments are validated”;
- treating `ABSTAIN` as a positive forecast or society-scale diffusion;
- treating agreement with the old status or a re-review consistency rate as accuracy;
- treating these two rounds as `GENUINE_FUTURE_OOS`;
- treating structural checks, input hashes, or public file reachability as proof of method validity;
- treating the current entrance as proof that the whole-society landscape is complete.

A genuine out-of-sample record still comes from a future judgment card whose text, information boundary, outcome definition, and observation window were frozen before the outcome was known. Historical `CALIBRATION` can explain known outcomes, find counterexamples, and revise rules; a historically contaminated relative test may at most compare relative discrimination and cannot replace future due-date evidence.

## What is required for the next state transition

Before a future round can claim stronger isolation, it must address the limits recorded in the public report: provide an audience-denominator field that does not carry the old conclusion, remove source-project clues from dispatch prompts, record each run timestamp, and make the order between hash submission and unsealing independently reviewable. If the rule text changes materially, the protocol also requires a new holdout and a new re-review; the old review cannot validate the new rule set.

Until those conditions are met, the correct public status is: **historical calibration has been partially executed; the isolated re-review has run twice; independent correctness and genuine forecast accuracy remain unproven.**
