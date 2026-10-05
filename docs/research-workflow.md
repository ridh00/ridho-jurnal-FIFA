# Research Flow

This is the operational research workflow of Better Research: ten stages, six flow gates, and two anchors. It is a project convention, not an external academic standard. Stages may repeat when evidence changes a decision; reopening a gate reopens everything downstream of it.

The flow is a chain. Each stage answers one question, and its answer is the input of the next stage. When one link is missing, the manuscript reads as disconnected: a theory that explains nothing, a gap that no question addresses, a finding that no conclusion uses.

```text
Context → Phenomenon → Theory → Gap → Novelty → RQ → Method → Findings → Dialogue → Conclusion → Manuscript
```

Three layers run at the same time:

| Layer | Content | Where |
|---|---|---|
| Research layer | Stages 0–8: the substance of the study | this document |
| Assessment layer | Quality gates G0–G7 bundled into flow gates FG0–FG5 | [quality gates](quality-gates.md) |
| Direction layer | GRO sections: one paragraph per part of the research outline, reported by the agent and verified by the researcher | [`GRO.md`](../GRO.md), [GRO rules](gro.md) |
| Operational layer | Issue → branch → PR → merge → checkpoint | [Git workflow](git-workflow.md) |

Two anchors hold the work together. [`GRO.md`](../GRO.md) answers *is the research going where the researcher wants* — eleven numbered sections following this outline, each a paragraph stating where that part is going and why, verified by the researcher section by section. [`brain.md`](../brain.md) answers *is the research internally consistent* — every statement typed, linked, and traceable to a record. A project can pass the second and fail the first, which is why both exist.

Coherence across the layers is kept in [`brain.md`](../brain.md): every statement the research makes is registered there with its upstream and downstream links, and every statement points to the records that support it (`SRC`, `DAT`, `PRM`, `RUN`, `DEC`). The [data structure](data-structure.md) defines those records. A manuscript may only say what the brain already holds, and the brain may only hold what a record supports.

In a RESEARCH project, every substantive task begins from an active Issue and follows the [Git workflow](git-workflow.md). File outputs enter `main` through PR, review, and merge. Save an Issue checkpoint at the end of a session and synchronize `brain.md` at the same time. Upstream TEMPLATE maintenance is not a research stage.

## Stage map

| Stage | Question the stage answers | Main output | Brain statements | Records | Skill | Gate |
|---|---|---|---|---|---|---|
| **0 Context** | What are the mandate, constraints, resources, and paradigm? | Project brief; paradigm statement | `CTX` | — | framing | G0 → **FG0** |
| **1 Phenomenon** | What is happening, where (locus), since when, and to whom? | Phenomenon description with locus evidence | `PHN` | `SRC` (search-online track), `DAT`, `PRM`, `RUN` | framing, evidence | feeds G1 |
| **2 Theoretical review** | Which theory can explain the phenomenon? | Theory map: one grand theory plus its developments; role of theory; constructs; theory gap | `THR`, `GAP` (theory) | `SRC` (theory track), `PRM`, `RUN` | theory, evidence | feeds G2, G3 |
| **3 Empirical literature review** | What has been studied, where, how, and with what result? | Literature matrix; synthesis patterns; research gap | `LIT`, `GAP` (research) | `SRC` (literature-review track), `PRM`, `RUN` | evidence | G2 |
| **4 State of the art, novelty, RQ** | Where is the frontier, where does this study stand, and what does it ask? | State-of-the-art statement; novelty; research questions; contribution statement; urgency and promised implications | `NOV`, `RQ`, `CTB`, `IMP` | — | framing, theory | G1, G3 → **FG1** |
| **5 Method** | How will the questions be answered defensibly? | Method decision record; design matrix; analysis plan; ethics/data plan; reporting standard as a parameter | `MTH` | `DEC`, `PRM` (including reporting), planned `DAT` | design | G4, G5 → **FG2** |
| **6 Results** | What did the data show, and does it answer every RQ? | Data presentation; interpretation; findings; RQ ↔ finding ↔ data matrix | `FND` | `DAT`, `RUN`, `PRM` | design, theory | G6 → **FG3** |
| **7 Discussion and conclusion** | What do the findings mean against theory and literature? | Findings versus theory; dialogue with literature; limitations; conclusions; implications delivered | `DIS`, `LIM`, `CCL`, `IMP` | — | theory, writing | feeds G7 |
| **8 Outline and writing** | Can the argument be traced and defended? | Manuscript outline; manuscript; title, abstract, keywords; completed reporting and abstract checklists | mapping only | `PRM` (reporting) | writing, audit | G7 → **FG4** |
| **9 Revision** | What do the reviewers actually want, and what changes answer it? | Revision table; changes with their justification; response letter | statements superseded or added | `REV`, plus any new `SRC`, `DAT`, `PRM`, `RUN` | writing, audit | reopens routed gates → **FG5** |

Templates for each stage are listed in the [template index](../templates/README.md). Copy a template only when its stage begins.

## Stage 0 — Context

- Record the researcher and project context: who is asking, the mandate, resources, constraints, and access to the locus.
- State the paradigm (postpositivist, constructivist, transformative, pragmatic — or another explicitly justified worldview) and the reason for it. It is declared here and confirmed again at FG2, once the research questions exist, because the method must be consistent with it.
- Output: project brief and `CTX` statements in the brain.
- **FG0 passes when** the context is verified, not assumed, and the paradigm is stated and explainable.

## Stage 1 — Phenomenon

- Define the phenomenon: what is happening, where (the locus), since when, and who is affected.
- Collect evidence that the phenomenon exists at the locus — reports, statistics, news, official documents — through online searching. Store the records in `literature/search-online/`, log every search run, and register the parameters used.
- Output: phenomenon description with locus evidence, registered as `PHN` statements. This is the direct material for the "general phenomenon → urgency" opening of the introduction.
- Locus evidence establishes that something is happening; it does not establish a research gap. Do not skip Stages 2–3 because the phenomenon feels urgent.

## Stage 2 — Theoretical review

- Purpose: find the theory that can explain the phenomenon. This stage looks for theory, not for empirical findings.
- **Grand theory:** one, read from its original source. Not limited by publication year.
- **Theory developments:** literature that extends, tests, or refines the grand theory, searched in Scopus (Q1–Q4) and Web of Science within the default ten-year window. The window and databases are parameters (`PRM`), recorded and justifiable, not fixed rules.
- **Role of theory:** state whether the theory serves as an interpretive lens, a hypothesis generator, or a set of sensitizing concepts. A theory that does no work in Stage 7 is decorative.
- **Derived constructs:** the variables or concepts the theory brings to the phenomenon. They are the basis of the keyword sets in Stage 3.
- Output: theory map (`THR`), theory gap (`GAP` with kind `theory`), construct list, and the questions the theory raises but has not answered for this phenomenon — the raw material of the research questions.
- Store records in `literature/theory/`.

## Stage 3 — Empirical literature review

- **Keywords:** generate a keyword set per construct and for the relations between constructs, from Stage 2. Register the set as a search parameter.
- **Search:** Scopus, default window five years, with journal quartile used as a **priority filter, not an eligibility criterion**. A quartile is a journal-level metric and says nothing about the quality of a specific article; appraisal happens per source in the source note. Adding Web of Science is recommended for parity with Stage 2. Record query, date, filters, and counts in the search log with a `RUN` ID.
- **Matrix:** author/year · context/locus · theory used · constructs · method · findings · limitations · **position in the debate**. Use the literature-matrix template.
- **Synthesis:** three to five patterns of what the literature agrees on, disagrees on, and has not examined — written as `LIT` statements, not as one summary per article.
- Output: research gap (`GAP` with kind `research`) traceable to the matrix.
- Store records in `literature/literature-review/`. Canonical works older than the window may be included with a recorded reason.

Stage 2 and Stage 3 differ in purpose (theory versus empirical studies), default window (ten versus five years), and output (theory gap versus research gap). Keep their records in separate tracks so the five-year matrix is not contaminated by theory sources.

## Stage 4 — State of the art, novelty, and research questions

- **State of the art** = Phenomenon × (Theoretical review + Empirical literature review): the current frontier of knowledge about this phenomenon.
- **Novelty** = the position of this study relative to the state of the art. It must address the theory gap, the research gap, or both. A new locus alone is not novelty.
- **Research questions** are derived from **the results of the theoretical review and from the novelty**: the theory supplies the questions worth asking; the novelty decides which of them this study is placed to answer. Every RQ must trace back to a named gap. Format the RQ according to the approach that will follow: a central question with sub-questions for qualitative work; hypotheses or precise questions for quantitative work; a quantitative question, a qualitative question, and an integration question for mixed methods.
- **Urgency and implications:** why now; theoretical implications (back to Stage 2) and practical implications (back to the locus of Stage 1). Implications are *promised* here as `IMP` statements and *delivered* in Stage 7.
- **Contribution statement:** one sentence, registered as `CTB`. It is reused, with variation, in the title, the abstract, the end of the introduction, and the discussion.
- **FG1 passes when** the chain Phenomenon → Theory → Gap → Novelty → RQ is connected without a jump **and relevant**: every link is actually needed to answer the RQ, and no theory or literature is riding along without a function.

FG1 is the gate most often skipped and the one that decides the study. A weak FG1 is not repaired by a strong method.

## Stage 5 — Method

The order of decisions is also the order of the method section:

1. **Approach** — derived from the paradigm (Stage 0) and the RQ (Stage 4).
2. **Method / design** — case study, survey, experiment, phenomenology, mixed-methods design, and so on, selected through the Creswell-first [method layer](../method/README.md) and the [method-selection protocol](../method/05-method-selection-protocol.md). The recommendation is recorded in a method decision record with status `PROPOSED`; only the researcher moves it to `APPROVED`.
3. **Data types** — primary and/or secondary, **following the design**, not the other way round.
4. **Data sources** — informants, respondents, documents, archives, databases. An AI assistant may help identify secondary sources that complement the primary data or serve as a basis for triangulation; the researcher verifies each source, and the assistance is recorded in the AI-use log.
5. **Data collection** — interviews, questionnaires, observation, documentation; instruments and procedures.
6. **Data analysis** — (a) data cleaning: keep only data within the focus of the RQ, record what was removed and why, as a cleaning parameter set and a run; (b) qualitative: for example thematic analysis of interviews (a default, not the only option), with source or method triangulation; (c) quantitative: validity and reliability tests **before** the main analysis; (d) a quality strategy appropriate to the approach (validity/reliability, trustworthiness, or integration quality).
7. **Ethics** — permissions, consent, confidentiality, storage.
8. **Reporting standard** — selected here according to the design and registered as a parameter set of type `reporting`, so that the manuscript can be checked against it in Stage 8. See the [reporting standards](reporting-standards.md).

Every parameter used at this stage (sampling, instrument, cleaning rules, analysis thresholds, reporting checklist) is a `PRM` record with a value, a justification, and a source. Thresholds without a justification are not parameters; they are habits.

- **FG2 passes when** paradigm, RQ, approach, method, data, and analysis are coherent; ethics and permission status match the planned activity; the reporting standard is registered; and the method decision record is `APPROVED`.

## Stage 6 — Results

- Generate the results: present the data after cleaning and triangulation, interpret it (stating the standpoint: theory, participant, or researcher), and formulate findings as `FND` statements.
- **RQ check:** complete the RQ ↔ finding ↔ data matrix in the brain. Every RQ must be answered by at least one finding; every finding must point to the `DAT` and `RUN` records behind it. A finding that answers no RQ is flagged — removed, or the RQ is revised through the decision log.
- Findings are **not** compared with the literature here. That is Stage 7. Separating the two is what keeps Results and Discussion from overlapping.
- **FG3 passes when** every RQ is answered by empirical findings traceable to data. **No manuscript outline is written before FG3 passes.**

## Stage 7 — Discussion and conclusion

- **Findings against theory (Stage 2):** for each finding, which theoretical statements are relevant to it and which are not, and why. The result is one of three categories per theory element: confirmed, extended, or not relevant/contradicted in this context. Record the outcome as `DIS` statements.
- **Dialogue with literature (Stage 3)**, in a fixed order: empirical finding → which literature it supports → where it differs or contradicts → why the difference arises → what this study adds → the limits of the interpretation. This is what makes the manuscript read as an international journal article: the data do not stand alone, the literature does not stand alone, and each tests the other.
- **Conclusion:** a conclusive answer to each RQ (`CCL`); limitations that name the inference they weaken and what was done about it (`LIM`); recommendations that follow from the limitations; an agenda for further research. Implications promised in Stage 4 are delivered here as `IMP` statements with the actor named.

## Stage 8 — Outline and writing

Written in English by default; another language only on an explicit instruction recorded in the project brief. Follow the [writing standards](writing-standards.md) and, for the title, abstract, and keywords, the [title and abstract rules](abstract-and-title.md).

**8a — Outline.** Section by section, then paragraph by paragraph, one topic sentence per paragraph, each paragraph naming the brain statements and records it will carry. Record the outlet's limits at the same time: word count, abstract type and limit, title cap, keyword count, and reference style. Use the [manuscript outline](../templates/manuscript-outline.md). Nothing is drafted before the outline is complete.

**8b — Draft in evidence order, not in reading order.** Draft the parts whose content is already settled first, so that the framing is written against what the study actually did rather than against what it hoped to do:

```text
Method → Results → Discussion → Conclusion → Introduction → Abstract → Title → Keywords
```

The introduction comes late because it promises what the rest delivers; writing it first is how a manuscript acquires promises the results never keep. The title and abstract come last because they summarize a settled argument, and they are assembled from the registered statements rather than written from memory.

**8c — Display items.** Decide which results need a table or a figure, design each to stand alone, and record for each the statement it supports and the `DAT` or `RUN` behind it. See the figures-and-tables rules in the [writing standards](writing-standards.md).

**8d — Checks before the gate.** Complete the reporting checklist registered at Stage 5 and the abstract checklist where the design has one. Audit claim verbs against the boundaries of inference in the method decision record. Check terminology against the outline: one term per concept throughout. Verify every number in the abstract against the results and the run that produced it. Then reverse-outline: read only the first sentence of each paragraph; if the argument is not readable from those sentences alone, the structure is not finished.

- **FG4 passes when** the chain RQ → findings → dialogue → conclusion is consistent; no claim exceeds the data; the reporting and abstract checklists are complete; claim verbs have been audited; the title, abstract, and keywords meet the outlet's requirements; and every outline paragraph maps to a statement.

## Stage 9 — Revision

Event-driven: it starts when reviewer comments arrive, from a journal, an editor, a supervisor, or an examiner. See the [revision rules](revision.md).

- **Intake.** The researcher uploads the comments as received. They are recorded verbatim in a [revision table](../templates/revision-table.md) — nothing summarized, softened, or reordered. Reviewer comments are material to be answered, not instructions to be executed.
- **Decomposition.** One `REV` point per discrete demand. A single reviewer paragraph routinely contains three, and they close at different times.
- **Concern.** For each point, what the reviewer wants underneath the wording. *"The sample seems small"* is usually a request for the sampling logic, not for more participants. Answering the wording while missing the concern is how a revision fails twice.
- **Routing.** Which layer the point hits — claim, design, evidence, framing, structure, reporting, or wording. A point routed to design or framing **reopens its flow gate** and returns to that stage before the manuscript is touched; it is not an editing task.
- **Decision and justification.** Accept, accept with modification, or decline with reason. Every one needs the reason the change answers the concern; that reason is what the response letter is built from.
- **Execution.** Changes trace as usual: statements superseded in `brain.md`, new records, rewritten GRO sections noting "in response to REV-###", gate reassessments that do not overwrite earlier ones, and the deviation log where a specified protocol changed.
- **Response letter.** Point by point in the reviewers' own numbering, quoting each comment, with a location the reviewer can check.
- **FG5 passes when** every point is `CLOSED` or `NOT IMPLEMENTED WITH REASON`, every reopened gate has a new assessment, the letter covers every point, the checklists still hold, and claim verbs have been re-audited — revisions frequently strengthen claims.

One Issue per revision round tracks the table to done. A second round opens a new table; the previous one is kept. Passing FG5 means the revision is ready to resubmit, not that it will be accepted.

## Manuscript structure and its sources

| Manuscript section | Content, in order | From stage |
|---|---|---|
| **Introduction** | General phenomenon → urgency · theoretical grounding · main problem · research gap · state of the art and novelty · RQ, implications, contribution statement | 1 · 2 · 1+2 · 3 · 4 · 4 |
| **Literature review** *(when a separate section is required)* | Grand theory → developments → matrix synthesis | 2 + 3 |
| **Method** | Approach · method/design · data types · data sources · collection · analysis · ethics | 5 |
| **Results** | Data presentation · interpretation · findings (skeleton = RQ ↔ finding matrix) | 6 |
| **Discussion** | Principal findings · findings versus theory · dialogue with literature · theoretical and practical implications | 7 |
| **Conclusion** | Answers to the RQ · limitations and recommendations · further research | 7 |
| **Statements** | Ethics · data availability · conflicts of interest · AI use | 5, AI-use log |
| **References** | Only cited sources · verified identifiers · theory from original sources | 2 + 3 |

Implications appear twice by design: promised in the introduction, delivered in the discussion and conclusion. Readers check whether the promise was kept.

## Flow gates

A flow gate is a hard stop. It bundles quality gates; it does not replace them. Each bundled gate is assessed with the [gate review](../templates/gate-review.md) at a defined scope and commit.

| Flow gate | Bundles | Passes when | Not allowed before it passes |
|---|---|---|---|
| **FG0 Context** | G0 | Context verified; paradigm stated | Framing statements treated as decided |
| **FG1 Framing** | G1, G2, G3 | Phenomenon → Theory → Gap → Novelty → RQ connected and relevant | Method selection; instrument design; data collection |
| **FG2 Method** | G4, G5 | Design coherent with paradigm and RQ; ethics and permissions real; reporting standard registered; method decision `APPROVED` | Data collection; analysis |
| **FG3 Findings** | G6 | Every RQ answered by findings traceable to data | Manuscript outline; results prose |
| **FG4 Manuscript** | G7 | Argument traceable; reporting and abstract checklists complete; claims calibrated; title, abstract, and keywords meet the outlet's requirements | Submission; export declared ready |
| **FG5 Revision** | the gates a reviewer point reopens, plus G7 | Every reviewer point closed with evidence or declined with reason; reopened gates reassessed; response letter complete | Resubmission |

A flow gate is recorded in `research/status.md` as the most conservative status among the gates it bundles. Reopening any bundled gate reopens the flow gate and every stage after it.

## Searching and access

Exploratory mapping may occur before a formal protocol. Do not retrospectively call an exploratory search "systematic" unless the process actually satisfies that claim. Record access limitations to databases; web search or AI recommendations do not prove comprehensive coverage.

Choose source types according to the question and discipline. Articles, monographs, archives, policy documents, datasets, dissertations/theses, and other primary sources can serve different functions across the three literature tracks. Not all evidence must be journal articles, and a journal quartile is not an appraisal.

For a structured review, specify deduplication, selection, extraction, disagreement resolution, appraisal, and synthesis procedures before relying on them — as parameters, so they can be inspected. If staffing limits independent review, report the practice actually used and its consequence.

## When to stop searching

Use stopping logic appropriate to the review design: complete planned searches, complete selection, address close prior work and counterevidence, record access limits, and define an update schedule. For iterative searching, document the basis for conceptual sufficiency. There is no universal article count that proves depth.

## Changes of direction

Record changes to concepts, methods, or research questions in the [decision log](../research/decision-log.md). Record deviations from an already specified protocol in the [deviation log](../research/deviation-log.md), including whether related results had already been seen. A materially changed statement receives a new ID in the brain with a `supersedes` link; the old statement is kept. Reopen affected gates.

## Gates and changing decision bases

Each stage is assessed through the [quality gates](quality-gates.md) at a particular scope and commit. If new evidence, a correction/retraction, an RQ change, a design change, or another material finding changes the basis of an earlier decision, reopen the affected gate and create a new assessment. Do not overwrite the old assessment.

## Glossary

Terms that appear in the flow, with the Indonesian working vocabulary many projects use:

| Term in this flow | Working equivalent | Meaning here |
|---|---|---|
| phenomenon | fenomena | the observable situation the study starts from |
| locus | lokus | the site, population, or setting where the phenomenon is observed |
| theoretical review | kajian teoretis | Stage 2: search for the theory that explains the phenomenon |
| empirical literature review | kajian literatur / tinjauan pustaka | Stage 3: search for what has been studied about it |
| state of the art | state of the art | the current frontier of knowledge about the phenomenon |
| novelty | novelty / kebaruan | the position of this study relative to the state of the art |
| dialogue with literature | dialog dengan literatur | Stage 7: findings and literature testing each other |
| flow gate | gate alur | a hard stop that bundles quality gates |
