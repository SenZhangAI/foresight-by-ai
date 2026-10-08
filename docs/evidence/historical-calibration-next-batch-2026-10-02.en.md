# Historical Forecast–Outcome Evidence Record: Next Batch (2026-10-02)

> **Evidence boundary first.** This batch freezes `CALIBRATION` / `UNKNOWN/UNVERIFIED` records selected from repository evidence after outcomes were known. It is not a holdout or genuine future out-of-sample evidence. It tests record definitions and method boundaries; it must not be used to calculate accuracy, Brier scores, relative discrimination increments, or method validity. This batch contains no `GENUINE_FUTURE_OOS` and no qualified `CONTAMINATED_RELATIVE_HOLDOUT`.
>
> **Freeze rule.** Each case must state the forecast action, decision time T, outcome window, forecast and outcome metrics, denominator/unit, original-source location, and reconstructability. A post-outcome case is `CALIBRATION`; if a field cannot be closed, the case remains `UNKNOWN/UNVERIFIED`. Similar metrics, secondary retellings, or whole-program totals cannot fill a same-window gap.

> **How this count relates to other counts:** This file is a batch, not a count of new cases and not the repository-wide archive. It contains **4 records**: 3 `CALIBRATION` records (`P-04` and `B-WEBVAN` carried forward from the first slice, with only `B-ETOYS` added in this batch) + 1 `UNKNOWN/UNVERIFIED` record (`T-SHUTTLE`). The repository-wide qualified `CALIBRATION` archive remains **6 pairs**; the methodology snapshot combines this batch with the first slice as 3 reconstructable pairs + 1 unknown candidate. See the [historical-retrospect count navigation](../en/01-retrospect.md#103-latest-cross-domain-evidence-slice-and-next-batch-classes-windows-and-metric-definitions-2026-10).

## 1. Batch register

| case_id | domain | forecast action and T | outcome window | comparable metric / denominator / unit | original source and location | reconstructability | class | supported boundary |
|---|---|---|---|---|---|---|---|---|
| `P-04` | politics / macroeconomics | FOMC material from 2007-10-30/31 gave a 1.8%–2.5% central range for 2008 real-GDP Q4/Q4 growth | 2008 Q4/Q4; BEA final release 2009-03-26 | US real GDP, Q4/Q4, percent; the forecast range was entirely positive and the outcome was −0.8% | Forecast: [`politics-calibration.en.md`](politics-calibration.en.md) §P-04, `politics-artifacts/P-04/prediction.html`, excerpt range and SHA in §54–60; outcome: same file §56–60, `outcome.html` | `CALIBRATION`: original copies, date boundary, excerpt locations, and hashes are recorded; the forecast page has no independent publication date, so the meeting-date limit remains | `CALIBRATION` | Can weaken a rule that a smooth baseline adequately protects against tail turns; cannot establish overall macro forecast accuracy |
| `B-WEBVAN` | business | Webvan’s 1999-12-10 S-1 disclosed a Goldman Sachs projection of $120.0m 2000 revenue and $154.3m 2000 net loss | Webvan FY2000; 10-K filed 2001-04-02 | Company 2000 `revenue`/`Net Sales` and `net loss`, USD millions; outcome Net Sales $178.456m and Net Loss $453.289m | Forecast/excerpt: [`business-forecast-calibration-2026-09.en.md`](business-forecast-calibration-2026-09.en.md) §A, SEC 0000891618-99-004914; outcome: same file §A, SEC 0001012870-01-001485 | `CALIBRATION`: T-before S-1 and outcome 10-K are locatable; `revenue`/`Net Sales` terminology is reduced to an auxiliary metric, with net loss as the primary comparable metric | `CALIBRATION` | Supports separating revenue scale, loss scale, rollout pace, and mechanism assumptions; cannot establish failure of a social-diffusion rule |
| `B-ETOYS` | business | A 2000-12-15 8-K froze a new Q3 estimate: net sales $120m–$130m and operating-loss rate 55%–65% | Same fiscal quarter ending 2000-12-31; 10-Q filed 2001-02-14 | Same-quarter `net sales`, USD thousands; outcome $131.166m; $1.166m (about 0.9%) above the interval ceiling | Forecast: [`business-forecast-calibration-2026-09.en.md`](business-forecast-calibration-2026-09.en.md) §B, SEC 0000912057-00-053869; outcome: same file §B, SEC 0000912057-01-005726 | `CALIBRATION`: version date, interval, and same-quarter outcome are locatable; the 10-30 old interval remains context only | `CALIBRATION` | Supports version-freezing before revision and separating interval coverage from deviation magnitude; does not support using the undelivered old source as evidence |
| `T-SHUTTLE` | technology / aerospace | A 1972 NASA economic-analysis plan projected 514 shuttle flights from 1979–1990 (43 per year); it was a planning scenario, not a probabilistic forecast | Candidate window 1979–1990; available NASA page gives only 135 missions for the entire 1981–2011 program | Requires same-window mission count, activity denominator, unit, and a rule for the no-launch years 1979–1980; current material lacks these | Forecast: [`technology-calibration-addendum-2026-10.en.md`](technology-calibration-addendum-2026-10.en.md) §3, NASA-CR-129570 §0.2.2/Table 0.1; candidate outcome and gap in §§35–38 | `UNKNOWN/UNVERIFIED`: the whole-program 135 cannot replace the 1979–1990 subset; the unverified “38” is excluded | `UNKNOWN/UNVERIFIED` | Supports distinguishing planning scenarios from probability forecasts and freezing the target window and denominator; cannot be written as a verified 514-versus-38 miss |

**Counting rule:** This batch contains four records: `P-04`, `B-WEBVAN`, and `B-ETOYS` are calibration cases selected after outcomes were known; `T-SHUTTLE` remains unknown because its gap is open. To prevent existing material from being misrepresented as new out-of-sample evidence, this batch has no qualified holdout and no `GENUINE_FUTURE_OOS`.

## 2. Case-by-case freeze and determination

### P-04: same-metric directional miss at a macro tail turn

- **Forecast action and T:** FOMC material from 2007-10-30/31 gave a 1.8%–2.5% central range for US real-GDP Q4/Q4 growth in 2008. The page confirms the meeting date but has no independent publication date; 2007-10-31 is not presented as a verified publication date.
- **Outcome window:** 2008 Q4/Q4; the BEA final page is marked for release on 2009-03-26 at 08:30 EST, and reports a 0.8% decline in real GDP.
- **Comparability and reconstructability:** The forecast footnote and BEA outcome both use Q4/Q4 real-GDP growth in percent; the forecast range was entirely positive and the outcome was −0.8%. Original HTML copies, derived text, excerpt ranges, and SHA-256 values are recorded in the political packet §§54–61.
- **Class:** `CALIBRATION`, primary class `direction`. The case was registered after the outcome was known and cannot be a holdout.
- **Method boundary:** It can weaken an uncalibrated claim that a smooth baseline covers crisis tails, but it does not isolate a cross-domain rule or establish overall macro accuracy.

### B-WEBVAN: direction near the mark, loss scale materially too low

- **Forecast action and T:** The 1999-12-10 Webvan S-1 disclosed Goldman Sachs projections of $120.0m 2000 revenue and $154.3m 2000 net loss. The forecast also listed rollout timing, order volume, market penetration, and competition assumptions.
- **Outcome window:** Webvan FY2000; the 2000 Form 10-K was filed 2001-04-02. Net Sales were $178.456m and Net Loss was $453.289m (the source table is in thousands of dollars).
- **Comparability and reconstructability:** Net loss is the primary same-metric field; actual loss was about 2.94 times forecast. Revenue is auxiliary because the forecast says `revenue` while the result table says `Net Sales`. The business packet records the SEC full submissions, page locations, hashes, and excerpts in §§6–45.
- **Class:** `CALIBRATION`, primary class `scale`. A near-correct revenue direction does not make the cost and profit result a hit.
- **Method boundary:** The case requires business records to separate revenue scale, loss scale, rollout pace, and mechanism assumptions; it does not by itself prove that a social-diffusion gate failed.

### B-ETOYS: revised forecast still crossed the interval ceiling

- **Forecast action and T:** On 2000-12-15, an 8-K/Exhibit 99.1 froze the new estimate for the same fiscal quarter at $120m–$130m net sales and a 55%–65% operating-loss rate. The 10-30 interval is historical context quoted by the document, not the delivered source for this case.
- **Outcome window:** The same fiscal quarter ending 2000-12-31; the 10-Q was filed 2001-02-14 and reported $131.166m net sales.
- **Comparability and reconstructability:** The result is stated in thousands of dollars and was $1.166m, about 0.9%, above the frozen interval ceiling. Under the case’s stated rule, this is a boundary `scale` miss, with revision timing recorded separately. The two SEC sources and locations are in the business packet §§51–99.
- **Class:** `CALIBRATION`, not an error assessment of the undelivered 10-30 interval.
- **Method boundary:** When the same metric is revised before reveal, each version must freeze its date and interval; interval coverage and deviation magnitude must not be collapsed into one label.

### T-SHUTTLE: technology planning scenario with an open outcome window

- **Forecast action and T:** NASA-CR-129570 is dated 1972-01-31 on its title page; §0.2.2/Table 0.1 states 514 flights over twelve years from 1979–1990, 43 per year. The document is a NASA/DoD mission-model planning/economic-analysis scenario, not a probability forecast.
- **Outcome window:** The target is the same 1979–1990 window, but the available NASA history page confirms only 135 missions for the full program from 1981-04-12 to 2011-07-21.
- **Missing fields:** No original task-by-task list closes the target window, and no frozen rule handles the no-launch years 1979–1980. The unverified “38 missions in 1981–1990” is memory or retelling and is excluded.
- **Class:** `UNKNOWN/UNVERIFIED`; stop upgrading and do not write “514 versus 38.” If an official task list is obtained, the case must be re-recorded with the result date, task list, window rule, and denominator.
- **Method boundary:** The case supports distinguishing planning scenarios, market-size estimates, financing covenants, and probability forecasts, and requires technology forecasts to state target years, activity denominator, and unit; it does not support a technology forecast accuracy claim.

## 3. What this batch supports, weakens, and cannot determine

### Supports (record discipline, not accuracy)

1. Forecast actor, forecast type, T, outcome window, metric, denominator, and unit must be separate fields. Webvan’s revenue/loss split and Shuttle’s planning/probability distinction show that “a number exists” is not one kind of evidence.
2. Forecast revisions must freeze each version. eToys’ 12-15 interval cannot be replaced by the 10-30 interval merely because the later filing quotes it.
3. An unclosed same-window result must remain `UNKNOWN/UNVERIFIED`. Shuttle’s whole-program total and unverified 38 cannot fill the target-window gap.

### Weakens

- P-04 weakens treating a smooth baseline or central interval as protection against crisis tails; it is still only a post-outcome macro calibration.
- Webvan weakens the coarse rule that a near-correct direction is a commercial forecast hit; actual loss was nearly three times forecast, so revenue direction cannot cover profit scale.
- eToys weakens merging a revised forecast with its prior version; it supports a time/version boundary, not a universal diffusion law.

### Cannot determine

- This batch cannot determine overall forecasting accuracy across the five parallel source classes.
- It contains no relative holdout and cannot determine an incremental advantage over a same-input baseline.
- It contains no `GENUINE_FUTURE_OOS` and cannot substitute for future judgment cards reviewed after their windows mature.
- It cannot infer social-scale diffusion, embodied-intelligence adoption, or universal technology uptake from corporate financial projections or an aerospace planning scenario.

## 4. Stop conditions for continuation

- To close `T-SHUTTLE`, obtain an official task-by-task list or equivalent primary statistic for 1979–1990, freeze the window, treatment of 1979–1980, task denominator, and locatable excerpt; until then it remains `UNKNOWN/UNVERIFIED`.
- To construct a historical pseudo-out-of-sample test, first freeze the enumerable candidate population, T-before materials, assignment salt, same-input baseline, and one-shot reveal rule; this batch must not be relabeled as a holdout.
- Method validity can only be supplied by preregistered judgment cards reviewed after their windows mature; this batch returns boundaries for reconstructable historical material to the method, not new future forecasts.

## 5. Related evidence packets

- [Political forecast-miss calibration packet](politics-calibration.en.md)
- [Business forecast-miss calibration packet](business-forecast-calibration-2026-09.en.md)
- [Technology-history calibration addendum](technology-calibration-addendum-2026-10.en.md)
- [Historical calibration evidence slice](historical-calibration-2026-10-02.en.md)

**Batch conclusion:** This batch freezes three reconstructable post-outcome calibration records and one explicitly retained unknown technology candidate, publishing each case’s metric boundaries and missing fields. It tightens historical evidence discipline but provides no accuracy, holdout, or genuine future out-of-sample evidence.
