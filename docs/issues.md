# Using Issues as Project Memory

In a RESEARCH project, a GitHub Issue must be selected or created before substantive work. The purpose is to let the researcher and a future AI session understand and continue the task without reading the full previous conversation. Upstream TEMPLATE maintenance follows the exception defined in the [Git workflow](git-workflow.md).

## Unit of work

One Issue should represent one independently reviewable output or decision.

Examples:

- “Verify source support for the central background claim.”
- “Specify the review protocol from the research question.”
- “Evaluate whether the proposed moderator is theoretically necessary.”

For a large stage, create a parent Issue with the overall objective and child Issues for independently reviewable outputs. Each child has its own scope, dependencies, and acceptance criteria. Link them in both directions. The parent remains open until all required outputs are integrated.

Do not create a new Issue for every small question inside the same task. Split an Issue when the scope has become multiple independently reviewable outputs or when the bounded context can no longer be summarized reliably.

## Required body content

Use the [research task template](../.github/ISSUE_TEMPLATE/research-task.md).

A strong Issue includes:

1. **Current snapshot:** work status, repository, branch, commit/checkpoint, PR, the GRO section this work belongs to and its status, blocker, and one concrete next step.
2. **Objective:** the end state to achieve and why it matters.
3. **Epistemic state:** KNOWN, SUPPORTED, INFERRED, ASSUMED, UNKNOWN, and DECISION NEEDED.
4. **Evidence required:** source/claim IDs, documents, locators, and access limits that must be checked.
5. **Scope:** what is included and what is explicitly outside the task.
6. **Outputs:** expected files/decisions and their canonical locations.
7. **Success criteria:** inspectable conditions that distinguish a designed protocol from an activity that was actually executed.
8. **Verification plan:** how each success criterion will be checked and what the limits of that check are.
9. **Falsification/alternatives:** when relevant, what could contradict the candidate claim or decision.
10. **Dependencies/authorization:** parent/child Issues, blockers, reviewer roles, and approvals actually required.
11. **Decision history:** DEC links and superseding decisions.
12. **Closure conditions:** final PR or an explicit reason for coordination-only closure without a file change.

For reviewed evidence, prefer commit permalinks when a specific version matters and branch links for active work. Never treat a page number, search count, or access status as verified merely because it was written in an Issue.

## Work status

GitHub has open/closed state. Use the following project work statuses in the Issue snapshot, with labels as an optional mirror:

| Work status | Meaning |
|---|---|
| DRAFT | Context or success criteria are insufficient to begin |
| READY | Task is clear and initial dependencies are satisfied |
| IN_PROGRESS | Work is active; branch/checkpoint is recorded |
| BLOCKED | A real dependency prevents progress; record what is needed |
| IN_REVIEW | Draft/final PR is being reviewed |
| READY_TO_MERGE | Verification is complete and merge authorization/protection has been checked |
| DONE | Output is integrated and closure is verified |
| CANCELLED | Task was cancelled with a reason; this is not academic completion |

Do not mark DONE after drafting, pushing a branch, or opening a PR. A label is not evidence that an activity occurred.

## Session-resistant updates

Update the snapshot in the Issue body and add a [checkpoint](../templates/session-checkpoint.md) comment:

- at the end of a session;
- before a known context compaction/transition;
- after a major decision;
- when blocked;
- before and after review/merge transitions.

Save progress before the context window feels critical; do not assume an agent will always receive a warning.

A checkpoint records what changed since the previous checkpoint, decisions and reasons, evidence/commits, what remains unchecked, and the next action. Do not flood the Issue with raw tool logs.

## Closing and reopening

For an output-producing Issue, use a closing keyword only in a PR that actually satisfies the full closure conditions. If required work remains inside the Issue scope, keep it open. Moving work to a child Issue does not automatically make the old scope complete; document the scope change explicitly.

If an error is found after closure, reopen the Issue or create a linked corrective Issue with evidence and the impact on gates/manuscript. Do not delete critical comments or rewrite history.
