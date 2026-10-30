#!/usr/bin/env python3
"""Adversarial tests for scripts/blind_fidelity.py.

These tests attack the boundary, not the happy path: CRLF and trailing spaces,
Unicode normalization, links/metadata, source-commit checkout binding, locator
hashes, and the exact-only id alias rule.
"""
from __future__ import annotations
import copy
import json
import subprocess
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blind_fidelity as bf


def run(*args: str, cwd: Path) -> None:
    subprocess.run(list(args), cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def card(cid: str, claim: str, *, crlf: bool = False, link: bool = False) -> str:
    e = "\r\n" if crlf else "\n"
    claim = claim + (" https://example.invalid/source" if link else "")
    return (
        f"### {cid} · Heading that is not emitted{e}"
        f"- **一句话判断**：{claim}{e}"
        f"  continuation  with  two spaces{e}"
        f"- **受众规模**：百万级读者{e}"
        f"- **推理链**：供给增加 → 约束保留{e}"
        f"- **时间窗**：2028–2030{e}"
        f"- **证伪条件**：到 2030 年未发生{e}"
        f"- **领先指标**：部署量{e}"
    )


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="blind-fidelity-test-") as td:
        repo = Path(td) / "repo"
        (repo / "docs/zh/ledger").mkdir(parents=True)
        (repo / "docs/en/ledger").mkdir(parents=True)
        zh = card("J-001", "保留 J-001 的字节边界：全宽Ａ与组合字符 e\u0301。", crlf=True)
        en = card("J-001", "Preserve J-001 byte boundaries: fullwidth Ａ and e\u0301.", crlf=True)
        (repo / "docs/zh/ledger/01.md").write_bytes(("# zh\r\n" + zh).encode())
        (repo / "docs/en/ledger/01.md").write_bytes(("# en\r\n" + en).encode())
        # These paired cards must be excluded, not cleaned: one carries a foreign
        # card id and the other carries a URL in a required source field.
        (repo / "docs/zh/ledger/02.md").write_bytes(card("J-002", "不可清洗 J-001").encode())
        (repo / "docs/en/ledger/02.md").write_bytes(card("J-002", "Must not be cleaned J-001").encode())
        (repo / "docs/zh/ledger/03.md").write_bytes(card("J-003", "不可清洗", link=True).encode())
        (repo / "docs/en/ledger/03.md").write_bytes(card("J-003", "Must not be cleaned", link=True).encode())
        (repo / "docs/zh/ledger/04.md").write_bytes(card("J-004", "不可清洗 diffusion-gate: reviewed").encode())
        (repo / "docs/en/ledger/04.md").write_bytes(card("J-004", "Must not be cleaned diffusion-gate: reviewed").encode())
        zh_bad = card("J-005", "UTF-8 invalid").encode().replace("部署量".encode(), b"\xff")
        en_bad = card("J-005", "UTF-8 invalid").encode().replace("部署量".encode(), b"\xff")
        (repo / "docs/zh/ledger/05.md").write_bytes(zh_bad)
        (repo / "docs/en/ledger/05.md").write_bytes(en_bad)
        (repo / "docs/zh/ledger/06.md").write_bytes(card("J-006", "不可清洗 status: reviewed").encode())
        (repo / "docs/en/ledger/06.md").write_bytes(card("J-006", "Must not be cleaned status: reviewed").encode())
        zh_trace = card("J-007", "不可清洗").encode().replace("百万级读者".encode(), b"docs/evidence/example.md").replace("供给增加".encode(), b"#section")
        en_trace = card("J-007", "Must not be cleaned").encode().replace("百万级读者".encode(), b"docs/evidence/example.md").replace("供给增加".encode(), b"#section")
        (repo / "docs/zh/ledger/07.md").write_bytes(zh_trace)
        (repo / "docs/en/ledger/07.md").write_bytes(en_trace)
        (repo / "docs/zh/ledger/08.md").write_bytes(card("J-008", "不可清洗 [source](docs/evidence/example.md#section)").encode())
        (repo / "docs/en/ledger/08.md").write_bytes(card("J-008", "Must not be cleaned [source](docs/evidence/example.md#section)").encode())
        (repo / "docs/zh/ledger/09.md").write_bytes(card("J-009", "不可清洗 /private/source.md#section").encode())
        (repo / "docs/en/ledger/09.md").write_bytes(card("J-009", "Must not be cleaned /private/source.md#section").encode())
        (repo / "docs/zh/ledger/10.md").write_bytes(card("J-010", "不可清洗 reports/source.md").encode())
        (repo / "docs/en/ledger/10.md").write_bytes(card("J-010", "Must not be cleaned reports/source.md").encode())
        (repo / "docs/zh/ledger/11.md").write_bytes(card("J-011", "不可清洗 #a").encode())
        (repo / "docs/en/ledger/11.md").write_bytes(card("J-011", "Must not be cleaned #a").encode())
        (repo / "docs/zh/ledger/12.md").write_bytes(card("J-012", "不可清洗 example.com/source").encode())
        (repo / "docs/en/ledger/12.md").write_bytes(card("J-012", "Must not be cleaned example.com/source").encode())
        (repo / "docs/zh/ledger/13.md").write_bytes(card("J-013", "不可清洗 snapshot fa4e657").encode())
        (repo / "docs/en/ledger/13.md").write_bytes(card("J-013", "Must not be cleaned snapshot fa4e657").encode())
        (repo / "docs/zh/ledger/14.md").write_bytes(card("J-014", r"不可清洗 C:\\repo\\source.md").encode())
        (repo / "docs/en/ledger/14.md").write_bytes(card("J-014", r"Must not be cleaned C:\\repo\\source.md").encode())
        (repo / "docs/zh/ledger/15.md").write_bytes(card("J-015", "不可清洗 ./docs/source.md").encode())
        (repo / "docs/en/ledger/15.md").write_bytes(card("J-015", "Must not be cleaned ./docs/source.md").encode())
        (repo / "docs/zh/ledger/16.md").write_bytes(card("J-016", "不可清洗 ../docs/source.md").encode())
        (repo / "docs/en/ledger/16.md").write_bytes(card("J-016", "Must not be cleaned ../docs/source.md").encode())
        run("git", "init", "-q", cwd=repo)
        run("git", "config", "user.email", "test@example.invalid", cwd=repo)
        run("git", "config", "user.name", "Test", cwd=repo)
        run("git", "add", "docs", cwd=repo)
        run("git", "commit", "-qm", "fixture", cwd=repo)
        source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()

        assert bf.main(["--repo", str(repo), "--source-commit", source, "--manifest-out", "docs/private-manifest.json"]) == 1
        try:
            bf.collect_manifest(repo, source[:12])
        except bf.Refused:
            pass
        else:
            raise AssertionError("abbreviated source commit was accepted")

        manifest = bf.collect_manifest(repo, source)
        assert manifest["coverage"] == {"candidate_total": 16, "included": 1, "excluded": 15}
        assert "field_policy" in manifest and "allowed_transform" in manifest["field_policy"]
        exclusion_reasons = " ".join(item["reason"] for item in manifest["exclusions"][0]["cards"])
        exclusion_fields = [field for item in manifest["exclusions"][0]["cards"] for field in item.get("fields", [])]
        assert "URL" in exclusion_reasons and "unmapped card identifier" in exclusion_reasons
        assert "commit/source metadata" in exclusion_reasons
        assert "Markdown link" in exclusion_reasons
        assert "source path" in exclusion_reasons
        assert "heading anchor" in exclusion_reasons
        assert "bare domain" in exclusion_reasons
        assert "gate/review metadata" in exclusion_reasons
        assert "status/review metadata" in exclusion_reasons
        assert "not UTF-8" in exclusion_reasons
        assert all(field["difference_verdict"] == "excluded_before_projection" for field in exclusion_fields)
        mp = repo / "manifest.json"
        mp.write_bytes(bf.canonical(manifest))
        out = Path(td) / "bundle"
        sealed = Path(td) / "sealed" / "mapping.json"
        result = bf.prepare(repo, mp, out, sealed)
        assert result["record_count"] == 1
        bundle = json.loads((out / "bundle.json").read_text())
        fields = bundle["records"][0]["zh"]
        assert "R-001" in fields["judgment"] and "J-001" not in fields["judgment"]
        assert fields["judgment"].startswith("- **一句话判断**：")
        assert "\r\n" in fields["judgment"]
        assert "  two spaces" in fields["judgment"]
        assert "Ａ" in fields["judgment"] and "e\u0301" in fields["judgment"]
        evidence = json.loads((out / "fidelity-evidence.json").read_text())
        assert all(item["difference_verdict"] == "exact_except_explicit_id_alias" for item in evidence["fields"])
        assert evidence["generator_commit"]
        assert len(evidence["generator_sha256"]) == 64
        exclusions = json.loads((out / "exclusion-evidence.json").read_text())
        assert exclusions["coverage"] == manifest["coverage"]
        assert exclusions["field_count"] == len(exclusion_fields)
        assert all(item["difference_verdict"] == "excluded_before_projection" for item in exclusions["fields"])
        assert all("source_path" not in item and "field_locator" not in item for item in exclusions["fields"])
        assert all("J-" not in item["reason"] for item in exclusions["fields"])
        assert bundle["source_commit"] == source

        # A dirty working-tree rewrite cannot affect a package pinned to the
        # immutable source commit.
        (repo / "docs/zh/ledger/01.md").write_text("### J-001\n- **一句话判断**：tampered\n", encoding="utf-8")
        out2 = Path(td) / "bundle-two"
        bf.prepare(repo, mp, out2, Path(td) / "sealed-two.json")
        assert (out / "bundle.json").read_bytes() == (out2 / "bundle.json").read_bytes()

        # Locator/hash tampering is refused; changing a label or offset cannot
        # masquerade as a faithful field.
        bad = copy.deepcopy(manifest)
        bad["cards"][0]["fields"]["zh"]["judgment"]["field_locator"]["start_byte"] += 1
        badp = Path(td) / "bad.json"
        badp.write_bytes(bf.canonical(bad))
        try:
            bf.prepare(repo, badp, Path(td) / "bad-out", Path(td) / "bad-map.json")
        except bf.Refused:
            pass
        else:
            raise AssertionError("tampered locator was accepted")

        # A self-consistent value-only locator attack is refused because prepare
        # re-parses the frozen section and compares the manifest metadata, rather
        # than trusting hashes supplied by the manifest.
        synced = copy.deepcopy(manifest)
        sf = synced["cards"][0]["fields"]["zh"]["judgment"]
        source_file = bf.snapshot(repo, source, synced["cards"][0]["zh_path"])
        vs, ve = sf["value_locator"]["start_byte"], sf["value_locator"]["end_byte"]
        fake = source_file[vs:ve]
        sf["field_locator"] = {"start_byte": vs, "end_byte": ve}
        sf["label_locator"] = {"start_byte": vs, "end_byte": vs + 1}
        sf["label"] = " "
        sf["label_sha256"] = bf.sha(b" ")
        sf["source_sha256"] = bf.sha(fake)
        syncedp = Path(td) / "synced-bad.json"
        syncedp.write_bytes(bf.canonical(synced))
        try:
            bf.prepare(repo, syncedp, Path(td) / "synced-bad-out", Path(td) / "synced-bad-map.json")
        except bf.Refused:
            pass
        else:
            raise AssertionError("self-consistent value-only locator attack was accepted")

        # Alias assignments are an explicit one-to-one map, not merely strings
        # that happen to have the R-NNN shape.
        duplicate_alias = copy.deepcopy(manifest)
        extra = copy.deepcopy(duplicate_alias["cards"][0])
        extra["id"] = "J-002"
        duplicate_alias["cards"].append(extra)
        try:
            bf.validate_manifest(duplicate_alias)
        except bf.Refused:
            pass
        else:
            raise AssertionError("duplicate alias was accepted")

        try:
            bf.prepare(repo, mp, Path(td) / "inside-map-out", repo / "mapping.json")
        except bf.Refused:
            pass
        else:
            raise AssertionError("mapping inside repository was accepted")

        # Only the declared id alias is allowed: a whitespace or Unicode change
        # is not a permissible substitute.
        src = " J-001\r\nＡ".encode("utf-8")
        projected, _ = bf.field_projection({"source_bytes": src}, {"J-001": "R-001"})
        assert projected == " R-001\r\nＡ".encode("utf-8")
        assert projected != "R-001\nA".encode("utf-8")
        embedded = b"J-0010 XJ-001 J-001"
        projected_embedded, _ = bf.field_projection({"source_bytes": embedded}, {"J-001": "R-001"})
        assert projected_embedded == b"J-0010 XJ-001 R-001"

    print("blind fidelity adversarial tests: PASS")


if __name__ == "__main__":
    main()
