# GitHub public-render verification — 2026-10-19

This record fixes the public rendering check to commit `f1b9ce2e071d3f7d462ccfff551923a54174f5ca` on `origin/main`.

## GitHub source parity

The raw GitHub API response matched the local files byte-for-byte for the ten public entry points used in the check: both READMEs, both near/mid/far landscape pages, and both bilingual ledgers. The comparison used the pinned commit above, not a moving `main` URL.

The repository checker also passed on the landing tree:

```text
all automated pre-publication checks pass
WARNINGS (1): en: 1 legacy card(s) through J-086 still lack Audience scale; new cards fail hard
```

The warning is pre-existing legacy-card coverage, not a rendering failure.

## Ledger measurement and the deliberate trade-off

The measurement page used GitHub's rendered HTML plus `github-markdown-css` 5.9.0. It measured the table's rendered box and `scrollWidth`, not source line numbers. A first-screen column counts only header cells fully inside the visible table box; a first-screen row counts only data rows fully inside the 886px viewport. The final public HTML contains 10 header cells and 119 data rows in each language.

| Language | Content width | Table box | Content width (`scrollWidth`) | Horizontal scroll | First-screen readable columns × rows |
|---|---:|---:|---:|---|---:|
| 中文 | 900px | 900px | 900px | no | 10 × 5 |
| 中文 | 1012px | 1012px | 1012px | no | 10 × 7 |
| 中文 | 375px | 375px | 794px | yes | 5 × 5 |
| 中文 | 414px | 414px | 794px | yes | 5 × 5 |
| English | 900px | 900px | 1106px | yes | 8 × 3 |
| English | 1012px | 1012px | 1106px | yes | 8 × 3 |
| English | 375px | 375px | 1106px | yes | 3 × 3 |
| English | 414px | 414px | 1106px | yes | 4 × 3 |

**Decision:** keep the complete wide table as the canonical audit/comparison view. No field is removed and it is not replaced by grouped summaries only. Narrow screens, and the English table at desktop widths, require horizontal scrolling, but every field remains reachable. Narrative readers should enter through the reasoning chains and judgment-card links; the ledger is the stable comparison and audit surface. The one-shot comparison value outweighs the cost of scattering the canonical view merely to eliminate overflow.

## Eight public landscape diagrams

Each of these eight public Markdown pages returned exactly one GitHub `data-type="mermaid"` render container at the pinned commit, and each was opened in GitHub's browser Preview with no Mermaid error panel:

- `README.md`
- `README.en.md`
- `docs/zh/10-near.md`
- `docs/zh/20-mid.md`
- `docs/zh/30-far.md`
- `docs/en/10-near.md`
- `docs/en/20-mid.md`
- `docs/en/30-far.md`

The README maps had required syntax repair during this check: GitHub's parser rejected the earlier grouped/cross-subgraph form even after edge simplification. The final maps define every node once in a flat flowchart with ordinary `-->` edges; the surrounding prose still explains that the arrows are reading entrances rather than causal claims.

The remaining 29 Mermaid blocks were not treated as proven by the eight landscape pages alone. As a minimum sample of both remaining classes, the public HTML returned the following containers:

- Chain skeleton samples: `docs/{zh,en}/chains/40-embodied-intelligence.md` (2 each) and `docs/{zh,en}/chains/90-aging-care-and-institutional-substitution.md` (2 each).
- `J-NNN` projection samples: `docs/{zh,en}/90-ledger.md` (1 each).

## 中英摘要

本次检查以公开提交 `f1b9ce2e071d3f7d462ccfff551923a54174f5ca` 为固定对象。双语 README、近／中／远页面与台账共十个入口均通过 raw 与本地逐字 diff；项目检查通过，仅保留一条既有旧卡 audience-scale 警告。台账在 900px、1012px、375px、414px 下的盒宽、横向滚动、首屏可见列／行已由 GitHub HTML 与官方 CSS 的本地量测页记录。完整宽表保留为审计与横向比较面，窄屏通过滚动访问全部字段。八个公开导航图均在 GitHub Preview 中显示为图且无解析错误；其余 Mermaid 则按链骨架与 J-NNN 投影两类抽样记录，避免把抽样误写成全量证明。
