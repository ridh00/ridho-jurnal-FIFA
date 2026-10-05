# Academic Standards Register

Reviewed for builder preparation on 7 September 2026. This is a register of guidance sources, not the substantive bibliography of any research project. Verify versions and relevance again when a specific design is selected.

| Primary source / steward | Scope | Use in this builder |
|---|---|---|
| Creswell, J. W., & Creswell, J. D. (2023), *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches* (6th ed., SAGE) | Research-design architecture and selection across qualitative, quantitative, and mixed methods | Default Creswell-first framework for the [`method/`](../method/README.md) decision layer; specialist technical sources are still required where the book is not a detailed method manual |
| [ALLEA European Code of Conduct, 2023 edition](https://allea.org/code-of-conduct/) | Cross-disciplinary research integrity | Reference for reliability, honesty, respect, and accountability; not a claim that European funding rules automatically bind a project |
| [PRISMA 2020](https://www.prisma-statement.org/prisma-2020) | Reporting systematic reviews, especially intervention evaluations | Select guidance according to review type; not mandatory for every dissertation or study |
| [PRISMA-S](https://www.prisma-statement.org/prisma-search) | Reporting search strategies | Basis for transparent search-source and query documentation |
| [PRISMA-ScR](https://www.prisma-statement.org/scoping) | Reporting scoping reviews | Consider when the mapping objective fits a scoping-review design |
| [PRISMA 2020 Statement](https://www.bmj.com/content/372/bmj.n71) | Explanation and scope of the guideline | Reporting checklist is not a method-quality score |
| [JBI Critical Appraisal Tools](https://jbi.global/critical-appraisal-tools) | Design-specific critical appraisal | Choose a suitable tool/version and record evidence for each judgment |
| [SRQR via EQUATOR](https://www.equator-network.org/reporting-guidelines/srqr/) | Reporting qualitative research | Transparency in approach, researcher position, process, and interpretation |
| [APA JARS](https://www.apa.org/pubs/journals/resources/apa-style-jars.html) | Reporting quantitative, qualitative, and mixed-methods research in psychology | Use only when discipline and design fit; does not prescribe an estimator |
| [Center for Open Science: Preregistration](https://www.cos.io/initiatives/prereg) | Time-stamped planning and distinction between planned and exploratory analysis | Record timing, results already known, and later plan changes |
| [COREQ](https://www.equator-network.org/reporting-guidelines/coreq/) — Tong, Sainsbury & Craig (2007) | Reporting interviews and focus groups | Preset under `parameters/presets/reporting/`; items 22 and 28 marked NOT APPLICABLE with a reason under traditions that do not use saturation or member checking |
| [STROBE](https://www.strobe-statement.org/) — von Elm et al. (2007) | Reporting observational and survey designs | Preset; register as a `PRM` of type reporting when the design is observational |
| [CONSORT](https://www.consort-statement.org/) — Schulz, Altman & Moher (2010); 2025 update | Reporting randomized experiments | Preset; record the version the outlet requires |
| [TREND](https://www.cdc.gov/trendstatement/) — Des Jarlais et al. (2004) | Reporting nonrandomized evaluations | Preset for quasi-experiments |
| [GRAMMS](https://doi.org/10.1258/jhsrp.2007.007074) — O'Cathain, Murphy & Nicholl (2008) | Reporting mixed-methods studies | Preset; register together with the standard of each strand |
| Hair, Risher, Sarstedt & Ringle (2019), *European Business Review* 31(1) | Reporting and threshold guidance for PLS-SEM | Preset whose thresholds are parameters requiring justification, not universal cut-offs |
| [EQUATOR Network](https://www.equator-network.org/) | Index of reporting guidelines by design | Source for guidelines not preset here; see [reporting standards](reporting-standards.md) |

## Rule classification

**Core integrity rules:** do not fabricate; attribute sources; report limitations; protect data; do not claim activities that did not occur.

**Research-design framework:** Creswell & Creswell (2023) is the builder's default methodological reasoning framework. This is a Better Research design choice, not an external regulation that automatically binds every institution or discipline.

**Conditional standards:** PRISMA, JBI, SRQR, JARS, preregistration, and other frameworks are selected according to purpose, design, discipline, and institutional requirements. They are not all required simultaneously.

**Local conventions:** folder names, traceability IDs (including the typed statement IDs in `brain.md` and the `DAT`/`PRM`/`RUN` records), gates G0–G7 and flow gates FG0–FG5, the ten-stage research flow, the treatment of reporting standards as parameters, the Git workflow, and Markdown templates are Better Research design choices, not academic regulations. The default search windows (ten years for theory developments, five years for empirical literature) and the use of journal quartile as a priority order are defaults recorded as parameters, not rules.

**Project-specific requirements that must be verified:** institutional dissertation/thesis rules, ethics/data-access requirements, AI/authorship policy, final citation style, discipline-specific reporting standards, and output language. Record the official source, version, date, scope, and adoption decision in the project brief.

## Adopting a standard

Record the standard name/version, official source, scope, reason for relevance, sections actually used, and any adaptation. Do not convert a checklist into a total quality score or pass threshold without methodological justification. Completing a checklist does not prove the findings or contribution are valid.

## Technical basis for local skills

The [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) describes skills as folders containing `SKILL.md` and supports project-local placement under `.agents/skills`. Availability depends on the environment; the local skill index provides an explicit fallback path.
