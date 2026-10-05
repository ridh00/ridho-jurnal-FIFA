# Synthetic Issue — Qualify Causal Wording in CLM-SYN-001

> **SYNTHETIC EXAMPLE.** This is not an active GitHub Issue and is not evidence of real research.

## Current snapshot

- Work status: READY FOR REVIEW
- Owner/repo: synthetic/example
- Branch / HEAD / PR: issue-12-qualify-role-clarity / synthetic
- Related gate/stage: G3 and G7
- Latest checkpoint: after verification
- Blocker: none
- Next step: review the diff, then merge

## Objective

Determine whether the causal wording in CLM-SYN-001 can be defended. If not, reduce the claim to a form supported by the available synthetic evidence.

## Epistemic state

### KNOWN

- The manuscript says “coordination routines increase role clarity.”
- SRC-SYN-001 represents a synthetic observational study.

### SUPPORTED

- SRC-SYN-001 supports only an association in this example.

### INFERRED

- The causal wording exceeds what the synthetic observational design can identify.

### ASSUMED

- No experiment or other causal-identification design exists elsewhere in the synthetic corpus.

### UNKNOWN

- Whether the causal mechanism is true in the real world.

### DECISION NEEDED

- Retain the causal wording or qualify it to associational wording.

## Evidence required

| Evidence/ID | Why required | Location/source | Status |
|---|---|---|---|
| SRC-SYN-001 | Inspect design and findings | source-note-SRC-SYN-001.md | FULL_TEXT synthetic |
| CLM-SYN-001 | Inspect evidence–claim relationship | claim-ledger.md | VERIFIED synthetic |

## Scope

### Included

- CLM-SYN-001
- one manuscript paragraph
- the related decision record

### Out of scope

- adding constructs
- redesigning the study
- rewriting the entire chapter

## Success criteria

- [x] Design represented in SRC-SYN-001 inspected.
- [x] Counterevidence to the causal wording recorded.
- [x] Claim decision recorded.
- [x] Only the affected paragraph revised.
- [x] Academic gate not upgraded automatically.

## Verification plan

| Criterion | Method | Expected evidence | Status |
|---|---|---|---|
| Wording matches design | Compare source note ↔ claim | causal claim removed | PASS |
| Scope remains surgical | Inspect changed artifacts | one paragraph + ledger/decision | PASS |
| Gate remains separate | Inspect gate review | G3 remains REVISION REQUIRED | PASS |

## Falsification / alternatives

The causal wording could be retained only if additional evidence actually identified a causal effect. That evidence does not exist in this synthetic example.

## Closure

Delivery can be completed after the synthetic PR is merged. Academic readiness remains a separate assessment.
