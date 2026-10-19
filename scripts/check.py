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
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("zh", "en")
# The dependency graph uses a full-width arrow in Chinese and ASCII in English.
GRAPH_ARROW = {"zh": u"\u2190", "en": "<-"}
CONFIDENCE = {
    "zh": {u"\u9ad8", u"\u4e2d", u"\u4f4e", u"\u4f4e\uff08\u4ec5\u56fe\u666f\uff09"},
    "en": {"High", "Medium", "Low", "Low (landscape only)"},
}
CONFIDENCE_FIELD = {"zh": u"\u7f6e\u4fe1\u5ea6", "en": "Confidence"}
AUDIENCE_FIELD = {"zh": u"\u53d7\u4f17\u89c4\u6a21", "en": "Audience scale"}
SUMMARY_LABEL = {"zh": u"摘要", "en": "Summary"}
FULL_CARD_LABEL = {"zh": u"完整卡", "en": "Full card"}
SUMMARY_TEXT = {"zh": u"完整卡见台账", "en": "See the Full card in the ledger"}
# J-001..J-086 predate the audience-scale requirement. They stay readable
# during migration, but every later card must carry the field. Freezing the
# boundary by identifier rather than by today's file contents means deleting a
# legacy card cannot silently redefine what counts as "new".
LEGACY_AUDIENCE_SCALE_MAX = 86
# The WHOLE field value is read, up to end of line. Truncating it at the first
# `。` / `.` / `(` / `（` — which is what this used to do — meant only a prefix
# was ever compared, so `中（偏高）` and `Medium (leaning high).` passed while
# the bare `中高` was caught: the same invented grade, waved through by writing
# it in brackets.
CONFIDENCE_VALUE = (r"\*\*(?:Confidence|\u7f6e\u4fe1\u5ea6)\*\*[:\uff1a]"
                    r"\s*([^\n]*)")
# The canonical values include the only allowed landscape qualifier. Punctuation
# is not optional: sentence-final periods are rejected to keep one spelling per
# field across both ledgers.
CARD_FIELDS = {
    "zh": [u"\u63d0\u51fa\u65e5\u671f", u"\u4e00\u53e5\u8bdd\u5224\u65ad", u"\u53d7\u4f17\u89c4\u6a21", u"\u900f\u955c",
           u"\u63a8\u7406\u94fe", u"\u65f6\u95f4\u7a97", u"\u8bc1\u4f2a\u6761\u4ef6",
           u"\u9886\u5148\u6307\u6807", u"\u7f6e\u4fe1\u5ea6", u"depends-on",
           u"\u6700\u5f3a\u53cd\u65b9", u"\u4e0e\u5171\u8bc6", u"\u5916\u90e8\u5bf9\u7167\u6765\u6e90",
           u"\u51fa\u5904", u"\u4e0b\u6b21\u68c0\u67e5\u65e5", u"\u72b6\u6001"],
    "en": ["Proposed date", "One-sentence judgment", "Audience scale", "Lens", "Reasoning chain",
           "Time window", "Falsifier", "Leading indicator", "Confidence", "depends-on",
           "Strongest opposing mechanism", "Against consensus",
           "External comparison source", "Source", "Next review", "Status"],
}

failures = []
warnings = []


def fail(check, detail):
    failures.append((check, detail))


def warn(check, detail):
    warnings.append((check, detail))


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


ROOT_MARKDOWN = ("README.md", "README.en.md",
                 "CONTRIBUTING.md", "CONTRIBUTING.en.md")


def markdown_files():
    """Every markdown file whose links are checked.

    `docs/` plus the top-level pair files. CONTRIBUTING is in here for the same
    reason the READMEs are: it is almost entirely links INTO the ledger and the
    methodology — it is where a stranger is told which heading defines
    `证伪条件`, `置信度` and the status words — so a link that stops landing
    sends the one reader who came to argue to a 404.
    """
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO, "docs")):
        for f in sorted(files):
            if is_markdown(f):
                out.append(os.path.relpath(os.path.join(root, f), REPO))
    for f in ROOT_MARKDOWN:
        if os.path.exists(os.path.join(REPO, f)):
            out.append(f)
    return out


def check_public_internal_ids(files):
    """Public Markdown must not expose internal work-unit identifiers.

    `wu-*` values are production-line handles, not public anchors: GitHub
    readers cannot resolve them and their lifecycle is not part of the
    repository's public contract. Keep the scan on the same Markdown surface
    used by the link checks so a newly added public page cannot bypass it.
    """
    pattern = re.compile(r"\bwu-[0-9a-fA-F-]{8,}\b")
    for path in files:
        text = read(path)
        match = pattern.search(text)
        if match:
            fail("public-internal-ids",
                 "%s:%d exposes %s" %
                 (path, text.count("\n", 0, match.start()) + 1,
                  match.group(0)))


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


TABLE_DELIMITER = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")


def check_table_rows(files):
    """Every pipe row is a row GitHub actually renders inside a table.

    A GFM table ends at the first blank line. Rows written after one are not
    a second table (they have no header and delimiter row): GitHub renders
    the whole run as a single paragraph of literal `|` text. The ledger
    overview parser below reads every `|` line in its section regardless, so
    a blank line inside the overview kept every count, dependency and parity
    check green while J-098–J-102 (zh) and J-099–J-102 (en) were unreadable
    on the published page. This check closes that parser/renderer gap: a run
    of pipe lines that does not open with a header row followed by a
    delimiter row, and is not the continuation of one, fails.

    Not covered: tables inside blockquotes (`> | ... |`) and fenced code,
    which GitHub does not render as top-level tables either way.
    """
    for path in files:
        lines = read(path).split("\n")
        fence = in_table = orphan = False
        for i, line in enumerate(lines):
            s = line.strip()
            if s.startswith("```") or s.startswith("~~~"):
                fence = not fence
                in_table = orphan = False
                continue
            if fence:
                continue
            if not s.startswith("|"):
                in_table = orphan = False
                continue
            if in_table or orphan:
                continue
            following = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if TABLE_DELIMITER.match(following):
                in_table = True
                continue
            orphan = True
            fail("table-rows",
                 "%s:%d pipe rows outside any table (a blank line split the "
                 "table above, or the header/delimiter row is missing); "
                 "GitHub renders them as literal text: %s"
                 % (path, i + 1, s[:60]))


LEDGER_ROOT = "docs/%s/90-ledger.md"
LEDGER_SHARD_DIR = "docs/%s/ledger"


def ledger_paths(lang):
    """The governance root followed by stable-numbered card shards."""
    root = LEDGER_ROOT % lang
    shard_dir = LEDGER_SHARD_DIR % lang
    shards = []
    if os.path.isdir(os.path.join(REPO, shard_dir)):
        for name in sorted(os.listdir(os.path.join(REPO, shard_dir))):
            if is_markdown(name):
                shards.append(os.path.join(shard_dir, name).replace(os.sep, "/"))
    return [root] + shards


def check_mermaid_projection(lang, root, cards):
    """Mermaid edges may only project authoritative card dependencies.

    The diagram is intentionally a partial, reader-friendly projection, so it
    need not enumerate every edge. It must never invent one: in `source -->
    target`, the target card must declare source in its `depends-on` field.
    """
    edges = re.findall(r"^\s*(J-?\d{3})\s*-->\s*(J-?\d{3})\s*$", root, re.M)
    for source, target in edges:
        source = source.replace("J", "J-") if "J-" not in source else source
        target = target.replace("J", "J-") if "J-" not in target else target
        if source not in cards or target not in cards:
            fail("mermaid-graph", "%s: %s --> %s names a card absent from shards"
                 % (lang, source, target))
            continue
        body = cards[target]
        m = re.search(r"\*\*depends-on\*\*[:：]\s*([^\n]*)", body)
        declared = set(re.findall(r"J-\d{3}", m.group(1) if m else ""))
        if source not in declared:
            fail("mermaid-graph", "%s: %s --> %s is not an authoritative depends-on edge"
                 % (lang, source, target))


def parse_ledger(lang):
    root = read(LEDGER_ROOT % lang)
    cards = {}
    card_files = {}
    for path in ledger_paths(lang)[1:]:
        text = read(path)
        parts = list(re.finditer(r"^### (J-\d{3})([^\n]*)$", text, re.M))
        for i, match in enumerate(parts):
            end = parts[i + 1].start() if i + 1 < len(parts) else len(text)
            section = re.search(r"^## ", text[match.end():end], re.M)
            if section:
                end = match.end() + section.start()
            jid = match.group(1)
            if jid in cards:
                fail("ledger", "docs/%s: %s has more than one card (including %s)"
                     % (lang, jid, path))
            cards[jid] = text[match.start():end]
            card_files[jid] = path
    if re.search(r"^### J-\d{3}", root, re.M):
        fail("ledger", "%s contains a level-3 card; complete cards belong in ledger/"
             % (LEDGER_ROOT % lang))
    stubs = {}
    for match in re.finditer(r"^#### (J-\d{3})([^\n]*)$", root, re.M):
        jid = match.group(1)
        end = re.search(r"^####? ", root[match.end():], re.M)
        body = root[match.end(): match.end() + end.start() if end else len(root)]
        if jid in stubs:
            fail("ledger", "%s: %s has more than one compatibility stub"
                 % (LEDGER_ROOT % lang, jid))
        stubs[jid] = (match.group(2), body)
    expected = set(cards)
    if set(stubs) != expected:
        fail("ledger-stubs", "%s stubs %d do not match shard cards %d (difference: %s)"
             % (lang, len(stubs), len(cards), sorted(set(stubs) ^ expected)))
    for jid, (title, body) in stubs.items():
        path = card_files.get(jid)
        if not path:
            continue
        link = re.search(r"\]\(([^)#]+)#([^\s)]+)\)", body)
        if not link:
            fail("ledger-stubs", "%s %s has no link to its complete shard card"
                 % (lang, jid))
            continue
        target, anchor = link.group(1), link.group(2)
        expected_target = os.path.basename(path)
        if target != "ledger/" + expected_target:
            fail("ledger-stubs", "%s %s links %s, expected ledger/%s"
                 % (lang, jid, target, expected_target))
        heading = re.search(r"^### %s([^\n]*)$" % jid, cards[jid], re.M)
        if not heading or anchor != slug(jid + heading.group(1)):
            fail("ledger-stubs", "%s %s link anchor does not match its shard heading"
                 % (lang, jid))
        if not title.strip() or not heading or title.strip() != heading.group(1).strip():
            fail("ledger-stubs", "%s %s stub title does not match its shard heading"
                 % (lang, jid))
        objective = re.search(r"^- \*\*(?:一句话判断|One-sentence judgment)\*\*[:：]\s*([^\n]*)$",
                              cards[jid], re.M)
        if not objective or objective.group(1).strip() not in body:
            fail("ledger-stubs", "%s %s stub has no matching one-sentence judgment"
                 % (lang, jid))
    graph = {}
    graph_rows = []
    pattern = r"^(J-\d{3})\s*%s\s*([^\n]*)$" % re.escape(GRAPH_ARROW[lang])
    for m in re.finditer(pattern, root, re.M):
        graph_rows.append(m.group(1))
        graph[m.group(1)] = set(re.findall(r"J-\d{3}", m.group(2)))
    for m in re.finditer(r"^(J-\d{3})\s+\(root\)$", root, re.M):
        graph_rows.append(m.group(1))
        graph.setdefault(m.group(1), set())
    overview = {}
    overview_rows = []
    overview_section = (re.search(r"^## (?:2\.|二、).*?(?=^## (?:3\.|三、))",
                                  root, re.M | re.S))
    overview_text = overview_section.group(0) if overview_section else ""
    for line in overview_text.split("\n"):
        m = re.match(r"^\|\s*\[(J-\d{3})\]\([^)]*\)\s*\|", line)
        if not m:
            continue
        overview_rows.append(m.group(1))
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 8:
            continue
        overview.setdefault(m.group(1), set(re.findall(r"J-\d{3}", cols[6])))
    expected = set(cards)
    for name, present in (("graph", set(graph_rows)), ("overview", set(overview_rows))):
        missing = sorted(expected - present)
        extra = sorted(present - expected)
        if missing or extra:
            fail("%s-rows" % name, "%s %s rows differ from shards (missing %s; extra %s)"
                 % (lang, name, missing, extra))
    graph_duplicates = sorted(jid for jid in set(graph_rows)
                             if graph_rows.count(jid) > 1)
    if graph_duplicates:
        fail("graph-rows", "%s duplicate dependency-graph rows: %s"
             % (lang, graph_duplicates))
    overview_duplicates = sorted(jid for jid in set(overview_rows)
                                 if overview_rows.count(jid) > 1)
    if overview_duplicates:
        fail("overview-rows", "%s duplicate overview rows: %s" % (lang, overview_duplicates))
    overview_consensus = {}
    for line in overview_text.split("\n"):
        m = re.match(r"^\|\s*\[(J-\d{3})\]\([^)]*\)\s*\|", line)
        if not m:
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 10:
            continue
        overview_consensus.setdefault(m.group(1), cols[8])
    check_mermaid_projection(lang, root, cards)
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
    """Human-readable description of the canonical field values."""
    return " / ".join(sorted(CONFIDENCE[lang]))


def confidence_is_whitelisted(lang, raw):
    """True only when the complete field value is a canonical value.

    Field punctuation is deliberately part of the schema: card values use no
    sentence-final period. This prevents `中。`, `High.`, and equivalent
    formatting drift from silently creating a second spelling of the field.
    """
    return raw.strip() in CONFIDENCE[lang]

def audience_scale_value(body, lang):
    """Return a standalone Audience scale field value, or None.

    Anchoring the bullet at line start is intentional: bolding the words inside
    Diffusion-gate review must not satisfy the separate-field contract.
    """
    field = re.escape(AUDIENCE_FIELD[lang])
    m = re.search(r"^- \*\*%s\*\*[:\uff1a]\s*([^\n]+)$" % field, body, re.M)
    return m.group(1).strip() if m else None


def audience_scale_is_structured(value, lang):
    """Mechanical floor: magnitude plus ceiling/enablement classification."""
    if not value:
        return False
    if lang == "zh":
        magnitude = re.search(u"(?:\u5341\u4e07|\u767e\u4e07|\u5343\u4e07|\u5341\u4ebf|\u4ebf)\u91cf\u7ea7", value)
        mode = (u"\u63d0\u9ad8\u65e2\u6709\u4e13\u4e1a\u8005\u4e0a\u9650" in value or
                u"\u8ba9\u539f\u672c\u4e0d\u4f1a\u7684\u4eba\u4e5f\u80fd\u505a" in value)
    else:
        magnitude = re.search(r"(?:hundred-thousand|million|tens-of-millions|"
                              r"hundred-millions|billion)-scale", value, re.I)
        lowered = value.lower().replace("’", "'")
        mode = ("raises existing professionals' ceiling" in lowered or
                "lets people who could not do it do it now" in lowered)
    # A magnitude at offset zero means no affected group precedes it. Requiring
    # some non-punctuation text before the bucket gives the checker a modest,
    # language-neutral identity floor without pretending to judge the group.
    identity = bool(magnitude and re.search(r"[\w\u4e00-\u9fff]", value[:magnitude.start()]))
    return bool(magnitude and identity and mode)


def check_ledger(lang):
    cards, graph, overview, overview_consensus = parse_ledger(lang)
    if not cards:
        fail("ledger", "%s: no judgment cards found" % lang)
        return cards
    legacy_audience_missing = []
    for jid in sorted(cards):
        body = cards[jid]
        missing = [f for f in CARD_FIELDS[lang]
                   if ("**%s**" % f) not in body]
        if missing:
            fail("card-fields", "%s %s missing %s" % (lang, jid, ", ".join(missing)))
        audience = AUDIENCE_FIELD[lang]
        audience_value = audience_scale_value(body, lang)
        if audience_value is None:
            number = int(jid.split("-")[1])
            detail = "%s %s missing standalone %s field" % (lang, jid, audience)
            if number <= LEGACY_AUDIENCE_SCALE_MAX:
                legacy_audience_missing.append(jid)
            else:
                fail("audience-scale", detail)
        elif not audience_scale_is_structured(audience_value, lang):
            fail("audience-scale", "%s %s: %s must state an allowed magnitude "
                 "and ceiling-versus-enablement classification" %
                 (lang, jid, audience))
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
    if legacy_audience_missing:
        warn("audience-scale", "%s: %d legacy card(s) through J-%03d still "
             "lack %s; new cards fail hard" %
             (lang, len(legacy_audience_missing), LEGACY_AUDIENCE_SCALE_MAX,
              AUDIENCE_FIELD[lang]))
    check_comparison(lang, cards, overview_consensus)
    return cards




def _summary_link_labels(lang):
    labels = {SUMMARY_LABEL[lang], FULL_CARD_LABEL[lang]}
    if lang == "zh":
        labels.add(u"台账")
    return labels


def _field_value(body, lang, field):
    """Return one reader-visible card field value, or None when absent."""
    matches = _field_occurrences(body, lang, field)
    return matches[0] if len(matches) == 1 else None


def _embedded_heading_level(raw):
    """Return the reader-visible ATX/HTML heading level, or None."""
    line = raw.strip()
    previous = None
    while line != previous:
        previous = line
        line = re.sub(r"^(?:>\s*)+", "", line)
        line = re.sub(r"^(?:<(?!h[1-6]\b)[A-Za-z][\w-]*(?:\s[^>]*)?>\s*)+", "", line, flags=re.I)
        line = re.sub(r"\s*</(?:blockquote|div|section|aside)>\s*$", "", line, flags=re.I)
        line = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", line)
    match = re.match(r"^#{1,6}(?= )", line)
    if match:
        return len(match.group(0))
    match = re.match(r"^<h([1-6])(?:\s[^>]*)?>", line, re.I)
    return int(match.group(1)) if match else None


def _embedded_card_sections(path, lang):
    """Yield formal card blocks embedded in a registered chain page.

    A block is considered formal when its heading is level 3 and its body carries
    at least one canonical card field. The heading is then validated separately:
    exactly one J-xxx id is required. Scanning by fields first is deliberate: a
    card heading with its id removed must be rejected, not silently treated as
    ordinary prose.
    """
    text = read(path)
    headings = [match for match in re.finditer(r"^.*$", text, re.M)
                if _embedded_heading_level(match.group(0)) is not None]
    for index, match in enumerate(headings):
        heading_text = match.group(0)
        heading_level = _embedded_heading_level(heading_text)
        if heading_level is None:
            continue
        # A formal card may contain explanatory subheadings. End its block at
        # the next heading of the same or a higher level, not at an arbitrary
        # nested heading that would otherwise split the reader-visible copy.
        end = len(text)
        for following in headings[index + 1:]:
            following_level = _embedded_heading_level(following.group(0))
            if following_level is not None and following_level <= heading_level:
                end = following.start()
                break
        section = text[match.start():end]
        heading = visible(heading_text)
        # Only a heading that advertises a judgment-card block is formal. A
        # normal prose section can contain bullets such as ``证伪条件`` or
        # ``领先指标`` without becoming an embedded copy; the card-id/missing-id
        # checks are still exercised by the explicit "判断卡片" heading marker.
        formal_heading = (re.search(r"J-\d{3}", heading) is not None or
                          re.search(r"判断卡片|Judgment card", heading,
                                    re.I) is not None)
        if not formal_heading:
            continue
        has_card_field = any(_field_occurrences(section, lang, field)
                             for field in CARD_FIELDS[lang])
        has_summary_marker = bool(re.search(
            r"^\s*(?:[-*+]\s+|\d+[.)]\s+)\*\*(?:摘要|Summary)\*\*[:：]", section, re.M))
        has_summary_link = any(
            link.group(1).strip() in _summary_link_labels(lang)
            for link in re.finditer(r"\[([^]]+)\]\(([^)]+)\)", section))
        if not has_card_field and not has_summary_marker and not has_summary_link:
            continue
        heading_ids = re.findall(r"(?<![A-Za-z0-9])J-\d{3}(?=$|[\s\]\)·—–,:：,，])",
                                 visible(match.group(0)))
        jid = heading_ids[0] if len(heading_ids) == 1 else None
        yield (jid, match.start(), section)


def _ledger_card_location(lang, jid):
    """Return the shard path and 1-based line of a ledger card."""
    for path in ledger_paths(lang)[1:]:
        text = read(path)
        match = re.search(r"^### %s(?:[^\n]*)$" % re.escape(jid), text, re.M)
        if match:
            return path, text.count("\n", 0, match.start()) + 1
    return None, None


def _summary_link_target(section, lang, jid):
    """Return the resolved ledger target named by an explicit summary link."""
    labels = _summary_link_labels(lang)
    for match in re.finditer(r"\[([^]]+)\]\(([^)]+)\)", section):
        if match.group(1).strip() not in labels:
            continue
        raw_target = match.group(2)
        target, anchor = raw_target.split("#", 1) if "#" in raw_target else (raw_target, "")
        return target, anchor
    return None


def _field_occurrences(body, lang, field):
    """Return all reader-visible occurrences of one canonical card field.

    Normalize Markdown list/blockquote wrappers and equivalent HTML list/bold
    wrappers before comparing labels. The caller has already constrained the
    body to a formal card block, so this reader-visible normalization does not
    make ordinary prose a card.
    """
    separator = r"\s*[:：]"
    pattern = re.compile(
        r"^(?:\*\*([^*\n]+)\*\*|<(?:strong|b)\b[^>]*>([^<\n]+)</(?:strong|b)>)"
        r"%s\s*(.*)$" % separator, re.I)
    values = []
    for raw_line in body.splitlines():
        line = raw_line
        previous = None
        while line != previous:
            previous = line
            line = re.sub(r"^\s*(?:>\s*)+", "", line)
            line = re.sub(
                r"^\s*(?:<(?!h[1-6]\b|strong\b|b\b)[A-Za-z][\w-]*(?:\s[^>]*)?>\s*)+",
                "", line, flags=re.I)
            line = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", line)
            line = re.sub(
                r"\s*(?:</(?:[A-Za-z][\w-]*)>\s*)+$", "", line, flags=re.I)
        match = pattern.match(line)
        if not match:
            continue
        label = match.group(1) or match.group(2)
        value = match.group(3)
        if visible(label).strip() == field:
            values.append(visible(value).strip())
    return values


def check_english_chain_punctuation(registry):
    """Reject Chinese sentence separators accidentally copied into English chains."""
    for paths in registry["en"].values():
        for path in paths:
            if not path.startswith("docs/en/"):
                continue
            text = read(path)
            if "；" in text:
                fail("english-punctuation", "%s contains Chinese semicolon" % path)


def check_chain_card_parity(registry, per_lang_cards):
    """Enumerate and validate formal chain-page card copies.

    A copy is either a full form (all canonical fields, compared after
    ``visible()``) or an explicit summary form carrying a link labelled
    ``完整卡`` / ``Full card`` to this language's ledger card. Anything that
    looks like a card block but matches neither form fails hard.
    """
    counts = {}
    inventories = {}
    for lang in LANGS:
        seen = set()
        paths = sorted(p for rows in registry[lang].values() for p in rows
                       if p.startswith("docs/%s/" % lang))
        for path in paths:
            if path in seen or not os.path.exists(os.path.join(REPO, path)):
                continue
            seen.add(path)
            for jid, offset, section in _embedded_card_sections(path, lang):
                line = read(path).count("\n", 0, offset) + 1
                ledger_body = per_lang_cards[lang].get(jid)
                ledger_path, ledger_line = (_ledger_card_location(lang, jid)
                                            if jid is not None else (None, None))
                print("embedded %s %s:%d %s -> %s:%s" %
                      (lang, path, line, jid, ledger_path or "(missing)",
                       ledger_line or "?"))
                counts[lang] = counts.get(lang, 0) + 1
                inventories.setdefault(lang, set()).add((
                    path[len("docs/%s/" % lang):], jid))
                location = "%s:%d %s" % (path, line, jid or "(missing card id)")
                if ledger_body is None or not ledger_path:
                    if jid is None:
                        fail("chain-card-parity", "%s formal card block heading must contain exactly one J-xxx id" % location)
                    else:
                        fail("chain-card-parity", "%s has no matching ledger card" % location)
                    continue
                field_values = {field: _field_occurrences(section, lang, field)
                                for field in CARD_FIELDS[lang]}
                duplicate_fields = [field for field, values in field_values.items()
                                    if len(values) > 1]
                if duplicate_fields:
                    fail("chain-card-parity",
                         "%s repeats canonical fields %s; use one complete copy" %
                         (location, duplicate_fields))
                    continue
                if all(len(values) == 1 for values in field_values.values()):
                    for field in CARD_FIELDS[lang]:
                        chain_value = field_values[field][0]
                        ledger_value = _field_value(ledger_body, lang, field)
                        if chain_value != ledger_value:
                            fail("chain-card-parity",
                                 "%s field %s differs from %s:%d (chain=%r; ledger=%r)" %
                                 (location, field, ledger_path, ledger_line,
                                  chain_value, ledger_value))
                    continue
                summary_marker = bool(re.search(
                    r"^\s*(?:[-*+]\s+|\d+[.)]\s+)\*\*%s\*\*[:：]" % re.escape(SUMMARY_LABEL[lang]),
                    section, re.M))
                summary_values = _field_occurrences(section, lang, SUMMARY_LABEL[lang])
                if (not summary_marker or len(summary_values) != 1 or
                        summary_values[0] != SUMMARY_TEXT[lang]):
                    fail("chain-card-parity",
                         "%s summary must be exactly %r" %
                         (location, SUMMARY_TEXT[lang]))
                    continue
                link = _summary_link_target(section, lang, jid)
                present_fields = [field for field, values in field_values.items()
                                  if values]
                if present_fields:
                    fail("chain-card-parity",
                         "%s summary form carries canonical fields %s; use a complete copy" %
                         (location, present_fields))
                    continue
                if not summary_marker or not link:
                    fail("chain-card-parity",
                         "%s is neither a complete field copy nor an explicit summary" %
                         location)
                    continue
                target, anchor = link
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target)).replace(os.sep, "/")
                heading = re.search(r"^### %s([^\n]*)$" % re.escape(jid), ledger_body, re.M)
                expected_anchor = slug(jid + heading.group(1)) if heading else ""
                if resolved != ledger_path or anchor != expected_anchor:
                    fail("chain-card-parity",
                         "%s summary link %s#%s does not target %s#%s" %
                         (location, resolved, anchor, ledger_path, expected_anchor))
        print("embedded card copies (%s): %d" % (lang, counts.get(lang, 0)))
    zh_only = inventories.get("zh", set()) - inventories.get("en", set())
    en_only = inventories.get("en", set()) - inventories.get("zh", set())
    if zh_only or en_only:
        fail("chain-card-parity",
             "bilingual embedded-card inventory differs: zh-only=%s en-only=%s" %
             (sorted(zh_only), sorted(en_only)))
    return counts


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

# Markup a reader does not see: emphasis and code markers, and HTML comments.
#
# Why the count check must strip these before reading anything. The two site
# invariants below (equal site counts, never both zero) assume the two READMEs
# are two independent witnesses — and they are not: this repository's own rule
# is that both trees change in the SAME commit. So a hand that writes
# `**66**张判断卡片` / `**Sixty-six** judgment cards` removes that site from
# both languages at once: the site counts stay equal, neither falls to zero,
# the other sites still read 65, and the checker exits 0 while the README shows
# a reader `66`. Verified by hand on 2026-09-19 against commit `aadb15d`.
#
# The class is "anything a reader still reads as a number, sitting between the
# number and its anchor, that a plain regex breaks on" — NOT a list of the
# characters that have been tried. The first attempt here was such a list, and
# a review broke it the same day with `[66](docs/zh/90-ledger.md) 张判断卡片`
# — the most natural edit in a README whose counts already sit beside links.
# So: comments, then links reduced to their text, then inline HTML tags, then
# every Cf character (U+200B/200C/200D/2060/FEFF/00AD at once), then NFKC so
# full-width digits are the digits they render as.
INVISIBLE = re.compile(u"<!--[\\s\\S]*?-->|[`*_]")
# The same reduction `slug()` performs on headings, reused rather than
# reinvented: a link is its text to a reader.
LINK_TEXT = re.compile(r"\[([^\]]*)\]\([^)]*\)")
# `<b>66</b>` renders bold. The leading character class keeps this off the
# repository's own prose about filenames (`<编号×10>-<英文 slug>.md`).
HTML_TAG = re.compile(r"</?[A-Za-z][^>]*>")


def visible(text):
    """The text as a reader sees it, with invisible markup removed."""
    t = INVISIBLE.sub("", text)
    t = LINK_TEXT.sub(r"\1", t)
    t = HTML_TAG.sub("", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Cf")
    return unicodedata.normalize("NFKC", t)


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




# ---------------------------------------------------------------------------
# Mermaid projections in chain pages and the eight copied navigation maps.
# These diagrams are deliberately only checked for the mechanical layer: a
# graph must parse, cite real cards, and have the same bilingual skeleton. The
# prose remains the authority for whether an arrow is a sound argument.
# ---------------------------------------------------------------------------

MERMAID_BLOCK = re.compile(r"^[ \t>]*```mermaid[^\n]*\n(?P<body>.*?)(?=^[ \t>]*```)",
                           re.M | re.S)
MERMAID_CARD = re.compile(r"(?<![0-9A-Za-z])J-\d{3}(?![0-9])")
MERMAID_EDGE = re.compile(
    r"^([A-Za-z][A-Za-z0-9_-]*)(?:\[[^\]]*\]|\{[^}]*\})?"
    r"\s*(-->|-.+?->)\s*(?:\|[^|]*\|\s*)?"
    r"([A-Za-z][A-Za-z0-9_-]*)(?:\[[^\]]*\]|\{[^}]*\})?$")
MERMAID_NODE = re.compile(
    r"^([A-Za-z][A-Za-z0-9_-]*)(\[[^\]]*\]|\{[^}]*\})$")
MERMAID_FLOW = re.compile(r"^flowchart\s+(?:LR|RL|TB|TD|BT)\s*$")
NAV_FILES = (
    "README.md", "README.en.md",
    "docs/zh/10-near.md", "docs/zh/20-mid.md", "docs/zh/30-far.md",
    "docs/en/10-near.md", "docs/en/20-mid.md", "docs/en/30-far.md",
)
NAV_CHAIN_IDS = {"C%d" % n for n in range(1, 14)}


def _mermaid_line(raw):
    """Remove the optional blockquote marker used by some quoted fences."""
    return re.sub(r"^\s*>\s?", "", raw).strip()


def _parse_mermaid(path, text, kind):
    """Return parsed Mermaid blocks, recording every syntax failure."""
    matches = list(MERMAID_BLOCK.finditer(text))
    if not matches:
        fail(kind, "%s: no Mermaid block found" % path)
        return []
    parsed = []
    for index, match in enumerate(matches, 1):
        start_line = text[:match.start()].count("\n") + 1
        lines = []
        for offset, raw in enumerate(match.group("body").splitlines()):
            line = _mermaid_line(raw)
            if line and not line.startswith("%%"):
                lines.append((start_line + offset + 1, line))
        if not lines or not MERMAID_FLOW.match(lines[0][1]):
            fail(kind, "%s:%d: Mermaid block %d has no valid flowchart declaration"
                 % (path, start_line, index))
            continue
        nodes = []
        node_shapes = {}
        edges = []
        malformed = False
        for line_no, line in lines[1:]:
            if line == "end" or line.startswith("subgraph "):
                continue
            edge = MERMAID_EDGE.match(line)
            if edge:
                source, arrow, target = edge.groups()
                shape_matches = list(re.finditer(
                    r"([A-Za-z][A-Za-z0-9_-]*)(\[|\{)", line))
                for shape_match in shape_matches:
                    node_id, opener = shape_match.groups()
                    if node_id not in node_shapes:
                        node_shapes[node_id] = opener
                        nodes.append(node_id)
                for node_id in (source, target):
                    if node_id not in node_shapes:
                        node_shapes[node_id] = ""
                        nodes.append(node_id)
                edges.append((source, "-->" if arrow.startswith("-->") else "-.->", target))
                continue
            node = MERMAID_NODE.match(line)
            if node:
                node_id, shape = node.groups()
                if node_id not in node_shapes:
                    node_shapes[node_id] = shape[0]
                    nodes.append(node_id)
                continue
            # A line that is neither a declaration nor an edge is not a graph
            # we can safely check. In particular, never skip a malformed label.
            fail(kind, "%s:%d: Mermaid block %d cannot parse line %r"
                 % (path, line_no, index, line))
            malformed = True
        if malformed:
            continue
        cards = sorted(set(MERMAID_CARD.findall(match.group("body"))))
        parsed.append({"path": path, "start": start_line, "nodes": nodes,
                       "shapes": node_shapes, "edges": edges, "cards": cards})
    return parsed


def _mermaid_skeleton(block):
    """Labels are reader-language text; ids, shapes, and edges are structure."""
    return (tuple((node, block["shapes"].get(node, "")) for node in block["nodes"]),
            tuple(block["edges"]))



def title_of(path):
    """(identifier, title) from a chain file's H1, or a reported failure."""
    h1 = re.search(r"^#\s+(.*)$", read(path), re.M)
    if not h1:
        return None, None
    head = CHAIN_H1.match("# " + h1.group(1).strip())
    if not head:
        return None, h1.group(1).strip()
    return head.group(1), head.group(2)


def check_chain_mermaid(registry, cards):
    """Check all registered chain diagrams and the zh/en skeleton pairs."""
    for cid in sorted(registry["zh"]):
        if int(cid[1:]) > 13:
            continue  # the first 13 registered chains are the Mermaid-paired set
        zh_paths = [p for p in registry["zh"][cid] if p.startswith(CHAIN_DIR % "zh")]
        en_paths = [p for p in registry["en"][cid] if p.startswith(CHAIN_DIR % "en")]
        if len(zh_paths) != 1 or len(en_paths) != 1:
            continue  # registry checks already report the cardinality failure
        parsed = {}
        for lang, path in (("zh", zh_paths[0]), ("en", en_paths[0])):
            if not os.path.exists(os.path.join(REPO, path)):
                continue  # chain-registry reports the missing file
            parsed[lang] = _parse_mermaid(path, read(path), "chain-mermaid")
            for block in parsed[lang]:
                for jid in block["cards"]:
                    if jid not in cards[lang]:
                        fail("chain-mermaid", "%s:%d: Mermaid cites %s, which has no %s card"
                             % (path, block["start"], jid, lang))
        if len(parsed) != 2:
            continue  # chain-registry reports the missing side
        if len(parsed["zh"]) != len(parsed["en"]):
            fail("chain-mermaid", "%s/%s: Mermaid block count differs (%d vs %d)"
                 % (zh_paths[0], en_paths[0], len(parsed["zh"]), len(parsed["en"])))
            continue
        for index, (zh_block, en_block) in enumerate(zip(parsed["zh"], parsed["en"]), 1):
            if _mermaid_skeleton(zh_block) != _mermaid_skeleton(en_block):
                fail("chain-mermaid", "%s block %d and %s block %d have different ids/shapes/edges"
                     % (zh_paths[0], index, en_paths[0], index))
    print("chain Mermaid     : checked all registered zh/en chain block pairs")


def _navigation_projection(path, text):
    blocks = _parse_mermaid(path, text, "navigation-mermaid")
    if len(blocks) != 1:
        fail("navigation-mermaid", "%s: expected exactly one navigation Mermaid block, got %d"
             % (path, len(blocks)))
        return None
    block = blocks[0]
    if path.startswith("docs/"):
        for source, _arrow, target in block["edges"]:
            if re.match(r"^C\d+$", target) and source not in ("N", "M"):
                fail("navigation-mermaid", "%s:%d: chain node %s has invalid source layer %s"
                     % (path, block["start"], target, source))
    chain_nodes = {node for node in block["nodes"] if re.match(r"^C\d+$", node)}
    raw_layers = [(source, target) for source, _arrow, target in block["edges"]
                  if source in ("N", "M") and re.match(r"^C\d+$", target)]
    seen_targets = {}
    for source, target in raw_layers:
        if target in seen_targets:
            relation = "conflicting" if seen_targets[target] != source else "duplicate"
            fail("navigation-mermaid", "%s:%d: %s N/M source edge for %s (%s and %s)"
                 % (path, block["start"], relation, target, seen_targets[target], source))
        else:
            seen_targets[target] = source
    layers = sorted(raw_layers)
    return chain_nodes, layers


def check_navigation_mermaid():
    """The eight hand-copied maps share chain nodes and N/M source layers."""
    projections = []
    for path in NAV_FILES:
        if not os.path.exists(os.path.join(REPO, path)):
            fail("navigation-mermaid", "%s: navigation file does not exist" % path)
            continue
        projection = _navigation_projection(path, read(path))
        if projection is not None:
            projections.append((path, projection))
    if len(projections) != len(NAV_FILES):
        return
    expected_nodes = projections[0][1][0]
    if expected_nodes != NAV_CHAIN_IDS:
        fail("navigation-mermaid", "%s: expected chain node set %s, got %s"
             % (projections[0][0], sorted(NAV_CHAIN_IDS), sorted(expected_nodes)))
    # README's story graph intentionally has no N/M scaffolding. The six
    # time-layer pages do, and all explicit layer projections must agree.
    expected_layers = None
    for path, (nodes, layers) in projections:
        if nodes != expected_nodes:
            fail("navigation-mermaid", "%s: chain node set %s differs from %s"
                 % (path, sorted(nodes), sorted(expected_nodes)))
        if layers:
            if expected_layers is None:
                expected_layers = layers
            elif layers != expected_layers:
                fail("navigation-mermaid", "%s: N/M source layers %s differ from %s"
                     % (path, layers, expected_layers))
        elif path.startswith("docs/"):
            fail("navigation-mermaid", "%s: time-layer map has no N/M source layers" % path)
    print("navigation Mermaid: checked %d copied maps (node set + explicit N/M layers)"
          % len(projections))


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


DIMENSION_GRADES = {
    "zh": (u"已覆盖", u"部分覆盖", u"尚未建立入口"),
    "en": ("Covered", "Partially covered", "No entry yet"),
}
DIMENSION_README_HEADING = {
    "zh": u"### 全景覆盖矩阵（当前边界）",
    "en": "### Coverage matrix (current boundary)",
}
DIMENSION_LEDGER_HEADING = {
    "zh": u"## 六、未覆盖维度缺口清单",
    "en": "## 6. Explicit gaps: dimensions not yet covered",
}


def _dimension_tables(text, heading, stop_heading, status_column):
    """Return (name, status) rows from the dimension section's tables."""
    start = text.find(heading)
    if start < 0:
        raise ValueError("missing heading %s" % heading)
    end = text.find(stop_heading, start + len(heading))
    if end < 0:
        end = len(text)
    rows = []
    section = text[start:end]
    for line in section.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not cells[0] or cells[0].lower() in (
                "社会维度", "social dimension", "缺口维度", "gap dimension"):
            continue
        if re.match(r"^\|?\s*:?-{2,}", line):
            continue
        rows.append((cells[0], cells[status_column]))
    return rows


def _leading_dimension_status(raw, grades):
    for grade in grades:
        if raw == grade or raw.startswith(grade):
            return grade
    return raw


def check_dimension_status():
    """README and ledger expose the same bilingual dimension/status ledger."""
    parsed = {}
    for lang in LANGS:
        try:
            readme_rows = _dimension_tables(
                read(REGISTRY_README[lang]), DIMENSION_README_HEADING[lang],
                "\n### ", 1)
            ledger_raw = _dimension_tables(
                read("docs/%s/90-ledger.md" % lang), DIMENSION_LEDGER_HEADING[lang],
                "### 6.1", 3)
            ledger_rows = [(name, _leading_dimension_status(status, DIMENSION_GRADES[lang]))
                           for name, status in ledger_raw]
        except ValueError as exc:
            fail("dimension-status", "%s: %s" % (lang, exc))
            continue
        grades = DIMENSION_GRADES[lang]
        for label, rows in (("README", readme_rows), ("ledger", ledger_rows)):
            if not rows:
                fail("dimension-status", "%s %s dimension table is empty" % (lang, label))
            names = [name for name, _status in rows]
            if len(names) != len(set(names)):
                fail("dimension-status", "%s %s has duplicate dimension names" % (lang, label))
            for name, status in rows:
                if status not in grades:
                    fail("dimension-status", "%s %s %r has unrecognized status %r" %
                         (lang, label, name, status))
        if readme_rows and ledger_rows:
            readme_names = {name for name, _status in readme_rows}
            ledger_names = {name for name, _status in ledger_rows}
            if readme_names != ledger_names:
                fail("dimension-status", "%s README/ledger dimension sets differ: README-only %s; ledger-only %s" %
                     (lang, sorted(readme_names - ledger_names), sorted(ledger_names - readme_names)))
            readme_status = dict(readme_rows)
            ledger_status = dict(ledger_rows)
            for name in sorted(readme_names & ledger_names):
                if readme_status[name] != ledger_status[name]:
                    fail("dimension-status", "%s %s status differs: README %s, ledger %s" %
                         (lang, name, readme_status[name], ledger_status[name]))
        parsed[lang] = (readme_rows, ledger_rows)
    for kind, index in (("README", 0), ("ledger", 1)):
        sequences = {lang: [DIMENSION_GRADES[lang].index(status)
                            for _name, status in parsed.get(lang, ([], []))[index]]
                     for lang in LANGS}
        if sequences["zh"] and sequences["en"] and sequences["zh"] != sequences["en"]:
            fail("dimension-status", "%s grade sequence differs between zh and en" % kind)



# ---------------------------------------------------------------------------
# Chain lens/card audit.  The README registry is the chain universe.
# ---------------------------------------------------------------------------
LENS_CODE = re.compile(r"(?<![A-Za-z0-9])L([1-9])(?![0-9])")
LENS_INVALID = re.compile(r"(?<![A-Za-z0-9])L(0|[1-9][0-9]+)(?![A-Za-z0-9])", re.I)
LENS_BROAD_RANGE = re.compile(r"L1\s*[-‐‑‒–—―－~至]\s*L9", re.I)
LENS_ANY_RANGE = re.compile(r"L\s*[0-9]+\s*[-‐‑‒–—―－~至]\s*L?\s*[0-9]+", re.I)
CHAIN_U_LABEL = {"zh": "**未使用的透镜**", "en": "**Lenses not used**"}
CARD_LENS = {"zh": re.compile(r"^- \*\*透镜\*\*[:：]([^\
]*)$", re.M),
             "en": re.compile(r"^- \*\*Lens\*\*:\s*([^\
]*)$", re.M)}
CARD_SOURCE = {"zh": re.compile(r"^- \*\*出处\*\*[:：]([^\
]*)$", re.M),
               "en": re.compile(r"^- \*\*Source\*\*:\s*([^\
]*)$", re.M)}


def _chain_path_set(registry):
    return {p for rows in registry.values() for paths in rows.values() for p in paths}


def _normalize_lens_text(text):
    t = visible(text).replace("\u2011", "-")
    return t.replace("Ｌ", "L")


def _lens_codes(text, location=None):
    """Read real L1..L9 declarations without treating explanatory ranges as codes."""
    t = _normalize_lens_text(text)
    # L1-L9 is the repository's documented universe phrase, not nine declarations.
    broad = LENS_BROAD_RANGE.sub("", t)
    bad_range = LENS_ANY_RANGE.search(broad)
    if bad_range:
        fail("lens-range", "%s: %r" % (location or "lens field", text))
    negative = r"(?:不调用|未调用|未使用|不使用|撤出|仅作历史|does not invoke|doesn\'t invoke|not invoke|not invoked|not used|withdrawn|historical context)"
    historical = bool(re.search(negative + r".{0,24}L10", broad, re.I) or re.search(r"L10.{0,80}(?:历史上下文|撤出工具箱|historical context|withdrawn)", broad, re.I))
    invalid = []
    for m in LENS_INVALID.finditer(broad):
        before = broad[max(0, m.start()-70):m.start()].lower()
        if re.search(negative + r"\W*$", before, re.I) or (m.group(1) == "10" and historical):
            continue
        invalid.append(m.group(0))
    if invalid:
        fail("lens-token", "%s: unknown lens token(s) %s; original=%r" %
             (location or "lens field", sorted(set(invalid)), text))
    codes = set()
    for m in LENS_CODE.finditer(broad):
        before = broad[max(0, m.start()-70):m.start()].lower()
        after = broad[m.end():m.end()+120]
        if (re.search(negative + r"\W*$", before, re.I) or
                re.search(negative, broad[max(0, m.start()-220):m.start()], re.I) or
                re.search(r"(?:未调用|not invoked|not invoke)", after, re.I)):
            continue
        codes.add("L" + m.group(1))
    return codes


def _parse_u(text, lang, path, cid):
    lines = text.splitlines()
    label = CHAIN_U_LABEL[lang]
    hits = [(i + 1, line) for i, line in enumerate(lines)
            if line.lstrip().startswith(label)]
    if len(hits) != 1:
        return None, "%s: U declaration count=%d (expected exactly one), original=%r" % (path, len(hits), hits)
    lineno, line = hits[0]
    rest = line[line.index(label) + len(label):]
    # C13's current declaration is a heading followed by one bullet per lens.
    if not re.match(r"^\s*[:：]", rest):
        bullets = []
        for candidate in lines[lineno:]:
            if re.match(r"^#{1,6}\s", candidate):
                break
            if not candidate.strip() or candidate.strip() == "</details>":
                continue
            if re.match(r"^[-*]\s+\*\*L(?:[1-9])\*\*", candidate):
                bullets.append(candidate)
                continue
            if bullets or candidate.lstrip().startswith(("-", "*")):
                return None, "%s:%d malformed U bullet, original=%r" % (path, lineno, candidate)
        if bullets:
            nums = re.findall(r"\*\*L([1-9])\*\*", "\n".join(bullets))
            if len(nums) != len(set(nums)):
                return None, "%s:%d duplicate U bullet, original=%r" % (path, lineno, line)
            print("chain-lenses adaptation: %s:%d bullet U" % (path, lineno))
            return {"L" + n for n in nums}, None
        return None, "%s:%d U has no list separator, original=%r" % (path, lineno, line)
    fragment = re.split(r"。|\.\s", re.split(r"[:：]", rest, maxsplit=1)[1], maxsplit=1)[0].strip()
    plain = visible(re.sub(r"\*\*", "", fragment))
    empty = re.match(r"^(无——|none\s*[—-])\s*", plain, re.I)
    if empty:
        tail = plain[empty.end():].lstrip(" 、,;；")
        if re.match(r"^L(?:[0-9]+)", tail, re.I):
            return None, "%s:%d empty marker followed by lens entries, original=%r" % (path, lineno, line)
        return set(), None
    item = r"L([1-9])(?:\s*(?:（[^）]*）|\([^)]*\)))?"
    if lang == "zh":
        pattern = r"^%s(?:、%s)*$" % (item, item)
    else:
        pattern = r"^%s(?:,\s*(?:and\s+)?%s|\s+and\s+%s)*$" % (item, item, item)
    if not re.match(pattern, plain):
        return None, "%s:%d malformed U fragment %r (original=%r)" % (path, lineno, fragment, line)
    nums = re.findall(r"L([1-9])", plain)
    if len(nums) != len(set(nums)):
        return None, "%s:%d duplicate U token, original=%r" % (path, lineno, line)
    return {"L" + n for n in nums}, None


def _card_body(path, jid):
    text = read(path)
    m = re.search(r"^### %s(?:[^\
]*)$" % re.escape(jid), text, re.M)
    if not m:
        return None
    nxt = re.search(r"^### J-\d{3}", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    sec = re.search(r"^## ", text[m.end():end], re.M)
    if sec:
        end = m.end() + sec.start()
    return text[m.start():end]


def _source_target(raw, card_path):
    m = re.search(r"\]\(([^)#\s]+)", raw)
    if not m:
        return None
    return os.path.normpath(os.path.join(os.path.dirname(card_path), m.group(1))).replace(os.sep, "/")


EXTERNAL_PAGE_PATTERNS = (
    re.compile(r"^docs/(?:zh|en)/(?:00-method|01-retrospect|10-near|20-mid|30-far|90-ledger|91-social-scale-register)\.md$"),
    re.compile(r"^evidence/[^/]+\.md$"),
)


def _is_listed_external(target):
    return any(pattern.match(target) for pattern in EXTERNAL_PAGE_PATTERNS)


def _all_cards(lang):
    out = {}
    for path in ledger_paths(lang)[1:]:
        for jid in re.findall(r"^### (J-\d{3})", read(path), re.M):
            if jid in out:
                fail("chain-card-source", "%s duplicated in %s and %s" % (jid, out[jid][0], path))
            out[jid] = (path, _card_body(path, jid))
    return out


def _card_lens(body, lang, location):
    fields = CARD_LENS[lang].findall(body or "")
    if len(fields) != 1:
        fail("chain-card-lens", "%s has %d Lens fields (expected exactly one)" % (location, len(fields)))
        return set(), ""
    return _lens_codes(fields[0], location), fields[0]


# Only these two intersections are allowed, and only if their exact wording remains.
LENS_INTERSECTION_WHITELIST = {
    ("zh", "C9", "L7", "J-096", "L7(制度滞后)、L9(关系不对称)"): "L7 也只承接「制度后到」这一端",
    ("en", "C9", "L7", "J-096", "L7 (institutional lag), L9 (relational asymmetry)"): "L7 covers only the “institutions arrive late” end",
}

# Existing cards whose prose explicitly records that no L1–L9 lens carries it.
# This is an auditable allowlist, not a generic empty-field escape hatch.
ZERO_CODE_ALLOWLIST = {
    (lang, cid, jid)
    for lang in LANGS
    for cid, jids in {
        "C7": {"J-087", "J-088", "J-089", "J-090", "J-091"},
        "C8": {"J-094", "J-095"},
        "C12": {"J-114", "J-115", "J-116"},
        "C13": {"J-105", "J-106", "J-107"},
        "C14": {"J-108"}, "C15": {"J-109", "J-110", "J-111"},
        "C16": {"J-112", "J-113"},
    }.items()
    for jid in jids
}



def _u_fragment(text, lang):
    label = CHAIN_U_LABEL[lang]
    item = r"L[1-9](?:\s*(?:（[^）]*）|\([^)]*\)))?"
    for line in text.splitlines():
        if line.lstrip().startswith(label) and re.search(r"[:：]", line):
            rest = visible(re.sub(r"\*\*", "", re.split(r"[:：]", line, maxsplit=1)[1])).lstrip()
            if lang == "zh":
                m = re.match(r"%s(?:、%s)*" % (item, item), rest)
            else:
                m = re.match(r"%s(?:,\s*(?:and\s+)?%s|\s+and\s+%s)*" % (item, item, item), rest)
            return m.group(0).strip() if m else ""
    return ""


def check_chain_lens_cards():
    registry = {lang: parse_registry(lang)[0] for lang in LANGS}
    chain_paths = _chain_path_set(registry)
    for lang in LANGS:
        cards = _all_cards(lang)
        for cid in sorted(registry[lang]):
            own_paths = sorted(p for p in registry[lang][cid] if p.startswith("docs/%s/" % lang))
            if len(own_paths) != 1:
                continue
            path = own_paths[0]
            if not os.path.exists(os.path.join(REPO, path)):
                continue
            text = read(path)
            u, err = _parse_u(text, lang, path, cid)
            if err:
                own_exists = any(
                    (CARD_SOURCE[lang].search(body or "") and
                     _source_target(CARD_SOURCE[lang].search(body or "").group(1), card_path) == path)
                    for card_path, body in cards.values())
                # C10 is the sole declared no-own-card exception; cardless
                # historical shells also keep an implicit empty U.
                fail("chain-lenses", err)
                u = set()
            categories = {"own": set(), "external": set(), "other": set(), "embedded": set(), "zero-code": set()}
            details = {}
            cited = set(re.findall(r"(?<![A-Za-z0-9])(J-\d{3})(?![A-Za-z0-9])", visible(text)))
            embedded = set(re.findall(r"^### (J-\d{3})", text, re.M))
            own_from_ledger = set()
            for jid, (card_path, body) in cards.items():
                sm = CARD_SOURCE[lang].search(body or "")
                target = _source_target(sm.group(1), card_path) if sm else None
                if target == path:
                    own_from_ledger.add(jid)
            candidates = cited | embedded | own_from_ledger
            origins = {}
            for jid in sorted(candidates):
                if jid in embedded:
                    body = _card_body(path, jid)
                    if body is None:
                        fail("chain-card-source", "%s embeds %s but its card body is unreadable" % (path, jid))
                        origins[jid] = "other"
                    else:
                        origins[jid] = "embedded"
                        details[jid] = body
                    continue
                if jid not in cards:
                    origins[jid] = "other"
                    fail("chain-card-source", "%s cites %s, but no ledger card is available" % (path, jid))
                    continue
                card_path, body = cards[jid]
                sm = CARD_SOURCE[lang].search(body or "")
                target = _source_target(sm.group(1), card_path) if sm else None
                if target == path:
                    origins[jid] = "own"
                    details[jid] = body
                elif target and os.path.exists(os.path.join(REPO, target)) and (target in chain_paths or _is_listed_external(target)):
                    origins[jid] = "external"
                else:
                    origins[jid] = "other"
            for jid, origin in origins.items():
                categories[origin].add(jid)
            # Origin categories are a partition; zero-code is deliberately an annotation.
            origin_sets = [categories[k] for k in ("own", "external", "other", "embedded")]
            overlap_ids = set()
            for i, left in enumerate(origin_sets):
                for right in origin_sets[i + 1:]:
                    overlap_ids |= left & right
            if overlap_ids:
                fail("chain-card-source", "%s has overlapping provenance categories: %s" % (path, ",".join(sorted(overlap_ids))))
            if set().union(*origin_sets) != candidates:
                fail("chain-card-source", "%s provenance categories are not exhaustive" % path)
            for jid in sorted(categories["other"]):
                fail("chain-card-source", "%s has unclassified card reference %s" % (path, jid))
            d = set()
            for jid in sorted(categories["own"] | categories["embedded"]):
                codes, raw = _card_lens(details.get(jid), lang, "%s:%s" % (path, jid))
                d |= codes
                if not codes:
                    categories["zero-code"].add(jid)
                    if (lang, cid, jid) not in ZERO_CODE_ALLOWLIST:
                        fail("chain-card-lens", "%s:%s has an unallowlisted zero-code Lens field" % (path, jid))
            overlap = sorted(u & d)
            u_fragment = _u_fragment(text, lang)
            for lens in overlap:
                for jid in sorted(categories["own"] | categories["embedded"]):
                    codes, raw = _card_lens(details.get(jid), lang, "%s:%s" % (path, jid))
                    if lens not in codes:
                        continue
                    expected = LENS_INTERSECTION_WHITELIST.get((lang, cid, lens, jid, u_fragment))
                    if expected is None:
                        fail("chain-lenses", "%s: U∩D contains %s via %s; U-original=%r, card-lens=%r" % (path, lens, jid, [x for x in text.splitlines() if CHAIN_U_LABEL[lang] in x], raw))
                    else:
                        phrase_count = raw.count(expected)
                        code_count = len(re.findall(r"(?<![A-Za-z0-9])L7(?![0-9])", _normalize_lens_text(raw)))
                        if phrase_count != 1 or code_count != 1 or expected not in raw:
                            fail("chain-lenses", "%s: stale/non-unique whitelist (%s), phrase_count=%d, L7_count=%d, card-lens=%r" % (path, (lang, cid, lens, jid), phrase_count, code_count, raw))
            if categories["other"]:
                fail("chain-card-source", "%s has unclassified card references: %s" % (path, ",".join(sorted(categories["other"]))))
            if not categories["own"] and cid != "C10":
                fail("chain-card-source", "%s has no own-chain cards (only C10 may be empty)" % path)
            print("chain %-3s %-2s U=%s own=%s external=%s other=%s embedded=%s zero-code=%s" %
                  (cid, lang, ",".join(sorted(u)) or "—", ",".join(sorted(categories["own"])) or "—",
                   ",".join(sorted(categories["external"])) or "—", ",".join(sorted(categories["other"])) or "—",
                   ",".join(sorted(categories["embedded"])) or "—", ",".join(sorted(categories["zero-code"])) or "—"))
            original = [line for line in text.splitlines() if CHAIN_U_LABEL[lang] in line]
            print("  U-original: %s" % (original[0] if original else "(implicit empty for cardless chain)"))

def run_checks():
    files = markdown_files()
    check_public_internal_ids(files)
    links = check_links(files)
    check_table_rows(files)
    cards = {lang: check_ledger(lang) for lang in LANGS}
    check_parity(cards)
    chains = check_chain_registry()
    registry = {lang: parse_registry(lang)[0] for lang in LANGS}
    check_chain_card_parity(registry, cards)
    check_english_chain_punctuation(registry)
    check_chain_mermaid(registry, cards)
    check_navigation_mermaid()
    check_chain_titles()
    check_chain_lens_cards()
    check_readme_counts(cards, len(chains))
    check_dimension_status()

    print("files checked      : %d" % len(files))
    print("internal links     : %d" % links)
    print("judgment cards     : zh %d / en %d" % (len(cards["zh"]), len(cards["en"])))
    print("chains registered  : %d (%s)" % (len(chains), ", ".join(sorted(chains))))
    if warnings:
        print("\nWARNINGS (%d):" % len(warnings))
        for check, detail in warnings:
            print("  [%s] %s" % (check, detail))
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
    """Copy exactly what the checks read: docs/ plus the top-level pair files."""
    shutil.copytree(os.path.join(REPO, "docs"), os.path.join(dst, "docs"))
    for name in ROOT_MARKDOWN:
        src = os.path.join(REPO, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dst, name))
    # README links to the repository licence as a non-Markdown root asset; the
    # self-test copy must carry that asset or its pristine baseline is false.
    if os.path.exists(os.path.join(REPO, "LICENSE")):
        shutil.copy2(os.path.join(REPO, "LICENSE"), os.path.join(dst, "LICENSE"))
    # The public README also links to package.json as the capability manifest.
    # Omitting it makes the pristine fixture fail before any negative mutation
    # runs, so the self-test would no longer prove the checker catches defects.
    if os.path.exists(os.path.join(REPO, "package.json")):
        shutil.copy2(os.path.join(REPO, "package.json"), os.path.join(dst, "package.json"))
    return dst


def _run_checker(root):
    proc = subprocess.Popen(
        [sys.executable, os.path.abspath(__file__), "--repo", root],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _ = proc.communicate()
    return proc.returncode, out.decode("utf-8", "replace")


def _ledger(root, lang):
    """Return the last shard, the fixture's card mutation surface."""
    shards = _card_shards(root, lang)
    return shards[-1] if shards else os.path.join(root, "docs", lang, "90-ledger.md")


def _card_shards(root, lang):
    directory = os.path.join(root, "docs", lang, "ledger")
    return [os.path.join(directory, name) for name in sorted(os.listdir(directory))
            if is_markdown(name)] if os.path.isdir(directory) else []


def _card_ids(root, lang):
    ids = []
    for path in _card_shards(root, lang):
        ids.extend(re.findall(r"^### (J-\d{3})", _read_file(path), re.M))
    return ids


def _card_path(root, lang, jid):
    for path in _card_shards(root, lang):
        if re.search(r"^### %s\b" % re.escape(jid), _read_file(path), re.M):
            return path
    raise AssertionError("fixture carries no card %s" % jid)


def _last_card_file(root, lang):
    paths = _card_shards(root, lang)
    if not paths:
        raise AssertionError("fixture carries no card shards")
    path = paths[-1]
    text = _read_file(path)
    start, end, jid = _last_card(text)
    return path, text, start, end, jid


def _first_card_file(root, lang):
    paths = _card_shards(root, lang)
    if not paths:
        raise AssertionError("fixture carries no card shards")
    path = paths[0]
    text = _read_file(path)
    start, jid = _first_card(text)
    return path, text, start, jid


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
    path = os.path.join(root, "docs", "zh", "90-ledger.md")
    text = _read_file(path)
    m = re.search(r"\]\(#([^)\s]+)\)", text)
    if not m:
        raise AssertionError("fixture carries no in-file anchor link")
    _write_file(path, text[:m.start(1)] + "no-such-heading-" + m.group(1)
                + text[m.end(1):])
    return u"zh ledger: first anchor link now points at #no-such-heading-…"


def _break_contributing_anchor(root):
    """A CONTRIBUTING link into the ledger that no longer lands.

    This case is what keeps CONTRIBUTING inside `markdown_files()` honest:
    drop it from `ROOT_MARKDOWN` and this is the one case that goes red, while
    every other link case stays green off the READMEs and docs/. The submission
    guide is nothing but links into the vocabulary it tells a stranger to use,
    so a heading rename that silently unhooks them is exactly the failure the
    file exists to prevent.
    """
    path = os.path.join(root, "CONTRIBUTING.md")
    if not os.path.exists(path):
        raise AssertionError("fixture carries no CONTRIBUTING.md")
    text = _read_file(path)
    m = re.search(r"\]\(docs/zh/90-ledger\.md#([^)\s]+)\)", text)
    if not m:
        raise AssertionError("CONTRIBUTING.md carries no ledger anchor link")
    _write_file(path, text[:m.start(1)] + "no-such-heading-" + m.group(1)
                + text[m.end(1):])
    return u"CONTRIBUTING.md: first ledger anchor now points at a dead heading"


def _break_dep_edge(root):
    path, text, start, _end, jid = _last_card_file(root, "zh")
    m = re.search(r"\*\*depends-on\*\*[:\uff1a]\s*([^\n]*)", text[start:])
    if not m or not re.search(r"J-\d{3}", m.group(1)):
        raise AssertionError("the last zh card declares no dependency to drop")
    _write_file(path, text[:start + m.start(1)] + u"\u2014\u3002"
                + text[start + m.end(1):])
    return (u"zh %s: card declares no depends-on while the graph and the "
            u"overview still carry the edge" % jid)


def _break_mermaid_edge(root):
    """Invent an edge in both diagrams; the projection check must reject it."""
    for lang in LANGS:
        path = os.path.join(root, "docs", lang, "90-ledger.md")
        text = _read_file(path)
        needle = "  J001 --> J006"
        if needle not in text:
            raise AssertionError("%s diagram has no stable edge" % lang)
        _write_file(path, text.replace(needle, needle + "\n  J079 --> J090", 1))
    return u"both Mermaid diagrams add non-authoritative J-079 --> J-090"


def _break_missing_overview_row(root):
    """Remove one overview row while leaving the card and graph present."""
    path = os.path.join(root, "docs", "zh", "90-ledger.md")
    text = _read_file(path)
    m = re.search(r"^\| \[J-095\].*\n", text, re.M)
    if not m:
        raise AssertionError("fixture has no J-095 overview row")
    _write_file(path, text[:m.start()] + text[m.end():])
    return u"zh J-095 overview row removed"


def _break_split_overview_table(root):
    """A blank line inside the overview: every parser count stays right,
    but GitHub stops rendering the rows after it as a table."""
    path = os.path.join(root, "docs", "en", "90-ledger.md")
    text = _read_file(path)
    m = re.search(r"^\| \[J-095\].*\n", text, re.M)
    if not m:
        raise AssertionError("fixture has no J-095 overview row")
    _write_file(path, text[:m.start()] + "\n" + text[m.start():])
    return u"en overview split by a blank line before J-095"


def _break_duplicate_graph_row(root):
    """Duplicate a text dependency row; the graph must reject it."""
    for lang in LANGS:
        path = os.path.join(root, "docs", lang, "90-ledger.md")
        text = _read_file(path)
        m = re.search(r"^J-095\s+%s[^\n]*\n" % re.escape(GRAPH_ARROW[lang]), text, re.M)
        if not m:
            raise AssertionError("%s graph has no J-095 row" % lang)
        _write_file(path, text[:m.end()] + m.group(0) + text[m.end():])
    return u"both dependency graphs duplicate J-095"


def _break_root_dep_edge(root):
    """The lowest-id card must remain dependency-rooted in the graph."""
    path = _card_path(root, "zh", "J-001")
    text = _read_file(path)
    root_id = "J-001"
    borrowed = "J-002"
    head = re.search(r"^### %s\b" % root_id, text, re.M).start()
    m = re.search(r"^- \*\*depends-on\*\*[:\uff1a][^\n]*$", text[head:], re.M)
    if not m:
        raise AssertionError("root card %s carries no depends-on line" % root_id)
    if re.search(r"J-\d{3}", m.group(0)):
        raise AssertionError("root card %s already declares an upstream" % root_id)
    line = u"- **depends-on**\uff1a%s\u3002" % borrowed
    _write_file(path, text[:head + m.start()] + line + text[head + m.end():])
    return (u"zh %s (lowest id): declares %s while the graph and overview "
            u"give it no upstream" % (root_id, borrowed))


def _break_single_language_card(lang):
    """Remove the last card from one language; parity must notice either way."""
    other = "en" if lang == "zh" else "zh"

    def mutate(root):
        path = _card_shards(root, lang)[-1]
        text = _read_file(path)
        start, end, jid = _last_card(text)
        _write_file(path, text[:start] + text[end:])
        return u"%s ledger: card %s removed, %s still carries it" % (
            lang, jid, other)

    return mutate


def _break_equal_count_bilingual_card_set(root):
    """Rename one English card everywhere while preserving the card count.

    This attacks identifier-set equality rather than the weaker count-equality
    shape covered by deleting a card. All English references and anchors move
    with the card, so [bilingual-cards] is the only intended failure class.
    """
    ids = set(_card_ids(root, "en"))
    old_id = max(ids)
    new_id = "J-%03d" % (max(int(j.split("-")[1]) for j in ids) + 1)
    ledger = _card_path(root, "en", old_id)
    text = _read_file(ledger)
    path = _card_path(root, "en", old_id)
    for base, _dirs, files in os.walk(root):
        for name in files:
            path = os.path.join(base, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            if not (rel.startswith("docs/en/") or name.endswith(".en.md")):
                continue
            content = _read_file(path)
            changed = content.replace(old_id, new_id)
            changed = changed.replace(old_id.lower(), new_id.lower())
            if changed != content:
                _write_file(path, changed)
    path = ledger
    text = _read_file(path)
    heading = re.search(r"^(### %s[^\n]*)$" % new_id, text, re.M)
    if not heading:
        raise AssertionError("renamed fixture card not found")
    field = ("\n\n- **Audience scale**: affected group = professional buyers; "
             "million-scale; raises existing professionals' ceiling")
    text = text[:heading.end()] + field + text[heading.end():]
    _write_file(path, text)
    return u"English %s renamed to %s everywhere; count unchanged" % (old_id, new_id)


def _break_new_card_without_audience_scale(root):
    """Add one bilingual shard card whose only defect is missing audience scale."""
    ids = set(_card_ids(root, "zh"))
    if ids != set(_card_ids(root, "en")):
        raise AssertionError("fixture ledgers do not start with equal id sets")
    new_id = "J-%03d" % (max(int(j.split("-")[1]) for j in ids) + 1)
    source_id = "J-055"
    for lang in LANGS:
        source_path = _card_path(root, lang, source_id)
        source_text = _read_file(source_path)
        source = re.search(r"^### %s[^\n]*" % source_id, source_text, re.M)
        next_card = re.search(r"^### J-\d{3}", source_text[source.end():], re.M)
        end = source.end() + next_card.start() if next_card else len(source_text)
        section = source_text[source.start():end].replace(source_id, new_id)
        # J-055 was picked because it predated the field; the legacy-card
        # migration has since given it one, which made this fixture raise
        # instead of testing anything. Strip the field so the clone's only
        # defect is the missing Audience scale, whatever the source carries.
        section = re.sub(r"^- \*\*%s\*\*[:\uff1a][^\n]*\n"
                         % re.escape(AUDIENCE_FIELD[lang]), "", section,
                         flags=re.M)
        if audience_scale_value(section, lang) is not None:
            raise AssertionError("source card unexpectedly carries audience scale")
        shard = os.path.join(root, "docs", lang, "ledger", "96-105.md")
        _write_file(shard, ("# 判断卡片 J-096–J-105\n\n" if lang == "zh"
                            else "# Judgment cards J-096–J-105\n\n") + section.strip() + "\n")
        root_path = os.path.join(root, "docs", lang, "90-ledger.md")
        root_text = _read_file(root_path)
        heading = re.search(r"^#### %s([^\n]*)$" % source_id, root_text, re.M)
        if not heading:
            raise AssertionError("source compatibility stub missing")
        stub = root_text[heading.start():]
        stub_end = re.search(r"^####? ", stub[heading.end() - heading.start():], re.M)
        # Use the source stub's title and objective, then point at the new shard.
        source_stub = stub[:stub_end.start() if stub_end else len(stub)]
        new_stub = source_stub.replace(source_id, new_id)
        new_stub = re.sub(r"ledger/\d{2}-\d{2}\.md", "ledger/96-105.md", new_stub)
        _write_file(root_path, root_text.rstrip() + "\n\n" + new_stub.strip() + "\n")
        # Clone the source overview row and dependency projection where present.
        root_text = _read_file(root_path)
        row = re.search(r"^\|\s*\[%s\]\([^\n]*$" % source_id, root_text, re.M)
        if row:
            _write_file(root_path, root_text.rstrip() + "\n" + row.group(0).replace(source_id, new_id) + "\n")
        _bump_readme_count(root, lang, "cards")
    return u"bilingual %s cloned from %s without Audience scale" % (new_id, source_id)


def _break_embedded_audience_scale(root):
    """Put a complete-looking audience token inside another field, not its own."""
    _break_new_card_without_audience_scale(root)
    for lang in LANGS:
        path = _ledger(root, lang)
        text = _read_file(path)
        ids = re.findall(r"^### (J-\d{3})", text, re.M)
        jid = max(ids)
        start = text.index("### %s" % jid)
        marker = (u"- **\u666e\u53ca\u95f8\u590d\u6838**\uff1a" if lang == "zh"
                  else "- **Diffusion-gate review**:")
        embedded = (u"**\u53d7\u4f17\u89c4\u6a21**\uff1d\u767e\u4e07\u91cf\u7ea7\u7684\u804c\u4e1a\u4e70\u65b9\uff1b\u63d0\u9ad8\u65e2\u6709\u4e13\u4e1a\u8005\u4e0a\u9650\uff1b" if lang == "zh"
                    else "**Audience scale** = professional buyers; million-scale; "
                         "raises existing professionals' ceiling; ")
        pos = text.find(marker, start)
        if pos == -1:
            raise AssertionError("fixture card has no diffusion-gate review")
        pos += len(marker)
        _write_file(path, text[:pos] + " " + embedded + text[pos:])
    return u"new bilingual card embeds a bold Audience scale token inside diffusion review"


def _break_malformed_audience_scale(root):
    """Add a standalone field whose value omits required audience structure."""
    _break_new_card_without_audience_scale(root)
    for lang in LANGS:
        path = _ledger(root, lang)
        text = _read_file(path)
        ids = re.findall(r"^### (J-\d{3})", text, re.M)
        jid = max(ids)
        heading = re.search(r"^(### %s[^\n]*)$" % jid, text, re.M)
        value = (u"\n\n- **\u53d7\u4f17\u89c4\u6a21**\uff1a\u2014"
                 if lang == "zh" else "\n\n- **Audience scale**: —")
        text = text[:heading.end()] + value + text[heading.end():]
        _write_file(path, text)
    return u"new bilingual card carries a standalone but unstructured Audience scale field"


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


def _sync_embedded_field_fixture(root, lang, jid, field, value):
    """Keep a valid fixture mutation synchronized across its formal copies."""
    directory = os.path.join(root, "docs", lang, "chains")
    separator = u"：" if lang == "zh" else ": "
    pattern = r"(^### [^\n]*?\b%s\b[^\n]*$)(.*?)(?=^### |^## |\Z)" % re.escape(jid)
    for name in sorted(os.listdir(directory)):
        if not is_markdown(name):
            continue
        path = os.path.join(directory, name)
        text = _read_file(path)
        changed = False
        def replace_section(match):
            nonlocal changed
            body = match.group(2)
            if not re.search(r"^- \*\*%s\*\*[:：]" % re.escape(field), body, re.M):
                return match.group(0)
            changed = True
            body = re.sub(r"^- \*\*%s\*\*[:：][^\n]*$" % re.escape(field),
                          "- **%s**%s%s" % (field, separator, value), body,
                          count=1, flags=re.M)
            return match.group(1) + body
        updated = re.sub(pattern, replace_section, text, flags=re.M | re.S)
        if changed:
            _write_file(path, updated)


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
        _sync_embedded_field_fixture(root, lang, jid, field, value)
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
    """Prose below the last card belongs to no card."""
    path = _ledger(root, "zh")
    text = _read_file(path)
    _start, end, _jid = _last_card(text)
    if end >= len(text):
        for lang in LANGS:
            p = _ledger(root, lang)
            title = u"附录（fixture）" if lang == "zh" else u"Appendix (fixture)"
            _write_file(p, _read_file(p).rstrip("\n") + u"\n\n## %s\n\n" % title)
        text = _read_file(path)
        _start, end, _jid = _last_card(text)
    nl = text.find("\n", end)
    if nl == -1:
        raise AssertionError("section after the last card has no body")
    extra = u"\n- **%s**：极高\n" % CONFIDENCE_FIELD["zh"]
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
    # Current READMEs have no announced row. Preserve the fixture's purpose by
    # making the last registered identifier collide with an existing one.
    i = last
    cells = lines[i].strip().strip("|").split("|")
    lines[i] = "| C4 |" + "|".join(cells[1:]) + "|"
    _write_file(path, "\n".join(lines))
    return u"README.md: fallback registry row now duplicates C4"


def _chain_citation_fixture(root):
    for path in [os.path.join(root, "README.md")] + [
            os.path.join(root, "docs", "zh", "ledger", name)
            for name in sorted(os.listdir(os.path.join(root, "docs", "zh", "ledger")))]:
        if not os.path.isfile(path):
            continue
        text = _read_file(path)
        match = CHAIN_CITE.search(text)
        if match:
            return path, text, match
    raise AssertionError("fixture carries no chain citation with a title")


def _break_chain_title(root):
    """The prose calls a chain something its own H1 does not.

    The replacement is not a truncation but a different name: a shortened
    title is legitimate and must stay green.
    """
    path, text, m = _chain_citation_fixture(root)
    renamed = u"\u53e6\u4e00\u4e2a\u540d\u5b57"  # 另一个名字
    _write_file(path, text[:m.start(2)] + renamed + text[m.end(2):])
    return u"README.md: %s is cited under a title its file does not carry" % m.group(1)


def _shorten_chain_title(root):
    """Not a breakage: a citation that abbreviates the title it points at.

    The slice deliberately starts past the first character, so this proves the
    rule accepts an abbreviation taken from the MIDDLE of the title — the form
    the ledger actually uses when it cites C2 by its subtitle.
    """
    path, text, m = _chain_citation_fixture(root)
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


def _bump_readme_count(root, lang, kind, delta=1):
    """Keep a stated README count true after a fixture changes the corpus."""
    path = _readme(root, lang)
    text = _read_file(path)

    def repl(m):
        n = parse_count(lang, m.group(1))
        return m.group(0) if n is None else "%d%s" % (n + delta, m.group(2))

    new = re.sub(_count_pattern(lang, kind), repl, text)
    if new == text:
        raise AssertionError("%s README states no readable %s count" % (lang, kind))
    _write_file(path, new)


def _bump_chain_count(root, lang, delta=1):
    """Keep the stated chain count true after a fixture chain is registered."""
    _bump_readme_count(root, lang, "chains", delta)


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
    _register_fixture_chain(root, 14, "140-no-h1-fixture",
                            body=u"No heading at all.\n\nBody.\n")
    return u"C14 registered, its files carry no H1"


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
                + u"\n\u9884\u544a\u6210C99\u3002\n")  # 预告成 C99。
    return u"README.md: prose cites C99 with no space before it"


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


def _break_count_hidden_by_link(root):
    """The evasion a review found the day the character list was written.

    A README whose counts already sit beside links (`打开[判断台账](…)。65 张
    判断卡片`) makes wrapping the number itself in a link the most natural
    edit of all — and it hid the count from both languages at once.
    """
    said = [_hide_count("zh", u"66", u"[%s](docs/zh/90-ledger.md)")(root),
            _hide_count("en", u"Sixty-six",
                        u"[%s](docs/en/90-ledger.md)")(root)]
    return u"the count wrapped in a link in both READMEs: %s" % "; ".join(said)


def _break_count_hidden_by_html(root):
    """Inline HTML renders exactly like the markup it replaces."""
    said = [_hide_count("zh", u"66", u"<b>%s</b>")(root),
            _hide_count("en", u"Sixty-six", u"<b>%s</b>")(root)]
    return u"the count wrapped in <b> in both READMEs: %s" % "; ".join(said)


def _break_count_in_fullwidth_digits(root):
    """Full-width digits read as digits and match no ASCII character class."""
    said = [_hide_count("zh", u"\uff16\uff16", u"%s")(root),
            _hide_count("en", u"\uff16\uff16", u"%s")(root)]
    return u"the count written in full-width digits: %s" % "; ".join(said)


def _break_duplicate_card(root):
    """The same judgment card pasted twice in one ledger shard.

    The fixture uses the final shard, which currently carries two cards. A
    duplicate identifier must be rejected even when the shard has no third
    card to use as an insertion boundary.
    """
    path = _ledger(root, "zh")
    text = _read_file(path)
    ms = list(re.finditer(r"^### (J-\d{3})", text, re.M))
    if len(ms) < 2:
        raise AssertionError("fixture ledger carries too few cards")
    a, b = ms[0].start(), ms[1].start()
    if "\n## " in text[a:b]:
        raise AssertionError("the chosen card spans a section break")
    _write_file(path, text[:b] + text[a:b] + text[b:])
    return u"zh ledger: %s pasted a second time" % ms[0].group(1)


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


def _break_dimension_status_ledger_grade(root):
    path = os.path.join(root, "docs", "zh", "90-ledger.md")
    text = _read_file(path)
    pattern = r"^(\| " + re.escape(u"人与人协作") + r" \|[^\n]*\| )" + re.escape(u"部分覆盖")
    if not re.search(pattern, text, re.M):
        raise AssertionError("zh ledger has no collaboration row with partial status")
    _write_file(path, re.sub(pattern, r"\1" + u"已覆盖", text, count=1, flags=re.M))
    return u"zh ledger: collaboration status changed from partial to covered"


def _break_dimension_status_missing_gap(root):
    path = os.path.join(root, "docs", "en", "90-ledger.md")
    text = _read_file(path)
    pattern = r"^\| Culture, entertainment, and leisure \|[^\n]*\n"
    if not re.search(pattern, text, re.M):
        raise AssertionError("en ledger has no culture gap row")
    _write_file(path, re.sub(pattern, "", text, count=1, flags=re.M))
    return u"en ledger: one no-entry dimension row removed"


def _break_public_internal_id(root):
    """A production-line work-unit handle must never reach public Markdown."""
    path = _readme(root, "en")
    _write_file(path, _read_file(path)
                + "\nTracking note: wu-01234567-89ab-cdef-0123-456789abcdef.\n")
    return u"README.en.md: appended an internal wu-* handle"






def _chain_doc(root, lang, cid):
    directory = os.path.join(root, "docs", lang, "chains")
    for name in sorted(os.listdir(directory)):
        if not is_markdown(name):
            continue
        path = os.path.join(directory, name)
        if re.search(r"^#\s+%s\b" % re.escape(cid), _read_file(path), re.M):
            return path
    raise AssertionError("fixture carries no chain %s/%s" % (lang, cid))


def _replace_chain_u(root, lang, cid, old, new):
    path = _chain_doc(root, lang, cid); text = _read_file(path)
    if old not in text:
        raise AssertionError("%s U fixture text not found" % old)
    _write_file(path, text.replace(old, new, 1))
    return "%s:%s U changed" % (lang, cid)


def _break_u_last_token(root, lang):
    if lang == "zh":
        return _replace_chain_u(root, lang, "C9", "L9（关系不对称）", "L9（关系不对称）、L8（人性）")
    return _replace_chain_u(root, lang, "C9", "L9 (relational asymmetry)", "L9 (relational asymmetry), and L8 (human nature)")


def _break_c4_u_j100(root):
    return _replace_chain_u(root, "zh", "C4", "**未使用的透镜**：无——", "**未使用的透镜**：L8（人性）")


def _break_c9_non_l7_j096(root):
    return _replace_chain_u(root, "zh", "C9", "L9（关系不对称）", "L8（人性）")


def _break_c9_l7_non_j096(root):
    path = _card_path(root, "zh", "J-097"); text = _read_file(path)
    m = re.search(r"(^### J-097.*?)(?=^### J-|\Z)", text, re.M | re.S)
    if not m: raise AssertionError("J-097 body not found")
    body = re.sub(r"(^- \*\*透镜\*\*[:：][^\n]*)", lambda x: x.group(1) + "、L7", m.group(1), count=1, flags=re.M)
    if body == m.group(1): raise AssertionError("J-097 lens field not found")
    _write_file(path, text[:m.start()] + body + text[m.end():])
    return "J-097 lens field gained L7"

def _break_c9_j096_extra_l7(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    text = re.sub(r"(^- \*\*透镜\*\*[:：])", r"\1L7（制度后到）；", text, count=1, flags=re.M)
    text = text.replace("L7 也只承接「制度后到」这一端", "L7 也只承接制度后到这一端", 1)
    _write_file(path, text)
    return "J-096 gained L7 without the exact whitelist phrase"


def _break_u_missing(root):
    path = _chain_doc(root, "zh", "C4"); text = _read_file(path)
    new = re.sub(r"^\*\*未使用的透镜\*\*：.*$\n?", "", text, count=1, flags=re.M)
    if new == text: raise AssertionError("zh U line not found")
    _write_file(path, new)
    return "%s: U line removed" % path


def _break_u_missing_en(root):
    path = _chain_doc(root, "en", "C4"); text = _read_file(path)
    new = re.sub(r"^\*\*Lenses not used\*\*:.*$\n?", "", text, count=1, flags=re.M)
    if new == text: raise AssertionError("en U line not found")
    _write_file(path, new)
    return "%s: U line removed" % path


def _break_u_range(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    text = re.sub(r"(^- \*\*透镜\*\*[:：][^\n]*)", lambda m: m.group(1) + "、L7–L9", text, count=1, flags=re.M)
    _write_file(path, text)
    return "J-096 lens field gained L7–L9"


def _break_u_fullwidth(root):
    return _replace_chain_u(root, "zh", "C9", "L9（关系不对称）", "L9（关系不对称）、Ｌ8（人性）")


def _break_u_fullwidth_dash(root):
    return _replace_chain_u(root, "zh", "C9", "L7（制度滞后）", "L1－L9")


def _break_c9_u_phrase(root):
    path = _chain_doc(root, "zh", "C9"); text = _read_file(path)
    new = text.replace("L7（制度滞后）", "L7（制度延迟）", 1)
    if new == text: raise AssertionError("C9 U phrase not found")
    _write_file(path, new)
    return "C9 U phrase changed without changing the card whitelist"


def _break_none_with_tail(root):
    return _replace_chain_u(root, "zh", "C4", "**未使用的透镜**：无——", "**未使用的透镜**：无——、L1（供需）")


def _break_source_other(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    text = re.sub(r"(^- \*\*出处\*\*[:：].*?\()[^)]*", r"\1../chains/999-unregistered.md", text, count=1, flags=re.M)
    _write_file(path, text)
    return "J-096 source points to an unregistered chain file"

def _break_source_existing_unlisted(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    text = re.sub(r"(^- \*\*出处\*\*[:：].*?\()[^)]*", r"\1../../../README.md", text, count=1, flags=re.M)
    _write_file(path, text)
    return "J-096 source points to an existing but unlisted page"


def _break_bullet_tail(root):
    path = _chain_doc(root, "zh", "C13"); text = _read_file(path)
    if "- **L9**" not in text: raise AssertionError("C13 L9 bullet not found")
    _write_file(path, text.replace("- **L9**", "- **L10**", 1))
    return "C13 U bullet changed to L10"


def _break_c10_u_missing(root):
    path = _chain_doc(root, "zh", "C10"); text = _read_file(path)
    new = re.sub(r"^\*\*未使用的透镜\*\*：.*$\n?", "", text, count=1, flags=re.M)
    _write_file(path, new)
    return "C10 U line removed despite its zero-card exemption"


def _break_unlisted_zero_code(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    m = re.search(r"(^### J-096.*?)(?=^### J-|\Z)", text, re.M | re.S)
    body = re.sub(r"^- \*\*透镜\*\*[:：].*$", "- **透镜**：本卡没有 L1–L9 承载。", m.group(1), count=1, flags=re.M)
    _write_file(path, text[:m.start()] + body + text[m.end():])
    return "J-096 became zero-code outside the allowlist"


LENS_NEGATIVE_CASES = [
    (u"U last-token intersection (zh)", "chain-lenses", lambda root: _break_u_last_token(root, "zh"), "C9"),
    (u"U last-token intersection (en)", "chain-lenses", lambda root: _break_u_last_token(root, "en"), "C9"),
    (u"C4 U names an own card lens", "chain-lenses", _break_c4_u_j100, "C4"),
    (u"C9 non-L7 lens intersects J-096", "chain-lenses", _break_c9_non_l7_j096, "C9"),
    (u"C9 L7 intersects a non-J-096 card", "chain-lenses", _break_c9_l7_non_j096, "C9"),
    (u"whitelist J-096 phrase is stale", "chain-lenses", _break_c9_j096_extra_l7, "J-096"),
    (u"whitelist U phrase is stale", "chain-lenses", _break_c9_u_phrase, "C9"),
    (u"zh U declaration is unreadable", "chain-lenses", _break_u_missing, "C4"),
    (u"en U declaration is unreadable", "chain-lenses", _break_u_missing_en, "C4"),
    (u"a non-universe lens range is rejected", "lens-range", _break_u_range, "J-096"),
    (u"full-width lens intersection is still visible", "chain-lenses", _break_u_fullwidth, "C9"),
    (u"full-width dash range is rejected", "chain-lenses", _break_u_fullwidth_dash, "C9"),
    (u"none marker may not have a tail", "chain-lenses", _break_none_with_tail, "C4"),
    (u"card source to an unregistered file is other", "chain-card-source", _break_source_other, "J-096"),
    (u"card source to an existing unlisted page is other", "chain-card-source", _break_source_existing_unlisted, "J-096"),
    (u"C13 malformed U bullet tail is rejected", "chain-lenses", _break_bullet_tail, "C13"),
    (u"C10 malformed U is not masked by zero-card exemption", "chain-lenses", _break_c10_u_missing, "C10"),
    (u"unallowlisted zero-code card is rejected", "chain-card-lens", _break_unlisted_zero_code, "J-096"),
]


def _positive_broad_range(root):
    path = _card_path(root, "zh", "J-096"); text = _read_file(path)
    text = re.sub(r"(^- \*\*透镜\*\*[:：][^\n]*)", lambda m: m.group(1) + "；L1–L9 L1‐L9 L1‑L9 L1‒L9 L1—L9 L1―L9 L1－L9 是范围说明", text, count=1, flags=re.M)
    _write_file(path, text)
    lens = re.search(r"^- \*\*透镜\*\*[:：]([^\n]*)$", text, re.M)
    if lens:
        _sync_embedded_field_fixture(root, "zh", "J-096", "透镜", lens.group(1))
    return "broad L1–L9 explanatory range remains non-declarative"


def _replace_embedded_summary(root, lang, heading_id="J-096"):
    path = _chain_doc(root, lang, "C9")
    text = _read_file(path)
    heading = ("### 判断卡片 1：%s" if lang == "zh" else "### Judgment card 1: %s") % heading_id
    match = re.search(r"(^### [^\n]*?%s.*?)(?=^### |^## |\Z)" % re.escape(heading_id),
                      text, re.M | re.S)
    if not match:
        raise AssertionError("C9 embedded %s heading not found" % heading_id)
    if lang == "zh":
        link = "../ledger/96-102.md#j-096--老龄化与家庭缩小把部分照护推向正式服务与协调层"
        summary = "- **摘要**：完整卡见[台账](%s)" % link
    else:
        link = "../ledger/96-102.md#j-096--ageing-and-smaller-households-move-part-of-care-toward-formal-and-coordination-layers"
        summary = "- **Summary**: See the [Full card](%s) in the ledger" % link
    replacement = heading + "\n\n" + summary + "\n"
    _write_file(path, text[:match.start()] + replacement + text[match.end():])
    return path


def _positive_embedded_summary(root):
    _replace_embedded_summary(root, "zh")
    _replace_embedded_summary(root, "en")
    return "zh/en C9 J-096 use explicit summary links"


def _break_summary_unknown_id(root):
    path = _replace_embedded_summary(root, "zh")
    text = _read_file(path).replace("### 判断卡片 1：J-096", "### 判断卡片 1：J-999", 1)
    _write_file(path, text)
    return "%s: summary heading uses unknown J-999" % path


def _break_summary_missing_id(root):
    path = _replace_embedded_summary(root, "zh", heading_id="J-096")
    text = _read_file(path).replace("### 判断卡片 1：J-096", "### 判断卡片 1", 1)
    _write_file(path, text)
    return "%s: summary heading lost J-096" % path


def _break_summary_content_disguise(root):
    """Rewrite a valid summary's prose while retaining its valid ledger link."""
    path = _replace_embedded_summary(root, "zh")
    text = _read_file(path).replace("完整卡见", "本页判断与台账相反，详见", 1)
    _write_file(path, text)
    return "%s: summary prose contradicts the required full-card handoff" % path


def _break_summary_appended_disguise(root):
    """Append a conflicting reader-visible sentence after an otherwise valid summary."""
    path = _replace_embedded_summary(root, "zh")
    text = _read_file(path)
    text = re.sub(r"(^- \*\*摘要\*\*[:：][^\n]*)",
                  r"\1；本页判断与台账相反", text, count=1, flags=re.M)
    _write_file(path, text)
    return "%s: valid summary link carries appended divergent prose" % path


def _break_summary_spaced_field(root):
    """Add a canonical field with visible whitespace before its colon."""
    path = _replace_embedded_summary(root, "zh")
    text = _read_file(path).replace(
        "\n\n- **摘要**", "\n\n- **一句话判断** ：本页采用另一判断\n- **摘要**", 1)
    _write_file(path, text)
    return "%s: canonical field has whitespace before its colon" % path


def _break_summary_missing_marker(root):
    """Keep a Chinese ledger link but remove the required summary field marker."""
    path = _replace_embedded_summary(root, "zh")
    text = _read_file(path).replace(
        "- **摘要**：完整卡见[台账]", "完整卡见[台账]", 1)
    _write_file(path, text)
    return "%s: Chinese ledger summary link has no 摘要 field" % path


def _break_english_chain_punctuation(root):
    path = _chain_doc(root, "en", "C11")
    text = _read_file(path)
    if "incidents; Use" not in text:
        raise AssertionError("C11 English action line has no stable punctuation")
    _write_file(path, text.replace("incidents; Use", "incidents；Use", 1))
    return "%s: English chain contains Chinese semicolon" % path


def _break_summary_wrong_language(root):
    path = _replace_embedded_summary(root, "en")
    text = _read_file(path).replace("**Summary**", "**摘要**", 1)
    text = text.replace("[Full card]", "[完整卡]", 1)
    _write_file(path, text)
    return "%s: English summary uses Chinese labels" % path


LENS_POSITIVE_CASES = [
    (u"broad L1–L9 prose is not nine declarations", _positive_broad_range),
    (u"explicit embedded summary link is accepted", _positive_embedded_summary),
]

def _break_chain_unknown_card_edge(root):
    path = os.path.join(root, "docs", "zh", "chains", "10-generation-becomes-free.md")
    text = _read_file(path)
    needle = '  S4 --> R4["J-017 连接变多，强关系不会同步变多"]'
    if needle not in text:
        raise AssertionError("C1 fixture has no stable terminal edge")
    _write_file(path, text.replace(needle, needle + '\n  R4 --> BAD["J-999 invented card"]', 1))
    return "zh C1: Mermaid edge cites J-999, which has no ledger card"


def _break_embedded_chain_field(root):
    """Change only a chain-page copy; the ledger remains authoritative."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    match = re.search(r"(^### 判断卡片 1：J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("C9 J-096 embedded card not found")
    body = re.sub(r"(^- \*\*一句话判断\*\*[:：][^\n]*)",
                  r"\1（副本负例）", match.group(1), count=1, flags=re.M)
    if body == match.group(1):
        raise AssertionError("C9 J-096 judgment field not found")
    _write_file(path, text[:match.start()] + body + text[match.end():])
    return "%s: J-096 one-sentence judgment diverged" % path


def _break_embedded_audience_field(root):
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    match = re.search(r"(^### 判断卡片 1：J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("C9 J-096 embedded card not found")
    body = re.sub(r"(^- \*\*受众规模\*\*[:：][^\n]*)",
                  r"\1（副本负例）", match.group(1), count=1, flags=re.M)
    if body == match.group(1):
        raise AssertionError("C9 J-096 audience field not found")
    _write_file(path, text[:match.start()] + body + text[match.end():])
    return "%s: J-096 audience scale diverged" % path


def _break_embedded_ledger_field(root):
    """Change the ledger field while leaving both embedded copies unchanged."""
    path = _card_path(root, "zh", "J-098")
    text = _read_file(path)
    body = re.sub(r"(^- \*\*一句话判断\*\*[:：][^\n]*)",
                  r"\1（台账负例）", text, count=1, flags=re.M)
    if body == text:
        raise AssertionError("J-098 judgment field not found")
    _write_file(path, body)
    return "zh J-098 ledger one-sentence judgment diverged"


def _break_embedded_en_field(root):
    """Change only the English chain-page copy for language-specific coverage."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    match = re.search(r"(^### Judgment card 1: J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("English C9 J-096 embedded card not found")
    body = re.sub(r"(^- \*\*One-sentence judgment\*\*:\s*[^\n]*)",
                  r"\1 (English-only negative control)", match.group(1), count=1, flags=re.M)
    if body == match.group(1):
        raise AssertionError("English J-096 judgment field not found")
    _write_file(path, text[:match.start()] + body + text[match.end():])
    return "%s: J-096 one-sentence judgment diverged (English only)" % path


def _break_embedded_en_missing_copy(root):
    """Remove the English C9 J-096 block while leaving the Chinese copy intact."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    pattern = r"^### Judgment card 1: J-096.*?(?=^### |^## |\Z)"
    new, count = re.subn(pattern, "", text, count=1, flags=re.M | re.S)
    if count != 1:
        raise AssertionError("English C9 J-096 embedded card not found")
    _write_file(path, new)
    return "%s: English J-096 embedded copy removed" % path


def _break_embedded_nested_heading(root):
    """Insert a nested heading before a divergent field in a card copy."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    heading = "### 判断卡片 1：J-096"
    if heading not in text:
        raise AssertionError("C9 J-096 embedded card not found")
    text = text.replace(heading,
                        heading + "\n\n#### 说明 0\n\n #### 说明 1\n\n  #### 说明 2\n\n   #### 说明 3\n",
                        1)
    old = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old not in text:
        raise AssertionError("C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, old + "（嵌套标题负例）", 1))
    return "%s: nested heading hides a divergent J-096 field" % path


def _break_embedded_english_fullwidth_colon(root):
    """Use a full-width field separator in a divergent English copy."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    old = "- **One-sentence judgment**: From 2027–2035"
    if old not in text:
        raise AssertionError("English C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, "- **One-sentence judgment**：From 2027–2035 (full-width separator negative)", 1))
    return "%s: full-width English field separator diverged" % path


def _break_embedded_indented_heading(root):
    """Indent a formal card heading while diverging one reader-visible field."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    heading = "### 判断卡片 1：J-096"
    if heading not in text:
        raise AssertionError("C9 J-096 embedded card not found")
    text = text.replace(heading, "  " + heading, 1)
    old = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old not in text:
        raise AssertionError("C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, old + "（缩进标题负例）", 1))
    return "%s: indented J-096 heading hides a divergent field" % path


def _break_embedded_indented_list_field(root):
    """Keep a divergent field reader-visible in an indented Markdown list."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old not in text:
        raise AssertionError("C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, "  * **一句话判断**：2027–2035 年（缩进列表负例）", 1))
    return "%s: indented-list J-096 field diverged" % path


def _break_embedded_ordered_list_field(root):
    """Keep a divergent field reader-visible in an ordered Markdown list."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    old = "- **One-sentence judgment**: From 2027–2035"
    if old not in text:
        raise AssertionError("English C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, "1. **One-sentence judgment**: From 2027–2035 (ordered-list negative)", 1))
    return "%s: ordered-list J-096 field diverged" % path


def _break_embedded_blockquote_field(root):
    """Keep a divergent field reader-visible inside a blockquote list."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old not in text:
        raise AssertionError("C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, "> - **一句话判断**：2027–2035 年（引用块负例）", 1))
    return "%s: blockquote J-096 field diverged" % path


def _break_embedded_html_field(root):
    """Keep a divergent field reader-visible with an HTML strong label."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    old = "- **One-sentence judgment**: From 2027–2035"
    if old not in text:
        raise AssertionError("English C9 J-096 judgment field not found")
    _write_file(path, text.replace(old, "- <strong>One-sentence judgment</strong>: From 2027–2035 (HTML label negative)", 1))
    return "%s: HTML-labeled J-096 field diverged" % path


def _break_embedded_html_heading(root):
    """Make a formal copy's heading reader-visible HTML while diverging a field."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old_heading = "### 判断卡片 1：J-096"
    old_field = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old_heading not in text or old_field not in text:
        raise AssertionError("C9 J-096 heading/field not found")
    text = text.replace(old_heading, "<h3>判断卡片 1：J-096</h3>", 1)
    _write_file(path, text.replace(old_field, "- **一句话判断**：2027–2035 年（HTML heading negative）", 1))
    return "%s: HTML-heading J-096 field diverged" % path


def _break_embedded_blockquote_heading(root):
    """Make a formal copy's heading reader-visible blockquote while diverging a field."""
    path = _chain_doc(root, "en", "C9")
    text = _read_file(path)
    old_heading = "### Judgment card 1: J-096"
    old_field = "- **One-sentence judgment**: From 2027–2035"
    if old_heading not in text or old_field not in text:
        raise AssertionError("English C9 J-096 heading/field not found")
    text = text.replace(old_heading, "> ### Judgment card 1: J-096", 1)
    _write_file(path, text.replace(old_field, "- **One-sentence judgment**: From 2027–2035 (blockquote heading negative)", 1))
    return "%s: blockquote-heading J-096 field diverged" % path


def _break_embedded_deep_blockquote_heading(root):
    """Keep a divergent copy under an arbitrarily nested blockquote heading."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old_heading = "### 判断卡片 1：J-096"
    old_field = "- **一句话判断**：2027–2035 年，老龄化与家庭缩小会使部分照护"
    if old_heading not in text or old_field not in text:
        raise AssertionError("C9 J-096 heading/field not found")
    text = text.replace(old_heading, "> > > > ### 判断卡片 1：J-096", 1)
    _write_file(path, text.replace(old_field, "- **一句话判断**：2027–2035 年（深层引用块负例）", 1))
    return "%s: deeply nested blockquote-heading J-096 field diverged" % path


def _break_embedded_mixed_field_wrappers(root):
    """Keep a divergent copy whose fields use mixed nested HTML/Markdown wrappers."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    heading = "### 判断卡片 1：J-096"
    start = text.find(heading)
    if start < 0:
        raise AssertionError("C9 J-096 heading not found")
    end = text.find("\n## ", start)
    if end < 0:
        end = len(text)
    section = text[start:end]
    field_lines = re.compile(r"(?m)^(- \*\*[^\n]+)$")
    wrapped, count = field_lines.subn(
        r"<div><blockquote><ul><li>\1</li></ul></blockquote></div>", section)
    if count < len(CARD_FIELDS["zh"]):
        raise AssertionError("C9 J-096 canonical fields not all found")
    wrapped = wrapped.replace("2027–2035 年，老龄化与家庭缩小会使部分照护",
                              "2027–2035 年（混合包装负例）", 1)
    _write_file(path, text[:start] + wrapped + text[end:])
    return "%s: mixed nested field wrappers diverged" % path


def _break_level_two_embedded_field(root):
    """Change the J-109 summary under its real level-two card heading."""
    path = _chain_doc(root, "zh", "C15")
    text = _read_file(path)
    old = "- **摘要**：完整卡见台账"
    if old not in text:
        raise AssertionError("C15 J-109 summary not found")
    _write_file(path, text.replace(old, old + "（副本负例）", 1))
    return "%s: level-two J-109 summary diverged" % path


def _break_embedded_unknown_card(root):
    """Rename a formal embedded heading to an unregistered judgment id."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "### 判断卡片 1：J-096"
    if old not in text:
        raise AssertionError("C9 J-096 embedded heading not found")
    _write_file(path, text.replace(old, "### 判断卡片 1：J-999", 1))
    return "%s: embedded heading changed from J-096 to unknown J-999" % path


def _break_embedded_card_id_suffix(root):
    """Append a visible letter so J-096 is no longer a valid card token."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "### 判断卡片 1：J-096"
    if old not in text:
        raise AssertionError("C9 J-096 embedded heading not found")
    _write_file(path, text.replace(old, "### 判断卡片 1：J-096X", 1))
    return "%s: embedded heading changed from J-096 to invalid J-096X" % path


def _break_embedded_missing_card_id(root):
    """Remove the id while retaining the formal card fields."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "### 判断卡片 1：J-096"
    if old not in text:
        raise AssertionError("C9 J-096 embedded heading not found")
    _write_file(path, text.replace(old, "### 判断卡片 1", 1))
    return "%s: embedded formal card heading lost J-096" % path


def _break_embedded_card_id_punctuation(root):
    """Append a dotted sub-number so J-096 is no longer a complete token."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    old = "### 判断卡片 1：J-096"
    if old not in text:
        raise AssertionError("C9 J-096 embedded heading not found")
    _write_file(path, text.replace(old, "### 判断卡片 1：J-096.1", 1))
    return "%s: embedded heading changed from J-096 to invalid J-096.1" % path


def _break_embedded_duplicate_field(root):
    """Duplicate a canonical field so it cannot be mistaken for a summary."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    match = re.search(r"(^### 判断卡片 1：J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("C9 J-096 embedded card not found")
    section = match.group(1)
    field = re.search(r"^- \*\*一句话判断\*\*[:：][^\n]*$", section, re.M)
    if not field:
        raise AssertionError("C9 J-096 judgment field not found")
    section = section[:field.end()] + "\n" + field.group(0) + section[field.end():]
    _write_file(path, text[:match.start()] + section + text[match.end():])
    return "%s: J-096 canonical field duplicated" % path


def _break_embedded_duplicate_all_fields(root):
    """Duplicate every canonical field to attack formal-block discovery itself."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    match = re.search(r"(^### 判断卡片 1：J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("C9 J-096 embedded card not found")
    section = match.group(1)
    for field in CARD_FIELDS["zh"]:
        pattern = r"^- \*\*%s\*\*[:：][^\n]*$" % re.escape(field)
        field_match = re.search(pattern, section, re.M)
        if not field_match:
            raise AssertionError("C9 J-096 field %s not found" % field)
        line = field_match.group(0)
        section = section[:field_match.end()] + "\n" + line + section[field_match.end():]
    _write_file(path, text[:match.start()] + section + text[match.end():])
    return "%s: all J-096 canonical fields duplicated" % path


def _break_embedded_zero_width_summary_disguise(root):
    """Hide every field label with Cf characters and add a misleading summary link."""
    path = _chain_doc(root, "zh", "C9")
    text = _read_file(path)
    match = re.search(r"(^### 判断卡片 1：J-096.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError("C9 J-096 embedded card not found")
    section = match.group(1)
    section = re.sub(r"(^- \*\*一句话判断\*\*[:：][^\n]*)",
                     r"\1（伪装负例）", section, count=1, flags=re.M)
    for field in CARD_FIELDS["zh"]:
        pattern = r"(^- \*\*)%s(\*\*[:：])" % re.escape(field)
        masked = "\u200b".join(field)
        section, count = re.subn(pattern, r"\1" + masked + r"\2", section, count=1, flags=re.M)
        if count != 1:
            raise AssertionError("C9 J-096 field %s not found" % field)
    section += "- **摘要**：完整卡见[台账](../ledger/96-102.md#j-096--老龄化与家庭缩小把部分照护推向正式服务与协调层)\n"
    _write_file(path, text[:match.start()] + section + text[match.end():])
    return "%s: zero-width field labels disguise a divergent summary" % path


def _break_bilingual_chain_skeleton(root):
    path = os.path.join(root, "docs", "en", "chains", "10-generation-becomes-free.md")
    text = _read_file(path)
    needle = '  S4 --> R4["J-017 connections multiply, strong ties do not follow"]'
    if needle not in text:
        raise AssertionError("C1 English fixture has no stable terminal edge")
    _write_file(path, text.replace(needle, '  S4 --> R3["J-017 More connections, not more strong ties"]', 1))
    return "en C1: one edge endpoint diverges from the Chinese skeleton"


def _break_malformed_labeled_chain_edge(root):
    path = os.path.join(root, "docs", "zh", "chains", "10-generation-becomes-free.md")
    text = _read_file(path)
    needle = '  S4 --> R4["J-017 连接变多，强关系不会同步变多"]'
    if needle not in text:
        raise AssertionError("C1 fixture has no stable terminal edge")
    _write_file(path, text.replace(needle, needle + '\n  R4 -->|"unclosed label" R3', 1))
    return "zh C1: malformed labeled Mermaid edge has no closing pipe/target"


def _break_navigation_node_set(root):
    path = os.path.join(root, "README.md")
    text = _read_file(path)
    needle = "  C13[C13 财政与政治] --> C9"
    if needle not in text:
        raise AssertionError("README navigation fixture has no C13 node")
    _write_file(path, text.replace(needle, "    C99[C99 财政与政治] --> C9", 1))
    return "README navigation: C13 node changed to C99 without changing N/M layers"


def _break_navigation_source_layer(root):
    path = os.path.join(root, "docs", "zh", "20-mid.md")
    text = _read_file(path)
    needle = "  M -.人口与照护.-> C9"
    if needle not in text:
        raise AssertionError("mid navigation fixture has no C9 layer edge")
    _write_file(path, text.replace(needle, "  N -.人口与照护.-> C9", 1))
    return "zh mid navigation: C9 source layer changed from M to N"


def _break_navigation_invalid_layer(root):
    path = os.path.join(root, "docs", "zh", "20-mid.md")
    text = _read_file(path)
    needle = "  M -.人口与照护.-> C9[C9 老龄化与制度化照护]"
    if needle not in text:
        raise AssertionError("mid navigation fixture has no C9 layer edge")
    _write_file(path, text.replace(needle, "  X -.人口与照护.-> C9[C9 老龄化与制度化照护]", 1))
    return "zh mid navigation: C9 source layer changed from M to invalid X"


def _break_navigation_duplicate_layer(root):
    path = os.path.join(root, "docs", "zh", "20-mid.md")
    text = _read_file(path)
    needle = "  M -.人口与照护.-> C9[C9 老龄化与制度化照护]"
    if needle not in text:
        raise AssertionError("mid navigation fixture has no C9 layer edge")
    _write_file(path, text.replace(needle, needle + "\n" + needle, 1))
    return "zh mid navigation: duplicate M source edge for C9"

PARITY_NEGATIVE_CASES = [
    (u"embedded audience field diverges", "chain-card-parity", _break_embedded_audience_field),
    (u"embedded chain card copy diverges", "chain-card-parity", _break_embedded_chain_field),
    (u"nested heading hides embedded card", "chain-card-parity", _break_embedded_nested_heading),
    (u"English full-width field separator diverges", "chain-card-parity", _break_embedded_english_fullwidth_colon),
    (u"indented heading hides embedded card", "chain-card-parity", _break_embedded_indented_heading),
    (u"indented-list embedded field diverges", "chain-card-parity", _break_embedded_indented_list_field),
    (u"ordered-list embedded field diverges", "chain-card-parity", _break_embedded_ordered_list_field),
    (u"blockquote embedded field diverges", "chain-card-parity", _break_embedded_blockquote_field),
    (u"HTML-labeled embedded field diverges", "chain-card-parity", _break_embedded_html_field),
    (u"HTML-heading embedded field diverges", "chain-card-parity", _break_embedded_html_heading),
    (u"blockquote-heading embedded field diverges", "chain-card-parity", _break_embedded_blockquote_heading),
    (u"deeply nested blockquote-heading embedded field diverges", "chain-card-parity", _break_embedded_deep_blockquote_heading),
    (u"mixed nested field wrappers diverge", "chain-card-parity", _break_embedded_mixed_field_wrappers),
    (u"level-two embedded card diverges", "chain-card-parity", _break_level_two_embedded_field),
    (u"English-only embedded copy diverges", "chain-card-parity", _break_embedded_en_field),
    (u"English embedded copy is missing", "chain-card-parity", _break_embedded_en_missing_copy),
    (u"embedded card heading uses unknown id", "chain-card-parity", _break_embedded_unknown_card),
    (u"embedded card heading has an invalid suffix", "chain-card-parity", _break_embedded_card_id_suffix),
    (u"embedded card heading has an invalid dotted suffix", "chain-card-parity", _break_embedded_card_id_punctuation),
    (u"embedded card heading loses its id", "chain-card-parity", _break_embedded_missing_card_id),
    (u"embedded card repeats a canonical field", "chain-card-parity", _break_embedded_duplicate_field),
    (u"embedded card repeats every canonical field", "chain-card-parity", _break_embedded_duplicate_all_fields),
    (u"zero-width fields disguise a summary", "chain-card-parity", _break_embedded_zero_width_summary_disguise),
    (u"summary card uses unknown id", "chain-card-parity", _break_summary_unknown_id),
    (u"summary card loses its id", "chain-card-parity", _break_summary_missing_id),
    (u"summary card prose is misleading", "chain-card-parity", _break_summary_content_disguise),
    (u"summary card appends divergent prose", "chain-card-parity", _break_summary_appended_disguise),
    (u"summary card has a spaced canonical field", "chain-card-parity", _break_summary_spaced_field),
    (u"summary card lacks its field marker", "chain-card-parity", _break_summary_missing_marker),
    (u"summary card crosses language labels", "chain-card-parity", _break_summary_wrong_language),
    (u"English chain uses Chinese semicolon", "english-punctuation", _break_english_chain_punctuation),
    (u"ledger card diverges from embedded copy", "chain-card-parity", _break_embedded_ledger_field),
]

PARITY_NEGATIVE_MARKERS = {
    u"embedded audience field diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"embedded chain card copy diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"nested heading hides embedded card": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"English full-width field separator diverges": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"indented heading hides embedded card": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"indented-list embedded field diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"ordered-list embedded field diverges": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"blockquote embedded field diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"HTML-labeled embedded field diverges": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"HTML-heading embedded field diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"blockquote-heading embedded field diverges": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"deeply nested blockquote-heading embedded field diverges": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"mixed nested field wrappers diverge": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"level-two embedded card diverges": ("docs/zh/chains/150-households-three-clocks.md", "J-109"),
    u"English-only embedded copy diverges": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"English embedded copy is missing": ("docs/en/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"embedded card heading uses unknown id": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-999"),
    u"embedded card heading has an invalid suffix": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "missing card id"),
    u"embedded card heading has an invalid dotted suffix": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "missing card id"),
    u"embedded card heading loses its id": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "missing card id"),
    u"embedded card repeats a canonical field": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"embedded card repeats every canonical field": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"zero-width fields disguise a summary": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"summary card uses unknown id": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-999"),
    u"summary card loses its id": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "missing card id"),
    u"summary card prose is misleading": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"summary card appends divergent prose": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"summary card has a spaced canonical field": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
    u"summary card lacks its field marker": ("docs/zh/chains/90-aging-care-and-institutional-substitution.md", "J-096"),
}

NEGATIVE_CASES = [
    (u"chain Mermaid cites a non-existent card", "chain-mermaid",
     _break_chain_unknown_card_edge),
    (u"bilingual chain Mermaid skeleton diverges", "chain-mermaid",
     _break_bilingual_chain_skeleton),
    (u"malformed labeled chain Mermaid edge", "chain-mermaid",
     _break_malformed_labeled_chain_edge),
    (u"navigation map loses a chain node", "navigation-mermaid",
     _break_navigation_node_set),
    (u"navigation map changes an N/M source layer", "navigation-mermaid",
     _break_navigation_source_layer),
    (u"navigation map duplicates an N/M source edge", "navigation-mermaid",
     _break_navigation_duplicate_layer),
    (u"navigation map uses an invalid source layer", "navigation-mermaid",
     _break_navigation_invalid_layer),
    (u"README/ledger dimension grade differs", "dimension-status",
     _break_dimension_status_ledger_grade),
    (u"ledger loses one no-entry dimension", "dimension-status",
     _break_dimension_status_missing_gap),
    (u"public prose exposes an internal work-unit id", "public-internal-ids",
     _break_public_internal_id),
    (u"dangling anchor", "links", _break_dangling_anchor),
    (u"CONTRIBUTING link into the ledger goes dead", "links",
     _break_contributing_anchor),
    (u"dependency edge disagrees with the card", "dep-graph", _break_dep_edge),
    (u"invented Mermaid dependency edge", "mermaid-graph", _break_mermaid_edge),
    (u"overview row missing while card remains", "overview-rows", _break_missing_overview_row),
    (u"blank line splits the overview table", "table-rows",
     _break_split_overview_table),
    (u"dependency graph row duplicated", "graph-rows", _break_duplicate_graph_row),
    (u"root card's dependency edge disagrees", "dep-graph",
     _break_root_dep_edge),
    (u"card exists in zh only", "bilingual-cards",
     _break_single_language_card("en")),
    (u"card exists in en only", "bilingual-cards",
     _break_single_language_card("zh")),
    (u"card ids differ while counts stay equal", "bilingual-cards",
     _break_equal_count_bilingual_card_set),
    (u"confidence outside the whitelist", "confidence",
     _set_confidence("zh", u"\u6781\u9ad8")),  # 极高
    (u"second confidence value in the same card", "confidence",
     _break_second_confidence),
    (u"confidence value unreadable", "confidence",
     _break_unreadable_confidence),
    (u"one value readable, one field unreadable", "confidence",
     _break_partial_readable_confidence),
    (u"required card field missing", "card-fields", _break_missing_field),
    (u"new card missing audience scale", "audience-scale",
     _break_new_card_without_audience_scale),
    (u"audience scale embedded inside diffusion review", "audience-scale",
     _break_embedded_audience_scale),
    (u"standalone audience scale lacks required structure", "audience-scale",
     _break_malformed_audience_scale),
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
         _read_file(_readme(root, "zh")) + u"\n\u53c2\u89c1 C99\u3002\n"),
         u"README.md: prose cites C99")[1]),
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
    (u"a registered chain whose file has no H1", "chain-registry",
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
    (u"a wrong count wrapped in a link", "readme-counts",
     _break_count_hidden_by_link),
    (u"a wrong count wrapped in inline HTML", "readme-counts",
     _break_count_hidden_by_html),
    (u"a wrong count in full-width digits", "readme-counts",
     _break_count_in_fullwidth_digits),
    (u"the same judgment card pasted twice", "ledger",
     _break_duplicate_card),
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
    ("zh", u"中。"),                 # sentence punctuation is not canonical
    ("zh", u"低（仅图景）。"),         # qualifier punctuation is not canonical
    ("en", "High."),                 # sentence punctuation is not canonical
    ("en", "Low (landscape only)."),  # qualifier punctuation is not canonical
    ("en", "high"),                  # canonical values are case-sensitive
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
    ("en", "High"), ("en", "Medium"), ("en", "Low"),
    # The canonical form is deliberately punctuation-free, including the
    # landscape-only qualifier. Sentence-final punctuation is a rejected drift.
    ("zh", u"\u4f4e\uff08\u4ec5\u56fe\u666f\uff09"),
    ("en", "Low (landscape only)"),
]


def _embedded_counts(output):
    """Read the parity inventory emitted by a checker run."""
    pairs = re.findall(r"embedded card copies \((zh|en)\): (\d+)", output)
    return tuple((lang, int(count)) for lang, count in pairs)


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
        baseline_embedded_counts = _embedded_counts(out)
        if (len(baseline_embedded_counts) != 2 or
                len(set(count for _lang, count in baseline_embedded_counts)) != 1):
            print("baseline: embedded-card inventory is unexpected: %r\n" %
                  (baseline_embedded_counts,))
            return 1
        print("baseline: embedded-card inventory %r\n" %
              (baseline_embedded_counts,))

        def fresh():
            work = os.path.join(base, "case-%d" % next(counter))
            shutil.copytree(pristine, work)
            return work

        print("negative cases (the checker must exit non-zero, "
              "and name the right check):")
        for title, tag, mutate in PARITY_NEGATIVE_CASES + NEGATIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            expected_marker = PARITY_NEGATIVE_MARKERS.get(title)
            marker_ok = (expected_marker is None or
                         all(part in out for part in expected_marker))
            ok = code != 0 and ("[%s]" % tag) in out and marker_ok
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, title, u"exit %d, expected [%s] — %s" % (code, tag, detail))

        print("\nlens/card negative cases (each must name its chain/card location):")
        for title, tag, mutate, marker in LENS_NEGATIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            ok = code != 0 and ("[%s]" % tag) in out and marker in out
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, title, u"exit %d, expected [%s] + %s — %s" %
                   (code, tag, marker, detail))

        print("\nlens/card edits that must NOT be reported:")
        for title, mutate in LENS_POSITIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            ok = code == 0 and _embedded_counts(out) == baseline_embedded_counts
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, title, u"exit %d — %s" % (code, detail))

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
            ok = code == 0 and _embedded_counts(out) == baseline_embedded_counts
            passed, failed = (passed + 1, failed) if ok else (passed, failed + 1)
            report(ok, u"%s card: %s" % (lang, value), u"exit %d" % code)

        print("\nedits that must NOT be reported:")
        for title, mutate in POSITIVE_CASES:
            work = fresh()
            detail = mutate(work)
            code, out = _run_checker(work)
            ok = code == 0 and _embedded_counts(out) == baseline_embedded_counts
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
