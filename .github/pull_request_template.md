## Result

Summarize the final outcome for a reviewer who has not read the conversation history. Explain the problem addressed and the changes actually made.

## Grand Research Outline

- GRO section(s) written or rewritten: GRO-0#
- Status after this PR: REPORTED / REVISED / unchanged
- Version: N
- Downstream sections this puts in question:

The section states where that part of the research is going **and why**, in one paragraph. An agent never marks a section `VERIFIED` — only the researcher does. A PR that touches no part of the research outline changes nothing in `GRO.md`. See [GRO rules](../docs/gro.md).

## Issue and scope

- Owner/repo:
- Primary Issue:
- Parent/child Issue or dependency:
- Base / head:
- Final scope:
- Scope changes from the original plan:

Use `Refs #<number>` for partial work. Use `Closes #<number>` only in the final PR when all closure conditions of that Issue are satisfied.

## Epistemic delta

Describe how the knowledge/decision state changed because of this PR, not only how the text changed.

| Item/ID | Before | After | Evidence basis | Confidence/status |
|---|---|---|---|---|

Example statuses: SUPPORTED / INFERRED / ASSUMED / UNKNOWN / RETRACTED / MIXED.

### Unknowns that remain

- 

### Assumptions that remain

- 

### Decisions made or superseded

| DEC ID | Decision | Evidence/claim IDs | Supersedes | Impact |
|---|---|---|---|---|

## Outputs and acceptance evidence

| Issue success criterion | File/permalink/commit | Actual evidence | Status |
|---|---|---|---|

Status: PASS / FAIL / BLOCKED / NOT APPLICABLE.

## Evidence and provenance

Link relevant identifiers.

- Sources/reports (SRC):
- Studies (STUDY):
- Claims (CLM):
- Decisions (DEC):
- Reviews/findings (REV):
- Data records / parameters / runs (DAT/PRM/RUN):
- Brain statements added, changed, or superseded (typed IDs):
- Protocol/deviation IDs:
- Evidence unavailable or not verified:

Do not state “source supports claim” merely because a source is listed. The support relationship should be visible in the source note/claim ledger.

## Falsification and alternatives

For substantive changes to claims, theory, or method:

- Counterevidence inspected:
- Alternative explanations inspected:
- Boundary conditions:
- What could still overturn this decision:

Use NOT APPLICABLE with a reason for purely mechanical changes that do not affect academic claims.

## Verification performed

| Check | Version/HEAD checked | Method | Result | Limitation |
|---|---|---|---|---|

Separate:

- **mechanical verification** — links, schema, syntax, paths, build/automated checks;
- **epistemic verification** — claim–evidence fit, counterevidence, inferential boundaries;
- **academic judgment** — quality-gate or human/agent review within a defined scope.

Do not convert a mechanical PASS into a claim that the research is academically valid.

## Surgical-change check

- [ ] Every substantive change is traceable to the Issue, evidence, DEC, REV, or an acceptance criterion.
- [ ] No unrelated drive-by refactor/rewrite was performed.
- [ ] Any cleanup beyond the direct task is limited to orphan/inconsistency consequences created by the change itself, unless scope was explicitly expanded.

## Data, ethics, and integrity

- [ ] No sensitive data, credentials, signed consent forms, or raw participant data were added.
- [ ] No source, result, quotation, locator, human review, permission, or activity is claimed without evidence.
- [ ] Ethics/permission status is not assumed.
- [ ] Licensed material was not added without an appropriate basis.

## Review and corrective actions

Record reviewer/role (agent/self/human), version reviewed, findings, responses, and unresolved items:

| REV ID | Reviewer/role | Finding | Action | Status |
|---|---|---|---|---|

Agent review is not supervisor approval, journal peer review, or ethics-committee approval.

## Integration readiness

- [ ] Target owner/repo, base, and head are correct.
- [ ] Success criteria being closed are PASS.
- [ ] Verification appropriate to the change is complete and its limits are recorded.
- [ ] Issue snapshot/checkpoint reflects the current state.
- [ ] `brain.md` is synchronized (commit recorded) and `python scripts/validate_repository.py` passes.
- [ ] The GRO section is written or rewritten, the snapshot at the top of `GRO.md` is updated, and the section fits in one paragraph.
- [ ] No academic quality gate was upgraded merely because the PR is ready to merge.
- [ ] Merge authorization and branch protection/rulesets were checked.

## Planned closure

- Issue(s) to close:
- Issue(s)/work remaining open:
- Gate(s) affected or reopened:
- How the result will be verified on `main` after merge:

Record the merge commit and MERGED status only after they actually exist; do not write future outcomes as facts.
