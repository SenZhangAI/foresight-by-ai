#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a byte-faithful blind-review package from one immutable Git snapshot.

This is intentionally separate from the historical cleaning generator.  A faithful
package never normalizes or edits a source field: it copies the exact UTF-8 field
bytes located by the frozen manifest.  The only permitted transformation is an
explicit, sealed card-id alias map.  A field containing any other traceback clue is
excluded, with its reason and locator recorded in the manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

SCHEMA_VERSION = 1
BUNDLE_SCHEMA_VERSION = 1
REQUIRED_FIELDS = {
    "提出日期": "proposed_date",
    "proposed date": "proposed_date",
    "一句话判断": "judgment",
    "one-sentence judgment": "judgment",
    "受众规模": "audience",
    "audience scale": "audience",
    "推理链": "reasoning_chain",
    "reasoning chain": "reasoning_chain",
    "时间窗": "time_window",
    "time window": "time_window",
    "证伪条件": "falsifier",
    "falsifier": "falsifier",
    "领先指标": "leading_indicator",
    "leading indicator": "leading_indicator",
}
FIELD_ORDER = ("judgment", "audience", "reasoning_chain", "time_window", "falsifier", "leading_indicator")
CARD_RE = re.compile(rb"^###\s+(J-\d{3})(?:\s|$).*?(?=^###\s+J-\d{3}|^##\s|\Z)", re.M | re.S)
FIELD_RE = re.compile(rb"^-\s+\*\*([^*]+)\*\*\s*(?:\x3a|\xef\xbc\x9a)", re.M)
ID_RE = re.compile(rb"(?<![A-Za-z0-9])J-\d{3}(?![A-Za-z0-9])")
URL_RE = re.compile(rb"(?:https?://|www\.)", re.I)
BARE_DOMAIN_RE = re.compile(rb"\b(?:[a-z0-9-]+\.)+[a-z]{2,}(?:/[^\s)>]*)?", re.I)
LINK_RE = re.compile(rb"!?\[[^\]]*\]\([^)]*\)")
PATH_RE = re.compile(rb"(?:^|[\s(])/(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_-]+)?(?:#[^\s)>]+)?|(?:^|[\s(])[A-Za-z0-9_-]+/(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_-]+)?(?:#[^\s)>]+)?|(?:\b(?:docs|chains|ledger|scripts|evidence)/[^\s)>]+)", re.I)
ANCHOR_RE = re.compile(rb"#[^\s)>]+")
GATE_RE = re.compile(rb"\b(?:gate|gating|diffusion-gate|review-gate)\b|\xe9\x97\xa8", re.I)
STATUS_RE = re.compile(rb"\b(?:ACTIVE|REVISED|ARCHIVED|SUPERSEDED|FALSIFIED|HIT|INDETERMINATE)\b|\xe7\x8a\xb6\xe6\x80\x81|\xe7\xbd\xae\xe4\xbf\xa1\xe5\xba\xa6|confidence|status", re.I)

class Refused(ValueError):
    pass

def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def git(repo: Path, *args: str) -> bytes:
    p = subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise Refused("git %s failed: %s" % (" ".join(args), p.stderr.decode("utf-8", "replace").strip()))
    return p.stdout

def commit_exists(repo: Path, commit: str) -> None:
    if not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise Refused("source_commit must be a full 40-character commit SHA")
    git(repo, "cat-file", "-e", commit + "^{commit}")

def snapshot(repo: Path, commit: str, path: str) -> bytes:
    if path.startswith("/") or ".." in Path(path).parts:
        raise Refused("source path is not repository-relative: %s" % path)
    return git(repo, "show", "%s:%s" % (commit, path))

def ledger_paths(repo: Path, commit: str, language: str) -> List[str]:
    prefix = "docs/%s/ledger/" % language
    names = git(repo, "ls-tree", "-r", "--name-only", commit, "--", prefix).decode().splitlines()
    return sorted(n for n in names if n.endswith(".md"))

def cards_in_file(raw: bytes) -> Dict[str, Tuple[int, int, bytes]]:
    return {m.group(1).decode(): (m.start(), m.end(), m.group(0)) for m in CARD_RE.finditer(raw)}

def extract_fields(section: bytes, card_id: str, base: int) -> Dict[str, Dict[str, Any]]:
    matches = list(FIELD_RE.finditer(section))
    fields: Dict[str, Dict[str, Any]] = {}
    for i, match in enumerate(matches):
        label = match.group(1).decode("utf-8")
        key = REQUIRED_FIELDS.get(label.lower(), REQUIRED_FIELDS.get(label))
        if key is None:
            continue
        if key in fields:
            raise Refused("%s: duplicate required field %s" % (card_id, key))
        # The complete source field starts at the bullet and ends immediately
        # before the next parsed field. Keeping this raw envelope makes label and
        # punctuation deletion observable instead of silently dropping structure.
        field_start = match.start()
        field_end = matches[i + 1].start() if i + 1 < len(matches) else len(section)
        field_raw = section[field_start:field_end]
        value_start = match.end()
        value_end = field_end
        # Stop at a non-field bullet/header while retaining the exact bytes before it.
        tail = section[value_start:value_end]
        for line_match in re.finditer(rb"(?:^|\r?\n)(?=-\s|#{1,6}\s)", tail, re.M):
            if line_match.start() > 0:
                value_end = value_start + line_match.start()
                field_raw = section[field_start:value_end]
                break
        value = section[value_start:value_end]
        fields[key] = {
            "label": label,
            "label_sha256": sha(match.group(1)),
            "label_locator": {"start_byte": base + match.start(1), "end_byte": base + match.end(1)},
            "field_locator": {"start_byte": base + field_start, "end_byte": base + value_end},
            "value_locator": {"start_byte": base + value_start, "end_byte": base + value_end},
            "source_sha256": sha(field_raw),
            "source_bytes": field_raw,
        }
    return fields

def decode(value: bytes, what: str) -> str:
    try:
        return value.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise Refused("%s is not UTF-8: %s" % (what, exc))

def replace_id_token(data: bytes, old: str, new: str) -> Tuple[bytes, int]:
    pattern = rb"(?<![A-Za-z0-9])" + re.escape(old.encode()) + rb"(?![A-Za-z0-9])"
    return re.subn(pattern, new.encode(), data)

def clue(value: bytes, own_id: str, known_ids: Iterable[str]) -> Optional[str]:
    # A field may carry its own card id; that id is replaced by the explicit alias.
    # Any other J-NNN is a traceback clue, even when that other card happened to be
    # a candidate in the same freeze. There is no implicit alias for foreign IDs.
    text, _ = replace_id_token(value, own_id, "")
    unknown_ids = sorted(set(m.group(0).decode() for m in ID_RE.finditer(text)))
    if unknown_ids:
        return "unmapped card identifier: " + ", ".join(unknown_ids)
    checks = ((URL_RE, "URL"), (LINK_RE, "Markdown link"), (PATH_RE, "source path"), (BARE_DOMAIN_RE, "bare domain"),
              (ANCHOR_RE, "heading anchor"), (GATE_RE, "gate/review metadata"),
              (STATUS_RE, "status/review metadata"))
    for pattern, label in checks:
        if pattern.search(text):
            return label
    return None

def field_projection(field: Dict[str, Any], aliases: Dict[str, str]) -> Tuple[bytes, List[Dict[str, Any]]]:
    raw = field["source_bytes"]
    out = raw
    changes: List[Dict[str, Any]] = []
    # Longest-first avoids a shorter alias consuming a prefix of a future alias.
    for old, new in sorted(aliases.items(), key=lambda item: len(item[0]), reverse=True):
        out, count = replace_id_token(out, old, new)
        if count:
            changes.append({"from": old, "to": new, "count": count})
    return out, changes

def validate_alias_only(source: bytes, emitted: bytes, aliases: Dict[str, str]) -> None:
    expected, _ = field_projection({"source_bytes": source}, aliases)
    if emitted != expected:
        raise Refused("field differs from source outside the explicit id alias map")

def collect_manifest(repo: Path, source_commit: str) -> Dict[str, Any]:
    commit_exists(repo, source_commit)
    paths = {lang: ledger_paths(repo, source_commit, lang) for lang in ("zh", "en")}
    by_lang: Dict[str, Dict[str, Tuple[str, int, int, bytes]]] = {"zh": {}, "en": {}}
    for lang in ("zh", "en"):
        for path in paths[lang]:
            raw = snapshot(repo, source_commit, path)
            for cid, (start, end, section) in cards_in_file(raw).items():
                if cid in by_lang[lang]:
                    raise Refused("%s appears in multiple %s files" % (cid, lang))
                by_lang[lang][cid] = (path, start, end, section)
    ids = sorted(set(by_lang["zh"]) | set(by_lang["en"]))
    cards: List[Dict[str, Any]] = []
    excluded: List[Dict[str, Any]] = []
    included_ids = sorted(set(by_lang["zh"]) & set(by_lang["en"]))
    # Alias assignments are explicit in the frozen input, but are not emitted in the
    # public bundle. A sealed mapping later records the reverse relation.
    aliases = {cid: "R-%03d" % (i + 1) for i, cid in enumerate(included_ids)}
    for cid in ids:
        if cid not in by_lang["zh"] or cid not in by_lang["en"]:
            excluded.append({"id": cid, "reason": "missing bilingual counterpart", "source": {"paths": [by_lang["zh"].get(cid, by_lang["en"].get(cid))[0]], "heading": cid}})
            continue
        per_lang: Dict[str, Dict[str, Any]] = {}
        reasons: List[str] = []
        field_exclusions: List[Dict[str, Any]] = []
        for lang in ("zh", "en"):
            path, start, end, section = by_lang[lang][cid]
            try:
                extracted = extract_fields(section, cid, start)
            except Refused as exc:
                reasons.append(str(exc))
                continue
            missing = [key for key in FIELD_ORDER if key not in extracted or not extracted[key]["source_bytes"]]
            invalid_utf8 = []
            for key in FIELD_ORDER:
                if key in extracted:
                    try:
                        decode(extracted[key]["source_bytes"], "%s.%s" % (cid, key))
                    except Refused:
                        invalid_utf8.append(key)
            if invalid_utf8:
                reasons.append("%s required fields are not UTF-8: %s" % (lang, ", ".join(invalid_utf8)))
                for key in invalid_utf8:
                    f = extracted[key]
                    field_exclusions.append({"language": lang, "field": key, "reason": "not UTF-8", "source_path": path, "label": f["label"], "field_locator": f["field_locator"], "source_sha256": f["source_sha256"], "difference_verdict": "excluded_before_projection"})
            if missing:
                reasons.append("%s missing required fields: %s" % (lang, ", ".join(missing)))
                for key in missing:
                    if key not in extracted:
                        field_exclusions.append({"language": lang, "field": key, "reason": "missing required field", "source_path": path, "label": None, "field_locator": None, "source_sha256": None, "difference_verdict": "excluded_before_projection"})
                continue
            per_lang[lang] = extracted
        if reasons:
            excluded.append({"id": cid, "reason": "; ".join(reasons), "source": {"paths": [by_lang["zh"][cid][0], by_lang["en"][cid][0]], "heading": cid}, "fields": field_exclusions})
            continue
        for lang in ("zh", "en"):
            for key in FIELD_ORDER:
                reason = clue(per_lang[lang][key]["source_bytes"], cid, aliases)
                if reason:
                    reasons.append("%s.%s contains %s; field excluded rather than cleaned" % (lang, key, reason))
                    f = per_lang[lang][key]
                    field_exclusions.append({"language": lang, "field": key, "reason": reason, "source_path": by_lang[lang][cid][0], "label": f["label"], "field_locator": f["field_locator"], "source_sha256": f["source_sha256"], "difference_verdict": "excluded_before_projection"})
        if reasons:
            excluded.append({"id": cid, "reason": "; ".join(reasons), "source": {"paths": [by_lang["zh"][cid][0], by_lang["en"][cid][0]], "heading": cid}, "fields": field_exclusions})
            continue
        fields = {}
        for lang in ("zh", "en"):
            fields[lang] = {}
            for key in FIELD_ORDER:
                f = per_lang[lang][key]
                fields[lang][key] = {k: v for k, v in f.items() if k != "source_bytes"}
        cards.append({"id": cid, "alias": aliases[cid], "zh_path": by_lang["zh"][cid][0], "en_path": by_lang["en"][cid][0], "card_locators": {lang: {"start_byte": by_lang[lang][cid][1], "end_byte": by_lang[lang][cid][2], "section_sha256": sha(by_lang[lang][cid][3])} for lang in ("zh", "en")}, "fields": fields})
    if not cards:
        raise Refused("strict fidelity freeze produced no included cards")
    exclusions = [{"subject": "strict source-field fidelity exclusions", "reason": "A required source field is missing, not UTF-8, or carries a traceback clue that cannot be cleaned under the byte-fidelity rule.", "count": len(excluded), "cards": excluded}] if excluded else []
    return {"schema_version": SCHEMA_VERSION, "source_commit": source_commit, "source_snapshot": "git archive of source_commit; working tree is never read", "field_policy": {"included": list(FIELD_ORDER), "omitted_fields": "All fields outside the six required fields are excluded, not cleaned.", "allowed_transform": "Only exact byte replacement of the explicit card-id aliases in cards[].alias is allowed."}, "alias_policy": "Each source J-NNN in the frozen included set has one explicit R-NNN alias; no Unicode, newline, whitespace, link, label, or metadata transformation is permitted.", "coverage": {"candidate_total": len(ids), "included": len(cards), "excluded": len(excluded)}, "exclusions": exclusions, "cards": cards}

def public_receipt(manifest: Dict[str, Any], manifest_sha256: str) -> Dict[str, Any]:
    counts: Dict[str, int] = {}
    for group in manifest.get("exclusions", []):
        for card in group.get("cards", []):
            reason = re.sub(r"J-\d{3}", "<opaque-id>", card.get("reason", ""))
            # Keep categories useful without publishing card identity or locators.
            for part in (p.strip() for p in reason.split(";")):
                if part:
                    category = part.split(" contains ", 1)[-1].split(":", 1)[0]
                    counts[category] = counts.get(category, 0) + 1
    return {"schema_version": 1, "public_receipt": True, "source_commit": manifest["source_commit"], "private_manifest_sha256": manifest_sha256, "coverage": manifest["coverage"], "field_policy": manifest["field_policy"], "alias_policy": "The private manifest has an explicit one-to-one card-id alias map; this receipt intentionally contains no source IDs, aliases, paths, locators, labels, or mapping.", "exclusion_reason_counts": counts}

def validate_manifest(manifest: Dict[str, Any]) -> None:
    required = {"schema_version", "source_commit", "source_snapshot", "field_policy", "alias_policy", "coverage", "exclusions", "cards"}
    if set(manifest) != required or manifest["schema_version"] != SCHEMA_VERSION:
        raise Refused("unsupported strict manifest schema or keys")
    commit = manifest["source_commit"]
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise Refused("manifest source_commit must be a full 40-character SHA")
    if tuple(manifest["field_policy"]["included"]) != FIELD_ORDER:
        raise Refused("manifest required field set/order is not the strict set")
    cards = manifest["cards"]
    if not cards:
        raise Refused("manifest contains no included cards")
    seen = set()
    aliases = set()
    for card in cards:
        if set(card) != {"id", "alias", "zh_path", "en_path", "card_locators", "fields"}:
            raise Refused("card entry has unsupported keys")
        if card["id"] in seen or not re.fullmatch(r"J-\d{3}", card["id"]):
            raise Refused("duplicate or invalid card id")
        if card["alias"] in aliases or not re.fullmatch(r"R-\d{3}", card["alias"]):
            raise Refused("duplicate or invalid explicit alias")
        seen.add(card["id"])
        aliases.add(card["alias"])
        for lang in ("zh", "en"):
            loc = card["card_locators"].get(lang)
            if not isinstance(loc, dict) or set(loc) != {"start_byte", "end_byte", "section_sha256"}:
                raise Refused("%s %s card locator schema mismatch" % (card["id"], lang))
            if not isinstance(loc["start_byte"], int) or not isinstance(loc["end_byte"], int) or not re.fullmatch(r"[0-9a-f]{64}", loc["section_sha256"]):
                raise Refused("%s %s card locator invalid" % (card["id"], lang))
            if set(card["fields"][lang]) != set(FIELD_ORDER):
                raise Refused("%s fields do not equal the strict required set" % card["id"])
            for key in FIELD_ORDER:
                f = card["fields"][lang][key]
                if set(f) != {"label", "label_sha256", "label_locator", "field_locator", "value_locator", "source_sha256"}:
                    raise Refused("%s.%s locator schema mismatch" % (card["id"], key))
                if not re.fullmatch(r"[0-9a-f]{64}", f["label_sha256"]):
                    raise Refused("%s.%s label hash invalid" % (card["id"], key))
                if not re.fullmatch(r"[0-9a-f]{64}", f["source_sha256"]):
                    raise Refused("%s.%s source hash invalid" % (card["id"], key))

def ensure_private_output(repo: Path, path: Path, name: str) -> Path:
    repo_root = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    target = path.resolve()
    if os.path.commonpath([str(repo_root), str(target)]) == str(repo_root):
        raise Refused("%s must be outside the repository" % name)
    return target

def prepare(repo: Path, manifest_path: Path, output_dir: Path, mapping_out: Path) -> Dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_manifest(manifest)
    commit_exists(repo, manifest["source_commit"])
    mapping_out = ensure_private_output(repo, mapping_out, "mapping-out")
    aliases = {c["id"]: c["alias"] for c in manifest["cards"]}
    records = []
    mapping = []
    field_diffs: List[Dict[str, Any]] = []
    for card in manifest["cards"]:
        projected: Dict[str, Dict[str, str]] = {}
        for lang in ("zh", "en"):
            projected[lang] = {}
            raw_file = snapshot(repo, manifest["source_commit"], card[lang + "_path"])
            cloc = card["card_locators"][lang]
            cs, ce = cloc["start_byte"], cloc["end_byte"]
            if cs < 0 or ce <= cs or ce > len(raw_file):
                raise Refused("%s %s card locator is outside its source file" % (card["id"], lang))
            section = raw_file[cs:ce]
            if sha(section) != cloc["section_sha256"]:
                raise Refused("%s %s card section does not match its frozen locator" % (card["id"], lang))
            heading = re.match(rb"^###\s+(J-\d{3})", section)
            if not heading or heading.group(1).decode() != card["id"]:
                raise Refused("%s %s card locator is not bound to its heading" % (card["id"], lang))
            actual_fields = extract_fields(section, card["id"], cs)
            if not set(FIELD_ORDER).issubset(set(actual_fields)):
                raise Refused("%s %s frozen card does not contain the strict field set" % (card["id"], lang))
            for key in FIELD_ORDER:
                f = card["fields"][lang][key]
                actual = actual_fields[key]
                actual_meta = {k: v for k, v in actual.items() if k != "source_bytes"}
                if actual_meta != f:
                    raise Refused("%s.%s manifest locator/label does not match the re-parsed source field" % (card["id"], key))
                f = actual
                la, lb = f["label_locator"]["start_byte"], f["label_locator"]["end_byte"]
                if la < 0 or lb < la or lb > len(raw_file):
                    raise Refused("%s.%s label locator is outside its source file" % (card["id"], key))
                raw_label = raw_file[la:lb]
                if sha(raw_label) != f["label_sha256"] or decode(raw_label, "%s.%s label" % (card["id"], key)) != f["label"]:
                    raise Refused("%s.%s source label does not match its frozen locator" % (card["id"], key))
                fs, fe = f["field_locator"]["start_byte"], f["field_locator"]["end_byte"]
                if fs < cs or fe < fs or fe > ce:
                    raise Refused("%s.%s field locator escapes its card section" % (card["id"], key))
                va, vb = f["value_locator"]["start_byte"], f["value_locator"]["end_byte"]
                if fs > la or lb > fe or va < fs or vb < va or vb > fe:
                    raise Refused("%s.%s label/value locator escapes its field" % (card["id"], key))
                raw = raw_file[fs:fe]
                if sha(raw) != f["source_sha256"]:
                    raise Refused("%s.%s source field bytes do not match frozen locator" % (card["id"], key))
                trace_reason = clue(raw, card["id"], ())
                if trace_reason:
                    raise Refused("%s.%s carries a traceback clue after freeze: %s" % (card["id"], key, trace_reason))
                emitted, changes = field_projection({"source_bytes": raw}, {card["id"]: card["alias"]})
                validate_alias_only(raw, emitted, {card["id"]: card["alias"]})
                # No decoding/encoding round trip may change bytes.
                text = decode(emitted, "%s.%s" % (card["alias"], key))
                if text.encode("utf-8") != emitted:
                    raise Refused("%s.%s changed during UTF-8 serialization" % (card["alias"], key))
                projected[lang][key] = text
                field_diffs.append({
                    "alias": card["alias"], "source_id": card["id"], "language": lang,
                    "field": key, "source_path": card[lang + "_path"],
                    "label": f["label"], "label_locator": f["label_locator"],
                    "field_locator": f["field_locator"], "value_locator": f["value_locator"],
                    "source_sha256": f["source_sha256"], "emitted_sha256": sha(emitted),
                    "alias_replacements": changes,
                    "difference_verdict": "exact_except_explicit_id_alias",
                })
        body = {"zh": projected["zh"], "en": projected["en"]}
        records.append({"id": card["alias"], **body})
        mapping.append({"alias": card["alias"], "source_id": card["id"], "record_sha256": sha(canonical(body))})
    records.sort(key=lambda r: r["id"])
    bundle = {"schema_version": BUNDLE_SCHEMA_VERSION, "source_commit": manifest["source_commit"], "field_policy": manifest["field_policy"], "records": records}
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "bundle.json").write_bytes(canonical(bundle))
    private_fidelity = {
        "schema_version": 1,
        "source_commit": manifest["source_commit"],
        "manifest_sha256": sha(manifest_path.read_bytes()),
        "bundle_sha256": sha(canonical(bundle)),
        "field_count": len(field_diffs),
        "fields": field_diffs,
        "exclusion_ledger": manifest["exclusions"],
        "rule": "Every emitted field is byte-identical to its frozen locator except exact replacements listed in alias_replacements; all other transformations are refused or excluded.",
    }
    public_fields = []
    for item in field_diffs:
        public_fields.append({"alias": item["alias"], "language": item["language"], "field": item["field"], "source_sha256": item["source_sha256"], "emitted_sha256": item["emitted_sha256"], "alias_replacement_counts": [change["count"] for change in item["alias_replacements"]], "difference_verdict": item["difference_verdict"]})
    public_fidelity = {"schema_version": 1, "source_commit": manifest["source_commit"], "manifest_sha256": sha(manifest_path.read_bytes()), "bundle_sha256": sha(canonical(bundle)), "field_count": len(public_fields), "fields": public_fields, "rule": "Every public field is byte-identical to its private frozen locator except exact opaque card-id alias tokens; source IDs, paths, labels, locators, and mapping are withheld."}
    (output_dir / "fidelity-evidence.json").write_bytes(canonical(public_fidelity))
    mapping_value = {"sealed": True, "source_commit": manifest["source_commit"], "bundle_sha256": sha(canonical(bundle)), "records": mapping}
    mapping_out.parent.mkdir(parents=True, exist_ok=True)
    mapping_out.write_bytes(canonical(mapping_value))
    private_fidelity_path = mapping_out.with_name(mapping_out.stem + "-fidelity-private.json")
    private_fidelity_path.write_bytes(canonical(private_fidelity))
    return {"status": "FAITHFUL_BUNDLE_PREPARED", "source_commit": manifest["source_commit"], "record_count": len(records), "bundle_sha256": sha(canonical(bundle)), "fidelity_evidence_sha256": sha(canonical(public_fidelity)), "private_fidelity_sha256": sha(canonical(private_fidelity)), "mapping_sha256": sha(canonical(mapping_value)), "field_count": len(field_diffs), "claim_boundary": "Exact source field bytes are preserved; only explicit card-id aliases may differ. Exclusions are recorded in the manifest."}

def main(argv: List[str]) -> int:
    p = argparse.ArgumentParser(description="Prepare a byte-faithful blind-review bundle from a frozen Git snapshot")
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--source-commit")
    p.add_argument("--manifest", type=Path)
    p.add_argument("--manifest-out", type=Path)
    p.add_argument("--receipt-out", type=Path)
    p.add_argument("--output-dir", type=Path)
    p.add_argument("--mapping-out", type=Path)
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args(argv)
    try:
        repo = args.repo.resolve()
        if args.self_test:
            return self_test(repo)
        if args.source_commit and args.manifest_out:
            m = collect_manifest(repo, args.source_commit)
            out = args.manifest_out if args.manifest_out.is_absolute() else repo / args.manifest_out
            out = ensure_private_output(repo, out, "manifest-out")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(canonical(m))
            print(json.dumps({"status": "FAITHFUL_MANIFEST_FROZEN", "source_commit": args.source_commit, "included": m["coverage"]["included"], "excluded": m["coverage"]["excluded"], "manifest_sha256": sha(out.read_bytes())}, ensure_ascii=False, indent=2))
            return 0
        if args.receipt_out and args.manifest:
            private_path = args.manifest if args.manifest.is_absolute() else repo / args.manifest
            private_bytes = private_path.read_bytes()
            private_manifest = json.loads(private_bytes)
            validate_manifest(private_manifest)
            receipt = public_receipt(private_manifest, sha(private_bytes))
            out = args.receipt_out if args.receipt_out.is_absolute() else repo / args.receipt_out
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(canonical(receipt))
            print(json.dumps({"status": "PUBLIC_MANIFEST_RECEIPT_WRITTEN", "receipt_sha256": sha(out.read_bytes()), "private_manifest_sha256": sha(private_bytes)}, ensure_ascii=False, indent=2))
            return 0
        if not args.manifest or not args.output_dir or not args.mapping_out:
            p.error("--source-commit + --manifest-out, or --manifest + --output-dir + --mapping-out is required")
        result = prepare(repo, (args.manifest if args.manifest.is_absolute() else repo / args.manifest).resolve(), (args.output_dir if args.output_dir.is_absolute() else repo / args.output_dir).resolve(), args.mapping_out.resolve())
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, Refused, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        return 1

def self_test(repo: Path) -> int:
    # The production path's adversarial proof is kept in a small fixture test file.
    # This executable hook is intentionally conservative: run the dedicated test.
    test = repo / "scripts" / "test_blind_fidelity.py"
    p = subprocess.run([sys.executable, str(test)], cwd=repo)
    return p.returncode

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
