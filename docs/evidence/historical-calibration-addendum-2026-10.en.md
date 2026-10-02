# Historical Evidence Addendum: FOMC Forecast for 2008 Real GDP

> **Evidence level: `CALIBRATION`, not relative `holdout` and not future out-of-sample evidence.** This case was selected from the repository's existing political calibration packet after the outcome was known and observable. It is a reproducible historical calibration record and a method-boundary test; it does not establish improved relative discrimination or future accuracy.

## 1. Case identity and selection timing

- **case_id:** `P-04`
- **Domain:** macroeconomics / public policy
- **Forecast owner:** Federal Reserve Board, FOMC participants
- **Forecast artifact:** *Summary of Economic Projections, October 30–31, 2007*
- **Repository forecast artifact:** [`prediction.html`](politics-artifacts/P-04/prediction.html); original response `HTTP 200`; SHA-256: `cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`
- **Forecast source:** <https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>
- **Forecast date / information cutoff:** 2007-10-30/31 (meeting dates and information cutoff). The artifact has no independent publication date; 2007-10-31 must not be presented as a verified publication date.
- **Outcome artifact:** Bureau of Economic Analysis, *Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*
- **Repository outcome artifact:** [`outcome.html`](politics-artifacts/P-04/outcome.html); the page marks release at 2009-03-26 08:30 EST; original response `HTTP 200`; SHA-256: `25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`
- **Outcome source:** <https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>
- **Outcome date / observation end:** final-estimate release on 2009-03-26; the target observation period is 2008 Q4/Q4 real GDP growth.
- **Selection date for this addendum:** 2026-10-02. Selection after the outcome was known makes the case `CALIBRATION` only.

## 2. Forecast/outcome pairing on the same metric

### Forecast

The repository artifact contains this locatable excerpt:

> “central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent”

- **forecast_metric:** US real GDP growth, 2008 Q4/Q4.
- **forecast_value:** 1.8%–2.5% (participants' central-tendency interval).
- **unit:** percent growth rate.
- **population/base:** US real GDP; 2007 Q4 base and 2008 Q4 target.
- **threshold / comparison rule:** the entire forecast interval is above zero; an outcome below zero is a directional miss.
- **Artifact location:** `prediction.html` byte range `[8275,8558)`; excerpt SHA-256: `d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`.

### Outcome

The repository artifact contains this locatable excerpt:

> “During 2008 ... real GDP decreased 0.8 percent.”

- **outcome_metric:** US real GDP growth, 2008 Q4/Q4.
- **outcome_value:** −0.8%.
- **unit:** percent growth rate.
- **population/base:** US real GDP; the same 2007 Q4 to 2008 Q4 comparison as the forecast.
- **Artifact location:** `outcome.html` byte range `[33844,34200)`; excerpt SHA-256: `484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`.

**Comparability finding:** both the forecast footnote and outcome artifact use Q4/Q4 real GDP growth. This pairing does not replace Q4/Q4 growth with annual-average growth, and does not substitute total GDP, nominal GDP, or per-capita GDP. It is therefore a same-metric directional and interval comparison. The denominator is not population; it is the 2007 Q4 real-GDP base implicit in the growth-rate definition. The forecast artifact does not provide a complete participant-level distribution from which individual probabilities or a weighted mean could be reconstructed, so those fields remain unknown.

## 3. Adjudication

- **Direction:** the forecast interval is positive (+1.8% to +2.5%), while the outcome is −0.8%; this is a `direction miss`.
- **Interval error:** the outcome is 2.6 percentage points below the forecast lower bound and 3.3 points below the upper bound. This describes this case only and cannot be converted into a population accuracy rate.
- **Timing:** forecast point 2007-10-30/31; target period 2008 Q4/Q4; outcome artifact released 2009-03-26. The forecast predates the target outcome.
- **Observation window:** 2008 Q4/Q4; the outcome artifact is a final release, but that does not prove all later historical revisions were exhausted.
- **Missing / unverified:** `unknown/unverified`: the full participant-level forecast distribution, forecast probabilities, real-time GDP data vintage at the forecast point, subsequent revision path, the complete inputs to same-time baseline forecasts, and a pre-specified comparative scoring rule. Without these fields, Brier score, log score, relative discrimination increment, and cross-case accuracy cannot be computed.

## 4. What it supports and what it does not

**Supports:** This is a source-locatable historical miss with a clear time order and comparable forecast/outcome metric. It specifically attacks the optimistic assumption that a smooth macro baseline is sufficient to cover tail transmission or crisis turning points: a positive interval did not cover the negative 2008 outcome. Future macro judgments should separately record the baseline scenario, tail risks, trigger conditions, and data vintage rather than only a central interval.

**Does not support:** This is a single `CALIBRATION` case selected after the outcome was known. It was not assigned from a frozen population as a relative `holdout`; it has no same-input baseline, pre-sealed scoring rule, or batch denominator. It therefore cannot support claims that method accuracy improved, that macro forecasts are generally unreliable, or that a specific diffusion gate has been falsified. It adds no future trend forecast.

## 5. Relation to the historical-validation protocol

This record follows the boundary in the [historical pseudo-out-of-sample validation protocol](../en/02-historical-validation-protocol.md): a case selected after its outcome is known may be used for `CALIBRATION`, but may not be presented as a holdout. Upgrading evidence to a relative holdout would require a separate run that freezes an as-yet-unrevealed enumerable candidate population, T-before materials, strata and assignment, same-input baselines, scoring rules, and reveal order. This addendum does not run those steps.

**Round conclusion:** the new deliverable is one reproducible calibration record and one method boundary, not an accuracy claim. Genuine future out-of-sample evidence still requires preregistered judgment cards to mature and be reviewed after their windows close.
