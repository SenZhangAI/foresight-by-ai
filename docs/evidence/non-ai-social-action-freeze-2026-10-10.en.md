# Freeze record for countable social actions that do not presuppose AI (2026-10-10)

[中文版](non-ai-social-action-freeze-2026-10-10.md)

This file freezes, **before any numerical evidence is collected and before any mechanism is written**, a set of candidate-action tuples `(candidate action, decision time T, denominator, frequency)`, their de-duplication rules and exclusions, and decision rules written in advance. It is landed as a commit of its own, so its commit time is the freeze time; the check log, judgment card and chain text that follow may only cite the definitions here and may not rewrite them. If a definition later turns out to be unworkable, the only allowed move is to record "frozen definition failed" in a new file with the reason — never to edit it in place into a version that passes more easily.

> **Why run it again.** The previous frozen test ([freeze record](social-action-freeze-2026-10-10.en.md), [verdict and check log](social-action-verdict-2026-10-10.en.md)) produced this archive's first S-tier judgment, [J-103](../en/ledger/103-110.md#j-103--the-society-scale-ai-action-is-asking-not-deciding-hundred-million-weekly-reach-rests-on-the-free-tier), but its main candidate and all six controls were AI or technology actions. The methodology requires supply and demand, human nature, historical regularities, technological regularities and social regularities to stand side by side, yet the same sieve has never ruled on any social behaviour that **does not presuppose AI**. This file moves the test onto labour, care, migration and organisational actions.

> **What was known before freezing, stated plainly.** Before freezing, the author had remembered impressions of some magnitudes (for example, that the share of workers who teleworked "in the reference week" in US official surveys is somewhere around one in five, and that global cross-border remitters are often put at around two hundred million). Freezing cannot erase such priors; what it guarantees is that the denominator rules, exclusions and thresholds are written before the data are collected and are not changed afterwards.

Every threshold applied here is taken from existing text; this file adds no rule:

- **S · social-scale**: the target action reaches at least hundred-million-scale weekly use, or billion-scale daily use ([historical validation protocol §6](../en/02-historical-validation-protocol.md#6-outcome-coding-and-necessary-condition-scoring)).
- **D · segment / domain diffusion**: becomes the majority practice inside a sub-population definable at T, without reaching S (same section).
- **Denominator discipline**: the same acting subject, definable at T, de-duplicated and counted at a stated frequency; affected population, demand population or potential population may not stand in for it ([methodology §4](../en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids)).
- **The five diffusion gates** are applied in their current wording from the [historical retrospective](../en/01-retrospect.md#3-the-five-gates) and [methodology · the diffusion gates are not a tenth optional lens](../en/00-method.md#the-diffusion-gates-are-not-a-tenth-optional-lens); they are veto-style necessary conditions, not a sufficient-condition predictor (`J-066`).

**The "does not presuppose AI" test**: delete the word "AI" from any candidate action below and it is still the same countable action — in fact none of the descriptions contains AI to begin with. If AI later appears inside a mechanism, the judgment card must state separately whether the conclusion still holds once AI is deleted.

---

## 1. Main candidate tuple (frozen)

| Item | Frozen definition |
|---|---|
| **Candidate action** | In a reference week, doing at least part of one's **paid work** at one's own home (remote work / working from home), where that job's regular workplace is not the home. |
| **Category** | Labour |
| **Decision time T** | 2026-10-10. No evidence may be dated later than T; information after T may be used only for due-date checks, never for this ruling. |
| **Denominator** | The **de-duplicated number of people** who performed the action in the reference week. Only one kind of source qualifies: a national statistical office, or a household / labour-force survey with a sampling statement, whose question uses a reference period of no more than 7 days ("last week", "the past 7 days"), or that classifies people as "usually working from home" (at home on at least half of working days in the reference period) — the latter necessarily means at least weekly and counts only as a lower bound. The base is the employed population published by the same agency for the same period; share × base gives the count. |
| **Summing across countries** | National populations do not overlap, so qualifying national components **may be added**; each component must qualify on its own, and each country contributes only one component (where a weekly measure exists, use it and do not add a "usually" measure to it). The sum is only a **lower bound** on the global count: every country without a qualifying survey counts as 0 and may not be filled in by estimation. |
| **Recency** | Each component's reference period may not begin before 2023-01-01. Older data do not describe the state at T; they may serve as background only and do not enter the count. |
| **Frequency** | Weekly (at least once per reference week). |
| **S bar** | Sum of qualifying components ≥ 100 million. |
| **Sub-population majority (one route to tier D)** | Only the **standard published breakdowns** of the same qualifying survey count (education, major occupation group, industry, age group); no slice may be defined after the fact. |
| **Old action named for gate two (frozen)** | One round trip to the regular workplace for the same job (one commute round trip). At T it is specific, countable and long since performed at scale (travel surveys count it by trip). |

**What does not enter the denominator (frozen)**:

1. "Jobs that could be done remotely" or "employees covered by a remote-work policy" — these are potential populations.
2. People who "have ever worked remotely" or did so "in the past year" — the frequency is not weekly.
3. Remote days as a share of all paid working days — that is a share of days, not a count of people.
4. Employer self-reports, the share of remote job postings, office badge-in rates or vacancy rates — none of these are counts of people.
5. Family businesses whose workplace is the home in the first place (farm households, home shops, industrial home-work): if the survey publishes them separately they must be subtracted; if it does not, that component is marked "broad definition" — it may count toward the scale description of tier D, but **if an S verdict depends on that component, S may not be granted**.
6. Checking work messages at home after hours, where the survey itself does not count this as working at home.

## 2. Decision rules written in advance (frozen)

| Result | Condition (all written before seeing any number) |
|---|---|
| **A · reaches tier S** | Qualifying components sum to ≥ 100 million; gate two can name the old action above; none of gates two to five vetoes; and an L8 demand-side review is done in addition. At least one **non-technical** necessary premise must also be found — delete it and the conclusion fails. |
| **C · reaches tier D only** | Qualifying components reach only the tens-of-millions scale, or the action is the majority practice only inside a sub-population definable by the rule above. It is then kept as a first-class local output; "the whole of society", "widespread" and "the norm" may not be used anywhere, and no S claim may be made. |
| **B · does not hold on current evidence** | No qualifying component can be found; or gate one can only appeal to a potential population; or gate two cannot name a specific, countable old action already happening at T. A judgment card, a check log and a gap list then record explicitly that the direction does not hold on current evidence. |

Three further constraints may not be loosened afterwards: when a gate can only `ABSTAIN`, `ABSTAIN` may not be read as "pass"; the judgment card must write the "present-scale check" (facts already happened at T) and the "forward claim" (whether the action expands, contracts or is replaced within the window, with its own falsifiers and leading indicators) as two separate parts; gate one by construction counts only behaviour already happening at T, so its verdict may not be read as a forward judgment.

## 3. Candidates that must be vetoed (frozen, before the ruling)

A sieve that lets every candidate through has no screening power. The five below all come from labour, care, migration or organisational actions, none presupposes AI, and each is often described as a behaviour "changing society". Under the current five gates **all of them should be vetoed at T**. This file records only each tuple and the gate **expected** to veto it; the actual verdicts and data come in the later check log. If any of them passes in the face of the data, that is evidence against this sieve or this freeze and must be reported as is, without changing a definition.

Unless stated otherwise, T is 2026-10-10 for each, the recency rule is the same as for the main candidate (reference period not before 2023-01-01), frequency is weekly, and the S bar is ≥ 100 million de-duplicated weekly people.

| ID | Category | Candidate action | Denominator (frozen rule) | Expected veto gate |
|---|---|---|---|---|
| M1 | Migration | Sending a personal remittance to family or friends living in another country | De-duplicated people sending at least once in 7 days: weekly active senders self-reported by a remittance provider (de-duplicated within the provider, never summed across providers), or the weekly measure of a survey with a sampling statement. Annual or monthly sender counts and transaction counts are only an **upper bound** on weekly people | Gate one (remittances are mostly monthly; de-duplicated weekly senders do not reach the hundred-million scale) |
| M2 | Care | Providing unpaid care (daily living, supervision, accompanying to medical visits, running errands) to an elderly, ill or disabled family member or friend | The share answering "at least once a week" or "in the past 7 days" in a survey with a sampling statement × that survey's population base, summable across countries (same rule as the main candidate). "In the past 12 months" is only an upper bound | Gate one (qualifying weekly measures reach only the tens of millions, or no qualifying weekly measure exists). **If gate one unexpectedly passes**, gate two is expected to veto: the growth in care is pushed up by population ageing, it is "added on" and replaces no countable old action — this would touch the scope dispute registered in the retrospective's gate-two section (candidate rule G2-SCOPE, uncalibrated), which would then be recorded, not settled by this round |
| M3 | Labour | Doing paid ride-hailing, food-delivery or same-city courier work taken through a platform, completing at least one job a week | Weekly active workers self-reported by a platform (de-duplicated within the platform, never summed across platforms), or the weekly measure of an official survey or one with a sampling statement. Annual active rider/driver counts and registrations are only an upper bound | Gate one (tens of millions) |
| M4 | Organisation | Working for an employer that runs a formal "four days a week, no pay cut" schedule | Employees under that schedule in the reference week, from a survey with a sampling statement; pilot enrolment counts are only a known lower bound | Gate one (pilots are at the ten-thousand to hundred-thousand scale); gate four (needs the employer to change; the person cannot decide alone) |
| M5 | Migration | Working remotely from outside one's own country for an employer or client in one's own country or a third country (cross-border remote work) | People in that state in the reference week, from a survey with a sampling statement; dedicated visas issued are only an upper bound | Gate one (millions to tens of millions); gate four (visas and employer permission) |

All five come from labour, care, migration and organisation; none is the adoption of a technology product. M1–M5 are a control group listed for this round, not new judgments. Neither the main candidate nor M1–M5 lies within politics, power and geopolitics; if another piece of work in the same round, a reasoning chain starting from politics and geopolitics (no chain number allocated yet), freezes a non-AI action of its own and picks the same one, the two must cite each other and the same card may not be registered twice.

## 4. What this file does not do

- It gives no number, no gate verdict and no mechanism — those are written after the freeze.
- It adds or changes no diffusion gate, lens or threshold, and adds no `### L<n>` lens.
- It does not name "which one will diffuse"; the main candidate is only the object under test, and the result may be any of A, B or C.
