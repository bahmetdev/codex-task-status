# Codex Task Status

A configurable Codex skill for concise, truthful task titles such as:

```text
Crop (work)
Release (committed)
News (10:00·19:00)
```

The workflow makes a busy task sidebar easier to scan while keeping important distinctions visible: agent work vs user QA, feedback vs approval, commit in progress vs verified commit, and Git-backed vs non-Git completion.

## Design principles

- One stable subject; only the status suffix changes.
- Evidence-backed transitions, not keyword guessing.
- Recommended defaults with full language and vocabulary customization.
- No rename on every prompt, tool call, build, or wait.
- Hooks are optional reminders, never autonomous semantic decision-makers.
- The skill still works when task-title controls are unavailable by proposing the exact title.

## Install

### Snapshot install

Use Codex's bundled skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo bahmetdev/codex-task-status \
  --path skills/codex-task-status
```

The installed snapshot is independent of this repository. The installer refuses an existing destination: to update, back up and move aside the exact installed skill directory before reinstalling. Keep personal customizations outside the installed package. There is no hidden automatic updater.

### Updateable checkout

Clone the repository and link the skill directory:

```bash
git clone https://github.com/bahmetdev/codex-task-status.git ~/Projects/codex-task-status
ln -s ~/Projects/codex-task-status/skills/codex-task-status ~/.codex/skills/codex-task-status
```

Update deliberately:

```bash
git -C ~/Projects/codex-task-status pull --ff-only
```

Codex discovers newly installed skills on a subsequent turn. If your current task does not see it, start a new turn or reopen the app.

## Configure

Installation makes the skill available; it does not force every task to invoke it. For persistent use, ask Codex to add the opt-in [`AGENTS.md snippet`](skills/codex-task-status/assets/agents-snippet.md) to your chosen project or global instructions. Review the change first. No hook or global configuration is installed automatically.

On first use, ask Codex to either:

- **Use recommended structure**, or
- **Customize structure**.

Customization can change the title format, subject language, whether subjects may contain spaces, state labels and meanings, Git/non-Git behavior, and recurring schedule notation. See [`references/configuration.md`](skills/codex-task-status/references/configuration.md).

Keep the chosen meanings and transitions in your own instructions or a linked policy file. Keep custom JSON outside this checkout so repository updates cannot overwrite it.

Example:

```text
Use $codex-task-status. Customize the structure for Ukrainian subjects,
square-bracket statuses, and no Git states.
```

## Validate a title

```bash
python3 skills/codex-task-status/scripts/validate_title.py "Crop (work)"
python3 skills/codex-task-status/scripts/validate_title.py \
  --config skills/codex-task-status/assets/task-status.example.json \
  "Release (pushed)"
```

The script validates syntax and configured vocabulary. It intentionally cannot decide whether a state is truthful.

## Optional hooks

Prompt templates for a start check and closeout check live in [`assets/prompts`](skills/codex-task-status/assets/prompts). They are not drop-in executable hook configuration because hook schemas vary across Codex surfaces and versions. Read [`references/hooks.md`](skills/codex-task-status/references/hooks.md) and integrate them only after checking the current runtime's official hook format.

The repository never edits global Codex configuration automatically.

## Development

Review instruction changes against the [workflow acceptance cases](tests/workflow-cases.md). These are a semantic review rubric; automated tests cover the deterministic validator only.

Run the dependency-free checks:

```bash
python3 skills/codex-task-status/scripts/test_validate_title.py
python3 -m py_compile skills/codex-task-status/scripts/*.py
```

## License

[MIT](LICENSE)
