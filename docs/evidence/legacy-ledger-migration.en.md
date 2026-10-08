# Legacy ledger migration: J-001–J-095 (English projection)

> **Projection notice.** This is the English projection of [`legacy-ledger-migration.md`](legacy-ledger-migration.md), the canonical bilingual audit inventory. It does not establish a second fact source: where wording or facts differ, the Chinese source controls.
>
> **Closed set:** J-001–J-095. Historical source: the pre-sharding Git snapshot `1f99c832be8cbc82631beb7679d82994a2b7e0fb^`; current cards are in `docs/{zh,en}/ledger/`. This projection is a card-by-card English historical migration audit, not a replacement for the ledgers.

## Scope and reading rules

- The historical snapshot `1f99c832be8cbc82631beb7679d82994a2b7e0fb^` contains 95 Chinese and 95 English cards; each card below retains its English file/line anchor.
- Each current J-001–J-095 shard links back to the bilingual inventory. Current-card evidence, narrowing, or status changes must not be back-projected into historical values.
- **Unknown / unverified boundary:** fields absent from the historical body remain unknown/unverified. The standalone Audience scale added to current cards is reconstructed only from that card’s existing Diffusion-gate review and is labelled as reconstructed; it is not presented as a historical field or independent statistic.
- Historical standalone Audience scale is 0/86. The historical schema kept scale inside the Diffusion-gate review, so the standalone field remains unknown rather than being invented.
- **Evidence level:** this inventory is a historical-card migration audit, not `CALIBRATION`, relative `holdout`, or genuine future out-of-sample evidence. For delivered historical cases, see the [political calibration packet](politics-calibration.md) and the [commercial forecast calibration packet](business-forecast-calibration-2026-09.md). Cases added after outcomes were known can calibrate rule boundaries only; genuine future out-of-sample evidence arises only when preregistered cards reach their due windows. This inventory does not back-project current-card outcomes into historical snapshots.
- **Canonical-source rule:** this projection preserves the English blocks and lineage metadata from the bilingual source. Consult the [Chinese canonical inventory](legacy-ledger-migration.md) for the controlling audit record and any bilingual context.

## Coverage summary

- Historical cards: 95 Chinese + 95 English; current paired cards: 95 Chinese + 95 English.
- Historical fields (proposed date, one-sentence judgment, Diffusion-gate review, lens, reasoning chain, time window, falsifier, leading indicator, confidence, depends-on, strongest counterargument, consensus, external comparison source, provenance, next check date, and status): 95/95 in both languages.
- Standalone Audience scale: historical J-001–J-086 is 0/86 in both languages (scale was inside the historical Diffusion-gate review); current J-001–J-095 paired cards are 95/95, with J-001–J-086 reconstructed from existing reviews and J-087–J-095 retaining their existing standalone field. Historical unknowns are not back-filled from current values.

## Per-card inventory

## J-001

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L5–L26`；`docs/en/ledger/01-10.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L520–L538`
- **Current card anchor**: `docs/en/ledger/01-10.md:L5–L26`
- **Original title**: Unit reasoning cost keeps falling
- **Original one-sentence judgment**: The unit cost of reasoning at equal capability falls another order of magnitude by the end of 2029.
- **Original reasoning chain**: Reasoning is parallelizable deterministic computation → cumulative production and engineering optimization create a learning curve → hardware efficiency, model efficiency, and scheduling/reuse provide relatively independent cost-decline paths → equal capability can be called more frequently.
- **Original time window**: 2026-01 to 2029-12.
- **Original falsifier**: For 18 consecutive months, the lowest public unit price for equal capability rises rather than falls, and the rise cannot be explained by temporary demand congestion or a one-off energy shock.
- **Original leading indicator**: Lowest public price for a fixed benchmark score, energy per unit of compute, and months for open models to catch the strongest closed model at the time; observe twice yearly.
- **Original confidence**: High.
- **Original depends-on**: —.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Directionally consistent, but the tenfold-by-2029 claim is unverified; sources support a decline channel, not the specific magnitude. Retained: the three decline channels (hardware efficiency, model efficiency, scheduling reuse) are relatively independent, and the sources simply do not measure the specific multiple rather than contradicting it; the magnitude risk is carried by the falsification condition on lowest public unit price.
- **Original external comparison source**: EXT-1 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-001` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-002

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L27–L49`；`docs/en/ledger/01-10.md:L27–L49`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L539–L558`
- **Current card anchor**: `docs/en/ledger/01-10.md:L27–L49`
- **Original title**: “Selecting objectively high quality from abundant output” is not a durable scarcity, but merely a 2–4 year window
- **Original one-sentence judgment**: Selecting objectively high quality from abundant output is not a durable scarcity; it is merely a 2–4 year window.
- **Original reasoning chain**: Objective quality is formalizable in most domains → anything formalizable can be checked automatically → generative models can sample and self-evaluate → selection is internalized as part of generation and is no longer an independent need
- **Original time window**: The window will be basically closed by the end of 2029
- **Original falsifier**: In 2030, a sizable independent market still exists whose core value is “picking the better one from AI output for the user,” and that market has not been internalized by model vendors
- **Original leading indicator**: Whether model vendors make “generate multiple options + automatically select the best” the default behavior; whether revenue from third-party “AI output quality assurance” products is expanding or being squeezed
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Retain with a different mechanism: objective selection may be partly internalized, while liability- and domain-sensitive QA may persist.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-002` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-003

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L50–L72`；`docs/en/ledger/01-10.md:L50–L72`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L559–L578`
- **Current card anchor**: `docs/en/ledger/01-10.md:L50–L72`
- **Original title**: The genuinely durable scarcity is ownership of “private context about you” and its usable form
- **Original one-sentence judgment**: The genuinely durable scarcity is ownership of private context about you and its usable form.
- **Original reasoning chain**: Objective quality can be automated, subjective fit cannot → the key input to subjective fit is an individual’s/organization’s history of choices → that input is private, unstructured, and impossible for the person to articulate → hard constraints (ownership + privacy) prevent the same force from acquiring it automatically
- **Original time window**: Demand becomes visible from 2027 and will not disappear before 2033
- **Original falsifier**: A method appears that can stably reproduce an individual’s/organization’s choice preferences using only a small amount of publicly available interaction (reaching over 80% approval by the person), making private history unnecessary
- **Original leading indicator**: ① Whether companies begin building dedicated assets for “our context / sensibility / boundaries” rather than leaving them scattered in prompts; ② whether individuals begin exporting and carrying their own preference profiles; ③ whether rejection reasons such as “this doesn’t feel like us” begin to be explicitly recorded
- **Original confidence**: Medium
- **Original depends-on**: J-001, J-002
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Retain with a narrower evidence boundary: sources support governance of private context, not that it must become durable scarcity.
- **Original external comparison source**: EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-003` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-004

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L73–L95`；`docs/en/ledger/01-10.md:L73–L95`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L579–L598`
- **Current card anchor**: `docs/en/ledger/01-10.md:L73–L95`
- **Original title**: As AI shifts from “generating content” to “executing actions,” the scarce item is infrastructure that “makes actions reversible”
- **Original one-sentence judgment**: As AI shifts from generating content to executing actions, the scarce item is infrastructure that makes actions reversible.
- **Original reasoning chain**: Generation becomes cheap → trial-and-error strategies spread → but trial and error presupposes reversible outcomes → AI begins touching irreversible actions (payments, deployment, sending, signing) → irreversibility exposes physical and legal/liability constraints that will not disappear as models improve → “reversibilization” becomes a prerequisite for using AI rather than an option
- **Original time window**: Demand becomes explicit from 2027 and becomes standard before 2032
- **Original falsifier**: By 2031, mainstream practice still lets AI directly execute irreversible actions in production environments/real accounts, and the incident rate is low enough that no one demands an isolation layer
- **Original leading indicator**: ① Whether enterprise procurement lists begin to include standalone items such as “AI action sandboxes / shadow environments / rollback”; ② whether insurers begin pricing “AI autonomous action”; ③ the public frequency of major AI execution incidents
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` — the opportunity-durability review of 2026-09-19 found that this card treated “reversible infrastructure” as a single scarce item without ever answering why the same force that makes generation abundant cannot copy it; it has been narrowed and superseded by `J-065`. Per the section-1 rule the card is kept verbatim, its ID is not reused, and it is no longer a basis for any opportunity candidate.
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Partly consistent: isolation, oversight, and recovery have support; scarcity and timing of reversible infrastructure remain unverified. Retained: irreversible actions trigger physical and legal/liability constraints that do not dissolve as models improve; the independent scarcity of reversible infrastructure is unconfirmed externally, so confidence stays Medium rather than rising.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-004` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.
- **出生攻击 / Boundary attack**：J-004 must retain the historical “reversible infrastructure” proposition. Replacing it with J-065’s “cross-party reversal right” while retaining only J-004 fails this ledger; both historical text and successor relation remain independently visible.
- **J-004 → J-065**：historical status explicitly records narrowing/supersession by J-065; current J-065 reasoning separately links back to J-004.

## J-005

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L96–L118`；`docs/en/ledger/01-10.md:L96–L118`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L618–L637`
- **Current card anchor**: `docs/en/ledger/01-10.md:L96–L118`
- **Original title**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality
- **Original one-sentence judgment**: After generation becomes abundant, value concentrates in three kinds of non-recombinable input: raw signals, accountable commitments, and validated causality.
- **Original reasoning chain**: Generation = recombination of existing patterns → what cannot be obtained through recombination will not become abundant → supply-and-demand law: what complements abundant goods without becoming abundant in parallel appreciates → the three kinds of input are respectively protected by the hard constraints of physical presence, legal liability, and experimental intervention
- **Original time window**: Clearly visible in pricing during 2029–2033
- **Original falsifier**: Reliable synthetic data/simulation-based reasoning systematically replaces real experiments in fields requiring new observations (such as new drugs and new materials), and regulators accept it
- **Original leading indicator**: ① Price trends for licensing first-party data (sensors, field sites, proprietary workflows); ② whether AI services with compensation commitments appear and command a premium; ③ the share of experiments and pilot production in R&D budgets
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Mechanistically consistent but should be limited to high-liability domains: traceable signals and real-world causal validation matter, without implying all three inputs broadly appreciate. Retained: the three input classes are protected by physical presence, legal liability, and interventional experiment, and cannot be produced by recombination; following the external evidence boundary, the claim is narrowed to high-liability domains rather than broad appreciation.
- **Original external comparison source**: EXT-7 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-005` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-006

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L119–L140`；`docs/en/ledger/01-10.md:L119–L140`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L658–L676`
- **Current card anchor**: `docs/en/ledger/01-10.md:L119–L140`
- **Original title**: Reasoning throughput precedes long-horizon autonomy
- **Original one-sentence judgment**: By 2028, the number of parallel reasoning paths affordable per task will rise substantially, making generate–compare–revise workflows common before long-horizon autonomous execution.
- **Original reasoning chain**: J-001 lowers unit cost → the same budget runs more candidate paths → a scheduler parallelizes simple steps and upgrades difficult ones → workflows shift from one answer to candidate search.
- **Original time window**: 2026–2028.
- **Original falsifier**: By the end of 2028, mainstream systems still support only one path per comparable task, and cost declines have not translated into parallel attempts.
- **Original leading indicator**: Per-task sample count, end-to-end latency, and quality curves for public systems; observe twice yearly.
- **Original confidence**: High.
- **Original depends-on**: J-001.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent but ordering is unproven: capability and throughput scaling before reliable long-horizon agents remains testable. Retained: parallel candidate search requires only falling unit cost and feasible scheduling, not external confirmation of ordering; the ordering risk is carried by the end-2028 falsification condition.
- **Original external comparison source**: EXT-1, EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-006` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-007

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L141–L162`；`docs/en/ledger/01-10.md:L141–L162`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L677–L695`
- **Current card anchor**: `docs/en/ledger/01-10.md:L141–L162`
- **Original title**: Resumable context precedes reliable long-term memory
- **Original one-sentence judgment**: From 2026 to 2029, task-level retrieval context will become a common base for multi-session collaboration before sourced, revisable long-term memory matures.
- **Original reasoning chain**: More parallel attempts create more state → one context window cannot hold the full history → tasks, evidence, and open questions must be retrieved → retrieval first solves “bring it back,” while provenance and versions solve “can it be trusted.”
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, mainstream long tasks still rely mainly on unstructured chat replay, and retrieval context produces no measurable continuation gain.
- **Original leading indicator**: Long-task recovery rate, retrieval hit rate, and the share of citations from outside the active context window; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent in direction but with a different mechanism: retrievable context is often combined with long windows, not proven to have a fixed industry order. Retained: “retrieve first, then establish trustworthiness” is a capability dependency that coexists with long windows; following the external boundary, the industry-ordering part is downgraded to a testable hypothesis.
- **Original external comparison source**: EXT-8 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-007` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-008

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L163–L184`；`docs/en/ledger/01-10.md:L163–L184`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L696–L714`
- **Current card anchor**: `docs/en/ledger/01-10.md:L163–L184`
- **Original title**: Sourced long-term memory becomes a prerequisite for reliable collaboration
- **Original one-sentence judgment**: From 2028 to 2031, long-term memory with sources, dates, and confidence boundaries will become necessary for high-value continuous collaboration rather than a chat-product extra.
- **Original reasoning chain**: Resumable context makes history retrievable → history contains stale and conflicting facts → events need sources, update times, and retraction relations → only revisable memory can support longer autonomous tasks.
- **Original time window**: 2028–2031.
- **Original falsifier**: By 2031, high-value continuous tasks using memory without provenance, versioning, or retraction maintain the same error rate and accountability as sourced memory.
- **Original leading indicator**: Enterprise requirements for memory provenance, timestamps, and retraction APIs; the share of incidents caused by bad memory; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain with a different mechanism: provenance, versioning, and revisability improve auditability, but are not proven necessary for every high-value collaboration.
- **Original external comparison source**: EXT-4, EXT-8 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-008` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-009

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L185–L206`；`docs/en/ledger/01-10.md:L185–L206`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L715–L733`
- **Current card anchor**: `docs/en/ledger/01-10.md:L185–L206`
- **Original title**: Continuous execution in constrained workflows matures first
- **Original one-sentence judgment**: From 2027 to 2030, constrained workflows with checkable inputs and outputs and limited permissions will achieve stable continuous execution before open-world autonomy matures.
- **Original reasoning chain**: Sourced memory reduces repeated errors → closed environments provide a limited state space → permissions and exits can be specified in advance → systems can complete multiple actions and stop at a known failure.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, open-world tasks have reliability indistinguishable from constrained workflows, and permission boundaries and stop conditions no longer affect deployment.
- **Original leading indicator**: Consecutive steps completed without intervention, constrained-environment success rate, and safe-stop rate after permission denial; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-008.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent with the consensus: constrained, checkable workflows mature before open-world autonomy; sources support the constraint transition, not a replacement of the original chain. Retained: the sources support the constraint transition itself, while constrained workflows stabilize first because their state space is bounded and permissions and stop conditions can be specified in advance — not a restatement of consensus.
- **Original external comparison source**: EXT-2, EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-009` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-010

**Current pair / 当前双语卡片**：`docs/zh/ledger/01-10.md:L207–L227`；`docs/en/ledger/01-10.md:L207–L227`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L734–L752`
- **Current card anchor**: `docs/en/ledger/01-10.md:L207–L227`
- **Original title**: Long-horizon autonomy follows constrained continuous execution
- **Original one-sentence judgment**: From 2029 to 2033, autonomous execution across longer horizons with fewer human confirmations will reach acceptable reliability in some high-value settings.
- **Original reasoning chain**: Constrained workflows accumulate state and failure data → long tasks expose more unanticipated states → the system must pause and request evidence under uncertainty → reliable long-horizon execution depends on environment observation and evaluation loops, not simply longer plans.
- **Original time window**: 2029–2033.
- **Original falsifier**: By 2033, long-horizon tasks still require step-by-step human confirmation, or their incident rate has not materially fallen from 2029.
- **Original leading indicator**: Average action span per authorization, proactive pause rate, human takeover rate, and irreversible incident rate; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent but the window is unverified: long-horizon capability is growing while reliable deployment remains horizon-limited. Retained: long-horizon reliability is bounded by environment observation and evaluation loops, which matches the external task-horizon curves; the window risk is carried by the 2033 falsification condition.
- **Original external comparison source**: EXT-3 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-010` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-011

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L28–L49`；`docs/en/ledger/11-20.md:L28–L49`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L753–L771`
- **Current card anchor**: `docs/en/ledger/11-20.md:L28–L49`
- **Original title**: Cross-media consistency precedes long-range coherence
- **Original one-sentence judgment**: From 2027 to 2030, local consistency of entities and formats across text, images, and audio will become reusable before causal coherence across long time spans.
- **Original reasoning chain**: More reasoning throughput → multiple media versions can be sampled for one task → shared representations and constraint checks solve local consistency first → long-range coherence still needs persistent state and repeated evaluation.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, causal, spatial, and action coherence in long interactive worlds is broadly stable while local cross-media consistency is not a default capability.
- **Original leading indicator**: Cross-media entity retention, shot or timbre continuity, and long-horizon state drift; observe quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain but with insufficient evidence: research supports long-range coherence difficulty, not that cross-media consistency must arrive first.
- **Original external comparison source**: EXT-5 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-011` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-012

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L50–L71`；`docs/en/ledger/11-20.md:L50–L71`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L772–L790`
- **Current card anchor**: `docs/en/ledger/11-20.md:L50–L71`
- **Original title**: Cross-time coherence depends on state and evaluation
- **Original one-sentence judgment**: From 2029 to 2034, cross-time coherence in long stories, persistent interactive environments, and multi-round design will reach production quality only after state memory and repeated evaluation mature.
- **Original reasoning chain**: Local cross-media consistency reduces frame-level errors → long tasks still accumulate drift in entities, space, and causality → sourced memory preserves state → automatic counterexamples and replay evaluation permit ongoing correction.
- **Original time window**: 2029–2034.
- **Original falsifier**: By 2034, production-grade long-generation neither depends on state tracking and replay evaluation nor has drift comparable to short segments.
- **Original leading indicator**: Long-generation state drift, replay reproducibility, and local-retention rate after cross-round edits; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-008, J-011.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Mechanistically consistent but the window is unverified: long-range coherence depends on state retention, spatiotemporal representation, and ongoing evaluation. Retained: long-range coherence depends on state retention and replay validation, which is the same difficulty the external review identifies; the window has no external support, so confidence stays Medium.
- **Original external comparison source**: EXT-5 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-012` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-013

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L72–L93`；`docs/en/ledger/11-20.md:L72–L93`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L791–L809`
- **Current card anchor**: `docs/en/ledger/11-20.md:L72–L93`
- **Original title**: Checkable tool calls precede open-environment action
- **Original one-sentence judgment**: From 2027 to 2030, tool calls with parameters, preconditions, permissions, and structured results will spread before systems expand into continuous action in complex environments.
- **Original reasoning chain**: Constrained continuous execution needs explicit boundaries → natural-language tool calls are hard to check → typed interfaces structure actions and results → structured calls first accumulate reliability on a few tools and then expand the tool surface.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, high-value tools broadly accept unstructured natural-language calls, with no error-rate difference from checkable interfaces.
- **Original leading indicator**: Tool-schema coverage, precondition rejection rate, parameter error rate, and replayable-result ratio; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Consistent with the consensus: structured, checkable tool calls are productized; the strict ordering remains this project’s judgment. Retained: the ordering follows from the checkability of structured interfaces, and productization evidence is consistent with it; the strict ordering is carried by the 2030 falsification condition.
- **Original external comparison source**: EXT-6 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-013` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-014

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L94–L115`；`docs/en/ledger/11-20.md:L94–L115`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L810–L828`
- **Current card anchor**: `docs/en/ledger/11-20.md:L94–L115`
- **Original title**: Rehearsable environments follow single-tool integration
- **Original one-sentence judgment**: From 2028 to 2032, environments combining snapshots, shadow execution, permission boundaries, and rollback points will arrive after single-tool integration but before high-value autonomous action becomes common.
- **Original reasoning chain**: Typed tools express one action → multiple actions share external state → real state cannot be freely trialed → isolation, snapshots, shadow execution, and rollback expand the safe attempt space.
- **Original time window**: 2028–2032.
- **Original falsifier**: By 2032, high-value autonomous action still writes directly to real environments, and isolation and rollback have not reduced incident cost or procurement barriers.
- **Original leading indicator**: Shadow-environment and rollback line items in AI-workflow procurement; recoverable-action ratio; autonomous-action insurance or liability pricing; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain only as an evidence-limited landscape: governance supports rehearsable, recoverable environments, not a market order or window.
- **Original external comparison source**: EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-014` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-015

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L116–L137`；`docs/en/ledger/11-20.md:L116–L137`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L829–L847`
- **Current card anchor**: `docs/en/ledger/11-20.md:L116–L137`
- **Original title**: Formal verification precedes open-world evaluation
- **Original one-sentence judgment**: From 2026 to 2029, tests, schemas, static checks, and counterexample search will be absorbed by generation systems before independent evaluation of real-world outcomes matures.
- **Original reasoning chain**: Parallel generation increases candidate count → formal properties can be judged quickly by programs → generate–test–discard loops lower output error → open-world outcomes still require waiting for observation and intervention and cannot be replaced immediately by self-evaluation.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, open-world outcome evaluation is broadly reliable while formal testing has not entered the default generation loop.
- **Original leading indicator**: Default-on automated-test ratio, counterexample-search coverage, schema-violation rate, and formal-verification impact on final adoption; observe quarterly.
- **Original confidence**: High.
- **Original depends-on**: J-006, J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Directionally consistent with a broader mechanism: executable tests generally precede open-world outcome evaluation, without proving universal default integration. Retained: formalizable properties can be decided immediately by programs while open-world outcomes must await observation, and that asymmetry is unchanged by the external material.
- **Original external comparison source**: EXT-2, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-015` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-016

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L138–L161`；`docs/en/ledger/11-20.md:L138–L161`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L848–L869`
- **Current card anchor**: `docs/en/ledger/11-20.md:L138–L161`
- **Original title**: Open-world evaluation is the final gate for expanding autonomy
- **Original one-sentence judgment**: From 2029 to 2035, independent observation, causal intervention, and continuous monitoring will become the final technical gate for widening the authorization of long-horizon autonomous action.
- **Original reasoning chain**: Formal verification covers only pre-specified properties → long tasks encounter unmodeled states and delayed side effects → external observation and intervention create independent evidence → continuous monitoring turns one-off tests into runtime feedback → authorization boundaries can expand incrementally.
- **Original time window**: 2029–2035.
- **Original falsifier**: By 2035, long-horizon autonomous systems reach open environments without independent observation, intervention, or continuous monitoring and still match constrained-environment incident rates.
- **Original leading indicator**: Share of external evidence in long tasks, causal-experiment trigger rate, runtime pause and rollback rate, and authorization expansion following evaluation results; observe twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-010, J-012, J-014, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Technology Capability Sequence`.
- **Original external comparison**: Retain only as an evidence-limited landscape: open-world feedback may constrain autonomous authority, but is not established as the final gate.
- **Original external comparison source**: EXT-3, EXT-4 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-016` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-017

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L5–L27`；`docs/en/ledger/11-20.md:L5–L27`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L638–L657`
- **Current card anchor**: `docs/en/ledger/11-20.md:L5–L27`
- **Original title**: AI mediation expands weak-tie coordination faster than strong relationships
- **Original one-sentence judgment**: From 2027 to 2033, AI mediation will expand weak-tie coordination faster than strong relationships, without expanding the number of relationships in which a person can remain present over time.
- **Original reasoning chain**: J-006 lowers the cost of multi-party coordination and information compression → J-007 makes shared context and history easier to resume → contact, translation, introductions, and scheduling for weak ties can scale → strong ties remain constrained by shared experience, mutual responsibility, conflict repair, and finite attention → more connections do not automatically become more commitments that people can rely on.
- **Original time window**: 2027–2033.
- **Original falsifier**: By 2033, longitudinal evidence after widespread AI mediation shows that the number of strong relationships a person can sustain and the number of relationships in which they can bear shared consequences both rise materially, without a new attention or presence bottleneck.
- **Original leading indicator**: Share of work, education, and transactions coordinated through AI mediation; human time per coordination; close-network size and relationship-repair frequency; measured annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-007.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Directionally consistent but causality remains unverified: sources support weak/strong tie differences, not an AI-mediated capacity effect. Retained: strong ties are bounded by shared experience, mutual exposure, and finite attention while weak-tie coordination scales; the causal gap is carried by longitudinal leading indicators, and confidence is not raised.
- **Original external comparison source**: EXT-17, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-017` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-018

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L162–L183`；`docs/en/ledger/11-20.md:L162–L183`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L870–L888`
- **Current card anchor**: `docs/en/ledger/11-20.md:L162–L183`
- **Original title**: Parallel reasoning before long-horizon autonomy
- **Original one-sentence judgment**: By 2028, generate–compare–revise becomes the default workflow before long-horizon autonomy.
- **Original reasoning chain**: J-006 raises parallel throughput → candidate search becomes cheap first → reliable long-horizon environmental control still requires J-009 boundaries and evaluation → parallel reasoning spreads first.
- **Original time window**: 2026–2028.
- **Original falsifier**: By end-2028, high-value workflows mainly rely on low-confirmation long-horizon autonomy rather than candidate search.
- **Original leading indicator**: Samples per task, automatic comparison share, and action span without human takeover; semiannual.
- **Original confidence**: High.
- **Original depends-on**: J-006, J-009.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the consensus: generate–compare–revise may become common before long-horizon autonomy, but the window remains this project’s inference. Retained: cheaper candidate search follows directly from J-006; the window remains this project’s inference and is carried by the end-2028 falsification condition.
- **Original external comparison source**: EXT-1 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-018` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-019

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L184–L205`；`docs/en/ledger/11-20.md:L184–L205`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L889–L907`
- **Current card anchor**: `docs/en/ledger/11-20.md:L184–L205`
- **Original title**: Token saving is a window
- **Original one-sentence judgment**: From 2026–2028, stronger models and cheaper repeated attempts compress the value of saving tokens; it is a window, not durable scarcity.
- **Original reasoning chain**: J-001 lowers unit cost → J-006 enables sampling → dud token cost falls → the independent premium for token saving shrinks.
- **Original time window**: 2026–2028.
- **Original falsifier**: By 2028, buyers still pay a structural premium for fewer model calls, without supply constraints explaining it.
- **Original leading indicator**: Calls per task, call price, and retention premium for token-optimization services; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Retain with a different mechanism: cost decline can come from inference efficiency and hardware scheduling; public prices do not prove optimization premiums vanish.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-019` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-020

**Current pair / 当前双语卡片**：`docs/zh/ledger/11-20.md:L206–L226`；`docs/en/ledger/11-20.md:L206–L226`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L908–L926`
- **Current card anchor**: `docs/en/ledger/11-20.md:L206–L226`
- **Original title**: Reproducible content keeps falling in price
- **Original one-sentence judgment**: By 2028, reproducible content keeps falling in marginal price as objective selection becomes part of generation.
- **Original reasoning chain**: J-002 formalizable quality is tested automatically → J-015 expands the generate–verify loop → homogeneous supply increases → mere content delivery loses price.
- **Original time window**: 2026–2028.
- **Original falsifier**: By 2028, generic reproducible content retains broad scarcity premiums without copyright or compute constraints.
- **Original leading indicator**: Generation cost, delivery price, and automatic-selection coverage; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-002, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with rising content supply, but liability-sensitive selection may persist; detection, labeling, and provenance remain specialized layers. Retained: the supply-demand inference that copyable content depresses marginal price holds; this card does not claim liability-sensitive selection disappears, and detection and provenance remain handled under J-022.
- **Original external comparison source**: EXT-1, EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-020` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-021

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L5–L26`；`docs/en/ledger/21-30.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L927–L945`
- **Current card anchor**: `docs/en/ledger/21-30.md:L5–L26`
- **Original title**: First-hand field signals earn a premium first
- **Original one-sentence judgment**: From 2026–2029, unrecorded field observations and traceable sources earn a premium earlier than second-hand expression.
- **Original reasoning chain**: J-005’s raw signals cannot be recombined → J-015 makes second-hand expression easier to screen → buyers shift premiums to field reality, sources, and accountability.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, buyers pay no differential for verifiable field reality over high-fidelity recombination.
- **Original leading indicator**: Premium for sourced material and field-data contracts; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-015.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Retain with a different mechanism: traceable first-hand sources may gain value first; broad field-premium pricing is unproven.
- **Original external comparison source**: EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-021` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-022

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L27–L48`；`docs/en/ledger/21-30.md:L27–L48`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L946–L964`
- **Current card anchor**: `docs/en/ledger/21-30.md:L27–L48`
- **Original title**: Forgable signals drive credential upgrades
- **Original one-sentence judgment**: From 2026–2029, more forgable personalized signals push important decisions toward costlier identity, fulfillment, and liability credentials.
- **Original reasoning chain**: J-005 raises accountable entities → J-017 cheapens weak-tie coordination → surface interaction is harder to distinguish → high-value decisions raise credential thresholds.
- **Original time window**: 2026–2029.
- **Original falsifier**: Acceptance of low-cost generated identity signals rises in high-value transactions without added liability or verification.
- **Original leading indicator**: Multifactor credential adoption, guarantees, and liability clauses; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-017.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with trust becoming more important, with a provenance, identity, and liability-credential mechanism; adoption and cost remain unknown. Retained: more forgeable signals necessarily raise the verification threshold for high-value judgments, which follows from the forgery mechanism; adoption and cost are unknown, so confidence stays Medium.
- **Original external comparison source**: EXT-4, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-022` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-023

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L49–L70`；`docs/en/ledger/21-30.md:L49–L70`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L965–L983`
- **Current card anchor**: `docs/en/ledger/21-30.md:L49–L70`
- **Original title**: Attention shifts toward fulfilled commitments
- **Original one-sentence judgment**: From 2027–2030, important attention allocation shifts from expression quality toward relationship continuity and fulfilled commitments.
- **Original reasoning chain**: J-017 expands coordination supply → J-022 makes surface signals easier to forge → one-off expression loses distinction → repeated fulfillment records gain weight.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, important choices are still predicted mainly by one-off generated expression rather than fulfillment records.
- **Original leading indicator**: Use of fulfillment, repeat relationships, and breach records; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-017, J-022, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Evidence is insufficient, though the direction is retained: fulfillment records may matter more as expression grows, but usage data does not prove an attention shift. Retained: the direction follows from declining discriminability of one-off expression plus durable records in repeated relationships, which current usage data can neither prove nor refute; the attention-shift risk is carried by the 2030 falsification condition.
- **Original external comparison source**: EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-023` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-024

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L71–L92`；`docs/en/ledger/21-30.md:L71–L92`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L984–L1002`
- **Current card anchor**: `docs/en/ledger/21-30.md:L71–L92`
- **Original title**: Credentials re-layer (landscape only)
- **Original one-sentence judgment**: From 2027–2032, credentials may re-layer around fulfillment, liability, and presence, but the institutional form is uncertain.
- **Original reasoning chain**: J-022 raises verification cost → J-023 raises the value of long records → risk contexts adopt different credential layers, subject to platform and legal choices.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, high-risk transactions still rely on one low-cost identity signal without contextual layers.
- **Original leading indicator**: Guarantees, audits, and presence proofs in high-risk services; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-022, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence supports possible credential stratification; the institutional endpoint remains uncertain, so keep it landscape-only. Retained as landscape only, with confidence not raised; upgrading to a bettable judgment requires evidence of an institutional endpoint (law or platforms explicitly adopting stratified credentials).
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-024` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-025

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L93–L114`；`docs/en/ledger/21-30.md:L93–L114`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1003–L1021`
- **Current card anchor**: `docs/en/ledger/21-30.md:L93–L114`
- **Original title**: Small-team output rises
- **Original one-sentence judgment**: From 2027–2030, small teams complete more verifiable output with fewer steps.
- **Original reasoning chain**: J-009 constrained continuity → J-013 inspectable tools → repeated knowledge steps become agent-mediated → verifiable output rises at constant headcount.
- **Original time window**: 2027–2030.
- **Original falsifier**: By 2030, comparable teams using constrained agents do not produce more verifiable output.
- **Original leading indicator**: Auditable tasks per employee, takeover rate, and output per unit; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with knowledge-work automation, but causal evidence for higher net output in small teams remains insufficient. Retained: rising verifiable output once repeated knowledge steps are delegated follows from the mechanism; the causal gap is carried by leading indicators comparing equally sized teams.
- **Original external comparison source**: EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-025` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-026

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L115–L136`；`docs/en/ledger/21-30.md:L115–L136`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1022–L1040`
- **Current card anchor**: `docs/en/ledger/21-30.md:L115–L136`
- **Original title**: Responsibility boundaries remain
- **Original one-sentence judgment**: From 2027–2032, responsibility boundaries do not disappear at the same rate as knowledge-work steps.
- **Original reasoning chain**: J-009 expands executable steps → J-013 makes permissions programmable → accidents still need a legal entity → authorization, review, and escalation remain scarce.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, high-value AI actions routinely have no identifiable person or organization bearing consequences.
- **Original leading indicator**: Liability clauses, escalation roles, and insurance claims; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-009, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the consensus: automating execution will not remove oversight and liability boundaries at the same rate; rules do not forecast job counts. Retained: the constraint that incidents require a legal subject does not dissolve with automation; this card forecasts no job counts, so the regulatory evidence does not conflict with it.
- **Original external comparison source**: EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-026` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-027

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L137–L158`；`docs/en/ledger/21-30.md:L137–L158`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1041–L1059`
- **Current card anchor**: `docs/en/ledger/21-30.md:L137–L158`
- **Original title**: Rented compute spreads capability
- **Original one-sentence judgment**: From 2026–2029, rented compute spreads access to AI capability for small organizations without distributing gains evenly.
- **Original reasoning chain**: J-001 lowers call cost → J-006 raises affordable attempts → renting lowers fixed-capital barriers → data, access, and liability capacity still differentiate gains.
- **Original time window**: 2026–2029.
- **Original falsifier**: By 2029, small organizations cannot obtain comparable general reasoning by renting, or diffusion eliminates gain differences.
- **Original leading indicator**: Small-organization call share, fixed compute capex, and rental price; quarterly.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-006.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with capability diffusion, with uneven gains more specifically constrained by energy, data, and organizational capacity. Retained: rentable capability and uneven gains arise from two different constraint sets (capital thresholds versus data, distribution, and liability capacity), and the diffusion evidence supports only the first.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-027` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-028

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L159–L180`；`docs/en/ledger/21-30.md:L159–L180`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1060–L1078`
- **Current card anchor**: `docs/en/ledger/21-30.md:L159–L180`
- **Original title**: Access becomes a bargaining node (landscape only)
- **Original one-sentence judgment**: From 2027–2032, proprietary data, distribution, and liability capacity may become more important bargaining nodes than models.
- **Original reasoning chain**: J-027 expands model access → J-005 raises the value of real inputs and responsibility → models become more reproducible → control of inputs, exits, and losses may earn rent.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, access controllers have no persistent premium over non-controllers absent regulatory constraints.
- **Original leading indicator**: Data licenses, distribution take rates, AI liability insurance, and channel exclusivity; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-005, J-013.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence only: energy, data, and liability access may become bargaining points, but persistent rents are unproven. Retained as landscape only, with confidence not raised; upgrading requires price evidence of persistent rents, not merely the existence of gatekeeping positions.
- **Original external comparison source**: EXT-4, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-028` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-029

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L181–L202`；`docs/en/ledger/21-30.md:L181–L202`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1079–L1097`
- **Current card anchor**: `docs/en/ledger/21-30.md:L181–L202`
- **Original title**: Demand-side anchors persist
- **Original one-sentence judgment**: From 2026–2030, status, certainty, embodied presence, and responsibility remain demand-side anchors despite richer expression and choice.
- **Original reasoning chain**: J-017 expands coordination → J-011 expands trial identities and expression → more options do not create shared consequences → demand remains organized around status, certainty, presence, and responsibility.
- **Original time window**: 2026–2030.
- **Original falsifier**: By 2030, these needs no longer predict important choices across groups, independent of measurement or institutional change.
- **Original leading indicator**: Preferences for presence and responsibility in high-value consumption, relationship, and commitment decisions; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-017, J-011.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Consistent with the conservative direction: social contact, well-being, and responsibility remain plausible demand anchors, but preferences through 2030 are unproven. Retained: the demand-side anchors follow from the stability of status, certainty, presence, and responsibility attribution; unchanged preferences through 2030 cannot be externally confirmed, and that risk is carried by the falsification condition.
- **Original external comparison source**: EXT-17, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-029` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-030

**Current pair / 当前双语卡片**：`docs/zh/ledger/21-30.md:L203–L223`；`docs/en/ledger/21-30.md:L203–L223`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1098–L1118`
- **Current card anchor**: `docs/en/ledger/21-30.md:L203–L223`
- **Original title**: AI mediates coordination, not shared experience (landscape only)
- **Original one-sentence judgment**: From 2027–2032, AI mediates context synchronization and relationship coordination but not experiences requiring embodied presence and shared consequences.
- **Original reasoning chain**: J-017 cheapens weak-tie coordination → J-011 enriches multimodal expression → shared experience still requires bodies, time, and reciprocal consequences → coordination agents do not expand strong-relationship capacity automatically.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, agent-mediated interaction reliably replaces shared experience in long relationships with no behavioral or reported difference.
- **Original leading indicator**: Agent messages versus shared activities, conflict-repair results, and retention; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-017, J-011.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Near-term landscape`.
- **Original external comparison**: Boundary evidence only: AI can mediate coordination, but causal and generational evidence for substituting shared experience is insufficient. Retained as landscape only: the hard constraint that shared experience requires bodies, time, and reciprocal consequences still holds, while substitution effects lack causal and generational evidence, so confidence is not raised.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-030` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-031

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L5–L27`；`docs/en/ledger/31-40.md:L5–L27`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1119–L1138`
- **Current card anchor**: `docs/en/ledger/31-40.md:L5–L27`
- **Original title**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Original one-sentence judgment**: Pausable, replayable, rollback-capable action environments become admission conditions for long-horizon AI execution
- **Original reasoning chain**: Organizations delegate long-horizon tasks → failure states and liability accumulate → observable, pausable, rollback-capable environments reduce irreversible loss → high-value deployments make the environment an admission condition
- **Original time window**: 2026–2032
- **Original falsifier**: By 2032, high-value agent execution still commonly connects directly to production systems without incident costs driving separate isolation procurement
- **Original leading indicator**: Sandbox, shadow-environment, and rollback items in procurement; agent incidents; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-010
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: logging, oversight, and risk control have institutional support; a complete rollback gate and its window are unverified.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-031` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-032

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L28–L50`；`docs/en/ledger/31-40.md:L28–L50`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1139–L1158`
- **Current card anchor**: `docs/en/ledger/31-40.md:L28–L50`
- **Original title**: Authorization review and exception escalation become scarcer than execution steps
- **Original one-sentence judgment**: Authorization review and exception escalation become scarcer than execution steps
- **Original reasoning chain**: Inspectable tool calls spread → execution steps become templated → cross-boundary authorization, exception escalation, and final responsibility still require judgment → review roles appreciate relative to execution steps
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, authorization-review hours fall at the same rate as execution hours without increased incidents
- **Original leading indicator**: Permission-denial rate, human escalation hours, responsibility-role hiring; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-013
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but relative scarcity is unproven: authorization review and escalation are institutionalized, while supply comparisons are missing. Retained: cross-boundary authorization, escalation, and final responsibility require judgment and are not absorbed by templating; relative scarcity lacks supply data, so confidence stays Medium.
- **Original external comparison source**: EXT-4, EXT-10, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-032` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-033

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L51–L73`；`docs/en/ledger/31-40.md:L51–L73`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1159–L1178`
- **Current card anchor**: `docs/en/ledger/31-40.md:L51–L73`
- **Original title**: Verifiable records of real interventions become more valuable than explanation itself
- **Original one-sentence judgment**: Verifiable records of real interventions become more valuable than explanation itself
- **Original reasoning chain**: Generated explanations become cheap → explanation supply becomes abundant → real interventions produce non-recombinable outcomes → verifiable records connect causality and responsibility → records earn a premium
- **Original time window**: 2029–2033
- **Original falsifier**: By 2033, high-liability markets no longer pay a premium for intervention records with field evidence
- **Original leading indicator**: First-hand intervention-license prices, audit requirements, evidence-backed renewal rates; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: compliance evidence, model risk controls, and intervention records are gaining value; superiority to explanation is unproven.
- **Original external comparison source**: EXT-7, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-033` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-034

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L74–L96`；`docs/en/ledger/31-40.md:L74–L96`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1179–L1198`
- **Current card anchor**: `docs/en/ledger/31-40.md:L74–L96`
- **Original title**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Original one-sentence judgment**: Synthetic evidence is accepted first in low-liability contexts; high-liability contexts still require real trials
- **Original reasoning chain**: Synthetic material lowers exploration cost → low-liability contexts tolerate model error → high-liability contexts bear bodily, legal, and compensation consequences → regulators retain real trials
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, high-liability fields broadly replace real trials with synthetic evidence without higher incident rates
- **Original leading indicator**: Regulatory acceptance scope, trial budgets, insurance clauses; annual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but the window is unverified: low-liability settings may adopt synthetic evidence earlier, while high-liability settings retain real-world validation. Retained: high-liability settings carry bodily, legal, and compensation consequences, which is why regulators preserve real trials; the window has no external support and is carried by the 2033 falsification condition.
- **Original external comparison source**: EXT-7, EXT-9 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-034` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-035

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L97–L119`；`docs/en/ledger/31-40.md:L97–L119`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1199–L1218`
- **Current card anchor**: `docs/en/ledger/31-40.md:L97–L119`
- **Original title**: Responsibility collateral enters the transaction structure for consequential AI output
- **Original one-sentence judgment**: Responsibility collateral enters the transaction structure for consequential AI output
- **Original reasoning chain**: Reproducible expression increases → error losses become harder to attribute → buyers ask who bears consequences → insurance, reserves, and audits enter contracts → responsibility collateral becomes a transaction condition
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, high-value AI services still lack liability pricing, compensation clauses, or audit requirements
- **Original leading indicator**: AI liability premiums, contractual caps, audit procurement; semiannual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: liability governance, insurance, and compensation are entering transactions, but universal “liability collateral” is unproven.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-035` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-036

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L120–L142`；`docs/en/ledger/31-40.md:L120–L142`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1219–L1238`
- **Current card anchor**: `docs/en/ledger/31-40.md:L120–L142`
- **Original title**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Original one-sentence judgment**: Long-term fulfillment records allocate attention better than one-off natural expression
- **Original reasoning chain**: Expression generation becomes cheap → surface credibility becomes hard to distinguish → repeated fulfillment leaves verifiable records → attention shifts to longitudinal consistency and delivery rate
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, important choices are still driven mainly by one-off expression rather than fulfillment records
- **Original leading indicator**: Adoption of performance-history recommendations, repeat and default rates; annual
- **Original confidence**: Medium
- **Original depends-on**: J-017
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient, though the direction is retained: long-term fulfillment records may support credibility, without direct attention-allocation evidence. Retained: cheap expression voids surface credibility while repeated fulfillment leaves verifiable records, a mechanism that does not depend on attention data; the gap is carried by leading indicators.
- **Original external comparison source**: EXT-13, EXT-14 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-036` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-037

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L143–L165`；`docs/en/ledger/31-40.md:L143–L165`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1239–L1258`
- **Current card anchor**: `docs/en/ledger/31-40.md:L143–L165`
- **Original title**: Comparable small teams produce more verifiable output
- **Original one-sentence judgment**: Comparable small teams produce more verifiable output
- **Original reasoning chain**: Constrained workflows stabilize → tool calls become inspectable → a few people orchestrate more agent steps → per-team output and audit records increase
- **Original time window**: 2027–2031
- **Original falsifier**: By 2031, agent-using small teams show no repeatable output gain over baseline
- **Original leading indicator**: Per-person delivery, rework, auditable-output share; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-009
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus but causally unproven: diffusion supports plausibility, not higher output by equally sized small teams. Retained: fewer people orchestrating more checkable steps follows from the mechanism; the causal gap on same-size output is carried by comparative leading indicators, and confidence is not raised.
- **Original external comparison source**: EXT-1, EXT-16 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-037` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-038

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L166–L188`；`docs/en/ledger/31-40.md:L166–L188`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1259–L1278`
- **Current card anchor**: `docs/en/ledger/31-40.md:L166–L188`
- **Original title**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Original one-sentence judgment**: Authorization, exception escalation, and responsibility roles do not shrink as fast as execution steps
- **Original reasoning chain**: Inspectable tool calls spread → permission boundaries clarify → normal steps automate → exceptions and cross-boundary consequences cannot be fully precomputed → responsibility roles remain
- **Original time window**: 2027–2032
- **Original falsifier**: By 2032, responsibility-role share falls at the same rate as execution roles without more high-risk incidents
- **Original leading indicator**: Exception volume, responsibility-role hiring, post-incident human intervention; quarterly
- **Original confidence**: Medium
- **Original depends-on**: J-013
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Consistent with the consensus: oversight, validation, escalation, and responsibility will not disappear with automation, while job counts and timing are unproven. Retained: exceptions and cross-boundary consequences cannot be enumerated in advance, which is why accountability roles persist; job counts and timing are not something the sources can supply and are carried by the falsification condition.
- **Original external comparison source**: EXT-10, EXT-13 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-038` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-039

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L189–L211`；`docs/en/ledger/31-40.md:L189–L211`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1279–L1298`
- **Current card anchor**: `docs/en/ledger/31-40.md:L189–L211`
- **Original title**: Rented models become abundant, while energy, data, and channel control create access rents
- **Original one-sentence judgment**: Rented models become abundant, while energy, data, and channel control create access rents
- **Original reasoning chain**: Unit reasoning cost falls → model capability becomes rentable → model differences narrow → energy access, exclusive data, and channels remain constrained by physics and ownership → controllers earn access rents
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, controllers of energy, data, and channels have no persistent premium over non-controllers
- **Original leading indicator**: Rented-model prices, data-license fees, channel take rates, energy-access spreads; annual
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Retain with a different mechanism: model rental may become abundant, while energy and infrastructure constraints are real; data and channel rents remain unproven.
- **Original external comparison source**: EXT-1, EXT-12 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-039` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-040

**Current pair / 当前双语卡片**：`docs/zh/ledger/31-40.md:L212–L233`；`docs/en/ledger/31-40.md:L212–L233`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1299–L1318`
- **Current card anchor**: `docs/en/ledger/31-40.md:L212–L233`
- **Original title**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Original one-sentence judgment**: Balance sheets able to absorb AI accidents become a separate scarcity
- **Original reasoning chain**: Real interventions and commitments appreciate → AI accident losses become measurable → contracts require compensation capacity → capital and insurance price solvency → large balance sheets gain admission advantage
- **Original time window**: 2028–2033
- **Original falsifier**: By 2033, compensation capacity does not affect AI contract prices, financing, or deployment eligibility
- **Original leading indicator**: Liability premiums, reserves, contract asset requirements; annual
- **Original confidence**: Medium
- **Original depends-on**: J-005
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient but grounded in current practice: insurance and liability governance exist, while a balance-sheet scarcity premium is unproven. Retained: pricing solvency through contracts and insurance extends current governance; the independent scarcity premium is unproven, so confidence stays Medium.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-040` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-041

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L5–L27`；`docs/en/ledger/41-50.md:L5–L27`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1319–L1338`
- **Current card anchor**: `docs/en/ledger/41-50.md:L5–L27`
- **Original title**: AI first expands the coordination radius of weak ties
- **Original one-sentence judgment**: AI first expands the coordination radius of weak ties
- **Original reasoning chain**: Communication and context-sync costs fall → translation, introductions, and scheduling scale → weak-tie connection radius expands → strong ties remain constrained by shared consequences
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, AI mediation neither increases cross-organization weak-tie connections nor reduces coordination time
- **Original leading indicator**: AI-mediated coordination share, cross-organization contacts, human time per coordination; annual
- **Original confidence**: Medium
- **Original depends-on**: J-017
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Directionally consistent but unproven: AI broadens communication and coordination, without enough causal data to separate weak- and strong-tie effects. Retained: falling coordination cost widens weak-tie radius first while strong ties remain bounded by shared exposure; the causal-separation gap is carried by weak-/strong-tie leading indicators.
- **Original external comparison source**: EXT-16, EXT-18 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-041` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-042

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L28–L50`；`docs/en/ledger/41-50.md:L28–L50`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1339–L1358`
- **Current card anchor**: `docs/en/ledger/41-50.md:L28–L50`
- **Original title**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Original one-sentence judgment**: Shared experience and embodied presence remain the capacity ceiling for strong ties (landscape only)
- **Original reasoning chain**: Multimodal expression becomes abundant → mediated companionship and reminders spread → shared experience still requires bodies, time, and reciprocal consequences → strong-tie capacity remains presence-constrained
- **Original time window**: 2027–2033
- **Original falsifier**: By 2033, agent-mediated interaction reliably replaces shared experience in long relationships with no reported or behavioral difference
- **Original leading indicator**: Agent interaction versus shared activity, conflict repair, relationship retention; annual
- **Original confidence**: Low
- **Original depends-on**: J-011
- **Original status and lineage**: ACTIVE.
- **Original source**: `Mid-term landscape`.
- **Original external comparison**: Evidence is insufficient: ethics and care governance preserve human agency, but do not establish strong-tie capacity or substitution effects. Retained as landscape only, with confidence not raised; upgrading requires both behavioral and self-reported evidence of substitution in long-term relationships.
- **Original external comparison source**: EXT-9 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-042` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-043

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L51–L72`；`docs/en/ledger/41-50.md:L51–L72`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1554–L1573`
- **Current card anchor**: `docs/en/ledger/41-50.md:L51–L72`
- **Original title**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only)
- **Original one-sentence judgment**: High-value agent execution may shift to boundary grants rather than step-by-step operation (landscape only).
- **Original reasoning chain**: Rollback-capable environments lower supervision cost → agents take more steps → supervision shifts to boundaries and escalation → high-value deployment uses boundary grants.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, high-value agents still require step approval and rollback has not lowered supervision cost.
- **Original leading indicator**: Boundary-grant share, step approvals, rehearsal procurement; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-031, J-032, J-014.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: current governance supports permission boundaries, but cannot establish a long-term shift from stepwise operation to boundary grants. Retained as landscape only, with confidence not raised; upgrading requires adoption evidence such as the share of boundary-grant contracts, not the existence of current permission design.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-043` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-044

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L73–L94`；`docs/en/ledger/41-50.md:L73–L94`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1574–L1593`
- **Current card anchor**: `docs/en/ledger/41-50.md:L73–L94`
- **Original title**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only)
- **Original one-sentence judgment**: Liability positions able to absorb accidents become the load-bearing wall of agent infrastructure (landscape only).
- **Original reasoning chain**: Execution scales → tail losses exceed one user’s capacity → collateral and balance sheets become admission conditions → solvent entities support infrastructure.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, solvency does not affect deployment, pricing, or financing.
- **Original leading indicator**: Liability premiums, reserves, solvency clauses; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-032, J-040.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: liability and insurance are institutional topics, but solvency as an agent-infrastructure bottleneck is unestablished. Retained as landscape only, with confidence not raised; upgrading requires direct evidence that solvency affects deployment, pricing, or financing.
- **Original external comparison source**: EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-044` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-045

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L95–L116`；`docs/en/ledger/41-50.md:L95–L116`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1594–L1613`
- **Current card anchor**: `docs/en/ledger/41-50.md:L95–L116`
- **Original title**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only)
- **Original one-sentence judgment**: As synthetic expression becomes abundant, unarranged observation of reality becomes scarce (landscape only).
- **Original reasoning chain**: Replayable supply grows → narrative loses distinctiveness → unarranged field observation becomes scarce → preserving conditions and causality gains value.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, high-liability decision-makers do not distinguish field from synthetic evidence.
- **Original leading indicator**: Field-evidence premium, raw-record requirements, synthetic substitution; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-033, J-034.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: provenance standards support the relative importance of original records, not inevitable scarcity of unarranged observation.
- **Original external comparison source**: EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-045` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-046

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L117–L138`；`docs/en/ledger/41-50.md:L117–L138`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1614–L1633`
- **Current card anchor**: `docs/en/ledger/41-50.md:L117–L138`
- **Original title**: High-liability settings retain a premium for field causal records (landscape only)
- **Original one-sentence judgment**: High-liability settings retain a premium for field causal records (landscape only).
- **Original reasoning chain**: Cheap explanations → liable parties distinguish advice from intervention → field records connect action, outcome and compensation → high-liability transactions pay.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, replacing field records with synthetic evidence changes neither accidents nor prices.
- **Original leading indicator**: Record licensing, insurance discounts, trial requirements; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-033, J-034.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: high-liability settings require provenance and validation, but a price premium for field causal records is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence of price or insurance-rate differences attributable to field causal records.
- **Original external comparison source**: EXT-7, EXT-11 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-046` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-047

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L139–L160`；`docs/en/ledger/41-50.md:L139–L160`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1634–L1653`
- **Current card anchor**: `docs/en/ledger/41-50.md:L139–L160`
- **Original title**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only)
- **Original one-sentence judgment**: Copyable AI relationships expand companionship supply, while non-copyable reciprocity becomes scarce (landscape only).
- **Original reasoning chain**: Copyable memory, patience and style → companionship scales → copyability reduces exclusivity and shared risk → non-copyable reciprocity is scarce.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, copyable companionship replaces human reciprocity with no behavioral difference.
- **Original leading indicator**: Copy rate, exit rate, retention and repair outcomes; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-042.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: copyable AI companionship may expand supply, but reciprocity scarcity and long-term substitution lack evidence. Retained as landscape only, with confidence not raised; upgrading requires long-term behavioral comparisons between copyable companionship and human reciprocity.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-047` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-048

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L161–L182`；`docs/en/ledger/41-50.md:L161–L182`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1654–L1673`
- **Current card anchor**: `docs/en/ledger/41-50.md:L161–L182`
- **Original title**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only)
- **Original one-sentence judgment**: Authorization, exit, and subject boundaries in human–AI relationships become normative issues (landscape only).
- **Original reasoning chain**: Copyable, pausable relationships → memory and commitment boundaries diverge → data, exit and liability conflicts grow → institutions define subjects.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, relationship-data and exit disputes do not persist and ordinary contracts suffice.
- **Original leading indicator**: Data disputes, exit clauses, dedicated rules or cases; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-042.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Consistent with the consensus that the normative issue exists, but predictive evidence is insufficient; authorization, exit, and subject boundaries lack a stable endpoint. Retained as landscape only, with confidence not raised; upgrading requires institutional evidence that disputes persist and ordinary contracts are insufficient.
- **Original external comparison source**: EXT-9, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-048` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-049

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L183–L204`；`docs/en/ledger/41-50.md:L183–L204`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1674–L1693`
- **Current card anchor**: `docs/en/ledger/41-50.md:L183–L204`
- **Original title**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only)
- **Original one-sentence judgment**: As AI coordination becomes abundant, jointly bearing irreversible commitments becomes scarce (landscape only).
- **Original reasoning chain**: Coordination costs fall → candidates multiply → choosing is not commitment; commitment bears failure → willing groups are scarce.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, more coordination also raises joint bearing of long-term failure and repair is no bottleneck.
- **Original leading indicator**: Commitment retention, exit rate, repair time; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-038.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: advice supply may grow, but comparable data on jointly bearing irreversible commitments is absent. Retained as landscape only, with confidence not raised; upgrading requires comparable data linking increased coordination to the share of jointly borne commitments.
- **Original external comparison source**: EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-049` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-050

**Current pair / 当前双语卡片**：`docs/zh/ledger/41-50.md:L205–L225`；`docs/en/ledger/41-50.md:L205–L225`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1694–L1713`
- **Current card anchor**: `docs/en/ledger/41-50.md:L205–L225`
- **Original title**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only)
- **Original one-sentence judgment**: The value of human collaboration shifts from doing steps together to choosing commitments together (landscape only).
- **Original reasoning chain**: Agents absorb coordination → human intervention shrinks → it concentrates on irreversible choices and joint liability → commitment quality measures collaboration.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, collaboration value remains step execution rather than commitment choice.
- **Original leading indicator**: Human-confirmed commitments, irreversible decisions, fulfillment; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-041, J-038.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: governance preserves human confirmation at key points, but does not prove a wholesale shift in collaboration value.
- **Original external comparison source**: EXT-4, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-050` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-051

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L137–L158`；`docs/en/ledger/51-60.md:L137–L158`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1714–L1733`
- **Current card anchor**: `docs/en/ledger/51-60.md:L137–L158`
- **Original title**: Abundant advice does not automatically disperse real action rights (landscape only)
- **Original one-sentence judgment**: Abundant advice does not automatically disperse real action rights (landscape only).
- **Original reasoning chain**: Advice is cheap → information grows → permissions, resources and compensation remain concentrated → advice does not disperse action rights.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, advice growth coincides with broad dispersion of energy, data, licensing, and compensation access.
- **Original leading indicator**: Resource concentration, authorization holders, advice-to-action distribution; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-039, J-040, J-035.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: Gate 1 fails; the billion-scale figure is an upper bound for affected people, not a count of distinct weekly actors; this card remains a low-confidence landscape/institutional judgment and is no longer a society-wide trend claim; original card text retained, identifier not reused, basis: `Retrospect · Gate 1`).
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: infrastructure, liability, and resource control may concentrate, but the relationship between advice abundance and action rights is unproven. Retained as landscape only, with confidence not raised; upgrading requires evidence on how dispersed the key gates of licensing, resource access, and compensation actually are.
- **Original external comparison source**: EXT-12, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-051` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-052

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L159–L180`；`docs/en/ledger/51-60.md:L159–L180`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1734–L1753`
- **Current card anchor**: `docs/en/ledger/51-60.md:L159–L180`
- **Original title**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only)
- **Original one-sentence judgment**: Energy, real-world data, authorization, and compensation form far-term institutional access points (landscape only).
- **Original reasoning chain**: Model supply expands → control migrates to real inputs, permissions and losses → institutions price four access points → control creates bargaining power.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, four access points create no persistent price, licensing, or financing advantage.
- **Original leading indicator**: Energy spreads, data fees, review fees, insurance reserves; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-039, J-040, J-035.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Retain but with insufficient evidence: energy, real-world data, authorization, and compensation have present-day entry points; the long-term combination remains an inference.
- **Original external comparison source**: EXT-12, EXT-14, EXT-15 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-052` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-053

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L181–L202`；`docs/en/ledger/51-60.md:L181–L202`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1754–L1773`
- **Current card anchor**: `docs/en/ledger/51-60.md:L181–L202`
- **Original title**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only)
- **Original one-sentence judgment**: As generatable goods become abundant, what one personally bore may become a signal of meaning (landscape only).
- **Original reasoning chain**: Generatable output loses distinction → real time, bodily risk and responsibility leave cost signals → personal burden becomes meaning/status signal.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, real responsibility no longer affects trust, status, or long-term choices.
- **Original leading indicator**: Trust premium for commitments, experience verification, narrative/outcome coupling; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-042, J-029.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: human agency and responsibility have current support, but personally borne experience as a meaning signal lacks generational evidence. Retained as landscape only, with confidence not raised; upgrading requires generational data on trust, status, or long-term choices.
- **Original external comparison source**: EXT-9, EXT-17 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-053` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-054

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L203–L223`；`docs/en/ledger/51-60.md:L203–L223`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1774–L1879`
- **Current card anchor**: `docs/en/ledger/51-60.md:L203–L223`
- **Original title**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only)
- **Original one-sentence judgment**: Non-delegable time, bodily risk, and long commitments remain demand-side scarcities (landscape only).
- **Original reasoning chain**: Choice grows but lifetime does not → bodily risk and long commitments remain personal → scarcity moves to non-delegable experience.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, agent substitution leaves no observable difference in preferences or outcomes around time and risk.
- **Original leading indicator**: Non-delegable time, long-commitment completion, embodied premium; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-042, J-029.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Far-term landscape`.
- **Original external comparison**: Evidence-limited landscape: bodies, care, and real-world risk remain governance objects, but demand-side scarcity through 2033–2040 is unproven. Retained as landscape only, with confidence not raised; upgrading requires studies on differences in preferences and outcomes after delegated experience substitutes for direct experience.
- **Original external comparison source**: EXT-9, EXT-10 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-054` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-055

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L5–L26`；`docs/en/ledger/51-60.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1359–L1377`
- **Current card anchor**: `docs/en/ledger/51-60.md:L5–L26`
- **Original title**: Real-world signals earn a premium as contract assets in high-liability tasks
- **Original one-sentence judgment**: In high-liability tasks, real-world signals with provenance, permission, calibration, and liability chains are more likely than data files alone to earn a structural premium.
- **Original reasoning chain**: C1 makes second-hand expression and synthetic samples abundant → ordinary data files lose marginal price → high-liability tasks still require real observations, provenance, and an accountable party → collection permission, calibration, usage boundaries, and compensation duties enter contracts → data becomes a contract asset with a liability chain.
- **Original time window**: 2029–2033.
- **Original falsifier**: By 2033, across multiple high-liability fields, regulators, insurers, and buyers broadly accept synthetic evidence with no worse incident rate than real signals, while provenance, calibration, and liability chains carry no observable premium.
- **Original leading indicator**: Synthetic-evidence share in high-liability approvals, premium for data contracts with provenance and calibration clauses, real-trial budget share, and data-liability insurance rates; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-033, J-034, J-039.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C2: How Real-World Signals Become Contract Assets`.
- **Original external comparison**: Directionally consistent with stronger data governance, provenance, and trust, but narrowed here to high-liability tasks; an independent premium for real-world signals remains unproven. Retained: high-liability tasks require real observation, provenance, and a recourse-bearing subject, none of which recombination can produce; the independent premium is unproven, so confidence stays Medium.
- **Original external comparison source**: EXT-7, EXT-10, EXT-14 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-055` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-056

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L27–L48`；`docs/en/ledger/51-60.md:L27–L48`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1378–L1396`
- **Current card anchor**: `docs/en/ledger/51-60.md:L27–L48`
- **Original title**: The binding constraint on compute expansion moves from chip supply to power delivery and interconnection permits
- **Original one-sentence judgment**: Within this window the binding constraint on compute expansion moves from chip supply to power delivery and interconnection permitting.
- **Original reasoning chain**: Chips are a mass-produced, shippable, globally reallocatable industrial good whose expansion elasticity rises with investment → transformers, high-voltage equipment, and lines are bound by heavy-manufacturing and construction cycles, can barely be accelerated by more orders, and cannot be reallocated across regions → interconnection, environmental, and land permits run on administrative and local-political cycles decoupled from technical progress → the three supply curves differ in slope by an order of magnitude → when capital concentrates, permits and interconnection queues are exhausted before wafers.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, among delays to new compute projects in major markets, those attributable to chip delivery still outnumber those attributable to power delivery and interconnection permitting; or average large-load interconnection wait times in major markets fall below their 2026 level.
- **Original leading indicator**: Large-load interconnection queue times, transformer and high-voltage switchgear lead times, average time from project announcement to energization, share of deals where power contracts are signed before hardware orders; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-027.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: Directionally consistent with "AI electricity growth is a real constraint," but this project's claim is narrower and more falsifiable — the binding constraint is the **timing** of delivery and permitting, not total generation. The comparison obtained this round covers generation-side queues only (EXT-19 explicitly excludes load-side queues), so the agreement holds at the mechanism level only. Why the judgment is retained: load-side statistics are still missing, but both legs of the mechanism are separately corroborated — DOE records connection lead times of 1–3 years for hyperscale facilities of 300–1000 MW+ and the resulting shift toward co-location with existing generation to get power faster (EXT-29), and ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30). Confidence stays at Medium rather than rising, because cross-market load-side queue statistics still do not exist.
- **Original external comparison source**: EXT-12, EXT-19, EXT-29, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-056` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-057

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L49–L70`；`docs/en/ledger/51-60.md:L49–L70`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1397–L1415`
- **Current card anchor**: `docs/en/ledger/51-60.md:L49–L70`
- **Original title**: What gets priced is not energy but certainty of delivery date
- **Original one-sentence judgment**: In compute-related power transactions, what is mainly priced is not energy but the certainty of being live on the promised date.
- **Original reasoning chain**: J-056 makes the queue the binding constraint → model generations turn over quickly, so capacity that arrives eighteen months late loses much of its competitive value → willingness to pay for an in-service date exceeds willingness to pay for a lower average tariff → contracts grow capacity reservation fees, in-service date guarantees, delay damages, and on-site generation or storage as a bridge → within one region, permitted and interconnected sites trade above bare land by far more than construction cost.
- **Original time window**: 2027–2032.
- **Original falsifier**: By 2032, price differences in large compute power contracts are mainly explained by per-kilowatt-hour price, and terms tied to delivery-date guarantees (reservation fees, lead-time premiums, delay damages) have not become common.
- **Original leading indicator**: Share of power and capacity contracts carrying in-service date guarantees and delay damages; price gap between permitted sites and bare land in the same region; adoption of on-site generation and storage as bridging; semiannual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Partly consistent, but the agreement does not sit where this card lands.** Agreement: regulator-approved large-load contracts are indeed tiered by commitment and term rather than by per-kilowatt-hour price — FERC directed PJM to create three tiers of co-located load service distinguished by capacity commitment (EXT-21), and the AEP Ohio tariff approved by PUCO builds its price protection from an 85% minimum take, a 12-year term, a 4-year ramp, exit fees and collateral (EXT-22). **Divergence**: those terms protect the **seller** against being stranded, whereas this card claims the **buyer** pays a premium for energization on date; both point at time and commitment being priced, but from opposite sides, and one does not substitute for the other. **Evidence boundary**: this card's falsifier asks how common such contract terms are, and commercial terms in large-load contracts are almost entirely confidential, so no public statistics exist and the falsifier is currently **not computable**. Why the judgment is retained: the direction of the mechanism has independent support in two jurisdictions, so the judgment stands with confidence at Medium rather than rising; and the leading indicator shifts from "share of contracts" to a publicly checkable proxy — the count of minimum-take and exit-fee provisions appearing in regulatory filings, and the price gap between permitted and raw sites in the same region.
- **Original external comparison source**: EXT-21, EXT-22 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-057` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-058

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L71–L92`；`docs/en/ledger/51-60.md:L71–L92`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1416–L1434`
- **Current card anchor**: `docs/en/ledger/51-60.md:L71–L92`
- **Original title**: AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a grid flexibility resource
- **Original one-sentence judgment**: AI load splits into latency-sensitive and schedulable halves, and the schedulable half becomes a flexibility resource the grid pays for rather than merely a burden.
- **Original reasoning chain**: Interactive inference is latency-sensitive, non-interruptible, and immobile → training, batch inference, and evaluation can be paused, deferred, and moved across time zones → for the latter the cost of interruption is time rather than spoilage, unlike aluminium smelting and similar heavy industrial load → what grids are shortest of is flexibility, and demand response, interruptible tariffs, and capacity markets are existing payment channels → schedulable compute is load and resource at once, and its real power cost can sit below its nominal tariff.
- **Original time window**: 2027–2033.
- **Original falsifier**: By 2033, contracted data-centre capacity in interruptible or demand-response programs in major markets remains negligible (under 5% of their contracted capacity) and large compute users broadly refuse interruptibility terms.
- **Original leading indicator**: Contracted data-centre demand-response capacity and its share, share of interruptible tariff contracts, public practice of cross-region scheduling of training jobs, data-centre bids in capacity markets; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056, J-018.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, scale unknown.** Agreement: schedulability has moved from inference to measurement — in EPRI's DCFlex demonstration in Phoenix an AI compute cluster cut 25% of its power through a three-hour grid peak without affecting core services (EXT-24), and Duke's Nicholas Institute puts an upper bound on the scale: if new large loads accept 0.25–1.0% annual curtailment, the 22 largest US balancing areas could host nearly 100 GW more load (EXT-23). **Divergence and evidence boundary**: both are **potential**, not **contracted**. This card's falsifier turns on whether contracted interruptible capacity stays below 5%, yet neither PJM's roughly 8,064.7 MW of cleared demand-response capacity (EXT-25) nor ERCOT's flexible-load estimates are broken out by industry, and no authority publishes data-centre-specific contracted capacity — so the falsifier is currently **not computable**. Why the judgment is retained: the mechanism side is better evidenced than when the card was written (inference became measurement), so the judgment stands with confidence at Medium; and one leading indicator is added — whether PJM or ERCOT begins disclosing data-centre demand-response registrations by industry, which is the precondition for this card becoming falsifiable again.
- **Original external comparison source**: EXT-23, EXT-24, EXT-25, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-058` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-059

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L93–L114`；`docs/en/ledger/51-60.md:L93–L114`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1435–L1453`
- **Current card anchor**: `docs/en/ledger/51-60.md:L93–L114`
- **Original title**: The handle of compute control moves from hardware export to the use side
- **Original one-sentence judgment**: Once rental architectures let capability cross borders while hardware stays put, the handle of compute control moves from hardware export to use-side control of parties, purposes, and site authorization.
- **Original reasoning chain**: Chips are discrete, countable, traceable, and must clear customs, making them an ideal control object → rented compute diffuses capability while hardware does not move (J-027) → governing "who owns" cannot constrain "who uses" → a regulator either accepts failed control or moves duties to the use side: identity and purpose declaration, remote-access restrictions, model-weight transfer rules, site and operator authorization → the object of control shifts from things to parties and contracts.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, major control regimes remain anchored only in hardware and entity lists, with no enforceable duties on weight transfer, remote access, or data-centre operator authorization, and no enforcement cases.
- **Original leading indicator**: Provisions and revisions covering weights, remote access, cloud services, and data-centre authorization; identity and purpose-declaration requirements imposed on compute providers; compliance clauses in cross-border compute contracts; enforcement and penalty cases; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-027.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Partly consistent, with one explicit divergence.** Agreement: control has already moved beyond the chip as a physical object, reaching the most advanced closed model weights and data-centre operator authorization (EXT-20). Divergence: this project's independent reasoning expected the handle to land mainly on accounts and remote-access licensing, whereas the observed landing point is weight thresholds plus site and operator authorization, with no standalone cloud-access licensing regime. Why the judgment is retained: the mechanism (rental hollows out entity control → duties migrate to parties and contracts) matches the observed direction, and the difference is the interface rather than the direction; the falsifiable part is therefore narrowed to "do enforceable use-side duties and enforcement cases appear," not "does a cloud-access licence appear."
- **Original external comparison source**: EXT-20 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-059` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-060

**Current pair / 当前双语卡片**：`docs/zh/ledger/51-60.md:L115–L136`；`docs/en/ledger/51-60.md:L115–L136`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1454–L1472`
- **Current card anchor**: `docs/en/ledger/51-60.md:L115–L136`
- **Original title**: Energy-rich hosts trade sites for compute and gain rent rather than capability sovereignty (landscape only)
- **Original one-sentence judgment**: Host states with surplus energy and fast permitting trade sites and power for compute investment and obtain rent, employment, and tax revenue rather than any right of disposal over the capability itself (landscape only).
- **Original reasoning chain**: Power and sites cannot be moved, chips can be moved but are export-controlled, and model weights move instantly → the three factors separate geographically and jurisdictionally → what a host state supplies is precisely the least movable factor → its leverage (cutting power, expropriation) is one-shot and extremely costly → what it gains shows up as rent and employment, not capability sovereignty.
- **Original time window**: 2028–2035.
- **Original falsifier**: By 2035, host states broadly obtain weight escrow, local usage quotas, or independent audit rights in cross-border compute contracts; or most new compute remains concentrated in states that hold both chip supply and jurisdiction, with no observable contract class for cross-border "sovereign compute sites."
- **Original leading indicator**: Terms obtained by host states in cross-border data-centre investment (local usage quotas, weight escrow, audit rights); arrangements trading energy subsidies for compute quotas; country-level compute caps and authorization regimes; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-056, J-059.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: Partly consistent with observed institutions — country-level compute allocation caps and data-centre operator authorization already exist (EXT-20), and Virginia's JLARC audit shows how little of the value a host jurisdiction retains even inside its own borders (EXT-28). But the inference about host states' long-run bargaining position lacks evidence. Why the judgment is retained: it is kept as landscape only and confidence is not raised; upgrading it requires verifiable evidence from cross-border contract terms — weight escrow, local usage quotas, or independent audit rights.
- **Original external comparison source**: EXT-20, EXT-28 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-060` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-061

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L27–L48`；`docs/en/ledger/61-70.md:L27–L48`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1473–L1491`
- **Current card anchor**: `docs/en/ledger/61-70.md:L27–L48`
- **Original title**: Local externalities of data centres become explicit and social licence becomes a real siting constraint
- **Original one-sentence judgment**: The local externalities of data centres become explicit, turning social licence from an implicit premise into a real cost line in siting.
- **Original reasoning chain**: Data centres are very large investments with few jobs and conspicuous power and water use → costs land locally while returns accrue to external shareholders → visibility is asymmetric: residents see a monthly electricity bill and never see the AI revenue → under loss aversion, local politics responds with moratoria, special tariff classes for very large customers, water restrictions, and agreements conditioned on tax and employment → siting costs acquire a line item that was previously priced at roughly zero.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, major markets show almost no local moratoria, large-load tariff classes, or water restrictions aimed at data centres, and residential power-price disputes produce no policy consequences.
- **Original leading indicator**: Count of local moratoria or rejections, introduction of large-load tariff classes, water-permit conditions, terms trading employment and tax for power; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Consistent, and half of it has already happened early.** Agreement: the dedicated large-load tariff this card expected is not a future landscape but an accomplished institutional fact — PUCO approved AEP Ohio's data-centre-specific tariff in July 2025 with the explicit purpose of shielding residential ratepayers (EXT-22), and the Georgia PSC established risk-priced minimum-billing rules for loads above 100 MW in January 2025 (EXT-32). Two jurisdictions moved the same way independently, ahead of this card's 2031 window. **Divergence and evidence boundary**: the other half lacks evidence — no government or academic body systematically counts local moratoria or rejected siting applications, and the trackers that exist are commercial or crowdsourced with opaque methodology; water conflicts so far exist as individual undecided lawsuits (Georgia residents alleging harm to their water), not as an established pattern. Why the judgment is retained: kept with confidence at Medium rather than raised — raising it needs a systematic count of moratoria, not more anecdotes; and this card's falsifier should first be evaluated on the tariff half, where evidence exists, with moratoria and water restrictions treated as boundary evidence until a counting standard appears.
- **Original external comparison source**: EXT-22, EXT-32 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-061` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-062

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L49–L70`；`docs/en/ledger/61-70.md:L49–L70`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1492–L1510`
- **Current card anchor**: `docs/en/ledger/61-70.md:L49–L70`
- **Original title**: Heavy assets are taxable while the value layer is mobile, so local shares stay structurally low (landscape only)
- **Original one-sentence judgment**: What can be taxed is the immovable heavy asset while what earns the profit is the instantly mobile value layer, so the share captured locally stays structurally low (landscape only).
- **Original reasoning chain**: Taxation requires a visible, immovable presence inside the jurisdiction → data centres are immovable while profit and model weights are mobile → localities can reach power prices, property tax, and a little employment, but not profit → localities keep raising demands on the heavy asset while firms hedge through siting competition → a structural mismatch forms between the taxed asset and the untaxed value layer.
- **Original time window**: 2028–2035.
- **Original falsifier**: By 2035, taxation of compute services in major markets shifts from the asset side to the use side (for example broadly adopted usage or destination-based taxes covering AI services), giving localities a tax base commensurate with the load they carry.
- **Original leading indicator**: Withdrawal or conditioning of data-centre tax abatements, local levies based on electricity consumption, legislative progress on taxing AI services, revenue-sharing terms between localities and firms; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-061, J-039.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, but only half of it.** Agreement: Virginia's JLARC audit of the largest US data-centre market quantifies this card's first step — the sales and use tax exemption forgoes roughly $928 million of state revenue a year (FY23) with about 90% of the industry claiming it, local retention rests mainly on property tax, and the jobs in the economic-impact figures are heavily concentrated in the construction phase rather than permanent operations (EXT-28). Across states, 36 offer data-centre-specific tax breaks while only 11 disclose which companies receive them, and subsidy per job in tracked megadeals averages over $262,000 (EXT-31 — ⚠ advocacy organization, not a full sample). **Divergence and evidence boundary**: what is evidenced is only that heavy assets are taxable and the local share is low; the other half — profits and model weights being mobile so the value layer escapes — is addressed by no government or cross-state study, and this card's falsifier points at whether taxation shifts from the asset side to the usage side, where cloud and AI services are covered only by scattered state tax rulings with no systematic research. Why the judgment is retained: kept as landscape only, confidence not raised; upgrading it to a bettable judgment needs two things — a comparable measure of local retained revenue against the load borne, and legislative movement on usage-side taxation.
- **Original external comparison source**: EXT-28, EXT-31 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-062` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-063

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L71–L92`；`docs/en/ledger/61-70.md:L71–L92`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1511–L1529`
- **Current card anchor**: `docs/en/ledger/61-70.md:L71–L92`
- **Original title**: The geography of compute is decided by interconnection queues and permitting speed, not by electricity price
- **Original one-sentence judgment**: Until grid expansion catches up, the geography of compute is explained mainly by interconnection queues and permitting speed rather than by electricity price.
- **Original reasoning chain**: New generation and transmission run in years and cannot be compressed in the short term → whoever has existing spare substation capacity and fast approvals receives compute investment first → the value of queue position exceeds the tariff differential (J-057) → a region with higher power prices but a short queue can beat a region with cheap power and a long queue → the geographic distribution of new capacity diverges from the cheapest power.
- **Original time window**: 2026–2030.
- **Original falsifier**: By 2030, the regional distribution of new compute capacity correlates more strongly with regional electricity prices than with interconnection wait times.
- **Original leading indicator**: Regional distribution of new capacity compared against regional queue times and tariffs; publicly stated siting rationales; annual.
- **Original confidence**: Medium.
- **Original depends-on**: J-056, J-057.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **Mechanism confirmed, the comparison is unavailable, and one source misuse must be corrected.** Agreement: DOE records connection lead times of 1–3 years for hyperscale facilities (300–1000 MW+) and the resulting shift toward co-location with existing generation to get power faster — exactly this card's mechanism that access speed rather than price decides where compute lands (EXT-29); ERCOT's large-load backlog keeps growing and is the only public load-side ISO dataset (EXT-30); and Virginia's JLARC records development constrained by substation and transmission capacity in Northern Virginia, the largest US cluster (EXT-28). **Correction**: EXT-19 (LBNL *Queued Up*) covers generation and storage interconnection only and **does not cover load**, so it must not be used as evidence about data-centre siting — this is the most common source misuse in this area and is now flagged in the source index. **Evidence boundary**: this card's falsifier asks which better explains the regional distribution of new capacity, local electricity price or interconnection wait time, and no institution has published such a quantitative comparison, so the test cannot be computed from public data. Why the judgment is retained: the mechanism-side evidence is consistent and comes from official documents, so the judgment stands with confidence at Medium; one leading indicator is added — whether ERCOT-style load-side queue disclosure spreads to PJM, MISO and other markets, which determines when this card becomes falsifiable again.
- **Original external comparison source**: EXT-28, EXT-29, EXT-30 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-063` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-064

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L93–L114`；`docs/en/ledger/61-70.md:L93–L114`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1530–L1553`
- **Current card anchor**: `docs/en/ledger/61-70.md:L93–L114`
- **Original title**: If efficiency gains keep outpacing load growth, the constraint in this chain dissolves in the long run (landscape only)
- **Original one-sentence judgment**: If energy per unit of service keeps falling faster than load grows, and schedulable load can migrate freely across regions, this chain's power and permitting constraint dissolves on its own in the long run (landscape only).
- **Original reasoning chain**: The constraint holds only while load growth exceeds deliverable-capacity growth → if efficiency gains and cross-region scheduling both take effect, peak load growth flattens → the queue stops being the binding constraint → the certainty premium and site rents disappear with it.
- **Original time window**: 2033–2040.
- **Original falsifier**: By 2040, compute-related load in major markets still grows faster than deliverable capacity and interconnection wait times show no systematic decline.
- **Original leading indicator**: Ratio between the decline in energy per unit of service and the growth of compute service volume, peak load growth, share of cross-region scheduled jobs; annual.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-056, J-058.
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C3: Electrons on the Ground`.
- **Original external comparison**: **The counter-hypothesis is historically real, but current data points the other way.** Agreement (the side that favours this card): efficiency outrunning load is not wishful — between 2010 and 2018 global data-centre compute instances grew 550% while energy use rose only about 6%, a peer-reviewed eight-year decoupling window (EXT-27). **Divergence and evidence boundary**: the current phase runs the other way — LBNL measures US data centres at about 4.4% of national electricity in 2023 heading to 6.7–12% by 2028 (EXT-26), and the IEA puts data-centre electricity growth at roughly 15% a year over 2024–2030, more than four times the combined growth of all other sectors (EXT-12); decoupling has clearly weakened in the large-model phase. Beyond that, no authority has published a dedicated analysis of an efficiency turning point, and this card's 2033–2040 window lies past the forecast boundary of every source cited here. Why the judgment is retained: kept as this chain's most important counter-hypothesis and not as a basis for action, with confidence not raised; its value is in naming the condition under which this chain's constraint dissolves, not in predicting that it will.
- **Original external comparison source**: EXT-12, EXT-26, EXT-27 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-064` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-065

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L5–L26`；`docs/en/ledger/61-70.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L599–L617`
- **Current card anchor**: `docs/en/ledger/61-70.md:L5–L26`
- **Original title**: Once AI executes across ownership boundaries, the scarce item is not rollback software but the right to reverse
- **Original one-sentence judgment**: What is scarce is not sandbox and rollback software but the right to pull state back out of the counterparty’s ledger.
- **Original reasoning chain**: `J-004` treated “reversible infrastructure” as one scarce item → taken apart layer by layer under opportunity-durability gate’s third question → when the action does not cross an ownership boundary (your own database, your own cloud resources, a test sandbox), rollback is pure software, exactly what the force making generation abundant is best at producing, and the system being operated on is held by the platform itself, which has every incentive to bundle it and give it away → that half has payers but fails the opportunity-durability gate, so its exit is a window opportunity → when the action does cross an ownership boundary (payment, shipping, signing, transfer of rights), the state lands in the counterparty’s ledger and in legal rights the counterparty has acquired, so reversal must be consented to and executed by that party → whose default interest is finality: what it sells is finality, and reversal capacity is rationed and separately priced (dispute fees, escrow fees, issuance fees) → historically, cross-party unwind has actually been built only inside a handful of closed networks (card-scheme chargebacks, securities settlement reversal, escrow and letters of credit), each a product of membership rules, collateral, and long-running repeated games → compute can copy sandbox code without limit; it cannot copy the counterparty’s obligation to unwind → the hard constraint therefore lands on ownership/privacy and trust/relationship, not on irreversibility (which is only a supporting lens) → for physically irreversible actions (consumed, harmed, injected) no reversibility product exists at all and the residue belongs to the compensating party, see `J-005`
- **Original time window**: 2027–2033, as demand becomes explicit with the volume of cross-party agent execution
- **Original falsifier**: By 2033, cross-party reversal for machine-initiated actions (delayed-finality settlement, programmable escrow, unilateral rescission windows) has become a default rule of the major payment and settlement networks, is not priced separately, and the access layer has produced no identifiable independent supplier
- **Original leading indicator**: ① Whether programmable escrow / delayed-finality settlement products aimed at agents appear and are separately priced; ② whether chargeback and dispute windows are extended to machine-initiated transactions; ③ whether contract templates begin to carry a “unilateral rescission window for AI-executed clauses”; ④ whether platforms bundle within-boundary sandbox / rollback as a default capability (that one turning true only confirms that the Window List row has closed and is not evidence for this judgment); observed every six months
- **Original confidence**: Medium
- **Original depends-on**: J-001
- **Original status and lineage**: `REVISED` (2026-09-20 diffusion-gate review: fails Gate 1; the audience ceiling is the occupational/organizational scale stated above, so this card is downgraded to an occupational/organizational judgment and no longer reads as a society-level trend. The original card text is kept word for word and the identifier is not reused; for the test see `Historical retrospective · Gate 1`.)
- **Original source**: `C1 · What Becomes Unbuyable After Generation Becomes Free`.
- **Original external comparison**: Comparison not completed this round: unknown. This judgment was produced on the spot by the opportunity-durability review of 2026-09-19 and has not yet been compared against any external judgment; it is explicitly marked unknown per `00-method.md` §1.1 item 4, must not be used as if compared, and the three elements will be completed in the next round.
- **Original external comparison source**: Comparison not completed this round.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-065` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-066

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L115–L136`；`docs/en/ledger/61-70.md:L115–L136`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1880–L1898`
- **Current card anchor**: `docs/en/ledger/61-70.md:L115–L136`
- **Original title**: The five gates are necessary, not sufficient
- **Original one-sentence judgment**: If a capability fails any one of the five diffusion gates it will not become the way a whole society does things; passing all five only means it qualifies to compete, and guarantees nothing.
- **Original reasoning chain**: Three self-attack locks are set up first → the third lock demands a case that passes all five gates and still fails → New Coke, 1985, gate by gate: scale (people who drink cola daily number in the billions), substitution (replaces the old Coke — same act, same price, same shelf), carrier (same production line and distribution network, zero marginal deployment cost), decision rights (Coca-Cola decides to produce unilaterally, consumers buy unilaterally), cost (zero learning, zero bodily, zero social cost, and it won blind taste tests) → launched 1985-07-11, the old formula announced back 79 days later → what the gates missed is on the demand side: what people buy is not always the thing itself, Coke sells an identity symbol, and a symbol's value comes precisely from not changing → therefore this gate set can only disprove, never prove → the correct use is "fails a gate ⇒ will essentially not become society-wide," never "passes all gates ⇒ will happen."
- **Original time window**: 2026-01 to 2036-12 (the period over which this rule is applied and tested).
- **Original falsifier**: A capability that **clearly fails at least one** of the five gates nevertheless reaches society-wide diffusion within ten years (billions of people daily, or hundreds of millions weekly), and its diffusion cannot be explained by an unlock condition already written into this document.
- **Original leading indicator**: (1) Every six months, enumerate the capabilities that newly reached society-wide scale in that period, back-fill the five-gate verdict for each, and record whether any counter-example diffused while failing a gate; (2) whether every new society-level judgment written in this project can pass the five-gate test; (3) whether a second "passes all gates, still fails" case appears (that turning true strengthens this card rather than weakening it); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: J-067, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: Rogers 1962's five attributes of an innovation (EXT-33) overlap with this document's Gate 2 and Gate 5 at relative advantage and complexity respectively; Moore 1991 (EXT-35) likewise argues technical success is not the same as crossing into a mass market. **Divergence and evidence boundary**: Rogers's five attributes are scored (higher means faster diffusion); this document rewrites them as veto-style necessary conditions and requires naming a concrete object (which act is replaced, who pays for the carrier, whose hands the decision sits in). A scored framework is nearly unfalsifiable; a veto checklist can be falsified. **Why the judgment is retained**: the cost of the veto-style reading is that every negative verdict rides on the gate set being complete, a cost explicitly acknowledged through the New Coke counter-example and written into both this card and section 6 of the prose, so confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-33, EXT-35 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-066` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-067

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L137–L158`；`docs/en/ledger/61-70.md:L137–L158`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1899–L1917`
- **Current card anchor**: `docs/en/ledger/61-70.md:L137–L158`
- **Original title**: The audience ceiling of a capability is the headcount and frequency of the activity it serves
- **Original one-sentence judgment**: The upper bound on how many people a capability can affect is set by how many people perform the activity it serves and how often they perform it, not by the ceiling of the technology.
- **Original reasoning chain**: Enumerate the capabilities that reached society-wide scale, and the activities they serve were already billions-scale and daily before diffusion — smartphones (contacts, looking things up, finding the way, paying; 4.3 billion owners in 2023, 54% of world population), health codes (entering a venue), mobile payment (paying for something) → then enumerate the cases where the technology fully succeeded and still stalled at a niche, and the headcount of the activity served was already insufficient: Concorde (transatlantic passengers willing to pay several times the fare to save three or four hours, hundreds of thousands of trips a year; 20 aircraft built over 27 years, 14 in commercial service), Iridium (calling from places without cellular coverage; 55,000 subscribers at bankruptcy against a break-even in the millions), Esperanto (since 1887 the vast majority of people never once encounter a cross-native-language everyday conversation) → the technology worked in all three; the difference is only the headcount of the activity → therefore you must count people before assessing the technology → and ask one layer deeper: does it raise the ceiling of existing professionals (ceiling = the size of that occupation), or let people who previously could not do it do it (which may enlarge the activity itself).
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability whose served activity was performed by only millions of people before diffusion nevertheless reaches billions of daily users within five years, and that growth cannot be explained by "it let people who previously could not do it do it, thereby enlarging the activity's headcount itself."
- **Original leading indicator**: (1) Whether every new society-level assertion in this project states the order of magnitude and frequency of the activity's headcount; (2) every six months, observe the capabilities newly reaching billions scale and the pre-diffusion headcount of the activity they serve; (3) whether a counter-example appears in which the activity's headcount did not change while the audience exploded; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: diffusion research broadly accepts that adoption has a ceiling. **Divergence and evidence boundary**: this is a genuine gap in the literature — this round's search found no existing diffusion framework that uses "the headcount and frequency of the activity served" as a prior screening variable: Rogers's five attributes characterize the innovation itself (EXT-33), and Bass 1969 treats market potential m as an **exogenously given parameter** (EXT-38); neither asks how many people actually perform the activity, which is exactly the quantity Gate 1 asks about. **Why the judgment is retained**: three failure cases (Concorde, Iridium, Esperanto) all succeeded technically and share exactly one feature — insufficient headcount for the activity — and that shared feature is enough to support the judgment; but because no external framework has ever calibrated it, confidence is no higher than Medium.
- **Original external comparison source**: EXT-33, EXT-38 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-067` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-068

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L159–L180`；`docs/en/ledger/61-70.md:L159–L180`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1918–L1936`
- **Current card anchor**: `docs/en/ledger/61-70.md:L159–L180`
- **Original title**: What diffuses replaces an activity already happening, not something added on top
- **Original one-sentence judgment**: Capabilities that diffuse all replace one concrete activity the user already performs today; anything that replaces nothing and merely adds one more thing is capped at hobbyists.
- **Original reasoning chain**: Adopting a new capability costs a fixed price in learning, purchase and process change → that price only pays off when there is an old activity to offset it against → replace nothing and the benefit must justify itself from scratch, so adoption runs on curiosity alone, and the stock of curiosity is exactly the headcount of hobbyists → passing side: containerization replaced break-bulk loading ($5.83 per ton in 1956 → 15.8 cents per ton, roughly a 97% drop), China's household responsibility system replaced work-point accounting (same land, same people; what changed was who bore the monitoring cost), QR-code payment replaced pulling out cash, making change and reconciling → blocked side: Google Glass replaced no activity and instead added a thing on your face ($1,500 in 2013, withdrawn January 2015), 3D television added an extra-cost attribute to "watching television" (ESPN 3D launched 2010-06-11, closed 2013-09-30), MOOCs **replaced the wrong object** — they replaced attending lectures, while what students buy is the credential, and the credential was not replaced at all (median completion rate of 12.6% in peer-reviewed work) → the veto condition is therefore exactly one: replaces nothing; the size of the cost drop is not a pass mark but a speed variable.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability that **replaces no existing concrete activity and is purely additive** reaches society-wide diffusion within five years (billions daily or hundreds of millions weekly), and its adoption is driven neither by coercion nor by a single subsidizing party.
- **Original leading indicator**: (1) Whether every new judgment can name the concrete, countable activity, already happening at the time, that it replaces; (2) the split between "purely additive" and "substitutive" among the period's fast-growing products; (3) whether new cases of replacing the wrong object appear (the surface activity replaced while what the user actually buys is not); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: heavily overlapping with relative advantage among Rogers 1962's five attributes (EXT-33); diffusion research has long accepted relative advantage as an explanatory variable for diffusion speed. **Divergence and evidence boundary**: this document rewrites it from a scored dimension into a veto condition, and narrows the veto condition to the single item of substitution versus addition — the size of the cost drop is explicitly demoted to a speed variable, because this document's own passing case (the household responsibility system) did not cut unit cost by an order of magnitude, and writing an order of magnitude into the pass mark would have this gate falsified by its own evidence. **Why the judgment is retained**: this narrowing is a proactive correction made before landing, at the cost of weakening Gate 2's power to say no (it can now only block the purely additive), which is stated in section 3 of the prose; confidence therefore stays at Medium.
- **Original external comparison source**: EXT-33 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-068` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-069

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L181–L202`；`docs/en/ledger/61-70.md:L181–L202`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1937–L1955`
- **Current card anchor**: `docs/en/ledger/61-70.md:L181–L202`
- **Original title**: Infrastructure that serves only one capability does not get built
- **Original one-sentence judgment**: If the new infrastructure a capability requires has no second use and no independent revenue source, that infrastructure either does not get built, or the capability must wait until someone else builds it for other reasons.
- **Original reasoning chain**: The 1964 Picturephone needed dedicated broadband loops and dedicated terminals, and that equipment had no second use beyond Picturephone → AT&T had to bear the entire cost alone and recover it from a user base that did not yet exist → Pittsburgh peaked at 32 sets and Chicago at 453, under 500 in total → video calling in 2020 required no dedicated infrastructure whatsoever: front cameras, broadband and screens were already in billions of pockets **for other reasons**, and the adopter's marginal hardware cost was zero → Zoom's daily meeting participants went from 10 million to 300 million in three months → the demand had not changed and the technology had not changed; what changed was who paid for the carrier → contrast: US television broadcast towers genuinely were newly built dedicated infrastructure, but they had an independent revenue source (advertising), so they got built (household ownership roughly 1% in 1948 → roughly 75% in 1955); health codes ran inside the already-installed Alipay and WeChat and made nobody install a new app → counter-example side: Iridium's 66 satellites plus dedicated handsets cost roughly $5 billion and existed for one thing only; Better Place's battery swapping needed both a station network and redesigned cars, and went bankrupt in May 2013 after raising about $850 million.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A capability requiring wholly new dedicated infrastructure that has neither a second use nor an independent revenue source, and for which no single party pays in full, nevertheless reaches society-wide diffusion within ten years.
- **Original leading indicator**: (1) Whether every judgment with a time window answers "who pays for the carrier"; (2) among the capabilities currently blocked, whether the resistance can be attributed to a missing carrier; (3) whether events of the form "the carrier got built for other reasons" unlock an existing judgment (such events are the trigger for revising time windows); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: the literature has adjacent concepts — Teece 1986's complementary assets, installed base in the network-effects literature, and Zittrain 2006's generativity (EXT-37). **Divergence and evidence boundary**: those answer "who can profit from an innovation" and "why general platforms grow unanticipated applications," whereas Gate 3 asks a prior existence question: will this dedicated infrastructure be built at all. This round found no existing framework that poses that question on its own. **Why the judgment is retained**: Picturephone 1964 versus 2020 is a natural control pair — same demand, same technology, different carrier — and the mechanism is clear enough; but because the merger risk between Gate 3 and Gate 4(b) has not been ruled out, confidence is no higher than Medium.
- **Original external comparison source**: EXT-37 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-069` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-070

**Current pair / 当前双语卡片**：`docs/zh/ledger/61-70.md:L203–L223`；`docs/en/ledger/61-70.md:L203–L223`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1956–L1974`
- **Current card anchor**: `docs/en/ledger/61-70.md:L203–L223`
- **Original title**: When many parties must change together, change needs enforceable and observable authority, a single subsidizing party, or a local closed loop
- **Original one-sentence judgment**: If adoption requires many parties to change at once, change moves beyond pilots only when one of three holds: a party that can both compel and observe compliance, a single party able to subsidize everyone's start-up cost at once, or a local closed loop that need not wait for the whole society.
- **Original reasoning chain**: Adoption decidable by one party passes automatically (ATMs: the bank deploys unilaterally, the depositor uses unilaterally; Barclays Enfield, 1967-06-27) → when many parties must change at once, each party's optimal strategy is to wait, so it stalls at pilots → unlock path (a) enforceable and observable: health codes could both be compelled and be seen being enforced at every venue entrance, rolled out nationwide in months; the household responsibility system went from 18 households in Xiaogang in 1978 → 51% of production teams in Anhui by end-1979 → the 1982 Central Document No. 1 → full rollout in 1983 → the other half of (a), by contradiction: Prohibition could compel but could **not see** — roughly 1,520 federal agents for a population of 106 million (about one per 70,000), with 30,000 to 100,000 speakeasies in New York City alone; repealed in 1933 → unlock path (b) a single subsidizing party: the 1958 BankAmericard Fresno drop mailed roughly 60,000 pre-activated cards to residents who had not applied, buying an entire city's start-up cost outright off its own balance sheet → unlock path (c) a local closed loop: the 1975 US Metric Conversion Act said in so many words that conversion was "wholly voluntary," with no deadline and no penalty; the Metric Board was abolished in 1982 and everyday life never converted, **yet science, medicine and the military use metric completely** — both sides of (c) appear inside the same case.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: A case of adoption requiring many parties to change at once reaches society-wide diffusion while **none** of the three unlock paths holds.
- **Original leading indicator**: (1) Whether every judgment involving coordination names the holder of decision rights and the unlock path; (2) among coordination-type capabilities stalled at pilots, whether the blockage can be attributed to the absence of all three paths; (3) whether large-scale coordination is ever completed spontaneously by network effects alone (that turning true triggers the falsifier directly); observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: consistent with Olson 1965, *The Logic of Collective Action* — rational self-interested individuals do not automatically act for a common interest unless the group is small or coercion and selective incentives exist (EXT-36); this document's three unlock paths map one-to-one onto Olson's coercion, selective incentives and small groups. Also consistent with the path-dependence and network-externality literature (EXT-34): the value of adopting depends on whether others adopt, which is exactly the source of difficulty in multi-party coordination. **Divergence and evidence boundary**: this document's increment is the half-clause inside (a) that enforcement must be observable — Olson discusses coercion, not the observability of coercion; that half comes from contrasting Prohibition (could compel, could not see, failed) with US metrication (no compulsion, no penalty, failed). **Why the judgment is retained**: that half-clause is supported by two cases pointing in opposite directions, but observability has never been tested on its own by any external framework, and the completeness of the three paths is in doubt (see the opposing mechanism), so confidence stays at Medium.
- **Original external comparison source**: EXT-34, EXT-36 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-070` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-071

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L5–L30`；`docs/en/ledger/71-80.md:L5–L30`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1975–L1997`
- **Current card anchor**: `docs/en/ledger/71-80.md:L5–L30`
- **Original title**: Recurring net burden, not gross friction, sets the voluntary-adoption ceiling
- **Original one-sentence judgment**: Voluntary adoption must compare **recurring net burden relative to the real incumbent**: added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost. Only a positive, material burden that accumulates with frequency pushes the ceiling far below the activity population.
- **Original reasoning chain**: The old rule treated any per-use friction as burden → Piggly Wiggly's 1916 self-service store made shoppers repeatedly walk the aisles, compare, and pick goods, yet expanded rapidly and helped make self-service the supermarket's basic form (EXT-55) → therefore recurring labor alone cannot veto adoption; the ledger must subtract waiting, price, time, and process savings from it → the failure side remains: contact lenses add repeated insertion and care relative to frames, 3D television adds glasses and viewing-position constraints, and Google Glass adds recurring social friction → seat belts show that compulsion can bypass voluntary net burden → the current rule vetoes only when **voluntary adoption carries a positive, material recurring net burden**.
- **Original time window**: 2026-01 to 2036-12.
- **Original falsifier**: Under voluntary adoption (no compulsion, no ongoing subsidy), a capability with a materially positive recurring net burden versus the real incumbent reaches majority adoption (>50%) of the population performing the activity within ten years; or calibration cannot find a case stopped only by recurring net burden rather than Gate 2 replacement.
- **Original leading indicator**: (1) whether new judgments record both added friction and saved waiting / price / time / process cost; (2) whether failure cases' net burden can be computed from as-of evidence; (3) whether high-retention products sustain a materially positive recurring net burden; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: —
- **Original status and lineage**: REVISED (2026-09-21 Gate 5 narrowed; v1 snapshot retained and counted in the calibration denominator).
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: **Agreement**: partly overlaps Rogers 1962's complexity and relative advantage (EXT-33). **Divergence and evidence boundary**: this card turns per-use net burden into a necessary-condition veto, whereas Rogers uses scored attributes; self-service retail refutes the gross-friction version but does not by itself prove the net-burden version. **Why the judgment is retained**: success-side self-service retail and failure-side contact lenses / 3D television / Google Glass force net accounting, but do not justify raising confidence.
- **Original external comparison source**: EXT-33, EXT-39, EXT-40, EXT-55, EXT-65, EXT-66 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-071` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-072

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L31–L54`；`docs/en/ledger/71-80.md:L31–L54`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L1998–L2022`
- **Current card anchor**: `docs/en/ledger/71-80.md:L31–L54`
- **Original title**: Choosing one from dozens of generated candidates is an occupational judgment, not a society-level trend
- **Original one-sentence judgment**: The activity "faced with a batch of already-generated candidates, pick one and own the outcome" is performed by a global population in the millions at weekly frequency, so any scarcity derived from it is an occupational judgment and must not be written in a society-level voice.
- **Original reasoning chain**: Define the activity — faced with a batch of already-generated candidates, pick one and own the outcome → whoever performs it must satisfy three conditions at once: an occupation that requires producing candidates in batches (advertising and marketing creative, design and product, architectural and engineering schemes, consulting proposals), personal authority to decide rather than to execute, and a frequency of at least once a week → people satisfying all three concentrate in the decision layer of those roles, and by role structure the global order of magnitude is 10⁶ at weekly frequency → gate by gate: Gate 2 passes (replaces "make three versions first, then choose among the three"), Gate 3 passes (rides on already-diffused generation tools), Gate 4 passes (one person decides unilaterally), Gate 5 is borderline (candidates to review go from 3 to 60, so the attention cost rises), **Gate 1 fails** (millions at weekly frequency, two to three orders of magnitude below the society-wide threshold of billions daily or hundreds of millions weekly) → what actually passes Gate 1 on the same chain is not choosing but making: "needing a usable document, diagram, copy or program" is something billions of people occasionally need, and most of them previously could not do it, which belongs to the "lets people who previously could not do it do it" class.
- **Original time window**: 2026-01 to 2031-12.
- **Original falsifier**: By the end of 2031, citable statistics show that the population who "pick one from batch candidates and own the outcome" has reached hundreds of millions at weekly-or-higher frequency, or the activity is shown to have spread into the everyday decisions of non-professionals.
- **Original leading indicator**: (1) Whether citable global role statistics appear that could replace this card's constructed estimate; (2) whether "generate dozens of candidates at once for the user to pick from" becomes the default interaction in consumer products (that turning true enlarges the activity's headcount and strikes this card directly); (3) whether downstream judgments in this project's C1 chain that depend on "choice becoming scarce" have had their audience voice narrowed per this card; observed every six months.
- **Original confidence**: Medium.
- **Original depends-on**: J-066, J-067.
- **Original status and lineage**: ACTIVE.
- **Original source**: `Retrospect: What It Takes to Become a Society-Wide Habit`.
- **Original external comparison**: Comparison not completed this round: unknown. This card's audience magnitude comes from a constructed estimate; no citable global role statistics were obtained this round and it was not compared against any external judgment. Per `00-method.md` §1.1 item 4 it is explicitly marked unknown, must not be used as compared, and the three elements are to be completed next round.
- **Original external comparison source**: Comparison not completed this round.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-072` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-073

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L55–L76`；`docs/en/ledger/71-80.md:L55–L76`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2023–L2041`
- **Current card anchor**: `docs/en/ledger/71-80.md:L55–L76`
- **Original title**: Embodied intelligence is the necessary complement for AI to reach the physical-labour population, not a sufficient condition for diffusion
- **Original one-sentence judgment**: As long as AI can only move information, Gate 1 holds its audience ceiling down to "the share of people whose work surface is a screen"; being able to move mass, be present on site, and touch a human body is the **necessary complement** that changes that denominator, but changing the denominator only opens Gate 1 — Gates 2 through 5 do not open automatically as model capability improves, so embodiment is **not** a sufficient condition for society-level diffusion.
- **Original reasoning chain**: Gate 1's test is a single sentence — how many people perform the activity this capability serves, and how often → people whose work surface is a screen and whose output is information are a **minority** of global employment (the best-paying roles, but not most of the population); the population sits where someone must move mass, stay on site, or touch another person's body: agricultural employment is still **hundreds of millions** (EXT-41), domestic workers are a separately counted group in the **tens of millions** (EXT-42), and in the United States alone hand material movers and home health aides are each **millions**-scale occupations (EXT-43) → therefore an AI that can only move information has its ceiling pinned to screen professionals; inside that ceiling it can be an excellent business, but by the diffusion-gate reading it will never become the way a whole society does things → the only route to a different denominator is to extend what AI can move from bits to mass → **but changing the denominator only opens Gate 1**: Gate 2 demands replacing an activity already performed today (the transfer robot replaced "lifting," not "being there," and what the buyer buys is the latter); Gate 3's carrier is physical space itself (corridor widths, floor flatness, connector standards, workcell retrofits, row spacing — nobody has built any of it for other reasons); Gate 4 requires nurses, families, insurers and regulators to nod at once; Gate 5's preparation, supervision, cleaning, fault handling and social awkwardness are paid on every use and never amortize → then the two curves: perception and policy fall along the software curve (fast variable), while actuators, reducers, torque sensors, batteries, deployment hours and priced liability fall along industrial and institutional curves (slow variables, typically single-digit percent per year) → the binding constraint therefore migrates from "model capability" to **cost per task + priced liability + deployment hours** → **when cost per task crosses labour**: only in squares that are structured, high-frequency, and whose object is semi-cooperative or inanimate does it cross first (milking, pallet handling, goods-to-person, fixed-station welding and painting; 2026–2030); squares that are unstructured but whose environment can be rebuilt cross at 2028–2034; touching human bodies and one-off sites cross at 2032–2040, and first in institutions and on job sites rather than in homes; open-ended household tasks do not cross inside this window → and crossing only means procurement departments start doing the arithmetic, not that the practice diffuses: **beating labour cost locally ≠ society-level diffusion** → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (every warehouse, plot and dwelling is a private, non-identical on-site input that compute cannot copy); neither can be copied away by the same force that produced the abundance.
- **Original time window**: 2026–2040.
- **Original falsifier**: By the end of 2035, citable statistics show that the repeat users of some **purely informational** capability (moving no mass, never present on site, never touching a body) are no longer mainly people whose work surface is a screen, and that they number a billion daily or hundreds of millions weekly — that falsifies the "embodiment is the necessary complement" half. The other half has its own test: if by the end of 2033 cost per task for embodied systems falls in step with model capability (no longer decoupled from the software curve), deployment hours per unit fall markedly with cumulative installed base, and a generally available insurance product with quotable rates covers embodied work, then the "not a sufficient condition" half should be narrowed.
- **Original leading indicator**: (1) the time series of cost per task for embodied systems (per piece, per effective operating hour) and whether it is decoupled from the model-capability curve; (2) dedicated insurance products, quotable rates, and the first liability rulings for embodied work; (3) the learning curve of deployment hours per unit against cumulative installed base, and the ratio of integrator service revenue to equipment revenue; (4) whether headcount and wages in occupational series (EXT-43's 53-7062 and 31-1121) diverge in adoption-dense regions ahead of the national series — a US-only observation window that must not be used as a global indicator; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-006, J-066, J-067, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **The mechanism agrees, but external sources only reach the two ends; nothing calibrates the arrival order in between.** Agreement: IFR reports that factory demand for robots doubled over ten years (EXT-45), which proves embodied capability **can** genuinely diffuse; Abundant Robotics shut its business down after reaching field-capable apple harvesting (EXT-46), which proves **technical feasibility is not commercial feasibility** — the second point coincides closely with this chain's independent reasoning and must be labelled honestly: **it is not this card's discovery; this card's increment is a structural explanation of such failures (utilization × fragmentation) plus observable leading indicators.** **Divergence and evidence boundary**: most external material discusses **installed totals** or **single cases**, while this card is about **arrival order** and **where the constraint sits**, and the former does not imply the latter; the key data not obtained this round is recorded as explicit gaps — cost-per-task time series by scene, insurance rates and liability rulings for embodied work, the learning curve of deployment hours per unit, and deployment scale and retention in care — none of which has a publicly checkable definition, so this card **uses** no precise global figure at all. **Why the judgment is retained**: the core argument depends on none of those missing numbers; it depends on an objective structural difference — perception and policy fall along the software curve while actuators, deployment and liability fall along industrial and institutional curves — and the gap between those slopes can be observed. But because nobody has calibrated the arrival order in between, confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-41, EXT-42, EXT-43, EXT-45, EXT-46 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-073` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-074

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L77–L98`；`docs/en/ledger/71-80.md:L77–L98`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2042–L2060`
- **Current card anchor**: `docs/en/ledger/71-80.md:L77–L98`
- **Original title**: Contact transfer in care crosses inside institutions first, and homes reach no society-level diffusion inside this window
- **Original one-sentence judgment**: Care is the square with the most certain demand, but what blocks it is not "can it lift" — it is "the person is alive throughout" plus the cost paid afresh on every single use; contact bed-to-chair transfer becomes standard institutional equipment no earlier than 2032–2038, and first in the handful of countries with the highest labour costs and heaviest nursing-injury compensation exposure, while home settings reach no society-level diffusion inside this window (to 2040).
- **Original reasoning chain**: Demographics make care the most certain demand (the number of people needing care rises, the number willing to do the work falls), and the gap cannot be closed by processing information — nobody lifts an elderly person from a bed into a wheelchair through a screen → the technical bottleneck is not load but that the person is alive: the same transfer needs a completely different torque trajectory for different weights, muscle tone and pain tolerance, and the person shifts posture, resists, or suddenly goes slack, which demands millimetre-scale position accuracy and newton-scale force control in one loop bounded by a human safety margin → Riken's ROBEAR demonstrated the capability side clearly in 2015 (EXT-44), and a decade later it is still not standard ward equipment: **the decade of silence is itself the evidence that what blocks this square is not capability** → what blocks it is Gate 5: preparation, supervision, cleaning, explaining and reassuring are paid every time and never amortize (the machine sent back in the chain's opening section completed twelve transfers in its first week with no pinch injury, and price appears nowhere in the reason it was returned) → compounded by Gate 3: a home additionally needs door widths, floors and bathrooms rebuilt, and nobody has built them for other reasons → compounded by Gate 4: putting a robot in a ward needs nurses, families, insurers and regulators to nod at once → **when cost per task crosses labour**: it is entirely plausible that a large institution in a high-wage country pushes the per-transfer cost below the wage cost of two aides, and at that moment the numbers work — while Gates 5 and 3 still stand in the way, so **crossing only means the procurement department starts doing the arithmetic, not that the practice reaches most of the people receiving care** → **Hard constraints**: **embodied presence** (the need itself requires someone to be physically there and to touch) compounded by **law / liability** (a party capable of being sued must carry a transfer accident); automating rostering, medication checks and fall-risk scoring completely removes not one transfer that must physically happen.
- **Original time window**: 2026–2038.
- **Original falsifier**: By the end of 2031, contact bed-to-chair transfer robots are standard institutional equipment in any major care market (verifiable through a reimbursement code, counting equipment against required staffing, or national installed-base coverage) — that falsifies this card's lower bound; or, before 2040, home contact transfer reaches daily use in hundreds of millions of households — that falsifies this card's home judgment.
- **Original leading indicator**: (1) whether regulators open a distinct approval pathway for contact transfer robots and whether a reimbursement code exists — without reimbursement, institutions buy from their own budget and the adoption curve stays flat; (2) whether staffing standards allow equipment to be counted against required headcount (that is the line that decides ROI, not the purchase price); (3) whether back-injury compensation rates fall in institutions with dense adoption — the hardest indicator to fake, because insurers rather than vendors produce it; (4) whether a production successor to a ROBEAR-class prototype ever appears; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: a ROBEAR-class prototype (EXT-44) proves the capability side of contact transfer was demonstrated a decade ago, which is the premise for "the silence cannot be explained by capability"; US occupational data lists home health aides among the fastest-growing occupations (EXT-43), consistent with "the most certain demand." **Divergence and evidence boundary**: the external material establishes one prototype and one country's occupational outlook, and covers no **arrival order**; this round found no checkable source on whether a production successor to ROBEAR exists, and none on deployment scale or retention in care worldwide — both recorded as gaps; EXT-43 covers the United States only and cannot be extrapolated globally. **Why the judgment is retained**: the argument depends on no deployment-scale figure; it depends on recurring costs that do not amortize and on a compensable party that must be suable, neither of which opens as model capability improves. But with deployment and retention data missing, confidence stays at Medium.
- **Original external comparison source**: EXT-43, EXT-44 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-074` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-075

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L99–L120`；`docs/en/ledger/71-80.md:L99–L120`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2061–L2079`
- **Current card anchor**: `docs/en/ledger/71-80.md:L99–L120`
- **Original title**: Warehousing's bottleneck has moved from moving to grasping: unstructured picking arrives first and door-to-door delivery does not hold inside this window
- **Original one-sentence judgment**: Warehousing is where embodied intelligence pencils out first (goods feel no pain, the building belongs to one legal entity, the floor is flat), and what is actually stuck is the cost of the failure tail in unstructured picking; scaled single-item picking in controlled large warehouses sits conservatively at 2028–2033, while door-to-door last-mile delivery does not hold inside this window because it trips Gate 3 and Gate 4 at once.
- **Original reasoning chain**: Autonomous mobility inside a structured warehouse is largely a solved problem (flat floors, mappable paths, stop-on-anomaly) → what is stuck is **unstructured picking**: mixed SKUs, transparent and reflective packaging, soft polybags, occluded stacks, the last item at the bottom of a tote → the difficulty is not average success rate but **the cost of the failure tail**: a missed grasp costs seconds, a mis-pick costs a rework of the whole fulfilment chain plus reputation → so the engineering target is not "can it pick" but picks per hour, error rate, and who takes over after a failure → structured movement, pallet handling and goods-to-person are already diffusing (continuing through 2026–2028), while scaled unstructured single-item picking in controlled large warehouses sits conservatively at 2028–2033 → door-to-door delivery faces stairs, entry systems, rain, dogs and unattended parcels: the carrier is someone else's stairwell (Gate 3) and building management, residents and platforms must all change (Gate 4), so it does not hold inside this window → **when cost per task crosses labour**: a single high-throughput, single-shift, tidy-SKU warehouse already pencils out, and the test is whether **per-pick pricing** appears (per picked item, with error-rate damages) — a vendor willing to price its own failure tail is the most honest signal of maturity → but the tail of global warehousing is small and mid-sized sites: low throughput, mixed goods, seasonal swings, a day of downtime hitting every order, so **capex does not amortize and downtime risk cannot be spread — and that is exactly where most material-handling jobs are**; treating the large-warehouse case as the sector's case inverts Gate 1, counting how many warehouses a machine can enter rather than how many people's activity it can replace → **Hard constraints**: **physical** (mass must move, time and energy must be spent) compounded by **ownership / privacy** (layout, SKU master data and order flow are private assets, any retrofit needs the owner's consent, and negotiation cost does not fall with model capability).
- **Original time window**: 2026–2033.
- **Original falsifier**: By the end of 2028, unstructured single-item picking is operating at scale in controlled large warehouses (per-pick pricing with error-rate damages having become the mainstream commercial model in that segment) — that falsifies this card's mid-segment window; or by the end of 2033 robotic door-to-door delivery is the mainstream delivery mode in any major market (a majority of that market's parcels) — that falsifies this card's last-mile judgment.
- **Original leading indicator**: (1) whether the commercial model shifts from selling machines to **per-pick pricing** with error-rate damages; (2) whether third-party logistics insurance quotes a separate rate for robotic picking; (3) whether deployment hours per site fall as the installed base grows; (4) whether hiring volumes and wages in occupations like O\*NET 53-7062 (EXT-43) diverge in adoption-dense regions ahead of the national series; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: US occupational data proves that "hand laborers and freight, stock and material movers" really is a millions-scale occupation with an official definition to cite (EXT-43), which supports the existence of this card's denominator and the use of headcount and wages as leading indicators. **Divergence and evidence boundary**: EXT-43 covers the United States only and cannot be extrapolated globally; this round obtained no public figures on the installed base of unstructured picking, the penetration of per-pick contracts, or deployment hours per site, so this card gives no precise numbers at all — only arrival order and observable indicators. **Why the judgment is retained**: the cost of the failure tail and the per-owner negotiation cost are both independent of model capability, and the mechanism is clear; but with no public data on the key indicators, confidence stays at Medium.
- **Original external comparison source**: EXT-43 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-075` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-076

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L121–L142`；`docs/en/ledger/71-80.md:L121–L142`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2080–L2098`
- **Current card anchor**: `docs/en/ledger/71-80.md:L121–L142`
- **Original title**: Manufacturing's one real scaling passed through Gate 4's local closed loop; flexible assembly and high-mix low-volume are still outside the gate
- **Original one-sentence judgment**: Manufacturing is the only scene where "robots already scaled" can be cited directly, but that scaling passed through Gate 4's clause (c), the local closed loop, and happened only inside one set of boundary conditions — repetitive motions, rigid workpieces, calibratable positions, fixed takt; flexible assembly becoming routine on high-volume lines sits conservatively at 2028–2034, and high-mix low-volume small and mid-sized manufacturers hold inside this window only locally, in the few industrial clusters with dense integrator ecosystems, which is not society-level diffusion.
- **Original reasoning chain**: IFR reports that factory demand for robots doubled over ten years (EXT-45) → that fact must be used in both directions: it proves embodied capability really can diffuse, and it **draws the boundary conditions under which the diffusion happened** → diffusion happened in welding, painting, machine tending and palletizing (repetitive motions, rigid workpieces, calibratable positions, fixed takt) and did not happen in flexible assembly (a wire harness must be routed as it deforms, a connector must know how far to back off and retry when it will not seat, every soft gasket has a different tolerance; humans work on immediate tactile feedback while machines need force control plus tolerance compensation, and today that stack costs disproportionately in both hardware and commissioning hours) → the subtler bottleneck is **changeover**: a high-volume single-product line amortizes one teaching pass, a high-mix low-volume shop does not, because every product change means reprogramming, recalibrating and re-validating safety → which is why robot density correlates far more strongly with **batch size** than with wage levels → **when cost per task crosses labour**: it crossed long ago on lines with large enough batches and fixed takt (that is what the IFR curve means), and it does not cross in high-mix low-volume work because too few pieces amortize one teaching pass → but look at which gate that scaling passed: **Gate 4's clause (c), the local closed loop** — a single factory can make it work internally without waiting for society; **a factory can close the loop because it is a walled space with one decision-maker and one standard, and care, agriculture, construction and homes have no such wall** → extrapolating the factory's diffusion rate to the other four squares assumes that wall is free → **Hard constraints**: **physical** compounded by **ownership / privacy** (a production line is a specific owner's private asset, the retrofit is theirs to authorize, and the lost output during the retrofit is theirs alone to absorb).
- **Original time window**: 2026–2034.
- **Original falsifier**: By the end of 2030, the **composition** of new installations in IFR-class series shows assembly and precision manipulation exceeding handling and palletizing, and high-mix low-volume small and mid-sized manufacturers diffuse in step (evidenced by systematically falling changeover time and a falling ratio of integrator service revenue to equipment revenue) — that falsifies "flexible assembly at 2028–2034, high-mix low-volume slower."
- **Original leading indicator**: (1) whether the **composition** of new installations in series like IFR's tilts toward assembly and precision manipulation — reading totals alone mistakes palletizing growth for an assembly breakthrough; (2) whether line changeover time falls systematically; (3) the ratio of integrator service revenue to equipment revenue (a ratio that stays high says deployment cost is still carried by on-site labour and the scale effect has not arrived); (4) the residual-value curve for used industrial robots (high residuals signal redeployability, the signal that fragmentation is being overcome); annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: IFR is the only directly citable evidence of scaling in this chain (EXT-45), and it supports the existence of the premise that embodied capability can genuinely diffuse. **Divergence and evidence boundary**: IFR's series is an **installed total**, while this card is about **arrival order and boundary conditions**, and a total does not imply a composition; this round obtained no public series for new-installation composition by application type, changeover time, or used-robot residual values — all three recorded as gaps. **Why the judgment is retained**: the boundary conditions (repetitive motion, rigid workpiece, calibratable, fixed takt, one decision-maker) can be read off by contrasting where diffusion happened with where it did not, and the mechanism is clear; but with the composition breakdown missing, confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-45 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-076` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-077

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L143–L164`；`docs/en/ledger/71-80.md:L143–L164`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2099–L2117`
- **Current card anchor**: `docs/en/ledger/71-80.md:L143–L164`
- **Original title**: In agriculture what crossed is milking, not harvesting: seasonality and fragmentation hold cost per task above labour
- **Original one-sentence judgment**: Automatic milking is already standard equipment on mid-to-large dairy farms in high-wage countries because the action repeats daily, the location is fixed, the animal walks into the machine by itself, the output is measurable and failure is contained; selective harvesting stays at local pilots on single crops inside this window and does not become a mainstream practice before 2030, because seasonality crushes the denominator while fragmentation inflates the adaptation cost.
- **Original reasoning chain**: Start with milking, which crossed, and list the conditions to see how strict they are — the action repeats two or three times a day, the location is fixed, **the animal walks into the machine by itself**, the output is measurable and priceable, and failure is contained (one missed cow); **a cow is a semi-cooperative object, and that condition is close to a free subsidy** → then selective harvesting, which failed: Abundant Robotics took apple harvesting to the point of working in orchards and still shut the business down (EXT-46) → this is not a capability story but a **utilization** story: a harvester works a few weeks a year and its capex must amortize over those weeks' operating hours, while row spacing, tree architecture and variety differ between orchards so every new customer means re-adaptation → **seasonality crushes the denominator, fragmentation inflates the adaptation cost in the numerator — squeezed from both ends, cost per task does not fall** → three further technical bottlenecks: perception robustness under natural light and occlusion, end effectors handling damageable produce (a bruised apple is downgraded, a strawberry more so), and biological variation (no two fruits on one tree share a position or a ripeness) → **when cost per task crosses labour**: only on structured operations that are high-frequency, fixed and semi-cooperative (milking, guided seeding and fertilizing, intra-row mechanical weeding; 2026–2030 is the scaling window); selective harvesting can cross only after annual effective operating hours rise markedly through cross-crop, cross-season reuse → globally, most of the potential object of agricultural embodiment is not on capital-intensive farms in high-wage countries at all (EXT-41), which puts society-level diffusion a generation behind equipment feasibility → so "agricultural robotics is proven" is a dangerous sentence: **what is proven is milking, not harvesting** → **Hard constraints**: **physical** (the machine must move through a field, bounded by weather and a seasonal window; energy and time are incompressible) compounded by **ownership / privacy** (each plot and orchard is a private, unique physical layout that compute cannot copy).
- **Original time window**: 2026–2030.
- **Original falsifier**: By the end of 2030, selective harvesting is the mainstream practice for a major crop in any major growing region — evidenced either by machine harvesting taking a majority of that crop's harvested volume in that region, or by per-acre or per-yield harvesting services earning repeat business at scale.
- **Original leading indicator**: (1) whether harvesting equipment earns **repeat business** under a per-acre or per-yield service model (repeat orders say more than first orders about whether the numbers work); (2) whether **annual effective operating hours** per machine rise (cross-crop, cross-season reuse is the only route that rescues utilization); (3) whether seasonal wages diverge in adoption-dense growing regions ahead of the national series; (4) whether insurers or grower cooperatives offer products covering yield loss from machine operation; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: Abundant Robotics shutting down after the technology worked (EXT-46) supports "technical feasibility is not commercial feasibility"; FAO's employment indicators support agricultural employment still being hundreds of millions with a markedly higher share in low- and middle-income countries (EXT-41), which supports where this card places the denominator. **Divergence and evidence boundary**: EXT-46 is a single company case and constitutes no statistic over the class; FAO is used for **orders of magnitude** only, with its definitions, years and statistical boundaries as given in the source; this round obtained no installed-base or repeat-purchase data for harvesting equipment. **Why the judgment is retained**: milking versus harvesting is a natural control pair inside one industry in one period, and the crossing conditions (high frequency, fixed location, semi-cooperative object) can be checked one by one; but with only a single case on the failure side, confidence stays at Medium.
- **Original external comparison source**: EXT-41, EXT-46 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-077` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-078

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L165–L186`；`docs/en/ledger/71-80.md:L165–L186`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2118–L2140`
- **Current card anchor**: `docs/en/ledger/71-80.md:L165–L186`
- **Original title**: Construction and domestic work are blocked by the one-off site and somebody else's home: inside this window they arrive only as single-operation equipment and single-task slices
- **Original one-sentence judgment**: Construction and domestic work share the hardest property — the work environment is different every time and does not belong to whoever is working in it; through 2040 on-site construction robots remain single-operation equipment and do not substitute for the site process as a whole, open-ended household tasks reach no society-level diffusion, and home embodiment continues as single-task slices (vacuuming, dishwashing, mowing).
- **Original reasoning chain**: **Construction** — a site is one-off: geometry, ground conditions, trade sequencing and weather never repeat, tolerances are in centimetres rather than millimetres, and multiple trades wait on each other in one space → FBR's Hadrian bricklaying machine is the most honest specimen here (EXT-47): a direction pushed for something on the order of a decade, still at single-operation and demonstration-project scale → what blocks it is not laying speed: **however fast a machine lays brick, it still waits on the preceding trade, on inspection, on permits and on weather** → construction's real structural path is to bypass the site — move the work into a prefabrication plant, converting the one-off site into structured space, at which point it degenerates into the manufacturing problem of J-076 → **Domestic work** — the hardest square, and the difficulty is not even execution but **task definition**: "tidy up" contains classification, value judgment (which object is rubbish and which is a keepsake), privacy boundaries and household-specific conventions → on ILO's count domestic workers are a group in the tens of millions (EXT-42), so the demand is real and already being paid for — but what is bought was never only the motions; it includes judgment, trustworthiness and the tacit understanding that saves the employer from specifying anything → and failure is irreversible: what breaks is not *a* cup, it is *that* cup (L6) → **when cost per task crosses labour**: even if a Hadrian-class machine pushes the unit cost of bricklaying below manual labour on some standardized houses, society-level diffusion requires **the site process, insurance rates and the inspection regime to change together** — Gate 4 multi-party coordination, not equipment performance; domestic work is the same, since between a machine folding laundry in a demo video and a hundred million households letting it into the bedroom daily sit ownership, trust and the cost paid on every use → **Hard constraints**: construction — **law / permitting** (building permits, inspection and injury liability must land on a party that can be sued) compounded by **physical**; domestic — **ownership / privacy** (someone's home is private space and entry requires authorization) compounded by **trust / relationship** (who gets a key is the product of repeated interaction over time and cannot be generated in one pass).
- **Original time window**: 2026–2040.
- **Original falsifier**: Before 2040, on-site construction robots substitute not for single operations but for the site process as a whole (verifiable through the number of trades and the share of schedule carried by robots in general contracts) — that falsifies this card's construction judgment; or a general-purpose home robot reaches daily performance of **open-ended household tasks** (not single-task slices such as vacuuming, dishwashing or mowing) in a majority of households in any country — that falsifies its domestic-work judgment.
- **Original leading indicator**: construction — (1) whether general contractors' insurance quotes a separate rate for robotic work; (2) whether schedule contracts start carrying default and stoppage clauses for robotic equipment; (3) whether the prefabrication share of work keeps rising. Domestic — (4) whether a general-purpose home robot falls into the durable-goods price band **and** carries a low enough recurring cost per task (no tidying beforehand, no supervision throughout); (5) whether domestic-worker headcount and wages diverge in high-adoption countries; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-073, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C4: Embodied Intelligence`.
- **Original external comparison**: **Agreement**: FBR's Hadrian, pushed for something on the order of a decade, is still at single-operation and demonstration scale (EXT-47), supporting "what blocks on-site construction is not laying speed"; ILO counts domestic workers as a separate group in the tens of millions with a large informal share (EXT-42), supporting that the demand is real and already paid for. **Divergence and evidence boundary**: both are **a single case or a single group definition** and cover no arrival order; ILO's statistical boundaries and years are as given in the source and this card takes orders of magnitude only; this round obtained no checkable series for prefabrication share, insurance rates for robotic work, or the recurring per-task cost of home robots. **Why the judgment is retained**: the card depends on two constraints that do not open as model capability improves — permitting and liability must land on a party that can be sued, and entering private space requires authorization and long-run trust. But as a negative judgment running to 2040 it is less checkable than this chain's mid-segment judgments, so confidence stays at Medium and is not raised.
- **Original external comparison source**: EXT-42, EXT-47 (see the source index above).
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-078` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-079

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L187–L208`；`docs/en/ledger/71-80.md:L187–L208`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2141–L2160`
- **Current card anchor**: `docs/en/ledger/71-80.md:L187–L208`
- **Original title**: Biomedical candidate generation and clinical-grade causal proof diverge
- **Original one-sentence judgment**: From 2026 to 2034, biomedical candidate generation and ranking get much cheaper, while clinical-grade causal proof does not accelerate proportionally.
- **Original reasoning chain**: Candidates are copyable and ranking costs fall → trustworthy causality still needs real samples, time, and subject protection → the bottleneck moves to prospective validation.
- **Original time window**: 2026–2034.
- **Original falsifier**: Before 2030, at least three high-liability categories halve median candidate-to-approved-intervention time without increasing real samples or follow-up intensity, while safety withdrawals do not rise.
- **Original leading indicator**: candidates per approval, share entering human trials, phase duration, post-market safety supplements, and withdrawals; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-005, J-034, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA evaluates AI credibility by Context of Use and risk, supporting “generation is not proof.” **Boundary**: it does not establish the window or acceleration ceiling. **Why retained**: real outcomes and subject protection do not copy with candidates.
- **Original external comparison source**: EXT-49, EXT-50.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-079` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-080

**Current pair / 当前双语卡片**：`docs/zh/ledger/71-80.md:L209–L229`；`docs/en/ledger/71-80.md:L209–L229`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2161–L2180`
- **Current card anchor**: `docs/en/ledger/71-80.md:L209–L229`
- **Original title**: Low-liability medical workflows diffuse before autonomous care without professional review
- **Original one-sentence judgment**: From 2026 to 2031, summarization, coding, scheduling, and review-based decision support become routine before autonomous diagnosis and treatment without professional review.
- **Original reasoning chain**: Low-liability tools replace existing work, fit current carriers, and remain reviewable → autonomous care crosses licensing, liability, and irreversible treatment → the former diffuses first.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, in at least two large jurisdictions, encounters covered by care without human review persistently exceed AI-assisted documentation and review-based support without one-off mandated procurement.
- **Original leading indicator**: FDA intended-use distribution, hospital recommend-review versus autonomous-action shares, insurance/liability terms, and clinical retention; twice yearly.
- **Original confidence**: Medium.
- **Original depends-on**: J-079, J-066, J-068, J-069.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA's list proves authorized regulated products exist. **Boundary**: it is not exhaustive and proves neither deployment scale nor autonomy. **Why retained**: review-based tools use an institutional loop; autonomous care needs additional action rights.
- **Original external comparison source**: EXT-48, EXT-50.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-080` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-081

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L5–L26`；`docs/en/ledger/81-90.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2181–L2200`
- **Current card anchor**: `docs/en/ledger/81-90.md:L5–L26`
- **Original title**: More drug candidates do not proportionally shorten human trial time
- **Original one-sentence judgment**: By 2034, AI increases drug candidates reaching laboratories, but candidate growth does not translate proportionally into approvals.
- **Original reasoning chain**: Search expands → more candidates compete for wet-lab, participant, site, and regulatory capacity that has not expanded proportionally → attrition or queues rise.
- **Original time window**: 2026–2034.
- **Original falsifier**: Between 2028 and 2034, AI-origin candidates cut both median first-in-human-to-approval time and failure rates by more than 50%, replicated in at least three therapeutic areas.
- **Original leading indicator**: Phase I AI-origin candidates, phase conversion, site start and recruitment completion time, and clinical candidates per approval; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-079, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: FDA requires risk-linked AI credibility. **Boundary**: it supports no timeline or success-rate forecast. **Why retained**: candidate computation and human time follow different production functions.
- **Original external comparison source**: EXT-49.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-081` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-082

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L27–L48`；`docs/en/ledger/81-90.md:L27–L48`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2201–L2224`
- **Current card anchor**: `docs/en/ledger/81-90.md:L27–L48`
- **Original title**: Once explanation is abundant, medical scarcity moves to authorized intervention and continuity of care (landscape only)
- **Original one-sentence judgment**: From 2027 to 2034, the bottleneck in chronic disease, ageing, and primary care moves from standard explanation to authorized intervention, continuous observation, and exception escalation.
- **Original reasoning chain**: Q&A is copyable → explanation and reminder costs fall → sampling, medication, transfer, follow-up, and exception judgment still need local resources and liability chains → advice becomes unmet demand without a carrier.
- **Original time window**: 2027–2034.
- **Original falsifier**: Across several countries, within five years of widespread AI Q&A, intervention hours, follow-up completion, and exception response speed rise together while staff and institutional capacity cease to be principal queue causes.
- **Original leading indicator**: post-advice follow-up, escalation latency, load per caregiver, primary-care vacancies, and twelve-month remote-program retention; annually.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-079, J-080, J-032, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C5: Biology and Medicine`.
- **Original external comparison**: **Agreement**: WHO supports workforce, accountability, and safety as real constraints. **Boundary**: it does not prove AI worsens care queues. **Why retained**: local intervention and liability chains do not emerge automatically from more explanation.
- **Original external comparison source**: EXT-50, EXT-51.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-082` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-083

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L49–L70`；`docs/en/ledger/81-90.md:L49–L70`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2225–L2244`
- **Current card anchor**: `docs/en/ledger/81-90.md:L49–L70`
- **Original title**: Personalized explanation becomes abundant before verifiable mastery
- **Original one-sentence judgment**: From 2026 to 2030, personalized explanations, examples, and immediate feedback become routine, but verifiable mastery does not grow proportionally.
- **Original reasoning chain**: Explanations are copyable → generation and translation costs fall → practice still requires attention, time, and behavioural change → understanding and independent performance diverge.
- **Original time window**: 2026–2030.
- **Original falsifier**: Across countries, ages, and subjects, after two years of widespread generative tutoring, controlled transfer and long-term retention rise proportionally with use without curriculum redesign.
- **Original leading indicator**: weekly AI-tutoring use, independent transfer scores, three- to six-month retention, completion, and dependence on assistance; each term.
- **Original confidence**: Medium.
- **Original depends-on**: J-001, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: UNESCO requires human-centred, age-appropriate, private, pedagogically designed use. **Boundary**: it does not prove outcomes fail to rise proportionally. **Why retained**: explanation cannot bear practice time for the learner.
- **Original external comparison source**: EXT-52.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-083` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-084

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L71–L92`；`docs/en/ledger/81-90.md:L71–L92`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2245–L2264`
- **Current card anchor**: `docs/en/ledger/81-90.md:L71–L92`
- **Original title**: AI tutoring enters teacher and institutional workflows before replacing schools
- **Original one-sentence judgment**: From 2026 to 2031, AI tutoring diffuses first through teacher assignment, curriculum alignment, and institutional supervision rather than large-scale school replacement.
- **Original reasoning chain**: Stand-alone chat adds a new action → embedded tutoring replaces Q&A, practice, and feedback → schools carry identity, curriculum, peers, assessment, and credentials → local loops diffuse first.
- **Original time window**: 2026–2031.
- **Original falsifier**: By 2031, in at least three large education systems, broadly recognized qualifications from AI pathways outside schools/employers persistently outnumber those from institution-embedded pathways.
- **Original leading indicator**: teacher-assigned versus direct purchase use, learning-system integration, twelve-month retention, teacher workload, and recognition breadth of independent AI credentials; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-083, J-066, J-068, J-069, J-070, J-071.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: OECD emphasizes governance, ecosystems, and teacher capacity. **Boundary**: it does not prove schools retain current boundaries. **Why retained**: schools bind learning to identity, assessment, and credential exits.
- **Original external comparison source**: EXT-53.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-084` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-085

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L93–L114`；`docs/en/ledger/81-90.md:L93–L114`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2265–L2284`
- **Current card anchor**: `docs/en/ledger/81-90.md:L93–L114`
- **Original title**: Take-home artifact signals weaken while controlled performance and process evidence gain weight
- **Original one-sentence judgment**: From 2027 to 2034, high-stakes admissions and hiring reduce the weight of take-home artifacts without process verification and increase controlled performance and process evidence.
- **Original reasoning chain**: Artifact-generation costs fall → artifacts correlate less with personal capability → selectors move toward costlier but harder-to-outsource identity, live performance, and longitudinal records.
- **Original time window**: 2027–2034.
- **Original falsifier**: By 2032, leading universities and large employers keep increasing the independent weight of take-home artifacts without process verification while their predictive validity does not decline.
- **Original leading indicator**: oral and live-task share, identity-verification spending, portfolio version-history requirements, and internship/apprenticeship weight; annually.
- **Original confidence**: Medium.
- **Original depends-on**: J-022, J-083, J-084, J-066.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: UNESCO supports assessment redesign. **Boundary**: it does not establish which assessment gains weight. **Why retained**: selection systems cannot indefinitely rely on a proxy that has lost correlation with capability.
- **Original external comparison source**: EXT-52.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-085` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-086

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L115–L136`；`docs/en/ledger/81-90.md:L115–L136`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2285–L2308`
- **Current card anchor**: `docs/en/ledger/81-90.md:L115–L136`
- **Original title**: The explanation gap narrows while practice and verification gaps may widen (landscape only)
- **Original one-sentence judgment**: From 2027 to 2034, AI narrows access gaps in explanation, but without carrier institutions skill and opportunity gaps may fail to fall or may widen.
- **Original reasoning chain**: Marginal explanation becomes cheap → people with devices and self-direction benefit first → mastery still needs time, feedback, and practice environments → credentials need institutional recognition → new supply is absorbed through existing resource differences.
- **Original time window**: 2027–2034.
- **Original falsifier**: Where low-cost AI tutoring is widespread without added teachers, devices, assessment, or social support, low- versus high-income gaps in independent mastery and qualifications shrink significantly for five consecutive years.
- **Original leading indicator**: device/connectivity access, use by income, independent assessment gaps, teacher contact, completion, qualifications, and employment conversion; annually.
- **Original confidence**: Low (landscape only).
- **Original depends-on**: J-083, J-084, J-066, J-069, J-070.
- **Original status and lineage**: ACTIVE.
- **Original source**: `C6: Education and Skill Formation`.
- **Original external comparison**: **Agreement**: the World Bank establishes the enormous scale of foundational learning deficits. **Boundary**: it does not support AI's direction of effect on inequality. **Why retained**: explanation is only one input to learning and is not the authority granting qualifications.
- **Original external comparison source**: EXT-54.
- **Original standalone audience scale**: Unknown/unverified: the historical card has no standalone Audience scale field; scale appears only inside Diffusion-gate review, and no later value is back-projected.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-086` appears once in each historical ledger and once in each current shard; anchors above are entry points.
- **修订谱系 / Revision lineage**：historical status is reproduced above when it states REVISED/FALSIFIED/supersession; otherwise lineage is unknown/unverified rather than inferred from a later card.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; this section is the historical boundary.

## J-087

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L137–L158`；`docs/en/ledger/81-90.md:L137–L158`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2309–L2328`
- **Current card anchor**: `docs/en/ledger/81-90.md:L137–L158`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2031, organizations adopting generation and tool use first split work into machine-default execution, human exception handling, and accountable boundary setting rather than broadly becoming staffless.
- **Audience scale**: constructed hundred-millions-scale reach across knowledge workers, operations staff, and managers; mainly **raises existing professionals' ceiling**, while organizations perform the work-unit redesign.
- **Diffusion-gate review**: The reach is not a citable same-action behaviour statistic, and organizations must complete workflow substitution and a local closed loop; Gate 1 **FAIL**, an organizational judgment.
- **Lens**: technology sequence + organizational carrier + diffusion Gates 2–4.
- **Reasoning chain**: Generation and tool use mature first → bounded reviewable tasks enter workflows first → exceptions and liability still need a principal → the minimum production unit becomes one accountable person supervising multiple machine executions.
- **Time window**: 2026–2031.
- **Falsifier**: By 2031, across at least three large knowledge-work industries, fewer than half of production AI deployments that persist for twelve months use a work unit combining machine-default execution, human exception handling, and accountable boundary setting. The card fails whether the remainder is end-to-end staffless execution or deployment broadly stalls in demonstrations and failures.
- **Leading indicator**: machine-default share, human takeover rate, executions per accountable owner, pre-deployment workflow-redesign hours, and twelve-month retention; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-006, J-007, J-009, J-066, J-068.
- **Strongest opposing mechanism**: End-to-end reliability may jump enough for organizations to delegate complete outcomes without passing through supervisory units.
- **Against consensus**: **Agreement**: NIST calls for governance, measurement, monitoring, and human oversight. **Boundary**: it does not establish this organizational form or time window. **Why retained**: existing accountable principals and workflows are already-built carriers, so task-by-task substitution clears the diffusion gates more easily than rebuilding firm boundaries at once.
- **External comparison source**: EXT-4.
- **Source**: [C7：技术先到，权力后到：能力出现次序如何穿过组织，才变成社会后果](../zh/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-087` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.
- **J-086/J-087 boundary attack**：J-086 remains a separate historical card and J-087 begins the next source section; replacing either historical proposition with the other’s current wording would fail this migration boundary.

## J-088

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L159–L180`；`docs/en/ledger/81-90.md:L159–L180`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2329–L2348`
- **Current card anchor**: `docs/en/ledger/81-90.md:L159–L180`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2034, in generation-intensive occupations junior production seats and routine hours shrink relatively before total occupational headcount, making supervised practice a skill-formation bottleneck.
- **Audience scale**: constructed tens-of-millions-scale reach across junior knowledge workers, applicants, and professional trainees; mainly **raises existing professionals' ceiling** while narrowing entry routes.
- **Diffusion-gate review**: Occupational entry is a low-frequency institutional arrangement, not one repeated action performed across society; Gate 1 **FAIL**, a labour-market and skill-formation judgment.
- **Lens**: task bundles + skill formation + signalling game.
- **Reasoning chain**: Junior production is easiest to verify and automate → seniors sustain output with fewer junior hours → entrants lose the carrier for real-task practice → apprenticeship, simulation, and supervised fieldwork become scarcer.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, across at least five generation-intensive occupations, junior-seat share does not decline before total occupational headcount; or it declines first but verifiable apprenticeship, simulation, rotation, or supervised-fieldwork capacity expands enough to preserve the pre-adoption replenishment rate of professionals. Junior seats falling at the same time as or after total occupational contraction also falsifies the card.
- **Leading indicator**: junior-to-senior hiring ratio, entry-task mix, apprenticeship places, supervised hours, time to promotion, and controlled performance of external candidates; annually.
- **Confidence**: Medium.
- **depends-on**: J-087, J-083, J-066.
- **Strongest opposing mechanism**: AI tutoring and high-fidelity simulation may lower training cost simultaneously, giving more entrants denser feedback than old jobs did.
- **Against consensus**: **Partial agreement**: the ILO's 2025 global occupational-exposure index finds about one in four workers in occupations with some GenAI exposure and judges transformation more likely than whole-job replacement for most occupations. **Boundary**: the index provides no evidence about junior hiring, apprenticeship carriers, net employment, or this card's time window. **Why retained**: the routine production being removed was also the old occupation's practice carrier, and generation does not automatically build a replacement carrier.
- **External comparison source**: EXT-60.
- **Source**: [C7：技术先到，权力后到：能力出现次序如何穿过组织，才变成社会后果](../zh/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-088` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-089

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L181–L202`；`docs/en/ledger/81-90.md:L181–L202`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2349–L2368`
- **Current card anchor**: `docs/en/ledger/81-90.md:L181–L202`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2026 to 2032, identity, permission, logging, pause, audit, and appeal enter core production systems before tool-using AI broadly receives high-liability autonomous authority.
- **Audience scale**: constructed hundred-millions-scale reach across employees, customers, and citizens affected by high-liability automation; mainly **raises existing professionals' ceiling**, while organizations and public institutions operate the controls.
- **Diffusion-gate review**: Affected reach is not the headcount executing the control action, and multi-party authorization depends on enforceable and observable coordination; Gate 1 **FAIL**, an institutional judgment.
- **Lens**: action rights + legal liability + diffusion Gate 4.
- **Reasoning chain**: Tool use enlarges possible consequences → asset owners require least privilege and interruptibility → disputes require logs, accountable signatures, and appeal → the control plane moves from compliance attachment to production dependency.
- **Time window**: 2026–2032.
- **Falsifier**: By 2030, across at least three high-liability industries, most production autonomous systems receive broad high-liability authority without principal-level authorization, tamper-evident action records, human pause, and dispute appeal as prior production dependencies. If systems receive broad authority first and regulators or buyers tighten only after accidents, the reversed order still falsifies the card.
- **Leading indicator**: fine-grained permission coverage, log retention, human pause rate, external-audit clauses, appeal latency, and procurements rejected for missing controls; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-007, J-009, J-031, J-055, J-070.
- **Strongest opposing mechanism**: Low accident rates and platform-level insurance may make black-box autonomy acceptable, replacing per-action control with ex-post compensation.
- **Against consensus**: **Agreement**: NIST and the EU AI Act support governance, logging, human oversight, and risk management. **Boundary**: they do not establish the diffusion order of appeal controls or consistency across industries. **Why retained**: execution touches other parties' assets and rights, so existing accountable principals need observable authorization and interruption paths before delegating.
- **External comparison source**: EXT-4, EXT-10.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-089` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-090

**Current pair / 当前双语卡片**：`docs/zh/ledger/81-90.md:L203–L223`；`docs/en/ledger/81-90.md:L203–L223`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2369–L2388`
- **Current card anchor**: `docs/en/ledger/81-90.md:L203–L223`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, early productivity gains after general-model prices fall flow first to parties owning customers, proprietary workflow data, licences, channels, liability-bearing capital, compute, or power rather than spreading automatically with technical access.
- **Audience scale**: constructed billion-scale reach across firms, workers, and consumers; mainly **raises existing professionals' ceiling**, while asset owners and institutions determine distribution.
- **Diffusion-gate review**: Billion-scale is distributional reach, not a same-action behaviour statistic, and the subject is an asset and institutional arrangement; Gate 1 **FAIL**, a capital-and-power judgment.
- **Lens**: complementary assets + capital returns + competition institutions.
- **Reasoning chain**: Model and call prices fall → scarcity rents on core capability compress → commercialization still needs scarce complementary assets and fixed redesign cost → incumbent asset owners absorb gains first → open standards, competition, and redistribution determine later spread.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five high-adoption industries, incumbent firms controlling customers, proprietary data, licences, channels, or infrastructure gain no relative margin, market share, or bargaining power. The card fails whether gains move to entrants, model suppliers, labour, or consumers.
- **Leading indicator**: industry margins, merger activity and concentration, returns by AI supply-chain layer, labour share, price decline, data portability, and channel switching; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-039, J-056, J-087.
- **Strongest opposing mechanism**: Model commoditization, open weights, and low-code distribution may make complementary assets rapidly replicable, letting small teams take incumbent channels and profits directly.
- **Against consensus**: **Agreement on mechanism, unknown on outcome**: Teece's complementary-assets theory supports value capture depending on scarce complements; Brynjolfsson, Rock, and Syverson's Productivity J-Curve supports general-purpose technologies requiring complementary intangible investment in business processes, human capital, and organizational co-invention. **Boundary**: neither establishes AI's distribution, the duration of concentration, or this card's time window. **Why retained**: model access does not simultaneously supply customers, licences, power, liability capital, and workflow-redesign capacity.
- **External comparison source**: EXT-37, EXT-61.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-090` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-091

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L5–L26`；`docs/en/ledger/91-95.md:L5–L26`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2389–L2412`
- **Current card anchor**: `docs/en/ledger/91-95.md:L5–L26`
- **Proposed date**: 2026-09-21.
- **One-sentence judgment**: From 2027 to 2035, AI-intensive industries see both lower labour hours per unit and expansion in variety, frequency, or customer segments; demand elasticity and non-automated hard constraints jointly determine net employment.
- **Audience scale**: constructed billion-scale reach across workers and consumers; the capability both **raises existing professionals' ceiling** and, in low-cost services, may let people who could not do it do it now for some consumption or production actions.
- **Diffusion-gate review**: The reach is not one repeated action and employment is an industry-level net result; Gate 1 **FAIL**, a demand-and-labour-structure judgment.
- **Lens**: supply-and-demand elasticity + task bundles + physical and institutional hard constraints.
- **Reasoning chain**: Labour hours per task fall → price, waiting, or customization costs fall → previously uneconomic demand enters → non-automated steps absorb part of the new volume → the relative size of expansion and savings determines net employment.
- **Time window**: 2027–2035.
- **Falsifier**: By 2032, across at least five adoption-intensive industries, significant labour-hour reductions per service are followed for three years by no expansion in variety, frequency, customer segments, or total output. Whether employment can also be explained by macroeconomic cycles, regulation, or other factors does not prevent falsification of the card's claim that demand expansion and task savings occur together.
- **Leading indicator**: labour hours per unit, price, wait time, SKU or service variety, frequency per customer, new-customer share, total output, and jobs in non-automated steps; annually.
- **Confidence**: Medium.
- **depends-on**: J-001, J-037, J-073, J-087.
- **Strongest opposing mechanism**: Where demand is saturated or income constraints do not move, cost reduction may become profit and job reduction without enough new volume.
- **Against consensus**: **Partial agreement**: the ILO's 2025 index judges task transformation more likely than whole-job replacement for most occupations and makes clear that exposure alone does not yield a net-employment outcome. **Boundary**: it provides no demand elasticity, output expansion, or net employment direction. **Why retained**: supply and demand determine whether lower cost expands quantity, while bodies, licences, and sites determine where that quantity lands; capability curves alone cannot yield the net result.
- **External comparison source**: EXT-60.
- **Source**: [C7: Technology Arrives First, Power Later: How Capability Sequence Passes Through Organizations Before Becoming Social Consequence](../en/chains/70-capability-to-social-consequences.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-091` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## 18. Judgment cards for the C8 upstream-materials and climate-coupling chain

> These four cards come from [C8：芯片之前的晶圆厂：为什么气候风险咬住的是「已验证瓶颈」](../zh/chains/80-fab-materials-and-climate.md) and [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md). They separate mineral stock and nominal supplier count from a qualified conversion path that can actually switch, and judge climate coupling through event–exposure–transmission rather than a single incident.

## J-092

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L27–L48`；`docs/en/ledger/91-95.md:L27–L48`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2413–L2432`
- **Current card anchor**: `docs/en/ledger/91-95.md:L27–L48`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2026 to 2032, resilience investment for advanced semiconductors shifts from larger raw-material and finished-goods inventories toward pre-qualified alternate refining, electronic-grade conversion, tool service, recipes, and process-transfer paths.
- **Audience scale**: a constructed million-scale set of semiconductor procurement, process, equipment, supply-chain, policy, and infrastructure professionals performs the work; this mainly **raises existing professionals' ceiling**, while consumers encounter indirect price and availability effects.
- **Diffusion-gate review**: This is low-frequency industrial configuration, not one activity diffusing across society; Gate 1 **FAIL**, so it remains an occupational/organizational judgment.
- **Lens**: supply elasticity + L2 constraint migration + L4 diffusion lag + geographic hard constraints.
- **Reasoning chain**: compute expansion raises demand for advanced-semiconductor capacity and resilience → some critical materials are by-products of other ore-processing systems, so incremental supply does not respond only to their own price → electronic-grade purity, recipes, tools, and customer approval turn chemically identical material into a process-specific input → inventory buffers disruption but cannot replace an unqualified conversion node → one firm rarely funds idle backup paths alone, so large buyers, public support, or cluster-level closed loops must coordinate them → firms move marginal resilience spending toward advance qualification and exercised switching.
- **Time window**: 2026–2032.
- **Falsifier**: By 2030, across at least three advanced-semiconductor clusters or ten major manufacturing, materials, or equipment firms, resilience spending still mainly increases raw or finished inventory, while pre-qualification of alternatives, dual process qualification, portable recipes, parts/service redundancy, and cross-site transfer time show no observable growth. Merely increasing nominal supplier count without qualification does not count as a hit.
- **Leading indicator**: share of dual-qualified materials, alternate-source qualification duration, portable recipe/mask coverage, parts and service redundancy, cross-site failover exercises, and inventory-to-qualification budget ratio; annually.
- **Confidence**: Medium.
- **depends-on**: J-056, J-069, J-070.
- **Strongest opposing mechanism**: material standardization, open tool interfaces, trusted simulation, and faster customer approval may compress qualification enough that inventory and nominal multi-sourcing regain primacy.
- **Against consensus**: **Agreement on exposure, unknown on response**: OECD, USGS, and DOE support regional concentration, by-product coupling, and segment vulnerability. **Boundary**: they do not establish the direction of resilience budgets or qualification duration. **Why retained**: unqualified materials and sites cannot carry the same specified output during disruption, so nominal supply is not switchable supply.
- **External comparison source**: EXT-67, EXT-68, EXT-69, EXT-70, EXT-72, EXT-73.
- **Source**: [C8：芯片之前的晶圆厂：为什么气候风险咬住的是「已验证瓶颈」](../zh/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-092` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-093

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L49–L70`；`docs/en/ledger/91-95.md:L49–L70`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2433–L2452`
- **Current card anchor**: `docs/en/ledger/91-95.md:L49–L70`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2026 to 2033, advanced-fab siting and public support increasingly price firm power, power quality, inlet-water quality, reuse, discharge, and climate adaptation as a bundle rather than comparing land, tax, and average utility prices separately.
- **Audience scale**: direct decision makers are a million-scale-or-smaller set of fab, materials, utility, government, and community professionals; millions around major clusters may be affected by allocation, while the capability mainly **raises existing professionals' ceiling**.
- **Diffusion-gate review**: affected residents are not performers of one weekly action, and siting is a low-frequency organizational choice; Gate 1 **FAIL**, an industrial/institutional judgment.
- **Lens**: complementary assets + site immobility + L7 institutional lag.
- **Reasoning chain**: advanced processes jointly require firm power, ultrapure water, gases and chemicals, and discharge capacity → failure of one utility makes cheap land unusable → climate risk increases variance in public systems → dedicated treatment, reuse, reserves, and power quality enter total siting cost and subsidy conditions.
- **Time window**: 2026–2033.
- **Falsifier**: By 2031, across at least ten new or substantially expanded advanced fabs, siting, subsidies, and utility contracts remain explained mainly by land, tax, and average water/power prices; power quality, withdrawal/discharge rights, reuse, drought/flood adaptation, and dedicated facilities neither change rankings nor create material contracts or capital spending.
- **Leading indicator**: project capital spending on dedicated water/power systems, withdrawal per wafer and recovery rate, power-quality clauses, withdrawal/discharge permitting time, climate-adaptation conditions, and projects exited or delayed for utility reasons; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-061, J-069.
- **Strongest opposing mechanism**: high recovery, closed-loop cooling, on-site treatment, dedicated generation, and flexible processes may decouple fabs from public systems and reduce the bundle to ordinary capital cost.
- **Against consensus**: **Agreement on operating constraints, unknown on pricing weight**: IEA, LBNL, DOE, and ERCOT support power-delivery and interconnection constraints for large loads, while DOE and TSMC support water, energy, and resilience as semiconductor operating issues. **Boundary**: they do not show a utility bundle outranking tax and land in fab siting. **Why retained**: these inputs are complements; a missing one prevents the others from becoming qualified output.
- **External comparison source**: EXT-12, EXT-26, EXT-29, EXT-30, EXT-69, EXT-71.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-06-30.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-093` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-094

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L71–L92`；`docs/en/ledger/91-95.md:L71–L92`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2453–L2472`
- **Current card anchor**: `docs/en/ledger/91-95.md:L71–L92`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2027 to 2034, semiconductor procurement, insurance, finance, and siting will systematically price climate risk, but the testable transmission unit is not the number of facilities in hazard zones: it is at least one multi-site qualified-output loss, longer alternate-path qualification, or related supplier interruption that inventory or qualified alternate paths cannot absorb; if the window ends without that transmission but pricing has changed based only on hazard maps or disclosure regulation, the judgment is falsified.
- **Audience scale**: a million-scale set of manufacturing, procurement, insurance, finance, equipment, and infrastructure professionals performs the work; this mainly **raises existing professionals' ceiling**; downstream consumers are a larger indirect reach.
- **Diffusion-gate review**: This is institutional risk pricing, not a weekly action by hundreds of millions of distinct people; Gate 1 **FAIL**.
- **Lens**: event–exposure–transmission + insurance pricing + qualification.
- **Reasoning chain**: a climate event is not a production loss → exposure damages output only through water, power, logistics, equipment service, or supplier nodes → inventory and qualified alternatives absorb part of the shock → only repeated, unabsorbed qualified transmission can change premiums, contracts, inventory, and siting; **no current source establishes that this transmission will occur inside the window, so its absence before expiry is neither a HIT nor automatically a falsification and must be reviewed against the preregistered conditions; if the loss trigger is absent but hazard-map or disclosure-regulation prior pricing appears, the symmetric falsifier applies**.
- **Time window**: 2027–2034.
- **Falsifier**: Before 2032, at least three manufacturing regions have each experienced repeated climate-related qualified-output loss that inventory or qualified alternate paths could not absorb; if, under that condition, semiconductor insurance terms, supplier contracts, qualification, inventory structure, financing cost, and siting standards show no systematic change, or changes follow hazard maps alone and remain unrelated to output loss and alternate-path qualification, the card fails. **If the loss trigger never occurs by the end of the 2034 window, but insurance terms, financing cost, or siting standards have systematically changed based only on hazard maps or disclosure regulation, the card also fails.** Repeated water, power, logistics, or site interruptions that are fully absorbed, and a trigger that never occurs without this kind of prior pricing, do not trigger falsification.
- **Leading indicator**: climate-related downtime and lost wafers, insurance deductibles and exclusions, climate audit clauses, alternate-source qualification time, common-node exposure, and post-event contract or siting changes; annually.
- **Confidence**: Medium.
- **depends-on**: J-092, J-093.
- **Strongest opposing mechanism**: long-term contracts, inventory, rapid repair, and demand substitution may keep absorbing climate shocks, allowing exposure to rise while output and financial terms remain unchanged.
- **Against consensus**: **Agreement on exposure, divergence on evidence unit**: UNU-EHS supports the exposure layer of Taiwan drought and water restrictions, FERC/NERC supports freeze-driven power-system interruption, and NXP supports only one firm's single shutdown transmission. **Boundary**: these materials do not establish repeated multi-site output loss or insurance and financing response. **Why retained**: only an event transmitted through a common node into unabsorbed loss changes economic behaviour; one incident is therefore insufficient evidence of a trend.
- **External comparison source**: EXT-69, EXT-71, EXT-74, EXT-75, EXT-76.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-094` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.

## J-095

**Current pair / 当前双语卡片**：`docs/zh/ledger/91-95.md:L93–L113`；`docs/en/ledger/91-95.md:L93–L113`

### English historical snapshot

- **Historical anchor**: `1f99c832be8cbc82631beb7679d82994a2b7e0fb^:docs/en/90-ledger.md:L2473–L2491`
- **Current card anchor**: `docs/en/ledger/91-95.md:L93–L113`
- **Proposed date**: 2026-09-22.
- **One-sentence judgment**: From 2027 to 2034, major fab projects increasingly specify in approvals, subsidies, and utility contracts who funds dedicated water, power, and adaptation assets and whether fabs, residents, or other industry are curtailed first during scarcity.
- **Audience scale**: major clusters create a constructed ten-million-scale affected population, while a million-scale-or-smaller set of governments, utilities, firms, and community representatives performs the decisions; this mainly **raises existing professionals' ceiling** and is distributional reach, **not** society-wide repeated action.
- **Diffusion-gate review**: contracting and approval are low-frequency institutional actions, and affected population cannot substitute for actor count; Gate 1 **FAIL**.
- **Lens**: local externalities + collective action + immovable infrastructure.
- **Reasoning chain**: fab resilience requires dedicated power, treatment, reuse, reserves, and emergency restoration → capital and national benefits travel while infrastructure cost and shortage risk stay local → under scarcity, ambiguous priority becomes political and financial risk → funding, curtailment, and restoration order enter approvals and contracts.
- **Time window**: 2027–2034.
- **Falsifier**: By 2032, across at least ten major new or expanded projects, fabs continue to take ordinary undifferentiated utility service, while dedicated-facility funding, scarcity curtailment, emergency restoration, and community compensation create neither approval disputes nor public decisions or contract terms.
- **Leading indicator**: sponsor share of dedicated-utility cost, industrial-versus-residential curtailment rules, priority-restoration clauses, community-benefit agreements, withdrawal disputes, rate cross-subsidy, and local moratoria or conditional approvals; semi-annually.
- **Confidence**: Medium.
- **depends-on**: J-061, J-070, J-093.
- **Strongest opposing mechanism**: closed-loop water, dedicated generation, and full sponsor funding may decouple projects from public resource allocation and avoid persistent bargaining.
- **Against consensus**: **Adjacent mechanism, unknown outcome**: J-061 and infrastructure material support large loads making local costs visible. **Boundary**: current sources do not establish fab allocation and curtailment clauses becoming standard. **Why retained**: immovable utilities place national benefits and local costs on different ledgers, forcing someone to choose an order under scarcity.
- **External comparison source**: EXT-69, EXT-71.
- **Source**: [C8: The Fab Before the Chip: Why Climate Risk Bites at Qualified Bottlenecks](../en/chains/80-fab-materials-and-climate.md).
- **Next review**: 2027-12-31.
- **Status**: ACTIVE.
- **Migration fields not separately recorded by the historical source**: Unknown/unverified: the frozen card does not record the current shard entry point, this inventory's audit status, or any later successor relation; this inventory records those fields without back-projecting them into the historical judgment.

### Pairing and lineage

- **双语配对 / Bilingual pairing**：`J-095` appears once in each frozen historical ledger and once in each current shard; the two language entries above are paired anchors.
- **修订谱系 / Revision lineage**：the historical status and any stated lineage are reproduced above; if the frozen source does not state a relation, it remains unknown/unverified rather than inferred from a current successor.
- **当前卡与历史关系 / Current-to-history rule**：current text is a later projection; it does not replace, rewrite, or silently cover the historical card above.
- **J-095/J-096 closed-set end-boundary attack**：J-095 is the final card in the mechanically extracted historical set J-001–J-095. J-096 and later current cards are outside this historical set; adding them here or omitting J-095 from either language would fail the boundary. The current Chinese and English J-095 entries both cover the complete card (`docs/{zh,en}/ledger/91-95.md:L93–L113`), while J-096 starts at `docs/{zh,en}/ledger/96-102.md:L5`.

## Verification checklist / 复核清单

- **Closed-set**：exactly J-001 through J-095, once each; J-096 and later current cards are outside this historical closed set.
- **Historical preservation**：each of the 95 cards has a frozen-source Git anchor, original fields in both languages, and a current Chinese/English shard entry.
- **Unknown semantics**：unknown/unverified is used only for absent standalone fields or unstated lineage; it does not erase information inside a broader field.
- **Bilingual anchors**：each of the 95 cards has paired Chinese/English current-shard and historical-snapshot anchors; J-086/J-087 and J-095 are explicit boundary checks.
- **Mechanical checks are structural evidence only**：the repository checker cannot prove semantic equivalence or detect a birth-time semantic replacement; fresh-context review must attack those boundaries.
