# Mixed Methods Research

## When to recommend mixed methods

Recommend mixed methods when a research problem is not adequately understood through quantitative or qualitative evidence alone and meaningful integration of both forms of data can provide additional insight.

Mixed methods is not simply:

```text
survey + interview
```

It requires:

```text
quantitative strand
        +
qualitative strand
        +
explicit integration
        =
mixed-methods inference
```

If the two strands never interact analytically, the study is not methodologically complete as mixed methods.

## Worldview tendency

Mixed-methods research commonly aligns with pragmatism because the research problem and intended consequences guide the choice of methods, and multiple forms of data may be used when they provide a better understanding.

A transformative worldview may also shape mixed-methods research when power, social justice, marginalization, collaboration, or change is central.

## Core mixed-methods concepts

The method section should define and operationalize:

- quantitative / closed-ended data;
- qualitative / open-ended data;
- mixed-methods design;
- integration;
- joint display;
- metainference.

## Integration is mandatory

Identify:

- **why** the datasets need to be combined;
- **when** integration occurs;
- **how** integration occurs;
- **what** additional inference is expected from integration.

Creswell-oriented integration procedures include merging, connecting, and embedding.

## Core designs

### Convergent design

Use when the intent is to compare or merge quantitative and qualitative evidence to obtain a more comprehensive understanding of the same research problem.

```text
QUAN collection ──→ QUAN analysis ──┐
                                    ├── MERGE / COMPARE ──→ metainference
QUAL collection ──→ QUAL analysis ──┘
```

Characteristics:

- both strands are commonly collected at roughly the same time;
- databases are analyzed separately first;
- findings are then merged or compared;
- convergence, divergence, contradiction, and complementarity should be examined;
- comparable constructs or concepts should be considered where appropriate.

### Explanatory sequential design

Use when quantitative results need deeper explanation through follow-up qualitative inquiry.

```text
QUAN
  ↓
analyze quantitative results
  ↓
identify results requiring explanation
  ↓
QUAL follow-up
  ↓
connect + integrate
  ↓
metainference
```

Typical purposes include explaining surprising quantitative results, explaining relationships among variables, understanding why a pattern occurred, and adding participant perspectives to quantitative findings.

The qualitative sampling and questions should be connected to the initial quantitative findings.

### Exploratory sequential design

Use when qualitative exploration is needed first and the findings will be used to build or adapt a quantitative component.

```text
QUAL exploration
  ↓
analysis
  ↓
build / adapt
instrument, variables, intervention, assessment, website, model
  ↓
QUAN test
  ↓
integrate
  ↓
metainference
```

Typical purposes include developing a context-sensitive instrument, identifying variables before testing them, designing an intervention, adapting an existing measure, or developing a quantitative assessment from participant-derived findings.

The AI must explain exactly **what is built from the qualitative findings**.

## Complex mixed-methods designs

Creswell & Creswell discuss complex designs that embed one or more core designs within a larger framework or process.

### Mixed-methods experimental / intervention design

Use when qualitative or mixed data augment an experiment or intervention, for example to understand participant experience, explain quantitative treatment outcomes, or examine implementation processes.

### Mixed-methods case study design

Use when a case-study framework contains a quantitative/qualitative core mixed-methods structure. The case must still be explicitly bounded.

### Mixed-methods participatory / social-justice design

Use when a transformative or participatory framework shapes the use and integration of quantitative and qualitative evidence.

### Mixed-methods evaluation design

Use when one or more core mixed-methods designs are embedded across phases of an evaluation process such as needs assessment, implementation, outcome assessment, or intervention evaluation.

## Choosing among mixed-methods designs

Primary selection should be based on **intent and procedures**.

### Intent

- compare/merge two forms of evidence → consider **convergent**;
- explain quantitative findings → consider **explanatory sequential**;
- build a quantitative component from qualitative exploration → consider **exploratory sequential**;
- augment a larger intervention, case, participatory framework, or evaluation → consider a **complex design**.

### Procedures

Ask:

- Will data be collected roughly at the same time or in phases?
- Does one phase need the results of another before it can begin?
- Will integration happen through merging, connecting, or embedding?
- Can one researcher realistically manage concurrent strands?
- Does the project require a team?
- What time and resources are available?

Practical considerations matter, but they are secondary to methodological intent.

## Mixed-methods questions

A strong mixed-methods study normally contains:

1. quantitative research question(s) or hypotheses;
2. qualitative research question(s);
3. a mixed-methods integration question.

The integration question should state what the study expects to learn by combining the datasets.

## Joint displays

A joint display places quantitative and qualitative evidence together so relationships, convergence, divergence, or developmental links can be interpreted.

Propose a joint-display structure during the design stage, not after results are known.

## Metainferences

Metainferences are conclusions or insights that arise from integrated evidence rather than either database alone.

Distinguish:

- quantitative inference;
- qualitative interpretation;
- mixed-methods metainference.

## Mixed-methods validity

Validity concerns exist at multiple layers:

- quality of the quantitative strand;
- quality of the qualitative strand;
- integrity of the integration procedure;
- appropriateness of sampling across phases;
- whether the second phase genuinely follows from the first in sequential designs;
- whether conclusions actually emerge from integrated evidence.

## Method-section input contract

Before drafting a mixed-methods method section, the AI must have or mark as unresolved:

```yaml
approach: mixed_methods
worldview:
mixed_methods_rationale:
core_or_complex_design:
design_name:
overall_research_problem:
quantitative_questions:
qualitative_questions:
mixed_methods_question:
quantitative_sampling:
qualitative_sampling:
phase_relationship:
quantitative_data_collection:
qualitative_data_collection:
quantitative_analysis:
qualitative_analysis:
integration_intent:
integration_procedure:
integration_point:
joint_display_plan:
metainference_plan:
validity_quantitative:
validation_qualitative:
integration_validity:
resources_and_timing:
team_structure:
ethics:
data_management:
limitations:
specialist_method_sources:
decision_status:
```

Mixed methods must not be marked ready for approval if the integration fields remain undefined.
