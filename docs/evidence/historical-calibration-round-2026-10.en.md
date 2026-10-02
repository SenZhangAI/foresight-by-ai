# Historical Calibration Round: Cross-Domain Forecast–Outcome Records (2026-10)

> **Evidence boundary:** This file records cases assembled after their outcomes were known. They are `CALIBRATION`, not relative `holdout` and not genuine future out-of-sample evidence. They expose historical misses and evidence gaps; they cannot establish accuracy, Brier scores, or a cross-domain discrimination increment.
>
> **No new future judgment is added in this round.** The technology direction still has no qualified pair under the strict threshold. Retaining `unknown/unverified` is the result; similar metrics are not used to manufacture a case count.

## 1. Recording rules and classifications

Each record includes the forecast date or information cutoff, outcome date and observation window, forecast and outcome metrics, units, population / object denominator or base, original-material locations, outcome-material locations, excerpts, and explicit missing fields. Classifications are:

- `CALIBRATION`: selected or assembled after the outcome was visible; usable for finding rule boundaries.
- `CONTAMINATED_RELATIVE_HOLDOUT`: usable only after the candidate population, T-before materials, assignment, same-input baselines, and reveal order were frozen in advance; this round has none.
- `GENUINE_FUTURE_OOS`: a preregistered future judgment card reviewed after maturity; this round has none.
- `UNKNOWN/UNVERIFIED`: at least one key artifact, comparable outcome, or location is not closed; it is not counted as a qualified case or accuracy denominator.

All cases were selected or assembled on 2026-10-02. Therefore every paired case in this file is `CALIBRATION` only.

## 2. Case table

| case_id | domain | forecast–outcome | evidence class | observation window | conclusion |
|---|---|---|---|---|---|
| `P-04` | macroeconomics / public policy | FOMC forecast positive 2008 real-GDP growth; BEA outcome negative | `CALIBRATION` | 2008 Q4/Q4; forecast point to 2009-03-26 release | Qualified same-metric directional miss; no accuracy claim |
| `B-WEBVAN` | business | 1999-disclosed 2000 revenue / net-loss projection; 2000 10-K outcome | `CALIBRATION` | 1999-12-10 to 2000-12-31 | Qualified numeric-scale miss; not evidence that a diffusion rule failed |
| `T-SHUTTLE` | technology / aerospace | 1972 Space Shuttle flight plan; outcome subset not reconstructed from originals | `UNKNOWN/UNVERIFIED` | 1979–1990 candidate window | Excluded; same-window result and denominator are missing |

**Counting rule:** two qualified paired cases in this round (`P-04`, `B-WEBVAN`), both calibration; zero qualified technology pairs. The count is not an accuracy rate or method validation.

## 3. P-04 · FOMC forecast for 2008 real GDP

### Identity and timing

- **Forecast owner:** Federal Reserve Board, FOMC participants.
- **Forecast artifact:** *Summary of Economic Projections, October 30–31, 2007*.
- **Forecast original:** [`politics-artifacts/P-04/prediction.html`](politics-artifacts/P-04/prediction.html), HTTP 200, SHA-256 `cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`; source: <https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>.
- **Forecast date / information cutoff:** 2007-10-30/31 meeting dates. The artifact has no independent publication date, so 2007-10-31 is not presented as a verified publication date.
- **Outcome owner:** Bureau of Economic Analysis.
- **Outcome artifact:** [`politics-artifacts/P-04/outcome.html`](politics-artifacts/P-04/outcome.html), marked 2009-03-26 08:30 EST, HTTP 200, SHA-256 `25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`; source: <https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>.
- **Outcome date / observation end:** final-estimate release on 2009-03-26; target window is 2008 Q4/Q4 real-GDP growth.

### Metric, denominator, and excerpts

- **Forecast metric / unit:** US real GDP, 2008 Q4/Q4, percent growth rate; interval `+1.8%–+2.5%`.
- **Object / base:** US real GDP; 2007 Q4 base and 2008 Q4 target. The denominator is the real-GDP base implicit in the growth rate, not population.
- **Forecast excerpt:** `prediction.html` byte range `[8275,8558)`; excerpt SHA-256 `d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`:
  > “central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent”
- **Outcome metric / unit:** same Q4/Q4 real-GDP growth rate, `−0.8%`.
- **Outcome excerpt:** `outcome.html` byte range `[33844,34200)`; excerpt SHA-256 `484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`:
  > “During 2008 ... real GDP decreased 0.8 percent.”

### Adjudication and gaps

- **Adjudication:** the forecast interval is entirely positive and the outcome negative: `direction miss`; the outcome is 2.6 percentage points below the lower bound and 3.3 below the upper bound.
- **Comparability:** both forecast footnote and outcome artifact use Q4/Q4 real-GDP growth; neither annual-average growth, nominal GDP, nor per-capita GDP substitutes for the metric.
- **Missing / unverified:** full participant distribution, probabilities, real-time data vintage, revision path, same-input baseline, and a pre-specified scoring rule are unknown. Brier score, log score, relative discrimination, and overall hit rate therefore cannot be computed.
- **Method boundary:** a smooth macro baseline may miss tail transmission or crisis turning points; future macro judgments should separately state a baseline, tail risks, triggers, and data vintage. This case does not by itself falsify a diffusion gate.

## 4. B-WEBVAN · Webvan 2000 financial projection

### Identity and timing

- **Forecast owner:** a Goldman Sachs representative's projection in an investor call, disclosed before the outcome in Webvan's S-1; this record does not turn the disclosure into a complete probabilistic forecast.
- **Forecast artifact:** Webvan S-1, filed 1999-12-10; original: <https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt>; repository location, page, line, and SHA-256 are recorded at lines 8–21 of [`business-forecast-calibration-2026-09.md`](business-forecast-calibration-2026-09.md).
- **Forecast date / information point:** 1999-12-10; target is fiscal year 2000.
- **Outcome artifact:** Webvan Group, Inc. 2000 Form 10-K, filed 2001-04-02; original: <https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt>; source location, page, lines, and SHA-256 are recorded at lines 23–37 of the same packet.
- **Outcome date / observation window:** fiscal-year outcome disclosed on 2001-04-02; approximately 12 months from forecast point to fiscal year end.

### Metric, denominator, and excerpts

- **Forecast metric / unit:** 2000 revenue `$120.0m`, 2000 net loss `$154.3m`; USD. The 2001 figures remain in the original but are outside this observation window.
- **Object / denominator:** Webvan's 2000 fiscal-year revenue and net loss; not user count, market total, or social adoption.
- **Forecast excerpt:**
  > “The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.”
- **Outcome metric / unit:** 2000 Net Sales `$178.456m`, Net Loss `$453.289m`; the original table is in thousands.
- **Outcome excerpts:**
  > “Net Sales $178,456”
  >
  > “Net Loss $ (453,289)”
  >
  > “Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.”

### Adjudication and gaps

- **Revenue scale:** actual was approximately 1.49 times forecast, about 48.7% higher.
- **Net-loss scale:** actual was approximately 2.94 times forecast, an absolute gap of about `$298.989m`; primary class is `scale miss`.
- **Comparability:** the primary metric is `net loss`, explicitly present on both sides; `revenue` and `Net Sales` are auxiliary and the terminology difference is not hidden.
- **Missing / unverified:** the forecast artifact gives a projection and assumptions, not a probability distribution, baseline forecast, or pre-specified scoring rule; one case cannot establish business-forecast accuracy.
- **Method boundary:** near-correct revenue direction does not cover a loss-scale error; commercial forecasts should separate revenue, losses, deployment pace, and mechanism assumptions. This case does not by itself falsify the five social-diffusion gates.

## 5. T-SHUTTLE · Unverified technology candidate

### Located forecast material

- **Forecast owner / artifact:** Mathematica, Inc.'s *Economic Analysis of the Space Shuttle System: Executive Summary* (NASA-CR-129570), prepared for NASA.
- **Forecast artifact:** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>; title-page date 1972-01-31; §0.2.2 p. 0-7 and Table 0.1 p. 0-8.
- **Forecast excerpt:** “from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year”.
- **Forecast metric / unit:** 514 Space Shuttle flights during 1979–1990, 43 per year; the material identifies this as a NASA / DoD mission-model planning and economic scenario, not a probabilistic forecast.

### Outcome material and missing fields

- **Currently located outcome source:** NASA's history-resources page, <https://www.nasa.gov/history/space-shuttle-history-resources/>, confirms only 135 missions for the whole program from 1981-04-12 to 2011-07-21.
- **Why it cannot be paired:** 135 is a whole-program total, not the 1979–1990 (or explicitly adjusted 1979–1980) same-window subset; the page has no year-by-year or mission-level original table.
- **Missing:** a NASA mission compilation or official year-by-year list, dates and locations for each mission, and a pre-specified treatment of the 1979–1990 denominator. The unverified retelling “38 flights from 1981–1990” is not counted.
- **Classification:** `UNKNOWN/UNVERIFIED`; no lawful outcome excerpt can be filled, so this is not written as a definite “514 versus 38” miss and is excluded from the qualified count.
- **Stop condition:** only a same-window official mission list that can be checked item by item may upgrade this candidate to a calibration pair; otherwise the gap remains open.

## 6. What this round supports and does not support

**Supports:**

1. Cross-domain records must retain forecast time, outcome window, metric, unit, denominator / base, original locations, excerpts, and missing fields.
2. The FOMC case shows that a macro central interval can miss a crisis turn; Webvan shows that near-correct revenue direction does not imply loss-scale calibration.
3. Technology cases must settle same-window outcomes and denominators before calling a forecast a miss; capabilities, planning scenarios, financing covenants, market estimates, and probabilistic forecasts must not be conflated.

**Does not support:**

- No accuracy rate, Brier score, overall hit rate, or cross-domain discrimination increment.
- No conversion of calibration into relative holdout; this round froze none of the required population, T-before packet, assignment salt, same-input baseline, or one-shot reveal.
- No claim that the five diffusion gates were validated or that one was falsified.
- No new future forecast; genuine out-of-sample evidence still comes from future preregistered judgment cards after their windows mature.

## 7. Reproducible entry points and bilingual parity

- Method boundary: [Historical Pseudo-Out-of-Sample Validation Protocol](../en/02-historical-validation-protocol.md).
- Political materials: [Political Calibration Packet](politics-calibration.en.md) and `politics-artifacts/P-04/`.
- Business materials: [Business Forecast Calibration Packet](business-forecast-calibration-2026-09.en.md).
- Technology gap: [Technology Calibration Addendum](technology-calibration-addendum-2026-10.en.md).
- Chinese mirror: [历史校准轮：跨领域预测—结果记录（2026-10）](historical-calibration-round-2026-10.md). Both files share case IDs, classes, and conclusions; English is not an independent count.

**Round delivery conclusion:** two reproducible `CALIBRATION` pairs and one explicit technology `UNKNOWN/UNVERIFIED` gap; no holdout, genuine future out-of-sample evidence, or accuracy claim.