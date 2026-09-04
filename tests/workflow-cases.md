# Workflow Acceptance Cases

Use these cases when editing the instructions. They are a review rubric, not a claim that the Python validator understands task semantics.

| Evidence | Expected behavior |
| --- | --- |
| A new feature request arrives in `Crop (committed)`. | Keep `Crop`, change to `work`. |
| Internal regression tests are still running. | Stay `work`, not `qa`. |
| Implementation and required agent checks are complete; user acceptance remains. | Use `qa`, even if a commit already exists. |
| The correct crop behavior depends on the user's aspect-ratio choice. | Use `feedback`. |
| Exact deletion targets are known but need permission. | Use `approval`, not `feedback`. |
| User asks to commit an accepted scope; no new commit exists yet. | Use `committing`, not `committed`. |
| The matching local commit is verified; publication is not required and no work or gate remains. | Use `committed`. |
| A push is running. | Use `pushing`, not `pushed`. |
| The matching remote commit is verified; no required work or acceptance gate remains. | Use `pushed`; do not imply CI or deployment. |
| A non-Git task is fully complete with no remaining gate. | Use `done`. |
| A read-only repository audit or requested local edit is complete; no commit or acceptance is required. | Use `done`; report any relevant uncommitted scope honestly. |
| A complete answer could be reviewed by the user, but acceptance was not requested or required. | Use `done`; do not create a QA gate. |
| Push succeeded, but required deployment or CI verification remains agent-owned. | Use `work`; report the verified push separately. |
| Push succeeded, but a failed external deployment service prevents meaningful progress. | Use `blocked`, not `pushed`. |
| Deployment was already authorized for this exact scope and can proceed. | Continue `work`; do not request authorization again. |
| User asks only to push an already verified matching commit. | Enter `pushing` directly, then verify the remote before `pushed`. |
| A recurring automation awaits required user input or authorization. | Use `attention`; restore its existing verified schedule when resolved. |
| A routine automation run has no intervention. | Keep the verified schedule title. |
| The user says thanks or asks for status. | Do not rename merely because another message arrived. |
| Title controls are unavailable. | Propose the exact title; do not claim a rename. |
| Custom labels were approved earlier. | Reuse their saved meanings; do not repeat onboarding. |
| The user changes `Crop (qa)` to `Photo Tools (qa)` in the UI, then requests a fix. | Read the live title and use `Photo Tools (work)`, never `Crop (work)`. |
| The user requests the subject `Мої фото` while the task is `qa`. | Use `Мої фото (qa)`; neither shorten/translate the name nor change the work state. |
| An established or explicitly user-named task has live title `Notes (Personal)` with no recognized workflow suffix. | Preserve the whole subject, for example `Notes (Personal) (work)`. |
| A manual title fails the default one-word validator. | Preserve the user's name; do not normalize it just to pass validation. |
| No fresh live title is available before a suffix write. | Skip the write and report the limitation; do not restore a remembered subject. |
| A new task has automatic title `Fix filter button appearance`; its first request asks for analysis under the one-word English policy. | Initialize once as `Filter (work)` during analysis, not only after implementation is requested. |
| A new task explicitly requests the name `My Filter Ideas`. | Preserve that name and add the truthful status; do not normalize to one word. |
| `Filter (qa)` resumes after restart or compaction with a revision request. | Use `Filter (work)`; never initialize the subject again. |
| An established multiword title has unknown origin and no naming history. | Preserve its live subject; do not treat missing history as proof of a new task. |
