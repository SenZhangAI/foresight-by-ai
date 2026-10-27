# Independent Re-prediction After Historical Calibration: Current Status

[中文版](../zh/independent-reprediction-status.md)

[Back to README / document map](../../README.en.md)

> **Bottom line first:** the isolated re-review has run twice, but it is not a forecasting system whose accuracy has been established. The public evidence lets readers distinguish the frozen input, procedural isolation, completed re-judgement, and still-open evidence boundaries. It does not support treating reproducibility as forecast correctness or claiming that the method has been validated.

## Why this page exists

After historical calibration, the project followed the stated sequence for reviewing the old forecast material in isolation. It did not simply give a new instance a ledger containing old statuses. It froze the input, generated a de-labelled, renumbered, shuffled bundle, sent records to fresh-context batches for item-by-item re-judgement, and only then unsealed the mapping.

This is the public reader's status entrance. It creates no new future judgment and does not replace the [Judgment Ledger](90-ledger.md), the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md), or the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md). It is a navigation page for the current evidence state, not a certificate that upgrades the historical review into a future out-of-sample forecast.

## From historical calibration to independent re-prediction: four status steps

These four steps use the same link set and order as the bilingual README. Each current status is separate evidence; a structural green light at a later step cannot replace an earlier one:

| Step | Entry | Current status |
|---|---|---|
| 1. Historical retrospect | [Retrospect](01-retrospect.md) | **Partial calibration completed**: cases explain known outcomes, expose counterexamples, and narrow rules; they do not produce future accuracy. |
| 2. Method validation | [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md) | **Protocol public; historical holdout not run**: freezing, retention, baselines, and leakage boundaries are specified; no pseudo-out-of-sample hit rate is reportable. |
| 3. Isolated re-prediction | [This independent re-prediction status](independent-reprediction-status.md) · [Isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md) · [Five-card supplement dated 2026-10-27](../evidence/independent-reprediction-supplement-2026-10-27.en.md) | **Two historical procedural rounds plus a five-card supplement completed, reproducibility only**: the leak, same-model, and run-record limits described below remain. |
| 4. Genuine out-of-sample result | [Ledger review log](90-ledger.md#8-review-log) | **Unverified**: no future card has both reached its observation window and been registered with a `GENUINE_FUTURE_OOS` result, so accuracy cannot be reported. |

A passing `python3 scripts/check.py` or `npm run check` proves only the structural and link contract; it does not prove method validity, forecast correctness, or a genuine out-of-sample result. For the full reading path, return to the [same four-step entrance in the English README](../../README.en.md).

## Read four statuses separately

| Status | Currently verifiable fact | What it must not be read as |
|---|---|---|
| **Frozen input** | The second-round baseline was frozen at commit `98fd95701da3bacef4d43e304db6b82e3f4d3b9b`; the manifest is `docs/evidence/blind-review/manifest-2026-10-09b.json`, SHA-256 `181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1`; 102 bilingual card pairs were frozen under the same inclusion rule. The 2026-10-27 supplement uses commit `30876ab9cbbdff898d82697e392f06042542d9a0` as its source, freezes only J-103–J-107, includes 5, and explicitly excludes the other 118. | Not every current ledger card entered a review: the 2026-10-09 historical round has no J-103–J-107 record, and the supplement does not cover the other 118. |
| **Isolation from old documents** | The bundle retained only the judgment, audience scale, reasoning chain, time window, falsifier, leading indicator, lenses, strongest counterargument, “what can be done now,” and proposal date. It removed card IDs, statuses, confidence, `REVISED` reasons, dependency graphs, source links, original paths, and explicit review passages, then renumbered and shuffled records by seed. | Not cryptographic isolation. Someone holding both the bundle and the public repository may still match records by text, and de-labelling cannot remove the same model's training memory. More importantly, the audience field still carried Gate 1's prior conclusion, so it is not valid to claim that every old-answer leak was removed. |
| **Independent re-judgement** | Two rounds were completed on 2026-10-09: round one used six mutually isolated batches for 102 records; after the de-labelling defect was fixed, round two re-judged the 28 records affected by the input defect. Results, hashes, mappings, and raw outputs have public evidence; round-two outputs are in `docs/evidence/blind-review/raw/round2/`. | This is procedural independent re-judgement, not proof of independent correctness. The re-reviewer was the same model as the original author; agreement measures reproducibility, not correctness. |
| **Current result** | The 2026-10-09 historical round gave each record entering the review a `VETO` or `ABSTAIN` disposition; round two repaired the input defect affecting 28 cards. The public report records `VETO 37 / ABSTAIN 65` for the 102-record accounting, alongside a separate accounting for the intact bilingual subset; the only new public status change triggered and retained by the historical round was the downgrade of J-029's society-scale wording. The 2026-10-27 supplement connects J-103–J-107 to de-labeled records and independent gate results: J-103 is `PASS`, and J-104–J-107 are `VETO`, with abstentions and missing evidence retained gate by gate. | `ABSTAIN` is not a pass, and zero falsifications does not mean that no judgment was falsified; neither the two historical rounds nor the five-card supplement checks future facts or produces a hit rate or accuracy estimate. |

## What this round actually completed

1. **A reproducible frozen input**: the source commit, manifest, inclusion rule, card count, bilingual projections, and hashes were recorded so cards could not be added or removed after seeing results.
2. **Material procedural isolation**: results were submitted before the mapping was unsealed; batches could not see one another or the full repository. Negative tests for the generator are recorded in the bundle evidence page.
3. **A repaired input defect and a second re-judgement**: the first round exposed that the one-sentence judgment of 28 cards had been erased by the title de-labelling rule. The project repaired the generator and re-judged them in round two rather than excluding them permanently; the first-round dispositions remain historical records only.
4. **Explicit limits rather than concealed limits**: the audience-field leak, missing run timestamp, owner-backed ordering of the round-two hash evidence, and same-model training-memory limitation remain publicly recorded.

The full per-card reasons, two historical rounds, five-card supplement, open gaps, and prohibited claims are in the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md) and the [supplemental independent re-review record](../evidence/independent-reprediction-supplement-2026-10-27.en.md). Evidence labels and the conditions for the next step are in the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md).

## 2026-10-27 supplement: J-103–J-107

This batch froze **exactly five cards, J-103–J-107**: source commit `30876ab9cbbdff898d82697e392f06042542d9a0`, with manifest coverage of 123 candidates, 5 reviewed, and 118 explicitly excluded. The mapping is `R-02→J-103`, `R-05→J-104`, `R-04→J-105`, `R-03→J-106`, `R-01→J-107`. Gate-by-gate results, the de-labeled bundle, hashes, and missing evidence are in the [supplemental independent re-review record](../evidence/independent-reprediction-supplement-2026-10-27.en.md) and its `blind-review/supplement-2026-10-27/` evidence directory.

| Card | Batch status | How readers should understand it |
|---|---|---|
| J-103 | `PASS` | No necessary-condition veto found; not a forecast hit |
| J-104 | `VETO` | Gate 1 scale veto; not a factual refutation of the forward claim |
| J-105 | `VETO` | Gate 1 scale veto and Gate 5 abstention; institutional persistence remains unobserved |
| J-106 | `VETO` | Gate 1 scale veto and Gates 2/5 abstention; recipient-side net resources remain unverified |
| J-107 | `VETO` | Gate 1 scale veto and Gates 2/5 abstention; coverage and causality remain open |

The other 118 cards are explicitly excluded from this batch. They are neither marked “reviewed” nor turned into results by the exclusion. None of the five-card results may be written as forecast accuracy or `GENUINE_FUTURE_OOS`. Evidence labels and the conditions for the next step are in the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md).

## What cannot be claimed now

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
