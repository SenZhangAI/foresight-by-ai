#!/usr/bin/env python3
"""Negative and smoke tests for the bilingual judgment query tool.

Run from the repository root with:
    python3 scripts/test_find_judgments.py

The tests use temporary ledger copies, so no source card is modified.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "find-judgments.py"


def load_query_module():
    spec = importlib.util.spec_from_file_location("find_judgments", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import find-judgments.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class QueryToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.module = load_query_module()
        self.tempdir = tempfile.TemporaryDirectory(prefix="find-judgments-test-")
        self.repo = Path(self.tempdir.name)
        (self.repo / "docs").mkdir()
        shutil.copytree(ROOT / "docs" / "zh" / "ledger", self.repo / "docs" / "zh" / "ledger")
        shutil.copytree(ROOT / "docs" / "en" / "ledger", self.repo / "docs" / "en" / "ledger")
        self.module.REPO = self.repo

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_current_register_is_dynamic_and_accepts_landscape_only(self) -> None:
        records = self.module.build_records()
        self.assertEqual(len(records), 123)
        self.assertEqual(records[-1]["id"], "J-123")
        self.assertEqual(next(record for record in records if record["id"] == "J-123")["status"], "LANDSCAPE_ONLY")

        # Add a syntactically valid next card to both projections. A fixed
        # J-001–J-123 implementation must not pass this assertion.
        for lang in ("zh", "en"):
            source = self.repo / "docs" / lang / "ledger" / "123-123.md"
            target = self.repo / "docs" / lang / "ledger" / "124-124.md"
            target.write_text(
                source.read_text(encoding="utf-8").replace("J-123", "J-124"),
                encoding="utf-8",
            )
        expanded = self.module.build_records()
        self.assertEqual(len(expanded), 124)
        self.assertEqual(expanded[-1]["id"], "J-124")

    def test_delete_one_language_card_fails_closed(self) -> None:
        (self.repo / "docs" / "en" / "ledger" / "123-123.md").unlink()
        with self.assertRaisesRegex(self.module.RegisterError, "bilingual ID mismatch"):
            self.module.build_records()

    def assert_metadata_drift(self, path: Path, old: str, new: str) -> None:
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        with self.assertRaisesRegex(self.module.RegisterError, "bilingual metadata mismatch"):
            self.module.build_records()

    def test_status_drift_fails_closed(self) -> None:
        self.assert_metadata_drift(
            self.repo / "docs" / "zh" / "ledger" / "122-122.md",
            "- **状态**：ACTIVE",
            "- **状态**：REVISED",
        )

    def test_confidence_drift_fails_closed(self) -> None:
        self.assert_metadata_drift(
            self.repo / "docs" / "zh" / "ledger" / "122-122.md",
            "- **置信度**：低",
            "- **置信度**：中",
        )

    def test_time_window_drift_fails_closed(self) -> None:
        self.assert_metadata_drift(
            self.repo / "docs" / "zh" / "ledger" / "122-122.md",
            "2027-01-01 至 2035-12-31",
            "2027-01-01 至 2035-12-30",
        )

    def test_duplicate_query_field_fails_explicitly(self) -> None:
        path = self.repo / "docs" / "zh" / "ledger" / "123-123.md"
        text = path.read_text(encoding="utf-8")
        marker = "- **状态**：LANDSCAPE_ONLY"
        self.assertEqual(text.count(marker), 1)
        path.write_text(text.replace(marker, marker + "\n" + marker, 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate query field"):
            self.module.build_records()

    def test_unsupported_status_fails_explicitly(self) -> None:
        path = self.repo / "docs" / "zh" / "ledger" / "123-123.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("- **状态**：LANDSCAPE_ONLY", "- **状态**：UNKNOWN", 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "cannot parse status"):
            self.module.build_records()

        # A known token embedded in an unknown value must not be accepted.
        path.write_text(text.replace("- **状态**：LANDSCAPE_ONLY", "- **状态**：UNKNOWN（previously ACTIVE）", 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "cannot parse status"):
            self.module.build_records()

    def test_cli_rejects_unfiltered_and_unknown_status(self) -> None:
        no_filter = subprocess.run(
            [sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True
        )
        self.assertNotEqual(no_filter.returncode, 0)
        self.assertIn("at least one filter is required", no_filter.stderr)

        unknown = subprocess.run(
            [sys.executable, str(SCRIPT), "--status", "UNKNOWN"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(unknown.returncode, 0)
        self.assertIn("invalid choice", unknown.stderr)

        empty = subprocess.run(
            [sys.executable, str(SCRIPT), "--chain", "C999", "--status", "ACTIVE"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(empty.returncode, 0)
        self.assertIn("No judgments matched the query.", empty.stdout)
        self.assertNotIn("J-001", empty.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
