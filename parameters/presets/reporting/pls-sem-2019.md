# Preset — PLS-SEM reporting and analysis parameters (Hair et al. 2019)

Type: `reporting` and `analysis`. Copy to `parameters/PRM-###-pls-sem.md` using the [parameter set](../../../templates/parameter-set.md) form (thresholds) and the [reporting checklist](../../../templates/reporting-checklist.md) form (items). Applies to partial least squares structural equation modeling. It complements, and does not replace, the reporting standard of the study design (STROBE or JARS-Quant for a survey).

Official source: Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report the results of PLS-SEM. *European Business Review*, 31(1), 2–24. Thresholds below are the values the article discusses as guidance; each is a **parameter** that needs a recorded justification in this project, not a universal cut-off. Verify against the source and later editions of Hair et al., *A Primer on PLS-SEM*.

## Threshold parameters

| Parameter | Guidance value | Justification | Source | Project value |
|---|---|---|---|---|
| Indicator loadings (reflective) | ≥ 0.708 | indicator explains at least half its variance | Hair et al. 2019 | NOT YET FILLED |
| Internal consistency reliability | Cronbach's alpha, rho_A, composite reliability between 0.70 and 0.95 | below 0.70 unreliable; above 0.95 redundant items | Hair et al. 2019 | NOT YET FILLED |
| Convergent validity (reflective) | AVE ≥ 0.50 | construct explains at least half of indicator variance | Hair et al. 2019 | NOT YET FILLED |
| Discriminant validity | HTMT < 0.90 (conceptually similar constructs) or < 0.85 (distinct); bootstrap interval not including 1 | HTMT preferred over Fornell–Larcker | Hair et al. 2019 | NOT YET FILLED |
| Convergent validity (formative) | redundancy-analysis correlation ≥ 0.70 | formative measure agrees with a global item | Hair et al. 2019 | NOT YET FILLED |
| Collinearity (formative indicators; structural model) | VIF < 3 ideally; < 5 tolerable | collinearity distorts weights and paths | Hair et al. 2019 | NOT YET FILLED |
| Path significance | bootstrapping, number of samples recorded (e.g. 10,000); percentile intervals | inference method for PLS | Hair et al. 2019 | NOT YET FILLED |
| Explanatory power | R² reported per endogenous construct; interpret by context, not by fixed labels | R² is discipline-dependent | Hair et al. 2019 | NOT YET FILLED |
| Effect sizes | f² per path; 0.02, 0.15, 0.35 as rough small, medium, large | relevance beyond significance | Hair et al. 2019 | NOT YET FILLED |
| Predictive relevance | Q² > 0; PLSpredict comparison against a linear benchmark | out-of-sample assessment | Hair et al. 2019 | NOT YET FILLED |
| Model fit | SRMR reported with caution; not a primary criterion in PLS-SEM | fit indices have limited meaning in PLS | Hair et al. 2019 | NOT YET FILLED |
| Sample size logic | recorded method (e.g. inverse square root) and resulting minimum | the "ten times" rule is not adequate | Hair et al. 2019 | NOT YET FILLED |
| Software and version | recorded | reproducibility | analysis plan | NOT YET FILLED |

## Reporting items

| Item | Requirement (paraphrase) | Manuscript location | Status | Evidence / notes |
|---|---|---|---|---|
| P1 | Rationale for PLS-SEM over covariance-based SEM tied to the research objective | | OPEN | |
| P2 | Model specification: reflective or formative measurement per construct; higher-order components; control variables | | OPEN | |
| P3 | Data: sample size logic, missing-data treatment, distribution, outliers | | OPEN | |
| P4 | Measurement model results against the registered thresholds | | OPEN | |
| P5 | Structural model results: collinearity, paths with intervals, R², f², Q² or PLSpredict | | OPEN | |
| P6 | Software, version, algorithm settings, bootstrap settings | | OPEN | |
| P7 | Boundaries of inference: no causal claim from cross-sectional data; good fit is not evidence of causality | | OPEN | |

The quality gates already state it: good fit or a significant indirect effect does not establish causality. The design decides what the path model may claim.
