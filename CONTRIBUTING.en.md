# How to Refute a Judgment Here

[中文版](CONTRIBUTING.md)

This repository has exactly one selling point: every judgment states how it dies. Writing down “what will happen” is cheap. Writing down “what I would have to observe to admit I was wrong” is expensive — and that is the deposit every judgment card here has to put up.

A deposit only counts if someone can claim it. If the author is the only one who ever checks the author on the due date, “falsifiable” decays into a writing format. So this file answers three things:

- [how to falsify a judgment](#how-to-falsify-a-judgment) — you hold a fact that overturns one;
- [how to propose a missing dimension](#how-to-propose-a-missing-dimension) — the landscape is missing a population, a physical constraint, or an institutional side;
- [what will not be taken up](#what-will-not-be-taken-up) — stated up front, to save us both the time.

Submissions come in as GitHub issues, with two templates: **Falsify a judgment** and **Propose a missing dimension**. Their fields map one-to-one onto the two sections below; filling in the form is enough.

## You only need four words

Every judgment holds one card in the [judgment ledger](docs/en/90-ledger.md), under a project-unique `J-NNN` identifier shared by both languages. The required fields are listed in [the ledger’s card fields](docs/en/90-ledger.md#11-judgment-card-fields), and the rule itself is in [the methodology](docs/en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids). You do not have to read either of them end to end. Four words are enough:

| Word | What it is | Where it is defined |
|---|---|---|
| **Falsifier** | the concrete event that would make the author admit this judgment is wrong | [Methodology §4](docs/en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids) |
| **Leading indicator** | an observable signal expected to move before the outcome does | [Methodology §4](docs/en/00-method.md#4-judgment-cards-the-five-part-requirement-and-ids) |
| **Confidence** | `high` / `medium` / `low` — how much is being bet, not how strong the tone is | [Methodology §8](docs/en/00-method.md#8-confidence-and-status) |
| **Status** | `ACTIVE` awaiting testing · `HIT` supported within the window · `FALSIFIED` falsifier triggered · `REVISED` rewritten by new evidence | [Methodology §8](docs/en/00-method.md#8-confidence-and-status), [Ledger §1.1](docs/en/90-ledger.md#11-judgment-card-fields) |

Those four words are the entire vocabulary; there is no second set. You submit in them, and the maintainers answer in them. The Chinese–English correspondence is in the [glossary](docs/glossary.zh-en.md); judgment identifiers are never translated or renumbered.

## How to falsify a judgment

A falsification that can actually be processed is a combination of three things: **the identifier + the verbatim falsifier it triggers + a verifiable evidence anchor**. Miss one and there is nothing to act on — not as a matter of attitude, but because there is no place to start.

**1. The identifier.** Write `J-NNN`, taken from the [registered-judgment overview](docs/en/90-ledger.md#2-registered-judgment-overview). Do not refer to a card by its title or as “the one about AI”: titles get rewritten, identifiers are never reused.

**2. Which falsifier.** Open the card and **quote verbatim** the line under “Falsifier” that you believe has triggered, then say which event triggered it. A judgment may list more than one trigger; naming the one you mean is what keeps the answer on the same subject.

If you think the **falsifier itself is written too loosely** — so loose that nothing could ever trigger it — that is also a valid falsification submission, and the most valuable kind. Say so directly, and give one concrete case that the falsifier should have caught and did not.

**3. The evidence anchor.** Give something a third party can open and check independently:

- **A link**: primary sources first (the original announcement, the original dataset, the statute, the audit report). Chase a second-hand account back to its source; if you cannot, say that you could not.
- **Data**: state the measurement basis. Two numbers measured differently cannot be subtracted, or divided — the ledger’s [external-comparison sources](docs/en/90-ledger.md#9-external-comparison-sources-for-this-round) already carry entries that spell out “this source does **not** support the stronger claim,” and that is the precision expected here.
- **A date**: the date the event happened, not the date you saw it. Time-window judgments are often decided by a few months.

**4. Optional, but useful: what it drags down with it.** The `depends-on` field forms a graph ([Ledger §3](docs/en/90-ledger.md#3-the-depends-on-graph)). When an upstream judgment falls, everything standing on it must be reviewed. If you list those, the blast radius of your falsification is settled in one pass.

### What the maintainers will do with it

The [expiry-review procedure](docs/en/90-ledger.md#5-expiry-review-procedure) is followed step by step. There are exactly three outcomes, and all three get written down:

- `FALSIFIED` — the falsifier did trigger. The card **stays where it is**, marked falsified, and every downstream dependency is reviewed along the graph.
- `REVISED` — the judgment needs rewriting rather than overturning. The old card is kept, the new version takes a new identifier, and the old one remains in git history.
- Still `ACTIVE` — the evidence does not settle it. In that case what is **still missing** must be stated, together with the next review date. Vagueness is not an option here.

Either way it is recorded in the [review log](docs/en/90-ledger.md#8-review-log); if the confidence level moved, it also enters the [confidence-change history](docs/en/90-ledger.md#4-confidence-change-history). Chinese and English are updated in the same commit.

One thing will not happen: **silent absorption**. Even when we do not accept your conclusion, the answer is written as an explicit paragraph — agreement / disagreement / why I still hold it — which is the fixed format of [Methodology §1.2](docs/en/00-method.md#12-fixed-format-for-external-comparison), not a courtesy.

### The rules themselves can be falsified, through the same channel

The five diffusion gates in the [retrospect](docs/en/01-retrospect.md) are not axioms. Each gate is itself a judgment card (`J-067`–`J-071`), as are the lock that says the five gates are necessary but not sufficient (`J-066`) and the card that runs the gates back over this repository's own writing (`J-072`) — all of them with falsifiers of their own. To attack one existing judgment, name the identifier, quote its falsifier, and bring evidence. To submit a batch of new historical cases that tests the rule set as a whole, first follow the [Historical Pseudo-Out-of-Sample Validation Protocol](docs/en/02-historical-validation-protocol.md): freeze the candidate pool, as-of dates, holdout, role isolation, baselines, and scoring before any outcome is examined.

What `J-066` demands, for instance, is a capability that **clearly fails at least one of the five gates and still reaches society-wide diffusion within ten years** (billions daily, or hundreds of millions weekly), whose diffusion cannot be explained by an unlock condition already written into the text (abridged; the card carries the full wording). Produce such a case and the gates have to change — that is an invitation printed in the text, not a loophole.

## How to propose a missing dimension

“A landscape covering every direction” is an **open clause** in this repository, not a finished job. The known gaps are registered in [the ledger’s list of dimensions not yet covered](docs/en/90-ledger.md#6-explicit-gaps-dimensions-not-yet-covered). **Read that table first**: what you have in mind may already be on it with the status “partially covered” — in which case saying precisely which half is missing is far more useful than filing it again.

A gap that can be processed answers two questions.

**1. What is missing.** Name a population, or a physical side (bodies, energy, land, materials, transport, climate), or an institutional side (law, property rights, regulation, permitting, compensation).

- Not a gap: “there should be more on ethics,” “the perspectives are not diverse enough.”
- A gap: “the constraint that care work requires a body to be physically present is covered by no judgment here” — it names the population, names the constraint, and can be reasoned forward from immediately.

**2. Whether it carries scale.** A niche phenomenon may not be written here in the voice of a society-wide trend. Using the yardstick of [Gate 1, “count the people before you look at the technology”](docs/en/01-retrospect.md#gate-1--count-the-people-before-you-look-at-the-technology), give four things:

- **Order of magnitude**: is the affected population a hundred thousand / a million / ten million / a billion;
- **Who they are**: occupation, role, region — “users” is not a population;
- **Frequency**: is the activity daily / weekly / monthly / yearly;
- **Which kind**: does it **raise the ceiling for people who already do this professionally** (the ceiling is then the headcount of that occupation), or does it **let people who could not do it do it at all** (which can enlarge the activity itself)? The second kind must name a mechanism, not merely claim one.

Failing to carry scale does not mean worthless. Such a finding is kept as a **local or occupational judgment**; it simply may not be written in the voice of “society,” “generally,” or “becomes the norm,” and no society-level consequence may be derived from it. The repository already holds one such card: [`J-072`](docs/en/90-ledger.md#j-072--choosing-one-from-dozens-of-generated-candidates-is-an-occupational-judgment-not-a-society-level-trend) rules this project’s own opening scene to be an occupational judgment with a ceiling in the millions — the gate cuts its author first.

### What the outcome will be

- It enters the gap list, with the question it must answer and a priority;
- or it is written straight into a judgment card (if you brought a falsifier and a leading indicator, most of that work is already done);
- or it is ruled a local judgment, stating which scale threshold it fails.

A gap is only ever filled or explicitly downgraded — **never silently deleted from the list**.

## What will not be taken up

The following are closed with a one-line explanation. This section exists so you do not have to write the whole thing before finding out it cannot come in.

- **An objection with no falsifier behind it.** “I don’t think that will happen,” “this is too optimistic” — please name the falsifier you believe triggered. (Arguing that the falsifier itself is too loose is a different matter; see [above](#how-to-falsify-a-judgment), and it is welcome.)
- **A position with no mechanism.** What the methodology demands of a “strongest opposing case” applies equally to objections from outside: it must be a specific mechanism that could occur, not an attitude. “You ignore human nature” is not an objection; “this judgment requires people to give up a status signal under condition X, and that has never happened” is.
- **Claims that cannot be checked.** No source; a source that does not open; a second-hand account with no traceable original; a private observation nobody else can reproduce; a screenshot with no provenance or date.
- **Somebody else’s forecast used as an argument.** “Institution X projects that by 2030…” is not an argument — [Methodology §1](docs/en/00-method.md#1-legitimate-starting-points-for-reasoning) explicitly refuses anyone’s prediction as a starting point. It may, however, be submitted as **external-comparison material**, which is a different thing: it is processed in the “agreement / disagreement / why I still hold it” format and registered as an `EXT-NN` source.
- **Claims that do not carry scale but are written in a society-wide voice** (see the four-part yardstick above).
- **Requests to delete a falsified judgment.** Falsified cards are never deleted: without them the hit rate per confidence level cannot be computed and nothing can be learned from the error. Such a card stays in place, marked `FALSIFIED`.
- **Proposals to add an automated delivery gate** (CI / workflows / “green means good”). Judgment quality here is not adjudicated by a machine. `scripts/check.py` checks mechanical invariants only — whether links resolve, whether required fields are present, whether a confidence value is on the whitelist, whether the two languages carry the same set of identifiers. It reports facts; it does not rule on whether a judgment is right, nor on whether this repository is fit to publish.
- **Pure style preferences.** “This section is too long” is not an issue. A specific expression problem is an issue, and a welcome one: which sentence does not parse, which term is used inconsistently, which link does not land where you expected.

## When to open a pull request instead

Small fixes need no issue first: typos, broken links, a Chinese–English mismatch in the [glossary](docs/glossary.zh-en.md), a plain factual error with a primary source — open a PR.

Two hard rules:

1. **Chinese and English must be updated in the same commit.** They are two projections of one judgment, not two sets of judgments. Change one side only, and the other starts rotting into a stale fork. If you work in only one of the two languages, open an issue rather than a PR and let a maintainer mirror it.
2. **The commit message states which judgment changed and on what new evidence** — not a running log such as `update docs` ([Methodology §9](docs/en/00-method.md#9-bilingual-and-git-discipline)). In this repository, git history is what carries the evolution of the judgments.

**To change a judgment itself, open an issue rather than a PR.** One rewrite has to move the card, the review log, the confidence-change history, and both languages at once, which is hard to get right in a pull request.

Before opening a PR you can run the mechanical self-check locally:

```sh
python3 scripts/check.py
```

It verifies that links resolve, that card fields are present, that confidence values are on the whitelist, and that the two languages register the same identifiers. Exit code 0 means those mechanical invariants hold — it does not mean your judgment is right. That is not something a machine rules on.

---

What this repository is least short of is judgments. What it is most short of is a fact that takes one down.
