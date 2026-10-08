# Historical Pseudo-Out-of-Sample Validation Protocol

[中文版](../zh/02-historical-validation-protocol.md)

[Back to README / document map](../../README.en.md)

> This is an **execution protocol**, not a round of backtesting, and it produces no new judgments about the future. It freezes how historical cases enter the pool, how they are split, who may see what, how scoring works, and what the results can support. The five diffusion gates are in [Retrospect](01-retrospect.md); the general rules of reasoning are in [Foresight Methodology](00-method.md); the genuine out-of-sample record for judgments about the future is still carried by the due-date checks in the [judgment ledger](90-ledger.md).

> **Version anchor**: v1 was frozen at commit `f5f0833`; the 2026-09-21 calibration narrowed Gate 5's input from “per-use cost” to “recurring net burden relative to the incumbent.” The v1 holdout therefore cannot validate v2; section 10 requires an isolated re-review.


| Ledger | What it can do | What it can support | What it cannot support |
|---|---|---|---|
| **Calibration set (calibration)** | Look at outcomes, hunt for counterexamples, revise rules and wording | Whether the rules explain known history, and where their boundaries lie | Predictive power, hit rate |
| **Historical pseudo-out-of-sample holdout (holdout)** | Freeze the rules and materials first, judge the gates first, reveal once at the very end | Whether, under shared leakage, it adds discrimination relative to a baseline | Uncontaminated absolute accuracy |
| **Future due-date judgment cards** | Check the falsifier once the card comes due | A genuine out-of-sample record | Samples are still few; calibration cannot be claimed in advance |

Once a case has entered the calibration set, it may never enter the holdout set. Once a holdout set has been revealed, it too is permanently retired into calibration material.

## 0. Evidence labels and the existing-judgment baseline

This protocol uses four mutually exclusive evidence labels. A label describes the evidence's temporal order and traceability; it is not a medal for a conclusion:

| Label | Determination | What it may support | What it must never be upgraded into |
|---|---|---|---|
| `CALIBRATION` | Historical material selected, assembled, or used to revise a rule after the outcome was known; it remains this class even when the as-of-T material can be reconstructed | Retrospective explanation, counterexamples, and recording boundaries | `CONTAMINATED_RELATIVE_HOLDOUT`, `GENUINE_FUTURE_OOS`, accuracy, or hit rate |
| `CONTAMINATED_RELATIVE_HOLDOUT` | Rules, candidates, inputs, and scoring were frozen before reveal; gates were judged before a one-shot reveal and compared with a same-input baseline, but model memory or case fingerprints create shared leakage | Relative discrimination against the baseline under shared leakage | Uncontaminated absolute accuracy or future hit rate |
| `GENUINE_FUTURE_OOS` | The judgment text, information cutoff, outcome definition, and observation window were frozen before the outcome was observed, and the outcome was revealed only after the window ended | A genuine out-of-sample record from a due future card | Any accuracy claim before maturity |
| `UNKNOWN/UNVERIFIED` | At least one of the original artifact's identity or stable location, same-window outcome, metric / unit, denominator, or measurement definition cannot be closed | The gap itself and the next verification action | Any definite miss, any of the three labels above, or an accuracy denominator |

A label may move upward only when its evidence conditions are met. It may not be upgraded because the narrative is fuller, the direction looks right, the file count increased, or a structure check passed. `UNKNOWN/UNVERIFIED` is not a failure finding; it must remain unknown until the gap is closed. A case assembled after its outcome was known can never become a holdout, and reconstructing what was visible at T after the fact can never become genuine future out-of-sample evidence.

The public boundary established by the current round is narrow: FOMC `P-04` and Webvan `B-WEBVAN` are reconstructible `CALIBRATION` pairs in the October 2026 records; `T-SHUTTLE` remains `UNKNOWN/UNVERIFIED` because the same-window official mission list and a pre-specified denominator rule are not closed. See the [cross-domain historical calibration record](../evidence/historical-calibration-round-2026-10.en.md). These materials support tighter recording and classification discipline only; they do not support accuracy, a validated method, a falsified diffusion gate, or a new future judgment. If later evidence closes a gap, the label conditions in this section must be rechecked; the existence of a protocol or a passing structure check is not a substitute for evidence.

Before a full re-review, the **existing-judgment baseline** must also be frozen so a reader can reproduce what was and was not reviewed: the complete card manifest, inclusion / exclusion rules and their generation time, the frozen commit SHA, Chinese and English paths with content hashes, card count, dependencies, and current statuses. Once frozen, cards may not be added or removed to fit the result. Any later change requires a new commit with its reason; it may not overwrite the original baseline.

## 1. Unit of analysis and the candidate pool

The **unit of analysis** is `(candidate activity / institution / supply, judgment time T)`, not a famous brand or person. The same capability at a different T is a different case; all five gates must use the same T.

The candidate pool may come only from **registries that already existed at T, that allow the population to be enumerated, and whose inclusion does not depend on later success or failure**. Drawing topics from "the ten greatest successes", "the biggest product failures in history", or the famous cases the author happens to remember is forbidden. Before the first round is executed, whoever sets the cases must write the registries actually used, their versions, coverage intervals, exclusion rules, and archive locations into the manifest; the table below freezes the permitted sampling frames and their minimum requirements:

| Domain | Preferred sampling frame | Entry as of T | Acceptable reveal sources | Main traps |
|---|---|---|---|---|
| Technology | USPTO / WIPO application publication records; arXiv submission lists by date and category; ClinicalTrials.gov registrations after mandatory registration took effect | An application, paper, or trial registration — not a later prize winner | Grant / citation / productization records; follow-up papers and approvals; trial termination or results | Patents and papers are not social adoption; the candidate activity and the target population must be defined separately; clinical trials before 2007 carry a high backfill bias |
| Politics / public policy | The complete set of bill numbers on Congress.gov / GovTrack; proposed rules in the Federal Register; the approved-project list of World Bank Projects | A proposal, a proposed rule, or an approved project — not an entry that later became a "milestone" | Bill life cycle, final rule / withdrawal, project completion and independent evaluation | Proposal thresholds vary; the outcome must not be self-assessed by the same agency that proposed the project |
| Business | The complete set of S-1 / F-1 filings on SEC EDGAR; archived snapshots of crowdfunding platforms at the moment projects went live; the full roster of an accelerator batch as announced | A filing, a launched project, or an entire admitted batch, including withdrawn and dormant entries | Listing / withdrawal / delisting records; goal attainment and delivery status; funding, acquisition, or shutdown | Current directories delete the failures; the snapshot of the time must be used — today's survivor pages cannot be used to reconstruct the population |

Each domain must use at least two heterogeneous registries, so that a single institution's screening preferences are not mistaken for the world's denominator. At least 12 cases per domain and at least 48 in the whole pool; every `domain × decade` stratum actually used must contain at least 4 cases and an even number, so that assignment leaves at least 24 cases in holdout. **Ordinary cases that drew no notable attention at T** must make up at least one third. If the quota cannot be met, the only remedy is to widen the registries — famous cases may not be used to fill the gap. These minima create basic holdout capacity only; they do **not** guarantee that reveal will produce enough S outcomes, `PASS` cases, or `VETO` cases. Section 9 treats such a result as insufficient information, not a failure of the rules.

## 2. What gets frozen before any outcome is looked at

Every row of the candidate-pool manifest must carry the fields below. A row missing any one of them may not enter the pool:

| Field | What it freezes |
|---|---|
| `case_id` | `HC-T-NN` / `HC-P-NN` / `HC-B-NN`; unique, never reused, shared by Chinese and English |
| `registry_source` | Registry name, year / version, entry number or archive URL |
| `T` | A single judgment time point; shared by all five gates |
| `candidate_activity` | "Who does what, in what setting"; must contain no outcome hints such as "failed", "eventually", or "famous" |
| `target_population` | The denominator for society-scale and segment-scale adoption rates; must be definable as of T |
| `as_of_packet` | The list of materials visible to the gate judge; each item carries a publication date or archive timestamp, none later than T |
| `reveal_source` | The pre-designated source of the outcome; before gate judging only its location is registered, its content is not opened |
| `outcome_window` | The observation window, uniform across the registry family and not adjustable case by case: technology T+15 years; politics / public policy T+10 years; business T+10 years |
| `split_stratum` | Domain × the decade T falls in; only attributes visible at T |
| `packet_hash` | SHA-256 of the as-of packet, used to prove the question did not change across the reveal |

If there is still no verifiable result by the end of the observation window, code it as "undetermined"; a more convenient cut-off may not be substituted. Only cases satisfying `T + outcome_window ≤ execution year` may enter this round; the rest stay in the reserve pool.

## 3. Pre-assignment to the calibration set / holdout set

The assignment rule is executed before any gate judging, and may not use the outcome, fame, whether the model recognizes the case, or "whether this case makes the point better".

1. The candidate-pool author first commits a manifest containing only the candidate pool and the section 2 fields; once committed, it may not be amended or replaced.
2. An **independent assignment operator who cannot see case outcomes** generates one 256-bit random salt after the manifest commit and immediately commits it separately; the salt may not come from the candidate-pool author and may not be redrawn after trial computation.
3. For each case compute:

```sh
printf '%s' "$SPLIT_SALT:$CASE_ID" | shasum -a 256 | cut -c1-8
```

4. Within each `domain × decade` stratum, sort ascending by `(computed key, case_id)` (`case_id` is the deterministic tie-break for an extremely unlikely hash collision): even positions (counting from 0) go to the holdout set, odd positions to the calibration set. This protocol requires every stratum to contain an even number; if the execution check finds otherwise, the manifest is invalid and returns to the candidate-pool author for completion **before assignment**.
5. Commit the split table and each case's computed key, so that anyone can recompute it. Once the salt or split has been seen, re-drawing is forbidden. Only three post-assignment errors can void a batch: a missing required field, a non-conforming stratum size, or a hash / sort that cannot be reproduced. Evidence of the error and its reason must be committed first, and **the entire exposed batch retires into calibration; the same cases may not be redrawn under a new salt**. After correction, a new manifest may be built only from never-assigned, never-read reserve cases, and a new independent operator generates a new salt.

**Once fixed, no case may be moved.** Whether the model happens to recognize a case affects only the stratified reporting in section 7, not the split. The random salt prevents a candidate-pool author who knows outcomes from grinding assignments by changing a commit SHA or `case_id`; what it guarantees is an independent, one-shot draw, not author self-restraint.

## 4. Role isolation: the same author cannot both know the answer and sign off on it

Each role is carried by an independent fresh-context instance; conversation history is not shared:

| Role | Can see | Delivers | May not take part in |
|---|---|---|---|
| **Candidate-pool / case author** | Registries and materials as of T; may incidentally know the outcome | The manifest and standardized as-of packets | Gate judging, outcome adjudication, final rulings |
| **Gate judge** | A single as-of packet, and a gate-judging handbook with every historical example removed | Identification probes, the five gate verdicts, reasons for abstention, unlocking conditions for the speed layer | The full repository, reveal sources, other roles' outputs |
| **Baseline arms** | Exactly the same as-of packet as the gate judge | Each baseline's split verdicts | The five-gate text, other arms' outputs, reveal sources |
| **Outcome adjudicator** | The frozen definitions in the manifest and the reveal sources | Outcome coding, the date the outcome threshold was first crossed (`NOT_REACHED` if it never was), and evidence anchors | Gate-judging results, baseline results, unlocking conditions |
| **Disagreement / unlocking arbiter** | The committed outcome coding and threshold-crossing date; for a dispute, the frozen case card and both sides' conclusions; for unlocking, the sealed condition written in advance and read-only, logged access to the reveal sources after outcome coding is frozen | Item-by-item rulings with reasons; an evidence-cited determination of whether an unlocking condition occurred before S | Rewriting case definitions, adding post-hoc conditions or material |

The gate-judging handbook may keep only the criteria of the five gates; every example — the Picturephone, the hydrogen car, New Coke, and all the rest — must be deleted. If a gate judge can reach this repository or a reveal source, that case is void but still retires; the same case may not be re-run with a different person.

## 5. Uniform output for the five gates

The gate judge fills this in case by case, and may not hand in a single overall impression:

| Gate | Required inputs | Output |
|---|---|---|
| Gate 1 · Scale | Activity definition, order of magnitude of the target population, frequency, and whether it raises the ceiling for people who already do this professionally or lets people who could not do it at all do it now | pass / fail / abstain |
| Gate 2 · Replacement | The specific old activity being replaced; if there is none, write `NONE` | pass / fail / abstain |
| Gate 3 · Carrier | Dedicated infrastructure, who pays for it, whether there is a second use or independent revenue | pass / fail / abstain |
| Gate 4 · Decision | The parties that must change together, and whether unilateral compulsion or a local closed loop exists | pass / fail / abstain |
| Gate 5 · Recurring net burden | Per-use net burden relative to the real incumbent at T: added bodily / social / learning / monetary burden minus saved waiting / price / time / process cost; plus whether an enforceable compelling party exists | pass / fail / abstain |

Every piece of evidence must be no later than T. Insufficient material permits only abstention, with "what is missing" written out; information from after T may not be used to patch the question. When a speed-layer gate (Gates 2 through 4) is failed, an unlocking condition must additionally be written that is **observable, has an agent, and has a time point**; if none can be written, the claim is handled as "will not reach society-scale diffusion within the observation window".

## 6. Outcome coding and necessary-condition scoring

The outcome adjudicator codes against the frozen `target_population` and observation window, and records `outcome_date` for every case: the date the coded threshold was first crossed. Write `NOT_REACHED` if it never was; if the exact day is unknown but a bounded interval is verifiable, record the narrowest defensible interval and use it as a sensitivity bound. An S or D code without a date and evidence anchor is invalid:

- **S · Society-scale diffusion**: the target activity reaches at least a hundred-million-scale population at weekly frequency, or a billion-scale population at daily frequency;
- **D · Segment / domain diffusion**: it becomes the majority practice within a sub-population already definable at T, but does not reach S;
- **I · Intermediate outcome**: there is sustained adoption, yet it has neither become the majority of a defining population nor exited;
- **N · Not diffused / exited**: it stays marginal for the long run, or the product / policy / organizational path was withdrawn or terminated;
- **U · Undetermined**: verifiable measurement is missing, or it still cannot be classified at the end of the observation window.

The five gates are a **necessary-condition filter, not a sufficient-condition predictor**: any gate failed = `VETO`; all five passed = `PASS`, which only means eligible to compete; any key input missing = `ABSTAIN`.

Necessary-condition errors are asymmetric:

| System output | Outcome S | Outcome D / I / N |
|---|---:|---:|
| `VETO` | **Fatal false veto, loss 10** | Correct veto, loss 0 |
| `PASS` | No penalty | Not counted as an error; the five gates never promised sufficiency |
| `ABSTAIN` | Loss 1 | Loss 1 |

Report sensitivity analyses at 5:1 and 20:1 as well; if the conclusion flips with the weight, the only thing that may be written is "no increment established". For a speed-layer `VETO`, if the unlocking condition written down in advance did in fact appear before S, record it separately as a "conditional hit" rather than a fatal false veto; an unlocking condition written in after the fact is void.

**Intermediate outcomes and abstentions must not disappear:** the main analysis merges D / I / N into "not S", and additionally reports both extremes — all I counted as S, and all I counted as not S; U does not enter the main denominator, but the bounds from counting all U as S and all U as not S must be reported. If a single gate judge's abstention rate exceeds 25%, that round may serve only as protocol debugging and may not report an increment.

## 7. Identification probes and known contamination

After the gate judge has read the as-of packet and **before** gate judging begins, three items are submitted at once and may not be revised afterwards:

1. Identity guess: the case's real name / subject; write `UNKNOWN` if not known;
2. Outcome guess: S / D / I / N / don't know;
3. Confidence in those guesses: high / medium / low.

Report by the following identification layers:

- `R0`: identity unknown, and the outcome guess is low confidence or don't know;
- `R1`: identity guessed but uncertain, or identity unknown with a medium-confidence outcome guess;
- `R2`: identity was definite before reveal, or the outcome guess was high confidence.

The strata are determined only by identity and confidence submitted **before reveal**; whether the guess was later correct is reported in a separate column and may not reassign a case. The main result must give both the whole set and the `R0+R1` subset; `R2` serves only as sensitivity analysis and may not be deleted so as to pretend there was no leakage. If `R2` exceeds half of the holdout set, the whole round is downgraded to calibration and may not be called "pseudo-out-of-sample". If a no-rule baseline still scores near perfect on `R0`, de-labelling has failed, and that batch is likewise downgraded.

These measures **cannot eliminate contamination**. A model's training data may already contain the cases, the outcomes, diffusion theory, even this repository; the dates, amounts, and structure preserved in an as-of packet may themselves be fingerprints. A fresh context isolates only this round's roles; it does not erase the model's memory. This protocol can therefore only compare **relative increments under shared leakage**.

## 8. Baselines on the same input and the same model

All model baselines must use the same model version, parameters, as-of packet, and run batch as the gate-judging arm, and must be executed in an independent fresh context:

| Baseline | Rule |
|---|---|
| **B0 · Base rate** | Always judge "not S", showing how skewed the candidate pool itself is; the model is not called |
| **B1 · Direct verdict without gates** | The five gates are not supplied; it is asked only whether S can be reached within the observation window, and abstention is allowed |
| **B2 · Technically mature means diffused** | If a runnable / mass-producible implementation already existed at T, judge it eligible to reach S; otherwise veto |
| **B3 · External method** | Use Rogers's five attributes, frozen in advance: relative advantage, compatibility, complexity (reversed), trialability, observability, 0–2 points each; total ≥6 is `PASS`, otherwise `VETO` |

The B3 threshold may not be adjusted after the reveal, and no baseline may be given more material. If the model version is changed during execution, every arm re-runs the whole round; results may not be stitched across versions.

## 9. Main metric, reveal, and stopping rules

Each arm's discrimination is defined as:

```text
D = P(S | PASS) - P(S | VETO)
```

When either the `PASS` or the `VETO` set is empty, D is recorded as not computable; a pretty one-sided precision is not substituted for it. The **main metric** is:

```text
ΔD = D(five gates) - max[D(B1), D(B2), D(B3)]
```

B0 reports the base rate only and does not take part in the `max`. If one model baseline has an empty `PASS` or `VETO` set, its D is not computable and is excluded from `max`, but must still be reported verbatim. If B1–B3 are all not computable, `ΔD` is also not computable and the batch is classified as insufficient information; a missing baseline may not be substituted with zero. Publish alongside it the raw counts of `VETO/PASS/ABSTAIN × S/D/I/N/U`, the coverage rate, the number of fatal false vetoes, and the asymmetric loss of section 6. If the batch contains no S outcomes, or if either `PASS` or `VETO` provides no observable contrast between S and non-S, the only permitted conclusion is "this batch's outcomes lack the information needed to test discrimination". That is neither a pass nor a failure of the rules, and it does **not** count toward the three substantive failures in section 10. Only when all of the following hold may one write "this round shows relative incremental discrimination":

1. `ΔD > 0`, and neither of the two conventions for I and U flips the sign;
2. At least 12 non-abstained cases, with at least 4 each in `PASS` and `VETO`;
3. The direction does not reverse in the `R0+R1` subset; when the sample is insufficient, write "cannot be determined" — the whole-set result may not be borrowed in its place;
4. Fatal false vetoes are 0. If one occurs, adjudicate it first under the corresponding [J-066–J-071 judgment card](90-ledger.md#13-judgment-cards-distilled-from-the-historical-retrospective)'s own falsifier, including its time window and exceptions. Revise the rule or withdraw the corresponding gate only if that original card's falsifier is triggered; otherwise register a disagreement between the protocol window and the card window. An average score may not conceal it, and this protocol may not silently override the ledger;
5. Every `VETO` can name which gate triggered it.

The order is irreversible:

1. Freeze the protocol version, the candidate pool, the split, the as-of packets, and the hashes;
2. Submit all identification probes and gate-judging results;
3. Submit all baseline results;
4. Only then does the outcome adjudicator open the reveal sources and submit the coding, `outcome_date`, and evidence anchors;
5. The disagreement / unlocking arbiter handles disputes under the frozen fields and, after outcome coding is frozen, verifies whether a pre-written unlocking condition occurred before S;
6. Compute the results and permanently retire this batch of the holdout set.

If a question is found to be defective midway, the whole case is void but still retires. After the reveal, answers may not be amended, cut-offs may not be swapped, hard cases may not be deleted, and nothing may be re-run into a "new holdout set".

## 10. Rule revision, holdout consumption, and version discipline

- First-round rules may be developed only on calibration; the first holdout batch may not be drawn until the rule text, the output tables, the baselines, and the scoring are all frozen.
- After calibration exposes a failure, the rules may be revised; every change records "old rule → failing case → new rule → the judgments and prose affected".
- **Any** change to gate wording, layer membership, outcome thresholds, baselines, or scoring rules invalidates every already-revealed holdout for the new version. The new version must draw a new holdout from the never-read reserve pool.
- The number of reserve entries per domain must be at least equal to the number already used; the as-of packets of reserve entries are neither prepared nor read before they are activated.
- If three consecutive holdout batches with **enough information to test the claim** still fail the incremental conditions in section 9, one must write "the historical material has not shown that this set of gates has relative incremental discrimination" and suspend further consumption of cases; from then on, genuine out-of-sample evidence accumulates only through future due-date cards. A batch that is not computable solely because of sample size, abstention, S=0, or an empty `PASS` / `VETO` group does not count toward the three; first enlarge the never-revealed candidate and reserve pools, then run a new batch.

## 11. Directly reusable execution checklists

### A. Extending historical cases and running one round of validation

- [ ] Write down the protocol version and the commit of the five-gate text; confirm whether the rules have changed since last time.
- [ ] The candidate-pool author first freezes the registries, coverage years, and inclusion / exclusion rules, and only then draws entries.
- [ ] Fill in every section 2 field; do not open `reveal_source`.
- [ ] After the manifest is committed, an independent assignment operator who cannot see outcomes generates and commits a one-shot random salt; use it to split per section 3, submit the computed keys, and record the B0 base rate.
- [ ] Before assignment, check that every stratum is even and the full pool is ≥48; after assignment, check holdout capacity only, without looking at outcomes.
- [ ] Prepare as-of packets of uniform length and field order; verify that every item is no later than T, and record the hash.
- [ ] Generate a gate-judging handbook containing no historical example whatsoever, and re-check it line by line.
- [ ] The gate judge submits the identification probe for each case first, then fills in the five gates and the unlocking conditions; all results are submitted at once.
- [ ] Run B1–B3 on the same model, the same input, and independent contexts, and submit.
- [ ] Only then does the outcome adjudicator open the pre-registered sources, code against the frozen denominator and observation window, record `outcome_date`, and cite evidence.
- [ ] Arbitrate disputes; anything that cannot be decided from the frozen fields is recorded as U — the question may not be patched. Only after outcome coding is frozen does the unlocking arbiter receive logged, read-only access to reveal sources, citing evidence for whether each pre-written condition occurred before S.
- [ ] Publish the raw counts, coverage, `ΔD`, identification strata, the intermediate-outcome / undetermined bounds, fatal false vetoes, and the asymmetric loss.
- [ ] If a fatal false veto appears, adjudicate it against the corresponding J-066–J-071 card's own falsifier; this protocol may not silently override the ledger.
- [ ] Draw the conclusion in the exact words of section 9; if the conditions are not met, distinguish "insufficient information" from "enough information, but no relative incremental discrimination established".
- [ ] Retire the whole holdout batch and update the reserve-pool balance and protocol gaps; feed substantive results back into the ledger review log, affected card status / confidence history, and prose that relies on the rule.

### B. Full re-review of predictions after a rule change

**Precondition: an independent reviewer must be runnable and able to receive the de-labelled packet.** In this protocol, “started” is an evidence term: it may be used only when all four items are verifiable together—the de-labelled bundle, independent reviewer raw output, input hash, and run timestamp. If the reviewer service is unavailable, its independent execution cannot be demonstrated, or any of those items cannot be retained, record only “no verifiable evidence that the re-review has started (do not claim that it has started)” and the blocking reason. Do not treat the protocol text, a structure check, or local self-reading as a re-review result; do not add future judgment cards, opportunity candidates, or accuracy claims.

- [ ] Freeze the **complete set** of cards to be reviewed and its bilingual baseline; drawing only suspicious-looking cards is forbidden. Record the manifest, inclusion / exclusion rules, generation time, commit SHA, hashes, and card count first.
- [ ] Produce a de-labelled packet: delete `J-NNN`, status, confidence, the original diffusion-gate review, the `REVISED` reason, source back-references, and the dependency graph; keep the judgment itself, its necessary preconditions, the time window, and the audience definition.
- [ ] Use the bundle's frozen commit SHA for a deterministic shuffle and renumber to `R-NN`; store the mapping separately and keep it from the re-reviewer.
- [ ] Confirm that the independent reviewer is runnable; the re-reviewer has no repository access, judges item by item whether the original judgment was recognized first, then judges under the new rules, retaining the raw reviewer output, model / version, input hash, and run timestamp.
- [ ] Submit the re-review results first, then unseal the `R-NN → J-NNN` mapping.
- [ ] For each card, record one of **retain / revise / falsify / downgrade / archive**, with evidence anchors, the reason, the new status, confidence, and the corresponding Chinese and English files.
- [ ] Register each item as consistent / inconsistent / cannot be determined; count the identification layers separately — a higher consistency rate among recognized items can only be read as leakage.
- [ ] Every inconsistency must flow back in place: amend the card, amend the prose, downgrade, or record an explicit disagreement; writing only a side report is not allowed. If archived, preserve the original card, the archive reason, and links to the replacement card or prose.
- [ ] If the re-review changes the rules again, return to section 10: old holdouts cannot validate the new version, and a new holdout must be drawn.

## 12. Mandatory statement about results

Every time a historical-validation result is reported, the following must be preserved in meaning exactly as written, in Chinese and English alike:

> This result is a **relative incremental discrimination** obtained under **shared leakage**: the gate-judging arm and the baseline arms use models of common origin, and the model's training data may contain the historical cases, their outcomes, the relevant theory, even this repository. Identification probes and fresh contexts can measure or isolate only part of this round's leakage; they cannot eliminate training memory. These numbers are therefore **not** genuine out-of-sample accuracy, and no hit rate for future judgments can be inferred from them. Genuine out-of-sample calibration comes only from future judgment cards that have come due.

Forbidden formulations:

- "Historical backtesting proves an accuracy of X%";
- "It passed a blind test, so the method is validated";
- Writing calibration's retrospective consistency up as a hit rate;
- Claiming "no leakage" after deleting the cases that were recognized;
- Reporting veto precision only, without coverage, the pass set, and the baselines.

Permitted conclusion template:

> Under the frozen as-of conditions of `[case_id list]`, the discrimination gap of the five gates against the strongest same-input baseline is `ΔD = …`, with non-abstained `N = …`; raw counts and identification strata are in …. This comparison shares the leakage caused by model memory, and its absolute level cannot be interpreted.
