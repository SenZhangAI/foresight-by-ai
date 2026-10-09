#!/usr/bin/env python3
"""Recount the society-scale register's headline number, card by card.

`docs/zh|en/91-social-scale-register.md` opens with a single claim: how many
registered judgments currently clear Gate 1 *and* are permitted to be written
at society scale. That number is the whole point of the page, so it must be
re-derivable by any reader in one command rather than trusted.

The numerator has three conditions, all of which must hold:

  1. the card's diffusion-gate review field records that Gate 1 PASSES;
  2. that pass has not been revoked in place on the card itself;
  3. the card is not landscape-only (confidence is neither `低`/`Low` nor
     `低（仅图景）`/`Low (landscape only)`) -- the methodology forbids using a
     landscape-only entry as a judgment at all.

Both language projections are counted separately and compared: they are two
projections of the same judgment, so a disagreement is a finding, not noise.

This script never writes anything. It is deliberately NOT wired into
`scripts/check.py`: it reports a number, it does not gate a commit.

Usage:  python3 scripts/count-social-scale.py [--verbose]
Exit code: 0 when both languages agree, 1 when they do not or a card cannot
be parsed (an unparsable card is reported, never silently skipped).
"""

import os
import re
import sys

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
    revoked, landscape = [], []
    for jid in sorted(found):
        title, body, path = found[jid]
        gate = field(body, FIELD[lang]["gate"])
        conf = field(body, FIELD[lang]["conf"])
        if gate is None or conf is None:
            unparsable.append((jid, path, "missing gate or confidence field"))
            continue
        if GATE1_PASS[lang].search(gate):
            passes.append(jid)
            if REVOKED[lang].search(body):
                revoked.append(jid)
            if conf in LANDSCAPE_ONLY_CONFIDENCE[lang]:
                landscape.append(jid)
        elif GATE1_FAIL[lang].search(gate):
            fails.append(jid)
        else:
            unparsable.append((jid, path, "no readable Gate 1 verdict"))

    usable = [j for j in passes
              if j not in revoked and j not in landscape]
    print("[%s] cards parsed        : %d" % (lang, len(found)))
    print("[%s] Gate 1 FAIL         : %d" % (lang, len(fails)))
    print("[%s] Gate 1 PASS         : %d  %s"
          % (lang, len(passes), ", ".join(passes)))
    print("[%s]   pass revoked      : %d  %s"
          % (lang, len(revoked), ", ".join(revoked)))
    print("[%s]   landscape-only    : %d  %s"
          % (lang, len(landscape), ", ".join(landscape)))
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
    return {"total": len(found), "fail": len(fails), "pass": len(passes),
            "revoked": len(revoked), "landscape": len(landscape),
            "usable": len(usable), "broken": len(unparsable) + len(dupes)}


def main():
    verbose = "--verbose" in sys.argv
    out = {lang: tally(lang, verbose) for lang in LANGS}
    ok = True
    for key in ("total", "fail", "pass", "revoked", "landscape", "usable"):
        if out["zh"][key] != out["en"][key]:
            print("MISMATCH %s: zh %d vs en %d"
                  % (key, out["zh"][key], out["en"][key]))
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
