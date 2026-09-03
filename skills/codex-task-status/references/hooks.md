# Optional Hook Integration

Hooks are advisory guardrails, not the owner of semantic state. The core workflow uses the opt-in AGENTS.md guidance; this package does not install executable hooks.

The [current Codex hook reference](https://learn.chatgpt.com/docs/hooks) supports command and MCP-tool handlers, but skips prompt and agent handlers. The Markdown files here are reminder text, not `type: prompt` handlers.

## Start check

Distinguish one-time initial naming from later suffix updates. A new task's
first substantive consultation also qualifies; do not wait for implementation.
Existing app-generated text is not proof of user naming. Preserve explicit
names and evidenced UI renames, and never reinitialize an established task.

Use the text from `assets/prompts/start-check.md` in the persistent instructions. An explicitly requested command-hook adapter may provide that reminder through `UserPromptSubmit` additional context. The active task, not the hook, decides whether the turn is substantive and whether its suffix is stale.

Do not trigger this check for acknowledgements, thanks, status-only questions, routine heartbeat runs, or messages that require no new work.

## Closeout check

Use the text from `assets/prompts/closeout-check.md` in the persistent instructions so the active task checks before its final response. A non-blocking `Stop` hook cannot guarantee another model action: the documented continuation mechanism is a blocking decision. Do not use that mechanism merely to police a title; it can create the very continuation loops this workflow avoids. Keep closeout agent-owned.

## Safety constraints

- Never parse the user's latest verb and write a status automatically.
- Never run a background renamer that races with the active task.
- Reminders must preserve the latest user-chosen subject, not the initial or cached name. Require a fresh live-title read before a suffix write; never enforce one-word or language defaults on a manual rename.
- Never block completion solely because title controls are unavailable.
- Never install or edit global hook configuration without explicit user authorization.
- Preserve an existing hook chain and ordering when the user authorizes integration.
- Make failures visible but non-fatal.
- Test hook prompts against at least: new work, QA handoff, feedback, approval, commit, push, non-Git completion, and a routine no-change turn.

Hook schemas differ between Codex surfaces and versions. Before wiring these prompts into a concrete runtime, consult that runtime's current official documentation or existing local hook schema. The files here are prompt templates, not drop-in executable hook configuration.
