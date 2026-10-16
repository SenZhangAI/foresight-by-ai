# Public main synchronization record — 2026-10-17

This record captures the public verification of the reading-experience update and the current publication boundary. It is an operational release record, not a claim that the forecasts are correct.

## Published tree

- Repository: `SenZhangAI/foresight-by-ai`
- Branch: `main`
- Published commit: `b5b6ce2947bc18e47dc4b7afac963ff21b116402`
- Reading-experience change included as an ancestor: `36d8654a1973fa56a0c93dd4f75e1a8a47229abe`

The published SHA was cross-checked through the GitHub API, anonymous HTTPS `git ls-remote`, and the local `main` ref. The three values matched; the reading-experience commit is an ancestor of the published tree.

## Mechanical check

`python3 scripts/check.py` passed on the publication tree:

- 140 files checked
- 5,013 internal links
- 113 Chinese and 113 English judgment cards
- 16 registered reasoning chains

## Public rendering spot-check

GitHub's own rendered HTML, pinned to the published SHA, returned the following Mermaid container counts:

| Page | Mermaid containers |
| --- | ---: |
| `README.md` | 1 |
| `README.en.md` | 1 |
| `docs/zh/chains/10-generation-becomes-free.md` (C1) | 1 |
| `docs/zh/chains/40-embodied-intelligence.md` (C4) | 2 |
| `docs/zh/chains/90-aging-care-and-institutional-substitution.md` (C9) | 2 |

Browser screenshots of the pinned GitHub Preview pages confirmed that README, C1, C4, and C9 render their headings, prose, and Mermaid diagrams. This does not cover mobile-width layout measurement, forecast accuracy, or the quality of the underlying evidence.
