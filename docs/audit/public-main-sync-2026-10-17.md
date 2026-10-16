# Public main synchronization record — 2026-10-17

This record captures the public verification of the reading-experience update and the current publication boundary. It is an operational release record, not a claim that the forecasts are correct.

## Published tree

- Repository: `SenZhangAI/foresight-by-ai`
- Branch: `main`
- Initial synchronization checkpoint: `b5b6ce2947bc18e47dc4b7afac963ff21b116402`
- This record's publication commit: `76d816edb4a816a6f1539357c8139cb9e32604d3`
- Reading-experience change included as an ancestor: `36d8654a1973fa56a0c93dd4f75e1a8a47229abe`

After pushing the record, three independent readings of the default branch matched at `76d816edb4a816a6f1539357c8139cb9e32604d3`:

```text
gh api repos/SenZhangAI/foresight-by-ai/commits/main --jq .sha
76d816edb4a816a6f1539357c8139cb9e32604d3

git ls-remote https://github.com/SenZhangAI/foresight-by-ai.git refs/heads/main
76d816edb4a816a6f1539357c8139cb9e32604d3  refs/heads/main

git rev-parse main
76d816edb4a816a6f1539357c8139cb9e32604d3

git merge-base --is-ancestor 36d8654a1973fa56a0c93dd4f75e1a8a47229abe 76d816edb4a816a6f1539357c8139cb9e32604d3
exit 0
```

## Mechanical check

`python3 scripts/check.py` passed on the committed archive tree:

- 141 files checked
- 5,013 internal links
- 113 Chinese and 113 English judgment cards
- 16 registered reasoning chains

## Public rendering spot-check

The following **default-branch URLs** were fetched directly from GitHub. Each returned HTTP 200; the Mermaid marker count is a structural signal that GitHub returned rendered diagram content, not a claim about visual quality:

| Default `main` URL path | HTTP | Mermaid markers |
| --- | ---: | ---: |
| [`README.md`](https://github.com/SenZhangAI/foresight-by-ai/blob/main/README.md) | 200 | 1 |
| [`README.en.md`](https://github.com/SenZhangAI/foresight-by-ai/blob/main/README.en.md) | 200 | 1 |
| [`docs/zh/chains/10-generation-becomes-free.md`](https://github.com/SenZhangAI/foresight-by-ai/blob/main/docs/zh/chains/10-generation-becomes-free.md) (C1) | 200 | 1 |
| [`docs/zh/chains/40-embodied-intelligence.md`](https://github.com/SenZhangAI/foresight-by-ai/blob/main/docs/zh/chains/40-embodied-intelligence.md) (C4) | 200 | 2 |
| [`docs/zh/chains/90-aging-care-and-institutional-substitution.md`](https://github.com/SenZhangAI/foresight-by-ai/blob/main/docs/zh/chains/90-aging-care-and-institutional-substitution.md) (C9) | 200 | 2 |

Browser screenshots of GitHub Preview confirmed the README and the C1, C4, and C9 pages render their headings, prose, and Mermaid diagrams. The default-branch C9 URL was also opened and visually checked after the synchronization; the other pages' HTML marker counts were checked from their default-branch URLs. This does not cover mobile-width layout measurement, forecast accuracy, or the quality of the underlying evidence.
