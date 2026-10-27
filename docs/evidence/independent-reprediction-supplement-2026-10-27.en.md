# Supplemental gate-screening record for J-103–J-107 (2026-10-27)

[中文版本](./independent-reprediction-supplement-2026-10-27.md)

> **Evidence boundary**: this page preserves the five-gate fresh-context outputs, but the recognition probes classify R2=3/5. Under §7 of the Historical Validation Protocol, this batch is downgraded to protocol-debugging/calibration material. It **must not** be called completed independent re-review, pseudo-out-of-sample evidence, forecast accuracy, or `GENUINE_FUTURE_OOS`. It supplies each uncovered card with a checkable screening record, missing evidence, and an explicit exclusion reason.

## 1. Frozen input and scope

This batch covers exactly the five cards named by the status-page gap: J-103–J-107. The other 118 cards in the current set of 123 are explicitly excluded; they are not silently treated as reviewed and are not covered by these results. The de-labeled input, mapping, raw outputs, and hashes are in [`blind-review/supplement-2026-10-27/`](blind-review/supplement-2026-10-27/):

- `manifest.json`: source commit `30876ab9cbbdff898d82697e392f06042542d9a0`, candidate total 123, included 5, explicitly excluded 118;
- `bundle.json`: only the five de-labeled bilingual records R-01–R-05;
- `mapping.json`: `R-02 → J-103`, `R-05 → J-104`, `R-04 → J-105`, `R-03 → J-106`, `R-01 → J-107`;
- `raw-results-v2.json` / `results.json`: complete JSON returned by the five fresh-context read-only gate judges, including pre-verdict probes, gate results, and missing evidence;
- `SHA256SUMS`: hashes for the JSON artifacts; batch time anchor `2026-10-27T05:42:40Z`. The subagent tool does not expose a model/version identifier, so this batch makes no model-comparison or accuracy claim.

Each judge received exactly one R record plus the five gate definitions, was instructed not to read the repository or coordinate, and submitted an identity/outcome/confidence probe before judging. Probe classification is `R0=0`, `R1=2`, `R2=3`; R2 over half is the direct reason for downgrading the batch.

## 2. Result overview (protocol-debugging accounting)

| Judgment | Record | G1 | G2 | G3 | G4 | G5 | Raw overall | Protocol status | Main exclusion / gap |
|---|---|---|---|---|---|---|---|---|---|
| J-103 | R-02 | PASS | PASS | PASS | PASS | ABSTAIN | `ABSTAIN` | Retained as debugging output; not independent re-review | Per-use net burden and enforceable actor are incomplete; R2 high-confidence S guess |
| J-104 | R-05 | **VETO** | PASS | PASS | **VETO** | ABSTAIN | `VETO` | Retained as debugging output; not independent re-review | Gates 1 and 4 veto; R2 high-confidence D guess |
| J-105 | R-04 | ABSTAIN | ABSTAIN | ABSTAIN | ABSTAIN | ABSTAIN | `ABSTAIN` | Retained as debugging output; not independent re-review | Five-gate mapping for institutional action and net burden is missing; R1 |
| J-106 | R-03 | ABSTAIN | PASS | ABSTAIN | ABSTAIN | ABSTAIN | `ABSTAIN` | Retained as debugging output; not independent re-review | Budget-action definition, scale, carrying conditions, and persistence burden are missing; R1 |
| J-107 | R-01 | PASS | ABSTAIN | ABSTAIN | ABSTAIN | ABSTAIN | `ABSTAIN` | Retained as debugging output; not independent re-review | Replacement action, carrying conditions, decision closure, and net burden are missing; R2 high-confidence D guess |

`VETO` remains only a necessary-condition screen, not a factual refutation of the forward claim; `ABSTAIN` means evidence is missing. Because R2 exceeds half, these five outputs cannot be published as protocol-level independent re-review results.

## 3. Per-card record and explicit exclusion

### J-103 · The society-scale AI action is asking, not deciding

The raw `R-02` output is `ABSTAIN`: Gates 1–4 pass and Gate 5 abstains because the record does not compare per-use added bodily/social/learning/monetary costs with saved costs or identify an enforceable actor. The pre-verdict probe made a high-confidence `S` guess, so this output cannot be called independent re-review. The missing per-use burden, enforcement mechanism, and independent weekly-user audit are retained as the card's exclusion reason for this batch.

### J-104 · Paid work from home stops at the D tier

The raw `R-05` output is `VETO`: Gate 1 vetoes at about 48 million, or about 66 million with the estimated EU addition, below the hundred-million threshold; Gate 4 vetoes because the worker cannot unilaterally enforce working from home and employer consent is required; Gate 5 abstains. The pre-verdict probe made a high-confidence `D` guess, so this cannot be called independent re-review. The ten-employer sample, future plateau, and per-use net-burden evidence remain missing.

### J-105 · Current recipients' nominal pensions are hardest to cut

The raw `R-04` output is `ABSTAIN`: all five gates abstain because the record does not map an institutional legislative/budget action to a countable action, frequency, replacement action, carrying structure, or per-use net burden. The pre-verdict probe is R1 (identity guess with medium confidence and unknown outcome), so this is still not completed independent re-review. The explicit exclusion reason is that the five-gate mapping for institutional action remains open; missing evidence is not rewritten as a pass or veto.

### J-106 · Aid gives way to defence

The raw `R-03` output is `ABSTAIN`: Gate 2 passes because the replaced ODA budget action is identifiable, while the other gates abstain because the budget action's unit, scale, carrying conditions, coordination closure, and net burden are not evidenced. The pre-verdict probe is R1; this batch cannot be called independent re-review. Project-level substitution, recipient-side net resources, and a common budget denominator remain explicit exclusion reasons.

### J-107 · Paid weekly work at 65+ stops at the D tier

The raw `R-01` output is `ABSTAIN`: Gate 1 passes, while Gates 2–5 abstain because the record lacks a specific replacement action, dedicated carrying conditions, unilateral/local decision closure, and per-use net burden. The pre-verdict probe made a high-confidence `D` guess, so this cannot be called independent re-review. Family-worker subtraction, China/EU coverage, causal evidence for pension-age effects, and sustained net burden remain explicit gaps.

## 4. Boundary of completion

This page completes the following record: each of the five uncovered cards is connected to frozen de-labeled input, a mapping, raw fresh-context output, recognition probes, hashes, and a card-specific exclusion reason; the R2>50% batch is explicitly downgraded to protocol debugging/calibration. It does not claim completed independent re-review, expand the frozen scope, silently mark the other 118 cards reviewed, or write any result as forecast accuracy or genuine future out-of-sample evidence. To bring these five cards into a protocol-level independent re-review, a new, never-before-revealed input batch must be frozen and run under the protocol.
