# Judgment Ledger

> The single register for all project judgments. Narrative documents cite `J-NNN`; the complete judgment card lives only here.
> This ledger records how judgments are proposed, linked, revised, and reviewed. A falsified judgment is never deleted.
> Last updated: 2026-09-18

---

## 1. How to use this ledger

### 1.1 Judgment-card fields

A testable judgment must contain every field below. If any field is missing, label the statement **landscape only**; it cannot serve as a business-opportunity judgment or summary conclusion.

- **ID**: `J-NNN`, three digits, globally unique; shared by Chinese and English; never reuse an old or revised ID.
- **Proposed date**: the date the judgment was first proposed, `YYYY-MM-DD`.
- **One-sentence judgment**: a proposition that can be supported or refuted by facts.
- **Reasoning chain**: each step from first principles and selected lenses; do not replace reasoning with another institution's prediction.
- **Time window**: the interval in which the judgment is expected to occur or remain valid.
- **Falsifier**: one concrete, observable event or data result that would make the author admit the judgment is wrong.
- **Leading indicator**: an observable signal expected to move before the outcome, with its observation frequency or source.
- **Confidence**: high / medium / low. Low-confidence items remain landscape only and do not enter the opportunity list.
- **depends-on**: the prerequisite `J-NNN` judgments. Write `—` when there is no dependency; never use a vague “see above.”
- **Status**: **ACTIVE** (awaiting evidence), **HIT** (supported), **FALSIFIED** (falsifier triggered), or **REVISED** (revised; old card retained). If rewritten, preserve the old card and assign the new version a new ID.

### 1.2 Completed example card (example only)

> **Example card | EXAMPLE-J-000 (explicitly excluded from the formal numbering)**
> - **ID**: EXAMPLE-J-000
> - **Proposed date**: 2026-09-18
> - **One-sentence judgment**: In a hypothetical market, if the unit cost of repeatedly generating proposals falls by an order of magnitude, the value of a service that merely supplies more proposals will decline within three years.
> - **Reasoning chain**: Supply increases → proposal marginal cost falls → buyers no longer lack proposal quantity → value moves to selection and validation. This demonstrates dependency notation and is not adopted as a project judgment.
> - **Time window**: 2026-09-18 to 2029-09-18.
> - **Falsifier**: By 2029-09-18, buyers still broadly pay a premium for proposal quantity rather than verifiable outcomes, without supply or regulatory constraints explaining it.
> - **Leading indicator**: Unit generation cost and the median amount buyers pay for human selection, recorded every six months.
> - **Confidence**: Medium (example value).
> - **depends-on**: —
> - **Status**: ACTIVE (example value).

Copy the fields, not the example ID. The example does not enter the formal index.

---

## 2. Registered-judgment overview

| ID | Proposed date | One-sentence judgment | Time window | Confidence | depends-on | Source | Against consensus | Status | Next review |
|---|---|---|---|---|---|---|---|---|---|
| J-001 | 2026-09-18 | Unit reasoning cost falls another order of magnitude by the end of 2029 | 2026–2029 | High | — | [C1](chains/10-generation-becomes-free.md) | Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude. | ACTIVE | 2027-03-31 |
| J-002 | 2026-09-18 | Objective quality selection is a 2–4 year window, not durable scarcity | through 2029 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Retain with a different mechanism: objective selection may be partly internalized, while liability- and domain-sensitive QA may persist. | ACTIVE | 2027-03-31 |
| J-003 | 2026-09-18 | Ownership and usable form of private personal or organizational context are more likely to become durable scarcity | 2027–2033 | Medium | J-001, J-002 | [C1](chains/10-generation-becomes-free.md) | Retain with a narrower evidence boundary: sources support governance of private context, not that it must become durable scarcity. | ACTIVE | 2027-06-30 |
| J-004 | 2026-09-18 | As AI executes actions, infrastructure that makes actions reversible becomes scarce | 2027–2032 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified. | ACTIVE | 2027-06-30 |
| J-005 | 2026-09-18 | Raw signals, accountable commitments, and verified causality become more valuable than reproducible text | 2029–2033 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate. | ACTIVE | 2027-06-30 |
| J-006 | 2026-09-18 | Reasoning throughput precedes long-horizon autonomy | 2026–2028 | High | J-001 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable. | ACTIVE | 2027-03-31 |
| J-007 | 2026-09-18 | Resumable context precedes reliable long-term memory | 2026–2029 | High | J-006 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order. | ACTIVE | 2027-03-31 |
| J-008 | 2026-09-18 | Sourced long-term memory becomes a prerequisite for reliable collaboration | 2028–2031 | Medium | J-007 | [Technology Capability Sequence](05-tech-sequence.md) | Retain with a different mechanism: provenance, versioning, and revisability improve auditability, but are not proven necessary for every high-value collaboration. | ACTIVE | 2027-06-30 |
| J-009 | 2026-09-18 | Continuous execution in constrained workflows matures first | 2027–2030 | High | J-008 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain. | ACTIVE | 2027-06-30 |
| J-010 | 2026-09-18 | Long-horizon autonomy follows constrained continuous execution | 2029–2033 | Medium | J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited. | ACTIVE | 2027-06-30 |
| J-011 | 2026-09-18 | Cross-media consistency precedes long-range coherence | 2027–2030 | Medium | J-006, J-007 | [Technology Capability Sequence](05-tech-sequence.md) | Retain but with insufficient evidence: research supports long-range coherence difficulty, not that cross-media consistency must arrive first. | ACTIVE | 2027-06-30 |
| J-012 | 2026-09-18 | Cross-time coherence depends on state and evaluation | 2029–2034 | Medium | J-008, J-011 | [Technology Capability Sequence](05-tech-sequence.md) | Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation. | ACTIVE | 2027-06-30 |
| J-013 | 2026-09-18 | Checkable tool calls precede open-environment action | 2027–2030 | High | J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment. | ACTIVE | 2027-03-31 |
| J-014 | 2026-09-18 | Rehearsable environments follow single-tool integration | 2028–2032 | Medium | J-009, J-013 | [Technology Capability Sequence](05-tech-sequence.md) | Retain only as an evidence-limited landscape: governance supports rehearsable, recoverable environments, not a market order or window. | ACTIVE | 2027-06-30 |
| J-015 | 2026-09-18 | Formal verification precedes open-world evaluation | 2026–2029 | High | J-006, J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration. | ACTIVE | 2027-03-31 |
| J-016 | 2026-09-18 | Open-world evaluation is the final gate for expanding autonomy | 2029–2035 | Medium | J-010, J-012, J-014, J-015 | [Technology Capability Sequence](05-tech-sequence.md) | Retain only as an evidence-limited landscape: open-world feedback may constrain autonomous authority, but is not established as the final gate. | ACTIVE | 2027-06-30 |
| J-017 | 2026-09-18 | AI mediation expands weak-tie coordination faster than strong relationships, without expanding the number of relationships in which people can remain present | 2027–2033 | Medium | J-006, J-007 | [C1](chains/10-generation-becomes-free.md) | Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect. | ACTIVE | 2027-06-30 |
| J-018 | 2026-09-18 | Parallel reasoning becomes the default workflow before long-horizon autonomy | 2026–2028 | High | J-006, J-009 | [Near-term landscape](10-near.md) | Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference. | ACTIVE | 2027-03-31 |
| J-019 | 2026-09-18 | Saving tokens itself is a window, not durable scarcity | 2026–2028 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Retain with a different mechanism: cost decline can come from inference efficiency and hardware scheduling; public prices do not prove optimization premiums vanish. | ACTIVE | 2027-03-31 |
| J-020 | 2026-09-18 | Reproducible content keeps falling in marginal price as objective selection is internalized | 2026–2028 | Medium | J-002, J-015 | [Near-term landscape](10-near.md) | Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers. | ACTIVE | 2027-03-31 |
| J-021 | 2026-09-18 | First-hand field signals earn a premium earlier than second-hand expression | 2026–2029 | Medium | J-005, J-015 | [Near-term landscape](10-near.md) | Retain with a different mechanism: traceable first-hand sources may gain value first; broad field-premium pricing is unproven. | ACTIVE | 2027-06-30 |
| J-022 | 2026-09-18 | As forgable signals multiply, selection moves toward more expensive credentials | 2026–2029 | Medium | J-005, J-017 | [Near-term landscape](10-near.md) | Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown. | ACTIVE | 2027-06-30 |
| J-023 | 2026-09-18 | Attention shifts from expression toward relationships and fulfilled commitments | 2027–2030 | Medium | J-017, J-022, J-013 | [Near-term landscape](10-near.md) | Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift. | ACTIVE | 2027-06-30 |
| J-024 | 2026-09-18 | Credentials may be re-layered, but the institutional destination remains uncertain | 2027–2032 | Low | J-022, J-013 | [Near-term landscape](10-near.md) | Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only. | ACTIVE | 2027-06-30 |
| J-025 | 2026-09-18 | Small teams complete more verifiable output with fewer steps | 2027–2030 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient. | ACTIVE | 2027-06-30 |
| J-026 | 2026-09-18 | Responsibility boundaries do not disappear at the same rate as knowledge-work capacity | 2027–2032 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts. | ACTIVE | 2027-06-30 |
| J-027 | 2026-09-18 | Rented compute spreads capability without distributing gains evenly | 2026–2029 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity. | ACTIVE | 2027-03-31 |
| J-028 | 2026-09-18 | Data, distribution, and liability access may become new bargaining nodes | 2027–2032 | Low | J-005, J-013 | [Near-term landscape](10-near.md) | Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven. | ACTIVE | 2027-06-30 |
| J-029 | 2026-09-18 | Status, certainty, embodied presence, and responsibility remain demand-side anchors | 2026–2030 | Medium | J-017, J-011 | [Near-term landscape](10-near.md) | Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven. | ACTIVE | 2027-06-30 |
| J-030 | 2026-09-18 | AI mediates coordination but cannot mediate shared experience | 2027–2032 | Low | J-017, J-011 | [Near-term landscape](10-near.md) | Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient. | ACTIVE | 2027-06-30 |
| J-031 | 2026-09-18 | Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution | 2026–2032 | Medium | J-010 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: logging, oversight, and risk control have institutional support; a complete rollback gate and its window are unverified. | ACTIVE | 2027-06-30 |
| J-032 | 2026-09-18 | Authorization review and exception escalation become scarcer than execution steps | 2027–2032 | Medium | J-013 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing. | ACTIVE | 2027-06-30 |
| J-033 | 2026-09-18 | Verifiable records of real interventions become more valuable than explanation itself | 2029–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: compliance evidence, model risk controls, and intervention records are gaining value; superiority to explanation is unproven. | ACTIVE | 2027-06-30 |
| J-034 | 2026-09-18 | Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation. | ACTIVE | 2027-06-30 |
| J-035 | 2026-09-18 | Responsibility collateral enters the transaction structure for consequential AI output | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: liability governance, insurance, and compensation are entering transactions, but universal “liability collateral” is unproven. | ACTIVE | 2027-06-30 |
| J-036 | 2026-09-18 | Long-term fulfillment records allocate attention better than one-off natural expression | 2027–2032 | Medium | J-017 | [Mid-term landscape](20-mid.md) | Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence. | ACTIVE | 2027-06-30 |
| J-037 | 2026-09-18 | Comparable small teams produce more verifiable output | 2027–2031 | Medium | J-009 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams. | ACTIVE | 2027-06-30 |
| J-038 | 2026-09-18 | Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps | 2027–2032 | Medium | J-013 | [Mid-term landscape](20-mid.md) | Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven. | ACTIVE | 2027-06-30 |
| J-039 | 2026-09-18 | Rented models become abundant, while energy, data, and channel control create access rents | 2027–2033 | Medium | J-001 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: model rental may become abundant, while energy and infrastructure constraints are real; data and channel rents remain unproven. | ACTIVE | 2027-06-30 |
| J-040 | 2026-09-18 | Balance sheets able to absorb AI accidents become a separate scarcity | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven. | ACTIVE | 2027-06-30 |
| J-041 | 2026-09-18 | AI first expands the coordination radius of weak ties | 2027–2033 | Medium | J-017 | [Mid-term landscape](20-mid.md) | Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects. | ACTIVE | 2027-06-30 |
| J-042 | 2026-09-18 | Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only) | 2027–2033 | Low | J-011 | [Mid-term landscape](20-mid.md) | Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects. | ACTIVE | 2027-06-30 |
| J-043 | 2026-09-18 | High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only) | 2033–2040 | Low | J-031, J-032, J-014 | [Far-term landscape](30-far.md) | Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants. | ACTIVE | 2027-12-31 |
| J-044 | 2026-09-18 | Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only) | 2033–2040 | Low | J-032, J-040 | [Far-term landscape](30-far.md) | Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished. | ACTIVE | 2027-12-31 |
| J-045 | 2026-09-18 | As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only) | 2033–2040 | Low | J-033, J-034 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: provenance standards support the relative importance of original records, not inevitable scarcity of unarranged observation. | ACTIVE | 2027-12-31 |
| J-046 | 2026-09-18 | High-liability settings retain a premium for field causal records (landscape only) | 2033–2040 | Low | J-033, J-034 | [Far-term landscape](30-far.md) | Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven. | ACTIVE | 2027-12-31 |
| J-047 | 2026-09-18 | Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only) | 2033–2040 | Low | J-041, J-042 | [Far-term landscape](30-far.md) | Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence. | ACTIVE | 2027-12-31 |
| J-048 | 2026-09-18 | Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only) | 2033–2040 | Low | J-041, J-042 | [Far-term landscape](30-far.md) | Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint. | ACTIVE | 2027-12-31 |
| J-049 | 2026-09-18 | As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only) | 2033–2040 | Low | J-041, J-038 | [Far-term landscape](30-far.md) | Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent. | ACTIVE | 2027-12-31 |
| J-050 | 2026-09-18 | The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only) | 2033–2040 | Low | J-041, J-038 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: governance preserves human confirmation at key points, but does not prove a wholesale shift in collaboration value. | ACTIVE | 2027-12-31 |
| J-051 | 2026-09-18 | Abundant advice does not automatically disperse real action rights (landscape only) | 2033–2040 | Low | J-039, J-040, J-035 | [Far-term landscape](30-far.md) | Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven. | ACTIVE | 2027-12-31 |
| J-052 | 2026-09-18 | Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only) | 2033–2040 | Low | J-039, J-040, J-035 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: energy, real-world data, authorization, and compensation have present-day entry points; the long-term combination remains an inference. | ACTIVE | 2027-12-31 |
| J-053 | 2026-09-18 | As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only) | 2033–2040 | Low | J-042, J-029 | [Far-term landscape](30-far.md) | Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence. | ACTIVE | 2027-12-31 |
| J-054 | 2026-09-18 | Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only) | 2033–2040 | Low | J-042, J-029 | [Far-term landscape](30-far.md) | Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven. | ACTIVE | 2027-12-31 |
| J-055 | 2026-09-18 | In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium | 2029–2033 | Medium | J-005, J-033, J-034, J-039 | [C2: How Real-World Signals Become Contract Assets](chains/20-real-signals-become-contracts.md) | Directionally consistent with stronger data governance and provenance, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven. | ACTIVE | 2027-06-30 |



The overview is a navigation aid. Every full card, strongest opposing mechanism, and evidence is registered in this ledger; source links return to the relevant narrative or technology chain, and IDs and statuses stay synchronized here. The overview’s “near / mid / far” labels are reading containers only; each card’s own time window is the judgment boundary, so overlap with or across a container is not a contradiction.
---

## 3. The `depends-on` graph

### Notation

Use comma-separated formal IDs, for example: `depends-on: J-001, J-002`. A dependency means “if the upstream mechanism fails, this judgment must be reviewed”; it does not mean that both judgments happen simultaneously or point to an article location. A far-horizon judgment without an explicit near-term dependency should be downgraded to landscape only.

Current dependency tree (complete view; each card’s `depends-on` is authoritative):

```text
J-001 (root)
J-002 <- J-001
J-003 <- J-001, J-002
J-004 <- J-001
J-005 <- J-001
J-006 <- J-001
J-007 <- J-006
J-008 <- J-007
J-009 <- J-008
J-010 <- J-009
J-011 <- J-006, J-007
J-012 <- J-008, J-011
J-013 <- J-009
J-014 <- J-009, J-013
J-015 <- J-006, J-009
J-016 <- J-010, J-012, J-014, J-015
J-017 <- J-006, J-007
J-018 <- J-006, J-009
J-019 <- J-001, J-006
J-020 <- J-002, J-015
J-021 <- J-005, J-015
J-022 <- J-005, J-017
J-023 <- J-017, J-022, J-013
J-024 <- J-022, J-013
J-025 <- J-009, J-013
J-026 <- J-009, J-013
J-027 <- J-001, J-006
J-028 <- J-005, J-013
J-029 <- J-017, J-011
J-030 <- J-017, J-011
J-031 <- J-010
J-032 <- J-013
J-033 <- J-005
J-034 <- J-005
J-035 <- J-005
J-036 <- J-017
J-037 <- J-009
J-038 <- J-013
J-039 <- J-001
J-040 <- J-005
J-041 <- J-017
J-042 <- J-011
J-043 <- J-031, J-032, J-014
J-044 <- J-032, J-040
J-045 <- J-033, J-034
J-046 <- J-033, J-034
J-047 <- J-041, J-042
J-048 <- J-041, J-042
J-049 <- J-041, J-038
J-050 <- J-041, J-038
J-051 <- J-039, J-040, J-035
J-052 <- J-039, J-040, J-035
J-053 <- J-042, J-029
J-054 <- J-042, J-029
J-055 <- J-005, J-033, J-034, J-039
```

### What to do when an upstream judgment is falsified

1. Change the upstream card to **FALSIFIED**, recording the trigger date, evidence, and observation scope while preserving the original card.
2. Search every card's `depends-on` field for direct downstream IDs, then repeat layer by layer to enumerate the complete affected set.
3. Mark every affected card `REVIEW_REQUIRED` (or, where the formal status vocabulary has only three values, record that review state in the review log); do not continue treating it as a live basis.
4. Recheck each affected card's reasoning chain, time window, falsifier, and leading indicator. Distinguish “still holds,” “needs a new numbered revision,” and “also falsified.”
5. Update the Chinese and English ledgers, narrative references, and opportunity sources in the same commit. The commit message must name the upstream ID, trigger evidence, and affected IDs.
6. Record the result in the review log. Never delete the old card: the propagation path must remain reconstructable.

---

## 4. Confidence-change history

Confidence is a reviewable stake size, not a rhetorical adverb. Append every change; do not overwrite the old value.

**Record format:**

```text
[YYYY-MM-DD] J-NNN: old confidence → new confidence
Triggering evidence: observable data, event, or reasoning change (with link or file anchor)
Impact: changed intermediate steps, falsifier, or dependency interpretation
Rationale: why this changes the stake size rather than only the wording
Author: <name or role>
```

**Format example (not a formal change):**

```text
[2027-03-01] EXAMPLE-J-000: medium → low
Triggering evidence: cost did not fall during the observation window and a repeatable substitute appeared (example/link)
Impact: the example may no longer enter the opportunity list
Rationale: the cost-decline premise of the reasoning chain weakened
Author: example
```

Change-history table:

| Date | Judgment ID | Old confidence | New confidence | Evidence and rationale | Commit |
|---|---|---|---|---|---|
| — | — | — | — | No formal changes yet | — |

---

## 5. Expiry-review procedure

The end of a time window is not an automatic HIT; it is a mandatory review event. Handle each expired card in this order:

1. Filter the overview for ACTIVE judgments whose window has ended. Read the full card and every upstream `depends-on` judgment first.
2. Check the card's **falsifier** literally: did the specified observable trigger occur? If so, record **FALSIFIED**, with date, evidence, and observation scope.
3. If the falsifier did not trigger, check the **leading indicator**: did it move in the expected direction, at the stated frequency, and without missing or substituted data? Supporting indicators without the full outcome remain ACTIVE; do not pre-label HIT.
4. Record **HIT** only when evidence within the window clearly supports the judgment and no falsifier triggered. State the supporting evidence and uncovered counterexamples.
5. If evidence is insufficient, leave the card ACTIVE, record `ACTIVE / insufficient evidence`, set the next review date, and name the missing indicator.
6. Check all downstream dependencies: an upstream HIT, FALSIFIED, or revision can require downstream review. Follow the propagation steps in Section 3.
7. Update both ledgers in one commit. Add the date, per-card result, evidence anchors, and next action to the review log. The commit message must name the judgment ID and new evidence, never a generic “update docs.”

Review-log format:

| Date | Judgment ID | Falsifier check | Leading-indicator check | Result (HIT / FALSIFIED / ACTIVE) | Evidence | Next action |
|---|---|---|---|---|---|---|
| 2026-09-18 | J-001 and other initial judgments | Not due | Registered; no review point yet | ACTIVE | Initial registration | Review at each card's window/checkpoint |

---

## 6. Explicit gaps: dimensions not yet covered

The full-landscape promise remains open. The first chain is not full coverage. Each gap below must remain visible until it receives an independent reasoning chain, bilingual document, and judgment cards.

| Gap dimension | Question to answer | Priority | Status |
|---|---|---|---|
| Social consequences of the technology sequence | The technology chain exists; its full consequences for society and organizations still need a dedicated reasoning chain. | High | Partially covered (technology chain is covered by J-006–J-016; social consequences remain open) |
| Energy and physical infrastructure | How do hard constraints in compute, data centers, grids, chips, and materials migrate? | High | Not covered |
| Biology and medicine | After generation enters experiments, diagnosis, and care, which steps remain constrained by bodies and trials? | High | Not covered |
| Education and skill formation | When “knowing how” becomes cheap, where do learning, screening, and qualification become scarce? | High | Not covered |
| Geopolitics and institutions | How do compute, data, and critical infrastructure change bargaining power among states and organizations? | Medium | Not covered |
| Law and property | How do liability, data ownership, model output, and licensing rewrite transaction boundaries? | High | Partially covered (C2 and J-055 cover only high-liability real-world signals; the institutional landscape remains open) |
| Organizations and employment | How do coordination costs, employment relationships, and firm boundaries change? | High | Covered (J-037–J-038; expansion remains) |
| Collaboration between people | How does AI mediation change division of labor, trust, negotiation, and joint decisions? | High | Not covered |
| Relationships between people and AI | What norms grow from asymmetries in memory, patience, copyability, and exclusivity? | High | Not covered |
| Attention and trust | When content is unlimited and signals are easy to forge, how are attention and credible credentials allocated? | High | Covered (J-035–J-036; expansion remains) |
| Capital and power | What new bottlenecks form around compute ownership, financing, and distribution of returns? | Medium | Covered (J-039–J-040; expansion remains) |
| Human needs, meaning, and embodied presence | Which needs remain stable under supply change, and which preferences actually drift? | Medium | Covered (J-041–J-042; expansion remains) |

Gaps may be filled or explicitly downgraded later, but never silently removed.

---

## 7. Formal judgment and opportunity index

| Source judgment | Opportunity or window | Hard constraint | Status |
|---|---|---|---|
| J-003 | Ownership layer for private context | Ownership/privacy | Candidate |
| J-004 | Reversible infrastructure for AI actions | Physical + law/liability (irreversibility is a supporting lens) | Candidate |
| J-005 | Accountable commitment layer | Legal liability | Candidate |
| J-002 | AI output quality assurance / selection | No hard constraint; likely automated | Window |
---

## 8. Review log

| Date | Action | Result |
|---|---|---|
| 2026-09-18 | J-031–J-042 metadata repair review | Restored source, next-review, and status fields in both bilingual cards; e25f0fd passed fresh-context acceptance | e25f0fd |
| 2026-09-18 | Mid-term expansion: added J-031–J-042, completed six-dimension narrative, dependency graph, and review log | Bilingual card fields are equivalent; low-confidence cards remain landscape only; window opportunities are marked in the narrative |
| 2026-09-18 | Narrow correction: restored J-006–J-016 to the overview, aligned the technology-chain gap status, and clarified containers versus card windows | Both ledgers cover J-001–J-030; technology-chain status is equivalent; card-specific windows remain authoritative |

---


## External-comparison sources for this round

This comparison followed the independent reasoning. External material marks agreement, disagreement, or evidence boundaries; it does not rewrite the reasoning chain or validate a forecast window by itself. Each source includes the chapter, abstract, or topic anchor actually used; “supports” is limited to that anchor and does not support the project’s full time window.

- **EXT-1**: Stanford AI Index 2025, **sections: Technical Performance / Inference Cost**; supports capability and unit-inference-cost decline, not the specific 2029 magnitude. <https://hai.stanford.edu/ai-index/2025-ai-index-report>
- **EXT-2**: Anthropic, Building effective agents, **sections: Workflows / When to use agents**; supports constrained workflows and agent boundaries, not industry timing. <https://www.anthropic.com/engineering/building-effective-agents>
- **EXT-3**: METR, AI task completion time horizons, **topic: task-duration/success-rate curves**; supports long-task reliability limits, not this project’s window. <https://metr.org/time-horizons/>
- **EXT-4**: NIST AI RMF Generative AI Profile, **topics: Govern / Measure / Manage**; supports governance, testing, monitoring, and human oversight, not long-term interface order. <https://www.nist.gov/itl/ai-risk-management-framework>
- **EXT-5**: Video-generation spatiotemporal-consistency review, **abstract/sections: spatiotemporal consistency and long-video evaluation**; supports long-range coherence difficulty, not cross-media ordering. <https://arxiv.org/html/2502.17863v2>
- **EXT-6**: OpenAI Structured Outputs / Function Calling, **sections: JSON Schema / tool calls**; supports productized structured tool calls, not ordering before open-world action. <https://developers.openai.com/api/docs/guides/structured-outputs>
- **EXT-7**: FDA Real-World Evidence, **sections: RWE definition and high-liability use**; supports the importance of real-world evidence in high-liability settings, not universal price premiums. <https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence>
- **EXT-8**: LongRAG and MemoRAG, **abstract/method sections: retrieval and memory for long-context tasks**; supports retrieval-memory mechanisms, not fixed industry order. <https://arxiv.org/abs/2406.15319>; <https://arxiv.org/abs/2409.05591>
- **EXT-9**: WHO, Ethics and governance of AI for health, **topics: human oversight / accountability**; supports real-world governance and human agency, not far-term relationship substitution. <https://www.who.int/publications/i/item/9789240029200>
- **EXT-10**: EU AI Act, **Article 14: Human oversight**, plus high-risk logging, accuracy, and resilience provisions; supports current oversight and permission requirements, not a 2033–2040 shift to boundary grants. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng>
- **EXT-11**: C2PA Content Credentials, **topics: signed provenance / edit history**; supports provenance mechanisms, not inevitable scarcity of field observation. <https://c2pa.org/>
- **EXT-12**: IEA Energy and AI, **sections: data-centre electricity demand / grid constraints**; supports energy and grid constraints, not the full rent chain. <https://www.iea.org/reports/energy-and-ai>
- **EXT-13**: Federal Reserve SR 11-7, **sections: validation / ongoing monitoring / independent review**; supports model-governance records, not attention-shift forecasts. <https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.pdf>
- **EXT-14**: NAIC AI Model Bulletin, **topics: insurance governance / accountability**; supports insurance and liability governance, not solvency as a far-term infrastructure bottleneck. <https://content.naic.org/sites/default/files/call_materials/Model%20Bulletin%2010.23%20Clean.pdf>
- **EXT-15**: European Commission AI liability rules, **topics: AI harm liability / evidence**; supports liability and evidence issues, not universal formation of “liability collateral.” <https://commission.europa.eu/topics/business-and-industry/contract-rules/digital-contracts/liability-rules-artificial-intelligence_en>
- **EXT-16**: Anthropic Economic Index, **topic: augmentation / automation use distribution**; supports coexistence of augmentation and automation, not causal conclusions about small teams or attention. <https://www.anthropic.com/research/the-anthropic-economic-index>
- **EXT-17**: MIT/OpenAI longitudinal chatbot study, **findings: AI interaction, loneliness, and offline social contact**; supports continuing relationship needs, not AI substitution for shared experience. <https://www.media.mit.edu/publications/how-ai-and-human-behaviors-shape-psychosocial-effects-of-extended-chatbot-use/>
- **EXT-18**: Weak- and strong-tie review, **sections: information opportunities / well-being / reciprocity**; supports relationship-type differences, not AI causal capacity change. <https://link.springer.com/chapter/10.1007/978-981-97-4084-0_4>

### J-043 · High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only).
- **Lens**: L2 constraint migration, L6 irreversibility.
- **Reasoning chain**: Rollback-capable environments lower supervision cost → agents take more steps → supervision shifts to boundaries and escalation → high-value deployment uses boundary grants.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, high-value agents still require step approval and rollback has not lowered supervision cost.
- **Leading indicator**: Boundary-grant share, step approvals, rehearsal procurement; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-031, J-032, J-014.
- **Strongest opposing mechanism**: Liability or regulation requires step approvals.
- **Against consensus**: Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants.
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-044 · Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only).
- **Lens**: L2 constraint migration, L7 institutional lag.
- **Reasoning chain**: Execution scales → tail losses exceed one user’s capacity → collateral and balance sheets become admission conditions → solvent entities support infrastructure.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, solvency does not affect deployment, pricing, or financing.
- **Leading indicator**: Liability premiums, reserves, solvency clauses; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-032, J-040.
- **Strongest opposing mechanism**: Liability is outsourced and losses are too low for a separate asset.
- **Against consensus**: Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished.
- **External comparison source**: EXT-14, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-045 · As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only).
- **Lens**: L1 abundance-to-scarcity, L5 signals and forgery.
- **Reasoning chain**: Replayable supply grows → narrative loses distinctiveness → unarranged field observation becomes scarce → preserving conditions and causality gains value.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, high-liability decision-makers do not distinguish field from synthetic evidence.
- **Leading indicator**: Field-evidence premium, raw-record requirements, synthetic substitution; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-033, J-034.
- **Strongest opposing mechanism**: High-fidelity simulation becomes equivalent to field observation.
- **Against consensus**: Retain but with insufficient evidence: provenance standards support the relative importance of original records, not inevitable scarcity of unarranged observation.
- **External comparison source**: EXT-11 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-046 · High-liability settings retain a premium for field causal records (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: High-liability settings retain a premium for field causal records (landscape only).
- **Lens**: L5 signals and forgery, L6 irreversibility.
- **Reasoning chain**: Cheap explanations → liable parties distinguish advice from intervention → field records connect action, outcome and compensation → high-liability transactions pay.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, replacing field records with synthetic evidence changes neither accidents nor prices.
- **Leading indicator**: Record licensing, insurance discounts, trial requirements; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-033, J-034.
- **Strongest opposing mechanism**: World models and regulators establish synthetic trials as equivalent.
- **Against consensus**: Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven.
- **External comparison source**: EXT-7, EXT-11 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-047 · Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only).
- **Lens**: L1 abundance-to-scarcity, L9 relational asymmetry.
- **Reasoning chain**: Copyable memory, patience and style → companionship scales → copyability reduces exclusivity and shared risk → non-copyable reciprocity is scarce.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, copyable companionship replaces human reciprocity with no behavioral difference.
- **Leading indicator**: Copy rate, exit rate, retention and repair outcomes; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-042.
- **Strongest opposing mechanism**: Institutions accept copyability and preferences change.
- **Against consensus**: Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-048 · Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only).
- **Lens**: L7 institutional lag, L9 relational asymmetry.
- **Reasoning chain**: Copyable, pausable relationships → memory and commitment boundaries diverge → data, exit and liability conflicts grow → institutions define subjects.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, relationship-data and exit disputes do not persist and ordinary contracts suffice.
- **Leading indicator**: Data disputes, exit clauses, dedicated rules or cases; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-042.
- **Strongest opposing mechanism**: AI remains an ordinary tool covered by existing contracts.
- **Against consensus**: Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint.
- **External comparison source**: EXT-9, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-049 · As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only).
- **Lens**: L1 abundance-to-scarcity, L8 human nature and demand.
- **Reasoning chain**: Coordination costs fall → candidates multiply → choosing is not commitment; commitment bears failure → willing groups are scarce.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, more coordination also raises joint bearing of long-term failure and repair is no bottleneck.
- **Leading indicator**: Commitment retention, exit rate, repair time; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-038.
- **Strongest opposing mechanism**: Agent reputation and arbitration bear risk without human commitment.
- **Against consensus**: Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent.
- **External comparison source**: EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-050 · The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only).
- **Lens**: L3 cost structure, L8 human nature and demand.
- **Reasoning chain**: Agents absorb coordination → human intervention shrinks → it concentrates on irreversible choices and joint liability → commitment quality measures collaboration.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, collaboration value remains step execution rather than commitment choice.
- **Leading indicator**: Human-confirmed commitments, irreversible decisions, fulfillment; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-038.
- **Strongest opposing mechanism**: Agents replace responsibility roles, leaving execution speed decisive.
- **Against consensus**: Retain but with insufficient evidence: governance preserves human confirmation at key points, but does not prove a wholesale shift in collaboration value.
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-051 · Abundant advice does not automatically disperse real action rights (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Abundant advice does not automatically disperse real action rights (landscape only).
- **Lens**: L2 constraint migration, L7 institutional lag.
- **Reasoning chain**: Advice is cheap → information grows → permissions, resources and compensation remain concentrated → advice does not disperse action rights.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, advice growth coincides with broad dispersion of energy, data, licensing, and compensation access.
- **Leading indicator**: Resource concentration, authorization holders, advice-to-action distribution; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-039, J-040, J-035.
- **Strongest opposing mechanism**: Open protocols and competition policy disperse access points.
- **Against consensus**: Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven.
- **External comparison source**: EXT-12, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-052 · Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only).
- **Lens**: L1 abundance-to-scarcity, L7 institutional lag.
- **Reasoning chain**: Model supply expands → control migrates to real inputs, permissions and losses → institutions price four access points → control creates bargaining power.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, four access points create no persistent price, licensing, or financing advantage.
- **Leading indicator**: Energy spreads, data fees, review fees, insurance reserves; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-039, J-040, J-035.
- **Strongest opposing mechanism**: All four inputs commoditize and control creates no rent.
- **Against consensus**: Retain but with insufficient evidence: energy, real-world data, authorization, and compensation have present-day entry points; the long-term combination remains an inference.
- **External comparison source**: EXT-12, EXT-14, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-053 · As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only).
- **Lens**: L1 abundance-to-scarcity, L8 human nature and demand.
- **Reasoning chain**: Generatable output loses distinction → real time, bodily risk and responsibility leave cost signals → personal burden becomes meaning/status signal.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, real responsibility no longer affects trust, status, or long-term choices.
- **Leading indicator**: Trust premium for commitments, experience verification, narrative/outcome coupling; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-042, J-029.
- **Strongest opposing mechanism**: Society stops valuing real responsibility.
- **Against consensus**: Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-054 · Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only).
- **Lens**: L6 irreversibility, L8 human nature and demand.
- **Reasoning chain**: Choice grows but lifetime does not → bodily risk and long commitments remain personal → scarcity moves to non-delegable experience.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, agent substitution leaves no observable difference in preferences or outcomes around time and risk.
- **Leading indicator**: Non-delegable time, long-commitment completion, embodied premium; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-042, J-029.
- **Strongest opposing mechanism**: Immersive agent experience becomes equivalent.
- **Against consensus**: Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven.
- **External comparison source**: EXT-9, EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

## 9. Judgment cards for the technology capability sequence

These judgments support the capability order in `05-tech-sequence.md`. Each preserves the five-part test and strongest opposing mechanism; the arrival of a capability is not the same as universal adoption.

### J-001 · Unit reasoning cost keeps falling

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The unit cost of reasoning at equal capability falls another order of magnitude by the end of 2029.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Reasoning is parallelizable deterministic computation → cumulative production and engineering optimization create a learning curve → hardware efficiency, model efficiency, and scheduling/reuse provide relatively independent cost-decline paths → equal capability can be called more frequently.
- **Time window**: 2026-01 to 2029-12.
- **Falsifier**: For 18 consecutive months, the lowest public unit price for equal capability rises rather than falls, and the rise cannot be explained by temporary demand congestion or a one-off energy shock.
- **Leading indicator**: Lowest public price for a fixed benchmark score, energy per unit of compute, and months for open models to catch the strongest closed model at the time; observe twice yearly.
- **Confidence**: High.
- **depends-on**: —.
- **Strongest opposing mechanism**: Energy, chip supply, or regulation creates a common hard ceiling that disables all three decline paths; if the falsifier triggers, withdraw this judgment and its downstream cost premise.
- **Against consensus**: Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude.
- **External comparison source**: EXT-1 (see the source index above).
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-002 · “Selecting objectively high quality from abundant output” is not a durable scarcity, but merely a 2–4 year window

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Selecting objectively high quality from abundant output is not a durable scarcity; it is merely a 2–4 year window.
- **Lens**: L1 (gate)
- **Reasoning chain**: Objective quality is formalizable in most domains → anything formalizable can be checked automatically → generative models can sample and self-evaluate → selection is internalized as part of generation and is no longer an independent need
- **Time window**: The window will be basically closed by the end of 2029
- **Falsifier**: In 2030, a sizable independent market still exists whose core value is “picking the better one from AI output for the user,” and that market has not been internalized by model vendors
- **Leading indicator**: Whether model vendors make “generate multiple options + automatically select the best” the default behavior; whether revenue from third-party “AI output quality assurance” products is expanding or being squeezed
- **Confidence**: Medium
- **Strongest opposing mechanism**: Subjective quality may remain difficult to formalize, or independent quality-control markets may persist because of liability and domain context. If multiple large, non-provider-controlled objective quality markets remain by 2030, withdraw this judgment.
- **External comparison note**: The comparison is recorded as “divergent”; the reason to hold is that executable quality checks diffuse with generators, not that an external forecast says so.
- **depends-on**: J-001
- **Against consensus**: Retain with a different mechanism: objective selection may be partly internalized, while liability- and domain-sensitive QA may persist.
- **External comparison source**: EXT-2, EXT-4 (see the source index above).
- **Status**: ACTIVE
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-03-31.

### J-003 · The genuinely durable scarcity is ownership of “private context about you” and its usable form

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The genuinely durable scarcity is ownership of private context about you and its usable form.
- **Lens**: L2 (the bottleneck jumps from production capacity to choice) + L1 (gate)
- **Reasoning chain**: Objective quality can be automated, subjective fit cannot → the key input to subjective fit is an individual’s/organization’s history of choices → that input is private, unstructured, and impossible for the person to articulate → hard constraints (ownership + privacy) prevent the same force from acquiring it automatically
- **Time window**: Demand becomes visible from 2027 and will not disappear before 2033
- **Falsifier**: A method appears that can stably reproduce an individual’s/organization’s choice preferences using only a small amount of publicly available interaction (reaching over 80% approval by the person), making private history unnecessary
- **Leading indicator**: ① Whether companies begin building dedicated assets for “our context / sensibility / boundaries” rather than leaving them scattered in prompts; ② whether individuals begin exporting and carrying their own preference profiles; ③ whether rejection reasons such as “this doesn’t feel like us” begin to be explicitly recorded
- **Confidence**: Medium
- **Strongest opposing mechanism**: Preferences may be reconstructible from very few interactions. If a reproducible public method reaches more than 80% individual acceptance without private history, withdraw this judgment.
- **External comparison note**: The comparison is “partly divergent”; the reason to hold is that model access to context is not the same as user ownership and bargaining power over context.
- **depends-on**: J-001, J-002
- **Against consensus**: Retain with a narrower evidence boundary: sources support governance of private context, not that it must become durable scarcity.
- **External comparison source**: EXT-4 (see the source index above).
- **Status**: ACTIVE
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-004 · As AI shifts from “generating content” to “executing actions,” the scarce item is infrastructure that “makes actions reversible”

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As AI shifts from generating content to executing actions, the scarce item is infrastructure that makes actions reversible.
- **Lens**: L6 (irreversibility) + L1 (gate).
- **Reasoning chain**: Generation becomes cheap → trial-and-error strategies spread → but trial and error presupposes reversible outcomes → AI begins touching irreversible actions (payments, deployment, sending, signing) → irreversibility exposes physical and legal/liability constraints that will not disappear as models improve → “reversibilization” becomes a prerequisite for using AI rather than an option
- **Time window**: Demand becomes explicit from 2027 and becomes standard before 2032
- **Falsifier**: By 2031, mainstream practice still lets AI directly execute irreversible actions in production environments/real accounts, and the incident rate is low enough that no one demands an isolation layer
- **Leading indicator**: ① Whether enterprise procurement lists begin to include standalone items such as “AI action sandboxes / shadow environments / rollback”; ② whether insurers begin pricing “AI autonomous action”; ③ the public frequency of major AI execution incidents
- **Confidence**: Medium
- **Strongest opposing mechanism**: Human approval of each item may replace sandboxes and rollback cheaply. If high-value deployments still rely on item-by-item approval by 2030 and show no separate environment procurement, withdraw the independent-infrastructure judgment.
- **External comparison note**: The comparison is “partly consistent”; the reason to hold the category judgment is that irreversibility, liability, and expected accident loss can turn isolation from a habit into a procurement condition.
- **depends-on**: J-001
- **Against consensus**: Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified.
- **External comparison source**: EXT-2, EXT-4 (see the source index above).
- **Status**: ACTIVE
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-005 · After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality.
- **Lens**: L1 (abundance → scarcity) + L2 (constraint migration).
- **Reasoning chain**: Generation = recombination of existing patterns → what cannot be obtained through recombination will not become abundant → supply-and-demand law: what complements abundant goods without becoming abundant in parallel appreciates → the three kinds of input are respectively protected by the hard constraints of physical presence, legal liability, and experimental intervention
- **Time window**: Clearly visible in pricing during 2029–2033
- **Falsifier**: Reliable synthetic data/simulation-based reasoning systematically replaces real experiments in fields requiring new observations (such as new drugs and new materials), and regulators accept it
- **Leading indicator**: ① Price trends for licensing first-party data (sensors, field sites, proprietary workflows); ② whether AI services with compensation commitments appear and command a premium; ③ the share of experiments and pilot production in R&D budgets
- **Confidence**: Medium
- **Strongest opposing mechanism**: High-fidelity simulation, synthetic data, or statutory liability allocation may systematically replace real observation, market commitments, or experimental intervention. If regulators accept those substitutes and pricing no longer rewards real inputs, withdraw this judgment.
- **External comparison note**: The comparison is “partly consistent”; the claim is not the slogan “data is oil,” but that physical observation, legal liability, and causal intervention have different hard constraints.
- **depends-on**: J-001
- **Against consensus**: Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate.
- **External comparison source**: EXT-7 (see the source index above).
- **Status**: ACTIVE
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-017 · AI mediation expands weak-tie coordination faster than strong relationships

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2033, AI mediation will expand weak-tie coordination faster than strong relationships, without expanding the number of relationships in which a person can remain present over time.
- **Lens**: L8 human needs and demand + L9 relational asymmetry + L2 constraint migration.
- **Reasoning chain**: J-006 lowers the cost of multi-party coordination and information compression → J-007 makes shared context and history easier to resume → contact, translation, introductions, and scheduling for weak ties can scale → strong ties remain constrained by shared experience, mutual responsibility, conflict repair, and finite attention → more connections do not automatically become more commitments that people can rely on.
- **Time window**: 2027–2033.
- **Falsifier**: By 2033, longitudinal evidence after widespread AI mediation shows that the number of strong relationships a person can sustain and the number of relationships in which they can bear shared consequences both rise materially, without a new attention or presence bottleneck.
- **Leading indicator**: Share of work, education, and transactions coordinated through AI mediation; human time per coordination; close-network size and relationship-repair frequency; measured annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007.
- **Strongest opposing mechanism**: AI may become a genuinely reciprocal relationship participant accepted by institutions and people, or materially increase the effective attention available for strong ties. If longitudinal evidence shows strong-tie capacity rising steadily with AI mediation, withdraw this judgment.
- **Against consensus**: Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect.
- **External comparison source**: EXT-17, EXT-18 (see the source index above).
- **Who should change what behavior**: People and organizations should delegate context synchronization to AI, but preserve shared-consequence decisions, conflict repair, and important rituals as human presence.
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-006 · Reasoning throughput precedes long-horizon autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, the number of parallel reasoning paths affordable per task will rise substantially, making generate–compare–revise workflows common before long-horizon autonomous execution.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: J-001 lowers unit cost → the same budget runs more candidate paths → a scheduler parallelizes simple steps and upgrades difficult ones → workflows shift from one answer to candidate search.
- **Time window**: 2026–2028.
- **Falsifier**: By the end of 2028, mainstream systems still support only one path per comparable task, and cost declines have not translated into parallel attempts.
- **Leading indicator**: Per-task sample count, end-to-end latency, and quality curves for public systems; observe twice yearly.
- **Confidence**: High.
- **depends-on**: J-001.
- **Strongest opposing mechanism**: Energy, bandwidth, or provider queues trap lower costs inside single calls; withdraw this judgment if per-task parallelism does not rise for two years.
- **Against consensus**: Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable.
- **External comparison source**: EXT-1, EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-007 · Resumable context precedes reliable long-term memory

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, task-level retrieval context will become a common base for multi-session collaboration before sourced, revisable long-term memory matures.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: More parallel attempts create more state → one context window cannot hold the full history → tasks, evidence, and open questions must be retrieved → retrieval first solves “bring it back,” while provenance and versions solve “can it be trusted.”
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, mainstream long tasks still rely mainly on unstructured chat replay, and retrieval context produces no measurable continuation gain.
- **Leading indicator**: Long-task recovery rate, retrieval hit rate, and the share of citations from outside the active context window; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006.
- **Strongest opposing mechanism**: Longer windows and stronger models may simply overpower retrieval and memory engineering; downgrade this judgment if long-window systems consistently outperform structured memory on long tasks.
- **Against consensus**: Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order.
- **External comparison source**: EXT-8 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-008 · Sourced long-term memory becomes a prerequisite for reliable collaboration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2031, long-term memory with sources, dates, and confidence boundaries will become necessary for high-value continuous collaboration rather than a chat-product extra.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Resumable context makes history retrievable → history contains stale and conflicting facts → events need sources, update times, and retraction relations → only revisable memory can support longer autonomous tasks.
- **Time window**: 2028–2031.
- **Falsifier**: By 2031, high-value continuous tasks using memory without provenance, versioning, or retraction maintain the same error rate and accountability as sourced memory.
- **Leading indicator**: Enterprise requirements for memory provenance, timestamps, and retraction APIs; the share of incidents caused by bad memory; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-007.
- **Strongest opposing mechanism**: Specialized systems may hide memory defects behind implicit state and human review; withdraw this judgment if long-task adoption grows stably without traceability.
- **Against consensus**: Retain with a different mechanism: provenance, versioning, and revisability improve auditability, but are not proven necessary for every high-value collaboration.
- **External comparison source**: EXT-4, EXT-8 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-009 · Continuous execution in constrained workflows matures first

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, constrained workflows with checkable inputs and outputs and limited permissions will achieve stable continuous execution before open-world autonomy matures.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Sourced memory reduces repeated errors → closed environments provide a limited state space → permissions and exits can be specified in advance → systems can complete multiple actions and stop at a known failure.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, open-world tasks have reliability indistinguishable from constrained workflows, and permission boundaries and stop conditions no longer affect deployment.
- **Leading indicator**: Consecutive steps completed without intervention, constrained-environment success rate, and safe-stop rate after permission denial; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-008.
- **Strongest opposing mechanism**: A sudden jump in general world modeling could erase the closed/open gap; withdraw this judgment if open tasks catch constrained tasks under the same evaluation standard.
- **Against consensus**: Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain.
- **External comparison source**: EXT-2, EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-010 · Long-horizon autonomy follows constrained continuous execution

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2033, autonomous execution across longer horizons with fewer human confirmations will reach acceptable reliability in some high-value settings.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Constrained workflows accumulate state and failure data → long tasks expose more unanticipated states → the system must pause and request evidence under uncertainty → reliable long-horizon execution depends on environment observation and evaluation loops, not simply longer plans.
- **Time window**: 2029–2033.
- **Falsifier**: By 2033, long-horizon tasks still require step-by-step human confirmation, or their incident rate has not materially fallen from 2029.
- **Leading indicator**: Average action span per authorization, proactive pause rate, human takeover rate, and irreversible incident rate; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Vendors may split long tasks into many hidden short tasks; rewrite this judgment if incident rates fall without expanding environmental observation.
- **Against consensus**: Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited.
- **External comparison source**: EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-011 · Cross-media consistency precedes long-range coherence

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, local consistency of entities and formats across text, images, and audio will become reusable before causal coherence across long time spans.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: More reasoning throughput → multiple media versions can be sampled for one task → shared representations and constraint checks solve local consistency first → long-range coherence still needs persistent state and repeated evaluation.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, causal, spatial, and action coherence in long interactive worlds is broadly stable while local cross-media consistency is not a default capability.
- **Leading indicator**: Cross-media entity retention, shot or timbre continuity, and long-horizon state drift; observe quarterly.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007.
- **Strongest opposing mechanism**: A unified world model may solve cross-media and cross-time consistency together; withdraw this judgment if independent tests show simultaneous jumps.
- **Against consensus**: Retain but with insufficient evidence: research supports long-range coherence difficulty, not that cross-media consistency must arrive first.
- **External comparison source**: EXT-5 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-012 · Cross-time coherence depends on state and evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2034, cross-time coherence in long stories, persistent interactive environments, and multi-round design will reach production quality only after state memory and repeated evaluation mature.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Local cross-media consistency reduces frame-level errors → long tasks still accumulate drift in entities, space, and causality → sourced memory preserves state → automatic counterexamples and replay evaluation permit ongoing correction.
- **Time window**: 2029–2034.
- **Falsifier**: By 2034, production-grade long-generation neither depends on state tracking and replay evaluation nor has drift comparable to short segments.
- **Leading indicator**: Long-generation state drift, replay reproducibility, and local-retention rate after cross-round edits; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-008, J-011.
- **Strongest opposing mechanism**: A new generation architecture may learn stable world state directly without explicit memory and evaluation; withdraw this judgment if independent tests show long coherence without those components.
- **Against consensus**: Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation.
- **External comparison source**: EXT-5 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-013 · Checkable tool calls precede open-environment action

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, tool calls with parameters, preconditions, permissions, and structured results will spread before systems expand into continuous action in complex environments.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Constrained continuous execution needs explicit boundaries → natural-language tool calls are hard to check → typed interfaces structure actions and results → structured calls first accumulate reliability on a few tools and then expand the tool surface.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, high-value tools broadly accept unstructured natural-language calls, with no error-rate difference from checkable interfaces.
- **Leading indicator**: Tool-schema coverage, precondition rejection rate, parameter error rate, and replayable-result ratio; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Models may self-correct through natural language and quickly absorb the value of structure; downgrade this judgment if schema-free tools consistently catch up in real tasks.
- **Against consensus**: Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment.
- **External comparison source**: EXT-6 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-014 · Rehearsable environments follow single-tool integration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2032, environments combining snapshots, shadow execution, permission boundaries, and rollback points will arrive after single-tool integration but before high-value autonomous action becomes common.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Typed tools express one action → multiple actions share external state → real state cannot be freely trialed → isolation, snapshots, shadow execution, and rollback expand the safe attempt space.
- **Time window**: 2028–2032.
- **Falsifier**: By 2032, high-value autonomous action still writes directly to real environments, and isolation and rollback have not reduced incident cost or procurement barriers.
- **Leading indicator**: Shadow-environment and rollback line items in AI-workflow procurement; recoverable-action ratio; autonomous-action insurance or liability pricing; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-009, J-013.
- **Strongest opposing mechanism**: Human approval may replace environment isolation at very low cost; if manual confirmation remains dominant and incident rates stay low, this should not be an independent capability layer.
- **Against consensus**: Retain only as an evidence-limited landscape: governance supports rehearsable, recoverable environments, not a market order or window.
- **External comparison source**: EXT-4 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-015 · Formal verification precedes open-world evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, tests, schemas, static checks, and counterexample search will be absorbed by generation systems before independent evaluation of real-world outcomes matures.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Parallel generation increases candidate count → formal properties can be judged quickly by programs → generate–test–discard loops lower output error → open-world outcomes still require waiting for observation and intervention and cannot be replaced immediately by self-evaluation.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, open-world outcome evaluation is broadly reliable while formal testing has not entered the default generation loop.
- **Leading indicator**: Default-on automated-test ratio, counterexample-search coverage, schema-violation rate, and formal-verification impact on final adoption; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006, J-009.
- **Strongest opposing mechanism**: General models may leap directly across formal and open-world evaluation; withdraw this judgment if independent external outcomes remain highly aligned with model self-evaluation across multiple domains.
- **Against consensus**: Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration.
- **External comparison source**: EXT-2, EXT-4 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-016 · Open-world evaluation is the final gate for expanding autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2035, independent observation, causal intervention, and continuous monitoring will become the final technical gate for widening the authorization of long-horizon autonomous action.
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Formal verification covers only pre-specified properties → long tasks encounter unmodeled states and delayed side effects → external observation and intervention create independent evidence → continuous monitoring turns one-off tests into runtime feedback → authorization boundaries can expand incrementally.
- **Time window**: 2029–2035.
- **Falsifier**: By 2035, long-horizon autonomous systems reach open environments without independent observation, intervention, or continuous monitoring and still match constrained-environment incident rates.
- **Leading indicator**: Share of external evidence in long tasks, causal-experiment trigger rate, runtime pause and rollback rate, and authorization expansion following evaluation results; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-010, J-012, J-014, J-015.
- **Strongest opposing mechanism**: A sufficiently strong world model may compress open environments into a formally simulable space, making independent evaluation unnecessary; withdraw this judgment if simulation forecasts remain at independent-observation quality in real tasks.
- **Against consensus**: Retain only as an evidence-limited landscape: open-world feedback may constrain autonomous authority, but is not established as the final gate.
- **External comparison source**: EXT-3, EXT-4 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

---


### J-018 · Parallel reasoning before long-horizon autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, generate–compare–revise becomes the default workflow before long-horizon autonomy.
- **Lens**: Abundance → scarcity + capability sequence.
- **Reasoning chain**: J-006 raises parallel throughput → candidate search becomes cheap first → reliable long-horizon environmental control still requires J-009 boundaries and evaluation → parallel reasoning spreads first.
- **Time window**: 2026–2028.
- **Falsifier**: By end-2028, high-value workflows mainly rely on low-confirmation long-horizon autonomy rather than candidate search.
- **Leading indicator**: Samples per task, automatic comparison share, and action span without human takeover; semiannual.
- **Confidence**: High.
- **depends-on**: J-006, J-009.
- **Strongest opposing mechanism**: A sudden reliability jump makes long-horizon execution and candidate search spread together; withdraw if long tasks match candidate-search validation standards.
- **Against consensus**: Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference.
- **External comparison source**: EXT-1 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-019 · Token saving is a window

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2028, stronger models and cheaper repeated attempts compress the value of saving tokens; it is a window, not durable scarcity.
- **Lens**: Abundance → scarcity + L7 rent windows.
- **Reasoning chain**: J-001 lowers unit cost → J-006 enables sampling → dud token cost falls → the independent premium for token saving shrinks.
- **Time window**: 2026–2028.
- **Falsifier**: By 2028, buyers still pay a structural premium for fewer model calls, without supply constraints explaining it.
- **Leading indicator**: Calls per task, call price, and retention premium for token-optimization services; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-001, J-006.
- **Strongest opposing mechanism**: Energy and service quotas remain scarce, keeping per-call opportunity cost high; withdraw if optimization premiums keep expanding.
- **Against consensus**: Retain with a different mechanism: cost decline can come from inference efficiency and hardware scheduling; public prices do not prove optimization premiums vanish.
- **External comparison source**: EXT-1, EXT-12 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-020 · Reproducible content keeps falling in price

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, reproducible content keeps falling in marginal price as objective selection becomes part of generation.
- **Lens**: Abundance → scarcity + capability sequence.
- **Reasoning chain**: J-002 formalizable quality is tested automatically → J-015 expands the generate–verify loop → homogeneous supply increases → mere content delivery loses price.
- **Time window**: 2026–2028.
- **Falsifier**: By 2028, generic reproducible content retains broad scarcity premiums without copyright or compute constraints.
- **Leading indicator**: Generation cost, delivery price, and automatic-selection coverage; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-002, J-015.
- **Strongest opposing mechanism**: Copyright, distribution, or real-data licensing constrains supply; downgrade if price stays detached from supply.
- **Against consensus**: Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers.
- **External comparison source**: EXT-1, EXT-4, EXT-11 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-021 · First-hand field signals earn a premium first

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, unrecorded field observations and traceable sources earn a premium earlier than second-hand expression.
- **Lens**: Abundance → scarcity + L5 signal forgery.
- **Reasoning chain**: J-005’s raw signals cannot be recombined → J-015 makes second-hand expression easier to screen → buyers shift premiums to field reality, sources, and accountability.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, buyers pay no differential for verifiable field reality over high-fidelity recombination.
- **Leading indicator**: Premium for sourced material and field-data contracts; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-005, J-015.
- **Strongest opposing mechanism**: High-fidelity simulation gains institutional and market acceptance as a field substitute; withdraw if substitution is stable across domains.
- **Against consensus**: Retain with a different mechanism: traceable first-hand sources may gain value first; broad field-premium pricing is unproven.
- **External comparison source**: EXT-4, EXT-11 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-022 · Forgable signals drive credential upgrades

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, more forgable personalized signals push important decisions toward costlier identity, fulfillment, and liability credentials.
- **Lens**: Abundance → scarcity + L5 signal forgery.
- **Reasoning chain**: J-005 raises accountable entities → J-017 cheapens weak-tie coordination → surface interaction is harder to distinguish → high-value decisions raise credential thresholds.
- **Time window**: 2026–2029.
- **Falsifier**: Acceptance of low-cost generated identity signals rises in high-value transactions without added liability or verification.
- **Leading indicator**: Multifactor credential adoption, guarantees, and liability clauses; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-005, J-017.
- **Strongest opposing mechanism**: Platforms provide trusted identity and compensation cheaply; revisit if internal verification lowers thresholds.
- **Against consensus**: Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown.
- **External comparison source**: EXT-4, EXT-11 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-023 · Attention shifts toward fulfilled commitments

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2030, important attention allocation shifts from expression quality toward relationship continuity and fulfilled commitments.
- **Lens**: Abundance → scarcity + L8 human constants.
- **Reasoning chain**: J-017 expands coordination supply → J-022 makes surface signals easier to forge → one-off expression loses distinction → repeated fulfillment records gain weight.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, important choices are still predicted mainly by one-off generated expression rather than fulfillment records.
- **Leading indicator**: Use of fulfillment, repeat relationships, and breach records; annual.
- **Confidence**: Medium.
- **depends-on**: J-017, J-022, J-013.
- **Strongest opposing mechanism**: One-time platform credentials predict fulfillment as well as repeated records; downgrade if they consistently outperform history.
- **Against consensus**: Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift.
- **External comparison source**: EXT-16 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-024 · Credentials re-layer (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, credentials may re-layer around fulfillment, liability, and presence, but the institutional form is uncertain.
- **Lens**: Abundance → scarcity + L5 signal forgery.
- **Reasoning chain**: J-022 raises verification cost → J-023 raises the value of long records → risk contexts adopt different credential layers, subject to platform and legal choices.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, high-risk transactions still rely on one low-cost identity signal without contextual layers.
- **Leading indicator**: Guarantees, audits, and presence proofs in high-risk services; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-022, J-013.
- **Strongest opposing mechanism**: One universal platform identity covers all risk contexts; withdraw if this persists.
- **Against consensus**: Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only.
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-025 · Small-team output rises

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2030, small teams complete more verifiable output with fewer steps.
- **Lens**: Abundance → scarcity + organizational boundaries.
- **Reasoning chain**: J-009 constrained continuity → J-013 inspectable tools → repeated knowledge steps become agent-mediated → verifiable output rises at constant headcount.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, comparable teams using constrained agents do not produce more verifiable output.
- **Leading indicator**: Auditable tasks per employee, takeover rate, and output per unit; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-009, J-013.
- **Strongest opposing mechanism**: Coordination, verification, and incident handling erase automation gains; downgrade if total output stays flat while oversight rises.
- **Against consensus**: Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient.
- **External comparison source**: EXT-16 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-026 · Responsibility boundaries remain

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, responsibility boundaries do not disappear at the same rate as knowledge-work steps.
- **Lens**: Abundance → scarcity + L3 organizational form.
- **Reasoning chain**: J-009 expands executable steps → J-013 makes permissions programmable → accidents still need a legal entity → authorization, review, and escalation remain scarce.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, high-value AI actions routinely have no identifiable person or organization bearing consequences.
- **Leading indicator**: Liability clauses, escalation roles, and insurance claims; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-009, J-013.
- **Strongest opposing mechanism**: Law transfers all responsibility to platforms; rewrite if platforms bear all high-value consequences.
- **Against consensus**: Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts.
- **External comparison source**: EXT-10 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-027 · Rented compute spreads capability

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, rented compute spreads access to AI capability for small organizations without distributing gains evenly.
- **Lens**: Abundance → scarcity + L7 rent windows.
- **Reasoning chain**: J-001 lowers call cost → J-006 raises affordable attempts → renting lowers fixed-capital barriers → data, access, and liability capacity still differentiate gains.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, small organizations cannot obtain comparable general reasoning by renting, or diffusion eliminates gain differences.
- **Leading indicator**: Small-organization call share, fixed compute capex, and rental price; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-001, J-006.
- **Strongest opposing mechanism**: Energy, quotas, or platform concentration keeps rented compute for large organizations; downgrade if small-organization access does not rise.
- **Against consensus**: Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity.
- **External comparison source**: EXT-1, EXT-12 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: ACTIVE.

### J-028 · Access becomes a bargaining node (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, proprietary data, distribution, and liability capacity may become more important bargaining nodes than models.
- **Lens**: Abundance → scarcity + L7 rent windows.
- **Reasoning chain**: J-027 expands model access → J-005 raises the value of real inputs and responsibility → models become more reproducible → control of inputs, exits, and losses may earn rent.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, access controllers have no persistent premium over non-controllers absent regulatory constraints.
- **Leading indicator**: Data licenses, distribution take rates, AI liability insurance, and channel exclusivity; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-005, J-013.
- **Strongest opposing mechanism**: Models, energy, and distribution commoditize and access rents disappear; withdraw if rent keeps falling.
- **Against consensus**: Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven.
- **External comparison source**: EXT-4, EXT-12 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-029 · Demand-side anchors persist

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2030, status, certainty, embodied presence, and responsibility remain demand-side anchors despite richer expression and choice.
- **Lens**: L8 human constants + abundance → scarcity.
- **Reasoning chain**: J-017 expands coordination → J-011 expands trial identities and expression → more options do not create shared consequences → demand remains organized around status, certainty, presence, and responsibility.
- **Time window**: 2026–2030.
- **Falsifier**: By 2030, these needs no longer predict important choices across groups, independent of measurement or institutional change.
- **Leading indicator**: Preferences for presence and responsibility in high-value consumption, relationship, and commitment decisions; annual.
- **Confidence**: Medium.
- **depends-on**: J-017, J-011.
- **Strongest opposing mechanism**: A stable, broad generational preference shift; downgrade if longitudinal data shows persistent drift.
- **Against consensus**: Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven.
- **External comparison source**: EXT-17, EXT-18 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-030 · AI mediates coordination, not shared experience (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, AI mediates context synchronization and relationship coordination but not experiences requiring embodied presence and shared consequences.
- **Lens**: L8 human constants + embodied-presence constraint.
- **Reasoning chain**: J-017 cheapens weak-tie coordination → J-011 enriches multimodal expression → shared experience still requires bodies, time, and reciprocal consequences → coordination agents do not expand strong-relationship capacity automatically.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, agent-mediated interaction reliably replaces shared experience in long relationships with no behavioral or reported difference.
- **Leading indicator**: Agent messages versus shared activities, conflict-repair results, and retention; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-017, J-011.
- **Strongest opposing mechanism**: People treat persistent AI interaction as sufficiently real reciprocity; rewrite if it reliably substitutes for shared experience.
- **Against consensus**: Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.



### J-031 · Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Lens**: L2 (constraint migration) + technology sequence
- **Reasoning chain**: Organizations delegate long-horizon tasks → failure states and liability accumulate → observable, pausable, rollback-capable environments reduce irreversible loss → high-value deployments make the environment an admission condition
- **Dependency impact**: If J-010 is falsified, the reliability premise for long-horizon tasks disappears; this card remains only for constrained workflows
- **Time window**: 2026–2032
- **Falsifier**: By 2032, high-value agent execution still commonly connects directly to production systems without incident costs driving separate isolation procurement
- **Leading indicator**: Sandbox, shadow-environment, and rollback items in procurement; agent incidents; semiannual
- **Confidence**: Medium
- **depends-on**: J-010
- **Strongest opposing mechanism**: If J-010 is falsified, the reliability premise for long-horizon tasks disappears; this card remains only for constrained workflows
- **Against consensus**: Retain with a different mechanism: logging, oversight, and risk control have institutional support; a complete rollback gate and its window are unverified.
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-032 · Authorization review and exception escalation become scarcer than execution steps

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization review and exception escalation become scarcer than execution steps
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Inspectable tool calls spread → execution steps become templated → cross-boundary authorization, exception escalation, and final responsibility still require judgment → review roles appreciate relative to execution steps
- **Dependency impact**: If J-013 is falsified, inspectable-permission infrastructure disappears; if authorization is not scarce despite it, this card fails
- **Time window**: 2027–2032
- **Falsifier**: By 2032, authorization-review hours fall at the same rate as execution hours without increased incidents
- **Leading indicator**: Permission-denial rate, human escalation hours, responsibility-role hiring; quarterly
- **Confidence**: Medium
- **depends-on**: J-013
- **Strongest opposing mechanism**: If J-013 is falsified, inspectable-permission infrastructure disappears; if authorization is not scarce despite it, this card fails
- **Against consensus**: Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing.
- **External comparison source**: EXT-4, EXT-10, EXT-13 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-033 · Verifiable records of real interventions become more valuable than explanation itself

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Verifiable records of real interventions become more valuable than explanation itself
- **Lens**: L1 (abundance-to-scarcity) + L2 (constraint migration)
- **Reasoning chain**: Generated explanations become cheap → explanation supply becomes abundant → real interventions produce non-recombinable outcomes → verifiable records connect causality and responsibility → records earn a premium
- **Dependency impact**: If J-005 is falsified, field signals and accountable commitments lose structural premium; this card weakens
- **Time window**: 2029–2033
- **Falsifier**: By 2033, high-liability markets no longer pay a premium for intervention records with field evidence
- **Leading indicator**: First-hand intervention-license prices, audit requirements, evidence-backed renewal rates; semiannual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, field signals and accountable commitments lose structural premium; this card weakens
- **Against consensus**: Retain with a different mechanism: compliance evidence, model risk controls, and intervention records are gaining value; superiority to explanation is unproven.
- **External comparison source**: EXT-7, EXT-13 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-034 · Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Synthetic material lowers exploration cost → low-liability contexts tolerate model error → high-liability contexts bear bodily, legal, and compensation consequences → regulators retain real trials
- **Dependency impact**: If J-005 is falsified, real trials lose their structural necessity; this card weakens
- **Time window**: 2028–2033
- **Falsifier**: By 2033, high-liability fields broadly replace real trials with synthetic evidence without higher incident rates
- **Leading indicator**: Regulatory acceptance scope, trial budgets, insurance clauses; annual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, real trials lose their structural necessity; this card weakens
- **Against consensus**: Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation.
- **External comparison source**: EXT-7, EXT-9 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-035 · Responsibility collateral enters the transaction structure for consequential AI output

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Responsibility collateral enters the transaction structure for consequential AI output
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Reproducible expression increases → error losses become harder to attribute → buyers ask who bears consequences → insurance, reserves, and audits enter contracts → responsibility collateral becomes a transaction condition
- **Dependency impact**: If J-005 is falsified, compensation and liability capacity are no longer scarce; this card weakens
- **Time window**: 2028–2033
- **Falsifier**: By 2033, high-value AI services still lack liability pricing, compensation clauses, or audit requirements
- **Leading indicator**: AI liability premiums, contractual caps, audit procurement; semiannual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, compensation and liability capacity are no longer scarce; this card weakens
- **Against consensus**: Retain with a different mechanism: liability governance, insurance, and compensation are entering transactions, but universal “liability collateral” is unproven.
- **External comparison source**: EXT-14, EXT-15 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-036 · Long-term fulfillment records allocate attention better than one-off natural expression

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Lens**: L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Expression generation becomes cheap → surface credibility becomes hard to distinguish → repeated fulfillment leaves verifiable records → attention shifts to longitudinal consistency and delivery rate
- **Dependency impact**: If J-017 is falsified, weak-tie coordination did not become cheap and pressure for credential upgrading disappears; this card weakens
- **Time window**: 2027–2032
- **Falsifier**: By 2032, important choices are still driven mainly by one-off expression rather than fulfillment records
- **Leading indicator**: Adoption of performance-history recommendations, repeat and default rates; annual
- **Confidence**: Medium
- **depends-on**: J-017
- **Strongest opposing mechanism**: If J-017 is falsified, weak-tie coordination did not become cheap and pressure for credential upgrading disappears; this card weakens
- **Against consensus**: Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence.
- **External comparison source**: EXT-13, EXT-14 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-037 · Comparable small teams produce more verifiable output

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Comparable small teams produce more verifiable output
- **Lens**: cost structure determines organizational form + technology sequence
- **Reasoning chain**: Constrained workflows stabilize → tool calls become inspectable → a few people orchestrate more agent steps → per-team output and audit records increase
- **Dependency impact**: If J-009 is falsified, the continuous-execution premise disappears; this card weakens
- **Time window**: 2027–2031
- **Falsifier**: By 2031, agent-using small teams show no repeatable output gain over baseline
- **Leading indicator**: Per-person delivery, rework, auditable-output share; quarterly
- **Confidence**: Medium
- **depends-on**: J-009
- **Strongest opposing mechanism**: If J-009 is falsified, the continuous-execution premise disappears; this card weakens
- **Against consensus**: Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams.
- **External comparison source**: EXT-1, EXT-16 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-038 · Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Lens**: L2 (constraint migration) + cost structure determines organizational form
- **Reasoning chain**: Inspectable tool calls spread → permission boundaries clarify → normal steps automate → exceptions and cross-boundary consequences cannot be fully precomputed → responsibility roles remain
- **Dependency impact**: If J-013 is falsified, programmable-permission infrastructure disappears; if responsibility roles still shrink, this card fails
- **Time window**: 2027–2032
- **Falsifier**: By 2032, responsibility-role share falls at the same rate as execution roles without more high-risk incidents
- **Leading indicator**: Exception volume, responsibility-role hiring, post-incident human intervention; quarterly
- **Confidence**: Medium
- **depends-on**: J-013
- **Strongest opposing mechanism**: If J-013 is falsified, programmable-permission infrastructure disappears; if responsibility roles still shrink, this card fails
- **Against consensus**: Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven.
- **External comparison source**: EXT-10, EXT-13 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-039 · Rented models become abundant, while energy, data, and channel control create access rents

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Rented models become abundant, while energy, data, and channel control create access rents
- **Lens**: L1 (abundance-to-scarcity) + L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Unit reasoning cost falls → model capability becomes rentable → model differences narrow → energy access, exclusive data, and channels remain constrained by physics and ownership → controllers earn access rents
- **Dependency impact**: If J-001 is falsified, the model-abundance premise disappears; this card weakens
- **Time window**: 2027–2033
- **Falsifier**: By 2033, controllers of energy, data, and channels have no persistent premium over non-controllers
- **Leading indicator**: Rented-model prices, data-license fees, channel take rates, energy-access spreads; annual
- **Confidence**: Medium
- **depends-on**: J-001
- **Strongest opposing mechanism**: If J-001 is falsified, the model-abundance premise disappears; this card weakens
- **Against consensus**: Retain with a different mechanism: model rental may become abundant, while energy and infrastructure constraints are real; data and channel rents remain unproven.
- **External comparison source**: EXT-1, EXT-12 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-040 · Balance sheets able to absorb AI accidents become a separate scarcity

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Real interventions and commitments appreciate → AI accident losses become measurable → contracts require compensation capacity → capital and insurance price solvency → large balance sheets gain admission advantage
- **Dependency impact**: If J-005 is falsified, liability absorption no longer earns a premium; this card weakens
- **Time window**: 2028–2033
- **Falsifier**: By 2033, compensation capacity does not affect AI contract prices, financing, or deployment eligibility
- **Leading indicator**: Liability premiums, reserves, contract asset requirements; annual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, liability absorption no longer earns a premium; this card weakens
- **Against consensus**: Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven.
- **External comparison source**: EXT-14, EXT-15 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-041 · AI first expands the coordination radius of weak ties

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: AI first expands the coordination radius of weak ties
- **Lens**: L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Communication and context-sync costs fall → translation, introductions, and scheduling scale → weak-tie connection radius expands → strong ties remain constrained by shared consequences
- **Dependency impact**: If J-017 is falsified, the coordination-supply premise disappears; this card weakens
- **Time window**: 2027–2033
- **Falsifier**: By 2033, AI mediation neither increases cross-organization weak-tie connections nor reduces coordination time
- **Leading indicator**: AI-mediated coordination share, cross-organization contacts, human time per coordination; annual
- **Confidence**: Medium
- **depends-on**: J-017
- **Strongest opposing mechanism**: If J-017 is falsified, the coordination-supply premise disappears; this card weakens
- **Against consensus**: Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects.
- **External comparison source**: EXT-16, EXT-18 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-042 · Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Lens**: L2 (constraint migration) + L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Multimodal expression becomes abundant → mediated companionship and reminders spread → shared experience still requires bodies, time, and reciprocal consequences → strong-tie capacity remains presence-constrained
- **Dependency impact**: If J-011 is falsified, the premise of richer multimodal expression weakens; if agents stably replace presence, this card weakens
- **Time window**: 2027–2033
- **Falsifier**: By 2033, agent-mediated interaction reliably replaces shared experience in long relationships with no reported or behavioral difference
- **Leading indicator**: Agent interaction versus shared activity, conflict repair, relationship retention; annual
- **Confidence**: Low
- **depends-on**: J-011
- **Strongest opposing mechanism**: If J-011 is falsified, the premise of richer multimodal expression weakens; if agents stably replace presence, this card weakens
- **Against consensus**: Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects.
- **External comparison source**: EXT-9 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-055 · Real-world signals earn a premium as contract assets in high-liability tasks

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium.
- **Lens**: L1 (abundance → scarcity) + L2 (constraint migration) + L5 (signal forgery) + L6 (irreversibility).
- **Reasoning chain**: C1 makes second-hand expression and synthetic samples abundant → ordinary data files lose marginal price → high-liability tasks still require real observations, provenance, and an accountable party → collection permission, calibration, usage boundaries, and compensation duties enter contracts → data becomes a contract asset with a liability chain.
- **Time window**: 2029–2033.
- **Falsifier**: By 2033, across multiple high-liability fields, regulators, insurers, and buyers broadly accept synthetic evidence with no worse incident rate than real signals, while provenance, calibration, and liability chains carry no observable premium.
- **Leading indicator**: Synthetic-evidence share in high-liability approvals, premium for data contracts with provenance and calibration clauses, real-trial budget share, and data-liability insurance rates; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-005, J-033, J-034, J-039.
- **Strongest opposing mechanism**: A high-fidelity world model and unified platform compensation may absorb real observation and provider liability internally; if platforms absorb all errors and buyers no longer pay separately for provenance and liability, an independent contract-asset layer does not form.
- **Against consensus**: Directionally consistent with stronger data governance, provenance, and trust, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven.
- **External comparison source**: EXT-7, EXT-10, EXT-14 (see the source index above).
- **Source**: [C2: How Real-World Signals Become Contract Assets](chains/20-real-signals-become-contracts.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

## 10. Pre-publication checklist

- [ ] Year boundaries match the single authority in `00-method.md`.
- [ ] Confidence uses only the whitelist: high / medium / low.
- [ ] Every judgment card has ID, proposed date, one-sentence judgment, lens, reasoning chain, time window, falsifier, leading indicator, confidence, depends-on, consensus comparison, source, status, and next review.
- [ ] Every internal link resolves and returns to the source argument.
- [ ] Chinese and English files are updated as equivalent projections in the same commit.
- [ ] Hard constraints use only the five-item whitelist: physical, legal/liability, trust/relationship, ownership/privacy, or embodied presence.
