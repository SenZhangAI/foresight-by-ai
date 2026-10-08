# Retrospect: What It Takes to Become a Society-Wide Habit

[中文版](../zh/01-retrospect.md)

[Back to README / document map](../../README.en.md)

> **Where this document sits**: after the methodology, before every chain of reasoning. It predicts nothing. It looks back at successes and failures that have already happened and extracts a set of gates from them—a way to judge whether a capability can become **the way a whole society does things**.
> **In one sentence**: a technology working is not the same thing as it happening. In the most expensive failures of the past sixty years, the technology worked every time.

---

## 1. In 1964, someone had already finished building the future

In April 1964 a queue formed at the Bell Labs pavilion at the New York World's Fair. Visitors took turns sitting in a small booth and talking, through a screen, to a stranger far away in California—**and they could see the other person's face**. That same month, Bell also completed a transcontinental video call between New York and Anaheim.

This was not a prototype. On 1 July 1970 the Picturephone entered commercial service in Pittsburgh, and expanded to Chicago the following year. AT&T's 1969 annual report put the forecast in writing: by 1980, one million sets, a billion-dollar business.

What actually happened: Pittsburgh peaked at 32 sets, Chicago at 453. **Fewer than 500 in total.** Cutting the monthly rent from $160 to $75 did not help either. A few years later the service was quietly shut down ([ETHW](https://ethw.org/Picturephone), [Wikipedia](https://en.wikipedia.org/wiki/Picturephone)).

Fifty-six years later, in March 2020, the same thing—**talking to someone while looking at their face**—was learned by hundreds of millions of people in three months. Zoom's daily meeting participants went from 10 million in December 2019 to 300 million in April 2020, a thirtyfold rise ([Zoom, official](https://www.zoom.com/en/blog/reflecting-looking-ahead/)).

Notice what did **not** change between the two events:

- Demand did not change. People in 1964 wanted to see each other's faces exactly as much as people in 2020 did.
- The technology did not become more "possible." The 1964 video call was already clear, usable, and ready for commercial service.

Something else changed. **Finding that something is this document's entire task.**

Before going further, one thing we did has to be admitted as a mistake: this project's reasoning has quietly assumed throughout that *technical capability arrives → the trend happens*. All nine lenses answer "how does change happen"; not one of them asks "will the change diffuse at all, and to enough people?" The Picturephone on its own is enough to show that default is wrong.

---

## 2. Three locks first: explanatory power is not evidence

The great danger of hindsight is that **it can always make itself come out right**. Hand me any failure and I can compose a set of very reasonable-sounding causes; hand me any success and I can do the same. A rule that explains every case is not a filter, it is a narrative.

So before proposing any rule at all, three locks:

1. **Every rule needs a control group**: at least 2 successes + 2 failures, with cases spanning technology, politics, and business. Anything supported only by successes is treated as survivorship bias.
2. **Every rule needs an exclusive case**: there must be at least one case that **only this rule stops**, with the other rules all letting it through. A rule with no exclusive case is a restatement of another rule and should be merged away.
3. **The set as a whole needs a counterexample**: we must be able to name a case that **passes all of them and still fails**. If we cannot, the set is quietly posing as a sufficient condition—and that is prophecy, not filtering.

Lock 2 is the heaviest attack this document makes on itself; section 5 is given over entirely to carrying it out. The answer to lock 3 is in section 6, and the answer is: **yes—and it is the most famous case in business history.**

---

## 3. The five gates

Each gate was induced from the batch of cases above; the gates did not come first, with cases hunted down afterwards to fit them. The test is the first line under each subtitle, ready to be used as it stands.

### Gate 1 · Count the people before you look at the technology

**The test**: the activity this capability serves—**how many people do it, and how often**? The ceiling on how many people a capability can reach is set by the headcount × frequency of that activity, not by the ceiling of the technology.

Ask one layer deeper: does it **raise the ceiling for people who already do this professionally**, or does it **let people who could not do it at all do it now**? The ceiling of the first is the headcount of that occupation; only the second can enlarge the activity itself.

**Passes, and did reach society scale**:

- *Technology*—the smartphone. The activity served is "contact someone, look at something, find your way, pay for something," which a billion people do dozens of times a day. In 2023, 4.3 billion people worldwide owned a smartphone, 54% of the world's population ([GSMA](https://www.gsma.com/newsroom/press-release/smartphone-owners-are-now-the-global-majority-new-gsma-report-reveals/)).
- *Politics*—China's health code. The activity served is "entering a venue," which the entire population does many times a day. By April 2020 it covered more than 200 cities.
- *Business*—mobile payment. The activity served is "paying for something," and a billion-scale population does it many times a day. Annual mobile-payment consumption in China runs into the trillions of dollars (industry figures differ widely; see section 11's weak-evidence list—**this is used only to indicate the order of magnitude, and the conclusion here does not rest on the number**, but on the headcount and frequency of the activity itself).

**Stopped by this gate**:

- *Business*—Concorde. The activity served is "crossing the Atlantic, and being willing to pay several times the fare to save three or four hours." The people doing that are counted on the order of a hundred thousand trips a year. Result: 27 years in service from 1976 to 2003, only 20 aircraft built in all, and only 14 ever in commercial operation ([Wikipedia](https://en.wikipedia.org/wiki/Concorde)). The technology was a complete success.
- *Business / technology*—the Iridium phone. The activity served is "making a call where there is no cellular signal." At bankruptcy in 1999 it had 55,000 subscribers, against the million-plus needed to break even ([Forbes 2001](https://www.forbes.com/2001/11/30/1130tentech.html), [Wikipedia](https://en.wikipedia.org/wiki/Iridium_Communications)). All 66 satellites launched successfully and the system worked exactly as designed.
- *Politics / society*—Esperanto. Published in 1887, more than one hundred and thirty years ago. The language itself is well designed, easy to learn, and neutral. But in the world of 1887, the overwhelming majority of people would never in their lives meet an occasion requiring everyday conversation across native languages—that activity simply did not exist for enough people. Estimates of fluent speakers today range from 63,000 to two million, a thirtyfold spread; that the range is disputed at all tells you the scale is small ([Wikipedia](https://en.wikipedia.org/wiki/Esperanto)).

**An important property of this gate: failing it is not the same as failing.** Professional video-editing software does not pass Gate 1—its ceiling is the number of editors there are—yet its adoption among editors approaches 100% and it is a good business. The correct reading of a Gate 1 failure is: **the ceiling equals the size of that group, and it will never become a society-wide habit.** That distinction is the most important correction this document makes to the project, and section 7 uses it on our own writing.

This rule is recorded as [J-067](ledger/61-70.md#j-067--the-audience-ceiling-of-a-capability-is-the-headcount-and-frequency-of-the-activity-it-serves).

### Gate 2 · Whatever diffuses was substituted in, never added on

**The test**: which activity that users **already do today** does it replace? Once replaced, how far does the unit cost of that activity (money, time, attention) fall? If the answer is "it replaces nothing, it is just one more thing to do," the ceiling is hobbyists.

**This gate has exactly one failing condition: it replaces nothing.** The size of the cost drop is not a pass mark but a speed variable—a capability that cuts cost by an order of magnitude (the container, 97%) moves fast, and one whose cost barely falls, or does not fall at all, still counts as replacement; it simply needs another gate to explain why it did not happen. Writing a cost threshold into the failing condition would let this gate swallow Gate 3; section 5 faces that fork head-on rather than stepping around it.

The logic lies in what the cost is measured against. Adopting a new capability means paying fixed costs—learning it, buying it, reorganizing a process around it—and those costs only pencil out when there is an old activity to charge them against. Replace nothing and the benefit has to prove itself from scratch, so adoption runs on curiosity alone—and the stock of curiosity is exactly the number of hobbyists.

**Passes**:

- *Business*—the shipping container. It replaced break-bulk loading. In 1956 the traditional method cost $5.83 per ton; the container method cost 15.8 cents per ton, a fall of about 97% (Marc Levinson, *The Box*, Princeton University Press).
- *Politics*—China's household responsibility system. It replaced work-point accounting by the production team. Same land, same people, same seed; the only thing that changed was who bore the cost of supervision. Justin Yifu Lin's 1992 study in the *American Economic Review* attributes **about half** of the growth in agricultural output between 1978 and 1984 to this decollectivization ([AER 82(1): 34-51](https://econpapers.repec.org/RePEc:aea:aecrev:v:82:y:1992:i:1:p:34-51)).
- *Business / technology*—QR-code payment. It replaced pulling out cash, making change, and reconciling the till.

**Stopped**:

- *Technology*—Google Glass. It replaces no activity you do today; it adds one to your face. The 2013 Explorer edition was priced at $1,500, and consumer sales ended in January 2015 ([Wikipedia](https://en.wikipedia.org/wiki/Google_Glass), [BBC](https://www.bbc.com/news/technology-30831128)).
- *Business*—3D television. It does not replace "watching television"; it adds an attribute to watching television, and that attribute costs extra. ESPN 3D launched on 11 June 2010 alongside the World Cup and closed on 30 September 2013, the official reason being "limited viewer adoption" ([Wikipedia](https://en.wikipedia.org/wiki/ESPN_3D)).
- *Politics / education*—MOOCs. This is the case most worth studying, because it **replaced the wrong thing**. A MOOC replaces "attending the lecture," but what students are actually buying is the credential—and the credential was not replaced at all. A peer-reviewed study published in *IRRODL* in 2015 gives a median completion rate of 12.6% (range 0.7%–52.1%, [Jordan 2015](https://www.irrodl.org/index.php/irrodl/article/view/2112)). The San Jose State University / Udacity pilot of spring 2013 had pass rates of only 20%–44% and was suspended that July ([LA Times](https://www.latimes.com/local/lanow/la-me-ln-san-jose-online-20130718-story.html)). Udacity founder Sebastian Thrun's own words at the time were "We have a lousy product" (*Fast Company*, November 2013).

This rule is recorded as [J-068](ledger/61-70.md#j-068--what-diffuses-replaces-an-activity-already-happening-not-something-added-on-top).

### Gate 3 · Nobody builds a road for one thing

**The test**: what new infrastructure does this capability need **exclusively for itself**? Who pays for it, and why? If that infrastructure has no second use beyond this capability and no independent revenue stream, then either it will not get built, or the capability has to wait until somebody else builds it for reasons of their own.

This is the thing that changed between 1964 and 2020. The Picturephone needed dedicated broadband loops and dedicated terminals, and that kit had no second use—AT&T had to carry the entire cost alone and recover it from a user base that did not yet exist. Video calling in 2020 needed no dedicated infrastructure whatsoever: front-facing cameras, broadband, and screens were already in billions of pockets **for other reasons**, and an adopter's marginal hardware cost was zero.

**Passes**:

- *Technology*—video calling, 2020. The carrier was supplied free of charge by the spread of the smartphone.
- *Business / technology*—television in the United States. Broadcast towers really were new, dedicated infrastructure—but they had an independent revenue stream: advertising. So they got built. American household television ownership was about 1% in 1948 and about 75% in 1955 ([Wikipedia](https://en.wikipedia.org/wiki/Television_in_the_United_States)).
- *Politics*—the health code. It ran inside Alipay and WeChat, which were already installed; it was a mini-program, and **it made nobody install a new app** ([Social Media + Society, 2020](https://journals.sagepub.com/doi/pdf/10.1177/2056305120947657)).

**Stopped**:

- *Technology*—the Picturephone, 1964. See above.
- *Business*—Iridium. 66 satellites plus dedicated handsets, roughly $5 billion, existing for this one thing only.
- *Business*—Better Place battery swapping. It needed a network of swap stations, and it needed carmakers to change their designs. It raised about $850 million and went bankrupt in May 2013; Israel sold 518 cars in all of 2012, against the founder's earlier promise of a hundred thousand by 2010 ([Wikipedia](https://en.wikipedia.org/wiki/Better_Place_(company))).

This rule is recorded as [J-069](ledger/61-70.md#j-069--infrastructure-that-serves-only-one-capability-does-not-get-built).

### Gate 4 · Who holds the decision settles the outcome earlier than how good the technology is

**The test**: in whose hands does the adoption decision land? If one party can decide unilaterally, this gate passes automatically. If **several parties must change at the same time**, then one of the following three is required; without one, it stops at the pilot:

- **(a) authority that can compel, and whose enforcement can be seen**—both conditions, neither optional;
- **(b) a single party able to subsidize away every side's start-up cost in one stroke**;
- **(c) a local closed loop**—two machines, one port dealing with one port, or one industry internally can get it working first, without waiting for society as a whole.

The "can be seen" half of clause (a) is the half history most often forgets.

**Passes**:

- *Politics*—the health code. It could compel, and enforcement was visible at the entrance of every venue. Nationwide within a few months.
- *Politics*—the household responsibility system. In 1978, 18 households in Xiaogang divided the land; by the end of 1979, 51% of production teams in Anhui had adopted some form of responsibility system; in 1982 Central Document No. 1 established it as national policy; in 1983 it was rolled out everywhere. Roughly four to five years from experiment to nationwide ([Wikipedia](https://en.wikipedia.org/wiki/Household_responsibility_system)).
- *Business*—the ATM. A bank deploys unilaterally, a depositor uses it unilaterally, neither has to wait for the other. Barclays installed the first one in Enfield, London, on 27 June 1967 ([Barclays](https://home.barclays/news/2017/06/from-the-archives-the-atm-is-50/)).
- *Business*—the BankAmericard "Fresno drop" of 1958. This is the textbook specimen of clause (b): credit cards have the classic chicken-and-egg problem—no cardholders, so merchants do not accept; no merchants, so nobody signs up. Bank of America's answer was to mail roughly 60,000 pre-activated cards to residents of Fresno **without anyone applying**, using its own balance sheet to buy out an entire city's start-up cost in one stroke.

**Stopped**:

- *Politics*—American Prohibition. It could compel, but it **could not be seen**. The Bureau of Prohibition had only about 1,520 federal agents for a 1920 population of roughly 106 million—about one agent per seventy thousand people. New York alone had between thirty thousand and a hundred thousand speakeasies, and the bootleg economy ran at around $3 billion a year. Repealed in 1933 by the Twenty-first Amendment ([Wikipedia](https://en.wikipedia.org/wiki/Prohibition_in_the_United_States)).
- *Politics*—American metric conversion. The Metric Conversion Act of 1975 states in so many words that conversion is "completely voluntary," with no deadline and no penalty, and the US Metric Board was abolished in 1982 ([Wikipedia](https://en.wikipedia.org/wiki/Metric_Conversion_Act)). **But note that it did not fail across the board**: American science, medicine, and the military use the metric system entirely—wherever a **local closed loop** held, it diffused; in daily life, which requires the whole of society to change at once, it did not. Here both sides of clause (c) appear in the very same case.
- *Technology*—the Picturephone. The value of installing one depends on whether the other party installs one too, and AT&T had no power to compel anyone.

**One correction about the container**: from 1956 to the publication of the ISO standards (1968–1970) took more than a decade, and becoming the mainstream way general cargo moved took another ten years or so—the resistance being exactly the multi-party coordination Gate 4 describes (ports, railroads, trucking, unions, insurers, box standards). The popular economic-history account says that "Vietnam War military shipping supplied a buyer who could give orders unilaterally, and that forced standardization." This document **does not adopt** that account: the primary material points the other way. The US Department of Defense was adapting to a civilian container system that had already been commercialized, and the military's own CONEX boxes (introduced in 1952, more than 200,000 of them by 1967) were a separate system. Between 1967 and 1973 Sea-Land did ship roughly 1,200 containers a month to Indochina and did take about $450 million in revenue from the Department of Defense—**that one large buyer held up the economics of the route is a fact; that it forced standardization is an unproven narrative.**

This rule is recorded as [J-070](ledger/61-70.md#j-070--when-many-parties-must-change-together-change-needs-enforceable-and-observable-authority-a-single-subsidizing-party-or-a-local-closed-loop).

### Gate 5 (narrowed on 2026-09-21) · Recurring net burden relative to the incumbent

> **Current rule (CALIBRATION candidate)**: asking only whether each use adds an action is insufficient. Self-service retail supplies a mechanism-level counterexample candidate: it repeatedly transferred picking and comparison labor to shoppers, yet by 1948 complete self-service was already the majority operating method among US chain grocers (56%; independents were 39%, EXT-65). The quantity to compare is the **whole-system recurring net burden relative to the real incumbent**: added bodily, social, learning, and monetary burden minus saved waiting, price, time, and process cost. Because this round has only one majority-threshold year rather than a full time series, the rule is written as a candidate for later holdout attack; calibration is not treated as accuracy validation. Gate 2 still asks only whether a real incumbent activity is replaced; Gate 5 asks whether each repeated use is net lighter or heavier after replacement, so the two are not merged for now. Section 10 carries the full evidence-and-impact matrix.

**Calibration boundary**: the frozen subgroup is “US chain grocers” and the target is complete self-service. It reached 56% in 1948 (EXT-65), so the case is coded `D`, with **1948 (the calendar year, the narrowest currently evidenced interval)** as `outcome_date`. This is not consumer-level `S`: the round has no same-definition hundred-million-weekly behavior count and does not generalize a chain-store majority to independent stores.

**v1 test (narrowed)**: what bodily cost, social cost, and learning cost does a user pay **on every single use**? A one-time cost (buy once, register once, learn once) can be subsidized by the vendor, and it is amortized across uses; a recurring cost is not amortized—it accumulates linearly with frequency. So the more frequent the activity, the more lethal a recurring cost is.

**Passes**:

- *Technology*—the touchscreen phone. The learning cost is close to zero, a three-year-old can use one, and it is paid once.
- *Business*—QR payment and the credit card. Point the camera; sign your name. Both are zero recurring cost on a high-frequency activity.
- *Politics*—the health code. Each entry to a venue adds one scan: two seconds, zero learning, zero social cost—one of the preconditions for something done daily by an entire population spreading within months. **To be explicit**: the health code also passes Gate 4 (compellable and observable), so it is not isolated evidence for Gate 5, only a passing sample for this gate in the political domain; whether Gate 5 stands on its own is answered by the exclusivity test in section 5.

**Stopped**:

- *Business*—3D television. Every single time: put the glasses on, sit square to the screen, and risk eye strain.
- *Technology*—Google Glass. Its recurring cost was **social**: wearers were barred from casinos and cinemas, a wearer was set upon in a San Francisco bar in 2014, and "Glasshole" became a word. The cost of the camera had long since gone to zero; the cost of being stared at had not.
- *Politics / society*—Esperanto. The learning cost runs to hundreds of hours, and the return on that cost depends on **whether the other person has paid it too**. It is stopped by Gate 1 and Gate 5 at once.
- *Medicine / consumption*—contact lenses. **This is the exclusive case Gate 5 needed** (see section 5): they replace the act of wearing frame glasses, require no new infrastructure, are decided by the individual alone, and serve a billion-scale daily activity—so all four other gates pass. What stops them is the cost paid every time: CDC guidance requires washing and drying hands before every insertion or removal, removing lenses before sleeping, showering, or swimming, and keeping lenses away from water (EXT-39). The cost is not merely inconvenient: all-cause keratitis produces about one million outpatient and emergency visits each year, with about $175 million in direct medical costs in 2010 (EXT-39). Result: 16.7% of U.S. adults wore them in 2014 (CDC self-report, 40.9 million), and about 45 million people of all ages in 2016; more than half a century after contact lenses appeared, they have never approached a majority of the population that needs vision correction.

**This gate's scope needs one further correction, and this round makes it explicit.** Its original conclusion said the ceiling was "hobbyists"—a wording pulled from the small-audience Google Glass and 3D television cases. Contact lenses show that recurring cost can leave a ceiling **far above** hobbyists: 16.7% of adults is not a niche hobby. It is still far below the headcount of the activity served. So the precise conclusion is: **recurring cost pushes the ceiling far below the population performing the activity; how far depends on the size of the cost, rather than always landing at hobbyists.** This makes the gate measurable (the ceiling as a share of the activity population), while making it **weaker** than the old wording—it no longer predicts a specific order of magnitude.

**The v1 compulsion boundary still holds, but no longer describes the current rule by itself.** Version 1 narrowed the claim to “under voluntary adoption, recurring cost sets the ceiling”: seat belts, helmets, and airport screening all charge a bodily cost on every use yet can diffuse through Gate 4's compulsion route. The second calibration round adds the opposite direction: even under fully voluntary adoption, recurring labor can be offset by larger relative gains. The current rule therefore keeps both points—compulsion is an institutional bypass; voluntary adoption compares **recurring net burden** with the incumbent rather than merely asking whether friction exists.

This rule is recorded as [J-071](ledger/71-80.md#j-071--recurring-net-burden-not-gross-friction-sets-the-voluntary-adoption-ceiling).

---

## 4. Two layers: one rules on the ceiling, one on speed

**All five gates remain, but Gate 5 has been narrowed from “does any recurring cost exist?” to “what is the recurring net burden relative to the incumbent?”** Gates 1 and 5 rule on the ceiling; Gates 2 through 4 rule on speed and unlocking conditions. This is the current structure:

| Layer | Gates | Failing means |
|---|---|---|
| **Ceiling layer** | Gate 1 scale, Gate 5 recurring net burden | The audience is capped far below the activity population; Gate 5 can be bypassed through compulsion |
| **Speed layer** | Gate 2 replacement, Gate 3 carrier, Gate 4 decision | It stops at the pilot **until an unlocking condition appears**; if no unlocking condition can be written, treat it as “will not happen” |

**Why narrow rather than delete Gate 5?** Self-service retail shows that “doing one more thing on every use” does not automatically impose a ceiling. Shoppers repeatedly walk the aisles, compare, and pick their own goods, but their net burden can still fall if that labor buys lower prices, faster service, or more choice. Contact lenses, 3D television, and Google Glass show the other side: after a real incumbent activity is replaced, a positive and material burden on every use can still suppress adoption independently. Together the cases require a net comparison, rather than folding Gate 5 into Gate 2's narrower question of whether replacement exists at all.

The most useful thing about the speed layer is not that it says no. It is that **it forces you to write down the unlocking condition, which makes the judgment checkable.** The Picturephone in 1964 was stopped by Gate 3 and Gate 4 at once, and the unlocking condition was: "the carrier gets built for other reasons, and the person on the other end has a terminal too." Smartphones satisfied that condition between 2007 and 2015—and so it diffused within three months in 2020. **The gates did not merely rule that it would not happen; they spelled out the conditions under which the ruling would be overturned, and that overturning actually occurred.** This is the strongest form of proof a filter can offer.

A rough speed table can be read off the cases:

| Situation | Sample | From technically available to society-scale diffusion |
|---|---|---|
| The carrier is already widespread for other reasons, and adopters can decide unilaterally | video calling 2020 (3 months), the health code (months) | months – a few years (both samples land in the months range; the upper bound is extrapolated and **rests on no case**) |
| The carrier must be newly built, but an independent revenue stream pays for it | American television (1% in 1948 → 75% in 1955) | 7 – 20 years |
| Several parties must change together and nobody can compel | the container (1956 → ISO 1968–70 → mainstream around the 1980s) | 20 years or more |
| The carrier exists only for this one thing | the Picturephone (1964 → service shut down in the mid-to-late 1970s) | does not happen, until the carrier is built for other reasons |

The time windows on this project's existing judgments were written without this table in hand. **When this section was written (2026-09-19), re-reviewing them against it was downstream work and this document did not touch a single existing card. The 2026-09-20 review is now invalid for the narrowed J-071 rule; the pending isolated re-review described in [§11.B of the Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change) owns the new frozen, de-labelled, shuffled, isolated re-review. Until it closes, the old result represents v1 diffusion-gate semantics only.**

---

## 5. Independence test: every gate must have a case only it can stop

This is the second lock from section 2. If a gate has no exclusive case, it is a restatement of another gate and should be merged away. The second calibration round did not delete Gate 5, but narrowed its exclusive proposition from “any recurring cost” to “a positive and material recurring net burden relative to the incumbent.” The current result is:

| Gate | Exclusive case | Verdict date | How the other four rule | Control |
|---|---|---|---|---|
| **1 · Scale** | Professional video-editing software | 2015 | Replacement (replaces cutting by hand) ✓, carrier (runs on an ordinary computer) ✓, decision (an editor buys it unilaterally) ✓, cost (professional training, but one-time) ✓ | Editing on a phone: same activity, ceiling moves from a few million editors to a billion people |
| **2 · Replacement** | MOOCs | 2012–2015 | Scale (tens of millions of university students) ✓, carrier (rides on the existing internet) ✓, decision (a student enrolls unilaterally) ✓, cost (no higher than the "attending a lecture" it replaces—the hours of self-study are the product itself, not a toll paid before use) ✓ | The same courses as **for-credit courses on campus**: connect them to the credential and adoption happens at once |
| **3 · Carrier** | Hydrogen fuel-cell cars | 2015–2024 | Scale (driving) ✓, replacement (replaces the act of refueling, in almost exactly the same form: a 3–5 minute fill, comparable range) ✓, decision (a consumer buys unilaterally) ✓, cost (refueling is as quick as filling a tank) ✓ | Battery-electric cars: same activity, same replacement; the only difference is that sockets were spread everywhere long ago for other reasons |
| **4 · Decision** | American metric conversion | 1975–1982 | Scale (weights and measures; everyone, daily) ✓, replacement (replaces imperial, and the arithmetic is simpler) ✓, carrier (change the ruler; cost is minimal) ✓, recurring net burden (learn once, not relearn on every use) ✓ | Science and medicine in the same country: the local closed loop holds, so diffusion is complete |
| **5 · Recurring net burden** | Contact lenses | 2014–2016 | Scale (vision correction, billion-scale globally, EXT-40) ✓, replacement (replaces frames on each occasion) ✓, carrier (existing optometry and retail channels) ✓, decision (individual alone) ✓ | Frame glasses and self-service retail: the former turns recurring care into a one-time wearing cost; the latter adds recurring labor but offsets it through waiting, price, and choice gains—forcing this gate to judge net rather than gross friction |

All five gates still have an exclusive proposition, but Gate 5's is narrower than v1: it judges not “a recurring cost exists,” but “recurring net burden versus the incumbent is positive and material.”

Six things must be said plainly, or this table will be read as stronger than it is:

- **The hydrogen fuel-cell cell is the weakest square in this table, and the fork is written here rather than hidden.** A hydrogen car replaces the act of refueling in almost exactly the same form, so by Gate 2's failing condition (it replaces nothing) it passes. But its **fuel cost per kilometre is higher than gasoline**—retail hydrogen has long run above $30 per kilogram. If a reader holds that "unit cost must fall" belongs in Gate 2's failing condition, then the hydrogen car is stopped by Gate 2 as well, Gate 3 immediately loses its exclusive case, and **by section 9's own rule Gate 3 should be merged into Gate 2, leaving four gates rather than five**. The reason this document does not write it that way: hydrogen's high retail price is to a large degree a *consequence* of the missing carrier (few stations → low utilization → high cost per unit), and treating a consequence as an independent second obstacle counts one cause twice. But that reason can be broken—the fuel-cell energy chain (electrolysis + compression + fuel cell, round-trip efficiency around thirty percent) means its cost disadvantage against electricity would not disappear even with stations everywhere. **Show that a hydrogen car still fails Gate 2 in the counterfactual where the carrier is fully built, and Gate 3 should be merged.**
- **The second calibration round did not delete Gate 5, but it overturned a veto based on gross friction.** The first row used the Dvorak keyboard; independent review showed that all of its cost was “learn once,” which should pass by the gate's own arithmetic, while “it is on everybody else's machine too” belonged to Gate 4. The prose then substituted contact lenses. Self-service retail keeps attacking the boundary: shoppers repeatedly bear the labor of walking the aisles, comparing, and picking goods, yet in 1948 complete self-service already covered 56% of US chain grocers (39% of independents, EXT-65). Calling that “zero recurring cost” excludes saved waiting, price, and choice. Once those gains are admitted, the test must read “recurring net burden relative to the incumbent.” **The current outcome is a narrowing candidate for later holdout attack, not a validated law**: Gate 2 asks whether a real incumbent activity is replaced; Gate 5 asks whether repeated use is materially net heavier after replacement. If future work cannot find a clean case stopped only by that net burden, merge Gate 5 into Gate 2. Contact lenses, 3D television, and Google Glass remain on the failure side; self-service retail is the success-side calibration.
- **The second row (MOOCs) received the same attack, and both the answer and the fork are recorded here.** The attack is that a credential's value depends on employers and schools recognizing it, so multiple parties must change together and MOOCs are also stopped by Gate 4. The answer is that Gate 4 asks whether **adoption** requires anyone else to change: a student can enroll in and complete a MOOC alone. What fails is not adoption but the thing the student gets—not the coordination mechanism. **But this answer can be broken**: if "adoption" is defined to include receiving the return from adoption, Gate 4 covers this row and Gate 2 must find another exclusive case; its other two stopped examples (Google Glass and 3D television) are already also stopped by Gate 5, so Gate 2's exclusivity falls with it.
- **Every row now carries a verdict date, and all five cells in a row must use the same date.** Without this constraint, "the other four pass" can nearly always be manufactured by selecting different dates for different cells: the first row's "carrier (runs on an ordinary computer)" is true today, while professional editing's ceiling was set when editing became an occupation; exclusivity loses its constraint if dates can be cherry-picked.
- **The most attackable part of the contact-lens row is "replacement," not "cost."** Most wearers have not thrown away their frame glasses; they use both. If that counts as adding one more thing rather than replacing one, contact lenses fail Gate 2 and Gate 5 loses its exclusive case again. The answer here is to judge replacement **per occasion**: on a morning when someone wears contacts, the act is fully substituted for wearing frames. But this answer depends on counting the activity by occasion, a convention not used elsewhere in this document, so it is the row's weak point.
- **No sales figures are given here for the hydrogen-versus-battery-electric comparison.** That pair is a qualitative control; the conclusion reaches only as far as "the difference lies in the carrier," and does not extend to market share.

---

## 6. The sufficiency counterexample: all five gates passed, withdrawn 79 days later

The third lock from section 2: can we name a case that passes all five gates and still fails?

We can, and it is the most famous case in business history. On 23 April 1985 Coca-Cola replaced a formula it had used for 99 years and launched New Coke. Gate by gate:

- **Scale**: people who drink cola every day number in the billions. ✓
- **Replacement**: what it replaced was old Coke—same activity, same price, same shelf. ✓
- **Carrier**: exactly the same production lines, bottlers, and distribution network; marginal deployment cost zero. ✓
- **Decision**: Coca-Cola decided unilaterally to make it, consumers decided unilaterally to buy it. ✓
- **Recurring net burden**: zero learning, bodily, or social friction—and **it tasted better in blind tests**, which is precisely why the formula was changed. ✓

All five gates passed. On 11 July 1985, that is **79 days later**, Coca-Cola announced the return of the old formula ([The Coca-Cola Company](https://www.coca-colacompany.com/about-us/history/new-coke-the-most-memorable-marketing-blunder-ever), [Wikipedia](https://en.wikipedia.org/wiki/New_Coke)).

What was missed? L8 in this project's methodology: **a change in supply does not guarantee that demand stays unchanged—but demand is not only function, either.** What people buy is not always the thing itself. Coca-Cola was never selling a flavor; it was selling a token of identity, and the value of a token comes precisely from its not changing.

The conclusion has to be written hard: **these five gates are a veto-style filter, not a predictor.** Fail a gate and it will essentially not become a society-wide habit; pass all five and you have merely qualified to compete. This is recorded as [J-066](ledger/61-70.md#j-066--the-five-gates-are-necessary-not-sufficient).

---

## 7. Running these gates on what we ourselves have written

This project's C1 chain opens with a scene: a head of marketing receives sixty complete proposals and spends two afternoons deciding nothing. The whole chain starts from there and derives "choosing and trading off become scarce."

Now run Gate 1 on it, and count the people mechanically.

**Definition of the activity**: faced with a batch of already-generated candidate proposals, **pick one and be accountable for the result**.

**Who does this?** Three things must hold at once:

1. the job requires producing candidates in bulk (advertising and marketing creative, design and product, architecture and engineering proposals, consulting proposals);
2. the person holds the final call rather than executing someone else's;
3. the frequency is at least once a week.

The people who satisfy all three are concentrated in the **decision-making tier** of those job families. Reasoning from occupational structure, the global order of magnitude is **10⁶ (millions)**, and the frequency is **weekly, not daily**.

**This has to be stated explicitly: it is an estimate, not a statistic.** No citable global occupational statistics were obtained this round; the order of magnitude above comes from a constructed estimate of "which job families satisfy all three conditions at once." A reader is free to attack that construction—which is exactly why it is written down.

**Gate by gate**:

| Gate | Ruling | Reason |
|---|---|---|
| 1 · Scale | **Fails** | Ceiling in the millions, weekly frequency. Against the society-scale threshold (a billion people daily, or a hundred million people weekly) that is two to three orders of magnitude short |
| 2 · Replacement | Passes | It replaces "make three versions first, then pick one of the three"; on the making side, cost falls by more than an order of magnitude |
| 3 · Carrier | Passes | It rides on generation tools that are already widespread; an adopter's marginal deployment cost is close to zero |
| 4 · Decision | Passes | One person can decide unilaterally whether to use it |
| 5 · Cost | Borderline | The attention cost **rises**: candidates to look through go from 3 to 60 |

**Conclusion: this is an occupational judgment, not a society-level trend.** It may hold perfectly well within its own audience, but by this project's rules it may not be written in the voice of "the whole of society," "generally," or "becomes the norm," and no society-level consequence may be derived from it. This is recorded as [J-072](ledger/71-80.md#j-072--choosing-one-from-dozens-of-generated-candidates-is-an-occupational-judgment-not-a-society-level-trend).

**So what *is* society-level?** On the same chain, the thing that passes Gate 1 is not "choosing" but "making." "Needing a usable document, diagram, piece of copy, or program"—a billion people need that occasionally, and until now most of them **could not do it**. That belongs to the "lets people who could not do it do it now" category, and only there is the ceiling society-level. So this project's genuinely society-level judgments ought to grow on the "making" side, not on the "choosing" side.

There is a sharper attack on ourselves, and writing it down beats hiding it: **"pick one out of a large pile of candidates" is something e-commerce recommendation has already done for a billion people every day, for years.** There, "generating candidates" was never the bottleneck, and "ranking" was automated away long ago. That lines up exactly with this project's existing [J-002](ledger/01-10.md#j-002--selecting-objectively-high-quality-from-abundant-output-is-not-a-durable-scarcity-but-merely-a-24-year-window): selection gets eaten by the same force that produced the abundance.

**When this section was written (2026-09-19) it deleted nothing and downgraded nothing.** It only attached an audience-size qualifier to the existing judgments, and explicitly left “re-reviewing every card in the ledger against the new gates” to a separate job. **The 2026-09-20 v1 review is now invalid because J-071 was narrowed**: it represents v1 diffusion-gate semantics only, not the current rule. The full affected-card set, de-labelling, deterministic shuffling, and isolated re-review under the narrowed rule are owned by the pending isolated re-review described in [§11.B of the Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change); until that goal closes, the v1 review must not be treated as a current-rule result.

---

## 8. External comparison: where we overlap with consensus, and where we add to it

Per §1.2 of this project's methodology, once independent reasoning is complete an explicit comparison must be made, stating agreement, disagreement, and why we still hold our view.

**Agreement (consistent with consensus here; not disguised as an independent discovery)**:

- Gate 2, "replacement," overlaps heavily with **relative advantage**, one of the five attributes in Everett Rogers's 1962 *Diffusion of Innovations*; Gate 5, "cost," partly overlaps with **complexity** among those same five ([Rogers's five attributes](https://en.wikipedia.org/wiki/Diffusion_of_innovations)).
- Gate 4, "decision," is consistent with Mancur Olson's 1965 *The Logic of Collective Action*: rational self-interested individuals do not automatically act for a common interest unless the group is small or coercion and selective incentives exist ([Wikipedia](https://en.wikipedia.org/wiki/The_Logic_of_Collective_Action)).
- "Whether a technology is adopted is not decided by technical merit alone" is consistent with Paul David's 1985 path dependence and with Katz and Shapiro's 1985 network externalities ([path dependence](https://en.wikipedia.org/wiki/Path_dependence)).
- "There is a break between early adopters and the early majority" is consistent with Geoffrey Moore's 1991 *Crossing the Chasm* ([Wikipedia](https://en.wikipedia.org/wiki/Crossing_the_Chasm)).

**Disagreement and additions**:

- **This document rewrites attributes into veto-style necessary conditions.** Rogers's five attributes are a scoring scheme—the higher an innovation scores across the five dimensions, the faster it spreads. The five gates here are **fail one and the answer is no**, and they demand that you name the specific object (which activity is being replaced? who pays for the carrier? in whose hands is the decision?). A scoring framework is very hard to falsify; a veto checklist can be.
- **Gate 3, "carrier," has no precise counterpart in the existing literature.** Teece's 1986 complementary assets, the installed base of the network-effects literature, and Zittrain's 2006 generativity are all adjacent without being equivalent: they answer "who can profit from an innovation" and "why standards lock in," whereas Gate 3 asks "will this dedicated infrastructure actually get built at all?"
- **Gate 1, "scale," is a genuine gap in the literature.** This round's search found no existing diffusion framework that uses "the headcount and frequency of the activity served" as a screening variable placed ahead of everything else: Rogers's five attributes characterize properties of the innovation itself, and Bass's 1969 diffusion model characterizes the shape of the adoption curve; neither asks "how many people actually do this activity?" **This is the real increment this document adds to the existing consensus—but it also means nobody has ever calibrated it, so its confidence is no higher than medium.**

---

## 9. How these rules enter the reasoning that follows

### Scope tags in downstream pages

A downstream paragraph may carry a compact **scope tag** instead of repeating the full downgrade explanation. The tag is not a new verdict: it means that the cited judgment(s) failed Gate 1 (audience scale) in the 2026-09-20 ledger review, so their ceiling is the named occupational, organizational, or institutional audience. The paragraph must not be read as a society-wide trend claim. The cited `J-NNN` links remain the traceable card-level record; the Gate 1 test is above in this document, and the complete per-card record is in the [ledger review log](90-ledger.md#8-review-log).

This shorthand preserves two things locally: **which judgments are being scoped** and **what readers must not infer**. It deliberately does not repeat the full historical evidence or the audience estimate in every section; those belong here and in the ledger, where a rule change can update them once rather than leave bilingual copies to drift.

The seven judgments distilled here are already recorded in the ledger, numbered [J-066](ledger/61-70.md#j-066--the-five-gates-are-necessary-not-sufficient) through [J-072](ledger/71-80.md#j-072--choosing-one-from-dozens-of-generated-candidates-is-an-occupational-judgment-not-a-society-level-trend). They hold a peculiar position in this project's dependency graph: **These seven are the only judgments in the whole ledger that do not depend on J-001**, of which J-067 through J-071 are roots (no upstream at all) while J-066 and J-072 stand only on those five. Every other judgment stands on the technical judgment that "unit reasoning cost keeps falling," whereas these seven come out of historical retrospect and need no premise about AI at all—if AI stopped improving tomorrow, they would still hold.

So who should change what behavior:

- **Anyone writing a new judgment**: before writing down any society-level assertion, run Gate 1 first—count the headcount and frequency of the activity, and state whether it "raises the ceiling for people who already do this professionally" or "lets people who could not do it do it now." If the scale cannot be answered, write it as an occupational judgment.
- **Anyone writing a time window**: do not hand out a year by feel. Answer Gate 3 and Gate 4 first—who pays for the carrier, in whose hands the decision sits—and then take a range from the speed table in section 4.
- **Anyone re-reviewing existing judgments**: the time windows and audience voice of the ledger cards were written before these gates existed. When this document was written (2026-09-19) it only erected the gates and touched not a single existing card. **The 2026-09-20 card-by-card review is now invalid for narrowed J-071.** The pending isolated re-review described in [§11.B of the Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change) owns freezing the affected set and running the de-labelled, shuffled, context-isolated re-review. This round does not hand-pick individual cards. Until it closes, the old result represents v1 diffusion-gate semantics only. After the next rule change, the full review must follow the [Historical Pseudo-Out-of-Sample Validation Protocol, Section 11 B](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change).
- **Anyone attacking this set of gates**: the exclusive-case table in section 5 is the most fragile place. **Show that the "exclusivity" of any one row does not hold—that is, that the case is in fact also stopped by another gate—and that gate should be merged away, and this document's conclusions must shrink accordingly.** To add historical cases in batches, first freeze the candidate pool, holdout, same-input baselines, and one-shot reveal under the [Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md); cases chosen after their outcomes are known belong only to calibration, never validation.

---

## 10. Second historical calibration round: known outcomes may change rules, not impersonate predictive accuracy

This round happened after the [historical pseudo-out-of-sample validation protocol](02-historical-validation-protocol.md) was frozen, but all four cases were **selected after their outcomes were known**. Every one is therefore labelled `CALIBRATION`. They may expose a rule defect and force in-place revision of old prose; they may not enter a holdout or support a claim that the gates became more accurate.

| Domain and case | Judgment time T / target activity | Outcome code | Attack on the old rule | Rule and prose impact |
|---|---|---|---|---|
| **Business success: Piggly Wiggly self-service grocery** | First store, 1916-09-06; target subgroup = US chain grocers; activity = complete self-service | `D`; `outcome_date=1948`: 56% of chain grocers were fully self-service versus 39% of independents (EXT-65); no hundred-million-weekly count, so not `S` | Old Gate 5 treated “doing one more thing every time” as burden. The patent transfers selection to shoppers while reducing clerks and overhead (EXT-55); the 1948 majority threshold shows the mechanism did not remain on paper | **Narrow J-071 as a rule candidate**: gross friction → recurring net burden relative to the incumbent; propose synchronized revisions to the method, protocol input table, and section-5 independence claim, with the input-table change landing only in the separate protocol commit; later holdout attack is still required |
| **Political success: US seat-belt laws** | New York's first state use law in 1984; subgroup = US front-seat outboard occupants; activity = buckle on a trip | `D`; `outcome_date=1994`: the first nationally representative NOPUS observation was 58% (EXT-66); 2024 was 91.2% (EXT-56), scoped to daytime front-seat outboard occupants; no hundred-million-weekly count, so not `S` | Enforceable compulsion can overpower per-use bodily friction. This is not a fatal Gate 5 counterexample because the old prose already stated that boundary | **Keep the Gate 4 bypass**; do not generalize the ratio to every occupant / time, and do not attribute the entire increase to law alone |
| **Technology / business withdrawal: Google Stadia** | Consumer service launched 2019-11-19; stream games over existing broadband | `N`: shutdown announced 2022-09-29; service ended 2023-01-18 (EXT-57) | Google called the underlying technology “proven at scale” and a “strong technology foundation” while acknowledging lower-than-expected user traction. Technical usability plus an existing carrier did not guarantee demand | **Change no necessary gate**: this only shows that technology plus carrier readiness is insufficient to guarantee demand; it does not establish that all five gates passed. Google did not explain why traction was low, so this document does not invent pricing or library causality |
| **Political withdrawal: US year-round daylight-saving experiment** | Emergency year-round DST began 1974-01-06; a nationwide clock regime | `N`: the experiment was rolled back early and standard time returned on 1974-10-27 (EXT-58) | Gate 4 passes: one authority deployed it quickly. Gate 5 can only `ABSTAIN` at T because the recurring net burden of dark winter mornings emerged through operation. This is **not** “all five passed, still failed” | **Do not count it as a J-066 sufficiency counterexample**; it only shows that compulsion can launch policy but cannot replace longitudinal observation of recurring net burden |

One **mechanism probe is excluded from the matrix**: India's 2016 demonetization. The RBI annual report confirms that withdrawal of specified banknotes created surplus banking-system liquidity (EXT-59), but this round did not obtain the exact return share from the same authoritative page and did not preregister one target activity. It cannot honestly be coded as a gate success or failure, so it remains a candidate for a later round rather than padding the failure count.

The round therefore supplies two successes (self-service retail, seat belts) and two failures / withdrawals (Stadia, year-round DST) across business, technology, and politics. Only self-service retail forces the method to form a **rule candidate for later holdout attack**; it is not written as a validated law. The other three draw boundaries: compulsion can bypass friction, strong technology is not demand, and compulsory launch does not mean Gate 5 is already decidable. Stadia likewise shows that technology plus carrier is insufficient, not that all five gates passed.

### 10.1 Independent calibration of commercial forecasts: separate revenue, losses, and adoption thresholds

This round also adds two **previously uncounted, independent commercial forecast-miss cases**: Webvan and eToys. They do not establish the accuracy of the five diffusion gates; they attack how evidence from “commercial forecasts” is recorded. The forecast and outcome originals, verbatim excerpts, SEC page / line locations, stable URLs, and SHA-256 hashes are delivered with the repository in the [commercial forecast evidence packet](../evidence/business-forecast-calibration-2026-09.en.md); the Chinese packet is [中文证据包](../evidence/business-forecast-calibration-2026-09.md). The packet retains Iridium as an appendix on a financing-covenant threshold miss, explicitly not counted among the two forecast misses.

| Case | Pre-T original and same-metric outcome | Miss classification | Conclusion for the existing rules |
|---|---|---|---|
| **Webvan (business / e-commerce)** | The S-1 disclosed Goldman Sachs projections of `$120.0m` revenue and `$154.3m` net loss for 2000; the 2000 10-K reported `$178.456m` revenue and `$453.289m` net loss | Revenue scale +48.7%; actual loss about 2.94× forecast; deployment and cost assumptions missed | Does not overturn the five gates; adds a boundary: correct revenue direction is not a hit on profit / cost structure |
| **eToys (business / e-commerce)** | On 2000-12-15, the company's 8-K Exhibit 99.1 froze the quarter-ending 12-31 sales interval at `$120m–$130m`; the same-quarter 10-Q reported `$131.166m` | Actual crossed the pre-T upper bound by `$1.166m` (about +0.9%), a boundary `scale` miss under the interval-coverage rule, with the revision timing recorded separately | Does not overturn the five gates; adds a boundary: freeze revisions by version and record interval coverage separately from deviation magnitude |

These two cases **must not be smuggled in as five-gate counterexamples**: neither isolates an exclusive failure mechanism for one gate, and Webvan certainly does not show that “revenue direction” and “society-wide diffusion” are the same metric. What they force us to correct is the evidence discipline: future commercial judgments must separately record metric, unit, target date, forecast owner and source type (company / underwriter / financing covenant), deployment pace, outcome window, and outcome original. “Revenue grew” cannot conceal “loss scale was wrong,” and “the system worked” cannot be treated as “the adoption curve will arrive on plan.” This is a recording boundary, not a new diffusion law.

Both cases were selected after their outcomes were visible, so they are `CALIBRATION`, not holdout cases, and cannot support a claim that method accuracy improved. To enter a historical pseudo-out-of-sample holdout, commercial cases must first be drawn from a frozen SEC S-1/F-1 population, with error thresholds for revenue, loss, subscriber/customer, and deployment milestones separated before outcomes are opened.

### 10.2 Three-domain total: the current evidence does not meet the 12-case threshold

This synthesis counts only cases actually delivered by the three investigations and reconstructable by a fresh-context reader from the evidence packets: **4 cases** (P-01–P-04) in the politics packet and **2 cases** (Webvan and eToys) in the business packet, for **6 cases total**. All six were selected after outcomes were known and are therefore `CALIBRATION`, not out-of-sample accuracy evidence. All six record a miss under the current classifications (P-01, P-02, P-03, and P-04 are direction misses; Webvan is a scale miss; eToys is a boundary scale miss), so the project may record “at least six historical miss calibrations,” but may not turn that count into a method hit rate.

The technology investigation submitted candidates involving nuclear power, Carter-era solar, fifth-generation computing, and VR. Fresh-context review found that the nuclear case mixed different price metrics, the solar case lacked an actual share on the same definition as the target, the fifth-generation-computing case substituted project goals / prototypes for commercial adoption, and the VR case mixed revenue forecasts with device-unit forecasts and outcomes. They therefore **do not count**, and cannot be used to reach four technology cases. The current technology-domain count is **0**, and the three-domain total is **6/12**; the round therefore does not meet the delivery bar of at least four cases in each of technology, politics, and business and at least twelve cases overall.

This is not a new forecast, and it does not change any of the five gates. It preserves the evidence gap explicitly: a technology candidate may enter `CALIBRATION` only after its pre-T original, same-metric outcome, observation window, unit, and stable location are supplied. Until then, a retrospective trend narrative must not be promoted into a forecast-miss case. See the [politics calibration packet](../evidence/politics-calibration.md) and [commercial forecast calibration packet](../evidence/business-forecast-calibration-2026-09.md).

### 10.3 Evidence classes for the currently reconstructable material (2026-10)

Readers can reach the original locations, excerpts, and missing fields through the [latest cross-domain historical calibration evidence slice](../evidence/historical-calibration-2026-10-02.en.md). The public conclusion returned here is deliberately narrower than “we found material”: it distinguishes what the material supports from what it cannot prove.

| Case | Current class | What this material supports | What this material does not support |
|---|---|---|---|
| [`P-04`](../evidence/historical-calibration-2026-10-02.en.md#3-p-04-fomc-forecast-for-2008-real-gdp) | `CALIBRATION` | One reconstructable same-metric directional miss, indicating that a macro central interval can miss a crisis turn | Overall macro-forecast accuracy, method hit rate, or validation of a diffusion gate |
| [`B-WEBVAN`](../evidence/historical-calibration-2026-10-02.en.md#4-b-webvan-webvan-2000-financial-projection) | `CALIBRATION` | One reconstructable company-finance scale miss, showing that revenue direction cannot stand in for loss / cost structure | Falsification of a social-diffusion rule or overall commercial-forecast accuracy |
| [`T-SHUTTLE`](../evidence/historical-calibration-2026-10-02.en.md#5-t-shuttle-technology-candidate-with-an-open-outcome-pair) | `UNKNOWN/UNVERIFIED` | A technology investigation that preserves the forecast original while naming the missing same-window outcome and denominator | A definite “514 versus 38” miss, a technology-pair count, or any accuracy denominator |

Only two pairs can currently be reconstructed from the repository evidence packets: `P-04` (the FOMC forecast for 2008 real GDP) and `B-WEBVAN` (Webvan's 2000 revenue / net-loss projection). Both **must remain `CALIBRATION`**: the forecast originals and same-metric outcomes are locatable, which is enough for retrospective calibration, exposing recording gaps, and narrowing claims, but not for calculating method accuracy, a hit rate, or a Brier score.

`T-SHUTTLE` remains `UNKNOWN/UNVERIFIED`. The 1972 Space Shuttle plan's target of 514 flights in 1979–1990 is a lead for further investigation, but the same-window official mission list and a pre-specified denominator rule are not closed. It must therefore not be written as a definite “514 versus 38” miss, and it must not enter the technology-pair count or any accuracy denominator.

The upgrade boundaries between evidence classes are hard. `CALIBRATION` is material assembled after outcomes were known: it may expose counterexamples, revise rules, and narrow scope, but it cannot be upgraded to `CONTAMINATED_RELATIVE_HOLDOUT`. The latter requires advance freezing of an enumerable population, T-before material packets, strata and assignment, same-input baselines, scoring rules, and one-shot reveal; only then can it speak to relative discrimination under shared leakage, and the current material did not execute those steps. `GENUINE_FUTURE_OOS` requires registering and freezing the judgment text, information cutoff, outcome definition, and observation window before the outcome is observed, then revealing and reviewing it after the future window closes; reconstructing what would have been visible at T cannot substitute for it, and no current item belongs to this class.

Accordingly, the only method boundaries supported by this material are: macro records must separate the central scenario, tail risks, and data vintage; commercial records must separate revenue, losses, deployment pace, and mechanism assumptions; technology records must separate capability, planning / mission scenarios, financing thresholds, market estimates, and probabilistic forecasts. The material supports no new future judgment, opportunity candidate, or society-wide prediction. It also supports none of the claims that “the method is validated,” “five-gate accuracy improved,” “a gate has been falsified,” or “future forecasting ability has been proved.” The current count is **two reconstructable `CALIBRATION` pairs, zero qualified technology pairs, with `T-SHUTTLE` excluded from the denominator**; this is a narrowing of evidence classification and method boundaries, not an accuracy conclusion.

### 10.4 Current evidence status and isolated re-review status (2026-10-08)

To stop readers from confusing “the repository contains historical material” with “the method has been validated,” the current status must be explicit:

| Status | What the current material supports | What the current material does not support |
|---|---|---|
| `CALIBRATION` | Only `P-04` and `B-WEBVAN` have both a locatable forecast original and a same-metric outcome; they can be used for retrospective calibration, exposing recording gaps, and narrowing rule wording | Method accuracy, hit rate, Brier score, or the overall validity of the five gates |
| `UNKNOWN/UNVERIFIED` | `T-SHUTTLE` remains an investigation lead, with its missing same-window outcome and denominator stated explicitly | Writing “514 versus 38” as a definite miss, or putting it into the technology-pair count or any accuracy denominator |
| Relative testing under shared leakage | `CONTAMINATED_RELATIVE_HOLDOUT` exists only after the protocol's freeze, same-input baseline, role isolation, one-shot reveal, and `ΔD` calculation are all complete | Existing calibration, the protocol text, structure checks, or local self-reading cannot stand in for a relative discrimination increment, still less for genuine out-of-sample accuracy |
| `GENUINE_FUTURE_OOS` | Only a judgment frozen before its outcome, with its information cutoff, outcome definition, and observation window, then reviewed after the window closes, qualifies as genuine future out-of-sample calibration; no current item belongs to this class | Reconstructing what would have been visible at T cannot substitute for a genuine future out-of-sample record |

**The independent isolated re-review is not complete and has not started.** As of this section's date, the fresh-context reviewer service is unavailable, and no verifiable de-labelled, renumbered, deterministically shuffled bundle has been generated. We therefore cannot claim that the old judgments have been re-judged under the narrowed rules, and cannot treat the 2026-09-20 v1 review as a current-rule result; the required preconditions are specified in [Section 11.B of the Historical Pseudo-Out-of-Sample Validation Protocol](02-historical-validation-protocol.md#b-full-re-review-of-predictions-after-a-rule-change). This is not a forecast and not a judgment about whether the method succeeds: it is the fact that the validation work has not occurred.

Finally, mechanical checks and method evidence are separate. Passing `npm_check` (`npm run check`) means only that the files, links, and repository structure passed that check; passing `ship:structure-placeholder` means only that the release-structure placeholder is present. Neither implies forecast accuracy, method validity, genuine future out-of-sample performance, or completion of this project's mission.

---

## 11. Sources for the history cited here, and how strong each one is

Historical fact is the foundation of every argument here, so each item is tagged with its strength. **Nothing in the weak tier carries argumentative weight**: every conclusion in this document still holds once all weak-tier evidence is removed.

**Strong (primary sources or authoritative institutions)**

- Zoom daily meeting participants 10 million → 300 million: [Zoom's official blog](https://www.zoom.com/en/blog/reflecting-looking-ahead/)
- 4.3 billion people worldwide own a smartphone (2023): [GSMA](https://www.gsma.com/newsroom/press-release/smartphone-owners-are-now-the-global-majority-new-gsma-report-reveals/)
- The first ATM (1967-06-27, Enfield, London): [Barclays' own archive](https://home.barclays/news/2017/06/from-the-archives-the-atm-is-50/)
- New Coke withdrawn after 79 days: [The Coca-Cola Company, official](https://www.coca-colacompany.com/about-us/history/new-coke-the-most-memorable-marketing-blunder-ever)
- MOOC median completion rate 12.6%: [Jordan 2015, IRRODL (peer-reviewed)](https://www.irrodl.org/index.php/irrodl/article/view/2112)
- The health code ran as a mini-program and added no new app: [Social Media + Society, 2020 (peer-reviewed)](https://journals.sagepub.com/doi/pdf/10.1177/2056305120947657)
- Decollectivization accounts for about half of 1978–1984 agricultural output growth: [Lin 1992, AER 82(1): 34-51](https://econpapers.repec.org/RePEc:aea:aecrev:v:82:y:1992:i:1:p:34-51)
- The Metric Conversion Act of 1975 says "completely voluntary" in so many words: [Wikipedia (quoting the US Code)](https://en.wikipedia.org/wiki/Metric_Conversion_Act)
- **EXT-65**: Ai Hisano, *Cellophane, the New Visuality, and the Creation of Self-Service Food Retailing* (Harvard Business School Working Paper 17-106, May 2017, p. 7, citing *Meat Merchandising* 24(8), August 1948), **data: in 1948, 39% of independent grocers and 56% of chain grocers were on a complete self-service basis**; supports recurring picking labor reaching a majority within the frozen subgroup; **does not support** consumer-level `S`, a majority of independents, or a full diffusion time series from one annual point. <https://ideas.repec.org/p/hbs/wpaper/17-106.html>
- **Container handling cost**: Marc Levinson, *The Box* (Princeton University Press); supports 1956 traditional handling at $5.83/ton versus container handling at 15.8 cents/ton, an approximately 97% reduction.
- **EXT-55**: Clarence Saunders, US patent [US1242872A, *Self-Serving Store*](https://patents.google.com/patent/US1242872A/en), filed 1916-10-21 and granted 1917-10-09. The text explicitly makes customers select goods themselves, traverse a continuous path, and settle at the exit, while claiming fewer clerks and lower overhead. It strongly supports the transfer-of-recurring-labor mechanism; the inventor's sales claims do not carry diffusion-scale proof.
- **EXT-66**: NHTSA, [*Seat Belt Use in 1994: Use Rates in the United States*](https://www.nhtsa.gov/behavioral-safety-research/seat-belts/seat-belt-use-1994-use-rates-united-states); the first nationally representative NOPUS daytime observation recorded 58% use among front-seat outboard occupants in 1994. It supports coding the seat-belt case as `D`, not `S` without an absolute count, and does not support law-only causality.
- **EXT-67**: [Commercial forecast-miss evidence packet](../evidence/business-forecast-calibration-2026-09.en.md); Webvan and eToys SEC forecast / outcome originals, plus the Iridium financing-covenant threshold appendix, with verbatim excerpts and SHA-256 hashes in the packet; supports numerical calibration of revenue, loss, and subscriber thresholds, not five-gate accuracy or single-mechanism causality.
- **EXT-56**: US NHTSA, [*Seat Belt Use in 2024—Overall Results*](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813799); 2024 national observed use was 91.2% among daytime front-seat outboard occupants. It supports high adoption under law and enforcement, not generalization to all occupants / hours or law-only causality.
- **EXT-57**: Google, [*A message on Stadia and our long term streaming strategy*](https://blog.google/products-and-platforms/products/stadia/message-on-stadia-streaming-strategy/), 2022-09-29. Google called the technology foundation proven at scale and strong, said user traction missed expectations, and announced shutdown on 2023-01-18. It supports “technical usability does not guarantee adoption,” not any invented specific failure cause.
- **EXT-58**: Congressional Research Service, [*Daylight Saving Time: Background and Legislation*](https://www.congress.gov/crs-product/R45208). Emergency year-round DST began 1974-01-06, was rolled back early, and standard time returned 1974-10-27. It supports the withdrawal chronology, not a single causal account of public opposition.
- **EXT-59**: Reserve Bank of India, [Annual Report 2017–18, Chapter V](https://www.rbi.org.in/scripts/AnnualReportPublications.aspx?Id=1232). It confirms that the 2016 withdrawal of specified banknotes created surplus banking-system liquidity. That page does not report the exact return share, so this round does not code demonetization as a success or failure from it.

**Medium (encyclopedias / authoritative media / multiple consistent sources)**

- Picturephone commercial details, monthly rent, and peak set counts: [ETHW](https://ethw.org/Picturephone), [Wikipedia](https://en.wikipedia.org/wiki/Picturephone)
- Iridium bankruptcy figures and break-even subscriber count: [Wikipedia](https://en.wikipedia.org/wiki/Iridium_Communications), [Forbes 2001](https://www.forbes.com/2001/11/30/1130tentech.html)
- Concorde's years in service and number built: [Wikipedia](https://en.wikipedia.org/wiki/Concorde)
- Google Glass pricing and the end of consumer sales in January 2015: [Wikipedia](https://en.wikipedia.org/wiki/Google_Glass), [BBC](https://www.bbc.com/news/technology-30831128)
- ESPN 3D start and end dates and the official reason for closing: [Wikipedia](https://en.wikipedia.org/wiki/ESPN_3D)
- San Jose State / Udacity pilot pass rates and suspension: [LA Times](https://www.latimes.com/local/lanow/la-me-ln-san-jose-online-20130718-story.html)
- Prohibition agent count, speakeasy count, and repeal date: [Wikipedia](https://en.wikipedia.org/wiki/Prohibition_in_the_United_States)
- Better Place funding, bankruptcy, and sales: [Wikipedia](https://en.wikipedia.org/wiki/Better_Place_(company))
- Timeline of the household responsibility system: [Wikipedia](https://en.wikipedia.org/wiki/Household_responsibility_system)
- American household television ownership (1% in 1948, 75% in 1955): [Wikipedia](https://en.wikipedia.org/wiki/Television_in_the_United_States); different yearbooks vary slightly in what they count
- Sea-Land's Vietnam shipping volume and Department of Defense revenue, and CONEX as a separate system: [Wikipedia](https://en.wikipedia.org/wiki/Sea-Land_Service), [GlobalSecurity](https://www.globalsecurity.org/military/systems/ship/container-mil.htm)
- Estimates of fluent Esperanto speakers (63,000 to two million, heavily disputed): [Wikipedia](https://en.wikipedia.org/wiki/Esperanto)

**Weak (second-hand, leaked, or disputed figures—this document does not let them carry the argument)**

- AT&T's "more than $500 million" spent on the Picturephone: only second-hand retellings; the body of this document does not use that figure
- Dean Kamen's "ten thousand a week" forecast: widely retold but the primary source is doubtful; the body of this document does not use that figure
- Segway cumulative sales of about 140,000 units, the peak shipment share of 3D televisions, cumulative Meta Quest sales: sourced from aggregator sites or leaked reports; the body of this document does not use these figures
- China's 2019 mobile-payment consumption exceeding US$6.5 trillion: an industry-media figure whose different statistical definitions diverge widely; the body has been rewritten to "runs into the trillions of dollars" and states explicitly that the conclusion there does not rest on the number
- Retail hydrogen above $30 per kilogram (California): industry and media reporting; no first-hand price series was obtained here. It is used only to indicate the direction of the hydrogen car's cost, and that direction is precisely the attack point section 5 names as able to overturn Gate 3's exclusivity
- "QR-code merchant costs are far below NFC terminal costs": at present only a qualitative consensus in industry media, with no strong quantitative literature found; [BIS Working Paper 1011](https://www.bis.org/publications/working-paper-1011-big-techs-qr-code-payments-and-financial-inclusion.pdf) supports the mechanism that "QR codes let merchants without POS terminals get connected," but provides no cost-comparison figures

## 12. Feasibility audit and freeze decision for historical candidate registries (2026-09-25)

### 12.1 What this audit examined

This is a **pre-freeze audit**, not a historical backtest and not a holdout result. The object of review is the set of registries permitted by the protocol: registries that existed at `T`, permit enumeration of a population, and do not select entries by later success or failure. During the audit, only the locations of `reveal_source` were registered; outcome contents were not opened. Nothing below may therefore be described as a success, failure, diffusion, or withdrawal sample.

The execution date for this round is 2026-09-25. The protocol's uniform technology window `T+15` therefore requires `T ≤ 2011-09-25`; politics/public policy and business use `T+10`, requiring `T ≤ 2016-09-25` (the final manifest must calculate this from exact dates). These are protocol constraints and are not relaxed because a candidate is famous or easy to verify.

### 12.2 Registry-level audit

| Domain | Enumerable registry and version anchor | Coverage and inclusion rule | Pre-registered reveal location | Current verdict |
|---|---|---|---|---|
| Technology | USPTO Patent Public Search / Official Gazette; WIPO PATENTSCOPE; arXiv categories and first `v1`; ClinicalTrials.gov historical registrations (mainly post-2007) | Use application-publication date, WO international-publication date, first public `v1` date, or first public registration date as `T`; retain ungranted, withdrawn, low-attention, and unknown-status entries | Patent Center / PATENTSCOPE dossier / later paper and productization records / ClinicalTrials.gov archive | **Registry feasible, not currently freezable**; post-2012 entries cannot enter this technology batch |
| Politics / public policy | Congress.gov / GovTrack / GovInfo bill sets; Federal Register Proposed Rules; World Bank Projects & Operations | Use formal bill number, publication date, or project approval date as `T`; do not use successful bills, final rules, or completed-project lists as the population | Bill history; later Federal Register records; World Bank project documents | **Registry feasible, not currently freezable**; Congress.gov and GovTrack are mainly two database views of the same bill population, not two independent institutional sources |
| Business | SEC EDGAR S-1/F-1 filing index; Kickstarter launch-time Wayback snapshots; historical complete YC batch rosters | Use initial filing, first launch, or batch-publication date as `T`; retain withdrawn, dormant, and low-attention entries; do not reconstruct the population from today's survivors | Later EDGAR filings; crowdfunding snapshots and delivery archives; batch archives and company-status records | **Registry feasible, not currently freezable**; current examples are too concentrated in famous cases and the ordinary-case fraction is unknown |

The live checks also exposed the execution boundary: the arXiv archive showed current and historical categories but not per-entry `v1` dates; the SEC full-index entry returned 403; the Federal Register entry redirected to a blocked page; and the World Bank project entry was dynamic and did not return reproducible content. These facts show that a registry entrance exists, not that T-before bytes have been obtained for hashing. They are not outcome evidence, and current web pages may not substitute for historical snapshots.

### 12.3 Case-level inventory (locations registered; outcomes unread)

The three independent audit legs supplied the 48 preliminary positions below. `NOT_GENERATED` is the honest state: without a frozen, canonical `as_of_packet`, there is no protocol-level hash. `Pending verification` is not a valid case and may not enter the manifest, random assignment, or gate judging.

#### Technology (16 preliminary positions)

| Candidate / registry entry | T | Window deadline | T-before `as_of_packet` anchor | `packet_hash` | `reveal_source` (location only) | `candidate_activity` | `target_population` | `split_stratum` | Audit verdict |
|---|---|---|---|---|---|---|---|---|---|
| T-01 USPTO US20100137140A1 | 2010-06-03, bibliography pending | 2025-06-03 | USPTO publication / bibliographic record | NOT_GENERATED: file set not frozen | Corresponding Patent Center file | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-02 USPTO US20070282930A1 | 2007-11-29, pending | 2022-11-29 | USPTO Gazette / application text | NOT_GENERATED: file set not frozen | Corresponding Patent Center file | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-03 USPTO 2009 publication search slot | Undetermined | Undetermined | Pre-frozen keyword search result | NOT_GENERATED: no final entry | Patent Center file | Not a case; redraw from registry | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-04 USPTO 2010 publication search slot | Undetermined | Undetermined | Pre-frozen keyword search result | NOT_GENERATED: no final entry | Patent Center file | Not a case; redraw from registry | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-05 WIPO WO 2008–2010 search slot | Undetermined | Undetermined | PATENTSCOPE bibliography / publication PDF | NOT_GENERATED: no publication number | PATENTSCOPE dossier | Not a case; redraw from registry | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-06 WIPO WO 2009–2011 search slot | Undetermined | Undetermined | PATENTSCOPE bibliography / publication text | NOT_GENERATED: no publication number | PATENTSCOPE dossier | Not a case; redraw from registry | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-07 arXiv:1001.4538 v1 | 2010, page check pending | Corresponding date in 2025 | arXiv abs v1 / v1 PDF | NOT_GENERATED: bytes not saved | Later versions / citation / adoption locations | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-08 arXiv:1003.0145 candidate | 2010, ID/title pending | Corresponding date in 2025 | arXiv abs v1 / v1 PDF | NOT_GENERATED: identity pending | Later versions and adoption locations | Not frozen | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-09 arXiv cs.RO/eess.SY date slot | Undetermined | Undetermined | Category date list and v1 PDF | NOT_GENERATED: no ID | Later versions / deployment record | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-10 arXiv cs.CL 2011 date slot | Undetermined | Undetermined | Category archive and v1 PDF | NOT_GENERATED: no ID | Later papers / software adoption | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-11 arXiv cs.DC/cs.OS 2011 date slot | Undetermined | Undetermined | Category archive and v1 PDF | NOT_GENERATED: no ID | Later deployment / software record | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-12 ClinicalTrials.gov NCT00433511 | 2007-03-07, archive check pending | 2022-03-07 | Earliest archived registration | NOT_GENERATED: historical version not saved | ClinicalTrials.gov archive | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-13 ClinicalTrials.gov NCT005xxxxx slot | Undetermined | Undetermined | Initial archived record | NOT_GENERATED: no NCT ID | Archive history | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-14 ClinicalTrials.gov NCT006xxxxx slot | Undetermined | Undetermined | Initial archived record | NOT_GENERATED: no NCT ID | Archive history | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-15 ClinicalTrials.gov NCT008xxxxx slot | Undetermined | Undetermined | Initial archived record | NOT_GENERATED: no NCT ID | Archive history | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| T-16 ClinicalTrials.gov NCT010xxxxx slot | Undetermined | Undetermined | Initial archived record | NOT_GENERATED: no NCT ID | Archive history | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |

Only T-01, T-02, T-07, and T-12 have concrete identifiers that can be checked further; the rest are slots for mechanical extraction from a frozen population, not 12 additional valid cases. Even after completion, technology must be rechecked for 2000s / 2010–2011 even strata, at least one-third ordinary cases, and an equal unread reserve.

#### Politics / public policy (16 preliminary positions)

| Candidate / registry entry | T | Window deadline | T-before `as_of_packet` anchor | `packet_hash` | `reveal_source` (location only) | `candidate_activity` | `target_population` | `split_stratum` | Audit verdict |
|---|---|---|---|---|---|---|---|---|---|
| P-01 H.R.2454, 111th | 2009-05-15, pending | 2019-05-15 | GovInfo initial BILLS package | NOT_GENERATED | Congress.gov history | Pending; likely high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-02 H.R.1, 111th | 2009-01-26, pending | 2019-01-26 | Congress.gov initial text | NOT_GENERATED | Bill history | Pending; likely high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-03 H.R.4173, 111th | 2009-12-02, pending | 2019-12-02 | Congress.gov initial text | NOT_GENERATED | Bill history | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-04 H.R.4872, 111th | 2010-03-17, pending | 2020-03-17 | Congress.gov initial text | NOT_GENERATED | Bill history | Pending; likely high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-05 S.744, 113th | 2013-06-27, pending | 2023-06-27 | Congress.gov initial record | NOT_GENERATED | Bill history | Pending; likely high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-06 H.R.2, 114th | 2015-01-06, pending | 2025-01-06 | Congress.gov initial text | NOT_GENERATED | Bill history | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-07 FR 2010-32061 | 2010-12-28, archive pending | 2020-12-28 | 75 FR 81722 original PDF | NOT_GENERATED | Later Federal Register archive | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-08 EPA proposed-rule search slot | 2011-07-07 direction, number pending | Undetermined | Original Federal Register publication | NOT_GENERATED: no document number | Federal Register archive | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-09 USDA proposed-rule search slot | 2012-01-26 direction, number pending | Undetermined | Original Federal Register publication | NOT_GENERATED: no document number | Federal Register archive | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-10 CMS proposed-rule search slot | 2013-07-19 direction, number pending | Undetermined | Original Federal Register publication | NOT_GENERATED: no document number | Federal Register archive | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-11 FCC proposed-rule search slot | 2014-05-15 direction, number pending | Undetermined | Original Federal Register publication | NOT_GENERATED: no document number | Federal Register archive | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-12 World Bank P113771 | 2010-06-30, approval pending | 2020-06-30 | Project detail / T-before project files | NOT_GENERATED: version not saved | Project documents | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-13 World Bank P121821 | 2010-09-30, approval pending | 2020-09-30 | Project detail / T-before project files | NOT_GENERATED: version not saved | Project documents | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-14 World Bank P123322 | 2011-06-21, approval pending | 2021-06-21 | Project detail / T-before project files | NOT_GENERATED: version not saved | Project documents | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-15 World Bank P133438 | 2012-11-01, approval pending | 2022-11-01 | Project detail / T-before project files | NOT_GENERATED: version not saved | Project documents | Pending | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| P-16 World Bank project-list slot | 2013 direction, project ID pending | Undetermined | Projects & Operations list | NOT_GENERATED: no project ID | Specific documents URL pending | Not a case; redraw | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |

The politics table has two structural problems: the 2000s currently has only three directional positions, not at least four and even; and P-08–P-11 and P-16 have no final identities. Congress.gov and GovTrack cannot be counted as two independent institutional registries merely because their pages differ; frozen Federal Register and World Bank bytes are needed for heterogeneity.

#### Business (16 preliminary positions)

| Candidate / registry entry | T | Window deadline | T-before `as_of_packet` anchor | `packet_hash` | `reveal_source` (location only) | `candidate_activity` | `target_population` | `split_stratum` | Audit verdict |
|---|---|---|---|---|---|---|---|---|---|
| B-01 SEC Tesla S-1 | 2010-01-29, filing check pending | 2020-01-29 | Initial EDGAR S-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-02 SEC LinkedIn S-1 | 2011-04-29, pending | 2021-04-29 | Initial EDGAR S-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-03 SEC Groupon S-1 | 2011-06-02, pending | 2021-06-02 | Initial EDGAR S-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-04 SEC Zynga S-1 | 2011-07-01, pending | 2021-07-01 | Initial EDGAR S-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-05 SEC Facebook S-1 | 2012-05-03, pending | 2022-05-03 | Initial EDGAR S-1 directory | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-06 SEC Twitter S-1 | 2013-10-03, pending | 2023-10-03 | Initial EDGAR S-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-07 SEC Alibaba F-1 | 2014-05-01, pending | 2024-05-01 | Initial EDGAR F-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-08 SEC Shopify F-1 | 2015-02-12, pending | 2025-02-12 | Initial EDGAR F-1 | NOT_GENERATED | Later EDGAR filing | Pending; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-09 Kickstarter Pebble snapshot | Month-level direction (exact day missing) | Not computable: exact T required | First-launch Wayback snapshot | NOT_GENERATED | Historical page / delivery archive | Directional position only, not a qualified case; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-10 Kickstarter Oculus Rift snapshot | Month-level direction (exact day missing) | Not computable: exact T required | First-launch Wayback snapshot | NOT_GENERATED | Historical page / delivery archive | Directional position only, not a qualified case; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-11 Kickstarter Coolest Cooler snapshot | Month-level direction (exact day missing) | Not computable: exact T required | First-launch Wayback snapshot | NOT_GENERATED | Historical page / delivery archive | Directional position only, not a qualified case; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-12 Kickstarter Exploding Kittens snapshot | Month-level direction (exact day missing) | Not computable: exact T required | First-launch Wayback snapshot | NOT_GENERATED | Historical page / delivery archive | Directional position only, not a qualified case; high attention | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-13 YC Winter 2011 roster | Year-level direction (exact day missing) | Not computable: exact T required | Complete batch-list snapshot | NOT_GENERATED | YC batch / company archive | Directional position only, not a qualified case; completeness unproven | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-14 YC Winter 2012 roster | Year-level direction (exact day missing) | Not computable: exact T required | Complete batch-list snapshot | NOT_GENERATED | YC batch / company archive | Directional position only, not a qualified case; completeness unproven | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-15 YC Winter 2013 roster | Year-level direction (exact day missing) | Not computable: exact T required | Complete batch-list snapshot | NOT_GENERATED | YC batch / company archive | Directional position only, not a qualified case; completeness unproven | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |
| B-16 YC Winter 2014 roster | Year-level direction (exact day missing) | Not computable: exact T required | Complete batch-list snapshot | NOT_GENERATED | YC batch / company archive | Directional position only, not a qualified case; completeness unproven | NOT_RECORDED | NOT_RECORDED | NOT_ASSIGNED |

This is not 16 valid business cases: it is eight famous S-1/F-1 examples, four famous crowdfunding examples, and four batch slots whose completeness has not been proved. It does not establish one-third ordinary cases or a 2000s stratum.

### 12.4 Quotas, gaps, and classification

| Check | Current audit result | Classification | Fixable by expanding registries? |
|---|---|---|---|
| At least two heterogeneous registries per domain | Directional sources exist in all three domains; Congress/GovTrack are mirrors of one bill population | Evidence currently insufficient | Yes: freeze Federal Register / World Bank, EDGAR / Wayback, and technology patent / paper or registration populations |
| At least 12 cases per domain | Each table has 16 “positions”, but many are slots or unverified entries | Evidence currently insufficient | In principle yes: mechanically sample from frozen populations; do not fill with famous cases |
| At least 48 cases overall | No 48 qualified cases exist yet | Evidence currently insufficient | In principle yes, after each domain passes its own floor |
| At least 4 and even in each domain × decade stratum | Technology excludes post-2012 entries under T+15; politics has only 3 initial 2000s positions; business lacks a 2000s stratum | Fixable by expansion, not met here | Yes, under the same registry rules; moving cases across decades is not a fix |
| At least one-third ordinary cases | Current examples are strongly famous; ordinary fraction is UNKNOWN | Evidence currently insufficient | Yes: define a T-time attention rule in advance and sample from complete populations |
| Equal unread reserve per domain | No unread, unprepared reserve manifest exists | Evidence currently insufficient | Yes: freeze and isolate a reserve; read candidates may not become reserve |
| T-before packet and hash for every case | No protocol-level packet hash can be generated in this audit | Evidence currently insufficient | Yes: save historical bytes, canonicalize ordering, and hash before reveal |
| Can current pages substitute for historical archives? | No; dynamic pages, 403, redirects, and current status do not prove T-time visibility | **Structurally unexecutable within the stated scope** | Only official archives / saved bytes can change this; changing the protocol cannot |
| Submit a holdout manifest now | Identity, strata, ordinary fraction, packet hashes, and reserve conditions are unmet | **Stop this batch** | Build a new pool first; do not patch or re-split a failed batch |

“Structurally unexecutable within the stated scope” applies only to the current approach without frozen historical bytes, exact entry identities, and role isolation. It does not mean the official registries can never be used, and it does not permit lowering the protocol floor.

### 12.5 Freeze decision and next step

**Freeze decision: do not submit a new manifest, generate a split salt, run random assignment, run the five gates or baselines, or reveal outcomes in this round.** The reason is that none of the 48 positions has been shown to satisfy exact identity, uniform observation window, T-before packet, reproducible hash, even decade strata, ordinary-case proportion, and an equal unread reserve simultaneously. Submitting a file that merely appears to have 48 rows would disguise candidate inventory as a holdout, which the protocol forbids.

This is not a finding that the historical method failed; it is a finding that candidate-pool evidence has not reached the freeze bar. The expandable repair path is:

1. Freeze at least two genuinely heterogeneous registries per domain, including version, coverage, query, archive location, and exclusion rules;
2. Mechanically sample from each complete population and fill `case_id`, registry entry, exact `T`, `candidate_activity`, `target_population`, `outcome_window`, and `split_stratum`;
3. Save canonical packets containing only T-before materials, with each file's date / archive anchor, fixed order, and SHA-256;
4. Register each `reveal_source` for opening only at the end, without reading it;
5. Check domain quotas, ordinary cases, and unread reserve before an independent allocator generates the one-shot salt;
6. Continue accumulating the existing future due-date cards; only due future cards provide genuine out-of-sample records independent of a frozen historical registry.

This audit cannot prove a relative discrimination increment for the five gates. That metric may be reported only after freeze, role isolation, same-input baselines, outcome reveal, and `ΔD` computation. This section contains no `PASS`, `VETO`, `S`, `D`, or `ΔD` result.

**[Self-imposed constraints — removable]** This section carries forward the protocol's 12/48 floors, even strata, one-third ordinary cases, equal reserve, T+15/T+10 windows, `packet_hash`, and independent-role requirements. These exact thresholds are not verbatim in the user's founding ask; they are constraints this project imposed to prevent survivorship bias, hindsight, and pseudo-holdout claims. If any is removed later, the evolution log must state why and whether this audit remains comparable.
