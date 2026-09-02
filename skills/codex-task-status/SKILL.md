---
name: codex-task-status
description: Configure and maintain concise, evidence-based Codex task titles such as `Crop (work)` or `Release (pushed)`. Use when defining a task-title workflow, choosing or localizing statuses, classifying a task at start or closeout, validating a proposed title, or adding advisory title checks without automatic status guessing.
---

# Codex Task Status

Keep task titles scannable without turning title updates into activity noise.

## Start Here

First reuse an existing user-approved naming policy; do not repeat onboarding on every invocation. When first configuring this workflow, offer exactly two paths:

1. **Use recommended structure** — use `<Subject> (<state>)` and the semantics in [references/status-model.md](references/status-model.md).
2. **Customize structure** — ask only for choices that differ: title format, subject language/shape, status names, transition meanings, Git states, non-Git completion, and automation schedule notation. Use [references/configuration.md](references/configuration.md).

Do not brand either path with a person's name. Do not call one path “minimal.” Treat the recommended structure as a useful default, not a mandatory standard.

For persistent use, propose the small opt-in `assets/agents-snippet.md` for the user's chosen project or global instructions. Save custom label meanings and transitions there or in a linked policy file, not only in conversation memory. Installing this skill alone does not guarantee invocation on every turn. Confirm scope before editing instructions; do not modify other tasks or archived titles unless explicitly requested.

## Operate the Workflow

1. Generate a subject only when no user-chosen title exists. A user's UI rename or explicit rename request becomes the new canonical subject, overriding the initial name and default word count/language. Preserve the user's exact wording; do not revert or normalize it.
2. Classify the current state from evidence, not from the latest verb in the user's message.
3. Before each title write, read the current live title and preserve its subject, not a cached name. Replace only a recognized trailing status/schedule; keep other parenthetical text. If no suffix is recognized, retain the full title as the subject. If the live title cannot be read, skip the write rather than overwrite a user rename. A subject-only rename does not change the work state.
4. Use the available task-title control to apply the title. If no title control exists, propose the exact title instead of claiming it changed.
5. Verify the resulting title when a title control can read it back.
6. Before finalizing non-trivial work, classify once more and correct a stale suffix.

Do not rename after every message, tool call, test, build, wait, or routine status update. For agent-detected scope drift, recommend a separate task rather than autonomously renaming it; this does not restrict the user's choice to rename the current task.

## Apply Evidence Rules

- `work` means implementation, investigation, or required agent-side validation is active.
- `qa` means the result is ready for user acceptance; it does not mean internal tests are merely running.
- `feedback` means the correct next action depends on missing user input.
- `approval` means the intended action is known but explicit authorization is required.
- `blocked` is a real non-user-input blocker; `paused` is intentional deferral.
- `committing` and `pushing` are in-progress states. Use `committed` or `pushed` only after verifying the matching Git result.
- A commit or push does not imply QA acceptance, CI, deployment, or delivery.
- Use `done` only for completed non-repository work when no other gate remains.
- A later relevant change returns a terminal Git or completion state to `work`.

Read [references/status-model.md](references/status-model.md) before changing the recommended semantics or resolving an ambiguous transition.

## Validate Titles

Use the bundled validator when a config exists or when installing the workflow:

```bash
python3 scripts/validate_title.py "Crop (work)"
python3 scripts/validate_title.py --config path/to/task-status.json "Release (pushed)"
```

The validator checks syntax and configured vocabulary only. It cannot prove that a semantic state is truthful. A user's manual name may intentionally fail the default one-word pattern; preserve that title and adapt the task-specific validation policy if needed, never rename it to satisfy the validator.

## Add Optional Automation Safely

The workflow must remain useful without hooks. If the user requests automation, use [references/hooks.md](references/hooks.md) and the prompt templates in `assets/prompts/`.

Hooks may remind the active task to classify its state and verify a title update. They must not infer or write the semantic state, silently edit global configuration, block useful work, or overwrite a user's naming scheme.
