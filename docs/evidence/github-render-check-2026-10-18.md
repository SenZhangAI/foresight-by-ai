# GitHub 渲染与窄屏实测（2026-10-18）

本页记录当前公开 `main` 的渲染复核，不把源码大小、WebFetch 摘要或截图解码失败当成渲染结论。测量提交固定为 `0c5bf915221dd3831384af76de9009faacbe4a2f`；公开 `main`、匿名 HTTPS `git ls-remote` 与本地 HEAD 在本轮复核中均指向此提交。

## 1. GitHub 自己的渲染 HTML

预期先写下：每种语言的总览表应为表头加 116 张卡，即 117 行、10 个表头单元；整页台账应有 12 个表格。使用：

```bash
sha=0c5bf915221dd3831384af76de9009faacbe4a2f
for lang in zh en; do
  gh api "repos/SenZhangAI/foresight-by-ai/contents/docs/$lang/90-ledger.md?ref=$sha" \
    -H 'Accept: application/vnd.github.html' > "$lang.html"
done
```

在返回 HTML 上用闭合标签正则（不是 `grep -c '<th'`）清点：

```text
zh render_bytes=599117 headings=153 user_content_ids=153 tables=12 overview_tr=117 overview_th=10 overview_td=1160
en render_bytes=618821 headings=153 user_content_ids=153 tables=12 overview_tr=117 overview_th=10 overview_td=1160
```

总览表在两种语言中都是真正的 117 行、10 列，未发现一段以 `|` 开头的断裂表格文本。Contents 渲染 HTML 是结构证据；它不等同于对页面在手机上的外框尺寸作了实机验证。

## 2. raw、blob 与 JSON 路由的取证边界

完整复核命令的核心形态如下：

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

本轮输出（英文路径同样执行）：

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

因此，blob 页直接 grep `user-content-` 的 0 是 SSR 外壳的假阴性，不是“没有锚点”；同一页面的 JSON 路由补回了渲染锚点。两份 raw 均与固定提交的本地 blob 逐字一致。此前迁移清单的固定提交测量仍见[迁移证据页](legacy-ledger-migration.md)；该页没有因此被分片，中文迁移清单仍是唯一 canonical 历史审计事实源。

## 3. 总览宽表的窄屏量测

量测流程：把第 1 节的 GitHub Contents 渲染 HTML 放入 `article.markdown-body`，使用 `github-markdown-css` 5.9.0；用 Chrome headless 在本地量测页中把正文容器设为 320、343、358、382 px，读取总览表的 `scrollWidth`、可见表头列数，以及 `article.scrollWidth == article.clientWidth`。这量的是 GitHub HTML 加官方 Markdown CSS 的可复现实验，不是把源码文件大小当作版面证据。

| 模拟正文宽度 | 中文：表格滚动宽度；完整可见列 | English: table scroll width; fully visible columns |
|---|---:|---:|
| 320 px | 862 px；3/10 | 1209 px；2/10 |
| 343 px | 862 px；4/10 | 1209 px；2/10 |
| 358 px | 862 px；4/10 | 1209 px；2/10 |
| 382 px | 862 px；4/10 | 1209 px；3/10 |

四个宽度下，页面级 `article.scrollWidth` 都等于容器宽度；溢出发生在表格自己的横向滚动区域，而不是页面级横向溢出。因此窄屏读者需要横向滑动总览表。未验：真实手机、GitHub 移动端外框边距、触摸滚动手感和不同浏览器的实际 viewport；本页不把它们写成已通过。

原始量测页与命令输出保留在本轮 `/tmp/f005-render.*`、`/tmp/f005-mobile.*` 临时目录中；临时目录不是仓库事实源，以上命令、固定提交和结果才是可复核记录。
