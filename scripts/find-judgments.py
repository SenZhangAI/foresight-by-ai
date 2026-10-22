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
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parent.parent
LANGS = ("zh", "en")
CARD_HEADING = re.compile(r"^###\s+(J-\d{3})\s+·\s+(.+?)\s*$")
FIELD_LINE = re.compile(r"^-\s+\*\*(.+?)\*\*\s*(?:：|:)\s*(.*)$")
CHAIN_RE = re.compile(r"\bC\d+\b")

FIELD_NAMES = {
    "zh": {
        "status": "状态",
        "confidence": "置信度",
        "time_window": "时间窗",
        "source": "出处",
        "judgment": "一句话判断",
    },
    "en": {
        "status": "Status",
        "confidence": "Confidence",
        "time_window": "Time window",
        "source": "Source",
        "judgment": "One-sentence judgment",
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


def iter_card_blocks(path: Path) -> Iterable[tuple[str, str, list[str], int]]:
    lines = path.read_text(encoding="utf-8").splitlines()
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


def parse_field(lines: list[str], label: str) -> str:
    for line in lines:
        match = FIELD_LINE.match(line)
        if match and match.group(1).strip() == label:
            return match.group(2).strip()
    return ""


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


def load_language(lang: str) -> dict[str, Card]:
    directory = REPO / "docs" / lang / "ledger"
    cards: dict[str, Card] = {}
    for path in sorted(directory.glob("*.md")):
        relative = path.relative_to(REPO).as_posix()
        for card_id, title, lines, _line in iter_card_blocks(path):
            if card_id in cards:
                raise ValueError(f"duplicate {card_id} in {lang}: {relative}")
            names = FIELD_NAMES[lang]
            source = parse_field(lines, names["source"])
            status_raw = parse_field(lines, names["status"])
            confidence_raw = parse_field(lines, names["confidence"])
            status = normalize_status(status_raw, lang)
            confidence = normalize_confidence(confidence_raw, lang)
            time_window = parse_field(lines, names["time_window"])
            judgment = parse_field(lines, names["judgment"])
            if not source or not time_window or not judgment:
                raise ValueError(f"{relative}: {card_id} is missing a query field")
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
                judgment=judgment,
            )
    return cards


def time_window_signature(value: str) -> tuple[str, ...]:
    """Compare bilingual windows by their explicit year/month endpoints."""
    tokens = tuple(re.findall(r"\b\d{4}(?:[-/]\d{1,2})?\b", unicodedata.normalize("NFKC", value)))
    return tokens or (normalize_time_window(value),)


def normalize_time_window(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower()
    value = value.replace("–", "-").replace("—", "-").replace("至", "-")
    value = "".join(char for char in value if unicodedata.category(char)[0] not in {"P", "S"} or char == "-")
    return re.sub(r"\s+", "", value)


def time_window_matches(requested: str, actual: str) -> bool:
    requested_signature = time_window_signature(requested)
    actual_signature = time_window_signature(actual)
    if any(re.search(r"\b\d{4}", token) for token in requested_signature):
        return all(token in actual_signature for token in requested_signature)
    return normalize_time_window(requested) in normalize_time_window(actual)


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
            "zh": {"title": zh.title, "judgment": zh.judgment, "status": zh.status_raw, "confidence": zh.confidence_raw, "time_window": zh.time_window, "link": card_link(zh)},
            "en": {"title": en.title, "judgment": en.judgment, "status": en.status_raw, "confidence": en.confidence_raw, "time_window": en.time_window, "link": card_link(en)},
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
