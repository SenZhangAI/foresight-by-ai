# Lens-absence declaration attack record (2026-10-10)

[中文版](lens-absence-attack-2026-10-10.md)

This project's [methodology](../en/00-method.md) §2 defines exactly nine lenses, L1–L9, and uses a mapping table (lines 161–165) to map the five §1 classes of legitimate starting-point clauses onto those lenses; after the table comes an entry-point gap register (from line 171; items on lines 173–181). The eleven reasoning chains C1–C11 declare at their head which lenses they use, which are "not used", and why; ledger cards declare lenses in their lens field. The repository is therefore full of self-critical sentences: "X is carried by no lens in L1–L9", "only partly carried", "this chain does not use L_n because…", "not a lens". These sentences are what sets the project apart from an ordinary trend report, but until they are attacked they are only rhetoric — a two-sample spot check on 2026-10-09 had already overturned one of the two (commit `da42125`: "institutional substitution" downgraded from "no carrier" to "only partly carried"). On 2026-10-10 every such declaration was first frozen by position and then attacked one by one. **Result: 97 verdicts — 43 hold, 32 withdrawn, 22 partly carried.** Of the 49 lens codes in the eleven chains' "not used" lists, only 16 still hold after a reverse attempt; of the 9 delegation sentences ("carried by chain X"), 7 were withdrawn and 2 narrowed.

> **What this file proves and what it does not.** It proves that every frozen absence declaration received one of three verdicts, with evidence that can be checked in the repository, and that every "holds" verdict comes with a reverse attempt rather than a single zero-hit search. It does **not** prove the attack was exhaustive: "holds" only means the reviewers tried hard to refute the declaration within the nine definitions and found no carrying lens, not that none will ever be found. It also **changes no rule**: none of the confirmed gaps is patched in this round — under methodology §1.3, adding or widening a lens is a substantive rule change and must first be calibrated against historical cases.

---

## 1. Method

**Freeze first, then judge.** Before any verdict, every absence declaration was listed by position (file + which declaration): the "gap and consequence" column of the mapping table, each item of the entry-point gap register, the "not used" lists and registered gaps at the head of all eleven chains, and the "no carrier", "only partly carried" and "not a lens" entries in ledger cards' lens fields. New problems found while judging (for example, three gaps that had never been registered) were registered separately; the frozen list itself was not altered.

**Attack passes.** Twelve independent attack passes, one mechanical cross-check (see section 5), and a per-chain re-check: every anchor cited in each chain's re-judgement paragraph — card number, section number, quotation — was checked against the source text again.

**Exactly three verdicts; no "out of scope" bucket.**

- **Holds**: the declaration is still true after the attack. A "holds" verdict must carry a reverse attempt — name the lens that looks most like a carrier (or the step in the body that looks most like that lens) and say why it does not carry. "The word does not appear in the definitions" is never enough.
- **Withdrawn**: an over-claim. For a "not used" list, the chain's own body or its own ledger cards do use the lens; for "no carrier", some lens does carry it; for a delegation sentence, the chain it points to does not carry it.
- **Partly carried**: for a "not used" list, the chain uses one face of the lens and not another (each chain head states which face is unused); for "no carrier", some lens carries one face of it; for a delegation sentence, the delegation holds only in part and has been narrowed.

**Unit of judgement.** In the tables below, one row is one lens code or one claim. The tree is authoritative; line numbers are those at the time of writing and are identical in the Chinese and English files. Changes to the chains landed in batches: C3 in `ce99d48`, C11 in `99eb2ca` (with one error corrected in `6e1d63c`, see section 5), and the first batch of re-judgements for the other chains in `7582110`.

## 2. Root cause

The mapping table defines "gap" precisely: **an item of a §1 starting-point clause that no sentence in L1–L9 carries** (methodology line 155). The entry-point gap register (line 171) also states that what it registers — a prose concept borrowed by a chain or card that no lens carries — is not the same predicate as the table's gap.

But the label "carried by no lens in L1–L9" came loose from that definition and was reused as a blanket denial on arbitrary prose concepts — demography, agency institutions, infrastructure order, widening of regional difference, task decomposition, distribution of gains — without searching the nine definitions paragraph by paragraph. The chains' "not used" lists are another form of the same failure: most denials were a single line, "this chain does not touch it" or "carried by chain X", without naming the step in the body that looks most like the lens. As a result, the denied lens was often written in the lens field of the chain's own ledger cards, or sat in a load-bearing step of the body.

Delegation sentences failed most consistently. C1 assigned L3 and three other lenses to C2, C3 and C10 to "carry separately", while each of those three chains denied L3 at its own head at the time. C4 pointed care-setting L9 to C9 and C11, C9 pointed L9 to C11, and C11's body never mentions care at all — the face that actually carries it is C4's own section 12.2 and card J-100, so the pointer went round in a circle back to where it started.

The tally in section 4 fits this root cause: of the 7 gap verdicts the mapping table states against its own clause-based definition, 6 hold, and the only withdrawn one is precisely an over-statement of "no §1 source sentence"; whereas of the 49 codes in the chains' "not used" lists only 16 hold, and none of the 9 delegation sentences holds in full.

## 3. Verdicts

### 3.1 Methodology §2 mapping table and entry-point gap register

File: [methodology](../en/00-method.md). Mapping table lines 161–165; entry-point gap register from line 171.

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 161 · supply/demand row | L3 is only an extension; no §1 clause contains its source sentence | Holds | "Coordination", "transaction", "boundary", "organization", "outsourcing", "employment": zero verbatim hits in the five §1 clauses | Attack verdict added |
| Line 162 · human-nature row | "Loss aversion" is carried by no lens | Holds | Zero hits for "aversion" in the nine definitions. Reverse attempt: L6 gives objective loss and L8 gives paying extra for certainty; neither yields "a visible loss weighs more than an invisible gain" | Verdict added; the drifted "line 119" pointer replaced by a section name |
| Line 163 · history row | "First creates disorder" is carried by no lens | Holds | Reverse attempt on L2: it carries only the positive face of disorder (L2: “Use this to look for new roles, categories, and risks”), while the faces this cell denies — who is thrown out, skill devaluation, distributional conflict — are all negative. Reverse attempt on L5: it devalues signals, not skills | Verdict added |
| Line 164 · technology row | The first half, "which work gets cheaper first", is carried by no lens | Holds | Lens-by-lens reverse attempts: L1 takes cheapening as given; L3 expressly expels technical capability from its criterion (L3: “not by technical capability alone”); L4 presupposes "can be done" and governs only adoption speed; L6 gives only the second half, and negating it does not yield the first half's ordering | Verdict added; C4's head-level statement of the same gap was narrowed separately (see 3.5) |
| Line 165 · social row | Norm formation has no source sentence in any §1 clause | Withdrawn | The second half of the history clause, "then new institutions and divisions of labor", is its source sentence — the history row gives L7 "verbatim" on exactly that half. What it lacks is a source in the social clause, not in §1 | Rewritten as "no source in the social clause; reachable only via the history clause" |
| Line 165 · social row | Who decides and multi-party coordination (Gate 4) have no source sentence in any §1 clause | Holds | Clause-by-clause check of all five §1 clauses: none addresses who has the right to decide or how multiple parties coordinate; Gate 4 is a diffusion gate, not a lens | Verdict added |
| Line 165 · social row | Mandatory adoption has no source sentence in any §1 clause | Holds | Clause-by-clause check of all five §1 clauses: no matching sentence | Verdict added |
| Line 173 · demography | Carried by no lens in L1–L9 | Holds | §2.1 is an example of not using L1: it registers a legitimate starting point, not a tenth lens; none of the nine definitions has a population variable | Verdict added |
| Line 174 · institutional substitution | Only partly carried (downgraded from "no carrier" on 2026-10-09) | Holds | The face of who carries the work is load-bearing on L3 (applying it to households is an extrapolation; the verbatim source of that question is §2.1); "institutions substituting for the existing carrier" itself has no source sentence; L7 takes only the "institutions arrive later" end | Downgraded wording kept |
| Line 175 · agency institutions | Carried by no lens in L1–L9 | Holds | Reverse attempts: L3's "employment relationships" criterion is cost, not the allocation of power; L8's "accountability" is a demand-side anchor, not who has the right to decide; what actually carries it is Gate 4, and a gate is not a lens | Verdict added |
| Line 175 · former merged item | "Agency institutions and power boundaries" as a whole have no carrier | Withdrawn | Power and relationship boundaries are partly carried by L7 and L9 — the lens field of [J-098](../en/ledger/96-102.md) itself says so | Merge withdrawn; only "agency institutions" stays uncarried |
| Line 176 · task decomposability | Carried by no lens in L1–L9 (as used by C9 and J-097) | Holds | Which segment of a task gets cheaper first is exactly the technology row's hardest gap | Verdict added; J-099's same-named claim judged separately (see 3.13) |
| Line 177 · infrastructure order | No carrier; filed under the technology-row gap | Holds | No sentence in the nine definitions carries it; but the technology-row gap holds only "which work gets cheaper first" and cannot hold "which infrastructure is in place first" | No-carrier verdict kept; re-filed as its own item |

**Three items registered in this round (each verdict is counted on its source row, not again here)**: the absolute date at which a class of work reaches a contractable cost (line 178, source C4, see 3.5); widening of regional difference (line 179, source J-101, see 3.13); geography — several nodes sharing one regional exposure (line 180, sources C8 and J-092, see 3.9). The verdict on line 181, "distribution of gains", is counted on the J-102 row (partly carried, see 3.13).

### 3.2 C1 · Generation becomes free

File: [C1](../en/chains/10-generation-becomes-free.md). Declarations: line 59 (lenses in use but previously omitted), line 61 (not used), line 63 (reverse lookup of the base).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 59 · L3 | Not used (does not reason about organizational boundaries or outsourcing) | Partly carried | The skeleton node in which Exit B lowers the coordination cost of weak ties runs the mechanism L3: “Organizational boundaries are shaped by coordination costs and transaction costs”; but the boundary being moved is a personal weak-tie network, not an organization, so applying L3 here is an extrapolation (the same case as J-096 applying L3 to households) | Recorded as partly used; the company-size, employment, outsourcing and bundling face remains unused |
| Line 59 · L4 | Not used (does not reason about adoption speed or time windows) | Partly carried | Section 7's judgement of a 2–4 year window is a load-bearing time window; but the window comes from the opportunity-durability gate, not from L4: “Depreciation cycles, regulatory cycles, procurement cycles, and skill-formation cycles determine the speed of adoption” | Recorded as partly used |
| Line 59 · L5 | Not used (does not reason about where screening goes once credential forgery becomes cheap) | Withdrawn | Section 9's sentence that society falls back on older, more expensive credentials — guarantees, collateral, long-term relationships, identity — nearly restates L5: “guarantees, collateral, long-term relationships, accountable identities, or embodied presence” | Moved to in use |
| Line 59 · L7 | Not used (does not reason about rent windows before and after institutions settle) | Partly carried | Section 8's second opposing case and its withdrawal signal make institutions settling the signal for withdrawing J-065, i.e. L7: “once institutions settle, the rents may disappear”; the "when does it open?" face is unused | Recorded as partly used |
| Line 59 · L9 | Not used (L9 is likewise not in this chain) | Withdrawn | The lens field of this chain's card J-017 lists L8, L9 and L2, and its source field points back to this chain; the body, however, names none of L9's four asymmetries | Moved to in use (declared by the card) |
| Line 61 · delegation | The first four lenses (including L3) are "carried separately" by C2, C3 and C10 | Withdrawn | Each of the three chains pointed to denied L3 at the time; the chain that explicitly writes out L3's organizational-boundary face is C7 (section 2, item 3); C2 still declares L3 unused; of L4's four cycles, only C3 derives any in its body | Rewritten to name the real carrier lens by lens; the pointer to C2 withdrawn |

### 3.3 C2 · Real signals become contracts

File: [C2](../en/chains/20-real-signals-become-contracts.md). Declarations: line 50 (in use but previously omitted), line 52 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 52 · L3 | Not used | Holds | Reverse attempt: section 4 describes what the buyer buys as a constrained bundle of commitments, which resembles L3's product bundling; but the bundle is derived from the three high-liability conditions, not from L3: “Organizational boundaries are shaped by coordination costs and transaction costs”, and the chain never infers on which side of an organizational boundary the liability layer lands | Bare conclusion rewritten as a reverse attempt |
| Line 52 · L4 | Not used | Holds | Reverse attempt: J-034's approval in low-liability settings first is indeed an adoption order, but it is ordered by liability, not derived from L4's four cycles; the year 2030 is a scenario setting, and the page gives no step a time window | Rewritten as a reverse attempt |
| Line 50 · L7 | Not used (only touched in section 8) | Partly carried | Section 2's skeleton draws J-039 (data access rent) and J-034 as load-bearing boxes, and both cards' lens fields declare L7; used are L7: “Technology comes first; institutions arrive later” and the rent itself; unused is the time face — when the rent opens and closes | Recorded as partly used |
| Line 50 · L8 | Not used (does not touch human-nature anchors on the demand side) | Partly carried | Section 6 says an independent value layer exists only if buyers keep paying for traceability, liability and update obligations — exactly the L8 demand-side check that L1's definition requires; it uses the accountability and certainty anchors | Recorded as partly used |
| Line 52 · L9 | Not used | Holds | Reverse attempt: section 1's information asymmetry between buyer and seller about where data came from; but that is an information asymmetry between trading parties, which the chain screens with calibration records and compensation clauses (an L5 move), and buyer and seller do not form the model of L9: “People build a relationship model of any object with which they interact continuously” | Rewritten as a reverse attempt |
| Line 52 · base | The base contains no historical or human-nature clause | Withdrawn | L7 enters via J-034 and J-039 and brings in the second half of the history clause; L8's two anchors bring in the human-nature clause | Sentence withdrawn; both classes added to the reverse lookup |
| Line 50 · delegation | The L7 rent window is carried by C3 | Partly carried | This chain itself partly uses L7 through two cards; the delegation holds only for the "when does it open / close" face | Delegation narrowed |

### 3.4 C3 · Electrons on the ground

File: [C3](../en/chains/30-power-land-and-permits.md). Declarations: line 52 (in use but previously omitted), line 54 (not used). Landed in `ce99d48`.

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 52 · L1 | Not used (value shifts inside the chain are all stated with L2) | Partly carried | Section 4 says a site that is permitted, grid-connected and ready to build will be priced far above bare cheap land, by much more than construction cost — a complement valuation, not a bottleneck shift; what becomes abundant is indeed only imported from C1 and the technology chain | Recorded as partly used |
| Line 52 · L3 | Not used | Withdrawn | The lens fields of this chain's cards J-057, J-058, J-060 and J-062 declare L3 | Moved to in use |
| Line 52 · L5 | Not used | Withdrawn | The lens field of this chain's card J-059 declares L5 | Moved to in use |
| Line 52 · L6 | Not used | Withdrawn | The lens field of this chain's card J-061 declares L6 | Moved to in use |
| Line 54 · L9 | Not used (irrelevant to this chain's question) | Holds | Reverse attempt: section 7 (portability of inputs and control) and section 8 (visibility asymmetry) each reason about an asymmetry; but the two sides in each (input holders and host countries, local residents and outside shareholders) form no relationship model, and the landing point is bargaining power and local political reaction, not the form of a relationship | Over-broad wording rewritten as a reverse attempt |
| Line 54 · base | Contains no technology or social clause | Withdrawn | After re-judgement, L6 brings in the second half of the technology clause and L5 brings in the social clause | Sentence withdrawn |
| Line 54 · section 8 | Can only be written as landscape-only | Withdrawn | Section 8's main judgement, J-061, has medium confidence and is registered as measurable / pilotable now | Withdrawn |
| Line 54 · section 8 | Enters no gate | Withdrawn | Contradicts the page's own opening statement that J-056–J-064 all went through the Gate 1 diffusion review and were judged not to pass | Withdrawn |

### 3.5 C4 · Embodied intelligence

File: [C4](../en/chains/40-embodied-intelligence.md). Declarations: line 45 (overview), line 47 (in use but previously omitted), line 49 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 47 · L1 | Not used | Withdrawn | Section 12.4's heading says the scarce thing is not the robot itself but the bundle that lets it keep working; the lens fields of J-099, J-101 and J-102 declare L1 | Moved to in use |
| Line 47 · L3 | Not used (takes part in no step of this chain) | Withdrawn | Section 5's sentence that every deployment has to be negotiated with a specific owner, and that negotiation cost does not fall with model capability, hits both halves of L3: “Organizational boundaries are shaped by coordination costs and transaction costs, not by technical capability alone”; the lens fields of J-076 and J-077 declare L3 | Moved to in use |
| Line 47 · L5 | Not used | Partly carried | Sections 4 and 5 rank leading indicators by how costly they are to forge, i.e. L5: “A signal is effective because forging it remains expensive”; unused is the trigger face, a collapse in forging cost driving a shift in screening | Recorded as partly used |
| Line 47 · L7 | Not used | Partly carried | The lens fields of J-099, J-101 and J-102 declare L7; sections 4 and 11 use the "when does it open?" face (billing codes, pilot tariffs); no time window is given for when the complementary-asset rent disappears | Recorded as partly used |
| Line 47 · L9 | Not used | Partly carried | Section 12.2 derives that family members shift in part from hands-on doers to authorizers, coordinators, payers and exception deciders, and card J-100 declares L9; none of the four asymmetries is named | Recorded as partly used |
| Line 47 · delegation | The L7 rent window is carried by C3 | Withdrawn | The rents in C3's body are host-country rents traded for sites (section 7) and energy-access rent (section 13); neither concerns embodied deployment | Withdrawn |
| Line 47 · delegation | Care-setting L9 is carried by C9 and C11 | Withdrawn | C11's body never mentions care; the card that declares L9 for the care setting, J-100, comes from this chain | Withdrawn |
| Line 45 · technology-row gap | "Which work becomes cheaper first" as a whole has no carrier in L1–L9 | Partly carried | The slow side is carried by L6 (the second half of the technology clause) and the non-synchrony by L2; what has no carrier is only two things: the positive ordering of which work gets cheaper **first**, and the absolute date at which a class of work reaches a contractable cost | Narrowed; both now in the methodology's gap table and entry-point gap register |

Anchor corrections (not counted separately): J-100 does not declare L1; J-099 and J-101 do not declare L9 — all artifacts of reading the range "L1–L9" as codes (see section 5). The English file was also fixed in three places: L8's name, a stray clause near line 86 (aligned to the Chinese), and a broken sentence at line 47.

### 3.6 C5 · Biology and medicine

File: [C5](../en/chains/50-biology-medicine.md). Declarations: line 26 (in use but previously omitted), line 28 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 26 · L3 | Not used | Holds | Holds at the level of mechanism: card J-081's lens field says "cost structure" (L3's name), but its reasoning is about queueing for human-trial capacity, not organizational boundaries; the body's most L3-like step (Gate 4: in-institution closed loops with a single liable party diffuse first) rules on diffusion speed | Because the card names it, moved out of "not used" and recorded separately as "named on a card, mechanism not run" — not counted as in use; annotated in J-081's lens field |
| Line 28 · L5 | Not used | Holds | Reverse attempt: section 2's three hard constraints — physical, legal/liability and bodily presence — share vocabulary with L5's list of credentials; but bodily presence is scarce here because treatment must act on a real body, not because a previously effective signal became cheap to forge | Rewritten as a reverse attempt |
| Line 26 · L8 | Not used (appears only in J-080's opposing case) | Withdrawn | The long-term-care row of section 2's opportunity-durability table answers the gate question with "cannot remove the cost of bodily and relational presence" — a load-bearing cell running L8: “accountability, real relationships, and the sense of presence are anchors for checking the demand side” | Moved to in use (three anchors only) |
| Line 28 · L9 | Not used | Holds | Reverse attempt: L9 names doctors and patients, and section 2's long-term-care row lists trust; but the chain never asks which element is asymmetric, and its landing point is which link becomes scarce, not the form of a relationship | Rewritten as a reverse attempt |
| Line 28 · delegation | L5 is carried by C2 and C10 | Partly carried | Those two chains carry L5's general mechanism; neither reasons about medical credentials | Narrowed: the shift in screening after medical credentials become forgeable is currently carried by no chain |
| Line 28 · delegation | Doctor–patient L9 is carried by C11 | Withdrawn | C11 uses L9 only for the human–AI authorization relationship and nowhere reasons about doctor–patient relationships | Withdrawn |

### 3.7 C6 · Education and skill formation

File: [C6](../en/chains/60-education-skill-formation.md). Declarations: line 26 (in use but previously omitted), line 28 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 28 · L3 | Not used | Holds | Reverse attempt: J-084 judges that the set of functions schools carry will not be unbundled by AI tutoring, which resembles product bundling; but its derivation is that local closed loops diffuse more easily than rebuilding institutions — an adoption order (the card declares L4 and the diffusion gates) — and no step uses coordination or transaction cost to place an organizational boundary | Rewritten as a reverse attempt |
| Line 28 · L6 | Not used | Holds | Reverse attempt: section 2's point that AI cannot bear the practice time for the learner resembles L6; but learning mistakes are usually reversible and repeatable, and no step assumes a learning mistake cannot be undone | Rewritten as a reverse attempt |
| Line 26 · L9 | Not used (only previewed) | Partly carried | The one-line claim that everyone first gets a tireless explainer is exactly the asymmetry L9: “one side has infinite patience, never tires, and never judges”; the new norms, dependencies and harms growing from it are not derived | Recorded as partly used |
| Line 26 · delegation | L9 is carried by C11 | Withdrawn | C11 takes from L9 only copying, pausing and rollback in human–AI authorization; its body has nothing on teachers, students or patience | Withdrawn |

Also: in the Chinese file, "four classes" corrected to "five classes" (not counted separately).

### 3.8 C7 · Technology first, power later

File: [C7](../en/chains/70-capability-to-social-consequences.md). Declarations: line 30 (the fourth force, "technology"), line 33 (in use but previously omitted), line 35 (not used), line 37 (registered gaps).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 33 · L2 | Not used | Withdrawn | Section 4 says that cutting junior seats without rebuilding apprenticeship, simulation, rotation or supervised practice leads within a few years to a shortfall in succession and professional judgement — exactly L2: “the bottleneck jumps to another part”; the J-088 card that section cites names apprenticeship carriers as the new bottleneck in its title | Moved to in use |
| Line 33 · L5 | Not used | Partly carried | J-088's lens field says "signalling game", which J-085 in the same ledger file equates with L5; the screening face is used, the trigger face (a collapse in forging cost) is not | Recorded as partly used |
| Line 35 · L9 | Not used | Holds | Reverse attempt: the control-surface list in section 5 (who can pause, audit, revoke and appeal after a dispute) resembles L9's third asymmetry; but here pausing and revoking are controls an organization holds over an executor, derived from action rights and legal liability, landing in permission tables and audit logs | Reverse attempt added |
| Lines 30, 37 · technology-row gap | The fourth force, "technology", is carried by no lens in L1–L9 | Holds | As in 3.1, technology row: which work gets cheaper first has no carrying lens | Kept |
| Line 37 · multi-party coordination | "Multi-party coordination" has no source sentence in §1 | Holds | As in 3.1, social row | Kept |
| Line 37 · lens voice | This chain does not assert capability arrival order in a lens voice | Withdrawn | The lens field of this chain's card J-087 says "technology sequence" — a declaration in exactly that voice | Rewritten; J-087's field annotated as the technology-row gap, carried by no lens |

Also: the English file restores the wording "hardest gap in the table" (not counted separately).

### 3.9 C8 · The fab before the chip

File: [C8](../en/chains/80-fab-materials-and-climate.md). Declarations: line 57 (in use but previously omitted), line 59 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 57 · L3 | Not used (does not reason about organizational boundaries or outsourcing) | Partly carried | Section 5 and J-093 price siting and public support as a bundle of stable power, water quality/reuse, emissions capacity and climate adaptation — the product-bundling use L3 lists; company size, employment and outsourcing of manufacturing itself are indeed not reasoned about | Recorded as partly used |
| Line 57 · L5 | Not used (does not involve credential forgery) | Partly carried | Section 7 requires switchover drills that expose shared nodes rather than merely proving a paper process exists: nominal redundancy stops counting as a resilience credential, i.e. L5: “A signal is effective because forging it remains expensive”; the trigger — forging cost having just collapsed — is unused | Recorded as partly used |
| Line 57 · L8 | Not used (does not involve the demand side) | Partly carried | The body makes a demand-side change conditional on who bears the failure also changing, using L8's accountability anchor | Recorded as partly used |
| Line 59 · L9 | Not used (not involved) | Holds | Reverse attempt: section 8's asymmetry — costs and priorities fall locally while gains may go to the nation or to multinationals; but the two sides form no relationship model, and what is asymmetric is whose ledger the costs and gains land on | Reverse attempt added |
| Line 59 · hard constraints | "Physical and geographical constraints" are not a lens | Holds | None of the nine definitions contains them; but geography (several nodes jointly exposed to one regional shock) had no home: it is not a lens, and not one of methodology §3's five hard-constraint classes — §3's "physical" covers only moving mass, consuming energy, waiting time and bodily operation | Kept; geography registered as an entry-point gap; J-092's "geographical hard constraint" annotated in place |

### 3.10 C9 · Ageing and institutional care

File: [C9](../en/chains/90-aging-care-and-institutional-substitution.md). Declarations: line 23 (starting variable), line 33 (in use but previously omitted), line 35 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 33 · L1 | Not used (does not invent an abundance→scarcity reversal) | Withdrawn | The lens field of this chain's card J-096 declares L1 and L3 under supply and payment; section 5 is headed "scarcity reversal" and runs the whole reversal. Not starting from L1 still holds | Moved to in use (local use, not the starting point) |
| Line 33 · L2 | Not used | Withdrawn | Section 3's point that AI can reduce coordination friction but cannot create accountable positions is a bottleneck shift; the outputs that follow land on the first two items of L2: “Use this to look for new roles, categories, and risks” | Moved to in use |
| Line 33 · L5 | Not used | Partly carried | Section 5's scarce items are exactly long-term relationships, embodied presence and accountability from L5's list of credentials; unused is the engine, a collapse in forging cost | Recorded as partly used |
| Line 35 · L7 | Not used | Holds | Reverse attempt: section 2's Japanese long-term care insurance, where institutions do arrive late; but here institutions follow demography rather than technology, and the chain derives no rent window that opens or closes as institutions settle | Rewritten as a reverse attempt |
| Line 35 · L9 | Not used | Holds | Reverse attempt: J-096's family retaining authorization, companionship and exception decisions does involve AI entering the care relationship; but the chain names none of L9's four asymmetries | Rewritten as a reverse attempt |
| Line 35 · delegation | L9 is carried by C11 | Withdrawn | C11's body never mentions care; the reallocation of family roles actually sits in C4 section 12.2 and J-100 | Pointer redirected to C4 section 12.2 and J-100 |
| Line 23 · demography | The starting variable is not any lens | Holds | As in 3.1, demography | Kept |
| Line 35 · institutional substitution | Only partly carried | Holds | As in 3.1, institutional substitution | Kept |
| Line 35 · miscitation | Institutional substitution "is registered as a clause gap in the social-regularity row" | Withdrawn | The mapping table's social row registers who decides, multi-party coordination and mandatory adoption — not institutional substitution | Miscitation withdrawn |
| Line 35 · task decomposability | Carried by no lens in L1–L9 | Holds | As in 3.1, task decomposability | Kept |

Also: in the Chinese file a non-canonical name for the diffusion gates was replaced by the canonical one, here and in ledger card J-097 (line 34) (not counted separately).

### 3.11 C10 · Collateralization of trust

File: [C10](../en/chains/100-trust-collateralization.md). Declarations: line 59 (in use but previously omitted), line 61 (not used).

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 59 · L1 | Not used (enters only as an input from C1) | Withdrawn | The four-step reversal of methodology §3 runs in full in this chain's body: what becomes abundant, what becomes scarce, whether it can become abundant again, and classification — the last two steps with this chain's own material | Moved to in use |
| Line 59 · L3 | Not used (does not reason about re-drawing procurement organizations' boundaries) | Withdrawn | All four branches of the skeleton hang under the premise node that buyers add verification to lower attribution cost only when the cost of error is large enough; verification and attribution costs are transaction costs | Moved to in use |
| Line 59 · L4 | Not used | Partly carried | The body gives a tentative observation window of 2028–2035, but does not derive it from L4's four cycles | Recorded as partly used |
| Line 59 · L7 | Not used | Withdrawn | The body says regulation may directly set uniform compensation and audit standards, leaving no rent — i.e. L7: “once institutions settle, the rents may disappear” | Moved to in use |
| Line 61 · L9 | Not used (this chain explicitly does not touch it) | Holds | Reverse attempt: section 4's list of what still cannot be collateralized in the same way, including goodwill in intimate relationships, does touch relationships; but it only draws the outer edge of collateralization, names no asymmetry, and the trading parties are accountable legal persons | Bare announcement rewritten as a reverse attempt |
| Line 59 · delegation | L7 is carried by C11 | Withdrawn | This chain uses L7 itself | Withdrawn |
| Confidence note | No historical clause → no historical calibration → confidence capped at medium | Withdrawn | After re-judgement L4 and L7 bring in the history clause, so the inference's premise no longer holds | Cap kept; its reason is now "the body cites no historical case" |

### 3.12 C11 · Authority before intelligence

File: [C11](../en/chains/110-authority-before-intelligence.md). Declarations: line 24 (starting variable), line 31 (in use but previously omitted), line 33 (not used). The L3 and L1 re-judgements landed in `99eb2ca`.

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| Line 31 · L1 | Not used | Withdrawn | On the chain body alone: section 4 is headed "scarcity reversal" and runs L1's complement mechanism (card J-098 does not declare L1, see section 5) | Moved to in use; false reason corrected the same day |
| Line 33 · L2 | Not used | Holds | The chain deliberately does not start from "the model gets stronger first" and does not reason about a bottleneck moving | Kept |
| Line 31 · L3 | Not used | Withdrawn | The lens field of this chain's only card, J-098, declares organisational coordination (L3) | Moved to in use |
| Line 31 · L4 | Not used | Partly carried | J-098 gives a time window of 2027–2035, but not derived from L4's four cycles | Recorded as partly used |
| Line 33 · L5 | Not used | Holds | No step in the body assumes a collapse in forging cost; the shift in screening after credential forgery is carried by C2 and C10 | Kept |
| Line 24 · agency institutions | The starting variable, institutionalized agency, is carried by no lens in L1–L9 | Holds | Reverse attempts: L3's "employment relationships" criterion is cost, not power; L8's "accountability" is a demand-side anchor; what carries it is Gate 4, and a gate is not a lens | Kept |
| Line 24 · who decides | Who decides and multi-party coordination have no §1 source sentence | Holds | As in 3.1, social row | Kept |

Same-day corrections (not counted separately): the original re-judgement reason, "the same card declares L1", was false and has been corrected in place; the paragraph cited "section 10", "section 11" and "section 3" in a chain with six sections, now replaced by the actual locations; two quotations that do not exist in the chain were replaced or dropped; the reverse-lookup sentence now places L1 under supply/demand and lists L4 as partly used, together with L7, under historical regularity.

### 3.13 Ledger cards

| Location | Original claim | Verdict | Evidence | Change |
|---|---|---|---|---|
| [J-096](../en/ledger/96-102.md) line 12 · demography | Carried by no lens in L1–L9 | Holds | As in 3.1, demography | Kept |
| [J-096](../en/ledger/96-102.md) line 12 · institutional substitution | Only partly carried; the carrier boundary is load-bearing on L3 | Holds | As in 3.1, institutional substitution | Note added: the uses L3's definition lists stop at company size, employment, outsourcing and bundling, so applying it to households is an extrapolation; the verbatim source of that question is §2.1 |
| [J-097](../en/ledger/96-102.md) line 34 · task decomposability | No carrier; part of the technology-row gap "which work gets cheaper first" | Holds | As in 3.1, task decomposability | Kept |
| [J-098](../en/ledger/96-102.md) line 56 · agency institutions | No carrier; part of the social-row clause gap | Holds | As in 3.1, the agency-institutions reverse attempts | Kept |
| [J-099](../en/ledger/96-102.md) line 78 · task decomposition | Carried by no lens in L1–L9 | Partly carried | After the split, human time moves to exception handling, relationship maintenance and liability sign-off — a bottleneck shift carried by L2: “the bottleneck jumps to another part”; the uncarried face is which task segment gets cheaper first | Changed to only partly carried |
| [J-100](../en/ledger/96-102.md) line 100 · demography | No carrier | Holds | As in 3.1, demography | Kept |
| [J-100](../en/ledger/96-102.md) line 100 · institutional substitution | Only partly carried (as J-096) | Holds | As in 3.1, institutional substitution | Kept |
| [J-101](../en/ledger/96-102.md) line 122 · widening of regional difference | No carrier | Holds | L4 carries only the card's own point that adoption speed is set by the local carrying bundle, and L1 only the rise of complements; the self-reinforcement of learning effects in deployment and maintenance networks and further concentration of capital and talent is carried by no sentence in the nine definitions | Registered in the methodology's entry-point gap register |
| [J-101](../en/ledger/96-102.md) line 122 · infrastructure | No carrier; part of the technology row's infrastructure-order gap | Holds | No carrier holds; but the technology-row gap holds only "which work gets cheaper first" | Re-filed as its own item in the entry-point gap register |
| [J-102](../en/ledger/96-102.md) line 144 · distribution of gains | Has neither a lens nor a §1 clause criterion | Partly carried | Which asset class gains first is carried by L1: “This lens is good at locating value migration”, whose §1 source is the supply/demand clause; whether concentration lasts is carried by L7: “once institutions settle, the rents may disappear”; uncarried is how gains are then re-divided among asset owners, workers and public finance, and a falsifiable criterion for such claims | Changed to only partly carried; the uncarried part registered in §1.6; the card's "§1.5" pointer corrected to §1.6 |

In-place annotations (not absence declarations; not counted):

- [J-081](../en/ledger/81-90.md) line 13: the lens field's "cost structure" shares L3's name, but the reasoning is about capacity queueing and does not run L3's mechanism; it is not counted as L3 in a reverse lookup by code. The field itself is unchanged.
- [J-087](../en/ledger/81-90.md) line 151: the lens field's "technology sequence" annotated as the mapping table's technology-row gap, carried by no lens.
- [J-092](../en/ledger/91-95.md) line 36: the lens field's "geographical hard constraint" annotated — methodology §3's five hard-constraint classes have no "geography" class.

## 4. Tally

Every number below is counted from the rows of the tables in section 3.

| Group | Rows | Holds | Withdrawn | Partly carried |
|---|---|---|---|---|
| 3.1 Methodology mapping table and gap register | 13 | 11 | 2 | 0 |
| 3.2 C1 | 6 | 0 | 3 | 3 |
| 3.3 C2 | 7 | 3 | 1 | 3 |
| 3.4 C3 | 8 | 1 | 6 | 1 |
| 3.5 C4 | 8 | 0 | 4 | 4 |
| 3.6 C5 | 6 | 3 | 2 | 1 |
| 3.7 C6 | 4 | 2 | 1 | 1 |
| 3.8 C7 | 6 | 3 | 2 | 1 |
| 3.9 C8 | 5 | 2 | 0 | 3 |
| 3.10 C9 | 10 | 5 | 4 | 1 |
| 3.11 C10 | 7 | 1 | 5 | 1 |
| 3.12 C11 | 7 | 4 | 2 | 1 |
| 3.13 Ledger cards | 10 | 8 | 0 | 2 |
| **Total** | **97** | **43** | **32** | **22** |

The same 97 rows split by type of declaration:

| Type | Rows | Holds | Withdrawn | Partly carried |
|---|---|---|---|---|
| Lens codes in chains' "not used" lists | 49 | 16 | 16 | 17 |
| Delegation sentences in chain heads ("carried by chain X") | 9 | 0 | 7 | 2 |
| Other claims in chain heads (base, gaps, gates, miscitations, etc.) | 16 | 8 | 7 | 1 |
| Methodology mapping table and gap register | 13 | 11 | 2 | 0 |
| Ledger card lens fields | 10 | 8 | 0 | 2 |

Two notes. First, C5's L3 is counted as "holds" at the level of mechanism: L3 does not run in that chain; but because card J-081 uses L3's name, the chain head has moved it out of the "not used" list and explains it separately. Second, the high share of "holds" in the methodology's 13 rows and the ledger's 10 rows is partly repeat counting of the same concepts: of the ledger's 8 "holds" rows, 6 are demography, institutional substitution, agency institutions and task decomposability recurring on different cards, with the same verdict as the corresponding row in 3.1.

## 5. Lesson from the mechanical cross-check

Besides the item-by-item attack, this round ran one mechanical check: for each chain, intersect its head's "not used" list with the lens fields of every card whose source field points back to that chain; a non-empty intersection is a candidate contradiction.

**The first version read the range notation "L1–L9" as naming the codes L1 and L9** (many cards write "carried by no lens in L1–L9"), and so produced a batch of false contradictions: C11's L1 against J-098; C4's L1 against J-099, J-100, J-101 and J-102; C4's L9 against J-099 and J-101; C9's L1 and L9 against J-096 and J-097. One of them reached a public commit: the message of `99eb2ca` says J-098 "declares L1" — false; J-098's lens field declares only L3, L6, L7 and L9. The error has been corrected in place at C11 line 31 (with a same-day correction note) and corrected explicitly in the message of the later commit `6e1d63c`. C11's withdrawal of the L1 denial still stands, but its evidence is now the chain body alone (see 3.12); C4's anchors of the same kind have been corrected one by one (see 3.5).

**Fixed algorithm**: strip every "L1–L9" range token before intersecting. One hit remains after the fix: C9's "not used" list contains L7, while J-096's lens field says “L7 covers only the “institutions arrive late” end”. On a sentence-by-sentence reading this is a statement of coverage, not a declaration of use, and it is kept.

Lesson: a mechanical check finds contradictions the eye misses, but its own input parsing must be checked too; before a script-produced "piece of evidence" enters the public record, someone has to look at the source text.

## 6. Not fixed in this round

The following are confirmed still present and are left for later:

- [C1](../en/chains/10-generation-becomes-free.md) line 202 (both languages): still says the trust-collateralization direction is not yet a separate chain and takes no chain number, although [C10](../en/chains/100-trust-collateralization.md) exists.
- [J-005](../en/ledger/01-10.md) line 108: the lens field lists only L1 and L2 and lacks L5.
- [C7](../en/chains/70-capability-to-social-consequences.md) lines 27–31: the "five forces" parenthetical is inconsistent with the mapping table's reverse lookup; C7 line 37 itself says this is not yet revised.
- Chinese C7 lines 62, 92, 102 and 112: link texts for J-087, J-089, J-090 and J-091 are truncated.
- [J-095](../en/ledger/91-95.md) line 105: "collective action" in the lens field is not yet annotated in place.
- The Chinese ledger index (`docs/zh/90-ledger.md`) line 1203: still uses the non-canonical name for the diffusion gates.
- A mechanical check — the intersection of a chain's "not used" list with its own cards' lens fields (after stripping "L1–L9") must be empty — is proposed but not yet built into the repository's check script.
