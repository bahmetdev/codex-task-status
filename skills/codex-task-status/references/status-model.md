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
| `qa` | The user can now accept or reject the result. | Internal tests/builds are still incomplete or the agent still owns required verification. |
| `feedback` | Correct work depends on a missing decision, clarification, material, or visual judgment. | The action is already known and only permission is missing. |
| `approval` | A known destructive, risky, external, production, account, purchase, or otherwise gated action needs explicit authorization. | Routine QA acceptance or ordinary clarification. |
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

If user acceptance is the active gate, `qa` remains the truthful visible state even when a commit already exists. When the user then explicitly requests the accepted work to be committed, transition through `committing` to `committed`.

## Non-Git completion

Use `done` only when Git does not belong to the outcome and no QA, feedback, approval, blocker, pause, or user action remains. Examples can include a completed Mail, calendar, research, or communication task.

## Recurring automations

For a healthy recurring task, a verified schedule may replace the state, for example:

- `Storage (08:00)`
- `News (10:00·19:00)`
- `Skills (Sun·09:00)`

During routine runs, keep the schedule stable. Temporarily use `attention`, `blocked`, or `paused` only when the automation genuinely needs intervention, then restore the verified schedule.

## Transition rules

- A substantive new or resumed request normally moves a stale terminal state back to `work`.
- A reported defect or requested revision moves `qa` back to `work`.
- `feedback` resolves to `work` once the missing input arrives.
- `approval` resolves to `work` when authorization arrives and execution begins.
- Change the suffix only on a meaningful evidence-backed transition.
- Never let a hook infer the state from keywords alone.
