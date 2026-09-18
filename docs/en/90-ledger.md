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
| J-TECH-001 | 2026-09-18 | Unit reasoning cost falls another order of magnitude by the end of 2029 | 2026–2029 | High | — | PENDING |
| J-SCAR-001 | 2026-09-18 | Objective quality selection is a 2–4 year window, not durable scarcity | through 2029 | Medium-high | J-TECH-001 | PENDING |
| J-SCAR-002 | 2026-09-18 | Ownership and usable form of private personal or organizational context are more likely to become durable scarcity | 2027–2033 | Medium | J-TECH-001, J-SCAR-001 | PENDING |
| J-SCAR-003 | 2026-09-18 | As AI executes actions, infrastructure that makes actions reversible becomes scarce | 2027–2032 | Medium-high | J-TECH-001 | PENDING |
| J-SCAR-004 | 2026-09-18 | Raw signals, accountable commitments, and verified causality become more valuable than reproducible text | 2029–2033 | Medium | J-TECH-001 | PENDING |

The overview is a navigation aid. The full card, strongest opposing mechanism, and evidence remain in the relevant narrative chain and must stay synchronized here.

---

## 3. The `depends-on` graph

### Notation

Use comma-separated formal IDs, for example: `depends-on: J-TECH-001, J-SCAR-001`. A dependency means “if the upstream mechanism fails, this judgment must be reviewed”; it does not mean that both judgments happen simultaneously or point to an article location. A far-horizon judgment without an explicit near-term dependency should be downgraded to landscape only.

Current chain:

```text
J-TECH-001 (reasoning cost keeps falling)
├── J-SCAR-001 (selection is a window)
│   └── J-SCAR-002 (private context is more durable scarcity)
├── J-SCAR-003 (reversible-action infrastructure)
└── J-SCAR-004 (non-recombinable inputs appreciate)
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
| 2026-09-18 | J-TECH-001 and other initial judgments | Not due | Registered; no review point yet | PENDING | Initial registration | Review at each card's window/checkpoint |

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
| J-SCAR-002 | Ownership layer for private context | Property / privacy | Candidate |
| J-SCAR-003 | Reversible-action infrastructure for AI | Irreversibility | Candidate |
| J-SCAR-004 | Accountable commitment layer | Legal liability | Candidate |
| J-SCAR-001 | AI-output selection and quality control | No hard constraint; likely automatable | Window |

---

## 8. Review log

| Date | Action | Result |
|---|---|---|
| 2026-09-18 | Added field definitions, example, dependency propagation, confidence history, expiry procedure, and explicit gap register | Awaiting subsequent judgments |
