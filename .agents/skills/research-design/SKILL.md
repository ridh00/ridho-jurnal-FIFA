---
name: research-design
description: Use Creswell-first reasoning to align research problems and questions with approach, design, evidence, analysis, ethics, and execution readiness.
---

# Research Design and Execution

Read the project brief, [academic integrity rules](../../../docs/academic-integrity.md), G4–G6 in the [quality gates](../../../docs/quality-gates.md), and the Creswell-first [method layer](../../../method/README.md). Before recommending a methodology, run the [method selection protocol](../../../method/05-method-selection-protocol.md) and read the relevant [qualitative](../../../method/02-qualitative.md), [quantitative](../../../method/03-quantitative.md), or [mixed-methods](../../../method/04-mixed-methods.md) guidance. Use the [design matrix](../../../templates/design-matrix.md), [analysis plan](../../../templates/analysis-plan.md), and [ethics and data plan](../../../templates/ethics-data-plan.md).

## Foundational decisions

Start from the research problem, purpose, and research questions. Use Creswell & Creswell's relationship among philosophical worldview, research approach, research design, and research methods as the default design architecture. Then consider the type of claim: descriptive, interpretive, explanatory, causal, predictive, evaluative, or conceptual. Compare feasible designs and explain the tradeoffs. A paradigm should fit the question and analytic practice; do not add philosophical labels that have no methodological consequences. Treat the AI's recommendation as `PROPOSED`; only the researcher can approve the methodological decision.

## Apply only what is relevant

- Quantitative: define the target estimand/population, sampling, operationalization, validity/reliability, sample size based on suitable precision/power/simulation logic, missingness, clustering, weights, confounding, and model assumptions. Statistical thresholds require justification; do not treat one number as universal.
- SEM: distinguish measurement and structural models, reflective/formative specification when relevant, identification, sample adequacy, and estimator choice. Good fit or a significant indirect effect does not establish causality.
- Qualitative: state the tradition, case-selection logic, researcher position and reflexivity, process of interpretation, context, corpus adequacy, and handling of negative/deviant cases or alternative readings. Do not impose saturation, inter-rater reliability, or member checking when they are not appropriate to the tradition.
- Mixed methods: explain why one approach is insufficient, sequence/priority, sample relationship, integration points, joint displays when useful, and how conflicting results will be handled.
- Conceptual/archival: justify the corpus, provenance, authenticity, historical context, rules of interpretation, access limitations, and alternative arguments.
- Review-based studies: align the question, selection/appraisal process, and synthesis method; distinguish primary from secondary sources and avoid double-counting studies.

## Before execution and interpretation

Record instrument permissions, adaptations, pilots, consent, access, and ethics status according to the actual project. No data collection is authorized merely because a template has been completed.

For planned analysis, define primary outputs, exclusion rules, sensitivity checks, and failure handling before inspecting relevant results. If the data have already been seen, state that explicitly. Preregistration does not turn retrospective analysis into prospective analysis.

During analysis, preserve safe data-version identifiers, transformations, code/software, parameters, and output trails. Do not invent results when data do not exist. Record deviations and adjust inferential status when needed. Conclusions must follow the design and assumptions, not the sophistication of the tool.

## Place in the research flow

This skill owns Stages 5 and 6 of the [research flow](../../../docs/research-workflow.md).

- Stage 5 decides in this order, which is also the order of the method section: approach → method/design → data types → data sources → data collection → data analysis → ethics → reporting standard. Data types follow the design, not the other way round. Record the recommendation in the [method decision record](../../../templates/method-decision-record.md) as `PROPOSED`; only the researcher moves it to `APPROVED`, recorded in the decision log.
- Every parameter — sampling, instrument, cleaning rules, analysis thresholds, bootstrap counts, software versions — is a `PRM` record with value, justification, and source. Thresholds without a source are not accepted at FG2. Specialist authorities are taken from the [methodology sources register](../../../docs/methodology-sources.md).
- **The reporting standard is a parameter.** Select it by design from the [reporting standards](../../../docs/reporting-standards.md), copy the preset into a `PRM` of type reporting, and link it from the method decision record, design matrix, and analysis plan.
- An AI assistant may propose secondary data sources that complement the primary data or serve as a basis for triangulation; each is verified by the researcher, receives a `DAT` record, and is logged in the AI-use log.
- Data cleaning keeps only data within the focus of the research questions; the rules are a `PRM` of type cleaning, each execution a `RUN`, each output a derived `DAT`. Quantitative validity and reliability tests run before the main analysis.
- Stage 6 produces `FND` statements, each citing `DAT` or `RUN`, and completes the RQ ↔ finding ↔ data matrix in `brain.md`. FG3 passes only when every RQ is answered; no manuscript outline before that. Findings are not compared with the literature here.

## Execution discipline

Apply the cross-skill principles in `research-rigor`: do not silently resolve uncertainty, use the minimum sufficient complexity, keep changes within task scope, and verify outcomes against explicit acceptance criteria. For high-impact claims or decisions, inspect counterevidence and alternative explanations before strengthening the conclusion.
