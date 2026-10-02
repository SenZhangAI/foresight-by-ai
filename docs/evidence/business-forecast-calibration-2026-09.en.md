# Commercial Forecast Misses: Reproducible Evidence Packet (2026-09)

> **Status boundary (read first)**: Webvan and eToys were selected after their outcomes were known and are `CALIBRATION`; they are not holdout cases and do not support improved method accuracy. There is no qualified relative-holdout result here: that requires a frozen enumerable population, as-of materials, assignment, and same-input baselines followed by a one-shot reveal, none of which this packet executes. Genuine future out-of-sample evidence comes only from preregistered future judgment cards reviewed after their windows mature; this packet supplies none. Forecast dates, outcome windows, metric definitions, and source locations are case-specific below; undelivered prior versions, counterfactual series, and unreconstructable causal claims remain explicitly unknown/unverified rather than being replaced by nearby metrics.
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

- **Primary same-metric measure**: this case uses `net loss` as the primary metric (the forecast and outcome both use that name verbatim); `revenue` / `Net Sales` is secondary because the terminology differs and does not carry the core miss determination.
- **Revenue scale**: forecast `$120.0m`, actual `$178.456m`; actual was about 1.49 times forecast, a +48.7% deviation. This is a measurable scale error, but not a reversal of demand direction.
- **Loss scale**: forecast net loss `$154.3m`, actual `$453.289m`; actual loss was about 2.94 times forecast, an absolute difference of about `$298.989m`. This is a `scale` miss, with losses underestimated.
- **Mechanism / timing**: the forecast source itself lists rollout timing, order volume, market penetration, and competition as assumptions that must be separated in future records. The outcome does not establish that any one variable alone caused the miss.
- **Independence**: this is an e-commerce infrastructure and organizational-expansion forecast, not the same forecaster, metric, or source as the existing Forrester US online-retail-total series.

### Rule impact

This case **does not overturn any of the five diffusion gates**: it tests numerical calibration of a corporate financial projection, not whether a capability becomes a society-wide habit. It adds a boundary to the method instead: commercial forecasts must separately log revenue scale, loss scale, deployment pace, and mechanism assumptions; a correct revenue direction does not make the cost structure or profit forecast a hit.

## Case B · eToys: an October 30 sales forecast was revised on December 15, and actual sales still missed the revised upper bound

### Pre-T forecast source

- **Forecast owner / source**: eToys disclosed a concrete forward estimate in Exhibit 99.1 to its Form 8-K; this is the company's own forecast, not a financing covenant or a secondary retelling.
- **Disclosure date**: 2000-12-15; the target was the fiscal third quarter ending 2000-12-31. This filing is the actual frozen pre-T forecast source for the case; it mentions the October 30 range, but the undelivered October 30 document and that old range are not used in the error calculation.
- **Stable source**: [SEC full submission 0000912057-00-053869](https://www.sec.gov/Archives/edgar/data/1052245/000091205700053869/a2033537zex-99_1.txt)
- **Location**: Printed page 1 of Exhibit 99.1, under the title `ETOYS EXPECTS LOWER THAN ESTIMATED FISCAL THIRD QUARTER OPERATING RESULTS`, in the paragraph beginning `Specifically, the company's new estimates...`, source lines 14–47; SHA-256 `71d6a22b0921fb49b23496abe3ece877c6a443aeaa5efc8bed7030f808ba8a87`.

**Verbatim excerpts**:

> “LOS ANGELES, December 15, 2000 -- As a result of weaker-than-expected holiday sales, eToys Inc. (NASDAQ: ETYS) today announced that it expects to report operating results for its fiscal third quarter ending December 31 that are lower than the estimates the company provided on October 30 of this year.”
>
> “Net sales are expected to be between $120 million and $130 million, rather than the $210 million to $240 million previously estimated.”
>
> “Operating losses are expected to be between 55 percent and 65 percent of revenue, rather than the 22 percent to 28 percent of revenue previously estimated...”

**Frozen pre-T metrics**: Q3 2000 (quarter ending December 31) sales interval `$120m–$130m`; operating-loss interval `55%–65%`. The `$210m–$240m` and `22%–28%` figures are only historical references inside the December 15 filing, not the measurable forecast original for this case. The interval-miss rule is fixed as: an actual value outside the pre-T published interval is a `scale` miss, with the deviation magnitude recorded separately. The primary observation window is 16 days from December 15 to December 31.

### Outcome source

- **Outcome source**: eToys Inc., Q3 2000 Form 10-Q, filed 2001-02-14, covering the same quarter ending 2000-12-31.
- **Stable source**: [SEC full submission 0000912057-01-005726](https://www.sec.gov/Archives/edgar/data/1052245/000091205701005726/a2034712z10-q.txt)
- **Location**: Printed page 3, the `CONSOLIDATED STATEMENTS OF OPERATIONS` table under `ITEM 1. CONSOLIDATED FINANCIAL STATEMENTS`, source lines 130–180; the `NET SALES` subsection also states the original estimate and actual result at source lines 973–1006; SHA-256 `17e484b5e00d06ebeaee13f5303e5a21c58173a000973fd9dc6e0a832cab06f3`.

**Verbatim excerpts**:

> “Net sales.......................................    $131,166     $ 106,751     $ 182,004     $ 128,032”
>
> “(IN THOUSANDS, EXCEPT PER SHARE AMOUNTS)”
>
> “It should be noted that net sales for the quarter ended December 31, 2000 were substantially below our original estimate of $210 million to $240 million, due to a harsh retail climate and dampened enthusiasm for Internet retailing.”
>
> “...in fact net sales for the quarter were only $131.2 million due to a harsh retail climate and dampened enthusiasm for Internet retailing.”

The table columns are quarter ended December 31, 2000 / 1999 and nine months ended; the same-metric actual quarterly net sales were therefore `$131.166m`.

### Classification

- **Revenue scale**: against the December 15 frozen interval of `$120m–$130m`, actual `$131.166m` exceeded the upper bound by `$1.166m` (about +0.9%), so it is recorded as a boundary `scale` miss under the stated interval-miss rule. The October 30 range is only undelivered background and cannot be used to enlarge this case's error.
- **Direction / timing**: the company acknowledged before the result that its earlier estimate had failed; for the December 15 version frozen in this case, actual results crossed the upper bound 16 days later. This is a `timing + scale` forecast-revision case.
- **Mechanism**: the source attributes the shortfall to a harsh retail climate, reduced enthusiasm for Internet retailing, and attention diverted by the presidential election; the evidence supports these as the company's disclosed explanations, not as a uniquely proven cause.
- **Independence**: eToys is an online toy retailer's own quarterly financial forecast, with a different company, forecaster, and disclosure from Webvan's Goldman Sachs projection; the miss mechanisms also differ: Webvan's boundary is distribution-center rollout and fixed-cost / loss scale, while eToys' boundary is holiday-demand shortfall and forecast-interval revision. Neither is the Forrester US online-retail-total series.

### Rule impact

This case does not overturn the five diffusion gates, but strengthens one recording rule: **when a forecast is revised before the outcome, freeze the date and range of every version and calculate error by version; when a forecast is an interval, record interval coverage separately from deviation magnitude**.

The `unverified` item for this case is the original October 30 `$210m–$240m` announcement: the December 15 filing only cites it, so this packet does not count it in the case metrics and does not claim its exact error. It tests only the delivered December 15 interval.


## Appendix · Iridium: commercial financing-covenant threshold miss (not counted among the two forecast misses)

### Pre-T source (commercial target, not an ordinary probabilistic forecast)

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

1. **Change the evidence requirement, not the five-gate conclusion**: a commercial forecast must record metric, unit, target date, forecast owner, forecast version, the pre-T location, and the outcome original; correct revenue direction does not erase loss-scale error, and a revision cannot erase the prior version.
2. **Do not treat Webvan and eToys as holdout cases**: both were selected after their historical outcomes were visible, so they are `CALIBRATION` and cannot support a claim that method accuracy improved.
3. **Do not smuggle “commercial forecast miss” into “diffusion rule falsified”**: Webvan and eToys do not isolate an exclusive failure mechanism for one of the five gates; the honest update is a stronger boundary and recording discipline, not a revision to Gates 1–5.
4. **Do not count Iridium among the two forecast misses**: it is a financing-covenant minimum threshold, retained as an appendix and an `unverified-as-forecast` boundary for “commercial target threshold miss,” not used to meet the forecast-case count.
5. **Next testable direction**: pre-freeze ordinary cases from the initial SEC S-1/F-1/8-K population, encode revenue, loss, subscriber/customer, deployment milestones, and forecast revisions separately, and set error thresholds before outcomes are opened. Only then can cases enter the historical pseudo-out-of-sample protocol instead of continuing to select famous failures.
