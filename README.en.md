# ai-future · A Foresight Sandbox

[中文版](README.md)

## What this is

This is a public knowledge archive for reasoning about future trends from first principles and then filtering the result for investable opportunities. The question is not merely whether a prediction sounds plausible. It is: when one capability becomes abundant, where do value and constraints migrate? Every usable judgment must carry a reasoning chain, time window, falsifier, leading indicator, and confidence level.

The project does not use anyone's prediction as an argument. It reasons first from supply and demand, human behavior, historical regularities, technology diffusion, and social dynamics. When a conclusion overlaps with common consensus, it is explicitly marked as “consistent with consensus.”

## How to read

- **Enter through the story:** start with the [near-term landscape](docs/en/10-near.md), then follow its J-NNN links.
- **Understand the method:** read the [foresight method](docs/en/00-method.md).
- **Follow technical sequencing:** read `docs/en/05-tech-sequence.md` (the first technical chain is still expanding).
- **Look for investable directions:** read [opportunity candidates](docs/en/40-opportunities.md).
- **Audit the reasoning:** open the [judgment ledger](docs/en/90-ledger.md).

Narrative files make a chain readable; the ledger stores its structured metadata. Narratives cite J-NNN; the ledger records each judgment's window, dependencies, and status. Farther judgments depend on nearer ones, but near/mid/far are coarse containers rather than a strict calendar ordering.

## How to use J-NNN

Every judgment receives a globally unique `J-NNN` identifier (for example, `J-001`). Chinese and English share the same identifier, and identifiers are never reused. From a narrative, follow J-NNN to the ledger for its reasoning chain, falsifier, leading indicator, confidence, and `depends-on` links. When a judgment is falsified, every downstream dependency must be reviewed; the old version remains in git history.

## Where is the judgment overview?

The overview is in [docs/en/90-ledger.md](docs/en/90-ledger.md), mirrored in [docs/zh/90-ledger.md](docs/zh/90-ledger.md). Opportunity sources and gate results are collected in [docs/en/40-opportunities.md](docs/en/40-opportunities.md).

## Document map

| Path | Purpose |
|---|---|
| `docs/{zh,en}/00-method.md` | Foresight rules and judgment-card template |
| `docs/{zh,en}/10-near.md` | Near-term landscape (about 2026–2029) |
| `docs/{zh,en}/20-mid.md` | Mid-term landscape (about 2029–2033) |
| `docs/{zh,en}/30-far.md` | Far-term landscape (about 2033–2041) |
| `docs/{zh,en}/40-opportunities.md` | Opportunities that pass the hard-constraint gate |
| `docs/{zh,en}/90-ledger.md` | Judgment overview, dependency graph, checks, and explicit gaps |
| `docs/glossary.zh-en.md` | Chinese–English terminology |

The articles in `chains/` are reader-facing stories; the numbered files are stable navigation anchors. The structure follows readability and reasoning dependencies, while git commits record how judgments evolve with new evidence.

## Git discipline

The Chinese and English trees must be updated in the same commit. Each commit must state **which judgment (J-NNN) changed and what new evidence motivated the change**; empty log messages such as `update docs` are prohibited. A judgment status transition (`ACTIVE`, `HIT`, `FALSIFIED`, or `REVISED`) should be recorded as its own commit so git can serve as the evolution history.

## Current boundary

The first round begins with one chain about generation becoming cheap. Technical sequencing, organizations, attention and trust, capital, energy, and human needs remain dimensions to develop. Unfinished dimensions must remain visible in the ledger's “explicit gaps”; the project must not pretend that a full landscape already exists.
