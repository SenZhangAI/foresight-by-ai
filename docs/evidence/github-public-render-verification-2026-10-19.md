# GitHub public-render verification — 2026-10-19

This record fixes the public rendering check to commit `91cd9ffa38aa06042d9d4811f5d5444166ad4186` on `origin/main`. The check was performed against that immutable SHA, and the remote was refreshed before capture (`git fetch origin main`; both `git rev-parse refs/remotes/origin/main` and `gh api repos/SenZhangAI/foresight-by-ai/commits/main --jq .sha` returned the same SHA).

## GitHub source parity

The raw GitHub API response matched the pinned git tree byte-for-byte for the ten public entry points used in the check: both READMEs, both near/mid/far landscape pages, and both bilingual ledgers. The comparison used the pinned commit above, not a moving `main` URL or a possibly newer working tree.

The exact parity command was:

```sh
SHA=91cd9ffa38aa06042d9d4811f5d5444166ad4186
for f in README.md README.en.md docs/zh/10-near.md docs/zh/20-mid.md docs/zh/30-far.md docs/en/10-near.md docs/en/20-mid.md docs/en/30-far.md docs/zh/90-ledger.md docs/en/90-ledger.md; do
  local=$(mktemp "$TMPDIR/foresight-local.XXXXXX")
  remote=$(mktemp "$TMPDIR/foresight-raw.XXXXXX")
  git show "$SHA:$f" > "$local"
  gh api "repos/SenZhangAI/foresight-by-ai/contents/$f?ref=$SHA" \
    -H 'Accept: application/vnd.github.raw' > "$remote"
  diff -u "$local" "$remote"
  rm "$local" "$remote"
done
```

The comparison deliberately uses `git show "$SHA:$f"`, not the possibly newer working tree, so the pinned tree and the pinned raw response are the two compared objects.

Captured result (mechanical byte comparison, one line per file):

```text
raw_tree=PASS README.md
raw_tree=PASS README.en.md
raw_tree=PASS docs/zh/10-near.md
raw_tree=PASS docs/zh/20-mid.md
raw_tree=PASS docs/zh/30-far.md
raw_tree=PASS docs/en/10-near.md
raw_tree=PASS docs/en/20-mid.md
raw_tree=PASS docs/en/30-far.md
raw_tree=PASS docs/zh/90-ledger.md
raw_tree=PASS docs/en/90-ledger.md
```

The repository checker also passed on the landing tree:

```text
all automated pre-publication checks pass
WARNINGS (1): en: 1 legacy card(s) through J-086 still lack Audience scale; new cards fail hard
```

The warning is pre-existing legacy-card coverage, not a rendering failure.

## Ledger measurement and the deliberate trade-off

The measurement page used GitHub's rendered HTML plus `github-markdown-css` 5.9.0. It measured the table's rendered box and `scrollWidth`, not source line numbers. A first-screen column counts only header cells fully inside the visible table box; a first-screen row counts only data rows fully inside the 886px viewport. The final public HTML contains 10 header cells and 119 data rows in each language. The measurement page was opened against the immediately preceding public tree `f1b9ce2`; the ten-file raw parity check above proves both ledger HTML sources are unchanged at the evidence commit `91cd9ffa38aa06042d9d4811f5d5444166ad4186`, so the measurements apply to the fixed target files recorded here.

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

The command and captured result for the eight containers were:

```sh
for f in README.md README.en.md docs/zh/10-near.md docs/zh/20-mid.md docs/zh/30-far.md docs/en/10-near.md docs/en/20-mid.md docs/en/30-far.md; do
  gh api "repos/SenZhangAI/foresight-by-ai/contents/$f?ref=91cd9ffa38aa06042d9d4811f5d5444166ad4186" \
    -H 'Accept: application/vnd.github.html' | grep -o 'data-type="mermaid"' | wc -l
done
```

Captured result (mechanical container count, one line per file):

```text
mermaid_container=1 README.md
mermaid_container=1 README.en.md
mermaid_container=1 docs/zh/10-near.md
mermaid_container=1 docs/zh/20-mid.md
mermaid_container=1 docs/zh/30-far.md
mermaid_container=1 docs/en/10-near.md
mermaid_container=1 docs/en/20-mid.md
mermaid_container=1 docs/en/30-far.md
```

Browser Preview screenshots were checked against the preceding public tree `f1b9ce2`; the raw parity results above show those eight Markdown sources are unchanged at `91cd9ffa38aa06042d9d4811f5d5444166ad4186`, so the same rendered diagrams and absence of Mermaid error panels apply to the fixed target files.

**Narrow diagram boundary:** this run did not obtain a browser DOM `clientWidth`/`scrollWidth` reading for the eight Mermaid SVGs at 375–414px. The available browser surface can show screenshots but cannot set a mobile viewport or expose the SVG layout metrics, and the GitHub HTML container count cannot substitute for that measurement. Therefore this record makes no claim that the diagrams fit, do not overflow, or remain readable on a phone; that sub-claim remains explicitly unverified. The maps are retained as navigational diagrams because no field or judgment content was removed, but this is a preservation decision, not a narrow-screen rendering result.


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

Captured sample result (mechanical HTML-container count, not a semantic judgment):

```text
mermaid_container=2 docs/zh/chains/40-embodied-intelligence.md
mermaid_container=2 docs/en/chains/40-embodied-intelligence.md
mermaid_container=2 docs/zh/chains/90-aging-care-and-institutional-substitution.md
mermaid_container=2 docs/en/chains/90-aging-care-and-institutional-substitution.md
mermaid_container=1 docs/zh/90-ledger.md
mermaid_container=1 docs/en/90-ledger.md
```

## 中英摘要

本次检查以公开提交 `91cd9ffa38aa06042d9d4811f5d5444166ad4186` 为固定对象。双语 README、近／中／远页面与台账共十个入口均通过 raw 与本地逐字 diff；项目检查通过，仅保留一条既有旧卡 audience-scale 警告。台账在 900px、1012px、375px、414px 下的盒宽、横向滚动、首屏可见列／行已由 GitHub HTML 与官方 CSS 的本地量测页记录。完整宽表保留为审计与横向比较面，窄屏通过滚动访问全部字段。八个公开导航图逐文件均返回 1 个 Mermaid 容器，且在 preceding public tree 的 Preview 截图中无解析错误；但本运行时没有拿到 375–414px 下 Mermaid SVG 的 DOM 宽度，因而不宣称其手机端不溢出或可读性已验证。其余 Mermaid 则按链骨架与 J-NNN 投影两类抽样记录（逐文件机械计数），避免把抽样误写成全量证明。
