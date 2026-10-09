# Countable social action freeze record (2026-10-10)

[中文版](social-action-freeze-2026-10-10.md)

This file freezes, **before any numerical evidence is collected and before any mechanism is written**, a set of candidate-action tuples `(candidate action, decision time T, denominator, frequency)`, their de-duplication rules and exclusions, and decision rules written in advance. It is landed as a commit of its own, so its commit time is the freeze time; the reasoning chain, judgment card and check log that follow may only cite the definitions here and may not rewrite them. If a definition later turns out to be unworkable, the only allowed move is to record "frozen definition failed" in a new file with the reason — never to edit it in place into a version that passes more easily.

> **Why freeze first.** This archive's [social-scale judgment register](../en/91-social-scale-register.md) currently reports **0** judgments that pass gate one in usable form, and it has received a challenge recorded verbatim: "AI 哪有那么多要决策的人？" ("Where would AI even find that many people who need to make decisions?"). The easiest mistake in answering it is to see an attractive number first and then trim the action definition, the denominator and the frequency until they just clear the gate. Freezing the definitions first closes that exit: what the denominator is, what does not count as one, and what the bar is are all written before any number is seen.

Every threshold applied here is taken from existing text; this file adds no rule:

- **S · social-scale**: the target action reaches at least hundred-million-scale weekly use, or billion-scale daily use ([historical validation protocol §6](../en/02-historical-validation-protocol.md#6-outcome-coding-and-necessary-condition-scoring)).
- **D · segment / domain diffusion**: becomes the majority practice inside a sub-population definable at T, without reaching S (same section).
- **Denominator discipline**: the same acting subject, definable at T, de-duplicated and counted at a stated frequency; affected population, demand population or potential population may not stand in for it ([methodology §4](../en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids)).
- **The five diffusion gates** are applied in their current wording from the [historical retrospective](../en/01-retrospect.md) and [methodology · the diffusion gates are not a tenth optional lens](../en/00-method.md#the-diffusion-gates-are-not-a-tenth-optional-lens); they are veto-style necessary conditions, not a sufficient-condition predictor (`J-066`).

---

## 1. Main candidate tuple (frozen)

| Item | Frozen definition |
|---|---|
| **Candidate action** | A person **actively** starts at least one question, or hands over one task, to a general-purpose AI assistant that is open to the public and whose main interface is natural-language conversation (for example the chat interfaces of ChatGPT, Gemini, Doubao, DeepSeek, Copilot, Meta AI). |
| **Decision time T** | 2026-10-10. No piece of evidence may be published later than T; information after T may be used only at the check date, never for this decision. |
| **Denominator** | The **de-duplicated number of people** who perform the action at least once in a 7-day window. Only two kinds of source qualify: (i) a **weekly active user** figure publicly reported by a single service — de-duplicated within that service, self-reported and unaudited, counted in accounts/users, and therefore only a **lower bound** on the people performing the action; figures from **different services may not be added**; (ii) a population survey with a sampling statement, reporting the share who used one "in the past week", multiplied by the population the survey represents. |
| **Frequency** | Weekly (at least once every 7 days). |
| **S bar** | A de-duplicated weekly denominator of ≥ 100 million from any qualifying source. |
| **Old action for gate two (frozen)** | Typing one information query into a web search engine. At T it is a specific, countable action that has long happened at scale. "Asking someone nearby the same question" is also being replaced, but it cannot be counted, so it is supplementary only and not a basis for the gate-two verdict. |

**What does not count toward the denominator (frozen)**:

1. Passive exposure the user did not start — AI summaries that appear automatically on a search results page, auto-generated in-app summaries, AI content in a recommendation feed. These are **reach**, not a behavioural denominator.
2. Programmatic, API, or in-company automated calls.
3. Accounts that only downloaded or registered and never started a conversation.
4. Monthly active users, cumulative users, downloads, visits, message counts — none of these is a weekly de-duplicated head count, and none may be converted into one.
5. Sums of weekly active users across services.

## 2. Decision rules written in advance (frozen)

| Result | Condition (all written before any number is seen) |
|---|---|
| **A · reaches S** | At least one qualifying source gives a de-duplicated weekly denominator ≥ 100 million at T; gate two can name the old action above; none of gates two to five vetoes; and an additional L8 demand-side review is done. At least one **non-technical** necessary premise must also be found — delete it and the conclusion no longer holds. |
| **C · D only** | Qualifying sources support only tens-of-millions scale, or majority practice only inside a sub-population definable at T. It is then kept as a first-class local output; the phrases "the whole of society", "universal" and "becomes the norm" are banned throughout, and passing S may not be claimed. |
| **B · does not hold now** | No qualifying denominator can be found; or gate one can only appeal to the number of potential actors; or gate two cannot name a specific, countable old action already happening at T. The judgment card, check log and gap list then record plainly that the direction does not hold on current evidence. |

Two further constraints may not be relaxed afterwards: if only self-reported weekly active users exist and no survey source does, the conclusion must state that "the lower bound comes from self-reported, unaudited figures"; and if any gate can only return `ABSTAIN`, that `ABSTAIN` may not be read as "pass".

## 3. Candidates this direction must veto (frozen, before any verdict)

A sieve that lets every candidate in a direction through has no selection power. The six candidates below come from the same direction ("which social-scale everyday action will AI bring") and are the ones most often called "the next smartphone". Under the current five gates, **all of them should be vetoed at T**; this file only writes down each tuple and the gate **expected** to veto it — the actual verdicts and data come in the later check log. If any of them passes in the face of the data, that is evidence against this sieve or this freeze, and it must be reported as it is, without changing the definition.

| ID | Candidate action | T | Denominator (frozen) | Frequency | Gate expected to veto |
|---|---|---|---|---|---|
| N1 | Facing a batch of AI-generated candidate proposals, choosing one and owning the result (`J-072`) | 2026-10-10 | De-duplicated people whose job requires batch-produced candidates, who hold sign-off authority, at least weekly | Weekly | Gate one (the existing constructed estimate is million-scale) |
| N2 | Companionship-style conversation with an AI companion / character app | 2026-10-10 | Daily or weekly actives self-reported by companion apps (de-duplicated within a service, not summed) | Daily | Gate one |
| N3 | Wearing smart glasses with an AI assistant every day | 2026-10-10 | Cumulative shipments are only an **upper bound** on wearers (devices are not people) | Daily | Gate one, gate five |
| N4 | Letting a general-purpose (humanoid) home robot do housework | 2026-10-10 | Installed base in homes and in use (a device upper bound) | Weekly | Gate one, gate three |
| N5 | Riding a driverless robotaxi | 2026-10-10 | Weekly paid rides are only an **upper bound** on weekly riders | Weekly | Gate one, gate four |
| N6 | Handing one purchase or booking to an AI agent that orders and pays | 2026-10-10 | De-duplicated weekly users of agent checkout as publicly reported by a platform | Weekly | Gate one (no qualifying denominator expected at T), gate four |

N1 is an existing judgment in this archive (`J-072`); it is listed so this round's verdict can be compared with the old one. N2–N6 are a control group listed this round; they are not new judgments.

## 4. What this file does not do

- It gives no numbers, no gate verdicts and no mechanism — all of that is written after the freeze.
- It adds or changes no diffusion gate, lens or threshold.
- It does not name "which one will diffuse"; the main candidate is only the object under test, and the result can be any of A, B or C.
