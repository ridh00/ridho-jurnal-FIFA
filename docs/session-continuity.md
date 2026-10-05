# Continuing Work When AI Context Is Limited

Conversation history must not be the only place where project state is stored. Use three layers: a concise Issue snapshot, checkpoint comments as history, and files/commits as evidence.

This guide applies to RESEARCH mode. User-authorized upstream TEMPLATE maintenance may continue from files and Git history without a research Issue, according to the [Git workflow](git-workflow.md).

## Starting or continuing a session

1. Read `AGENTS.md`, `GRO.md` (the snapshot, the sections already verified, and any section still awaiting the researcher), `brain.md`, the project brief, research status, and the active owner/repo. Inspect the checkout so work does not drift into the upstream repository.
2. Read the active Issue: snapshot, scope, checklist/success criteria, latest checkpoint, dependencies, and decisions that remain in force.
3. Read linked PRs, changes after the checkpoint, open review findings, and the actual branch/commit state. Fetch/status may be needed to detect changes made by another session; do not force-checkout over local user work.
4. Open only the evidence and skills required for the active task. Read long Issues incrementally; retrieve older comments only when the snapshot and links are insufficient.
5. Summarize the current position and next step. If Issue body, comments, and Git disagree, compare timestamps and actual evidence, reconcile the Issue, then continue. Do not choose the version that is merely most convenient.
6. Execute the task within scope and save a checkpoint at meaningful transition points.

## Checkpoint content

Use the [checkpoint template](../templates/session-checkpoint.md). Include:

- Time, Issue, repo, branch, HEAD, and PR.
- What was completed since the previous checkpoint and the related artifact/commit.
- Decisions, reasons, and alternatives rejected.
- Actual checks, limitations, and unresolved review findings.
- Uncommitted/unpushed local changes and their safe location.
- Brain synchronization: statements added, changed, or superseded; records registered; the commit recorded in `brain.md`.
- GRO section written or rewritten, its status, and which sections are awaiting the researcher's verification.
- Blockers/dependencies and what or who is required.
- A concrete next action that a new session can execute immediately.
- Relevant authorization limits; never store secrets.

Prefer a summary that can be scanned quickly. Link to detail rather than duplicating long evidence. Readability is a goal, not permission to discard important decisions or evidence.

## Synchronization

The Issue stores delivery state and coordination. `research/status.md` stores research-stage and academic-gate state, with links to active Issues when relevant. Do not maintain competing manual delivery-status lists.

Scientific decisions remain in the decision/deviation logs and are linked from the Issue. Statements and their links remain in `brain.md`, which is synchronized at every checkpoint; the Issue points to the statement IDs it affects rather than restating them. Bibliography, claim ledger, manuscript, and analysis remain canonical in files rather than being copied wholesale into comments.

If GitHub is unavailable, save a temporary checkpoint in a safe, clearly identified local file and synchronize it to the Issue once GitHub is available, before beginning unrelated substantive work. Do not claim remote persistence merely because a local file exists.

## Handoff is complete when

A new session can answer: what is the objective, what has been done, what evidence supports the decisions, which version is current, what remains incomplete, and what action comes next—using the Issue and linked files rather than relying on conversation memory.
