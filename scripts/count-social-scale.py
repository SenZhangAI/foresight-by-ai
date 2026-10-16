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

This script never writes anything. It is deliberately NOT wired into
`scripts/check.py`: it reports the count and checks the two public register pages,
but it does not gate a commit.

Usage:  python3 scripts/count-social-scale.py [--verbose]
Exit code: 0 when both languages agree, 1 when they do not or a card cannot
be parsed (an unparsable card is reported, never silently skipped).
"""

import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("zh", "en")

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
    "zh": re.compile(r"闸一[^。；]{0,24}?(\*\*不过\*\*|不过)"),
    "en": re.compile(r"Gate 1\b[^.;]{0,30}?(\*\*FAIL\*\*|fails\b)"),
}

GATE1_NOT_APPLICABLE = {
    "zh": re.compile(r"闸一不适用"),
    "en": re.compile(r"Gate 1 does not apply"),
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
        if gate is None or conf is None or status is None:
            unparsable.append((jid, path, "missing gate, confidence or status field"))
            continue
        if GATE1_PASS[lang].search(gate):
            passes.append(jid)
            if REVOKED[lang].search(body):
                revoked.append(jid)
            if conf in LANDSCAPE_ONLY_CONFIDENCE[lang]:
                landscape.append(jid)
            if not status.rstrip("。.!` ").strip() == "ACTIVE":
                inactive.append(jid)
        elif GATE1_FAIL[lang].search(gate):
            fails.append(jid)
        elif GATE1_NOT_APPLICABLE[lang].search(gate):
            not_applicable.append(jid)
        else:
            unparsable.append((jid, path, "no readable Gate 1 verdict"))

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
            "all_ids": sorted(found),
            "broken": len(unparsable) + len(dupes)}


def check_page(lang, counts):
    path = os.path.join(REPO, "docs", lang, "91-social-scale-register.md")
    text = open(path, encoding="utf-8").read()
    section_start = r"^## 四、" if lang == "zh" else r"^## 4\."
    section_end = r"^## 五、" if lang == "zh" else r"^## 5\."
    section_match = re.search(section_start + r"[\s\S]*?(?=" + section_end + r")", text, re.M)
    page_ids = re.findall(r"^\| \[(J-\d{3})\b", section_match.group(0), re.M) if section_match else []
    expected_ids = counts["all_ids"]
    checks = []
    if not section_match:
        checks.append(("section 4", section_start))
    elif Counter(page_ids) != Counter(expected_ids):
        checks.append(("section 4 card set", "expected each ledger card exactly once"))
    group_heading = r"^### 第[零一二三四五六]组" if lang == "zh" else r"^### Group [0-6]"
    group_count = len(re.findall(group_heading, section_match.group(0), re.M)) if section_match else 0
    if group_count != 7:
        checks.append(("section 4 group headings", "seven groups"))
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
    return failures


def main():
    verbose = "--verbose" in sys.argv
    out = {lang: tally(lang, verbose) for lang in LANGS}
    ok = True
    for key in ("total", "fail", "not_applicable", "pass", "revoked", "landscape", "inactive", "usable"):
        if out["zh"][key] != out["en"][key]:
            print("MISMATCH %s: zh %d vs en %d"
                  % (key, out["zh"][key], out["en"][key]))
            ok = False
    for lang in LANGS:
        for path, label, pattern in check_page(lang, out[lang]):
            print("PAGE MISMATCH [%s] %s in %s: %s"
                  % (lang, label, path, pattern))
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
