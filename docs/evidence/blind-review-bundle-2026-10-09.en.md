# Blind-review bundle preparation evidence: 2026-10-09

## Claim boundary

The delivered state is **`BUNDLE_PREPARED`**, not a re-review result. This record proves that frozen inputs were transformed into de-labelled, renumbered, shuffled material; **there is still no verifiable evidence that the re-review has started**. No independent reviewer raw output or run timestamp exists, so this must not be described as a re-review that started, ran, or finished, and it must not be upgraded into evidence of method validity, prediction accuracy, or a historical holdout.

The de-labelled material is only isolated from a reviewer who cannot access this repository; it is not cryptographic isolation. Retained fields remain the judgment prose. Anyone holding both the bundle and the public repository may still restore the pairing by content comparison. Therefore `bundle.json`, the original seed, and the `R-NN -> J-NNN` mapping are not committed; this evidence records only seed, input, and output hashes.

## This round: per-language and index consistency checks, and the defect they found

The previous round's generator (commit `66db88f`) serialized the Chinese and English records into **one merged string** for its leakage scan. Independent verification found that the acceptance requirement — run the semantic, path, index and mapping-reachability checks separately for Chinese and English — had not been implemented. This round adds six independent branches, each of which names the language and the `R-NN` it refuses on:

| Branch | What it judges | Why the merged scan cannot |
|---|---|---|
| `lang_semantic` | One language projection's retained-field whitelist, and whether each required field still carries readable content | The merged scan looks for forbidden text that is PRESENT; it is blind to a field that is **emptied or absent** |
| `lang_path` | Heading anchors and bare file names surviving in one language projection | `LINK_RE` needs brackets, `URL_RE` needs a scheme, `PATH_RE` needs a directory prefix; `#anchor` and `02.md` match none of the three |
| `lang_count` | One language's record count against the frozen manifest | The old `zh_count` / `en_count` were incremented together in one loop, so they were identically equal and could never judge false |
| `index_order` | Identifiers must read `R-01 … R-NN` with no gap, and that sequence must equal the order recomputed from the seed-keyed content digests | This is a property of the sequence, belonging to no single record |
| `cross_language` | The Chinese and English logical card sets are the same, and each record carries the same field meanings in both | Same reason; after merging you cannot see which side is missing a field |
| `mapping_reachability` | Every `R-NN` must resolve to exactly one source card and vice versa | When two records share a body the mapping can still be written but is unusable, and nothing leaks for a scan to find |

**These checks immediately judged the material the previous round actually shipped to be false.** Recomputed over the 102 cards on the tree at the frozen commit `0eb7474`: **28 cards lost their one-sentence judgment field entirely during de-labelling** — **15 failing in Chinese only, 0 in English only, and 13 in both**. The root cause is that these cards reuse the one-sentence judgment as the `### J-NNN · <title>` heading title, and de-labelling removed every title indiscriminately, so the claim prose went with it. The merged scan is structurally blind to this: an empty field leaks no clue.

This was verified to be a **pre-existing defect, not one introduced this round**: recomputing on the same tree with the original `redact_traceback_clues` from commit `66db88f` (without this round's anchor / bare-filename stripping) yields exactly the same 41 emptied fields across 28 cards. The bundle published last round (`a2fdc9db…`) therefore did contain 28 records with no claim in them, and no check at the time would have reported it.

> ⚠ **The "exclude them explicitly" resolution below is superseded and kept only as a record.** It contradicts this project's own acceptance bar — "the bundle retains only the original claim" and "every existing judgment receives a conclusion": those 28 cards do carry a one-sentence judgment, it was merely identical to the card title and deleted along with it, and excluding a card that carries a claim means it can never receive a conclusion. For the current resolution see [the final section, "Round 2"](#round-2--fixing-the-de-labelling-defect-instead-supersedes-the-exclusion-above).

~~The resolution is to exclude them explicitly under the **same inclusion rule**, not to relax the check: the rule was always "both language cards carry the six required retained fields", and this round only evaluates it **after** de-labelling — keeping a card with no claim is worse than excluding it. The selection logic lives in `scripts/blind_manifest.py`, deliberately outside the generator.~~

## Frozen input

- freezer: `scripts/blind_manifest.py` (selection logic lives here; the generator only turns a frozen input into a bundle)
- manifest: `docs/evidence/blind-review/manifest-2026-10-09.json`
- `source_commit`: `b0e025a40037058ee7c56678705cb48b447db64c`
- inclusion rule: every current Chinese and English ledger card with all six required retained fields — `judgment`, `audience`, `reasoning_chain`, `time_window`, `falsifier`, `leading_indicator` — **and still carrying readable content in each of them after de-labelling**.
- coverage: 197 candidates; 74 included; 123 excluded = 95 migration snapshots + 28 cards whose claim does not survive de-labelling.
- manifest SHA-256: `404acac527338ca8ef11b3d3a775c22af9fe78d6a26ff40632f5e3220f723107`

```sh
# Freeze command actually run
python3 scripts/blind_manifest.py --repo . \
  --out docs/evidence/blind-review/manifest-2026-10-09.json
# exit code: 0
# source_commit=b0e025a40037058ee7c56678705cb48b447db64c
# candidate=197 included=74 excluded=123
```

## Run log

The production run used temporary directories outside the repository. The seed was generated with `secrets.token_hex(32)`; its plaintext is not recorded, only its hash `080c2d1cc05dfd1b4f6e333d97647465fba3b4418ebf7016e97ba7c2a0cfc48f`.

```sh
# Command actually run (the seed plaintext existed only in the local shell variable)
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

Production result:

- status: `BUNDLE_PREPARED`
- bundle SHA-256: `7bfc5ffcdf9cdf37a81c0d7024017c58010c453c66c340e655b2a210d3418b3d`
- records: 74; Chinese 74; English 74
- per-language checks: `semantic_fields` / `path_and_anchor` / `count_against_manifest` all `passed` for Chinese and for English separately (recorded per language under `per_language_checks` in the evidence JSON).
- structural checks: `index_order`, `cross_language_card_set_and_field_meanings`, `mapping_reachability`, `merged_leakage_scan` all `passed`.
- two independent temporary directories: byte-identical; both hashes equal the bundle hash above.
- reversed manifest order: byte-identical output.
- ordinary checkout and `git archive HEAD`: `archive_same_bytes=true`.
- different seed: `seed_changes_assignment=true`.
- mapping: written only outside the repository; the bundle contains no mapping, and the generator never reads one.

## Self-test and boundary attack

`python3 scripts/blind_bundle.py --self-test` exited 0 with `SELF_TEST_PASSED`: a four-card fixture, **18 negative cases and 18 mutation cases** (previous round: 9 and 9).

The nine existing merged-scan negatives all regress green: legacy identifier, status word, revised reason, diffusion gate, source path, original title, dependency marker, confusable legacy identifier, and a legacy identifier split across lines. Each exits non-zero naming an `R-NN`, and disabling its own branch lets exactly that defect through.

Nine negatives are new. Each is first confirmed to be reported **by its own branch**, then re-run with only that branch disabled to confirm the defect survives — so none of them relies on the pre-existing merged scan to report indirectly:

| Negative case | Branch | Actual refusal (excerpt) |
|---|---|---|
| `zh_required_field_emptied` | `lang_semantic` | `R-02 (zh): required field 'falsifier' carries no readable content after de-labelling` |
| `en_required_field_emptied` | `lang_semantic` | `R-01 (en): required field 'falsifier' carries no readable content after de-labelling` |
| `zh_bare_heading_anchor` | `lang_path` | `R-02 (zh): field 'leading_indicator' keeps a heading anchor … #锚点二` |
| `en_bare_source_filename` | `lang_path` | `R-02 (en): field 'leading_indicator' keeps a bare source file name: 02.md` |
| `en_field_meaning_dropped` | `cross_language` | `R-02: … (zh-only: ['opposing_mechanism']; en-only: -)` |
| `duplicate_record_body` | `mapping_reachability` | `R-01 = R-02 share one record body, so neither resolves to a single source card` |
| `index_order_permuted` | `index_order` | `index/order inconsistency at position 1: R-01 sits where R-02 belongs …` |
| `language_count_short` | `lang_count` | `zh projection carries 3 records but the frozen manifest pins 4 cards` |
| `card_set_unpaired` | `cross_language` | `the zh and en logical card sets differ: 1 card(s) only in zh, 0 only in en` |

The first two are the direct evidence of **failing in one language only**: the self-test asserts that the Chinese failure message must contain `(zh)` and must not contain `(en)`, and the English one the reverse. If the two languages were still judged as one merged string, that pair of assertions could not both hold.

The last three (`index_order_permuted`, `language_count_short`, `card_set_unpaired`) are triggered through a test-only injection point, because **no valid frozen manifest can produce these defects** — they are generator-internal invariants, and injection is the only way to show those guards have teeth. The injection point is not exposed on the CLI.

Also verified: `refused_run_exit_code=1` (the refusal path and the process exit code are the same thing), `mapping_pairs_match_bundle=true`, the manifest hash guard, refusal to write the mapping inside the repository, `archive_same_bytes=true`, and `seed_changes_assignment=true`.

These are structural and isolation checks only. They do not prove that the historical rules work, that predictions are accurate, that the re-review has started, or that the bundle is cryptographically irreversible for someone who has both the bundle and the repository.

## Check record

- `npm run check`: exit code 0; output was `all automated pre-publication checks pass`. This is mechanical structure evidence only, not evidence of method validity or prediction accuracy.
- `git diff --check`: exit code 0, no output.
- committed in this unit: the generator, the freezer, the re-frozen manifest, the hash evidence, the bilingual protocol, and this evidence package; the bundle, seed, and mapping never enter the repository.

## Round 2 — fixing the de-labelling defect instead (supersedes the exclusion above)

The "exclude the 28 cards explicitly" resolution above is superseded. The reason is not taste: it violates this project's own acceptance clauses. "The bundle retains only the original claim" requires the claim to survive, and "every existing judgment receives a retain / REVISED / FALSIFIED / explicit-downgrade conclusion" requires every card to get a conclusion — excluding a card that does carry a judgment satisfies neither.

**A first-hand diagnosis replaced the guess with a fact.** Running a per-card, per-field diagnosis on the real ledger with the repository's own `blind_bundle` and `blind_manifest` modules — that is, with the blanket title deletion described above — the cause of death across the 28 excluded cards is `Counter({'judgment': 41})`: **all 41 failing (card, language) instances, and only those, land on the `judgment` field**. None of the other five required fields (audience, reasoning chain, time window, falsifier, leading indicator) was damaged at all. So this was never "these cards have incomplete fields"; it was "de-labelling deleted titles too broadly".

**The exemption is narrow and symmetric.** Only a card's **own** title, and only inside that card's **own** `judgment` field, may survive. Another card's title appearing in any field, or this card's title appearing in any other field, is still rejected — that remains a reverse-lookup key. The cost is stated rather than hidden: the claim prose can now be reverse-looked-up by anyone holding both the bundle and the public repository, but that is the same order of exposure as the reasoning chain, time window and falsifier, which already appear in the bundle verbatim. The isolation was always procedural (the reviewer is barred from the repository by role), never cryptographic.

**The exemption is load-bearing, and three fixtures hold it there** (all inside `--self-test`):

| Fixture | Kind | What it proves |
|---|---|---|
| a card whose claim == its own title must be included | positive regression | both languages keep it verbatim and `blank_claim_fields: 0`; if the exemption breaks, this fails immediately |
| `foreign_title_in_claim` | structural injection (negative) | another card's title injected into `judgment` must be rejected by the `title` branch, and must pass when only that branch is disabled — proving no other branch catches it indirectly |
| `drop_claim_exemption` | TEST_FAULT (withdraw the exemption) | with the exemption withdrawn the claim is emptied again, and only `lang_semantic` reports it — proving the exemption is why those 41 fields survive |

`python3 scripts/blind_bundle.py --self-test` currently reports `SELF_TEST_PASSED`, `negative_cases=20`, `mutation_cases=20`, `regression_cases=1`, `refused_run_exit_code=1`, `mapping_pairs_match_bundle=true`.

### The re-frozen input and bundle

```sh
# freeze (verbatim)
python3 scripts/blind_manifest.py --repo . \
  --out docs/evidence/blind-review/manifest-2026-10-09b.json
# candidate=197 included=102 excluded=95

# production run (bundle / mapping / seed all in a temp dir outside the repository)
python3 scripts/blind_bundle.py --repo . \
  --manifest docs/evidence/blind-review/manifest-2026-10-09b.json \
  --output-dir "$tmpdir/bundle" --mapping-out "$tmpdir/mapping.json" \
  --seed "$seed" --verify-determinism \
  --evidence docs/evidence/blind-review/bundle-prepared-2026-10-09b.json
```

- `source_commit`: `98fd95701da3bacef4d43e304db6b82e3f4d3b9b`
- manifest SHA-256: `181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1`
- coverage: 197 candidates; **102** included; **95** excluded (historical migration snapshots only; the `claim_lost` bucket is now empty)
- bundle SHA-256: `e15b0e36d427432aeddb436f6fe205f53af691c04c0a58083b51647e34f43360`; 102 records (102 zh / 102 en); **zero empty judgment fields in either language**
- seed SHA-256: `a18ea18e3a88ffd865b44d3ca93555a7ac60f91f2e8cc3a4e22df6f5b2c775e0` (the seed itself never enters the repository)
- determinism: `same_bytes=true`, `order_independent=true`, `archive_same_bytes=true`, `seed_changes_assignment=true`
- per-language checks: `semantic_fields` / `path_and_anchor` / `count_against_manifest` all `passed` for zh and for en
- structural checks: `index_order`, `cross_language_card_set_and_field_meanings`, `mapping_reachability`, `merged_leakage_scan` all `passed`

**No earlier evidence was overwritten** [**corrected 2026-10-10: not true of round 1's originals** — the paths `manifest-2026-10-09.json` and `bundle-prepared-2026-10-09.json` were both overwritten in place by the 74-record version during the first remediation after round 1 (`da4ef29`), so what this sentence calls preserved is that 74-record version, not round 1's originals. The originals were restored from commit `66db88f` as [`manifest-2026-10-09a.json`](blind-review/manifest-2026-10-09a.json) (`7c06add3…`) and [`bundle-prepared-2026-10-09a.json`](blind-review/bundle-prepared-2026-10-09a.json); the latter records bundle hash `a2fdc9db…`, which differs from the bundle actually dispatched in round 1 (`5d4e4732…`), and the source of that difference has not been established. Round 2's `-b` files are unaffected]: `manifest-2026-10-09.json` (74 included) and `bundle-prepared-2026-10-09.json` are preserved as they were, and round 2 uses new `-b` filenames. That means the repository now holds three frozen inputs (`7c06add3…` at 102, `404acac5…` at 74, `181b35ec…` at 102); a reader must keep them apart by the round context given here and **must not mix their counts**.

### What this section does not prove

It does not prove that predictions are accurate, that the method works, or that the isolation is cryptographic. It proves one thing: de-labelling no longer eats the claim, and that property is held by a test which fails when the exemption is withdrawn. The re-judgment of the 28 cards on this bundle is in [section 11 of the isolated blind re-review](blind-review-reaudit-2026-10-09.en.md#11-round-2--the-28-cards-re-judged-on-the-repaired-bundle).
