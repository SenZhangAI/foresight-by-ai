# Judgment-card query tool

[中文版](../zh/judgment-query.md)

The repository currently registers 123 judgment cards, not a second static index. The bilingual cards under `docs/zh/ledger/` and `docs/en/ledger/` are the only inputs. On every invocation, the reproducible query tool parses both projections, discovers the contiguous `J-001`–`J-NNN` range from the card headings (currently ending at `J-123`), requires the two languages to expose the same ID set, checks that normalized chains, status, confidence, and time-window endpoints agree, and uses the latest Git parent commit to check the bilingual change set for six meaning-bearing fields. A missing card, ID gap, bilingual metadata drift, or unreadable semantic baseline is an explicit structural error (exit code 2), not an incomplete result. This prevents a third maintained index from drifting away from the cards. The query requires a readable Git parent commit; on a GitHub ZIP, shallow clone, or parentless copy it fails closed rather than pretending to complete the semantic check.

## Usage

Run from the repository root:

```bash
python3 scripts/find-judgments.py --chain C4 --status ACTIVE
```

Composable filters:

- `--chain C4`: a reasoning-chain identifier such as `C4` or `C12`;
- `--status ACTIVE|HIT|FALSIFIED|REVISED|LANDSCAPE_ONLY`: the card status; `LANDSCAPE_ONLY` is a landscape-only card and must not be treated as an actionable judgment or bet;
- `--confidence HIGH|MEDIUM|LOW|LOW_LANDSCAPE`: the normalized confidence value;
- `--time-window TEXT`: match the card's time-window field (case, whitespace, common dash differences, and bilingual `to`/`至` wording are normalized; explicit year/month endpoints are compared structurally);
- `--format table|json`: a bilingual Markdown table by default, or machine-readable JSON.

At least one filter is required. With no filter, the command fails explicitly instead of silently dumping the whole ledger. Unknown statuses, confidence values, or formats are rejected by the CLI. A syntactically valid chain/status combination whose chain is not registered prints `No judgments matched the query.` and exits 0, preserving an empty result rather than falling back to the full register. A newly added bilingual card has no parent snapshot to compare against, so the query explicitly refuses it (`bilingual semantic baseline missing`) instead of skipping semantic checks; the next commit provides a comparable parent snapshot.

The default table output includes normalized `status`, `confidence`, and time window, both one-sentence judgments, and a card link for each language. `--format json` additionally preserves each language's title, judgment, reasoning chain, falsifier, leading indicator, strongest opposing mechanism, raw status, raw confidence, time window, and link for downstream tooling. The semantic check is change-set parity against the latest Git parent: it rejects a meaning-bearing field changed on only one side, but “both sides changed” is not proof that the current Chinese and English semantics are equivalent; synchronized bilingual edits still require human or independent review.

## Negative cases and failure boundaries

Maintainers can run `python3 scripts/test_find_judgments.py` for the query tool's negative suite: deleting a card from one language reports a bilingual ID mismatch; changing the other language's `status`, `confidence`, or `time-window` reports metadata drift; and an unsupported status fails explicitly. Direct calls also reject unknown field values and unfiltered queries without printing the full register.


The command generates its result directly from the current bilingual cards. The block below is an **output-format example only**, not the current repository result and not a fixed card list; run the command above to inspect the current result:

```text
Query: chain=C4, status=ACTIVE
ID | Chains | Status | Confidence | Time window | 中文 | English
---|---|---|---|---|---|---
J-NNN (the script generates bilingual card links from current paths) | C4 | ACTIVE | MEDIUM | <read from card> | <Chinese judgment> | <English judgment>
Result count: <computed from current cards>
```

This is not a hand-maintained result table: after a card changes, rerunning the command recomputes the result set and field values from the card text. For close reading, enter through the [C4 embodied-intelligence chain](chains/40-embodied-intelligence.md), then open the bilingual card links returned by the script.

## Boundary

The tool covers registration, filtering, and bilingual-card discovery. It does not judge forecast quality or interpret `ACTIVE` as “historically validated.” Historical evidence, falsifiers, dependencies, and reasons for status changes remain authoritative in the [Judgment Ledger](90-ledger.md) and the card bodies.
