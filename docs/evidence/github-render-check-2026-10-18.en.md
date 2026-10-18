# GitHub rendering and narrow-screen measurement (2026-10-18)

This page records a rendering check against the public `main`. It does not treat source-file size, a WebFetch summary, or a screenshot decoding failure as rendering evidence. The measurement is pinned to public commit `0c5bf915221dd3831384af76de9009faacbe4a2f`; public `main`, anonymous HTTPS `git ls-remote`, and the local HEAD all pointed to this commit during the check.

## 1. GitHub's own rendered HTML

The expectation was written before counting: each overview table should contain a header plus 116 cards, therefore 117 rows and 10 header cells; the full ledger should contain 12 tables per language. The fetch shape was:

```bash
sha=0c5bf915221dd3831384af76de9009faacbe4a2f
for lang in zh en; do
  gh api "repos/SenZhangAI/foresight-by-ai/contents/docs/$lang/90-ledger.md?ref=$sha" \
    -H 'Accept: application/vnd.github.html' > "$lang.html"
done
```

Closed-tag patterns (not `grep -c '<th'`) produced:

```text
zh render_bytes=599117 headings=153 user_content_ids=153 tables=12 overview_tr=117 overview_th=10 overview_td=1160
en render_bytes=618821 headings=153 user_content_ids=153 tables=12 overview_tr=117 overview_th=10 overview_td=1160
```

Both language versions therefore render a real 117-row, 10-column overview table. No overview rows appeared as a paragraph beginning with a literal `|`. Contents HTML is structural evidence; it is not a real-device measurement of a phone's outer frame.

## 2. Evidence boundary across raw, blob, and JSON routes

The core form of the reproducible check was:

```bash
curl -sS -o zh.raw -w 'zh raw_http=%{http_code} raw_bytes=%{size_download}\n' \
  "https://raw.githubusercontent.com/SenZhangAI/foresight-by-ai/$sha/docs/zh/90-ledger.md"
cmp -s zh.raw <(git show "$sha:docs/zh/90-ledger.md")
curl -sSL -o zh.blob.html -w 'zh blob_http=%{http_code} blob_bytes=%{size_download}\n' \
  "https://github.com/SenZhangAI/foresight-by-ai/blob/$sha/docs/zh/90-ledger.md"
grep -o 'user-content-' zh.blob.html | wc -l
curl -sSL -H 'Accept: application/json' -H 'X-Requested-With: XMLHttpRequest' \
  -H 'GitHub-Verified-Fetch: true' \
  "https://github.com/SenZhangAI/foresight-by-ai/blob/$sha/docs/zh/90-ledger.md" > zh.json.html
```

The output (the English path was run identically) was:

```text
zh raw_http=200 raw_bytes=317071
zh raw_local_cmp=identical
zh blob_http=200 blob_bytes=771554
zh blob_user_content=0
zh blob_truncated_flags=richTextTruncated":true
zh json_user_content=153
zh json_truncated_flags=richTextTruncated":false
en raw_http=200 raw_bytes=378400
en raw_local_cmp=identical
en blob_http=200 blob_bytes=848820
en blob_user_content=0
en blob_truncated_flags=richTextTruncated":true
en json_user_content=153
en json_truncated_flags=richTextTruncated":false
```

The zero from grepping `user-content-` in the blob page is therefore an SSR-shell false negative, not evidence that anchors are absent; the same page's JSON route restores the rendered anchors. Both raw files matched their local blobs from the fixed commit byte-for-byte. The earlier fixed-commit measurement of the migration inventory remains in the [migration evidence page](legacy-ledger-migration.en.md); it did not justify sharding the inventory, whose Chinese version remains the sole canonical historical-audit source.

## 3. Narrow-screen measurement of the overview table

The procedure placed the GitHub Contents rendered HTML inside `article.markdown-body`, used `github-markdown-css` 5.9.0, and used a local Chrome headless measurement page. The article wrapper was set to 320, 343, 358, and 382 px in turn. The page read the overview table's `scrollWidth`, the number of fully visible header columns, and whether `article.scrollWidth == article.clientWidth`. This is a reproducible experiment on GitHub HTML plus the official Markdown CSS, not a substitution of source-file size for layout evidence.

| Simulated article width | Chinese: table scroll width; fully visible columns | English: table scroll width; fully visible columns |
|---|---:|---:|
| 320 px | 862 px; 3/10 | 1209 px; 2/10 |
| 343 px | 862 px; 4/10 | 1209 px; 2/10 |
| 358 px | 862 px; 4/10 | 1209 px; 2/10 |
| 382 px | 862 px; 4/10 | 1209 px; 3/10 |

At all four widths, the article's `scrollWidth` equalled its container width; overflow was inside the table's horizontal scrolling area, not page-level horizontal overflow. Narrow-screen readers therefore need to swipe the overview table horizontally. **Not measured:** a real phone, GitHub's mobile outer-frame margins, touch scrolling, and browser-specific viewport behaviour. This page does not present those as verified.

The raw measurement pages and command output were kept during this run in `/tmp/f005-render.*` and `/tmp/f005-mobile.*`; those temporary directories are not repository sources of truth. The commands, fixed commit, and results above are the reproducible record.
