#!/usr/bin/env python3
"""Read-only negative-control audit for blind Gate-2 veto backflow.

The source is each card's effective R1 blind-review line. Round-2 lines marked
in doubt/void are not silently treated as current evidence; the card's own
R1 retain record is the auditable source used by the current reconciliation.
This intentionally stays outside scripts/check.py: it audits judgment fields,
not repository mechanics.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

CARD_RE = re.compile(r"(?m)^### (J-\d{3}) ·.*?(?=^### J-|\Z)", re.S)

def cards(root: Path, lang: str):
    for path in sorted((root / "docs" / lang / "ledger").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in CARD_RE.finditer(text):
            yield match.group(1), path, match.group(0)

def effective_veto(block: str, lang: str):
    if lang == "en":
        blind = [line for line in block.splitlines()
                 if line.startswith("- **Isolated blind re-review") and
                 "blind record R1-" in line]
        gate = next((line for line in block.splitlines()
                     if line.startswith("- **Diffusion-gate review**")), "")
        if not blind or "verdict `VETO`" not in blind[-1] or "Gate 2" not in blind[-1] or "disposition: retain" not in blind[-1]:
            return None, gate
        return blind[-1], gate
    blind = [line for line in block.splitlines()
             if line.startswith("- **隔离盲判复审") and "盲判编号 R1-" in line]
    gate = next((line for line in block.splitlines()
                 if line.startswith("- **普及闸复核**")), "")
    if not blind or "裁定 `VETO`" not in blind[-1] or "闸二" not in blind[-1] or "处置「保留" not in blind[-1]:
        return None, gate
    return blind[-1], gate

def scan(root: Path, lang: str, inject: bool = False):
    mismatches = []
    source = []
    for card_id, path, block in cards(root, lang):
        blind, gate = effective_veto(block, lang)
        if blind is None:
            continue
        source.append(card_id)
        mentions_gate2 = ("Gate 2" in gate) if lang == "en" else ("闸二" in gate)
        if not mentions_gate2:
            mismatches.append({"card": card_id, "path": str(path.relative_to(root)), "reason": "blind Gate-2 veto not in diffusion field"})
    if inject:
        source.append("J-NEGATIVE-CONTROL")
        mismatches.append({"card": "J-NEGATIVE-CONTROL", "path": "<injected>", "reason": "blind Gate-2 VETO not in diffusion field"})
    return {"source_gate2_veto_cards": sorted(source), "missing_backflow": mismatches}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--inject-mismatch", action="store_true", help="inject a synthetic blind-Gate-2-only counterexample")
    args = parser.parse_args()
    result = {lang: scan(args.root, lang, args.inject_mismatch) for lang in ("zh", "en")}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    if not args.inject_mismatch and any(v["missing_backflow"] for v in result.values()):
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
