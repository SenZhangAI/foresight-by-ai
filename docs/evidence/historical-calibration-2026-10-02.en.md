# Historical Calibration Evidence Slice: Technology, Public Policy, and Business (2026-10-02)

> **Evidence boundary (read first):** This file is a cross-domain `CALIBRATION` slice assembled after outcomes were known. It is useful for calibrating record fields and exposing forecast failure boundaries; it does not establish accuracy, Brier scores, cross-domain discrimination, or future forecasting ability. It is neither `CONTAMINATED_RELATIVE_HOLDOUT` nor `GENUINE_FUTURE_OOS`.
>
> No cases are padded to reach a target count. Two cases have reconstructable forecast–outcome pairs; the technology case has reconstructable forecast material but its same-window outcome pair remains open, so it is explicitly retained as `UNKNOWN/UNVERIFIED`. All cases were selected or assembled on 2026-10-02; post-outcome selection limits their maximum evidence class to `CALIBRATION`.

> **How this count relates to the other files:** This is the canonical public evidence-slice navigation entry, not the repository-wide archive. The slice itself contains **2** reconstructable pairs (`P-04`, `B-WEBVAN`) + **1** `UNKNOWN/UNVERIFIED` candidate (`T-SHUTTLE`). The earlier [historical-calibration round archive](historical-calibration-round-2026-10.en.md) is another record of the same case set, not a second sample and not additive; only the next batch adds `B-ETOYS`. The repository-wide `CALIBRATION` archive contains **6** pairs; the de-duplicated methodology snapshot contains **3** pairs + 1 unknown candidate. See the [historical-retrospect count navigation](../en/01-retrospect.md#103-latest-cross-domain-evidence-slice-and-next-batch-classes-windows-and-metric-definitions-2026-10).

## 1. Classification and recording protocol

Each case records, where available: forecast owner and original material, outcome owner and original material, forecast date or information cutoff, outcome date, observation window, forecast and outcome metrics, units, population / object denominator or base, comparison rule, verbatim excerpts, repository locations, raw-byte hashes, and `unknown/unverified` gaps.

- `CALIBRATION`: selected or assembled after the outcome was visible; useful for finding rule boundaries, not for an unfrozen overall accuracy rate.
- `CONTAMINATED_RELATIVE_HOLDOUT`: requires advance freezing of an enumerable candidate population, T-before materials, strata and assignment, same-input baselines, scoring rules, and reveal order; this slice does none of that.
- `GENUINE_FUTURE_OOS`: a preregistered future judgment card reviewed after its window closes; this slice contains none.
- `UNKNOWN/UNVERIFIED`: a key original artifact, same-metric outcome, location, or denominator remains open; it is excluded from qualified counts and accuracy denominators.

## 2. Slice index

| case_id | domain | forecast and outcome | evidence class | observation window | May support | May not support |
|---|---|---|---|---|---|---|
| `P-04` | public policy / macroeconomics | FOMC forecast positive 2008 real-GDP growth; BEA same-metric outcome −0.8% | `CALIBRATION` | forecast point 2007-10-30/31; target 2008 Q4/Q4; outcome release 2009-03-26 | One reconstructable directional miss; boundary evidence that a macro central interval missed a crisis turn | Overall macro accuracy, Brier score, diffusion-gate validation |
| `B-WEBVAN` | business | Webvan projection disclosed in 1999 for 2000 revenue / net loss; 2000 10-K outcome | `CALIBRATION` | 1999-12-10 to 2000 fiscal year end; disclosed 2001-04-02 | One reconstructable corporate-scale miss; revenue, losses, and deployment assumptions should be recorded separately | Falsification of a social-diffusion rule or overall business-forecast accuracy |
| `T-SHUTTLE` | technology / aerospace | 1972 plan projected 514 Space Shuttle flights in 1979–1990; same-window outcome not reconstructed from an original mission list | `UNKNOWN/UNVERIFIED` | candidate window 1979–1990, twelve years | Evidence that technology cases must close the same-window outcome and denominator; an investigation candidate | A definite “514 versus 38” miss or a qualified-pair count |

**Current count:** two reconstructable pairs (`P-04`, `B-WEBVAN`), zero qualified technology pairs; `T-SHUTTLE` is excluded from the denominator. This is not a sample-size validation or an accuracy rate.

## 3. `P-04`: FOMC forecast for 2008 real GDP

### 3.1 Identity, original locations, and dates

- **Forecast owner:** Federal Reserve Board, FOMC participants.
- **Forecast original:** *Summary of Economic Projections, October 30–31, 2007*; repository copy [`prediction.html`](politics-artifacts/P-04/prediction.html), HTTP 200, raw-byte SHA-256 `cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`; source: <https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>.
- **Forecast date / information cutoff:** meeting dates 2007-10-30/31. The copy has no independent publication date, so 2007-10-31 is not presented as a verified publication date.
- **Outcome owner:** Bureau of Economic Analysis.
- **Outcome original:** *Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*; repository copy [`outcome.html`](politics-artifacts/P-04/outcome.html), marked 2009-03-26 08:30 EST, HTTP 200, raw-byte SHA-256 `25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`; source: <https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>.
- **Outcome date / observation end:** final-estimate release on 2009-03-26; target observation period is 2008 Q4/Q4.
- **Evidence class:** `CALIBRATION`, selected on 2026-10-02 from material with a known outcome.

### 3.2 Metric, unit, denominator, and excerpts

- **Forecast metric:** US real GDP, 2008 Q4/Q4 growth.
- **Forecast value / unit:** `+1.8%–+2.5%`, percent growth rate.
- **Denominator / base:** 2007 Q4 real GDP is the base and 2008 Q4 is the target; this is not a population denominator.
- **Forecast location:** `prediction.html` byte range `[8275,8558)`, excerpt SHA-256 `d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`; original: `central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent`.
- **Outcome metric:** same Q4/Q4 real-GDP growth rate, `−0.8%`.
- **Outcome location:** `outcome.html` byte range `[33844,34200)`, excerpt SHA-256 `484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`; original: `During 2008 ... real GDP decreased 0.8 percent.`

### 3.3 Adjudication and gaps

- **Adjudication:** the forecast interval is entirely positive and the outcome is negative: `direction miss`; the outcome is 2.6 percentage points below the lower bound and 3.3 below the upper bound.
- **Same-metric basis:** forecast footnote and outcome original both use Q4/Q4 real-GDP growth; annual-average growth, nominal GDP, per-capita GDP, and total GDP are not substituted.
- **`unknown/unverified`:** full participant-level distribution, probabilities, real-time data vintage, subsequent revision path, same-input baseline, and pre-specified scoring rule.
- **Permitted interpretation:** this supports the boundary that a smooth macro central interval may miss a crisis turn; it does not establish that macro forecasts are generally unreliable or independently falsify a diffusion gate.

## 4. `B-WEBVAN`: Webvan 2000 financial projection

### 4.1 Identity, original locations, and dates

- **Forecast owner:** a Goldman Sachs representative's investor-call projection, disclosed in Webvan's S-1 before the outcome. The disclosure is not expanded into a complete probabilistic forecast.
- **Forecast original:** Webvan S-1, filed 1999-12-10; SEC original: <https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt>; repository location, printed page, source lines 820–929, and SHA-256 `05b7375d74ddd6835230d15a6e625206b93ce78a4457fa6d28d54ceafcb55ece` are in the [business calibration packet](business-forecast-calibration-2026-09.md).
- **Forecast date / information point:** 1999-12-10; target is fiscal 2000, about twelve months to year end.
- **Outcome original:** Webvan Group, Inc. 2000 Form 10-K, filed 2001-04-02; SEC original: <https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt>; repository location, printed page, source lines 830–863, and SHA-256 `1fa9948622c6eeb5a8b15ce05ad98b0fe0b7060afae75ec17a8de4d430909e28` are in the same packet.
- **Outcome date / observation end:** 2000 fiscal-year result disclosed in the 2001-04-02 filing.
- **Evidence class:** `CALIBRATION`, selected after the outcome was known.

### 4.2 Metrics, units, denominator, and excerpts

- **Forecast metrics / unit:** Webvan 2000 fiscal-year revenue `$120.0m` and net loss `$154.3m`, in USD.
- **Object / denominator:** one company's fiscal-year financial outcomes, not user count, market total, or social adoption.
- **Forecast excerpt:** `The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.`
- **Outcome metrics / unit:** 2000 Net Sales `$178.456m` and Net Loss `$453.289m`; the 10-K table is in thousands.
- **Outcome excerpts:** `Net Sales $178,456`; `Net Loss $ (453,289)`; `Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.`

### 4.3 Adjudication and gaps

- **Adjudication:** actual revenue was about 1.49 times forecast, or 48.7% higher; actual net loss was about 2.94 times forecast, an absolute gap of about `$298.989m`, classified primarily as a `scale miss`.
- **Same-metric basis:** the primary metric is `net loss`, explicitly present on both sides; `revenue` and `Net Sales` are auxiliary and the terminology difference is not hidden.
- **`unknown/unverified`:** no probability distribution, baseline forecast, or pre-specified scoring rule; one company case cannot establish business-forecast accuracy.
- **Permitted interpretation:** the case requires separate records for revenue, losses, deployment pace, and mechanism assumptions; it is not evidence that a social-diffusion rule failed.

## 5. `T-SHUTTLE`: technology candidate with an open outcome pair

### 5.1 Reconstructable forecast material

- **Forecast owner / material:** Mathematica, Inc.'s *Economic Analysis of the Space Shuttle System: Executive Summary* (NASA-CR-129570), prepared for NASA.
- **Forecast source:** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>; title-page date 1972-01-31; location §0.2.2 p. 0-7 and Table 0.1 p. 0-8.
- **Verbatim excerpt:** `from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year`.
- **Forecast metric / unit:** 514 Space Shuttle flights in 1979–1990, twelve years; point value 514, annual average 43.
- **Object denominator:** the twelve-year window and planned mission count; the material describes a NASA / DoD mission-model planning and economic scenario, not a probabilistic forecast.
- **Evidence class:** `UNKNOWN/UNVERIFIED`, not a calibration pair.

### 5.2 Why the outcome cannot yet be filled

- The located NASA history-resources page, <https://www.nasa.gov/history/space-shuttle-history-resources/>, confirms only 135 missions for the whole program from 1981-04-12 through 2011-07-21.
- 135 is a whole-program total, not the same-window 1979–1990 subset; the page contains no original year-by-year or mission-level table.
- Missing: an official NASA year-by-year or mission list, dates and locations for each mission, and a pre-fixed denominator rule for the no-launch years 1979–1980.
- Therefore the unverified retelling “38 flights from 1981–1990” cannot be written as the outcome, and the case cannot be presented as a definite “514 versus 38” miss.
- **Upgrade condition:** obtain and check an official same-window mission list item by item and fix the denominator treatment. Otherwise retain `UNKNOWN/UNVERIFIED`.

## 6. What this material changes and does not change

**Supports:**

1. Cross-domain cases must retain forecast timing, outcome window, metric, unit, denominator / base, original locations, excerpts, and gaps; topical similarity is not same-metric evidence.
2. A macro central interval may miss a crisis turn; near-correct company revenue does not imply loss-scale calibration; a technology planning scenario cannot become a miss without a same-window mission list.
3. Technology cases must separate capability, planning scenario, financing threshold, market-size estimate, and probabilistic forecast; these evidence types cannot be pooled.

**Does not support:**

- No accuracy rate, Brier score, hit rate, or cross-domain discrimination increment.
- No conversion into `CONTAMINATED_RELATIVE_HOLDOUT`: no population, T-before packet, assignment, same-input baseline, scoring rule, or one-shot reveal was frozen in advance.
- No claim that the five diffusion gates have been validated or that one has been falsified.
- No new future judgment card; genuine `GENUINE_FUTURE_OOS` evidence still requires preregistration and a future window to mature.

## 7. Traceable entry points and bilingual constraint

- Method boundary: [Historical Pseudo-Out-of-Sample Validation Protocol](../en/02-historical-validation-protocol.md).
- Existing cross-domain round: [Historical Calibration Round](historical-calibration-round-2026-10.en.md).
- Political materials: [Political Calibration Packet](politics-calibration.en.md) and `politics-artifacts/P-04/`.
- Business materials: [Business Forecast Calibration Packet](business-forecast-calibration-2026-09.en.md).
- Technology materials: [Technology Calibration Addendum](technology-calibration-addendum-2026-10.en.md); this slice adds only the reconstructability boundary for `T-SHUTTLE` and does not upgrade it to a qualified case.
- Chinese mirror: [历史校准证据切片](historical-calibration-2026-10-02.md). Both files share case IDs, evidence classes, dates, metrics, and gaps; English is not an independent count.

**Slice delivery conclusion:** two reconstructable `CALIBRATION` pairs (one public-policy, one business) and one technology `UNKNOWN/UNVERIFIED` candidate; no relative holdout, genuine future out-of-sample evidence, or accuracy claim.
