# Reporting Standards as Parameters

A reporting standard is selected by the research design at Stage 5 and registered as a parameter set of type `reporting`. It is not chosen by the writer at Stage 8. Its item list becomes the checklist that FG4 verifies, and the completed checklist accompanies the manuscript. See the [data structure](data-structure.md) for the `PRM` record and the [flow](research-workflow.md) for the stages.

Completing a checklist does not make the findings valid, and a checklist must not be turned into a total score or pass threshold. It is a transparency instrument: every item is either addressed at a named manuscript location, or marked `NOT APPLICABLE` with a design-based reason, or open.

## How to register one

1. At Stage 5, identify the design family from the method decision record.
2. Copy the matching preset from `parameters/presets/reporting/` to `parameters/PRM-###-reporting-<standard>.md`, using the [reporting checklist](../templates/reporting-checklist.md) form.
3. Record the standard, version, official source, and the reason it fits. If two standards apply (for example STROBE for the survey strand and COREQ for the interview strand of a mixed-methods study, plus GRAMMS for the integration), register each.
4. Link the `PRM` from the method decision record, the design matrix, and the analysis plan.
5. At Stage 8, fill the manuscript location and status of every item. At FG4, the gate review inspects the checklist.

Item wording in the presets is a short paraphrase for orientation. Verify every item against the official checklist before relying on it, and record the version actually used.

## Register by methodology

| Methodology | Reporting standard | Quality criteria the reviewers apply | What must be visible in the manuscript | Preset |
|---|---|---|---|---|
| Qualitative — interviews or focus groups, thematic analysis | COREQ, 32 items (Tong, Sainsbury & Craig 2007); SRQR, 21 items (O'Brien et al. 2014) | Trustworthiness: credibility, transferability, dependability, confirmability (Lincoln & Guba 1985); big-tent criteria (Tracy 2010); reflexive thematic analysis (Braun & Clarke 2006, 2019) | Researcher position and reflexivity; logic of informant selection; interview guide; coding process; themes with coded extracts; triangulation | [COREQ](../parameters/presets/reporting/coreq-2007.md), [SRQR](../parameters/presets/reporting/srqr-2014.md) |
| Qualitative — case study (management, policy) | SRQR; Yin 2018 case-study protocol | Eisenhardt 1989; Gioia, Corley & Hamilton 2013; Pratt 2009 | Case boundary and selection rationale; chain of evidence; data structure (first-order → second-order → aggregate); power and proof quotes | [SRQR](../parameters/presets/reporting/srqr-2014.md) |
| Quantitative — survey, cross-sectional, nonexperimental | JARS-Quant (Appelbaum et al. 2018); STROBE, 22 items (von Elm et al. 2007) | Wilkinson & Task Force 1999; Wasserstein & Lazar 2016 | Population and sampling frame; sample-size logic; instrument source, adaptation, validity and reliability evidence; missing data; model assumptions; effect sizes with intervals; associational, not causal, language | [JARS-Quant](../parameters/presets/reporting/jars-quant-2018.md), [STROBE](../parameters/presets/reporting/strobe-2007.md) |
| Quantitative — experiment or quasi-experiment | CONSORT 2010, 25 items (Schulz, Altman & Moher 2010; updated 2025); TREND, 22 items, for nonrandomized designs (Des Jarlais et al. 2004) | Threats to internal and external validity (Creswell & Creswell 2023, chapter 8; Shadish, Cook & Campbell 2002) | Allocation, control, attrition, blinding where relevant; validity threats and mitigation | [CONSORT](../parameters/presets/reporting/consort-2010.md), [TREND](../parameters/presets/reporting/trend-2004.md) |
| Structural equation modeling, PLS-SEM | Reporting guidance in Hair, Risher, Sarstedt & Ringle 2019; Kline 2023 | Separation of measurement and structural models | Reflective or formative specification; reliability and validity statistics with their thresholds registered as parameters; fit; sample size; no causal claim from cross-sectional data | [PLS-SEM](../parameters/presets/reporting/pls-sem-2019.md) |
| Mixed methods | GRAMMS, 6 items (O'Cathain, Murphy & Nicholl 2008); JARS-Mixed (Levitt et al. 2018) | Integration and joint displays (Fetters, Curry & Creswell 2013); Creswell & Plano Clark 2018 | Reason one strand is insufficient; design; point of integration; joint display; metainference; treatment of discrepant results | [GRAMMS](../parameters/presets/reporting/gramms-2008.md), [JARS-Mixed](../parameters/presets/reporting/jars-mixed-2018.md) |
| Qualitative — any design, psychology and adjacent fields | JARS-Qual (Levitt et al. 2018) | Methodological integrity: fidelity to the subject matter and utility in achieving goals | Research design overview; participants or data sources; recruitment and selection; data collection; analysis and integrity | [JARS-Qual](../parameters/presets/reporting/jars-qual-2018.md) |
| Abstract of a systematic review | PRISMA 2020 for Abstracts, 12 items (Page et al. 2021) | completeness of the summary readers actually read | objective, eligibility, sources, risk of bias, synthesis, included studies, results with intervals, limitations of evidence, interpretation, funding, registration | [PRISMA for Abstracts](../parameters/presets/reporting/prisma-abstracts-2020.md) |
| Abstract of a randomized trial | CONSORT for Abstracts (Hopewell et al. 2008; CONSORT 2010 item 1b) | same | design, participants, interventions, outcome, randomisation, blinding, numbers, effect size with precision, harms, registration | [CONSORT for Abstracts](../parameters/presets/reporting/consort-abstracts-2008.md) |
| Literature review as a study | PRISMA 2020, 27 items (Page et al. 2021); PRISMA-S for the search | Tranfield, Denyer & Smart 2003; Snyder 2019; Gough, Oliver & Thomas 2017 | Two or more databases; verbatim queries; flow diagram; selection criteria; appraisal; reports and studies not double-counted | [PRISMA](../parameters/presets/reporting/prisma-2020.md) |

Abstract checklists are registered alongside the main checklist, not instead of it. Where a design has no abstract checklist of its own, the abstract follows the generic structure in the [title and abstract rules](abstract-and-title.md).

## Selection rule

| Design (from the method decision record) | Register first | Register also when |
|---|---|---|
| Interviews or focus groups | COREQ | SRQR when the journal or discipline prefers it |
| Other qualitative designs | SRQR or JARS-Qual | — |
| Survey or observational | STROBE | JARS-Quant in psychology and adjacent fields |
| Experiment | CONSORT | TREND when allocation is not randomized |
| SEM or PLS-SEM analysis | STROBE or JARS-Quant for the design | PLS-SEM reporting guidance for the analysis |
| Mixed methods | GRAMMS | the standard for each strand |
| Systematic, scoping, or structured review | PRISMA 2020 | PRISMA-ScR for scoping reviews |

## Caveats that prevent false compliance

- **COREQ items 22 (data saturation) and 28 (participant checking)** describe practices that are not coherent with every qualitative tradition. Under reflexive thematic analysis, mark them `NOT APPLICABLE` with the methodological reason rather than reporting a saturation that was not conceptually meaningful. The repository rule already forbids imposing saturation, member checking, or intercoder agreement on every tradition.
- **PLS-SEM thresholds** (indicator loadings, composite reliability, average variance extracted, heterotrait–monotrait ratio, variance inflation factors) are parameters. Register each value with its source; do not treat them as universal cut-offs.
- **Journal quartile** is not part of any reporting standard. It is a priority filter for searching, not evidence of source quality.
- **A checklist is not appraisal.** JBI and design-specific appraisal tools assess the quality of sources read; reporting standards assess the completeness of what this study reports.
- **Versions change.** Record the version actually used; CONSORT was updated in 2025 and PRISMA in 2020. Verify against the official source at the time of use.

## Sources

- Appelbaum, M., Cooper, H., Kline, R. B., Mayo-Wilson, E., Nezu, A. M., & Rao, S. M. (2018). Journal article reporting standards for quantitative research in psychology. *American Psychologist*, 73(1), 3–25.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
- Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597.
- Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE.
- Des Jarlais, D. C., Lyles, C., Crepaz, N., & the TREND Group. (2004). Improving the reporting quality of nonrandomized evaluations of behavioral and public health interventions: The TREND statement. *American Journal of Public Health*, 94(3), 361–366.
- Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review*, 14(4), 532–550.
- Fetters, M. D., Curry, L. A., & Creswell, J. W. (2013). Achieving integration in mixed methods designs. *Health Services Research*, 48(6, pt 2), 2134–2156.
- Gough, D., Oliver, S., & Thomas, J. (2017). *An Introduction to Systematic Reviews* (2nd ed.). SAGE.
- Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report the results of PLS-SEM. *European Business Review*, 31(1), 2–24.
- Kline, R. B. (2023). *Principles and Practice of Structural Equation Modeling* (5th ed.). Guilford.
- Levitt, H. M., Bamberg, M., Creswell, J. W., Frost, D. M., Josselson, R., & Suárez-Orozco, C. (2018). Journal article reporting standards for qualitative primary, qualitative meta-analytic, and mixed methods research in psychology. *American Psychologist*, 73(1), 26–46.
- Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic Inquiry*. SAGE.
- O'Brien, B. C., Harris, I. B., Beckman, T. J., Reed, D. A., & Cook, D. A. (2014). Standards for reporting qualitative research: A synthesis of recommendations. *Academic Medicine*, 89(9), 1245–1251.
- O'Cathain, A., Murphy, E., & Nicholl, J. (2008). The quality of mixed methods studies in health services research. *Journal of Health Services Research & Policy*, 13(2), 92–98.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372, n71.
- Schulz, K. F., Altman, D. G., & Moher, D. (2010). CONSORT 2010 statement. *BMJ*, 340, c332.
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Houghton Mifflin.
- Tong, A., Sainsbury, P., & Craig, J. (2007). Consolidated criteria for reporting qualitative research (COREQ). *International Journal for Quality in Health Care*, 19(6), 349–357.
- Tracy, S. J. (2010). Qualitative quality: Eight "big-tent" criteria for excellent qualitative research. *Qualitative Inquiry*, 16(10), 837–851.
- von Elm, E., et al. (2007). The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement. *PLoS Medicine*, 4(10), e296.
- Yin, R. K. (2018). *Case Study Research and Applications* (6th ed.). SAGE.

The EQUATOR Network (equator-network.org) indexes reporting guidelines by design; the [standards register](standards.md) records which of them a project adopts.
