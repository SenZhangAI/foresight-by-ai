# Public main synchronization record — 2026-10-17

This record captures the public verification of the reading-experience update and the current publication boundary. It is an operational release record, not a claim that the forecasts are correct.

## Published tree

- Repository: `SenZhangAI/foresight-by-ai`
- Branch: `main`
- Initial synchronization checkpoint: `b5b6ce2947bc18e47dc4b7afac963ff21b116402`
- First audit-record commit: `76d816edb4a816a6f1539357c8139cb9e32604d3`
- Latest verification snapshot recorded here: `d7362c77ca2f30398b78afec61b24f4a54f4d52b`
- Reading-experience change included as an ancestor: `36d8654a1973fa56a0c93dd4f75e1a8a47229abe`

At the verification snapshot, three independent readings of the default branch matched:

```text
gh api repos/SenZhangAI/foresight-by-ai/commits/main --jq .sha
d7362c77ca2f30398b78afec61b24f4a54f4d52b

git ls-remote https://github.com/SenZhangAI/foresight-by-ai.git refs/heads/main
d7362c77ca2f30398b78afec61b24f4a54f4d52b  refs/heads/main

git rev-parse main
d7362c77ca2f30398b78afec61b24f4a54f4d52b

git merge-base --is-ancestor 36d8654a1973fa56a0c93dd4f75e1a8a47229abe d7362c77ca2f30398b78afec61b24f4a54f4d52b
exit 0
```

The verification snapshot is intentionally identified separately from the file's own later commits: adding a record necessarily advances `main`, so the commands above are the reproducible evidence rather than a claim that this prose can freeze a moving branch head. Re-run the same three reads before treating it as the current head.

## Mechanical check

`python3 scripts/check.py` passed on the committed archive tree. The observed command output ended with `CHECK_EXIT=0`:

```text
files checked      : 141
internal links     : 5013
judgment cards     : zh 113 / en 113
chains registered  : 16 (C1, C10, C11, C12, C13, C14, C15, C16, C2, C3, C4, C5, C6, C7, C8, C9)

all automated pre-publication checks pass
CHECK_EXIT=0
```

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
