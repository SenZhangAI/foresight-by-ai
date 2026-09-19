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


def is_markdown(name):
    """Extension match, case-insensitively.

    macOS filesystems are case-insensitive, so `90-x.MD` and `90-x.md` are the
    same file to a human and to git checkout, but a case-sensitive `.endswith`
    sees only one of them: a chain file landing as `.MD` would be invisible to
    every check here while reading as an ordinary chain on GitHub.
    """
    return name.lower().endswith(".md")


def markdown_files():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO, "docs")):
        for f in sorted(files):
            if is_markdown(f):
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
        # occurrence in the card is tested, not only the first, and as many
        # values must be readable as there are fields.
        found = list(re.finditer(CONFIDENCE_VALUE, body))
        markers = len(re.findall(r"\*\*(?:Confidence|\u7f6e\u4fe1\u5ea6)\*\*",
                                 body))
        if len(found) != markers:
            # Not "no value at all" but "fewer values than fields": a card
            # carrying one readable grade plus a `- **置信度** 极高` line with no
            # separator would otherwise have its second field read by nobody —
            # present enough for the field check, invisible to the whitelist.
            fail("confidence",
                 "%s %s: %d confidence field(s) but %d readable value(s)"
                 % (lang, jid, markers, len(found)))
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
                if is_markdown(f):
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


# ---------------------------------------------------------------------------
# The chain registry, and the counts the READMEs state about the tree.
#
# Everything above this line reads the ledger. The two READMEs were checked by
# nothing at all — and they are where a human hand writes the two quantities
# that change every round: how many judgment cards the ledger holds, and which
# reasoning chains exist. Two of the three cross-file drifts this repository
# has shipped started exactly there.
#
# These checks are mechanical invariants only — two numbers equal, a link
# resolves, two sets match. None of them judges whether a chain is any good.
# ---------------------------------------------------------------------------

REGISTRY_README = {"zh": "README.md", "en": "README.en.md"}
CHAIN_DIR = "docs/%s/chains/"
# A registry row's first cell must be exactly this, never merely contain it.
CHAIN_ID = re.compile(r"^C(\d+)$")
# A citation anywhere in the prose. The boundary is written by hand because
# `\b` does not fire between a CJK character and `C`: both are word characters
# to Python, so `\bC3` misses `预告成C3`.
CHAIN_ID_TOKEN = re.compile(r"(?<![0-9A-Za-z])C(\d+)(?![0-9])")
CHAIN_LINK = re.compile(r"\]\((docs/(?:zh|en)/chains/[^)#\s]+)\)")
# `[C3 · full title](path)`, `[C3：short title](path)` — any citation that
# names a chain, whichever separator it uses. A bare `[C1](path)` names no
# title and is not one of these.
CHAIN_CITE = re.compile(u"\\[(C\\d+)\\s*[\u00b7:\uff1a]\\s*([^\\]]*)\\]"
                        u"\\(([^)\\s]+)\\)")
CHAIN_H1 = re.compile(u"^#\\s+(C\\d+)\\s*[\u00b7:\uff1a]\\s*(.*)$")

# 〇零一二三四五六七八九十百两 — the numerals a Chinese count may be spelled with.
ZH_NUMERALS = (u"\u3007\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b"
               u"\u4e5d\u5341\u767e\u4e24")
ZH_DIGIT = {u"\u3007": 0, u"\u96f6": 0, u"\u4e00": 1, u"\u4e8c": 2,
            u"\u4e24": 2, u"\u4e09": 3, u"\u56db": 4, u"\u4e94": 5,
            u"\u516d": 6, u"\u4e03": 7, u"\u516b": 8, u"\u4e5d": 9}
ZH_UNIT = {u"\u5341": 10, u"\u767e": 100}
EN_ONES = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
           "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
           "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
           "nineteen": 19}
EN_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
           "seventy": 70, "eighty": 80, "ninety": 90}

# The exact phrases the count check reads. A rewrite that drops one of them
# does not silently shrink the check's reach: the site counts below must stay
# equal across the two languages and must never both fall to zero.
COUNT_ANCHOR = {
    # 张判断卡片 / 条独立推演链
    "cards": {"zh": u"\u5f20\u5224\u65ad\u5361\u7247", "en": "judgment cards"},
    "chains": {"zh": u"\u6761\u72ec\u7acb\u63a8\u6f14\u94fe",
               "en": "independent reasoning chains"},
}

# Markup a reader does not see: emphasis and code markers, the zero-width
# space, the BOM, and HTML comments.
#
# Why the count check must strip these before reading anything. The two site
# invariants below (equal site counts, never both zero) assume the two READMEs
# are two independent witnesses — and they are not: this repository's own rule
# is that both trees change in the SAME commit. So a hand that writes
# `**66**张判断卡片` / `**Sixty-six** judgment cards` removes that site from
# both languages at once: the site counts stay equal, neither falls to zero,
# the other sites still read 65, and the checker exits 0 while the README shows
# a reader `66`. Verified by hand on 2026-09-19 against commit `aadb15d`. The
# same hole is opened by a zero-width space or an empty HTML comment wedged
# between the number and its anchor, which is why this is a class and not the
# three characters that were tried.
INVISIBLE = re.compile(u"<!--[\\s\\S]*?-->|[`*_\u200b\ufeff]")


def visible(text):
    """The text as a reader sees it, with invisible markup removed."""
    return INVISIBLE.sub("", text)


def parse_count(lang, token):
    """`65` / `六十五` / `sixty-five` -> 65; anything else -> None."""
    raw = token.strip()
    if re.match(r"^\d+$", raw):
        return int(raw)
    if lang == "zh":
        total, section, seen = 0, 0, False
        for ch in raw:
            if ch in ZH_DIGIT:
                section, seen = ZH_DIGIT[ch], True
            elif ch in ZH_UNIT:
                section = (section or 1) * ZH_UNIT[ch]
                total, section, seen = total + section, 0, True
            else:
                return None
        return total + section if seen else None
    total, seen = 0, False
    for part in re.split(r"[-\s]+", raw.lower()):
        if not part or part == "and":
            continue
        if part in EN_ONES:
            total, seen = total + EN_ONES[part], True
        elif part in EN_TENS:
            total, seen = total + EN_TENS[part], True
        elif part == "hundred":
            total, seen = (total or 1) * 100, True
        else:
            return None
    return total if seen else None


def chain_files_on_disk():
    found = set()
    for lang in LANGS:
        root = os.path.join(REPO, "docs", lang, "chains")
        if not os.path.isdir(root):
            continue
        for r, _d, fs in os.walk(root):
            for f in sorted(fs):
                if is_markdown(f):
                    rel = os.path.relpath(os.path.join(r, f), REPO)
                    found.add(rel.replace(os.sep, "/"))
    return found


def table_rows(text):
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            yield [c.strip() for c in s.strip("|").split("|")]


def parse_registry(lang):
    """({C-id: set of chain files}, {C-id: topic cell}) for one README.

    A row takes part only when its first cell is exactly `C<n>`. The table's
    last row is an announced direction (`—（不占编号）` / `— (holds no
    number)`) which links a landscape file rather than a chain: a looser match
    would drag it in and the whole check would collapse on it. A cell that
    CONTAINS an identifier without being one (`C4 (draft)`) is reported rather
    than skipped — silently ignoring such a row is how a chain stops being
    checked while still reading as registered.
    """
    readme = REGISTRY_README[lang]
    rows = {}
    topics = {}
    for cols in table_rows(read(readme)):
        cell = re.sub(r"[`*\s]", "", cols[0] if cols else "")
        if not CHAIN_ID.match(cell):
            if CHAIN_ID_TOKEN.search(cell):
                fail("chain-registry",
                     "%s: registry row starts with %r, which is not a bare "
                     "C<n>, so the row would not be checked" % (readme, cols[0]))
            continue
        if cell in rows:
            fail("chain-registry", "%s: %s has more than one registry row"
                 % (readme, cell))
        links = set()
        for col in cols:
            for m in CHAIN_LINK.finditer(col):
                links.add(os.path.normpath(m.group(1)).replace(os.sep, "/"))
        rows.setdefault(cell, set()).update(links)
        topics.setdefault(cell, cols[1].strip() if len(cols) > 1 else "")
    return rows, topics


def check_chain_registry():
    """Registry, disk and citations agree. Returns the registered ids."""
    disk = chain_files_on_disk()
    if not disk:
        fail("chain-registry", "no chain file found under docs/*/chains/")
    registry = {}
    topics = {}
    for lang in LANGS:
        registry[lang], topics[lang] = parse_registry(lang)
        if not registry[lang]:
            fail("chain-registry", "%s: no registry row found, so no chain is "
                 "checked at all" % REGISTRY_README[lang])
    if set(registry["zh"]) != set(registry["en"]):
        fail("chain-registry",
             "the two registries allocate different identifiers: %s"
             % sorted(set(registry["zh"]) ^ set(registry["en"])))
    for lang in LANGS:
        readme = REGISTRY_README[lang]
        for cid in sorted(registry[lang]):
            paths = registry[lang][cid]
            for p in sorted(paths):
                if not os.path.exists(os.path.join(REPO, p)):
                    fail("chain-registry", "%s: %s links %s, which does not "
                         "exist" % (readme, cid, p))
            for side in LANGS:
                own = sorted(p for p in paths if p.startswith(CHAIN_DIR % side))
                # Exactly one, not merely at least one. "At least one" let a
                # second file ride along on an existing row — a same-named
                # shadow under `chains/extra/` satisfied every other rule here
                # while being a chain nobody had allocated a number to.
                if len(own) != 1:
                    fail("chain-registry", "%s: %s links %d %s chain files, "
                         "not exactly one: %s"
                         % (readme, cid, len(own), side, own or "(none)"))
            # The rule the README states: the filename is `<id x 10>-<slug>.md`,
            # identical in both languages.
            prefix = "%d-" % (int(cid[1:]) * 10)
            for p in sorted(paths):
                if not os.path.basename(p).startswith(prefix):
                    fail("chain-registry", "%s: %s links %s, whose filename "
                         "does not start with %s" % (readme, cid, p, prefix))
            # Stated directly, though it is also fenced in by `bilingual-files`
            # parity and by the rule that every chain file on disk must be
            # registered: with those two standing, no isolated negative case
            # for this line exists, and it is kept as a statement of the
            # README's naming rule rather than as the only guard.
            names = set(os.path.basename(p) for p in paths)
            if len(names) > 1:
                fail("chain-registry", "%s: %s links differently named files: "
                     "%s" % (readme, cid, sorted(names)))
    for cid in sorted(set(registry["zh"]) & set(registry["en"])):
        if registry["zh"][cid] != registry["en"][cid]:
            fail("chain-registry", "%s: the zh registry links %s, the en "
                 "registry links %s" % (cid, sorted(registry["zh"][cid]),
                                        sorted(registry["en"][cid])))
    for lang in LANGS:
        linked = set()
        for paths in registry[lang].values():
            linked |= paths
        for p in sorted(disk - linked):
            fail("chain-registry", "%s: %s exists on disk but no registry row "
                 "links it" % (REGISTRY_README[lang], p))
    known = set(registry["zh"]) | set(registry["en"])
    check_registry_topics(registry, topics)
    for f in markdown_files():
        cited = set()
        for m in CHAIN_ID_TOKEN.finditer(read(f)):
            cited.add("C%s" % m.group(1))
        for cid in sorted(cited - known):
            fail("chain-id", "%s cites %s, which the chain registry does not "
                 "allocate" % (f, cid))
    return known


def title_of(path):
    """(identifier, title) from a chain file's H1, or a reported failure."""
    h1 = re.search(r"^#\s+(.*)$", read(path), re.M)
    if not h1:
        return None, None
    head = CHAIN_H1.match("# " + h1.group(1).strip())
    if not head:
        return None, h1.group(1).strip()
    return head.group(1), head.group(2)


def check_registry_topics(registry, topics):
    """The registry's Topic cell must name the chain its row links.

    This is the cell the collision of 2026-09-19 actually turned on: C1's
    closing section announced trust collateralisation as C3, while the file
    written as C3 was the power-and-permits chain. Every other part of a row is
    now tied to the file — the identifier, the filename, both languages, the
    file's existence — and the one cell saying WHICH chain the identifier
    stands for was tied to nothing at all, so the registry could go on naming a
    chain that is not the one it links.

    Containment, like the citation rule, because a registry topic may legally
    be shorter than the H1; and case-insensitive, because the English registry
    writes its cells in sentence case while the H1s are in title case
    (`What becomes unbuyable…` against `What Becomes Unbuyable…`) — a
    case-sensitive rule would report the whole English table and be turned off
    within a day.
    """
    for lang in LANGS:
        readme = REGISTRY_README[lang]
        for cid in sorted(topics[lang]):
            topic = topics[lang][cid]
            own = [p for p in sorted(registry[lang][cid])
                   if p.startswith(CHAIN_DIR % lang)]
            if len(own) != 1:
                continue  # already reported as a link failure
            path = own[0]
            if not os.path.exists(os.path.join(REPO, path)):
                continue  # already reported as a dangling row
            file_id, title = title_of(path)
            if file_id != cid:
                # One criterion, not three. "No H1", "an H1 that does not open
                # with an identifier" and "an H1 opening with the wrong
                # identifier" are the same failure — the file does not say it
                # is this chain — and splitting them produced branches no
                # negative case could reach on its own, because whichever ran
                # first hid the others. The heading is printed so a reader can
                # still tell which of the three they are looking at.
                fail("chain-title", "%s: the %s row links %s, whose first "
                     "heading is %r rather than `# %s \u00b7 <title>`"
                     % (readme, cid, path, title, cid))
            elif not topic:
                fail("chain-title", "%s: %s registers no topic, so the table "
                     "does not say which chain the identifier is"
                     % (readme, cid))
            elif topic.lower() not in title.lower():
                fail("chain-title", "%s: %s is registered as %r, which is no "
                     "part of %s's title %r" % (readme, cid, topic, path,
                                                title))


def check_chain_titles():
    """A citation may shorten a chain's title; it may not rename it.

    The defect this closes: the same chain was called one thing by its own H1
    and the registry, and another by the "where to start" paragraph, so a
    reader following the identifier met a second name for the file they had
    just opened.

    The rule is containment, not equality, because the repository abbreviates
    in two directions and both are honest: the ledger cites C1 by the opening
    of its title and C2 by its subtitle. What containment still refuses is a
    title the file does not contain at all — `[C3 · 电子落地：为什么算力的上限
    不在芯片]` against a file titled `电子落地：算力的瓶颈从芯片移到电网`. It is
    separator-agnostic (the ledger cites with `：`, the READMEs with `·`), and
    a citation carrying no title (`[C1](path)`) asserts nothing that could
    contradict the file, so it is not read here. The comparison is
    case-insensitive for the same reason the registry topics are: the English
    side writes sentence case in prose and title case in H1s, and that is a
    typographic convention, not a rename.
    """
    for f in markdown_files():
        base = os.path.dirname(f)
        for m in CHAIN_CITE.finditer(read(f)):
            cid, title = m.group(1), m.group(2).strip()
            path = m.group(3).partition("#")[0]
            if not path:
                continue
            target = os.path.normpath(os.path.join(base, path))
            if not os.path.exists(os.path.join(REPO, target)):
                continue  # check_links reports the missing file
            file_id, h1_title = title_of(target)
            if file_id != cid:
                fail("chain-title", "%s: cited as %s, but %s opens with %r"
                     % (f, cid, target, h1_title))
            elif title and title.lower() not in h1_title.lower():
                fail("chain-title", "%s: %s is cited as %r, which is no part "
                     "of %s's title %r" % (f, cid, title, target, h1_title))


def count_claims(lang, anchor):
    """(values, unreadable) for one count phrase in one README.

    The text is normalised first: a count is a claim made to a READER, so it
    must be read the way a reader reads it. See INVISIBLE.
    """
    text = visible(read(REGISTRY_README[lang]))
    if lang == "zh":
        pattern = u"([0-9%s]+)\\s*%s" % (ZH_NUMERALS, re.escape(anchor))
    else:
        pattern = r"([A-Za-z0-9-]+)\s+%s" % re.escape(anchor)
    values, unreadable = [], []
    for m in re.finditer(pattern, text):
        raw = m.group(1)
        n = parse_count(lang, raw)
        if n is not None:
            values.append((n, raw))
        elif lang == "zh" or re.search(r"\d", raw):
            # An English anchor can legitimately follow an ordinary word
            # ("all the judgment cards"), which is prose and not a claim. A
            # Chinese match always begins with a numeral, and an English one
            # carrying a digit is a number that failed to parse: both are a
            # count nobody can read, and neither is waved through.
            unreadable.append(raw)
    return values, unreadable


def check_readme_counts(per_lang_cards, chains):
    """Every count the READMEs state equals what the repository holds.

    Coverage is held by the two site invariants rather than by trying to parse
    every sentence: the two languages must state each count the same number of
    times, and a count may not vanish from both at once. A rewrite that drops
    one side is therefore caught; one that drops both in a single commit is
    not, and that is the honest boundary of this check.

    What is no longer a boundary, because the site invariants could not see it:
    a number dressed in markup (`**66**`, a zero-width space, an HTML comment)
    stayed visible to the reader and vanished from BOTH languages' site counts
    at once. The text is normalised before it is read — see INVISIBLE.
    """
    for kind in ("cards", "chains"):
        sites = {}
        for lang in LANGS:
            readme, anchor = REGISTRY_README[lang], COUNT_ANCHOR[kind][lang]
            values, unreadable = count_claims(lang, anchor)
            for raw in unreadable:
                fail("readme-counts", "%s: %r before %r is not a number"
                     % (readme, raw, anchor))
            want = len(per_lang_cards[lang]) if kind == "cards" else chains
            for n, raw in values:
                if n != want:
                    fail("readme-counts",
                         "%s says %r %s, the repository has %d"
                         % (readme, raw, anchor, want))
            sites[lang] = len(values)
        if sites["zh"] != sites["en"]:
            fail("readme-counts", "the %s count is stated %d time(s) in %s and "
                 "%d time(s) in %s" % (kind, sites["zh"], REGISTRY_README["zh"],
                                       sites["en"], REGISTRY_README["en"]))
        if not sites["zh"] and not sites["en"]:
            fail("readme-counts", "neither README states the %s count, so this "
                 "check covers nothing" % kind)


def run_checks():
    files = markdown_files()
    links = check_links(files)
    cards = {lang: check_ledger(lang) for lang in LANGS}
    check_parity(cards)
    chains = check_chain_registry()
    check_chain_titles()
    check_readme_counts(cards, len(chains))

    print("files checked      : %d" % len(files))
    print("internal links     : %d" % links)
    print("judgment cards     : zh %d / en %d" % (len(cards["zh"]), len(cards["en"])))
    print("chains registered  : %d (%s)" % (len(chains), ", ".join(sorted(chains))))
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


def _break_single_language_card(lang):
    """Remove the last card from one language; parity must notice either way."""
    other = "en" if lang == "zh" else "zh"

    def mutate(root):
        path = _ledger(root, lang)
        text = _read_file(path)
        start, end, jid = _last_card(text)
        _write_file(path, text[:start] + text[end:])
        return u"%s ledger: card %s removed, %s still carries it" % (
            lang, jid, other)

    return mutate


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


def _break_partial_readable_confidence(root):
    """One readable value beside one unreadable field, in the same card.

    Each fix alone leaves this open: `found` is non-empty so "no value at all"
    never fires, and the unreadable line never enters the whitelist loop.
    """
    path = _ledger(root, "zh")
    text = _read_file(path)
    head, jid = _first_card(text)
    field = CONFIDENCE_FIELD["zh"]
    m = re.search(r"^- \*\*%s\*\*[:\uff1a][^\n]*\n" % re.escape(field),
                  text[head:], re.M)
    if not m:
        raise AssertionError("zh %s carries no %s line" % (jid, field))
    extra = u"- **%s** \u6781\u9ad8\n" % field  # readable line above, none here
    _write_file(path, text[:head + m.end()] + extra + text[head + m.end():])
    return (u"zh %s: a valid value, plus a second field with no separator"
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


# --- fixtures for the registry and the README counts -----------------------

def _readme(root, lang):
    return os.path.join(root, REGISTRY_README[lang])


def _registry_row_indexes(text):
    """Line numbers of the README lines that are `C<n>` registry rows."""
    out = []
    for i, line in enumerate(text.split("\n")):
        s = line.strip()
        if not s.startswith("|"):
            continue
        first = re.sub(r"[`*\s]", "", s.strip("|").split("|")[0])
        if CHAIN_ID.match(first):
            out.append(i)
    if not out:
        raise AssertionError("fixture README carries no registry row")
    return out


def _edit_registry_row(root, lang, which, edit):
    """Rewrite one registry row in place; `edit` takes and returns the line."""
    path = _readme(root, lang)
    lines = _read_file(path).split("\n")
    i = _registry_row_indexes("\n".join(lines))[which]
    before = lines[i]
    lines[i] = edit(before)
    if lines[i] == before:
        raise AssertionError("registry fixture changed nothing: %r" % before)
    _write_file(path, "\n".join(lines))
    return lines[i]


def _add_chain_file(root, stem, langs=LANGS):
    for lang in langs:
        d = os.path.join(root, "docs", lang, "chains")
        if not os.path.isdir(d):
            raise AssertionError("fixture has no docs/%s/chains/" % lang)
        _write_file(os.path.join(d, "%s.md" % stem),
                    u"# C9 \u00b7 fixture chain\n\nBody.\n")


def _break_unregistered_chain_file(root):
    """A chain file lands on disk and no registry row mentions it."""
    _add_chain_file(root, "90-unregistered-fixture")
    return u"docs/{zh,en}/chains/90-unregistered-fixture.md added, registered nowhere"


def _break_registry_row_removed(root):
    """The chain file stays; its registry row is deleted."""
    path = _readme(root, "zh")
    lines = _read_file(path).split("\n")
    i = _registry_row_indexes("\n".join(lines))[-1]
    gone = lines.pop(i)
    _write_file(path, "\n".join(lines))
    return u"README.md: last registry row deleted (%s)" % gone.strip()[:40]


def _break_registry_single_language_link(root):
    """A row that registers the chain in one language only."""
    def edit(line):
        return re.sub(r"\s*\u00b7\s*\[[^\]]*\]\(docs/en/chains/[^)]*\)", "", line)
    row = _edit_registry_row(root, "zh", 0, edit)
    return u"README.md: first row now links no English chain file"


def _break_registry_id_unreadable(root):
    """`C3 (draft)` — an id a strict first-column match would skip."""
    def edit(line):
        head, sep, rest = line.partition("|")
        cid, sep2, tail = rest.partition("|")
        return head + sep + cid.rstrip() + u" (draft) " + sep2 + tail
    row = _edit_registry_row(root, "zh", -1, edit)
    return u"README.md: %s" % row.strip()[:52]


def _break_registry_dangling_link(root):
    """A row pointing at a chain file that is not there."""
    def edit(line):
        return line.replace("chains/10-", "chains/10-no-such-")
    row = _edit_registry_row(root, "zh", 0, edit)
    return u"README.md: first row links docs/*/chains/10-no-such-*.md"


def _break_registry_one_sided_id(root):
    """A new chain registered in the Chinese README only."""
    _add_chain_file(root, "90-one-sided-fixture")
    path = _readme(root, "zh")
    lines = _read_file(path).split("\n")
    i = _registry_row_indexes("\n".join(lines))[-1]
    lines.insert(i + 1,
                 u"| C9 | fixture | \u5df2\u5199\u6210 | "
                 u"[\u4e2d\u6587](docs/zh/chains/90-one-sided-fixture.md) \u00b7 "
                 u"[English](docs/en/chains/90-one-sided-fixture.md) |")
    _write_file(path, "\n".join(lines))
    return u"C9 registered in README.md only, files present in both languages"


def _break_forecast_row_numbered(root):
    """The announced-direction row takes a number it must not have.

    It links a landscape file rather than a chain, so the moment it claims an
    identifier the registry is describing a chain that does not exist.
    """
    path = _readme(root, "zh")
    lines = _read_file(path).split("\n")
    last = _registry_row_indexes("\n".join(lines))[-1]
    for i in range(last + 1, len(lines)):
        if lines[i].strip().startswith("|"):
            cells = lines[i].strip().strip("|").split("|")
            lines[i] = "| C4 |" + "|".join(cells[1:]) + "|"
            _write_file(path, "\n".join(lines))
            return u"README.md: the announced-direction row now claims C4"
    raise AssertionError("fixture has no row after the last registry row")


def _break_chain_title(root):
    """The prose calls a chain something its own H1 does not.

    The replacement is not a truncation but a different name: a shortened
    title is legitimate and must stay green.
    """
    path = _readme(root, "zh")
    text = _read_file(path)
    m = CHAIN_CITE.search(text)
    if not m:
        raise AssertionError("fixture README cites no chain by title")
    renamed = u"\u53e6\u4e00\u4e2a\u540d\u5b57"  # 另一个名字
    _write_file(path, text[:m.start(2)] + renamed + text[m.end(2):])
    return u"README.md: %s is cited under a title its file does not carry" % m.group(1)


def _shorten_chain_title(root):
    """Not a breakage: a citation that abbreviates the title it points at.

    The slice deliberately starts past the first character, so this proves the
    rule accepts an abbreviation taken from the MIDDLE of the title — the form
    the ledger actually uses when it cites C2 by its subtitle.
    """
    path = _readme(root, "zh")
    text = _read_file(path)
    m = CHAIN_CITE.search(text)
    if not m:
        raise AssertionError("fixture README cites no chain by title")
    title = m.group(2).strip()
    if len(title) < 5:
        raise AssertionError("fixture title is too short to abbreviate")
    part = title[1:4]
    _write_file(path, text[:m.start(2)] + part + text[m.end(2):])
    return u"README.md: %s cited as %r, taken from inside its title" % (
        m.group(1), part)


def _set_count(lang, anchor_kind, replacement):
    """Rewrite the FIRST count claim of one kind in one README."""
    def mutate(root):
        path = _readme(root, lang)
        text = _read_file(path)
        anchor = COUNT_ANCHOR[anchor_kind][lang]
        if lang == "zh":
            pattern = u"([0-9%s]+)(\\s*%s)" % (ZH_NUMERALS, re.escape(anchor))
        else:
            pattern = r"([A-Za-z0-9-]+)(\s+%s)" % re.escape(anchor)
        m = re.search(pattern, text)
        if not m:
            raise AssertionError("%s states no %s count" % (lang, anchor_kind))
        _write_file(path, text[:m.start(1)] + replacement + text[m.end(1):])
        return u"%s: %r -> %r before %r" % (REGISTRY_README[lang], m.group(1),
                                            replacement, anchor)

    return mutate


def _break_count_site_removed(root):
    """One language stops stating a count the other still states."""
    path = _readme(root, "zh")
    text = _read_file(path)
    anchor = COUNT_ANCHOR["cards"]["zh"]
    m = re.search(u"[0-9%s]+\\s*%s" % (ZH_NUMERALS, re.escape(anchor)), text)
    if not m:
        raise AssertionError("zh README states no card count")
    _write_file(path, text[:m.start()] + anchor + text[m.end():])
    return u"README.md: one card-count claim rewritten without its number"


def _extra_announced_row(root):
    """Not a breakage: a second announced direction, holding no number."""
    for lang in LANGS:
        path = _readme(root, lang)
        lines = _read_file(path).split("\n")
        i = _registry_row_indexes("\n".join(lines))[-1]
        lines.insert(i + 1, u"| \u2014 | fixture direction | announced | "
                            u"[far](docs/%s/30-far.md) |" % lang)
        _write_file(path, "\n".join(lines))
    return u"a second `—` row added to both registries"


def _prose_mentioning_the_anchor(root):
    """Not a breakage: prose that names cards without counting them."""
    zh = _readme(root, "zh")
    _write_file(zh, _read_file(zh)
                + u"\n\u6bcf\u5f20\u5224\u65ad\u5361\u7247\u90fd\u6709\u7f16\u53f7\u3002\n")
    en = _readme(root, "en")
    _write_file(en, _read_file(en)
                + u"\nAll the judgment cards carry a falsifier.\n")
    return u"`每张判断卡片…` / `All the judgment cards…` appended to the READMEs"


def _count_pattern(lang, kind):
    anchor = COUNT_ANCHOR[kind][lang]
    if lang == "zh":
        return u"([0-9%s]+)(\\s*%s)" % (ZH_NUMERALS, re.escape(anchor))
    return r"([A-Za-z0-9-]+)(\s+%s)" % re.escape(anchor)


def _bump_chain_count(root, lang, delta=1):
    """Keep the stated chain count true after a fixture chain is registered."""
    path = _readme(root, lang)
    text = _read_file(path)

    def repl(m):
        n = parse_count(lang, m.group(1))
        return m.group(0) if n is None else "%d%s" % (n + delta, m.group(2))

    new = re.sub(_count_pattern(lang, "chains"), repl, text)
    if new == text:
        raise AssertionError("%s README states no readable chain count" % lang)
    _write_file(path, new)


def _register_fixture_chain(root, n, stem, body=None, topic=u"fixture"):
    """Add a chain that satisfies EVERY registry rule but one.

    A negative case proves something about one criterion only when it leaves
    all the others satisfied — otherwise it would still fail after that
    criterion was deleted, and would be testing its neighbours. So a fixture
    chain lands in both languages, is registered in both READMEs, is named by
    the `<id x 10>-` rule, carries an H1 its Topic cell is part of, and bumps
    the chain count both READMEs state. Each caller then breaks one thing.
    """
    cid = "C%d" % n
    default = u"# %s \u00b7 %s chain\n\nBody.\n" % (cid, topic)
    for lang in LANGS:
        d = os.path.join(root, "docs", lang, "chains")
        if not os.path.isdir(d):
            raise AssertionError("fixture has no docs/%s/chains/" % lang)
        _write_file(os.path.join(d, "%s.md" % stem),
                    default if body is None else body)
    for lang in LANGS:
        path = _readme(root, lang)
        lines = _read_file(path).split("\n")
        i = _registry_row_indexes("\n".join(lines))[-1]
        lines.insert(i + 1, u"| %s | %s | fixture | "
                            u"[zh](docs/zh/chains/%s.md) \u00b7 "
                            u"[en](docs/en/chains/%s.md) |"
                     % (cid, topic, stem, stem))
        _write_file(path, "\n".join(lines))
        _bump_chain_count(root, lang)
    return cid


def _break_chain_filename_prefix(root):
    """A registered chain whose filename does not follow `<id x 10>-`."""
    _register_fixture_chain(root, 9, "99-prefix-fixture")
    return u"C9 registered, but its files are named 99-prefix-fixture.md"


def _break_registered_chain_without_h1(root):
    """A registered chain whose file never says what it is called.

    Nothing read this before: registry rows link with plain link text
    (`[中文](path)`), so the citation check never opened these files at all.
    """
    _register_fixture_chain(root, 9, "90-no-h1-fixture",
                            body=u"No heading at all.\n\nBody.\n")
    return u"C9 registered, its files carry no H1"


def _break_registry_topic_renamed(root):
    """The Topic cell names a chain other than the file the row links.

    The cell the 2026-09-19 collision turned on, and the only cell of a row
    that used to be tied to nothing.
    """
    def edit(line):
        cells = line.strip().strip("|").split("|")
        cells[1] = u" \u53e6\u4e00\u6761\u94fe\u7684\u540d\u5b57 "  # 另一条链的名字
        return "|" + "|".join(cells) + "|"
    _edit_registry_row(root, "zh", 0, edit)
    return u"README.md: the first row's Topic cell renamed"


def _break_registry_topic_empty(root):
    """A row that allocates an identifier and says nothing about it.

    Containment alone waves this through — the empty string is part of every
    title — so the emptiness has to be refused on its own.
    """
    def edit(line):
        cells = line.strip().strip("|").split("|")
        cells[1] = "  "
        return "|" + "|".join(cells) + "|"
    _edit_registry_row(root, "zh", 0, edit)
    return u"README.md: the first row's Topic cell emptied"


def _break_shadow_chain_file(root):
    """A second, same-named chain file riding along on an existing row.

    `docs/*/chains/extra/10-...md` satisfies every other rule: it exists, it
    is registered, both languages have it, the name follows the prefix rule,
    the parity check sees the same filename on both sides. Only "exactly one
    file per language" refuses it.
    """
    stem = "10-generation-becomes-free"
    for lang in LANGS:
        d = os.path.join(root, "docs", lang, "chains", "extra")
        if not os.path.isdir(d):
            os.makedirs(d)
        _write_file(os.path.join(d, "%s.md" % stem),
                    u"# C1 \u00b7 shadow\n\nBody.\n")
    for lang in LANGS:
        def edit(line):
            return line.rstrip().rstrip("|") + (
                u" \u00b7 [shadow-zh](docs/zh/chains/extra/%s.md) \u00b7 "
                u"[shadow-en](docs/en/chains/extra/%s.md) |" % (stem, stem))
        _edit_registry_row(root, lang, 0, edit)
    return u"docs/*/chains/extra/%s.md added to the C1 row" % stem


def _break_uppercase_md_chain_file(root):
    """An unregistered chain file whose extension is `.MD`.

    On a case-insensitive filesystem this is the same file to everyone except
    a case-sensitive `endswith('.md')`, which used to skip it — so a chain
    could land on disk, be readable on GitHub, and be checked by nothing.
    """
    for lang in LANGS:
        d = os.path.join(root, "docs", lang, "chains")
        _write_file(os.path.join(d, "90-uppercase-fixture.MD"),
                    u"# C9 \u00b7 fixture chain\n\nBody.\n")
    return u"docs/{zh,en}/chains/90-uppercase-fixture.MD added, registered nowhere"


def _break_duplicate_registry_row(root):
    """The same identifier registered twice in one table."""
    path = _readme(root, "zh")
    lines = _read_file(path).split("\n")
    i = _registry_row_indexes("\n".join(lines))[0]
    lines.insert(i + 1, lines[i])
    _write_file(path, "\n".join(lines))
    return u"README.md: the first registry row duplicated"


def _break_citation_wrong_identifier(root):
    """Prose cites one chain's file under another chain's identifier."""
    path = _readme(root, "zh")
    _write_file(path, _read_file(path) + u"\n\u53c2\u89c1 [C2 \u00b7 "
                u"\u751f\u6210\u53d8\u5f97\u514d\u8d39\u4e4b\u540e]"
                u"(docs/zh/chains/10-generation-becomes-free.md)\u3002\n")
    return u"README.md: C1's file cited as C2"


def _break_citation_without_space(root):
    """An identifier cited with a CJK character directly before it.

    `\\b` does not fire between a CJK character and `C`, which is why the
    boundary is written by hand — and why it needs a case of its own: the
    spaced citation above stays caught even if the hand-written lookbehind is
    dropped for `\\b`.
    """
    path = _readme(root, "zh")
    _write_file(path, _read_file(path)
                + u"\n\u9884\u544a\u6210C7\u3002\n")  # 预告成C7。
    return u"README.md: prose cites C7 with no space before it"


def _hide_count(lang, wrong, filler):
    """Rewrite the first card count into a form a reader still reads."""
    def apply(root):
        path = _readme(root, lang)
        text = _read_file(path)
        m = re.search(_count_pattern(lang, "cards"), text)
        if not m:
            raise AssertionError("%s README states no card count" % lang)
        _write_file(path, text[:m.start(1)] + filler % wrong + text[m.end(1):])
        return u"%s: %r -> %r" % (REGISTRY_README[lang], m.group(1),
                                  filler % wrong)
    return apply


def _break_count_hidden_by_bold(root):
    """The attack the two site invariants cannot see, and why they cannot.

    Both READMEs change in the same commit — that is this repository's own
    rule — so they are not two independent witnesses. Emboldening the SAME
    count site in both languages removes it from both site counts at once:
    the counts stay equal, neither falls to zero, the remaining sites still
    agree with the ledger, and the checker exits 0 while the README shows the
    reader a number that is wrong.
    """
    said = [_hide_count("zh", u"66", u"**%s**")(root),
            _hide_count("en", u"Sixty-six", u"**%s**")(root)]
    return u"emboldened and wrong in both READMEs: %s" % "; ".join(said)


def _break_count_hidden_by_zero_width(root):
    """The same evasion by a character that is not `\\s` to Python."""
    said = [_hide_count("zh", u"66", u"%s\u200b")(root),
            _hide_count("en", u"Sixty-six", u"%s\u200b")(root)]
    return u"zero-width space after the number in both READMEs: %s" % "; ".join(said)


def _break_both_languages_stop_counting(root):
    """Both languages stop stating the chain count in one commit.

    EVERY site goes, not just the first: the English README also carries the
    anchor inside a placeholder (`"N independent reasoning chains"`), and
    stripping one site while the real one stands is the unequal-site-count
    case, which would catch this fixture for the wrong reason.
    """
    for lang in LANGS:
        path = _readme(root, lang)
        text = _read_file(path)
        new = re.sub(_count_pattern(lang, "chains"), lambda m: m.group(2), text)
        if new == text:
            raise AssertionError("%s README states no chain count" % lang)
        _write_file(path, new)
    return u"every chain-count site removed from both READMEs"


def _break_citation_to_a_file_that_is_no_chain(root):
    """Prose cites a chain identifier, pointing at a file that is not a chain.

    The landscape file it points at opens with an ordinary title, so nothing
    in it says which chain it is — the citation asserts an identity the file
    does not carry.
    """
    path = _readme(root, "zh")
    _write_file(path, _read_file(path) + u"\n\u53c2\u89c1 [C1 \u00b7 "
                u"\u8fdc\u671f\u56fe\u666f](docs/zh/30-far.md)\u3002\n")
    return u"README.md: C1 cited as docs/zh/30-far.md, which is no chain"


def _embolden_correct_count(root):
    """Not a breakage: the right number, written in bold."""
    for lang, in (("zh",), ("en",)):
        path = _readme(root, lang)
        text = _read_file(path)
        m = re.search(_count_pattern(lang, "cards"), text)
        if not m:
            raise AssertionError("%s README states no card count" % lang)
        _write_file(path, text[:m.start(1)] + "**" + m.group(1) + "**"
                    + text[m.end(1):])
    return u"the first card count wrapped in `**` in both READMEs"


# Breakages that must be caught, each with the check tag that must report it.
NEGATIVE_CASES = [
    (u"dangling anchor", "links", _break_dangling_anchor),
    (u"dependency edge disagrees with the card", "dep-graph", _break_dep_edge),
    (u"root card's dependency edge disagrees", "dep-graph",
     _break_root_dep_edge),
    (u"card exists in zh only", "bilingual-cards",
     _break_single_language_card("en")),
    (u"card exists in en only", "bilingual-cards",
     _break_single_language_card("zh")),
    (u"confidence outside the whitelist", "confidence",
     _set_confidence("zh", u"\u6781\u9ad8")),  # 极高
    (u"second confidence value in the same card", "confidence",
     _break_second_confidence),
    (u"confidence value unreadable", "confidence",
     _break_unreadable_confidence),
    (u"one value readable, one field unreadable", "confidence",
     _break_partial_readable_confidence),
    (u"required card field missing", "card-fields", _break_missing_field),
    (u"chain file on disk, registered nowhere", "chain-registry",
     _break_unregistered_chain_file),
    (u"registry row deleted, chain file still there", "chain-registry",
     _break_registry_row_removed),
    (u"row registers one language only", "chain-registry",
     _break_registry_single_language_link),
    (u"row id is `C3 (draft)`, not a bare id", "chain-registry",
     _break_registry_id_unreadable),
    (u"registry row links a file that is not there", "chain-registry",
     _break_registry_dangling_link),
    (u"identifier registered in one README only", "chain-registry",
     _break_registry_one_sided_id),
    (u"the announced row claims an identifier", "chain-registry",
     _break_forecast_row_numbered),
    (u"registered filename breaks the `<id x 10>-` rule", "chain-registry",
     _break_chain_filename_prefix),
    (u"a shadow file rides along on an existing row", "chain-registry",
     _break_shadow_chain_file),
    (u"an unregistered chain file named `.MD`", "chain-registry",
     _break_uppercase_md_chain_file),
    (u"the same identifier registered twice", "chain-registry",
     _break_duplicate_registry_row),
    (u"prose cites an unallocated identifier", "chain-id",
     lambda root: (_write_file(
         _readme(root, "zh"),
         _read_file(_readme(root, "zh")) + u"\n\u53c2\u89c1 C7\u3002\n"),
         u"README.md: prose cites C7")[1]),
    (u"an unallocated identifier cited with no space", "chain-id",
     _break_citation_without_space),
    (u"chain linked under a title its file lacks", "chain-title",
     _break_chain_title),
    (u"one chain's file cited as another chain", "chain-title",
     _break_citation_wrong_identifier),
    (u"the registry topic names a different chain", "chain-title",
     _break_registry_topic_renamed),
    (u"the registry allocates an id with no topic", "chain-title",
     _break_registry_topic_empty),
    (u"a registered chain whose file has no H1", "chain-title",
     _break_registered_chain_without_h1),
    (u"an identifier cited for a file that is no chain", "chain-title",
     _break_citation_to_a_file_that_is_no_chain),
    (u"zh card count off by one", "readme-counts",
     _set_count("zh", "cards", "66")),
    (u"en card count off by one", "readme-counts",
     _set_count("en", "cards", "Sixty-six")),
    (u"en card count spelled unparseably", "readme-counts",
     _set_count("en", "cards", "65x")),
    (u"chain count stale in zh", "readme-counts",
     _set_count("zh", "chains", u"\u56db")),  # 四
    (u"chain count stale in en", "readme-counts",
     _set_count("en", "chains", "four")),
    (u"one language stops stating the card count", "readme-counts",
     _break_count_site_removed),
    (u"both languages stop stating the chain count", "readme-counts",
     _break_both_languages_stop_counting),
    (u"a wrong count emboldened in both languages", "readme-counts",
     _break_count_hidden_by_bold),
    (u"a wrong count hidden by a zero-width space", "readme-counts",
     _break_count_hidden_by_zero_width),
]

# Edits that must NOT be reported: the checker has to stay usable.
POSITIVE_CASES = [
    (u"prose below the last card belongs to no card", _text_after_last_card),
    (u"a second announced direction holding no number", _extra_announced_row),
    (u"prose naming cards without counting them",
     _prose_mentioning_the_anchor),
    (u"a citation that abbreviates the title it points at",
     _shorten_chain_title),
    (u"a count written in bold", _embolden_correct_count),
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
  --self-test    break a temporary copy of the tree one way at a time and
                 assert every breakage is caught by the right check, plus the
                 edits that must NOT be reported (the repository is not
                 touched). The count is printed; it is not fixed here, because
                 a number in prose goes stale the moment a case is added."""


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
