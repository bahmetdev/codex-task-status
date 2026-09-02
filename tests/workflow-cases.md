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
| The matching local commit is verified, but remote state is not. | Use `committed`. |
| A push is running. | Use `pushing`, not `pushed`. |
| The matching remote commit is verified and acceptance is complete. | Use `pushed`; do not imply CI or deployment. |
| A non-Git task is fully complete with no remaining gate. | Use `done`. |
| A routine automation run has no intervention. | Keep the verified schedule title. |
| The user says thanks or asks for status. | Do not rename merely because another message arrived. |
| Title controls are unavailable. | Propose the exact title; do not claim a rename. |
| Custom labels were approved earlier. | Reuse their saved meanings; do not repeat onboarding. |
