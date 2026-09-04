# Recommended Status Model

The recommended title is `<Subject> (<state>)`.

`Subject` is one stable, concrete noun in the user's preferred language. A one-word subject is the recommended default because it scans well in a narrow sidebar. Users may configure phrases when their work requires them. A manual UI rename or explicit rename request also overrides the initial subject and defaults for that task, without requiring global reconfiguration. Preserve the exact chosen name, including spaces, language, and punctuation. Before every suffix update, reread the live title; never restore a cached subject. Change only a recognized trailing workflow suffix, not other parenthetical text. A subject-only rename leaves the work state unchanged.

## Working states

Initialize the subject and truthful state once during the first substantive turn,
including consultation. The app's automatic title is not evidence of a user
choice; an explicit name or evidenced UI rename is. After initialization, use
suffix-only transitions and preserve user renames. Resume, restart, compaction,
and later prompts do not restart naming. Preserve established titles when
their origin is uncertain; never infer ownership from wording alone.

| State | Use when | Do not use when |
| --- | --- | --- |
| `work` | Implementation, investigation, revision, or required agent-side validation is active. | The result is genuinely ready for user acceptance. |
| `qa` | Agent work is complete and user acceptance is a requested or required next gate. | Internal checks remain, or the request is complete without a user acceptance requirement. |
| `feedback` | Correct work depends on a missing decision, clarification, material, or visual judgment. | The action is already known and only permission is missing. |
| `approval` | A known action requires authorization that has not yet been granted for this scope. | Authorization already exists, routine QA acceptance, or ordinary clarification. |
| `blocked` | A real non-user-input condition prevents meaningful progress. | Work can continue independently or the task only awaits the user. |
| `paused` | The task was intentionally deferred. | A process happens to be idle. |

## Git states

| State | Evidence required |
| --- | --- |
| `committing` | The accepted scope is actively being inspected, staged, and committed. |
| `committed` | The matching local commit exists, was verified, and has no later relevant uncommitted change. |
| `pushing` | The verified local commit is actively being published to its configured remote. |
| `pushed` | The matching remote/upstream state was verified and no later relevant change exists. |

Do not jump directly from `work` to `committed` before the commit succeeds, or from `committed` to `pushed` before remote verification. Git states do not prove QA, CI, deployment, release, or delivery.

Remaining required work or a gate takes precedence over Git milestones. After a successful push, use `work` while required CI checks, deployment, or delivery remain agent-owned; use the applicable waiting state if progress is gated. A failed external dependency that prevents progress is `blocked`, even if the push succeeded. Report verified Git milestones separately.

If user acceptance is the active gate, keep `qa` even after a commit or push. Do not create that gate merely because the user could review the result. When an authorized Git-only phase begins, use `committing` or `pushing` directly; existing scope authorization is sufficient. Use `committed` or `pushed` for closeout only when no required work or gate remains.

## Completion without a required Git phase

Use `done` when a commit or publication is neither requested nor required and no QA, feedback, approval, blocker, pause, or user action remains. Examples include completed Mail, calendar, research, communication, read-only repository audits, and scoped local work whose outcome does not require a commit. This state does not claim Git publication. An existing user-approved naming policy takes precedence over these defaults.

## Recurring automations

For a healthy recurring task, a verified schedule may replace the state, for example:

- `Storage (08:00)`
- `News (10:00·19:00)`
- `Skills (Sun·09:00)`

During routine runs, keep the schedule stable. Use `attention` when user input or authorization is required, `blocked` for an external non-user-input blocker, and `paused` for intentional suspension. After resolution, restore the verified schedule from the existing automation. Never infer a schedule from an old title or create or change scheduling just to repair its suffix.

## Transition rules

- A substantive new or resumed request normally moves a stale terminal state back to `work`; an authorized commit-only or push-only request enters its corresponding in-progress Git state.
- A reported defect or requested revision moves `qa` back to `work`.
- `feedback` resolves to `work` once the missing input arrives.
- `approval` resolves to `work` when authorization arrives and execution begins.
- Change the suffix only on a meaningful evidence-backed transition.
- Never let a hook infer the state from keywords alone.
