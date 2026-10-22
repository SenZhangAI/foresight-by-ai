# 判断卡查询器

[English version](../en/judgment-query.md)

本仓库当前登记的 123 张判断卡不是另一张静态索引；它们以 `docs/zh/ledger/` 与 `docs/en/ledger/` 下的双语卡片为唯一输入。可复现查询器每次运行都会重新解析两种语言，从卡片标题动态发现连续的 `J-001`–`J-NNN` 编号（当前最高编号为 `J-123`），再要求两边的编号集合相同，校验推演链、状态、置信度和时间窗端点在规范化后保持一致。缺卡、编号缺口或双语元数据漂移会明确报结构错误（退出码 2），不会静默返回不完整结果，因此不会因为维护一张第三份索引而产生漂移。

## 用法

在仓库根目录运行：

```bash
python3 scripts/find-judgments.py --chain C4 --status ACTIVE
```

可组合的过滤字段：

- `--chain C4`：推演链编号，例如 `C4` 或 `C12`；
- `--status ACTIVE|HIT|FALSIFIED|REVISED|LANDSCAPE_ONLY`：卡片状态；`LANDSCAPE_ONLY` 表示仅图景，不能当作可用判断或下注依据；
- `--confidence HIGH|MEDIUM|LOW|LOW_LANDSCAPE`：规范化置信度；
- `--time-window TEXT`：匹配卡片的「时间窗」字段（忽略大小写、空白、常见破折号差异及中英文 `to`/`至` 写法；明确的年月端点会按结构比较）；
- `--format table|json`：默认输出双语 Markdown 表，也可输出机器可读 JSON。

至少给出一个过滤条件。没有过滤条件时命令会明确失败，而不是悄悄打印整张台账。未知状态、置信度或格式由 CLI 明确拒绝；语法合法但登记中不存在的推演链与状态组合会输出 `No judgments matched the query.` 并以退出码 0 结束，保留空结果而不会退化成全量结果。

默认表输出规范化的 `status`、`confidence` 和时间窗，并给出中文与英文一句话判断及两种语言各自的卡片链接；`--format json` 还会保留两种语言各自的标题、原始状态、原始置信度、判断、时间窗和链接，适合脚本继续处理。

## 负例与失败边界

维护者可运行 `python3 scripts/test_find_judgments.py` 验证查询器的负例：删除一侧卡片会报双语编号不一致；改变另一侧的 `status`、`confidence` 或 `time-window` 会报元数据漂移；写入不支持的状态会明确失败。直接调用时，未知字段值和无过滤调用也会由 CLI 拒绝，且不会输出全库。


命令：

```bash
python3 scripts/find-judgments.py --chain C4 --status ACTIVE
```

在当前仓库内容上，结果集应为以下 10 个编号（脚本输出的 `Result count` 应为 `10`）：

| 编号 | 状态 | 置信度 | 时间窗（中文卡原值） |
|---|---|---|---|
| J-073 | ACTIVE | MEDIUM | 2026–2040。 |
| J-074 | ACTIVE | MEDIUM | 2026–2038。 |
| J-075 | ACTIVE | MEDIUM | 2026–2033。 |
| J-076 | ACTIVE | MEDIUM | 2026–2034。 |
| J-077 | ACTIVE | MEDIUM | 2026–2030。 |
| J-078 | ACTIVE | MEDIUM | 2026–2040。 |
| J-099 | ACTIVE | MEDIUM | 2027–2035。 |
| J-100 | ACTIVE | MEDIUM | 2027–2038。 |
| J-101 | ACTIVE | MEDIUM | 2028–2038。 |
| J-102 | ACTIVE | MEDIUM | 2028–2038。 |

这不是手工维护的结果表：修改卡片后重新执行命令，结果集和字段值会从卡片内容重新计算。逐卡阅读请从 [C4 具身智能推演链](chains/40-embodied-intelligence.md) 进入，再打开脚本返回的双语卡片链接。

## 边界

查询器解决的是登记、过滤和双语链接发现，不替代判断质量审查，也不把 `ACTIVE` 解释成“已被历史验证”。历史证据、证伪条件、依赖关系和状态理由仍以[判断台账](90-ledger.md)及卡片正文为准。
