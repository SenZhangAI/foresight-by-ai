# Blind-review bundle preparation evidence: 2026-10-09

## Claim boundary

The delivered state is **`BUNDLE_PREPARED`**, not a re-review result. This record proves that frozen inputs were transformed into de-labelled, renumbered, shuffled material; **there is still no verifiable evidence that the re-review has started**. No independent reviewer raw output or run timestamp exists, so this must not be described as a re-review that started, ran, or finished, and it must not be upgraded into evidence of method validity, prediction accuracy, or a historical holdout.

The de-labelled material is only isolated from a reviewer who cannot access this repository; it is not cryptographic isolation. Retained fields remain the judgment prose. Anyone holding both the bundle and the public repository may still restore the pairing by content comparison. Therefore `bundle.json`, the original seed, and the `R-NN -> J-NNN` mapping are not committed; this evidence records only seed, input, and output hashes.

## Frozen input

- manifest: `docs/evidence/blind-review/manifest-2026-10-09.json`
- `source_commit`: `0eb7474ef19533d9db40ba966e0ccf788ea05adb`
- inclusion rule: every current Chinese and English ledger card with all six required retained fields: `judgment`, `audience`, `reasoning_chain`, `time_window`, `falsifier`, and `leading_indicator`.
- coverage: 197 candidates; 102 included; 95 excluded. The exclusions are migration snapshots in `docs/evidence/legacy-ledger-migration.md`; they duplicate current judgments and are not a second judgment set.
- manifest SHA-256: `7c06add34bb30f022b5ad9dc25b915cb53d6bc77d7627f7d9d8dde40caa881ee`

## Run log

The production run used temporary directories outside the repository. The seed was generated with `secrets.token_hex(32)`; its plaintext is not recorded, only its hash `8092bf51618ff9b95a7d51dfb9b0c7a63e7ee0a285c091f1ec1f099d51ad3d0d`.

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
- bundle SHA-256: `a2fdc9db7f46cf6236568c12a0038e994f0e9d7315f451a35fed0c635a47cda1`
- records: 102; Chinese 102; English 102
- two independent temporary directories: byte-identical; both hashes equal the bundle hash above.
- reversed manifest order: byte-identical output.
- ordinary checkout and `git archive HEAD`: `archive_same_bytes=true`.
- different seed: the fixture self-test demonstrates that ordering can change; the production bundle records only this run's seed hash.
- mapping: written only outside the repository; the bundle contains no mapping, and the generator never reads one.

## Self-test and boundary attack

`python3 scripts/blind_bundle.py --self-test` exited 0 with `SELF_TEST_PASSED`: a four-card fixture, nine single-defect negative cases, and nine mutation cases. Every negative case exited non-zero and named an `R-NN`; this run included `R-04` for a legacy identifier, `R-01` for a status word, and `R-03` for a revised reason / diffusion gate / confusable legacy identifier. The nine mutations disable, one at a time, the identifier, status, metadata, gate, path, title, dependency, and related detection branches; the corresponding defect then passes exactly as expected. The self-test also checks `mapping_pairs_match_bundle=true`, the manifest hash guard, in-repository mapping refusal, `archive_same_bytes=true`, and `seed_changes_assignment=true`.

These are structural and isolation checks only. They do not prove that the historical rules work, that predictions are accurate, that the re-review has started, or that the bundle is cryptographically irreversible for someone who has both the bundle and the repository.

## Check record

- `npm run check`: exit code 0; `files checked: 95`, `internal links: 2960`, judgment cards `zh 102 / en 102`, and 11 registered chains; output was `all automated pre-publication checks pass`. This is mechanical structure evidence only, not evidence of method validity or prediction accuracy.
- `git diff --check`: exit code 0, no output.
- pre-commit working tree: `git status --short` listed this evidence package, the generator, the manifest, and the bilingual protocol (plus the JSON under `docs/evidence/blind-review/`); the bundle, seed, and mapping were outside the repository. Confirm a clean working tree after commit.
