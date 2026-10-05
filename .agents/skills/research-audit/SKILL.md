---
name: research-audit
description: Audit research quality, stage readiness, manuscript consistency, and the defensibility of the research contribution using concrete evidence.
---

# Academic Audit and Examination Preparation

Read the [quality gates](../../../docs/quality-gates.md), [academic integrity rules](../../../docs/academic-integrity.md), the project brief, and the artifacts within the audit scope. Use the [gate review](../../../templates/gate-review.md). Auditing files is not the same as verifying every research activity.

## Procedure

1. Define the scope, version, available evidence, and what was not inspected. Do not make a project-wide judgment from one chapter.
2. Reconstruct the author’s argument before criticizing it. Inspect the chain: problem → questions → theory → evidence/design → results → contribution.
3. Test major claims against sources, counterevidence, and design limits. Distinguish a real reference from a reference that actually supports the sentence.
4. Separate conceptual, methodological, evidential, integrity, and editorial weaknesses. Do not inflate a style problem into a scientific failure.
5. Report findings with location, evidence, consequence for the conclusion, corrective action, and closure condition. Prioritize issues that affect validity or feasibility.
6. Record READY / REVISION REQUIRED / NOT ASSESSED / NOT APPLICABLE for each relevant gate. Do not mark a gate READY merely because the documents look complete when the underlying activity has not been evidenced.
7. Revisit earlier criticism and responses; close a finding only when the change actually resolves the issue.

## Examination or defense preparation

Develop examiner questions from real vulnerabilities: significance of the problem, contribution comparators, alternative theories, method fit, inferential basis, contradictory results, and limits of application. Practice answers should point to evidence locations; unresolved gaps must be acknowledged.

Agent review must not be described as supervisor review, independent human review, or ethics approval. For routine drafting work, report the corrections required without inventing new approval procedures.

## Place in the research flow

Gate assessments are organized by the flow gates of the [research flow](../../../docs/research-workflow.md): FG0 bundles G0; FG1 bundles G1–G3; FG2 bundles G4–G5; FG3 bundles G6; FG4 bundles G7. A flow gate takes the most conservative status among its gates.

- Before any flow-gate assessment, inspect `GRO.md`: the sections belonging to that gate, whether the researcher has verified them, and their revision history. A section still `REPORTED` means the researcher has not agreed to that direction; an unexplained change of direction between versions is recorded as a finding rather than corrected quietly.
- Then inspect `brain.md`: the coherence check rows, the commit recorded as synchronized, and the output of `python scripts/coherence_report.py`. Dangling or orphan identifiers are evidence that the chain is not traceable; record them as findings.
- FG1: verify the chain Phenomenon → Theory → Gap → Novelty → RQ is connected and relevant, and that research questions trace to named gaps.
- FG2: verify the method decision record is `APPROVED`, every parameter has a justification and source, and the reporting standard is registered as a `PRM`.
- FG3: verify every RQ is answered by findings that cite `DAT` or `RUN`.
- FG4: verify the reporting and abstract checklists are complete, claim verbs respect the boundaries of inference, the title and abstract meet the outlet's requirements and the design's limits, every number in the abstract matches its run, promised implications are delivered, and every outline paragraph maps to statements.
- FG5: verify every reviewer point is closed with evidence or declined with a recorded reason, every gate a point reopened has a new assessment rather than an assumption, the response letter covers every point with a checkable location, and claim verbs were re-audited — revisions frequently strengthen claims.

## Execution discipline

Apply the cross-skill principles in `research-rigor`: do not silently resolve uncertainty, use the minimum sufficient complexity, keep changes within task scope, and verify outcomes against explicit acceptance criteria. For high-impact claims or decisions, inspect counterevidence and alternative explanations before strengthening the conclusion.

## Gate diagnostics

When assessing a gate, use the critical-failure criteria and reopen triggers in the [quality gates](../../../docs/quality-gates.md). A gate that was previously READY must be reopened when the basis of the decision materially changes; do not overwrite the earlier assessment.
