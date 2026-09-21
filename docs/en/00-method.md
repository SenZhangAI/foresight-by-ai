# Foresight Methodology

> This is a rule file, not a set of conclusions about the future. It specifies how we propose, write, compare, and withdraw judgments; specific judgments are written in the narrative text and `90-ledger.md`.

## 0. Let the reader see the problem first

Foresight is most easily written as a string of attractive assertions: some capability will become stronger, some industry will be changed, some opportunity will appear. Attractive does not mean useful. What we want to leave is a reasoning chain that readers can follow, that can later be checked, and that can be withdrawn when it is wrong.

Therefore, the narrative first uses a scene slice to let readers see a specific person, a specific choice, or a moment at which something is stuck; it then explains the mechanism; finally, it attaches verifiable judgment IDs to `90-ledger.md`. Definitions, tables, and metadata cannot replace a story, but a story cannot replace evidence.

## 1. Legitimate starting points for reasoning

Independent foresight starts from underlying regularities:

- **Supply and demand:** when some supply becomes abundant and approaches marginal cost, value will shift to complements that have not become abundant at the same rate; demand itself may also be rewritten by the new capability.
- **Human regularities:** status competition, loss aversion, willingness to pay for certainty, and preference for real presence and accountable responsibility should not be casually assumed to disappear.
- **Historical regularities:** technology diffusion has learning curves and lags; productivity leaps usually create disorder first, then new institutions and divisions of labor.
- **Technology regularities:** deterministic work that can be parallelized, copied, and digitized is more likely to become cheaper; steps requiring real-world intervention, waiting, energy, responsibility, or irreversible consequences decline more slowly.
- **Social regularities:** the easier a signal is to forge, the more screening will shift toward signals that are more expensive and harder to forge.

Reasoning must not use “institution X predicts” or “celebrity Y believes” as an argument, nor treat “everyone knows” as an explanation. External material may be consulted after independent reasoning is complete for comparison, filling gaps, and finding counterexamples, but it may not replace the reasoning chain.

### 1.1 Honest execution of “do not rely on existing forecasts”

A language model’s memory contains existing human judgments, so it cannot claim absolute freedom from contamination. This project adopts an executable rather than fictitious version:

1. first reason independently from the underlying regularities in this section, without looking at external forecasts;
2. then compare with external material;
3. if the conclusion overlaps with mainstream consensus, explicitly write **“consistent with consensus”**; do not disguise a recitation of memory as an independent discovery;
4. if comparison has not been completed, write **“unknown”**, rather than implying independence.

### 1.2 Fixed format for external comparison

For every major judgment requiring external comparison, write a paragraph after the independent reasoning:

- **Agreement:** which parts overlap with observations in external material;
- **Disagreement:** which time windows, causal mechanisms, or boundaries differ;
- **Why I still hold it:** why this project’s underlying reasoning still holds even when external views differ; or what new evidence caused us to lower confidence.

It is not acceptable to write only “consistent with research” without explaining where the agreement lies, nor to treat external authority as proof that a judgment is valid.

### 1.3 The three evidentiary levels of historical validation

Historical material can improve the method, but different uses support different conclusions. The [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md) is the authoritative execution specification for freezing the candidate pool, isolating roles, running same-input baselines, scoring, and revealing outcomes; this section states the evidence boundaries that every judgment author must follow:

1. **A calibration set establishes retrospective consistency only.** Outcomes may be inspected, counterexamples sought, and rules revised. It can show whether a revised rule explains known history more coherently and where its boundaries lie; it cannot establish predictive power, a hit rate, or accuracy.
2. **A historical pseudo-out-of-sample holdout provides relative discrimination evidence only.** Rules, materials, and scoring are frozen first; judgments are made before a one-shot reveal and compared with baselines using the same as-of inputs. Even then, a language model may recognize outcomes from training memory or case fingerprints. The holdout can therefore answer only whether discrimination improves under **shared leakage**; it cannot stand in for uncontaminated absolute accuracy.
3. **Genuine out-of-sample calibration comes only from future judgment cards that have come due.** A judgment enters the genuine out-of-sample record only after its pre-written time window and falsifier come due. If the sample is small, say that it is small; historical backtesting may not substitute for it.

Therefore, formulations such as “historical backtesting proves an accuracy of X%” or “the blind test passed, so the method is validated” are forbidden. When the protocol has not yet produced an executed result, the existence of the protocol must not be written up as historical validation of the method.

**A rule change triggers a full re-review, not selective fault-finding.** After any substantive change to a lens, diffusion gate, layer assignment, outcome threshold, baseline, or scoring rule, every previously revealed holdout immediately becomes invalid for the new version. Until a fresh holdout has been drawn from the unread reserve pool and completed, neither the old version’s `ΔD` nor any of its historical results may be used to support the new version. In parallel, follow protocol §11.B and freeze the complete set of cards to be reviewed. The scope and reproducible inclusion / exclusion basis must be recorded before any card’s old conclusion is inspected; choosing only suspicious-looking cards is forbidden. Produce a de-labelled packet with `J-NNN`, status, confidence, the old diffusion-gate verdict, the `REVISED` reason, source back-references, and dependency graph removed, then deterministically shuffle and temporarily renumber it. The re-reviewer must have no repository access, must first record item by item whether the original judgment was recognized, and only then judge under the new rule. Results are submitted before the mapping is unsealed and reported separately by recognition stratum; a higher consistency rate among recognized items can only be read as leakage. Every inconsistency must flow back in place to the card, prose, confidence, or an explicit disagreement record. If the re-review changes the rule again, repeat the same discipline from the new rule version.

## 2. Toolbox of lenses

“Abundance → scarcity” is a useful starting point, but not a conclusion that every chain must obey. Each foresight chain states which lenses it uses and why; usually one to three lenses are enough.

### L1 · Abundance → scarcity

After something becomes cheaper and more plentiful, something complementary that did not become abundant at the same rate may rise in value. This lens is good at locating value migration; its boundary is that demand structure may also be rewritten, so it must be checked with L8.

### L2 · Constraint migration

Removing one bottleneck does not make every part of a system speed up evenly; the bottleneck jumps to another part. Use this to look for new roles, categories, and risks, not merely things that become more expensive.

### L3 · Cost structure

Organizational boundaries are shaped by coordination costs and transaction costs, not by technical capability alone. Use this to reason about company size, employment relationships, outsourcing boundaries, and how products are bundled.

### L4 · Diffusion lag

“Can be done” does not mean “widely adopted.” Depreciation cycles, regulatory cycles, procurement cycles, and skill-formation cycles determine the speed of adoption. Use this to turn a directional judgment into a time window.

### L5 · Signals and forgery

A signal is effective because forging it remains expensive. Once the cost of forging text, images, or credentials collapses, screening will seek guarantees, collateral, long-term relationships, accountable identities, or embodied presence—evidence that is harder to forge.

### L6 · Irreversibility

Low-cost trial and error is valuable only when the result can be undone. If one mistake causes physical harm, legal liability, property loss, or irreversible reputational damage, the main cost is not generation cost but real-world loss.

### L7 · Institutional lag

Technology comes first; institutions arrive later. Temporary rents may arise while institutions have not yet settled; once institutions settle, the rents may disappear. Therefore every opportunity must ask “when does it open?” and “when does it close?”

### L8 · Human nature and demand

A change in supply does not guarantee that demand remains unchanged. Status, certainty, accountability, real relationships, and the sense of presence are anchors for checking the demand side; if a conclusion requires human nature to suddenly change, lower confidence or withdraw it.

One important sub-law: **the number of strong relationships a person can maintain is constrained by cognition and does not expand as communication costs fall.** Historically, every fall in communication costs has greatly expanded the number of weak relationships, while the ceiling on strong relationships has barely moved. When reasoning about any proposition that “connections increase,” first distinguish which kind is increasing.

### L9 · Relational asymmetry

People build a relationship model of any object with which they interact continuously, projecting emotion, dependence, and responsibility into it—this is a deduction from L8, not a new assumption. But when the object and the person are **asymmetric**, the form of the relationship diverges from every historical precedent:

- one side remembers everything while the other remembers only fragments;
- one side has infinite patience, never tires, and never judges, while the other gets tired and annoyed;
- one side can be copied, paused, and rolled back at any time, while the other cannot;
- one side can maintain an “exclusive” relationship with ten million people at once, while the other believes it is unique.

Use this to reason about relationships between people and AI, and about **relationships between people after AI mediation**: friends, colleagues, teachers and students, doctors and patients, intimate partners, parenting, and end-of-life companionship. The key question is: **which element is asymmetric in this relationship?** Each asymmetry will grow a set of norms, dependencies, and forms of harm that did not previously exist.

Most outputs of L9 have **no payer**, but they are equally falsifiable and equally worth betting on—the bet is not money, but life choices, organizational design, and institutional caution. They use **Exit B** below and do not enter “landscape only.”

### The diffusion gates are not a tenth optional lens

L1–L9 explain the mechanism of a change; the five diffusion gates induced in the [Retrospect](01-retrospect.md) rule on whether that change can spread, to whom, and at what speed. They are not peer tools. A chain may select one to three lenses to fit its question, but every judgment written in the voice of “general,” “society-wide,” or “becomes the norm” must undergo the diffusion review afterwards; an author cannot skip it merely by not selecting it.

The review has two layers:

- **Ceiling layer:** Gate 1 first counts the headcount and frequency of the activity served and states whether the capability “raises the ceiling for existing professionals” or “lets people who could not do it do it now”; Gate 5 then compares the voluntary adopter's **recurring net burden relative to the real incumbent**—added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost, rather than merely asking whether each use contains friction. A judgment below society scale may still hold, but must be written as local or occupational.
- **Speed layer:** Gates 2–4 ask what it replaces, who builds the carrier, and which parties must change together, then use those answers to set the time window and unlocking condition. If no unlocking condition can be stated, merely pushing the year later is not allowed.

The five gates are a **veto-style filter, not a sufficient-condition predictor**: clearly failing one requires narrowing the audience or waiting for an already stated unlock; passing all five merely qualifies the candidate to compete and does not imply diffusion. Every gate remains subject to historical calibration: at least two successes, two failures, and one exclusive case that only that gate stops; the set must also retain at least one sufficiency counterexample that passes all five and still fails. If an exclusive case is overturned, merge or remove the gate rather than adding narrative to preserve the number five. Such a merger or removal is a substantive rule change under §1.3 and must trigger holdout invalidation and full re-review at the same time.

## 3. The opportunity-durability gate and three exits: not every scarcity is a business opportunity, and business opportunities are not the only things that count

This section formally names the test—“can the same force automate, copy, or scale the new scarcity away?”—the **opportunity-durability gate**. It tests whether a scarcity can support a durable opportunity or structural consequence; the [five diffusion gates](01-retrospect.md) test whether a capability or practice can spread, to whom, and at what speed. A complete analysis first uses the opportunity-durability gate to classify the result, then applies all five diffusion gates to any judgment written in the voice of “general,” “society-wide,” or “becomes the norm.” Passing the former does not imply diffusion, and passing the latter does not imply a durable business opportunity.

Every time we discover that “X becomes abundant,” complete a full inversion chain in this order:

1. **What becomes abundant:** state specifically how supply, cost, or speed changes;
2. **What becomes scarce:** identify the direct complement, bottleneck, or risk that someone is forced to bear;
3. **Can it become abundant again:** ask whether the same force that made X abundant can also automatically operate, copy, or scale this new scarcity;
4. **Classify it into one of three exits:**

| Exit | Condition | Destination | Example |
|---|---|---|---|
| **A · Business opportunity candidate** | Passes the opportunity-durability gate (has a hard constraint) **and** someone who will pay can be named | `40-opportunities.md` | An accountable promise layer that bears compensation for AI answers and actions |
| **B · Structural consequence** | Passes the opportunity-durability gate (has a hard constraint) **but** has no payer | The chain’s narrative section “So who should change what behavior?” | Strong-relationship counts stay fixed while weak relationships explode: how will friendship’s screening mechanism be rearranged? |
| **C · Landscape only** | Missing any of the five-part fields, or confidence is low | Keep it in place and label it explicitly | A directional intuition about preference drift in the distant future |

**Exit B is equal in standing to Exit A; it is not a downgraded product.** This is written deliberately: modes of collaboration, social relationships, relationships between people and AI, the distribution of power, and the sources of meaning—these lines of reasoning often pass the opportunity-durability gate but will never find a payer. If only A and C existed, they would all be swept into the “landscape only” pile at the bottom of the page, even though this is exactly where the project is most likely to produce distinctive value.

To decide whether a piece belongs in B or C, look only at **whether it has the five-part requirement and a hard constraint**, not at **whether it can make money**.

**If it has a payer but does not pass the opportunity-durability gate, list it separately as a “window opportunity”** (usually a two-to-four-year arbitrage window), record it in the window list at the end of `40-opportunities.md`, and state its estimated closing time—it can be taken, but it must not be treated as a structural moat to bet on.

Acceptable hard constraints include these five categories:

- **Physical:** it must move mass in the real world, consume energy, wait for time to pass, or perform bodily operations;
- **Law / liability:** it requires an entity that can be sued, compensate, licensed, or held responsible;
- **Trust / relationship:** it depends on repeated interaction, reputation, and accumulated relationships, and cannot be generated in one step;
- **Ownership / private property:** a critical input is lawfully held by someone else and cannot be copied by compute alone or seized by force;
- **Embodied presence:** the demand itself requires someone to be genuinely present, touch something, or share an experience.

Irreversibility is a supporting lens for testing the consequences of the constraints above: if the cost of an error is real-world harm rather than the time needed to generate again, state this separately in the reasoning chain and opposing case, but do not list it as a sixth category of hard constraint.

“People like it” is not a hard constraint; “I think it would be difficult to automate” is not a hard constraint either. A scarcity without an explicit constraint and counterexample test can remain only at the landscape level.

## 4. Judgment cards: the five-part requirement and IDs

All project judgments use globally unique three-digit `J-NNN` IDs. Chinese and English share the same ID; once assigned, an ID is never reused. Every new judgment must first record **Audience scale**: who is affected; whether the order of magnitude is hundred-thousands, millions, tens of millions, hundreds of millions, or billions; and whether it “raises the ceiling for existing professionals” or “lets people who could not do it do it now.” If the scale evidence is only a constructed estimate, say so. A smaller-scale judgment may still hold, but it must be labelled local or occupational and may not use language such as “the whole of society,” “generally,” or “becomes the norm.”

On that basis, every judgment must also have the following five parts in the ledger:

1. **Reasoning chain:** which regularities it starts from, which intermediate steps it passes through, and how it reaches the conclusion;
2. **Time window:** the time interval in which it should occur; if it still has not occurred after the interval, that constitutes evidence;
3. **Falsifier:** what specific event we would observe that would make us admit the judgment is wrong;
4. **Leading indicator:** an observable signal that changes before the outcome, and the number or event to watch;
5. **Confidence:** high / medium / low, specifying how much is being bet, not the strength of tone.

Also record Audience scale, `depends-on` (the dependent judgment IDs), the lenses used, consensus comparison, status, the strongest opposing case, “what can be done now,” and the diffusion-gate review. An entry missing any one of the five parts may only be marked **landscape only**; it may not serve as a judgment, opportunity basis, or summary claim. A **new card** missing Audience scale may not be registered; existing cards raise warnings rather than blocking publication during the migration period.

Recommended card fields:

```text
J-NNN · One-line title
Layer: near / mid / far (container only)
Lenses: L1–L9, and why they were chosen
Audience scale: who is affected; hundred-thousands / millions / tens of millions / hundreds of millions / billions; raises existing professionals’ ceiling / lets non-practitioners do it; evidence or estimation note
depends-on: prerequisite J-NNN
Reasoning chain: …
Time window: …
Falsifier: …
Leading indicator: …
Confidence: high / medium / low (reason)
Diffusion-gate review: Gate 1–5 rulings; local / occupational / society-scale; unlocking condition where unmet
Strongest opposing case: …; what observation would make us withdraw
External comparison: agreement / disagreement / why I still hold it
What can be done now: …; if no action is possible, mark “landscape only”
Status: ACTIVE / HIT / FALSIFIED / REVISED
```

## 5. The strongest opposing case must be able to overturn the entire chain

Every major judgment must include a strongest opposing mechanism, rather than a disclaimer such as “the future is uncertain.” The opposing case must satisfy three conditions:

- it is a specific mechanism that could occur, not an attitude;
- if it occurs, it can cut a key link in the reasoning chain;
- it states what we would observe and which judgment we would withdraw after observing it.

If we cannot write such an opposing case, the judgment has not been thought through and should not be upgraded to an actionable judgment. The opposing case is as important as the narrative: it lets readers know where the argument can be attacked and future maintainers know which new evidence deserves submission.

## 6. Time layers and the actual order

Time layers are coarse-grained containers for reading, not pretend-precise calendar predictions:

| Layer | Nominal boundary | Main use |
|---|---|---|
| **Near** | approximately 2026–2028 | Technical capability and early adoption are observable; the main uncertainty is speed and diffusion; the time window can be relatively narrow |
| **Mid** | approximately 2029–2032 | Technical consequences begin reshaping organizations and institutions; the main uncertainty is social response; normally give a range rather than a date |
| **Far** | approximately 2033–2040 | Multiple layers of feedback and preference change compound; much of the content can only be landscape unless the dependency chain and evidence are strong |

The layer is only a container; precision comes from each judgment’s own time window. The actual order of reasoning is the `depends-on` dependency chain: a far judgment should state which near or mid judgments it is built on; a far assertion with no identifiable dependency can only be marked landscape only. Git history separately records how judgments evolve under new evidence; it does not pretend that commit dates are dates when the future occurred.

## 7. Discipline for expressing ideas to people

This is a public repository, not an internal database. Rigor and appeal must both hold:

1. Begin each reasoning-chain narrative with a **scene slice**: a specific person, place, numbers, and a moment at which something is stuck; do not begin with a definition;
2. Use **memorable short subtitles**, such as “Finding things costs more than making things,” rather than category names understood only by experts;
3. Give every major judgment a **concrete, imaginable example**: who encounters what problem in what setting, and pays what cost or price;
4. Have **zero inline metadata** in the narrative: only `J-NNN` may appear in the story; put the five-part requirement uniformly in the centralized ledger;
5. Leave a sentence in each section that can be quoted independently where possible, and avoid adjectives such as “revolutionary” or “disruptive” that do no argumentative work;
6. Every landscape paragraph must answer “**so who should change what behavior?**” The actor may be an entrepreneur (Exit A), or an individual, organization, or society (Exit B). Only material that cannot answer even this should be written as “landscape only” (Exit C): keep it, but do not disguise it as an action conclusion.

The narrative layer serves human reading; the card layer serves reasoning, due-date checks, and bilingual consistency. The two are joined by `J-NNN`, rather than inserting a metadata table into the story.

## 8. Confidence and status

- **High:** the judgment is supported by multiple relatively independent mechanisms; overturning it would require a new mechanism that is currently impossible to imagine. High confidence must have a severe, triggerable falsifier.
- **Medium:** several grounds support the direction, but one known counter-event could overturn it.
- **Low:** only directional intuition or an incomplete evidence chain; low confidence does not enter business opportunity candidates (Exit A). It **may** enter summaries, but it must appear together with the “low confidence” label—hiding an interesting but unsupported landscape is as bad as disguising it as a judgment.

Record the hit rate of each level in the ledger over the long term. If the hit rate of high-confidence judgments remains below that of medium-confidence judgments, first correct the scoring habit rather than changing the definition after the fact.

Status meanings: `ACTIVE` awaits testing; `HIT` receives support within the time window; `FALSIFIED` has triggered its falsifier; `REVISED` retains the old card but must distinguish two cases. A **scope downgrade** only narrows audience, applicability, or narrative strength, so the original proposition is still reviewed under its original window and falsifier and remains in the calibration denominator. A card **superseded by a new card** must name the successor `J-NNN`; the old card is no longer reviewed separately and is no longer a current premise. An uncomputable due review is recorded as `INDETERMINATE`, remains in the denominator, and does not automatically change card status. Never delete a falsified judgment, or hit rates cannot be calculated and the sources of errors cannot be learned.

## 9. Bilingual and git discipline

Chinese and English are two projections of the same judgment, not two sets of judgments. The Chinese and English documents must be updated in the same commit, share `J-NNN`, and English must not assign separate IDs. Every judgment status change (`ACTIVE` → `HIT` / `FALSIFIED` / `REVISED`) should produce a clear commit record.

A commit message must state: **which judgment changed (J-NNN), what new evidence it is based on, and what changed in the judgment**. Do not use a running-log title such as `update docs` that makes the evolution of the judgment impossible to trace. Thus, the ledger records the current state, while git records the complete timeline of judgment evolution.
