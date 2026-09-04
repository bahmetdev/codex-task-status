#!/usr/bin/env python3
"""Validate Codex task titles against a configurable status model."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "title_pattern": r"^(?P<subject>[^\s()]+) \((?P<status>[^()]+)\)$",
    "states": [
        "work", "qa", "feedback", "approval", "blocked", "paused",
        "committing", "committed", "pushing", "pushed", "done", "attention",
    ],
    "schedule_pattern": (
        r"^(?:(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)·)?"
        r"(?:[01]\d|2[0-3]):[0-5]\d"
        r"(?:·(?:[01]\d|2[0-3]):[0-5]\d)*$"
    ),
    "case_sensitive": True,
}


class ConfigError(ValueError):
    """Raised when the validator configuration is invalid."""


def load_config(path: Path | None) -> dict[str, Any]:
    config = dict(DEFAULT_CONFIG)
    if path is not None:
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ConfigError(f"cannot read config: {exc}") from exc
        if not isinstance(loaded, dict):
            raise ConfigError("config root must be a JSON object")
        config.update(loaded)
    validate_config(config)
    return config


def validate_config(config: dict[str, Any]) -> None:
    unknown = set(config) - set(DEFAULT_CONFIG)
    if unknown:
        raise ConfigError("unknown config keys: " + ", ".join(sorted(unknown)))
    pattern = config.get("title_pattern")
    states = config.get("states")
    schedule_pattern = config.get("schedule_pattern")
    case_sensitive = config.get("case_sensitive", True)

    if not isinstance(pattern, str) or not pattern:
        raise ConfigError("title_pattern must be a non-empty string")
    if not isinstance(states, list) or not states:
        raise ConfigError("states must be a non-empty list")
    if any(not isinstance(state, str) or not state.strip() for state in states):
        raise ConfigError("every state must be a non-empty string")
    if len(states) != len(set(states)):
        raise ConfigError("states must be unique")
    if schedule_pattern is not None and not isinstance(schedule_pattern, str):
        raise ConfigError("schedule_pattern must be a string or null")
    if not isinstance(case_sensitive, bool):
        raise ConfigError("case_sensitive must be true or false")
    if not case_sensitive and len(states) != len({s.casefold() for s in states}):
        raise ConfigError("states must be unique under case-insensitive matching")

    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        compiled = re.compile(pattern, flags)
        if schedule_pattern is not None:
            re.compile(schedule_pattern, flags)
    except re.error as exc:
        raise ConfigError(f"invalid regular expression: {exc}") from exc
    missing = {"subject", "status"} - set(compiled.groupindex)
    if missing:
        raise ConfigError(
            "title_pattern must define named groups: " + ", ".join(sorted(missing))
        )


def validate_title(title: str, config: dict[str, Any]) -> tuple[bool, str]:
    flags = 0 if config.get("case_sensitive", True) else re.IGNORECASE
    match = re.fullmatch(config["title_pattern"], title, flags)
    if match is None:
        return False, "title does not match title_pattern"

    subject = match.group("subject")
    status = match.group("status")
    if not subject or not subject.strip():
        return False, "subject is empty"
    if not status or not status.strip():
        return False, "status is empty"

    states = config["states"]
    if config.get("case_sensitive", True):
        known = status in states
    else:
        known = status.casefold() in {state.casefold() for state in states}

    schedule_pattern = config.get("schedule_pattern")
    scheduled = bool(
        schedule_pattern and re.fullmatch(schedule_pattern, status, flags)
    )
    if not known and not scheduled:
        return False, f"unknown status or schedule: {status}"
    return True, f"subject={subject}; status={status}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("titles", nargs="+", help="task title(s) to validate")
    parser.add_argument("--config", type=Path, help="JSON configuration path")
    parser.add_argument("--json", action="store_true", help="emit JSON results")
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return 2

    results = []
    all_valid = True
    for title in args.titles:
        valid, reason = validate_title(title, config)
        all_valid = all_valid and valid
        results.append({"title": title, "valid": valid, "reason": reason})

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            marker = "OK" if result["valid"] else "INVALID"
            print(f"{marker}: {result['title']} — {result['reason']}")
    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
