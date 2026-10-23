#!/usr/bin/env python3
"""Recount the society-scale register's headline number, card by card.

`docs/zh|en/91-social-scale-register.md` opens with a single claim: how many
registered judgments currently clear Gate 1 *and* are permitted to be written
at society scale. That number is the whole point of the page, so it must be
re-derivable by any reader in one command rather than trusted.

The numerator has four conditions, all of which must hold:

  1. the card's diffusion-gate review field records that Gate 1 PASSES;
  2. that pass has not been revoked in place on the card itself;
  3. the card is not landscape-only (confidence is neither `低`/`Low` nor
     `低（仅图景）`/`Low (landscape only)`) -- the methodology forbids using a
     landscape-only entry as a judgment at all;
  4. the card's status is ACTIVE -- a revised or otherwise non-active card is
     not part of the current usable numerator.

Both language projections are counted separately and compared: they are two
projections of the same judgment, so a disagreement is a finding, not noise.

This script never writes anything. It checks both the card inventory and the two public register pages, and it is also called by `scripts/check.py` so a drift fails the aggregate check.

Usage:  python3 scripts/count-social-scale.py [--repo DIR] [--verbose]
Exit code: 0 when both languages agree and both pages match, 1 when they do not or a card cannot
be parsed (an unparsable card is reported, never silently skipped).
"""

import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("zh", "en")
CLOSED_IDS = ["J-%03d" % number for number in range(1, 124)]
# The last four cards exercise two different source-field boundaries: J-120 to
# J-122 are institutional/household impact surfaces whose Gate 1 field fails,
# while J-123 records a scale-axis pass but remains landscape-only.  The public
# page must keep those facts visible in their corresponding groups rather than
# merely preserving a bilingual permutation.
EXPECTED_GROUP_FOR_LATE_CARDS = {
    "J-120": 5,
    "J-121": 5,
    "J-122": 5,
    "J-123": 1,
}

# Compatibility shards: navigation stubs that re-point at the real card files.
# They hold no card headings of their own; listing them keeps the count honest
# if that ever changes (a duplicate id is reported rather than double-counted).
SHARD_DIR = "docs/%s/ledger"

FIELD = {
    "zh": {"gate": "普及闸复核", "conf": "置信度", "status": "状态"},
    "en": {"gate": "Diffusion-gate review", "conf": "Confidence",
           "status": "Status"},
}

GATE1_PASS = {
    "zh": re.compile(r"闸一\s*\*\*过\*\*"),
    "en": re.compile(r"Gate 1\s*\*\*PASS\*\*"),
}

GATE1_FAIL = {
    "zh": re.compile(r"(?:闸一[^。；]{0,24}?(\*\*不过\*\*|不过)|不能声称十亿级周频动作)"),
    "en": re.compile(r"(?:Gate 1\b[^.;]{0,30}?(\*\*FAIL\*\*|fails\b)|not a claim of a billion weekly actions)"),
}

GATE1_NOT_APPLICABLE = {
    "zh": re.compile(r"闸一不适用"),
    "en": re.compile(r"(?:Gate 1 does not apply|Not applicable)"),
}

# Some pre-existing cards encode the diffusion decision in the audience-scale
# paragraph rather than carrying a dedicated gate field. Keep that historical
# card text unchanged and derive only the same two register buckets from the
# explicit denominator wording. Unknown legacy shapes remain unparsable.
LEGACY_GATE = {
    "zh": {
        "not_applicable": re.compile(r"实际重复执行者／行为分母＝不适用"),
        "fail": re.compile(r"当前没有跨国统一分母，不能声称亿级普及"),
    },
    "en": {
        "not_applicable": re.compile(
            r"actual repeated actors/behaviour denominator = not applicable"),
        "fail": re.compile(
            r"no cross-country common denominator exists, so billion-scale diffusion is not claimed"),
    },
}

# A pass that the card itself has taken back. Matched against the whole card so
# the revocation is found wherever it was written in place.
REVOKED = {
    "zh": re.compile(r"社会级书写许可已被收回"),
    "en": re.compile(r"society-level writing licence granted by this line is "
                     r"withdrawn"),
}

LANDSCAPE_ONLY_CONFIDENCE = {
    "zh": {"低", "低（仅图景）"},
    "en": {"Low", "Low (landscape only)"},
}


def shards(lang):
    d = os.path.join(REPO, SHARD_DIR % lang)
    return [os.path.join(SHARD_DIR % lang, n) for n in sorted(os.listdir(d))
            if n.lower().endswith(".md")]


def field(body, name):
    m = re.search(r"^- \*\*%s\*\*[:：]\s*(.*)$" % re.escape(name), body, re.M)
    return m.group(1).strip() if m else None


def cards(lang):
    """Every card id -> (title, body, shard path). Duplicates are reported."""
    found, dupes = {}, []
    for path in shards(lang):
        text = open(os.path.join(REPO, path), encoding="utf-8").read()
        for block in re.split(r"\n(?=### J-\d{3})", text):
            m = re.match(r"### (J-\d{3})\s*·\s*(.*)", block)
            if not m:
                continue
            jid, title = m.group(1), m.group(2).strip()
            if jid in found:
                dupes.append((jid, path))
                continue
            found[jid] = (title, block, path)
    return found, dupes


def tally(lang, verbose):
    found, dupes = cards(lang)
    unparsable, passes, fails = [], [], []
    not_applicable = []
    revoked, landscape, inactive = [], [], []
    for jid in sorted(found):
        title, body, path = found[jid]
        gate = field(body, FIELD[lang]["gate"])
        conf = field(body, FIELD[lang]["conf"])
        status = field(body, FIELD[lang]["status"])
        if conf is None or status is None:
            unparsable.append((jid, path, "missing confidence or status field"))
            continue
        if gate is None:
            if LEGACY_GATE[lang]["not_applicable"].search(body):
                gate_kind = "not_applicable"
            elif LEGACY_GATE[lang]["fail"].search(body):
                gate_kind = "fail"
            else:
                unparsable.append((jid, path, "missing gate field"))
                continue
        elif GATE1_PASS[lang].search(gate):
            gate_kind = "pass"
        elif GATE1_FAIL[lang].search(gate):
            gate_kind = "fail"
        elif GATE1_NOT_APPLICABLE[lang].search(gate):
            gate_kind = "not_applicable"
        else:
            unparsable.append((jid, path, "no readable Gate 1 verdict"))
            continue
        if gate_kind == "pass":
            passes.append(jid)
            if REVOKED[lang].search(body):
                revoked.append(jid)
            if conf in LANDSCAPE_ONLY_CONFIDENCE[lang]:
                landscape.append(jid)
            if not status.rstrip("。.!` ").strip() == "ACTIVE":
                inactive.append(jid)
        elif gate_kind == "fail":
            fails.append(jid)
        elif gate_kind == "not_applicable":
            not_applicable.append(jid)

    usable = [j for j in passes
              if j not in revoked and j not in landscape and j not in inactive]
    print("[%s] cards parsed        : %d" % (lang, len(found)))
    print("[%s] Gate 1 FAIL         : %d" % (lang, len(fails)))
    print("[%s] Gate 1 NOT APPLICABLE: %d  %s"
          % (lang, len(not_applicable), ", ".join(not_applicable)))
    print("[%s] Gate 1 PASS         : %d  %s"
          % (lang, len(passes), ", ".join(passes)))
    print("[%s]   pass revoked      : %d  %s"
          % (lang, len(revoked), ", ".join(revoked)))
    print("[%s]   landscape-only    : %d  %s"
          % (lang, len(landscape), ", ".join(landscape)))
    print("[%s]   inactive          : %d  %s"
          % (lang, len(inactive), ", ".join(inactive)))
    print("[%s] CLEARS GATE 1 AND MAY BE WRITTEN AT SOCIETY SCALE: %d  %s"
          % (lang, len(usable), ", ".join(usable) or "(none)"))
    for jid, path, why in unparsable:
        print("[%s] UNPARSABLE %s in %s: %s" % (lang, jid, path, why))
    for jid, path in dupes:
        print("[%s] DUPLICATE %s also in %s" % (lang, jid, path))
    if verbose:
        for jid in sorted(found):
            print("[%s]   %s %s" % (lang, jid, found[jid][0]))
    print("")
    return {"total": len(found), "fail": len(fails), "not_applicable": len(not_applicable),
            "pass": len(passes), "revoked": len(revoked), "landscape": len(landscape),
            "inactive": len(inactive), "usable": len(usable),
            "pass_ids": passes, "usable_ids": usable,
            "revoked_ids": revoked, "landscape_ids": landscape,
            "inactive_ids": inactive, "all_ids": sorted(found),
            "broken": len(unparsable) + len(dupes)}


def check_page(lang, counts):
    path = os.path.join(REPO, "docs", lang, "91-social-scale-register.md")
    text = open(path, encoding="utf-8").read()
    section_start = r"^## 四、" if lang == "zh" else r"^## 4\."
    section_end = r"^## 五、" if lang == "zh" else r"^## 5\."
    section_match = re.search(section_start + r"[\s\S]*?(?=" + section_end + r")", text, re.M)
    page_ids = re.findall(r"^\| \[(J-\d{3})\b", section_match.group(0), re.M) if section_match else []
    raw_links = dict(re.findall(r"^\| \[(J-\d{3})[^\]]*\]\(([^)]+)\)",
                              section_match.group(0), re.M)) if section_match else {}
    checks = []
    page_links = {}
    for jid, href in raw_links.items():
        anchor_match = re.search(r"^([^#]+)#(j-\d{3})--", href)
        if not anchor_match:
            checks.append(("%s link" % jid, "a ledger href with a card anchor"))
            page_links[jid] = (href, "invalid")
        else:
            page_links[jid] = (anchor_match.group(1), anchor_match.group(2).upper())
            if anchor_match.group(2).upper() != jid:
                checks.append(("%s link" % jid, "an anchor for the displayed card"))
    expected_ids = CLOSED_IDS
    group_ids = []
    if Counter(counts["all_ids"]) != Counter(CLOSED_IDS):
        checks.append(("closed ledger set", "J-001 through J-123 exactly once"))
    if not section_match:
        checks.append(("section 4", section_start))
    elif Counter(page_ids) != Counter(expected_ids):
        checks.append(("section 4 card set", "expected each ledger card exactly once"))
    group_heading = r"^### 第[零一二三四五六]组[^\n]*" if lang == "zh" else r"^### Group [0-6][^\n]*"
    group_matches = list(re.finditer(group_heading, section_match.group(0), re.M)) if section_match else []
    group_count = len(group_matches)
    if group_count != 7:
        checks.append(("section 4 group headings", "seven groups"))
    elif section_match:
        group_bodies = []
        section_text = section_match.group(0)
        group_ids = []
        for index, heading in enumerate(group_matches):
            end = group_matches[index + 1].start() if index + 1 < group_count else len(section_text)
            body = section_text[heading.end():end]
            ids = re.findall(r"^\| \[(J-\d{3})\b", body, re.M)
            group_bodies.append(body)
            group_ids.append(ids)
            number_match = re.search(r"\((\d+)(?: 条)?\)\s*$", heading.group(0))
            if number_match is None:
                number_match = re.search(r"[,，]\s*(\d+)(?: 条)?\)\s*$", heading.group(0))
            if number_match is None or int(number_match.group(1)) != len(ids):
                checks.append(("group heading count", heading.group(0)))
        group0_ids = group_ids[0]
        group1_ids = group_ids[1]
        group2_ids = group_ids[2]
        expected_group2 = sorted(set(counts["revoked_ids"]) - set(counts["landscape_ids"]))
        if Counter(group0_ids) != Counter(counts["usable_ids"]):
            checks.append(("group 0 members", "the usable card set"))
        if Counter(group1_ids) != Counter(counts["landscape_ids"]):
            checks.append(("group 1 members", "the landscape-only PASS set"))
        if Counter(group2_ids) != Counter(expected_group2):
            checks.append(("group 2 members", "the revoked PASS set"))
        # Keep the late additions tied to their ledger facts.  This is a
        # deliberately small semantic cross-check: it catches a page that
        # preserves totals and bilingual parity while moving one card to a
        # plausible but wrong group.
        for jid, expected_group in EXPECTED_GROUP_FOR_LATE_CARDS.items():
            actual_groups = [index for index, ids in enumerate(group_ids)
                             if jid in ids]
            if actual_groups != [expected_group]:
                checks.append(("%s group" % jid,
                               "ledger-derived group %d" % expected_group))
    if lang == "zh":
        pass_members = "、".join("`%s`" % jid for jid in counts["pass_ids"])
        usable_members = "、".join("`%s`" % jid for jid in counts["usable_ids"])
        checks += [
            ("headline total", r"全库 %d 张在册判断卡" % counts["total"]),
            ("result total", r"全库 %d 张卡" % counts["total"]),
            ("group total", r"其余 %d 张按" % (counts["total"] - 1)),
            ("FAIL row", r"\| 「普及闸复核」写「闸一\*\*不过\*\*」 \| \*\*%d\*\* \|" % counts["fail"]),
            ("not-applicable row", r"\| 「普及闸复核」写「闸一不适用」 \| \*\*%d\*\* \|" % counts["not_applicable"]),
            ("PASS row", r"\| 「普及闸复核」写「闸一\*\*过\*\*」 \| \*\*%d\*\* \|.*%s" % (counts["pass"], re.escape(pass_members))),
            ("usable row", r"\| \*\*已过闸一且可作社会级书写的判断\*\* \| \*\*%d\*\* \|.*%s" % (counts["usable"], re.escape(usable_members))),
            ("J-108 listing", r"J-108"),
        ]
    else:
        pass_members = ", ".join("`%s`" % jid for jid in counts["pass_ids"])
        usable_members = ", ".join("`%s`" % jid for jid in counts["usable_ids"])
        checks += [
            ("headline total", r"all %d registered judgment cards" % counts["total"]),
            ("result total", r"all %d cards" % counts["total"]),
            ("group total", r"the other %d are in six groups" % (counts["total"] - 1)),
            ("FAIL row", r'\| "Diffusion-gate review" records Gate 1 \*\*FAIL\*\* \| \*\*%d\*\* \|' % counts["fail"]),
            ("not-applicable row", r'\| "Diffusion-gate review" records Gate 1 \*\*not applicable\*\* \| \*\*%d\*\* \|' % counts["not_applicable"]),
            ("PASS row", r'\| "Diffusion-gate review" records Gate 1 \*\*PASS\*\* \| \*\*%d\*\* \|.*%s' % (counts["pass"], re.escape(pass_members))),
            ("usable row", r"\| \*\*Judgments clearing Gate 1 and permitted to be written at society scale\*\* \| \*\*%d\*\* \|.*%s" % (counts["usable"], re.escape(usable_members))),
            ("J-108 listing", r"J-108"),
        ]
    failures = []
    for label, pattern in checks:
        if not re.search(pattern, text):
            failures.append((path, label, pattern))
    return failures, group_ids, page_links


def main():
    global REPO
    args = list(sys.argv[1:])
    verbose = False
    while args:
        arg = args.pop(0)
        if arg == "--verbose":
            verbose = True
        elif arg == "--repo" and args:
            REPO = os.path.abspath(args.pop(0))
        else:
            print("unknown argument: %s" % arg)
            return 2
    out = {lang: tally(lang, verbose) for lang in LANGS}
    ok = True
    for key in ("total", "fail", "not_applicable", "pass", "revoked", "landscape", "inactive", "usable"):
        if out["zh"][key] != out["en"][key]:
            print("MISMATCH %s: zh %d vs en %d"
                  % (key, out["zh"][key], out["en"][key]))
            ok = False
    page_groups = {}
    page_links = {}
    for lang in LANGS:
        failures, groups, links = check_page(lang, out[lang])
        page_groups[lang] = groups
        page_links[lang] = links
        for path, label, pattern in failures:
            print("PAGE MISMATCH [%s] %s in %s: %s"
                  % (lang, label, path, pattern))
            ok = False
    if page_groups["zh"] != page_groups["en"]:
        print("PAGE MISMATCH: Chinese and English group membership differs")
        ok = False
    if page_links["zh"] != page_links["en"]:
        print("PAGE MISMATCH: Chinese and English card links differ")
        ok = False
    if out["zh"]["broken"] or out["en"]["broken"]:
        ok = False
    if ok:
        print("both language projections agree; headline number = %d"
              % out["zh"]["usable"])
        return 0
    print("the two projections disagree, or a card could not be read -- the "
          "page's headline number is not currently re-derivable")
    return 1


if __name__ == "__main__":
    sys.exit(main())
