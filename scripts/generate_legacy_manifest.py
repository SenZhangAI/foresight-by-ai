#!/usr/bin/env python3
"""Generate the fixed J-001--J-086 legacy migration manifest."""
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASELINE_SHA = "aa01c7c6531cb769a284c8e36cd4573f298497bd"
IDS = [f"J-{n:03d}" for n in range(1, 87)]
FIELDS = {
    "zh": {
        "proposed_date": "提出日期", "judgment": "一句话判断", "audience_scale": "受众规模",
        "diffusion_gate": "普及闸复核", "lens": "透镜", "reasoning_chain": "推理链",
        "time_window": "时间窗", "falsifier": "证伪条件", "leading_indicator": "领先指标",
        "confidence": "置信度", "depends_on": "depends-on", "opposing_mechanism": "最强反方",
        "consensus": "与共识", "comparison_source": "外部对照来源", "source": "出处",
        "next_review": "下次检查日", "status": "状态",
    },
    "en": {
        "proposed_date": "Proposed date", "judgment": "One-sentence judgment", "audience_scale": "Audience scale",
        "diffusion_gate": "Diffusion-gate review", "lens": "Lens", "reasoning_chain": "Reasoning chain",
        "time_window": "Time window", "falsifier": "Falsifier", "leading_indicator": "Leading indicator",
        "confidence": "Confidence", "depends_on": "depends-on", "opposing_mechanism": "Strongest opposing mechanism",
        "consensus": "Against consensus", "comparison_source": "External comparison source", "source": "Source",
        "next_review": "Next review", "status": "Status",
    },
}

def blocks(text):
    matches = list(re.finditer(r"^### (J-\d{3})\b[^\n]*.*?(?=^### J-|\Z)", text, re.M | re.S))
    return {m.group(1): (m.start(), m.group(0)) for m in matches}

def field_value(block, label):
    pattern = re.compile(r"^\s*-\s*\*\*" + re.escape(label) + r"\*\*[:：]\s*(.*)$", re.M)
    matches = list(pattern.finditer(block))
    if len(matches) != 1:
        raise SystemExit(f"expected one {label!r}, got {len(matches)}")
    return matches[0].group(1).strip(), matches[0].start()

def line_anchor(block, label, value=None):
    lines = block.splitlines()
    for i, line in enumerate(lines):
        if re.search(r"^\s*-\s*\*\*" + re.escape(label) + r"\*\*[:：]", line):
            if value is None or value in line:
                return sum(len(x) + 1 for x in lines[:i])
    return 0

def line_number(text, offset):
    return text.count("\n", 0, offset) + 1

def git_file(lang):
    path = f"docs/{lang}/90-ledger.md"
    return subprocess.check_output(["git", "show", f"{BASELINE_SHA}:{path}"], text=True), path

def current_file(lang, jid):
    for p in sorted((ROOT / "docs" / lang / "ledger").glob("*.md")):
        text = p.read_text()
        if re.search(r"^### " + re.escape(jid) + r"\b", text, re.M):
            return text, str(p.relative_to(ROOT))
    raise SystemExit(f"missing current {lang} {jid}")

cards = []
current_digest_rows = []
for jid in IDS:
    entry = {"id": jid, "languages": {}}
    for lang in ("zh", "en"):
        historical_text, historical_path = git_file(lang)
        historical_blocks = blocks(historical_text)
        if jid not in historical_blocks:
            raise SystemExit(f"missing historical {lang} {jid}")
        h_start, h_block = historical_blocks[jid]
        current_text, current_path = current_file(lang, jid)
        current_blocks = blocks(current_text)
        c_start, c_block = current_blocks[jid]
        fields = {}
        for key, label in FIELDS[lang].items():
            if key == "audience_scale":
                try:
                    h_value, _ = field_value(h_block, label)
                except SystemExit:
                    h = {"status": "UNKNOWN", "value": None,
                         "reason": ("历史快照无独立字段；数值与分类嵌在普及闸复核中，不得反投影。"
                                    if lang == "zh" else
                                    "The fixed historical baseline has no standalone Audience scale field; its scale is embedded in the Diffusion-gate review and must not be back-projected."),
                         "source": {"sha": BASELINE_SHA, "path": historical_path,
                                    "line": line_number(historical_text, h_start)}}
                else:
                    h = {"status": "KNOWN", "value": h_value,
                         "reason": "Copied verbatim from the fixed historical baseline.",
                         "source": {"sha": BASELINE_SHA, "path": historical_path,
                                    "line": line_number(historical_text, h_start + line_anchor(h_block, label, h_value))}}
            else:
                h_value, _ = field_value(h_block, label)
                h = {"status": "KNOWN", "value": h_value,
                     "reason": "Copied verbatim from the fixed historical baseline.",
                     "source": {"sha": BASELINE_SHA, "path": historical_path,
                                "line": line_number(historical_text, h_start + line_anchor(h_block, label, h_value))}}
            c_value, _ = field_value(c_block, label)
            if key == "audience_scale" and c_value.startswith("UNKNOWN"):
                c = {"status": "UNKNOWN", "value": c_value,
                     "reason": "Current card deliberately carries an explicit UNKNOWN boundary because the migration audit lacks independent audience evidence.",
                     "source": {"path": current_path,
                                "line": line_number(current_text, c_start + line_anchor(c_block, label, c_value))}}
            else:
                c = {"status": "KNOWN", "value": c_value,
                     "reason": "Current migration value copied from the paired ledger card.",
                     "source": {"path": current_path,
                                "line": line_number(current_text, c_start + line_anchor(c_block, label, c_value))}}
            fields[key] = {"label": label, "historical": h, "current": c}
            current_digest_rows.append([jid, lang, key, c["status"], c["value"]])
        entry["languages"][lang] = {
            "file": current_path,
            "heading": {"line": line_number(current_text, c_start), "text": current_text[c_start:current_text.find("\n", c_start)]},
            "fields": fields,
        }
    cards.append(entry)

digest = hashlib.sha256(json.dumps(current_digest_rows, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
manifest = {
    "schema_version": 1,
    "purpose": "Canonical bilingual migration inventory for the closed legacy set J-001--J-086.",
    "baseline_sha": BASELINE_SHA,
    "baseline_source": "git show <baseline_sha>:docs/{zh,en}/90-ledger.md",
    "closed_ids": IDS,
    "canonical_fields": list(FIELDS["en"]),
    "current_digest": digest,
    "cards": cards,
}
out = ROOT / "docs" / "evidence" / "legacy-ledger-migration-manifest.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(out)
print("cards", len(cards), "digest", digest)
