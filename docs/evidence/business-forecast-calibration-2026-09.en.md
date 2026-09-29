# Commercial Forecast Misses: Reproducible Evidence Packet (2026-09)

> **Purpose**: This file is the evidence packet for the second historical-calibration round in `docs/en/01-retrospect.md`. It uses only verbatim excerpts and stable source locations delivered with the repository. These are `CALIBRATION` cases, not out-of-sample accuracy results and not holdout cases.
>
> **Evidence rule**: A forecast must precede the target outcome; the outcome must use the same metric or explicitly state why it is not comparable; a secondary retelling cannot replace an original filing. SHA-256 hashes of the downloaded SEC full submissions are recorded so readers can redownload and verify the excerpts.

## Case A · Webvan: revenue was directionally close, but loss scale was badly misestimated

### Pre-T forecast source

- **Forecast owner / source**: A Goldman Sachs representative gave projections during an investor conference call; Webvan's S-1 disclosed the statement and its provenance and limitations before the target year.
- **Disclosure date**: 1999-12-10 (S-1 filed); the projection appears under the risk-factor heading `OUR LIMITED OPERATING HISTORY MAKES FINANCIAL FORECASTING DIFFICULT FOR US AND FOR FINANCIAL ANALYSTS THAT MAY PUBLISH ESTIMATES OF OUR FINANCIAL RESULTS`, followed by the paragraph beginning `The article also referred to...`.
- **Stable source**: [SEC full submission 0000891618-99-004914](https://www.sec.gov/Archives/edgar/data/1092657/000089161899004914/0000891618-99-004914.txt)
- **Location**: Printed page 13 of the SEC text (`<PAGE> 13`), the above `Risk Factors` section and its `The article also referred to...` paragraph, source lines 820–929; SHA-256 `05b7375d74ddd6835230d15a6e625206b93ce78a4457fa6d28d54ceafcb55ece`.

**Verbatim excerpt (original wording and figures retained)**:

> “The representative of Goldman, Sachs & Co. stated during the call that its financial projections for our company were: $11.9 million of revenue and a $73.8 million net loss for the year 1999, $120.0 million of revenue and a $154.3 million net loss for the year 2000 and $518.2 million of revenue and a $302 million net loss for the year 2001.”
>
> “These projections are based upon a number of estimates and assumptions and are inherently subject to significant uncertainties and contingencies, including the timing and cost of our distribution center roll-out, the volume and size of customer orders, market penetration and competition.”

**Frozen pre-T metrics**: 2000 revenue `$120.0m`; 2000 net loss `$154.3m`; 2001 revenue `$518.2m`; 2001 net loss `$302m`. The primary same-metric window is the 2000 fiscal year, approximately twelve months from forecast disclosure to year end.

### Outcome source

- **Outcome source**: Webvan Group, Inc., 2000 Form 10-K filed 2001-04-02.
- **Stable source**: [SEC full submission 0001012870-01-001485](https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt)
- **Location**: Printed page 12 of the SEC text, the `Consolidated Statements of Operations Data` table under `ITEM 6. SELECTED CONSOLIDATED FINANCIAL DATA` (`Net Sales` / `Net Loss` rows), source lines 830–863; SHA-256 `1fa9948622c6eeb5a8b15ce05ad98b0fe0b7060afae75ec17a8de4d430909e28`.

**Verbatim excerpts**:

> “Net Sales                                                            $    178,456    $     13,305   $         -”
>
> “Net Loss                                                             $   (453,289)   $   (144,569)  $   (12,004)”
>
> “Net sales were $178.5 million for 2000 compared to $13.3 million for 1999.”

The table states `(In thousands, except share and per share data)`, so 2000 actual net sales were `$178.456m` and actual net loss was `$453.289m`.

### Classification

- **Revenue scale**: forecast `$120.0m`, actual `$178.456m`; actual was about 1.49 times forecast, a +48.7% deviation. This is a measurable scale error, but not a reversal of demand direction.
- **Loss scale**: forecast net loss `$154.3m`, actual `$453.289m`; actual loss was about 2.94 times forecast, an absolute difference of about `$298.989m`. This is a `scale` miss, with losses underestimated.
- **Mechanism / timing**: the forecast source itself lists rollout timing, order volume, market penetration, and competition as assumptions that must be separated in future records. The outcome does not establish that any one variable alone caused the miss.
- **Independence**: this is an e-commerce infrastructure and organizational-expansion forecast, not the same forecaster, metric, or source as the existing Forrester US online-retail-total series.

### Rule impact

This case **does not overturn any of the five diffusion gates**: it tests numerical calibration of a corporate financial projection, not whether a capability becomes a society-wide habit. It adds a boundary to the method instead: commercial forecasts must separately log revenue scale, loss scale, deployment pace, and mechanism assumptions; a correct revenue direction does not make the cost structure or profit forecast a hit.

## Case B · Iridium: pre-T subscriber and revenue thresholds were missed by the first quarter

### Pre-T forecast source

- **Source**: Iridium World Communications Ltd.; the sole pre-T original used for this case is its `424B4` prospectus filed 1999-01-25. This source is not part of the Forrester series. It discloses the minimum revenue and subscriber levels required by its secured bank facility at future dates. These are dated, testable financing-covenant targets available before the outcomes; this case treats them as commercial target thresholds and does not mislabel them as an ordinary probabilistic forecast.
- **Stable source**: [SEC full submission 000095013399000162](https://www.sec.gov/Archives/edgar/data/948421/000095013399000162/0000950133-99-000162.txt)
- **Location**: Pages 17–18 of the SEC text (`<PAGE> 17`–`<PAGE> 18`), the risk-factor / covenant section headed `IRIDIUM MAY BE UNABLE TO SATISFY OR MAY BE ADVERSELY CONSTRAINED BY THE COVENANTS IN ITS BANK FACILITIES AND DEBT SECURITIES`, source lines 1258–1272; SHA-256 `762d4dac8b26a55cddf805c3e135df51b3173ad956ac72576f1ec33e02956109`.

**Verbatim excerpts**:

> “IRIDIUM MAY BE UNABLE TO SATISFY OR MAY BE ADVERSELY CONSTRAINED BY THE COVENANTS IN ITS BANK FACILITIES AND DEBT SECURITIES”
>
> “at March 31, 1999 it have cumulative cash revenues of at least $4 million, cumulative accrued revenues of at least $30 million, at least 27,000 Iridium World Satellite Service subscribers and at least 52,000 total subscribers;”
>
> “at June 30, 1999 it have cumulative cash revenues of at least $50 million, cumulative accrued revenues of at least $150 million, at least 88,000 Iridium World Satellite Service subscribers and at least 213,000 total subscribers; and”
>
> “at September 30, 1999 it have cumulative cash revenues of at least $220 million, cumulative accrued revenues of at least $470 million, at least 173,000 Iridium World Satellite Service subscribers and at least 454,000 total subscribers.”

**Frozen pre-T metrics**: by 1999-03-31, cumulative cash revenue `$4m`, cumulative accrued revenue `$30m`, Iridium World Satellite Service subscribers `27,000`, and total subscribers `52,000`.

### Outcome source

- **Outcome source**: Iridium LLC, Q1 1999 Form 10-Q filed 1999-05-17; the results are as of 1999-03-31, within the target horizon, and the filing explicitly explains the waiver.
- **Stable source**: [SEC full submission 000095013399001884](https://www.sec.gov/Archives/edgar/data/948421/000095013399001884/0000950133-99-001884.txt)
- **Location**: Page 24 of the SEC text (`<PAGE> 24`), section heading `Iridium Expects that it Will Not Satisfy the Secured Bank Facility Revenue and Subscriber Covenants`, source lines 1729–1760; SHA-256 `ce3e246e41856e395be0c36ed39419a6e566fc02eacb14c5153811c15fd0b8c8`.

**Verbatim excerpts**:

> “As a result of various factors, Iridium's subscriber levels and revenues have been significantly below its prior estimates.”
>
> “As of March 31, 1999, Iridium had $195,000 of cumulative cash revenues, $1.637 million of cumulative accrued revenues, 7,188 Iridium World Satellite Service subscribers and 10,294 total subscribers.”
>
> “Iridium now expects that it will not satisfy the secured bank facility's May 31, 1999 (extended from March 31, 1999) minimum subscriber and revenue covenants and also expects that it will not be able to satisfy the June 30, 1999 and September 30, 1999 covenants.”

### Classification

- **Cash revenue**: `$0.195m / $4m = 4.875%`; about 4.9% of target.
- **Cumulative accrued revenue**: `$1.637m / $30m ≈ 5.46%`; about 5.5% of target.
- **Service subscribers**: `7,188 / 27,000 ≈ 26.6%`.
- **Total subscribers**: `10,294 / 52,000 ≈ 19.8%`.
- **Classification**: `scale` (the revenue and subscriber targets substantially overestimated actual results) + `timing` (the first covenant date was missed) + `mechanism` (commercial rollout, equipment distribution, service providers, and marketing coordination did not form as earlier estimates assumed; this packet cites only what the filing supports and does not inflate it into a single-cause explanation).

### Rule impact

This case likewise **does not overturn any of the five diffusion gates**. It cannot isolate whether Gate 1, Gate 3, or Gate 4 alone stopped satellite telephony, because the target was jointly exposed to financing covenants, equipment supply, service providers, and market adoption. It exposes another methodological boundary: **a record must distinguish a target / covenant threshold from a probabilistic forecast**; both can be tested, but they are not the same kind of forecast evidence. It also reminds us that a technically complete system does not imply that the commercial adoption curve will follow a capital plan.

## Cross-case conclusion: what changes and what does not

1. **Change the evidence requirement, not the five-gate conclusion**: a commercial forecast record must include metric, unit, target date, source identity (company / underwriter / financing covenant), the pre-T location, and an outcome source; correct revenue direction does not erase loss-scale error.
2. **Do not treat these as holdout cases**: both were selected after their historical outcomes were visible, so they are `CALIBRATION` and cannot support a claim that method accuracy improved.
3. **Do not smuggle “commercial forecast miss” into “diffusion rule falsified”**: Webvan and Iridium are useful counterevidence, but neither isolates an exclusive failure mechanism for one of the five gates. The honest update is a stronger boundary and recording discipline, not a revision to Gates 1–5.
4. **Next testable direction**: pre-freeze ordinary cases from the initial SEC S-1/F-1 population, encode revenue, loss, subscriber/customer, and deployment milestones separately, and set error thresholds before opening results. Only then can cases enter the historical pseudo-out-of-sample protocol instead of continuing to select famous failures.
