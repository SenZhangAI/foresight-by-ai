# Isolated blind re-review (2026-10-09)

[中文版](blind-review-reaudit-2026-10-09.md)

> **What this file proves, and what it does not.** It proves that 102 registered judgment cards were de-labelled, renumbered and shuffled, then re-judged card by card against the current five diffusion gates by six mutually invisible fresh-context batches, with the results fixed and hashed *before* the mapping was unsealed; and that every judgment therefore carries a recorded disposition. It does **not** prove those judgments are accurate, and it does **not** prove this project's method works. A same-model, same-criteria re-judgment can only test **reproducibility**: agreement with the old conclusion is not independent evidence of correctness, and disagreement does not automatically mean the old conclusion was wrong. Genuine out-of-sample calibration comes only from future judgment cards reaching their due date.

---

## 1. The question this round answers

The quality order asked for was: first calibrate the method against history, then re-analyse the documents in full, avoiding contamination by what the earlier documents already say. The first half landed in [Retrospect](../en/01-retrospect.md) and the [historical validation protocol](../en/02-historical-validation-protocol.md); this round does the second half, and treats "avoid contamination by the earlier documents" as something that must be **materialised**, not as an instruction handed to the executor.

A previous attempt already proved that swapping the instance is not isolation: the diffusion-gate review, the `REVISED` reason, the card identifier and the README summary all leak the old answer on the ledger's very first screen. So isolation here is a de-labelled, renumbered, seed-shuffled bundle; the re-reviewer sees no repository, no card identifier and no pre-existing review conclusion.

This round does **not** answer whether these judgments will come true, what the accuracy rate is, or whether the method has been validated.

## 2. Input baseline and isolation evidence

| Item | Value |
| --- | --- |
| Frozen source commit | `0eb7474ef19533d9db40ba966e0ccf788ea05adb` |
| Input manifest | `docs/evidence/blind-review/manifest-2026-10-09.json`, SHA-256 `7c06add34bb30f022b5ad9dc25b915cb53d6bc77d7627f7d9d8dde40caa881ee` |
| Inclusion rule | Every registered card whose Chinese and English versions both carry all six required retained fields (judgment, audience, reasoning chain, time window, falsifier, leading indicator) |
| Coverage | 197 candidates → 102 included → 95 excluded |
| Exclusion reason | The 95 excluded entries are the historical migration snapshots in `docs/evidence/legacy-ledger-migration.en.md`; they duplicate the current cards and are not a second judgment set |
| Output bundle | SHA-256 `5d4e4732a07f80eaceed12e39299b7a77152cd700fede1adc82215a645bfa14e`, 102 records in each language |
| Determinism | Two independent runs on the same seed are byte-identical; a plain checkout and `git archive HEAD` agree; a different seed changes the identifier assignment |
| Generator | `scripts/blind_bundle.py`; `--self-test` exits 0, and nine negative fixtures — each injecting exactly one defect — all exit non-zero and name the specific `R-NN` (card status word, revision reason, diffusion gate, original file path, real legacy title, dependency identifier, and confusable / line-split legacy identifiers) |
| Mapping seal | The `R-NN → J-NNN` mapping and the seed live only in a temporary directory outside the repository; the generator does not read it; neither the public commit nor `git archive` can reach it |

The fields retained in the bundle are only: one-sentence judgment, audience scale, reasoning chain, time window, falsifier, leading indicator, lens, strongest opposing mechanism, what can be done now, proposed date. Stripped: card identifier, status, confidence, diffusion-gate review, `REVISED` reason, dependency graph, source links, original file paths and anchors, pre-existing review conclusions, downgrade counts and markers.

**The real boundary of this isolation**: it is **procedural**, not cryptographic. Anyone holding both the bundle and the public repository can still restore the mapping by comparing prose word for word; more importantly, the re-reviewer and the original author are the same model, and de-labelling cannot remove training memory. This round therefore required a self-reported "did you recognise the original judgment" on every record, counted separately by identification stratum (section 4) — that **measures** leakage, it does not **remove** it.

## 3. Execution, and the evidence that results came before unsealing

Six batches each received 17 records (6 × 17 = 102), invisible to one another, none connected to the repository. Each record required: first state whether the original judgment was recognised, then give `PASS` / `VETO` / `ABSTAIN` per gate, then an overall verdict with its rationale and the missing evidence. The verdict vocabulary has only two values, which is the gate set's own discipline ([J-066](../en/ledger/61-70.md#j-066--the-five-gates-are-necessary-not-sufficient): the gates are a veto-style filter, not a sufficiency predictor):

- `VETO` — at least one gate clearly fails;
- `ABSTAIN` — no gate was shown to fail. **This is not a pass**; passing all five only means it qualifies to keep competing.

Each batch reported the SHA-256 of its own raw output on delivery, while the mapping was still sealed. Recomputed after unsealing, all six hashes are unchanged byte for byte:

```
e6d12b513adff3062f9242f117f309ea14a3547bc775369401876fe8095fa099  raw-1.jsonl
cf8a0306037d093f4d57d26d4ebb7224642f90f94021c57459266d9035a6a586  raw-2.jsonl
238481cd95453844fbb3e1669f52da0296c1df4d2b5e2962a8976a2ebd0bd49a  raw-3.jsonl
3855e7d7d474a97009b77d0d0fb546ddd5cc91868d2546e067ef924a749e704c  raw-4.jsonl
0bc49749a1149ce37be88e77d1e67af2a2303dfcd88e05f34d4c75780d418565  raw-5.jsonl
d1f76c7f6f5ed9665d9f13e6a83d6136d979a8747f3ed9f1597300bfbd464fec  raw-6.jsonl
```

The per-record verbatim rationale and missing-evidence note, together with the mapping result, are kept in [`blind-review/reaudit-2026-10-09.json`](blind-review/reaudit-2026-10-09.json). The re-reviewers answered in Chinese and that file preserves their wording as written; both language versions of this report use the same counts and the same disposition vocabulary.

## 4. Results: three sets of counts

**Verdict distribution**: `VETO` 37 / `ABSTAIN` 65.

**State before the re-review** (the side that only becomes readable after unsealing): already `REVISED` 62 / already limited to an occupational or institutional judgment 34 / already marked landscape-only 5 / unlimited 1. In other words, 101 of the 102 cards entered this round with their scope already limited by an earlier diffusion-gate review; exactly one still held a licence for society-level voice.

**Reproducibility**: across those 101 already-limited cards, the blind review reproduced the limit 36 times (35.6%). In the other 65 it established no gate failure at all. By the gates' own discipline those 65 are **not grounds for an upgrade** — a gate can veto, never affirm — but the number is hard: under de-labelled conditions, about two thirds of the existing limits could not be independently rebuilt by the same model. That is the quantified form of the boundary "a same-model re-judgment tests reproducibility only".

**Identification strata** (section 11 of the protocol requires stratified counting): 83 records self-reported recognising the original judgment, 19 did not.

| Identification stratum | Records | `VETO` rate |
| --- | --- | --- |
| Recognised | 83 | 26.5% |
| Not recognised | 19 | 78.9% |

Recognised records were vetoed markedly less often (26.5% vs 78.9%). The protocol's own sentence is "a higher agreement rate among recognised items can only be explained as leakage"; what shows up here is the same phenomenon from the other side — **familiarity breeds leniency**. It cannot be read as "the recognised cards are better"; it can only be read as training memory affecting how strictly the gates get applied. Every count in this round therefore carries the same discount: they measure a reproduction process contaminated by the model's own memory.

**Dispositions** (vocabulary taken from section 11.B of the protocol: retain / revise / falsify / downgrade / archive):

| Disposition | Records |
| --- | --- |
| Retain — the blind review reproduced the existing limit | 36 |
| Retain — no veto found (a gate can only veto, never upgrade) | 65 |
| Downgrade — newly triggered this round | 1 |
| Falsify | 0 |
| Archive | 0 |

**Zero falsifications is a scope result, not an omission**: the re-reviewers in this round only ran the diffusion gates; they did not rule on whether any card's falsifier has been triggered. Checking falsifiers belongs to the due-date review process ([ledger, section 5](../en/90-ledger.md#5-expiry-review-procedure)) and needs citable outcome data rather than gate reasoning. Reading "this round falsified nothing" as "no card is falsified" is wrong.

## 5. The one new downgrade: J-029

[J-029 · Demand-side anchors persist](../en/ledger/21-30.md#j-029--demand-side-anchors-persist) was the only card entering this round still holding a licence for society-level voice (its diffusion-gate review reads "Gate 1 **passes** — may be written as a society-level judgment"). The blind review (`R-65`, original not recognised) returned `VETO`: the scale and frequency of the demand satisfy Gate 1, but this is a demand-side anchor judgment that replaces no existing activity, so Gate 2 vetoes it.

There is an internal inconsistency in the card itself, visible only after unsealing: its audience-scale field already states "this card is a demand-side/method test judgment, not capability diffusion; the classification is not applicable", while simultaneously invoking a Gate 1 pass to license society-level voice. **You cannot both claim the gates do not apply, so as to escape Gate 2, and invoke a Gate 1 pass to buy a society-level licence.**

Disposition: downgrade (a scope downgrade; not one word of the original is deleted and the identifier is not reused). A licence for society-level voice must come from a test valid for the "human-nature constant / demand-side anchor" class of judgment, and this project's method currently has no such test — that is the gap registered in section 8. Until it exists, J-029 is written as an institutional / human-nature-constant judgment, must not be cited in the voice of "the whole of society" or "generally", and must not be used to derive society-level consequences. Its proposition, time window, falsifier and review date are all retained, and it continues to face due-date review on its own.

## 6. The largest single finding: 27 of the 37 vetoes come from one sentence

Of the 37 `VETO` records, **27 fail on Gate 2 alone**, and the rationale is almost always the same sentence: "this card replaces no existing activity". The cards vetoed by that sentence are of wildly different kinds — a human-nature constant (J-029), landscape-only claims (J-042, J-053), the method rules themselves (J-066, J-069, J-070), a negative boundary judgment (J-078), an infrastructure-ordering claim (J-089), gain distribution (J-090, J-102), risk pricing (J-094).

A rule that returns the same veto reason for ten different kinds of claim is not filtering; it is out of bounds. Gate 2's original induction domain can be read straight off its own case table: the cases [Retrospect](../en/01-retrospect.md) used to induce the five gates — smartphones, health codes, QR payment, containerization, China's household responsibility system, against the control group Google Glass, 3D television, MOOCs, Concorde, Iridium, Esperanto, New Coke — are **without exception about whether one capability or product becomes the way a whole society does things**. Not one of them is about how gains are distributed, how risk is priced, whether a human-nature constant holds, or about a forecasting rule itself.

So this round's conclusion is: most of those 27 vetoes are **not a rejection of the predictions but a rejection of how the method was applied**. They changed no card's status (26 of the 27 cards were already limited), but they consistently point at one thing: the diffusion gates were used outside the question they were induced from.

That yields a **candidate rule**, which must **not** be used yet:

> **Candidate rule G2-SCOPE (Gate 2's domain and the mandate exception)** — Gate 2 (it must replace an existing activity) applies only to claims about voluntary capability diffusion. Where adoption is required by a party that can both compel and observe compliance, "replaces no existing activity" is not a veto; the veto power moves to Gate 4 (does such a party actually exist) and Gate 5 (who carries the recurring net burden relative to not adopting). For the four classes of gain distribution, risk pricing, human-nature constants and method rules, Gate 2 does not apply and a separate test is needed.

By this project's own rule ([method](../en/00-method.md): no forecasting rule may be added out of thin air; each new rule needs at least 2 success cases and 2 failure cases, and must be able to return "no" on some real case), G2-SCOPE is only a candidate: its success and failure cases have not had their sources and dates frozen under the as-of discipline of the historical validation protocol, and examples from memory do not count as calibration. Its expected falsification shape has to be written down first: **if a real case can be found where a party that can compel and observe required adoption, the thing genuinely replaced no existing activity, and it still failed to diffuse, with that failure caused precisely by "replacing no existing activity", G2-SCOPE is refuted.** Until calibration is complete it is neither written into the five-gate text nor used to excuse any card from a Gate 2 veto — the downgrade in the previous section was executed under the **current** gate text and did not invoke this candidate.

## 7. Does this constitute a substantive rule change

[Method §1.3](../en/00-method.md) requires a substantive rule change to trigger holdout invalidation and a full re-review; [section 10 of the historical validation protocol](../en/02-historical-validation-protocol.md) requires that if a re-review changes the rules again, the old holdout cannot vouch for the new version and a fresh holdout must be drawn.

This round did **not** change the five-gate text: G2-SCOPE is registered as a candidate only, was not adopted, and was not used to change any verdict. So this round does not trigger holdout invalidation.

But one consequence must be stated plainly: **this round cannot simultaneously serve as "the full re-review under a rule set containing G2-SCOPE"**. What those 27 Gate 2 vetoes would conclude under the new rule was never tested here — a candidate rule only says the old verdict does not apply; it supplies no replacement test. So the disposition of those 27 cards is "retained plus explicitly unresolved", not "re-reviewed and cleared". Once G2-SCOPE completes historical calibration and is adopted, the two provisions above require drawing a fresh holdout and running a full re-review again.

## 8. Open gaps

1. **Four classes of claim have no test**: gain distribution, risk pricing, human-nature constants / demand-side anchors, and forecasting rules themselves have no falsifiable filter at all. J-029's society-level licence was withdrawn precisely because of this hole. Next entry point: build and calibrate a candidate test for at least one of these classes under the protocol's as-of discipline (2 successes + 2 failures + 1 exclusive case + it must be able to say no).
2. **G2-SCOPE is uncalibrated**: see section 6, including its expected falsification shape.
3. **The 27 Gate 2 vetoes have not been re-reviewed under the new rule**: see section 7.
4. **The bundle carries no claim class**: de-labelling also erased the information "this is a method card / a landscape-only card / a negative boundary card", so the re-reviewers ran the capability-diffusion gates on method cards too (J-066, J-069, J-070). That is not the reviewers' error; it is a boundary of the bundle's design. The next round should carry a **neutral claim-class label** (for instance "capability diffusion / distribution / pricing / constant / rule") without leaking the old answer, and prove with negative fixtures first that the label cannot be used to recover the old identifiers.
5. **Reproducibility is only 35.6%**: about two thirds of the existing limits could not be rebuilt by the same model under de-labelled conditions. That number itself needs explaining — either the grounds for the limit are written too thinly (the card does not say why Gate 1 fails), or the gate verdicts are themselves unstable. The two causes call for opposite fixes, and this round cannot tell them apart.
6. **The leniency bias across identification strata is uncorrected**: a 26.5% `VETO` rate for recognised records against 78.9% for unrecognised. This round only measures it, and under a same-model setup there is no way to correct it.
7. **Leakage isolation is procedural**: anyone holding both the bundle and the public repository can restore the mapping, and training memory cannot be removed.

## 9. Forbidden statements

The results of this round must not be written up as any of the following:

- "The blind re-review passed, the judgments are validated" — `ABSTAIN` is not a pass;
- "Only 1 of 102 cards needed a downgrade, so judgment quality is high" — 101 cards entered this round already limited; the denominator had been consumed by the earlier downgrades;
- "The blind review agreed with the old conclusions X% of the time, so the method works" — same-model agreement is not correctness;
- "Zero falsifications, so no judgment was overturned" — this round does not rule on falsifiers;
- "Old-answer leakage has been eliminated" — it was measured, not eliminated.

## 10. Per-card disposition table

The table below carries the disposition of all 102 cards. The verbatim rationale and missing-evidence note for each is in the record with the same `R-NN` in [`blind-review/reaudit-2026-10-09.json`](blind-review/reaudit-2026-10-09.json); the same disposition line is also written into each card in place, immediately above its Status field.

| Card | Blind id | Blind verdict | Gates failed | Recognised the original | State before this round | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| J-001 | R-24 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-002 | R-11 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-003 | R-23 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-004 | R-85 | VETO | Gate 3 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-005 | R-57 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-006 | R-83 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-007 | R-96 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-008 | R-20 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-009 | R-75 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-010 | R-51 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-011 | R-80 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-012 | R-100 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-013 | R-64 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-014 | R-102 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-015 | R-13 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-016 | R-54 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-017 | R-26 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-018 | R-66 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-019 | R-68 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-020 | R-76 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-021 | R-84 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-022 | R-99 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-023 | R-101 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-024 | R-33 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-025 | R-53 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-026 | R-60 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-027 | R-42 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-028 | R-41 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-029 | R-65 | VETO | Gate 2 | no | unlimited (licensed for society-level voice) | downgrade — newly triggered this round |
| J-030 | R-93 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-031 | R-91 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-032 | R-92 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-033 | R-34 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-034 | R-78 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-035 | R-87 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-036 | R-79 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-037 | R-82 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-038 | R-10 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-039 | R-69 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-040 | R-07 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-041 | R-03 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-042 | R-90 | VETO | Gate 2 | no | already marked landscape-only | retain — the blind review reproduced the existing limit |
| J-043 | R-71 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-044 | R-31 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-045 | R-95 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-046 | R-09 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-047 | R-28 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-048 | R-49 | VETO | Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-049 | R-32 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-050 | R-52 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-051 | R-43 | VETO | Gate 1, Gate 2 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-052 | R-73 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-053 | R-15 | VETO | Gate 2 | yes | already marked landscape-only | retain — the blind review reproduced the existing limit |
| J-054 | R-27 | ABSTAIN | — | yes | already marked landscape-only | retain — no veto found (a gate can only veto, never upgrade) |
| J-055 | R-46 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-056 | R-67 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-057 | R-08 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-058 | R-40 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-059 | R-14 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-060 | R-70 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-061 | R-88 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-062 | R-30 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-063 | R-98 | ABSTAIN | — | yes | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-064 | R-01 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-065 | R-17 | VETO | Gate 2 | yes | already REVISED | retain — the blind review reproduced the existing limit |
| J-066 | R-61 | VETO | Gate 1, Gate 2 | no | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-067 | R-19 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-068 | R-12 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-069 | R-02 | VETO | Gate 2 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-070 | R-05 | VETO | Gate 2 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-071 | R-81 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-072 | R-94 | VETO | Gate 1 | no | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-073 | R-38 | VETO | Gate 3 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-074 | R-18 | VETO | Gate 3 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-075 | R-56 | VETO | Gate 1, Gate 5 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-076 | R-45 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-077 | R-62 | VETO | Gate 1, Gate 5 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-078 | R-74 | VETO | Gate 2 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-079 | R-58 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-080 | R-44 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-081 | R-48 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-082 | R-86 | ABSTAIN | — | no | already marked landscape-only | retain — no veto found (a gate can only veto, never upgrade) |
| J-083 | R-36 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-084 | R-77 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-085 | R-35 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-086 | R-04 | ABSTAIN | — | yes | already marked landscape-only | retain — no veto found (a gate can only veto, never upgrade) |
| J-087 | R-21 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-088 | R-97 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-089 | R-55 | VETO | Gate 2 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-090 | R-63 | VETO | Gate 2 | no | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-091 | R-39 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-092 | R-50 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-093 | R-89 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-094 | R-06 | VETO | Gate 2 | yes | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
| J-095 | R-47 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-096 | R-37 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-097 | R-25 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-098 | R-22 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-099 | R-16 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-100 | R-72 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-101 | R-29 | ABSTAIN | — | yes | already limited to an occupational/institutional judgment | retain — no veto found (a gate can only veto, never upgrade) |
| J-102 | R-59 | VETO | Gate 2 | no | already limited to an occupational/institutional judgment | retain — the blind review reproduced the existing limit |
