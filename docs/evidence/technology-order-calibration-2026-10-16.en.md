# Technology-order calibration (2026-10-16): calibration failed; T-PV's in-window system cost is not closed

[中文版](technology-order-calibration-2026-10-16.md) · [Methodology §2](../en/00-method.md#2-toolbox-of-lenses) · [Frozen packet](technology-order-calibration-freeze-2026-10-16.en.md)

> **Status boundary:** this is `CALIBRATION`, not `HOLDOUT` and not `GENUINE_FUTURE_OOS`. The cases were selected after their outcomes were known. The frozen candidate packet is the ancestor of this judgment record; the figures and outcome sources below were collected after that freeze. This page records a failed historical calibration only; it does not support admitting a lens, a method-accuracy claim, or out-of-sample evidence.

## 1. Frozen rule and admission verdict (failed)

The frozen rule was R-T1: among technical systems at time `T`, standardised repeatable units that can be manufactured in parallel and deployed across sites with fewer site-specific interfaces, approvals, and irreversible liabilities should reach sustained comparable unit-cost decline plus cross-site diffusion earlier. Strong site coupling, long approval/build cycles, or irreversible physical responsibility are reasons to rank a system later and to judge “will arrive first” **No**.

R-T2 requires stage separation: a prototype or a falling component price is not system success until the same object's comparable unit-cost measure and cross-site diffusion are both evidenced in a defined window.

**Decision: calibration failed; this gap cannot currently be closed.** T-PV has no comparable unit-cost series for the same system boundary inside the frozen window ending in 2010. Frozen rule R-T2 forbids treating a prototype or component price as system success; the IRENA 2010–2023 comparison found this round extends beyond the window and can only be recorded as an out-of-window supplement. Under the exclusion rule, the four cases cannot honestly be counted as two successes plus two negative controls, and L11 cannot be admitted to the methodology.

### Internal contradiction in the frozen packet and this round's choice

The T-PV test column in the frozen packet literally says “by 2010: comparable module-price decline + cross-site cumulative-capacity diffusion.” Read on its own, that wording allows the OWID module-price and cumulative-capacity figures in this record to close T-PV and push the result toward option 2(a). But R-T2 in the same packet explicitly says that “a falling component price does not count as system-level success” and requires a comparable unit-cost measure and cross-site diffusion for the same object; the two provisions cannot be applied together without an explicit choice.

This page applies the stricter reading of R-T2: module price is not system-level cost, so T-PV remains `UNKNOWN/UNVERIFIED` and the calibration ends under option 2(b). This was not a pre-outcome frozen rule choice; it was a conservative choice made after the result became visible: 1b83337 first made T-PV close on module price, ca8dfc8 then tried to use the out-of-window IRENA system-cost comparison, and both approaches were rejected in review before this page settled on the current reading. The stricter direction avoids upgrading mismatched evidence into a second success case, but readers should treat it as a post-outcome adjudication caused by a design defect in the frozen packet, not as a clean calibration of the rule. The frozen packet must not be rewritten in this round; if it is frozen again, its T-PV test column must first be made consistent with R-T2.

## 2. Case matrix

| ID | T and frozen ranking | Result and rule relation | Evidence status |
|---|---|---|---|
| T-CONT | 1956-04-26 Ideal X voyage; predicted earliest “Yes” in this set | Modern containerisation began with 58 trailer bodies on Ideal X. The Richmond Fed’s 2012 *The Voyage to Containerization* reports conventional cargo handling at about $5.83 per ton, while McLean’s experts estimated Ideal-X loading at 15.8 cents per ton; the same article records containers as only 8% of Port of New York freight and 2% of West Coast freight in 1962. In-window cross-site diffusion: a Port of Rotterdam history records Sea-Land's Fairland arriving in Rotterdam on 1966-05-03 on a weekly transatlantic all-container service calling at Elizabeth, Rotterdam, Bremen, and Grangemouth. IICL's “hundreds of millions of containerised cargo units annually” is a present-day figure, an out-of-window supplement not used to close the test ending in 1966. **Closes inside the window; retained as a success candidate.** | Cost comparison is handling cost, not whole-voyage social cost; diffusion evidence is a qualitative port-history record. The Richmond Fed text attributes the cost figures to Levinson, so they are not an independent whole-system cost series. |
| T-PV | 1954-04-25 Bell Labs demonstration; predicted “Yes”, but later than T-CONT | Bell System Memorial reports the early silicon cell at about 6% efficiency. OWID's World series gives PV module cost 132.3757 (1975), 2.5118067 (2010), and 0.26518628 (2024), in the chart's stated module-cost unit; its cumulative-capacity CSV gives 0.756669 GW (2000), 39.84921 GW (2010), 710.7258 GW (2020), and 1866.8978 GW (2024). IRENA's comparable whole-system LCOE comparison is 2010 versus 2023, outside the frozen window ending in 2010; the window therefore has no same-system-boundary cost-decline series. **`UNKNOWN/UNVERIFIED`: it cannot count as a success case; the conflict between the frozen packet's test column and R-T2, and this page's post-outcome choice, are disclosed in §1.** | Module price and cumulative capacity are supplementary material; the out-of-window IRENA figures cannot close R-T2. The IEA-PVPS *Germany 2010 National Survey Report* page confirms that the report exists, but this runtime could not retrieve the PDF body or its turnkey-price table, so unread figures are not treated as evidence. |
| T-NUC | 1954-06-27 Atomic Energy Act; predicted **No** for first low-cost mass diffusion | The available description of the OECD NEA’s 2020 study says Gen-III reactors in several regions produced delays and construction-cost overruns that challenged nuclear competitiveness, and identifies harmonised regulation, standards, licensing, financing, and SMR/advanced designs as cost-reduction work still needed. IAEA's 2023 data report nuclear at nearly 10% of world electricity, with output up 2.6%; these data postdate the frozen window ending in 2020, serve only as an out-of-window supplement, and are not evidence of first, broadly low-cost replication either. **Directionally consistent with the No call, but weakly evidenced:** this can rely only on the in-window NEA 2020 discussion of delays, cost overruns, and remaining cost-reduction work; this page has not directly read the full NEA text for a deployment conclusion, and it has no in-window, like-for-like evidence for “geographically broad deployment.” | “Low cost” is not a single global tariff; the in-window evidence is a qualitative study of overruns and outstanding cost-reduction work, not a whole-system price series. This is a bounded negative result, not “nuclear failed”. |
| T-SST | 1962-11-05 SST programme period; predicted **No** for first low-cost mass passenger diffusion | Smithsonian records Concorde service beginning in 1976, 16 production aircraft (20 built in all), up to 100 passengers, average round-trip fare above $12,000, high operating cost, route contraction, and retirement in 2003; many flights were half full. GAO's 1978 report says airport-local noise regulation might not be viable and that a sound federal standard was needed. **Negative control consistent with the No call.** | The target is mass, low-cost replication, not technical flight or premium service; accident, manufacturer support, and post-2001 demand are confounders that do not erase the cost/regulatory evidence. |

Because T-PV did not close inside the frozen window, the calibration cannot conclude that “container transport → photovoltaic system diffusion” passed. T-CONT is the only success candidate currently standing; T-NUC and T-SST remain negative controls, but they do not satisfy the minimum of two successes.

## 3. What the candidate rule was meant to carry and not carry (not admitted; record only)

The following is the frozen candidate's design scope, kept so that a future re-calibration has a starting point. Because this calibration failed, **none** of it is part of the current methodology, and no judgment card may claim lens support from it.

**Was meant to carry:**

- The first-order ranking question “which class reaches repeatable cost decline plus cross-site diffusion earlier?”
- A negative call when the candidate is a tightly coupled, approval-heavy, liability-heavy system and the target is mass, low-cost replication.
- The distinction between a reproducible component and a deployable system; photovoltaic modules are modular, while grid-connected projects still require site, grid, finance, and permitting interfaces.

**Was not meant to carry:**

- A precise date for a breakthrough or contractable unit cost.
- A causal estimate of how much modularity contributes relative to subsidy, public R&D, geopolitics, finance, or standards.
- A claim that modularity always wins, or that nuclear and supersonic flight are technically impossible.
- Purely digital capability ordering; this lens concerns physical or socio-technical systems whose deployment interfaces can be inspected.

## 4. Falsifier and leading indicators

(Not admitted; record only: these are the falsifiers the candidate would carry if a future re-calibration passed.) A future judgment should mark the candidate rule wrong if a frozen **No** type reaches low-cost mass diffusion ahead of modular low-coupling alternatives in the same target window, or if a strongly modular case repeatedly fails because site coupling dominates despite standard interfaces. Leading indicators are: fraction of product cost in repeatable factory modules; number of site-specific engineering changes; approval duration variance; time from first unit to second and tenth site; comparable unit cost after financing and integration; and the share of deployments using the same interface and maintenance workflow.

If a future re-calibration passes, a card using the rule must state whether it predicts component cost, whole-system cost, or delivered service cost, and must name the deployment interfaces and liabilities that could reverse the ordering. This round failed, so no card may use it now.

## 5. External comparison (agreement / divergence / why we still hold it)

- **Agreement:** this overlaps the established learning-curve and standardisation literature, and the sources above explicitly discuss learning, licensing, financing, and standardisation. It is not presented as an independent discovery.
- **Divergence:** the popular “technology arrives in capability order” story collapses prototype, component, system, and mass adoption into one date. The four cases reject that collapse: Bell Labs' working cell did not equal photovoltaic system diffusion; Concorde's working service did not equal mass passenger diffusion.
- **Why it is not held:** the incremental claim is narrower and falsifiable: deployment coupling and irreversible responsibility should affect the ordering of comparable cost decline plus cross-site diffusion, and should be able to return **No**. But this round closes only one success case inside its window (T-CONT); T-PV did not close, so the minimum of two successes is not met and the rule is not admitted. Agreement with outside literature does not substitute for in-window evidence.

## 6. New forecast-miss cases found in this round

**0 new qualified forecast-miss cases.** The four cases here are historical rule-calibration cases, not a newly discovered dated forecast paired with a same-metric outcome. The existing technology-history addendum likewise records zero qualified forecast–outcome pairs. This round therefore does not claim that a named forecaster was wrong; it records where the new rule passes, says no, and remains exposed to measurement gaps.

## 7. Disposition and re-review consequence

L11 is not admitted. The frozen rule was not rewritten; because T-PV lacks an in-window system-cost closure, the calibration ends under option 2(b): “this gap cannot currently be closed.” This page does not rewrite any judgment card's conclusion, status, confidence, or time window, and it creates no holdout. Any future attempt to admit this kind of lens must freeze a new candidate set, close the in-window same-system evidence, and follow §1.3's re-review consequences.

## 8. Sources and fetch notes

- Richmond Federal Reserve, *The Voyage to Containerization*: <https://www.richmondfed.org/-/media/richmondfedorg/publications/research/econ_focus/2012/q2-3/pdf/economic_history.pdf> (the PDF body was directly retrieved and checked this round: it reports conventional handling at about $5.83 per ton, Ideal-X loading at 15.8 cents per ton, and containers at 8% of Port of New York freight and 2% of West Coast freight in 1962; it attributes the cost comparison to Levinson, so it remains handling cost rather than whole-system cost).
- Institute of International Container Lessors, *History of Containerization*: <https://www.iicl.org/about/history-of-containerization/> (1956 Ideal X / 58 trailer bodies; global multimodal scale is a present-day figure, an out-of-window supplement).
- SuperSummary, summary of *The Box* by Marc Levinson: <https://www.supersummary.com/the-box-marc-levinson/summary/> (1956 Ideal X loading at about 15.8 cents/ton versus $5.83/ton for conventional break-bulk; secondary summary, used as in-window cost evidence and recorded as a limitation).
- Port of Rotterdam history (docslib copy): <https://docslib.org/doc/9660426/port-of-rotterdam-brief-history-of-container-transport-forty-years-ago-on-3-may-1966-sea-lands-container-ship-fairland-a> (Sea-Land's Fairland reaching Rotterdam on 1966-05-03 on a weekly transatlantic all-container service calling at Elizabeth, Rotterdam, Bremen, and Grangemouth; in-window cross-site diffusion evidence).
- Bell System Memorial, *Bell Labs—Photovoltaics*: <https://memorial.bellsystem.com/belllabs_photovoltaics.html> (1954 demonstration; about 6% efficiency).
- Our World in Data, *Solar PV module cost* CSV: <https://ourworldindata.org/grapher/solar-pv-prices.csv> (directly fetched after freeze; values reported above).
- Our World in Data, *Solar photovoltaic cumulative capacity* CSV: <https://ourworldindata.org/grapher/solar-pv-cumulative-capacity.csv> (directly fetched after freeze; values reported above).
- IRENA, *Renewable Power Generation Costs in 2023*: <https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023> (2010 versus 2023 PV LCOE comparison; 2023 is outside the frozen window and cannot close the test ending in 2010).
- IEA-PVPS, *National Survey Report Germany – 2010*: <https://iea-pvps.org/national_survey/national-survey-report-germany-2010/>; PDF: <https://iea-pvps.org/wp-content/uploads/2020/01/nsr_2010_DEU.pdf> (the page confirms the report identity and download address; this runtime could not retrieve the PDF body or turnkey-price table, so no in-window figures are treated as obtained evidence).
- U.S. Department of Energy, *Solar Achievements Timeline*: <https://www.energy.gov/cmei/systems/solar-achievements-timeline> (2008 actual and counterfactual module-cost estimate; counterfactual, not market price).
- OECD Nuclear Energy Agency, *Unlocking Reductions in the Construction Costs of Nuclear*: <https://www.oecd.org/en/publications/unlocking-reductions-in-the-construction-costs-of-nuclear_33ba86e1-en.html> (2020 cost/standards/licensing/financing study; page protection limited direct fetch in this runtime).
- IAEA, *Nuclear Power Data and Operating Experience for 2023*: <https://www.iaea.org/newscenter/news/iaea-releases-nuclear-power-data-and-operating-experience-for-2023> (2023 scale and generation figures; postdates the frozen window ending in 2020 and is an out-of-window supplement only; page protection limited direct fetch in this runtime).
- Smithsonian National Air and Space Museum, *Concorde, Fox Alpha, Air France*: <https://airandspace.si.edu/collection-objects/concorde-fox-alpha-air-france/nasm_A20030139000> (service, fleet, fare, occupancy, and retirement facts).
- U.S. GAO, *Concorde Monitoring and Noise Regulation*, CED-78-52: <https://www.gao.gov/products/ced-78-52> (1978 noise-regulation and public-acceptance evidence).
