# Gate 1 coverage calibration: frozen record (2026-10-16)

[中文版](social-scale-coverage-calibration-freeze-2026-10-16.md)

This file freezes the cases, decision times, denominators, frequencies, and rule before extraction and re-judgment. It is the ancestor of this round's decision commit and must not be rewritten after that commit. The later verdict page must verify each source, number, and limitation case by case; definitions cannot be changed after seeing the result.

## 1. Rule under test (verbatim)

The Gate 1 evidence rule is: **“The denominator is the number of repeat executors definable at T; a country without a qualifying survey counts as 0.”**

This round keeps the project's existing society-scale threshold: at least **100 million people weekly**, or **one billion people daily**. A qualifying component must count the same action, over the same reference period, as deduplicated people; jobs, positions, doses, trips, and annual totals cannot be substituted for people. A survey published by a national statistical office with an explicit reference period and person-level count is a qualifying survey. Administrative registers or operating statistics enter only when they explicitly provide deduplicated people and a reference period; doses and trips are never silently converted into people.

No lens or diffusion gate is added or changed in this round.

## 2. Success cases (two cases frozen)

| ID | Action and decision time T | Denominator and frequency | Public figure (frozen before extraction) | Expected result under the current rule |
|---|---|---|---|---|
| S1 | Employed people in the US civilian noninstitutional population during the September 2026 CPS reference week; T = September 2026 (Table A-1 released 2026-10-02) | Deduplicated people employed in the reference week; weekly. BLS counts a person with multiple jobs once. | BLS CPS A-1: **162,667 thousand = 162.667 million** employed, not seasonally adjusted. The definition includes people who worked at least one hour in the reference week and other stated employment categories; this is a person count, not a job count. Source: <https://www.bls.gov/news.release/empsit.t01.htm>; definitions: <https://www.bls.gov/cps/definitions.htm> | **Passes S tier**: one country's qualifying component is already ≥100 million; no missing country is needed to reach the threshold. |
| S2 | Employed people aged 15+ in India under PLFS Current Weekly Status (CWS); T = April–June 2026 quarter | Each respondent's employment status in the preceding seven days; deduplicated people, weekly reference period; the bulletin reports a quarterly average. | India's MoSPI PLFS bulletin reports an average **56.6 crore = 566 million** employed people; CWS uses the preceding seven days, not job count. Source: <https://mospi.gov.in/uploads/latestReleases/latest_release_1786356517178_3a125c52-4680-4258-9dc5-aebea9b8f3f0_Press_note_Apr-Jun_2026_PLFS_QB.pdf>; topic page: <https://www.mospi.gov.in/themes/product/69-periodic-labour-force-survey-plfs> | **Passes S tier**: one country's qualifying component is already ≥100 million. The verdict must say this is a quarterly average of person-specific preceding-seven-day reference periods, not one shared calendar week. |

Neither case is AI adoption or platform self-report. Both are social actions counted by national official labour statistics. Their time conventions differ (a US monthly reference week; India's quarterly average of person-specific preceding-seven-day periods), but both count people on the frozen weekly/recent-seven-day basis, and their numbers must not be added together.

## 3. Failure controls (two cases frozen)

| ID | Action and decision time T | Denominator and frequency | Public figure (frozen before extraction) | Expected result under the current rule |
|---|---|---|---|---|
| F1 | Australians aged 15+ doing unpaid voluntary work through an organisation; T = 2025 | At least once in the preceding 12 months; this is a looser upper-bound-like measure than weekly. | Australian Bureau of Statistics General Social Survey 2025: just under one quarter, **23%**. Source: <https://www.abs.gov.au/statistics/people/people-and-communities/general-social-survey-summary-results-australia/latest-release> | **Fail**: even this loose once-a-year measure supplies no basis for upgrading the action to 100-million weekly repeaters; visibility and organisation do not replace the denominator discipline. |
| F2 | Everyday cycling by residents of England; T = 2023 | National Travel Survey travel diary; the published denominator is trips and annual trips per person, not deduplicated weekly people, so trips cannot be substituted for people. | UK Department for Transport NTS 2023: cycling is **2% of all trips**, at **15 trips per person per year**. Source: <https://www.gov.uk/government/statistics/national-travel-survey-2023/nts-2023-active-travel> | **Fail**: the available official denominator is not 100-million weekly deduplicated people; street visibility does not change the denominator rule. |

F1 and F2 are controls for “looks widespread” rather than “passes whenever a number exists”: F1 is only 23% even under a once-a-year broad window, while F2's public figure is trips rather than people and only 2% of trips. Both must remain separate from the success cases' person-level weekly measures.

## 4. Decision branch written in advance

- **(a) Misclassification**: if S1 or S2 is recorded as 0 under the strict current rule because no qualifying survey exists, or another real success reaches the threshold but is rejected, propose a corrected rule stating the boundary between administrative statistics and surveys, with bounds and deduplication rules, and show with F1 and F2 that the corrected rule still rejects the controls.
- **(b) No misclassification**: if S1 and S2 each clear the threshold from a qualifying official survey in one country, while F1 and F2 remain rejected, publish that **evidence asymmetry is a coverage limitation, not a systemic bias**. Missing countries for J-104, J-107, and M2 remain counted as 0; this means their current lower-bound evidence is incomplete, not that their latent scale is proven society-wide.

The branch is not preselected. It must be chosen only after the frozen record and case-by-case extraction.
