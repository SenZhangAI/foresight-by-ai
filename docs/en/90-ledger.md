# Judgment Ledger

> The single index of judgments. Any addition or change must update this table.

## Registered judgments

| ID | Claim | Layer | Window | Confidence | Depends on | Consensus | Status |
|---|---|---|---|---|---|---|---|
| J-TECH-001 | Unit reasoning cost falls another order of magnitude by end-2029 | Near | 2026–2029 | High | — | Consistent | ACTIVE |
| J-SCAR-001 | Objective quality selection is a 2–4 year window, not durable scarcity | Near | through 2029 | Medium-high | J-TECH-001 | Divergent | ACTIVE |
| J-SCAR-002 | Ownership and usability of private context become durable scarcity | Near–mid | 2027–2033 | Medium | J-TECH-001, J-SCAR-001 | Partly divergent | ACTIVE |
| J-SCAR-003 | Reversible infrastructure becomes scarce when AI executes actions | Near–mid | 2027–2032 | Medium-high | J-TECH-001 | Partly consistent | ACTIVE |
| J-SCAR-004 | Raw signals, accountable commitments, and verified causality rise in value | Mid | 2029–2033 | Medium | J-TECH-001 | Partly consistent | ACTIVE |

`ACTIVE` awaits testing; `HIT` is supported; `FALSIFIED` is refuted; `REVISED` is superseded by a corrected version. Never delete falsified judgments.

## Dependency graph

```text
J-TECH-001
├── J-SCAR-001
│   └── J-SCAR-002
├── J-SCAR-003
└── J-SCAR-004
    └── future chain: contractual data pricing → trust collateralization
```

When a judgment is falsified or revised, every downstream dependency enters review.

## Opportunity index

| Candidate | Source | Hard constraint | Status |
|---|---|---|---|
| O-001 Private-context ownership | J-SCAR-002 | Ownership/private property | Candidate |
| O-002 Reversible AI action | J-SCAR-003 | Irreversibility | Candidate |
| O-003 Accountable commitment | J-SCAR-004 | Legal liability | Candidate |
| Quality selection; prompt optimization | J-SCAR-001 | None; automatable | Window |

## Explicit gaps

The full-landscape promise remains open. Technical sequence, organizations and employment, attention and trust, capital and power, education, energy and physical constraints, and human needs require additional chains.

## Review log

| Date | Action | Result |
|---|---|---|
| 2026-09-18 | Created the initial ledger and three opportunity candidates | Pending |
