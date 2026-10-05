---
name: research-rigor
description: Cross-skill guardrails for reducing hidden assumptions, unnecessary complexity, scope drift, unverified claims, and one-sided confirmation in AI-assisted research.
license: MIT
---

# Research Rigor

This meta-skill governs how an agent works across all research stages. It adapts four execution principles from [Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills) to research: think before claiming, prefer minimum sufficient complexity, make surgical changes, and work toward verifiable success criteria.

Apply these principles alongside the relevant academic skill. Use them proportionally for routine tasks; apply them fully for substantive, ambiguous, difficult-to-reverse, or inference-sensitive decisions.

## 1. Think Before Claiming

Do not silently resolve epistemic uncertainty.

Before making a substantive claim or decision, distinguish:

- **KNOWN** — information actually provided or observed.
- **SUPPORTED** — a claim supported by evidence that has been inspected.
- **INFERRED** — a conclusion drawn from evidence, with its reasoning and limits.
- **ASSUMED** — a working assumption that remains unverified.
- **UNKNOWN** — information not yet known or accessible.
- **DECISION NEEDED** — a choice requiring researcher judgment or additional evidence.

If several interpretations are plausible and the choice affects the result, surface the alternatives. Do not convert a lack of search results into a research gap, correlation into causation, a citation into support for a claim, or a plausible model into a tested theory.

## 2. Parsimony First

Use the minimum conceptual and methodological complexity required to answer the research question.

Do not add theories, constructs, variables, mediators, moderators, methods, robustness checks, or abstraction layers merely to make the study appear sophisticated. Every element must have an explainable function.

For every new element, ask:

1. Is this necessary to answer the research question?
2. Does it improve explanatory power, validity, or the ability to distinguish alternative explanations?
3. Are the available evidence and resources sufficient to support it?
4. Could a simpler design yield the same or a more defensible inference?

Complexity is justified when required by the question and evidence, not as a signal of doctoral quality.

## 3. Surgical Research Changes

Change only what is required to meet the task objective. Do not perform unrelated “while we are here” improvements.

Every substantive change must be traceable to at least one of:

- the Issue objective or acceptance criterion;
- newly verified evidence;
- a recorded research decision;
- a review/audit finding;
- an inconsistency that directly blocks the task.

Do not change research questions, theories, methods, construct definitions, samples, or other claims merely because an adjacent improvement seems attractive. If the requested change creates an orphan artifact or direct inconsistency, fix only the consequences introduced by that change.

Simple test: every important change should have a reason visible in the diff, Issue, decision log, review finding, or evidence trail.

## 4. Goal-Driven Research

Convert broad instructions into testable goals before making changes.

For nontrivial work, define:

1. **Objective** — the desired end state.
2. **Scope** — what may and may not change.
3. **Evidence required** — the minimum evidence needed.
4. **Success criteria** — inspectable conditions for completion.
5. **Verification** — how those conditions will be checked.

Example:

```text
Objective:
Determine whether the candidate theoretical contribution
can be defended.

Success criteria:
[ ] Core constructs are defined from verified sources.
[ ] Closest prior studies are compared.
[ ] Contradictory evidence is recorded.
[ ] Alternative explanations are inspected.
[ ] Retain / narrow / defer / reject decision is recorded.
```

If the criteria cannot be satisfied because data, sources, permissions, or researcher decisions are unavailable, mark the task **BLOCKED** or **UNVERIFIED**. Do not fill the gap with assumptions.

## 5. Falsification Before Affirmation

For important claims, do not search only for support.

Default sequence:

1. formulate the candidate claim narrowly;
2. search for supporting evidence;
3. deliberately search for counterevidence;
4. inspect alternative explanations;
5. identify boundary conditions and inferential limits;
6. only then decide the strength of the claim.

Failure to falsify a claim is not proof that the claim is true. If counterevidence has not been searched or literature access is limited, reduce the level of confidence.

## 6. Verification Loop

An agent may iterate until the success criteria are satisfied, but must not silently expand the scope.

```text
inspect
  ↓
identify failure
  ↓
make minimum justified change
  ↓
verify
  ↓
pass / blocked
  ↓
checkpoint
```

Local verification is different from an academic quality gate. A PR may satisfy its acceptance criteria while the research stage still remains REVISION REQUIRED or NOT ASSESSED.

## 7. Contract with the Git workflow

In RESEARCH mode, an Issue is the bounded context for one unit of work. It should preserve the objective, known/unknown state, scope, evidence required, success criteria, decisions, blockers, and checkpoints.

```text
Issue objective
    ↓
Assumptions / unknowns
    ↓
Evidence required
    ↓
Minimum justified change
    ↓
Verification
    ↓
Checkpoint
    ↓
PR
    ↓
Academic quality gate remains separately assessed
```

Do not use conversation history as the only working memory. Do not claim that merging a PR proves scientific quality, inferential validity, or institutional approval.

## Attribution

The initial execution principles are adapted from `multica-ai/andrej-karpathy-skills`, especially Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution. This implementation rewrites those ideas for research and adds epistemic discipline, falsification, evidence traceability, and separation between task acceptance criteria and academic quality gates.
