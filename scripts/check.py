#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-publication checks for this repository.

Runs the machine-checkable half of the pre-publication checklist in
`docs/{zh,en}/90-ledger.md` section 10. The remaining items in that list are
judgment calls a script cannot make (whether a falsifier is sharp enough,
whether an "Against consensus" paragraph really carries its three elements)
and stay manual.

Usage:  python3 scripts/check.py
Exit:   0 = all checks pass, 1 = at least one failure (details on stdout)

No dependencies beyond the standard library, and it reads the tree only.
"""

import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("zh", "en")
# The dependency graph uses a full-width arrow in Chinese and ASCII in English.
GRAPH_ARROW = {"zh": u"\u2190", "en": "<-"}
CONFIDENCE = {
    "zh": {u"\u9ad8", u"\u4e2d", u"\u4f4e"},
    "en": {"high", "medium", "low"},
}
CARD_FIELDS = {
    "zh": [u"\u63d0\u51fa\u65e5\u671f", u"\u4e00\u53e5\u8bdd\u5224\u65ad", u"\u900f\u955c",
           u"\u63a8\u7406\u94fe", u"\u65f6\u95f4\u7a97", u"\u8bc1\u4f2a\u6761\u4ef6",
           u"\u9886\u5148\u6307\u6807", u"\u7f6e\u4fe1\u5ea6", u"depends-on",
           u"\u6700\u5f3a\u53cd\u65b9", u"\u4e0e\u5171\u8bc6", u"\u5916\u90e8\u5bf9\u7167\u6765\u6e90",
           u"\u51fa\u5904", u"\u4e0b\u6b21\u68c0\u67e5\u65e5", u"\u72b6\u6001"],
    "en": ["Proposed date", "One-sentence judgment", "Lens", "Reasoning chain",
           "Time window", "Falsifier", "Leading indicator", "Confidence", "depends-on",
           "Strongest opposing mechanism", "Against consensus",
           "External comparison source", "Source", "Next review", "Status"],
}

failures = []


def fail(check, detail):
    failures.append((check, detail))


def read(path):
    return io.open(os.path.join(REPO, path), encoding="utf-8").read()


def slug(title):
    """Reproduce GitHub's heading-anchor rule.

    Lowercase, drop everything that is not alphanumeric / hyphen / underscore
    (CJK is alphanumeric and survives), turn spaces into hyphens. Runs of
    hyphens are NOT collapsed: `J-001 - Title` yields `j-001---title`, and a
    checker that collapses them reports hundreds of false positives.
    """
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", title.strip())  # links -> text
    t = re.sub(r"[`*_]", "", t).lower()
    return "".join("-" if c == " " else c
                   for c in t if c == " " or c.isalnum() or c in "-_")


def markdown_files():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO, "docs")):
        for f in sorted(files):
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(root, f), REPO))
    for f in ("README.md", "README.en.md"):
        if os.path.exists(os.path.join(REPO, f)):
            out.append(f)
    return out


def check_links(files):
    """Every relative link resolves, and every anchor matches a real heading."""
    anchors = {}
    for f in files:
        seen, found = {}, set()
        for m in re.finditer(r"^#{1,6}\s+(.*)$", read(f), re.M):
            s = slug(m.group(1))
            n = seen.get(s, 0)
            seen[s] = n + 1
            found.add(s if n == 0 else "%s-%d" % (s, n))
        anchors[f] = found
    total = 0
    for f in files:
        base = os.path.dirname(f)
        for m in re.finditer(r"\]\(([^)\s]+)\)", read(f)):
            link = m.group(1)
            if link.startswith("http") or link.startswith("mailto"):
                continue
            total += 1
            path, _, anchor = link.partition("#")
            target = os.path.normpath(os.path.join(base, path)) if path else f
            if path and not os.path.exists(os.path.join(REPO, target)):
                fail("links", "%s -> %s (file missing)" % (f, link))
                continue
            if anchor and target in anchors and anchor not in anchors[target]:
                fail("links", "%s -> %s (no such heading)" % (f, link))
    return total


def parse_ledger(lang):
    text = read("docs/%s/90-ledger.md" % lang)
    cards = {}
    parts = re.split(r"^### (J-\d{3})", text, flags=re.M)
    for i in range(1, len(parts), 2):
        cards[parts[i]] = parts[i + 1]
    graph = {}
    pattern = r"^(J-\d{3})\s*%s\s*([^\n]*)$" % re.escape(GRAPH_ARROW[lang])
    for m in re.finditer(pattern, text, re.M):
        graph[m.group(1)] = set(re.findall(r"J-\d{3}", m.group(2)))
    overview = {}
    for line in text.split("\n"):
        m = re.match(r"^\|\s*\[(J-\d{3})\]\([^)]*\)\s*\|", line)
        if not m:
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 8:
            continue
        overview.setdefault(m.group(1), set(re.findall(r"J-\d{3}", cols[6])))
    overview_consensus = {}
    for line in text.split("\n"):
        m = re.match(r"^\|\s*\[(J-\d{3})\]\([^)]*\)\s*\|", line)
        if not m:
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 10:
            continue
        overview_consensus.setdefault(m.group(1), cols[8])
    return cards, graph, overview, overview_consensus


# A judgment may legitimately carry no external comparison yet, but then it must
# say so in BOTH places. The failure this catches is a card whose body records a
# completed comparison while the overview table still reads "unknown" (or the
# reverse) — two statements of the same fact drifting apart.
UNCOMPARED = {
    "zh": u"\u672c\u8f6e\u672a\u5b8c\u6210\u5916\u90e8\u5bf9\u7167",
    "en": "not completed this round",
}
CONSENSUS_FIELD = {"zh": u"\u4e0e\u5171\u8bc6", "en": "Against consensus"}
SOURCE_FIELD = {"zh": u"\u5916\u90e8\u5bf9\u7167\u6765\u6e90",
                "en": "External comparison source"}


def check_comparison(lang, cards, overview_consensus):
    text = read("docs/%s/90-ledger.md" % lang)
    defined = set(re.findall(r"^- \*\*(EXT-\d+)\*\*", text, re.M))
    marker = UNCOMPARED[lang]
    for jid in sorted(cards):
        body = cards[jid]
        m = re.search(r"\*\*%s\*\*[:\uff1a]\s*([^\n]*)" % CONSENSUS_FIELD[lang], body)
        card_uncompared = bool(m) and marker in m.group(1)
        row = overview_consensus.get(jid)
        if row is None:
            fail("overview-consensus", "%s %s: no overview row carrying a consensus column"
                 % (lang, jid))
            continue
        if card_uncompared != (marker in row):
            fail("consensus-drift",
                 "%s %s: card says %s, overview says %s"
                 % (lang, jid,
                    "not compared" if card_uncompared else "compared",
                    "not compared" if marker in row else "compared"))
        src = re.search(r"\*\*%s\*\*[:\uff1a]\s*([^\n]*)" % SOURCE_FIELD[lang], body)
        cited = set(re.findall(r"EXT-\d+", src.group(1))) if src else set()
        if not card_uncompared and not cited:
            fail("comparison-source",
                 "%s %s: comparison is recorded as done but cites no EXT source"
                 % (lang, jid))
        for ext in sorted(cited - defined):
            fail("comparison-source",
                 "%s %s cites %s, which the source index does not define"
                 % (lang, jid, ext))


def check_ledger(lang):
    cards, graph, overview, overview_consensus = parse_ledger(lang)
    if not cards:
        fail("ledger", "%s: no judgment cards found" % lang)
        return cards
    for jid in sorted(cards):
        body = cards[jid]
        missing = [f for f in CARD_FIELDS[lang]
                   if ("**%s**" % f) not in body]
        if missing:
            fail("card-fields", "%s %s missing %s" % (lang, jid, ", ".join(missing)))
        m = re.search(r"\*\*(?:Confidence|\u7f6e\u4fe1\u5ea6)\*\*[:\uff1a]\s*([^\n\u3002.(\uff08]*)",
                      body)
        if m:
            value = m.group(1).strip().lower()
            if not any(v in value for v in CONFIDENCE[lang]):
                fail("confidence", "%s %s: %r outside the whitelist" % (lang, jid, value))
        declared = set(re.findall(r"J-\d{3}",
                       (re.search(r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", body)
                        or re.match("", "")).group(1) if re.search(
                           r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", body) else ""))
        for dep in declared:
            if dep not in cards:
                fail("depends-on", "%s %s depends on %s, which has no card" % (lang, jid, dep))
        if jid == min(cards):
            continue  # root card carries no edge in the graph
        if declared != graph.get(jid, set()):
            fail("dep-graph", "%s %s: card %s vs graph %s"
                 % (lang, jid, sorted(declared), sorted(graph.get(jid, set()))))
        if declared != overview.get(jid, set()):
            fail("dep-overview", "%s %s: card %s vs overview %s"
                 % (lang, jid, sorted(declared), sorted(overview.get(jid, set()))))
    check_comparison(lang, cards, overview_consensus)
    return cards


def check_parity(per_lang_cards):
    names = {}
    for lang in LANGS:
        root = os.path.join(REPO, "docs", lang)
        found = set()
        for r, _d, fs in os.walk(root):
            for f in fs:
                if f.endswith(".md"):
                    found.add(os.path.relpath(os.path.join(r, f), root))
        names[lang] = found
    only_zh = names["zh"] - names["en"]
    only_en = names["en"] - names["zh"]
    if only_zh or only_en:
        fail("bilingual-files", "zh-only %s / en-only %s"
             % (sorted(only_zh), sorted(only_en)))
    if set(per_lang_cards["zh"]) != set(per_lang_cards["en"]):
        diff = set(per_lang_cards["zh"]) ^ set(per_lang_cards["en"])
        fail("bilingual-cards", "judgment IDs present in one language only: %s"
             % sorted(diff))
    for name in sorted(names["zh"] & names["en"]):
        h = {}
        for lang in LANGS:
            h[lang] = len(re.findall(r"^##\s", read("docs/%s/%s" % (lang, name)), re.M))
        if h["zh"] != h["en"]:
            fail("bilingual-sections", "docs/*/%s: zh has %d sections, en has %d"
                 % (name, h["zh"], h["en"]))


def main():
    files = markdown_files()
    links = check_links(files)
    cards = {lang: check_ledger(lang) for lang in LANGS}
    check_parity(cards)

    print("files checked      : %d" % len(files))
    print("internal links     : %d" % links)
    print("judgment cards     : zh %d / en %d" % (len(cards["zh"]), len(cards["en"])))
    if failures:
        print("\nFAILED (%d):" % len(failures))
        for check, detail in failures:
            print("  [%s] %s" % (check, detail))
        return 1
    print("\nall automated pre-publication checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
