# Actionability audit for J-096 onward — 2026-10-18

This audit checks every judgment card from J-096 through J-116, in both language shards. The question is narrow: does each card say **who** can act, **what they can do now and in what setting**, and **which indicators to inspect next**? It does not re-validate the forecast itself.

## Harvest scope and coverage

| Language | Files scanned | Cards found | Coverage |
| --- | --- | ---: | --- |
| Chinese | `docs/zh/ledger/96-102.md`, `103-110.md`, `111-113.md`, `114-116.md`, `117-120.md` | 21 | J-096–J-116, every registered card |
| English | `docs/en/ledger/96-102.md`, `103-110.md`, `111-113.md`, `114-116.md`, `117-120.md` | 21 | Same 21 IDs |

The harvest was deliberately wider than the suspected problem: all 21 cards were inspected, not only cards whose headings mention technology or embodied systems. No ledger shard in the J-096–J-116 range was unscanned.

## Kill list

Each row below was a candidate finding generated during the wide scan: “the action section may be missing, generic, or mismatched.” The candidate was killed only after reading both language versions and checking for the three required elements. A killed candidate is not a defect.

| Card | Chinese pointer | English pointer | Falsification result |
| --- | --- | --- | --- |
| J-096 | `docs/zh/ledger/96-102.md:11` | `docs/en/ledger/96-102.md:11` | Killed: names a care-service operations lead, a 20-record institutional sample, and coordination/leave/service indicators. |
| J-097 | `docs/zh/ledger/96-102.md:33` | `docs/en/ledger/96-102.md:33` | Killed: names a nursing-facility equipment lead, 10 transfer/observation tasks, and retention/takeover/incident indicators. |
| J-098 | `docs/zh/ledger/96-102.md:55` | `docs/en/ledger/96-102.md:55` | Killed: names a high-liability procurement/risk lead, one narrow workflow plus a revocation drill, and contract/revocation/liability indicators. |
| J-099 | `docs/zh/ledger/96-102.md:77` | `docs/en/ledger/96-102.md:77` | Killed: names an operating supervisor, 20 comparable task records, and task-hours/takeover/exception/headcount indicators. |
| J-100 | `docs/zh/ledger/96-102.md:99` | `docs/en/ledger/96-102.md:99` | Killed: names a family-care coordinator, 10 episodes for one recipient, and burden/coordination/takeover indicators. |
| J-101 | `docs/zh/ledger/96-102.md:121` | `docs/en/ledger/96-102.md:121` | Killed: names a local embodied-deployment lead, five local sites, and deployment/repair/retention/insurance indicators. |
| J-102 | `docs/zh/ledger/96-102.md:143` | `docs/en/ledger/96-102.md:143` | Killed: names a buyer or industrial-policy evaluator, 10 completed projects, and ownership/liability/wage/price indicators. |
| J-103 | `docs/zh/ledger/103-110.md:13` | `docs/en/ledger/103-110.md:13` | Killed: names a general-purpose AI product lead, 30 real requests, and usage/free-tier/delegated-payment indicators. |
| J-104 | `docs/zh/ledger/103-110.md:36` | `docs/en/ledger/103-110.md:36` | Killed: names a city-transport/workplace-policy lead, 10 employers, and attendance/remote-work/commuting indicators. |
| J-105 | `docs/zh/ledger/103-110.md:58` | `docs/en/ledger/103-110.md:58` | Killed: names a pension-insurance product lead, a coded national proposal table, and exhaustion/savings/budget/market indicators. |
| J-106 | `docs/zh/ledger/103-110.md:80` | `docs/en/ledger/103-110.md:80` | Killed: names an NGO finance lead, a 12-month project substitution table, and aid/defence/refugee/fiscal indicators. |
| J-107 | `docs/zh/ledger/103-110.md:104` | `docs/en/ledger/103-110.md:104` | Killed: names an older-worker hiring analyst, two comparable age bands, and age-specific employment indicators. |
| J-108 | `docs/zh/ledger/103-110.md:126` | `docs/en/ledger/103-110.md:126` | Killed: names a security-policy researcher, four-country dated official records, and timestamped A/B response indicators. |
| J-109 | `docs/zh/ledger/111-113.md:13` | `docs/en/ledger/111-113.md:13` | Killed: names a city-housing analyst, three metropolitan areas, and housing/inflow/family-formation indicators. |
| J-110 | `docs/zh/ledger/111-113.md:34` | `docs/en/ledger/111-113.md:34` | Killed: names a labour-and-care planning lead, one registered receiving country, and migration/care/housing/credential indicators. |
| J-111 | `docs/zh/ledger/111-113.md:55` | `docs/en/ledger/111-113.md:55` | Killed: names a family-policy evaluator, three OECD countries aligned by year, and childcare/fertility/employment indicators. |
| J-112 | `docs/zh/ledger/114-116.md:12` | `docs/en/ledger/114-116.md:12` | Killed: names a cultural-venue or city-culture lead, 20 visits/purchases, and time/price/access/streaming indicators. |
| J-113 | `docs/zh/ledger/114-116.md:32` | `docs/en/ledger/114-116.md:32` | Killed: names an insurer or local-finance lead, latest-quarter records by income group, and loss/insurance/outage/adaptation indicators. |
| J-114 | `docs/zh/ledger/117-120.md:13` | `docs/en/ledger/117-120.md:13` | Killed: names an embodied-deployment lead, five runs in each of two settings, and retention/takeover/incident/renewal indicators. |
| J-115 | `docs/zh/ledger/117-120.md:34` | `docs/en/ledger/117-120.md:34` | Killed: names a power-system planning lead, 10 recent projects, and interconnection/storage/permitting/cancellation indicators. |
| J-116 | `docs/zh/ledger/117-120.md:55` | `docs/en/ledger/117-120.md:55` | Killed: names an advanced-manufacturing supply-chain lead, three substitute paths, and qualification/yield/utility/insurance indicators. |

## Survivors and lanes

No candidate survived the falsification pass. Therefore there are no `fix-doc`, `code-bug`, `fix-code-trivial`, or `user-call` findings from this audit, and no card needed to be downgraded to “landscape only.” The action text is not a generic “monitor the trend” instruction: every card specifies a local sample or comparison, a time-bounded first step, and a next-indicator set. The English and Chinese rows are corresponding actions rather than one language using a shared template to hide a missing action.

This result does **not** claim that the judgments are correct or that the proposed samples are statistically sufficient for causal inference. It only records that the cards satisfy the actionability check requested by this goal.

## Self-imposed constraints — say the word and any of these is dropped

- **[self-imposed] Treat “who / what now / what to watch” as three separately required fields** — this makes the audit falsifiable instead of accepting a generic action sentence.
- **[self-imposed] Require a concrete local-first sample or comparison** — this preserves the cards’ existing distinction between an immediately inspectable observation and a population-level background indicator.
- **[self-imposed] Check both language shards for every ID** — this tests bilingual correspondence without treating translation identity as a substitute for meaning.

## Verification command and provenance

The harvest and parity check reported 21 cards in each language, no action-field issues, and no ID mismatches for J-096 onward. The exact command was a repository-local Python scan over the five ledger shards per language; the pointers above are the evidence used for the per-card kill decisions.

The scan was run against the exact index tree that became audit commit `815850410a61008bc1baa002dcfc4188706310c6`. The pre-commit tree digest was `d55a7e2afa87fd6c28c45d5c6f7c02e04119d3ea` (the `CommitWork`-returned tree for that commit). The reviewed ledger paths in that tree were:

```text
docs/zh/ledger/96-102.md
docs/zh/ledger/103-110.md
docs/zh/ledger/111-113.md
docs/zh/ledger/114-116.md
docs/zh/ledger/117-120.md
docs/en/ledger/96-102.md
docs/en/ledger/103-110.md
docs/en/ledger/111-113.md
docs/en/ledger/114-116.md
docs/en/ledger/117-120.md
```

This provenance identifies the committed source tree being audited; it does not claim that a later tree has identical card contents. The subsequent provenance-only correction is recorded in the commit that modifies this audit file.
