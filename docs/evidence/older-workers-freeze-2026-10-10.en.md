# Paid work at 65 and over, every week: freeze record for a countable social action (2026-10-10)

[中文版](older-workers-freeze-2026-10-10.md)

This file serves a reasoning chain that starts from **public finance and sovereign debt** and does not presuppose AI. The README registry assigns that chain its number when the chain lands. **Before any numerical evidence is collected**, this file freezes the tuple `(candidate action, decision time T, denominator, frequency)` for one candidate action, together with its de-duplication rules, its exclusions and decision rules written in advance. The file lands as a commit of its own, so its commit time is the freeze time. The check log, judgment card and chain text that follow may cite these definitions but may not rewrite them. If a definition later proves unworkable, the only allowed move is to record "frozen definition failed" in a new file, with the reason.

> **Why this action.** One of the most direct ways a fiscal squeeze reaches individuals is by raising the age at which the public pension can be claimed, so that some people keep working every week at an age when they would otherwise have retired. "Aged 65 or over and doing paid work in the reference week" can be counted per week and per de-duplicated person, and its description contains no AI. It is not the action frozen in the other freeze record from the same day ([freeze record for countable social actions that do not presuppose AI](non-ai-social-action-freeze-2026-10-10.en.md)). That record froze remote work as the main candidate plus five controls, M1–M5. The two records do not register the same card twice.

> **What was known before freezing.** Before freezing, the author had remembered impressions of some magnitudes: a little over ten million employed people aged 65+ in the United States, about nine million in Japan, and a few million each in Korea, the EU and the UK. Freezing cannot erase these priors. It only guarantees that the denominator rules, exclusions and thresholds are written before the data are collected and are not changed afterwards. On these impressions the author **expects** a D-tier result in advance. That is an expectation, not a verdict.

Every threshold comes from existing text; this file adds no rule:

- **S · social-scale**: the target action happens weekly across a hundred-million-scale population, or daily across a billion-scale population ([historical validation protocol §6](../en/02-historical-validation-protocol.md#6-outcome-coding-and-necessary-condition-scoring)).
- **D · segment / domain diffusion**: the action is the majority practice inside a sub-population definable at T, without reaching S (same section).
- **Denominator discipline**: the denominator must be the same acting subject, definable at T, de-duplicated and counted at a stated frequency. Affected or potential populations may not stand in for it ([methodology §4](../en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids)).
- **The five diffusion gates** apply in their current wording from the [historical retrospective](../en/01-retrospect.md#3-the-five-gates) and [methodology · the diffusion gates are not a tenth optional lens](../en/00-method.md#the-diffusion-gates-are-not-a-tenth-optional-lens).

---

## 1. The tuple (frozen)

| Item | Frozen definition |
|---|---|
| **Candidate action** | In the reference week, the person worked at least one hour for pay or profit under the ILO definition of employment (self-employment included), and was aged 65 or over in that week. |
| **Category** | Labour (linked to the fiscal politics of pension ages) |
| **Decision time T** | 2026-10-10. No evidence may be published after T; information after T is used only at expiry review. |
| **Denominator** | The de-duplicated number of people who performed the action in the reference week. Only these sources count: a national statistical office's labour force survey, or a household survey with a documented sampling design, with a reference period of at most 7 days. The survey must publish the number employed aged 65+, or a sum of contiguous age groups starting at 65. A share multiplied by the same office's contemporaneous 65+ population base also counts. A component that publishes only ages 65–74 counts as a lower bound. A country that publishes only 60+ or 55+ and cannot isolate 65+ counts as 0. |
| **Cross-country sum** | National populations do not overlap, so qualifying components **may be added**. Take one component per country: the latest annual average or the latest quarter. The sum is a **lower bound**. Countries without a qualifying survey count as 0 and may not be filled in by estimate. |
| **Recency** | No component's reference period may begin before 2023-01-01. |
| **Frequency** | Weekly (at least once per reference week). |
| **S threshold** | Sum of qualifying components ≥ 100 million. |
| **Sub-population majority (one route to D)** | Only the **standard age groups published by the same qualifying survey** count (for example 65–69), and more than half of that group must be employed. No slice may be defined after the fact. |

**Not counted in the denominator (frozen)**:

1. People who were looking for work but did not work in the reference week (the unemployed).
2. People doing only unpaid housework, unpaid care or volunteering.
3. Counts of public-pension recipients.
4. Counts of people who worked "in the past 12 months", because that is not weekly.
5. Employer-reported counts of older staff, and hiring data.
6. Unpaid contributing family workers: subtract them where the survey reports them separately. Where it does not, mark the component "broad definition". It may then enter the scale description for D, but **if reaching S depends on that component, S may not be awarded**.

## 2. Decision rules written in advance (frozen)

| Result | Conditions (all written before looking at data) |
|---|---|
| **A · reaches S** | The sum of qualifying components is ≥ 100 million; no gate from two to five vetoes; and an L8 demand-side review is passed separately. |
| **C · D tier only** | The sum of qualifying components is ≥ 10 million and < 100 million; or more than half of a standard age group in some qualifying survey is employed. "Whole society", "universal" and "becomes the norm" may not be used anywhere. |
| **B · not established at T** | No qualifying component exists; or the sum is < 10 million and no standard age group passes one half. |

Three further constraints may not be relaxed afterwards:

- If the qualifying sum does not reach 100 million, gates two to five and the L8 review are **not evaluated**. The verdict records them as "not evaluated", never as "passed".
- The judgment card must keep the "present-scale review" (facts already true at T) separate from the "forward claim" (expansion, contraction or crossing of the S threshold within the window, with its own falsifier and leading indicators). Gate one by construction recognises only behaviour already happening at T, so its result may not be read as a forward judgment.
- Expiry review uses every rule in this table. If any country's qualifying definition has changed by expiry, the change is recorded as a definitional change and may not count as a hit.

## 3. What this file does not do

- It gives no number, no gate verdict and no mechanism. Those are written after the freeze.
- It adds or changes no diffusion gate, lens or threshold, and adds no `### L<n>` lens.
- It lists no separate controls that must be vetoed. The decision rules above are already open to two negative outcomes, B and C. The sieve's screening power is tested in the other freeze record from the same day, cited above.
