# 盲判材料准备证据：2026-10-09

## 结论边界

本记录的交付状态是 **`BUNDLE_PREPARED`**，不是重审结果。它证明冻结输入已经被转成去标签、重编号和乱序的材料；**尚无可核验的重审启动证据**。没有独立 reviewer 的原始输出和运行时间，因此不得声称重审已启动、执行或完成，也不得把本记录升级为方法有效性、预测准确率或历史 holdout 证据。

去标签材料只对拿不到本仓库的重审者成立，不是密码学隔离：保留字段仍是判断正文的文字。若同一人同时持有 bundle 和公开仓库，仍可能靠内容比对恢复对应关系。因此 `bundle.json`、原始 seed 和 `R-NN → J-NNN` 映射均不进入 git；本次证据只保留 seed 哈希、输入哈希和输出哈希。

## 冻结输入

- manifest：`docs/evidence/blind-review/manifest-2026-10-09.json`
- `source_commit`：`0eb7474ef19533d9db40ba966e0ccf788ea05adb`
- 纳入规则：中英文当前台账卡均具备 `judgment`、`audience`、`reasoning_chain`、`time_window`、`falsifier`、`leading_indicator` 六个必填保留字段。
- 覆盖：候选 197；纳入 102；排除 95。排除项是 `docs/evidence/legacy-ledger-migration.md` 的迁移快照，它们重复当前判断，不构成第二套判断。
- manifest SHA-256：`7c06add34bb30f022b5ad9dc25b915cb53d6bc77d7627f7d9d8dde40caa881ee`

## 运行记录

生产运行使用仓库外临时目录；seed 由 `secrets.token_hex(32)` 生成，原文不记录，只记录哈希 `8092bf51618ff9b95a7d51dfb9b0c7a63e7ee0a285c091f1ec1f099d51ad3d0d`。

```sh
# 实际执行的命令（seed 原文只存在于本地 shell 变量）
tmpdir=$(mktemp -d /tmp/foresight-blind-bundle.XXXXXX)
seed=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
python3 scripts/blind_bundle.py \
  --repo . \
  --manifest docs/evidence/blind-review/manifest-2026-10-09.json \
  --output-dir "$tmpdir/bundle" \
  --mapping-out "$tmpdir/mapping.json" \
  --seed "$seed" \
  --verify-determinism \
  --evidence docs/evidence/blind-review/bundle-prepared-2026-10-09.json
# exit code: 0
```

生产结果：

- 状态：`BUNDLE_PREPARED`
- bundle SHA-256：`a2fdc9db7f46cf6236568c12a0038e994f0e9d7315f451a35fed0c635a47cda1`
- 记录数：102；中文 102；英文 102
- 两个独立临时目录：逐字节一致；两次哈希均为上述 bundle 哈希。
- 反转 manifest 卡片顺序：输出逐字节一致。
- 普通 checkout 与 `git archive HEAD`：`archive_same_bytes=true`。
- 不同 seed：fixture 自测已证明顺序可改变；生产 bundle 只记录本次 seed 哈希。
- mapping：仅写入仓库外临时目录；bundle 不含 mapping，生成器不读取 mapping。

## 自测与边界攻击

`python3 scripts/blind_bundle.py --self-test` 退出码为 0，输出 `SELF_TEST_PASSED`：fixture 4 张卡、9 个单缺陷负例、9 个 mutation。每个负例均非零退出并点名 `R-NN`；本轮示例包括 `R-04` 的旧编号、`R-01` 的 status、`R-03` 的修订理由／普及闸／同形旧编号。9 个 mutation 分别禁用 identifier、status、metadata、gate、path、title、dependency 分支后恰好放行对应缺陷。自测还验证 `mapping_pairs_match_bundle=true`、manifest 哈希闸、mapping 仓内拒绝、`archive_same_bytes=true`、`seed_changes_assignment=true`。

这些全是结构与隔离证据。它们不证明历史规则有效、不证明预测准确、不证明重审已经开始，也不证明对同时拥有 bundle 和仓库的人具有密码学不可逆性。

## 检查记录

- `npm run check`：退出码 0；`files checked: 95`、`internal links: 2960`、判断卡 `zh 102 / en 102`、登记推演链 11；输出为 `all automated pre-publication checks pass`。这只是机械结构证据，不是方法有效性或预测准确率证据。
- `git diff --check`：退出码 0，无输出。
- 提交前工作树：`git status --short` 列出本证据包、生成器、manifest、双语 protocol（以及 `docs/evidence/blind-review/` 下的 JSON）；bundle、seed、mapping 不在仓库。提交后应再次确认工作树干净。
