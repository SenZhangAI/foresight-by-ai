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

The addendum still preserves stably locatable candidate forecast–outcome pair records: Candidate A places the 1972 Space Shuttle flight-count planning scenario alongside NASA's historical outcome page, and Candidate B places the 1998 Iridium subscriber estimate alongside the 1999 10-Q outcome. These are forecast–outcome material pairs awaiting verification, not qualified pairings that passed this round's strict bar; the sections below record why they cannot be counted.

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

## 8. Primary-source capture review on 2026-10-09: three new technology candidates end as UNKNOWN/UNVERIFIED

This section is a bounded primary-source capture, not a renamed report of the old candidates. Timestamps are UTC; `bytes` is the downloaded response-body size and each SHA-256 identifies that body. All three candidates contain source identifiers and verbatim excerpts absent from the repository before this commit, proving that the sources were actually fetched. All three remain `UNKNOWN/UNVERIFIED` because their outcome metric or program identity is not closed; the technology qualified count therefore does not increase.

### 8.1 T-X33: X-33 flight-test start date (UNKNOWN/UNVERIFIED)

- **T-before artifact:** NASA NTRS citation `19990070318`, *The X-33 Flight Test Challenge*; source <https://ntrs.nasa.gov/api/citations/19990070318>.
- **Capture proof:** `2026-10-09T03:07:26Z`; HTTP `200`; `3,654` bytes; SHA-256 `22f932ca781b99da8d9437954cb79d2df1b0ed6e7e9a45409797ad704140f095`.
- **New verbatim excerpt:** “Flight testing will begin in July 2000, with launches originating from Edwards Air Force Base and initial landings at Michael Army Airfield in Utah.”
- **Technology-domain attribution:** the forecast quantity is a flight-test deployment milestone, not revenue, loss, or subscriber count.
- **Outcome-side capture:** the full-text response for NASA NTRS citation `20110016255`, captured at `2026-10-09T03:07:29Z`, HTTP `200`, `34,058` bytes, SHA-256 `ea57e94432d546013b21e9848a75bc4c38a29c09ae7aa367f4f53caa2dbe865e`; its new excerpt is “Although a cryogenic tank failure during testing ultimately led to the end of the effort”.
- **Terminal verdict and gap:** `UNKNOWN/UNVERIFIED`. The outcome artifact confirms that the effort ended after a tank failure, but this round did not establish from the same outcome material whether the first flight had occurred by July 2000, or define a zero-flight denominator. “The program ended” cannot be substituted for “the July forecast missed.” The strongest alternative explanation is that the forecast promised the start of testing, not a completed first flight; the current outcome artifact does not rule that out.
- **Exclusion record:** the same forecast material also discusses low-cost access, engines, and thermal-protection validation. Those are cost goals or subsystem tests, not the flight-test-start metric, and cannot replace the outcome column.

### 8.2 T-X34: X-34 first-flight schedule (UNKNOWN/UNVERIFIED)

- **T-before artifact:** NASA NTRS citation `19990019135`, *X-34 Program Status*; source <https://ntrs.nasa.gov/api/citations/19990019135>.
- **Capture proof:** `2026-10-09T03:18:53Z`; HTTP `200`; `3,256` bytes; SHA-256 `8e926b7f4d8d8b5aa0102aff8c70eea964c98fdab6e29c27d9b135a425d94c07`.
- **New verbatim excerpt:** “The X-34 program has moved rapidly from the drawing board to hardware build-up, with the first flight scheduled for 1999.”
- **Technology-domain attribution:** the forecast quantity is the first deployment of a reusable launch-vehicle technology demonstrator, not company revenue or an operating metric.
- **Outcome-side lead:** NASA NTRS citation `20000092068` (*X-34 Project: Overview and Status*) was captured at `2026-10-09T03:18:55Z`, HTTP `200`, `3,378` bytes, SHA-256 `8d3434fd0164e8bdaf72b3cc9f1a661f2d401a0e75124e76ed2269879d58311c`. It proves that a later status artifact exists, but this round did not obtain a locatable result passage for the actual 1999 flight or the pre-cancellation state.
- **Terminal verdict and gap:** `UNKNOWN/UNVERIFIED`. The same-window official outcome excerpt, cancellation date, and explicit “powered flight completed?” denominator are missing. A second-hand “later cancelled” narrative cannot be used as the result. The strongest alternative explanation is that “first flight” referred to an unpowered or captive-carry test rather than powered flight; this round obtained no primary artifact that rules that out.
- **Exclusion record:** later status material about engines, thermal protection, and design views describes capability or component status, not first-flight outcome, and cannot fill the observation window.

### 8.3 T-FREEDOM: Space Station Freedom first element versus ISS first element (UNKNOWN/UNVERIFIED)

- **T-before artifact:** NASA NTRS citation `19900046020`, *Space Station Freedom — A program update*; source <https://ntrs.nasa.gov/api/citations/19900046020>.
- **Capture proof:** `2026-10-09T03:11:02Z`; HTTP `200`; `2,881` bytes; SHA-256 `b1393592c9f584c5a285a88d8ecac63357e0bc0cdc642f905f6bbeb926edce0e`.
- **New verbatim excerpt:** “A first Freedom-element launch by the Space Shuttle is planned for 1995, with completion of the assembly process by 1998.”
- **Technology-domain attribution:** the forecast quantities are space-station deployment milestones, not commercial financial quantities.
- **Outcome-side artifact:** the response for NASA NTRS citation `20000109670`, captured at `2026-10-09T03:11:04Z`, HTTP `200`, `3,778` bytes, SHA-256 `6a4e6eaefb817bcfb7c91d1ad72dffd5e83c1ddd819a4eb14ac238d0e95a6ab9`; new excerpt: “This element (Stage 1A/R) was launched on 20 November 1998 and is currently operating on-orbit.”
- **Terminal verdict and gap:** `UNKNOWN/UNVERIFIED`. The forecast names Freedom, while the outcome artifact concerns the subsequently restructured ISS. This round did not obtain a same-program “Freedom first element / assembly complete” outcome, so it cannot establish a common denominator. The strongest alternative explanation is that ISS should be treated as a continuous deployment of Freedom after redesign, making the 1998 FGB launch comparable; that requires a program-lineage and metric-mapping artifact that is not present.
- **Exclusion record:** the outcome artifact also contains a 2000 Service Module schedule and a TBD U.S. Laboratory schedule. These are different components and versions, not interchangeable with the 1990 Freedom first-element / assembly-completion columns.

### 8.4 Round verdict and boundary

All three new candidates end as `UNKNOWN/UNVERIFIED`; the qualified technology-pair count remains **0**, and the three-domain total remains **6/12**. They are not the old `T-SHUTTLE` or Iridium 2002 records, nor repeats of nuclear power, Carter-era solar, fifth-generation computing, or VR. The new identifiers `19990070318`, `19990019135`, and `19900046020`, together with their field-level gaps, leave information that was not in the repository before this round. `CALIBRATION` does not support overturning a diffusion gate; this round names no exclusive-case-table row and does not touch the re-review debt at `:388`, so it makes no gate-overturning claim.

This round cannot be upgraded into a hit rate, Brier score, holdout, or out-of-sample evidence. If the search continues, each candidate first needs a result original, the same observation window, denominator / metric definition, forecast version, and result vintage. Until then, none may enter the qualified technology denominator.

## 9. Relation to the historical-validation protocol

This record follows the [Historical Pseudo-Out-of-Sample Validation Protocol](../en/02-historical-validation-protocol.md) and the methodology's `CALIBRATION` boundary: cases selected after outcomes are known may calibrate rules and expose evidence gaps, but may not impersonate holdouts. Genuine future out-of-sample evidence still comes only from preregistered judgment cards reviewed after their windows mature.
