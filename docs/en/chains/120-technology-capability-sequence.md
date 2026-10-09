# C12 · Technology Capability Sequence: what arrives first, and what only then becomes possible

[中文版](../../zh/chains/120-technology-capability-sequence.md)

[Back to README / document map](../../../README.en.md)

> **Registration note (2026-10-10)**: this file used to live at `docs/en/05-tech-sequence.md`. It was written before the [chain registry](../../../README.en.md#chain-registry) existed and never received a number, so from the outside the archive looked as if it had 11 chains and as if it had 12. It is now registered as **C12** under the criteria the registry states (it advances dependencies vertically around one question, carries its testable judgments on `J-NNN` cards, and declares its lenses at the head of the page). It is one of twelve parallel chains: it answers “which capability arrives first,” but it does not decide for the other chains “what becomes abundant,” and it is not a precondition layer shared beneath them; what a capability still has to pass through after it arrives before it becomes a social consequence is answered by [C7](70-capability-to-social-consequences.md). Not a word of the prose or of the 12 cards was deleted; the old path remains as a redirect page.

At four o'clock on Wednesday, Lin gives a workbench one sentence: “Turn last quarter’s customer feedback into three actionable redesigns; do not send anything yet.”

Ten minutes later, the system returns three plans, prototypes, risk lists, and contradictory evidence. It has not failed because it cannot generate. It has failed because it cannot decide what to trust next. Lin asks it to check the sources, open a test environment, and rerun the validation; the system proposes new hypotheses. The decisive change is not one model suddenly learning one task. Capabilities have to arrive in an order: cheap reasoning makes attempts routine, memory connects attempts, interfaces let attempts touch an environment, and evaluation determines which actions deserve to remain.

This chain discusses only how capabilities arrive. It does not pre-write their social consequences. At every step, ask the same question: **what arrives first → what does that make possible → what can arrive next.**

**Lens declaration for this chain** (written 2026-10-10; codes defined in [Methodology §2 · Toolbox of lenses](../00-method.md#2-toolbox-of-lenses); reverse lookup to the five starting points in the [mapping table](../00-method.md#mapping-the-five-starting-points-to-l1l9)):

- **L2 · Constraint migration**: every section ends on a change of bottleneck. Once reasoning becomes cheap, what blocks is “what did I do last time?” (end of section 1); once memory is connected, what blocks is the right “to touch the outside world” (end of section 2); once interfaces are connected, what blocks is “knowing that an action was correct” (end of section 5). That is exactly L2: “Removing one bottleneck does not make every part of a system speed up evenly; the bottleneck jumps to another part”. All 12 cards list L2 in their lens fields.
- **L6 · Irreversibility** (previously unrecorded): section 3's “continuous completion of several steps where the task boundary is clear, actions can pause, and failure has an explicit exit” and section 5's “shadow-run or simulate before touching real state” run on L6: “Low-cost trial and error is valuable only when the result can be undone”. The reasoning chain of [J-014](../ledger/11-20.md#j-014--rehearsable-environments-follow-single-tool-integration), “real state cannot be freely trialed → isolation, snapshots, shadow execution, and rollback expand the safe attempt space”, advances on it as well, while that card's lens field lists only “technology sequencing + L2 constraint migration”; the card has been annotated in place. Per the mapping table, L6 is the only lens carrying the second half of the technology clause (“steps requiring real-world intervention, waiting, energy, responsibility, or irreversible consequences decline more slowly”).

**The backbone has no lens behind it**: the backbone of this chain is which kind of capability arrives **first** and which only later becomes reliable, and at that ordering step the reasoning of this chain is not carried by L1–L9. The “technology sequencing” in the 12 cards' lens fields is none of L1–L9; it is precisely the hardest gap recorded in the [mapping table's “Technology regularities” row](../00-method.md#mapping-the-five-starting-points-to-l1l9): the first half of the clause, “deterministic work that can be parallelized, copied, and digitized is more likely to become cheaper”, is carried by no sentence in the nine definitions. Section 6, “Evaluation first covers formal properties, then the open world”, is almost an unfolding of that half-clause, but its grounds trace back only to the §1 technology clause and to each card's comparison with consensus; **it is not a checkable lens source**. Under §1.3, adding a lens to carry it is a substantive rule change that must first pass historical-case calibration, so this round declares the gap only: no lens is added and no judgment is changed; the lens fields of the 12 cards have been annotated in place. Under the mapping table's standing discipline, when another chain needs “this capability has arrived” as a premise, it must declare `depends-on` to a `J-NNN` in this chain and must not assert arrival in the voice of a lens.

**Lenses not used**: L1, L3, L4, L5, L7, L8, L9. Each was tried in reverse:

- **L1**: this chain only writes capability arrival; it never says anything rises in value because of it. The closest to L1 is the opening, “It has not failed because it cannot generate. It has failed because it cannot decide what to trust next”, but that is the bottleneck jumping from generation to evaluation (L2), not the valuation of a complement; “what rises in value once things are cheap” is carried by [C1](10-generation-becomes-free.md).
- **L3**: L3 says of itself that it is for reasoning about “how products are bundled”, and this chain's strongest opposing case in section 7 does say that “vendor packaging may hide memory, tools, and evaluation inside one product”; but that is a counter-mechanism that could mask the observable order, and this chain derives no packaging boundary from coordination or transaction costs. Section 1's “route simple steps to smaller models” is scheduling, not an organizational boundary.
- **L4**: the time windows here are capability windows, not adoption speed (the ledger's own section for these cards says “the arrival of a capability is not the same as universal adoption”). Depreciation, regulatory, procurement, and skill-formation cycles drive no step in this chain; J-014's leading indicator borrows “shadow-environment and rollback line items in AI-workflow procurement”, but only as a measurement, and the reasoning chain passes through no adoption cycle. Adoption is carried by [C7](70-capability-to-social-consequences.md) and [C4](40-embodied-intelligence.md).
- **L5**: section 2's memory “with sources, dates, and confidence boundaries” and section 6's “facts can be independently checked” look like a credentials question; but L5 is triggered “once the cost of forging text, images, or credentials collapses”, and nowhere does this chain take cheaper forgery as a premise. Sources here are internal state that lets the system revise locally, not a hard-to-forge credential that screeners turn to.
- **L7**: the nearest thing to institutions is [J-016](../ledger/11-20.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy)'s leading indicator “authorization expansion following evaluation results”; but this chain writes authorization expansion as a technical threshold that follows evaluation evidence, and derives neither when institutions settle nor when rents open or close. Authorization institutions are carried by [C11](110-authority-before-intelligence.md).
- **L8**: this chain derives no change in demand; Lin's “do not send anything yet” in the opening is a scene, not a demand derived from a preference for certainty.
- **L9**: the closest to L9 are section 2's long-term memory (L9's first asymmetry, “one side remembers everything while the other remembers only fragments”) and the pausing and rollback of sections 3 and 5 (its third, “one side can be copied, paused, and rolled back at any time”). But in this chain memory is task state, and pausing and rollback are environment controls (derived from L6); no party in the chain builds the relationship model L9 describes, and no new norm, dependency, or form of harm is derived. Relationships between people and AI are carried by [C11](110-authority-before-intelligence.md).

By reverse lookup in the [mapping table](../00-method.md#mapping-the-five-starting-points-to-l1l9), this chain stands on an **extension of supply and demand** (L2, no source sentence in the clause) plus **the second half of the technology clause** (L6); the first half of the technology clause — that is, this chain's backbone — has no lens behind it, as stated above. That is this chain's place in the system: it is not the engine of all the forces, but the chain of one force, “technology,” and that force still has a recorded gap at the lens layer.

> **All 12 cards cited in this file were downgraded by the diffusion gate (2026-09-20)**: the 12 judgments cited here — J-001 and J-006–J-016 — were every one of them ruled **FAIL** on Gate 1 (audience scale) in the ledger-wide review of 2026-09-20. Their audience scale reaches only million-scale (model developers, cloud providers, professionals using knowledge tools, and organizational buyers); each is a technical precondition rather than a daily society-wide activity, two to three orders of magnitude short of the society-level threshold of a hundred million distinct individuals performing the same action every week. All 12 are therefore downgraded to **occupational/organizational judgments** and set to `REVISED`, with the original card text kept word for word and identifiers not reused. Of them, [J-008](../ledger/01-10.md#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration), [J-012](../ledger/11-20.md#j-012--cross-time-coherence-depends-on-state-and-evaluation), [J-015](../ledger/11-20.md#j-015--formal-verification-precedes-open-world-evaluation), and [J-016](../ledger/11-20.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) **land only in this file** and have no second prose location, so this is the only place their downgrade can be stated. For the test see [Historical retrospective · Gate 1](../01-retrospect.md); for the per-card verdicts and this round's counting method see the [judgment ledger · review log](../90-ledger.md#8-review-log).

> **Gate status · read this before reading the capability order (annotated 2026-10-10)**: the “FAIL” in the paragraph above was judged against the original wording of [Historical retrospective · Gate 1](../01-retrospect.md#gate-1--count-the-people-before-you-look-at-the-technology): “the activity this capability serves—**how many people do it, and how often**? The ceiling on how many people a capability can reach is set by the headcount × frequency of that activity, not by the ceiling of the technology.” The “Diffusion-gate review” field of every one of the 12 cards in the table below carries the same conclusion, word for word: “Gate 1 **FAIL** — downgraded by the diffusion gate to an occupational/organizational judgment; not to be cited in the voice of “the whole of society,” “generally,” or “becomes the norm.””, and every one is `REVISED`. The [isolated blind re-review](../../evidence/blind-review-reaudit-2026-10-09.en.md) of 2026-10-09 re-judged these 12 with the labels removed: J-006 was vetoed again at Gate 1, J-011 was vetoed at Gate 2, and the other 10 came back `ABSTAIN` (no gate established a failure; a gate can only veto, so this is no upgrade). **So read the order below with two discounts**: (1) scale — each step holds only within the occupational or organizational population named on the cited card, not as a society-wide trend; (2) method — the “what arrives first” step has no registered lens behind it (see the lens declaration above and the [mapping table's “Technology regularities” row](../00-method.md#mapping-the-five-starting-points-to-l1l9)), and its grounds trace back only to the §1 technology clause and each card's external comparison. The legitimate use of these 12 cards is to be `depends-on`'d by other chains as falsifiable premises that “this capability has arrived” — which is exactly how [C3](30-power-land-and-permits.md), [C4](40-embodied-intelligence.md), and [C7](70-capability-to-social-consequences.md) cite this chain.

| Card | Audience scale (card field) | Gate 1 (2026-09-20) | Isolated blind re-review (2026-10-09) |
|---|---|---|---|
| [J-001](../ledger/01-10.md#j-001--unit-reasoning-cost-keeps-falling) | Million-scale: model developers, cloud providers, and organizational buyers | FAIL | `ABSTAIN` |
| [J-006](../ledger/01-10.md#j-006--reasoning-throughput-precedes-long-horizon-autonomy) | Million-scale: model researchers and infrastructure operators | FAIL | `VETO` · Gate 1 |
| [J-007](../ledger/01-10.md#j-007--resumable-context-precedes-reliable-long-term-memory) | Million-scale: professionals and organizations using knowledge tools | FAIL | `ABSTAIN` |
| [J-008](../ledger/01-10.md#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration) | Million-scale: professionals and organizations needing auditable collaboration | FAIL | `ABSTAIN` |
| [J-009](../ledger/01-10.md#j-009--continuous-execution-in-constrained-workflows-matures-first) | Million-scale: organizations and professionals adopting constrained workflows | FAIL | `ABSTAIN` |
| [J-010](../ledger/01-10.md#j-010--long-horizon-autonomy-follows-constrained-continuous-execution) | Million-scale: high-liability organizations and agent-system operators | FAIL | `ABSTAIN` |
| [J-011](../ledger/11-20.md#j-011--cross-media-consistency-precedes-long-range-coherence) | Million-scale: content and product teams | FAIL | `VETO` · Gate 2 |
| [J-012](../ledger/11-20.md#j-012--cross-time-coherence-depends-on-state-and-evaluation) | Million-scale: long-horizon content, R&D, and operations organizations | FAIL | `ABSTAIN` |
| [J-013](../ledger/11-20.md#j-013--checkable-tool-calls-precede-open-environment-action) | Million-scale: organizations and developers using tool calls | FAIL | `ABSTAIN` |
| [J-014](../ledger/11-20.md#j-014--rehearsable-environments-follow-single-tool-integration) | Million-scale: agent-system operators and high-liability organizations | FAIL | `ABSTAIN` |
| [J-015](../ledger/11-20.md#j-015--formal-verification-precedes-open-world-evaluation) | Million-scale: model developers, enterprise evaluators, and auditors | FAIL | `ABSTAIN` |
| [J-016](../ledger/11-20.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) | Million-scale: high-liability organizations and regulatory or evaluation bodies | FAIL | `ABSTAIN` |

> **Capability-arrival diagram (reading projection):** The diagram below only projects the order already argued in this chapter; it adds no new capability judgment. Full fields remain authoritative in the linked `J-NNN` ledger cards. An arrow means that reliable use treats the earlier capability as a substrate, not that it must become perfect before the later one can appear.
>
> ```mermaid
> flowchart LR
>   A[J-001 lower unit reasoning cost] --> B[J-006 higher throughput and parallel attempts]
>   B --> C[J-007 resumable context]
>   C --> D[J-008 sourced long-term memory]
>   D --> E[J-009 constrained workflow execution]
>   E --> F[J-010 longer bounded execution]
>   B --> G[J-011 cross-media consistency]
>   G --> H[J-012 cross-time coherence]
>   E --> I[J-013 checkable tool calls]
>   I --> J[J-014 rehearsable isolated environments]
>   B --> K[J-015 formal-property evaluation]
>   F --> L[J-016 open-world independent evaluation]
>   H --> L
>   J --> L
>   K --> L
> ```

## 1. First comes cheaper, denser reasoning

The first change is not whether a model can “think,” but whether equal capability can be called many times. Once one answer becomes cheap, a system can explore several routes, retry, route simple steps to smaller models, and reserve stronger models for hard steps. “Generate an answer” becomes “generate, compare, and revise a batch of answers.” This is the cost foundation described by [J-001](../ledger/01-10.md#j-001--unit-reasoning-cost-keeps-falling).

As throughput rises and latency falls, workflows no longer need to be built around one question and one answer. A system can keep working in the background, wait for new evidence, and search locally among candidates. [J-006](../ledger/01-10.md#j-006--reasoning-throughput-precedes-long-horizon-autonomy) is not mainly about a smarter single response; it is about allowing more attempts to happen in parallel inside one task.

But it only opens a possibility. It does not solve “what did I do last time?” or “why did I choose this route?” The next capability therefore is not more candidates, but context that survives.

> **Scope tag · Gate 1**: The cited J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 2. Next comes traceable context and memory

When Lin returns the next day, the system must know which plans were rejected, why they were rejected, and which facts are still hypotheses. Pasting the entire conversation back into the window is not memory: the window fills, old conclusions mix with new facts, and errors get repeated.

The first layer is retrievable short-term context: separate tasks, evidence, decisions, and open questions, then retrieve them when needed. [J-007](../ledger/01-10.md#j-007--resumable-context-precedes-reliable-long-term-memory) describes how this makes a multi-session task resumable. Later, the system must write memory as events with sources, dates, and confidence boundaries rather than as an opaque summary; [J-008](../ledger/01-10.md#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration) makes it possible to ask where a memory came from and whether later evidence overturned it.

Once memory has sources, the system can revise one part when new evidence arrives instead of rewriting everything. Reliable autonomous execution now has a necessary internal state, but it still has no right to touch the outside world.

> **Scope tag · Gate 1**: The cited J-007, J-008 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 3. Then comes autonomous execution bounded by permissions

A system without reliable memory can only repeat suggestions; a system with memory but no boundaries can mistake a hypothesis for an instruction. The first form of autonomous execution is not total release. It is continuous completion of several steps where the task boundary is clear, actions can pause, and failure has an explicit exit.

[J-009](../ledger/01-10.md#j-009--continuous-execution-in-constrained-workflows-matures-first) therefore expects constrained workflows to become reliable first: inputs and outputs can be checked, permissions are narrow, and failures have named exits. This makes “turn a plan into a sequence of actions” possible. Only later will systems attempt longer horizons, fewer human confirmations, and more uncertain states; [J-010](../ledger/01-10.md#j-010--long-horizon-autonomy-follows-constrained-continuous-execution) says that open-world reliability will not arrive at the same time as bounded workflow reliability.

This does not remove safety from the capability chain. It recognizes two different gates: completing an action sequence in a closed environment, and knowing when not to continue in a changing world. The former arrives first; the latter must wait for better state observation and evaluation.

> **Scope tag · Gate 1**: The cited J-009, J-010 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 4. Multimodal generation gains consistency before long-range coherence

When reasoning becomes cheaper and context can persist, systems will handle text, images, audio, and video together. The first breakthrough is not that every style becomes generatable. It is that characters, dimensions, tone, camera, and data remain consistent across media within one task. [J-011](../ledger/11-20.md#j-011--cross-media-consistency-precedes-long-range-coherence) describes this constrained consistency: it turns multimodal output from a pretty sample into composable work material.

Only later comes long-duration coherence: a story preserves causality, space, and motion over time, or an interactive environment changes continuously with the user’s actions. [J-012](../ledger/11-20.md#j-012--cross-time-coherence-depends-on-state-and-evaluation) holds that this requires stronger state memory, world models, and repeated evaluation, so it will not follow automatically from a better one-shot generator.

The sequence claim is narrower: cross-modal resemblance arrives before cross-time validity.

> **Scope tag · Gate 1**: The cited J-011, J-012 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 5. Tools and environment interfaces let capability leave the window

Even a system that can reason, remember, and generate may remain trapped in a chat window. To read a database, edit a file, run an experiment, or control a device, tools must expose understandable actions, permissions, state, and errors. [J-013](../ledger/11-20.md#j-013--checkable-tool-calls-precede-open-environment-action) describes the first typed tool interfaces: the system receives checkable parameters, preconditions, and results rather than only natural language.

An interface is a handle, not a room. High-value work also needs an observable, isolated, recoverable environment where the system can shadow-run or simulate before touching real state. [J-014](../ledger/11-20.md#j-014--rehearsable-environments-follow-single-tool-integration) therefore places the next step in the environment: tool calls, snapshots, permission boundaries, and rollback points combine into a rehearsable workspace.

Only then does the system have an “acting body.” But acting is not knowing that an action was correct. As interfaces multiply, so do error paths; evaluation has to catch up.

> **Scope tag · Gate 1**: The cited J-013, J-014 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 6. Evaluation first covers formal properties, then the open world

The earliest mature evaluation is executable: whether code passes tests, output satisfies a schema, facts can be independently checked, or an action violates a permission. [J-015](../ledger/11-20.md#j-015--formal-verification-precedes-open-world-evaluation) predicts that systems will combine generation with tests, counterexample search, and static checks; “generate many, then discard errors” becomes a default loop.

Open tasks are different. Their correctness may require waiting for real feedback: whether an experiment worked, whether a strategy caused side effects, or whether a long-term goal is still being met. [J-016](../ledger/11-20.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) describes the next step as a loop combining independent evidence, external observation, causal intervention, and continuous monitoring. Longer autonomous execution can expand only when the system knows what it does not know.

The sequence is therefore not a straight line toward “more intelligence.” It is a set of gates:

```text
Lower unit reasoning cost (J-001)
  → higher throughput and parallel attempts (J-006)
  → resumable context (J-007)
  → sourced, revisable long-term memory (J-008)
  → continuous execution in constrained workflows (J-009)
  → longer execution still bounded by permissions (J-010)
  → cross-media consistency (J-011)
  → cross-time coherent generation (J-012)
  → checkable tool calls (J-013)
  → rehearsable, isolated environments (J-014)
  → automatic evaluation of formal properties (J-015)
  → independent evaluation of open-world outcomes (J-016)
```

The claim is not that a later capability must wait for an earlier one to become perfect. It is that reliable use of the later capability treats the earlier one as a substrate. If an upstream judgment is falsified, follow the judgment dependency chain downstream and review the chain instead of editing only the last paragraph.

> **Scope tag · Gate 1**: The cited J-015, J-016, J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.

## 7. Boundary of the chain

The strongest opposing mechanism is not simply “technology may slow down.” Specialized systems, human procedures, and vendor packaging may hide memory, tools, and evaluation inside one product, making the capabilities appear simultaneous. Or energy, hardware supply, and data access may hold reasoning costs on a plateau, preventing parallel attempts from becoming widespread. If either mechanism persists, the windows for [J-001](../ledger/01-10.md#j-001--unit-reasoning-cost-keeps-falling) and [J-006](../ledger/01-10.md#j-006--reasoning-throughput-precedes-long-horizon-autonomy) move, and the later order must be rearranged.

To observe this chain, do not begin by asking which company wins. Ask whether three visible changes occur in sequence: unit reasoning cost continues to fall; systems begin saving sourced state rather than only chat transcripts; and high-value tools offer simulation, permissions, and result checks before expanding autonomous authority. Observable order is a better object for a bet than an attractive end state.

> **Scope tag · Gate 1**: The cited J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](../01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](../90-ledger.md#8-review-log) for card-level evidence.
