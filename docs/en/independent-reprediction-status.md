# Independent Re-prediction After Historical Calibration: Current Status

[中文版](../zh/independent-reprediction-status.md)

[Back to README / document map](../../README.en.md)

> **Bottom line first:** the isolated re-review has run twice, but it is not a forecasting system whose accuracy has been established. The public evidence lets readers distinguish the frozen input, procedural isolation, completed re-judgement, and still-open evidence boundaries. It does not support treating reproducibility as forecast correctness or claiming that the method has been validated.

## Why this page exists

After historical calibration, the project followed the stated sequence for reviewing the old forecast material in isolation. It did not simply give a new instance a ledger containing old statuses. It froze the input, generated a de-labelled, renumbered, shuffled bundle, sent records to fresh-context batches for item-by-item re-judgement, and only then unsealed the mapping.

This is the public reader's status entrance. It creates no new future judgment and does not replace the [Judgment Ledger](90-ledger.md), the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md), or the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md). It is a navigation page for the current evidence state, not a certificate that upgrades the historical review into a future out-of-sample forecast.

## Read four statuses separately

| Status | Currently verifiable fact | What it must not be read as |
|---|---|---|
| **Frozen input** | The second-round baseline was frozen at commit `98fd95701da3bacef4d43e304db6b82e3f4d3b9b`; the manifest is `docs/evidence/blind-review/manifest-2026-10-09b.json`, SHA-256 `181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1`; 102 bilingual card pairs were frozen under the same inclusion rule. | Not every current ledger card entered this review; cards registered later, including J-103–J-107, have no blind-review record from this round. |
| **Isolation from old documents** | The bundle retained only the judgment, audience scale, reasoning chain, time window, falsifier, leading indicator, lenses, strongest counterargument, “what can be done now,” and proposal date. It removed card IDs, statuses, confidence, `REVISED` reasons, dependency graphs, source links, original paths, and explicit review passages, then renumbered and shuffled records by seed. | Not cryptographic isolation. Someone holding both the bundle and the public repository may still match records by text, and de-labelling cannot remove the same model's training memory. More importantly, the audience field still carried Gate 1's prior conclusion, so it is not valid to claim that every old-answer leak was removed. |
| **Independent re-judgement** | Two rounds were completed on 2026-10-09: round one used six mutually isolated batches for 102 records; after the de-labelling defect was fixed, round two re-judged the 28 records affected by the input defect. Results, hashes, mappings, and raw outputs have public evidence; round-two outputs are in `docs/evidence/blind-review/raw/round2/`. | This is procedural independent re-judgement, not proof of independent correctness. The re-reviewer was the same model as the original author; agreement measures reproducibility, not correctness. |
| **Current result** | Each record entering the review received a `VETO` or `ABSTAIN` disposition; round two corrected the input defect affecting 28 cards. The public report records `VETO 37 / ABSTAIN 65` for the 102-record accounting, alongside a separate accounting for the subset with intact bilingual claims; the only new public status change triggered and retained by this round was the downgrade of J-029's society-scale wording. | `ABSTAIN` is not a pass, and zero falsifications does not mean that no judgment was falsified. This round did not check whether future facts occurred and produced no hit rate or accuracy estimate. |

## What this round actually completed

1. **A reproducible frozen input**: the source commit, manifest, inclusion rule, card count, bilingual projections, and hashes were recorded so cards could not be added or removed after seeing results.
2. **Material procedural isolation**: results were submitted before the mapping was unsealed; batches could not see one another or the full repository. Negative tests for the generator are recorded in the bundle evidence page.
3. **A repaired input defect and a second re-judgement**: the first round exposed that the one-sentence judgment of 28 cards had been erased by the title de-labelling rule. The project repaired the generator and re-judged them in round two rather than excluding them permanently; the first-round dispositions remain historical records only.
4. **Explicit limits rather than concealed limits**: the audience-field leak, missing run timestamp, owner-backed ordering of the round-two hash evidence, and same-model training-memory limitation remain publicly recorded.

The full per-card reasons, two-round accounting, open gaps, and prohibited claims are in the [isolated blind re-review report](../evidence/blind-review-reaudit-2026-10-09.en.md). Evidence labels and the conditions for the next step are in the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md).

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
