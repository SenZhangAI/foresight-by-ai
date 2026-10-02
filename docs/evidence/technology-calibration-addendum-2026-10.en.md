# Technology-History Calibration Addendum: Missed-Forecast Candidates and Evidence Gaps (2026-10)

> **Evidence level: `CALIBRATION`, not relative `holdout` and not future out-of-sample evidence.** This addendum searched for candidates after their outcomes were known. It tests the boundary of historical rules; it does not show that the method's accuracy improved. When a candidate cannot satisfy the same-metric and source-reconstruction bar, it remains an explicit gap rather than a claimed example.

## 1. Scope and adjudication rule

- **Domain:** technology history; this does not duplicate the political/macro or business calibration packets.
- **Aim:** pair a T-before technology forecast with a later same-metric outcome, prioritizing misses.
- **Qualification:** (1) a forecast source with a publication date or verifiable information cutoff; (2) forecast metric, value/range, target window, and unit; (3) an outcome source and date; (4) the same metric, denominator, and unit on both sides; (5) locatable excerpts; and (6) an explicit `CALIBRATION` label because selection follows the outcome.
- **Missing-evidence rule:** any missing element is `unknown/unverified` or excluded. Memory, secondary narrative, or a nearby metric cannot fill the gap.
- **Selection date:** 2026-10-02. Every result was already observable, so none has sample-out-of-sample meaning.

## 2. Qualified pairings

**Qualified pairings this round: 0.**

This does not mean that no technology forecast failed. It means that the material searched here does not yet satisfy the strict combination of source reconstruction, same-metric outcome, and timing proof. The candidates below remain because their missing fields are reviewable—not because they are evidence.

## 3. Candidate A: Space Shuttle flight count — outcome subset not verified from the primary source (excluded)

### T-before forecast artifact

- **Owner/artifact:** Mathematica, Inc., *Economic Analysis of the Space Shuttle System: Executive Summary* (NASA-CR-129570), prepared for NASA.
- **Date:** 1972-01-31 (title page); the report updated the 1971-05-31 analysis.
- **Source:** <https://ntrs.nasa.gov/api/citations/19730005253/downloads/19730005253.txt>
- **Location:** §0.2.2, p. 0-7; Table 0.1, p. 0-8.
- **Verbatim excerpt:** “from 1979 to 1990 (twelve years) of 514 Space Shuttle flights, or an average of 43 Space Shuttle flights per year”.
- **Metric:** 514 Space Shuttle flights over 1979–1990 (12 years), with an average of 43 per year.
- **Status caveat:** this is a NASA/DoD mission-model planning/economic scenario, not a probability forecast; that limitation must remain attached to the case.

### Outcome and gap

- NASA's historical-resources page confirms only that the program flew 135 missions from 1981-04-12 through 2011-07-21: <https://www.nasa.gov/history/space-shuttle-history-resources/>.
- The 135 denominator covers the entire program, not the 1979–1990 or 1981–1990 subset. The page has no year-by-year or mission-by-mission table from which the target-window outcome can be derived.
- **Missing:** a NASA mission summary or primary mission list that permits item-by-item verification of the 1979–1990 count (including an explicit treatment of the years before the first launch), with date and location. The circulating “38 missions in 1981–1990” figure was not verified against such a source and is not counted.
- **Adjudication:** `unknown/unverified`; not a qualified miss. The record must not state “514 versus 38” as an established comparison.

## 4. Candidate B: Iridium subscriber counts — the long-range forecast has no same-window outcome, while the short-range covenant is not a T-before forecast (excluded)

### Long-range forecast artifact

- **Owner/artifact:** Iridium LLC / Iridium World Communications Ltd., FY1997 Form 10-K405.
- **Filing date:** 1998-03-25.
- **Source:** <https://www.sec.gov/Archives/edgar/data/948421/0000950133-98-000917.txt>
- **Location:** `THE IRIDIUM MARKET – GENERAL`, approximately source-text lines 900–930 (re-locate against the downloaded SEC artifact before publication).
- **Verbatim excerpt:** “Iridium estimates that it will have customer counts in the year 2002 in the range of 2.2 million to 2.5 million for its satellite-based voice services … 1.0 million to 1.3 million … and 350,000 to 500,000 …”.
- **Metric:** 2002 customer counts by service type; unit subscribers/customers.

### Outcome and comparability gap

- Iridium's 1999-03-31 10-Q, filed 1999-05-17, reports 7,188 Iridium World Satellite Service subscribers and 10,294 total subscribers as of 1999-03-31: <https://www.sec.gov/Archives/edgar/data/1035442/0000950133-99-001884.txt>, approximately source-text line 1760.
- This is a 1999-03-31 outcome, not 2002; the long-range forecast is also service-segmented while the available outcome excerpt is an aggregate, so the forecast and outcome are not same-window, same-group pairings.
- The 10-Q also describes a **minimum financing covenant for 1999-03-31**: “at least 27,000 Iridium World Satellite Service subscribers and at least 52,000 total subscribers.” Because this 10-Q was filed after the outcome date, it is not a T-before forecast artifact. Comparing 27,000/52,000 with 7,188/10,294 would create a false forecast pairing.
- **Missing:** a primary document published before 1999-03-31 proving that 27,000/52,000 was a publicly stated forecast or target at that time, and identifying whether it was a company forecast or a financing covenant. This round did not establish that.
- **Adjudication:** the 2002 case is `unknown/unverified`; the 1999 covenant case is excluded and is not counted as a qualified miss.

## 5. Explicitly rejected substitutes

- **Using NASA's 135 whole-program missions as the 1979–1990 outcome:** wrong denominator.
- **Using the unverified 38-mission figure:** the primary outcome source was not checked.
- **Treating the post-outcome Iridium 10-Q covenant as a T-before forecast:** wrong time order.
- **Directly comparing the 2002 forecast with the 1999 outcome:** wrong observation window and service grouping.

## 6. Limited calibration implication

This round adds no future judgment card and produces no sample for a hit rate, Brier score, relative discrimination increment, or cross-case accuracy claim. It does leave an operational boundary: a technology-history case does not become a miss merely because the technology later failed to diffuse as advertised. The target year, activity denominator, unit, and outcome metric must be frozen and matched first. For technology cases, planning scenarios, financing covenants, market-size estimates, probability forecasts, and retrospective narratives must remain separate classes.

If the search continues, the next priority should be a readable NASA mission-by-mission summary or an equivalent official forecast/statistics series. Until then, the honest result is **zero qualified cases, with concrete gaps recorded**.

## 7. Relation to the historical-validation protocol

This record follows the [Historical Pseudo-Out-of-Sample Validation Protocol](../en/02-historical-validation-protocol.md) and the methodology's `CALIBRATION` boundary: cases selected after outcomes are known may calibrate rules and expose missing evidence, but may not be presented as holdouts. Genuine future out-of-sample evidence still comes only from preregistered judgment cards reviewed after their windows mature.
