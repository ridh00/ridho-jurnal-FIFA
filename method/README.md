# Method

> **Creswell-first methodological reasoning for Better Research**

This folder is the methodological decision layer for Better Research. It helps an AI agent reason from a research problem to an appropriate research approach, design, and method without jumping directly to a familiar statistical technique or qualitative procedure.

The primary methodological anchor is:

**Creswell, J. W., & Creswell, J. D. (2023). _Research Design: Qualitative, Quantitative, and Mixed Methods Approaches_ (6th ed.). SAGE.**

Better Research treats Creswell & Creswell as the default framework for **research-design reasoning**. More specialized methodological literature is still required when a study moves into technical procedures that Creswell introduces but does not develop in specialist depth.

## Core rule

Do not begin with a method.

Begin with the research problem.

```text
Research problem
    ↓
Purpose / study aim
    ↓
Research question(s)
    ↓
Philosophical worldview
    ↓
Research approach
    ├── Qualitative
    ├── Quantitative
    └── Mixed methods
    ↓
Research design
    ↓
Sampling / participants / cases
    ↓
Data collection
    ↓
Data analysis
    ↓
Interpretation
    ↓
Validity / reliability / qualitative validation / mixed-methods integration
    ↓
Method chapter
```

The AI may **recommend** a methodological path, but it must not silently convert that recommendation into a final research decision. Final methodological judgment remains with the researcher.

## Files in this folder

- [`01-creswell-research-design-flow.md`](01-creswell-research-design-flow.md) — full reasoning sequence from problem to method.
- [`02-qualitative.md`](02-qualitative.md) — qualitative decision logic, designs, procedures, and method-writing inputs.
- [`03-quantitative.md`](03-quantitative.md) — quantitative decision logic, survey and experimental families, procedures, and method-writing inputs.
- [`04-mixed-methods.md`](04-mixed-methods.md) — mixed-methods rationale, core and complex designs, integration, and method-writing inputs.
- [`05-method-selection-protocol.md`](05-method-selection-protocol.md) — operational decision protocol an AI should run before recommending a method.
- [`06-method-chapter-blueprint.md`](06-method-chapter-blueprint.md) — practical blueprint for drafting methodology/method chapters after design approval.
- [`07-ai-method-rules.md`](07-ai-method-rules.md) — explicit rules and output contract for AI agents.
- [`references.md`](references.md) — source scope and methodological boundaries.

## Creswell-first, not Creswell-only

Creswell & Creswell provide the organizing framework for the relationship among philosophical assumptions, research approaches, research designs, and research methods. The book emphasizes essential features of research design rather than attempting to be a complete specialist manual for every technical method.

Therefore:

1. Use Creswell first to decide the **architecture of the study**.
2. Use specialist methodological sources to decide **technical implementation** when needed.
3. Never use a specialist technique to retroactively invent the research design.
4. Record any methodological departure from this framework and justify it.

## Where the decisions are recorded

The recommendation produced by the protocol is written into the [method decision record](../templates/method-decision-record.md) with status `PROPOSED`; the researcher's approval is a decision (`DEC`) in the decision log. Every threshold, sample-size assumption, cleaning rule, and analysis setting the design relies on is a parameter set (`PRM`) with a value, a justification, and a source; the reporting standard the design requires is a `PRM` of type `reporting`. Method statements (`MTH`) are registered in [`brain.md`](../brain.md) and link those records. See the [research flow](../docs/research-workflow.md), the [data structure](../docs/data-structure.md), and the [methodology sources register](../docs/methodology-sources.md) for specialist authorities beyond Creswell & Creswell.

## Human control

The purpose of this folder is not to make methodology automatic. It is to make methodological reasoning explicit.

AI should help the researcher expose assumptions, compare plausible designs, detect methodological mismatch, maintain consistency, identify evidence still required, prepare checkpoints, and draft the method section only after decisions are traceable.

The researcher remains responsible for the final methodological judgment.
