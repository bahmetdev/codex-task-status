#!/usr/bin/env python3
"""Dependency-free tests for validate_title.py."""

import json
import tempfile
import unittest
from pathlib import Path

from validate_title import ConfigError, load_config, validate_config, validate_title


class ValidateTitleTests(unittest.TestCase):
    def test_recommended_state(self) -> None:
        valid, _ = validate_title("Crop (work)", load_config(None))
        self.assertTrue(valid)

    def test_recommended_schedule(self) -> None:
        valid, _ = validate_title("News (10:00·19:00)", load_config(None))
        self.assertTrue(valid)

    def test_rejects_phrase_subject_by_default(self) -> None:
        valid, _ = validate_title("Crop Menu (work)", load_config(None))
        self.assertFalse(valid)

    def test_rejects_unknown_state(self) -> None:
        valid, _ = validate_title("Crop (working)", load_config(None))
        self.assertFalse(valid)

    def test_rejects_invalid_clock(self) -> None:
        for title in ["News (24:00)", "News (09:60)", "News (9:00)"]:
            with self.subTest(title=title):
                self.assertFalse(validate_title(title, load_config(None))[0])

    def test_example_matches_defaults(self) -> None:
        example = Path(__file__).parents[1] / "assets/task-status.example.json"
        self.assertEqual(load_config(example), load_config(None))

    def test_optional_groups_fail_without_crashing(self) -> None:
        config = load_config(None)
        config["title_pattern"] = r"^(?P<subject>A)?(?P<status>work)?$"
        validate_config(config)
        self.assertFalse(validate_title("", config)[0])

    def test_case_insensitive_duplicate_states_rejected(self) -> None:
        config = load_config(None)
        config.update(states=["work", "WORK"], case_sensitive=False)
        with self.assertRaises(ConfigError):
            validate_config(config)

    def test_custom_language_and_phrase(self) -> None:
        custom = {
            "title_pattern": r"^(?P<subject>[^()]+) \[(?P<status>[^\[\]]+)\]$",
            "states": ["робота", "перевірка"],
            "schedule_pattern": None,
            "case_sensitive": True,
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(custom), encoding="utf-8")
            config = load_config(path)
        valid, _ = validate_title("Меню кадрування [робота]", config)
        self.assertTrue(valid)

    def test_requires_named_groups(self) -> None:
        custom = {
            "title_pattern": r"^.+$",
            "states": ["work"],
            "schedule_pattern": None,
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(custom), encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
