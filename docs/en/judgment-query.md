# Judgment-card query tool

[中文版](../zh/judgment-query.md)

The repository currently registers 123 judgment cards, not a second static index. The bilingual cards under `docs/zh/ledger/` and `docs/en/ledger/` are the only inputs. On every invocation, the reproducible query tool parses both projections, discovers the contiguous `J-001`–`J-NNN` range from the card headings (currently ending at `J-123`), requires the two languages to expose the same ID set, checks that normalized chains, status, confidence, and time-window endpoints agree, and applies filters to that shared set. A missing card, ID gap, or bilingual metadata drift is an explicit structural error (exit code 2), not an incomplete result. This prevents a third maintained index from drifting away from the cards.

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

At least one filter is required. With no filter, the command fails explicitly instead of silently dumping the whole ledger. Unknown statuses, confidence values, or formats are rejected by the CLI. A syntactically valid chain/status combination whose chain is not registered prints `No judgments matched the query.` and exits 0, preserving an empty result rather than falling back to the full register.

The default table output includes normalized `status`, `confidence`, and time window, both one-sentence judgments, and a card link for each language. `--format json` additionally preserves each language's title, raw status, raw confidence, judgment, time window, and link for downstream tooling.

## Negative cases and failure boundaries

Maintainers can run `python3 scripts/test_find_judgments.py` for the query tool's negative suite: deleting a card from one language reports a bilingual ID mismatch; changing the other language's `status`, `confidence`, or `time-window` reports metadata drift; and an unsupported status fails explicitly. Direct calls also reject unknown field values and unfiltered queries without printing the full register.


Command:

```bash
python3 scripts/find-judgments.py --chain C4 --status ACTIVE
```

Against the current repository contents, the result set must contain these 10 IDs (the script's `Result count` must be `10`):

| ID | Status | Confidence | Time window (Chinese card's raw value) |
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

This is not a hand-maintained result table: after a card changes, rerunning the command recomputes the result set and field values from the card text. For close reading, enter through the [C4 embodied-intelligence chain](chains/40-embodied-intelligence.md), then open the bilingual card links returned by the script.

## Boundary

The tool covers registration, filtering, and bilingual-card discovery. It does not judge forecast quality or interpret `ACTIVE` as “historically validated.” Historical evidence, falsifiers, dependencies, and reasons for status changes remain authoritative in the [Judgment Ledger](90-ledger.md) and the card bodies.
