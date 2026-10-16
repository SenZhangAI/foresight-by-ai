# Technology-order calibration (2026-10-16): modularity and coupling admitted as L11 at medium-low confidence

[中文版](technology-order-calibration-2026-10-16.md) · [Methodology §2](../en/00-method.md#2-toolbox-of-lenses) · [Frozen packet](technology-order-calibration-freeze-2026-10-16.en.md)

> **Status boundary:** this is `CALIBRATION`, not `HOLDOUT` and not `GENUINE_FUTURE_OOS`. The cases were selected after their outcomes were known. The frozen candidate packet is the ancestor of this judgment record; the figures and outcome sources below were collected after that freeze. The record supports a bounded lens, not a method accuracy claim.

## 1. Frozen rule and admission decision

The frozen rule was R-T1: among technical systems at time `T`, standardised repeatable units that can be manufactured in parallel and deployed across sites with fewer site-specific interfaces, approvals, and irreversible liabilities should reach sustained comparable unit-cost decline plus cross-site diffusion earlier. Strong site coupling, long approval/build cycles, or irreversible physical responsibility are reasons to rank a system later and to judge “will arrive first” **No**.

R-T2 requires stage separation: a prototype or a falling component price is not system success until the same object's comparable unit-cost measure and cross-site diffusion are both evidenced in a defined window.

**Decision: admit as L11, medium-low confidence, with scope narrowed to an ordering / veto lens.** The four cases meet the requested 2-success + 2-negative-control calibration shape, and the rule makes genuine “No” calls. It does not yield a rate, accuracy score, or sample-out-of-time evidence.

## 2. Case matrix

| ID | T and frozen ranking | Result and rule relation | Evidence status |
|---|---|---|---|
| T-CONT | 1956-04-26 Ideal X voyage; predicted earliest “Yes” in this set | Modern containerisation began with 58 trailer bodies on Ideal X. A Richmond Fed history reports traditional handling at about $5.83/ton versus under $0.16/ton for container loading, while IICL records the later global multimodal system involving hundreds of millions of containerised cargo units annually. **Consistent success case.** | Cost comparison is handling cost, not whole-voyage social cost; diffusion source is qualitative. |
| T-PV | 1954-04-25 Bell Labs demonstration; predicted “Yes”, but later than T-CONT | Bell System Memorial reports the early silicon cell at about 6% efficiency. OWID's World series gives PV module cost 132.3757 (1975), 2.5118067 (2010), and 0.26518628 (2024), in the chart's stated module-cost unit; its cumulative-capacity CSV gives 0.756669 GW (2000), 39.84921 GW (2010), 710.7258 GW (2020), and 1866.8978 GW (2024). To close R-T2 on the same system boundary, IRENA's comparable whole-system LCOE record reports solar PV at 414% above the cheapest fossil-fuel solution in 2010 and 56% below it in 2023; this, paired with cumulative PV-generation-system diffusion, closes the system-level test, while module price is corroborating learning-curve evidence only. **Consistent success case.** | The price series is module cost; the system-level closure uses IRENA LCOE and cumulative capacity: the former is a comparable unit-cost measure for the same PV-generation-system class in 2010 and 2023, and the latter is cross-site diffusion. Module price remains corroborating evidence, not a direct comparison of component and whole-system prices; the 1954 prototype is not counted as system success. |
| T-NUC | 1954-06-27 Atomic Energy Act; predicted **No** for first low-cost mass diffusion | OECD NEA's 2020 study says Gen-III reactors in several regions produced delays and construction-cost overruns that challenged nuclear competitiveness, and identifies harmonised regulation, standards, licensing, financing, and SMR/advanced designs as cost-reduction work still needed. IAEA's 2023 data report nuclear at nearly 10% of world electricity, with output up 2.6%; this is real scale, but not evidence of first, broadly low-cost replication. **Negative control consistent with the No call.** | “Low cost” is not a single global tariff; IAEA scale is not a whole-system price series. This is a bounded negative result, not “nuclear failed”. |
| T-SST | 1962-11-05 SST programme period; predicted **No** for first low-cost mass passenger diffusion | Smithsonian records Concorde service beginning in 1976, 16 production aircraft (20 built in all), up to 100 passengers, average round-trip fare above $12,000, high operating cost, route contraction, and retirement in 2003; many flights were half full. GAO's 1978 report says airport-local noise regulation might not be viable and that a sound federal standard was needed. **Negative control consistent with the No call.** | The target is mass, low-cost replication, not technical flight or premium service; accident, manufacturer support, and post-2001 demand are confounders that do not erase the cost/regulatory evidence. |

The predicted ordering was **container transport → photovoltaic system diffusion**, with nuclear and SST explicitly outside the “first low-cost mass diffusion” set. The result is consistent with that ordering and with both negative calls. No frozen No case reached the target first.

## 3. What the rule can and cannot carry

**Carries:**

- The first-order ranking question “which class reaches repeatable cost decline plus cross-site diffusion earlier?”
- A negative call when the candidate is a tightly coupled, approval-heavy, liability-heavy system and the target is mass, low-cost replication.
- The distinction between a reproducible component and a deployable system; photovoltaic modules are modular, while grid-connected projects still require site, grid, finance, and permitting interfaces.

**Does not carry:**

- A precise date for a breakthrough or contractable unit cost.
- A causal estimate of how much modularity contributes relative to subsidy, public R&D, geopolitics, finance, or standards.
- A claim that modularity always wins, or that nuclear and supersonic flight are technically impossible.
- Purely digital capability ordering; this lens concerns physical or socio-technical systems whose deployment interfaces can be inspected.

## 4. Falsifier and leading indicators

A future judgment should mark L11 wrong if a frozen **No** type reaches low-cost mass diffusion ahead of modular low-coupling alternatives in the same target window, or if a strongly modular case repeatedly fails because site coupling dominates despite standard interfaces. Leading indicators are: fraction of product cost in repeatable factory modules; number of site-specific engineering changes; approval duration variance; time from first unit to second and tenth site; comparable unit cost after financing and integration; and the share of deployments using the same interface and maintenance workflow.

A future card using L11 must state whether it predicts component cost, whole-system cost, or delivered service cost, and must name the deployment interfaces and liabilities that could reverse the ordering.

## 5. External comparison (agreement / divergence / why we still hold it)

- **Agreement:** this overlaps the established learning-curve and standardisation literature, and the sources above explicitly discuss learning, licensing, financing, and standardisation. It is not presented as an independent discovery.
- **Divergence:** the popular “technology arrives in capability order” story collapses prototype, component, system, and mass adoption into one date. The four cases reject that collapse: Bell Labs' working cell did not equal photovoltaic system diffusion; Concorde's working service did not equal mass passenger diffusion.
- **Why still hold it:** the incremental claim is narrower and falsifiable: deployment coupling and irreversible responsibility should affect the ordering of comparable cost decline plus cross-site diffusion, and should be able to return **No**. The two success cases and two negative controls support admission only at medium-low confidence.

## 6. New forecast-miss cases found in this round

**0 new qualified forecast-miss cases.** The four cases here are historical rule-calibration cases, not a newly discovered dated forecast paired with a same-metric outcome. The existing technology-history addendum likewise records zero qualified forecast–outcome pairs. This round therefore does not claim that a named forecaster was wrong; it records where the new rule passes, says no, and remains exposed to measurement gaps.

## 7. Disposition and re-review consequence

L11 is admitted as a current lens, but this calibration does not create a holdout. Any earlier judgment whose reasoning asserted an unqualified technology sequence remains subject to the method's rule-change re-review protocol; this record does not rewrite judgment-card conclusion, status, confidence, or time-window fields. Future L11 use must be explicit about the target metric and the system boundary.

## 8. Sources and fetch notes

- Richmond Federal Reserve, *The Voyage to Containerization*: <https://www.richmondfed.org/-/media/richmondfedorg/publications/research/econ_focus/2012/q2-3/pdf/economic_history.pdf> (the PDF was not retrievable in this runtime; the handling-cost figures are retained as delegated research evidence and marked as a limitation).
- Institute of International Container Lessors, *History of Containerization*: <https://www.iicl.org/about/history-of-containerization/> (1956 Ideal X / 58 trailer bodies; global multimodal scale).
- Bell System Memorial, *Bell Labs—Photovoltaics*: <https://memorial.bellsystem.com/belllabs_photovoltaics.html> (1954 demonstration; about 6% efficiency).
- Our World in Data, *Solar PV module cost* CSV: <https://ourworldindata.org/grapher/solar-pv-prices.csv> (directly fetched after freeze; values reported above).
- Our World in Data, *Solar photovoltaic cumulative capacity* CSV: <https://ourworldindata.org/grapher/solar-pv-cumulative-capacity.csv> (directly fetched after freeze; values reported above).
- IRENA, *Renewable Power Generation Costs in 2023*: <https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023> (comparable 2010 and 2023 PV LCOE; the search extract supplies the relative fossil-fuel figures).
- U.S. Department of Energy, *Solar Achievements Timeline*: <https://www.energy.gov/cmei/systems/solar-achievements-timeline> (2008 actual and counterfactual module-cost estimate; counterfactual, not market price).
- OECD Nuclear Energy Agency, *Unlocking Reductions in the Construction Costs of Nuclear*: <https://www.oecd.org/en/publications/unlocking-reductions-in-the-construction-costs-of-nuclear_33ba86e1-en.html> (2020 cost/standards/licensing/financing study; page protection limited direct fetch in this runtime).
- IAEA, *Nuclear Power Data and Operating Experience for 2023*: <https://www.iaea.org/newscenter/news/iaea-releases-nuclear-power-data-and-operating-experience-for-2023> (2023 scale and generation figures; page protection limited direct fetch in this runtime).
- Smithsonian National Air and Space Museum, *Concorde, Fox Alpha, Air France*: <https://airandspace.si.edu/collection-objects/concorde-fox-alpha-air-france/nasm_A20030139000> (service, fleet, fare, occupancy, and retirement facts).
- U.S. GAO, *Concorde Monitoring and Noise Regulation*, CED-78-52: <https://www.gao.gov/products/ced-78-52> (1978 noise-regulation and public-acceptance evidence).
