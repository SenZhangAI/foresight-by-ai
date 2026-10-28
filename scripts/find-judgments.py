#!/usr/bin/env python3
"""Query the bilingual judgment-card register without rebuilding a second index.

The canonical input is the card shards under ``docs/{zh,en}/ledger``.  The
script parses both projections on every invocation, compares their J-NNN sets,
and then applies the same normalized filters to the shared IDs.  It deliberately
requires at least one filter: an accidental unfiltered invocation must not look
like a meaningful query over the whole register.

Examples:
    python3 scripts/find-judgments.py --chain C4 --status ACTIVE
    python3 scripts/find-judgments.py --chain C4 --confidence MEDIUM --format json

Exit status is 0 for a valid query (including an explicit empty result), 2 for
invalid CLI values or an inconsistent bilingual register, and 1 for an
unexpected parse/input error.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parent.parent
SOURCE_REPO = REPO
BASELINE_REF = "HEAD^"
LANGS = ("zh", "en")
CARD_HEADING = re.compile(r"^###\s+(J-\d{3})\s+·\s+(.+?)\s*$")
FIELD_LINE = re.compile(r"^-\s+\*\*(.+?)\*\*\s*(?:：|:)\s*(.*)$")
CHAIN_RE = re.compile(r"\bC\d+\b")
SEMANTIC_FIELDS = (
    "title", "judgment", "reasoning_chain", "falsifier",
    "leading_indicator", "opposing_mechanism",
)

FIELD_NAMES = {
    "zh": {
        "status": "状态",
        "confidence": "置信度",
        "time_window": "时间窗",
        "source": "出处",
        "judgment": "一句话判断",
        "reasoning_chain": "推理链",
        "falsifier": "证伪条件",
        "leading_indicator": "领先指标",
        "opposing_mechanism": "最强反方",
    },
    "en": {
        "status": "Status",
        "confidence": "Confidence",
        "time_window": "Time window",
        "source": "Source",
        "judgment": "One-sentence judgment",
        "reasoning_chain": "Reasoning chain",
        "falsifier": "Falsifier",
        "leading_indicator": "Leading indicator",
        "opposing_mechanism": "Strongest opposing mechanism",
    },
}
STATUS_VALUES = {"ACTIVE", "HIT", "FALSIFIED", "REVISED", "LANDSCAPE_ONLY"}
CONFIDENCE_VALUES = {"HIGH", "MEDIUM", "LOW", "LOW_LANDSCAPE"}
CONFIDENCE_DISPLAY = {
    "zh": {"高": "HIGH", "中": "MEDIUM", "低": "LOW", "低（仅图景）": "LOW_LANDSCAPE"},
    "en": {"High": "HIGH", "Medium": "MEDIUM", "Low": "LOW", "Low (landscape only)": "LOW_LANDSCAPE"},
}

class RegisterError(ValueError):
    """The bilingual register violates the query tool's structural contract."""


@dataclass(frozen=True)
class Card:
    id: str
    title: str
    language: str
    path: str
    anchor: str
    status: str
    status_raw: str
    confidence: str
    confidence_raw: str
    time_window: str
    chains: tuple[str, ...]
    judgment: str
    reasoning_chain: str
    falsifier: str
    leading_indicator: str
    opposing_mechanism: str


def slugify_heading(text: str) -> str:
    """Approximate GitHub's heading slug for the stable card headings."""
    text = unicodedata.normalize("NFKC", text).lower()
    out: list[str] = []
    for char in text:
        category = unicodedata.category(char)
        if char in "-_" or category[0] in {"L", "N"}:
            out.append(char)
        elif char.isspace():
            out.append("-")
        # GitHub drops punctuation and symbols from these headings.
    return "".join(out).strip("-")


def iter_card_blocks_text(text: str) -> Iterable[tuple[str, str, list[str], int]]:
    lines = text.splitlines()
    current: tuple[str, str, list[str], int] | None = None
    for number, line in enumerate(lines, start=1):
        match = CARD_HEADING.match(line)
        if match:
            if current is not None:
                yield current
            current = (match.group(1), match.group(2), [], number)
        elif current is not None:
            current[2].append(line)
    if current is not None:
        yield current


def iter_card_blocks(path: Path) -> Iterable[tuple[str, str, list[str], int]]:
    yield from iter_card_blocks_text(path.read_text(encoding="utf-8"))


def parse_field(lines: list[str], label: str) -> str:
    matches = []
    for line in lines:
        match = FIELD_LINE.match(line)
        if match and match.group(1).strip() == label:
            matches.append(match.group(2).strip())
    if len(matches) > 1:
        raise ValueError(f"duplicate query field {label!r}: {matches!r}")
    return matches[0] if matches else ""


def normalize_status(raw: str, lang: str) -> str:
    # Status notes are allowed after a valid token (for example, a parenthetical
    # review note), but an unknown prefix/suffix must never be hidden by a
    # substring match such as ``UNKNOWN (previously ACTIVE)``.
    value = raw.strip()
    match = re.fullmatch(
        r"`?(LANDSCAPE_ONLY|ACTIVE|HIT|FALSIFIED|REVISED)`?"
        r"\s*(?:[。.]|[（(][\s\S]*[）)][。.]?|[—-]{1,2}[\s\S]*)?",
        value,
    )
    if match:
        return match.group(1)
    raise ValueError(f"{lang}: cannot parse status: {raw!r}")


def normalize_confidence(raw: str, lang: str) -> str:
    value = raw.strip().strip("`").split("（", 1)[0].split("(", 1)[0].strip()
    if raw.strip() in CONFIDENCE_DISPLAY[lang]:
        return CONFIDENCE_DISPLAY[lang][raw.strip()]
    if lang == "zh":
        if "低" in raw and "图景" in raw:
            return "LOW_LANDSCAPE"
        value = {"高": "HIGH", "中": "MEDIUM", "低": "LOW"}.get(value, "")
    else:
        value = {"High": "HIGH", "Medium": "MEDIUM", "Low": "LOW"}.get(value, "")
    if value not in CONFIDENCE_VALUES:
        raise ValueError(f"{lang}: cannot parse confidence: {raw!r}")
    return value


def load_language(lang: str, repo: Path | None = None, git_ref: str | None = None) -> dict[str, Card]:
    root = repo or REPO
    directory = root / "docs" / lang / "ledger"
    cards: dict[str, Card] = {}
    for path in sorted(directory.glob("*.md")):
        relative = path.relative_to(root).as_posix()
        if git_ref is None:
            text = path.read_text(encoding="utf-8")
        else:
            try:
                text = subprocess.check_output(
                    ["git", "-C", str(root), "show", f"{git_ref}:{relative}"],
                    stderr=subprocess.STDOUT,
                    text=True,
                )
            except (OSError, subprocess.CalledProcessError) as error:
                raise RegisterError(
                    f"cannot read bilingual baseline {git_ref}:{relative}: {error}"
                ) from error
        for card_id, title, lines, _line in iter_card_blocks_text(text):
            if card_id in cards:
                raise ValueError(f"duplicate {card_id} in {lang}: {relative}")
            names = FIELD_NAMES[lang]
            source = parse_field(lines, names["source"])
            status_raw = parse_field(lines, names["status"])
            confidence_raw = parse_field(lines, names["confidence"])
            status = normalize_status(status_raw, lang)
            confidence = normalize_confidence(confidence_raw, lang)
            time_window = parse_field(lines, names["time_window"])
            semantic = {
                key: parse_field(lines, names[key])
                for key in SEMANTIC_FIELDS
                if key != "title"
            }
            if not source or not time_window or any(not semantic[key] for key in semantic):
                missing = [key for key, value in semantic.items() if not value]
                raise ValueError(
                    f"{relative}: {card_id} is missing a query field"
                    + (f" ({', '.join(missing)})" if missing else "")
                )
            cards[card_id] = Card(
                id=card_id,
                title=title,
                language=lang,
                path=relative,
                anchor=slugify_heading(f"{card_id} · {title}"),
                status=status,
                status_raw=status_raw,
                confidence=confidence,
                confidence_raw=confidence_raw,
                time_window=time_window,
                chains=tuple(sorted(set(CHAIN_RE.findall(source)), key=lambda item: int(item[1:]))),
                judgment=semantic["judgment"],
                reasoning_chain=semantic["reasoning_chain"],
                falsifier=semantic["falsifier"],
                leading_indicator=semantic["leading_indicator"],
                opposing_mechanism=semantic["opposing_mechanism"],
            )
    return cards


def time_window_signature(value: str) -> tuple[str, ...]:
    """Compare bilingual windows by their explicit date or year endpoints."""
    tokens = tuple(
        re.findall(r"\b\d{4}(?:[-/]\d{1,2}(?:[-/]\d{1,2})?)?\b", unicodedata.normalize("NFKC", value))
    )
    return tokens or (normalize_time_window(value),)


def normalize_time_window(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower()
    value = re.sub(r"\bto\b", "-", value)
    value = value.replace("–", "-").replace("—", "-").replace("至", "-")
    value = "".join(char for char in value if unicodedata.category(char)[0] not in {"P", "S"} or char == "-")
    return re.sub(r"\s+", "", value)


def time_window_matches(requested: str, actual: str) -> bool:
    requested_signature = time_window_signature(requested)
    actual_signature = time_window_signature(actual)
    if any(re.search(r"\b\d{4}", token) for token in requested_signature):
        return all(
            any(token == actual_token or actual_token.startswith(token + "-") for actual_token in actual_signature)
            for token in requested_signature
        )
    return normalize_time_window(requested) in normalize_time_window(actual)


def compare_semantic_fields(
    current: dict[str, dict[str, Card]],
    baseline: dict[str, dict[str, Card]],
) -> None:
    """Reject one-sided edits to bilingual meaning-bearing fields.

    Chinese and English text cannot be compared byte-for-byte.  Instead, the
    check compares the *change set* for every paired field against the last
    committed bilingual snapshot: a title or argument changed on only one
    side is semantic drift, while a deliberate bilingual edit changes both
    projections together.  This also gives an actionable field name instead
    of treating the issue as generic metadata drift.
    """
    for card_id in sorted(set(current["zh"]) & set(current["en"])):
        for field in SEMANTIC_FIELDS:
            current_zh = getattr(current["zh"][card_id], field)
            current_en = getattr(current["en"][card_id], field)
            baseline_zh = getattr(baseline["zh"].get(card_id), field, None)
            baseline_en = getattr(baseline["en"].get(card_id), field, None)
            if baseline_zh is None or baseline_en is None:
                continue
            zh_changed = current_zh != baseline_zh
            en_changed = current_en != baseline_en
            if zh_changed != en_changed:
                changed_language = "zh" if zh_changed else "en"
                raise RegisterError(
                    f"bilingual semantic field drift for {card_id}; "
                    f"field={field}; changed only in {changed_language}"
                )


def load_baseline() -> dict[str, dict[str, Card]]:
    """Load the previous bilingual snapshot used for change-set parity.

    Tests replace ``REPO`` with a temporary copy; in that case ``SOURCE_REPO``
    remains the checked-out project and provides the same baseline.  If the
    repository has no parent commit (or Git is unavailable), the semantic
    guarantee cannot be established, so this function fails closed instead of
    silently reducing the check to field presence.
    """
    root = SOURCE_REPO if REPO != SOURCE_REPO else REPO
    try:
        return {
            lang: load_language(lang, repo=root, git_ref=BASELINE_REF)
            for lang in LANGS
        }
    except (OSError, RegisterError, ValueError, UnicodeError) as error:
        raise RegisterError(
            "bilingual semantic baseline unavailable; refusing to run semantic checks"
        ) from error


def card_link(card: Card) -> str:
    return f"{card.path}#{card.anchor}"


def validate_register_ids(ids: set[str], lang: str) -> None:
    """Reject malformed or gapped IDs without freezing a card-count constant."""
    malformed = sorted(card_id for card_id in ids if not re.fullmatch(r"J-\d{3}", card_id))
    if malformed:
        raise RegisterError(f"invalid judgment IDs in {lang}: {malformed}")
    if not ids:
        raise RegisterError(f"empty judgment register in {lang}")
    numbers = sorted(int(card_id[2:]) for card_id in ids)
    expected = set(range(1, numbers[-1] + 1))
    actual = set(numbers)
    if actual != expected:
        missing = [f"J-{number:03d}" for number in sorted(expected - actual)]
        raise RegisterError(f"gapped judgment register in {lang}; missing={missing}")


def build_records() -> list[dict]:
    projections = {lang: load_language(lang) for lang in LANGS}
    ids = {lang: set(cards) for lang, cards in projections.items()}
    for lang, card_ids in ids.items():
        validate_register_ids(card_ids, lang)
    zh_ids, en_ids = ids["zh"], ids["en"]
    if zh_ids != en_ids:
        missing_zh = sorted(en_ids - zh_ids)
        missing_en = sorted(zh_ids - en_ids)
        raise RegisterError(f"bilingual ID mismatch; missing zh={missing_zh}, missing en={missing_en}")
    compare_semantic_fields(projections, load_baseline())
    records: list[dict] = []
    for card_id in sorted(zh_ids, key=lambda item: int(item[2:])):
        zh, en = projections["zh"][card_id], projections["en"][card_id]
        if (
            zh.chains != en.chains
            or zh.status != en.status
            or zh.confidence != en.confidence
            or time_window_signature(zh.time_window) != time_window_signature(en.time_window)
        ):
            raise RegisterError(
                f"bilingual metadata mismatch for {card_id}; "
                f"zh=(chains={zh.chains}, status={zh.status}, confidence={zh.confidence}, time_window={zh.time_window!r}), "
                f"en=(chains={en.chains}, status={en.status}, confidence={en.confidence}, time_window={en.time_window!r})"
            )
        records.append({
            "id": card_id,
            "chains": list(zh.chains),
            "status": zh.status,
            "confidence": zh.confidence,
            "time_window": zh.time_window,
            "zh": {
                "title": zh.title,
                "judgment": zh.judgment,
                "reasoning_chain": zh.reasoning_chain,
                "falsifier": zh.falsifier,
                "leading_indicator": zh.leading_indicator,
                "opposing_mechanism": zh.opposing_mechanism,
                "status": zh.status_raw,
                "confidence": zh.confidence_raw,
                "time_window": zh.time_window,
                "link": card_link(zh),
            },
            "en": {
                "title": en.title,
                "judgment": en.judgment,
                "reasoning_chain": en.reasoning_chain,
                "falsifier": en.falsifier,
                "leading_indicator": en.leading_indicator,
                "opposing_mechanism": en.opposing_mechanism,
                "status": en.status_raw,
                "confidence": en.confidence_raw,
                "time_window": en.time_window,
                "link": card_link(en),
            },
        })
    return records


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query the bilingual judgment-card register discovered from the ledger shards.")
    parser.add_argument("--chain", metavar="C4", help="filter by chain identifier, e.g. C4")
    parser.add_argument("--status", choices=sorted(STATUS_VALUES), help="filter by card status")
    parser.add_argument("--confidence", choices=sorted(CONFIDENCE_VALUES), help="filter by normalized confidence")
    parser.add_argument("--time-window", metavar="TEXT", help="match the normalized time-window field")
    parser.add_argument("--format", choices=("table", "json"), default="table")
    args = parser.parse_args(argv)
    if not any((args.chain, args.status, args.confidence, args.time_window)):
        parser.error("at least one filter is required; refusing an unfiltered full-register dump")
    if args.chain and not re.fullmatch(r"C\d+", args.chain.upper()):
        parser.error("--chain must be a chain identifier such as C4 or C12")
    return args


def filter_records(records: list[dict], args: argparse.Namespace) -> list[dict]:
    chain = args.chain.upper() if args.chain else None
    requested_window = args.time_window if args.time_window else None
    selected = []
    for record in records:
        if chain and chain not in record["chains"]:
            continue
        if args.status and record["status"] != args.status:
            continue
        if args.confidence and record["confidence"] != args.confidence:
            continue
        if requested_window and not time_window_matches(requested_window, record["time_window"]):
            continue
        selected.append(record)
    return selected


def print_table(records: list[dict], args: argparse.Namespace) -> None:
    filters = []
    for key in ("chain", "status", "confidence", "time_window"):
        value = getattr(args, key)
        if value:
            filters.append(f"{key}={value}")
    print(f"Query: {', '.join(filters)}")
    if not records:
        print("No judgments matched the query.")
        return
    print("ID | Chains | Status | Confidence | Time window | 中文 | English")
    print("---|---|---|---|---|---|---")
    for record in records:
        print(" | ".join([
            f"[{record['id']}]({record['zh']['link']}) / [{record['id']}]({record['en']['link']})",
            ", ".join(record["chains"]) or "—",
            record["status"],
            record["confidence"],
            record["time_window"],
            record["zh"]["judgment"],
            record["en"]["judgment"],
        ]))
    print(f"Result count: {len(records)}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        records = build_records()
        selected = filter_records(records, args)
    except RegisterError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        print_table(selected, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
