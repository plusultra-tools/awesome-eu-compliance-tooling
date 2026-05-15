"""Smoke tests for tools.auto_update.

Run with: ``python -m unittest tests.test_auto_update -v``
Stdlib only; no pytest needed.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Make tools/ importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import tools.auto_update as au  # noqa: E402

FIXTURE_README = """# Awesome EU Compliance Tooling

## Cyber Resilience Act (CRA)

- [syft](https://github.com/anchore/syft) — Generate SBOM from container images. `go` · `Apache-2.0` · *last release: 2025-12*
- [cyclonedx-cli](https://github.com/CycloneDX/cyclonedx-cli) — CLI for CycloneDX SBOMs. `dotnet` · `Apache-2.0` · *last release: 2025-11*

## GDPR — engineering tooling

- [presidio](https://github.com/microsoft/presidio) — PII de-identification SDK. `python` · `MIT` · *last release: 2026-01*
"""


class TestParseReadmeSections(unittest.TestCase):
    """parse_readme_sections splits the README into (section, name, url, desc) tuples."""

    def setUp(self) -> None:
        self.tmp = Path("/tmp") / "test_readme_fixture.md"
        self.tmp.write_text(FIXTURE_README, encoding="utf-8")

    def tearDown(self) -> None:
        try:
            self.tmp.unlink()
        except FileNotFoundError:
            pass

    def test_parses_at_least_three_entries(self) -> None:
        entries = au.parse_readme_sections(str(self.tmp))
        self.assertGreaterEqual(len(entries), 3, f"expected >=3 entries, got {len(entries)}: {entries}")

    def test_extracts_names_and_urls(self) -> None:
        entries = au.parse_readme_sections(str(self.tmp))
        names = {e[1] for e in entries}
        self.assertIn("syft", names)
        self.assertIn("presidio", names)
        for e in entries:
            self.assertTrue(e[2].startswith("https://"), f"non-https URL: {e[2]}")


class TestProposeAdditions(unittest.TestCase):
    """propose_additions returns empty when scraped is a subset of current."""

    def test_subset_returns_empty(self) -> None:
        scraped = [
            {"repo": "anchore/syft", "url": "https://github.com/anchore/syft", "description": "SBOM tool"},
        ]
        current = [
            ("Cyber Resilience Act (CRA)", "syft", "https://github.com/anchore/syft", "..."),
        ]
        result = au.propose_additions(scraped, current, eu_keywords=["GDPR", "CRA"])
        self.assertEqual(result, [], "subset should yield no additions")

    def test_new_entry_matches_keyword(self) -> None:
        scraped = [
            {"repo": "example/cra-evidence", "url": "https://github.com/example/cra-evidence",
             "description": "CRA Article 14 evidence pack generator"},
        ]
        current: list[tuple[str, str, str, str]] = []
        result = au.propose_additions(scraped, current, eu_keywords=["CRA"])
        self.assertEqual(len(result), 1, "should propose 1 new entry")
        self.assertEqual(result[0]["repo"], "example/cra-evidence")


if __name__ == "__main__":
    unittest.main(verbosity=2)
