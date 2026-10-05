# Quality and Readiness Gates

A quality gate is an evidence-based decision about a **defined scope**, not a count of completed files or a delivery status. Every research gate starts as **NOT ASSESSED**.

Statuses:

- `NOT ASSESSED`
- `REVISION REQUIRED`
- `READY`
- `NOT APPLICABLE` — requires a design-based reason

Every assessment records the commit/version, evidence inspected, evidence not inspected, assessor and role, any critical failure, closure conditions, and reopen triggers. Use the [gate review template](../templates/gate-review.md).

**A PR PASS or repository-check PASS does not make an academic gate READY.**

## Flow gates

The [research flow](research-workflow.md) bundles the quality gates into five hard stops. A flow gate takes the most conservative status among the gates it bundles, and reopening any bundled gate reopens the flow gate and every stage after it.

| Flow gate | Bundles | Hard stop it enforces |
|---|---|---|
| FG0 Context | G0 | no framing statement treated as decided |
| FG1 Framing | G1, G2, G3 | no method selection, instrument design, or data collection |
| FG2 Method | G4, G5 | no data collection or analysis |
| FG3 Findings | G6 | no manuscript outline, no results prose |
| FG4 Manuscript | G7 | no submission, no export declared ready |
| FG5 Revision | the gates a reviewer point reopens, plus G7 | no resubmission until every point is closed with evidence or declined with a reason |

Before assessing a flow gate, inspect `GRO.md` — the sections belonging to that gate, whether the researcher has verified them, and their revision history: a section still `REPORTED` means the researcher has not agreed to that direction, and an unexplained change of destination between versions is recorded as a finding. Then inspect the coherence check in `brain.md` and the coherence report; a dangling or orphan identifier is evidence that the chain is not traceable. At FG2 the reporting standard must be registered as a parameter set; at FG4 its checklist — and the abstract checklist where the design has one — must be complete. At FG5, inspect the [revision table](../templates/revision-table.md): a point routed to design or framing reopens its gate, and closing it requires a new assessment rather than an edit.

## Gate matrix

| Gate | Minimum evidence for READY | Critical failure / REVISION REQUIRED | Reopen trigger |
|---|---|---|---|
| **G0 Context** | Project brief distinguishes verified information, unknowns, constraints, mandate, and open decisions; relevant institutional requirements are available | Core purpose, access, institutional rules, or mandate remain assumed even though a decision depends on them | institutional/guideline change, data-access change, project-purpose change, deadline/resource change, or mandate change |
| **G1 Problem** | Empirical/conceptual problem is clear; RQ, unit of analysis, context, and significance are aligned and answerable | broad topic only; normative problem without an object of analysis; RQ contains the answer; unclear unit of analysis; question cannot be answered with realistic evidence | change in RQ, unit of analysis, phenomenon, scope, or evidence mapping that undermines the framing |
| **G2 Protocol & evidence** | Review type is justified; search/screening trail, source notes, appraisal, and claim provenance match the claimed coverage | core sources not read; selection untraceable; reports counted as separate studies; appraisal inappropriate to design; “systematic/comprehensive” claim without supporting process | change in RQ/protocol, new database/access, new core source, correction/retraction, or material deduplication finding |
| **G3 Theory & contribution** | Closest studies, mechanisms/arguments, functional use of theory, counterevidence, alternatives, boundary conditions, and contribution limits are mapped | novelty based only on location/variable combination/method; no closest-study comparison; decorative theory; ignored counterevidence; unsupported “first” claim | new close prior study, construct/RQ change, important correction/retraction, or empirical result that changes the contribution |
| **G4 Design** | RQ–data–design–analysis are coherent; inferential target, assumptions, sampling/corpus, measurement, feasibility, ethics, and limitations are explicit | method chosen because it is popular; evidence cannot support the claim; causal language without identification; unjustified estimator/model; unrealistic access/feasibility | change in RQ, data source, sample/corpus, instrument, analysis target, assumption, or feasibility |
| **G5 Execution readiness** | Ethics/permission status and access match the planned activity; procedures/instruments, pilot when relevant, governance, capacity, and analysis plan are adequate | required approval absent; protocol treated as equivalent to execution; consent/access assumed; unsafe data storage | change in procedure, population, location, data sensitivity, instrument, permission, or governance |
| **G6 Results & interpretation** | Analysis is traceable; preprocessing/parameters/deviations are recorded; uncertainty, null/contradictory results, sensitivity, and inferential limits are reported | fabricated/selectively reported results; unexplained exclusion; hidden HARKing; claim exceeds design; contradictory result removed | new data/analysis, code correction, new exclusion/sensitivity check, protocol deviation, or discovery that changes interpretation |
| **G7 Manuscript & examination** | problem→RQ→theory→design→results→contribution are coherent; claim–evidence paths are traceable; citations, tables/figures, references, responses to critique, and exports are checked; the reporting and abstract checklists are complete; the title, abstract, and keywords meet the outlet's requirements and the design's boundaries of inference | major claim without evidence; cross-chapter inconsistency; hidden substantive TODO; citation does not support sentence; unperformed result/approval written as fact | substantive change to G1–G6, major reviewer finding, citation correction/retraction, or material institutional-format change |

## Conditional criteria

### Quantitative

When relevant, inspect: target estimand/population, sampling, sample size based on precision/power/simulation, measurement validity/reliability, missingness, clustering, weights, confounding, model assumptions, multiplicity, robustness/sensitivity, and uncertainty.

### SEM / latent-variable models

Distinguish measurement and structural models, reflective/formative specification when relevant, identification, estimator, sample adequacy, model fit, alternative models, and the limits of causal interpretation.

### Qualitative

Inspect fit with the research tradition, case selection, positionality/reflexivity, corpus provenance, interpretive process, negative/deviant cases, context, and adequacy according to the approach. Do not impose saturation, member checking, or intercoder agreement on every qualitative tradition.

### Mixed methods

Inspect the reason for integration, sequence/priority, sample relationship, integration points, joint display when relevant, and how discrepant results affect the meta-inference.

### Conceptual / archival

Inspect corpus selection, provenance, authenticity/context, rules of interpretation, alternative readings, and access limitations.

### Review without participants

Determine whether any ethics or data-permission requirement still applies. Do not fabricate approval or assume every review study requires participant procedures.

## Decision rule

Use the most conservative status supported by the evidence within the assessed scope:

- **READY:** all applicable minimum evidence was inspected, no critical failure remains open, and limitations are recorded.
- **REVISION REQUIRED:** a critical failure or deficiency could materially affect validity or defensibility.
- **NOT ASSESSED:** scope/evidence are insufficient for an assessment.
- **NOT APPLICABLE:** the gate or criterion does not apply because of the design, with an explicit reason.

Do not use an aggregate score to hide a critical failure.

## Scope and reviewer identity

Every gate review records what was **not inspected**. An agent assessment is a judgment about the artifacts actually read, not approval from a supervisor, ethics committee, journal reviewer, or institution.

If a human reviewer makes a decision, record the identity/role as appropriate to the project but do not infer independence or authority that was not explicitly stated.

## Reopening

A gate that was previously READY must be reopened when a material trigger changes the basis of the decision. Reopening does not imply the earlier work was wrong; it means the evidence basis has changed.

Example:

```text
G3 = READY
    ↓
new close prior study discovered
    ↓
G3 = REASSESSMENT REQUIRED
    ↓
review evidence + contribution
    ↓
READY / REVISION REQUIRED
```

Do not erase gate history. Save the new assessment as a new review and link the earlier assessment.
