#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare a deterministic, de-labelled bilingual review bundle (BUNDLE_PREPARED).

Scope of this program: it turns a FROZEN machine-readable manifest into one
public `bundle.json` whose records carry fresh `R-NN` identifiers and nothing
that lets a reader trace a record back to its original card. Preparing the
bundle is NOT a re-review: this program never claims that any review started,
ran, or finished, and it produces no finding about the method's validity or
about prediction accuracy.

What it reads: the manifest, and exactly the source files the manifest pins by
SHA-256. It never reads an existing bundle, an `R-NN -> J-NNN` mapping, an
index, a README, the protocol, or its own previous output.

Usage
  blind_bundle.py --manifest M --output-dir D --seed S [--evidence E]
                  [--verify-determinism] [--mapping-out ABS_PATH_OUTSIDE_REPO]
  blind_bundle.py --self-test

Exit: 0 = success, 1 = refused (reason on stderr). Every refusal that concerns
a record names that record's `R-NN`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

SCHEMA_VERSION = 1
BUNDLE_SCHEMA_VERSION = 1
BUNDLE_FILENAME = "bundle.json"
REQUIRED_MANIFEST_KEYS = {
    "schema_version", "source_commit", "inclusion_rule", "exclusions", "coverage", "cards",
}
CARD_KEYS = {"id", "zh_path", "en_path", "zh_sha256", "en_sha256", "include_reason"}
CARD_ID_RE = re.compile(r"^J-\d{3}$")
HEADING_RE = re.compile(r"^###\s+(J-\d{3})([^\n]*)$", re.M)
FIELD_RE = re.compile(r"^-\s+\*\*([^*]+)\*\*\s*[:：]\s*(.*)$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
URL_RE = re.compile(r"(?:https?://|www\.)[^\s)>]+", re.I)
PATH_RE = re.compile(r"(?:\.\.?/|(?:docs|chains|ledger|scripts|evidence)/)[^\s)>]*", re.I)
ID_RE = re.compile(r"J\s*[-_/]?\s*\d{3}", re.I)
STATUS_RE = re.compile(r"\b(?:ACTIVE|REVISED|ARCHIVED|SUPERSEDED|FALSIFIED|HIT|INDETERMINATE)\b")
CODE_RE = re.compile(r"```|~~~|<!--|^---\s*$", re.M)

# Cyrillic/Greek/fullwidth look-alikes and the dash family: a plain ASCII scan
# would miss `Ј－００１`, which reads as the old identifier to a human.
CONFUSABLES = str.maketrans({
    "Ј": "J", "ј": "j", "Ј": "J", "Ｊ": "J", "ϳ": "j",
    "О": "O", "о": "o", "Ο": "O", "ο": "o", "Ｏ": "O",
    "І": "I", "і": "i", "Ι": "I", "ι": "i",
    "А": "A", "а": "a", "Α": "A", "Ε": "E", "Е": "E", "е": "e",
    "С": "C", "с": "c", "Х": "X", "х": "x", "М": "M", "м": "m",
    "Р": "P", "р": "p", "Т": "T", "т": "t", "В": "B", "Ν": "N",
    "－": "-", "–": "-", "—": "-", "−": "-", "‐": "-", "‑": "-", "‒": "-", "―": "-",
    "０": "0", "１": "1", "２": "2", "３": "3", "４": "4",
    "５": "5", "６": "6", "７": "7", "８": "8", "９": "9",
})

# Only the fields a reader needs to judge the original claim on its own merits.
ALLOWED_FIELDS = {
    "提出日期": "proposed_date", "proposed date": "proposed_date",
    "一句话判断": "judgment", "one-sentence judgment": "judgment",
    "受众规模": "audience", "audience scale": "audience",
    "所以现在可以做什么": "actionable", "what can be done now": "actionable",
    "透镜": "lens", "lens": "lens",
    "推理链": "reasoning_chain", "reasoning chain": "reasoning_chain",
    "时间窗": "time_window", "time window": "time_window",
    "证伪条件": "falsifier", "falsifier": "falsifier",
    "领先指标": "leading_indicator", "leading indicator": "leading_indicator",
    "最强反方": "opposing_mechanism", "strongest opposing mechanism": "opposing_mechanism",
}
RETAINED_KEYS = sorted(set(ALLOWED_FIELDS.values()))
REQUIRED_KEYS = ("judgment", "audience", "reasoning_chain", "time_window",
                 "falsifier", "leading_indicator")

# Review metadata that must never reach the bundle, in both languages.
METADATA_TOKENS = (
    "外部对照来源", "external comparison source", "与共识", "against consensus",
    "下次检查日", "next review", "出处", "历史迁移", "修订理由", "revised reason",
    "置信度", "confidence", "状态", "status",
)
GATE_TOKENS = ("普及闸", "adoption gate", "diffusion-gate", "diffusion gate", "闸复核")
DEPENDENCY_TOKENS = ("depends-on", "depends on", "depends_on", "依赖于", "上游判断")

CHECK_NAMES = ("identifier", "status", "gate", "metadata", "dependency", "path",
               "link", "title", "code")


class Refused(ValueError):
    """A refusal: the generator will not emit a bundle in this state."""


def fail(message: str) -> None:
    raise Refused(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> bytes:
    """One byte-exact spelling: UTF-8, LF, sorted keys, no spaces, no locale."""
    text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return (text + "\n").encode("utf-8")


def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFKC", text).replace("\r\n", "\n").replace("\r", "\n")


def fold(text: str) -> str:
    return normalize_text(text).translate(CONFUSABLES)


def read_manifest(path: Path) -> Tuple[Dict[str, Any], bytes]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail("manifest is not valid UTF-8 JSON: %s" % exc)
    if not isinstance(value, dict):
        fail("manifest root must be a JSON object")
    return value, raw


def validate_manifest(manifest: Dict[str, Any]) -> None:
    missing = REQUIRED_MANIFEST_KEYS - set(manifest)
    unknown = set(manifest) - REQUIRED_MANIFEST_KEYS
    if missing:
        fail("manifest missing keys: " + ", ".join(sorted(missing)))
    if unknown:
        fail("manifest has unsupported keys: " + ", ".join(sorted(unknown)))
    if manifest["schema_version"] != SCHEMA_VERSION:
        fail("unsupported manifest schema_version: %r" % (manifest["schema_version"],))
    if not isinstance(manifest["source_commit"], str) or not re.fullmatch(
            r"[0-9a-fA-F]{7,64}", manifest["source_commit"]):
        fail("source_commit must be a hexadecimal commit SHA")
    if not isinstance(manifest["inclusion_rule"], str) or not manifest["inclusion_rule"].strip():
        fail("inclusion_rule must be a non-empty statement")
    exclusions = manifest["exclusions"]
    if not isinstance(exclusions, list):
        fail("exclusions must be a list")
    excluded_total = 0
    for item in exclusions:
        if not isinstance(item, dict) or set(item) != {"subject", "reason", "count"}:
            fail("each exclusion must be {subject, reason, count}")
        if not isinstance(item["subject"], str) or not item["subject"].strip():
            fail("exclusion subject must be non-empty")
        if not isinstance(item["reason"], str) or not item["reason"].strip():
            fail("exclusion reason must be non-empty")
        if not isinstance(item["count"], int) or isinstance(item["count"], bool) or item["count"] < 1:
            fail("exclusion count must be a positive integer")
        excluded_total += item["count"]
    coverage = manifest["coverage"]
    if not isinstance(coverage, dict) or set(coverage) != {"candidate_total", "included", "excluded"}:
        fail("coverage must be {candidate_total, included, excluded}")
    for key in ("candidate_total", "included", "excluded"):
        if not isinstance(coverage[key], int) or isinstance(coverage[key], bool) or coverage[key] < 0:
            fail("coverage.%s must be a non-negative integer" % key)
    cards = manifest["cards"]
    if not isinstance(cards, list) or not cards:
        fail("cards must be a non-empty list")
    if coverage["included"] != len(cards):
        fail("coverage.included (%d) does not match the card count (%d)"
             % (coverage["included"], len(cards)))
    if coverage["excluded"] != excluded_total:
        fail("coverage.excluded (%d) does not match the exclusion counts (%d)"
             % (coverage["excluded"], excluded_total))
    if coverage["candidate_total"] != coverage["included"] + coverage["excluded"]:
        fail("coverage.candidate_total must equal included + excluded")
    seen: Set[str] = set()
    for card in cards:
        if not isinstance(card, dict) or set(card) != CARD_KEYS:
            fail("each card must have exactly the keys %s" % sorted(CARD_KEYS))
        cid = card["id"]
        if not isinstance(cid, str) or not CARD_ID_RE.fullmatch(cid):
            fail("invalid card id: %r" % (cid,))
        if cid in seen:
            fail("duplicate card id: %s" % cid)
        seen.add(cid)
        if not isinstance(card["include_reason"], str) or not card["include_reason"].strip():
            fail("%s: include_reason must be non-empty" % cid)
        for key in ("zh_sha256", "en_sha256"):
            if not isinstance(card[key], str) or not re.fullmatch(r"[0-9a-f]{64}", card[key]):
                fail("%s: %s must be a lowercase SHA-256" % (cid, key))


def resolve_source(repo: Path, output_dir: Path, item: str, cid: str) -> Path:
    if not isinstance(item, str) or not item or os.path.isabs(item):
        fail("%s: source path must be a non-empty relative path" % cid)
    path = (repo / item).resolve()
    try:
        path.relative_to(repo.resolve())
    except ValueError:
        fail("%s: source path escapes the repository: %s" % (cid, item))
    name = path.name.lower()
    if name == BUNDLE_FILENAME or "mapping" in name or "bundle" in name:
        fail("%s: refusing to read a bundle/mapping file as a source: %s" % (cid, item))
    try:
        path.relative_to(output_dir.resolve())
    except ValueError:
        pass
    else:
        fail("%s: refusing to read its own output directory as a source: %s" % (cid, item))
    return path


def card_section(text: str, card_id: str) -> str:
    matches = [m for m in HEADING_RE.finditer(text) if m.group(1) == card_id]
    if len(matches) != 1:
        fail("%s: expected exactly one card heading, found %d" % (card_id, len(matches)))
    start, after = matches[0].start(), matches[0].end()
    nxt = re.search(r"^###\s+J-\d{3}|^##\s+", text[after:], re.M)
    return text[start:after + nxt.start()] if nxt else text[start:]


def clean_value(value: str) -> str:
    value = normalize_text(value)
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    value = LINK_RE.sub(r"\1", value)
    value = URL_RE.sub("", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def de_label_value(value: str) -> str:
    """Remove old-card metadata that can survive inside an allowed field.

    Whitelisting fields is necessary but not sufficient: migrated cards sometimes
    mention an old ID, a gate review, or a status inside the prose of an otherwise
    retained field. Those references are not part of the claim a fresh reviewer
    needs, so redact them before the independent leakage scan.
    """
    text = fold(value)
    text = re.sub(r"J\s*[-_/]?\s*\d{3}", "the preceding judgment", text, flags=re.I)
    for token in GATE_TOKENS + METADATA_TOKENS + DEPENDENCY_TOKENS:
        text = re.sub(re.escape(fold(token)), "", text, flags=re.I)
    text = STATUS_RE.sub("", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*([,，;；:：、])\s*", r"\1", text)
    return text.strip(" ,，;；:：、")


def extract_fields(section: str, card_id: str, redact_values: bool = True) -> Dict[str, str]:
    """Keep only explicitly allowed bullet fields.

    Parsing bullet by bullet (rather than deleting forbidden substrings) is what
    makes the stripping a whitelist: an unrecognised field, a continuation line
    of a forbidden field, or a newly added metadata bullet is dropped because it
    was never allowed in, not because a pattern happened to match it.
    """
    lines = normalize_text(section).splitlines()
    fields: Dict[str, str] = {}
    current: Optional[str] = None
    buffer: List[str] = []

    def flush() -> None:
        if current and buffer:
            cleaned = clean_value(" ".join(buffer))
            fields[current] = de_label_value(cleaned) if redact_values else cleaned

    for line in lines[1:]:
        stripped = line.strip()
        match = FIELD_RE.match(stripped)
        if match:
            flush()
            label = match.group(1).strip()
            key = ALLOWED_FIELDS.get(label) or ALLOWED_FIELDS.get(label.lower())
            current, buffer = key, ([match.group(2)] if key else [])
        elif current and stripped and not stripped.startswith("#") and not stripped.startswith("-"):
            buffer.append(stripped)
        elif stripped.startswith("#") or (stripped.startswith("-") and not match):
            flush()
            current, buffer = None, []
    flush()
    missing = sorted(k for k in REQUIRED_KEYS if not fields.get(k))
    if missing:
        fail("%s: missing required fields after de-labelling: %s" % (card_id, ", ".join(missing)))
    return {k: v for k, v in sorted(fields.items()) if v}


def redact_traceback_clues(record: Dict[str, Any], titles: Iterable[str],
                           paths: Iterable[str]) -> None:
    """Remove exact source titles and paths that occur inside retained prose."""
    title_clues = [fold(title) for title in titles if title and len(title) >= 4]
    path_clues = [fold(path) for path in paths if path]
    for language in ("zh", "en"):
        for key, value in record[language].items():
            text = fold(value)
            for clue in title_clues + path_clues:
                text = text.replace(clue, "")
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"\s*([,，;；:：、])\s*", r"\1", text)
            record[language][key] = text.strip(" ,，;；:：、")


def record_problems(record: Dict[str, Any], titles: Iterable[str],
                    paths: Iterable[str], disabled: Set[str]) -> List[str]:
    """Every traceback clue this record would hand a reader, by check name."""
    text = canonical_json({k: v for k, v in record.items() if k != "id"}).decode("utf-8")
    folded = fold(text)
    # Collapse whitespace AND the JSON escapes a line break becomes, so that an
    # identifier split across lines cannot slip past the identifier scan.
    compact = re.sub(r"(?:\\n|\\r|\\t|\s)+", "", folded)
    lower = folded.lower()
    problems: List[str] = []

    def hit(check: str, detail: str) -> None:
        if check not in disabled:
            problems.append("%s (%s)" % (detail, check))

    if ID_RE.search(folded) or ID_RE.search(compact):
        hit("identifier", "legacy card identifier")
    if STATUS_RE.search(folded):
        hit("status", "card status word")
    for token in GATE_TOKENS:
        if token.lower() in lower:
            hit("gate", "diffusion-gate review text: %s" % token)
            break
    for token in METADATA_TOKENS:
        if token.lower() in lower:
            hit("metadata", "review metadata: %s" % token)
            break
    for token in DEPENDENCY_TOKENS:
        if token.lower() in lower:
            hit("dependency", "dependency reference: %s" % token)
            break
    if PATH_RE.search(folded):
        hit("path", "source path reference")
    if LINK_RE.search(text) or URL_RE.search(text):
        hit("link", "link or URL")
    if CODE_RE.search(text):
        hit("code", "code block, comment, or front matter")
    for title in titles:
        if title and len(title) >= 4 and title in fold(text):
            hit("title", "original card title")
            break
    for path in paths:
        if path and path in folded:
            hit("path", "original file path")
            break
    return problems


def scan_records(records: List[Dict[str, Any]], titles: Iterable[str],
                 paths: Iterable[str], disabled: Set[str]) -> None:
    titles, paths = list(titles), list(paths)
    for record in records:
        problems = record_problems(record, titles, paths, disabled)
        if problems:
            fail("%s leaks a traceback clue: %s" % (record["id"], "; ".join(sorted(set(problems)))))


def shuffle_key(seed: str, record: Dict[str, Any]) -> Tuple[str, str]:
    """Order by a seed-keyed digest of the record's own content.

    Deliberately NOT a permutation of the manifest's order: with a content-keyed
    sort, the position of a record in the bundle carries no information about
    where it sat in the manifest, so neither the manifest order nor the language
    arrangement can be walked back into the old numbering. The canonical form is
    the deterministic tie-break.
    """
    body = record_body(record)
    return (hashlib.sha256(seed.encode("utf-8") + b"\x00" + body).hexdigest(),
            body.decode("utf-8"))


def record_body(record: Dict[str, Any]) -> bytes:
    """The public half of an internal record: the two language field maps.

    The card id lives beside this, never inside it, so it can reach the sealed
    mapping without ever reaching the shuffle key or the bundle.
    """
    return canonical_json({"zh": record["zh"], "en": record["en"]})


def runtime_environment() -> Dict[str, str]:
    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "system": platform.system(),
        "encoding": "UTF-8",
        "newline": "LF",
        "unicode_normalization": "NFKC",
        "locale_independent": "sorted keys, byte ordering, no locale collation",
        "prng": "SHA-256 keyed content digest; no random module, no PYTHONHASHSEED dependence",
    }


def prepare(repo: Path, manifest_path: Path, output_dir: Path, seed: str,
            evidence_path: Optional[Path] = None, verify_determinism: bool = False,
            mapping_out: Optional[Path] = None,
            disabled_checks: Optional[Set[str]] = None,
            redact_values: bool = True) -> Dict[str, Any]:
    if not isinstance(seed, str) or not seed.strip():
        fail("seed must be a non-empty string")
    disabled = set(disabled_checks or ())
    unknown = disabled - set(CHECK_NAMES)
    if unknown:
        fail("unknown check name(s): " + ", ".join(sorted(unknown)))
    manifest, manifest_raw = read_manifest(manifest_path)
    validate_manifest(manifest)

    records: List[Dict[str, Any]] = []
    titles: List[str] = []
    paths: List[str] = []
    zh_count = en_count = 0
    for card in manifest["cards"]:
        cid = card["id"]
        zh_path = resolve_source(repo, output_dir, card["zh_path"], cid)
        en_path = resolve_source(repo, output_dir, card["en_path"], cid)
        zh_raw, en_raw = zh_path.read_bytes(), en_path.read_bytes()
        if sha256_bytes(zh_raw) != card["zh_sha256"]:
            fail("%s: zh source hash does not match the frozen manifest" % cid)
        if sha256_bytes(en_raw) != card["en_sha256"]:
            fail("%s: en source hash does not match the frozen manifest" % cid)
        try:
            zh_text, en_text = zh_raw.decode("utf-8"), en_raw.decode("utf-8")
        except UnicodeDecodeError:
            fail("%s: source files must be UTF-8" % cid)
        zh_section = card_section(zh_text, cid)
        en_section = card_section(en_text, cid)
        for section in (zh_section, en_section):
            heading = HEADING_RE.search(section)
            if heading:
                tail = heading.group(2)
                for part in re.split(r"[·:：]", tail):
                    part = clean_value(part)
                    if part:
                        titles.append(fold(part))
        paths.extend([card["zh_path"], card["en_path"]])
        zh_fields = extract_fields(zh_section, cid, redact_values=redact_values)
        en_fields = extract_fields(en_section, cid, redact_values=redact_values)
        zh_count += 1
        en_count += 1
        records.append({"cid": cid, "zh": zh_fields, "en": en_fields})

    if zh_count != en_count or zh_count != len(manifest["cards"]):
        fail("bilingual pairing is incomplete: zh=%d en=%d cards=%d"
             % (zh_count, en_count, len(manifest["cards"])))

    if redact_values:
        for record in records:
            redact_traceback_clues(record, titles, paths)
    ordered = sorted(records, key=lambda r: shuffle_key(seed, r))
    public = [{"id": "R-%02d" % i, "zh": r["zh"], "en": r["en"]}
              for i, r in enumerate(ordered, 1)]
    if len({r["id"] for r in public}) != len(public):
        fail("renumbering produced duplicate R-NN identifiers")
    scan_records(public, titles, paths, disabled)

    bundle_bytes = canonical_json({"schema_version": BUNDLE_SCHEMA_VERSION, "records": public})
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / BUNDLE_FILENAME).write_bytes(bundle_bytes)
    for stray in output_dir.iterdir():
        if stray.name != BUNDLE_FILENAME:
            fail("the public bundle directory must contain only %s; found %s"
                 % (BUNDLE_FILENAME, stray.name))

    result: Dict[str, Any] = {
        "status": "BUNDLE_PREPARED",
        "claim_boundary": ("A bundle was prepared. No re-review has started, run, or finished; "
                           "this says nothing about method validity or prediction accuracy."),
        "input_manifest_sha256": sha256_bytes(manifest_raw),
        "bundle_sha256": sha256_bytes(bundle_bytes),
        "source_commit": manifest["source_commit"],
        "seed_sha256": sha256_bytes(seed.encode("utf-8")),
        "record_count": len(public),
        "zh_records": zh_count,
        "en_records": en_count,
        "coverage": manifest["coverage"],
        "renumbering": "R-NN assigned after a seed-keyed content shuffle",
        "mapping_in_bundle": False,
        "mapping_readable_by_generator": False,
        "runtime": runtime_environment(),
        "output_file": BUNDLE_FILENAME,
    }
    if verify_determinism:
        result["determinism"] = verify_reproducibility(repo, manifest_path, seed, bundle_bytes)
    else:
        # Without --verify-determinism nothing was recomputed, so `same_bytes`
        # must stay unanswered rather than default to true: an evidence pack is
        # read as proof, and a single run proves byte-identity of nothing.
        result["determinism"] = {"independent_runs": 1, "same_bytes": None,
                                 "archive_same_bytes": None, "order_independent": None}
    if mapping_out is not None:
        write_mapping(repo, mapping_out, ordered, manifest, seed, result)
        result["mapping_path_outside_repo"] = True
    if evidence_path is not None:
        evidence_path.parent.mkdir(parents=True, exist_ok=True)
        evidence_path.write_bytes(canonical_json(result))
    return result


def write_mapping(repo: Path, mapping_out: Path, ordered: List[Dict[str, Any]],
                  manifest: Dict[str, Any], seed: str, result: Dict[str, Any]) -> None:
    """Write the sealed `R-NN -> J-NNN` mapping, and only outside the repository.

    The mapping is the one artifact whose disclosure would undo the whole
    exercise, so the refusal is structural rather than advisory: a destination
    inside the repository is refused even if it is gitignored, because an ignore
    rule is one edit away from publishing it.
    """
    if not mapping_out.is_absolute():
        fail("--mapping-out must be an absolute path outside the repository")
    try:
        mapping_out.resolve().relative_to(repo.resolve())
    except ValueError:
        pass
    else:
        fail("refusing to write the mapping inside the repository: %s" % mapping_out)
    pairs = [{"r_id": "R-%02d" % i, "card_id": record["cid"],
              "record_sha256": sha256_bytes(record_body(record))}
             for i, record in enumerate(ordered, 1)]
    mapping_out.parent.mkdir(parents=True, exist_ok=True)
    mapping_out.write_bytes(canonical_json({
        "sealed": True,
        "note": "Hold outside the repository until the re-review results are submitted.",
        "seed": seed,
        "source_commit": manifest["source_commit"],
        "bundle_sha256": result["bundle_sha256"],
        "records": pairs,
    }))


def verify_reproducibility(repo: Path, manifest_path: Path, seed: str,
                           expected: bytes) -> Dict[str, Any]:
    """Two independent temp dirs, a plain checkout, and `git archive HEAD`.

    The archive leg matters because it is a different checkout shape: it catches
    an accidental dependence on the working tree, on `.git`, or on filesystem
    enumeration order that two runs in the same tree would never reveal.
    """
    manifest, _ = read_manifest(manifest_path)
    with tempfile.TemporaryDirectory(prefix="blind-bundle-verify-") as td:
        root = Path(td)
        mcopy = root / "manifest.json"
        mcopy.write_bytes(manifest_path.read_bytes())
        hashes = []
        for name in ("run-one", "run-two"):
            out = prepare(repo, mcopy, root / name, seed)
            hashes.append(out["bundle_sha256"])
        one = (root / "run-one" / BUNDLE_FILENAME).read_bytes()
        two = (root / "run-two" / BUNDLE_FILENAME).read_bytes()
        if one != two or one != expected:
            fail("two independent runs produced different bundle bytes")

        reordered = dict(manifest)
        reordered["cards"] = list(reversed(manifest["cards"]))
        rpath = root / "manifest-reordered.json"
        rpath.write_bytes(canonical_json(reordered))
        prepare(repo, rpath, root / "run-reordered", seed)
        order_independent = (root / "run-reordered" / BUNDLE_FILENAME).read_bytes() == expected

        other = prepare(repo, mcopy, root / "run-other-seed", seed + "-different")
        seed_changes_order = other["bundle_sha256"] != sha256_bytes(expected) or len(manifest["cards"]) == 1

        archive_same: Optional[bool] = None
        git = shutil.which("git")
        if git:
            proc = subprocess.run([git, "-C", str(repo), "archive", "--format=tar", "HEAD"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode == 0:
                tar_path = root / "head.tar"
                tar_path.write_bytes(proc.stdout)
                extracted = root / "head"
                extracted.mkdir()
                subprocess.run(["tar", "-xf", str(tar_path), "-C", str(extracted)], check=True)
                prepare(extracted, mcopy, root / "run-archive", seed)
                archive_same = (root / "run-archive" / BUNDLE_FILENAME).read_bytes() == expected
        return {
            "independent_runs": 2,
            "same_bytes": True,
            "run_hashes": hashes,
            "order_independent": order_independent,
            "seed_changes_assignment": bool(seed_changes_order),
            "archive_same_bytes": archive_same,
            "input_sha256": sha256_bytes(manifest_path.read_bytes()),
            "output_sha256": sha256_bytes(expected),
            "runtime": runtime_environment(),
        }


ZH_FIXTURE = (
    "# fixture\n\n"
    "### J-001 · 固定装置的原始标题不得出现在材料中\n"
    "- **提出日期**：2026-01-01\n"
    "- **一句话判断**：测试材料中的判断必须保持可读而不暴露来源。\n"
    "- **受众规模**：百万量级以内的既有专业者。\n"
    "- **普及闸复核**：闸一不过，应被删除。\n"
    "- **所以现在可以做什么**：先测量一个可重复动作。\n"
    "- **透镜**：供需关系。\n"
    "- **推理链**：需求持续存在 → 承载物形成 → 动作被重复执行。\n"
    "- **时间窗**：2027–2030。\n"
    "- **证伪条件**：到 2030 年该动作没有出现可重复执行者。\n"
    "- **领先指标**：年度部署量与接管次数。\n"
    "- **置信度**：中\n"
    "- **depends-on**：J-002\n"
    "- **最强反方**：承载物可能被平台统一提供。\n"
    "- **出处**：[内部链](../chains/private.md)。\n"
    "- **下次检查日**：2027-06-30。\n"
    "- **状态**：REVISED\n"
)
EN_FIXTURE = (
    "# fixture\n\n"
    "### J-001 · The fixture original title must not appear in the packet\n"
    "- **Proposed date**: 2026-01-01\n"
    "- **One-sentence judgment**: A test judgment must stay readable without exposing its source.\n"
    "- **Audience scale**: No more than a million-scale group of existing professionals.\n"
    "- **Diffusion-gate review**: Gate 1 fails; this must be removed.\n"
    "- **What can be done now**: Measure one repeatable action first.\n"
    "- **Lens**: Supply and demand.\n"
    "- **Reasoning chain**: Demand persists -> a carrier forms -> the action repeats.\n"
    "- **Time window**: 2027-2030.\n"
    "- **Falsifier**: By 2030 no repeated actor performs the action.\n"
    "- **Leading indicator**: Annual deployments and takeover counts.\n"
    "- **Confidence**: Medium\n"
    "- **depends-on**: J-002\n"
    "- **Strongest opposing mechanism**: A platform may supply the carrier.\n"
    "- **Source**: [internal](../chains/private.md).\n"
    "- **Next review**: 2027-06-30.\n"
    "- **Status**: REVISED\n"
)
ZH_FIXTURE_2 = ZH_FIXTURE.replace("J-001", "J-003").replace(
    "测试材料中的判断必须保持可读而不暴露来源。", "第二条测试判断用于证明乱序与配对成立。").replace(
    "固定装置的原始标题不得出现在材料中", "第二张固定装置卡的原始标题")
EN_FIXTURE_2 = EN_FIXTURE.replace("J-001", "J-003").replace(
    "A test judgment must stay readable without exposing its source.",
    "A second test judgment exists so shuffling and pairing can be observed.").replace(
    "The fixture original title must not appear in the packet",
    "The second fixture card original title")

# One injected defect per case. The payload replaces a sentence inside a
# RETAINED field, so the whitelist cannot drop it for free: each case must be
# caught by the named check.
INJECTIONS: Tuple[Tuple[str, str, str], ...] = (
    ("legacy_id", "identifier", "先测量一个可重复动作，参见 J-004 的定义。"),
    ("status_word", "status", "先测量一个可重复动作，该卡仍为 ACTIVE。"),
    ("revised_reason", "metadata", "先测量一个可重复动作；修订理由见原记录。"),
    ("adoption_gate", "gate", "先测量一个可重复动作，普及闸一已判不过。"),
    ("source_path", "path", "先测量一个可重复动作，详见 docs/zh/ledger/01.md。"),
    ("original_title", "title", "先测量一个可重复动作：固定装置的原始标题不得出现在材料中。"),
    ("dependency", "dependency", "先测量一个可重复动作，depends-on 上游判断。"),
    ("confusable_id", "identifier", "先测量一个可重复动作，参见 Ј－００４。"),
    ("split_id", "identifier", "先测量一个可重复动作，参见 J-\n    004 的定义。"),
)
ANCHOR = "先测量一个可重复动作。"


def _fixture_repo(root: Path) -> Tuple[Path, Path, Path, Path, Path, Path, Path, Path, Path]:
    repo = root / "repo"
    (repo / "docs/zh/ledger").mkdir(parents=True)
    (repo / "docs/en/ledger").mkdir(parents=True)
    zh1, en1 = repo / "docs/zh/ledger/01.md", repo / "docs/en/ledger/01.md"
    zh2, en2 = repo / "docs/zh/ledger/02.md", repo / "docs/en/ledger/02.md"
    zh3, en3 = repo / "docs/zh/ledger/03.md", repo / "docs/en/ledger/03.md"
    zh4, en4 = repo / "docs/zh/ledger/04.md", repo / "docs/en/ledger/04.md"
    zh1.write_bytes(ZH_FIXTURE.encode("utf-8"))
    en1.write_bytes(EN_FIXTURE.encode("utf-8"))
    zh2.write_bytes(ZH_FIXTURE_2.encode("utf-8"))
    en2.write_bytes(EN_FIXTURE_2.encode("utf-8"))
    zh3.write_bytes(ZH_FIXTURE_2.replace("J-003", "J-005").replace(
        "第二条测试判断用于证明乱序与配对成立。", "第三条测试判断用于证明不同 seed 可以改变顺序。")
        .replace("第二张固定装置卡的原始标题", "第三张固定装置卡的原始标题").encode("utf-8"))
    en3.write_bytes(EN_FIXTURE_2.replace("J-003", "J-005").replace(
        "A second test judgment exists so shuffling and pairing can be observed.",
        "A third test judgment exists so a different seed can change ordering.")
        .replace("The second fixture card original title", "The third fixture card original title").encode("utf-8"))
    zh4.write_bytes(ZH_FIXTURE_2.replace("J-003", "J-007").replace(
        "第二条测试判断用于证明乱序与配对成立。", "第四条测试判断用于证明内容键排序。")
        .replace("第二张固定装置卡的原始标题", "第四张固定装置卡的原始标题").encode("utf-8"))
    en4.write_bytes(EN_FIXTURE_2.replace("J-003", "J-007").replace(
        "A second test judgment exists so shuffling and pairing can be observed.",
        "A fourth test judgment exists so content-key sorting can be checked.")
        .replace("The second fixture card original title", "The fourth fixture card original title").encode("utf-8"))
    # Make the fixture a real checkout so the archive leg tests the same path as production.
    subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "fixture@example.invalid"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "Fixture"], check=True)
    subprocess.run(["git", "-C", str(repo), "add", "docs"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-qm", "fixture"], check=True)
    return repo, zh1, en1, zh2, en2, zh3, en3, zh4, en4


def _fixture_manifest(repo: Path, files: Dict[str, Path]) -> Dict[str, Any]:
    cards = []
    for cid, (zh, en) in files.items():
        cards.append({
            "id": cid,
            "zh_path": zh.relative_to(repo).as_posix(),
            "en_path": en.relative_to(repo).as_posix(),
            "zh_sha256": sha256_bytes(zh.read_bytes()),
            "en_sha256": sha256_bytes(en.read_bytes()),
            "include_reason": "fixture card with all required retained fields",
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "source_commit": "a" * 40,
        "inclusion_rule": "fixture: every card in the fixture tree",
        "exclusions": [{"subject": "fixture excluded card", "reason": "missing audience field", "count": 1}],
        "coverage": {"candidate_total": len(cards) + 1, "included": len(cards), "excluded": 1},
        "cards": cards,
    }


def run_self_test() -> Dict[str, Any]:
    """Negative cases, a mutation check per detection branch, and determinism."""
    with tempfile.TemporaryDirectory(prefix="blind-bundle-self-test-") as td:
        root = Path(td)
        repo, zh1, en1, zh2, en2, zh3, en3, zh4, en4 = _fixture_repo(root)
        files = {
            "J-001": (zh1, en1), "J-003": (zh2, en2),
            "J-005": (zh3, en3), "J-007": (zh4, en4),
        }
        manifest_path = repo / "manifest.json"

        def freeze() -> None:
            manifest_path.write_bytes(canonical_json(_fixture_manifest(repo, files)))

        freeze()
        baseline = prepare(repo, manifest_path, root / "out", "fixture-seed",
                           verify_determinism=True)
        det = baseline["determinism"]
        if not (det["same_bytes"] and det["order_independent"]):
            fail("determinism did not hold on the fixture")
        if baseline["record_count"] != 4 or baseline["record_count"] != baseline["zh_records"] \
                or baseline["zh_records"] != baseline["en_records"]:
            fail("fixture record counts are wrong")
        if not baseline["determinism"]["seed_changes_assignment"]:
            fail("fixture did not demonstrate a seed-dependent ordering")

        mapping_inside = repo / "mapping.json"
        try:
            prepare(repo, manifest_path, root / "out-map", "fixture-seed",
                    mapping_out=mapping_inside)
        except Refused:
            mapping_refused_inside = True
        else:
            mapping_refused_inside = False
        mapping_outside = root / "sealed" / "mapping.json"
        mapping_run = prepare(repo, manifest_path, root / "out-map2", "fixture-seed",
                              mapping_out=mapping_outside)
        mapping_is_test_only = mapping_outside.exists() and not str(mapping_outside).startswith(str(repo))
        mapping_value = json.loads(mapping_outside.read_text(encoding="utf-8"))
        bundle_value = json.loads((root / "out-map2" / BUNDLE_FILENAME).read_text(encoding="utf-8"))
        expected_card_by_hash: Dict[str, str] = {}
        fixture_titles: List[str] = []
        fixture_paths: List[str] = []
        for cid, (zh_path, en_path) in files.items():
            for path, language in ((zh_path, "zh"), (en_path, "en")):
                section = card_section(path.read_text(encoding="utf-8"), cid)
                heading = HEADING_RE.search(section)
                if heading:
                    for part in re.split(r"[·:：]", heading.group(2)):
                        part = clean_value(part)
                        if part:
                            fixture_titles.append(fold(part))
                fixture_paths.append(path.relative_to(repo).as_posix())
        for cid, (zh_path, en_path) in files.items():
            zh_text = zh_path.read_bytes().decode("utf-8")
            en_text = en_path.read_bytes().decode("utf-8")
            internal = {"cid": cid,
                        "zh": extract_fields(card_section(zh_text, cid), cid),
                        "en": extract_fields(card_section(en_text, cid), cid)}
            redact_traceback_clues(internal, fixture_titles, fixture_paths)
            expected_card_by_hash[sha256_bytes(record_body(internal))] = cid
        mapping_pairs_match = (
            mapping_run["bundle_sha256"] == sha256_bytes((root / "out-map2" / BUNDLE_FILENAME).read_bytes())
            and len(mapping_value["records"]) == len(bundle_value["records"]) == 4
            and all(
                pair["r_id"] == public["id"]
                and pair["card_id"] == expected_card_by_hash.get(pair["record_sha256"])
                and pair["record_sha256"] == sha256_bytes(
                    canonical_json({"zh": public["zh"], "en": public["en"]})
                )
                for pair, public in zip(mapping_value["records"], bundle_value["records"])
            )
        )

        original = zh1.read_bytes().decode("utf-8")
        negative: List[Dict[str, str]] = []
        for name, check, payload in INJECTIONS:
            zh1.write_bytes(original.replace(ANCHOR, payload).encode("utf-8"))
            freeze()
            try:
                prepare(repo, manifest_path, root / ("neg-" + name), "fixture-seed",
                        redact_values=False)
            except Refused as exc:
                message = str(exc)
                if not re.search(r"\bR-\d{2}\b", message):
                    fail("negative case %s did not name an R-NN record: %s" % (name, message))
                negative.append({"case": name, "check": check, "error": message})
            else:
                fail("negative case %s was not caught" % name)
            finally:
                zh1.write_bytes(original.encode("utf-8"))
                freeze()

        # Mutation: disable exactly one detection branch and confirm the case it
        # owns slips through while the rest still fail. A branch whose removal
        # changes nothing was never doing the work.
        mutation: List[Dict[str, Any]] = []
        for name, check, payload in INJECTIONS:
            zh1.write_bytes(original.replace(ANCHOR, payload).encode("utf-8"))
            freeze()
            try:
                prepare(repo, manifest_path, root / ("mut-" + name), "fixture-seed",
                        disabled_checks={check}, redact_values=False)
            except Refused as exc:
                zh1.write_bytes(original.encode("utf-8"))
                freeze()
                fail("mutation for %s stayed green via another branch: %s" % (name, exc))
            else:
                mutation.append({"case": name, "disabled_check": check, "leak_passed": True})
            finally:
                zh1.write_bytes(original.encode("utf-8"))
                freeze()

        # A hash mismatch against the frozen manifest must also refuse.
        tampered = _fixture_manifest(repo, files)
        tampered["cards"][0]["zh_sha256"] = "0" * 64
        manifest_path.write_bytes(canonical_json(tampered))
        try:
            prepare(repo, manifest_path, root / "neg-hash", "fixture-seed")
        except Refused:
            hash_guard = True
        else:
            hash_guard = False
        freeze()

        if len(negative) != len(INJECTIONS) or len(mutation) != len(INJECTIONS):
            fail("negative or mutation coverage is incomplete")
        if not (mapping_refused_inside and mapping_is_test_only and mapping_pairs_match and hash_guard):
            fail("mapping or manifest guards did not hold")
        return {
            "status": "SELF_TEST_PASSED",
            "negative_cases": len(negative),
            "mutation_cases": len(mutation),
            "all_expected_failures": True,
            "negative_detail": negative,
            "mutation_detail": mutation,
            "mapping_refused_inside_repo": mapping_refused_inside,
            "mapping_is_test_only_not_production": mapping_is_test_only,
            "mapping_pairs_match_bundle": mapping_pairs_match,
            "manifest_hash_guard": hash_guard,
            "determinism": det,
            "claim_boundary": ("These are structural isolation checks only. They say nothing "
                               "about method validity or prediction accuracy."),
        }


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Prepare a de-labelled bilingual review bundle.")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--mapping-out", type=Path,
                        help="absolute path OUTSIDE the repository for the sealed mapping")
    parser.add_argument("--seed")
    parser.add_argument("--verify-determinism", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    def anchor(path: Optional[Path]) -> Optional[Path]:
        if path is None:
            return None
        return path if path.is_absolute() else (args.repo / path)

    try:
        if args.self_test:
            print(json.dumps(run_self_test(), ensure_ascii=False, sort_keys=True, indent=2))
            return 0
        if not args.manifest or not args.output_dir or args.seed is None:
            parser.error("--manifest, --output-dir and --seed are required unless --self-test is used")
        result = prepare(
            args.repo.resolve(),
            anchor(args.manifest).resolve(),
            anchor(args.output_dir).resolve(),
            args.seed,
            anchor(args.evidence),
            args.verify_determinism,
            args.mapping_out,
        )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (OSError, Refused, subprocess.CalledProcessError) as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
