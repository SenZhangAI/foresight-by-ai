# How Judgments Change: Rules, Scope, and the Re-review Promise

> This page records the **evolution of the judgment system**, not a new round of forecasting. It separates committed rule changes, card-status changes, and re-reviews that have not yet happened. `REVISED` does not mean confidence fell; `CALIBRATION` does not mean a forecast hit. A real `HIT` or `FALSIFIED` result can be recorded only after a card’s own review window has arrived.

## Read this first

As of the commits linked on this page, the repository has undergone three different kinds of change:

1. **Rule changes**: five diffusion gates were derived from historical material, and the second calibration round narrowed Gate 5 from “does any gross friction exist?” to “what is the recurring net burden relative to the incumbent?” That changes how later judgments are assessed; it cannot turn an old result into evidence for the new rule.
2. **Scope and status changes**: the 2026-09-20 Gate 1 review, within the 72-card corpus then in existence, narrowed the society-wide voice of 60 formerly `ACTIVE` cards to occupational or organizational scope. J-004, already `REVISED` for another reason, also received a Gate 1 field, so that historical snapshot contained 61 cards carrying a Gate 1 narrowing note. This is not the same calibration set: the 60 scope-downgraded cards continue independently into due review and the calibration denominator generated from preregistered windows; J-004 is a named-supersession case, is not counted as a separate result, and is reviewed together with J-065. The other 61-card set in ledger §5 is the scope-downgraded set, which includes J-071 but excludes J-004; the two 61s must not be conflated. J-071’s v1 snapshot remains an independent rule version in calibration; the narrowed v2 candidate does not enter holdout before the isolated re-review.
3. **A re-review obligation**: after Gate 5 changed on 2026-09-21, the v1 card-by-card review became invalid for v2. Protocol §11.B requires a complete de-labelled, deterministically shuffled, isolated re-review. It has been **triggered but not run**; it must not be described as completed, a hit, or a falsification.

## Evolution table

| Category | Former rule / event | New rule or current interpretation | Affected judgments | Real commit anchor |
|---|---|---|---|---|
| Historical diffusion gates introduced | The nine L1–L9 lenses had no independent filter for whether a claim could become a society-wide trend | Added Gate 1 scale, Gate 2 substitution, Gate 3 carrier, Gate 4 decision rights, and Gate 5 recurring cost; necessary conditions, not sufficient conditions | New J-066–J-072; J-001–J-065 had not yet been reviewed against the gates | `2f8f54f` |
| Gate 5 exclusive-case correction | Dvorak keyboard was used as the exclusive failure case for “recurring cost” | Independent review found that Dvorak’s main cost was one-time learning, while “other people’s machines use it” belonged to Gate 4; contact lenses replaced it, and J-071 was narrowed from an “enthusiast ceiling” to a measurable ceiling below the population served | J-071; Retrospect §§5, 8, 10 and EXT-39/40 | `99b754d` |
| Full Gate 1 scope review | Cards could use society-wide language without a per-card audience and activity-frequency boundary | All 72 cards received audience scale, frequency, and a Gate 1 result; 60 formerly `ACTIVE` cards became `REVISED` with original prose retained; J-004, already revised for another reason, received only the new field; 61 cards now carry a Gate 1 narrowing note | 60 newly revised cards (the full-set commit is `a0789ea`); J-004 was an earlier status change; J-066–J-072 are rule cards and were not downgraded by this pass | `a0789ea` |
| Status separated from calibration denominator | `REVISED` could be mistaken for “no longer reviewed,” or J-004 → J-065 for two independent outcomes | Due reviews are generated from preregistered windows, falsifiers, and review dates; the 60 scope-downgraded `REVISED` cards remain in the calibration denominator; the named J-004/J-065 succession is counted once; uncomputable cases remain `INDETERMINATE` rather than being removed | All scope-downgraded `REVISED` cards, especially J-004 (superseded, not counted separately) and J-065 | `4a111a0`, `0938b07` |
| Second historical calibration: Gate 5 narrowed | Gate 5 treated “doing one more thing every time” as a proxy for burden, which could misclassify successful self-service retail | Compare the whole-system recurring net burden with the real incumbent: added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost; this is a holdout-test candidate, not a validated law | J-071; Retrospect §10; v2 protocol input table; later Gate 5 review of existing cards | `9e28494`, `0e1485d` |
| Second-round boundary correction | Stadia and year-round DST could have been described as “all five gates passed, yet failure” | Stadia shows that technology and a carrier are insufficient; year-round DST exposed net burden only during operation and is `ABSTAIN` at T; neither is a qualified sufficiency counterexample | J-066; Retrospect §10 and the bilingual card | `9e28494` |

## How the second calibration round flowed back

The second round was not “a historical accuracy percentage.” It calibrated the rule. The complete chain is:

| Old rule | Case exposing the boundary | New Gate 5 rule | Affected judgment / prose | Real commit anchor |
|---|---|---|---|---|
| Repeated bodily, learning, or operating friction could count as recurring cost | Piggly Wiggly self-service retail: shoppers repeatedly selected, compared, and picked goods, yet by 1948 complete self-service covered 56% of U.S. chain grocers (39% of independents, EXT-65) | Do not use gross friction; ask whether recurring net burden relative to the real incumbent is positive and material | J-071; Gate 5, exclusivity discussion, and second-round table in `01-retrospect.md`; protocol §10 rule version and §11.B re-review inputs | `9e28494` |
| Dvorak could serve as Gate 5’s exclusive failure case | Independent review found its main cost was one-time learning; “other people’s machines use QWERTY” was a Gate 4 coordination/carrier issue | Gate 5 must own an exclusive mechanism; contact lenses became the failure-side case, with “replacement rather than addition” explicitly retained as a weakness | J-071; Retrospect §§5, 8, 10 | `99b754d` |
| “All five gates passed, yet failure” could be supported by Stadia and year-round DST | Stadia failed at demand/adoption rather than proving all five passed; year-round DST had not exposed its operating burden at the decision point | Preserve J-066’s necessary-not-sufficient boundary, but do not call either case a qualified sufficiency counterexample; undecidable cases are `ABSTAIN` | J-066; Retrospect §10; v1 evidence denominator remains, without pretending it is a v2 result | `9e28494` |

The honest current claim is therefore narrower: the second round made Gate 5 **more specific and more attackable**; it did not prove Gate 5’s ability to forecast future adoption. Piggly Wiggly is calibration. The future holdout must still run under the frozen protocol; historical material has not produced a genuine future hit rate.

## J-043: status changed, confidence did not

J-043’s history can be checked directly against the committed trees:

| Date / commit | Confidence | What changed | Was this a confidence change? |
|---|---|---|---|
| 2026-09-18, `4be031e` | Low (landscape only) | First proposed that high-value agent execution might shift from stepwise approval to boundary authorization; time window 2033–2040 | No; this was the initial value |
| 2026-09-18, `846ea78` | Low (landscape only) | In the first external-comparison snapshot, J-043 gained “may,” the evidence boundary, and the reason to retain the landscape; the ledger review log records the round rather than attributing these changes to the earlier first registration | No; wording and comparison-state change. The anchor identifies the `846ea78` tree containing J-043’s first comparison snapshot; the commit message covers the J-001–J-054 comparison round |
| 2026-09-20, `a0789ea` | Low (landscape only) | Gate 1 narrowed the audience from language that could be read as society-wide to tens-of-millions of organizational buyers and operators, and marked the card `REVISED` | No; scope/status change, with no confidence-field change |
| Current ledger: J-043 in `docs/en/90-ledger.md` | Low (landscape only) | The card still retains its time window, falsifier, leading indicators, and evidence-insufficient landscape note; its status is `REVISED` | **No**. `REVISED` is not another confidence downgrade |

This distinction matters: J-043 has had no real due-date review, so no `HIT` or `FALSIFIED` result can be recorded. Nor is there evidence for turning the external comparison or Gate 1 failure into a numerical confidence change.

## The re-review already triggered by Gate 5

The 2026-09-21 narrowing of J-071 changed the Gate 5 rule. Under [Historical Pseudo-Out-of-Sample Validation Protocol §11.B](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change), the promised actions are:

1. Freeze the complete affected-card set rather than selecting cards that look suspicious;
2. Delete `J-NNN`, status, confidence, the old gate review, the `REVISED` reason, source back-references, and the dependency graph; retain the judgment, prerequisites, time window, and audience definition;
3. Use the frozen commit SHA for a deterministic shuffle into `R-NN`, so the reviewer cannot see the mapping;
4. Submit the isolated review before unsealing the mapping, then flow every inconsistency back into the card and prose in place.

Execution is owned by **`wu-c97b8976-7eb7-4f53-b2af-6af99dcac803` (full isolated re-review of existing predictions after methodology stabilization)**. As of this page’s record, it has not delivered completion. The 2026-09-20 v1 review therefore remains a historical record of v1 semantics only; it cannot be cited as a result under the current v2 rule.

## Do not conflate these terms

- **Scope change**: for example, narrowing “society-wide” to “occupational/organizational,” or changing Gate 5 from gross friction to net burden.
- **Status change**: for example, changing `ACTIVE` to `REVISED`, meaning the public scope or applicability note changed.
- **Confidence change**: requires explicit before/after values, date, reason, and evidence; J-043 has no such change at present.
- **Due-date result**: only after a card’s own review window arrives and its preregistered conditions are checked may the ledger say `HIT`, `FALSIFIED`, or `INDETERMINATE`.

This page adds no new forecast and does not present the unrun re-review as a result. Its purpose is to let readers follow real commits: when a rule was proposed, which case forced it to narrow, which cards changed only in scope, and what remains owed.
