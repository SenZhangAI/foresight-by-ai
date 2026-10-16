# Calibrating social-regularity candidates against history (2026-10-10): constituency lock-in admitted, then refuted by an estate-tax counterexample and withdrawn; preference-falsification cascades not admitted because they cannot say no

[中文版](social-regularity-calibration-2026-10-10.md) · [Methodology §2](../en/00-method.md#2-toolbox-of-lenses) · [Retrospect](../en/01-retrospect.md)

> **Update, 2026-10-10 (read this first):** The veto form of L10, constituency lock-in, was refuted by the US federal estate tax under the frozen window definition in [§2.6](#26-operational-definition-of-a-repeal-window) and **withdrawn from the toolbox**. Sections 2.1–2.5 preserve the admission-time record; references there to admission describe the earlier judgment.

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

**How to overturn it:** find a public arrangement for which (i) or (ii) is no, yet which survived a [repeal window as defined in §2.6](#26-operational-definition-of-a-repeal-window). A single such case breaks the veto form of L10, and it must then be deleted or narrowed. (Before 2026-10-10 this sentence said “survived a genuine repeal window” without saying what counts as a window; the definition is in §2.6.) **This condition has now occurred**: the federal estate tax survived windows in the 114th and 115th Congresses; L10 is withdrawn.

### 2.5 External comparison (agreement / divergence / why we still hold it)

- **Agreement (this agrees with consensus; it is not presented as an independent discovery):** the asymmetry of concentrated benefits and diffuse costs comes from Mancur Olson's 1965 *The Logic of Collective Action*; the “client politics” type in James Q. Wilson (ed.), *The Politics of Regulation* (Basic Books, 1980); and Paul Pierson, *Dismantling the Welfare State? Reagan, Thatcher and the Politics of Retrenchment* (Cambridge University Press, 1994), on welfare programmes creating their own supporters and retrenchment advancing through obfuscation and grandfathering. Page numbers in these two books were not re-checked in this round.
- **Divergence:** the popular version often treats “once an entitlement exists it is irreversible” as a prediction. AFDC shows that this positive claim already failed within this round's calibration; this page keeps only the half that can say no.
- **Why we still hold it:** the increment is not a novel mechanism but writing it as two variables checkable at time T, keeping only the veto direction, and stating what would overturn it.

### 2.6 Operational definition of a repeal window

> **Frozen on 2026-10-10, written before the case-by-case re-judgment and the counterexample test.** This section lands on its own, in a commit that contains only the definition and the test list; the re-judgment under it is written into a separate section in a later commit, and this section may not be changed afterwards. Before freezing, the author roughly knew how each case ended (like everything on this page, this is `CALIBRATION` with known outcomes), but had not yet looked up any of the legislative vote records used below.

§2.4 used to say “survived a genuine repeal window” without saying what counts as a window. Any survival could then be explained as “the window had not opened yet”, which is the same defect that got candidate B rejected: protecting a rule with a quantity that can be moved after the fact. The definition below turns the window into an event that can be looked up case by case in legislative records.

**Object:** a public arrangement A established by legislation, whether a benefit, a regulation or a tax. Coding of (i) and (ii) follows §2.2.

**Outright-repeal measure:** a measure such that, once all its provisions are in force, the individual benefit claims A confers, or the obligations it imposes, end for everyone, and all three of the following hold: (a) current recipients or obligors are not kept on (no grandfather clause); (b) they are not replaced by an individual claim of the same type (the same benefit paid under a new name does not count); (c) there is no sunset clause that brings A back on expiry. A measure that relaxes only part of A (some roads, some groups, some years), or cuts only the cost side, is not an outright-repeal measure. This is the same yardstick by which §2.3 records S2 (“penalty set to $0, benefits kept”) as survival.

**Window opens:** in the legislature with the power to repeal A, a bill carrying an outright-repeal measure against A wins final passage in at least one vote that the measure must clear. In a bicameral legislature, final passage on the floor of either chamber suffices, including passage as part of a larger bill; in a unicameral or parliamentary legislature, passage at second reading or an equivalent vote on principle counts. The window opens on the date of that passage.

**Window closes:** at the end of that legislative term. For the US, that is the end of that Congress, the day before the next Congress convenes.

**What does not open a window:** a measure that is only introduced, only reported out of committee, defeated on the floor, or merely advocated by the head of the executive in a speech or a budget. These show only that not even one required majority has yet chosen repeal.

**How to decide:** at US federal level, use the “Passed House” / “Passed Senate” entries and roll-call numbers in congress.gov (or api.congress.gov) bill actions to fix the date of passage, the passed text to decide whether it is an outright-repeal measure, and the public-law text (govinfo) to decide whether it became law. For other legislatures, use their official records of proceedings.

**What the rule claims about time:** under this definition, “outright repeal is within reach” in the veto form of L10 means one thing only: for an arrangement with (i) or (ii) no, **once a window opens, outright repeal becomes law before that window closes** (including over an executive veto). The rule does not predict when a window opens or whether one ever will; an arrangement continuing to exist in years with no window is neither evidence nor counterexample. For an arrangement with both (i) and (ii) yes, the rule predicts nothing within a window; it says only that repeal will meet defenders.

**Overturn condition (replaces “a genuine repeal window” in §2.4):** an arrangement with (i) or (ii) no that still exists when a window opened under this definition closes — that is, outright repeal did not become law — is a counterexample. One such case breaks the veto form of L10, which must then be deleted or narrowed under §2.4, with the change marked in place in the “social regularities” row of the methodology mapping table and in the L10 section.

**Test list (frozen with this section):**

1. **Re-judge the five cases.** Re-judge S1, S2, F1, F2 and X1 under this definition, giving for each whether a window occurred within the interval, its opening and closing dates, and source locators. The intervals:
   - S1: 2005-01-04 to 2007-01-03 (the 109th Congress);
   - S2: 2010-03-23 to 2019-01-03 (from enactment to the end of the 115th Congress);
   - F1: 1988-07-01 to 1989-12-13;
   - F2: 1974-01-02 to 1995-11-28, with **a separate answer on whether a window occurred between 1974-01-02 and 1987-12-31**;
   - X1: 1993-01-05 to 1996-08-22.
2. **Counterexample test: the US federal estate tax**, interval 1999-01-06 to 2019-01-03 (the 106th to the 115th Congress). Coded in advance: estate-tax revenue goes into the general budget, and no group draws its benefit on a recurring basis, so (i) is no. Indirect income that estate planners, life insurers or charities earn because of the tax is not counted as “the arrangement's benefit”; F2 likewise did not count insurers' gains from fewer crashes as a benefit, so the yardstick is the same. The rule therefore says “no protection from beneficiaries” and predicts that, within a window, outright repeal becomes law. The reason for choosing it is stated plainly: before freezing, the author already knew that its repeal had been proposed many times, had passed the House, and that the tax still exists; it is the most conspicuous candidate the author could name. Like every other case on this page, it was chosen after its outcome was known.
3. **Disposition fixed in advance.** If any counterexample holds, the veto form of L10 fails under §2.4; the deletion, narrowing or downgrade, and the in-place marking, are made public in the re-judgment commit. This section may not be changed afterwards to escape the result.

### 2.7 Case-by-case re-judgment and counterexample test: L10 veto form refuted and withdrawn

> This section was written after §2.6 was frozen (commit `c9188d9`). The definition in §2.6 is unchanged. Every legislative vote and bill text used below was checked only after the freeze; the source files, byte counts and SHA-256 values are listed in the “2026-10-10 additions” table at the end of §6.

**Conclusion:** the counterexample test holds. The federal estate tax was coded in advance as (i) no, yet the 114th and 115th Congresses each opened an outright-repeal window and both windows closed with the tax still in force. Therefore **the veto form of L10 fails and is withdrawn from the toolbox**. None of the five original cases conflicts with the rule under the new definition: F1 and F2 are consistent; S1, S2 and X1 are outside its predictions. F2 had no qualifying window from 1974 through 1987.

The dates below use the §2.6 convention: a US window closes on the day before the next Congress convenes. “No window” means no qualifying outright-repeal measure passed a required chamber; it is not evidence that the arrangement would survive a window.

| Case | (i) / (ii) | Interval | Window | Opened (evidence) | Closed | Outcome | Relation to rule |
|---|---|---|---|---|---|---|---|
| **S1 Social Security personal accounts** | yes / yes | 2005-01-04 to 2007-01-03 (109th Congress) | **No** | — (no qualifying passage: of the 10 reform bills in the 109th Congress, “None received congressional action”, [CRS RL33544](https://www.everycrsreport.com/files/20070425_RL33544_b869fb4b80374de65d8b7cecc5188b4a0330ed66.html), Summary) | — (no window, so nothing to close) | Still in force at the end of the tested interval, 2007-01-03; the proposal itself left those born before 1950 unchanged ([CRS RL32879](https://www.everycrsreport.com/reports/RL32879.html)) | No prediction; not a test |
| **S2 Affordable Care Act** | yes / yes (coding time: see below) | 2010-03-23 to 2019-01-03 | **Yes, three times** | 2011-01-19: House passed H.R.2 (112th), 245–189, Roll no.14, text “such Act is repealed” ([`BILLS-112hr2eh`](https://www.govinfo.gov/content/pkg/BILLS-112hr2eh/html/BILLS-112hr2eh.htm); [`BILLSTATUS-112hr2`](https://www.govinfo.gov/bulkdata/BILLSTATUS/112/hr/BILLSTATUS-112hr2.xml)); 2013-05-16: House passed H.R.45 (113th), 229–195, Roll no.154 ([`BILLSTATUS-113hr45`](https://www.govinfo.gov/bulkdata/BILLSTATUS/113/hr/BILLSTATUS-113hr45.xml)); no later than 2015-12-03: Senate passed H.R.3762 (114th), 52–47, Record Vote 329, repealing the premium tax credits, cost-sharing subsidies and the Medicaid expansion ([`BILLSTATUS-114hr3762`](https://www.govinfo.gov/bulkdata/BILLSTATUS/114/hr/BILLSTATUS-114hr3762.xml); [`BILLS-114hr3762enr`](https://www.govinfo.gov/content/pkg/BILLS-114hr3762enr/html/BILLS-114hr3762enr.htm)) | At the end of the 112th, 113th and 114th Congresses respectively: 2013-01-02, 2015-01-02, 2017-01-02 | Survived all three closures; H.R.3762 was vetoed on 2016-01-08 and the House override failed on 2016-02-02, 241–186, Roll no.53 ([`BILLSTATUS-114hr3762`](https://www.govinfo.gov/bulkdata/BILLSTATUS/114/hr/BILLSTATUS-114hr3762.xml)) | No prediction (has defenders) |
| **F1 Medicare Catastrophic Coverage Act** | partly / no | 1988-07-01 to 1989-12-13 | **Yes** | No later than 1989-11-08: the House passed H.R.3607 “to repeal Medicare provisions in the MCCA of 1988” (legislative history of P.L. 101-234: “Nov. 8, considered and passed House”, [`STATUTE-103-Pg1979`](https://www.govinfo.gov/content/pkg/STATUTE-103/pdf/STATUTE-103-Pg1979.pdf)). “No later than”: the window opened on this date or earlier; no earlier date is asserted. | End of the 101st Congress (1991-01-02 under the §2.6 convention); repeal became law first, inside the window | Outright repeal became law on 1989-12-13 (P.L. 101-234; H.R.3607 actions, api.congress.gov `bill/101/hr/3607/actions`, §6) | **Consistent** |
| **F2 national 55-mph speed limit** | no / — | 1974-01-02 to 1995-11-28 | **None in 1974–1987; opened 1995-09-20** | 1995-09-20: the House passed S.440 with an amendment, Sec.348 “Sections 141(a) and 154 … are repealed” ([`BILLS-104s440eah`](https://www.govinfo.gov/content/pkg/BILLS-104s440eah/html/BILLS-104s440eah.htm)); the 1974–1987 negative answer rests on [CRS IB86153](https://www.everycrsreport.com/files/19870409_IB86153_08fe581aa020b58ac495c0d557a726689e362119.pdf) and the *History of Bills* 1983–1987 volumes (e.g. [`HOB-1983`](https://www.govinfo.gov/content/pkg/HOB-1983/html/HOB-1983.htm)), with the gap stated below | End of the 104th Congress (1997-01-02 under the §2.6 convention); repeal became law first, inside the window | 1995-11-28: P.L. 104-59 §205(d) became law, inside the window ([P.L. 104-59](https://www.govinfo.gov/content/pkg/PLAW-104publ59/html/PLAW-104publ59.htm)) | **Consistent** |
| **X1 AFDC** | yes / yes | 1993-01-05 to 1996-08-22 | **Yes** | 1995-03-24: the House passed H.R.4 (title I turned AFDC into TANF block grants to states; the claim belongs to the state, not the individual) ([`BILLS-104hr4eh`](https://www.govinfo.gov/content/pkg/BILLS-104hr4eh/html/BILLS-104hr4eh.htm)) | End of the 104th Congress (1997-01-02 under the §2.6 convention); the law came first, inside the window | 1996-08-22: P.L. 104-193 became law ([P.L. 104-193](https://www.govinfo.gov/content/pkg/PLAW-104publ193/html/PLAW-104publ193.htm)) | No prediction; strong form refuted (§2.3 unchanged) |
| **Federal estate tax (counterexample test)** | **no** (pre-coded before the freeze) | 1999-01-06 to 2019-01-03 | **Yes; 2 principal windows** | 2015-04-16: House passed H.R.1105 (114th), 240–179, Roll no.161 ([`BILLS-114hr1105eh`](https://www.govinfo.gov/content/pkg/BILLS-114hr1105eh/html/BILLS-114hr1105eh.htm); [`BILLSTATUS-114hr1105`](https://www.govinfo.gov/bulkdata/BILLSTATUS/114/hr/BILLSTATUS-114hr1105.xml)); 2017-11-16: House passed H.R.1 (115th), 227–205, Roll no.637 ([`BILLS-115hr1eh`](https://www.govinfo.gov/content/pkg/BILLS-115hr1eh/html/BILLS-115hr1eh.htm); [`BILLSTATUS-115hr1`](https://www.govinfo.gov/bulkdata/BILLSTATUS/115/hr/BILLSTATUS-115hr1.xml)) | 2017-01-02; 2019-01-02 | Still in force at both closures; P.L. 115-97 §11061 only doubled the basic exclusion ([P.L. 115-97](https://www.govinfo.gov/content/pkg/PLAW-115publ97/html/PLAW-115publ97.htm)) | **Counterexample** |

**F2 from 1974 through 1987:** on the records currently available, no qualifying window occurred. The floor measures that were actually voted on were partial relaxations, not outright repeal under §2.6. CRS IB86153 (updated 1987-04-09) records that the eight bills introduced in the 99th Congress received no favorable committee action; the 1986 McCurdy and Symms amendments and the 1987 P.L.100-17 changes were also partial relaxations. The *History of Bills* volumes were checked for 1983–1987, while 1974–1982 remains a coverage gap: the CRS legislative-history narrative was checked, but each Congress's floor amendments were not. This 13-year period is neither evidence nor a counterexample because no window was found and the rule makes no claim without one.

**F2 from 1988 through 1995:** the separate repeal bills in 1992, 1993 and 1995 did not pass a chamber; the 1991 ISTEA amendments were not checked individually and remain a stated gap. The Senate's 1995-06-22 S.440 measure applied the limit only to certain commercial motor vehicles and therefore was a partial relaxation. The House's 1995-09-20 version was the first qualifying outright-repeal measure; the law followed 69 days later.

**Estate tax: why it is a counterexample, and where a critic could attack.** H.R.1105's §2210 would have ended the estate-tax chapter for estates of decedents dying on or after enactment, without a sunset or carryover-basis replacement; H.R.1's §1602 similarly would have ended it for estates after 2024-12-31 while preserving the stepped-up basis. Excluding versions that used carryover basis still leaves these two counterexamples. Indirect income to estate planners, life insurers and charities remains excluded exactly as pre-coded; changing that definition after seeing the result would move the goalposts. The fact that pre-enactment deaths leave already-accrued tax liabilities is not a grandfather clause, just as F2 and X1's repeals applied prospectively. Gift tax is a separate chapter from the pre-coded federal estate-tax object, so its survival does not change the test.

**S2 did not open a qualifying window in the 115th Congress:** the House-passed H.R.1628 (2017-05-04, 217–213, Roll no.256) used replacement refundable credits for exchange subsidies and grandfathered Medicaid-expansion enrollees, so it failed §2.6(a) and (b). Senate SA 667 failed 49–51 (§2.3; source row in §6). The coding-time gap is stated honestly: §2.2 does not say whether (i) is recoded when a window opens; under the §2.3 coding S2 remains yes/yes, and recoding at the window would not rescue L10's estate-tax counterexample.

**Disposition: withdrawal, not narrowing.** Narrowing the object to benefit programmes would discard F2 and leave only one “no” control, below the 2+2 admission threshold. Changing the window definition after seeing the counterexample is forbidden by §2.6. The institutional veto points that stopped estate-tax repeal are not beneficiary protection. They may motivate a new candidate, but are not a successor rule here.

### 2.8 Protocol §11.B affected-card inventory (2026-10-10)

The bilingual inventory covered all 107 cards. Only three C13 cards had reasoning that factually depended on the “incumbent beneficiaries block repeal/reform” logic: J-105, J-106 and J-107. Only J-106 invoked L10. After withdrawal its lens field states that this step is carried by no lens in L1–L9; its conclusion, status, confidence, time window and falsifier are unchanged. J-105 and J-107 already said they did not invoke L10 and are unchanged. The other keyword hits were incidental mentions, not uses of the logic.

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
- it does not support continued use of L10: the estate-tax counterexample refuted and withdrew its veto form;
- it does not support using the positive half of L10 as a survival prediction;
- it changes no judgment card's conclusion or status; §2.8 records the inventory, and only J-106's lens field was amended;
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
| F1 | H.R.3607 (101st Congress) actions: 1989-11-21 “Failed by the Yeas and Nays: 55 - 346 (Roll no. 378)”, “The Senate amendment sought to avoid a complete repeal”; 1989-12-13 “Became Public Law No: 101-234”, api.congress.gov `bill/101/hr/3607/actions` (path added 2026-10-10; legislative-history date also appears in the `STATUTE-103-Pg1979.pdf` row at the end of this table) | 200 / 31416 | `f15301f9517c54c65bc2c651dc17e0669201a25b4c8417224b3233d85fb03d7d` |
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
| M4 | Commons debate 1990-04-03 “community-charge-capping” (historic-hansard, via Wayback) <https://web.archive.org/web/20241015105151id_/https://api.parliament.uk/historic-hansard/commons/1990/apr/03/community-charge-capping> (URL added and source re-fetched on 2026-10-10; decompressed byte count and SHA-256 match the original record) | 200 / 277835 | `a57c3d3267eec89276199b456f1320e4fd5615a84ac786931cb6f7b69b0f3a4e` |
| Candidate B | Bush news conference, 1989-06-05 <https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-45> | 200 / 81260 | prefix `efb0ed36` |
| Candidate B | CRS R40095, Food Aid section <https://www.everycrsreport.com/reports/R40095.html> | 200 / 149523 | prefix `d9a79b93` |
| Candidate B | Timur Kuran, “Now Out of Never,” *World Politics* 44(1): 7–48 (1991), uvm.edu scan via Wayback, OCR'd locally (cited pages p.31, p.36 and p.43 re-fetched and re-checked by OCR on 2026-10-09) <https://web.archive.org/web/2024id_/https://pdodds.w3.uvm.edu/teaching/courses/2009-08UVM-300/docs/others/1991/kuran1991a.pdf> | 200 / 4151579 | `8f327873804146a271eae7a5e692bf3ccd36678451317b367ba1b89fcfcce4bd` |

**2026-10-10 additions (primary sources used in §2.7, fetched UTC 2026-10-10).** Where the “Source and locator” column starts with a package name, the URL is built in one of three fixed forms: bill text `https://www.govinfo.gov/content/pkg/<package>/html/<package>.htm`; bill actions `https://www.govinfo.gov/bulkdata/BILLSTATUS/<Congress>/hr/<package>.xml` (govinfo has this bulk data only from the 108th Congress on); *History of Bills* annual volumes `https://www.govinfo.gov/content/pkg/<package>/html/<package>.htm`, with packages named like `HOB-1983`. Every other row gives its full URL. govinfo occasionally returns 200 with a truncated body, so compare byte counts and SHA-256 when re-checking.

| Use | Source and locator | HTTP / bytes | SHA-256 |
|---|---|---|---|
| S2 112th | `BILLS-112hr2eh`: “such Act is repealed”; “Passed the House of Representatives January 19, 2011” | 200 / 2559 | `eb10596e9f6b95207ea399e7c57530dd1fa8c94dfa3df2b0fd3e314658dc6a0a` |
| S2 112th | `BILLSTATUS-112hr2`: “245 - 189 (Roll no. 14)” | 200 / 110870 | `3fda21f64e47b085ed522af69128727ae1e489d3806c1d5f67d161d4c3ae57dc` |
| S2 113th | `BILLSTATUS-113hr45`: “229 - 195 (Roll no. 154)” | 200 / 83882 | `aa1801bb117d2d6fe003d19cde23ff5ec476fc9bd671262e090928bd2caa0383` |
| S2 114th | `BILLSTATUS-114hr3762`: 2015-12-03 “Passed Senate with an amendment by Yea-Nay Vote. 52 - 47. Record Vote Number: 329.”; 2016-01-08 “Vetoed by President”; 2016-02-02 override failed “241 - 186 (Roll no. 53)” | 200 / 257363 | `d0917f6ad9928d3ae9119553a210484f2188752cffb65f117f7044d5840a9829` |
| S2 114th | `BILLS-114hr3762enr`: Sec.202 “Premium tax credit and cost-sharing subsidies”, Sec.207 “Medicaid” | 200 / 21188 | `30c9a4f968eb7f3731480be73e5ca561b48ec9fedfdc5f2332b6305050eb6bbf` |
| S2 115th | `BILLS-115hr1628eh`: Sec.112 “Repeal of Medicaid expansion” and “grandfathered expansion enrollee”; Sec.214 “Refundable tax credit for health insurance coverage”; “Passed the House of Representatives May 4, 2017” | 200 / 177535 | `9aa3de8b0346e4b7e90dce408d5c7f5b2c9216f35f2a4184b1763452689bf22c` |
| S2 115th | `BILLSTATUS-115hr1628`: “217 - 213 (Roll no. 256)” | 200 / 488455 | `82709f1498e14e29d5026328e5bddc62fa99ee5a125582187f0763271c502908` |
| F1 | P.L. 101-234 legislative history, “Nov. 8, considered and passed House” <https://www.govinfo.gov/content/pkg/STATUTE-103/pdf/STATUTE-103-Pg1979.pdf> | 200 / 1341281 | `282170e603d7dbee1f5b032b07051c84b7b54f8bf2a725ba107fdd4815cb53d5` |
| F2 1974–1987 | CRS IB86153, *Speed Limits for Motor Vehicles* (updated 1987-04-09), legislative-history section: the 8 speed-limit bills of the 99th Congress — “None of these bills received favorable committee action”; McCurdy amendment 198–298, Symms amendment 56–36, Hecht amendment 36–60; 1987 Symms amendment 65–33, H.Con.Res.77 217–206 and 60–21, veto override <https://www.everycrsreport.com/files/19870409_IB86153_08fe581aa020b58ac495c0d557a726689e362119.pdf> | 200 / 686658 | `96f4719fb11855ccfa3a858c1816fd0946ff9592ecc3dc440015e7e6aa926de2` |
| F2 1983 | `HOB-1983`: S.1121 “A bill to repeal the national maximum speed limit for motor vehicles”, H.R.785, H.R.851, H.R.2826 — introduction and cosponsorship only | 200 / 3236464 | `07fddd31d7bc0b8842c50b065cb2cce5fcda50840a4fea6e460a5e316e9e0fab` |
| F2 1984 | `HOB-1984`: no speed-limit bill entry at all, i.e. no action that year | 200 / 2157884 | `a7d6f8b0b6678f0fa5bc40adfd6e4d39eaa517e891e60ecbdc811932d36cc4f1` |
| F2 1985 | `HOB-1985`: H.R.1086 “A bill to repeal section 154 of title 23” — introduction and cosponsorship only | 200 / 2394773 | `b23628c0cf69a8b8eb3d102b4b17d6192e592c1c321a3ab91ac2cc0342697c60` |
| F2 1986 | `HOB-1986`: H.R.1086 — cosponsorship only | 200 / 2135716 | `5a6879e9de9415b3bcd2c2ad4dc93936f610794deb376ee42e61fa213e653ebf` |
| F2 1987 | `HOB-1987`: H.R.263 “A bill to repeal section 154”, H.R.670 “to repeal the 55-mile-per-hour speed limit requirements” — introduction and cosponsorship only | 200 / 3072657 | `bbd654cb7ace1d1b9649fa446fc3e43bd80430deda53a36512f4ac699a474f8f` |
| F2 1992 | `HOB-1992`: H.R.5606, H.R.5884 — introduction only | 200 / 2847725 | `01643e0db9647580f66e7ba45d3e50ae09bd78da12ed902e9bb8229d549b9038` |
| F2 1993 | `HOB-1993`: H.R.1512 “to repeal provisions establishing a national maximum speed limit” — introduction only | 200 / 3092453 | `3dcad963a10817c9cc9cb7df208a4caece63118c46f940c302b92440d8f05c2b` |
| F2 1995 | `HOB-1995`: S.476 “to eliminate the national maximum speed limit”, H.R.427 — introduction and cosponsorship only | 200 / 2611286 | `a237750db1ee1a42060136bed452ec139e8c5b86caa20b78690d6f2e75279dd8` |
| F2 1995 | `BILLS-104s440es`: “Sec. 115. Limitation of national maximum speed limit to certain commercial motor vehicles”; “Passed the Senate June 22 (legislative day, June 19), 1995” | 200 / 116431 | `11a0738bb176b7db7039c3648b2af0767a5aa99551753d36a76c35f53e7d09c9` |
| F2 1995 | Senate proceedings on passing S.440, 1995-06-22 <https://www.govinfo.gov/content/pkg/CREC-1995-06-22/html/CREC-1995-06-22-pt1-PgS8924.htm> | 200 / 122930 | `ae08be42d89dc7419bb6a7afb40d614388dd76f7e421f16675a2bdf982daad4e` |
| F2 1995 | `BILLS-104s440eah`: “In the House of Representatives, U. S., September 20, 1995”; Sec.348 “Sections 141(a) and 154 of title 23 … are repealed” | 200 / 146193 | `6101af3303e7178739c15fded8fada65dcc31a4ae422804818576f7dae6f56a7` |
| X1 | `BILLS-104hr4eh`: “Title I--Block grants for temporary assistance for needy families”; “Passed the House of Representatives March 24, 1995” | 200 / 545570 | `2e53b5d8909e5f13ec924f322991a99e2847551b792ba9d0c87a712fafe4b9cb` |
| Estate tax 114th | `BILLS-114hr1105eh`: §2210 “shall not apply to the estates of decedents dying on or after the date of the enactment”, §2664; “Passed the House of Representatives April 16, 2015” | 200 / 8571 | `d6bbf52a4ad1b0b2cc159354a4cb9d7e8d8d8e10f3ae57eb7ffb79ea553a1fe5` |
| Estate tax 114th | `BILLSTATUS-114hr1105`: “240 - 179 (Roll no. 161)” | 200 / 80284 | `cd014425963ca534d2c7f990eca51505d4ce447555b0aaff37f30579290b83c9` |
| Estate tax 115th | `BILLS-115hr1eh`: Sec.1602 §2210 “shall not apply to the estates of decedents dying after December 31, 2024”; “Passed the House of Representatives November 16, 2017” | 200 / 585883 | `305dd662c250fa9a25ddab62b2628d6df9b2cb0155cdc2c1a365e5ebafb9fac9` |
| Estate tax 115th | `BILLSTATUS-115hr1`: “227 - 205 (Roll no. 637)” | 200 / 1024095 | `3a350dfa93e1ae57f1ccd671554e5b5efee6863cb34ec842fc2e28ab56ea4207` |
| Estate tax 115th | P.L. 115-97 §11061: “after December 31, 2017, and before January 1, 2026”, “$10,000,000” for “$5,000,000”; the same original as the S2 row above, with identical byte count and SHA-256 | 200 / 677577 | `ff67e79aff30ec09b589027898ad702318e6074020fb644cc07e1fea6dbadfb1` |
| Estate-tax sensitivity | `BILLS-106hr8eh`: “June 9, 2000”; new §1022 “Carryover basis for certain property acquired from a decedent” | 200 / 45705 | `9a2aebe6a3f92fb983e2579b62a6422de5ef6752fcb32a5830c878db6db1e20c` |
| Estate-tax sensitivity | `BILLS-106hr8enr`: the enrolled bill after passage by both chambers | 200 / 40478 | `b3682d15e75bb26bd08655697c337996abd9f76d80e6a0e565240f192666ad14` |
| Estate-tax sensitivity | `BILLS-107hr2143eh`: “June 6, 2002” | 200 / 1778 | `cfd80f1c9b0da98077929d8605cb8f2d498307fbbb812698969e31b06c6229a0` |
| Estate-tax sensitivity | `BILLSTATUS-108hr8`: “264 - 163 (Roll no. 288)” | 200 / 106919 | `88a2a23a5f0f7606ffa0e9d8cca3a99f7aaa13305159f8d114a0e91f3f946d9c` |
| Estate-tax sensitivity | `BILLS-109hr8eh`: “Passed the House of Representatives April 13, 2005” | 200 / 1266 | `d3d31311b7c6b8fb63b1a0cab8a402d9c3a875db71c88463260bb7e6fdde8b46` |
| Estate-tax sensitivity | `BILLSTATUS-109hr8`: “272 - 162 (Roll no. 102)”; Senate “57 - 41. Record Vote Number: 164” | 200 / 115071 | `314027b13969fda42a4d67bc273694979c4310b5cd7843b8c397a2b432859202` |

Primary sources that could not be obtained (and must not be filled in from memory): the DIA / NID originals in the CIA reading room (the site redirects requests to its home page), the 1988 original on cbo.gov (403), the roll-call detail for Senate vote 179 on senate.gov (403), and the primary source for the UK's 1991 announcement abolishing the poll tax; 2026-10-10 additions: the online *History of Bills* volumes for 1974–1982 (govinfo starts in 1983), the govinfo subject index needed to check the 1991 ISTEA floor amendments, and a primary source for the veto date of the 106th Congress's H.R.8 (govinfo bulk bill actions start with the 108th Congress, and the api.congress.gov public demo key was over its limit that day).
