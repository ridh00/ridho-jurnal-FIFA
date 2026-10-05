# Changelog

All notable changes to Better Research are recorded here. The repository uses semantic versioning for the **builder contract**, not for the maturity of any research project.

## [0.3.0] - 2026-09-17

An explicit research process. Version 0.2.0 could reason about methodology; it had no workflow. This release adds the ten stages, the gates that stop work from running ahead of its evidence, two anchors that keep direction and coherence inspectable, and machine-checked traceability from a sentence in the manuscript back to the run that produced its evidence.

### Added

**Research flow**

- Ten-stage [research flow](docs/research-workflow.md): context → phenomenon → theoretical review → empirical literature review → state of the art, novelty, and research questions → method → results → discussion and conclusion → outline and writing → revision.
- Six flow gates FG0–FG5 bundling the quality gates G0–G7 into hard stops: no method, instrument, or data collection before FG1; no analysis before FG2; no manuscript outline or results prose before FG3; no submission before FG4; no resubmission before FG5. A flow gate takes the most conservative status among the gates it bundles, and reopening one reopens every stage after it.
- Three literature tracks with separate folders, presets, and windows: `literature/search-online/` (locus evidence), `literature/theory/` (grand theory and its developments, ten years, Scopus Q1–Q4 and Web of Science), `literature/literature-review/` (empirical studies, five years). The theoretical review looks for theory; the empirical review looks for studies; mixing them was how the two gaps became one vague gap.

**Anchors**

- `GRO.md` and its [rules](docs/gro.md): the Grand Research Outline, the report written for the researcher. Eleven numbered sections follow the research outline — introduction, grand theory, literature and gap, novelty, research questions, method, data and analysis, findings, discussion, conclusion, manuscript — each one paragraph stating where that part is going **and why**. The reasoning is what the researcher verifies. The agent marks a section `REPORTED`; only the researcher marks it `VERIFIED`, with a name and a date. Sections are rewritten as the research changes, raising their version and keeping the old paragraph with its reason.
- `brain.md` and the [data structure](docs/data-structure.md): typed statements (`CTX`, `PHN`, `THR`, `LIT`, `GAP`, `NOV`, `CTB`, `MTH`, `FND`, `DIS`, `LIM`, `CCL`, `IMP`) with upstream and downstream links, plus `DAT`, `PRM`, and `RUN` records for every data item, parameter set, and execution. The manuscript may only say what the brain holds, and the brain may only hold what a record supports.

**Reporting as parameters**

- `parameters/` with presets for the three search tracks and thirteen reporting standards: COREQ, SRQR, JARS-Qual, JARS-Quant, JARS-Mixed, STROBE, CONSORT, TREND, GRAMMS, PRISMA 2020, PLS-SEM, PRISMA 2020 for Abstracts, CONSORT for Abstracts.
- **A reporting standard is a parameter**, selected by the design at Stage 5 and verified as a checklist at FG4, so the standard cannot be chosen after the results are known. See [reporting standards](docs/reporting-standards.md).
- [Methodology sources register](docs/methodology-sources.md): specialist authorities by technique family, with the parameters each family must register — closing the "Creswell-first, not Creswell-only" gap that 0.2.0 left as an unkept promise.

**Writing**

- [Writing standards](docs/writing-standards.md): eleven characteristics of international research articles, each mapped to where the flow implements it, a comparison of the flow against established practice, and rules for figures and tables drawn from reputable-outlet conventions.
- [Title, abstract, and keywords](docs/abstract-and-title.md): title construction for Scopus and Web of Science indexing, the design-naming requirement of each reporting standard, abstracts governed by the design's own abstract checklist, and keyword selection that complements the title rather than repeating it. The abstract is assembled from registered statements, never written from memory; every number must match the run that produced it.
- Stage 8 drafts in evidence order — method, results, discussion, conclusion, introduction, abstract, title, keywords — so the framing is written against what the study did rather than what it hoped to do. The outlet's limits are recorded in the outline before drafting begins.

**Revision**

- Stage 9 and gate **FG5**, event-driven: it starts when reviewer comments arrive. See [revision](docs/revision.md). Comments are recorded verbatim in a [revision table](templates/revision-table.md), decomposed into `REV` points, each given the concern behind its wording (marked confirmed or inferred) and routed to the layer it hits. A point routed to design or framing reopens its flow gate and returns to that stage rather than being edited. Reviewer comments are material to be answered, not instructions to be executed. The [review response](templates/review-response.md) letter is built from the table after the changes exist.

**Templates and tooling**

- Ten new templates: GRO section, method decision record, manuscript outline, literature matrix, parameter set, reporting checklist, data record, data dictionary, run record, revision table.
- `scripts/coherence_report.py` prints the chain report: statement counts, record index, dangling and orphan identifiers, research-question coverage, findings without evidence, and statements missing links.
- Validator checks: every identifier referenced in `brain.md` or a record must resolve; GRO section numbers unique; GRO status vocabulary; a `VERIFIED` section must name a verifier and a date, so an agent cannot verify its own report; warnings for sections awaiting the researcher and for paragraphs over the word limit.

### Changed

- All fourteen existing templates carry the flow stages, typed statement IDs, and record links.
- Research questions are derived from the theoretical review **and** the novelty: the theory supplies the questions worth asking, the novelty decides which this study can answer. Every research question traces to a named gap.
- Journal quartile is a priority order for reading, never an eligibility or quality criterion. Appraisal stays per source.
- **Research outputs are written in English by default.** Another language is used only on an explicit instruction from the researcher or a requirement of the institution, outlet, or participants, recorded in the project brief. An agent does not switch the output language on its own or infer it from the language of the conversation. Source material stays in its original language.
- Findings are not compared with the literature until Stage 7, which is what keeps Results and Discussion from merging.
- Every skill states its place in the research flow. `research-workflow` owns GRO sections and brain synchronization; `research-writing` owns the outline, the title and abstract, and the revision table; `research-audit` checks GRO verification status and the revision table before assessing a gate.
- `AGENTS.md`, `README.md`, and the adapters now describe the mechanism explicitly — what triggers what, what each gate blocks, and where the researcher's judgment enters — so both a human reader and an agent can follow it from one document. The duplicate stage table in `README.md` was removed.
- Issue and PR templates carry the GRO section, the statement IDs, and the record IDs.
- Builder version bumped to 0.3.0.

### Known limits

- Reporting-checklist item wording in the presets is a **paraphrase for orientation**. Every project verifies each item against the official source and records the version used.
- Bibliography entries in the writing, reporting, and methodology registers are pointers, not verified metadata; they are checked before being cited in a manuscript.
- **No worked examples yet.** `examples/toy-research/` still demonstrates only the 0.2.0 provenance cycle. Tracked in issue #7.

### Migration

Projects on 0.2.0 should follow [0.2.0 → 0.3.0](docs/migrations/0.2.0-to-0.3.0.md). The migration adds process infrastructure; it does not invalidate an approved design or rewrite existing research artifacts. Backfilling the anchors is a recording exercise and must not become a retrospective rewrite.

## [0.2.0] - 2026-09-08

Creswell-first methodological decision layer.

### Added

- New `method/` knowledge layer grounded in Creswell & Creswell (2023).
- Explicit research-design flow from research problem and questions to worldview, approach, design, methods, and method-chapter drafting.
- Detailed qualitative, quantitative, and mixed-methods design guidance.
- AI method-selection protocol with human approval checkpoints and falsification checks.
- Practical method-chapter blueprint and method-input contracts.

### Changed

- `AGENTS.md` now requires the Creswell-first method layer before substantive methodology recommendations.
- `research-design` now uses Creswell & Creswell as the default research-design architecture while retaining specialist sources for technical methods.
- Research workflow, skill index, standards register, repository map, and project brief now reference the methodology layer.
- Builder version bumped to 0.2.0.

### Migration

Projects on 0.1.1 should follow [0.1.1 → 0.2.0](docs/migrations/0.1.1-to-0.2.0.md). Migration adds a methodological decision framework; it does not automatically invalidate or rewrite an already approved research design.

## [0.1.1] - 2026-09-07

Global-English documentation and multilingual research-output policy.

### Changed

- Repository documentation, skills, templates, examples, and project scaffolding are now written in English for global portability.
- Canonical placeholder/status tokens are now English: `NOT YET FILLED`, `NOT YET DECIDED`, `NOT YET VERIFIED`, `NOT ASSESSED`, `REVISION REQUIRED`, `READY`, and `NOT APPLICABLE`.
- The project brief now treats research-output language as a project-level decision rather than assuming Indonesian.
- `research-writing` and manuscript guidance explicitly support Indonesian, English, bilingual, and multilingual research outputs.
- The bootstrap script now targets the English project-brief schema.

### Migration

Projects on 0.1.0 should follow [0.1.0 → 0.1.1](docs/migrations/0.1.0-to-0.1.1.md). Existing research projects should not translate active empirical content merely to match the builder; the migration concerns builder instructions, scaffolding, and status vocabulary.

## [0.1.0] - 2026-09-07

First explicitly versioned builder baseline.

### Added

- Epistemic bounded-context Issue schema.
- Pull Request epistemic delta and layered verification.
- Mechanical repository-integrity checks in GitHub Actions.
- Formal SRC/STUDY/CLM/DEC/REV provenance model.
- Bibliographic identity and report–study lifecycle rules.
- Synthetic golden end-to-end research example.
- Diagnostic quality-gate structure and reopen rules.
- Cross-agent adapter files that redirect to the canonical `AGENTS.md`.
- Explicit MIT license and upstream attribution.
- Builder version and migration policy.

### Changed

- Local skills use the `research-*` namespace.
- `research-rigor` applies Karpathy-inspired execution discipline to research.
- README centers recoverable, bounded-context research rather than chat memory.

### Migration

Projects copied before versioning should follow [unversioned → 0.1.0](docs/migrations/unversioned-to-0.1.0.md). Existing research projects do **not** automatically inherit this version.
