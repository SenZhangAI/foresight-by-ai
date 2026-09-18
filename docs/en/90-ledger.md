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
| J-001 | 2026-09-18 | Unit reasoning cost falls another order of magnitude by the end of 2029 | 2026–2029 | High | — | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-03-31 |
| J-002 | 2026-09-18 | Objective quality selection is a 2–4 year window, not durable scarcity | through 2029 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-03-31 |
| J-003 | 2026-09-18 | Ownership and usable form of private personal or organizational context are more likely to become durable scarcity | 2027–2033 | Medium | J-001, J-002 | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-06-30 |
| J-004 | 2026-09-18 | As AI executes actions, infrastructure that makes actions reversible becomes scarce | 2027–2032 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-06-30 |
| J-005 | 2026-09-18 | Raw signals, accountable commitments, and verified causality become more valuable than reproducible text | 2029–2033 | Medium | J-001 | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-06-30 |
| J-017 | 2026-09-18 | AI mediation expands weak-tie coordination faster than strong relationships, without expanding the number of relationships in which people can remain present | 2027–2033 | Medium | J-006, J-007 | [C1](chains/10-generation-becomes-free.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-06-30 |
| J-018 | 2026-09-18 | Parallel reasoning becomes the default workflow before long-horizon autonomy | 2026–2028 | High | J-006, J-009 | [Near-term landscape](10-near.md) | Consistent with consensus (mechanism pending comparison) | ACTIVE | 2027-03-31 |
| J-019 | 2026-09-18 | Saving tokens itself is a window, not durable scarcity | 2026–2028 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-03-31 |
| J-020 | 2026-09-18 | Reproducible content keeps falling in marginal price as objective selection is internalized | 2026–2028 | Medium | J-002, J-015 | [Near-term landscape](10-near.md) | Consistent with the direction of content abundance | ACTIVE | 2027-03-31 |
| J-021 | 2026-09-18 | First-hand field signals earn a premium earlier than second-hand expression | 2026–2029 | Medium | J-005, J-015 | [Near-term landscape](10-near.md) | Unknown (external comparison not yet completed) | ACTIVE | 2027-06-30 |
| J-022 | 2026-09-18 | As forgable signals multiply, selection moves toward more expensive credentials | 2026–2029 | Medium | J-005, J-017 | [Near-term landscape](10-near.md) | Consistent with the direction that trust matters more | ACTIVE | 2027-06-30 |
| J-023 | 2026-09-18 | Attention shifts from expression toward relationships and fulfilled commitments | 2027–2030 | Medium | J-017, J-005 | [Near-term landscape](10-near.md) | Consistent with the direction that trust matters more | ACTIVE | 2027-06-30 |
| J-024 | 2026-09-18 | Credentials may be re-layered, but the institutional destination remains uncertain | 2027–2032 | Low | J-022, J-013 | [Near-term landscape](10-near.md) | Unknown (landscape only) | ACTIVE | 2027-06-30 |
| J-025 | 2026-09-18 | Small teams complete more verifiable output with fewer steps | 2027–2030 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Consistent with the direction of knowledge-work automation | ACTIVE | 2027-06-30 |
| J-026 | 2026-09-18 | Responsibility boundaries do not disappear at the same rate as knowledge-work capacity | 2027–2032 | Medium | J-009, J-013 | [Near-term landscape](10-near.md) | Unknown (mechanism pending comparison) | ACTIVE | 2027-06-30 |
| J-027 | 2026-09-18 | Rented compute spreads capability without distributing gains evenly | 2026–2029 | Medium | J-001, J-006 | [Near-term landscape](10-near.md) | Consistent with the direction of capability diffusion | ACTIVE | 2027-03-31 |
| J-028 | 2026-09-18 | Data, distribution, and liability access may become new bargaining nodes | 2027–2032 | Low | J-005, J-013 | [Near-term landscape](10-near.md) | Unknown (landscape only) | ACTIVE | 2027-06-30 |
| J-029 | 2026-09-18 | Status, certainty, embodied presence, and responsibility remain demand-side anchors | 2026–2030 | Medium | J-017, J-011 | [Near-term landscape](10-near.md) | Consistent with the conservative direction that tools do not change every need | ACTIVE | 2027-06-30 |
| J-030 | 2026-09-18 | AI mediates coordination but cannot mediate shared experience | 2027–2032 | Low | J-017, J-011 | [Near-term landscape](10-near.md) | Unknown (landscape only) | ACTIVE | 2027-06-30 |

The overview is a navigation aid. Every full card, strongest opposing mechanism, and evidence is registered in this ledger; source links return to the relevant narrative or technology chain, and IDs and statuses stay synchronized here.
---

## 3. The `depends-on` graph

### Notation

Use comma-separated formal IDs, for example: `depends-on: J-001, J-002`. A dependency means “if the upstream mechanism fails, this judgment must be reviewed”; it does not mean that both judgments happen simultaneously or point to an article location. A far-horizon judgment without an explicit near-term dependency should be downgraded to landscape only.

Current dependency tree (complete view; each card’s `depends-on` is authoritative):

```text
J-001
├── J-002
│   └── J-003
├── J-004
├── J-005
└── J-006
    └── J-007
        └── J-008
            └── J-009
                ├── J-010
                ├── J-013
                │   └── J-014
                └── J-015
J-006 + J-007 ──> J-011 ──> J-012
J-010 + J-012 + J-014 + J-015 ──> J-016
J-006 + J-007 ──> J-017
├── J-018 (J-006, J-009)
├── J-019 (J-001, J-006)
├── J-020 (J-002, J-015)
├── J-021 (J-005, J-015)
├── J-022 (J-005, J-017)
├── J-023 (J-017, J-022)
├── J-024 (J-022, J-013)
├── J-025 (J-009, J-013)
├── J-026 (J-009, J-013)
├── J-027 (J-001, J-006)
├── J-028 (J-005, J-013)
├── J-029 (J-017, J-011)
└── J-030 (J-017, J-011)
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
| Technology sequence as a standalone chain | Which capability arrives first, and what does it enable next? | High | Not covered |
| Energy and physical infrastructure | How do hard constraints in compute, data centers, grids, chips, and materials migrate? | High | Not covered |
| Biology and medicine | After generation enters experiments, diagnosis, and care, which steps remain constrained by bodies and trials? | High | Not covered |
| Education and skill formation | When “knowing how” becomes cheap, where do learning, screening, and qualification become scarce? | High | Not covered |
| Geopolitics and institutions | How do compute, data, and critical infrastructure change bargaining power among states and organizations? | Medium | Not covered |
| Law and property | How do liability, data ownership, model output, and licensing rewrite transaction boundaries? | High | Not covered |
| Organizations and employment | How do coordination costs, employment relationships, and firm boundaries change? | High | Not covered |
| Collaboration between people | How does AI mediation change division of labor, trust, negotiation, and joint decisions? | High | Not covered |
| Relationships between people and AI | What norms grow from asymmetries in memory, patience, copyability, and exclusivity? | High | Not covered |
| Attention and trust | When content is unlimited and signals are easy to forge, how are attention and credible credentials allocated? | High | Not covered |
| Capital and power | What new bottlenecks form around compute ownership, financing, and distribution of returns? | Medium | Not covered |
| Human needs, meaning, and embodied presence | Which needs remain stable under supply change, and which preferences actually drift? | Medium | Not covered |

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
| 2026-09-18 | Added field definitions, example, dependency propagation, confidence history, expiry procedure, and explicit gap register | Awaiting subsequent judgments |

---

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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked).
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Unknown (external comparison has not yet been completed in this round; the comparison hypothesis remains to be checked)
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
- **Against consensus**: Consistent with “reasoning scales before agents mature,” but timing remains to be compared.
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
- **Against consensus**: Unknown (external comparison not yet completed).
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
- **Against consensus**: Consistent with the direction of content abundance.
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
- **Against consensus**: Consistent with content abundance, but the field-premium mechanism remains to be compared.
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
- **Against consensus**: Consistent with the direction that trust matters more.
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
- **depends-on**: J-017, J-022.
- **Strongest opposing mechanism**: One-time platform credentials predict fulfillment as well as repeated records; downgrade if they consistently outperform history.
- **Against consensus**: Consistent with trust moving from content toward relationships.
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
- **Against consensus**: Unknown; landscape only.
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
- **Against consensus**: Consistent with knowledge-work automation.
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
- **Against consensus**: Unknown (mechanism pending comparison).
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
- **Against consensus**: Consistent with capability diffusion.
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
- **Against consensus**: Unknown; landscape only.
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
- **Against consensus**: Consistent with the conservative direction that tools do not automatically rewrite every need.
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
- **Against consensus**: Unknown; landscape only.
- **Source**: [Near-term landscape](10-near.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.

## 10. Pre-publication checklist

- [ ] Year boundaries match the single authority in `00-method.md`.
- [ ] Confidence uses only the whitelist: high / medium / low.
- [ ] Every judgment card has ID, proposed date, one-sentence judgment, lens, reasoning chain, time window, falsifier, leading indicator, confidence, depends-on, consensus comparison, source, status, and next review.
- [ ] Every internal link resolves and returns to the source argument.
- [ ] Chinese and English files are updated as equivalent projections in the same commit.
- [ ] Hard constraints use only the five-item whitelist: physical, legal/liability, trust/relationship, ownership/privacy, or embodied presence.
