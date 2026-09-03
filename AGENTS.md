# Repository maintenance

- Keep this public skill configurable and free of machine-specific paths and private data.
- For maintainer-requested updates to this repository, completion includes focused validation, a scoped commit, and pushing the approved changes to the configured GitHub remote unless the maintainer explicitly asks to keep them local.
- Preserve unrelated changes. Never force-push or publish unrelated commits; inspect the outgoing range and stop on divergence or an unclear publication scope.
- Verify the remote branch SHA after pushing and distinguish publication from local-only completion. Do not claim GitHub is current after a failed push.
- Reuse passing checks when their relevant inputs are unchanged. For instruction changes, review tests/workflow-cases.md; for validator changes, run python3 skills/codex-task-status/scripts/test_validate_title.py.
- These are source-repository maintenance rules, not permissions for users who install the skill to publish their own work. Do not put this publication requirement in the installed skill's task-status semantics.
