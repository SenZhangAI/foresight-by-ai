# Historical misfit boundary slice: institutional outcomes, national outcomes, and counterfactual metrics (2026-10)

[中文版](historical-misfit-calibration-2026-10.md) · [Politics calibration packet](politics-calibration.en.md) · [English retrospective §10.7](../en/01-retrospect.md#107-narrow-slice-institutional-outcomes-nationwide-outcomes-and-counterfactual-metrics)

> **Read the status boundary first:** This page extracts four already-registered political cases into a narrow slice; it adds no future judgment, opportunity candidate, or diffusion gate. P-01 and P-02 were assembled after their outcomes were known and are labelled `CALIBRATION`; P-03 and P-05 remain incomplete and are labelled `UNKNOWN/UNVERIFIED`. This is not a holdout and provides no accuracy, hit-rate, or out-of-sample evidence.

## 1. Slice question and selection rule

This slice attacks one recording boundary: **the object named by a forecast must be the same object, metric, denominator, and observation window used for the outcome check; “nearby direction” cannot stand in for an institutional outcome, “entering the capital” cannot stand in for nationwide takeover, and actual growth cannot stand in for a counterfactual level difference.**

All four cases come from the existing [politics calibration packet](politics-calibration.en.md), so no new search material or retrospective story has been mixed in. The selection rule is:

1. the forecast predates the target outcome and the original material is locatable;
2. the forecast target, forecast date, outcome window, and comparison rule can be stated;
3. if the outcome artifact, denominator, or metric is not closed, preserve `UNKNOWN/UNVERIFIED` rather than guessing to create a “miss”;
4. this slice changes only the evidence-record boundary: it adds no lens, changes no diffusion gate, and produces no future forecast.

## 2. Four-case register

| case_id | Domain and object | Forecast date and original location | Observation window and outcome location | Metric / denominator | Status and conclusion |
|---|---|---|---|---|---|
| P-01 | UK Brexit referendum: Remain / Leave winner direction | 2016-06-23; YouGov *on the day poll*, original [`prediction.html`](politics-artifacts/P-01/prediction.html); full declaration and byte range in [politics packet §P-01](politics-calibration.en.md#p-01--uk-eu-referendum-yougov-on-the-day-poll-reversed-the-direction) | 2016-06-24; UK Prime Minister's Office result page, original [`outcome.html`](politics-artifacts/P-01/outcome.html) | Same referendum question; percentages and first-place direction, with referendum voters as the base | `CALIBRATION`: the forecast made Remain more likely to win; Leave won. This is a `direction` miss, not a forecast of institutional or long-run economic consequences |
| P-02 | UK 2017 general election: Conservative majority government | 2017-06-07; YouGov *Final call poll*, original [`prediction.html`](politics-artifacts/P-02/prediction.html); excerpt in [politics packet §P-02](politics-calibration.en.md#p-02--2017-uk-general-election-majority-government-forecast-failed) | 2017-06-08 is the election outcome; the House of Commons Library page was published 2019-01-29, original [`outcome.html`](politics-artifacts/P-02/outcome.html) | Institutional outcome: whether any party won an overall Commons majority; not vote share substituted for majority | `CALIBRATION`: the forecast expected an increased Conservative majority; the result was a hung Parliament. This is an institutional-outcome `direction` miss, not proof that the vote-share estimate was also wrong |
| P-03 | “Nationwide takeover” after the 2021 Afghanistan withdrawal | Fixed candidate register dated 2026-09-29; forecast copy [`prediction.html`](politics-artifacts/P-03/prediction.html) is preserved | The available material does not preserve the CRS / official outcome original in the repository; a URL or search snippet does not close the outcome | Target is nationwide takeover; “entered the capital” or partial control cannot substitute for nationwide control | `UNKNOWN/UNVERIFIED`: missing outcome original, stable excerpt, and nationwide denominator. Excluded from miss and accuracy denominators. Stop conditions are in the [politics packet's unverified candidates](politics-calibration.en.md#stop-conditions-for-unverified-candidates) |
| P-05 | Post-Brexit UK GDP counterfactual shock | Fixed candidate register dated 2026-09-29; forecast original [`prediction.html`](politics-artifacts/P-05/prediction.html) and candidate note are in the [politics packet register](politics-calibration.en.md#fixed-candidate-register-do-not-delete-rows) | An outcome page [`outcome.html`](politics-artifacts/P-05/outcome.html) exists, but supplies actual annual growth rather than the same counterfactual series | Forecast is the two-year level difference relative to a Remain baseline; outcome lacks the same counterfactual baseline mapping | `UNKNOWN/UNVERIFIED`: actual annual growth cannot replace a relative counterfactual level; excluded from miss and accuracy denominators. Stop conditions are in the [politics packet's unverified candidates](politics-calibration.en.md#stop-conditions-for-unverified-candidates) |

## 3. Case comparison and what can be determined

### P-01: referendum direction, not institutional consequences

YouGov's pre-T statement ranked Remain first and called a Remain win more likely; the official result confirmed Leave. Both sides answer the same question, and the window runs from the election-day forecast to the result announcement, so the case is `CALIBRATION`. It supports only the narrow conclusion that the forecast missed the **winner direction**. It contains no forecast–outcome pair for post-Brexit GDP, trade, migration, or institutional stability, so the direction miss must not be expanded into “the consequence forecast also failed.”

### P-02: vote share is not a Commons majority

The forecast object is an increased Conservative majority government; the outcome object is that no party won an overall majority. Both are institutional outcomes and are directly comparable. The same House of Commons Library page also reports seats and vote shares, but this slice uses only the binary majority-government metric, preventing 42.3% / 40.0% vote shares from being substituted for a Commons majority. The supported boundary is: **an institutional threshold must be encoded separately; an adjacent continuous opinion metric cannot replace it.**

### P-03: the nationwide outcome is not closed

The forecast copy exists and points to a nationwide outcome, but the repository does not preserve a checkable CRS / official outcome original, nor does it fix “entered the capital,” “controlled most territory,” and “nationwide takeover” as separate codes. Writing “the forecast was wrong” now would substitute narrative for an outcome definition. The case therefore remains `UNKNOWN/UNVERIFIED`; the next step is to add the outcome original, publisher, date, excerpt location, and nationwide denominator before judging it.

### P-05: a counterfactual series cannot be patched with actual growth

The forecast asks for the two-year GDP level difference relative to a “Remain” baseline; the available outcome page reports actual annual growth. Even though both mention GDP, they do not share a comparison base. Without the counterfactual series, forecast direction or magnitude cannot be judged; adding a seemingly related annual-growth figure would create false closure. The case remains unknown and does not enter the calibration denominator.

## 4. Method boundary returned to the project

This slice supports only these three recording rules:

1. **Separate direction on the same question from consequences.** P-01 can judge the referendum winner direction; it cannot judge economic or institutional consequences by substitution.
2. **Separate institutional outcomes from continuous indicators.** P-02 must be checked against whether a Commons majority formed, not against vote share.
3. **The same topic is not the same metric.** P-03's nationwide takeover and partial control, and P-05's counterfactual GDP and actual annual growth, cannot be exchanged because they are thematically related.

It does not support:

- overall political-forecast accuracy, method hit rate, or Brier score;
- a new forecasting lens, diffusion gate, or society-level trend;
- writing P-03 or P-05 as definite misses;
- counting existing P-01 and P-02 again as new repository cases.

The four evidence classes are fixed by the original politics packet: `CALIBRATION=2` (P-01, P-02), `UNKNOWN/UNVERIFIED=2` (P-03, P-05). This page is a public-readable boundary slice; it does not change the repository-wide `CALIBRATION` count and does not trigger an isolated full re-review.

## 5. Sources and evidence levels

- **Strong:** the [politics calibration packet](politics-calibration.en.md)'s fixed candidate register, P-01 / P-02 forecast and outcome originals, and their SHA-256 hashes, excerpt ranges, and source URLs.
- **Medium:** the P-03 / P-05 candidate register and stop conditions; they explicitly document gaps but do not provide countable closed outcomes.
- **Boundary note:** this page does not promote search snippets, memory, or nearby metrics into original outcomes. `UNKNOWN/UNVERIFIED` is part of the delivery, not a missing quota of “failed” cases.
