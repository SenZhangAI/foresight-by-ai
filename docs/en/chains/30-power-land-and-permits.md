# C3 · Electrons on the Ground: The Bottleneck Moves from Chips to Grids, Land, and Permits

> **This chain extends C1 and the technology sequence.** C1 argues that generation becomes cheap; the technology chain argues that capabilities arrive in a specific order. Both quietly assume one thing: that compute can be bought if you are willing to pay. This chain takes that assumption apart. Turning model capability into a real service requires turning electrons into computation, and that step happens in land, transformers, and permitting windows.
> **In one sentence**: the scarce thing is not electricity but **the kilowatt-hour that is already permitted and can be delivered on the promised date**; and once the constraint moves from portable chips to immovable grids and sites, control regimes, taxation, and local politics move with it.

## 1. 2029: a project manager holding a queue number

A model company decides to build its own training cluster. Chips are allocated, financing has closed, the engineering drawings take three weeks. The project manager loads everything into a schedule, and the thing that blocks it is a single sheet of paper: the interconnection application receipt, with an expected response date two years out.

He tries three alternatives. A remote site with surplus power — not enough cooling water, and fiber would have to be pulled. An existing industrial building — its substation capacity is one sixth of what he needs, and expanding it means the same queue. Bridging with on-site turbines and storage — that covers the first two years, but environmental permits are their own window.

What he finally does is the revealing part: he moves the site from the region with the cheapest power to one where power costs forty percent more, but where spare substation capacity already exists and the local government is willing to approve quickly.

At that moment the object being priced quietly changes. **The buyer is no longer buying cheap electricity; he is buying the promise that power will be live on a specific date.** And the supply of that promise is governed by slow variables that do not accelerate with compute demand at all: equipment manufacturing cycles, construction cycles, and administrative approval cycles.

## 2. Skeleton of the chain

```text
Model capability and token supply become abundant (C1 / technology chain)
        │
        ▼
Capital floods into compute → electrons must become computation
        │
        ├──▶ Chips: mass-produced, portable, embargoable (fast variable)
        │
        └──▶ Power delivery + interconnection permits + land and cooling (slow variables)
                 │
                 ▼
        The binding constraint moves to deliverable power and interconnection capacity
                 │
                 ├──▶ What is priced is certainty of the delivery date, not energy
                 ├──▶ Load splits: latency-sensitive / schedulable (the latter becomes a grid resource)
                 ├──▶ Control follows the constraint: hardware export → the use side
                 └──▶ Immovable heavy assets land in specific places
                          ├──▶ Social licence becomes a real cost
                          └──▶ Tax base and value layer diverge (landscape only)
```

This chain uses L2 (constraint migration), L4 (diffusion lag), L7 (institutional lag), and L8 (human needs — specifically, paying for certainty). It does **not** claim that "there will not be enough electricity," and it forecasts neither total demand nor emissions. It reasons only about **where the binding constraint sits**, and whose bargaining power changes once the constraint moves.

## 3. Step one: compute supply is three curves, not one

Treating "compute" as a single commodity guarantees a wrong read on the bottleneck. It is at least three supply curves stacked together, and they expand at speeds that differ by an order of magnitude:

1. **Chips and systems**: an industrial mass-produced good. Expanding capacity takes capital and advanced fabs and runs in years, but **its elasticity rises with investment**, and the output can be shipped, stockpiled, and reallocated globally.
2. **Power delivery**: transformers, high-voltage switchgear, transmission lines, substations. Constrained by heavy-equipment manufacturing schedules and construction time, it **cannot be meaningfully accelerated by placing more orders**, and it can barely be reallocated across regions — a transformer can be shipped, a transmission line cannot.
3. **Permits and land**: interconnection approval, environmental review, water rights, land use. This one is peculiar: its cycle is set by administrative process and local politics, and is **fully decoupled from technical progress**. AI making design a hundred times faster does not remove one public hearing.

Only the first curve steepens materially in this investment wave. So the conclusion is close to arithmetic: **when capital is abundant enough, what runs out first is not wafers but permits and interconnection queues.** That is [J-056](../90-ledger.md#j-056--the-binding-constraint-on-compute-expansion-moves-from-chip-supply-to-power-delivery-and-interconnection-permits).

It can be wrong. The strongest counter is not "there will be enough power" but **demand collapsing on its own**: if energy per unit of service falls faster than service volume grows, the load curve never catches the grid curve and the constraint never binds. That is written into the card's falsifier, and it gets its own long-run branch in section 9.

## 4. Step two: what is scarce is not energy but "live on that date"

Once the bottleneck sits in a queue, the scarce good becomes certainty about time, not energy itself.

The reason is on the demand side. Model generations have short windows: a cluster that comes online eighteen months late usually faces a model generation that has already turned over and customers who have already been taken. Buyers will therefore pay a clear premium for "live on this date" over and above the price of the energy — an old L8 regularity: people pay separately to remove uncertainty, not merely for the expected value.

Contract structure deforms accordingly. It stops being mainly "price per kilowatt-hour" and grows capacity reservation fees, in-service date guarantees, delay damages, and on-site generation or storage as a bridge. Within one region, a site that is permitted, interconnected, and shovel-ready will trade far above a site that is merely cheap — and the gap will exceed construction cost, because what differs is the position in the queue. That is [J-057](../90-ledger.md#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date).

**Power you can buy and power you can buy on schedule are two different commodities.**

This judgment also yields a counterintuitive corollary: over these few years the geography of compute is better explained by **queue length and permitting speed** than by electricity price. Once grid expansion catches up, the corollary expires; until then it is observable and falsifiable as [J-063](../90-ledger.md#j-063--the-geography-of-compute-is-decided-by-interconnection-queues-and-permitting-speed-not-by-electricity-price).

## 5. Step three: the split personality of AI load

Treating a data centre as "a very large factory" is the other way to misread this. AI load divides into at least two halves whose meaning for the grid is opposite:

- **The latency-sensitive half**: interactive inference. A user is waiting, milliseconds are visible, it cannot be interrupted or moved. To the grid it is pure rigid load.
- **The schedulable half**: training, batch inference, evaluation, data processing. It can be paused, deferred to night, or moved across time zones to another campus.

The second kind has a property traditional industrial load lacks: **the cost of interruption is mostly time, not spoilage.** Cutting power to an aluminium smelter for a few hours can destroy a production line; cutting power to a batch inference job for a few hours means it finishes a few hours later.

What grids are shortest of is precisely flexibility. So schedulable compute is not only a burden on the grid — it is a resource the grid can pay for, and demand response, interruptible tariffs, and capacity markets are existing payment channels. That means the real power cost of a large compute user may sit below its nominal tariff, and that on the grid side "AI strains the power system" and "AI helps fill the valleys" may both be true at once. That is [J-058](../90-ledger.md#j-058--ai-load-splits-into-latency-sensitive-and-schedulable-halves-and-the-schedulable-half-becomes-a-grid-flexibility-resource).

Its falsifier is clean: if, by the end of the window, contracted data-centre capacity in interruptible or demand-response programs is still negligible, this half of the personality does not exist commercially.

## 6. Step four: control follows the constraint — from hardware export to the use side

The technology chain already noted that renting compute widens capability diffusion ([J-027](../90-ledger.md#j-027--rented-compute-spreads-capability)). For a control regime, that sentence is a problem.

Chips are an ideal object of control because they are discrete, countable, traceable, and must cross a customs border. A rental architecture removes every one of those properties: the hardware does not move a metre, while the capability crosses the border anyway. As long as remote access is unconstrained, an entity list governs *who owns*, not *who uses*.

Facing that gap, a regulator has two options: accept that control has failed, or move the handle to the use side — identity and purpose declaration for accounts, restrictions on cross-border remote access, rules on transferring model weights, authorization of sites and operators, logging and reporting duties. **When the controlled object cannot be stopped at the border, control migrates onto people and contracts.** That is [J-059](../90-ledger.md#j-059--the-handle-of-compute-control-moves-from-hardware-export-to-the-use-side).

Part of this is already observable, so it is **partly consistent with consensus** and must be labelled as such. What this chain adds is not the direction but the mechanism and the falsifier: if, by the end of the window, the major control regimes are still anchored only in hardware and entity lists, with no enforceable duties on remote access or weight transfer and no enforcement cases, the reasoning is wrong. Its counter-mechanism is equally concrete: if open weights and local models make high-value capability broadly available outside any control perimeter, use-side control degrades into symbolic text.

## 7. Step five: site here, hardware there, jurisdiction elsewhere (landscape only)

Stacking the first four steps produces a geographic split across three factors:

| Factor | Movable? | Who actually controls it |
|---|---|---|
| Power and site | No | Host state and local government |
| Chips and systems | Yes, but export-controlled | Supplying state and vendors |
| Model weights | Instantly | The holder, who can withdraw at any time |

A new state role appears: countries with surplus energy, fast approvals, and geopolitical acceptability rent out sites and power in exchange for investment, employment, and rent. What they obtain is **rent**, not **capability sovereignty** — the hardware and the use authorization stay with others, weights can be withdrawn overnight, and the leverage they hold (cutting power, expropriation) is one-shot and extremely costly to use.

This is a structural consequence with no identifiable payer, so it belongs to Exit B; but its evidence chain is incomplete and confidence can only be low, so per the methodology it is recorded as [J-060](../90-ledger.md#j-060--energy-rich-hosts-trade-sites-for-compute-and-gain-rent-rather-than-capability-sovereignty-landscape-only) (landscape only). Upgrading it requires an observable class of contract terms: whether host states obtain local usage quotas, weight escrow, or audit rights.

## 8. Step six: who receives the bill

Heavy assets must land somewhere specific, and the people who live there see the bill.

The asymmetry is here: a data centre is a very large investment with very few jobs, while its electricity and water use are conspicuous and its returns accrue to shareholders elsewhere. Worse, the **visibility is asymmetric** — residents see a monthly electricity bill and never see the AI revenue. Under L8, loss aversion plus asymmetric visibility is enough to produce a local political response: moratoria, special tariff classes for very large customers, water restrictions, agreements conditioned on tax and employment.

The result is a line item that was previously priced at roughly zero: **social licence**. That is [J-061](../90-ledger.md#j-061--local-externalities-of-data-centres-become-explicit-and-social-licence-becomes-a-real-siting-constraint). Its counter-mechanism is solid too: if data centres broadly bring their own generation and storage and switch to closed-loop cooling, decoupling from the public grid and public water, local externalities fall sharply and the conflict does not arise.

One step further is weaker but worth keeping: **what can be taxed is the immovable heavy asset; what earns the profit is the instantly mobile value layer.** A locality can reach electricity prices, property tax, and a little employment; it cannot reach the profit. So localities keep raising their demands on the heavy asset while firms hedge through siting competition. Whether this mismatch gets absorbed by international tax reform is not something current evidence can settle, so it is kept as [J-062](../90-ledger.md#j-062--heavy-assets-are-taxable-while-the-value-layer-is-mobile-so-local-shares-stay-structurally-low-landscape-only) (landscape only).

## 9. The gate: what gets eaten by the same force

Section 3 of the methodology requires asking whether a new scarcity can be automated away by the same force that created the abundance. Item by item:

- **Will be eaten**: site evaluation, load forecasting, power-flow simulation, design and engineering documents, permit application preparation, dispatch optimization. These are information work, and AI will compress their cost and cycle time substantially.
- **Will not be eaten**: making a transformer that has not been manufactured exist; energizing a line that has not been approved; removing the need for a public hearing; making land you do not own usable. The hard constraints here are **physical** (mass must move and time must pass), **law / permitting** (some authority must be able to grant the permit), and **ownership** (a key input is lawfully held by someone else).

So the opportunity exit of this chain is narrow rather than broad. It is not the slogan "AI needs power, therefore energy is an opportunity," but the specific layer [J-057](../90-ledger.md#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date) points at: **turning certainty of delivery time into a tradable product** — development and transfer of permitted sites, bridge generation and storage, interconnection and permitting acceleration. It is recorded against the gate in [Opportunity Candidates](../40-opportunities.md).

Bridge generation is only a **window**, not a structural opportunity: its value comes entirely from the queue and closes when grid expansion catches up. It must be treated as such.

Finally, one self-falsifying long-run branch: if efficiency gains keep outpacing load growth and schedulable load can migrate freely across regions, this chain's constraint dissolves on its own. It has no adequate evidence chain and is labelled [J-064](../90-ledger.md#j-064--if-efficiency-gains-keep-outpacing-load-growth-the-constraint-in-this-chain-dissolves-in-the-long-run-landscape-only) (landscape only), but it stays in the ledger as the single most important opposing hypothesis for the whole chain.

## 10. So who should change what

- **Compute buyers (the payers behind Exit A)**: change the procurement question from "how much per kilowatt-hour" to "on which date will power be live, and who pays if it slips." Lock power and interconnection *before* signing hardware orders, not after.
- **Compute operators**: split load explicitly into latency-sensitive and schedulable, and contract for them separately — buy certainty for the part that cannot move, sell flexibility for the part that can.
- **Grids and regulators**: treat large-load interconnection rules, interruptibility terms, and tariff classes as one design. Expanding the queue without pricing flexibility solves with the most expensive instrument (new capacity) a problem the cheapest instrument (load scheduling) could have relieved.
- **Local governments (the actors behind Exit B)**: the negotiation is not "data centre yes or no" but "on what terms": special tariffs, water conditions, allocation of local power-cost increases, and curtailment order during scarcity. Without those terms, the public grid is subsidizing external shareholders.
- **Founders**: the entry point is certainty and permitting, not electricity. You cannot build generation; you can work on queues, permits, bridging, and dispatch — while knowing that the bridging part has a scheduled closing date.

## 11. Where I could be wrong

**Counter one: demand collapses on its own.** If energy per unit of service falls faster than service volume grows, or compute investment pulls back sharply, the queue disappears, certainty stops being scarce, and [J-056](../90-ledger.md#j-056--the-binding-constraint-on-compute-expansion-moves-from-chip-supply-to-power-delivery-and-interconnection-permits) and [J-057](../90-ledger.md#j-057--what-gets-priced-is-not-energy-but-certainty-of-delivery-date) fall together. The metric to watch is the ratio between new-load growth and the decline in energy per unit of service.

**Counter two: compute decouples from the grid.** If on-site generation plus storage becomes standard and data centres largely bypass public interconnection, the queue stops being the binding constraint and the local conflict in [J-061](../90-ledger.md#j-061--local-externalities-of-data-centres-become-explicit-and-social-licence-becomes-a-real-siting-constraint) weakens substantially.

**Counter three: control loses its point.** If open weights and local deployment make high-value capability broadly available outside the perimeter, [J-059](../90-ledger.md#j-059--the-handle-of-compute-control-moves-from-hardware-export-to-the-use-side) is left with symbolic clauses, and the three-way split in [J-060](../90-ledger.md#j-060--energy-rich-hosts-trade-sites-for-compute-and-gain-rent-rather-than-capability-sovereignty-landscape-only) does not hold either.

**Counter four: latency-sensitive load dominates.** If interactive inference is an overwhelming share of total load and service-level agreements forbid interruption, the flexible share in [J-058](../90-ledger.md#j-058--ai-load-splits-into-latency-sensitive-and-schedulable-halves-and-the-schedulable-half-becomes-a-grid-flexibility-resource) is too small to matter commercially.

## 12. Comparison with external material

The comparison was made after the reasoning above, and is used only to mark agreement, divergence, and the boundary of evidence. It does not write back into the reasoning chain.

- **Agreement**: external material supports the direction that data-centre electricity growth and grid interconnection are real constraints, and supports the existence of control measures now reaching model weights and data-centre operator authorization (see the "external comparison source" field on each card).
- **Divergence**: external material generally discusses **totals** (demand growth, installed capacity, emissions), whereas this chain is about **where the binding constraint sits** and **the pricing of delivery time**; the former does not imply the latter. The queue evidence obtained this round covers generation-side interconnection only and explicitly does not cover large-load queues. On control, the observed handle so far is weights plus site and operator authorization, not the account-level remote-access licensing this chain's independent reasoning expected — that divergence is recorded on the card rather than smoothed over.
- **Why I still hold the line**: the slope difference between the three supply curves is structural and does not depend on any specific demand forecast; even if total forecasts are revised down sharply, concentrated investment plus unchanged approval cycles still exhausts the queue before the wafers. If large-load interconnection waits fall systematically, I withdraw [J-056](../90-ledger.md#j-056--the-binding-constraint-on-compute-expansion-moves-from-chip-supply-to-power-delivery-and-interconnection-permits) first and then re-review the rest of the chain along the dependency links.

## 13. What grows out of this chain

- It turns the "energy access rent" of [J-039](../90-ledger.md#j-039--rented-models-become-abundant-while-energy-data-and-channel-control-create-access-rents) from a conclusion into a testable mechanism: the rent does not come from generation, it comes from queue position and permits.
- It adds an institutional backlash to [J-027](../90-ledger.md#j-027--rented-compute-spreads-capability)'s "rental widens diffusion": the more diffusion runs through rental, the more inevitably control migrates to the use side.
- If [J-063](../90-ledger.md#j-063--the-geography-of-compute-is-decided-by-interconnection-queues-and-permitting-speed-not-by-electricity-price) holds, the next step is to reason about the second migration after grid expansion completes: the constraint returns to price and carbon, and this chain's window opportunities close at the same time.
- Adjacent dimensions this chain does not cover: material and equipment constraints inside chip manufacturing itself, cooling water and climate coupling, and the distributional consequences of rising power prices for non-AI users. They remain in the ledger's explicit gap list.

> **Current status**: this is a near-to-mid-term chain whose tests are observable queues and contract terms. The full judgment cards are [J-056](../90-ledger.md#j-056--the-binding-constraint-on-compute-expansion-moves-from-chip-supply-to-power-delivery-and-interconnection-permits) through [J-064](../90-ledger.md#j-064--if-efficiency-gains-keep-outpacing-load-growth-the-constraint-in-this-chain-dissolves-in-the-long-run-landscape-only).
