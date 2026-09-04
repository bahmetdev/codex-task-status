# Configuration

## Recommended setup

Use `assets/task-status.example.json` unchanged when the user wants the recommended structure.

## Custom setup

Ask only for choices that materially change behavior:

1. What should a title look like?
2. May the subject contain spaces, and which language should subjects use?
3. Which state labels should replace or extend the recommended labels?
4. Does Git apply, and how should local commit and remote push states differ?
5. Which label represents completed non-Git work?
6. How should recurring schedules appear?

Translate labels when requested, but preserve their distinct meanings. In particular, do not collapse `feedback` into `approval`, `qa` into `done`, or in-progress Git operations into verified Git results unless the user explicitly accepts that loss of information.

## Make it persistent

Installing a skill makes it available; it does not guarantee that every task invokes it. For ongoing use, show the user `assets/agents-snippet.md`, adapt it to their approved choices, and place it in the project or global agent instructions only with their authorization. Preserve unrelated guidance. Do not install duplicate rules at both scopes unless an actual project override is needed.

Record custom label-to-meaning mappings and transitions in those instructions or a linked `task-status.md` policy. The JSON below validates syntax only and is not a substitute for that semantic policy. If no persistent setup is requested, apply the convention only in the current task and say so.

## Validator config

The JSON config supports:

```json
{
  "title_pattern": "^(?P<subject>[^\\s()]+) \\((?P<status>[^()]+)\\)$",
  "states": ["work", "qa", "feedback"],
  "schedule_pattern": "^(?:[01]\\d|2[0-3]):[0-5]\\d(?:·(?:[01]\\d|2[0-3]):[0-5]\\d)*$",
  "case_sensitive": true
}
```

Requirements:

- `title_pattern` must be a valid regular expression with named groups `subject` and `status`.
- `states` must be a non-empty list of unique non-empty strings.
- Unknown keys are rejected so misspelled settings cannot silently fall back to defaults.
- Omitted keys inherit the recommended defaults. Set `schedule_pattern` to `null` to disable schedule suffixes; when a pattern is present, a matching suffix is accepted in addition to `states`.
- `case_sensitive` defaults to `true`.

Keep project-specific config near the project instructions when the repository owns the convention. Keep personal cross-project config in the user's private Codex setup. Do not publish private paths, task names, schedules, or organization vocabulary in a reusable skill fork.
