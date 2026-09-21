# Judgment Ledger

> The single register for all project judgments. Narrative documents cite `J-NNN`; the complete judgment card lives only here.
> This ledger records how judgments are proposed, linked, revised, and reviewed. A falsified judgment is never deleted.

---

## 1. How to use this ledger

### 1.1 Judgment-card fields

A testable judgment must contain every field below. J-001–J-086 are pre-migration cards and may temporarily carry scale only inside Diffusion-gate review while the checker warns; **J-087 and later fail validation without a standalone Audience scale field**. If any other field is missing, label the statement **landscape only**; it cannot serve as a business-opportunity judgment or summary conclusion.

- **ID**: `J-NNN`, three digits, globally unique; shared by Chinese and English; never reuse an old or revised ID.
- **Proposed date**: the date the judgment was first proposed, `YYYY-MM-DD`.
- **One-sentence judgment**: a proposition that can be supported or refuted by facts.
- **Audience scale** (standalone and required from J-087): affected group; hundred-thousand / million / tens-of-millions / hundred-millions / billion-scale; whether it raises existing professionals' ceiling or lets people who could not do it do it now; label a constructed estimate explicitly.
- **Diffusion-gate review**: state the audience magnitude, audience identity, Gate 1 verdict, and whether the judgment raises the ceiling of existing professionals or lets people who previously could not do the activity do it.
- **Lens**: name the supply–demand, human-nature, historical, technological, social, or other calibrated lenses actually used; do not force unused lenses merely for symmetry.
- **Reasoning chain**: each step from first principles and selected lenses; do not replace reasoning with another institution's prediction.
- **Time window**: the interval in which the judgment is expected to occur or remain valid.
- **Falsifier**: one concrete, observable event or data result that would make the author admit the judgment is wrong.
- **Leading indicator**: an observable signal expected to move before the outcome, with its observation frequency or source.
- **Confidence**: high / medium / low. Low-confidence items remain landscape only and do not enter the opportunity list.
- **depends-on**: the prerequisite `J-NNN` judgments. Write `—` when there is no dependency; never use a vague “see above.”
- **Strongest opposing mechanism**: the alternative mechanism or counterexample most capable of invalidating the judgment.
- **Against consensus**: the three comparison elements — where it agrees, where it diverges or what the evidence boundary is, and why the judgment is retained or confidence lowered; write “unknown” explicitly when the round is incomplete.
- **External comparison source**: the `EXT-NN` source identifiers supporting the comparison; state that comparison is incomplete when applicable.
- **Source**: the narrative document or chain where the judgment appears.
- **Next review**: the next date to review the falsifier, leading indicators, and external evidence.
- **Status**: **ACTIVE** (awaiting evidence), **HIT** (supported), **FALSIFIED** (falsifier triggered), or **REVISED** (the old card is retained, but the status note must distinguish two cases): (1) **scope downgrade** — only the audience, applicability, or narrative strength was narrowed, while the original proposition still has a time window, falsifier, and review date; the card remains independently due for review and stays in the calibration denominator. (2) **superseded by a new card** — the status note must name the successor `J-NNN` and state that the old card is no longer reviewed separately; review it with the successor when due, but do not use it as a current judgment or opportunity premise. Never infer calibration exclusion from the `REVISED` label alone.

### 1.2 Completed example card (example only)

> **Example card | EXAMPLE-J-000 (explicitly excluded from the formal numbering)**
> - **ID**: EXAMPLE-J-000
> - **Proposed date**: 2026-09-18
> - **One-sentence judgment**: In a hypothetical market, if the unit cost of repeatedly generating proposals falls by an order of magnitude, the value of a service that merely supplies more proposals will decline within three years.
> - **Audience scale**: affected group = professional buyers; million-scale; raises existing professionals' ceiling; constructed example estimate.
> - **Diffusion-gate review**: The example audience is millions of professional buyers; it raises the ceiling of existing professionals rather than enabling a new activity; Gate 1 fails.
> - **Lens**: Supply–demand and technological regularities.
> - **Reasoning chain**: Supply increases → proposal marginal cost falls → buyers no longer lack proposal quantity → value moves to selection and validation. This demonstrates dependency notation and is not adopted as a project judgment.
> - **Time window**: 2026-09-18 to 2029-09-18.
> - **Falsifier**: By 2029-09-18, buyers still broadly pay a premium for proposal quantity rather than verifiable outcomes, without supply or regulatory constraints explaining it.
> - **Leading indicator**: Unit generation cost and the median amount buyers pay for human selection, recorded every six months.
> - **Confidence**: Medium (example value).
> - **depends-on**: —
> - **Strongest opposing mechanism**: Regulation, liability, or scarce inputs may prevent proposal supply from expanding, preserving a quantity premium.
> - **Against consensus**: Unknown; this example does not perform an external comparison.
> - **External comparison source**: Comparison not completed (example).
> - **Source**: This example section.
> - **Next review**: 2029-09-18 (example value).
> - **Status**: ACTIVE (example value).

Copy the fields, not the example ID. The example does not enter the formal index.

---

## 2. Registered-judgment overview

| ID | Proposed date | One-sentence judgment | Time window | Confidence | depends-on | Source | Against consensus | Status | Next review |
|---|---|---|---|---|---|---|---|---|---|
| [J-001](#j-001--unit-reasoning-cost-keeps-falling) | 2026-09-18 | Unit reasoning cost falls another order of magnitude by the end of 2029 | 2026–2029 | High | — | [C1](chains/10-generation-becomes-free.md) | Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-002](#j-002--selecting-objectively-high-quality-from-abundant-output-is-not-a-durable-scarcity-but-merely-a-24-year-window) | 2026-09-18 | Objective quality selection is a 2–4 year window, not durable scarcity | through 2029 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Retain with a different mechanism: objective selection may be partly internalized, while liability- and domain-sensitive QA may persist. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-003](#j-003--the-genuinely-durable-scarcity-is-ownership-of-private-context-about-you-and-its-usable-form) | 2026-09-18 | Ownership and usable form of private personal or organizational context are more likely to become durable scarcity | 2027–2033 | Medium | J-001, J-002 | [C1](chains/10-generation-becomes-free.md) | Retain with a narrower evidence boundary: sources support governance of private context, not that it must become durable scarcity. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-004](#j-004--as-ai-shifts-from-generating-content-to-executing-actions-the-scarce-item-is-infrastructure-that-makes-actions-reversible) | 2026-09-18 | As AI executes actions, infrastructure that makes actions reversible becomes scarce | 2027–2032 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified. | REVISED (2026-09-19 opportunity-durability review; narrowed and superseded by J-065; the old card is kept) | — |
| [J-005](#j-005--after-generation-becomes-abundant-value-concentrates-in-three-kinds-of-non-recombinable-input-raw-signals-accountable-commitments-and-validated-causality) | 2026-09-18 | Raw signals, accountable commitments, and verified causality become more valuable than reproducible text | 2029–2033 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-006](#j-006--reasoning-throughput-precedes-long-horizon-autonomy) | 2026-09-18 | Reasoning throughput precedes long-horizon autonomy | 2026–2028 | High | J-001 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-007](#j-007--resumable-context-precedes-reliable-long-term-memory) | 2026-09-18 | Resumable context precedes reliable long-term memory | 2026–2029 | High | J-006 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-008](#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration) | 2026-09-18 | Sourced long-term memory becomes a prerequisite for reliable collaboration | 2028–2031 | Medium | J-007 | [Technology Capability Sequence](05-tech-sequence.md) | Retain with a different mechanism: provenance, versioning, and revisability improve auditability, but are not proven necessary for every high-value collaboration. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-009](#j-009--continuous-execution-in-constrained-workflows-matures-first) | 2026-09-18 | Continuous execution in constrained workflows matures first | 2027–2030 | High | J-008 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-010](#j-010--long-horizon-autonomy-follows-constrained-continuous-execution) | 2026-09-18 | Long-horizon autonomy follows constrained continuous execution | 2029–2033 | Medium | J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-011](#j-011--cross-media-consistency-precedes-long-range-coherence) | 2026-09-18 | Cross-media consistency precedes long-range coherence | 2027–2030 | Medium | J-006, J-007 | [Technology Capability Sequence](05-tech-sequence.md) | Retain but with insufficient evidence: research supports long-range coherence difficulty, not that cross-media consistency must arrive first. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-012](#j-012--cross-time-coherence-depends-on-state-and-evaluation) | 2026-09-18 | Cross-time coherence depends on state and evaluation | 2029–2034 | Medium | J-008, J-011 | [Technology Capability Sequence](05-tech-sequence.md) | Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-013](#j-013--checkable-tool-calls-precede-open-environment-action) | 2026-09-18 | Checkable tool calls precede open-environment action | 2027–2030 | High | J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-014](#j-014--rehearsable-environments-follow-single-tool-integration) | 2026-09-18 | Rehearsable environments follow single-tool integration | 2028–2032 | Medium | J-009, J-013 | [Technology Capability Sequence](05-tech-sequence.md) | Retain only as an evidence-limited landscape: governance supports rehearsable, recoverable environments, not a market order or window. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-015](#j-015--formal-verification-precedes-open-world-evaluation) | 2026-09-18 | Formal verification precedes open-world evaluation | 2026–2029 | High | J-006, J-009 | [Technology Capability Sequence](05-tech-sequence.md) | Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-016](#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) | 2026-09-18 | Open-world evaluation is the final gate for expanding autonomy | 2029–2035 | Medium | J-010, J-012, J-014, J-015 | [Technology Capability Sequence](05-tech-sequence.md) | Retain only as an evidence-limited landscape: open-world feedback may constrain autonomous authority, but is not established as the final gate. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-017](#j-017--ai-mediation-expands-weak-tie-coordination-faster-than-strong-relationships) | 2026-09-18 | AI mediation expands weak-tie coordination faster than strong relationships, without expanding the number of relationships in which people can remain present | 2027–2033 | Medium | J-006, J-007 | [C1](chains/10-generation-becomes-free.md) | Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-018](#j-018--parallel-reasoning-before-long-horizon-autonomy) | 2026-09-18 | Parallel reasoning becomes the default workflow before long-horizon autonomy | 2026–2028 | High | J-006, J-009 | [Near-term landscape](10-near.md) | Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-019](#j-019--token-saving-is-a-window) | 2026-09-18 | Saving tokens itself is a window, not durable scarcity | 2026–2028 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Retain with a different mechanism: cost decline can come from inference efficiency and hardware scheduling; public prices do not prove optimization premiums vanish. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-020](#j-020--reproducible-content-keeps-falling-in-price) | 2026-09-18 | Reproducible content keeps falling in marginal price as objective selection is internalized | 2026–2028 | Medium | J-002, J-015 | [Near-term landscape](10-near.md) | Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-021](#j-021--first-hand-field-signals-earn-a-premium-first) | 2026-09-18 | First-hand field signals earn a premium earlier than second-hand expression | 2026–2029 | Medium | J-005, J-015 | [Near-term landscape](10-near.md) | Retain with a different mechanism: traceable first-hand sources may gain value first; broad field-premium pricing is unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-022](#j-022--forgable-signals-drive-credential-upgrades) | 2026-09-18 | As forgable signals multiply, selection moves toward more expensive credentials | 2026–2029 | Medium | J-005, J-017 | [Near-term landscape](10-near.md) | Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-023](#j-023--attention-shifts-toward-fulfilled-commitments) | 2026-09-18 | Attention shifts from expression toward relationships and fulfilled commitments | 2027–2030 | Medium | J-017, J-022, J-013 | [Near-term landscape](10-near.md) | Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-024](#j-024--credentials-re-layer-landscape-only) | 2026-09-18 | Credentials may be re-layered, but the institutional destination remains uncertain | 2027–2032 | Low | J-022, J-013 | [Near-term landscape](10-near.md) | Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-025](#j-025--small-team-output-rises) | 2026-09-18 | Small teams complete more verifiable output with fewer steps | 2027–2030 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-026](#j-026--responsibility-boundaries-remain) | 2026-09-18 | Responsibility boundaries do not disappear at the same rate as knowledge-work capacity | 2027–2032 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-027](#j-027--rented-compute-spreads-capability) | 2026-09-18 | Rented compute spreads capability without distributing gains evenly | 2026–2029 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-028](#j-028--access-becomes-a-bargaining-node-landscape-only) | 2026-09-18 | Data, distribution, and liability access may become new bargaining nodes | 2027–2032 | Low | J-005, J-013 | [Near-term landscape](10-near.md) | Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-029](#j-029--demand-side-anchors-persist) | 2026-09-18 | Status, certainty, embodied presence, and responsibility remain demand-side anchors | 2026–2030 | Medium | J-017, J-011 | [Near-term landscape](10-near.md) | Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven. | ACTIVE | 2027-06-30 |
| [J-030](#j-030--ai-mediates-coordination-not-shared-experience-landscape-only) | 2026-09-18 | AI mediates coordination but cannot mediate shared experience | 2027–2032 | Low | J-017, J-011 | [Near-term landscape](10-near.md) | Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-031](#j-031--pausable-replayable-rollback-capable-action-environments-become-admission-conditions-for-long-horizon-ai-execution) | 2026-09-18 | Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution | 2026–2032 | Medium | J-010 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: logging, oversight, and risk control have institutional support; a complete rollback gate and its window are unverified. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-032](#j-032--authorization-review-and-exception-escalation-become-scarcer-than-execution-steps) | 2026-09-18 | Authorization review and exception escalation become scarcer than execution steps | 2027–2032 | Medium | J-013 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-033](#j-033--verifiable-records-of-real-interventions-become-more-valuable-than-explanation-itself) | 2026-09-18 | Verifiable records of real interventions become more valuable than explanation itself | 2029–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: compliance evidence, model risk controls, and intervention records are gaining value; superiority to explanation is unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-034](#j-034--synthetic-evidence-is-accepted-first-in-low-liability-contexts-high-liability-contexts-still-require-real-trials) | 2026-09-18 | Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-035](#j-035--responsibility-collateral-enters-the-transaction-structure-for-consequential-ai-output) | 2026-09-18 | Responsibility collateral enters the transaction structure for consequential AI output | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: liability governance, insurance, and compensation are entering transactions, but universal “liability collateral” is unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-036](#j-036--long-term-fulfillment-records-allocate-attention-better-than-one-off-natural-expression) | 2026-09-18 | Long-term fulfillment records allocate attention better than one-off natural expression | 2027–2032 | Medium | J-017 | [Mid-term landscape](20-mid.md) | Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-037](#j-037--comparable-small-teams-produce-more-verifiable-output) | 2026-09-18 | Comparable small teams produce more verifiable output | 2027–2031 | Medium | J-009 | [Mid-term landscape](20-mid.md) | Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-038](#j-038--authorization-exception-escalation-and-responsibility-roles-do-not-shrink-as-fast-as-execution-steps) | 2026-09-18 | Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps | 2027–2032 | Medium | J-013 | [Mid-term landscape](20-mid.md) | Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-039](#j-039--rented-models-become-abundant-while-energy-data-and-channel-control-create-access-rents) | 2026-09-18 | Rented models become abundant, while energy, data, and channel control create access rents | 2027–2033 | Medium | J-001 | [Mid-term landscape](20-mid.md) | Retain with a different mechanism: model rental may become abundant, while energy and infrastructure constraints are real; data and channel rents remain unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-040](#j-040--balance-sheets-able-to-absorb-ai-accidents-become-a-separate-scarcity) | 2026-09-18 | Balance sheets able to absorb AI accidents become a separate scarcity | 2028–2033 | Medium | J-005 | [Mid-term landscape](20-mid.md) | Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-041](#j-041--ai-first-expands-the-coordination-radius-of-weak-ties) | 2026-09-18 | AI first expands the coordination radius of weak ties | 2027–2033 | Medium | J-017 | [Mid-term landscape](20-mid.md) | Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-042](#j-042--shared-experience-and-embodied-presence-remain-the-capacity-ceiling-for-strong-ties-landscape-only) | 2026-09-18 | Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only) | 2027–2033 | Low | J-011 | [Mid-term landscape](20-mid.md) | Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects. | ACTIVE | 2027-06-30 |
| [J-043](#j-043--high-value-agent-execution-may-shift-to-boundary-grants-rather-than-step-by-step-operation-landscape-only) | 2026-09-18 | High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only) | 2033–2040 | Low | J-031, J-032, J-014 | [Far-term landscape](30-far.md) | Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-044](#j-044--liability-positions-able-to-absorb-accidents-become-the-load-bearing-wall-of-agent-infrastructure-landscape-only) | 2026-09-18 | Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only) | 2033–2040 | Low | J-032, J-040 | [Far-term landscape](30-far.md) | Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-045](#j-045--as-synthetic-expression-becomes-abundant-unarranged-observation-of-reality-becomes-scarce-landscape-only) | 2026-09-18 | As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only) | 2033–2040 | Low | J-033, J-034 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: provenance standards support the relative importance of original records, not inevitable scarcity of unarranged observation. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-046](#j-046--high-liability-settings-retain-a-premium-for-field-causal-records-landscape-only) | 2026-09-18 | High-liability settings retain a premium for field causal records (landscape only) | 2033–2040 | Low | J-033, J-034 | [Far-term landscape](30-far.md) | Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-047](#j-047--copyable-ai-relationships-expand-companionship-supply-while-non-copyable-reciprocity-becomes-scarce-landscape-only) | 2026-09-18 | Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only) | 2033–2040 | Low | J-041, J-042 | [Far-term landscape](30-far.md) | Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-048](#j-048--authorization-exit-and-subject-boundaries-in-humanai-relationships-become-normative-issues-landscape-only) | 2026-09-18 | Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only) | 2033–2040 | Low | J-041, J-042 | [Far-term landscape](30-far.md) | Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-049](#j-049--as-ai-coordination-becomes-abundant-jointly-bearing-irreversible-commitments-becomes-scarce-landscape-only) | 2026-09-18 | As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only) | 2033–2040 | Low | J-041, J-038 | [Far-term landscape](30-far.md) | Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-050](#j-050--the-value-of-human-collaboration-shifts-from-doing-steps-together-to-choosing-commitments-together-landscape-only) | 2026-09-18 | The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only) | 2033–2040 | Low | J-041, J-038 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: governance preserves human confirmation at key points, but does not prove a wholesale shift in collaboration value. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-051](#j-051--abundant-advice-does-not-automatically-disperse-real-action-rights-landscape-only) | 2026-09-18 | Abundant advice does not automatically disperse real action rights (landscape only) | 2033–2040 | Low | J-039, J-040, J-035 | [Far-term landscape](30-far.md) | Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven. | REVISED (2026-09-20 diffusion gate: the billion-scale figure is an upper bound for affected people, not a count of distinct weekly actors; the object is an institutional arrangement, retained as a landscape/institutional judgment) | 2027-12-31 |
| [J-052](#j-052--energy-real-world-data-authorization-and-compensation-form-far-term-institutional-access-points-landscape-only) | 2026-09-18 | Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only) | 2033–2040 | Low | J-039, J-040, J-035 | [Far-term landscape](30-far.md) | Retain but with insufficient evidence: energy, real-world data, authorization, and compensation have present-day entry points; the long-term combination remains an inference. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-053](#j-053--as-generatable-goods-become-abundant-what-one-personally-bore-may-become-a-signal-of-meaning-landscape-only) | 2026-09-18 | As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only) | 2033–2040 | Low | J-042, J-029 | [Far-term landscape](30-far.md) | Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence. | ACTIVE | 2027-12-31 |
| [J-054](#j-054--non-delegable-time-bodily-risk-and-long-commitments-remain-demand-side-scarcities-landscape-only) | 2026-09-18 | Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only) | 2033–2040 | Low | J-042, J-029 | [Far-term landscape](30-far.md) | Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven. | ACTIVE | 2027-12-31 |
| [J-055](#j-055--real-world-signals-earn-a-premium-as-contract-assets-in-high-liability-tasks) | 2026-09-18 | In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium | 2029–2033 | Medium | J-005, J-033, J-034, J-039 | [C2: How Real-World Signals Become Contract Assets](chains/20-real-signals-become-contracts.md) | Directionally consistent with stronger data governance and provenance, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-056](#j-056--the-binding-constraint-on-compute-expansion-moves-from-chip-supply-to-power-delivery-and-interconnection-permits) | 2026-09-19 | The binding constraint on compute expansion moves from chip supply to power delivery and interconnection permitting | 2026–2031 | Medium | J-001, J-027 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Directionally consistent with "AI electricity use is a real constraint," but this project claims something narrower: the binding constraint is the timing of delivery and permitting, not total generation; load-side queue data was not obtained this round. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-057](#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date) | 2026-09-19 | In compute power transactions what is priced is mainly not energy but certainty of being live on the promised date | 2027–2032 | Medium | J-056 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Partly consistent but reversed: terms protect the seller, the card claims buyer premium; falsifier not computable today. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-058](#j-058--ai-load-splits-into-latency-sensitive-and-schedulable-halves-and-the-schedulable-half-becomes-a-grid-flexibility-resource) | 2026-09-19 | AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a flexibility resource the grid pays for | 2027–2033 | Medium | J-056, J-018 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Mechanism confirmed (EPRI measurement), scale unknown: no industry breakdown of contracted capacity; falsifier not computable. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-059](#j-059--the-handle-of-compute-control-moves-from-hardware-export-to-the-use-side) | 2026-09-19 | Rental lets capability cross borders while hardware stays put, so the handle of compute control moves from hardware export to parties, purposes, and site authorization | 2026–2031 | Medium | J-001, J-027 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Partly consistent with one divergence: control has indeed moved beyond the chip (weights and data-centre authorization), but the landing point is not the account-level remote-access licensing this project expected. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-060](#j-060--energy-rich-hosts-trade-sites-for-compute-and-gain-rent-rather-than-capability-sovereignty-landscape-only) | 2026-09-19 | Energy-rich hosts trade sites and power for compute investment and gain rent and employment rather than capability sovereignty (landscape only) | 2028–2035 | Low | J-056, J-059 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Country-level caps and data-centre authorization already exist, but the inference about host states' long-run bargaining position lacks evidence; kept as landscape only. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-061](#j-061--local-externalities-of-data-centres-become-explicit-and-social-licence-becomes-a-real-siting-constraint) | 2026-09-19 | Local externalities of data centres become explicit and social licence becomes a real cost line in siting | 2026–2031 | Medium | J-056 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Consistent, and the tariff half already happened early (Ohio, Georgia); the moratoria half has no systematic count. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-062](#j-062--heavy-assets-are-taxable-while-the-value-layer-is-mobile-so-local-shares-stay-structurally-low-landscape-only) | 2026-09-19 | What can be taxed is the immovable heavy asset while the profit sits in a mobile value layer, so local shares stay structurally low (landscape only) | 2028–2035 | Low | J-061, J-039 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Half evidenced: taxable assets quantified (JLARC), value-layer escape unstudied. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-063](#j-063--the-geography-of-compute-is-decided-by-interconnection-queues-and-permitting-speed-not-by-electricity-price) | 2026-09-19 | Until grid expansion catches up, the geography of compute is explained by interconnection queues and permitting speed rather than electricity price | 2026–2030 | Medium | J-056, J-057 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Mechanism confirmed (DOE, ERCOT); no price-versus-wait-time data exists, so the falsifier is not computable. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-03-31 |
| [J-064](#j-064--if-efficiency-gains-keep-outpacing-load-growth-the-constraint-in-this-chain-dissolves-in-the-long-run-landscape-only) | 2026-09-19 | If efficiency gains keep outpacing load growth and load can migrate across regions, this chain's constraint dissolves in the long run (landscape only) | 2033–2040 | Low | J-056, J-058 | [C3: Electrons on the Ground](chains/30-power-land-and-permits.md) | Decoupling happened historically (2010-2018), current data runs the other way (LBNL, IEA); kept as counter-hypothesis. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-12-31 |
| [J-065](#j-065--once-ai-executes-across-ownership-boundaries-the-scarce-item-is-not-rollback-software-but-the-right-to-reverse) | 2026-09-19 | What is scarce is not sandbox and rollback software but the right to pull state back out of the counterparty's ledger | 2027–2033 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Comparison not completed this round: unknown. | REVISED (2026-09-20 diffusion-gate downgrade to an occupational/organizational judgment; the old card is kept) | 2027-06-30 |
| [J-066](#j-066--the-five-gates-are-necessary-not-sufficient) | 2026-09-19 | The five diffusion gates are necessary, not sufficient: fail any one and the answer is no, pass all five and you merely qualify to compete | 2026–2036 | Medium | J-067, J-068, J-069, J-070, J-071 | [Retrospect](01-retrospect.md) | Consistent with Rogers 1962's five attributes and Moore 1991's chasm; the divergence is that this document rewrites scored attributes into veto-style necessary conditions, at the cost of betting everything on the gate set being complete — a cost the New Coke counter-example makes explicit. | ACTIVE | 2027-06-30 |
| [J-067](#j-067--the-audience-ceiling-of-a-capability-is-the-headcount-and-frequency-of-the-activity-it-serves) | 2026-09-19 | A capability's audience ceiling is set by how many people perform the activity it serves and how often, not by the ceiling of the technology | 2026–2036 | Medium | — | [Retrospect](01-retrospect.md) | A genuine gap in the literature: Rogers characterizes attributes of the innovation itself and Bass treats market potential as an exogenous parameter; neither asks how many people perform the activity. Confidence is not raised because no external framework has ever calibrated it. | ACTIVE | 2027-06-30 |
| [J-068](#j-068--what-diffuses-replaces-an-activity-already-happening-not-something-added-on-top) | 2026-09-19 | What diffuses replaces an activity already happening, rather than adding one more thing on top of it | 2026–2036 | Medium | — | [Retrospect](01-retrospect.md) | Heavily overlapping with Rogers's relative advantage; the divergence is that only "replaces nothing" is treated as a veto condition here, with the size of the cost drop demoted to a speed variable rather than a pass mark. | ACTIVE | 2027-06-30 |
| [J-069](#j-069--infrastructure-that-serves-only-one-capability-does-not-get-built) | 2026-09-19 | Dedicated infrastructure that exists for one capability alone does not get built; the capability waits until its carrier exists for other reasons | 2026–2036 | Medium | — | [Retrospect](01-retrospect.md) | The literature offers only neighbours (Teece's complementary assets, Zittrain's generativity); they answer who profits and why general platforms grow unexpected applications, not whether this dedicated infrastructure will be built at all. | ACTIVE | 2027-06-30 |
| [J-070](#j-070--when-many-parties-must-change-together-change-needs-enforceable-and-observable-authority-a-single-subsidizing-party-or-a-local-closed-loop) | 2026-09-19 | When many parties must change together, change happens only if one of three unlocks holds: enforceable and observable authority, a single subsidizing party, or a local closed loop | 2026–2036 | Medium | — | [Retrospect](01-retrospect.md) | Consistent with Olson 1965 on collective action (coercion, selective incentives, small groups); the increment here is the half-clause that enforcement must be observable, drawn from Prohibition and the US metrication attempt. | ACTIVE | 2027-06-30 |
| [J-071](#j-071--recurring-net-burden-not-gross-friction-sets-the-voluntary-adoption-ceiling) | 2026-09-19 | Voluntary adoption must compare recurring net burden with the real incumbent; only a positive, material burden that accumulates with frequency pushes the ceiling far below the activity population | 2026–2036 | Medium | — | [Retrospect](01-retrospect.md) | Partly overlaps Rogers's complexity and relative advantage; self-service retail refuted the veto based on any recurring friction, so this round narrows the rule to a net comparison. | REVISED | 2027-06-30 |
| [J-072](#j-072--choosing-one-from-dozens-of-generated-candidates-is-an-occupational-judgment-not-a-society-level-trend) | 2026-09-19 | "Choosing one from dozens of candidates" is an occupational judgment with a ceiling in the millions at weekly frequency; it fails Gate 1 | 2026–2031 | Medium | J-066, J-067 | [Retrospect](01-retrospect.md) | Comparison not completed this round: unknown. | ACTIVE | 2027-06-30 |
| [J-073](#j-073--embodied-intelligence-is-the-necessary-complement-for-ai-to-reach-the-physical-labour-population-not-a-sufficient-condition-for-diffusion) | 2026-09-20 | Embodiment is the necessary complement for AI to reach the physical-labour population, not a sufficient condition: changing the denominator only opens Gate 1 | 2026–2040 | Medium | J-006, J-066, J-067, J-068, J-069, J-070, J-071 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Both ends agree (IFR proves embodied capability can diffuse; Abundant Robotics proves technical feasibility is not commercial feasibility); nothing calibrates the arrival order in between, and four key data series are recorded as gaps. | ACTIVE | 2027-06-30 |
| [J-074](#j-074--contact-transfer-in-care-crosses-inside-institutions-first-and-homes-reach-no-society-level-diffusion-inside-this-window) | 2026-09-20 | Contact bed-to-chair transfer becomes standard institutional equipment no earlier than 2032–2038; homes reach no society-level diffusion inside this window | 2026–2038 | Medium | J-073, J-066 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Agreement: ROBEAR proves capability-side feasibility was demonstrated a decade ago, so the silence cannot be explained by capability; the boundary is no deployment-scale or retention data, and US-only occupational figures. | ACTIVE | 2027-12-31 |
| [J-075](#j-075--warehousings-bottleneck-has-moved-from-moving-to-grasping-unstructured-picking-arrives-first-and-door-to-door-delivery-does-not-hold-inside-this-window) | 2026-09-20 | Warehousing's bottleneck moved from moving to grasping; unstructured picking at 2028–2033, door-to-door delivery does not hold inside this window | 2026–2033 | Medium | J-073, J-066 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Agreement: official occupational data proves material-handling roles are millions-scale and citable; the boundary is one country only, with no public data on per-pick pricing penetration or deployment hours. | ACTIVE | 2027-06-30 |
| [J-076](#j-076--manufacturings-one-real-scaling-passed-through-gate-4s-local-closed-loop-flexible-assembly-and-high-mix-low-volume-are-still-outside-the-gate) | 2026-09-20 | Manufacturing's scaling passed through Gate 4's local closed loop; flexible assembly at 2028–2034, high-mix low-volume holds only locally inside this window | 2026–2034 | Medium | J-073, J-066 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Agreement: IFR proves embodied capability can genuinely diffuse; the divergence is that a total does not imply a composition, and no public series exists for installation composition, changeover time or residual values. | ACTIVE | 2027-06-30 |
| [J-077](#j-077--in-agriculture-what-crossed-is-milking-not-harvesting-seasonality-and-fragmentation-hold-cost-per-task-above-labour) | 2026-09-20 | In agriculture what crossed is milking, not harvesting; selective harvesting is not a mainstream practice before 2030 | 2026–2030 | Medium | J-073, J-066 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Agreement: Abundant Robotics proves technical feasibility is not commercial feasibility and FAO supports where the denominator sits; the boundary is a single case on the failure side and FAO used for magnitude only. | ACTIVE | 2027-06-30 |
| [J-078](#j-078--construction-and-domestic-work-are-blocked-by-the-one-off-site-and-somebody-elses-home-inside-this-window-they-arrive-only-as-single-operation-equipment-and-single-task-slices) | 2026-09-20 | On-site construction robots remain single-operation equipment through 2040, and open-ended household tasks reach no society-level diffusion inside this window | 2026–2040 | Medium | J-073, J-066 | [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) | Agreement: Hadrian is still at single-operation scale after a decade, and ILO proves domestic demand is already paid for; the boundary is that both are single-case or single-group definitions and this is a negative long-window judgment. | ACTIVE | 2027-12-31 |
| [J-079](#j-079--biomedical-candidate-generation-and-clinical-grade-causal-proof-diverge) | 2026-09-21 | Biomedical candidate generation and ranking get cheaper, while clinical-grade causal proof does not accelerate proportionally | 2026–2034 | Medium | J-005, J-034, J-066 | [C5: Biology and Medicine](chains/50-biology-medicine.md) | FDA's risk and context-of-use framework supports “generation is not proof,” not this card's window or acceleration ceiling. | ACTIVE | 2027-06-30 |
| [J-080](#j-080--low-liability-medical-workflows-diffuse-before-autonomous-care-without-professional-review) | 2026-09-21 | Summarization, coding, scheduling, and review-based decision support become routine before autonomous diagnosis and treatment without professional review | 2026–2031 | Medium | J-079, J-066, J-068, J-069 | [C5: Biology and Medicine](chains/50-biology-medicine.md) | FDA's list proves authorized products exist, not deployment scale or autonomy level. | ACTIVE | 2027-06-30 |
| [J-081](#j-081--more-drug-candidates-do-not-proportionally-shorten-human-trial-time) | 2026-09-21 | AI increases drug candidates reaching laboratories, but candidate growth does not translate proportionally into approvals | 2026–2034 | Medium | J-079, J-066 | [C5: Biology and Medicine](chains/50-biology-medicine.md) | FDA supports risk-linked credibility requirements, not a forecast of development time or success rate. | ACTIVE | 2027-06-30 |
| [J-082](#j-082--once-explanation-is-abundant-medical-scarcity-moves-to-authorized-intervention-and-continuity-of-care-landscape-only) | 2026-09-21 | In chronic disease, ageing, and primary care, the bottleneck moves from standard explanation to authorized intervention, continuous observation, and exception escalation | 2027–2034 | Low (landscape only) | J-079, J-080, J-032, J-066 | [C5: Biology and Medicine](chains/50-biology-medicine.md) | WHO supports workforce, accountability, and safety boundaries, not that AI worsens care queues. | ACTIVE | 2027-12-31 |
| [J-083](#j-083--personalized-explanation-becomes-abundant-before-verifiable-mastery) | 2026-09-21 | Personalized explanations, examples, and immediate feedback become routine, but verifiable mastery does not grow proportionally | 2026–2030 | Medium | J-001, J-066 | [C6: Education and Skill Formation](chains/60-education-skill-formation.md) | UNESCO supports human-centred and pedagogical boundaries, not that outcomes fail to rise proportionally. | ACTIVE | 2027-06-30 |
| [J-084](#j-084--ai-tutoring-enters-teacher-and-institutional-workflows-before-replacing-schools) | 2026-09-21 | AI tutoring diffuses first through teacher assignment, curriculum alignment, and institutional supervision rather than large-scale school replacement | 2026–2031 | Medium | J-083, J-066, J-068, J-069, J-070, J-071 | [C6: Education and Skill Formation](chains/60-education-skill-formation.md) | OECD supports institutions as carriers, not that schools retain their current boundaries. | ACTIVE | 2027-06-30 |
| [J-085](#j-085--take-home-artifact-signals-weaken-while-controlled-performance-and-process-evidence-gain-weight) | 2026-09-21 | High-stakes admissions and hiring reduce the weight of take-home artifacts without process verification and increase controlled performance and process evidence | 2027–2034 | Medium | J-022, J-083, J-084, J-066 | [C6: Education and Skill Formation](chains/60-education-skill-formation.md) | UNESCO supports assessment redesign, not which assessment forms gain weight. | ACTIVE | 2027-06-30 |
| [J-086](#j-086--the-explanation-gap-narrows-while-practice-and-verification-gaps-may-widen-landscape-only) | 2026-09-21 | AI narrows access gaps in explanation, but without carrier institutions skill and opportunity gaps may fail to fall or may widen | 2027–2034 | Low (landscape only) | J-083, J-084, J-066, J-069, J-070 | [C6: Education and Skill Formation](chains/60-education-skill-formation.md) | The World Bank supports the scale of foundational learning deficits, not AI's direction of effect on inequality. | ACTIVE | 2027-12-31 |
| [J-087](#j-087--humanmachine-supervisory-units-become-mainstream-before-staffless-organizations) | 2026-09-21 | Human–machine supervisory units become mainstream before staffless organizations | 2026–2031 | Medium | J-006, J-007, J-009, J-066, J-068 | [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md) | NIST supports governance, monitoring, and human oversight, not this organizational form or its time window. | ACTIVE | 2027-06-30 |
| [J-088](#j-088--junior-production-seats-shrink-before-occupations-as-a-whole-apprenticeship-carriers-become-the-new-bottleneck) | 2026-09-21 | Junior production seats shrink before occupations as a whole; apprenticeship carriers become the new bottleneck | 2027–2034 | Medium | J-087, J-083, J-066 | [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md) | Anthropic supports coexistence of augmentation and automation, not the direction of junior hiring or skill formation. | ACTIVE | 2027-06-30 |
| [J-089](#j-089--permission-audit-and-appeal-control-planes-become-production-infrastructure-before-broad-autonomous-authority) | 2026-09-21 | Permission, audit, and appeal control planes become production infrastructure before broad autonomous authority | 2026–2032 | Medium | J-007, J-009, J-031, J-055, J-070 | [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md) | NIST and the EU AI Act support governance, logging, and human oversight, not the diffusion order of appeal control planes. | ACTIVE | 2027-06-30 |
| [J-090](#j-090--productivity-gains-first-concentrate-with-scarce-complementary-asset-owners-competition-and-institutions-decide-whether-they-spread) | 2026-09-21 | Productivity gains first concentrate with scarce complementary-asset owners; competition and institutions decide whether they spread | 2027–2035 | Medium | J-001, J-039, J-056, J-087 | [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md) | Teece's complementary-assets theory supports the value-capture mechanism, not AI's distribution or the length of concentration. | ACTIVE | 2027-12-31 |
| [J-091](#j-091--demand-expansion-and-task-savings-occur-together-net-employment-cannot-be-inferred-from-the-capability-curve-alone) | 2026-09-21 | Demand expansion and task savings occur together; net employment cannot be inferred from the capability curve alone | 2027–2035 | Medium | J-001, J-037, J-073, J-087 | [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md) | Existing comparisons support coexistence of augmentation and automation, not demand elasticity, output expansion, or net employment direction. | ACTIVE | 2027-12-31 |



The overview is a navigation aid. Every full card, strongest opposing mechanism, and evidence is registered in this ledger; source links return to the relevant narrative or technology chain, and IDs and statuses stay synchronized here. The overview’s “near / mid / far” labels are reading containers only; each card’s own time window is the judgment boundary, so overlap with or across a container is not a contradiction.
---

## 3. The `depends-on` graph

### Notation

Use comma-separated formal IDs, for example: `depends-on: J-001, J-002`. A dependency means “if the upstream mechanism fails, this judgment must be reviewed”; it does not mean that both judgments happen simultaneously or point to an article location. A far-horizon judgment without an explicit near-term dependency should be downgraded to landscape only.

Every dependency edge is stored three times in this ledger: on the card’s `depends-on` field (authoritative), in the graph below, and in the depends-on column of the section-2 overview. When a card is added or any `depends-on` changes, update all three in the same commit. Adding a card without wiring it into the graph lets the “complete” view below silently omit the new judgment, which destroys its only purpose: enumerating every affected judgment when an upstream is falsified.

Current dependency tree (complete view, covering J-001–J-091; each card’s `depends-on` is authoritative):

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
J-056 <- J-001, J-027
J-057 <- J-056
J-058 <- J-056, J-018
J-059 <- J-001, J-027
J-060 <- J-056, J-059
J-061 <- J-056
J-062 <- J-061, J-039
J-063 <- J-056, J-057
J-064 <- J-056, J-058
J-065 <- J-001
J-066 <- J-067, J-068, J-069, J-070, J-071
J-067 (root)
J-068 (root)
J-069 (root)
J-070 (root)
J-071 (root)
J-072 <- J-066, J-067
J-073 <- J-006, J-066, J-067, J-068, J-069, J-070, J-071
J-074 <- J-073, J-066
J-075 <- J-073, J-066
J-076 <- J-073, J-066
J-077 <- J-073, J-066
J-078 <- J-073, J-066
J-079 <- J-005, J-034, J-066
J-080 <- J-079, J-066, J-068, J-069
J-081 <- J-079, J-066
J-082 <- J-079, J-080, J-032, J-066
J-083 <- J-001, J-066
J-084 <- J-083, J-066, J-068, J-069, J-070, J-071
J-085 <- J-022, J-083, J-084, J-066
J-086 <- J-083, J-084, J-066, J-069, J-070
J-087 <- J-006, J-007, J-009, J-066, J-068
J-088 <- J-087, J-083, J-066
J-089 <- J-007, J-009, J-031, J-055, J-070
J-090 <- J-001, J-039, J-056, J-087
J-091 <- J-001, J-037, J-073, J-087
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

The end of a time window or arrival of a **Next review** date is not an automatic HIT; it is a mandatory review event. **Build the due set from preregistered fields, never from status or the observed result**: every card with an original time window, falsifier, and due review date enters the review and calibration denominator whether its status is `ACTIVE` or scope-downgraded `REVISED`. **Classification snapshot as of 2026-09-21**: the scope-downgraded `REVISED` set is **J-001–J-003, J-005–J-028, J-030–J-041, J-043–J-052, and J-055–J-065: 60 cards**. Their audience, applicability, or narrative strength was narrowed, but the original propositions still face reality. The only card currently superseded by a named successor is **J-004 → J-065**: do not count J-004 as a separate outcome; review it with J-065 to avoid counting the same proposition twice. This enumeration is a dated aid for human review, not the selection rule; future due sets follow each card's Section 1 classification, and any new supersession must name its successor in the old card's status note. A bare `REVISED` label is never an exclusion rule.

Handle each due card in this order:

1. Filter the overview for every preregistered judgment whose **Next review** date has arrived or whose time window has ended, including both `ACTIVE` cards and the scope-downgraded `REVISED` set above. Read the full card and every upstream `depends-on` judgment first. Only an old card that names a successor and explicitly says it is no longer reviewed separately may be merged with its successor.
2. Check the card's **falsifier** literally: did the specified observable trigger occur? If so, record `FALSIFIED`, with date, evidence, and observation scope.
3. If the falsifier did not trigger, check the **leading indicator**: did it move in the expected direction, at the stated frequency, and without missing or substituted data? Supporting indicators without the full outcome must not be pre-labelled `HIT`.
4. Record `HIT` only when evidence within the window clearly supports the judgment and no falsifier triggered. State the supporting evidence and uncovered counterexamples.
5. If the preregistered condition cannot be computed because data are private, definitions changed, a source ended, or for another reason, record **`INDETERMINATE`**, naming the missing quantity, why it is not computable, and the next review date. Do not rewrite the original condition to manufacture a result, and do not remove the card from the due set or calibration denominator. `INDETERMINATE` is the result of this review; it does not automatically change the card's `ACTIVE` / `REVISED` status.
6. Use **all independent preregistered judgments due in this round** as the calibration denominator. Report counts and shares for `HIT`, `FALSIFIED`, and `INDETERMINATE`. Never exclude a card after the fact because of its status label, missing evidence, an unfavorable result, a scope downgrade, or a miss. A named predecessor–successor pair counts once, with the mapping recorded in the log.
7. Check all downstream dependencies: an upstream HIT, FALSIFIED, INDETERMINATE, or revision can require downstream review. Follow the propagation steps in Section 3.
8. Update both ledgers in one commit. Add the date, per-card result, evidence anchors, and next action to the review log. The commit message must name the judgment ID and new evidence, never a generic “update docs.”

Review-log format:

| Date | Judgment ID | Status at review | Falsifier check | Leading-indicator check | Result (HIT / FALSIFIED / INDETERMINATE) | In denominator? | Evidence / reason indeterminate | Next action |
|---|---|---|---|---|---|---|---|---|
| 2026-09-18 | J-001 and other initial judgments | ACTIVE | Not due | Registered; no review point yet | — | Not yet | Initial registration | Review at each card's window or checkpoint |

---

## 6. Explicit gaps: dimensions not yet covered

The full-landscape promise remains open. The first chain is not full coverage. Each gap below must remain visible until it receives an independent reasoning chain, bilingual document, and judgment cards.

| Gap dimension | Question to answer | Priority | Status |
|---|---|---|---|
| Embodied intelligence and physical-world labour | How does AI extend beyond screens into care, logistics, manufacturing, agriculture, construction, and domestic work that moves mass or touches bodies? | High | Covered (C4: arrival order, cost per task, priced liability, and scene fragmentation; care deployment scale and cross-scene cost series remain explicit gaps) |
| Social consequences of the technology capability sequence | As technical capabilities arrive in sequence, how are division of labour, institutions, employment, and human–AI relationships rewritten step by step? | High | Covered (C7: organizational work units, occupational entry, permission/audit/appeal, complementary-asset returns, and demand elasticity; cross-national longitudinal organizational data remain an evidence gap) |
| Energy and physical infrastructure | How do hard constraints in compute, data centers, grids, chips, and materials migrate? | High | Covered (C3: J-056–J-064; material and equipment constraints inside chip manufacturing remain open) |
| Biology and medicine | After generation enters experiments, diagnosis, and care, which steps remain constrained by bodies and trials? | High | Covered (C5: candidate generation, clinical proof, drug trials, and continuity of care; cross-national deployment scale and long-term outcome series remain open) |
| Education and skill formation | When “knowing how” becomes cheap, where do learning, screening, and qualification become scarce? | High | Covered (C6: explanation, mastery, institutional carriers, assessment, and qualification; long-term cross-national randomized trials and credential-recognition series remain open) |
| Geopolitics and institutions | How do compute, data, and critical infrastructure change bargaining power among states and organizations? | Medium | Partially covered (J-059–J-060 cover the migration of the control handle and host-state bargaining; inter-state competition and security questions remain open) |
| Law and property | How do liability, data ownership, model output, and licensing rewrite transaction boundaries? | High | Partially covered (C2 and J-055 cover high-liability real-world signals; C3's J-061–J-062 cover local externalities and the tax-base mismatch; data ownership and model-output licensing remain open) |
| Organizations and employment | How do coordination costs, employment relationships, and firm boundaries change? | High | Covered (J-037–J-038; expansion remains) |
| Collaboration between people | How does AI mediation change division of labor, trust, negotiation, and joint decisions? | High | Covered (far-term landscape §4, J-049–J-050; concrete institutional and organizational cases still need expansion) |
| Relationships between people and AI | What norms grow from asymmetries in memory, patience, copyability, and exclusivity? | High | Covered (far-term landscape §3, J-047–J-048; concrete institutional and product boundaries still need expansion) |
| Attention and trust | When content is unlimited and signals are easy to forge, how are attention and credible credentials allocated? | High | Covered (J-035–J-036; expansion remains) |
| Capital and power | What new bottlenecks form around compute ownership, financing, and distribution of returns? | Medium | Covered (J-039–J-040; expansion remains) |
| Human needs, meaning, and embodied presence | Which needs remain stable under supply change, and which preferences actually drift? | Medium | Covered (J-041–J-042; expansion remains) |
| Upstream materials and climate coupling of compute | How do chip-manufacturing materials and equipment, cooling water and climate conditions, and the distributional effect of rising power prices on non-AI users constrain expansion? | Medium | Not covered (new gap identified while reasoning through C3) |
| Population ageing and family care | Starting without AI, how do ageing, smaller families, and care institutions change who repeatedly cares for older people; does this actually become a hundred-million-person weekly action? | High | Gap record (below; first probe, not a judgment card) |

### 6.1 First non-AI social-force diffusion-gate gap record: population ageing × smaller families

> **Record type**: This is a gap entering later historical calibration, not a J-NNN judgment card, and it does not claim to pass the diffusion gates. It deliberately starts from demographic and institutional forces, then checks the intersection with AI.

- **Candidate force**: population ageing raises long-term-care demand, while lower fertility, later marriage, and smaller households reduce the care time available from co-resident relatives. This mechanism does not require falling model cost.
- **Repeat action to test**: an adult personally provides hands-on care for an older relative **at least weekly**, or repeatedly coordinates medication, appointments, home services, and paid care. Later validation must separate hands-on care from care coordination; counts of older people, potentially affected households, or service budgets must not be substituted for actual repeat actors.
- **Best current frequency evidence**: OECD's *Health at a Glance 2023* reports that across 25 countries with comparable data, 13% of surveyed people aged 50 and over provided informal care on average; 8% did so daily and 6% weekly (the components reflect rounding and survey definitions and should not be mechanically added). This establishes that weekly and daily action exists, but **does not provide a worldwide count of distinct people**: only 25 countries are covered, only people aged 50 and over are counted, and SHARE, ELSA, HRS, and national survey definitions are not fully identical. There is therefore not yet enough evidence to write “a hundred million distinct people perform this weekly.” The actual-actor denominator remains an explicit data gap rather than something to fill by extrapolating the older population or the 13% figure.
- **Historical case (“mechanism present,” not society-wide scale)**: Japan introduced long-term-care insurance in 2000. A JILPT policy review describes it as promoting the “socialization” of long-term care and reducing the burden on families with older relatives needing care. The case shows that ageing and family burden can force financing and service carriers to reorganize without AI. It also shows that the result need not be ever more hands-on family care; actions can move to insurance, formal services, and coordinators.
- **Counterexample (`NO` to “ageing necessarily creates mass hands-on weekly family care”)**: Sweden is also old, yet the country's official portal places overall responsibility for elder care on municipalities and lists home help, special housing, and around-the-clock assistance. This does not prove zero family care and supplies no family-carer share. What it does refute is the direct mechanism from ageing to family members necessarily becoming mass weekly hands-on carers. Institutions can change who performs the action, so Gate 1 must count actual actors, while Gates 3 and 4 must examine the public-service carrier and decision rights.
- **Intersection with AI root J-001**: cheaper generation and reasoning may reduce the cost of scheduling, records, reminders, benefits navigation, and cross-provider coordination; embodied systems may also take over some standardized physical tasks. Delete J-001 entirely, however, and the rise in older people, contraction of family-care supply, and reorganization of long-term-care finance and municipal/insurance carriers remain. AI changes **who performs some sub-actions and at what cost**; it is not the root cause of this social force.
- **Next evidence gate**: promotion to a formal judgment requires cross-nationally comparable data for “distinct carers × weekly/daily frequency × hands-on/coordination action,” plus like-for-like comparison of at least two systems with strong formal care supply and two with high family-care shares. Until then, affected population must not masquerade as performing population.

Gaps may be filled or explicitly downgraded later, but never silently removed.

---

## 7. Formal judgment and opportunity index

| Source judgment | Opportunity or window | Hard constraint | Status |
|---|---|---|---|
| [J-003](#j-003--the-genuinely-durable-scarcity-is-ownership-of-private-context-about-you-and-its-usable-form) | [O-001 · Ownership layer for private context](40-opportunities.md#o-001--ownership-layer-for-private-context) | Ownership/privacy | Candidate |
| [J-065](#j-065--once-ai-executes-across-ownership-boundaries-the-scarce-item-is-not-rollback-software-but-the-right-to-reverse) | [O-002 · The Access Layer for Cross-Party Reversal Rights](40-opportunities.md#o-002--the-access-layer-for-cross-party-reversal-rights) | Ownership/privacy + trust/relationship | Candidate (narrowed 2026-09-19 out of J-004 / the former O-002) |
| [J-005](#j-005--after-generation-becomes-abundant-value-concentrates-in-three-kinds-of-non-recombinable-input-raw-signals-accountable-commitments-and-validated-causality) | [O-003 · Accountable commitment layer](40-opportunities.md#o-003--accountable-commitment-layer) | Legal liability | Candidate |
| [J-057](#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date) | [O-004 · Certainty layer for deliverable power and permitted sites](40-opportunities.md#o-004--certainty-layer-for-deliverable-power-and-permitted-sites) | Physical + law/liability + ownership/privacy | Candidate |
| [J-002](#j-002--selecting-objectively-high-quality-from-abundant-output-is-not-a-durable-scarcity-but-merely-a-24-year-window) | AI output quality assurance / selection | No hard constraint; likely automated | Window |
| [J-019](#j-019--token-saving-is-a-window) | Prompt optimization / token-saving tools | No hard constraint; the rejection rate falls as models get stronger | Window |
| [J-065](#j-065--once-ai-executes-across-ownership-boundaries-the-scarce-item-is-not-rollback-software-but-the-right-to-reverse) · [J-031](#j-031--pausable-replayable-rollback-capable-action-environments-become-admission-conditions-for-long-horizon-ai-execution) | Within-boundary action sandboxes / shadow environments / rollback of your own resources | No hard constraint; the platform has every incentive to bundle it as a default and give it away | Window (downgraded 2026-09-19 out of the former O-002) |
| [J-057](#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date) | Bridge generation and interconnection acceleration | Value comes from the queue; it closes once grid expansion catches up | Window |
---

## 8. Review log

| Date | Action | Result | Commit |
|---|---|---|---|
| 2026-09-18 | J-031–J-042 metadata repair review | Repaired misaligned Source, Next review, and Status fields in the bilingual cards; e25f0fd passed fresh-context acceptance | e25f0fd |
| 2026-09-18 | Mid-term expansion: added J-031–J-042, completed six-dimension narrative, dependency graph, and review log | Bilingual card fields are equivalent; low-confidence cards remain landscape only; window opportunities are marked in the narrative | — |
| 2026-09-18 | Narrow correction: restored J-006–J-016 to the overview, aligned the technology-chain gap status, and clarified containers versus card windows | Both ledgers cover J-001–J-030; technology-chain status is equivalent; card-specific windows remain authoritative | — |
| 2026-09-18 | C2 successor chain and J-055 bilingual delivery | Added the real-signal contract-asset chain; connected bilingual C1 links; synchronized J-055 in the overview, dependency graph, and full card; kept the law-and-property gap partially covered | c4e4adcc |
| 2026-09-19 | Dependency-graph completeness and duplicate review (J-001–J-055, both languages) | Edge-by-edge check: 55 graph entries, 55 cards, and 55 overview rows agree exactly; no duplicate edges, no edge pointing at a non-existent ID, no cycles, every node traces back to J-001; the Chinese and English graphs match edge for edge. Also recorded the three-place synchronization rule in section 3 and in the pre-publication checklist | — |
| 2026-09-19 |  First external-comparison round closed (J-001–J-055, both languages) | All 55 cards carry "Against consensus" and "External comparison source"; the EXT-1–EXT-18 index now names the chapter or topic anchor actually used and what each source does and does not support. The 40 cards that previously stated only agreement/divergence received the third §1.2 element — why the judgment is retained or confidence lowered; J-043 was re-marked as "may / landscape only"; the stale "external comparison is not complete" sentence in `20-mid.md` was replaced with the actual comparison verdict. Independent reasoning text and reasoning chains were left unchanged, and both languages landed in one commit  | — |
| 2026-09-19 | C3 energy–geopolitics–law chain delivered: added J-056–J-064 and the bilingual chain document | The nine new cards are synchronized across the overview, the dependency graph, and the card section; in the gap list "energy and physical infrastructure" becomes covered, "geopolitics and institutions" and "law and property" become partially covered, and a new gap for upstream materials and climate coupling was added; EXT-19 and EXT-20 were registered; J-057, J-058, J-061, J-062, J-063, and J-064 completed no external comparison this round and are explicitly marked unknown per the methodology | — |
| 2026-09-19 |  First external comparison closed for the nine C3 cards (J-056–J-064, both languages) | Twelve sources added as EXT-21–EXT-32 (FERC's PJM co-located load order, PUCO's AEP Ohio data-centre tariff, Georgia PSC large-load billing rules, Duke Nicholas Institute flexible-load modelling, EPRI DCFlex field measurement, PJM cleared demand response, the LBNL data-centre energy report, Masanet et al. 2020, Virginia JLARC Report 598, DOE's recommendations on powering AI, ERCOT large-load queue data, and Good Jobs First [⚠ advocacy]). J-057, J-058, J-061, J-062, J-063 and J-064 — previously marked "unknown / comparison not completed" — now carry all three elements, and J-056 and J-060 received the third; no ACTIVE judgment in the ledger still lacks a comparison. Three falsifiers were found to be **not computable today** and this was written into the cards (J-057 confidential contract terms, J-058 no industry breakdown of demand response, J-063 no price-versus-wait-time comparison), with one leading indicator added to J-058 and J-063 to make each falsifiable again. One source misuse is corrected: EXT-19 (LBNL *Queued Up*) covers generation and storage interconnection only, not the load side. Independent reasoning text, reasoning chains and falsifiers were left unchanged, and both languages landed in one commit  | — |
| 2026-09-19 | Reader reachability and bilingual parity closed (whole repository, both languages) | The README document map became a bilingual table of real links and gained entries for the three time-layer files; every J-NNN and O-NNN in prose now points at a full heading-slug anchor (GitHub does not match short anchors); English `10-near.md` and `30-far.md` had 39 malformed nested links removed; the glossary gained the five hard-constraint categories, the three exits, and the card-field vocabulary, and three terms were corrected to match actual usage in the prose. **One failed self-check is corrected here**: the commit message of d28d747 claims "596 internal links resolve with zero failures", but that figure came from an intermediate tree without the C3 references; its own tree had 602 links and 6 dangling ones, because the README referenced a C3 chain not yet committed. 6c47aee closed the gap at 842 links with zero failures. Lesson: run the checklist on the tree you are about to commit, never on an intermediate one | d28d747 / 6c47aee |
| 2026-09-19 | O-002 re-reviewed against the opportunity-durability gate's third question: disposition decided and the candidate narrowed (both languages) | The former O-002, "Reversible Infrastructure for AI Action," contained **not one sentence** answering the opportunity-durability gate's third question, and the subject of its "physical" argument was the protected object rather than the scarce item. Taken apart layer by layer, it splits in two: when an action does **not** cross an ownership boundary (your own database, your own cloud resources, a test sandbox), rollback is pure software and the system being operated on is held by the platform itself, which has every incentive to bundle it as a default and give it away — that half has payers but fails the opportunity-durability gate, and is downgraded to the Window List; when an action **does** cross an ownership boundary, the state lands in the counterparty's ledger, reversal must be consented to and executed by that party, whose default interest is finality, and compute cannot copy that obligation — that half is retained as candidate O-002, "The Access Layer for Cross-Party Reversal Rights," with the hard constraint changed from "physical + law/liability" to **ownership/privacy + trust/relationship**. Per the section-1 rule, J-004 is marked `REVISED` and kept verbatim, and the new card J-065 carries the narrowed judgment, synchronized into the overview, the dependency graph, and the opportunity index. Three related contradictions were fixed alongside: `00-method.md`'s example for exit A was precisely the item being downgraded (the methodology was citing itself into a contradiction); `20-mid.md` had long described "pausable, replayable, rollback-capable action environments" as a window opportunity without ever registering it (now registered, source J-031); and the section-7 index was missing the J-019 window row (added). **The cost is recorded honestly**: J-065 completed no external comparison this round and is marked "unknown" per the methodology, so the property "no ACTIVE judgment in this ledger still lacks a comparison" is temporarily void until the next comparison round | — |
| 2026-09-19 | Historical retrospective delivered: diffusion gates extracted from the history of technology, politics and business, then attacked (both languages) | Added the bilingual `01-retrospect.md` prose plus seven cards J-066–J-072 and six sources EXT-33–EXT-38. **Every new section this round is appended at the end of the file as section 11; not one existing section number and not one existing card was touched.** Each of the five gates (scale / substitution / carrier / decision rights / cost) carries 2 successes + 2 failures across all three domains, with three self-attack locks attached: the exclusivity test (section 5), the sufficiency counter-example New Coke (section 6 — passes all five gates, withdrawn after 79 days), and a back-check of this project's own judgments (section 7: the C1 opening, "choosing one out of sixty candidates," is judged an **occupational** matter at millions scale and weekly frequency and fails Gate 1; no existing card was deleted or downgraded, only qualified by audience size). **Three proactive corrections with their costs recorded**: (1) the popular narrative that Vietnam War military shipping forced container standardization runs opposite to the primary material (the DoD was adapting to an already-commercialized civilian system, and the military CONEX was a separate system), so the prose explicitly declines to use it; (2) J-068's originally drafted title contained "and cuts the unit cost by an order of magnitude," which conflicts with this document's own passing case (China's household responsibility system), so before landing it was narrowed to judge on "substitution vs addition" alone, with the size of the cost drop demoted to a speed variable; (3) the hydrogen fuel-cell car cell is the weakest in the exclusivity table (retail hydrogen per kilometre costs more than gasoline), so the fork — if that row's exclusivity fails, Gate 3 should be merged into Gate 2 and the five gates contract to four — is written into the prose rather than avoided. J-072 completed no external comparison this round and is marked "unknown" per the methodology | — |
| 2026-09-19 | Historical retrospective repaired after independent review | After `2f8f54f`, fresh-context review rejected the fifth row in section 5: by Gate 5's own test Dvorak was a one-time amortizable cost, and "on everybody else's machine too" was Gate 4's mechanism. Gate 5 was rebuilt rather than merged because Google Glass's social cost and 3D television's per-use burden contain no multi-party coordination. J-071's "hobbyists" wording was narrowed to the measurable "far below the headcount of the activity," with the falsifier changed to majority adoption (>50%); verdict dates were added. The MOOC attack and answer are in the narrative; EXT-39 (CDC) and EXT-40 (WHO) were added. The unresolved weak point is contact lenses' "replacement": most wearers use them alongside frame glasses. | 2f8f54f |
| 2026-09-20 | Embodied-intelligence and physical-world labour dimension delivered (C4, both languages) | Added the C4 chain across care, logistics, manufacturing, agriculture, construction, and domestic work; recorded that embodied capability is necessary but not sufficient for diffusion, and corrected the coverage status of collaboration and human–AI relationships. | — |
| 2026-09-20 | Diffusion gate (Gate 1 · scale) reviewed across the whole ledger: all 72 cards given an audience-scale magnitude and a pass/fail verdict, with the conclusions fed back into the prose (both languages) | **Counting method**: each card's “Diffusion-gate review” field records exactly one audience-scale magnitude, so the 72 cards map one-to-one onto magnitudes with no double counting and no omission; the buckets sum to 72. **Distribution**: hundred-thousand-scale 6 (J-066–J-071) / million-scale 17 (J-001–J-016, J-072) / ten-million-scale 26 / hundred-million-scale 18 / billion-scale 5. **The two figures this round was asked for**: (1) **occupational “million-scale”** — strictly the million-scale bucket, **17 cards, 23.6%**; widened to “occupational/method judgments at million-scale or below” (adding the 6 hundred-thousand-scale cards), **23 cards, 31.9%**. (2) **“billion-scale, society-wide”** — **5 cards, 6.9%**, of which **4 pass Gate 1** (J-029, J-042, J-053, J-054; 5.6%); J-051 has a billion-scale audience but what it judges is an institutional and resource-allocation arrangement rather than a repeatable individual consumption activity, so it fails. **Disposition**: the **60 cards** that fail Gate 1 and were `ACTIVE` are now `REVISED`, with the original card text kept word for word and identifiers not reused; the overview table's status column is synchronised. J-004 was already `REVISED` on 2026-09-19 for a different reason, so this round only adds its diffusion-gate review field and leaves the status alone. J-066–J-072 are the test itself rather than predicted society-wide consumption activities: their diffusion-gate verdicts are recorded but their status is not downgraded. **Fed back into the prose**: the C1 opening now reads as an occupational scenario instead of an “inevitable result” and links to J-072; 39 sections across 10-near / 20-mid / 30-far / chains carry a visible downgrade marker (39 per language, section-for-section symmetric); O-001–O-004 and the window list in 40-opportunities each carry an upstream-downgrade note; both READMEs correct the false claim that the chains and time layers cover the same judgments (measured overlap is only 9; 14 chain-only, 39 time-layer-only, 10 in neither) and state that all 12 far-term cards (J-043–J-054) carry confidence “Low (landscape only).” **Cost recorded honestly**: every audience-scale magnitude is a constructed estimate, not citable occupational statistics, and can be attacked; this is the only weak-evidence source added this round, as weak and from the same source as the section-7 estimate for the C1 opening. **Three clarifications added after the 2026-09-20 review**: (1) **why hundred-million-scale plus weekly frequency still fails Gate 1 (audience scale)** — the figures on all 18 hundred-million-scale cards (J-017, J-018, J-020, J-022, J-023, J-025, J-026, J-030, J-036, J-037, J-038, J-041, J-045, J-047, J-048, J-049, J-050, J-061) are constructed upper bounds on the audience (estimated from occupational roles, organizational nodes, or a population in need), not citable statistics, and not one of them establishes the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 fails on every one of them. The 10 whose audience is written as possible users, platform participants, or an affected population (J-017, J-020, J-022, J-023, J-030, J-036, J-041, J-047, J-048, J-061) additionally record that **an estimate of reach is not a count of people repeating the action**. None of these 18 verdicts is upgraded merely because the number itself is larger. (2) **Self-attack on this test** — the threshold line itself (“a hundred million distinct individuals performing the same action every week”) has been calibrated against no external literature at all (see section 8 of the historical retrospective: Gate 1 is a genuine gap in the literature); and “pick one out of a large pile of candidates” is something e-commerce recommendation has done for a billion people daily for years, which shows the scale test can both mistake an activity that was automated long ago for new scarcity and, by counting only “the same action,” miss one force spread across several actions. The way to overturn this test is citable occupational or behavioural statistics, not a larger adjective. (3) **61 and 60 are not the same number** — 60 cards were newly set to `REVISED` this round; adding J-004, which was already `REVISED` on 2026-09-19 for a different reason and received only a diffusion-gate narrowing note this round, **61 cards currently carry a diffusion-gate narrowing note**. The two numbers must not be swapped where the READMEs or the prose cite them | — |
| 2026-09-20 | The C4 chain's six judgments formally registered as J-073–J-078 (both languages) | The six judgments in the prose of the [C4 chain](chains/40-embodied-intelligence.md) are now registered as cards: **J-073, the core judgment** — embodied intelligence is the **necessary complement** for AI to reach the physical-labour population, not a **sufficient condition** for diffusion (changing the denominator only opens Gate 1; Gates 2 through 5 do not open automatically as model capability improves); **J-074–J-078** are the five squares — care, warehousing and logistics, manufacturing and assembly, agriculture, and construction / domestic work. The six cards entered **section 2's overview, section 3's complete graph, and the C4 card area** in step, with the dependency edges identical in all three places (J-073 ← J-006, J-066–J-071; J-074–J-078 ← J-073, J-066), and the complete graph's coverage statement changed from J-001–J-072 to **J-001–J-078**. **Every card is registered against Gate 1's two questions**: an audience-scale magnitude (J-073 billion-scale, J-074–J-078 hundred-million-scale, all judged **FAIL on Gate 1** under the 2026-09-20 review's definitions, and all written as occupational/organizational judgments from the start, so no downgrade is at issue), and the "raises the ceiling of existing professionals / lets people who previously could not do it do it" verdict — all six fall in the former, and the only two that could have fallen in the latter (home contact transfer, open-ended household tasks) are both judged not to hold inside this window. Each card's reasoning chain states **when cost per task crosses labour** and its **hard constraints** (inside the five-category whitelist). Seven sources were added as EXT-41–EXT-47 (FAO employment indicators, ILO domestic workers, O\*NET 53-7062 / 31-1121, Riken ROBEAR, IFR, The Robot Report [⚠ a single company case], FBR Hadrian [⚠ vendor self-description]), and all six cards completed the three-element comparison. **Costs recorded honestly**: (1) all six audience-scale magnitudes are constructed estimates rather than citable statistics; (2) the four data series that matter most to this chain had no publicly checkable definition this round (cost-per-task time series by scene, insurance rates and liability rulings for embodied work, the learning curve of deployment hours per unit, and deployment scale and retention in care worldwide), so confidence stays at Medium across the board; (3) **this round changed both bilingual READMEs and both bilingual ledgers**: the README card count now agrees with J-073–J-078 at 78, and the README coverage wording for collaboration between people and relationships between people and AI now agrees with the ledger; the ledger restores and explicitly retains the uncovered gap for the social consequences of the technology capability sequence. The chain prose and other sections were left untouched by this round | — |
| 2026-09-21 | C5 biology/medicine and C6 education/skill formation delivered bilingually (J-079–J-086) | Added two chains and eight cards; registered EXT-48–EXT-54; changed both gaps to “covered with evidence gaps retained.” All eight cards entered the overview, dependency graph, and card section; both Gate 1 questions are recorded per card; J-082 and J-086 are explicitly low-confidence landscape only. **Cost recorded honestly**: all eight audience magnitudes are constructed reach/occupational estimates rather than citable statistics for the same repeated action, so all fail Gate 1; education lacks cross-national long-term randomized trials and credential-recognition series, while medicine lacks cross-national deployment and long-term outcome series. | af13853 |
| 2026-09-21 | C7 social consequences of capability sequence delivered bilingually (J-087–J-091) | Added a five-stage transmission chain across organizations, labour, institutions, capital, and demand. Every card treats capability as a trigger rather than the sole engine and registers audience scale, dependencies, external comparison, falsifier, and data gaps; the corresponding high-priority gap is now covered. | — |
| 2026-09-21 | `REVISED` due-calibration semantics repaired (both languages) | Due sets now come from preregistered time windows, falsifiers, and review dates rather than status labels; the 60 scope-downgraded `REVISED` cards remain independently due and in the denominator, while J-004 is explicitly reviewed together with successor J-065; uncomputable preregistered checks are recorded as `INDETERMINATE` and remain in the denominator. The methodology and contribution guide now use the same two-case definition. | 4a111a0 / follow-up revision |

---


## 9. External-comparison sources for this round

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
- **EXT-19**: Lawrence Berkeley National Laboratory, *Queued Up: 2026 Edition* (characteristics of plants seeking interconnection as of end-2025), **sections: queue size / time from interconnection request to commercial operation**; supports grid interconnection being a slow variable — the generation and storage queue is very large and the median time from request to commercial operation exceeded five years for projects completed in 2025; **does not support** any conclusion about load-side (data-centre) queues, which the report does not cover, nor this project's time window. <https://emp.lbl.gov/queues>
- **EXT-20**: U.S. BIS, *Regulatory Framework for the Responsible Diffusion of Advanced Artificial Intelligence Technology* (January 2025), **topics: advanced computing chip controls / controls on closed model weights (10^26 operations threshold) / Data Center Validated End User authorization (UVEU and NVEU) and security conditions**; supports control having moved beyond the chip as a physical object to model weights and data-centre operator authorization; **does not support** the existence of a standalone cloud or remote-access licensing regime (the framework manages foreign access through site authorization and country allocations), nor this project's time window or assumed enforcement intensity for use-side duties. <https://www.bis.gov/press-release/biden-harris-administration-announces-regulatory-framework-responsible-diffusion-advanced-artificial>

- **EXT-21**: U.S. FERC, *PJM Interconnection, L.L.C.*, 193 FERC ¶ 61,217 (18 December 2025), **sections: three tiers of transmission service for co-located load — interim non-firm, firm contract demand (minimum one-year committed capacity), non-firm contract demand — plus unreserved use charges for over-withdrawal**; supports the claim that large-load contracts are tiered by commitment level and term rather than by per-kilowatt-hour price; **does not support** any transaction price or damages figure, applies to PJM only, and is rulemaking rather than transaction statistics. <https://www.ferc.gov/news-events/news/ferc-directs-nations-largest-grid-operator-create-new-rules-embrace-innovation-and>
- **EXT-22**: Public Utilities Commission of Ohio (PUCO), AEP Ohio data-centre tariff settlement (Case No. 24-508-EL-ATA, approved 9 July 2025), **terms: new data centres above 25 MW must pay for at least 85% of subscribed capacity, contract terms up to 12 years, a 4-year ramp, early-termination exit fees and collateral**; supports that regulators have separated large load into its own class, built price protection around whether commitments are honoured, and did so to shield residential ratepayers; **does not support** cross-state generality (AEP Ohio territory only), contains no delay-damages formula for missed delivery dates, and includes no after-the-fact assessment of residential bill impact. <https://puco.ohio.gov/news/puco-orders-aep-ohio-to-create-data-center-specific-tariff>
- **EXT-23**: Nicholas Institute, Duke University, *Rethinking Load Growth: Assessing the Potential for Integration of Large Flexible Loads in US Power Systems* (February 2025), **sections: curtailment modelling across the 22 largest balancing areas and the curtailment-duration tables**; supports the technical potential that if new large loads accept 0.25–1.0% annual curtailment (averaging 1.7–2.5 hours per event), the US could host nearly 100 GW of additional load; **does not support** any contracted capacity, and models large flexible loads generically (electrolysers, charging, and others) rather than AI training and inference specifically. <https://nicholasinstitute.duke.edu/publications/rethinking-load-growth>
- **EXT-24**: EPRI, DCFlex initiative field demonstration in Phoenix (with Emerald AI, 2025), **result: an AI compute cluster reduced power draw by 25% through a three-hour grid peak event without affecting core services**; supports the measured feasibility of the mechanism that part of AI load is pausable, deferrable and shiftable; **does not support** any conclusion about scale — a single pilot with a very small sample, and EPRI states explicitly that data centres cannot simply be cut like traditional interruptible load. <https://dcflex.epri.com/>
- **EXT-25**: PJM Monitoring Analytics, *2024 State of the Market Report for PJM*, **Section 6 Demand Response: cleared demand-response capacity (UCAP) of about 8,064.7 MW**; supports that demand response has reached contracted scale at the largest US grid operator; **does not support** any answer about data centres themselves — the figure is an all-sector total mixing industrial, commercial and residential load, with no industry breakdown. <https://www.monitoringanalytics.com/reports/PJM_State_of_the_Market/2024/2024-som-pjm-sec6.pdf>
- **EXT-26**: Lawrence Berkeley National Laboratory / DOE, *2024 United States Data Center Energy Usage Report* (December 2024), **sections: Executive Summary key findings and the 2014–2028 historical/projected data tables**; supports that US data-centre electricity rose from about 4.4% of national consumption in 2023 toward 6.7–12% by 2028, meaning recent load growth has outpaced what efficiency gains offset; **does not support** a global reading (US only), and the 2028 range is wide and scenario-dependent. <https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf>
- **EXT-27**: Masanet, Shehabi, Koomey et al., *Recalibrating global data center energy-use estimates*, *Science* (February 2020, peer-reviewed), **body text and figures: global data-centre compute instances versus energy use, 2010–2018**; supports the historical precedent that efficiency once outran load growth for eight years (compute instances up 550%, energy up only about 6%); **does not support** extrapolation past 2019 into the large-model era, and the paper itself makes no prediction about whether decoupling continues. <https://www.science.org/doi/10.1126/science.aba3758>
- **EXT-28**: Virginia Joint Legislative Audit and Review Commission (JLARC), *Data Centers in Virginia* (Report 598, December 2024), **sections: the sales and use tax exemption (about $928 million of state revenue forgone in FY23, claimed by roughly 90% of the industry), local property tax as the main retained revenue, the construction-phase share of jobs in the economic-impact figures, and grid capacity constraints in Northern Virginia**; supports both the mechanism that immovable heavy assets are taxable while local retention rests on property tax with jobs concentrated in construction, and the finding that the largest cluster is development-constrained by substation and transmission capacity; **does not support** national generalization (Virginia only) and gives no permanent-jobs-per-dollar ratio. <https://jlarc.virginia.gov/pdfs/reports/Rpt598.pdf>
- **EXT-29**: U.S. Department of Energy, *Recommendations on Powering Artificial Intelligence and Data Center Infrastructure* (30 July 2024), **sections: connection requests for hyperscale facilities of 300–1000 MW+ with 1–3 year lead times, and co-location with existing generation to obtain power faster**; supports the mechanism that access speed rather than electricity price drives siting and sourcing; **does not support** any quantitative conclusion — it is an advisory, descriptive document with no correlation test between siting and price or queue length. <https://www.energy.gov/sites/default/files/2024-08/Powering%20AI%20and%20Data%20Center%20Infrastructure%20Recommendations%20July%202024.pdf>
- **EXT-30**: ERCOT, *Large Load Interconnection (LLI) Status & Analytics Update* (monthly), **charts: MW with planning studies approved versus MW approved to energize**; supports a persistent and growing backlog in large-load interconnection, and is currently the **only** public ISO-level queue data specifically covering the load side rather than generation; **does not support** cross-market comparison (Texas only), counts queued requests rather than built capacity, and carries no electricity-price variable for comparison. <https://www.ercot.com/gridinfo/planning>
- **EXT-31**: Good Jobs First, *Most States Fail to Disclose which Data Center Companies Get Huge Tax Breaks* (2024) and *2023: A Year of Megadeals in Review* (2024), **statistics: 36 states offer data-centre-specific tax breaks while only 11 disclose the recipient companies; subsidy per job in tracked megadeals averages over $262,000**; supports the argument that investment is large while jobs are few and incentive transparency is low; **⚠ this is a subsidy-watchdog advocacy organization rather than a government body**, its sample is the megadeals it tracks itself, and 14 states are missing from the data, so it must not be read as a full-sample statistic. <https://goodjobsfirst.org/most-states-fail-to-disclose-which-data-center-companies-get-huge-tax-breaks/>
- **EXT-32**: Georgia Public Service Commission, large-load billing rules (approved 23 January 2025) and *Data Center Fact Sheet*, **content: risk-priced minimum-billing requirements and longer contract terms for loads above 100 MW**; supports a second jurisdiction independently separating large load into its own class to prevent cost shifting onto residential customers; **does not support** any effect assessment — it is a rule document and does not quantify the actual impact on residential bills. <https://psc.ga.gov/site/downloads/datacenterfactsheet.pdf>
- **EXT-33**: Everett Rogers, *Diffusion of Innovations* (first edition 1962), **subject: the five attributes of an innovation — relative advantage, compatibility, complexity, trialability, observability**; supports the overlap between this document's Gate 2 and relative advantage, and between Gate 5 and complexity, as well as the tradition of explaining diffusion speed by attributes of the innovation itself; **does not support** the veto-style reading used here (Rogers's five attributes are scored — higher means faster — not "fail one and the answer is no"), and offers no prior screening variable of the form "how many people perform the activity, and how often." <https://en.wikipedia.org/wiki/Diffusion_of_innovations>
- **EXT-34**: Paul David, *Clio and the Economics of QWERTY* (1985) and Katz & Shapiro, *Network Externalities, Competition, and Compatibility* (1985), **subject: path dependence and network externalities**; supports the claim that adoption is not decided by technical merit alone, and the mechanism by which the value of adopting depends on whether others adopt too — which is what sharpens Gates 4 and 5; **does not support** this document's three-way split of unlock conditions (enforceable and observable authority / a single subsidizing party / a local closed loop), which is induced here from cases rather than taken from either paper. <https://en.wikipedia.org/wiki/Path_dependence>
- **EXT-35**: Geoffrey Moore, *Crossing the Chasm* (1991), **subject: the discontinuity between early adopters and the early majority**; supports the existence of this document's premise that technical success is not the same as crossing into a mass market; **does not support** the five gates — Moore offers a market-entry strategy (pick a beachhead, build the whole product), not a screen for whether a capability can reach society-wide scale. <https://en.wikipedia.org/wiki/Crossing_the_Chasm>
- **EXT-36**: Mancur Olson, *The Logic of Collective Action* (1965), **subject: rational self-interested individuals do not automatically act for a common interest unless the group is small or coercion and selective incentives exist**; supports the core mechanism of Gate 4 and the theoretical origin of its three unlock paths (coercion → (a), selective incentives → (b) a single subsidizing party, small groups → (c) a local closed loop); **does not support** this document's emphasis on the half-clause that enforcement must be observable — that half comes from Prohibition and the US metrication attempt, not from Olson. <https://en.wikipedia.org/wiki/The_Logic_of_Collective_Action>
- **EXT-37**: David Teece, *Profiting from Technological Innovation* (1986) on complementary assets, and Jonathan Zittrain, *The Generative Internet* (2006) on generativity, **subject: the complementary assets innovation profit depends on, and why general-purpose platforms can carry unanticipated applications**; supports the claim that the notion of a "carrier" has neighbours in the literature; **does not support** treating either as equivalent to Gate 3 — they answer who captures value from an innovation and why general platforms grow new applications, whereas Gate 3 asks a prior existence question: will this dedicated infrastructure be built at all. <https://en.wikipedia.org/wiki/David_Teece>
- **EXT-38**: Frank Bass, *A New Product Growth for Model Consumer Durables* (1969), **subject: the shape of an adoption curve characterized by coefficients of innovation and imitation**; supports the claim that diffusion has a modellable temporal form; **does not support** Gate 1 — the Bass model treats market potential m as an **exogenously given parameter** and never asks how many people perform the activity, which is precisely the quantity Gate 1 asks about. <https://en.wikipedia.org/wiki/Bass_diffusion_model>
- **EXT-39**: U.S. CDC, contact-lens wear and care series (MMWR 2015 *Contact Lens Wearer Demographics and Risk Behaviors*, MMWR 2016 *Contact Lens–Related Corneal Infections*, and CDC care guidance), **data: 16.7% of U.S. adults wore contact lenses in 2014 (40.9 million, self-report); about 45 million people of all ages in 2016; about one million all-cause keratitis outpatient and emergency visits per year and about $175 million in direct medical costs in 2010; guidance requires washing and drying hands before every insertion or removal, removing lenses before sleep, showering or swimming, and keeping lenses away from water**; supports the Gate 5 exclusive case and its ceiling magnitude; **does not support** the stronger claim that adoption has stalled, nor provide the share of vision-correction users wearing contacts (CDC combines glasses and contacts in NHIS); <https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6432a2.htm>
- **EXT-40**: World Health Organization, *Blindness and visual impairment* fact sheet, **data: at least 2.2 billion people have near or distance vision impairment; about 1 billion have an unmet need, including 826 million with presbyopia and 88.4 million with uncorrected refractive error**; supports the billion-scale daily activity of vision correction; **does not support** using this as the denominator of people already wearing corrective lenses, so this document does not calculate that ratio; <https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment>

- **EXT-41**: Food and Agriculture Organization of the United Nations (FAO), *Employment indicators 2000–2023* (July 2025 update), **subject: the size of agricultural employment and its share across income groups**; supports the **order of magnitude** that agricultural employment worldwide is still in the **hundreds of millions** with a markedly higher share in low- and middle-income countries, and supports the claim that most of the potential object of agricultural embodiment is not on capital-intensive farms in high-wage countries; **does not support** any precise global figure (definitions, years and statistical boundaries are as given in the source), nor any automatable share broken down by operation type. <https://www.fao.org/statistics/highlights-archive/highlights-detail/employment-indicators-2000-2023-%28july-2025-update%29/en>
- **EXT-42**: International Labour Organization (ILO), *Domestic workers* topic page, **subject: domestic workers as a separately counted group and the informal share among them**; supports domestic workers being a group in the **tens of millions**, a large part of it informally employed, and therefore that domestic demand is real and already being paid for; **does not support** treating that headcount as an addressable market for home robots, nor any conclusion about the automatable share of domestic tasks. <https://www.ilo.org/topics-and-sectors/domestic-workers>
- **EXT-43**: U.S. O\*NET occupational data, **53-7062 "Laborers and Freight, Stock, and Material Movers, Hand"** and **31-1121 "Home Health Aides"**, **content: occupation size and outlook (the latter listed among the fastest-growing)**; supports the existence proof that these physical activities really do exist at **millions scale** with an official definition to cite, and supports using headcount and wages as a leading indicator in adoption-dense regions; **does not support** extrapolation to the world (United States only), nor any conclusion about machine substitution rates. <https://www.onetonline.org/link/localtrends/53-7062.00>; <https://www.onetonline.org/link/localtrends/31-1121.00>
- **EXT-44**: Riken (Japan), ROBEAR transfer-robot prototype (released 2015-02-23), **content: a force-controlled prototype demonstration of lifting and transferring a care recipient**; supports the **capability-side** feasibility of contact transfer having been demonstrated a decade ago, so that "still not standard ward equipment a decade later" cannot be explained by capability; **does not support** any conclusion about deployment scale, retention, or a production successor — no checkable source was found this round. <https://www.riken.jp/en/news_pubs/research_news/pr/2015/20150223_2/>
- **EXT-45**: International Federation of Robotics (IFR), *Global robot demand in factories doubles over 10 years*, **content: a ten-year view of factory robot demand**; supports that embodied capability **can** genuinely diffuse, and draws the boundary conditions under which that diffusion happened (repetitive motion, rigid workpieces, calibratable positions, fixed takt); **does not support** any breakdown of new installations by application type (a total cannot separate palletizing growth from an assembly breakthrough), nor extrapolating the factory's diffusion rate to care, agriculture, construction and homes. <https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years>
- **EXT-46**: The Robot Report, *Abundant Robotics shuts down fruit harvesting business*, **content: an apple-harvesting robot company shutting the business down after the technology worked in orchards**; supports "technical feasibility is not commercial feasibility" and serves as the concrete specimen on the failure side of selective harvesting; **⚠ a single company case**, not a statistic over the class, and the shutdown may be jointly driven by funding and management reasons, so it must not be read as proof that harvesting is technically infeasible. <https://www.therobotreport.com/abundant-robotics-shuts-down-fruit-harvesting-business/>
- **EXT-47**: FBR, Hadrian bricklaying machine product page, **content: a decade-scale push in this direction and the stage it currently sits at (single operation and demonstration projects)**; supports "what blocks on-site construction is not laying speed but trade sequencing, inspection, permits and weather"; **⚠ vendor self-description**, not an independent assessment, and supports no conclusion about cost, schedule or deployment scale. <https://www.fbr.com.au/view/hadrian>
- **EXT-48**: U.S. FDA, *AI-enabled Medical Devices*, **topic: FDA-authorized AI medical-device list, market pathways, and decision dates (accessed 2026-09-21)**; supports that AI medical devices have received market authorization through multiple pathways and that intended use and decision dates are traceable; **does not support** exhaustive coverage, clinical adoption scale, complete identification of foundation models, or widespread autonomous care. <https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices>
- **EXT-49**: U.S. FDA, *Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products*, **topic: Context of Use, risk, and the model-credibility framework**; supports establishing credibility according to Context of Use and risk; **does not support** a particular acceleration magnitude, success rate, or this chain's windows. <https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological>
- **EXT-50**: WHO, *Ethics and governance of artificial intelligence for health* (the same source as EXT-9), **topic: six ethical principles and autonomy, transparency, accountability, equity, and safety in governance**; supports these boundaries not being automatically erased by model capability; **does not support** a particular regulatory endpoint or adoption order. <https://www.who.int/publications/i/item/9789240029200>
- **EXT-51**: WHO, *Health workforce*, **topic: health-worker supply, occupational categories, and geographic-distribution constraints**; supports health-worker supply and geographic distribution as real capacity constraints; **does not support** converting workforce shortages into an AI market or automation share. <https://www.who.int/news-room/fact-sheets/detail/health-workforce>
- **EXT-52**: UNESCO, *Guidance for generative AI in education and research*, **topic: human-centred design, age appropriateness, privacy, teacher involvement, and pedagogy**; supports these boundaries for educational use; **does not support** a specific learning effect, teacher replacement, or assessment endpoint. <https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research>
- **EXT-53**: OECD, *Digital Education Outlook 2023*, **topic: digital-education governance, interoperable ecosystems, and teacher capacity**; supports digital education depending on these institutional capabilities rather than one tool; **does not support** a generative-AI adoption order or permanent school boundaries. <https://www.oecd.org/en/publications/oecd-digital-education-outlook-2023_c74f03de-en.html>
- **EXT-54**: World Bank, *What is Learning Poverty?*, **topic: definition and global scale of foundational learning deficits**; supports foundational learning deficits as a billion-scale education-system problem; **does not support** attributing the deficit to scarcity of explanation or predicting AI's direction of effect on inequality. <https://www.worldbank.org/en/topic/education/brief/what-is-learning-poverty>
- **EXT-55**: Clarence Saunders, US patent *Self-Serving Store* (US1242872A), **mechanism: customers select goods themselves, traverse a continuous path, and settle at the exit, reducing clerks and overhead**; supports transfer of recurring picking labor to shoppers and the need to compare net rather than gross friction; **does not support** the inventor's sales claims or protocol `S` scale. <https://patents.google.com/patent/US1242872A/en>
- **EXT-56**: US NHTSA, *Seat Belt Use in 2024—Overall Results*, **data: 91.2% observed national use, scoped to daytime front-seat outboard occupants**; supports recurring bodily friction reaching high adoption under law and enforcement; **does not support** all occupants / all hours or law-only causality. <https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813799>
- **EXT-57**: Google, *A message on Stadia and our long term streaming strategy* (2022-09-29), **facts: Google called the technology proven at scale and strong, yet ended service on 2023-01-18 because user traction missed expectations**; supports technical usability not guaranteeing adoption; **does not support** any specific pricing, library, or competition cause. <https://blog.google/products-and-platforms/products/stadia/message-on-stadia-streaming-strategy/>
- **EXT-58**: US Congressional Research Service, *Daylight Saving Time: Background and Legislation*, **chronology: emergency year-round DST began 1974-01-06, was rolled back early, and standard time returned 1974-10-27**; supports compulsory launch not guaranteeing retention; **does not support** one causal account of public opposition. <https://www.congress.gov/crs-product/R45208>
- **EXT-59**: Reserve Bank of India, Annual Report 2017–18 Chapter V, **fact: the 2016 withdrawal of specified banknotes created surplus banking-system liquidity**; retained only as a mechanism probe; **does not support** an exact return share or success/failure coding because this page contains neither. <https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1232>
- **EXT-60**: International Labour Organization (ILO), *Generative AI and Jobs: A Refined Global Index of Occupational Exposure* (Working Paper 140, 20 May 2025), **topic: global occupational-exposure gradients built from 29,753 tasks, and the boundary between task transformation and whole-job replacement**; supports that about one in four workers are in occupations with some GenAI exposure and that task transformation is more likely than whole-job replacement for most occupations; **does not support** claims about junior seats, apprenticeship carriers, demand elasticity, or net employment, and the exposure index must be linked with national microdata for more specific projections. <https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure>
- **EXT-61**: Brynjolfsson, Rock, and Syverson, *The Productivity J-Curve: How Intangibles Complement General Purpose Technologies* (NBER Working Paper 25148, 2018; revised 2020; published 2021), **topic: general-purpose technologies requiring complementary intangible investment in business processes, products, business models, and human capital before measured productivity gains arrive**; supports organizational co-invention and fixed redesign cost after core capability arrives; **does not support** who captures AI gains, the duration of concentration, or this chain's time window. <https://www.nber.org/papers/w25148>

> **Second historical calibration round closed (2026-09-21)**: EXT-55 through EXT-59 were added. All four known-outcome cases are labelled `CALIBRATION` and may enter neither the holdout nor an accuracy denominator. Piggly Wiggly self-service retail narrows J-071 in place from “any recurring gross friction” to “recurring net burden relative to the real incumbent”; seat belts only confirm the compulsion bypass; Stadia and US year-round DST only add sufficiency counterexamples that strengthen J-066 without changing a necessary gate. India demonetization remains a mechanism probe because no single target activity was preregistered and the authoritative page used here lacks the exact return share. The rule-change feedback surface is `00-method.md`, `01-retrospect.md`, `02-historical-validation-protocol.md`, and J-066 / J-071; old holdouts may not validate the new version, which triggers the downstream isolated full re-review under the protocol.

> **C3 comparison round closed (19 September 2026)**: EXT-21 through EXT-32 were added here. All nine cards J-056–J-064 have now completed their first external comparison, and no ACTIVE judgment in this ledger is still marked "unknown / comparison not completed" (**this clause went void the same day**: the later O-002 opportunity-durability review added J-065, which is a product of that re-review, has not been compared yet, and is marked "unknown" per the methodology until the next round). The added comparison surfaced three cases where the **falsifier is currently not computable**, each written into the card itself rather than hidden: J-057 (large-load contract terms are commercially confidential and no public statistics on terms exist), J-058 (no statistics on contracted data-centre demand-response capacity broken out by industry), and J-063 (no public data comparing the explanatory power of electricity price versus interconnection wait time for siting). One **frequently misused source is also corrected**: EXT-19 (LBNL *Queued Up*) covers generation and storage interconnection queues only and **does not cover the load side**, so it must not be used as evidence about data-centre siting or large-load queues.

> **C4 comparison round closed (20 September 2026)**: EXT-41 through EXT-47 were added here, and all six cards J-073–J-078 completed their first external comparison with the three elements present, so this registration adds no judgment marked "unknown / comparison not completed." **The evidential strength of this batch must be read honestly**: only EXT-45 (IFR) is an industry-level statistic; EXT-41, EXT-42 and EXT-43 are **order-of-magnitude** and existence evidence (O\*NET covers the United States only); EXT-44, EXT-46 and EXT-47 are **a single prototype or a single company case**, with EXT-46's shutdown possibly driven jointly by funding and management reasons and EXT-47 being vendor self-description. The four data series that matter most to this chain were **all unavailable this round**, and each is written into the cards rather than hidden: (1) cost-per-task time series by scene; (2) insurance rates and liability rulings for embodied work; (3) the learning curve of deployment hours per unit; (4) deployment scale and retention in care worldwide. Confidence for J-073–J-078 therefore stays at Medium across the board, and none of these cards may be cited as grounds for "embodied intelligence is about to diffuse."

## 10. Judgment cards for technology and cross-domain chains

These judgments support the capability order in `05-tech-sequence.md`. Each preserves the five-part test and strongest opposing mechanism; the arrival of a capability is not the same as universal adoption.

### J-001 · Unit reasoning cost keeps falling

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The unit cost of reasoning at equal capability falls another order of magnitude by the end of 2029.
- **Diffusion-gate review**: audience scale = million-scale (model developers, cloud providers, and organizational buyers), a technical precondition, not a daily society-wide action; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Reasoning is parallelizable deterministic computation → cumulative production and engineering optimization create a learning curve → hardware efficiency, model efficiency, and scheduling/reuse provide relatively independent cost-decline paths → equal capability can be called more frequently.
- **Time window**: 2026-01 to 2029-12.
- **Falsifier**: For 18 consecutive months, the lowest public unit price for equal capability rises rather than falls, and the rise cannot be explained by temporary demand congestion or a one-off energy shock.
- **Leading indicator**: Lowest public price for a fixed benchmark score, energy per unit of compute, and months for open models to catch the strongest closed model at the time; observe twice yearly.
- **Confidence**: High.
- **depends-on**: —.
- **Strongest opposing mechanism**: Energy, chip supply, or regulation creates a common hard ceiling that disables all three decline paths; if the falsifier triggers, withdraw this judgment and its downstream cost premise.
- **Against consensus**: Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude. Retained: the three decline channels (hardware efficiency, model efficiency, scheduling reuse) are relatively independent, and the sources simply do not measure the specific multiple rather than contradicting it; the magnitude risk is carried by the falsification condition on lowest public unit price.
- **External comparison source**: EXT-1 (see the source index above).
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-002 · “Selecting objectively high quality from abundant output” is not a durable scarcity, but merely a 2–4 year window

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Selecting objectively high quality from abundant output is not a durable scarcity; it is merely a 2–4 year window.
- **Diffusion-gate review**: audience scale = million-scale (knowledge workers and organizational buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L1 (opportunity-durability gate)
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-03-31.

### J-003 · The genuinely durable scarcity is ownership of “private context about you” and its usable form

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The genuinely durable scarcity is ownership of private context about you and its usable form.
- **Diffusion-gate review**: audience scale = million-scale (professional individuals and organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (the bottleneck jumps from production capacity to choice) + L1 (opportunity-durability gate)
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-004 · As AI shifts from “generating content” to “executing actions,” the scarce item is infrastructure that “makes actions reversible”

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As AI shifts from generating content to executing actions, the scarce item is infrastructure that makes actions reversible.
- **Diffusion-gate review**: audience scale = million-scale (organizations deploying AI and high-liability professionals), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L6 (irreversibility) + L1 (opportunity-durability gate).
- **Reasoning chain**: Generation becomes cheap → trial-and-error strategies spread → but trial and error presupposes reversible outcomes → AI begins touching irreversible actions (payments, deployment, sending, signing) → irreversibility exposes physical and legal/liability constraints that will not disappear as models improve → “reversibilization” becomes a prerequisite for using AI rather than an option
- **Time window**: Demand becomes explicit from 2027 and becomes standard before 2032
- **Falsifier**: By 2031, mainstream practice still lets AI directly execute irreversible actions in production environments/real accounts, and the incident rate is low enough that no one demands an isolation layer
- **Leading indicator**: ① Whether enterprise procurement lists begin to include standalone items such as “AI action sandboxes / shadow environments / rollback”; ② whether insurers begin pricing “AI autonomous action”; ③ the public frequency of major AI execution incidents
- **Confidence**: Medium
- **Strongest opposing mechanism**: Human approval of each item may replace sandboxes and rollback cheaply. If high-value deployments still rely on item-by-item approval by 2030 and show no separate environment procurement, withdraw the independent-infrastructure judgment.
- **External comparison note**: The comparison is “partly consistent”; the reason to hold the category judgment is that irreversibility, liability, and expected accident loss can turn isolation from a habit into a procurement condition.
- **depends-on**: J-001
- **Against consensus**: Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified. Retained: irreversible actions trigger physical and legal/liability constraints that do not dissolve as models improve; the independent scarcity of reversible infrastructure is unconfirmed externally, so confidence stays Medium rather than rising.
- **External comparison source**: EXT-2, EXT-4 (see the source index above).
- **Status**: `REVISED` — the opportunity-durability review of 2026-09-19 found that this card treated “reversible infrastructure” as a single scarce item without ever answering why the same force that makes generation abundant cannot copy it; it has been narrowed and superseded by [J-065](#j-065--once-ai-executes-across-ownership-boundaries-the-scarce-item-is-not-rollback-software-but-the-right-to-reverse). Per the section-1 rule the card is kept verbatim, its ID is not reused, and it is no longer a basis for any opportunity candidate.
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: no longer reviewed on its own; reviewed together with [J-065](#j-065--once-ai-executes-across-ownership-boundaries-the-scarce-item-is-not-rollback-software-but-the-right-to-reverse).

### J-065 · Once AI executes across ownership boundaries, the scarce item is not rollback software but the right to reverse

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: What is scarce is not sandbox and rollback software but the right to pull state back out of the counterparty’s ledger.
- **Diffusion-gate review**: audience scale = ten-million-scale (organizations in cross-party payment, logistics, contracting, and settlement), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L1 (opportunity-durability gate’s third question) + L2 (constraint migration).
- **Reasoning chain**: [J-004](#j-004--as-ai-shifts-from-generating-content-to-executing-actions-the-scarce-item-is-infrastructure-that-makes-actions-reversible) treated “reversible infrastructure” as one scarce item → taken apart layer by layer under opportunity-durability gate’s third question → when the action does not cross an ownership boundary (your own database, your own cloud resources, a test sandbox), rollback is pure software, exactly what the force making generation abundant is best at producing, and the system being operated on is held by the platform itself, which has every incentive to bundle it and give it away → that half has payers but fails the opportunity-durability gate, so its exit is a window opportunity → when the action does cross an ownership boundary (payment, shipping, signing, transfer of rights), the state lands in the counterparty’s ledger and in legal rights the counterparty has acquired, so reversal must be consented to and executed by that party → whose default interest is finality: what it sells is finality, and reversal capacity is rationed and separately priced (dispute fees, escrow fees, issuance fees) → historically, cross-party unwind has actually been built only inside a handful of closed networks (card-scheme chargebacks, securities settlement reversal, escrow and letters of credit), each a product of membership rules, collateral, and long-running repeated games → compute can copy sandbox code without limit; it cannot copy the counterparty’s obligation to unwind → the hard constraint therefore lands on ownership/privacy and trust/relationship, not on irreversibility (which is only a supporting lens) → for physically irreversible actions (consumed, harmed, injected) no reversibility product exists at all and the residue belongs to the compensating party, see [J-005](#j-005--after-generation-becomes-abundant-value-concentrates-in-three-kinds-of-non-recombinable-input-raw-signals-accountable-commitments-and-validated-causality)
- **Time window**: 2027–2033, as demand becomes explicit with the volume of cross-party agent execution
- **Falsifier**: By 2033, cross-party reversal for machine-initiated actions (delayed-finality settlement, programmable escrow, unilateral rescission windows) has become a default rule of the major payment and settlement networks, is not priced separately, and the access layer has produced no identifiable independent supplier
- **Leading indicator**: ① Whether programmable escrow / delayed-finality settlement products aimed at agents appear and are separately priced; ② whether chargeback and dispute windows are extended to machine-initiated transactions; ③ whether contract templates begin to carry a “unilateral rescission window for AI-executed clauses”; ④ whether platforms bundle within-boundary sandbox / rollback as a default capability (that one turning true only confirms that the Window List row has closed and is not evidence for this judgment); observed every six months
- **Confidence**: Medium
- **Strongest opposing mechanism**: Two, and each severs the chain on its own. First, the holders of the reversal right internalize it — payment and settlement networks, or regulators, mandate a uniform reversal window for machine actions and give it away, leaving the access layer nothing to do. Second, buyers do not want reversibility — delayed finality ties up capital, and if that cost of capital exceeds the expected loss from accidents, organizations will rationally choose “irreversible plus compensate afterwards,” and demand flows to the commitment layer of [J-005](#j-005--after-generation-becomes-abundant-value-concentrates-in-three-kinds-of-non-recombinable-input-raw-signals-accountable-commitments-and-validated-causality) rather than to this one.
- **Against consensus**: Comparison not completed this round: unknown. This judgment was produced on the spot by the opportunity-durability review of 2026-09-19 and has not yet been compared against any external judgment; it is explicitly marked unknown per `00-method.md` §1.1 item 4, must not be used as if compared, and the three elements will be completed in the next round.
- **External comparison source**: Comparison not completed this round.
- **depends-on**: J-001
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-005 · After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality.
- **Diffusion-gate review**: audience scale = million-scale (high-liability professionals and organizations in medicine, engineering, and compliance), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L1 (abundance → scarcity) + L2 (constraint migration).
- **Reasoning chain**: Generation = recombination of existing patterns → what cannot be obtained through recombination will not become abundant → supply-and-demand law: what complements abundant goods without becoming abundant in parallel appreciates → the three kinds of input are respectively protected by the hard constraints of physical presence, legal liability, and experimental intervention
- **Time window**: Clearly visible in pricing during 2029–2033
- **Falsifier**: Reliable synthetic data/simulation-based reasoning systematically replaces real experiments in fields requiring new observations (such as new drugs and new materials), and regulators accept it
- **Leading indicator**: ① Price trends for licensing first-party data (sensors, field sites, proprietary workflows); ② whether AI services with compensation commitments appear and command a premium; ③ the share of experiments and pilot production in R&D budgets
- **Confidence**: Medium
- **Strongest opposing mechanism**: High-fidelity simulation, synthetic data, or statutory liability allocation may systematically replace real observation, market commitments, or experimental intervention. If regulators accept those substitutes and pricing no longer rewards real inputs, withdraw this judgment.
- **External comparison note**: The comparison is “partly consistent”; the claim is not the slogan “data is oil,” but that physical observation, legal liability, and causal intervention have different hard constraints.
- **depends-on**: J-001
- **Against consensus**: Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate. Retained: the three input classes are protected by physical presence, legal liability, and interventional experiment, and cannot be produced by recombination; following the external evidence boundary, the claim is narrowed to high-liability domains rather than broad appreciation.
- **External comparison source**: EXT-7 (see the source index above).
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.

### J-017 · AI mediation expands weak-tie coordination faster than strong relationships

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2033, AI mediation will expand weak-tie coordination faster than strong relationships, without expanding the number of relationships in which a person can remain present over time.
- **Diffusion-gate review**: audience scale = hundred-million-scale (professionals and organizations using digital communication), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L8 human needs and demand + L9 relational asymmetry + L2 constraint migration.
- **Reasoning chain**: J-006 lowers the cost of multi-party coordination and information compression → J-007 makes shared context and history easier to resume → contact, translation, introductions, and scheduling for weak ties can scale → strong ties remain constrained by shared experience, mutual responsibility, conflict repair, and finite attention → more connections do not automatically become more commitments that people can rely on.
- **Time window**: 2027–2033.
- **Falsifier**: By 2033, longitudinal evidence after widespread AI mediation shows that the number of strong relationships a person can sustain and the number of relationships in which they can bear shared consequences both rise materially, without a new attention or presence bottleneck.
- **Leading indicator**: Share of work, education, and transactions coordinated through AI mediation; human time per coordination; close-network size and relationship-repair frequency; measured annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007.
- **Strongest opposing mechanism**: AI may become a genuinely reciprocal relationship participant accepted by institutions and people, or materially increase the effective attention available for strong ties. If longitudinal evidence shows strong-tie capacity rising steadily with AI mediation, withdraw this judgment.
- **Against consensus**: Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect. Retained: strong ties are bounded by shared experience, mutual exposure, and finite attention while weak-tie coordination scales; the causal gap is carried by longitudinal leading indicators, and confidence is not raised.
- **External comparison source**: EXT-17, EXT-18 (see the source index above).
- **Who should change what behavior**: People and organizations should delegate context synchronization to AI, but preserve shared-consequence decisions, conflict repair, and important rituals as human presence.
- **Source**: [C1 · What Becomes Unbuyable After Generation Becomes Free](chains/10-generation-becomes-free.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-006 · Reasoning throughput precedes long-horizon autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, the number of parallel reasoning paths affordable per task will rise substantially, making generate–compare–revise workflows common before long-horizon autonomous execution.
- **Diffusion-gate review**: audience scale = million-scale (model researchers and infrastructure operators), a technical precondition, not a daily society-wide action; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: J-001 lowers unit cost → the same budget runs more candidate paths → a scheduler parallelizes simple steps and upgrades difficult ones → workflows shift from one answer to candidate search.
- **Time window**: 2026–2028.
- **Falsifier**: By the end of 2028, mainstream systems still support only one path per comparable task, and cost declines have not translated into parallel attempts.
- **Leading indicator**: Per-task sample count, end-to-end latency, and quality curves for public systems; observe twice yearly.
- **Confidence**: High.
- **depends-on**: J-001.
- **Strongest opposing mechanism**: Energy, bandwidth, or provider queues trap lower costs inside single calls; withdraw this judgment if per-task parallelism does not rise for two years.
- **Against consensus**: Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable. Retained: parallel candidate search requires only falling unit cost and feasible scheduling, not external confirmation of ordering; the ordering risk is carried by the end-2028 falsification condition.
- **External comparison source**: EXT-1, EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-007 · Resumable context precedes reliable long-term memory

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, task-level retrieval context will become a common base for multi-session collaboration before sourced, revisable long-term memory matures.
- **Diffusion-gate review**: audience scale = million-scale (professionals and organizations using knowledge tools), a technical precondition, not a daily society-wide action; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: More parallel attempts create more state → one context window cannot hold the full history → tasks, evidence, and open questions must be retrieved → retrieval first solves “bring it back,” while provenance and versions solve “can it be trusted.”
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, mainstream long tasks still rely mainly on unstructured chat replay, and retrieval context produces no measurable continuation gain.
- **Leading indicator**: Long-task recovery rate, retrieval hit rate, and the share of citations from outside the active context window; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006.
- **Strongest opposing mechanism**: Longer windows and stronger models may simply overpower retrieval and memory engineering; downgrade this judgment if long-window systems consistently outperform structured memory on long tasks.
- **Against consensus**: Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order. Retained: “retrieve first, then establish trustworthiness” is a capability dependency that coexists with long windows; following the external boundary, the industry-ordering part is downgraded to a testable hypothesis.
- **External comparison source**: EXT-8 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-008 · Sourced long-term memory becomes a prerequisite for reliable collaboration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2031, long-term memory with sources, dates, and confidence boundaries will become necessary for high-value continuous collaboration rather than a chat-product extra.
- **Diffusion-gate review**: audience scale = million-scale (professionals and organizations needing auditable collaboration), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-009 · Continuous execution in constrained workflows matures first

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, constrained workflows with checkable inputs and outputs and limited permissions will achieve stable continuous execution before open-world autonomy matures.
- **Diffusion-gate review**: audience scale = million-scale (organizations and professionals adopting constrained workflows), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Sourced memory reduces repeated errors → closed environments provide a limited state space → permissions and exits can be specified in advance → systems can complete multiple actions and stop at a known failure.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, open-world tasks have reliability indistinguishable from constrained workflows, and permission boundaries and stop conditions no longer affect deployment.
- **Leading indicator**: Consecutive steps completed without intervention, constrained-environment success rate, and safe-stop rate after permission denial; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-008.
- **Strongest opposing mechanism**: A sudden jump in general world modeling could erase the closed/open gap; withdraw this judgment if open tasks catch constrained tasks under the same evaluation standard.
- **Against consensus**: Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain. Retained: the sources support the constraint transition itself, while constrained workflows stabilize first because their state space is bounded and permissions and stop conditions can be specified in advance — not a restatement of consensus.
- **External comparison source**: EXT-2, EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-010 · Long-horizon autonomy follows constrained continuous execution

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2033, autonomous execution across longer horizons with fewer human confirmations will reach acceptable reliability in some high-value settings.
- **Diffusion-gate review**: audience scale = million-scale (high-liability organizations and agent-system operators), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Constrained workflows accumulate state and failure data → long tasks expose more unanticipated states → the system must pause and request evidence under uncertainty → reliable long-horizon execution depends on environment observation and evaluation loops, not simply longer plans.
- **Time window**: 2029–2033.
- **Falsifier**: By 2033, long-horizon tasks still require step-by-step human confirmation, or their incident rate has not materially fallen from 2029.
- **Leading indicator**: Average action span per authorization, proactive pause rate, human takeover rate, and irreversible incident rate; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Vendors may split long tasks into many hidden short tasks; rewrite this judgment if incident rates fall without expanding environmental observation.
- **Against consensus**: Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited. Retained: long-horizon reliability is bounded by environment observation and evaluation loops, which matches the external task-horizon curves; the window risk is carried by the 2033 falsification condition.
- **External comparison source**: EXT-3 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-011 · Cross-media consistency precedes long-range coherence

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, local consistency of entities and formats across text, images, and audio will become reusable before causal coherence across long time spans.
- **Diffusion-gate review**: audience scale = million-scale (content and product teams), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-012 · Cross-time coherence depends on state and evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2034, cross-time coherence in long stories, persistent interactive environments, and multi-round design will reach production quality only after state memory and repeated evaluation mature.
- **Diffusion-gate review**: audience scale = million-scale (long-horizon content, R&D, and operations organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Local cross-media consistency reduces frame-level errors → long tasks still accumulate drift in entities, space, and causality → sourced memory preserves state → automatic counterexamples and replay evaluation permit ongoing correction.
- **Time window**: 2029–2034.
- **Falsifier**: By 2034, production-grade long-generation neither depends on state tracking and replay evaluation nor has drift comparable to short segments.
- **Leading indicator**: Long-generation state drift, replay reproducibility, and local-retention rate after cross-round edits; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-008, J-011.
- **Strongest opposing mechanism**: A new generation architecture may learn stable world state directly without explicit memory and evaluation; withdraw this judgment if independent tests show long coherence without those components.
- **Against consensus**: Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation. Retained: long-range coherence depends on state retention and replay validation, which is the same difficulty the external review identifies; the window has no external support, so confidence stays Medium.
- **External comparison source**: EXT-5 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-013 · Checkable tool calls precede open-environment action

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, tool calls with parameters, preconditions, permissions, and structured results will spread before systems expand into continuous action in complex environments.
- **Diffusion-gate review**: audience scale = million-scale (organizations and developers using tool calls), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Constrained continuous execution needs explicit boundaries → natural-language tool calls are hard to check → typed interfaces structure actions and results → structured calls first accumulate reliability on a few tools and then expand the tool surface.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, high-value tools broadly accept unstructured natural-language calls, with no error-rate difference from checkable interfaces.
- **Leading indicator**: Tool-schema coverage, precondition rejection rate, parameter error rate, and replayable-result ratio; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Models may self-correct through natural language and quickly absorb the value of structure; downgrade this judgment if schema-free tools consistently catch up in real tasks.
- **Against consensus**: Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment. Retained: the ordering follows from the checkability of structured interfaces, and productization evidence is consistent with it; the strict ordering is carried by the 2030 falsification condition.
- **External comparison source**: EXT-6 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-014 · Rehearsable environments follow single-tool integration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2032, environments combining snapshots, shadow execution, permission boundaries, and rollback points will arrive after single-tool integration but before high-value autonomous action becomes common.
- **Diffusion-gate review**: audience scale = million-scale (agent-system operators and high-liability organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-015 · Formal verification precedes open-world evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, tests, schemas, static checks, and counterexample search will be absorbed by generation systems before independent evaluation of real-world outcomes matures.
- **Diffusion-gate review**: audience scale = million-scale (model developers, enterprise evaluators, and auditors), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: technology sequencing + L2 constraint migration.
- **Reasoning chain**: Parallel generation increases candidate count → formal properties can be judged quickly by programs → generate–test–discard loops lower output error → open-world outcomes still require waiting for observation and intervention and cannot be replaced immediately by self-evaluation.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, open-world outcome evaluation is broadly reliable while formal testing has not entered the default generation loop.
- **Leading indicator**: Default-on automated-test ratio, counterexample-search coverage, schema-violation rate, and formal-verification impact on final adoption; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006, J-009.
- **Strongest opposing mechanism**: General models may leap directly across formal and open-world evaluation; withdraw this judgment if independent external outcomes remain highly aligned with model self-evaluation across multiple domains.
- **Against consensus**: Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration. Retained: formalizable properties can be decided immediately by programs while open-world outcomes must await observation, and that asymmetry is unchanged by the external material.
- **External comparison source**: EXT-2, EXT-4 (see the source index above).
- **Source**: [Technology Capability Sequence](05-tech-sequence.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-016 · Open-world evaluation is the final gate for expanding autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2035, independent observation, causal intervention, and continuous monitoring will become the final technical gate for widening the authorization of long-horizon autonomous action.
- **Diffusion-gate review**: audience scale = million-scale (high-liability organizations and regulatory or evaluation bodies), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

---


### J-018 · Parallel reasoning before long-horizon autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, generate–compare–revise becomes the default workflow before long-horizon autonomy.
- **Diffusion-gate review**: audience scale = hundred-million-scale (knowledge workers, product teams, and organizational decision-makers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: Abundance → scarcity + capability sequence.
- **Reasoning chain**: J-006 raises parallel throughput → candidate search becomes cheap first → reliable long-horizon environmental control still requires J-009 boundaries and evaluation → parallel reasoning spreads first.
- **Time window**: 2026–2028.
- **Falsifier**: By end-2028, high-value workflows mainly rely on low-confirmation long-horizon autonomy rather than candidate search.
- **Leading indicator**: Samples per task, automatic comparison share, and action span without human takeover; semiannual.
- **Confidence**: High.
- **depends-on**: J-006, J-009.
- **Strongest opposing mechanism**: A sudden reliability jump makes long-horizon execution and candidate search spread together; withdraw if long tasks match candidate-search validation standards.
- **Against consensus**: Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference. Retained: cheaper candidate search follows directly from J-006; the window remains this project’s inference and is carried by the end-2028 falsification condition.
- **External comparison source**: EXT-1 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-019 · Token saving is a window

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2028, stronger models and cheaper repeated attempts compress the value of saving tokens; it is a window, not durable scarcity.
- **Diffusion-gate review**: audience scale = ten-million-scale (developers, content teams, and heavy AI users), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-020 · Reproducible content keeps falling in price

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, reproducible content keeps falling in marginal price as objective selection becomes part of generation.
- **Diffusion-gate review**: audience scale = hundred-million-scale (content producers, marketing teams, and platform buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: Abundance → scarcity + capability sequence.
- **Reasoning chain**: J-002 formalizable quality is tested automatically → J-015 expands the generate–verify loop → homogeneous supply increases → mere content delivery loses price.
- **Time window**: 2026–2028.
- **Falsifier**: By 2028, generic reproducible content retains broad scarcity premiums without copyright or compute constraints.
- **Leading indicator**: Generation cost, delivery price, and automatic-selection coverage; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-002, J-015.
- **Strongest opposing mechanism**: Copyright, distribution, or real-data licensing constrains supply; downgrade if price stays detached from supply.
- **Against consensus**: Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers. Retained: the supply-demand inference that copyable content depresses marginal price holds; this card does not claim liability-sensitive selection disappears, and detection and provenance remain handled under J-022.
- **External comparison source**: EXT-1, EXT-4, EXT-11 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-021 · First-hand field signals earn a premium first

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, unrecorded field observations and traceable sources earn a premium earlier than second-hand expression.
- **Diffusion-gate review**: audience scale = ten-million-scale (professionals and buyers in high-liability industries), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-022 · Forgable signals drive credential upgrades

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, more forgable personalized signals push important decisions toward costlier identity, fulfillment, and liability credentials.
- **Diffusion-gate review**: audience scale = hundred-million-scale (professional services, platforms, and organizational buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: Abundance → scarcity + L5 signal forgery.
- **Reasoning chain**: J-005 raises accountable entities → J-017 cheapens weak-tie coordination → surface interaction is harder to distinguish → high-value decisions raise credential thresholds.
- **Time window**: 2026–2029.
- **Falsifier**: Acceptance of low-cost generated identity signals rises in high-value transactions without added liability or verification.
- **Leading indicator**: Multifactor credential adoption, guarantees, and liability clauses; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-005, J-017.
- **Strongest opposing mechanism**: Platforms provide trusted identity and compensation cheaply; revisit if internal verification lowers thresholds.
- **Against consensus**: Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown. Retained: more forgeable signals necessarily raise the verification threshold for high-value judgments, which follows from the forgery mechanism; adoption and cost are unknown, so confidence stays Medium.
- **External comparison source**: EXT-4, EXT-11 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-023 · Attention shifts toward fulfilled commitments

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2030, important attention allocation shifts from expression quality toward relationship continuity and fulfilled commitments.
- **Diffusion-gate review**: audience scale = hundred-million-scale (platform users and content or relationship operators), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: Abundance → scarcity + L8 human constants.
- **Reasoning chain**: J-017 expands coordination supply → J-022 makes surface signals easier to forge → one-off expression loses distinction → repeated fulfillment records gain weight.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, important choices are still predicted mainly by one-off generated expression rather than fulfillment records.
- **Leading indicator**: Use of fulfillment, repeat relationships, and breach records; annual.
- **Confidence**: Medium.
- **depends-on**: J-017, J-022, J-013.
- **Strongest opposing mechanism**: One-time platform credentials predict fulfillment as well as repeated records; downgrade if they consistently outperform history.
- **Against consensus**: Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift. Retained: the direction follows from declining discriminability of one-off expression plus durable records in repeated relationships, which current usage data can neither prove nor refute; the attention-shift risk is carried by the 2030 falsification condition.
- **External comparison source**: EXT-16 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-024 · Credentials re-layer (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, credentials may re-layer around fulfillment, liability, and presence, but the institutional form is uncertain.
- **Diffusion-gate review**: audience scale = ten-million-scale (professional services and organizational buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: Abundance → scarcity + L5 signal forgery.
- **Reasoning chain**: J-022 raises verification cost → J-023 raises the value of long records → risk contexts adopt different credential layers, subject to platform and legal choices.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, high-risk transactions still rely on one low-cost identity signal without contextual layers.
- **Leading indicator**: Guarantees, audits, and presence proofs in high-risk services; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-022, J-013.
- **Strongest opposing mechanism**: One universal platform identity covers all risk contexts; withdraw if this persists.
- **Against consensus**: Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only. Retained as landscape only, with confidence not raised; upgrading to a bettable judgment requires evidence of an institutional endpoint (law or platforms explicitly adopting stratified credentials).
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-025 · Small-team output rises

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2030, small teams complete more verifiable output with fewer steps.
- **Diffusion-gate review**: audience scale = hundred-million-scale (knowledge workers and small teams), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: Abundance → scarcity + organizational boundaries.
- **Reasoning chain**: J-009 constrained continuity → J-013 inspectable tools → repeated knowledge steps become agent-mediated → verifiable output rises at constant headcount.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, comparable teams using constrained agents do not produce more verifiable output.
- **Leading indicator**: Auditable tasks per employee, takeover rate, and output per unit; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-009, J-013.
- **Strongest opposing mechanism**: Coordination, verification, and incident handling erase automation gains; downgrade if total output stays flat while oversight rises.
- **Against consensus**: Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient. Retained: rising verifiable output once repeated knowledge steps are delegated follows from the mechanism; the causal gap is carried by leading indicators comparing equally sized teams.
- **External comparison source**: EXT-16 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-026 · Responsibility boundaries remain

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, responsibility boundaries do not disappear at the same rate as knowledge-work steps.
- **Diffusion-gate review**: audience scale = hundred-million-scale (supervisors, accountable owners, and professionals inside organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: Abundance → scarcity + L3 organizational form.
- **Reasoning chain**: J-009 expands executable steps → J-013 makes permissions programmable → accidents still need a legal entity → authorization, review, and escalation remain scarce.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, high-value AI actions routinely have no identifiable person or organization bearing consequences.
- **Leading indicator**: Liability clauses, escalation roles, and insurance claims; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-009, J-013.
- **Strongest opposing mechanism**: Law transfers all responsibility to platforms; rewrite if platforms bear all high-value consequences.
- **Against consensus**: Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts. Retained: the constraint that incidents require a legal subject does not dissolve with automation; this card forecasts no job counts, so the regulatory evidence does not conflict with it.
- **External comparison source**: EXT-10 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-027 · Rented compute spreads capability

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2029, rented compute spreads access to AI capability for small organizations without distributing gains evenly.
- **Diffusion-gate review**: audience scale = ten-million-scale (developers, model-using organizations, and infrastructure buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: Abundance → scarcity + L7 rent windows.
- **Reasoning chain**: J-001 lowers call cost → J-006 raises affordable attempts → renting lowers fixed-capital barriers → data, access, and liability capacity still differentiate gains.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, small organizations cannot obtain comparable general reasoning by renting, or diffusion eliminates gain differences.
- **Leading indicator**: Small-organization call share, fixed compute capex, and rental price; quarterly.
- **Confidence**: Medium.
- **depends-on**: J-001, J-006.
- **Strongest opposing mechanism**: Energy, quotas, or platform concentration keeps rented compute for large organizations; downgrade if small-organization access does not rise.
- **Against consensus**: Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity. Retained: rentable capability and uneven gains arise from two different constraint sets (capital thresholds versus data, distribution, and liability capacity), and the diffusion evidence supports only the first.
- **External comparison source**: EXT-1, EXT-12 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-028 · Access becomes a bargaining node (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, proprietary data, distribution, and liability capacity may become more important bargaining nodes than models.
- **Diffusion-gate review**: audience scale = ten-million-scale (controllers of data, channel, energy, and liability access points), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: Abundance → scarcity + L7 rent windows.
- **Reasoning chain**: J-027 expands model access → J-005 raises the value of real inputs and responsibility → models become more reproducible → control of inputs, exits, and losses may earn rent.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, access controllers have no persistent premium over non-controllers absent regulatory constraints.
- **Leading indicator**: Data licenses, distribution take rates, AI liability insurance, and channel exclusivity; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-005, J-013.
- **Strongest opposing mechanism**: Models, energy, and distribution commoditize and access rents disappear; withdraw if rent keeps falling.
- **Against consensus**: Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven. Retained as landscape only, with confidence not raised; upgrading requires price evidence of persistent rents, not merely the existence of gatekeeping positions.
- **External comparison source**: EXT-4, EXT-12 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-029 · Demand-side anchors persist

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026–2030, status, certainty, embodied presence, and responsibility remain demand-side anchors despite richer expression and choice.
- **Diffusion-gate review**: audience scale = billion-scale (ordinary people’s needs for status, certainty, presence, and responsibility), daily/weekly; Gate 1 **PASS** — may be written as a society-level judgment.
- **Lens**: L8 human constants + abundance → scarcity.
- **Reasoning chain**: J-017 expands coordination → J-011 expands trial identities and expression → more options do not create shared consequences → demand remains organized around status, certainty, presence, and responsibility.
- **Time window**: 2026–2030.
- **Falsifier**: By 2030, these needs no longer predict important choices across groups, independent of measurement or institutional change.
- **Leading indicator**: Preferences for presence and responsibility in high-value consumption, relationship, and commitment decisions; annual.
- **Confidence**: Medium.
- **depends-on**: J-017, J-011.
- **Strongest opposing mechanism**: A stable, broad generational preference shift; downgrade if longitudinal data shows persistent drift.
- **Against consensus**: Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven. Retained: the demand-side anchors follow from the stability of status, certainty, presence, and responsibility attribution; unchanged preferences through 2030 cannot be externally confirmed, and that risk is carried by the falsification condition.
- **External comparison source**: EXT-17, EXT-18 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-030 · AI mediates coordination, not shared experience (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027–2032, AI mediates context synchronization and relationship coordination but not experiences requiring embodied presence and shared consequences.
- **Diffusion-gate review**: audience scale = hundred-million-scale (people and organizations using AI coordination tools), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L8 human constants + embodied-presence constraint.
- **Reasoning chain**: J-017 cheapens weak-tie coordination → J-011 enriches multimodal expression → shared experience still requires bodies, time, and reciprocal consequences → coordination agents do not expand strong-relationship capacity automatically.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, agent-mediated interaction reliably replaces shared experience in long relationships with no behavioral or reported difference.
- **Leading indicator**: Agent messages versus shared activities, conflict-repair results, and retention; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-017, J-011.
- **Strongest opposing mechanism**: People treat persistent AI interaction as sufficiently real reciprocity; rewrite if it reliably substitutes for shared experience.
- **Against consensus**: Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient. Retained as landscape only: the hard constraint that shared experience requires bodies, time, and reciprocal consequences still holds, while substitution effects lack causal and generational evidence, so confidence is not raised.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)



### J-031 · Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Diffusion-gate review**: audience scale = ten-million-scale (organizations and developers letting AI take real actions), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-032 · Authorization review and exception escalation become scarcer than execution steps

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization review and exception escalation become scarcer than execution steps
- **Diffusion-gate review**: audience scale = ten-million-scale (authorization, review, and escalation roles and their organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Inspectable tool calls spread → execution steps become templated → cross-boundary authorization, exception escalation, and final responsibility still require judgment → review roles appreciate relative to execution steps
- **Dependency impact**: If J-013 is falsified, inspectable-permission infrastructure disappears; if authorization is not scarce despite it, this card fails
- **Time window**: 2027–2032
- **Falsifier**: By 2032, authorization-review hours fall at the same rate as execution hours without increased incidents
- **Leading indicator**: Permission-denial rate, human escalation hours, responsibility-role hiring; quarterly
- **Confidence**: Medium
- **depends-on**: J-013
- **Strongest opposing mechanism**: If J-013 is falsified, inspectable-permission infrastructure disappears; if authorization is not scarce despite it, this card fails
- **Against consensus**: Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing. Retained: cross-boundary authorization, escalation, and final responsibility require judgment and are not absorbed by templating; relative scarcity lacks supply data, so confidence stays Medium.
- **External comparison source**: EXT-4, EXT-10, EXT-13 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-033 · Verifiable records of real interventions become more valuable than explanation itself

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Verifiable records of real interventions become more valuable than explanation itself
- **Diffusion-gate review**: audience scale = ten-million-scale (high-liability professionals and organizations in medicine, engineering, and compliance), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-034 · Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Diffusion-gate review**: audience scale = ten-million-scale (high-liability organizations, auditors, and regulators), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Synthetic material lowers exploration cost → low-liability contexts tolerate model error → high-liability contexts bear bodily, legal, and compensation consequences → regulators retain real trials
- **Dependency impact**: If J-005 is falsified, real trials lose their structural necessity; this card weakens
- **Time window**: 2028–2033
- **Falsifier**: By 2033, high-liability fields broadly replace real trials with synthetic evidence without higher incident rates
- **Leading indicator**: Regulatory acceptance scope, trial budgets, insurance clauses; annual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, real trials lose their structural necessity; this card weakens
- **Against consensus**: Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation. Retained: high-liability settings carry bodily, legal, and compensation consequences, which is why regulators preserve real trials; the window has no external support and is carried by the 2033 falsification condition.
- **External comparison source**: EXT-7, EXT-9 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-035 · Responsibility collateral enters the transaction structure for consequential AI output

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Responsibility collateral enters the transaction structure for consequential AI output
- **Diffusion-gate review**: audience scale = ten-million-scale (buyers, insurers, and professionals around consequential output), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-036 · Long-term fulfillment records allocate attention better than one-off natural expression

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Diffusion-gate review**: audience scale = hundred-million-scale (platforms, content producers, and users of digital services), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Expression generation becomes cheap → surface credibility becomes hard to distinguish → repeated fulfillment leaves verifiable records → attention shifts to longitudinal consistency and delivery rate
- **Dependency impact**: If J-017 is falsified, weak-tie coordination did not become cheap and pressure for credential upgrading disappears; this card weakens
- **Time window**: 2027–2032
- **Falsifier**: By 2032, important choices are still driven mainly by one-off expression rather than fulfillment records
- **Leading indicator**: Adoption of performance-history recommendations, repeat and default rates; annual
- **Confidence**: Medium
- **depends-on**: J-017
- **Strongest opposing mechanism**: If J-017 is falsified, weak-tie coordination did not become cheap and pressure for credential upgrading disappears; this card weakens
- **Against consensus**: Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence. Retained: cheap expression voids surface credibility while repeated fulfillment leaves verifiable records, a mechanism that does not depend on attention data; the gap is carried by leading indicators.
- **External comparison source**: EXT-13, EXT-14 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-037 · Comparable small teams produce more verifiable output

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Comparable small teams produce more verifiable output
- **Diffusion-gate review**: audience scale = hundred-million-scale (small teams and knowledge workers adopting agents), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: cost structure determines organizational form + technology sequence
- **Reasoning chain**: Constrained workflows stabilize → tool calls become inspectable → a few people orchestrate more agent steps → per-team output and audit records increase
- **Dependency impact**: If J-009 is falsified, the continuous-execution premise disappears; this card weakens
- **Time window**: 2027–2031
- **Falsifier**: By 2031, agent-using small teams show no repeatable output gain over baseline
- **Leading indicator**: Per-person delivery, rework, auditable-output share; quarterly
- **Confidence**: Medium
- **depends-on**: J-009
- **Strongest opposing mechanism**: If J-009 is falsified, the continuous-execution premise disappears; this card weakens
- **Against consensus**: Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams. Retained: fewer people orchestrating more checkable steps follows from the mechanism; the causal gap on same-size output is carried by comparative leading indicators, and confidence is not raised.
- **External comparison source**: EXT-1, EXT-16 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-038 · Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Diffusion-gate review**: audience scale = hundred-million-scale (accountable roles, supervisors, and professionals inside organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: L2 (constraint migration) + cost structure determines organizational form
- **Reasoning chain**: Inspectable tool calls spread → permission boundaries clarify → normal steps automate → exceptions and cross-boundary consequences cannot be fully precomputed → responsibility roles remain
- **Dependency impact**: If J-013 is falsified, programmable-permission infrastructure disappears; if responsibility roles still shrink, this card fails
- **Time window**: 2027–2032
- **Falsifier**: By 2032, responsibility-role share falls at the same rate as execution roles without more high-risk incidents
- **Leading indicator**: Exception volume, responsibility-role hiring, post-incident human intervention; quarterly
- **Confidence**: Medium
- **depends-on**: J-013
- **Strongest opposing mechanism**: If J-013 is falsified, programmable-permission infrastructure disappears; if responsibility roles still shrink, this card fails
- **Against consensus**: Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven. Retained: exceptions and cross-boundary consequences cannot be enumerated in advance, which is why accountability roles persist; job counts and timing are not something the sources can supply and are carried by the falsification condition.
- **External comparison source**: EXT-10, EXT-13 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-039 · Rented models become abundant, while energy, data, and channel control create access rents

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Rented models become abundant, while energy, data, and channel control create access rents
- **Diffusion-gate review**: audience scale = ten-million-scale (model buyers and controllers of energy, data, and channels), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-040 · Balance sheets able to absorb AI accidents become a separate scarcity

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Diffusion-gate review**: audience scale = ten-million-scale (insurers, capital providers, and high-liability organizations), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration) + L7 (institutional-rent window)
- **Reasoning chain**: Real interventions and commitments appreciate → AI accident losses become measurable → contracts require compensation capacity → capital and insurance price solvency → large balance sheets gain admission advantage
- **Dependency impact**: If J-005 is falsified, liability absorption no longer earns a premium; this card weakens
- **Time window**: 2028–2033
- **Falsifier**: By 2033, compensation capacity does not affect AI contract prices, financing, or deployment eligibility
- **Leading indicator**: Liability premiums, reserves, contract asset requirements; annual
- **Confidence**: Medium
- **depends-on**: J-005
- **Strongest opposing mechanism**: If J-005 is falsified, liability absorption no longer earns a premium; this card weakens
- **Against consensus**: Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven. Retained: pricing solvency through contracts and insurance extends current governance; the independent scarcity premium is unproven, so confidence stays Medium.
- **External comparison source**: EXT-14, EXT-15 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-041 · AI first expands the coordination radius of weak ties

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: AI first expands the coordination radius of weak ties
- **Diffusion-gate review**: audience scale = hundred-million-scale (digital communicators and organizational coordinators), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Communication and context-sync costs fall → translation, introductions, and scheduling scale → weak-tie connection radius expands → strong ties remain constrained by shared consequences
- **Dependency impact**: If J-017 is falsified, the coordination-supply premise disappears; this card weakens
- **Time window**: 2027–2033
- **Falsifier**: By 2033, AI mediation neither increases cross-organization weak-tie connections nor reduces coordination time
- **Leading indicator**: AI-mediated coordination share, cross-organization contacts, human time per coordination; annual
- **Confidence**: Medium
- **depends-on**: J-017
- **Strongest opposing mechanism**: If J-017 is falsified, the coordination-supply premise disappears; this card weakens
- **Against consensus**: Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects. Retained: falling coordination cost widens weak-tie radius first while strong ties remain bounded by shared exposure; the causal-separation gap is carried by weak-/strong-tie leading indicators.
- **External comparison source**: EXT-16, EXT-18 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-042 · Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Diffusion-gate review**: audience scale = billion-scale (everyone needing shared experience and embodied presence), daily/weekly; Gate 1 **PASS** — may be written as a society-level judgment.
- **Lens**: L2 (constraint migration) + L8 (human constants) + L9 (relationship asymmetry)
- **Reasoning chain**: Multimodal expression becomes abundant → mediated companionship and reminders spread → shared experience still requires bodies, time, and reciprocal consequences → strong-tie capacity remains presence-constrained
- **Dependency impact**: If J-011 is falsified, the premise of richer multimodal expression weakens; if agents stably replace presence, this card weakens
- **Time window**: 2027–2033
- **Falsifier**: By 2033, agent-mediated interaction reliably replaces shared experience in long relationships with no reported or behavioral difference
- **Leading indicator**: Agent interaction versus shared activity, conflict repair, relationship retention; annual
- **Confidence**: Low
- **depends-on**: J-011
- **Strongest opposing mechanism**: If J-011 is falsified, the premise of richer multimodal expression weakens; if agents stably replace presence, this card weakens
- **Against consensus**: Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects. Retained as landscape only, with confidence not raised; upgrading requires both behavioral and self-reported evidence of substitution in long-term relationships.
- **External comparison source**: EXT-9 (see the source index above).
- **Source**: [Mid-term landscape](20-mid.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-055 · Real-world signals earn a premium as contract assets in high-liability tasks

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium.
- **Diffusion-gate review**: audience scale = ten-million-scale (professionals, buyers, and underwriters in high-liability tasks), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L1 (abundance → scarcity) + L2 (constraint migration) + L5 (signal forgery) + L6 (irreversibility).
- **Reasoning chain**: C1 makes second-hand expression and synthetic samples abundant → ordinary data files lose marginal price → high-liability tasks still require real observations, provenance, and an accountable party → collection permission, calibration, usage boundaries, and compensation duties enter contracts → data becomes a contract asset with a liability chain.
- **Time window**: 2029–2033.
- **Falsifier**: By 2033, across multiple high-liability fields, regulators, insurers, and buyers broadly accept synthetic evidence with no worse incident rate than real signals, while provenance, calibration, and liability chains carry no observable premium.
- **Leading indicator**: Synthetic-evidence share in high-liability approvals, premium for data contracts with provenance and calibration clauses, real-trial budget share, and data-liability insurance rates; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-005, J-033, J-034, J-039.
- **Strongest opposing mechanism**: A high-fidelity world model and unified platform compensation may absorb real observation and provider liability internally; if platforms absorb all errors and buyers no longer pay separately for provenance and liability, an independent contract-asset layer does not form.
- **Against consensus**: Directionally consistent with stronger data governance, provenance, and trust, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven. Retained: high-liability tasks require real observation, provenance, and a recourse-bearing subject, none of which recombination can produce; the independent premium is unproven, so confidence stays Medium.
- **External comparison source**: EXT-7, EXT-10, EXT-14 (see the source index above).
- **Source**: [C2: How Real-World Signals Become Contract Assets](chains/20-real-signals-become-contracts.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-056 · The binding constraint on compute expansion moves from chip supply to power delivery and interconnection permits

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: Within this window the binding constraint on compute expansion moves from chip supply to power delivery and interconnection permitting.
- **Diffusion-gate review**: audience scale = ten-million-scale (data-center operators, power developers, and permitting bodies), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration), L4 (diffusion lag).
- **Reasoning chain**: Chips are a mass-produced, shippable, globally reallocatable industrial good whose expansion elasticity rises with investment → transformers, high-voltage equipment, and lines are bound by heavy-manufacturing and construction cycles, can barely be accelerated by more orders, and cannot be reallocated across regions → interconnection, environmental, and land permits run on administrative and local-political cycles decoupled from technical progress → the three supply curves differ in slope by an order of magnitude → when capital concentrates, permits and interconnection queues are exhausted before wafers.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, among delays to new compute projects in major markets, those attributable to chip delivery still outnumber those attributable to power delivery and interconnection permitting; or average large-load interconnection wait times in major markets fall below their 2026 level.
- **Leading indicator**: Large-load interconnection queue times, transformer and high-voltage switchgear lead times, average time from project announcement to energization, share of deals where power contracts are signed before hardware orders; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-001, J-027.
- **Strongest opposing mechanism**: Energy per unit of service falls faster than service volume grows, or compute investment pulls back sharply, so load growth never catches grid expansion and the constraint never binds; if new-load growth runs below deliverable-capacity growth, this card weakens.
- **Against consensus**: Directionally consistent with "AI electricity growth is a real constraint," but this project's claim is narrower and more falsifiable — the binding constraint is the **timing** of delivery and permitting, not total generation. The comparison obtained this round covers generation-side queues only (EXT-19 explicitly excludes load-side queues), so the agreement holds at the mechanism level only. Why the judgment is retained: load-side statistics are still missing, but both legs of the mechanism are separately corroborated — DOE records connection lead times of 1–3 years for hyperscale facilities of 300–1000 MW+ and the resulting shift toward co-location with existing generation to get power faster (EXT-29), and ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30). Confidence stays at Medium rather than rising, because cross-market load-side queue statistics still do not exist.
- **External comparison source**: EXT-12, EXT-19, EXT-29, EXT-30 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-057 · What gets priced is not energy but certainty of delivery date

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: In compute-related power transactions, what is mainly priced is not energy but the certainty of being live on the promised date.
- **Diffusion-gate review**: audience scale = ten-million-scale (compute buyers, operators, and site developers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L8 (human needs — paying for certainty), L3 (cost structure).
- **Reasoning chain**: J-056 makes the queue the binding constraint → model generations turn over quickly, so capacity that arrives eighteen months late loses much of its competitive value → willingness to pay for an in-service date exceeds willingness to pay for a lower average tariff → contracts grow capacity reservation fees, in-service date guarantees, delay damages, and on-site generation or storage as a bridge → within one region, permitted and interconnected sites trade above bare land by far more than construction cost.
- **Time window**: 2027–2032.
- **Falsifier**: By 2032, price differences in large compute power contracts are mainly explained by per-kilowatt-hour price, and terms tied to delivery-date guarantees (reservation fees, lead-time premiums, delay damages) have not become common.
- **Leading indicator**: Share of power and capacity contracts carrying in-service date guarantees and delay damages; price gap between permitted sites and bare land in the same region; adoption of on-site generation and storage as bridging; semiannual.
- **Confidence**: Medium.
- **depends-on**: J-056.
- **Strongest opposing mechanism**: A sharp pullback in compute demand empties the queue; or grids accelerate broadly so wait times no longer discriminate between sites, and certainty stops being scarce.
- **Against consensus**: **Partly consistent, but the agreement does not sit where this card lands.** Agreement: regulator-approved large-load contracts are indeed tiered by commitment and term rather than by per-kilowatt-hour price — FERC directed PJM to create three tiers of co-located load service distinguished by capacity commitment (EXT-21), and the AEP Ohio tariff approved by PUCO builds its price protection from an 85% minimum take, a 12-year term, a 4-year ramp, exit fees and collateral (EXT-22). **Divergence**: those terms protect the **seller** against being stranded, whereas this card claims the **buyer** pays a premium for energization on date; both point at time and commitment being priced, but from opposite sides, and one does not substitute for the other. **Evidence boundary**: this card's falsifier asks how common such contract terms are, and commercial terms in large-load contracts are almost entirely confidential, so no public statistics exist and the falsifier is currently **not computable**. Why the judgment is retained: the direction of the mechanism has independent support in two jurisdictions, so the judgment stands with confidence at Medium rather than rising; and the leading indicator shifts from "share of contracts" to a publicly checkable proxy — the count of minimum-take and exit-fee provisions appearing in regulatory filings, and the price gap between permitted and raw sites in the same region.
- **External comparison source**: EXT-21, EXT-22 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-058 · AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a grid flexibility resource

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a flexibility resource the grid pays for rather than merely a burden.
- **Diffusion-gate review**: audience scale = ten-million-scale (grid, data-center, and energy-market participants), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration), L3 (cost structure).
- **Reasoning chain**: Interactive inference is latency-sensitive, non-interruptible, and immobile → training, batch inference, and evaluation can be paused, deferred, and moved across time zones → for the latter the cost of interruption is time rather than spoilage, unlike aluminium smelting and similar heavy industrial load → what grids are shortest of is flexibility, and demand response, interruptible tariffs, and capacity markets are existing payment channels → schedulable compute is load and resource at once, and its real power cost can sit below its nominal tariff.
- **Time window**: 2027–2033.
- **Falsifier**: By 2033, contracted data-centre capacity in interruptible or demand-response programs in major markets remains negligible (under 5% of their contracted capacity) and large compute users broadly refuse interruptibility terms.
- **Leading indicator**: Contracted data-centre demand-response capacity and its share, share of interruptible tariff contracts, public practice of cross-region scheduling of training jobs, data-centre bids in capacity markets; annual.
- **Confidence**: Medium.
- **depends-on**: J-056, J-018.
- **Strongest opposing mechanism**: Interactive inference dominates total load and service-level agreements forbid interruption, leaving a flexible share too small to matter; if the schedulable share stays in the low single digits, withdraw this card.
- **Against consensus**: **Mechanism confirmed, scale unknown.** Agreement: schedulability has moved from inference to measurement — in EPRI's DCFlex demonstration in Phoenix an AI compute cluster cut 25% of its power through a three-hour grid peak without affecting core services (EXT-24), and Duke's Nicholas Institute puts an upper bound on the scale: if new large loads accept 0.25–1.0% annual curtailment, the 22 largest US balancing areas could host nearly 100 GW more load (EXT-23). **Divergence and evidence boundary**: both are **potential**, not **contracted**. This card's falsifier turns on whether contracted interruptible capacity stays below 5%, yet neither PJM's roughly 8,064.7 MW of cleared demand-response capacity (EXT-25) nor ERCOT's flexible-load estimates are broken out by industry, and no authority publishes data-centre-specific contracted capacity — so the falsifier is currently **not computable**. Why the judgment is retained: the mechanism side is better evidenced than when the card was written (inference became measurement), so the judgment stands with confidence at Medium; and one leading indicator is added — whether PJM or ERCOT begins disclosing data-centre demand-response registrations by industry, which is the precondition for this card becoming falsifiable again.
- **External comparison source**: EXT-23, EXT-24, EXT-25, EXT-30 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-059 · The handle of compute control moves from hardware export to the use side

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: Once rental architectures let capability cross borders while hardware stays put, the handle of compute control moves from hardware export to use-side control of parties, purposes, and site authorization.
- **Diffusion-gate review**: audience scale = ten-million-scale (regulators, cloud providers, and organizational buyers), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration), L7 (institutional lag), L5 (signals and forgery).
- **Reasoning chain**: Chips are discrete, countable, traceable, and must clear customs, making them an ideal control object → rented compute diffuses capability while hardware does not move (J-027) → governing "who owns" cannot constrain "who uses" → a regulator either accepts failed control or moves duties to the use side: identity and purpose declaration, remote-access restrictions, model-weight transfer rules, site and operator authorization → the object of control shifts from things to parties and contracts.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, major control regimes remain anchored only in hardware and entity lists, with no enforceable duties on weight transfer, remote access, or data-centre operator authorization, and no enforcement cases.
- **Leading indicator**: Provisions and revisions covering weights, remote access, cloud services, and data-centre authorization; identity and purpose-declaration requirements imposed on compute providers; compliance clauses in cross-border compute contracts; enforcement and penalty cases; annual.
- **Confidence**: Medium.
- **depends-on**: J-001, J-027.
- **Strongest opposing mechanism**: Open weights and local deployment make high-value capability broadly available outside the perimeter, degrading use-side control into symbolic clauses.
- **Against consensus**: **Partly consistent, with one explicit divergence.** Agreement: control has already moved beyond the chip as a physical object, reaching the most advanced closed model weights and data-centre operator authorization (EXT-20). Divergence: this project's independent reasoning expected the handle to land mainly on accounts and remote-access licensing, whereas the observed landing point is weight thresholds plus site and operator authorization, with no standalone cloud-access licensing regime. Why the judgment is retained: the mechanism (rental hollows out entity control → duties migrate to parties and contracts) matches the observed direction, and the difference is the interface rather than the direction; the falsifiable part is therefore narrowed to "do enforceable use-side duties and enforcement cases appear," not "does a cloud-access licence appear."
- **External comparison source**: EXT-20 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-060 · Energy-rich hosts trade sites for compute and gain rent rather than capability sovereignty (landscape only)

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: Host states with surplus energy and fast permitting trade sites and power for compute investment and obtain rent, employment, and tax revenue rather than any right of disposal over the capability itself (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (governments, developers, and industrial workers in energy-rich regions), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L3 (cost structure), L7 (institutional lag).
- **Reasoning chain**: Power and sites cannot be moved, chips can be moved but are export-controlled, and model weights move instantly → the three factors separate geographically and jurisdictionally → what a host state supplies is precisely the least movable factor → its leverage (cutting power, expropriation) is one-shot and extremely costly → what it gains shows up as rent and employment, not capability sovereignty.
- **Time window**: 2028–2035.
- **Falsifier**: By 2035, host states broadly obtain weight escrow, local usage quotas, or independent audit rights in cross-border compute contracts; or most new compute remains concentrated in states that hold both chip supply and jurisdiction, with no observable contract class for cross-border "sovereign compute sites."
- **Leading indicator**: Terms obtained by host states in cross-border data-centre investment (local usage quotas, weight escrow, audit rights); arrangements trading energy subsidies for compute quotas; country-level compute caps and authorization regimes; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-056, J-059.
- **Strongest opposing mechanism**: Host states form a bargaining bloc, or control upstream energy and critical materials as well, so their leverage stops being one-shot.
- **Against consensus**: Partly consistent with observed institutions — country-level compute allocation caps and data-centre operator authorization already exist (EXT-20), and Virginia's JLARC audit shows how little of the value a host jurisdiction retains even inside its own borders (EXT-28). But the inference about host states' long-run bargaining position lacks evidence. Why the judgment is retained: it is kept as landscape only and confidence is not raised; upgrading it requires verifiable evidence from cross-border contract terms — weight escrow, local usage quotas, or independent audit rights.
- **External comparison source**: EXT-20, EXT-28 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-061 · Local externalities of data centres become explicit and social licence becomes a real siting constraint

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: The local externalities of data centres become explicit, turning social licence from an implicit premise into a real cost line in siting.
- **Diffusion-gate review**: audience scale = hundred-million-scale (residents near data centers, local governments, and infrastructure participants), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L7 (institutional lag), L8 (human needs), L6 (irreversibility).
- **Reasoning chain**: Data centres are very large investments with few jobs and conspicuous power and water use → costs land locally while returns accrue to external shareholders → visibility is asymmetric: residents see a monthly electricity bill and never see the AI revenue → under loss aversion, local politics responds with moratoria, special tariff classes for very large customers, water restrictions, and agreements conditioned on tax and employment → siting costs acquire a line item that was previously priced at roughly zero.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, major markets show almost no local moratoria, large-load tariff classes, or water restrictions aimed at data centres, and residential power-price disputes produce no policy consequences.
- **Leading indicator**: Count of local moratoria or rejections, introduction of large-load tariff classes, water-permit conditions, terms trading employment and tax for power; annual.
- **Confidence**: Medium.
- **depends-on**: J-056.
- **Strongest opposing mechanism**: Data centres broadly adopt on-site generation, storage, and closed-loop cooling, decoupling from the public grid and public water so local externalities fall sharply and the conflict does not arise.
- **Against consensus**: **Consistent, and half of it has already happened early.** Agreement: the dedicated large-load tariff this card expected is not a future landscape but an accomplished institutional fact — PUCO approved AEP Ohio's data-centre-specific tariff in July 2025 with the explicit purpose of shielding residential ratepayers (EXT-22), and the Georgia PSC established risk-priced minimum-billing rules for loads above 100 MW in January 2025 (EXT-32). Two jurisdictions moved the same way independently, ahead of this card's 2031 window. **Divergence and evidence boundary**: the other half lacks evidence — no government or academic body systematically counts local moratoria or rejected siting applications, and the trackers that exist are commercial or crowdsourced with opaque methodology; water conflicts so far exist as individual undecided lawsuits (Georgia residents alleging harm to their water), not as an established pattern. Why the judgment is retained: kept with confidence at Medium rather than raised — raising it needs a systematic count of moratoria, not more anecdotes; and this card's falsifier should first be evaluated on the tariff half, where evidence exists, with moratoria and water restrictions treated as boundary evidence until a counting standard appears.
- **External comparison source**: EXT-22, EXT-32 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-06-30.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-062 · Heavy assets are taxable while the value layer is mobile, so local shares stay structurally low (landscape only)

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: What can be taxed is the immovable heavy asset while what earns the profit is the instantly mobile value layer, so the share captured locally stays structurally low (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (local governments, data-center owners, and taxing authorities), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L3 (cost structure), L7 (institutional lag).
- **Reasoning chain**: Taxation requires a visible, immovable presence inside the jurisdiction → data centres are immovable while profit and model weights are mobile → localities can reach power prices, property tax, and a little employment, but not profit → localities keep raising demands on the heavy asset while firms hedge through siting competition → a structural mismatch forms between the taxed asset and the untaxed value layer.
- **Time window**: 2028–2035.
- **Falsifier**: By 2035, taxation of compute services in major markets shifts from the asset side to the use side (for example broadly adopted usage or destination-based taxes covering AI services), giving localities a tax base commensurate with the load they carry.
- **Leading indicator**: Withdrawal or conditioning of data-centre tax abatements, local levies based on electricity consumption, legislative progress on taxing AI services, revenue-sharing terms between localities and firms; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-061, J-039.
- **Strongest opposing mechanism**: International tax reform lands quickly and absorbs the mismatch; or indirect tax revenue from automation gains compensates the local base.
- **Against consensus**: **Mechanism confirmed, but only half of it.** Agreement: Virginia's JLARC audit of the largest US data-centre market quantifies this card's first step — the sales and use tax exemption forgoes roughly $928 million of state revenue a year (FY23) with about 90% of the industry claiming it, local retention rests mainly on property tax, and the jobs in the economic-impact figures are heavily concentrated in the construction phase rather than permanent operations (EXT-28). Across states, 36 offer data-centre-specific tax breaks while only 11 disclose which companies receive them, and subsidy per job in tracked megadeals averages over $262,000 (EXT-31 — ⚠ advocacy organization, not a full sample). **Divergence and evidence boundary**: what is evidenced is only that heavy assets are taxable and the local share is low; the other half — profits and model weights being mobile so the value layer escapes — is addressed by no government or cross-state study, and this card's falsifier points at whether taxation shifts from the asset side to the usage side, where cloud and AI services are covered only by scattered state tax rulings with no systematic research. Why the judgment is retained: kept as landscape only, confidence not raised; upgrading it to a bettable judgment needs two things — a comparable measure of local retained revenue against the load borne, and legislative movement on usage-side taxation.
- **External comparison source**: EXT-28, EXT-31 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-063 · The geography of compute is decided by interconnection queues and permitting speed, not by electricity price

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: Until grid expansion catches up, the geography of compute is explained mainly by interconnection queues and permitting speed rather than by electricity price.
- **Diffusion-gate review**: audience scale = ten-million-scale (grid planners, data-center operators, and local permitting authorities), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L4 (diffusion lag), L2 (constraint migration).
- **Reasoning chain**: New generation and transmission run in years and cannot be compressed in the short term → whoever has existing spare substation capacity and fast approvals receives compute investment first → the value of queue position exceeds the tariff differential (J-057) → a region with higher power prices but a short queue can beat a region with cheap power and a long queue → the geographic distribution of new capacity diverges from the cheapest power.
- **Time window**: 2026–2030.
- **Falsifier**: By 2030, the regional distribution of new compute capacity correlates more strongly with regional electricity prices than with interconnection wait times.
- **Leading indicator**: Regional distribution of new capacity compared against regional queue times and tariffs; publicly stated siting rationales; annual.
- **Confidence**: Medium.
- **depends-on**: J-056, J-057.
- **Strongest opposing mechanism**: Grids accelerate broadly or on-site generation becomes common, so wait times stop discriminating and siting returns to price and climate.
- **Against consensus**: **Mechanism confirmed, the comparison is unavailable, and one source misuse must be corrected.** Agreement: DOE records connection lead times of 1–3 years for hyperscale facilities (300–1000 MW+) and the resulting shift toward co-location with existing generation to get power faster — exactly this card's mechanism that access speed rather than price decides where compute lands (EXT-29); ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30); and Virginia's JLARC records development constrained by substation and transmission capacity in Northern Virginia, the largest US cluster (EXT-28). **Correction**: EXT-19 (LBNL *Queued Up*) covers generation and storage interconnection only and **does not cover load**, so it must not be used as evidence about data-centre siting — this is the most common source misuse in this area and is now flagged in the source index. **Evidence boundary**: this card's falsifier asks which better explains the regional distribution of new capacity, local electricity price or interconnection wait time, and no institution has published such a quantitative comparison, so the test cannot be computed from public data. Why the judgment is retained: the mechanism-side evidence is consistent and comes from official documents, so the judgment stands with confidence at Medium; one leading indicator is added — whether ERCOT-style load-side queue disclosure spreads to PJM, MISO and other markets, which determines when this card becomes falsifiable again.
- **External comparison source**: EXT-28, EXT-29, EXT-30 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-03-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)

### J-064 · If efficiency gains keep outpacing load growth, the constraint in this chain dissolves in the long run (landscape only)

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: If energy per unit of service keeps falling faster than load grows, and schedulable load can migrate freely across regions, this chain's power and permitting constraint dissolves on its own in the long run (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (energy, data-center, and grid research and operations participants), annual; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 (constraint migration), L4 (diffusion lag).
- **Reasoning chain**: The constraint holds only while load growth exceeds deliverable-capacity growth → if efficiency gains and cross-region scheduling both take effect, peak load growth flattens → the queue stops being the binding constraint → the certainty premium and site rents disappear with it.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, compute-related load in major markets still grows faster than deliverable capacity and interconnection wait times show no systematic decline.
- **Leading indicator**: Ratio between the decline in energy per unit of service and the growth of compute service volume, peak load growth, share of cross-region scheduled jobs; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-056, J-058.
- **Strongest opposing mechanism**: Efficiency gains are fully absorbed by rebound demand — cheaper means more used — so load growth rises rather than falls.
- **Against consensus**: **The counter-hypothesis is historically real, but current data points the other way.** Agreement (the side that favours this card): efficiency outrunning load is not wishful — between 2010 and 2018 global data-centre compute instances grew 550% while energy use rose only about 6%, a peer-reviewed eight-year decoupling window (EXT-27). **Divergence and evidence boundary**: the current phase runs the other way — LBNL measures US data centres at about 4.4% of national electricity in 2023 heading to 6.7–12% by 2028 (EXT-26), and the IEA puts data-centre electricity growth at roughly 15% a year over 2024–2030, more than four times the combined growth of all other sectors (EXT-12); decoupling has clearly weakened in the large-model phase. Beyond that, no authority has published a dedicated analysis of an efficiency turning point, and this card's 2033–2040 window lies past the forecast boundary of every source cited here. Why the judgment is retained: kept as this chain's most important counter-hypothesis and not as a basis for action, with confidence not raised; its value is in naming the condition under which this chain's constraint dissolves, not in predicting that it will.
- **External comparison source**: EXT-12, EXT-26, EXT-27 (see the source index above).
- **Source**: [C3: Electrons on the Ground](chains/30-power-land-and-permits.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


## 11. Judgment cards for the far-term social landscape

> This section collects the far-term social-landscape cards (J-043–J-054). They cover cross-domain consequences for agents, real-world signals, human and human–AI relationships, institutions, and meaning; they are not judgments about the order in which technical capabilities appear. Low-confidence cards are explicitly marked landscape only.

### J-043 · High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (organizational buyers and operators of high-value agents), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 constraint migration, L6 irreversibility.
- **Reasoning chain**: Rollback-capable environments lower supervision cost → agents take more steps → supervision shifts to boundaries and escalation → high-value deployment uses boundary grants.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, high-value agents still require step approval and rollback has not lowered supervision cost.
- **Leading indicator**: Boundary-grant share, step approvals, rehearsal procurement; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-031, J-032, J-014.
- **Strongest opposing mechanism**: Liability or regulation requires step approvals.
- **Against consensus**: Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants. Retained as landscape only, with confidence not raised; upgrading requires adoption evidence such as the share of boundary-grant contracts, not the existence of current permission design.
- **External comparison source**: EXT-4, EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-044 · Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (organizations deploying agents, insurers, and liable parties), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L2 constraint migration, L7 institutional lag.
- **Reasoning chain**: Execution scales → tail losses exceed one user’s capacity → collateral and balance sheets become admission conditions → solvent entities support infrastructure.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, solvency does not affect deployment, pricing, or financing.
- **Leading indicator**: Liability premiums, reserves, solvency clauses; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-032, J-040.
- **Strongest opposing mechanism**: Liability is outsourced and losses are too low for a separate asset.
- **Against consensus**: Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished. Retained as landscape only, with confidence not raised; upgrading requires direct evidence that solvency affects deployment, pricing, or financing.
- **External comparison source**: EXT-14, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-045 · As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only).
- **Diffusion-gate review**: audience scale = hundred-million-scale (people and organizations needing unarranged observation of reality), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-046 · High-liability settings retain a premium for field causal records (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: High-liability settings retain a premium for field causal records (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (professionals and organizations in high-liability industries), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
- **Lens**: L5 signals and forgery, L6 irreversibility.
- **Reasoning chain**: Cheap explanations → liable parties distinguish advice from intervention → field records connect action, outcome and compensation → high-liability transactions pay.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, replacing field records with synthetic evidence changes neither accidents nor prices.
- **Leading indicator**: Record licensing, insurance discounts, trial requirements; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-033, J-034.
- **Strongest opposing mechanism**: World models and regulators establish synthetic trials as equivalent.
- **Against consensus**: Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence of price or insurance-rate differences attributable to field causal records.
- **External comparison source**: EXT-7, EXT-11 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-047 · Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only).
- **Diffusion-gate review**: audience scale = hundred-million-scale (people who may use AI companionship), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L1 abundance-to-scarcity, L9 relational asymmetry.
- **Reasoning chain**: Copyable memory, patience and style → companionship scales → copyability reduces exclusivity and shared risk → non-copyable reciprocity is scarce.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, copyable companionship replaces human reciprocity with no behavioral difference.
- **Leading indicator**: Copy rate, exit rate, retention and repair outcomes; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-042.
- **Strongest opposing mechanism**: Institutions accept copyability and preferences change.
- **Against consensus**: Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence. Retained as landscape only, with confidence not raised; upgrading requires long-term behavioral comparisons between copyable companionship and human reciprocity.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-048 · Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only).
- **Diffusion-gate review**: audience scale = hundred-million-scale (individuals, families, and organizations using AI), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails. This card's audience is written as possible users, platform participants, or an affected population: **an estimate of reach is not a count of people repeating the action**, and it is no ground for upgrading the Gate 1 verdict.
- **Lens**: L7 institutional lag, L9 relational asymmetry.
- **Reasoning chain**: Copyable, pausable relationships → memory and commitment boundaries diverge → data, exit and liability conflicts grow → institutions define subjects.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, relationship-data and exit disputes do not persist and ordinary contracts suffice.
- **Leading indicator**: Data disputes, exit clauses, dedicated rules or cases; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-042.
- **Strongest opposing mechanism**: AI remains an ordinary tool covered by existing contracts.
- **Against consensus**: Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint. Retained as landscape only, with confidence not raised; upgrading requires institutional evidence that disputes persist and ordinary contracts are insufficient.
- **External comparison source**: EXT-9, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-049 · As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only).
- **Diffusion-gate review**: audience scale = hundred-million-scale (groups and organizations needing joint commitments), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
- **Lens**: L1 abundance-to-scarcity, L8 human nature and demand.
- **Reasoning chain**: Coordination costs fall → candidates multiply → choosing is not commitment; commitment bears failure → willing groups are scarce.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, more coordination also raises joint bearing of long-term failure and repair is no bottleneck.
- **Leading indicator**: Commitment retention, exit rate, repair time; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-041, J-038.
- **Strongest opposing mechanism**: Agent reputation and arbitration bear risk without human commitment.
- **Against consensus**: Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent. Retained as landscape only, with confidence not raised; upgrading requires comparable data linking increased coordination to the share of jointly borne commitments.
- **External comparison source**: EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-050 · The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only).
- **Diffusion-gate review**: audience scale = hundred-million-scale (workers, organization members, and collaborators), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.” **Scale rationale**: the hundred-million figure here is only a constructed upper bound on the audience (estimated from occupational roles, organizational nodes, or a population in need), not a citable statistic, and it does not establish the society-level threshold of a hundred million distinct individuals performing the same action every week, so Gate 1 still fails.
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-051 · Abundant advice does not automatically disperse real action rights (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Abundant advice does not automatically disperse real action rights (landscape only).
- **Diffusion-gate review**: audience scale = billion-scale (ordinary people affected by institutions and resource allocation), weekly; Gate 1 **FAIL** — the billion-scale figure is a constructed upper bound for people affected, not proof that a billion distinct people repeat the same action weekly; this card concerns institutional/resource-allocation arrangements rather than a repeatable personal consumption action, so it cannot pass the “hundred-million weekly” threshold and remains a landscape/institutional judgment, not a society-wide claim.
- **Lens**: L2 constraint migration, L7 institutional lag.
- **Reasoning chain**: Advice is cheap → information grows → permissions, resources and compensation remain concentrated → advice does not disperse action rights.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, advice growth coincides with broad dispersion of energy, data, licensing, and compensation access.
- **Leading indicator**: Resource concentration, authorization holders, advice-to-action distribution; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-039, J-040, J-035.
- **Strongest opposing mechanism**: Open protocols and competition policy disperse access points.
- **Against consensus**: Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence on how dispersed the key gates of licensing, resource access, and compensation actually are.
- **External comparison source**: EXT-12, EXT-15 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: Gate 1 fails; the billion-scale figure is an upper bound for affected people, not a count of distinct weekly actors; this card remains a low-confidence landscape/institutional judgment and is no longer a society-wide trend claim; original card text retained, identifier not reused, basis: [Retrospect · Gate 1](01-retrospect.md)).


### J-052 · Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only).
- **Diffusion-gate review**: audience scale = ten-million-scale (organizational participants in energy, real-world data, authorization, and compensation regimes), weekly; Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.”
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
- **Status**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see [Historical retrospective · Gate 1](01-retrospect.md).)


### J-053 · As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only).
- **Diffusion-gate review**: audience scale = billion-scale (everyone seeking meaning, identity, and commitment), weekly; Gate 1 **PASS** — may be written as a society-level judgment.
- **Lens**: L1 abundance-to-scarcity, L8 human nature and demand.
- **Reasoning chain**: Generatable output loses distinction → real time, bodily risk and responsibility leave cost signals → personal burden becomes meaning/status signal.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, real responsibility no longer affects trust, status, or long-term choices.
- **Leading indicator**: Trust premium for commitments, experience verification, narrative/outcome coupling; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-042, J-029.
- **Strongest opposing mechanism**: Society stops valuing real responsibility.
- **Against consensus**: Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence. Retained as landscape only, with confidence not raised; upgrading requires generational data on trust, status, or long-term choices.
- **External comparison source**: EXT-9, EXT-17 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.


### J-054 · Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only)

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only).
- **Diffusion-gate review**: audience scale = billion-scale (everyone’s time, bodily risk, and long commitments), daily/weekly; Gate 1 **PASS** — may be written as a society-level judgment.
- **Lens**: L6 irreversibility, L8 human nature and demand.
- **Reasoning chain**: Choice grows but lifetime does not → bodily risk and long commitments remain personal → scarcity moves to non-delegable experience.
- **Time window**: 2033–2040.
- **Falsifier**: By 2040, agent substitution leaves no observable difference in preferences or outcomes around time and risk.
- **Leading indicator**: Non-delegable time, long-commitment completion, embodied premium; annual.
- **Confidence**: Low (landscape only).
- **depends-on**: J-042, J-029.
- **Strongest opposing mechanism**: Immersive agent experience becomes equivalent.
- **Against consensus**: Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven. Retained as landscape only, with confidence not raised; upgrading requires studies on differences in preferences and outcomes after delegated experience substitutes for direct experience.
- **External comparison source**: EXT-9, EXT-10 (see the source index above).
- **Source**: [Far-term landscape](30-far.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.


## 12. Pre-publication checklist

Run the script first, then walk the items it cannot judge:

```
python3 scripts/check.py
```

It covers the machine-checkable half of the list below. Exit code 0 means
pass; otherwise it prints each failure. On the ledger side: internal links and
heading anchors, required card fields, the standalone Audience scale field on
new cards (J-001–J-086 warn during migration; a later identifier fails if the
field is missing), duplicate J identifiers inside either ledger, the confidence
whitelist, dependency edges agreeing in all three places, and bilingual parity
— where "parity" means exactly three things, that the two trees hold the **same
filenames**, the **same judgment-card identifiers**, and the **same number of
`##` sections per same-named file**. It does **not** compare prose, so two files
with the same name saying different things pass. On the README side: the chain
registry and the chain files on disk cover each other in both directions (every
chain file is linked by both registries; every row's files exist, are linked on
both sides, and are named by the `<ID x 10>-` rule; the two registries allocate
the same identifiers), the registry Topic is contained in the corresponding
chain file's H1, every `C<n>` cited anywhere is an identifier the registry
allocated, a chain cited by title carries a title taken verbatim from that
file's own H1 (an abbreviation is allowed, a rename is not), the two languages
state each count the same number of times, and the two counts the READMEs state
— "N judgment cards" and "N independent reasoning chains" — equal what the
repository holds. State the count check's boundary plainly: it reads only those
two fixed phrasings, and its reach is held by the rule that both languages must
state each count the same number of times and may never both fall to zero. A
rewrite on one side is caught; **dropping the same count from both languages in
one commit is not**. One recurring trap: GitHub does **not** collapse runs of
hyphens in heading anchors, so `J-001 · Title` is `#j-001--title`; a short
`#j-001` fragment silently fails to jump (43 of them were repaired in one pass
on 2026-09-19).

The script's own credibility is carried by negative cases:

```
python3 scripts/check.py --self-test
```

It copies the tree into a temporary directory and breaks that copy one way at a
time — dangling anchor, a dependency edge disagreeing with its card, a card in
one language only, **equal bilingual card counts with different identifier
members**, an out-of-whitelist confidence value, a missing required field, a
**new card with Audience scale missing, embedded inside another field, or
structurally incomplete**; a chain file landing on disk with no registry row, a
registry row deleted while its file stays, a row registering one language only,
an identifier registered in one README only, a row linking a file that is not
there, a registry Topic absent from its chain file's H1, the announced-direction
row claiming an identifier, a row id written as `C3 (draft)`, prose citing an
unallocated identifier, a chain cited under a title its file does not carry; a
card count off by one, a count spelled so it cannot be read, a stale chain
count, a count dropped from one language, and the **same J identifier registered
twice** — plus an accept/reject matrix over confidence values and the edits that
must **not** be reported (an abbreviated title citation, a second announced row
holding no number, prose naming cards without counting them). It asserts every
breakage is caught **by the right check**; the repository itself is not modified.
Run it whenever the script changes: on 2026-09-19 the confidence whitelist was
compared by substring, so `极高` ("extremely high", which contains `高`) passed
while every positive case stayed green — only a negative case exposes a
criterion written too wide. The second lesson of that same day is the other
half: `ee3a5eb` claimed "verified against four deliberate breakages" but left
nothing re-runnable behind, and one of the four turned out not to work at all.
**A claim does not count; only a negative case sitting in `NEGATIVE_CASES`,
which the next person can re-run unchanged, counts.**

The remaining items are judgment calls a script cannot make. Walk them by
hand before publishing:

- [ ] Year boundaries match the single authority in `00-method.md`.
- [ ] Every judgment card has ID, proposed date, one-sentence judgment, diffusion-gate review, lens, reasoning chain, time window, falsifier, leading indicator, confidence, depends-on, strongest opposing mechanism, consensus comparison, external comparison source, source, next review, and status; **J-087 and later must also carry a standalone Audience scale field**, not bury scale only inside the diffusion-gate review.
- [ ] Every internal link resolves and returns to the source argument.
- [ ] Chinese and English files are updated as equivalent projections in the same commit.
- [ ] Dependency edges agree in all three places: each card's `depends-on`, the section-3 graph, and the depends-on column of the section-2 overview; the graph covers every registered ID, has no duplicate lines, and has no edge pointing at a non-existent ID.
- [ ] Hard constraints use only the five-item whitelist: physical, legal/liability, trust/relationship, ownership/privacy, or embodied presence.
- [ ] **For every opportunity candidate you can point at the one sentence saying why the scarce item cannot be copied by the same force**: open each candidate in `40-opportunities.md`, find that anti-copying sentence in the prose, and confirm it meets two conditions — the **subject is the scarce item itself** (not the object being protected, and not a demand-side reason of the form "why anyone needs it"), and it is **not a restatement of the irreversibility lens** (per section 3 irreversibility is only a supporting lens, so "the cost of a mistake is real-world damage" does not answer the second question). Any candidate without that sentence falls back to being a window opportunity. The item above can only check the hard constraint's **label**, which does not stop a relabelling: the O-002 of 2026-09-19 landed literally inside the whitelist two rounds in a row while not one sentence in the section answered the second question, and this is the item that caught it.
- [ ] Every card's "Against consensus" field is in one of exactly two acceptable states, and is never simply missing: (a) comparison done — it carries all three elements from `00-method.md` §1.2 (where it agrees, where it diverges or where the evidence ends, and why the judgment is retained or confidence lowered accordingly) plus at least one EXT ID in "External comparison source"; or (b) comparison not done this round — it says "unknown" explicitly per `00-method.md` §1.1 item 4, and "External comparison source" is marked not completed. A bare "consistent with the consensus" without saying where, and an uncompared card that fails to say "unknown", are both non-compliant.

---

## 13. Judgment cards distilled from the historical retrospective

> The seven cards in this section come from [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md), and are this project's first batch of judgments that **depend on no premise about AI at all**: they are induced from cases in technology, politics and business between 1956 and 2020, and would still hold if AI stopped improving tomorrow. J-067 through J-071 are the only roots in the whole ledger that do not depend on J-001.

### J-066 · The five gates are necessary, not sufficient

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: If a capability fails any one of the five diffusion gates it will not become the way a whole society does things; passing all five only means it qualifies to compete, and guarantees nothing.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (researchers, investors, and strategists who make society-level trend judgments), no fixed cadence; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates (induced from historical cases in section 3 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md); not one of the L1–L9 lenses in `00-method.md`).
- **Reasoning chain**: Three self-attack locks are set up first → the third lock demands a case that passes all five gates and still fails → New Coke, 1985, gate by gate: scale (people who drink cola daily number in the billions), substitution (replaces the old Coke — same act, same price, same shelf), carrier (same production line and distribution network, zero marginal deployment cost), decision rights (Coca-Cola decides to produce unilaterally, consumers buy unilaterally), cost (zero learning, zero bodily, zero social cost, and it won blind taste tests) → launched 1985-07-11, the old formula announced back 79 days later → what the gates missed is on the demand side: what people buy is not always the thing itself, Coke sells an identity symbol, and a symbol's value comes precisely from not changing → therefore this gate set can only disprove, never prove → the correct use is "fails a gate ⇒ will essentially not become society-wide," never "passes all gates ⇒ will happen."
- **Time window**: 2026-01 to 2036-12 (the period over which this rule is applied and tested).
- **Falsifier**: A capability that **clearly fails at least one** of the five gates nevertheless reaches society-wide diffusion within ten years (billions of people daily, or hundreds of millions weekly), and its diffusion cannot be explained by an unlock condition already written into this document.
- **Leading indicator**: (1) Every six months, enumerate the capabilities that newly reached society-wide scale in that period, back-fill the five-gate verdict for each, and record whether any counter-example diffused while failing a gate; (2) whether every new society-level judgment written in this project can pass the five-gate test; (3) whether a second "passes all gates, still fails" case appears (that turning true strengthens this card rather than weakening it); observed every six months.
- **Confidence**: Medium.
- **depends-on**: J-067, J-068, J-069, J-070, J-071.
- **Strongest opposing mechanism**: The gate set may be incomplete. If a sixth or seventh veto class exists—for instance the demand-side symbolic value New Coke missed—then “passes all five” carries less information and the card risks tautology. Its defence is the exclusive-case table in section 5 of the [Retrospect](01-retrospect.md), but exclusivity itself is attackable: the first independent review rejected Gate 5's original Dvorak case; the second calibration round used self-service retail to reject the rule that any recurring gross friction vetoes adoption, narrowing J-071 to recurring net burden versus the incumbent. If the next round still cannot find a case stopped only by that net burden, Gate 5 should merge into Gate 2. Stadia and year-round DST add two “passed yet withdrawn” sufficiency counterexamples; they strengthen this card without proving the set complete.
- **Against consensus**: **Agreement**: Rogers 1962's five attributes of an innovation (EXT-33) overlap with this document's Gate 2 and Gate 5 at relative advantage and complexity respectively; Moore 1991 (EXT-35) likewise argues technical success is not the same as crossing into a mass market. **Divergence and evidence boundary**: Rogers's five attributes are scored (higher means faster diffusion); this document rewrites them as veto-style necessary conditions and requires naming a concrete object (which act is replaced, who pays for the carrier, whose hands the decision sits in). A scored framework is nearly unfalsifiable; a veto checklist can be falsified. **Why the judgment is retained**: the cost of the veto-style reading is that every negative verdict rides on the gate set being complete, a cost explicitly acknowledged through the New Coke counter-example and written into both this card and section 6 of the prose, so confidence stays at Medium and is not raised.
- **External comparison source**: EXT-33, EXT-35 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-067 · The audience ceiling of a capability is the headcount and frequency of the activity it serves

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: The upper bound on how many people a capability can affect is set by how many people perform the activity it serves and how often they perform it, not by the ceiling of the technology.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (researchers, investors, and strategists who make society-level trend judgments), no fixed cadence; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 1 (induced from historical cases in section 3 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md)).
- **Reasoning chain**: Enumerate the capabilities that reached society-wide scale, and the activities they serve were already billions-scale and daily before diffusion — smartphones (contacts, looking things up, finding the way, paying; 4.3 billion owners in 2023, 54% of world population), health codes (entering a venue), mobile payment (paying for something) → then enumerate the cases where the technology fully succeeded and still stalled at a niche, and the headcount of the activity served was already insufficient: Concorde (transatlantic passengers willing to pay several times the fare to save three or four hours, hundreds of thousands of trips a year; 20 aircraft built over 27 years, 14 in commercial service), Iridium (calling from places without cellular coverage; 55,000 subscribers at bankruptcy against a break-even in the millions), Esperanto (since 1887 the vast majority of people never once encounter a cross-native-language everyday conversation) → the technology worked in all three; the difference is only the headcount of the activity → therefore you must count people before assessing the technology → and ask one layer deeper: does it raise the ceiling of existing professionals (ceiling = the size of that occupation), or let people who previously could not do it do it (which may enlarge the activity itself).
- **Time window**: 2026-01 to 2036-12.
- **Falsifier**: A capability whose served activity was performed by only millions of people before diffusion nevertheless reaches billions of daily users within five years, and that growth cannot be explained by "it let people who previously could not do it do it, thereby enlarging the activity's headcount itself."
- **Leading indicator**: (1) Whether every new society-level assertion in this project states the order of magnitude and frequency of the activity's headcount; (2) every six months, observe the capabilities newly reaching billions scale and the pre-diffusion headcount of the activity they serve; (3) whether a counter-example appears in which the activity's headcount did not change while the audience exploded; observed every six months.
- **Confidence**: Medium.
- **depends-on**: —
- **Strongest opposing mechanism**: An activity can be created by the capability itself. Shooting short video was not a billion-person activity before smartphones; the capability enlarged the activity. If Gate 1 is allowed to ask about "potential headcount" rather than "current headcount," the gate becomes markedly looser and can slide into unfalsifiability — any capability can claim it will create demand. This card's defence is to require "letting people who previously could not do it do it" to be a named, checkable mechanism rather than a disclaimer; but that defence rests on writing discipline, not on a formal constraint.
- **Against consensus**: **Agreement**: diffusion research broadly accepts that adoption has a ceiling. **Divergence and evidence boundary**: this is a genuine gap in the literature — this round's search found no existing diffusion framework that uses "the headcount and frequency of the activity served" as a prior screening variable: Rogers's five attributes characterize the innovation itself (EXT-33), and Bass 1969 treats market potential m as an **exogenously given parameter** (EXT-38); neither asks how many people actually perform the activity, which is exactly the quantity Gate 1 asks about. **Why the judgment is retained**: three failure cases (Concorde, Iridium, Esperanto) all succeeded technically and share exactly one feature — insufficient headcount for the activity — and that shared feature is enough to support the judgment; but because no external framework has ever calibrated it, confidence is no higher than Medium.
- **External comparison source**: EXT-33, EXT-38 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-068 · What diffuses replaces an activity already happening, not something added on top

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: Capabilities that diffuse all replace one concrete activity the user already performs today; anything that replaces nothing and merely adds one more thing is capped at hobbyists.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (researchers, investors, and strategists who make society-level trend judgments), no fixed cadence; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 2 (induced from historical cases in section 3 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md)).
- **Reasoning chain**: Adopting a new capability costs a fixed price in learning, purchase and process change → that price only pays off when there is an old activity to offset it against → replace nothing and the benefit must justify itself from scratch, so adoption runs on curiosity alone, and the stock of curiosity is exactly the headcount of hobbyists → passing side: containerization replaced break-bulk loading ($5.83 per ton in 1956 → 15.8 cents per ton, roughly a 97% drop), China's household responsibility system replaced work-point accounting (same land, same people; what changed was who bore the monitoring cost), QR-code payment replaced pulling out cash, making change and reconciling → blocked side: Google Glass replaced no activity and instead added a thing on your face ($1,500 in 2013, withdrawn January 2015), 3D television added an extra-cost attribute to "watching television" (ESPN 3D launched 2010-06-11, closed 2013-09-30), MOOCs **replaced the wrong object** — they replaced attending lectures, while what students buy is the credential, and the credential was not replaced at all (median completion rate of 12.6% in peer-reviewed work) → the veto condition is therefore exactly one: replaces nothing; the size of the cost drop is not a pass mark but a speed variable.
- **Time window**: 2026-01 to 2036-12.
- **Falsifier**: A capability that **replaces no existing concrete activity and is purely additive** reaches society-wide diffusion within five years (billions daily or hundreds of millions weekly), and its adoption is driven neither by coercion nor by a single subsidizing party.
- **Leading indicator**: (1) Whether every new judgment can name the concrete, countable activity, already happening at the time, that it replaces; (2) the split between "purely additive" and "substitutive" among the period's fast-growing products; (3) whether new cases of replacing the wrong object appear (the surface activity replaced while what the user actually buys is not); observed every six months.
- **Confidence**: Medium.
- **depends-on**: —
- **Strongest opposing mechanism**: "What it replaces" can be defined flexibly after the fact. Anything new can be described as replacing "boredom" or "the old use of attention"; if the replaced object can be named arbitrarily, this gate degenerates into unfalsifiability. The card's defence is to require naming a **concrete, countable activity that was already happening**, but that defence is writing discipline rather than a formal constraint — an author willing to be vague can walk around it.
- **Against consensus**: **Agreement**: heavily overlapping with relative advantage among Rogers 1962's five attributes (EXT-33); diffusion research has long accepted relative advantage as an explanatory variable for diffusion speed. **Divergence and evidence boundary**: this document rewrites it from a scored dimension into a veto condition, and narrows the veto condition to the single item of substitution versus addition — the size of the cost drop is explicitly demoted to a speed variable, because this document's own passing case (the household responsibility system) did not cut unit cost by an order of magnitude, and writing an order of magnitude into the pass mark would have this gate falsified by its own evidence. **Why the judgment is retained**: this narrowing is a proactive correction made before landing, at the cost of weakening Gate 2's power to say no (it can now only block the purely additive), which is stated in section 3 of the prose; confidence therefore stays at Medium.
- **External comparison source**: EXT-33 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-069 · Infrastructure that serves only one capability does not get built

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: If the new infrastructure a capability requires has no second use and no independent revenue source, that infrastructure either does not get built, or the capability must wait until someone else builds it for other reasons.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (researchers and decision-makers judging infrastructure), no fixed cadence; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 3 (induced from historical cases in section 3 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md)).
- **Reasoning chain**: The 1964 Picturephone needed dedicated broadband loops and dedicated terminals, and that equipment had no second use beyond Picturephone → AT&T had to bear the entire cost alone and recover it from a user base that did not yet exist → Pittsburgh peaked at 32 sets and Chicago at 453, under 500 in total → video calling in 2020 required no dedicated infrastructure whatsoever: front cameras, broadband and screens were already in billions of pockets **for other reasons**, and the adopter's marginal hardware cost was zero → Zoom's daily meeting participants went from 10 million to 300 million in three months → the demand had not changed and the technology had not changed; what changed was who paid for the carrier → contrast: US television broadcast towers genuinely were newly built dedicated infrastructure, but they had an independent revenue source (advertising), so they got built (household ownership roughly 1% in 1948 → roughly 75% in 1955); health codes ran inside the already-installed Alipay and WeChat and made nobody install a new app → counter-example side: Iridium's 66 satellites plus dedicated handsets cost roughly $5 billion and existed for one thing only; Better Place's battery swapping needed both a station network and redesigned cars, and went bankrupt in May 2013 after raising about $850 million.
- **Time window**: 2026-01 to 2036-12.
- **Falsifier**: A capability requiring wholly new dedicated infrastructure that has neither a second use nor an independent revenue source, and for which no single party pays in full, nevertheless reaches society-wide diffusion within ten years.
- **Leading indicator**: (1) Whether every judgment with a time window answers "who pays for the carrier"; (2) among the capabilities currently blocked, whether the resistance can be attributed to a missing carrier; (3) whether events of the form "the carrier got built for other reasons" unlock an existing judgment (such events are the trigger for revising time windows); observed every six months.
- **Confidence**: Medium.
- **depends-on**: —
- **Strongest opposing mechanism**: National industrial policy can pay for dedicated infrastructure directly (high-speed rail, 5G, charging networks), in which case "no second use" stops being resistance at all. If so, Gate 3 is really a special case of Gate 4 clause (b) (a single subsidizing party), and **by the exclusivity rule of section 5 it should be merged into Gate 4 or Gate 2**. Section 5 of the prose puts this merger risk in plain sight and identifies the hydrogen fuel-cell car row as its weakest support.
- **Against consensus**: **Agreement**: the literature has adjacent concepts — Teece 1986's complementary assets, installed base in the network-effects literature, and Zittrain 2006's generativity (EXT-37). **Divergence and evidence boundary**: those answer "who can profit from an innovation" and "why general platforms grow unanticipated applications," whereas Gate 3 asks a prior existence question: will this dedicated infrastructure be built at all. This round found no existing framework that poses that question on its own. **Why the judgment is retained**: Picturephone 1964 versus 2020 is a natural control pair — same demand, same technology, different carrier — and the mechanism is clear enough; but because the merger risk between Gate 3 and Gate 4(b) has not been ruled out, confidence is no higher than Medium.
- **External comparison source**: EXT-37 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-070 · When many parties must change together, change needs enforceable and observable authority, a single subsidizing party, or a local closed loop

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: If adoption requires many parties to change at once, change moves beyond pilots only when one of three holds: a party that can both compel and observe compliance, a single party able to subsidize everyone's start-up cost at once, or a local closed loop that need not wait for the whole society.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (institution designers and researchers judging institutions), no fixed cadence; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 4 (induced from historical cases in section 3 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md)).
- **Reasoning chain**: Adoption decidable by one party passes automatically (ATMs: the bank deploys unilaterally, the depositor uses unilaterally; Barclays Enfield, 1967-06-27) → when many parties must change at once, each party's optimal strategy is to wait, so it stalls at pilots → unlock path (a) enforceable and observable: health codes could both be compelled and be seen being enforced at every venue entrance, rolled out nationwide in months; the household responsibility system went from 18 households in Xiaogang in 1978 → 51% of production teams in Anhui by end-1979 → the 1982 Central Document No. 1 → full rollout in 1983 → the other half of (a), by contradiction: Prohibition could compel but could **not see** — roughly 1,520 federal agents for a population of 106 million (about one per 70,000), with 30,000 to 100,000 speakeasies in New York City alone; repealed in 1933 → unlock path (b) a single subsidizing party: the 1958 BankAmericard Fresno drop mailed roughly 60,000 pre-activated cards to residents who had not applied, buying an entire city's start-up cost outright off its own balance sheet → unlock path (c) a local closed loop: the 1975 US Metric Conversion Act said in so many words that conversion was "wholly voluntary," with no deadline and no penalty; the Metric Board was abolished in 1982 and everyday life never converted, **yet science, medicine and the military use metric completely** — both sides of (c) appear inside the same case.
- **Time window**: 2026-01 to 2036-12.
- **Falsifier**: A case of adoption requiring many parties to change at once reaches society-wide diffusion while **none** of the three unlock paths holds.
- **Leading indicator**: (1) Whether every judgment involving coordination names the holder of decision rights and the unlock path; (2) among coordination-type capabilities stalled at pilots, whether the blockage can be attributed to the absence of all three paths; (3) whether large-scale coordination is ever completed spontaneously by network effects alone (that turning true triggers the falsifier directly); observed every six months.
- **Confidence**: Medium.
- **depends-on**: —
- **Strongest opposing mechanism**: The three unlock paths may be incomplete. The diffusion of fax machines and email involved neither coercion nor a single subsidizing party, and does not obviously look like a local closed loop either — if they really travelled a fourth path of "spontaneous coordination by pure network effects," then this card's three-way split is incomplete. A possible defence is that both began inside and between firms, which is a local closed loop, and spilled outward from there; but that defence smells of post-hoc accommodation, and **this card states it here rather than hiding it precisely because "local closed loop" is the one of the three paths most easily stretched into a universal explanation**.
- **Against consensus**: **Agreement**: consistent with Olson 1965, *The Logic of Collective Action* — rational self-interested individuals do not automatically act for a common interest unless the group is small or coercion and selective incentives exist (EXT-36); this document's three unlock paths map one-to-one onto Olson's coercion, selective incentives and small groups. Also consistent with the path-dependence and network-externality literature (EXT-34): the value of adopting depends on whether others adopt, which is exactly the source of difficulty in multi-party coordination. **Divergence and evidence boundary**: this document's increment is the half-clause inside (a) that enforcement must be observable — Olson discusses coercion, not the observability of coercion; that half comes from contrasting Prohibition (could compel, could not see, failed) with US metrication (no compulsion, no penalty, failed). **Why the judgment is retained**: that half-clause is supported by two cases pointing in opposite directions, but observability has never been tested on its own by any external framework, and the completeness of the three paths is in doubt (see the opposing mechanism), so confidence stays at Medium.
- **External comparison source**: EXT-34, EXT-36 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-071 · Recurring net burden, not gross friction, sets the voluntary-adoption ceiling

- **Proposed date**: 2026-09-19; **revised date**: 2026-09-21.
- **One-sentence judgment**: Voluntary adoption must compare **recurring net burden relative to the real incumbent**: added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost. Only a positive, material burden that accumulates with frequency pushes the ceiling far below the activity population.
- **Diffusion-gate review**: audience scale = hundred-thousand-scale (researchers and practitioners judging adoption cost structure), no fixed cadence; Gate 1 **FAIL** — this is a test, not a predicted society-wide consumption activity, so it is written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 5; an in-place narrowing of the old “one-time costs can be subsidized, recurring costs cannot.”
- **Reasoning chain**: The old rule treated any per-use friction as burden → Piggly Wiggly's 1916 self-service store made shoppers repeatedly walk the aisles, compare, and pick goods, yet expanded rapidly and helped make self-service the supermarket's basic form (EXT-55) → therefore recurring labor alone cannot veto adoption; the ledger must subtract waiting, price, time, and process savings from it → the failure side remains: contact lenses add repeated insertion and care relative to frames, 3D television adds glasses and viewing-position constraints, and Google Glass adds recurring social friction → seat belts show that compulsion can bypass voluntary net burden → the current rule vetoes only when **voluntary adoption carries a positive, material recurring net burden**.
- **Time window**: 2026-01 to 2036-12.
- **Falsifier**: Under voluntary adoption (no compulsion, no ongoing subsidy), a capability with a materially positive recurring net burden versus the real incumbent reaches majority adoption (>50%) of the population performing the activity within ten years; or calibration cannot find a case stopped only by recurring net burden rather than Gate 2 replacement.
- **Leading indicator**: (1) whether new judgments record both added friction and saved waiting / price / time / process cost; (2) whether failure cases' net burden can be computed from as-of evidence; (3) whether high-retention products sustain a materially positive recurring net burden; observed every six months.
- **Confidence**: Medium.
- **depends-on**: —
- **Strongest opposing mechanism**: Net burden may simply restate Rogers's relative advantage, making Gate 5 inseparable from Gate 2. The gates remain separate for now because Gate 2 asks whether a real incumbent activity is replaced, while Gate 5 asks whether each use is materially net heavier after replacement. If the next round cannot find an exclusive case, merge them rather than adding another narrative patch.
- **Against consensus**: **Agreement**: partly overlaps Rogers 1962's complexity and relative advantage (EXT-33). **Divergence and evidence boundary**: this card turns per-use net burden into a necessary-condition veto, whereas Rogers uses scored attributes; self-service retail refutes the gross-friction version but does not by itself prove the net-burden version. **Why the judgment is retained**: success-side self-service retail and failure-side contact lenses / 3D television / Google Glass force net accounting, but do not justify raising confidence.
- **External comparison source**: EXT-33, EXT-39, EXT-40, EXT-55 (see the source index above).
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: REVISED.

### J-072 · Choosing one from dozens of generated candidates is an occupational judgment, not a society-level trend

- **Proposed date**: 2026-09-19
- **One-sentence judgment**: The activity "faced with a batch of already-generated candidates, pick one and own the outcome" is performed by a global population in the millions at weekly frequency, so any scarcity derived from it is an occupational judgment and must not be written in a society-level voice.
- **Diffusion-gate review**: audience scale = million-scale (professionals deciding in product, marketing, R&D, and organizations), weekly; Gate 1 **FAIL** — this card is the test itself, not a predicted society-wide consumption activity, so its status is not downgraded; written as an occupational judgment.
- **Lens**: Diffusion gates · Gate 1 (from the back-check of this project's own judgments in section 7 of [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md)).
- **Reasoning chain**: Define the activity — faced with a batch of already-generated candidates, pick one and own the outcome → whoever performs it must satisfy three conditions at once: an occupation that requires producing candidates in batches (advertising and marketing creative, design and product, architectural and engineering schemes, consulting proposals), personal authority to decide rather than to execute, and a frequency of at least once a week → people satisfying all three concentrate in the decision layer of those roles, and by role structure the global order of magnitude is 10⁶ at weekly frequency → gate by gate: Gate 2 passes (replaces "make three versions first, then choose among the three"), Gate 3 passes (rides on already-diffused generation tools), Gate 4 passes (one person decides unilaterally), Gate 5 is borderline (candidates to review go from 3 to 60, so the attention cost rises), **Gate 1 fails** (millions at weekly frequency, two to three orders of magnitude below the society-wide threshold of billions daily or hundreds of millions weekly) → what actually passes Gate 1 on the same chain is not choosing but making: "needing a usable document, diagram, copy or program" is something billions of people occasionally need, and most of them previously could not do it, which belongs to the "lets people who previously could not do it do it" class.
- **Time window**: 2026-01 to 2031-12.
- **Falsifier**: By the end of 2031, citable statistics show that the population who "pick one from batch candidates and own the outcome" has reached hundreds of millions at weekly-or-higher frequency, or the activity is shown to have spread into the everyday decisions of non-professionals.
- **Leading indicator**: (1) Whether citable global role statistics appear that could replace this card's constructed estimate; (2) whether "generate dozens of candidates at once for the user to pick from" becomes the default interaction in consumer products (that turning true enlarges the activity's headcount and strikes this card directly); (3) whether downstream judgments in this project's C1 chain that depend on "choice becoming scarce" have had their audience voice narrowed per this card; observed every six months.
- **Confidence**: Medium.
- **depends-on**: J-066, J-067.
- **Strongest opposing mechanism**: The activity's headcount can be enlarged by the capability itself. If "generate candidates in batches, then pick one" moves from an occupational behaviour to something billions of people also do in consumer decisions (asking AI for 60 travel plans, 60 résumé versions), the ceiling in the millions fails and this card should be narrowed or withdrawn. This is precisely J-067's own strongest opposing mechanism projected onto this card. A second independent objection: this card's order of magnitude is a **constructed estimate rather than a statistic** — no citable global role data was obtained this round, and the construction itself (three simultaneously satisfied conditions) is attackable.
- **Against consensus**: Comparison not completed this round: unknown. This card's audience magnitude comes from a constructed estimate; no citable global role statistics were obtained this round and it was not compared against any external judgment. Per `00-method.md` §1.1 item 4 it is explicitly marked unknown, must not be used as compared, and the three elements are to be completed next round.
- **External comparison source**: Comparison not completed this round.
- **Source**: [Retrospect: What It Takes to Become a Society-Wide Habit](01-retrospect.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

---

## 14. Judgment cards for the C4 embodied-intelligence chain

> The six cards in this section come from [C4: Embodied Intelligence](chains/40-embodied-intelligence.md) and were registered on 2026-09-20. By convention the chain's prose allocates no judgment identifiers; the complete card fields are registered here. J-073 is the chain's core judgment; J-074 through J-078 are the per-square judgments for care, warehousing and logistics, manufacturing and assembly, agriculture, and construction and domestic work, and all of them stand on J-073 and J-066. **All six cards are written as occupational/organizational judgments**: what they judge is the order in which embodied capability arrives in which scenes, not a daily activity of "the whole society," and each card carries its own Gate 1 verdict.

### J-073 · Embodied intelligence is the necessary complement for AI to reach the physical-labour population, not a sufficient condition for diffusion

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: As long as AI can only move information, Gate 1 holds its audience ceiling down to "the share of people whose work surface is a screen"; being able to move mass, be present on site, and touch a human body is the **necessary complement** that changes that denominator, but changing the denominator only opens Gate 1 — Gates 2 through 5 do not open automatically as model capability improves, so embodiment is **not** a sufficient condition for society-level diffusion.
- **Diffusion-gate review**: audience scale = billion-scale (the global workforce whose main work is moving mass, being present on site, or touching a human body, including unpaid household labour); Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20, this billion-scale figure is a constructed upper bound that adds up **several different activities** (agriculture, domestic work, material handling, care, construction), and the card does not establish that a billion distinct individuals perform the same action daily; an estimate of reach is not a count of people repeating an action. The card is therefore written as an occupational/organizational judgment from the start, must not be cited in a "whole society" or "universal" voice, and is registered directly as ACTIVE, with no downgrade at issue. **Gate 1's second question**: while it can only move information, AI can only **raise the ceiling of existing professionals** (the ceiling is the headcount of the occupations whose work surface is a screen, inside which penetration can approach 100%); to **let people who previously could not do it do it** — and thereby enlarge the activity itself — a body is required first, and the only nameable instance in this chain is contact transfer performed at home by a family member, which J-074 judges not to hold inside this window.
- **Lens**: Diffusion gates · Gate 1, plus L2 constraint migration and L4 diffusion lag.
- **Reasoning chain**: Gate 1's test is a single sentence — how many people perform the activity this capability serves, and how often → people whose work surface is a screen and whose output is information are a **minority** of global employment (the best-paying roles, but not most of the population); the population sits where someone must move mass, stay on site, or touch another person's body: agricultural employment is still **hundreds of millions** (EXT-41), domestic workers are a separately counted group in the **tens of millions** (EXT-42), and in the United States alone hand material movers and home health aides are each **millions**-scale occupations (EXT-43) → therefore an AI that can only move information has its ceiling pinned to screen professionals; inside that ceiling it can be an excellent business, but by the diffusion-gate reading it will never become the way a whole society does things → the only route to a different denominator is to extend what AI can move from bits to mass → **but changing the denominator only opens Gate 1**: Gate 2 demands replacing an activity already performed today (the transfer robot replaced "lifting," not "being there," and what the buyer buys is the latter); Gate 3's carrier is physical space itself (corridor widths, floor flatness, connector standards, workcell retrofits, row spacing — nobody has built any of it for other reasons); Gate 4 requires nurses, families, insurers and regulators to nod at once; Gate 5's preparation, supervision, cleaning, fault handling and social awkwardness are paid on every use and never amortize → then the two curves: perception and policy fall along the software curve (fast variable), while actuators, reducers, torque sensors, batteries, deployment hours and priced liability fall along industrial and institutional curves (slow variables, typically single-digit percent per year) → the binding constraint therefore migrates from "model capability" to **cost per task + priced liability + deployment hours** → **when cost per task crosses labour**: only in squares that are structured, high-frequency, and whose object is semi-cooperative or inanimate does it cross first (milking, pallet handling, goods-to-person, fixed-station welding and painting; 2026–2030); squares that are unstructured but whose environment can be rebuilt cross at 2028–2034; touching human bodies and one-off sites cross at 2032–2040, and first in institutions and on job sites rather than in homes; open-ended household tasks do not cross inside this window → and crossing only means procurement departments start doing the arithmetic, not that the practice diffuses: **beating labour cost locally ≠ society-level diffusion** → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (every warehouse, plot and dwelling is a private, non-identical on-site input that compute cannot copy); neither can be copied away by the same force that produced the abundance.
- **Time window**: 2026–2040.
- **Falsifier**: By the end of 2035, citable statistics show that the repeat users of some **purely informational** capability (moving no mass, never present on site, never touching a body) are no longer mainly people whose work surface is a screen, and that they number a billion daily or hundreds of millions weekly — that falsifies the "embodiment is the necessary complement" half. The other half has its own test: if by the end of 2033 cost per task for embodied systems falls in step with model capability (no longer decoupled from the software curve), deployment hours per unit fall markedly with cumulative installed base, and a generally available insurance product with quotable rates covers embodied work, then the "not a sufficient condition" half should be narrowed.
- **Leading indicator**: (1) the time series of cost per task for embodied systems (per piece, per effective operating hour) and whether it is decoupled from the model-capability curve; (2) dedicated insurance products, quotable rates, and the first liability rulings for embodied work; (3) the learning curve of deployment hours per unit against cumulative installed base, and the ratio of integrator service revenue to equipment revenue; (4) whether headcount and wages in occupational series (EXT-43's 53-7062 and 31-1121) diverge in adoption-dense regions ahead of the national series — a US-only observation window that must not be used as a global indicator; annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-066, J-067, J-068, J-069, J-070, J-071.
- **Strongest opposing mechanism**: Three mechanisms, each independent and each able on its own to cut the chain from "capability arrives" to "bodies diffuse." (1) **Hardware cost per task does not fall with model capability**: actuators, reducers and batteries travel the industrial manufacturing curve at typically single-digit percent per year; if capex, maintenance, spares and downtime are all amortized in and the total still exceeds labour, no amount of model capability gets it adopted — the adoption decision looks at cost per piece. (2) **Failure liability cannot be priced**: insurance needs actuarial data, actuarial data needs deployment scale, deployment scale needs affordable premiums — a self-closing loop; if it never opens, embodied deployment stays inside large enterprises that can self-insure, and **AI changed the denominator only for another equally small denominator**. (3) **Scene fragmentation defeats economies of scale**: every deployment is an on-site engineering job, so the scale effect lands on integrator labour and embodied intelligence becomes a service business — and service businesses do not diffuse exponentially. If any one of the three holds for long, this chain is left with a handful of **local crossing points** rather than a road to society-level diffusion. One further objection points the other way: this card's population arithmetic is **orders of magnitude**, not precise global statistics (O\*NET covers the United States only; FAO's and ILO's definitions and years are in the sources), so if the true size of "people whose work surface is a screen" is far larger than assumed here, the tightness of Gate 1 is overstated.
- **Against consensus**: **The mechanism agrees, but external sources only reach the two ends; nothing calibrates the arrival order in between.** Agreement: IFR reports that factory demand for robots doubled over ten years (EXT-45), which proves embodied capability **can** genuinely diffuse; Abundant Robotics shut its business down after reaching field-capable apple harvesting (EXT-46), which proves **technical feasibility is not commercial feasibility** — the second point coincides closely with this chain's independent reasoning and must be labelled honestly: **it is not this card's discovery; this card's increment is a structural explanation of such failures (utilization × fragmentation) plus observable leading indicators.** **Divergence and evidence boundary**: most external material discusses **installed totals** or **single cases**, while this card is about **arrival order** and **where the constraint sits**, and the former does not imply the latter; the key data not obtained this round is recorded as explicit gaps — cost-per-task time series by scene, insurance rates and liability rulings for embodied work, the learning curve of deployment hours per unit, and deployment scale and retention in care — none of which has a publicly checkable definition, so this card **uses** no precise global figure at all. **Why the judgment is retained**: the core argument depends on none of those missing numbers; it depends on an objective structural difference — perception and policy fall along the software curve while actuators, deployment and liability fall along industrial and institutional curves — and the gap between those slopes can be observed. But because nobody has calibrated the arrival order in between, confidence stays at Medium and is not raised.
- **External comparison source**: EXT-41, EXT-42, EXT-43, EXT-45, EXT-46 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-074 · Contact transfer in care crosses inside institutions first, and homes reach no society-level diffusion inside this window

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: Care is the square with the most certain demand, but what blocks it is not "can it lift" — it is "the person is alive throughout" plus the cost paid afresh on every single use; contact bed-to-chair transfer becomes standard institutional equipment no earlier than 2032–2038, and first in the handful of countries with the highest labour costs and heaviest nursing-injury compensation exposure, while home settings reach no society-level diffusion inside this window (to 2040).
- **Diffusion-gate review**: audience scale = hundred-million-scale (care workers and care recipients worldwide, in institutions and at home), daily; Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20 this hundred-million-scale figure is a constructed upper bound from a population in need and a role structure, not a citable statistic, and nothing in it establishes a hundred million distinct individuals performing the same action every week. The card is written as an occupational/organizational judgment and registered directly as ACTIVE. **Gate 1's second question**: the institutional case **raises the ceiling of existing professionals** (the ceiling is the nursing workforce; the machine replaces only the "lifting" third of a transfer), while the home case is the one that would **let people who previously could not do it do it** (a family member without the physical strength completing a transfer alone, which could enlarge the activity itself) — and it is precisely the latter that does not hold inside this window, which is this card's most important sentence.
- **Lens**: Diffusion gates · Gates 3 and 5, plus L4 diffusion lag, L8 human nature and demand, and L6 irreversibility.
- **Reasoning chain**: Demographics make care the most certain demand (the number of people needing care rises, the number willing to do the work falls), and the gap cannot be closed by processing information — nobody lifts an elderly person from a bed into a wheelchair through a screen → the technical bottleneck is not load but that the person is alive: the same transfer needs a completely different torque trajectory for different weights, muscle tone and pain tolerance, and the person shifts posture, resists, or suddenly goes slack, which demands millimetre-scale position accuracy and newton-scale force control in one loop bounded by a human safety margin → Riken's ROBEAR demonstrated the capability side clearly in 2015 (EXT-44), and a decade later it is still not standard ward equipment: **the decade of silence is itself the evidence that what blocks this square is not capability** → what blocks it is Gate 5: preparation, supervision, cleaning, explaining and reassuring are paid every time and never amortize (the machine sent back in the chain's opening section completed twelve transfers in its first week with no pinch injury, and price appears nowhere in the reason it was returned) → compounded by Gate 3: a home additionally needs door widths, floors and bathrooms rebuilt, and nobody has built them for other reasons → compounded by Gate 4: putting a robot in a ward needs nurses, families, insurers and regulators to nod at once → **when cost per task crosses labour**: it is entirely plausible that a large institution in a high-wage country pushes the per-transfer cost below the wage cost of two aides, and at that moment the numbers work — while Gates 5 and 3 still stand in the way, so **crossing only means the procurement department starts doing the arithmetic, not that the practice reaches most of the people receiving care** → **Hard constraints**: **embodied presence** (the need itself requires someone to be physically there and to touch) compounded by **law / liability** (a party capable of being sued must carry a transfer accident); automating rostering, medication checks and fall-risk scoring completely removes not one transfer that must physically happen.
- **Time window**: 2026–2038.
- **Falsifier**: By the end of 2031, contact bed-to-chair transfer robots are standard institutional equipment in any major care market (verifiable through a reimbursement code, counting equipment against required staffing, or national installed-base coverage) — that falsifies this card's lower bound; or, before 2040, home contact transfer reaches daily use in hundreds of millions of households — that falsifies this card's home judgment.
- **Leading indicator**: (1) whether regulators open a distinct approval pathway for contact transfer robots and whether a reimbursement code exists — without reimbursement, institutions buy from their own budget and the adoption curve stays flat; (2) whether staffing standards allow equipment to be counted against required headcount (that is the line that decides ROI, not the purchase price); (3) whether back-injury compensation rates fall in institutions with dense adoption — the hardest indicator to fake, because insurers rather than vendors produce it; (4) whether a production successor to a ROBEAR-class prototype ever appears; annually.
- **Confidence**: Medium.
- **depends-on**: J-073, J-066.
- **Strongest opposing mechanism**: If regulators or insurers break the liability-pricing loop by taking the first half-step (pilot rates and reimbursement codes for constrained settings, trading bounded deployment for actuarial data), the institutional window moves forward as a whole. The opposite objection: if the loop never opens, contact transfer stays forever inside large institutions that can self-insure, and this card is too optimistic even about the institutional side. A third, independent objection: this card treats "a decade of silence" as evidence of non-capability factors, but the silence could equally come from funding and market size rather than from Gates 3 and 5 — an explanation this round has no independent evidence to exclude.
- **Against consensus**: **Agreement**: a ROBEAR-class prototype (EXT-44) proves the capability side of contact transfer was demonstrated a decade ago, which is the premise for "the silence cannot be explained by capability"; US occupational data lists home health aides among the fastest-growing occupations (EXT-43), consistent with "the most certain demand." **Divergence and evidence boundary**: the external material establishes one prototype and one country's occupational outlook, and covers no **arrival order**; this round found no checkable source on whether a production successor to ROBEAR exists, and none on deployment scale or retention in care worldwide — both recorded as gaps; EXT-43 covers the United States only and cannot be extrapolated globally. **Why the judgment is retained**: the argument depends on no deployment-scale figure; it depends on recurring costs that do not amortize and on a compensable party that must be suable, neither of which opens as model capability improves. But with deployment and retention data missing, confidence stays at Medium.
- **External comparison source**: EXT-43, EXT-44 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-075 · Warehousing's bottleneck has moved from moving to grasping: unstructured picking arrives first and door-to-door delivery does not hold inside this window

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: Warehousing is where embodied intelligence pencils out first (goods feel no pain, the building belongs to one legal entity, the floor is flat), and what is actually stuck is the cost of the failure tail in unstructured picking; scaled single-item picking in controlled large warehouses sits conservatively at 2028–2033, while door-to-door last-mile delivery does not hold inside this window because it trips Gate 3 and Gate 4 at once.
- **Diffusion-gate review**: audience scale = hundred-million-scale (warehousing, material-handling and delivery workers worldwide; in the United States alone "hand laborers and freight, stock and material movers" is already a millions-scale occupation, EXT-43), daily; Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20 this is a constructed upper bound from role structure rather than a citable statistic, and an estimate of reach is not a count of people repeating an action. The card is written as an occupational/organizational judgment and registered directly as ACTIVE. **Gate 1's second question**: this square **raises the ceiling of existing professionals** (the ceiling is the headcount of handling and picking roles, and the machine replaces the most structured segment of those roles); it does **not** let people who previously could not do it do it — no mechanism here enlarges the headcount of "picking" itself.
- **Lens**: L2 constraint migration and L4 diffusion lag, plus Diffusion gates · Gates 3 and 4.
- **Reasoning chain**: Autonomous mobility inside a structured warehouse is largely a solved problem (flat floors, mappable paths, stop-on-anomaly) → what is stuck is **unstructured picking**: mixed SKUs, transparent and reflective packaging, soft polybags, occluded stacks, the last item at the bottom of a tote → the difficulty is not average success rate but **the cost of the failure tail**: a missed grasp costs seconds, a mis-pick costs a rework of the whole fulfilment chain plus reputation → so the engineering target is not "can it pick" but picks per hour, error rate, and who takes over after a failure → structured movement, pallet handling and goods-to-person are already diffusing (continuing through 2026–2028), while scaled unstructured single-item picking in controlled large warehouses sits conservatively at 2028–2033 → door-to-door delivery faces stairs, entry systems, rain, dogs and unattended parcels: the carrier is someone else's stairwell (Gate 3) and building management, residents and platforms must all change (Gate 4), so it does not hold inside this window → **when cost per task crosses labour**: a single high-throughput, single-shift, tidy-SKU warehouse already pencils out, and the test is whether **per-pick pricing** appears (per picked item, with error-rate damages) — a vendor willing to price its own failure tail is the most honest signal of maturity → but the tail of global warehousing is small and mid-sized sites: low throughput, mixed goods, seasonal swings, a day of downtime hitting every order, so **capex does not amortize and downtime risk cannot be spread — and that is exactly where most material-handling jobs are**; treating the large-warehouse case as the sector's case inverts Gate 1, counting how many warehouses a machine can enter rather than how many people's activity it can replace → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (layout, SKU master data and order flow are private assets, any retrofit needs the owner's consent, and negotiation cost does not fall with model capability).
- **Time window**: 2026–2033.
- **Falsifier**: By the end of 2028, unstructured single-item picking is operating at scale in controlled large warehouses (per-pick pricing with error-rate damages having become the mainstream commercial model in that segment) — that falsifies this card's mid-segment window; or by the end of 2033 robotic door-to-door delivery is the mainstream delivery mode in any major market (a majority of that market's parcels) — that falsifies this card's last-mile judgment.
- **Leading indicator**: (1) whether the commercial model shifts from selling machines to **per-pick pricing** with error-rate damages; (2) whether third-party logistics insurance quotes a separate rate for robotic picking; (3) whether deployment hours per site fall as the installed base grows; (4) whether hiring volumes and wages in occupations like O\*NET 53-7062 (EXT-43) diverge in adoption-dense regions ahead of the national series; annually.
- **Confidence**: Medium.
- **depends-on**: J-073, J-066.
- **Strongest opposing mechanism**: If fragmentation is dissolved at scale by standardized pallets, standardized totes and common interfaces, deployment hours will fall with installed base and this card's mid-segment window moves forward as a whole. The opposite objection: if per-pick pricing never appears, vendors themselves are unwilling to price the failure tail and the 2028–2033 segment should move back as a whole. A third, independent objection: this card separates "the large warehouse pencils out" from "the sector diffuses," but no citable data exists on the stock and throughput distribution of small and mid-sized warehouses, so that denominator is constructed too.
- **Against consensus**: **Agreement**: US occupational data proves that "hand laborers and freight, stock and material movers" really is a millions-scale occupation with an official definition to cite (EXT-43), which supports the existence of this card's denominator and the use of headcount and wages as leading indicators. **Divergence and evidence boundary**: EXT-43 covers the United States only and cannot be extrapolated globally; this round obtained no public figures on the installed base of unstructured picking, the penetration of per-pick contracts, or deployment hours per site, so this card gives no precise numbers at all — only arrival order and observable indicators. **Why the judgment is retained**: the cost of the failure tail and the per-owner negotiation cost are both independent of model capability, and the mechanism is clear; but with no public data on the key indicators, confidence stays at Medium.
- **External comparison source**: EXT-43 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-076 · Manufacturing's one real scaling passed through Gate 4's local closed loop; flexible assembly and high-mix low-volume are still outside the gate

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: Manufacturing is the only scene where "robots already scaled" can be cited directly, but that scaling passed through Gate 4's clause (c), the local closed loop, and happened only inside one set of boundary conditions — repetitive motions, rigid workpieces, calibratable positions, fixed takt; flexible assembly becoming routine on high-volume lines sits conservatively at 2028–2034, and high-mix low-volume small and mid-sized manufacturers hold inside this window only locally, in the few industrial clusters with dense integrator ecosystems, which is not society-level diffusion.
- **Diffusion-gate review**: audience scale = hundred-million-scale (front-line manufacturing workers worldwide), daily; Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20 this is a constructed upper bound mixing roles and process steps, and it establishes no "hundred million distinct individuals performing the same action every week." The card is written as an occupational/organizational judgment and registered directly as ACTIVE. **Gate 1's second question**: it **raises the ceiling of existing professionals** (the ceiling is the headcount of line and integration roles); it does **not** let people who previously could not do it do it — the decision and the money for a line retrofit both sit with the owner, and the activity's headcount is not enlarged.
- **Lens**: L4 diffusion lag and L3 cost structure, plus Diffusion gates · Gate 4.
- **Reasoning chain**: IFR reports that factory demand for robots doubled over ten years (EXT-45) → that fact must be used in both directions: it proves embodied capability really can diffuse, and it **draws the boundary conditions under which the diffusion happened** → diffusion happened in welding, painting, machine tending and palletizing (repetitive motions, rigid workpieces, calibratable positions, fixed takt) and did not happen in flexible assembly (a wire harness must be routed as it deforms, a connector must know how far to back off and retry when it will not seat, every soft gasket has a different tolerance; humans work on immediate tactile feedback while machines need force control plus tolerance compensation, and today that stack costs disproportionately in both hardware and commissioning hours) → the subtler bottleneck is **changeover**: a high-volume single-product line amortizes one teaching pass, a high-mix low-volume shop does not, because every product change means reprogramming, recalibrating and re-validating safety → which is why robot density correlates far more strongly with **batch size** than with wage levels → **when cost per task crosses labour**: it crossed long ago on lines with large enough batches and fixed takt (that is what the IFR curve means), and it does not cross in high-mix low-volume work because too few pieces amortize one teaching pass → but look at which gate that scaling passed: **Gate 4's clause (c), the local closed loop** — a single factory can make it work internally without waiting for society; **a factory can close the loop because it is a walled space with one decision-maker and one standard, and care, agriculture, construction and homes have no such wall** → extrapolating the factory's diffusion rate to the other four squares assumes that wall is free → **Hard constraints**: **physical** compounded by **ownership / privacy** (a production line is a specific owner's private asset, the retrofit is theirs to authorize, and the lost output during the retrofit is theirs alone to absorb).
- **Time window**: 2026–2034.
- **Falsifier**: By the end of 2030, the **composition** of new installations in IFR-class series shows assembly and precision manipulation exceeding handling and palletizing, and high-mix low-volume small and mid-sized manufacturers diffuse in step (evidenced by systematically falling changeover time and a falling ratio of integrator service revenue to equipment revenue) — that falsifies "flexible assembly at 2028–2034, high-mix low-volume slower."
- **Leading indicator**: (1) whether the **composition** of new installations in series like IFR's tilts toward assembly and precision manipulation — reading totals alone mistakes palletizing growth for an assembly breakthrough; (2) whether line changeover time falls systematically; (3) the ratio of integrator service revenue to equipment revenue (a ratio that stays high says deployment cost is still carried by on-site labour and the scale effect has not arrived); (4) the residual-value curve for used industrial robots (high residuals signal redeployability, the signal that fragmentation is being overcome); annually.
- **Confidence**: Medium.
- **depends-on**: J-073, J-066.
- **Strongest opposing mechanism**: If general-purpose force control and teach-free assembly push commissioning hours to near zero, the changeover bottleneck disappears and high-mix low-volume diffuses alongside high-volume, voiding this card's boundary-condition argument. Second: IFR's aggregate series may already contain rapid assembly-class growth that this card underestimates because it cannot obtain the breakdown — which is exactly why leading indicator (1) exists. Third: manufacturing is the one square in this chain with a real scaling to cite, which makes it the easiest to turn around into "the other four will go the same way"; this card's defence — that the wall is not free — is an argument, not data.
- **Against consensus**: **Agreement**: IFR is the only directly citable evidence of scaling in this chain (EXT-45), and it supports the existence of the premise that embodied capability can genuinely diffuse. **Divergence and evidence boundary**: IFR's series is an **installed total**, while this card is about **arrival order and boundary conditions**, and a total does not imply a composition; this round obtained no public series for new-installation composition by application type, changeover time, or used-robot residual values — all three recorded as gaps. **Why the judgment is retained**: the boundary conditions (repetitive motion, rigid workpiece, calibratable, fixed takt, one decision-maker) can be read off by contrasting where diffusion happened with where it did not, and the mechanism is clear; but with the composition breakdown missing, confidence stays at Medium and is not raised.
- **External comparison source**: EXT-45 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-077 · In agriculture what crossed is milking, not harvesting: seasonality and fragmentation hold cost per task above labour

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: Automatic milking is already standard equipment on mid-to-large dairy farms in high-wage countries because the action repeats daily, the location is fixed, the animal walks into the machine by itself, the output is measurable and failure is contained; selective harvesting stays at local pilots on single crops inside this window and does not become a mainstream practice before 2030, because seasonality crushes the denominator while fragmentation inflates the adaptation cost.
- **Diffusion-gate review**: audience scale = hundred-million-scale (agricultural employment worldwide; still hundreds of millions on FAO's count, with a markedly higher share in low- and middle-income countries, EXT-41), daily and seasonal; Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20 this is a constructed upper bound that adds up several different activities (sowing, field management, harvesting) and establishes no society-level repetition of the same action. The card is written as an occupational/organizational judgment and registered directly as ACTIVE. **Gate 1's second question**: it **raises the ceiling of existing professionals** (the ceiling is the headcount of farm operators and agricultural labourers); it does **not** let people who previously could not do it do it — the equipment is paid for and decided on by the farmer, and the activity's headcount is not enlarged.
- **Lens**: L2 constraint migration, L3 cost structure and L4 diffusion lag, plus Diffusion gates · Gate 1.
- **Reasoning chain**: Start with milking, which crossed, and list the conditions to see how strict they are — the action repeats two or three times a day, the location is fixed, **the animal walks into the machine by itself**, the output is measurable and priceable, and failure is contained (one missed cow); **a cow is a semi-cooperative object, and that condition is close to a free subsidy** → then selective harvesting, which failed: Abundant Robotics took apple harvesting to the point of working in orchards and still shut the business down (EXT-46) → this is not a capability story but a **utilization** story: a harvester works a few weeks a year and its capex must amortize over those weeks' operating hours, while row spacing, tree architecture and variety differ between orchards so every new customer means re-adaptation → **seasonality crushes the denominator, fragmentation inflates the adaptation cost in the numerator — squeezed from both ends, cost per task does not fall** → three further technical bottlenecks: perception robustness under natural light and occlusion, end effectors handling damageable produce (a bruised apple is downgraded, a strawberry more so), and biological variation (no two fruits on one tree share a position or a ripeness) → **when cost per task crosses labour**: only on structured operations that are high-frequency, fixed and semi-cooperative (milking, guided seeding and fertilizing, intra-row mechanical weeding; 2026–2030 is the scaling window); selective harvesting can cross only after annual effective operating hours rise markedly through cross-crop, cross-season reuse → globally, most of the potential object of agricultural embodiment is not on capital-intensive farms in high-wage countries at all (EXT-41), which puts society-level diffusion a generation behind equipment feasibility → so "agricultural robotics is proven" is a dangerous sentence: **what is proven is milking, not harvesting** → **Hard constraints**: **physical** (the machine must move through a field, bounded by weather and a seasonal window; energy and time are incompressible) compounded by **ownership / privacy** (each plot and orchard is a private, unique physical layout that compute cannot copy).
- **Time window**: 2026–2030.
- **Falsifier**: By the end of 2030, selective harvesting is the mainstream practice for a major crop in any major growing region — evidenced either by machine harvesting taking a majority of that crop's harvested volume in that region, or by per-acre or per-yield harvesting services earning repeat business at scale.
- **Leading indicator**: (1) whether harvesting equipment earns **repeat business** under a per-acre or per-yield service model (repeat orders say more than first orders about whether the numbers work); (2) whether **annual effective operating hours** per machine rise (cross-crop, cross-season reuse is the only route that rescues utilization); (3) whether seasonal wages diverge in adoption-dense growing regions ahead of the national series; (4) whether insurers or grower cooperatives offer products covering yield loss from machine operation; annually.
- **Confidence**: Medium.
- **depends-on**: J-073, J-066.
- **Strongest opposing mechanism**: The growing side can adapt to the machine instead — dwarf high-density planting, standardized row spacing and single-variety new plantings are themselves a conversion of unstructured environment into structured space; if new orchards are designed to machine standards, the fragmentation half dissolves and the harvesting window moves forward. A second independent objection: this card uses one company's shutdown (EXT-46) as the principal evidence on the failure side, and a single case may be driven by funding and management reasons and cannot represent a whole class of technology.
- **Against consensus**: **Agreement**: Abundant Robotics shutting down after the technology worked (EXT-46) supports "technical feasibility is not commercial feasibility"; FAO's employment indicators support agricultural employment still being hundreds of millions with a markedly higher share in low- and middle-income countries (EXT-41), which supports where this card places the denominator. **Divergence and evidence boundary**: EXT-46 is a single company case and constitutes no statistic over the class; FAO is used for **orders of magnitude** only, with its definitions, years and statistical boundaries as given in the source; this round obtained no installed-base or repeat-purchase data for harvesting equipment. **Why the judgment is retained**: milking versus harvesting is a natural control pair inside one industry in one period, and the crossing conditions (high frequency, fixed location, semi-cooperative object) can be checked one by one; but with only a single case on the failure side, confidence stays at Medium.
- **External comparison source**: EXT-41, EXT-46 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-078 · Construction and domestic work are blocked by the one-off site and somebody else's home: inside this window they arrive only as single-operation equipment and single-task slices

- **Proposed date**: 2026-09-20
- **One-sentence judgment**: Construction and domestic work share the hardest property — the work environment is different every time and does not belong to whoever is working in it; through 2040 on-site construction robots remain single-operation equipment and do not substitute for the site process as a whole, open-ended household tasks reach no society-level diffusion, and home embodiment continues as single-task slices (vacuuming, dishwashing, mowing).
- **Diffusion-gate review**: audience scale = hundred-million-scale (construction workers and domestic workers worldwide; on ILO's count domestic workers alone are a group in the tens of millions, a large share of them informally employed, EXT-42), daily; Gate 1 **FAIL** — per the whole-ledger review of 2026-09-20 this is a constructed upper bound adding up two different classes of activity and establishes no society-level repetition of the same action. The card is written as an occupational/organizational judgment and registered directly as ACTIVE. **Gate 1's second question**: construction **raises the ceiling of existing professionals** (the ceiling is the headcount of the site trades); the "open-ended household task" in domestic work is the one that, if it held, would **let people who previously could not do it do it** — extending "somebody tidies up for you" from households that can afford domestic help to all households, which could enlarge the activity itself — and this card judges that it does not hold inside this window, so that route to a larger denominator does not open before 2040.
- **Lens**: L6 irreversibility, L8 human nature and demand, and L4 diffusion lag, plus Diffusion gates · Gates 3, 4 and 5.
- **Reasoning chain**: **Construction** — a site is one-off: geometry, ground conditions, trade sequencing and weather never repeat, tolerances are in centimetres rather than millimetres, and multiple trades wait on each other in one space → FBR's Hadrian bricklaying machine is the most honest specimen here (EXT-47): a direction pushed for something on the order of a decade, still at single-operation and demonstration-project scale → what blocks it is not laying speed: **however fast a machine lays brick, it still waits on the preceding trade, on inspection, on permits and on weather** → construction's real structural path is to bypass the site — move the work into a prefabrication plant, converting the one-off site into structured space, at which point it degenerates into the manufacturing problem of J-076 → **Domestic work** — the hardest square, and the difficulty is not even execution but **task definition**: "tidy up" contains classification, value judgment (which object is rubbish and which is a keepsake), privacy boundaries and household-specific conventions → on ILO's count domestic workers are a group in the tens of millions (EXT-42), so the demand is real and already being paid for — but what is bought was never only the motions; it includes judgment, trustworthiness and the tacit understanding that saves the employer from specifying anything → and failure is irreversible: what breaks is not *a* cup, it is *that* cup (L6) → **when cost per task crosses labour**: even if a Hadrian-class machine pushes the unit cost of bricklaying below manual labour on some standardized houses, society-level diffusion requires **the site process, insurance rates and the inspection regime to change together** — Gate 4 multi-party coordination, not equipment performance; domestic work is the same, since between a machine folding laundry in a demo video and a hundred million households letting it into the bedroom daily sit ownership, trust and the cost paid on every use → **Hard constraints**: construction — **law / permitting** (building permits, inspection and injury liability must land on a party that can be sued) compounded by **physical**; domestic — **ownership / privacy** (someone's home is private space and entry requires authorization) compounded by **trust / relationship** (who gets a key is the product of repeated interaction over time and cannot be generated in one pass).
- **Time window**: 2026–2040.
- **Falsifier**: Before 2040, on-site construction robots substitute not for single operations but for the site process as a whole (verifiable through the number of trades and the share of schedule carried by robots in general contracts) — that falsifies this card's construction judgment; or a general-purpose home robot reaches daily performance of **open-ended household tasks** (not single-task slices such as vacuuming, dishwashing or mowing) in a majority of households in any country — that falsifies its domestic-work judgment.
- **Leading indicator**: construction — (1) whether general contractors' insurance quotes a separate rate for robotic work; (2) whether schedule contracts start carrying default and stoppage clauses for robotic equipment; (3) whether the prefabrication share of work keeps rising. Domestic — (4) whether a general-purpose home robot falls into the durable-goods price band **and** carries a low enough recurring cost per task (no tidying beforehand, no supervision throughout); (5) whether domestic-worker headcount and wages diverge in high-adoption countries; annually.
- **Confidence**: Medium.
- **depends-on**: J-073, J-066.
- **Strongest opposing mechanism**: If prefabrication moves the great majority of trades off the site, "on-site robots do not replace the whole process" becomes irrelevant — the structural substitution happens elsewhere and this card's construction half fails in the "right but unimportant" way. On the domestic side, price and trust may be bypassed by a platform service model in which the provider owns the equipment and the liability and enters per visit, so "who gets a key" is no longer decided household by household. A third, independent objection: this card's claim about 2040 is a **negative** long-window judgment, harder to overturn with short-run evidence than a positive forecast, which by itself lowers its information content.
- **Against consensus**: **Agreement**: FBR's Hadrian, pushed for something on the order of a decade, is still at single-operation and demonstration scale (EXT-47), supporting "what blocks on-site construction is not laying speed"; ILO counts domestic workers as a separate group in the tens of millions with a large informal share (EXT-42), supporting that the demand is real and already paid for. **Divergence and evidence boundary**: both are **a single case or a single group definition** and cover no arrival order; ILO's statistical boundaries and years are as given in the source and this card takes orders of magnitude only; this round obtained no checkable series for prefabrication share, insurance rates for robotic work, or the recurring per-task cost of home robots. **Why the judgment is retained**: the card depends on two constraints that do not open as model capability improves — permitting and liability must land on a party that can be sued, and entering private space requires authorization and long-run trust. But as a negative judgment running to 2040 it is less checkable than this chain's mid-segment judgments, so confidence stays at Medium and is not raised.
- **External comparison source**: EXT-42, EXT-47 (see the source index above).
- **Source**: [C4: Embodied Intelligence](chains/40-embodied-intelligence.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

## 15. Judgment cards for the C5 biology-and-medicine chain

> These four cards come from [C5: Biology and Medicine](chains/50-biology-medicine.md). They judge professional and institutional processes; patient reach does not substitute for the audience performing the repeated action.

### J-079 · Biomedical candidate generation and clinical-grade causal proof diverge

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2034, biomedical candidate generation and ranking get much cheaper, while clinical-grade causal proof does not accelerate proportionally.
- **Audience scale**: constructed billion-scale patient reach and million-scale direct action population; mainly **raises existing professionals' ceiling** (neither is a citable behavioural statistic).
- **Diffusion-gate review**: Patient reach is a constructed billion-scale estimate, while the direct action is performed by a constructed millions-scale population of R&D, regulatory, and clinical professionals; neither is a citable behavioural statistic. Gate 1 **FAIL**, an occupational/organizational judgment. **Gate 1 second question**: it mainly raises the candidate-generation and validation ceiling of existing professionals; it does not let people without R&D or clinical-validation capability complete the action independently.
- **Lens**: L2 constraint migration + L6 irreversibility + diffusion gates.
- **Reasoning chain**: Candidates are copyable and ranking costs fall → trustworthy causality still needs real samples, time, and subject protection → the bottleneck moves to prospective validation.
- **Time window**: 2026–2034.
- **Falsifier**: Before 2030, at least three high-liability categories halve median candidate-to-approved-intervention time without increasing real samples or follow-up intensity, while safety withdrawals do not rise.
- **Leading indicator**: candidates per approval, share entering human trials, phase duration, post-market safety supplements, and withdrawals; annually.
- **Confidence**: Medium.
- **depends-on**: J-005, J-034, J-066.
- **Strongest opposing mechanism**: biological models, surrogate endpoints, and synthetic controls may compress experimental and clinical stages together; if the falsifier triggers, withdraw the asynchronous claim.
- **Against consensus**: **Agreement**: FDA evaluates AI credibility by Context of Use and risk, supporting “generation is not proof.” **Boundary**: it does not establish the window or acceleration ceiling. **Why retained**: real outcomes and subject protection do not copy with candidates.
- **External comparison source**: EXT-49, EXT-50.
- **Source**: [C5: Biology and Medicine](chains/50-biology-medicine.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-080 · Low-liability medical workflows diffuse before autonomous care without professional review

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2031, summarization, coding, scheduling, and review-based decision support become routine before autonomous diagnosis and treatment without professional review.
- **Audience scale**: constructed tens-of-millions-scale clinical and administrative users; mainly **raises existing professionals' ceiling** (not a citable behavioural statistic).
- **Diffusion-gate review**: Direct users are a constructed tens-of-millions-scale population across clinical and administrative staff, not a citable behavioural statistic; this is a professional workflow and Gate 1 **FAIL**. **Gate 1 second question**: it raises the workflow ceiling of existing clinical and administrative staff; it does not let unlicensed people diagnose or treat independently.
- **Lens**: L4 diffusion lag + diffusion Gates 2–5.
- **Reasoning chain**: Low-liability tools replace existing work, fit current carriers, and remain reviewable → autonomous care crosses licensing, liability, and irreversible treatment → the former diffuses first.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, in at least two large jurisdictions, encounters covered by care without human review persistently exceed AI-assisted documentation and review-based support without one-off mandated procurement.
- **Leading indicator**: FDA intended-use distribution, hospital recommend-review versus autonomous-action shares, insurance/liability terms, and clinical retention; twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-079, J-066, J-068, J-069.
- **Strongest opposing mechanism**: underserved regions may accept “worse but immediately available” autonomous systems and reverse the order.
- **Against consensus**: **Agreement**: FDA's list proves authorized regulated products exist. **Boundary**: it is not exhaustive and proves neither deployment scale nor autonomy. **Why retained**: review-based tools use an institutional loop; autonomous care needs additional action rights.
- **External comparison source**: EXT-48, EXT-50.
- **Source**: [C5: Biology and Medicine](chains/50-biology-medicine.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-081 · More drug candidates do not proportionally shorten human trial time

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: By 2034, AI increases drug candidates reaching laboratories, but candidate growth does not translate proportionally into approvals.
- **Audience scale**: constructed million-scale R&D, trial, and regulatory action population; mainly **raises existing professionals' ceiling** (not a citable behavioural statistic).
- **Diffusion-gate review**: The direct action is performed by a constructed millions-scale population of R&D, trial, and regulatory participants, not a citable behavioural statistic; Gate 1 **FAIL**. **Gate 1 second question**: it raises the search ceiling of existing drug developers; it does not let people without wet-lab or human-trial capability complete the development loop independently.
- **Lens**: L2 constraint migration + cost structure.
- **Reasoning chain**: Search expands → more candidates compete for wet-lab, participant, site, and regulatory capacity that has not expanded proportionally → attrition or queues rise.
- **Time window**: 2026–2034.
- **Falsifier**: Between 2028 and 2034, AI-origin candidates cut both median first-in-human-to-approval time and failure rates by more than 50%, replicated in at least three therapeutic areas.
- **Leading indicator**: Phase I AI-origin candidates, phase conversion, site start and recruitment completion time, and clinical candidates per approval; annually.
- **Confidence**: Medium.
- **depends-on**: J-079, J-066.
- **Strongest opposing mechanism**: predictive biomarkers, adaptive trials, and digital endpoints may reduce samples and follow-up together.
- **Against consensus**: **Agreement**: FDA requires risk-linked AI credibility. **Boundary**: it supports no timeline or success-rate forecast. **Why retained**: candidate computation and human time follow different production functions.
- **External comparison source**: EXT-49.
- **Source**: [C5: Biology and Medicine](chains/50-biology-medicine.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-082 · Once explanation is abundant, medical scarcity moves to authorized intervention and continuity of care (landscape only)

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, the bottleneck in chronic disease, ageing, and primary care moves from standard explanation to authorized intervention, continuous observation, and exception escalation.
- **Audience scale**: constructed billion-scale patient reach and hundred-millions-scale direct carers/workers; mainly **raises existing professionals' ceiling** (neither is a citable behavioural statistic).
- **Diffusion-gate review**: Patient reach is a constructed billion-scale estimate, while direct carers and workers are a constructed tens-to-hundreds-of-millions-scale population; neither is a citable behavioural statistic. This is an institutional/occupational arrangement and Gate 1 **FAIL**. **Gate 1 second question**: it raises the explanation and monitoring ceiling of existing carers and professionals; it does not let people without authorization independently deliver continuity of care.
- **Lens**: L2 constraint migration + embodied-presence hard constraint.
- **Reasoning chain**: Q&A is copyable → explanation and reminder costs fall → sampling, medication, transfer, follow-up, and exception judgment still need local resources and liability chains → advice becomes unmet demand without a carrier.
- **Time window**: 2027–2034.
- **Falsifier**: Across several countries, within five years of widespread AI Q&A, intervention hours, follow-up completion, and exception response speed rise together while staff and institutional capacity cease to be principal queue causes.
- **Leading indicator**: post-advice follow-up, escalation latency, load per caregiver, primary-care vacancies, and twelve-month remote-program retention; annually.
- **Confidence**: Low (landscape only).
- **depends-on**: J-079, J-080, J-032, J-066.
- **Strongest opposing mechanism**: remote monitoring, home robotics, and task redesign may make continuity of care scalable.
- **Against consensus**: **Agreement**: WHO supports workforce, accountability, and safety as real constraints. **Boundary**: it does not prove AI worsens care queues. **Why retained**: local intervention and liability chains do not emerge automatically from more explanation.
- **External comparison source**: EXT-50, EXT-51.
- **Source**: [C5: Biology and Medicine](chains/50-biology-medicine.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

## 16. Judgment cards for the C6 education-and-skill-formation chain

> These four cards come from [C6: Education and Skill Formation](chains/60-education-skill-formation.md). The scale gate screens the people and frequency of the action; “affects billions” does not itself create a society-level forecast.

### J-083 · Personalized explanation becomes abundant before verifiable mastery

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2030, personalized explanations, examples, and immediate feedback become routine, but verifiable mastery does not grow proportionally.
- **Audience scale**: constructed billion-scale learner reach and potentially daily learning; it both **raises existing professionals' ceiling** and gives some previously excluded learners access, but no billion-scale same-action statistic exists.
- **Diffusion-gate review**: Learners' reach is a constructed billion-scale estimate and learning can be daily, but no citable statistic establishes a billion distinct people performing the same AI-tutoring action daily; Gate 1 **FAIL**, so this remains a learning-context judgment. **Gate 1 second question**: it both raises existing learners' feedback ceiling and gives personalized explanation to people who previously lacked it; whether that becomes mastery remains governed by this card's falsifier.
- **Lens**: L2 constraint migration + diffusion gates.
- **Reasoning chain**: Explanations are copyable → generation and translation costs fall → practice still requires attention, time, and behavioural change → understanding and independent performance diverge.
- **Time window**: 2026–2030.
- **Falsifier**: Across countries, ages, and subjects, after two years of widespread generative tutoring, controlled transfer and long-term retention rise proportionally with use without curriculum redesign.
- **Leading indicator**: weekly AI-tutoring use, independent transfer scores, three- to six-month retention, completion, and dependence on assistance; each term.
- **Confidence**: Medium.
- **depends-on**: J-001, J-066.
- **Strongest opposing mechanism**: adaptive tutoring may improve feedback, pacing, and motivation together, converting explanation directly into mastery.
- **Against consensus**: **Agreement**: UNESCO requires human-centred, age-appropriate, private, pedagogically designed use. **Boundary**: it does not prove outcomes fail to rise proportionally. **Why retained**: explanation cannot bear practice time for the learner.
- **External comparison source**: EXT-52.
- **Source**: [C6: Education and Skill Formation](chains/60-education-skill-formation.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-084 · AI tutoring enters teacher and institutional workflows before replacing schools

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2031, AI tutoring diffuses first through teacher assignment, curriculum alignment, and institutional supervision rather than large-scale school replacement.
- **Audience scale**: constructed billion-scale student and working-learner reach with potentially weekly learning; it mainly **raises existing professionals' ceiling**, while the action subject remains the school/employer carrier.
- **Diffusion-gate review**: Students and working learners have constructed billion-scale reach and learning can be weekly, but no citable behavioural statistic exists and the object is whether schools/employers become the carrier rather than one repeated student action; Gate 1 **FAIL**, an institutional judgment. **Gate 1 second question**: it mainly raises the tutoring ceiling of existing teachers and institutions; it does not give people without authority the power to run schools, assess, or grant credentials.
- **Lens**: L4 diffusion lag + diffusion Gates 3–5.
- **Reasoning chain**: Stand-alone chat adds a new action → embedded tutoring replaces Q&A, practice, and feedback → schools carry identity, curriculum, peers, assessment, and credentials → local loops diffuse first.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, in at least three large education systems, broadly recognized qualifications from AI pathways outside schools/employers persistently outnumber those from institution-embedded pathways.
- **Leading indicator**: teacher-assigned versus direct purchase use, learning-system integration, twelve-month retention, teacher workload, and recognition breadth of independent AI credentials; annually.
- **Confidence**: Medium.
- **depends-on**: J-083, J-066, J-068, J-069, J-070, J-071.
- **Strongest opposing mechanism**: school cost, geography, and adult demand may let direct systems bypass institutions.
- **Against consensus**: **Agreement**: OECD emphasizes governance, ecosystems, and teacher capacity. **Boundary**: it does not prove schools retain current boundaries. **Why retained**: schools bind learning to identity, assessment, and credential exits.
- **External comparison source**: EXT-53.
- **Source**: [C6: Education and Skill Formation](chains/60-education-skill-formation.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-085 · Take-home artifact signals weaken while controlled performance and process evidence gain weight

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, high-stakes admissions and hiring reduce the weight of take-home artifacts without process verification and increase controlled performance and process evidence.
- **Audience scale**: constructed hundred-millions-scale reach across applicants, workers, and learners; it mainly **raises existing professionals' ceiling**, while assessment is low-frequency and performed by schools/employers.
- **Diffusion-gate review**: Direct reach across applicants, workers, and learners is a constructed hundreds-of-millions-scale estimate, not a citable behavioural statistic, and the action is low-frequency; Gate 1 **FAIL**, an institutional judgment. **Gate 1 second question**: it changes the screening ceiling and evidence structure of existing schools and employers; it does not give people without admissions or hiring authority the power to grant qualifications.
- **Lens**: L5 signalling game + L1 abundance → scarcity.
- **Reasoning chain**: Artifact-generation costs fall → artifacts correlate less with personal capability → selectors move toward costlier but harder-to-outsource identity, live performance, and longitudinal records.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, leading universities and large employers keep increasing the independent weight of take-home artifacts without process verification while their predictive validity does not decline.
- **Leading indicator**: oral and live-task share, identity-verification spending, portfolio version-history requirements, and internship/apprenticeship weight; annually.
- **Confidence**: Medium.
- **depends-on**: J-022, J-083, J-084, J-066.
- **Strongest opposing mechanism**: process records can be forged and controlled assessment is costly; institutions may use open collaboration assessment rather than return to exams.
- **Against consensus**: **Agreement**: UNESCO supports assessment redesign. **Boundary**: it does not establish which assessment gains weight. **Why retained**: selection systems cannot indefinitely rely on a proxy that has lost correlation with capability.
- **External comparison source**: EXT-52.
- **Source**: [C6: Education and Skill Formation](chains/60-education-skill-formation.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-086 · The explanation gap narrows while practice and verification gaps may widen (landscape only)

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, AI narrows access gaps in explanation, but without carrier institutions skill and opportunity gaps may fail to fall or may widen.
- **Audience scale**: constructed billion-scale learner reach; the tool **lets people who could not do it do it now** for some learning actions, while skill, credentials, and opportunity still depend on public, school, or employer carriers.
- **Diffusion-gate review**: Learner reach is a constructed billion-scale estimate and learning is frequent, but it is not a citable behavioural statistic and the object is the distributional result when public, school, or employer carriers are absent; Gate 1 **FAIL**, an institutional landscape. **Gate 1 second question**: explanation tools can help people who previously lacked access, but the skill, credential, and opportunity judged here remain governed by institutions and resource conditions.
- **Lens**: L2 constraint migration + distribution and power.
- **Reasoning chain**: Marginal explanation becomes cheap → people with devices and self-direction benefit first → mastery still needs time, feedback, and practice environments → credentials need institutional recognition → new supply is absorbed through existing resource differences.
- **Time window**: 2027–2034.
- **Falsifier**: Where low-cost AI tutoring is widespread without added teachers, devices, assessment, or social support, low- versus high-income gaps in independent mastery and qualifications shrink significantly for five consecutive years.
- **Leading indicator**: device/connectivity access, use by income, independent assessment gaps, teacher contact, completion, qualifications, and employment conversion; annually.
- **Confidence**: Low (landscape only).
- **depends-on**: J-083, J-084, J-066, J-069, J-070.
- **Strongest opposing mechanism**: low-cost, offline, high-quality tutoring may deliver the largest marginal gains to learners with the fewest resources.
- **Against consensus**: **Agreement**: the World Bank establishes the enormous scale of foundational learning deficits. **Boundary**: it does not support AI's direction of effect on inequality. **Why retained**: explanation is only one input to learning and is not the authority granting qualifications.
- **External comparison source**: EXT-54.
- **Source**: [C6: Education and Skill Formation](chains/60-education-skill-formation.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

## 17. Judgment cards for the C7 social-consequence chain

> These five cards come from [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md). They test how capability passes through organizations, labour, institutions, capital, and demand. Capability is a trigger and feasibility boundary, while diffusion gates, supply and demand, human behaviour, and institutions jointly determine the outcome.

### J-087 · Human–machine supervisory units become mainstream before staffless organizations

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2031, organizations adopting generation and tool use first split work into machine-default execution, human exception handling, and accountable boundary setting rather than broadly becoming staffless.
- **Audience scale**: constructed hundred-millions-scale reach across knowledge workers, operations staff, and managers; mainly **raises existing professionals' ceiling**, while organizations perform the work-unit redesign.
- **Diffusion-gate review**: The reach is not a citable same-action behaviour statistic, and organizations must complete workflow substitution and a local closed loop; Gate 1 **FAIL**, an organizational judgment.
- **Lens**: technology sequence + organizational carrier + diffusion Gates 2–4.
- **Reasoning chain**: Generation and tool use mature first → bounded reviewable tasks enter workflows first → exceptions and liability still need a principal → the minimum production unit becomes one accountable person supervising multiple machine executions.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, across at least three large knowledge-work industries, fewer than half of production AI deployments that persist for twelve months use a work unit combining machine-default execution, human exception handling, and accountable boundary setting. The card fails whether the remainder is end-to-end staffless execution or deployment broadly stalls in demonstrations and failures.
- **Leading indicator**: machine-default share, human takeover rate, executions per accountable owner, pre-deployment workflow-redesign hours, and twelve-month retention; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007, J-009, J-066, J-068.
- **Strongest opposing mechanism**: End-to-end reliability may jump enough for organizations to delegate complete outcomes without passing through supervisory units.
- **Against consensus**: **Agreement**: NIST calls for governance, measurement, monitoring, and human oversight. **Boundary**: it does not establish this organizational form or time window. **Why retained**: existing accountable principals and workflows are already-built carriers, so task-by-task substitution clears the diffusion gates more easily than rebuilding firm boundaries at once.
- **External comparison source**: EXT-4.
- **Source**: [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-088 · Junior production seats shrink before occupations as a whole; apprenticeship carriers become the new bottleneck

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, in generation-intensive occupations junior production seats and routine hours shrink relatively before total occupational headcount, making supervised practice a skill-formation bottleneck.
- **Audience scale**: constructed tens-of-millions-scale reach across junior knowledge workers, applicants, and professional trainees; mainly **raises existing professionals' ceiling** while narrowing entry routes.
- **Diffusion-gate review**: Occupational entry is a low-frequency institutional arrangement, not one repeated action performed across society; Gate 1 **FAIL**, a labour-market and skill-formation judgment.
- **Lens**: task bundles + skill formation + signalling game.
- **Reasoning chain**: Junior production is easiest to verify and automate → seniors sustain output with fewer junior hours → entrants lose the carrier for real-task practice → apprenticeship, simulation, and supervised fieldwork become scarcer.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, across at least five generation-intensive occupations, junior-seat share does not decline before total occupational headcount; or it declines first but verifiable apprenticeship, simulation, rotation, or supervised-fieldwork capacity expands enough to preserve the pre-adoption replenishment rate of professionals. Junior seats falling at the same time as or after total occupational contraction also falsifies the card.
- **Leading indicator**: junior-to-senior hiring ratio, entry-task mix, apprenticeship places, supervised hours, time to promotion, and controlled performance of external candidates; annually.
- **Confidence**: Medium.
- **depends-on**: J-087, J-083, J-066.
- **Strongest opposing mechanism**: AI tutoring and high-fidelity simulation may lower training cost simultaneously, giving more entrants denser feedback than old jobs did.
- **Against consensus**: **Partial agreement**: the ILO's 2025 global occupational-exposure index finds about one in four workers in occupations with some GenAI exposure and judges transformation more likely than whole-job replacement for most occupations. **Boundary**: the index provides no evidence about junior hiring, apprenticeship carriers, net employment, or this card's time window. **Why retained**: the routine production being removed was also the old occupation's practice carrier, and generation does not automatically build a replacement carrier.
- **External comparison source**: EXT-60.
- **Source**: [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-089 · Permission, audit, and appeal control planes become production infrastructure before broad autonomous authority

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2032, identity, permission, logging, pause, audit, and appeal enter core production systems before tool-using AI broadly receives high-liability autonomous authority.
- **Audience scale**: constructed hundred-millions-scale reach across employees, customers, and citizens affected by high-liability automation; mainly **raises existing professionals' ceiling**, while organizations and public institutions operate the controls.
- **Diffusion-gate review**: Affected reach is not the headcount executing the control action, and multi-party authorization depends on enforceable and observable coordination; Gate 1 **FAIL**, an institutional judgment.
- **Lens**: action rights + legal liability + diffusion Gate 4.
- **Reasoning chain**: Tool use enlarges possible consequences → asset owners require least privilege and interruptibility → disputes require logs, accountable signatures, and appeal → the control plane moves from compliance attachment to production dependency.
- **Time window**: 2026–2032.
- **Falsifier**: By 2030, across at least three high-liability industries, most production autonomous systems receive broad high-liability authority without principal-level authorization, tamper-evident action records, human pause, and dispute appeal as prior production dependencies. If systems receive broad authority first and regulators or buyers tighten only after accidents, the reversed order still falsifies the card.
- **Leading indicator**: fine-grained permission coverage, log retention, human pause rate, external-audit clauses, appeal latency, and procurements rejected for missing controls; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-007, J-009, J-031, J-055, J-070.
- **Strongest opposing mechanism**: Low accident rates and platform-level insurance may make black-box autonomy acceptable, replacing per-action control with ex-post compensation.
- **Against consensus**: **Agreement**: NIST and the EU AI Act support governance, logging, human oversight, and risk management. **Boundary**: they do not establish the diffusion order of appeal controls or consistency across industries. **Why retained**: execution touches other parties' assets and rights, so existing accountable principals need observable authorization and interruption paths before delegating.
- **External comparison source**: EXT-4, EXT-10.
- **Source**: [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

### J-090 · Productivity gains first concentrate with scarce complementary-asset owners; competition and institutions decide whether they spread

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, early productivity gains after general-model prices fall flow first to parties owning customers, proprietary workflow data, licences, channels, liability-bearing capital, compute, or power rather than spreading automatically with technical access.
- **Audience scale**: constructed billion-scale reach across firms, workers, and consumers; mainly **raises existing professionals' ceiling**, while asset owners and institutions determine distribution.
- **Diffusion-gate review**: Billion-scale is distributional reach, not a same-action behaviour statistic, and the subject is an asset and institutional arrangement; Gate 1 **FAIL**, a capital-and-power judgment.
- **Lens**: complementary assets + capital returns + competition institutions.
- **Reasoning chain**: Model and call prices fall → scarcity rents on core capability compress → commercialization still needs scarce complementary assets and fixed redesign cost → incumbent asset owners absorb gains first → open standards, competition, and redistribution determine later spread.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five high-adoption industries, incumbent firms controlling customers, proprietary data, licences, channels, or infrastructure gain no relative margin, market share, or bargaining power. The card fails whether gains move to entrants, model suppliers, labour, or consumers.
- **Leading indicator**: industry margins, merger activity and concentration, returns by AI supply-chain layer, labour share, price decline, data portability, and channel switching; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-039, J-056, J-087.
- **Strongest opposing mechanism**: Model commoditization, open weights, and low-code distribution may make complementary assets rapidly replicable, letting small teams take incumbent channels and profits directly.
- **Against consensus**: **Agreement on mechanism, unknown on outcome**: Teece's complementary-assets theory supports value capture depending on scarce complements; Brynjolfsson, Rock, and Syverson's Productivity J-Curve supports general-purpose technologies requiring complementary intangible investment in business processes, human capital, and organizational co-invention. **Boundary**: neither establishes AI's distribution, the duration of concentration, or this card's time window. **Why retained**: model access does not simultaneously supply customers, licences, power, liability capital, and workflow-redesign capacity.
- **External comparison source**: EXT-37, EXT-61.
- **Source**: [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.

### J-091 · Demand expansion and task savings occur together; net employment cannot be inferred from the capability curve alone

- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, AI-intensive industries see both lower labour hours per unit and expansion in variety, frequency, or customer segments; demand elasticity and non-automated hard constraints jointly determine net employment.
- **Audience scale**: constructed billion-scale reach across workers and consumers; the capability both **raises existing professionals' ceiling** and, in low-cost services, may let people who could not do it do it now for some consumption or production actions.
- **Diffusion-gate review**: The reach is not one repeated action and employment is an industry-level net result; Gate 1 **FAIL**, a demand-and-labour-structure judgment.
- **Lens**: supply-and-demand elasticity + task bundles + physical and institutional hard constraints.
- **Reasoning chain**: Labour hours per task fall → price, waiting, or customization costs fall → previously uneconomic demand enters → non-automated steps absorb part of the new volume → the relative size of expansion and savings determines net employment.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five adoption-intensive industries, significant labour-hour reductions per service are followed for three years by no expansion in variety, frequency, customer segments, or total output. Whether employment can also be explained by macroeconomic cycles, regulation, or other factors does not prevent falsification of the card's claim that demand expansion and task savings occur together.
- **Leading indicator**: labour hours per unit, price, wait time, SKU or service variety, frequency per customer, new-customer share, total output, and jobs in non-automated steps; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-037, J-073, J-087.
- **Strongest opposing mechanism**: Where demand is saturated or income constraints do not move, cost reduction may become profit and job reduction without enough new volume.
- **Against consensus**: **Partial agreement**: the ILO's 2025 index judges task transformation more likely than whole-job replacement for most occupations and makes clear that exposure alone does not yield a net-employment outcome. **Boundary**: it provides no demand elasticity, output expansion, or net employment direction. **Why retained**: supply and demand determine whether lower cost expands quantity, while bodies, licences, and sites determine where that quantity lands; capability curves alone cannot yield the net result.
- **External comparison source**: EXT-60.
- **Source**: [C7: Technology Arrives First, Power Later](chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
