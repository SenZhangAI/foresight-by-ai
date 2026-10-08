# Project map and capability declaration

> This is a public navigation map, not a second judgment ledger. The linked chain pages and `J-NNN` ledger cards remain authoritative for judgments, dependencies, evidence, and gaps.

## What this project is

This is a public, bilingual knowledge repository for a future-society sandbox. It starts from historical calibration and constraints from supply and demand, human behaviour, technology, society, and the physical world. It follows reasoning chains into future landscapes while preserving uncertainty, falsifiers, and evidence gaps. Opportunities are one outlet, not the only subject.

## How the public entries divide the work

| Entry | Role |
|---|---|
| `README.md` / `README.en.md` | Five-minute entry, scope, and navigation for new readers |
| `docs/zh/` / `docs/en/` | Bilingual methodology, retrospectives, chains, landscapes, and opportunities |
| `docs/*/ledger/` and `90-ledger.md` | The sole public source for `J-NNN` judgment-card facts, dependencies, and status |
| `docs/evidence/` | Historical-calibration material, evidence boundaries, and reproducibility records |
| `scripts/check.py` | Mechanical invariants for links, bilingual structure, and ledger projections; it does not judge forecast quality |
| `package.json` | Machine-discoverable capability declarations; it does not carry judgment content |

## Current capability declaration

The current `package.json` declares only one `scripts.ship:*` entry: `ship:structure-placeholder`, whose command is `true`. The key must remain in the manifest for the project's quality gate to enumerate it as `npm_ship`; it is a **structural placeholder** that keeps the public repository's capability-registration shape complete, not a gate for content quality, evidence completeness, forecast accuracy, or project completion.

Read its boundaries separately:

- The repository's `scripts/check.py`, prose, ledger, and coverage matrix do not read or aggregate `ship:`;
- An external capability derivation layer may record `scripts.ship:*` as a machine capability, so an external project status may expose “declared but not yet judged” or another mechanical state; this repository does not translate that state into a content-quality conclusion;
- The repository has no release entry point or CI release flow that upgrades this placeholder state into a fact of publication;
- The external derivation rules for a missing key, `null`, `false`, or another non-string value are outside what this repository can verify, so the repository must not assert how they are parsed.

`ship:` therefore only says that the capability-registration shape exists. Whether a judgment is credible, evidence is sufficient, or the current landscape is acceptable must be assessed from the public prose, ledger, and historical review—not from this placeholder key.

## Current boundary

The project is still expanding: public prose now covers, to different degrees, the full-landscape entry, embodied intelligence, care, infrastructure, organizations, education, biomedicine, and supply-chain resilience. Institutional, scale, long-term-outcome, and cross-region evidence remains open in places. The map does not turn “has an entry” into “complete.”

## Reading path

1. To understand the scope quickly, start with the repository-root README.
2. To understand the method, read the [methodology](00-method.md) and [retrospective](01-retrospect.md).
3. To follow causal structure, enter any chain, click a `J-NNN`, and follow `depends-on` upstream.
4. To verify status, use the [judgment ledger](90-ledger.md) and its shards.
5. To challenge a judgment, use its own falsifier through the [contribution and falsification guide](../../CONTRIBUTING.en.md).
