# Technology Capability Sequence

[Back to README / document map](../../README.en.md)

At four o'clock on Wednesday, Lin gives a workbench one sentence: “Turn last quarter’s customer feedback into three actionable redesigns; do not send anything yet.”

Ten minutes later, the system returns three plans, prototypes, risk lists, and contradictory evidence. It has not failed because it cannot generate. It has failed because it cannot decide what to trust next. Lin asks it to check the sources, open a test environment, and rerun the validation; the system proposes new hypotheses. The decisive change is not one model suddenly learning one task. Capabilities have to arrive in an order: cheap reasoning makes attempts routine, memory connects attempts, interfaces let attempts touch an environment, and evaluation determines which actions deserve to remain.

This chain discusses only how capabilities arrive. It does not pre-write their social consequences. At every step, ask the same question: **what arrives first → what does that make possible → what can arrive next.**

> **All 12 cards cited in this file were downgraded by the diffusion gate (2026-09-20)**: the 12 judgments cited here — J-001 and J-006–J-016 — were every one of them ruled **FAIL** on Gate 1 (audience scale) in the ledger-wide review of 2026-09-20. Their audience scale reaches only million-scale (model developers, cloud providers, professionals using knowledge tools, and organizational buyers); each is a technical precondition rather than a daily society-wide activity, two to three orders of magnitude short of the society-level threshold of a hundred million distinct individuals performing the same action every week. All 12 are therefore downgraded to **occupational/organizational judgments** and set to `REVISED`, with the original card text kept word for word and identifiers not reused. Of them, [J-008](90-ledger.md#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration), [J-012](90-ledger.md#j-012--cross-time-coherence-depends-on-state-and-evaluation), [J-015](90-ledger.md#j-015--formal-verification-precedes-open-world-evaluation), and [J-016](90-ledger.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) **land only in this file** and have no second prose location, so this is the only place their downgrade can be stated. For the test see [Historical retrospective · Gate 1](01-retrospect.md); for the per-card verdicts and this round's counting method see the [judgment ledger · review log](90-ledger.md#8-review-log).

## 1. First comes cheaper, denser reasoning

The first change is not whether a model can “think,” but whether equal capability can be called many times. Once one answer becomes cheap, a system can explore several routes, retry, route simple steps to smaller models, and reserve stronger models for hard steps. “Generate an answer” becomes “generate, compare, and revise a batch of answers.” This is the cost foundation described by [J-001](90-ledger.md#j-001--unit-reasoning-cost-keeps-falling).

As throughput rises and latency falls, workflows no longer need to be built around one question and one answer. A system can keep working in the background, wait for new evidence, and search locally among candidates. [J-006](90-ledger.md#j-006--reasoning-throughput-precedes-long-horizon-autonomy) is not mainly about a smarter single response; it is about allowing more attempts to happen in parallel inside one task.

But it only opens a possibility. It does not solve “what did I do last time?” or “why did I choose this route?” The next capability therefore is not more candidates, but context that survives.

> **Scope tag · Gate 1**: The cited J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 2. Next comes traceable context and memory

When Lin returns the next day, the system must know which plans were rejected, why they were rejected, and which facts are still hypotheses. Pasting the entire conversation back into the window is not memory: the window fills, old conclusions mix with new facts, and errors get repeated.

The first layer is retrievable short-term context: separate tasks, evidence, decisions, and open questions, then retrieve them when needed. [J-007](90-ledger.md#j-007--resumable-context-precedes-reliable-long-term-memory) describes how this makes a multi-session task resumable. Later, the system must write memory as events with sources, dates, and confidence boundaries rather than as an opaque summary; [J-008](90-ledger.md#j-008--sourced-long-term-memory-becomes-a-prerequisite-for-reliable-collaboration) makes it possible to ask where a memory came from and whether later evidence overturned it.

Once memory has sources, the system can revise one part when new evidence arrives instead of rewriting everything. Reliable autonomous execution now has a necessary internal state, but it still has no right to touch the outside world.

> **Scope tag · Gate 1**: The cited J-007, J-008 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 3. Then comes autonomous execution bounded by permissions

A system without reliable memory can only repeat suggestions; a system with memory but no boundaries can mistake a hypothesis for an instruction. The first form of autonomous execution is not total release. It is continuous completion of several steps where the task boundary is clear, actions can pause, and failure has an explicit exit.

[J-009](90-ledger.md#j-009--continuous-execution-in-constrained-workflows-matures-first) therefore expects constrained workflows to become reliable first: inputs and outputs can be checked, permissions are narrow, and failures have named exits. This makes “turn a plan into a sequence of actions” possible. Only later will systems attempt longer horizons, fewer human confirmations, and more uncertain states; [J-010](90-ledger.md#j-010--long-horizon-autonomy-follows-constrained-continuous-execution) says that open-world reliability will not arrive at the same time as bounded workflow reliability.

This does not remove safety from the capability chain. It recognizes two different gates: completing an action sequence in a closed environment, and knowing when not to continue in a changing world. The former arrives first; the latter must wait for better state observation and evaluation.

> **Scope tag · Gate 1**: The cited J-009, J-010 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 4. Multimodal generation gains consistency before long-range coherence

When reasoning becomes cheaper and context can persist, systems will handle text, images, audio, and video together. The first breakthrough is not that every style becomes generatable. It is that characters, dimensions, tone, camera, and data remain consistent across media within one task. [J-011](90-ledger.md#j-011--cross-media-consistency-precedes-long-range-coherence) describes this constrained consistency: it turns multimodal output from a pretty sample into composable work material.

Only later comes long-duration coherence: a story preserves causality, space, and motion over time, or an interactive environment changes continuously with the user’s actions. [J-012](90-ledger.md#j-012--cross-time-coherence-depends-on-state-and-evaluation) holds that this requires stronger state memory, world models, and repeated evaluation, so it will not follow automatically from a better one-shot generator.

The sequence claim is narrower: cross-modal resemblance arrives before cross-time validity.

> **Scope tag · Gate 1**: The cited J-011, J-012 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 5. Tools and environment interfaces let capability leave the window

Even a system that can reason, remember, and generate may remain trapped in a chat window. To read a database, edit a file, run an experiment, or control a device, tools must expose understandable actions, permissions, state, and errors. [J-013](90-ledger.md#j-013--checkable-tool-calls-precede-open-environment-action) describes the first typed tool interfaces: the system receives checkable parameters, preconditions, and results rather than only natural language.

An interface is a handle, not a room. High-value work also needs an observable, isolated, recoverable environment where the system can shadow-run or simulate before touching real state. [J-014](90-ledger.md#j-014--rehearsable-environments-follow-single-tool-integration) therefore places the next step in the environment: tool calls, snapshots, permission boundaries, and rollback points combine into a rehearsable workspace.

Only then does the system have an “acting body.” But acting is not knowing that an action was correct. As interfaces multiply, so do error paths; evaluation has to catch up.

> **Scope tag · Gate 1**: The cited J-013, J-014 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 6. Evaluation first covers formal properties, then the open world

The earliest mature evaluation is executable: whether code passes tests, output satisfies a schema, facts can be independently checked, or an action violates a permission. [J-015](90-ledger.md#j-015--formal-verification-precedes-open-world-evaluation) predicts that systems will combine generation with tests, counterexample search, and static checks; “generate many, then discard errors” becomes a default loop.

Open tasks are different. Their correctness may require waiting for real feedback: whether an experiment worked, whether a strategy caused side effects, or whether a long-term goal is still being met. [J-016](90-ledger.md#j-016--open-world-evaluation-is-the-final-gate-for-expanding-autonomy) describes the next step as a loop combining independent evidence, external observation, causal intervention, and continuous monitoring. Longer autonomous execution can expand only when the system knows what it does not know.

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

> **Scope tag · Gate 1**: The cited J-015, J-016, J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.

## 7. Boundary of the chain

The strongest opposing mechanism is not simply “technology may slow down.” Specialized systems, human procedures, and vendor packaging may hide memory, tools, and evaluation inside one product, making the capabilities appear simultaneous. Or energy, hardware supply, and data access may hold reasoning costs on a plateau, preventing parallel attempts from becoming widespread. If either mechanism persists, the windows for [J-001](90-ledger.md#j-001--unit-reasoning-cost-keeps-falling) and [J-006](90-ledger.md#j-006--reasoning-throughput-precedes-long-horizon-autonomy) move, and the later order must be rearranged.

To observe this chain, do not begin by asking which company wins. Ask whether three visible changes occur in sequence: unit reasoning cost continues to fall; systems begin saving sourced state rather than only chat transcripts; and high-value tools offer simulation, permissions, and result checks before expanding autonomous authority. Observable order is a better object for a bet than an attractive end state.

> **Scope tag · Gate 1**: The cited J-001, J-006 are occupational/organizational judgments; their audience ceiling is defined by the cited cards, so this passage makes no society-wide trend claim. See [Historical retrospective · Gate 1](01-retrospect.md#7-running-these-gates-on-what-we-ourselves-have-written) for the criterion and the [ledger review log](90-ledger.md#8-review-log) for card-level evidence.
