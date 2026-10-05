---
name: Research task
about: Bounded context for one unit of work: objective, epistemic state, evidence, scope, acceptance criteria, verification, decisions, and checkpoints.
title: ''
labels: ''
assignees: ''
---

## Current snapshot

- Work status: DRAFT
- Owner/repo:
- Branch / HEAD / PR:
- Related gate/stage (Stage 0–9, FG0–FG5):
- GRO section this work belongs to, and its status:
- Brain statements affected (typed IDs):
- Records touched (SRC/DAT/PRM/RUN):
- Latest checkpoint:
- Blocker:
- Next step:

## Objective

State the end condition this task should achieve. Avoid vague instructions such as “improve the chapter” or “continue the research.”

## Epistemic state

### KNOWN
Facts or information actually provided, observed, or already recorded.

### SUPPORTED
Claims currently supported by evidence that has been inspected. Link SRC/STUDY/CLM IDs or the evidence location.

### INFERRED
Researcher/agent inferences drawn from evidence. State the reasoning and limits.

### ASSUMED
Working assumptions that remain unverified.

### UNKNOWN
Information not yet known or available.

### DECISION NEEDED
Choices requiring researcher judgment, additional evidence, or external authorization.

## Evidence required

List the minimum evidence required before the claim or decision can be treated as verified.

| Evidence/ID | Why it is required | Location/source | Access/verification status |
|---|---|---|---|

## Scope

### Included
- 

### Out of scope
- 

Changes outside scope require an explicit reason and, when substantive, a recorded scope decision or a separate Issue.

## Outputs and canonical locations

| Output/decision | Canonical file/location | Related ID | Acceptance evidence |
|---|---|---|---|

## Success criteria

Write task-specific, inspectable conditions. Do not rely only on a generic checklist.

- [ ] 
- [ ] 
- [ ] 

## Verification plan

Explain how each success criterion will be checked and what the limits of that verification are.

| Criterion | Verification method | Expected evidence | Status |
|---|---|---|---|

Status: PENDING / PASS / FAIL / BLOCKED.

## Falsification / alternatives

For substantive claims or decisions:

- What evidence could falsify the candidate claim?
- Which alternative explanations should be inspected?
- Which boundary conditions could limit the conclusion?

Use NOT APPLICABLE with a reason when this section genuinely does not apply.

## Dependencies and authorization

- Parent/child Issue:
- Dependency:
- Approval/authorization actually required:
- Reviewer/responsible person if known:

Do not fabricate permission status, human review, or institutional approval.

## Decisions and scope changes

| DEC ID | Date | Decision/status | Evidence basis | Impact | Supersedes |
|---|---|---|---|---|---|

Preserve decision history; do not rewrite old decisions merely to make the project appear internally consistent.

## Checkpoints

Add a comment using `templates/session-checkpoint.md` at the end of a session, after a major decision change, when blocked, or during review transitions. Update the snapshot above so a new session can recover the state without reading the full conversation history.

## Closure conditions

An Issue that produces project files may be closed only when:

- [ ] applicable success criteria are PASS;
- [ ] decisions and evidence limits are recorded;
- [ ] canonical outputs exist at their final locations;
- [ ] the final PR has been reviewed and merged into `main`;
- [ ] the resulting `main` commit and Issue state have been verified;
- [ ] the closing checkpoint reflects the actual final state.

A coordination-only Issue with no file change may be closed with a reason and evidence; do not create an empty PR merely to satisfy process.
