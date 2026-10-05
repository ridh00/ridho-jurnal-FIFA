# Issue → Branch → PR → Review → Merge

**In a RESEARCH project, every substantive task requires a GitHub Issue and every file change entering `main` must go through an inspected Pull Request.** This includes research, writing, review, documentation, skills, and small fixes inside the research project.

**In the upstream TEMPLATE repository, builder maintenance explicitly requested by the user may be performed, inspected, committed, and pushed without a research Issue/PR.** The mode is recorded in the project brief. This exception does not apply to copied repositories being used for actual research. Do not change modes to bypass the research rules.

The remainder of this document describes the RESEARCH workflow.

## What each layer is for

| Layer | Canonical purpose |
|---|---|
| Issue | Objective, bounded context, acceptance criteria, decisions, dependencies, checkpoints, and next steps |
| Branch/commit | Recoverable versions of work in progress |
| PR | Final change set, verification evidence, review discussion, and integration into `main` |
| GRO section | One paragraph per part of the research outline: where that part is going and why, for the researcher to verify |
| Project files | Canonical manuscript, structured evidence, protocols, decisions, and research records |
| AI conversation | Temporary interaction; important decisions must be transferred into Issues/files |

An Issue is cross-session working memory. It is not a place to store entire PDFs, participant data, or full conversation transcripts. Keep the latest state near the top, preserve decision history through comments/logs, and link to the relevant artifacts.

## Required sequence

1. **Confirm the repository.** Inspect the Git origin and canonical GitHub owner/repo. Do not write to the upstream builder by mistake. For GitHub operations, use an explicit owner/repo. After a rename, verify redirects and the actual target before writing.
2. **Find or create the Issue.** Read the body, latest checkpoint, relevant comments, and linked PRs. Do not duplicate work already covered. Define scope and acceptance criteria before substantive execution.
3. **Create or continue a branch from current `main`:** `issue-<number>-<summary>`. If temporary work depends on another branch, document the temporary base and retarget the final integration to `main`.
4. **Work within scope.** Include `Refs #<number>` in commits when appropriate. Save checkpoints after major decisions, at the end of a session, when blocked, and before a context transition. Synchronize `brain.md` with every checkpoint: statements added or changed, records registered, commit recorded.
5. **Open a draft PR once there is reviewable work.** Link the Issue and keep the PR description synchronized with the actual state. Empty PRs are unnecessary. When the PR advances or changes a part of the research outline, write or rewrite the matching [GRO](gro.md) section in the same PR, record the PR in its version line, and mark it `REPORTED`. A PR that touches no part of the outline changes nothing in `GRO.md`.
6. **Inspect and revise.** Verify acceptance criteria, relevant academic checks, links, and data safety. Distinguish agent review, human review, and institutional approval.
7. **Merge through the PR within the user’s authorization.** Authorization to complete the work through `main` includes merging after verification; a request for a draft only or a request to wait for review does not. Respect user-specified approval boundaries and server-side protections.
8. **Verify the actual result.** Confirm the PR is MERGED, the resulting commit exists on `main`, and the Issue state matches the acceptance criteria. Add a closing summary to the Issue and synchronize local checkouts without overwriting user changes.

Creating Issues, checkpoints, and draft PRs is part of the requested workflow; do not ask for repeated permission at every step. Participant contact, external messages, and institution-facing actions still require the appropriate authorization.

## Boundaries and special cases

- Clarifying/status questions within ongoing work stay on the active Issue and do not require a new Issue. A genuinely new project decision or independently reviewable output should have its own Issue.
- Reading/review work that produces a project artifact should be saved as a memo or other canonical file and integrated through a PR. If an Issue is coordination-only and produces no file change, close it with evidence and a reason; do not create a fake PR.
- If GitHub is unavailable, keep a safe local checkpoint marked **NOT YET SYNCED**. Do not claim that an Issue or PR exists, do not begin unrelated substantive work without the required Issue, and do not bypass PR integration.
- Do not rewrite old decisions merely to make project history appear consistent. Record a superseding decision, its reason, and its impact.
- Creating a new research repository may copy the builder snapshot and set RESEARCH mode during provisioning. After provisioning, project customization and research outputs follow the required Issue/PR workflow.
- Do not force-push, erase history, or use admin bypass to evade required review.

Detailed guides: [Issues](issues.md), [session continuity](session-continuity.md), [PRs and merge](pull-requests.md).

## Definition of done

For a file-producing task: Issue acceptance criteria are satisfied, actual review is recorded, the PR is merged into `main`, the result is verified, and the Issue closure contains evidence. Delivery completion does not mean an academic gate has passed or that fieldwork/analysis has occurred.
