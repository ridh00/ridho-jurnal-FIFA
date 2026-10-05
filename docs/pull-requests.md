# Pull Requests, Review, and Final Integration

In a RESEARCH project, every file change entering `main` must go through a Pull Request. The PR is the reviewable integration package; the Issue stores the requirement and bounded context. A pushed branch is not the same as an integrated result. Upstream TEMPLATE maintenance follows the exception in the [Git workflow](git-workflow.md).

## Creating a PR

- Create a branch named `issue-<number>-<summary>` and use commits that reference the Issue. Verify owner/repo and base/head before opening the PR.
- Open a draft PR once there is meaningful, reviewable work. Use the [PR template](../.github/pull_request_template.md).
- When the PR advances or changes a part of the research outline, write or rewrite the matching [GRO](gro.md) section in the same PR and mark it `REPORTED`; record the PR in its version line and, for a rewrite, add a row to the revision history naming the downstream sections it puts in question. Mechanical PRs change nothing in `GRO.md`.
- Include the problem, before/after state, final scope, canonical files, evidence, decision changes, actual checks, limitations, and acceptance evidence.
- One PR may complete only part of an Issue. Use `Refs #<number>` when the entire Issue is not yet complete.
- Use `Closes #<number>` only in the final PR that satisfies all closure conditions of the related Issue. Do not close a parent Issue that still has required child work.
- The final base is `main` or another explicitly verified default branch. Do not put a closing keyword only in a comment and assume the Issue will close automatically.

GitHub interprets closing keywords in a PR description targeting the default branch; merging that PR may close the linked Issue. Always verify the actual state after merge. See the [GitHub documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

## Review before merge

1. Compare the output with the Issue and its success criteria. If scope changed, update both Issue and PR description explicitly.
2. Inspect the changed content, source/claim limits, manuscript consistency, sensitive-data risk, and affected rules.
3. Run checks appropriate to the change: links/frontmatter for docs and skills; citation audit for literature; analytic validation for results; rendering for exports.
4. Record reviewer/role, the HEAD version inspected, findings, and corrective actions. Self/agent review must not be represented as independent human or supervisor review.
5. Resolve findings that affect validity, integrity, scope, or security. New substantive changes after review require review proportional to their impact.
6. Mark a draft PR ready only when no required work remains. Save a READY_TO_MERGE checkpoint.

## Merge and authorization

Merge only after actual review, satisfied acceptance criteria, and within the authorization that applies. If the user authorized completion through `main`, use the PR path and do not repeatedly ask for permission after every routine step. If the user requested a draft only, asked to wait for a supervisor, or imposed a special approval boundary, respect it.

A skill or checkbox cannot create new authorization. Do not infer ethics or supervisor approval from a PR label. Do not use admin bypass to evade required review/protection.

Use a merge method permitted by the repository. Record the actual resulting commit; do not assume the branch commit SHA equals the squash-merge commit. Resolve conflicts on the branch and rerun checks affected by the conflict resolution.

## After merge

- Confirm the PR state is MERGED and the resulting commit exists on `main`.
- Confirm the final Issue is closed only if its closure conditions are actually satisfied; inspect parent/child Issues and follow-up tasks.
- Add a closing comment summarizing the outcome, PR/merge commit, validation, limitations, and follow-up links.
- Synchronize local checkouts safely. Do not mark an academic gate READY merely because the PR merged.
- An Issue with a partial PR remains open until all agreed outputs are complete.

## Written rules versus server enforcement

Markdown rules guide agent behavior; they do not block a push by themselves. Branch protection/rulesets are a separate enforcement layer and depend on repository settings and account features. Record only protections that were actually inspected; do not claim protection is active merely because this file says it should be.

If protection exists, follow it and do not weaken it. New protection settings should preserve existing rules and reflect the reviewers actually available; self-approval should not be represented as independent review.
