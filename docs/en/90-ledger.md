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
- **Status**: `待定` / **PENDING** (ACTIVE, awaiting evidence), `命中` / **HIT** (supported), or `证伪` / **FALSIFIED** (falsifier triggered). If rewritten, preserve the old card and assign the new version a new ID.

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
> - **Status**: PENDING (example value).

Copy the fields, not the example ID. The example does not enter the formal index.

---

## 2. Registered-judgment overview

| ID | Proposed date | One-sentence judgment | Time window | Confidence | depends-on | Status |
|---|---|---|---|---|---|---|
| J-001 | 2026-09-18 | Unit reasoning cost falls another order of magnitude by the end of 2029 | 2026–2029 | High | — | PENDING |
| J-002 | 2026-09-18 | Objective quality selection is a 2–4 year window, not durable scarcity | through 2029 | Medium-high | J-001 | PENDING |
| J-003 | 2026-09-18 | Ownership and usable form of private personal or organizational context are more likely to become durable scarcity | 2027–2033 | Medium | J-001, J-002 | PENDING |
| J-004 | 2026-09-18 | As AI executes actions, infrastructure that makes actions reversible becomes scarce | 2027–2032 | Medium-high | J-001 | PENDING |
| J-005 | 2026-09-18 | Raw signals, accountable commitments, and verified causality become more valuable than reproducible text | 2029–2033 | Medium | J-001 | PENDING |

The overview is a navigation aid. The full card, strongest opposing mechanism, and evidence remain in the relevant narrative chain and must stay synchronized here.

---

## 3. The `depends-on` graph

### Notation

Use comma-separated formal IDs, for example: `depends-on: J-001, J-002`. A dependency means “if the upstream mechanism fails, this judgment must be reviewed”; it does not mean that both judgments happen simultaneously or point to an article location. A far-horizon judgment without an explicit near-term dependency should be downgraded to landscape only.

Current chain:

```text
J-001 (reasoning cost keeps falling)
├── J-002 (selection is a window)
│   └── J-003 (private context is more durable scarcity)
├── J-004 (reversible-action infrastructure)
└── J-005 (non-recombinable inputs appreciate)
    └── To be registered: contractual data pricing
        └── To be registered: trust collateralization (far horizon, possibly landscape only)
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

1. Filter the overview for PENDING judgments whose window has ended. Read the full card and every upstream `depends-on` judgment first.
2. Check the card's **falsifier** literally: did the specified observable trigger occur? If so, record **FALSIFIED**, with date, evidence, and observation scope.
3. If the falsifier did not trigger, check the **leading indicator**: did it move in the expected direction, at the stated frequency, and without missing or substituted data? Supporting indicators without the full outcome remain PENDING; do not pre-label HIT.
4. Record **HIT** only when evidence within the window clearly supports the judgment and no falsifier triggered. State the supporting evidence and uncovered counterexamples.
5. If evidence is insufficient, leave the card PENDING, record `PENDING / insufficient evidence`, set the next review date, and name the missing indicator.
6. Check all downstream dependencies: an upstream HIT, FALSIFIED, or revision can require downstream review. Follow the propagation steps in Section 3.
7. Update both ledgers in one commit. Add the date, per-card result, evidence anchors, and next action to the review log. The commit message must name the judgment ID and new evidence, never a generic “update docs.”

Review-log format:

| Date | Judgment ID | Falsifier check | Leading-indicator check | Result (HIT / FALSIFIED / PENDING) | Evidence | Next action |
|---|---|---|---|---|---|---|
| 2026-09-18 | J-001 and other initial judgments | Not due | Registered; no review point yet | PENDING | Initial registration | Review at each card's window/checkpoint |

---

## 6. Explicit gaps: dimensions not yet covered

The full-landscape promise remains open. The first chain is not full coverage. Each gap below must remain visible until it receives an independent reasoning chain, bilingual document, and judgment cards.

| Gap dimension | Question to answer | Priority | Status |
|---|---|---|---|
| Energy and physical infrastructure | How do hard constraints in compute, data centers, grids, chips, and materials migrate? | High | Not covered |
| Biology and medicine | After generation enters experiments, diagnosis, and care, which steps remain constrained by bodies and trials? | High | Not covered |
| Education and skill formation | When “knowing how” becomes cheap, where do learning, screening, and qualification become scarce? | High | Not covered |
| Geopolitics and institutions | How do compute, data, and critical infrastructure change bargaining power among states and organizations? | Medium | Not covered |
| Law and property | How do liability, data ownership, model output, and licensing rewrite transaction boundaries? | High | Not covered |
| Organizations and employment | How do coordination costs, employment relationships, and firm boundaries change? | High | Not covered |
| Attention and trust | When content is unlimited and signals are easy to forge, how are attention and credible credentials allocated? | High | Not covered |
| Capital and power | What new bottlenecks form around compute ownership, financing, and distribution of returns? | Medium | Not covered |
| Human needs, meaning, and embodied presence | Which needs remain stable under supply change, and which preferences actually drift? | Medium | Not covered |

Gaps may be filled or explicitly downgraded later, but never silently removed.

---

## 7. Formal judgment and opportunity index

| Source judgment | Opportunity or window | Hard constraint | Status |
|---|---|---|---|
| J-003 | Ownership layer for private context | Property / privacy | Candidate |
| J-004 | Reversible-action infrastructure for AI | Irreversibility | Candidate |
| J-005 | Accountable commitment layer | Legal liability | Candidate |
| J-002 | AI-output selection and quality control | No hard constraint; likely automatable | Window |

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
- **Reasoning chain**: Reasoning is parallelizable deterministic computation → cumulative production and engineering optimization create a learning curve → hardware efficiency, model efficiency, and scheduling/reuse provide relatively independent cost-decline paths → equal capability can be called more frequently.
- **Time window**: 2026-01 to 2029-12.
- **Falsifier**: For 18 consecutive months, the lowest public unit price for equal capability rises rather than falls, and the rise cannot be explained by temporary demand congestion or a one-off energy shock.
- **Leading indicator**: Lowest public price for a fixed benchmark score, energy per unit of compute, and months for open models to catch the strongest closed model at the time; observe twice yearly.
- **Confidence**: High.
- **depends-on**: —.
- **Strongest opposing mechanism**: Energy, chip supply, or regulation creates a common hard ceiling that disables all three decline paths; if the falsifier triggers, withdraw this judgment and its downstream cost premise.
- **External comparison**: This is where the conclusion agrees with the consensus; the independent part is the redundant three-path reasoning, not an external forecast.
- **Status**: PENDING.

### J-006 · Reasoning throughput precedes long-horizon autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: By 2028, the number of parallel reasoning paths affordable per task will rise substantially, making generate–compare–revise workflows common before long-horizon autonomous execution.
- **Reasoning chain**: J-001 lowers unit cost → the same budget runs more candidate paths → a scheduler parallelizes simple steps and upgrades difficult ones → workflows shift from one answer to candidate search.
- **Time window**: 2026–2028.
- **Falsifier**: By the end of 2028, mainstream systems still support only one path per comparable task, and cost declines have not translated into parallel attempts.
- **Leading indicator**: Per-task sample count, end-to-end latency, and quality curves for public systems; observe twice yearly.
- **Confidence**: High.
- **depends-on**: J-001.
- **Strongest opposing mechanism**: Energy, bandwidth, or provider queues trap lower costs inside single calls; withdraw this judgment if per-task parallelism does not rise for two years.
- **External comparison**: This is where the conclusion agrees with the consensus; the difference is treating “throughput before autonomy” as an ordering claim rather than a feature list.
- **Status**: PENDING.

### J-007 · Resumable context precedes reliable long-term memory

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, task-level retrieval context will become a common base for multi-session collaboration before sourced, revisable long-term memory matures.
- **Reasoning chain**: More parallel attempts create more state → one context window cannot hold the full history → tasks, evidence, and open questions must be retrieved → retrieval first solves “bring it back,” while provenance and versions solve “can it be trusted.”
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, mainstream long tasks still rely mainly on unstructured chat replay, and retrieval context produces no measurable continuation gain.
- **Leading indicator**: Long-task recovery rate, retrieval hit rate, and the share of citations from outside the active context window; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006.
- **Strongest opposing mechanism**: Longer windows and stronger models may simply overpower retrieval and memory engineering; downgrade this judgment if long-window systems consistently outperform structured memory on long tasks.
- **External comparison**: The conclusion agrees with the consensus that context matters; the difference is splitting resumable context from trustworthy long-term memory into two steps.
- **Status**: PENDING.

### J-008 · Sourced long-term memory becomes a prerequisite for reliable collaboration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2031, long-term memory with sources, dates, and confidence boundaries will become necessary for high-value continuous collaboration rather than a chat-product extra.
- **Reasoning chain**: Resumable context makes history retrievable → history contains stale and conflicting facts → events need sources, update times, and retraction relations → only revisable memory can support longer autonomous tasks.
- **Time window**: 2028–2031.
- **Falsifier**: By 2031, high-value continuous tasks using memory without provenance, versioning, or retraction maintain the same error rate and accountability as sourced memory.
- **Leading indicator**: Enterprise requirements for memory provenance, timestamps, and retraction APIs; the share of incidents caused by bad memory; observe twice yearly.
- **Confidence**: Medium-high.
- **depends-on**: J-007.
- **Strongest opposing mechanism**: Specialized systems may hide memory defects behind implicit state and human review; withdraw this judgment if long-task adoption grows stably without traceability.
- **External comparison**: The conclusion agrees with the consensus that AI memory will grow; the difference is treating provenance and revisability as the core of reliability, not merely retaining more history.
- **Status**: PENDING.

### J-009 · Continuous execution in constrained workflows matures first

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, constrained workflows with checkable inputs and outputs and limited permissions will achieve stable continuous execution before open-world autonomy matures.
- **Reasoning chain**: Sourced memory reduces repeated errors → closed environments provide a limited state space → permissions and exits can be specified in advance → systems can complete multiple actions and stop at a known failure.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, open-world tasks have reliability indistinguishable from constrained workflows, and permission boundaries and stop conditions no longer affect deployment.
- **Leading indicator**: Consecutive steps completed without intervention, constrained-environment success rate, and safe-stop rate after permission denial; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-008.
- **Strongest opposing mechanism**: A sudden jump in general world modeling could erase the closed/open gap; withdraw this judgment if open tasks catch constrained tasks under the same evaluation standard.
- **External comparison**: The conclusion agrees with the consensus that agents land in constrained tasks first; the emphasis is on observable execution boundaries rather than product categories.
- **Status**: PENDING.

### J-010 · Long-horizon autonomy follows constrained continuous execution

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2033, autonomous execution across longer horizons with fewer human confirmations will reach acceptable reliability in some high-value settings.
- **Reasoning chain**: Constrained workflows accumulate state and failure data → long tasks expose more unanticipated states → the system must pause and request evidence under uncertainty → reliable long-horizon execution depends on environment observation and evaluation loops, not simply longer plans.
- **Time window**: 2029–2033.
- **Falsifier**: By 2033, long-horizon tasks still require step-by-step human confirmation, or their incident rate has not materially fallen from 2029.
- **Leading indicator**: Average action span per authorization, proactive pause rate, human takeover rate, and irreversible incident rate; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Vendors may split long tasks into many hidden short tasks; rewrite this judgment if incident rates fall without expanding environmental observation.
- **External comparison**: The conclusion agrees with the consensus that autonomous agents remain reliability-limited; the difference is specifying the constrained-then-long-horizon mechanism.
- **Status**: PENDING.

### J-011 · Cross-media consistency precedes long-range coherence

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, local consistency of entities and formats across text, images, and audio will become reusable before causal coherence across long time spans.
- **Reasoning chain**: More reasoning throughput → multiple media versions can be sampled for one task → shared representations and constraint checks solve local consistency first → long-range coherence still needs persistent state and repeated evaluation.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, causal, spatial, and action coherence in long interactive worlds is broadly stable while local cross-media consistency is not a default capability.
- **Leading indicator**: Cross-media entity retention, shot or timbre continuity, and long-horizon state drift; observe quarterly.
- **Confidence**: Medium-high.
- **depends-on**: J-006, J-007, J-010.
- **Strongest opposing mechanism**: A unified world model may solve cross-media and cross-time consistency together; withdraw this judgment if independent tests show simultaneous jumps.
- **External comparison**: The conclusion agrees with the consensus that multimodality expands; the difference is separating “looks alike” from “continues to hold.”
- **Status**: PENDING.

### J-012 · Cross-time coherence depends on state and evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2034, cross-time coherence in long stories, persistent interactive environments, and multi-round design will reach production quality only after state memory and repeated evaluation mature.
- **Reasoning chain**: Local cross-media consistency reduces frame-level errors → long tasks still accumulate drift in entities, space, and causality → sourced memory preserves state → automatic counterexamples and replay evaluation permit ongoing correction.
- **Time window**: 2029–2034.
- **Falsifier**: By 2034, production-grade long-generation neither depends on state tracking and replay evaluation nor has drift comparable to short segments.
- **Leading indicator**: Long-generation state drift, replay reproducibility, and local-retention rate after cross-round edits; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-008, J-011.
- **Strongest opposing mechanism**: A new generation architecture may learn stable world state directly without explicit memory and evaluation; withdraw this judgment if independent tests show long coherence without those components.
- **External comparison**: The conclusion agrees with the consensus that long video and interactive content are harder; the difference is locating the bottleneck in state and evaluation rather than compute alone.
- **Status**: PENDING.

### J-013 · Checkable tool calls precede open-environment action

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2027 to 2030, tool calls with parameters, preconditions, permissions, and structured results will spread before systems expand into continuous action in complex environments.
- **Reasoning chain**: Constrained continuous execution needs explicit boundaries → natural-language tool calls are hard to check → typed interfaces structure actions and results → structured calls first accumulate reliability on a few tools and then expand the tool surface.
- **Time window**: 2027–2030.
- **Falsifier**: By 2030, high-value tools broadly accept unstructured natural-language calls, with no error-rate difference from checkable interfaces.
- **Leading indicator**: Tool-schema coverage, precondition rejection rate, parameter error rate, and replayable-result ratio; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-009.
- **Strongest opposing mechanism**: Models may self-correct through natural language and quickly absorb the value of structure; downgrade this judgment if schema-free tools consistently catch up in real tasks.
- **External comparison**: The conclusion agrees with the consensus that tool calls will standardize; the difference is treating checkability as a prerequisite for continuous action.
- **Status**: PENDING.

### J-014 · Rehearsable environments follow single-tool integration

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2028 to 2032, environments combining snapshots, shadow execution, permission boundaries, and rollback points will arrive after single-tool integration but before high-value autonomous action becomes common.
- **Reasoning chain**: Typed tools express one action → multiple actions share external state → real state cannot be freely trialed → isolation, snapshots, shadow execution, and rollback expand the safe attempt space.
- **Time window**: 2028–2032.
- **Falsifier**: By 2032, high-value autonomous action still writes directly to real environments, and isolation and rollback have not reduced incident cost or procurement barriers.
- **Leading indicator**: Shadow-environment and rollback line items in AI-workflow procurement; recoverable-action ratio; autonomous-action insurance or liability pricing; observe twice yearly.
- **Confidence**: Medium-high.
- **depends-on**: J-010, J-013.
- **Strongest opposing mechanism**: Human approval may replace environment isolation at very low cost; if manual confirmation remains dominant and incident rates stay low, this should not be an independent capability layer.
- **External comparison**: The conclusion agrees with the consensus that sandboxes and guardrails matter; the difference is predicting them to become environment infrastructure rather than a safety add-on.
- **Status**: PENDING.

### J-015 · Formal verification precedes open-world evaluation

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2026 to 2029, tests, schemas, static checks, and counterexample search will be absorbed by generation systems before independent evaluation of real-world outcomes matures.
- **Reasoning chain**: Parallel generation increases candidate count → formal properties can be judged quickly by programs → generate–test–discard loops lower output error → open-world outcomes still require waiting for observation and intervention and cannot be replaced immediately by self-evaluation.
- **Time window**: 2026–2029.
- **Falsifier**: By 2029, open-world outcome evaluation is broadly reliable while formal testing has not entered the default generation loop.
- **Leading indicator**: Default-on automated-test ratio, counterexample-search coverage, schema-violation rate, and formal-verification impact on final adoption; observe quarterly.
- **Confidence**: High.
- **depends-on**: J-006, J-009.
- **Strongest opposing mechanism**: General models may leap directly across formal and open-world evaluation; withdraw this judgment if independent external outcomes remain highly aligned with model self-evaluation across multiple domains.
- **External comparison**: The conclusion agrees with the consensus that automated testing grows in areas such as coding; the difference is specifying its place in the order rather than treating all evaluation as one thing.
- **Status**: PENDING.

### J-016 · Open-world evaluation is the final gate for expanding autonomy

- **Proposed date**: 2026-09-18
- **One-sentence judgment**: From 2029 to 2035, independent observation, causal intervention, and continuous monitoring will become the final technical gate for widening the authorization of long-horizon autonomous action.
- **Reasoning chain**: Formal verification covers only pre-specified properties → long tasks encounter unmodeled states and delayed side effects → external observation and intervention create independent evidence → continuous monitoring turns one-off tests into runtime feedback → authorization boundaries can expand incrementally.
- **Time window**: 2029–2035.
- **Falsifier**: By 2035, long-horizon autonomous systems reach open environments without independent observation, intervention, or continuous monitoring and still match constrained-environment incident rates.
- **Leading indicator**: Share of external evidence in long tasks, causal-experiment trigger rate, runtime pause and rollback rate, and authorization expansion following evaluation results; observe twice yearly.
- **Confidence**: Medium.
- **depends-on**: J-010, J-012, J-014, J-015.
- **Strongest opposing mechanism**: A sufficiently strong world model may compress open environments into a formally simulable space, making independent evaluation unnecessary; withdraw this judgment if simulation forecasts remain at independent-observation quality in real tasks.
- **External comparison**: The conclusion agrees with the consensus that agents need evaluation and monitoring; the difference is treating independent real-world feedback as the final condition for expanded authority rather than post-deployment governance.
- **Status**: PENDING.
