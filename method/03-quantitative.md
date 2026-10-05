# Quantitative Research

## When to recommend a quantitative approach

Recommend quantitative research when the research problem requires measurement and statistical examination of variables, groups, trends, associations, predictions, or intervention effects.

Typical signals include:

- testing a theory or explanation;
- examining relationships among variables;
- identifying predictors of outcomes;
- comparing groups;
- estimating population trends, attitudes, or opinions;
- testing whether a treatment or intervention influences an outcome.

The AI must distinguish **association** from **causation**. A correlational or survey design does not become causal because the model contains arrows.

## Worldview tendency

Quantitative studies commonly align with a postpositivist worldview:

- knowledge is fallible rather than absolute;
- theories are tested and refined;
- observation and measurement matter;
- alternative explanations must be considered;
- validity, reliability, and bias control are important.

## Design selection

### Survey / nonexperimental family

Use survey research when the study needs a quantitative description of trends, attitudes, opinions, characteristics, or relationships in a population by studying a sample.

Survey designs may be cross-sectional or longitudinal.

Survey methods can test hypothesized associations and predictions. They normally do not provide the same basis for causal inference as a true experiment.

A survey plan should address:

- purpose and rationale;
- survey form and data-collection mode;
- population;
- sampling design;
- sampling type;
- stratification when relevant;
- sample-size determination;
- power analysis when applicable;
- instrumentation and measures;
- validity of scores;
- reliability of scores;
- pilot testing when appropriate;
- administration;
- variables;
- analysis plan;
- interpretation and reporting;
- preregistration when appropriate.

### Experimental family

Use an experimental design when the research question asks whether a treatment, intervention, or manipulated condition influences an outcome.

#### True experiment

Use when random assignment to treatment conditions is feasible and ethically defensible. This provides stronger control over alternative explanations and is the preferred family when the study makes a genuine causal claim.

#### Quasi-experiment

Use when an intervention or treatment is studied but random assignment is not feasible. Explicitly discuss weaker control of alternative explanations and relevant threats to validity.

#### Single-subject design

Use when an intervention is repeatedly observed within a single individual or a small number of individuals across time and conditions.

### Other nonexperimental quantitative designs

Creswell & Creswell acknowledge designs such as correlational and causal-comparative research and discuss longitudinal forms. The sixth edition develops survey and experimental method plans in greater detail.

Better Research therefore distinguishes:

- **design family supported by Creswell's framework**, from
- **specialized analytical technique requiring an additional methodological source**.

## Variables

Classify variables correctly when relevant:

- independent / manipulated;
- dependent / outcome;
- predictor;
- criterion / response;
- mediator;
- moderator;
- confounder.

Variable labels must reflect the actual design. Do not call a naturally occurring predictor an experimentally manipulated independent variable.

## Causal reasoning

Before causal language is permitted, ask:

1. Is the presumed cause temporally prior to the outcome?
2. Is there a plausible alternative or confounding variable?
3. Does the design manipulate the causal factor?
4. Is there random assignment?
5. What threats to internal validity remain?

If the design is observational, default to association/prediction language unless a stronger causal strategy is independently justified.

## Population and sampling

A quantitative method plan should identify:

- target population;
- accessible population;
- sampling frame where available;
- single-stage or multistage / cluster sampling;
- probability or nonprobability selection;
- systematic sampling if used;
- stratification if needed;
- sample-size rationale.

Sample size should follow the analysis plan and expected outcomes rather than an arbitrary percentage of the population. Where inference testing is planned, power analysis should be considered at the study-planning stage.

## Instrumentation

For each instrument or measure, document:

- construct or variable measured;
- original source;
- whether it is original, adapted, or modified;
- permission/licensing if relevant;
- items and scoring;
- evidence for validity of scores;
- evidence for reliability;
- context and population in which it was previously validated;
- pilot testing if required;
- translation/adaptation procedures where relevant.

An instrument should not be treated as valid merely because it has been published.

## Analysis planning

The analysis must answer the research questions or hypotheses.

```text
Research question / hypothesis
        ↓
Variables
        ↓
Measurement level
        ↓
Design
        ↓
Required assumptions
        ↓
Statistical analysis
        ↓
Interpretation permitted by design
```

Creswell provides the design framework, but specialized analyses such as SEM, multilevel modeling, advanced longitudinal modeling, psychometrics, causal inference, or complex mediation/moderation normally require additional methodological authorities.

## Experimental validity

Experimental plans should explicitly consider threats to internal and external validity and describe procedures used to minimize those threats.

## Method-section input contract

Before drafting a quantitative method section, the AI must have or mark as unresolved:

```yaml
approach: quantitative
worldview:
design:
research_questions:
hypotheses:
theory:
population:
sampling_frame:
sampling_design:
sampling_type:
sample_size:
power_analysis:
variables:
measures:
instrument_validity:
instrument_reliability:
data_collection:
pilot_testing:
analysis_plan:
statistical_assumptions:
causal_claim_level:
validity_threats:
preregistration:
ethics:
data_management:
limitations:
specialist_method_sources:
decision_status:
```

Missing information must be surfaced, not fabricated.
