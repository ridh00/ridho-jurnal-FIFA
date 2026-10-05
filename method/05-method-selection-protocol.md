# Method Selection Protocol

## Purpose

Run this protocol whenever a researcher asks which methodology, design, or analysis technique should be used.

The AI should not answer by naming a method immediately.

## Stage 0 — Reject method-first reasoning

If the user begins with a technique, restate it as a proposal.

```text
User: "I want to use PLS-SEM."

AI:
PLS-SEM is currently a proposed analysis technique, not yet an approved research design.
First establish the research problem, questions, theory, variables, and design.
```

## Stage 1 — Diagnose the research problem

Collect or infer cautiously:

```yaml
research_problem:
what_is_known:
what_is_unknown:
why_it_matters:
target_context:
unit_of_interest:
evidence_available:
```

If the research problem is unclear, status is `BLOCKED`.

## Stage 2 — Determine the knowledge intent

| Knowledge intent | Initial methodological direction |
|---|---|
| Explore meaning, experience, context, or an unknown phenomenon | Qualitative |
| Describe population trends, attitudes, opinions, or characteristics | Quantitative survey |
| Examine association or prediction among measured variables | Quantitative nonexperimental / survey family |
| Test a treatment or intervention effect | Experimental / quasi-experimental |
| Explain a quantitative result in depth | Explanatory sequential mixed methods |
| Build a measure, variable set, intervention, or assessment from qualitative findings | Exploratory sequential mixed methods |
| Compare or merge qualitative and quantitative perspectives on the same problem | Convergent mixed methods |
| Embed mixed evidence in an experiment, case, participatory framework, or evaluation | Complex mixed methods |

This table is a decision aid, not an automatic classifier.

## Stage 3 — Check the research questions

### Qualitative question check

- exploratory wording;
- one central phenomenon;
- participant meaning and context;
- broad enough for emergence.

### Quantitative question check

- measurable variables;
- relationship, prediction, comparison, description, or effect;
- hypotheses where appropriate;
- causal wording only when the design can support it.

### Mixed-methods question check

- quantitative question(s);
- qualitative question(s);
- explicit integration question.

If question and intended design conflict, status is `REVISION REQUIRED`.

## Stage 4 — Surface worldview assumptions

Recommend the most coherent worldview tendency and explain the alignment. Do not use worldview labels decoratively.

## Stage 5 — Select the approach

Compare at least two plausible alternatives when the decision is not obvious.

```yaml
candidate_approaches:
  - approach:
    fit:
    weaknesses:
  - approach:
    fit:
    weaknesses:

recommended_approach:
reason:
```

## Stage 6 — Select the design

### If qualitative

```text
Stories/life chronology?              → Narrative
Shared lived experience / essence?    → Phenomenology
Process/action/interaction + theory?  → Grounded theory
Culture-sharing patterns?             → Ethnography
Bounded case in context?              → Case study
Close descriptive account/themes?     → Descriptive method
```

### If quantitative

```text
Population trends/opinions/associations? → Survey / nonexperimental
Treatment/intervention effect?            → Experiment / quasi-experiment
Repeated intervention within individual?  → Single-subject
```

Then identify whether the analysis requires a specialist methodological source.

### If mixed methods

```text
Merge/comparison?                → Convergent
QUAN then explain with QUAL?     → Explanatory sequential
QUAL then build/test QUAN?       → Exploratory sequential
Embedded in larger framework?    → Complex design
```

## Stage 7 — Check feasibility

Check:

- participant access;
- sampling frame;
- data availability;
- researcher skill;
- time;
- funding;
- software;
- field access;
- ethics;
- team capacity;
- instrument access/licensing;
- ability to conduct multiple phases.

Feasibility may modify the design, but it must not disguise poor fit.

## Stage 8 — Check evidence requirements

Identify what must still be verified, for example:

- evidence that a construct has an appropriate validated instrument;
- evidence that the qualitative design is used appropriately in the field;
- power-analysis assumptions;
- availability of a sampling frame;
- specialist procedures for the selected analysis;
- existing theory;
- precedent for a mixed-methods integration strategy.

## Stage 9 — Falsify the recommendation

Ask:

- What would make this design wrong?
- Is there a simpler design that answers the question?
- Am I recommending mixed methods only because it seems richer?
- Am I calling the study causal without experimental control?
- Am I naming a qualitative tradition that the question does not require?
- Am I selecting a method because the researcher already knows the software?
- Could the same question be answered with less methodological complexity?

## Stage 10 — Produce the recommendation

```markdown
## Methodological recommendation

**Status:** PROPOSED

**Research problem**
...

**Knowledge intent**
...

**Recommended approach**
...

**Worldview alignment**
...

**Recommended design**
...

**Why this design fits**
...

**Alternatives considered**
...

**Methods likely required**
...

**Claims this design can support**
...

**Claims this design cannot support**
...

**Unresolved decisions**
...

**Evidence / specialist sources still required**
...

**Researcher decision**
APPROVE / REVISE / REJECT
```

The AI must stop at `PROPOSED` until a human explicitly makes the methodological decision.

Record the recommendation in `research/method-decision-record.md` using the [method decision record](../templates/method-decision-record.md) template, link the research questions it answers, register the parameter sets it relies on (including the reporting standard as a `PRM` of type `reporting`), and register the resulting `MTH` statements in `brain.md` once the researcher approves.
