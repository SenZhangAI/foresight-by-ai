# ai-future · A Foresight Sandbox

[中文版](README.md)

## What this is

This is a public knowledge archive for reasoning about future trends from first principles and then filtering the result for investable opportunities. The core question is not whether a prediction sounds right. It is: when one capability becomes abundant, where do value and constraints migrate? Every usable judgment carries a reasoning chain, a time window, a falsifier, a leading indicator, and a confidence level.

Business opportunities are not the only destination. The project also records **structural consequences**: how people coordinate, how social relationships are rearranged, how people relate to AI, and how power, meaning, and institutions may change. A line with a payer enters the opportunity list; a consequence with no payer but a complete evidence chain remains its equal; only insufficiently evidenced material is labeled “landscape only.”

The project does not use anyone else’s forecast as an argument. It reasons first from supply and demand, human behavior, historical regularities, technology diffusion, and social dynamics. When a conclusion overlaps with common consensus, it is explicitly marked “consistent with consensus.”

## Where to start

Four paths. Pick the one that matches what you want — each lands directly on a file, and none of them requires reading the methodology first.

- **You want a story that lands** → read the reasoning chains. [C1 · What Becomes Unbuyable After Generation Becomes Free](docs/en/chains/10-generation-becomes-free.md) opens on an afternoon when sixty finished options sit on the screen and the person in charge still cannot decide anything. [C2 · When Data Is No Longer Free: How Real-World Signals Become Contract Assets](docs/en/chains/20-real-signals-become-contracts.md) then answers why a single real observation is worth money, and what it takes to write one into a contract. [C3 · Electrons on the Ground: Why the Ceiling on Compute Is Not the Chip but the Transformer and the Permit](docs/en/chains/30-power-land-and-permits.md) pushes the chain down to ground level: once models can be rented and chips can be bought, what you still cannot queue past is a transformer that has not been built and a hearing that has to be held.
- **You want the whole landscape** → read the three time layers in order: [near term, 2026–2028](docs/en/10-near.md) → [mid term, 2029–2032](docs/en/20-mid.md) → [far term, 2033–2040](docs/en/30-far.md). Each covers six dimensions side by side, from technology, content, and trust through to power and meaning.
- **You want directions worth betting on** → go straight to [opportunity candidates](docs/en/40-opportunities.md): four candidates that pass the hard-constraint gate (who pays, how much, why now, strongest counterargument), plus a list of windows you can profit from now but that the same force will close.
- **You want to check whether any of this holds up** → open the [judgment ledger](docs/en/90-ledger.md). Sixty-five judgment cards, each with its reasoning chain, time window, falsifier, leading indicator, confidence, and the upstream judgments it stands on. The rules themselves are in the [foresight methodology](docs/en/00-method.md); start with the hard-constraint gate in section 3.

The chains and the time-layer files cover the same judgments, cut differently: a **chain** follows one causal line all the way down and reads best first; a **time layer** spreads several dimensions across the same window and reads best when you want coverage. Both inline only `J-NNN` in the prose; all metadata lives in the ledger.

The arrival order of technical capability has its own file: [Technology Capability Sequence](docs/en/05-tech-sequence.md) answers only “what arrives first, and what does that make possible next,” without importing social consequences ahead of time.

## How to use `J-NNN`

Every judgment receives a globally unique `J-NNN` identifier (for example, `J-001`). Chinese and English share the same identifier, and identifiers are never reused; opportunity candidates use `O-NNN`.

**Every identifier in the prose is a link** — clicking [J-003](docs/en/90-ledger.md#j-003--the-genuinely-durable-scarcity-is-ownership-of-private-context-about-you-and-its-usable-form) lands directly on its ledger card, with the full reasoning chain, falsifier, leading indicator, confidence, and `depends-on` links. When a judgment is falsified, every downstream dependency must be reviewed; the old version remains in git history.

## How to read the structure

Near, mid, and far are coarse containers, not a strict calendar; each judgment’s own time window supplies the precision. The actual order lives in each card’s `depends-on` links: a farther judgment must say which nearer or mid-horizon judgments it builds on.

To read backward from a far judgment, open its ledger card and follow every `depends-on` link upstream until the chain ends. If a near-term judgment is falsified, search for cards that depend on it and walk downstream layer by layer, marking and reviewing every affected far-horizon judgment. The result keeps the story readable while making the reasoning order traceable.

## Document map

| English | 中文 | What you get |
|---|---|---|
| [Foresight Methodology](docs/en/00-method.md) | [推演方法论](docs/zh/00-method.md) | What makes a judgment count: the five required fields, nine lenses, the hard-constraint gate, and three exits |
| [Technology Capability Sequence](docs/en/05-tech-sequence.md) | [技术能力演进链](docs/zh/05-tech-sequence.md) | The arrival order of capability: twelve gates from unit reasoning cost to open-world evaluation |
| [Near-term landscape, 2026–2028](docs/en/10-near.md) | [近期图景](docs/zh/10-near.md) | What is becoming abundant across six dimensions, and what becomes scarce as a result |
| [Mid-term landscape, 2029–2032](docs/en/20-mid.md) | [中期图景](docs/zh/20-mid.md) | Once the near-term judgments hold, how organizations, content, trust, and collaboration are forced to rearrange |
| [Far-term landscape, 2033–2040](docs/en/30-far.md) | [远期图景](docs/zh/30-far.md) | Load-bearing-wall check: if the mid term holds, what must people and institutions rearrange |
| [Opportunity Candidates](docs/en/40-opportunities.md) | [商机候选](docs/zh/40-opportunities.md) | Directions that pass the hard-constraint gate and have a named payer, plus the list judged to be windows |
| [Reasoning chains C1–C3](#chain-registry) | [推演链 C1–C3](README.md#推演链登记) | Three long vertical arguments; identifiers, topics, status, and file paths all live in the [chain registry](#chain-registry) below |
| [Judgment Ledger](docs/en/90-ledger.md) | [判断台账](docs/zh/90-ledger.md) | Sixty-five judgment cards, the dependency graph, confidence history, review log, and explicit gaps |
| [Glossary](docs/glossary.zh-en.md) | Same file | Chinese–English terminology; judgment identifiers are never translated or renumbered |

## Chain registry

**Chain identifiers are allocated here, and only here.** Before writing a new chain, read this table: which numbers are already spent, and which direction has already been announced. Elsewhere the prose may cite an identifier, but it may not open a new one or restate status — this table is the only authority.

| ID | Topic | Status | Files |
|---|---|---|---|
| C1 | What becomes unbuyable after generation becomes free | Written | [English](docs/en/chains/10-generation-becomes-free.md) · [中文](docs/zh/chains/10-generation-becomes-free.md) |
| C2 | When data is no longer free: how real-world signals become contract assets | Written | [English](docs/en/chains/20-real-signals-become-contracts.md) · [中文](docs/zh/chains/20-real-signals-become-contracts.md) |
| C3 | Electrons on the ground: the bottleneck moves from chips to grids, land, and permits | Written | [English](docs/en/chains/30-power-land-and-permits.md) · [中文](docs/zh/chains/30-power-land-and-permits.md) |
| — (holds no number) | Collateralization of trust: when “speaking well” is no longer a capability signal, society falls back on guarantees, collateral, and long relationships | Announced, not yet written as a chain | Currently in [section 5 of the far-term landscape](docs/en/30-far.md#5-power-and-institutions-more-answers-do-not-mean-dispersed-action-rights) and [J-035](docs/en/90-ledger.md#j-035--responsibility-collateral-enters-the-transaction-structure-for-consequential-ai-output), mostly as “landscape only” |

**Rules**: identifiers are allocated in the order chains are written — never reserved, never reused; the filename is `<ID×10>-<english-slug>.md`, identical in both languages. **A direction that has been announced but not yet written receives no identifier**; it is registered here with its topic and where it currently lives.

Why this table exists: before 2026-09-19 the tail of C1 announced “collateralization of trust” as C3, while the file actually written as C3 was the power-and-permits chain — two unrelated chains colliding on one identifier. The unit that wrote the announcement and the unit that wrote the file had no point of contact, and nowhere in the repository was it recorded what C3 was, so neither could have detected the conflict. The collision was closed on the rule that an identifier must point at a file you can actually open: C3 belongs to the power chain, and the announcement gave its number back and moved to the last row of this table.

## Git discipline

Run `python3 scripts/check.py` (no dependencies) before committing: it checks internal links and anchors, required judgment-card fields, dependency edges agreeing in all three places, and bilingual parity. It does not replace the judgment items in the [pre-publication checklist](docs/en/90-ledger.md#10-pre-publication-checklist). The Chinese and English trees must be updated in the same commit. Each commit must state **which judgment (J-NNN) changed and what new evidence motivated the change**; empty log messages such as `update docs` are prohibited. A judgment status transition (`ACTIVE`, `HIT`, `FALSIFIED`, or `REVISED`) should be recorded as its own commit so git can serve as the evolution history.

## Current boundary

The first round now contains one technology-capability sequence, three time layers, three independent reasoning chains, four opportunity candidates, and sixty-five judgment cards in the ledger. The “full landscape” promise nevertheless remains open: energy and physical infrastructure is now covered by C3, and geopolitics, institutions, law, and property have risen to partial coverage; complete chains for biology and medicine and for education and qualification, concrete human–AI relationship norms, and the upstream materials and climate coupling of chip manufacturing remain uncovered or only partially covered. Those gaps are kept as explicit entries in [section 6 of the ledger](docs/en/90-ledger.md#6-explicit-gaps-dimensions-not-yet-covered) and will not be silently dropped just because the first round produced output.
