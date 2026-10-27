# Genuine Future Out-of-Sample Results Register

[中文版](future-oos-results-register.md)

[Back to README / document map](../../README.en.md)

> This is the public result-return path, not an accuracy report. No `GENUINE_FUTURE_OOS` record has yet reached its review window and completed outcome disclosure; the empty table is a result state, not “all hits” or “all misses.”

## Current state

- **Evidence class**: `GENUINE_FUTURE_OOS`
- **Current result state**: `UNKNOWN/UNVERIFIED` (no completed future-due outcome is available yet)
- **Completed records**: `0`
- **Accuracy / hit-rate denominator**: not established
- **Authority**: this page registers outcomes; the full preregistration fields for each judgment remain in the [bilingual judgment ledger](../en/90-ledger.md).

Historical `CALIBRATION`, `CONTAMINATED_RELATIVE_HOLDOUT` under shared leakage, structure checks, and retrospective material are not copied into this table and cannot be upgraded into genuine future out-of-sample evidence. When an outcome is missing, retain `UNKNOWN/UNVERIFIED`; do not fill it with a similar metric, a second-hand number, memory, or narrative fit.

## When a row may be added

A record must be registered before its outcome is observable and must preserve these frozen fields:

1. **Judgment ID and freeze time**: for example, `J-NNN`; record the card freeze date and the information cutoff (`as-of`).
2. **Forecast content**: the original Chinese and English judgment text, or stable links to the frozen card; it must not be silently rewritten after reveal.
3. **Observation window**: start date, end date, maturity/review date, and when the outcome was revealed.
4. **Leading indicator**: the preregistered indicator, unit, frequency, source, and direction of the test.
5. **Audience scale**: the affected population's identity, order of magnitude, and behavioural denominator; reach is not a count of repeated actors.
6. **Maturity rule**: the preregistered rule for `HIT`, `FALSIFIED`, or `INDETERMINATE`; if it cannot be computed, name what is missing rather than rewriting the condition.
7. **Outcome evidence**: stable URL / file location, access or capture date, same-basis excerpt, unit, denominator, and any required hash or version information.
8. **Status**: `PENDING` after registration; only after the window closes and the evidence is reviewed may it become `HIT`, `FALSIFIED`, or `INDETERMINATE`. `UNKNOWN/UNVERIFIED` means the evidence chain is not closed; it is not a hit or a miss.

Review takes place after the observation window closes and places the frozen forecast text beside the outcome-side evidence. If the evidence is insufficient, record `INDETERMINATE` and preserve the gap; it remains in the due-review record but does not automatically enter an accuracy numerator or denominator.

## Results table

No record currently satisfies all three conditions—frozen before the outcome was observed, observation window closed, and outcome evidence disclosed—so the table remains empty. New records must use the same field order; historical calibration cases and structure checks must not be entered here.

| Judgment ID | Freeze time / information cutoff | Forecast content (zh / en) | Observation window (start / end) | Maturity date | Maturity rule | Outcome reveal time | Leading indicator (unit / denominator) | Audience scale and behavioural denominator | Outcome evidence (source / excerpt / access date) | Evidence unit / denominator | Evidence version / hash | Result status | Evidence class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | — | — | — | `UNKNOWN/UNVERIFIED` | No completed `GENUINE_FUTURE_OOS` record |

## Review discipline

- Build the due set from the ledger's preregistered window, falsifier, and next-review date—not from the observed result.
- A due date is not an automatic `HIT`; read the frozen card, dependencies, leading indicators, and outcome evidence item by item.
- If a review finds that most cards' falsifiers are undecidable, or that judgments were silently rewritten to fit what happened, record it as a method-failure signal in the [Judgment Evolution record](../en/03-evolution.md), rather than deleting adverse records.
- Update the Chinese and English registers in the same commit; the commit message should name the judgment ID, result change, and new evidence.
- `python3 scripts/check.py` or `npm run check` proves structure and links only; it does not upgrade this empty state into future out-of-sample evidence.

This empty state will change after the first genuine due-review round. Until then, the project reports no future accuracy.
