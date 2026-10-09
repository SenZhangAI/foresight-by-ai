# Isolated blind re-review (2026-10-09)

[中文版](blind-review-reaudit-2026-10-09.md)

> **What this file proves, and what it does not.** It proves that 102 registered judgment cards were de-labelled, renumbered and shuffled, then re-judged card by card against the current five diffusion gates by six mutually invisible fresh-context batches, with the results fixed and hashed *before* the mapping was unsealed; and that every judgment therefore carries a recorded disposition. It does **not** prove those judgments are accurate, and it does **not** prove this project's method works. A same-model, same-criteria re-judgment can only test **reproducibility**: agreement with the old conclusion is not independent evidence of correctness, and disagreement does not automatically mean the old conclusion was wrong. Genuine out-of-sample calibration comes only from future judgment cards reaching their due date.

> ⚠ **Retrospective correction, 2026-10-09: a check added this round judged this file's input to be false; the defect has been fixed and the affected cards re-judged.** After the generator gained a semantic-field check that runs separately per language, recomputation found that of the 102 cards in the manifest this file used (`7c06add3…`), **28 cards had their one-sentence judgment field emptied entirely by de-labelling** (15 failing in Chinese only, 13 in both). The root cause is that these cards reuse the one-sentence judgment as the `### J-NNN · <title>` heading title, and de-labelling removed every title indiscriminately. Twenty-eight of the 102 dispositions below therefore rest on an insufficient evidentiary premise. The merged leakage scan of the time was structurally blind to an emptied field and reported nothing.
>
> **The remedy was not to exclude those 28 cards but to fix the de-labelling defect.** The intermediate version (manifest `404acac5…`, 74 cards included) excluded them explicitly; that path is retired, because excluding a card that does carry a claim cannot satisfy "every existing judgment receives a conclusion". The generator now lets **a card's own title survive inside that card's own judgment field only** (another card's title appearing in any field, or this card's title appearing in any other field, is still rejected), the input was re-frozen under the same inclusion rule at **102 cards** (manifest `181b35ec…`), and the 28 cards were re-judged in a second round on the repaired bundle (`e15b0e36…`). The results are in [section 11](#11-round-2--the-28-cards-re-judged-on-the-repaired-bundle) of this file; the verbatim rationales are in [`blind-review/reaudit-2026-10-09b.json`](blind-review/reaudit-2026-10-09b.json).
>
> **The status of those 28 round-1 verdicts must be stated in two classes and never conflated.** **Thirteen cards were blank in both languages** (J-032, J-033, J-035, J-036, J-037, J-040, J-041, J-042, J-043, J-044, J-046, J-050, J-051): the reviewer saw no claim in any projection, so the round-1 verdict is **void**. **Fifteen were blank in the Chinese projection only, with the English projection intact word for word** (J-002–J-005, J-031, J-034, J-038, J-039, J-045, J-047–J-049, J-052–J-054): every bundle record ships both projections, so the claim *was* in the record and the round-1 verdict is **in doubt**, not provably void. The 28 corresponding rows in the table below stand as a historical record only; the governing disposition is in section 11. See [`blind-review-bundle-2026-10-09.en.md`](blind-review-bundle-2026-10-09.en.md).

---

## 1. The question this round answers

The quality order asked for was: first calibrate the method against history, then re-analyse the documents in full, avoiding contamination by what the earlier documents already say. The first half landed in [Retrospect](../en/01-retrospect.md) and the [historical validation protocol](../en/02-historical-validation-protocol.md); this round does the second half, and treats "avoid contamination by the earlier documents" as something that must be **materialised**, not as an instruction handed to the executor.

A previous attempt already proved that swapping the instance is not isolation: the diffusion-gate review, the `REVISED` reason, the card identifier and the README summary all leak the old answer on the ledger's very first screen. So isolation here is a de-labelled, renumbered, seed-shuffled bundle; the re-reviewer sees no repository, no card identifier, no status or confidence value, and no **explicit** review paragraph or `REVISED` reason.

> ⚠ **This sentence used to read "and no pre-existing review conclusion". That claim was withdrawn on 2026-10-09.** Measured: in **101 of 102** current ledger cards the audience field carries the answer to gate one's own binary question — "raises the ceiling of existing professionals" vs. "enables people who previously could not" — and that binary was itself decided by the 2026-09-20 diffusion-gate review. In the round-1 bundle (`5d4e4732…`), **101** of the 102 audience fields keep that conclusion and **86** additionally say "reconstructed from the existing review". De-labelling stripped the words "diffusion gate", not the review's conclusion. See section 11.3, item 1. The isolation this round can claim is therefore bounded by the line above; it may **not** be stated as "pre-existing review conclusions were stripped".

This round does **not** answer whether these judgments will come true, what the accuracy rate is, or whether the method has been validated.

## 2. Input baseline and isolation evidence

| Item | Value |
| --- | --- |
| Frozen source commit | `0eb7474ef19533d9db40ba966e0ccf788ea05adb` |
| Input manifest | `docs/evidence/blind-review/manifest-2026-10-09a.json`, SHA-256 `7c06add34bb30f022b5ad9dc25b915cb53d6bc77d7627f7d9d8dde40caa881ee` (**path corrected 2026-10-09**: this round's original was first written to `manifest-2026-10-09.json`, and that path was later overwritten in place by the first remedy's 74-card version, `404acac5…`; the original has been restored from commit `66db88f` under the `-a` name and still hashes to the value above. The overwritten file is left exactly as it is, so the overwrite stays on the record) |
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

Each batch reported the SHA-256 of its own raw output on delivery, while the mapping was still sealed. Recomputed after unsealing, all six hashes are unchanged byte for byte. **Those six raw outputs were committed to this repository on 2026-10-09** (`docs/evidence/blind-review/raw/round1/raw-1.jsonl` … `raw-6.jsonl`), so a reader can now `shasum -a 256` them against the values below; until then the six hashes rested on the round owner's word alone. They carry only `review_id` / `recognized` / `gates` / `verdict` / `rationale` / verbatim missing-evidence, no `J-NNN` and no repository path, and the `R-NN → J-NNN` mapping needed to read them as per-card verdicts is already public in `reaudit-2026-10-09.json`, so committing them adds no leak. **Round 2's three raw outputs do not get this treatment**: they were never committed and the temporary directory is gone, so the three hashes listed in section 11.1 **cannot be verified by a reader** and rest on the owner's word. That is a permanent gap — see section 8.

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

> **Scope notice (read before this section)**: every figure below is on the **102-record scope**, which includes the 28 records whose input was defective (their one-sentence judgment was wiped during de-labelling — see [section 11](#11-round-2--the-28-cards-re-judged-on-the-repaired-bundle)). **Two subset scopes also exist**: the **74 records** that exclude only those 28 whole-field deletions — `VETO` 26 / `ABSTAIN` 48, gate-two-only vetoes **18**, recognized 64 (`VETO` rate 28.1%) / unrecognized 10 (80.0%), reproducibility 25/73 = 34.2%; and, after further excluding the two **half-sentence remnants** (`J-017`'s zh claim and `J-029`'s en claim — see [section 8, gap 13](#8-open-gaps)), the **72 records intact in both languages** — `VETO` 25 / `ABSTAIN` 47, gate-two-only vetoes **17**, reproducibility 25/72 = 34.7%. The three sets **must not be added together**, and any citation must say which one it uses; **the 74-card basis must not be called "claims intact"** — that label is withdrawn. The three-column comparison is in [method §1.5(3)](../en/00-method.md) and [§11.5 below](#115-coverage).

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

> ⚠ **This section is partly weakened by section 11; do not read it alone.** Nine of those 27 Gate-2-only vetoes (J-005, J-039, J-040, J-041, J-042, J-045, J-048, J-052, J-053) fell on cards whose claim field had been emptied. Once the claim prose was restored and the cards re-judged, **all nine disappeared**: five became `ABSTAIN` (J-041, J-042, J-045, J-048, J-053) and four became Gate 1 vetoes (J-005, J-039, J-040, J-052); round 2 produced **zero** Gate 2 vetoes across all 28 cards. So the Gate-2 concentration was inflated by the input defect: on the 74 cards whose claim was intact it is **18 of 26 vetoes** — still concentrated, but not 27. Among the examples named below, **J-042 and J-053 are no longer instances of a Gate 2 veto**; they are kept here only as a record.

Of the 37 `VETO` records, **27 fail on Gate 2 alone**, and the rationale is almost always the same sentence: "this card replaces no existing activity". The cards vetoed by that sentence are of wildly different kinds — a human-nature constant (J-029), landscape-only claims (J-042, J-053, **whose verdicts are superseded in section 11**), the method rules themselves (J-066, J-069, J-070), a negative boundary judgment (J-078), an infrastructure-ordering claim (J-089), gain distribution (J-090, J-102), risk pricing (J-094).

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
3. **Eighteen Gate 2 vetoes have not been re-reviewed under the new rule**: see section 7. This was registered as 27; nine of them fell on cards whose claim had been emptied and all nine disappeared in the round-2 re-judgment (not one is still vetoed on Gate 2), leaving 18 that came from cards with intact claims and still await review.
4. **The bundle carries no claim class**: de-labelling also erased the information "this is a method card / a landscape-only card / a negative boundary card", so the re-reviewers ran the capability-diffusion gates on method cards too (J-066, J-069, J-070). That is not the reviewers' error; it is a boundary of the bundle's design. The next round should carry a **neutral claim-class label** (for instance "capability diffusion / distribution / pricing / constant / rule") without leaking the old answer, and prove with negative fixtures first that the label cannot be used to recover the old identifiers.
5. **Reproducibility is only 35.6%**: about two thirds of the existing limits could not be rebuilt by the same model under de-labelled conditions. That number itself needs explaining — either the grounds for the limit are written too thinly (the card does not say why Gate 1 fails), or the gate verdicts are themselves unstable. The two causes call for opposite fixes, and this round cannot tell them apart.
6. **The leniency bias across identification strata is uncorrected**: a 26.5% `VETO` rate for recognised records against 78.9% for unrecognised. This round only measures it, and under a same-model setup there is no way to correct it. **The field is also not comparable across rounds**: the same 28 cards were self-reported as recognised 19/28 in round 1 and 0/28 in round 2 (see section 11.2).
7. **Leakage isolation is procedural**: anyone holding both the bundle and the public repository can restore the mapping, and training memory cannot be removed.
8. **Round 2's dispatch prompt itself leaked the source project**: its hard-constraint block named the repository path, the `docs/` directory and the `J-NNN` identifier shape, and two batches disclosed unprompted that this let them infer the project (see section 11.3). A future round must phrase the prohibition without naming any path or identifier shape; until that is changed, provenance isolation must not be claimed as achieved.
9. **The attribution of round 2's Gate 1 concentration is undetermined**: all 15 vetoes fail Gate 1, but these 28 cards are a specific subset of landscape-only cards about relationships, meaning and care, and their audience fields share one boilerplate sentence. "Caused by the repair" and "a property of the subset" cannot be separated by this round; it needs re-testing on another subset whose claims were intact.
10. **The two rounds' counts cannot be merged**: they are not the same bundle, the same batches or the same seed, and their `R-NN` namespaces are disjoint. Any "102-record statistic" must be stated per round and never summed.
11. **The audience field handed gate one's review conclusion to the reviewer**: all 102 cards carry one side or the other of it — 101 of 102 cards carry, in the audience field, the "raises an existing professional's ceiling vs. enables someone who previously could not" binary that the gate-one review itself decided, and 86 of the round-1 bundle's 102 records additionally say "reconstructed from the existing review" (section 11.3, item 1). Both rounds are affected. To close it: split "gate-one conclusion" from "audience scale and behavioural denominator" into two fields on the card, let only the latter enter the bundle, and first prove by negative case that the split audience field is not enough to recover the gate-one conclusion. **Until that is done, no claim that pre-existing review conclusions were stripped may be made, and no "blind verdict reproduced the existing scope limit" count may be used as evidence of independent reconstruction.**
12. **Round 2's three raw outputs can never be verified**: round 1's six were committed to the repository (section 3) and a reader can recompute them; round 2's three were never committed and the temporary directory is gone, so the three hashes in section 11.1 rest on the round owner's word alone. This does not void round 2's verdicts — the per-card verdicts and verbatim missing-evidence are inside `reaudit-2026-10-09b.json` — but the "results first, unseal second" step **cannot be audited by a third party** for round 2. To close it: it cannot be closed; a future round must commit its raw outputs in the same commit that publishes their hashes.
13. **The label "74 records with intact claims" does not hold: the half-sentence-remnant class has three members, and one of them sits inside the numerator of 18/26.** On 2026-10-09 the de-labeller gained a `lang_claim_scar` check ("is what remains after deletion still a complete claim"), and running it against the real round-1 bundle (`5d4e4732…`) produced 24 hits: 16 are whole-field deletions (`lang_semantic` already caught those, and all of them sit among the 28 cards), and **3 are half-sentence remnants** —
    - `J-017` (zh judgment): what remained was "2027-2033 年,,但不会同步扩大…"; the affirmative half was deleted. Verdict `ABSTAIN` with no gate vetoed, so **it is in neither the 26 nor the 18** (the ledger previously registered it as the contaminant behind 18/26; that registration is withdrawn in place).
    - `J-029` (**en** judgment): what remained was "From 2026-2030,,certainty,embodied presence,and responsibility…"; one of the four demand-side anchors was deleted, while the zh projection stayed intact. Verdict `VETO`, **gate-two-only**, and it is the **only `downgrade`** in the 74-card subset — the single disposition this round that actually rewrote a public card's state. **Its downgrade is not void**: the veto rationale reads verbatim "this is a demand-side anchor judgment and replaces no existing action," which does not route through the deleted span.
    - `J-053` (en falsifier): that card sits among the 28, is already excluded, and affects no current figure.
    **Consequence**: any wording of the form "74 records with intact claims" is a false label. The subset intact in **both** languages is **72 records**, with `VETO` 25 / `ABSTAIN` 47 / gate-two-only vetoes **17** / reproducibility 25/72 = 34.7%. Every 74-card citation in this report and in the methodology now reads "the 74 records that exclude only whole-field deletions," stated beside the 72-card basis. To close it: the check has landed (negative case `foreign_title_cut_out_of_claim`; self-test green at 21/21); whether `J-017` and `J-029` get re-judged must wait for the audience-field split and happen together with the 12 records in section 11.3. This round re-runs nothing.
    **One methodological discipline**: these three were found by pointing the check at the real OUTPUT, not by the repository-side approximation "is the heading title a substring of the judgment" — that approximation finds only `J-017`, because the de-labeller splits each title on `·` / `:` and deletes the fragments, which a whole-string comparison on the input side cannot see. **To find a de-labelling defect, inspect the output, not the input.**


The results of this round must not be written up as any of the following:

- "The blind re-review passed, the judgments are validated" — `ABSTAIN` is not a pass;
- "Only 1 of 102 cards needed a downgrade, so judgment quality is high" — 101 cards entered this round already limited; the denominator had been consumed by the earlier downgrades;
- "The blind review agreed with the old conclusions X% of the time, so the method works" — same-model agreement is not correctness;
- "Zero falsifications, so no judgment was overturned" — this round does not rule on falsifiers;
- "Old-answer leakage has been eliminated" — it was measured, not eliminated.

## 10. Per-card disposition table

The table below carries round 1's disposition for 102 cards. The verbatim rationale and missing-evidence note for each is in the record with the same `R-NN` in [`blind-review/reaudit-2026-10-09.json`](blind-review/reaudit-2026-10-09.json).

> ⚠ **Twenty-eight rows in this table are superseded.** The records for J-002–J-005 and J-031–J-054 had their claim field emptied in the round-1 bundle (13 blank in both languages, 15 in Chinese only); those rows stand as a historical record only and **the governing disposition is in [section 11](#11-round-2--the-28-cards-re-judged-on-the-repaired-bundle)**. The other 74 rows are valid and are what the cards themselves carry; the disposition line on those 28 cards has been rewritten in place with the round-2 result.

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

## 11. Round 2 — the 28 cards re-judged on the repaired bundle

> **Identifier warning**: the `R-NN` names in this section and the `R-NN` names in [section 10](#10-per-card-disposition-table) are **two disjoint namespaces**. Measured: **all 28** of round 2's identifiers reuse a round-1 name while pointing at a different card (`R-04` = round 1 `J-086` / round 2 `J-002`; `R-44` = `J-080` / `J-032`; `R-50` = `J-092` / `J-043`). Any cross-section citation must carry the round; identical names across the two sections are **not interchangeable**.

Round 1's verdicts on these 28 cards are unusable (13 void, 15 in doubt — see the banner at the top). Once the defect was fixed, the 28 cards were re-judged on the re-frozen 102-record bundle. The relation to section 10 is: **those 28 rows in section 10 are retired and this section governs**; the other 74 rows are unaffected and were deliberately **not** re-run (a re-run would only test reproducibility a second time, and would create two incompatible `R-NN` namespaces).

### 11.1 Input and the "results first, unseal second" evidence

| Item | Value |
| --- | --- |
| Frozen source commit | `98fd95701da3bacef4d43e304db6b82e3f4d3b9b` |
| Input manifest | `docs/evidence/blind-review/manifest-2026-10-09b.json`, SHA-256 `181b35ecec7ed9aa04a4af212ac3ca58edf0f6b153820c20cda69c483b4c1af1` |
| Inclusion rule | The same rule as round 1: both language versions carry all six required retained fields, and every one of them still has readable content **after** de-labelling. The only change this round is that **a card's own title survives inside that card's own judgment field** |
| Coverage | 197 candidates → **102** included → 95 excluded (historical migration snapshots only; round 1's "lost its claim to de-labelling" exclusion bucket is now empty) |
| Output bundle | SHA-256 `e15b0e36d427432aeddb436f6fe205f53af691c04c0a58083b51647e34f43360`, 102 records in each language; **zero** empty judgment fields in either language |
| Selection rule | Re-judge only the 28 cards whose claim had been emptied in round 1 (13 blank in both languages + 15 blank in Chinese only). The list was fixed before any new verdict existed and is independent of any prior verdict |
| Batches | 3 mutually invisible fresh-context batches (10 / 9 / 9 records), none with repository access |
| Raw-output hashes | Each batch reported the SHA-256 of its own output while the mapping was still sealed; after unsealing, the leader recomputed all three and they matched byte-for-byte |

```
60593387b75b93802e9116c10f90ff7cf5f9405cf9d25d082d0fe284543f8159  raw-1.jsonl
25b20d976c2e3b764bb05e8e945ab83f1481cf619f085d04dbc133bc1cbd2277  raw-2.jsonl
76aae999b8b8b8681fe785a1977548ad29b270fc33c1a7565b76e9c79eb2abaa  raw-3.jsonl
```

### 11.2 Results

**Verdict distribution**: `VETO` 15 / `ABSTAIN` 13. `FALSIFIED` 0 — this round again adjudicates no card's falsifier, so that zero is a scoping result, not a finding that no judgment was overturned.

**Every veto lands on Gate 1.** All 15 vetoes fail Gate 1 (the audience ceiling) and **none** fails Gate 2. Compare round 1's verdicts on these same 28 cards when the claim prose was missing — `VETO` 11 / `ABSTAIN` 17, with 10 Gate 2 vetoes and only 1 Gate 1 veto — and the shift has a clear direction: with nothing readable about *what this replaces*, the reviewer tends to veto on Gate 2; once the claim prose is back, the veto reason moves wholesale to "this population cannot carry society-level scale". That directly weakens the "27 Gate 2 vetoes" finding of section 6, which is annotated in place.

**This does not license the conclusion that Gate 2 itself is broken.** These 28 cards are a specific subset (J-002–J-005 and J-031–J-054, mostly landscape-only cards about relationships, meaning and care, whose audience fields all carry the same "raises existing professionals' ceiling" boilerplate), so the Gate 1 concentration may be a property of the subset rather than an effect of the repair. This round cannot separate the two explanations.

**Agreement with round 1**: the verdict word matches on **12 of 28** (42.9%); the verdict *and* the failing gate match on only **7 of 28** (25.0%). This number is **not** evidence about which round was right: round 1 answered on empty or half-empty records, which is not a comparable baseline. Its only use is to quantify how far an input defect can move a verdict.

**Identification stratum**: self-reported recognition of the original judgment, **0 of 28**. The same 28 cards were self-reported as recognised 19/28 in round 1. **Identification counts are therefore not comparable across rounds**: same cards, same model, and the self-reported recognition rate fell from 68% to 0%, while two batches this round volunteered that they could infer which project the records came from. Read the field as "did I recognise this judgment", never as a leakage measurement.

### 11.3 Residual leakage introduced this round (stated, not hidden)

1. **The audience field handed the reviewer gate one's own review conclusion (a conclusion-level leak, not merely an existence-level one)**. Measured two ways, which agree. **From the cards (a reader can recompute this; it is this item's primary evidence)**: of the 102 current ledger cards, **101** have an audience field containing "raises the ceiling of existing professionals", **10** contain "enables people who previously could not", and **9 carry both**, so the number of cards carrying one side or the other of that binary is **102 — all of them** (this item originally said "101", which omitted the other side of the binary and understated the scope; corrected); on the English side 101 contain `raises the ceiling of existing professionals`. **From the bundle**: in the round-1 bundle (`5d4e4732…`, byte-identical to the hash published in section 2), **101** of the 102 audience fields keep that conclusion and **86** additionally read "reconstructed from the existing review" — but neither that bundle nor its seed is committed (see the [bilingual bundle evidence pack](blind-review-bundle-2026-10-09.en.md)), so **this side cannot be recomputed by a reader and rests on the round owner's word alone**. The two are not equally verifiable; only the card-side measurement is. That binary — raises an existing professional's ceiling vs. enables someone who previously could not — **is exactly the question gate one asks**, and its answer was produced by the 2026-09-20 diffusion-gate review. De-labelling removed the words "diffusion gate" and left both the conclusion and the fact that a review had happened.

   **This violates the acceptance clause "strip the diffusion-gate review … and any pre-existing review conclusion in the prose"; it is not a marginal residue.** The boundary must be rewritten (an independent review on 2026-10-09 refuted what this paragraph previously said): it originally asserted that the leak does **not** void any verdict because the reviewer still answered gate by gate against the claim text. **That is false for most of round 2's vetoes.** Measured: of round 2's 15 gate-one vetoes, **12** (`J-002`, `J-003`, `J-032`, `J-033`, `J-034`, `J-035`, `J-039`, `J-040`, `J-043`, `J-044`, `J-046`, `J-052`) give as their ratio decidendi a **direct quotation of the leaked audience conclusion** — e.g. "the audience field self-reports … and explicitly says 'raises the ceiling of existing professionals', so under gate one the ceiling is the size of that profession". For those 12, what the reviewer judged on was the old conclusion handed to it, not the claim text. **Consequence**: although those 12 are recorded as "retained · blind verdict reproduced the existing scope limit", they **must not be read as independent reproduction** — they hand back what was handed in; section 8's gap 9 previously offered only two attributions ("an artifact of the fix" vs "the subset is simply like that") and called them indistinguishable, and a third is now added and evidenced item by item: **round 2's high gate-one veto rate comes in part directly from the audience-field leak.** It also forces the withdrawal of the sentence "the re-reviewer sees no pre-existing review conclusion" (withdrawn in place in section 1), and it narrows what **both rounds** (the card prose did not change between them, so this is not specific to round 2) can claim to "card identifiers, status, confidence, explicit review paragraphs and the dependency graph were stripped". **Until the audience field is written differently, no claim that pre-existing review conclusions were stripped may be made.** The fix for a future round is not to delete the audience field — it is gate one's required input — but to split "gate-one conclusion" from "audience scale and behavioural denominator" into two fields on the card, and let only the latter enter the bundle. This item previously recorded the scale as "10 / 9 / 9 records in the three batch files"; that was only the count of the literal "reconstructed from the existing review" phrase in round 2's three slices, missing both round 1 and the more serious half (the conclusion itself). That record is corrected here.
2. **The dispatch prompt itself leaked the source project**: in the hard-constraint block the leader named the repository path, the `docs/` directory and the `J-NNN` identifier shape — intended as a prohibition on reading them, with the effect of telling the reviewer which project the records belong to. Batches 2 and 3 both **disclosed this unprompted**. This leak was **introduced** this round, by the leader; it leaks provenance, not any prior verdict. A future round must phrase the prohibition without naming any path or identifier shape.
3. **The old boundary of procedural isolation is unchanged**: anyone holding both the bundle and the public repository can restore the mapping by comparing prose word for word, and the reviewer and the original author are the same model, so training memory cannot be removed by de-labelling.

### 11.4 Per-card disposition (28 records)

The `Round-1 status` column has only two values: **void** = the claim was blank in both languages, so the round-1 verdict cannot be attributed to this judgment; **in doubt** = blank in the Chinese projection only, with the English projection intact word for word, so the claim *was* in the record and the round-1 verdict rests on an insufficient premise without being provably void.

| Card | Round-1 status | Round-1 verdict (on record) | Round-2 record | Round-2 verdict | Gates failed | Recognised | State before review | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J-002 | in doubt | ABSTAIN (no gate) | R-04 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-003 | in doubt | ABSTAIN (no gate) | R-46 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-004 | in doubt | VETO (Gate 3) | R-06 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-005 | in doubt | VETO (Gate 2) | R-101 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-031 | in doubt | ABSTAIN (no gate) | R-64 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-032 | void | ABSTAIN (no gate) | R-44 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-033 | void | ABSTAIN (no gate) | R-70 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-034 | in doubt | ABSTAIN (no gate) | R-10 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-035 | void | ABSTAIN (no gate) | R-55 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-036 | void | ABSTAIN (no gate) | R-39 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-037 | void | ABSTAIN (no gate) | R-90 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-038 | in doubt | ABSTAIN (no gate) | R-08 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-039 | in doubt | VETO (Gate 2) | R-41 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-040 | void | VETO (Gate 2) | R-56 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-041 | void | VETO (Gate 2) | R-81 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-042 | void | VETO (Gate 2) | R-07 | ABSTAIN | — | no | already marked landscape only | retain — no veto found (a gate can only veto, never upgrade) |
| J-043 | void | ABSTAIN (no gate) | R-50 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-044 | void | ABSTAIN (no gate) | R-102 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-045 | in doubt | VETO (Gate 2) | R-91 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-046 | void | ABSTAIN (no gate) | R-34 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-047 | in doubt | ABSTAIN (no gate) | R-86 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-048 | in doubt | VETO (Gate 2) | R-58 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-049 | in doubt | ABSTAIN (no gate) | R-97 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-050 | void | ABSTAIN (no gate) | R-79 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-051 | void | VETO (Gate 1, Gate 2) | R-49 | ABSTAIN | — | no | already REVISED | retain — no veto found (a gate can only veto, never upgrade) |
| J-052 | in doubt | VETO (Gate 2) | R-33 | VETO | Gate 1 | no | already REVISED | retain — the blind review reproduced the existing limit |
| J-053 | in doubt | VETO (Gate 2) | R-62 | ABSTAIN | — | no | already marked landscape only | retain — no veto found (a gate can only veto, never upgrade) |
| J-054 | in doubt | ABSTAIN (no gate) | R-43 | ABSTAIN | — | no | already marked landscape only | retain — no veto found (a gate can only veto, never upgrade) |

### 11.5 Coverage

Of the 102 registered judgment cards, **all 102** now carry a blind disposition made on a record whose claim prose was intact: 74 from round 1 (section 10) and 28 from this round (this section). Both rounds used the same inclusion rule and the same five gate criteria, but **not the same bundle, not the same batches and not the same seed**, so the two rounds' `R-NN` namespaces are disjoint and their counts must not be added into a single "102-record statistic".

Two things must be stated precisely:

- **Section 4 prints the 102-record figures** (`VETO` 37 / `ABSTAIN` 65, gate-2-only 27, recognition strata 83 / 19, reproducibility 36/101 = 35.6%), and those include the 28 records whose input was defective. **Round 1's still-valid 74-card subset has its own figures**: `VETO` 26 / `ABSTAIN` 48, gate-2-only **18**, recognised 64 (`VETO` rate 28.1%) / not recognised 10 (80.0%), reproducibility 25/73 = 34.2%, with the single new downgrade `J-029` still inside it. That is a **recomputation** over a subset of section 10's disposition table, not a re-run; the three rows side by side are in [methodology §1.5(iii)](../en/00-method.md). This section previously said "the three count groups in section 4 hold only for round 1's valid 74-card subset" — **that sentence was wrong** and is superseded by this paragraph.
- **`R-NN` is round-scoped: the same literal identifier denotes different cards in the two rounds.** Measured: **all 28** of round 2's identifiers collide with a round-1 identifier pointing at a different card — e.g. `R-04` = round 1 `J-086` / round 2 `J-002`, `R-44` = `J-080` / `J-032`, `R-50` = `J-092` / `J-043`. Always carry the round when citing an identifier; the same identifier in section 10 and section 11.4 is **not** interchangeable.
