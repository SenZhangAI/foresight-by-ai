# Foresight Method

> This is a rulebook, not a set of forecasts. It defines how we propose, write, compare, and withdraw judgments; concrete judgments live in the narrative chapters and `90-ledger.md`.

## 0. Let the reader see the problem first

Future writing easily becomes a string of attractive assertions: one capability gets stronger, one industry changes, one opportunity appears. Attractive is not the same as useful. We want a reasoning chain that a reader can follow, that can later be checked, and that can be withdrawn when it is wrong.

For that reason, narrative starts with a scene: a specific person, choice, or stuck moment. It then explains the mechanism and attaches verifiable judgment IDs to `90-ledger.md`. Definitions, tables, and metadata cannot replace a story, but a story cannot replace evidence.

## 1. Legitimate starting points

Independent analysis starts from underlying regularities:

- **Supply and demand:** when a supply becomes abundant and approaches marginal cost, value may move to a complementary input that did not become abundant at the same rate; demand itself may also be rewritten.
- **Human regularities:** status competition, loss aversion, willingness to pay for certainty, and preference for embodied presence and accountable responsibility should not be assumed to disappear.
- **Historical regularities:** diffusion follows learning curves and lags; productivity shifts commonly produce disorder before new institutions and divisions of labor emerge.
- **Technology regularities:** parallel, copyable, digital, deterministic work tends to become cheaper; work requiring real-world intervention, waiting, energy, liability, or irreversible consequences falls in cost more slowly.
- **Social regularities:** as a signal becomes easier to forge, screening moves toward a more expensive and harder-to-forge signal.

An argument may not rely on “institution X predicts” or “person Y believes,” nor treat “everyone knows” as an explanation. External material may be consulted after independent analysis for comparison, missing evidence, and counterexamples; it may not replace the reasoning chain.

### 1.1 An honest execution of “do not rely on existing forecasts”

A language model's memory contains existing human judgments, so it cannot honestly claim perfect independence. We use an executable version instead:

1. reason independently from the underlying regularities above before reading external forecasts;
2. compare with external views afterwards;
3. when the conclusion overlaps with mainstream consensus, explicitly write **“consistent with consensus”** rather than presenting remembered consensus as an independent discovery;
4. when no comparison has been done, write **“unknown”** rather than implying independence.

### 1.2 Fixed format for external comparison

For each major judgment that needs comparison, write this section after the independent reasoning:

- **Agreement:** which observations overlap with external material;
- **Disagreement:** which time windows, mechanisms, or boundaries differ;
- **Why I still hold it:** why the underlying reasoning remains valid despite disagreement, or what new evidence lowered confidence.

Do not write only “consistent with research” without saying where the agreement lies. Do not treat external authority as proof that a judgment is true.

## 2. A toolbox of lenses

“Abundance → scarcity” is a useful starting point, not a conclusion that every chain must obey. Each chain states which lenses it uses and why; one to three lenses are usually enough.

### L1 · Abundance → scarcity

When something becomes cheaper and more plentiful, its complementary input may rise in value if it did not become abundant at the same rate. This locates value migration; its boundary is that demand can also be rewritten, so L8 must check it.

### L2 · Constraint migration

Removing one bottleneck does not make every part of a system faster. The bottleneck moves elsewhere. Use this to find new roles, categories, and risks, not only things that become more expensive.

### L3 · Cost structure

Organizational boundaries are shaped by coordination and transaction costs, not technical capability alone. Use it to reason about firm size, employment, outsourcing, and product packaging.

### L4 · Diffusion lag

“Can be done” is not “widely adopted.” Depreciation, regulation, procurement, and skill-formation cycles determine adoption speed. Use it to turn direction into a time window.

### L5 · Signals and forgery

A signal works because forging it remains expensive. When text, images, or credentials become cheap to forge, screening seeks harder-to-forge evidence: guarantees, collateral, repeated relationships, accountable identity, or embodied presence.

### L6 · Irreversibility

Cheap trial and error helps only when results can be undone. If an error causes physical harm, legal liability, property loss, or irreversible reputational damage, the main cost is real-world loss rather than generation.

### L7 · Institutional lag

Technology arrives before institutions. Temporary rents may appear before rules settle, then disappear when rules arrive. Every opportunity must ask not only “when does it open?” but also “when does it close?”

### L8 · Human needs and constants

Supply change does not guarantee stable demand. Status, certainty, accountability, real relationships, and presence are anchors for checking the demand side. If a conclusion requires human nature to suddenly change, reduce confidence or withdraw it.

## 3. The two-way gate: not every scarcity is an opportunity

Whenever a lens produces “something becomes scarce,” complete the following inversion chain:

1. **What becomes abundant:** specify how supply, cost, or speed changes;
2. **What becomes scarce:** identify the direct complement, bottleneck, or newly carried risk;
3. **Can it be made abundant again:** ask whether the same force that made the original thing abundant can automate, copy, or scale this new scarcity;
4. **Classify it:**
   - if the answer is **yes**, record a **window opportunity** (usually a roughly two-to-four-year arbitrage window), not a structural opportunity;
   - if the answer is **no**, name the hard constraint and observable evidence before it may enter the opportunity candidates;
   - if unknown, label it **landscape only**, not an opportunity.

Acceptable hard constraints are these five:

- **Physical:** real-world presence, moving mass, energy use, waiting, or bodily action is required;
- **Law / liability:** a licensable or suable entity must accept responsibility and pay damages;
- **Trust / relationship:** repeated interaction, reputation, and relationship accumulation cannot be generated in one step;
- **Ownership / private property:** a critical input is lawfully held by someone who will not or cannot provide it;
- **Embodied presence:** the demand itself requires someone to be physically present, touch, or share an experience.

Irreversibility is a supporting lens for the consequences of these constraints: when an error causes real harm rather than merely requiring another generation, state that explicitly in the reasoning chain and opposing case, but do not count it as a sixth hard-constraint category.

“People like it” is not a hard constraint. “It feels difficult to automate” is not a hard constraint. Without a named constraint and a negative-case test, the scarcity remains landscape only.

## 4. Judgment cards: the five-part requirement and IDs

All project judgments use a globally unique three-digit `J-NNN` ID. Chinese and English share the same ID; an ID is never reused. Each judgment must have these five parts in the ledger:

1. **Reasoning chain:** which regularities it starts from, which intermediate steps follow, and how the conclusion is obtained;
2. **Time window:** the interval in which it should occur; failure to occur after the interval is evidence;
3. **Falsifier:** a concrete observable event that would make us admit the judgment is wrong;
4. **Leading indicator:** an observable signal that moves first and the number or event to watch;
5. **Confidence:** high / medium / low, representing stake size rather than rhetorical force.

Also record `depends-on` (judgment IDs), lenses, consensus comparison, status, the strongest opposing mechanism, and “what can be done now.” Missing any one of the five parts means the entry is **landscape only**, not a judgment, opportunity basis, or summary claim.

Recommended card fields:

```text
J-NNN · One-line title
Layer: near / mid / far (container only)
Lenses: L1–L8 and why
depends-on: prerequisite J-NNN IDs
Reasoning chain: …
Time window: …
Falsifier: …
Leading indicator: …
Confidence: high / medium / low (why)
Strongest opposing mechanism: …; what observation would make us withdraw
External comparison: agreement / disagreement / why I still hold it
What can be done now: …; label “landscape only” if none
Status: ACTIVE / HIT / FALSIFIED / REVISED
```

## 5. The strongest opposing case must be able to overturn the chain

Every major judgment must contain one concrete opposing mechanism, not the disclaimer “the future is uncertain.” It must:

- be a possible mechanism, not an attitude;
- break a key link in the reasoning chain if it occurs;
- state what we would observe and which judgment we would withdraw.

If no such case can be written, the judgment is not yet thought through and should not become actionable. The opposing case matters as much as the main narrative: it tells readers where to attack and future maintainers what evidence deserves a new commit.

## 6. Time layers and the actual order

Time layers are coarse containers for reading, not falsely precise calendar predictions:

| Layer | Nominal boundary | Main use |
|---|---|---|
| **Near** | approximately 2026–2028 | Capability and early adoption are observable; uncertainty is mainly speed and diffusion; windows can be relatively narrow |
| **Mid** | approximately 2029–2032 | Technical consequences reshape organizations and institutions; uncertainty is mainly social response; use ranges rather than dates |
| **Far** | approximately 2033–2040 | Feedback loops and preference changes compound; much is landscape only unless dependency and evidence are strong |

The layer is only a container; each judgment's own time window supplies precision. The real reasoning order is the `depends-on` graph: a far judgment should name the near or mid judgments on which it rests. A far assertion without dependencies is landscape only. Git history separately records how judgments evolve under new evidence; commit dates are not dates when the future happened.

## 7. Writing for people

This is a public repository, not an internal database. Rigor and appeal must coexist:

1. Begin each time-layer narrative with a **scene slice**: a specific person, place, numbers, and a stuck moment; do not begin with a definition;
2. Use **memorable short subtitles**, such as “Finding something costs more than making it,” not taxonomies only experts can parse;
3. Give each major judgment a **concrete, imaginable example**: who encounters what problem, where, and at what cost or price;
4. Keep **inline metadata at zero**: narrative may contain judgment IDs such as `J-NNN`, while the five-part card belongs in the centralized ledger;
5. Prefer a sentence that can stand alone and be quoted; avoid adjectives such as “revolutionary” and “unprecedented” when they do no argumentative work;
6. Every landscape paragraph must answer “what can be done now.” If it cannot, explicitly write “landscape only,” preserve it, and do not disguise it as an actionable conclusion.

The narrative layer serves human reading. The card layer serves reasoning, review, and bilingual consistency. They are joined by `J-NNN`, rather than interrupting the story with a metadata table.

## 8. Confidence and status

- **High:** several relatively independent mechanisms support the judgment; overturning it would require a mechanism not currently imaginable. High confidence requires a severe, triggerable falsifier.
- **Medium:** several reasons support the direction, but a known counter-event could overturn it.
- **Low:** directional intuition or an incomplete evidence chain; low confidence is landscape only and does not enter opportunity candidates or summaries.

The ledger records hit rates over time. If high-confidence judgments consistently perform worse than medium-confidence ones, first correct the scoring habit rather than changing the definition after the fact.

Status meanings: `ACTIVE` awaits testing; `HIT` receives supporting evidence inside its window; `FALSIFIED` has triggered its falsifier; `REVISED` is rewritten by new evidence while the old version remains in git history. Never delete a falsified judgment: without it, hit rates cannot be calculated and errors cannot be learned from.

## 9. Bilingual and git discipline

Chinese and English are two projections of the same judgment, not two judgment sets. Both trees must be updated in the same commit, share `J-NNN`, and never assign separate English IDs. Each state change (`ACTIVE` → `HIT` / `FALSIFIED` / `REVISED`) should have a clear commit.

A commit message must state: **which judgment changed (J-NNN), what new evidence supports the change, and what changed in the judgment**. Do not use an untraceable diary title such as `update docs`. The ledger holds current state; git holds the complete evolution of judgment.
