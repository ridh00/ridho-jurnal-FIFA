# Revision Table

One table per revision round. Built from the reviewer comments as they were received, before any change is made. See the [revision rules](../docs/revision.md). Working location: `reviews/YYYY-MM-DD-revision-round-N.md`.

## Round

- Round number: NOT YET FILLED
- Source: journal reviewers / editor / supervisor / examiner (name the outlet or person)
- Decision received: major revision / minor revision / revise and resubmit / other
- Date received / deadline: NOT YET FILLED
- Manuscript version reviewed (commit or export): NOT YET FILLED
- Issue tracking this round: NOT YET FILLED
- Editor's letter takes precedence over a conflicting reviewer point: NOT YET CHECKED

## 1. Points

One row per discrete demand. A single reviewer paragraph usually contains several; each closes on its own evidence. Quote the comment verbatim — never trimmed into something easier to answer.

| `REV` | Reviewer / their numbering | Comment, verbatim | Concern behind it | Confirmed or inferred | Layer | Decision | Priority |
|---|---|---|---|---|---|---|---|

**Layer:** claim / design / evidence / framing / structure / reporting / wording. A point routed to **design** or **framing** reopens a flow gate and returns to that stage before the manuscript is touched.

**Decision:** ACCEPT / ACCEPT WITH MODIFICATION / DECLINE WITH REASON.

**Priority:** critical (integrity, permission, validity, or inference may fail) / major (argument, method, evidence, or consistency) / editorial (does not change the conclusion).

An inferred concern that drives a substantive change is flagged for the researcher before the change is made: NOT YET FILLED.

## 2. Changes and their justification

The reason each change answers the concern — this is what the response letter is built from.

| `REV` | Change made | Why this answers the concern | Location in the manuscript | Statements changed or superseded | Records added (`SRC`, `DAT`, `PRM`, `RUN`) | Evidence of the change (commit or PR) |
|---|---|---|---|---|---|---|

## 3. Gates reopened

A point routed to claim, design, evidence, or framing changes the basis of an earlier assessment. Record the reassessment; do not overwrite the earlier gate review.

| `REV` | Gate or flow gate | Why it reopens | New assessment (`REV` of the gate review) | Status |
|---|---|---|---|---|

## 4. GRO sections affected

A change to a part of the research outline rewrites its GRO section, raises the version, and records the response in the revision history.

| `REV` | GRO section | New version | Re-reported to the researcher | Verified |
|---|---|---|---|---|

## 5. Conflicts and unresolved points

Where two reviewers ask for opposite changes, or a point cannot be satisfied within the design, resources, or ethics of the study.

| `REV` | Conflict or obstacle | How it was resolved, or why it could not be | Recorded in the letter |
|---|---|---|---|

## 6. Closure

| `REV` | Status | Verified by / date | How closure was verified |
|---|---|---|---|

**Status:** OPEN / IN PROGRESS / REVISED NOT YET VERIFIED / CLOSED / NOT IMPLEMENTED WITH REASON.

Do not close a point because the wording was polished. A criticism of substance is closed only by a change of substance.

## FG5 check

- [ ] Every point is CLOSED or NOT IMPLEMENTED WITH REASON
- [ ] Every substantive change traces to a statement, a record, or a gate reassessment
- [ ] Every reopened gate has a new assessment rather than an assumption
- [ ] The response letter covers every point with a verifiable location
- [ ] Reporting and abstract checklists still hold after the changes
- [ ] Claim verbs re-audited — revisions frequently strengthen claims
- [ ] Deviation log updated where an already specified protocol changed

FG5 status: NOT ASSESSED. Passing it means the revision is ready to resubmit; it is not a judgment by the editor or the reviewers.
