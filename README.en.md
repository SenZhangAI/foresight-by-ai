# ai-future · A Foresight Sandbox

[中文版](README.md)

## What this is

This is a public knowledge archive for reasoning about future trends from first principles and then filtering the result for investable opportunities. The core question is not whether a prediction sounds right. It is: when one capability becomes abundant, where do value and constraints migrate? Every usable judgment carries a reasoning chain, a time window, a falsifier, a leading indicator, and a confidence level.

Business opportunities are not the only destination. The project also records **structural consequences**: how people coordinate, how social relationships are rearranged, how people relate to AI, and how power, meaning, and institutions may change. A line with a payer enters the opportunity list; a consequence with no payer but a complete evidence chain remains its equal; only insufficiently evidenced material is labeled “landscape only.”

The project does not use anyone else’s forecast as an argument. It reasons first from supply and demand, human behavior, historical regularities, technology diffusion, and social dynamics. When a conclusion overlaps with common consensus, it is explicitly marked “consistent with consensus.”

## How to read

- **Enter through the stories:** start with the [reasoning chains](docs/en/chains/). The recommended first read is [What Becomes Unbuyable After Generation Becomes Free](docs/en/chains/10-generation-becomes-free.md).
- **Understand the method:** read the [foresight methodology](docs/en/00-method.md).
- **Follow technical sequencing:** read the [technology capability sequence](docs/en/05-tech-sequence.md).
- **Look for investable directions:** read the [opportunity candidates](docs/en/40-opportunities.md).
- **Audit the reasoning:** open the [judgment ledger](docs/en/90-ledger.md).

Reasoning chains make a complete story readable; the technology file answers separately “what arrives first, and what does that make possible next”; the ledger stores structured judgment metadata. Narratives cite `J-NNN`; the ledger records each judgment’s time window, lenses, dependencies, and status. Farther judgments step forward through dependencies rather than being forced into calendar folders.

## How to read the structure

Near, mid, and far are coarse containers, not a strict calendar; each judgment’s own time window supplies the precision. The actual order lives in each card’s `depends-on` links: a farther judgment must say which nearer or mid-horizon judgments it builds on.

To read backward from a far judgment, open its ledger card and follow every `depends-on` link upstream until the chain ends. If a near-term judgment is falsified, search for cards that depend on it and walk downstream layer by layer, marking and reviewing every affected far-horizon judgment. The result keeps the story readable while making the reasoning order traceable.

## How to use `J-NNN`

Every judgment receives a globally unique `J-NNN` identifier (for example, `J-001`). Chinese and English share the same identifier, and identifiers are never reused. From a narrative, follow `J-NNN` to the ledger for its reasoning chain, falsifier, leading indicator, confidence, and `depends-on` links. When a judgment is falsified, every downstream dependency must be reviewed; the old version remains in git history.

## Document map

| Path | Purpose |
|---|---|
| `docs/{zh,en}/00-method.md` | Foresight rules, nine lenses, three exits, and judgment fields |
| `docs/{zh,en}/chains/` | Reader-facing reasoning stories; one chain may cross near, mid, and far horizons |
| `docs/{zh,en}/05-tech-sequence.md` | Technology capability order and dependency chain |
| `docs/{zh,en}/40-opportunities.md` | Opportunity candidates that pass the hard-constraint gate and have a named payer |
| `docs/{zh,en}/90-ledger.md` | Judgment overview, dependency graph, review log, and explicit gaps |
| `docs/glossary.zh-en.md` | Chinese–English terminology |

Near, mid, and far are coarse fields on judgment cards, not narrative folders. Farther judgments necessarily depend on nearer ones, and time windows move as evidence changes; splitting prose by time layer would create duplication and drift. Git commits record how judgments evolve with new evidence.

## Git discipline

The Chinese and English trees must be updated in the same commit. Each commit must state **which judgment (J-NNN) changed and what new evidence motivated the change**; empty log messages such as `update docs` are prohibited. A judgment status transition (`ACTIVE`, `HIT`, `FALSIFIED`, or `REVISED`) should be recorded as its own commit so git can serve as the evolution history.

## Current boundary

The first round now contains one complete reasoning chain and one technology-capability sequence, but the “full landscape” promise remains open. Organizations and employment, attention and trust, capital and power, energy, biology and medicine, education, collaboration between people, and relationships between people and AI remain explicit gaps in the ledger and must not be silently treated as covered.
