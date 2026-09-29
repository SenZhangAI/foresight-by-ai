# Political Forecast-Miss Calibration: Preservable Evidence Packet (2026-09)

> **Evidence level: `CALIBRATION`, not out-of-sample accuracy.** This file uses historical material whose outcomes are already known to identify failure boundaries in the method. It cannot establish a general hit rate and does not create future forecast cards.
>
> **The four-case count is derived from the candidate register.** P-01–P-06 are a fixed register; only rows with `status=qualified` count. Candidates must not be deleted to preserve a target count. Each `qualified` case supplies a repository-readable `prediction_artifact` and `outcome_artifact` containing original response/file bytes, identity, source dates, retrieval date, HTTP/file status, raw-byte hash, and excerpt location/hash.

## Evidence packet index

- **Canonical manifest hash:** `80ec916729e3b669fe7d9b1da66c254be70b9747c275ce958f9ad3bc20723a63` (manifest content appears at the end; version ID `politics-calibration-2026-09-v2`)
- **Artifact root:** [`politics-artifacts/`](politics-artifacts/)
- **Retrieval date:** 2026-09-29 (UTC date; source publication dates are listed per artifact)
- HTML artifacts preserve response bytes; PDF/TXT artifacts preserve downloaded file or text-file bytes. Excerpts are derived from artifacts and are not substitutes for them.
- `raw_bytes_sha256` hashes the repository artifact itself; `excerpt_sha256` hashes bytes from `byte_offset_start` inclusive to `byte_offset_end` exclusive. Readers can recompute it with `dd` or a script.

## Fixed candidate register (do not delete rows)

| case_id | candidate | status | count | reason |
|---|---|---|---:|---|
| P-01 | 2016 UK EU referendum on-the-day poll | `qualified` | 1 | Forecast and outcome use the referendum direction/percentage; both HTML artifacts are readable and the dates and excerpts are reconstructable. |
| P-02 | 2017 UK general-election majority-government forecast | `qualified` | 1 | The forecast is an institutional majority outcome; the outcome artifact states a hung Parliament. Seat majority must not be exchanged for vote share. |
| P-03 | 2021 Afghanistan post-withdrawal national takeover forecast | `unverified` | 0 | The prediction artifact is preserved, but the CRS outcome artifact could not be preserved in this run; a URL/search snippet cannot count. |
| P-04 | FOMC forecast for 2008 real GDP | `qualified` | 1 | Forecast and outcome are both 2008 Q4/Q4 real GDP growth in percent; both HTML artifacts are readable. |
| P-05 | UK GDP counterfactual shock forecast after Brexit | `unverified` | 0 | The forecast is a two-year level difference against a Remain counterfactual; the preserved outcome is actual annual growth and lacks the same counterfactual series. |
| P-06 | Iraqi WMD stockpile forecast | `qualified` | 1 | The pre-war forecast and post-war investigation both directly address stockpiles; PDF/TXT artifacts and excerpt locations are reconstructable. |

**Qualified cases (derived from rows with `status=qualified`): 4.** P-03 and P-05, including their IDs, statuses, and reasons, must remain in the register; they are not count-padding failures.

## Shared fields and classification rule

Each case records `forecast_metric`, `outcome_metric`, `unit`, `population/base`, `forecast_date`, `outcome_date`, `observation_window`, and `threshold_or_comparison_rule`. Exactly one primary class is used: `direction`, `timing`, `scale`, or `mechanism`. Where forecast and outcome fields are not identical, the `derived/comparable_with_rule` mapping is explicit; topical similarity is not comparability.

## Qualified cases

### P-01 · UK EU referendum: YouGov on-the-day poll reversed the direction

- **Forecast source/artifact:** YouGov, *YouGov on the day poll: Remain 52%, Leave 48%*, published 2016-06-23. Artifact: [`prediction.html`](politics-artifacts/P-01/prediction.html), media type `text/html`, retrieval HTTP `200`, `raw_bytes_sha256=b7167d06dafb7f1f52e7939d6ea2499798c661d80cadb072490a5ddabe04ad1f`, source URL: <https://yougov.com/en-gb/articles/15778-yougov-day-poll>.
- **Forecast excerpt:** `Remain are on 52% with Leave on 48%.`; artifact byte range `[231946,231986)`; `excerpt_sha256=64bbba25935acc518678156eab4ec408dd013acd3893422517686651efcaf643`.
- **Outcome source/artifact:** UK Prime Minister’s Office, *The result of the EU Referendum: Ambassador's Statement*, published 2016-06-24. Artifact: [`outcome.html`](politics-artifacts/P-01/outcome.html), `text/html`, retrieval HTTP `200`, `raw_bytes_sha256=d774df6ad02ba3c0ec6420f760c279ead9b88f12539f847f8070b5ee3c71e8ad`, source URL: <https://www.gov.uk/government/news/the-result-of-the-eu-referendum-ambassadors-statement>.
- **Outcome excerpt:** `their decision to leave the European Union is respected.`; the artifact contains GOV.UK's original JSON/HTML response; byte range `[4093,4389)` (escaped HTML in JSON, directly recomputable); `excerpt_sha256=693ba6f3814ba35f901e894c9a30d5123736718f46f3ea956df2bde05f434015`.
- **forecast_metric:** Leave/Remain valid-vote shares and first-place direction; **outcome_metric:** Leave/Remain referendum direction; **unit:** percent / ordinal winner; **population/base:** UK EU-membership referendum voters; **forecast_date:** 2016-06-23; **outcome_date:** 2016-06-24; **observation_window:** poll publication to result announcement; **threshold_or_comparison_rule:** forecast ranked Remain first, official outcome ranked Leave first; **derived/comparable_with_rule:** same referendum question, comparing winner direction only, without treating percentage differences as a separate `scale` miss.
- **Single classification:** `direction`.

### P-02 · 2017 UK general election: majority-government forecast failed

- **Forecast source/artifact:** YouGov, *Final call poll: Tories lead by seven points and set to increase majority*, published 2017-06-07. Artifact: [`prediction.html`](politics-artifacts/P-02/prediction.html), `text/html`, HTTP `200`, `raw_bytes_sha256=e47041289e141fcc3b013e67cddf112fd1b4d2b67d340d3f3ebdb5ed9d64be26`, source URL: <https://yougov.com/en-gb/articles/18339-final-call-poll-tories-seven-points-and-set-increa>.
- **Forecast excerpt:** `increased Conservative majority in the Commons.`; byte range `[360124,360175)`; `excerpt_sha256=39ebee32d1b50ba3ce97aa1d83aec05143407ac09d58ffaee168ca7bbda71756`.
- **Outcome source/artifact:** House of Commons Library, *General Election 2017: results and analysis*, published 2017-06-09. Artifact: [`outcome.html`](politics-artifacts/P-02/outcome.html), `text/html`, HTTP `200`, `raw_bytes_sha256=555b715c8417cb1c717f26ecd5033fef4cf7ef89fa6aaa50943c31128fcbb5d1`, source URL: <https://commonslibrary.parliament.uk/research-briefings/cbp-7979/>.
- **Outcome excerpt:** `The 2017 General Election resulted in a hung Parliament, with no party winning an overall majority.`; the same original paragraph gives Conservative 317 seats / 42.3% vote and Labour 262 seats / 40.0%; byte range `[46194,46576)`; `excerpt_sha256=f0ec768ff5d77a54adab4176db5860a943de290ddd8eeff661a6c34c67a3bd38`.
- **forecast_metric:** whether a Conservative majority government would result; **outcome_metric:** whether any party obtained an overall Commons majority; **unit:** binary institutional outcome; **population/base:** UK House of Commons election; **forecast_date:** 2017-06-07; **outcome_date:** 2017-06-08; **observation_window:** final call to election result; **threshold_or_comparison_rule:** `increased Conservative majority` versus `no party winning an overall majority`; **derived/comparable_with_rule:** institutional outcome only—42% vote share is not substituted for seat majority, and seats and votes are not mixed.
- **Single classification:** `direction`.

### P-04 · US 2008 growth: FOMC forecast positive growth, outcome contracted

- **Forecast source/artifact:** Federal Reserve Board, *Summary of Economic Projections, October 30–31, 2007*, published 2007-10-31. Artifact: [`prediction.html`](politics-artifacts/P-04/prediction.html), `text/html`, HTTP `200`, `raw_bytes_sha256=cab478c6be574fb093de71a750d7b860e67e5e9480800678b544c7f2a7c7a8d8`, source URL: <https://www.federalreserve.gov/monetarypolicy/fomcminutes20071031ep.htm>.
- **Forecast excerpt:** `central tendency of participants projections for real GDP growth in 2008 was revised down to 1.8 to 2.5 percent`; byte range `[8275,8558)`; `excerpt_sha256=d2a31bd0f113557331e69bf7ea16ede9e060fd6ab10436ce76ca21f0d3fc45ae`.
- **Outcome source/artifact:** Bureau of Economic Analysis, *Gross Domestic Product, Fourth Quarter 2008 (final) and Corporate Profits*, published 2009-03-27. Artifact: [`outcome.html`](politics-artifacts/P-04/outcome.html), `text/html`, HTTP `200`, `raw_bytes_sha256=25e1cd908db8c40127a72cc95ef511170960e83bd9707d33398151c72c60ffd1`, source URL: <https://www.bea.gov/news/2009/gross-domestic-product-fourth-quarter-2008-final-and-corporate-profits>.
- **Outcome excerpt:** `During 2008 ... real GDP decreased 0.8 percent.`; byte range `[33844,34200)`; `excerpt_sha256=484045ac20e0e7f2a3168983b07c6cd1ed6d37986c79a574b4b6292cbe357c25`.
- **forecast_metric:** US real GDP growth, Q4/Q4; **outcome_metric:** US real GDP growth, Q4/Q4; **unit:** percent; **population/base:** US real GDP, fourth-quarter-to-fourth-quarter; **forecast_date:** 2007-10-31; **outcome_date:** 2009-03-27 final-estimate release; **observation_window:** 2008 Q4/Q4; **threshold_or_comparison_rule:** forecast interval wholly positive (1.8–2.5%), final same-metric value −0.8%; **derived/comparable_with_rule:** both the forecast footnote and outcome artifact use Q4/Q4, not annual-average growth.
- **Single classification:** `direction`.

### P-06 · Iraqi WMD: pre-war stockpile assertion versus post-war investigation

- **Forecast source/artifact:** US Intelligence Community, *Iraq’s Weapons of Mass Destruction Programs*, September 2002. Artifact: [`prediction.pdf`](politics-artifacts/P-06/prediction.pdf), media type `application/pdf`, file status `200`, `raw_bytes_sha256=336043a37c995baa80e4b01c0d9310fb4450fab886d2ffbc7cc785338c9b7b6a`; readable derived text artifact: [`prediction.txt`](politics-artifacts/P-06/prediction.txt), `text/plain`, `raw_bytes_sha256=5df02216a31f30d9aafee76933993895b0c6df3a618b9eb2a7d4a668426b56e1`, archive URL: <https://archive.org/details/cia-readingroom-document-0005479946>.
- **Forecast excerpt:** `Iraq has stockpiles of CW and BW agents and munitions`; TXT artifact byte range `[549,634)`; `excerpt_sha256=b5f5a0607f2cc52ac217bac6ff76d2ff0ee4660fec082371598d5dee2dbcc64b`. The PDF is scanned; the TXT is an OCR/text derivative from the same archive and must not be presented as the PDF byte hash.
- **Outcome source/artifact:** Charles A. Duelfer / Iraq Survey Group, *The Iraq Survey Group and the Search for WMD*, final report released 2004-09-30; the repository copy comes from the public CIA Reading Room archive entry (archive release/declassification metadata dated 2018-11-20), whose body discusses the post-war search. Artifact: [`outcome.pdf`](politics-artifacts/P-06/outcome.pdf), `application/pdf`, file status `200`, `raw_bytes_sha256=83d697983426fbccc5e858bde29704261e8d3ad308b3df86c4c4ce50701d80f0`; readable derived text artifact: [`outcome.txt`](politics-artifacts/P-06/outcome.txt), `text/plain`, `raw_bytes_sha256=83bd2b6c8198bde45999392d4c06b55d9401a94cc7d38b0a48477dff7262f6c5`, archive URL: <https://archive.org/details/cia-readingroom-document-05618006>.
- **Outcome excerpt:** `ISG teams found no stockpiles of weapons`; TXT artifact byte range `[11805,12061)`; `excerpt_sha256=c6f5e144394c769dfb79cebd8ac0bbb8445af77d364d3f19ba26f627e6dc077c`. OCR line breaks and hyphenation are preserved; the PDF remains the original result file, while TXT supplies stable text positioning.
- **forecast_metric:** Iraqi stockpiles of chemical/biological warfare agents and munitions; **outcome_metric:** WMD weapon stockpiles found by ISG; **unit:** binary existence claim; **population/base:** Iraqi WMD stockpiles; **forecast_date:** 2002-09-01 (report month); **outcome_date:** 2004-09-30 (Duelfer Report release; the repository copy's CIA archive metadata date is 2018-11-20); **observation_window:** pre-war assessment to ISG search report; **threshold_or_comparison_rule:** forecast asserted stockpiles existed, result reported none found; **derived/comparable_with_rule:** both compare stockpile existence, without substituting capability, intent, or activity.
- **Single classification:** `direction`.

## Stop conditions for unverified candidates

- **P-03:** Save the CRS/official outcome file in the repository with media type, publisher, title/number, date, file status, raw-byte hash, and excerpt location. A search snippet or URL is not enough. The result must establish national takeover, not substitute entry into the capital for control of the country.
- **P-05:** Save an outcome series using the forecast’s same “GDP level relative to the Remain counterfactual” metric, or an explicit reconstructable mapping to that baseline. Actual annual growth cannot replace a two-year counterfactual level difference.

## Method boundary

All four qualified cases were selected after their outcomes were known, so they are `CALIBRATION`. They can weaken rules such as “direction is stable near the event,” “vote share directly implies institutional outcome,” “a smooth baseline covers tail transmission,” and “capability/intent equals inventory,” but cannot establish cross-domain forecast accuracy. Genuine out-of-sample evidence still requires pre-registered, future-revealed judgment cards.

## Manifest

The following manifest is the shared identity index for the Chinese and English mirrors. The English mirror must use the same case IDs, statuses, artifact paths, and hashes; it must not independently change the counts:

```yaml
manifest_id: politics-calibration-2026-09-v2
candidate_ids: [P-01, P-02, P-03, P-04, P-05, P-06]
qualified_case_ids: [P-01, P-02, P-04, P-06]
unverified_case_ids: [P-03, P-05]
raw_artifacts_root: docs/evidence/politics-artifacts
count_rule: count rows whose status is exactly qualified
calibration_only: true
```
