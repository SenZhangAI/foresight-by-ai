# Calibrating social-regularity candidates against history (2026-10-10): constituency lock-in admitted in veto form; preference-falsification cascades not admitted because they cannot say no

[中文版](social-regularity-calibration-2026-10-10.md) · [Methodology §2](../en/00-method.md#2-toolbox-of-lenses) · [Retrospect](../en/01-retrospect.md)

> **Status boundary (read this first):** every case on this page was selected **after its outcome was known** and is `CALIBRATION`. The candidate texts were written before the case-by-case verification, but the author already knew roughly how these cases ended, so this is **not** a blind test and not a holdout. It can show only whether a rule can be calibrated on known history and where it fails; it provides no predictive power, hit rate, or accuracy. All primary sources were fetched on UTC 2026-10-09. None of them is stored in this repository; reproducibility rests on the URLs, page locators, and SHA-256 values below.

## 1. Why this round

The “social regularities” row of the [methodology mapping table](../en/00-method.md#mapping-the-five-starting-points-to-l1l9) admits that this is “least deserved” of the five starting points: the social clause states exactly one mechanism, signal forgery, and political and business history had entered calibration only as **forecast-miss cases**, never as regularities that could be carried forward. Under the principle that “a new reasoning rule must first be calibrated on historical cases, and must be able to say no”, this round put forward two candidates from political history. Each needed at least 2 success cases and 2 failure controls, and had to return “no” on at least one real case.

## 2. Candidate A · Constituency lock-in

### 2.1 The frozen text (strong form) and where it broke

**Strong form as frozen:** if a public arrangement pays a recurring, visible benefit to a concentrated, identifiable group while its cost is spread over a larger population, then after at least one full benefit cycle attempts at outright repeal will fail; reform will happen only by grandfathering (new rules for newcomers) or by cutting the cost side while keeping the benefit. Conversely, if the beneficiaries are themselves the payers, or there is no group drawing a recurring benefit at all, there is no lock-in and the arrangement can be repealed outright when a political window opens.

**The positive half of the strong form is refuted directly by AFDC (1996)** (X1 in 2.3). What enters the toolbox is therefore the **veto form**:

> **L10 · Constituency lock-in (veto form):** if a public arrangement has no group that has already drawn its benefit on a recurring basis, is identifiable, and does not bear the arrangement's visible cost, it has no protection from beneficiaries when a political window opens, and outright repeal is within reach; the existence of such a group shows only that outright repeal will meet defenders, not that the arrangement will survive.

This mirrors the structure of the [five diffusion gates](../en/01-retrospect.md#6-the-sufficiency-counterexample-all-five-gates-passed-withdrawn-79-days-later): a veto-style necessary condition, not a sufficient-condition predictor. AFDC plays the role New Coke plays there.

### 2.2 Two decision variables (visible at time T)

- **(i)** Is there an identifiable group that has already drawn this arrangement's benefit on a recurring basis?
- **(ii)** Does that group **not** bear the arrangement's visible cost?

Both yes → the rule says “it has defenders” (a pass only; no survival prediction). Either no → the rule says **no**: there is no protection from beneficiaries.

### 2.3 Case matrix

| ID | Case (domain) | Time T | (i) / (ii) | Rule's verdict | Outcome | Consistent? |
|---|---|---|---|---|---|---|
| S1 | US Social Security personal-accounts proposal (politics) | 2005-02-02 State of the Union | Yes: retirees paid monthly since the 1935 creation / Yes: cost borne mainly through workers' payroll tax | Has defenders | Of the 10 reform bills in the 109th Congress, “None received congressional action”; the proposal itself told those 55 and older the system “will not change in any way” | Consistent (the strong form is consistent too) |
| S2 | Repeal of the US Affordable Care Act (politics) | 2017-07-28 Senate vote | Yes: enacted 2010, exchange benefits from 2014 / Yes: the individual-mandate penalty fell on the uninsured | Has defenders | SA 667 failed 49–51; later that year TCJA §11081 set the penalty to $0 and kept the benefits | Consistent (only the cost borne by non-beneficiaries was cut) |
| F1 | US Medicare Catastrophic Coverage Act (politics) | Signed 1988-07-01 → repealed 1989 | Partly / **No**: beneficiaries paid a supplemental premium themselves | **No** | Repealed outright 1989-12-13 (P.L. 101-234); the House rejected, 55–346, the Senate version that “sought to avoid a complete repeal” | Consistent |
| F2 | US national 55 mph speed limit (politics / institutions) | Enacted 1974-01-02 | **No**: the benefit was diffuse fuel saving and safety, with no group drawing it on a recurring basis / the cost was every driver's time on every trip | **No** | Relaxed to 65 in 1987 over a presidential veto; repealed outright 1995-11-28 | Consistent (but the rule says nothing about timing: 13 years passed before the relaxation) |
| X1 | US AFDC cash welfare (politics) | 1996 reform | Yes: caseload had “more than tripled since 1965” / Yes: borne by taxpayers | Has defenders (strong form predicted: outright repeal fails, or grandfathering only) | 1996-08-22: individual entitlement abolished and replaced by TANF block grants, with no grandfathering | **Strong form refuted**; under the veto form it is a sufficiency counterexample |
| — | UK poll tax (politics) | Introduced in England 1990 → replaced 1993 | Uncertain: moving from property-based rates to a flat per-head charge necessarily left some people paying less than before, and whether they form a group under (i) cannot be decided from the material obtained | Not judged | Replaced by council tax on 1993-04-01 | **Not counted**: `UNKNOWN/UNVERIFIED` (the primary source for the 1991 abolition announcement was not obtained either) |

**Cases judged “no”, and why:** F1 — the beneficiaries were the payers, (ii) is no, and the rule says “no protection from beneficiaries”; the outcome was outright repeal within 17 months. F2 — there was no group drawing a recurring benefit at all, (i) is no, and the rule returns the same “no”; the outcome was relaxation followed by outright repeal.

**F1's confound must be stated:** part of the Act's benefits may not have run a full cycle before repeal, so this case cannot be credited to the “beneficiaries pay” clause on its own. Both readings point to “no”; the rule got it right, but the credit cannot be given to one clause alone.

### 2.4 Conclusion and confidence

The veto form meets the admission bar: 2 passed-and-survived (S1, S2), 2 judged-no-and-repealed (F1, F2), and 1 sufficiency counterexample (X1). The positive half (“lock-in means survival / grandfathering only”) is **refuted and must not be used as a prediction**. Confidence: medium-low — all 5 cases are post-1970 US cases, and all are calibration material with known outcomes.

**How to overturn it:** find a public arrangement for which (i) or (ii) is no, yet which survived a genuine repeal window. A single such case breaks the veto form of L10, and it must then be deleted or narrowed.

### 2.5 External comparison (agreement / divergence / why we still hold it)

- **Agreement (this agrees with consensus; it is not presented as an independent discovery):** the asymmetry of concentrated benefits and diffuse costs comes from Mancur Olson's 1965 *The Logic of Collective Action*; the “client politics” type in James Q. Wilson (ed.), *The Politics of Regulation* (Basic Books, 1980); and Paul Pierson, *Dismantling the Welfare State? Reagan, Thatcher and the Politics of Retrenchment* (Cambridge University Press, 1994), on welfare programmes creating their own supporters and retrenchment advancing through obfuscation and grandfathering. Page numbers in these two books were not re-checked in this round.
- **Divergence:** the popular version often treats “once an entitlement exists it is irreversible” as a prediction. AFDC shows that this positive claim already failed within this round's calibration; this page keeps only the half that can say no.
- **Why we still hold it:** the increment is not a novel mechanism but writing it as two variables checkable at time T, keeping only the veto direction, and stating what would overturn it.

## 3. Candidate B · Preference-falsification cascades: not admitted (cannot say no)

**Frozen text:** when expressing dissent in public is costly, visible public support overstates private support; stability forecasts extrapolated from public compliance will therefore miss sudden collapse, and the collapse comes as a cascade once a visible minority starts to speak.

| Case | Does the rule apply? | Outcome | What it means for the rule |
|---|---|---|---|
| East Germany 1989 | Yes: dissent was costly; mass public expression in Leipzig on 1989-10-09 | Borders opened 1989-11-09 | Consistent |
| Iran 1978 | Yes: public compliance; intelligence judged stability on the premise of coercive power | The Shah left in 1979-01 | Consistent (see M2 in section 4) |
| China 1989 | Yes: both the precondition and a visible dissenting minority were present | No cascade | **The rule says “cascade” and is wrong** |
| North Korea, mid-1990s famine | Precondition extremely strong, but the trigger (a visible minority) never appeared | No collapse | No discriminating power |
| Poland, 1989-06-04 election | Precondition removed (secret ballot, low cost of expression) | Solidarity won overwhelmingly | Consistent, but not a test of saying no |

**Why it cannot say no:** what actually separates China from East Germany is “whether the army fired” and “whether the outside patron state held back.” Kuran himself writes that before the revolution “it was not at all clear that the Soviet Union would sit back” (Kuran 1991, p.36), and the 1988 US intelligence estimate expected exactly the opposite, that the Soviets would intervene (M1 in section 4). Those two variables belong to a coercion / political-opportunity mechanism, not to this rule. Saying instead that “the threshold was not reached” uses a threshold that cannot itself be observed (Kuran 1991, p.43), and such a rescue cannot be falsified. The public–private gap can also persist for a long time without triggering collapse: surveys of East European emigrants in the 1970s and 1980s gave the Communist Party “at most a tenth of the vote” (Kuran 1991, p.31), and no collapse followed for about twenty years. So **this rule can explain only after the fact and cannot say “no” beforehand**, and under the principle it does not enter the toolbox. The one testable remnant — “stability forecasts based on public compliance systematically overstate stability” — would need a counting test, and M1's own estimate did warn of upheaval, which shows that even this bias is not clean.

## 4. Forecast-miss cases newly found in this round (4, none upgraded into the qualified count)

None of these 4 cases **changes** the qualified pair count in [Retrospect §10.2](../en/01-retrospect.md#102-three-domain-total-the-current-evidence-does-not-meet-the-12-case-threshold) (still 6/12): each either lacks an observation window stated in the text, or has an unclosed primary source or outcome side, or is not a forecast set against an outcome.

### M1 · The 1988 US National Intelligence Estimate: “The Berlin Wall will stay”

- **Forecast:** NIE 11/12-9-88, *Soviet Policy Toward Eastern Europe Under Gorbachev*, approved 1988-05-26; reproduced in CIA CSI, *At Cold War's End* (1999), Document 8. Paragraph 32: “(The Berlin Wall will stay, whatever tactical advantages Gorbachev might see in its removal.)”; elsewhere: “In extremis, however, there is no reason to doubt his willingness to intervene to preserve party rule and decisive Soviet influence in the region.”
- **What the same estimate got right:** “popular upheaval is the most likely contingency” — it warned of upheaval; what it did not foresee was the scale, East Germany, and the Wall.
- **Outcome:** President Bush, 1989-11-09: “I welcome the decision by the East German leadership to open the borders to those wishing to emigrate or travel.”
- **Class:** a directional miss; the text states no observation window and the primary source is not stored in the repository → not upgraded into the qualified `CALIBRATION` count.

### M2 · The 1978 US Defense Intelligence Agency: “in power over the next ten years”

- **Forecast:** the DIA “prognosis” of 1978-09-28, quoted on p.6 of the House Intelligence Committee staff report *Iran: Evaluation of U.S. Intelligence Performance Prior to November 1978* (January 1979): the Shah “is expected to remain actively in power over the next ten years.” The same page records the opposite conclusion of a March 1978 State Department INR seminar: “time is not on the side of the Shah.”
- **Outcome:** President Carter's news conference, 1979-01-17: “As you know, the Shah has left Iran; he says for a vacation.”
- **Class:** `UNKNOWN/UNVERIFIED` — the DIA original was not obtained (only the congressional report's quotation), and the outcome text obtained proves departure, which is not the same as “losing power.”

### M3 · The 1988 Congressional Budget Office cost estimate for the catastrophic drug benefit doubled within a year

- **Material:** CBO, *Updated Estimates of Medicare's Catastrophic Drug Insurance Program* (October 1989), chapter II, p.24: the June 1988 estimate put 1990–1993 outlays at $5.7 billion; the July 1989 re-estimate raised this to “a total of $11.8 billion for the 1990-1993 period.”
- **Class:** `UNKNOWN/UNVERIFIED` — this is an estimate against a re-estimate, not a forecast against an outcome; the benefit was repealed before it was ever paid. The 1988 original was not obtained (cbo.gov refused access); only the 1989 report's restatement is available.

### M4 · The 1990 UK poll tax: actual average charge above the government's figure

- **Material:** House of Commons debate, 1990-04-03 (HC Deb vol 170), c1033, Patten: “The average charge is £363 in England”; c1036, Gould: bills “on average, £85 above Government estimates.”
- **Class:** `UNKNOWN/UNVERIFIED` — the government's own figure (January 1990) was not obtained from a primary source, and it was a normative figure computed from standard spending, so strictly it is not a forecast.

### Three statements not counted (not forecasts)

- Carter's toast in Tehran, 1977-12-31, calling Iran “an island of stability”: present-tense diplomatic praise with no time horizon.
- The foreword of CIA's August 1978 *Iran After the Shah* said Iran was “not in a revolutionary or even a 'prerevolutionary' situation”: that assessment describes itself as “not an assessment of what will happen” (HPSCI report pp.6–7), so it is a framing characterisation.
- Bush, 1989-06-05: “the forces of democracy are going to overcome these unfortunate events in Tiananmen Square” — rhetoric, not a testable forecast.

## 5. What this page does not support

- It does not support “L10 has been validated,” “the method's accuracy improved,” or any holdout / out-of-sample conclusion;
- it does not support using the positive half of L10 as a survival prediction;
- it changes no judgment card's conclusion or status, and does not claim that any card has been re-reviewed with L10;
- it does not change the 6/12 qualified pair count of §10.2.

## 6. Sources and fetch record (UTC 2026-10-09)

| Use | Source and locator | HTTP / bytes | SHA-256 |
|---|---|---|---|
| S1 | Bush 2005 State of the Union <https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-14> | 200 / 93731 | `426049006eee010de8b4259508362ef88d213eca232f307433ebe7e8fdf95490` |
| S1 | CRS RL33544 (updated 2007-04-25), Summary <https://www.everycrsreport.com/files/20070425_RL33544_b869fb4b80374de65d8b7cecc5188b4a0330ed66.html> | 200 / 157158 | `da528b2eba2b0faf121a8a99c64c592094b6af2969803add63b79394cd6b3b7c` |
| S1 | CRS RL32879 <https://www.everycrsreport.com/reports/RL32879.html>: “individuals born prior to 1950 would have experienced no change in their Social Security benefits.” | 200 / 270813 | `4d8ac99d78af5540cd31faa0e8c42eb40f0be61dff9838694c139e724c1f524c` |
| S2 | P.L. 111-148: “Approved March 23, 2010”; §1311 exchanges “not later than January 1, 2014” <https://www.govinfo.gov/content/pkg/PLAW-111publ148/html/PLAW-111publ148.htm> | 200 / 3393094 | `5d2bbe0a6e6b11072567704fd8050da0e182b9db13bd9c638ad5cb4c2e00e084` |
| S2 | SA 667 (to H.R.1628) actions: “not agreed to in Senate by Yea-Nay Vote. 49 - 51. Record Vote Number: 179.”, api.congress.gov `amendment/115/samdt/667/actions`; the name “skinny repeal” has no primary source | 200 / 3740 | `324886a755ce3c74dda3951799bf1ac9023f3c29cc89c88d8dce4184eab62286` |
| S2 | P.L. 115-97 §11081: penalty “$695” changed to “$0”, “2.5 percent” to “Zero percent”, for “months beginning after December 31, 2018” <https://www.govinfo.gov/content/pkg/PLAW-115publ97/html/PLAW-115publ97.htm> | 200 / 677577 | `ff67e79aff30ec09b589027898ad702318e6074020fb644cc07e1fea6dbadfb1` |
| F1 | H.R.2470 (100th Congress) actions: 1988-07-01 “Became Public Law No: 100-360”, api.congress.gov `bill/100/hr/2470/actions` | 200 / 29091 | `ea0378c017c5e86c54fe918837d9288755cc560007f6e3ace4fa0f0580484118` |
| F1 | CRS summary of conference report H.Rept 100-661: “impose an annual supplemental Medicare premium on individuals who are eligible for benefits under part A … and whose tax liability equals or exceeds $150”, `bill/100/hr/2470/summaries` | 200 / 78563 | `f0566750ff005981aeabbb8958f344f92d9b490a09c58b6638943543f97f1faf` |
| F1 | H.R.3607 (101st Congress) actions: 1989-11-21 “Failed by the Yeas and Nays: 55 - 346 (Roll no. 378)”, “The Senate amendment sought to avoid a complete repeal”; 1989-12-13 “Became Public Law No: 101-234” | 200 / 31416 | `f15301f9517c54c65bc2c651dc17e0669201a25b4c8417224b3233d85fb03d7d` |
| F2 | P.L. 93-239, 87 Stat. 1046: “to conserve fuel … national maximum highway speed limit”, “in excess of 55 miles per hour”, govinfo `STATUTE-87-Pg1046.pdf` | 200 / 647430 | `3d51ac9bf0d7662b46e57bb7db60542d307c88d6287444878adfd3cf907c8042` |
| F2 | P.L. 100-17 §174, 101 Stat. 218: rural interstates “in excess of 65 miles per hour”; legislative history “Mar. 31, House overrode veto. Apr. 2, Senate overrode veto.”, govinfo `STATUTE-101-Pg132.pdf` | 200 / 22233731 | `a2fbba00306b1d3e81c69d8f9eba786c3f5843013e278f50b650ca376d45ec60` |
| F2 | P.L. 104-59 §205(d): “Repeal of National Maximum Speed Limit Compliance Program”; “Approved November 28, 1995” <https://www.govinfo.gov/content/pkg/PLAW-104publ59/html/PLAW-104publ59.htm> | 200 / 231974 | `8ac715b1ae816ccfd6fa3a021eef0ae98fdf14746ff6c1c58c536235b31d1da6` |
| X1 | P.L. 104-193 §103 and new §401(b) “No Individual Entitlement”; findings (5) <https://www.govinfo.gov/content/pkg/PLAW-104publ193/html/PLAW-104publ193.htm> | 200 / 918058 | `5accfc2ae0f6d16ff61401e9af898cf5d12f38d03a392f992474e48d14f90c01` |
| X1 | Clinton signing statement <https://www.presidency.ucsb.edu/documents/statement-signing-the-personal-responsibility-and-work-opportunity-reconciliation-act-1996> | 200 / 69082 | `a479cfc5b6fc7b70303f818282c888a80356f2d768c9146a96d88be3d195fd8d` |
| Poll tax | House of Commons Library SN06583 §1.1 (via Wayback) <https://web.archive.org/web/2024id_/https://researchbriefings.files.parliament.uk/documents/SN06583/SN06583.pdf> | 200 / 421950 | `3d8db512e5396a7251a0c0a2a5691414631193d29f8a78d928cdde7791f353c2` |
| M1 | CIA CSI *At Cold War's End*, part 3 PDF (NIE 11/12-9-88, paragraph 32, book p.165) <https://www.cia.gov/resources/csi/static/At-Cold-Wars-End3-End-of-Empire-I-and-2.pdf> | 200 / 6515457 | `87557bcd7917bcadee31dfd33883b17e4cdeb1c30cf911c75a9835f38d9aee3f` |
| M1 | Bush remarks and Q&A, 1989-11-09 <https://www.presidency.ucsb.edu/documents/remarks-and-question-and-answer-session-with-reporters-the-relaxation-east-german-border> | 200 / 73800 | `d98a6392b289e3b4d29ae6c3592e7aed38e46ef14df0af509ca5dbc059a3faba` |
| M2 | HPSCI report scan (UCLA copy, user upload), p.6 <https://archive.org/download/iran_20260528/Iran.pdf> | 200 / 3055460 | `68f6c690308ad05f7c8a635b3ffad0f10f16883764b1004bcf6264d3adfdeb83` |
| M2 | Carter news conference, 1979-01-17 <https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-979> | 200 / 91938 | prefix `66d0857c` |
| M3 | CBO 1989 report, OCR text <https://archive.org/download/micro_IA41152639_0271/micro_IA41152639_0271_djvu.txt> | 200 / 130045 | `a7e51e1f604a7d11d923c4489b93231d6fae6a7d81e596b54234f9f4ee0cb51d` |
| M4 | Commons debate 1990-04-03 “community-charge-capping” (historic-hansard, via Wayback) | 200 / 277835 | `a57c3d3267eec89276199b456f1320e4fd5615a84ac786931cb6f7b69b0f3a4e` |
| Candidate B | Bush news conference, 1989-06-05 <https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-45> | 200 / 81260 | prefix `efb0ed36` |
| Candidate B | CRS R40095, Food Aid section <https://www.everycrsreport.com/reports/R40095.html> | 200 / 149523 | prefix `d9a79b93` |
| Candidate B | Timur Kuran, “Now Out of Never,” *World Politics* 44(1): 7–48 (1991), uvm.edu scan via Wayback, OCR'd locally (cited pages p.31, p.36 and p.43 re-fetched and re-checked by OCR on 2026-10-09) <https://web.archive.org/web/2024id_/https://pdodds.w3.uvm.edu/teaching/courses/2009-08UVM-300/docs/others/1991/kuran1991a.pdf> | 200 / 4151579 | `8f327873804146a271eae7a5e692bf3ccd36678451317b367ba1b89fcfcce4bd` |

Primary sources that could not be obtained (and must not be filled in from memory): the DIA / NID originals in the CIA reading room (the site redirects requests to its home page), the 1988 original on cbo.gov (403), the roll-call detail for Senate vote 179 on senate.gov (403), and the primary source for the UK's 1991 announcement abolishing the poll tax.
