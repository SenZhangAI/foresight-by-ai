#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-publication checks for this repository.

Runs the machine-checkable half of the pre-publication checklist in
`docs/{zh,en}/90-ledger.md` section 10. The remaining items in that list are
judgment calls a script cannot make (whether a falsifier is sharp enough,
whether an "Against consensus" paragraph really carries its three elements)
and stay manual.

Usage:  python3 scripts/check.py              check this repository
        python3 scripts/check.py --repo DIR   check another copy of the tree
        python3 scripts/check.py --self-test  run the negative cases (see below)
Exit:   0 = all checks pass, 1 = at least one failure (details on stdout)

No dependencies beyond the standard library. The checks read the tree only;
`--self-test` writes solely into a temporary directory it then deletes.
"""

import io
import itertools
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("zh", "en")
# The dependency graph uses a full-width arrow in Chinese and ASCII in English.
GRAPH_ARROW = {"zh": u"\u2190", "en": "<-"}
CONFIDENCE = {
    "zh": {u"\u9ad8", u"\u4e2d", u"\u4f4e"},
    "en": {"high", "medium", "low"},
}
CONFIDENCE_FIELD = {"zh": u"\u7f6e\u4fe1\u5ea6", "en": "Confidence"}
# The WHOLE field value is read, up to end of line. Truncating it at the first
# `。` / `.` / `(` / `（` — which is what this used to do — meant only a prefix
# was ever compared, so `中（偏高）` and `Medium (leaning high).` passed while
# the bare `中高` was caught: the same invented grade, waved through by writing
# it in brackets.
CONFIDENCE_VALUE = (r"\*\*(?:Confidence|\u7f6e\u4fe1\u5ea6)\*\*[:\uff1a]"
                    r"\s*([^\n]*)")
# A value may carry exactly one qualifier, and only the standing one: the
# ledger marks low-confidence judgments as landscape-only. Anything else in the
# brackets is a grade the whitelist does not define.
CONFIDENCE_QUALIFIER = {"zh": {u"\u4ec5\u56fe\u666f"}, "en": {"landscape only"}}
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
        body = parts[i + 1]
        # A card ends at the next top-level section. Without this the LAST
        # card's body runs to end of file and swallows whatever follows it
        # (section 10 today), so that text would be checked — and reported —
        # as if it belonged to the card.
        end = re.search(r"^## ", body, re.M)
        cards[parts[i]] = body[:end.start()] if end else body
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


def allowed_confidence(lang):
    """Human-readable description of the values this check accepts."""
    grades = " / ".join(sorted(CONFIDENCE[lang]))
    quals = " / ".join(sorted(CONFIDENCE_QUALIFIER[lang]))
    return "%s, optionally followed by (%s)" % (grades, quals)


def confidence_is_whitelisted(lang, raw):
    """True when the whole field value states a whitelisted grade.

    Accepts `低`, `Low.`, `低（仅图景）。`, `Low (landscape only).` — a grade,
    an optional trailing sentence period, and at most the one standing
    qualifier. It rejects `中高`, `极高`, `very high` and, since the value is
    read whole rather than up to the first bracket, `中（偏高）` as well: a
    bracket is not a place to smuggle a grade the whitelist does not define.
    """
    value = raw.strip().rstrip(u"\u3002.").strip()
    m = re.match(u"^([^(\uff08]*)[(\uff08]([^)\uff09]*)[)\uff09]$", value)
    if m:
        if m.group(2).strip().lower() not in CONFIDENCE_QUALIFIER[lang]:
            return False
        value = m.group(1).strip()
    return value.lower() in CONFIDENCE[lang]


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
        # Exact membership over the WHOLE value, never substring over a prefix.
        # `极高` contains `高` and `very high` contains `high`, so a substring
        # test passes every positive case while letting through exactly the
        # invented grades this check exists to catch; truncating the value at
        # the first bracket let the same grades back in as `中（偏高）`. Every
        # occurrence in the card is tested, not only the first, and a field
        # whose value cannot be read is a failure rather than a silent skip.
        found = list(re.finditer(CONFIDENCE_VALUE, body))
        if not found and any(("**%s**" % CONFIDENCE_FIELD[l]) in body
                             for l in LANGS):
            fail("confidence",
                 "%s %s: confidence field present but no value could be read"
                 % (lang, jid))
        for m in found:
            if not confidence_is_whitelisted(lang, m.group(1)):
                fail("confidence", "%s %s: %r is not %s"
                     % (lang, jid, m.group(1).strip(), allowed_confidence(lang)))
        declared = set(re.findall(r"J-\d{3}",
                       (re.search(r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", body)
                        or re.match("", "")).group(1) if re.search(
                           r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", body) else ""))
        for dep in declared:
            if dep not in cards:
                fail("depends-on", "%s %s depends on %s, which has no card" % (lang, jid, dep))
        # The root card is NOT exempt: it carries no edge in the graph, which
        # is exactly the claim `declared == graph.get(jid, set())` makes when
        # both are empty. Skipping it let the root declare an upstream that
        # neither the graph nor the overview knows about.
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


def run_checks():
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


# ---------------------------------------------------------------------------
# Self-test: the negative cases, as something that can be re-run.
#
# A checker earns its exit code only if a deliberate breakage makes it fail.
# `--self-test` copies the checkable surface into a temporary directory, breaks
# that copy one way at a time, and asserts the checker exits non-zero *for the
# expected reason* (the check tag must appear in the output, so a breakage that
# happens to trip some other check does not count as caught).
#
# This exists because a claim of "verified against four deliberate breakages"
# left nothing re-runnable behind, and one of the four silently did not work:
# the confidence whitelist compared by substring, so `极高` — which contains
# `高` — passed. Positive cases stayed green throughout.
#
# The repository itself is never modified; every write lands in the temporary
# copy, which is deleted afterwards.
# ---------------------------------------------------------------------------

def _copy_checkable_tree(dst):
    """Copy exactly what the checks read: docs/ plus the top-level READMEs."""
    shutil.copytree(os.path.join(REPO, "docs"), os.path.join(dst, "docs"))
    for name in ("README.md", "README.en.md"):
        src = os.path.join(REPO, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dst, name))
    return dst


def _run_checker(root):
    proc = subprocess.Popen(
        [sys.executable, os.path.abspath(__file__), "--repo", root],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _ = proc.communicate()
    return proc.returncode, out.decode("utf-8", "replace")


def _ledger(root, lang):
    return os.path.join(root, "docs", lang, "90-ledger.md")


def _read_file(path):
    return io.open(path, encoding="utf-8").read()


def _write_file(path, text):
    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _first_card(text):
    """(offset, id) of the first card IN FILE ORDER.

    The ledger is not sorted by id — today the file opens with J-043 — so this
    is deliberately not the same card as `min(ids)`, which is the one the
    dependency comparison used to exempt.
    """
    m = re.search(r"^### (J-\d{3})", text, re.M)
    if not m:
        raise AssertionError("fixture carries no judgment card")
    return m.start(), m.group(1)


def _last_card(text):
    """(start, end, id) of the last card; end is the next `## ` or EOF."""
    ms = list(re.finditer(r"^### (J-\d{3})", text, re.M))
    if not ms:
        raise AssertionError("fixture carries no judgment card")
    m = ms[-1]
    nxt = text.find("\n## ", m.end())
    return m.start(), (len(text) if nxt == -1 else nxt + 1), m.group(1)


def _break_dangling_anchor(root):
    path = _ledger(root, "zh")
    text = _read_file(path)
    m = re.search(r"\]\(#([^)\s]+)\)", text)
    if not m:
        raise AssertionError("fixture carries no in-file anchor link")
    _write_file(path, text[:m.start(1)] + "no-such-heading-" + m.group(1)
                + text[m.end(1):])
    return u"zh ledger: first anchor link now points at #no-such-heading-…"


def _break_dep_edge(root):
    path = _ledger(root, "zh")
    text = _read_file(path)
    start, _end, jid = _last_card(text)
    m = re.search(r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", text[start:])
    if not m or not re.search(r"J-\d{3}", m.group(1)):
        raise AssertionError("the last zh card declares no dependency to drop")
    _write_file(path, text[:start + m.start(1)] + u"\u2014\u3002"
                + text[start + m.end(1):])
    return (u"zh %s: card declares no depends-on while the graph and the "
            u"overview still carry the edge" % jid)


def _break_root_dep_edge(root):
    """The root card — `min(ids)` — used to be exempt from both comparisons.

    It must be located by id, not by position: the ledger opens with J-043,
    and mutating that card would exercise the ordinary path and pass whether
    or not the exemption is still there.
    """
    path = _ledger(root, "zh")
    text = _read_file(path)
    ids = re.findall(r"^### (J-\d{3})", text, re.M)
    if len(ids) < 2:
        raise AssertionError("fixture needs at least two cards")
    root_id = min(ids)
    borrowed = min(i for i in ids if i != root_id)
    head = re.search(r"^### %s\b" % root_id, text, re.M).start()
    m = re.search(r"^- \*\*depends-on\*\*[:\uff1a][^\n]*$", text[head:], re.M)
    if not m:
        raise AssertionError("root card %s carries no depends-on line" % root_id)
    if re.search(r"J-\d{3}", m.group(0)):
        raise AssertionError("root card %s already declares an upstream, so "
                             "this fixture proves nothing" % root_id)
    line = u"- **depends-on**\uff1a%s\u3002" % borrowed
    _write_file(path, text[:head + m.start()] + line + text[head + m.end():])
    return (u"zh %s (lowest id, the exempted card): declares %s while the "
            u"graph and the overview give it no upstream" % (root_id, borrowed))


def _break_single_language_card(root):
    path = _ledger(root, "en")
    text = _read_file(path)
    start, end, jid = _last_card(text)
    _write_file(path, text[:start] + text[end:])
    return u"en ledger: card %s removed, zh still carries it" % jid


def _break_missing_field(root):
    path = _ledger(root, "zh")
    text = _read_file(path)
    head, jid = _first_card(text)
    field = u"\u8bc1\u4f2a\u6761\u4ef6"  # 证伪条件
    m = re.search(r"^- \*\*%s\*\*[:\uff1a][^\n]*\n" % re.escape(field),
                  text[head:], re.M)
    if not m:
        raise AssertionError("zh %s carries no %s line" % (jid, field))
    _write_file(path, text[:head + m.start()] + text[head + m.end():])
    return u"zh %s: the %s line is gone" % (jid, field)


def _set_confidence(lang, value):
    """Rewrite the first card's confidence value in `lang` to `value`."""
    field = CONFIDENCE_FIELD[lang]
    sep = u"\uff1a" if lang == "zh" else ": "

    def mutate(root):
        path = _ledger(root, lang)
        text = _read_file(path)
        head, jid = _first_card(text)
        m = re.search(r"^- \*\*%s\*\*[:\uff1a][^\n]*$" % re.escape(field),
                      text[head:], re.M)
        if not m:
            raise AssertionError("%s %s carries no %s line"
                                 % (lang, jid, field))
        line = u"- **%s**%s%s" % (field, sep, value)
        _write_file(path, text[:head + m.start()] + line
                    + text[head + m.end():])
        if line not in _read_file(path):
            raise AssertionError("confidence fixture was not applied")
        return u"%s %s: confidence = %s" % (lang, jid, value)

    return mutate


def _break_second_confidence(root):
    """A card whose FIRST confidence value is fine and second is not."""
    path = _ledger(root, "zh")
    text = _read_file(path)
    head, jid = _first_card(text)
    field = CONFIDENCE_FIELD["zh"]
    m = re.search(r"^- \*\*%s\*\*[:\uff1a][^\n]*\n" % re.escape(field),
                  text[head:], re.M)
    if not m:
        raise AssertionError("zh %s carries no %s line" % (jid, field))
    extra = u"- **%s**\uff1a\u6781\u9ad8\n" % field  # 极高
    _write_file(path, text[:head + m.end()] + extra + text[head + m.end():])
    return (u"zh %s: a second confidence line, 极高, below a valid one"
            % jid)


def _break_unreadable_confidence(root):
    """Field present, value unreachable: the check must not silently skip."""
    path = _ledger(root, "zh")
    text = _read_file(path)
    head, jid = _first_card(text)
    field = CONFIDENCE_FIELD["zh"]
    m = re.search(r"^- \*\*%s\*\*[:\uff1a][^\n]*$" % re.escape(field),
                  text[head:], re.M)
    if not m:
        raise AssertionError("zh %s carries no %s line" % (jid, field))
    line = u"- **%s** \u6781\u9ad8" % field  # no separator after the field
    _write_file(path, text[:head + m.start()] + line + text[head + m.end():])
    return (u"zh %s: `- **置信度** 极高` — field present, no separator"
            % jid)


def _text_after_last_card(root):
    """Not a breakage: prose BELOW the last card belongs to no card.

    The card body used to run to end of file, so a confidence example in the
    checklist section was read as if J-064 had written it.
    """
    path = _ledger(root, "zh")
    text = _read_file(path)
    _start, end, _jid = _last_card(text)
    if end >= len(text):
        raise AssertionError("fixture has no section after the last card")
    nl = text.find("\n", end)
    if nl == -1:
        raise AssertionError("section after the last card has no body")
    extra = u"\n- **%s**\uff1a\u6781\u9ad8\n" % CONFIDENCE_FIELD["zh"]
    _write_file(path, text[:nl + 1] + extra + text[nl + 1:])
    return u"zh: `- **置信度**：极高` added to the section after the last card"


# Breakages that must be caught, each with the check tag that must report it.
NEGATIVE_CASES = [
    (u"dangling anchor", "links", _break_dangling_anchor),
    (u"dependency edge disagrees with the card", "dep-graph", _break_dep_edge),
    (u"root card's dependency edge disagrees", "dep-graph",
     _break_root_dep_edge),
    (u"card exists in one language only", "bilingual-cards",
     _break_single_language_card),
    (u"confidence outside the whitelist", "confidence",
     _set_confidence("zh", u"\u6781\u9ad8")),  # 极高
    (u"second confidence value in the same card", "confidence",
     _break_second_confidence),
    (u"confidence value unreadable", "confidence",
     _break_unreadable_confidence),
    (u"required card field missing", "card-fields", _break_missing_field),
]

# Edits that must NOT be reported: the checker has to stay usable.
POSITIVE_CASES = [
    (u"prose below the last card belongs to no card", _text_after_last_card),
]

# The whitelist is per language, so a value must be an exact member of ITS
# language's set: `high` in a Chinese card is rejected on purpose.
CONFIDENCE_REJECTED = [
    ("zh", u"\u6781\u9ad8"),        # 极高  — contains 高
    ("zh", u"\u5f88\u4f4e"),        # 很低  — contains 低
    ("zh", u"\u4e2d\u9ad8"),        # 中高  — the grade that actually shipped once
    ("zh", u"\u4e2d\uff08\u504f\u9ad8\uff09"),   # 中（偏高） — same grade, in brackets
    ("en", "Medium (leaning high)."),
    ("zh", u"\u672a\u77e5"),        # 未知
    ("zh", "0.8"),
    ("en", "very high"),
    ("en", "high-ish"),
    ("en", "0.8"),
    ("zh", "high"),                 # right grade, wrong language
]
CONFIDENCE_ACCEPTED = [
    ("zh", u"\u9ad8"), ("zh", u"\u4e2d"), ("zh", u"\u4f4e"),
    ("en", "high"), ("en", "medium"), ("en", "low"),
    # The form the ledger actually uses for landscape-only judgments.
    ("zh", u"\u4f4e\uff08\u4ec5\u56fe\u666f\uff09\u3002"),
    ("en", "Low (landscape only)."),
]


def self_test():
    base = tempfile.mkdtemp(prefix="ledger-check-self-test-")
    counter = itertools.count()
    passed, failed = 0, 0

    def report(ok, title, detail):
        print("  %-4s %-44s %s" % ("PASS" if ok else "FAIL", title, detail))

    try:
        pristine = _copy_checkable_tree(os.path.join(base, "pristine"))
        code, out = _run_checker(pristine)
        if code != 0:
            print("baseline: the unbroken copy already fails (exit %d), so the "
                  "negative cases below would prove nothing. Fix the tree "
                  "first.\n" % code)
            print(out)
            return 1
        print("baseline: unbroken copy exits 0\n")

        def fresh():
            work = os.path.join(base, "case-%d" % next(counter))
            shutil.copytree(pristine, work)
            return work

        print("negative cases (the checker must exit non-zero, "
              "and name the right check):")
        for title, tag, mutate in NEGATIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            ok = code != 0 and ("[%s]" % tag) in out
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, title, u"exit %d, expected [%s] — %s" % (code, tag, detail))

        print("\nconfidence values that must be rejected:")
        for lang, value in CONFIDENCE_REJECTED:
            work = fresh()
            _set_confidence(lang, value)(work)
            code, out = _run_checker(work)
            ok = code != 0 and "[confidence]" in out
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, u"%s card: %s" % (lang, value), u"exit %d" % code)

        print("\nconfidence values that must be accepted:")
        for lang, value in CONFIDENCE_ACCEPTED:
            work = fresh()
            _set_confidence(lang, value)(work)
            code, out = _run_checker(work)
            ok = code == 0
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, u"%s card: %s" % (lang, value), u"exit %d" % code)

        print("\nedits that must NOT be reported:")
        for title, mutate in POSITIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            ok = code == 0
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, title, u"exit %d — %s" % (code, detail))

        print("\nself-test: %d passed, %d failed" % (passed, failed))
        return 1 if failed else 0
    finally:
        shutil.rmtree(base, ignore_errors=True)


USAGE = """usage: python3 scripts/check.py [--repo DIR] [--self-test]

  (no argument)  check this repository
  --repo DIR     check the tree rooted at DIR instead
  --self-test    break a temporary copy of the tree five ways and assert the
                 checker catches each one (the repository is not touched)"""


def main(argv):
    global REPO
    args = list(argv)
    wants_self_test = False
    while args:
        arg = args.pop(0)
        if arg == "--self-test":
            wants_self_test = True
        elif arg == "--repo":
            if not args:
                print("--repo needs a directory\n%s" % USAGE)
                return 2
            REPO = os.path.abspath(args.pop(0))
        elif arg in ("-h", "--help"):
            print(USAGE)
            return 0
        else:
            print("unknown argument: %s\n%s" % (arg, USAGE))
            return 2
    return self_test() if wants_self_test else run_checks()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
