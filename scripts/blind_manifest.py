#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Freeze the machine-readable input manifest for `blind_bundle.py`.

The selection rule lives HERE, deliberately outside the generator: the
generator must be auditable as "turn this frozen input into that bundle", and a
generator that also decides what goes in could quietly change the population
between runs while every hash still agreed with itself.

The rule it applies is the published one — a card is included when BOTH its
Chinese and its English card carry all six required retained fields — with one
correction over the 2026-10-09 freeze: the rule is evaluated AFTER de-labelling
rather than before. Several cards repeat their one-sentence judgment as the
card's heading title, so removing the title (which the isolation requirement
demands) leaves the judgment field blank. Such a card has no claim left for a
reviewer to judge, so it is excluded with a reason rather than shipped empty.

Usage
  blind_manifest.py --repo . --out docs/evidence/blind-review/manifest-<date>.json
"""
from __future__ import annotations

import argparse
import copy
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import blind_bundle as bb  # noqa: E402  (same-directory tool, imported for one rule)

LEDGER_GLOB = "docs/%s/ledger/*.md"
MIGRATION_SNAPSHOT = "docs/evidence/legacy-ledger-migration.md"
MIGRATION_HEADING_RE = re.compile(r"^##\s+(J-\d{3})\s*$", re.M)
CARD_HEADING_RE = re.compile(r"^###\s+(J-\d{3})", re.M)


def collect_cards(repo: Path, language: str) -> Dict[str, str]:
    """card id -> repo-relative path, for one language's ledger."""
    found: Dict[str, str] = {}
    for path in sorted(repo.glob(LEDGER_GLOB % language)):
        text = path.read_text(encoding="utf-8")
        for cid in CARD_HEADING_RE.findall(text):
            rel = path.relative_to(repo).as_posix()
            if cid in found:
                raise SystemExit("%s appears in both %s and %s" % (cid, found[cid], rel))
            found[cid] = rel
    return found


def claim_survives(repo: Path, cid: str, zh_rel: str, en_rel: str,
                   titles: List[str], paths: List[str]) -> Tuple[bool, str]:
    """Apply the generator's own extraction + redaction, then test the rule.

    `titles`/`paths` are built from EVERY candidate card, not just the ones that
    end up included. That makes this redaction a superset of the generator's
    (whose clue list is built from the included cards only), so a field that
    survives here cannot be emptied later — the conservative direction.
    """
    record = {"cid": cid}
    for language, rel in (("zh", zh_rel), ("en", en_rel)):
        text = (repo / rel).read_text(encoding="utf-8")
        try:
            section = bb.card_section(text, cid)
            record[language] = bb.extract_fields(section, cid)
        except bb.Refused as exc:
            return False, str(exc).replace(cid, "the card")
    bb.redact_traceback_clues(record, titles, paths)
    for language in bb.LANGUAGES:
        for key in bb.REQUIRED_KEYS:
            if not re.search(r"[0-9A-Za-z\u4e00-\u9fff]", record[language].get(key, "")):
                return False, ("the %s %s field carries no readable content once the "
                               "heading title is removed" % (language, key))
    return True, ""


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Freeze the blind-review input manifest.")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    repo = args.repo.resolve()

    zh = collect_cards(repo, "zh")
    en = collect_cards(repo, "en")
    paired = sorted(set(zh) & set(en))
    unpaired = sorted(set(zh) ^ set(en))

    titles: List[str] = []
    paths: List[str] = []
    for cid in paired:
        for rel in (zh[cid], en[cid]):
            section = bb.card_section((repo / rel).read_text(encoding="utf-8"), cid)
            heading = bb.HEADING_RE.search(section)
            if heading:
                for part in re.split(r"[·:：]", heading.group(2)):
                    part = bb.clean_value(part)
                    if part:
                        titles.append(bb.fold(part))
            paths.append(rel)

    cards: List[Dict[str, Any]] = []
    claim_lost: List[str] = []
    for cid in paired:
        ok, reason = claim_survives(repo, cid, zh[cid], en[cid], titles, paths)
        if not ok:
            claim_lost.append(reason)
            continue
        cards.append({
            "id": cid,
            "zh_path": zh[cid],
            "en_path": en[cid],
            "zh_sha256": bb.sha256_bytes((repo / zh[cid]).read_bytes()),
            "en_sha256": bb.sha256_bytes((repo / en[cid]).read_bytes()),
            "include_reason": ("both language cards carry all six required retained "
                               "fields and keep a readable claim after de-labelling"),
        })

    migration = len(MIGRATION_HEADING_RE.findall(
        (repo / MIGRATION_SNAPSHOT).read_text(encoding="utf-8")))
    exclusions: List[Dict[str, Any]] = [{
        "subject": "%s migration snapshots" % MIGRATION_SNAPSHOT,
        "reason": ("Historical migration snapshots duplicate the current ledger cards "
                   "and are not a second judgment set."),
        "count": migration,
    }]
    if claim_lost:
        exclusions.append({
            "subject": "ledger cards whose claim does not survive de-labelling",
            "reason": ("The card repeats its one-sentence judgment as its heading title, "
                       "so removing the title — which the isolation requirement demands — "
                       "leaves no claim for a reviewer to judge. Shipping the record blank "
                       "would be worse than excluding it."),
            "count": len(claim_lost),
        })
    if unpaired:
        exclusions.append({
            "subject": "ledger cards present in only one language",
            "reason": "A card with no bilingual counterpart cannot be paired in the bundle.",
            "count": len(unpaired),
        })

    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                          stdout=subprocess.PIPE, check=True).stdout.decode().strip()
    excluded = sum(item["count"] for item in exclusions)
    manifest = {
        "schema_version": bb.SCHEMA_VERSION,
        "source_commit": head,
        "inclusion_rule": (
            "Include every current ledger card for which both the Chinese and English "
            "card contain all six required retained fields — judgment, audience, "
            "reasoning chain, time window, falsifier, leading indicator — AND still "
            "carry readable content in each of them after de-labelling. Exclude "
            "migration snapshots because they duplicate current judgments."),
        "exclusions": exclusions,
        "coverage": {"candidate_total": len(cards) + excluded,
                     "included": len(cards), "excluded": excluded},
        "cards": cards,
    }
    bb.validate_manifest(copy.deepcopy(manifest))
    out = args.out if args.out.is_absolute() else (repo / args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(bb.canonical_json(manifest))
    print("frozen %s\n  source_commit=%s\n  candidate=%d included=%d excluded=%d\n"
          "  manifest_sha256=%s"
          % (out, head, manifest["coverage"]["candidate_total"], len(cards), excluded,
             bb.sha256_bytes(out.read_bytes())))
    for reason in sorted(set(claim_lost)):
        print("  excluded (claim lost): %s" % reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
