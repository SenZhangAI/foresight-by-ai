# Commercial-history calibration: payer–beneficiary closure candidate (B1)

> **Status: `CALIBRATION`; candidate not admitted to the toolbox.** This page looks at historical outcomes first, then proposes a falsifiable commercial regularity candidate. It does not assume AI and does not claim forecasting accuracy.
>
> Chinese counterpart: [商业史校准：支付者—受益者闭环候选（B1）](business-regularity-calibration-2026-10-16.md).

## 1. Candidate rule (written so it can say no)

**B1, the “payer–beneficiary closure” candidate**: when a commercial innovation requires a dedicated fixed start-up cost (infrastructure, subsidy, network build-out, or organizational rework), it can reach repeatable diffusion only if, at the decision date, at least one observable path exists:

1. one actor with authority can pay the start-up cost and capture recurring revenue or direct savings linked to rising usage; or
2. the start-up asset has a second use or independent revenue stream, so the entire recovery burden does not rest on a user base that does not yet exist.

**Fail condition**: if there is no actor able to authorize the payment, no recovery mechanism linked to usage, and no second use or independent revenue stream, B1 says **no**: the innovation may be technically feasible and may even attract early users, but its own commercial mechanism cannot cross the diffusion threshold.

This is a historical candidate, not the circular claim that “higher profit wins.” The decision must be written using the payer, cost bearer, and revenue path observable at the same date; a subsidy found after failure may not be filled in retroactively.

## 2. Four control cases

### Success 1: US broadcast television (1948–1955)

- **Decision date T**: 1948, when television ownership was about 1% of US households.
- **B1 call**: pass. Broadcast towers were new dedicated infrastructure, but advertising supplied an independent revenue stream; broadcasters did not have to recover the entire tower network from household fees before the audience existed.
- **Outcome**: by 1955, US household television ownership was about 75%, a society-scale transition in seven years.
- **Source location**: this repository’s [01-retrospect.md §3, “Gate 3 · Nobody builds a road for one thing”](../en/01-retrospect.md), the US television bullet; it links to [Television in the United States](https://en.wikipedia.org/wiki/Television_in_the_United_States) and records both years and the advertising mechanism.

### Success 2: BankAmericard’s “Fresno Drop” (1958)

- **Decision date T**: the September 1958 launch of the Fresno experiment.
- **B1 call**: pass. Bank of America used its own balance sheet to absorb the start-up cost of mailing roughly 60,000 pre-activated cards; merchant fees, interest, and transaction volume supplied a recurring recovery path. It did not wait for cardholders and merchants to appear first.
- **Outcome**: the credit-card network expanded from the city experiment into the basis of the later Visa system. The judgment is that a start-up loop existed, not that later global scale was inevitable in 1958.
- **Source location**: this repository’s [01-retrospect.md §3, “Gate 4 · Who holds the decision”](../en/01-retrospect.md), the BankAmericard bullet; a checkable external account is [99% Invisible: The Fresno Drop](https://99percentinvisible.org/episode/the-fresno-drop/), which records the 1958 date, approximately 60,000 cards, and the no-application distribution.

### Failure 1: Webvan (1999–2001)

- **Decision date T**: the 10 December 1999 S-1 filing, when distribution-center rollout and order density were still explicit prerequisites for expansion.
- **B1 call**: fail. The company was carrying dedicated warehouse, delivery, and rollout costs, but there was no evidence that order density could already produce recurring recovery at the same pace; customer growth, order size, and distribution-center rollout remained unverified quantities.
- **Outcome**: Webvan’s 2000 Form 10-K reports approximately $178.456 million in net sales and a $453.289 million net loss; the pre-T 2000 forecast was a $154.3 million net loss, so the realized loss was about 2.94 times the forecast. The model did not establish a sustainable fixed-cost recovery loop.
- **Source location**: this repository’s [business-forecast-calibration-2026-09.md §Case A](business-forecast-calibration-2026-09.md) (the anchor text should be read from the rendered heading; the page itself is the stable entry), which preserves stable SEC S-1 and 2000 Form 10-K URLs, page/line locations, and SHA-256 hashes. That page classifies this as commercial forecast calibration, not as an exclusive falsification of a diffusion gate.

### Failure 2: Better Place battery swapping (2010–2013)

- **Decision date T**: the commercial deployment promise period around 2010.
- **B1 call**: fail. The swap network required about $850 million in financing, dedicated stations, and simultaneous changes by carmakers; the payer had to invest first, while the vehicle volume needed for high-frequency recovery had not formed, and the dedicated assets had no independent second use.
- **Outcome**: Israel sold only 518 related cars during all of 2012, and Better Place filed for bankruptcy in May 2013.
- **Source location**: this repository’s [01-retrospect.md §3, “Gate 3”](../en/01-retrospect.md), the Better Place bullet, which links to [Better Place](https://en.wikipedia.org/wiki/Better_Place_(company)) and records the financing, 2012 sales, and 2013 bankruptcy.

## 3. Counterexample and independence test

The four cases provide two passing controls and two failing controls; B1 gives an explicit “no” to Webvan and Better Place rather than merely explaining success.

But the candidate **fails the admission test for the toolbox**, not because the four cases lack support, but because it has no independent discriminating power against the existing gates:

- US television’s independent advertising revenue is already a positive example under existing Gate 3;
- Better Place’s dedicated swap network is already a Gate 3 failure and also invokes Gate 4’s multi-party coordination;
- Webvan’s fixed-cost and order-density problem falls under Gate 3’s carrier condition and Gate 5’s incumbent-relative net burden boundary;
- BankAmericard’s “one actor subsidizes the start-up cost in one stroke” is already an explicit Gate 4 route.

B1 therefore renames the revenue-recovery side of existing **Gate 3 (carrier)** and **Gate 4 (decision)**, without finding a case in which every other gate passes and B1 alone says no. Under the methodology’s independence lock, it cannot become a new L lens; adding it would count one bottleneck twice.

**Calibration verdict: B1 was tried and not admitted because its independent discriminating power against Gates 3/4 could not be shown.** It remains a commercial-history failure candidate and boundary note; no existing L1–L10 definition is expanded.

## 4. Forecast-miss count and feedback

- **New commercial-history “inaccurate forecast” cases found this round: 0.** The four cases above were selected after their outcomes and are `CALIBRATION` controls, not forecasts frozen before their outcomes. They cannot be presented as accuracy evidence. The existing Webvan/eToys forecast-miss record remains in [business-forecast-calibration-2026-09.md](business-forecast-calibration-2026-09.md); this round adds no countable forecast miss.
- **Existing judgment cards affected: 0.** B1 was not admitted, so it introduces no new lens verdict that could negate a card’s reasoning step, and no existing conclusion, status, confidence, or time window is changed. Search method: search `docs/{zh,en}/chains` and `docs/{zh,en}/ledger` for `B1`, `payer`, `beneficiary`, `支付者`, `受益者`, `固定成本`, and `交叉补贴`, then inspect each hit to distinguish existing Gate 3/4 prose from a B1-registered card; no judgment card registered as B1 was found. The feedback result is therefore “0 cards affected.”

## 5. Method status

This page completes historical `CALIBRATION` only. It supports a writing reminder—make the payer and recovery path for fixed costs explicit—but does not upgrade that reminder into a new lens or provide future forecast accuracy. A future attempt must freeze a new, outcome-independent commercial case set and define the independence test in advance; these four cases cannot be used to claim that the method has been validated.
