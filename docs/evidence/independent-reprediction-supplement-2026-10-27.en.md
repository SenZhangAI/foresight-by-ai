# Supplemental independent re-review for J-103–J-107 (2026-10-27)

[中文版本](./independent-reprediction-supplement-2026-10-27.md)

> **Evidence boundary**: this page records an independent necessary-condition screen using the five diffusion gates. It is not forecast accuracy and is not `GENUINE_FUTURE_OOS` (genuine future out-of-sample) evidence. Future judgments remain subject to each card's own time window, falsifiers, leading indicators, and next-review date.

## 1. Frozen input and scope

This round covers only J-103–J-107, the five cards named by the status-page gap. The other 118 cards in the current set of 123 are explicitly excluded from this supplement; they are not silently treated as reviewed and are not covered by these results. The de-labeled input, mapping, hashes, and per-record results are in [`blind-review/supplement-2026-10-27/`](blind-review/supplement-2026-10-27/):

- `manifest.json`: source commit `30876ab9cbbdff898d82697e392f06042542d9a0`, frozen candidate total 123, included 5, excluded 118;
- `bundle.json`: only the five de-labeled bilingual records R-01–R-05;
- `mapping.json`: `R-02 → J-103`, `R-05 → J-104`, `R-04 → J-105`, `R-03 → J-106`, `R-01 → J-107`;
- `results.json`: gate-by-gate results, missing evidence, and boundary statement; `SHA256SUMS`: file hashes.

Five fresh-context, read-only gate judges each received exactly one R record and were instructed not to read the repository or coordinate. The `recognized` field is preserved as returned: it indicates whether the judge recognised an existing judgment from the de-labeled text; it does not expose the J identifier and is not treated as sufficient proof of independence.

## 2. Result overview

| Judgment | De-labeled record | G1 | G2 | G3 | G4 | G5 | Overall | Key gap |
|---|---|---|---|---|---|---|---|---|
| J-103 | R-02 | PASS | PASS | PASS | PASS | PASS | `PASS` | Provider self-report is unaudited; delegated-payment weekly count and the 30-request sample were not supplied |
| J-104 | R-05 | **VETO** | PASS | PASS | PASS | PASS | `VETO` | Future plateau, ten-employer sample, and EU denominator remain unobserved |
| J-105 | R-04 | **VETO** | PASS | PASS | ABSTAIN | `VETO` | `VETO` | No verified personal-action denominator for an institutional judgment; persistence through 2034 is unobserved |
| J-106 | R-03 | **VETO** | ABSTAIN | PASS | PASS | ABSTAIN | `VETO` | Affected population, project substitution rate, and recipient-side net-resource change are unverified |
| J-107 | R-01 | **VETO** | ABSTAIN | PASS | PASS | ABSTAIN | `VETO` | Family-worker subtraction, coverage, and separation of ageing from fiscal pressure remain unresolved |

`VETO` is the result of a necessary-condition screen, not a falsification of the future judgment; `ABSTAIN` means evidence is missing and must not be rewritten as PASS.

## 3. Per-card record

### J-103 · The society-scale AI action is asking, not deciding

Independent re-review: `R-02`; overall `PASS`. The judge preserved the boundary between asking or handing off a low-consequence task and delegated ordering/payment. The former passes the scale gate on the single-service self-report above 900 million weekly users; its incumbents are search, asking another person, and requesting writing help; existing phones/browsers and the free tier provide carrying capacity; the user can initiate it unilaterally. Delegated payment still lacks a public de-duplicated weekly count. Gaps include the unaudited provider report, whether the free tier persists, and the card's 30-real-request sample, which was not in the frozen input.

This means only that the gate screen found no necessary-condition veto. It does not change the card's medium confidence or prove its 2029 forward claim.

### J-104 · Paid work from home stops at the D tier

Independent re-review: `R-05`; overall `VETO`. Gate 1 vetoes the frozen measure at about 48 million (about 66 million with the estimated EU addition), below 100 million. Gates 2–5 retain the replacement of commuting/office work, existing broadband/devices, employer decision rights, and observed repeat use. The future 19%–25% plateau, ten-employer sample, EU employment base, and disability-related scale remain unobserved.

This corroborates the card's existing D-tier scale screen but is not forecast-accuracy evidence.

### J-105 · Current recipients' nominal pensions are hardest to cut

Independent re-review: `R-04`; overall `VETO`. The judge recognised this as an institutional judgment rather than a weekly personal action: Gate 1 vetoes because there is no verified personal-action denominator; alternative budget routes, fiscal carrying conditions, and decision-makers are supported in the record; Gate 5 abstains on persistence through 2034. The result does not turn “not applicable” into a forecast confirmation or treat future OASI handling as observed.

### J-106 · Aid gives way to defence

Independent re-review: `R-03`; overall `VETO`. Gate 1 vetoes because the affected head count is explicitly unverified and the direct actors are four governments and parliaments. Alternative funding, budget carrying conditions, and decision-makers are supported; project-level substitution and sustained recipient-side net-resource change are insufficient, so Gates 2 and 5 abstain. ODA reclassification risk must remain separate from a real aid cut.

### J-107 · Paid weekly work at 65+ stops at the D tier

Independent re-review: `R-01`; overall `VETO`. Gate 1 vetoes the frozen qualifying total of about 10.29–51.64 million as tens-of-millions scale; Gates 2 and 5 abstain because the record does not cleanly separate the replacement/fiscal-pressure mechanism or establish sustained net burden; Gates 3 and 4 have record-level support. Family-worker subtraction, China/EU coverage, and causal separation of ageing from fiscal pressure remain gaps.

## 4. Boundary of completion

This page connects each of the five uncovered cards named by the status page to a checkable de-labeled input, mapping, and independent re-review result or missing-evidence record. It does not expand the frozen scope, silently mark the other 118 cards as reviewed, or interpret any `PASS`/`VETO` as forecast accuracy or genuine future out-of-sample evidence.
