# Brain — Coherence Anchor

Project: NOT YET FILLED.
Builder version: 0.3.0. Mode: TEMPLATE.
Last synced commit: NOT YET FILLED. Synced by: NOT YET FILLED.

> Every statement this research makes lives here first. The manuscript may only say what the brain already holds, and the brain may only hold what a registered record supports. Structure and identifiers follow the [data structure](docs/data-structure.md); the stages follow the [research flow](docs/research-workflow.md). Write the statements in the project's research language; keep the structure and IDs as defined.

## How the brain works

| Layer | What enters | Where it is recorded |
|---|---|---|
| Perception | data items, parameters, executions | `DAT` in `data/records/`, `PRM` in `parameters/`, `RUN` in `analysis/runs/` and the search log |
| Memory | sources, theory map, literature matrix | `SRC` notes in `literature/theory/`, `literature/literature-review/`, `literature/search-online/` |
| Reasoning | typed statements with upstream and downstream links | the tables below |
| Decision | decisions and gate assessments | `DEC` in the decision log, `REV` in `reviews/` |
| Expression | manuscript paragraphs mapped to statements | `manuscript/outline.md` and Stage 8 below |

Rules:

- One sentence per statement. Two sentences are two statements.
- An ID is never reused. A materially changed statement gets a new ID and names the one it supersedes; the old row stays with status `SUPERSEDED` or `RETRACTED`.
- Status is one of `KNOWN`, `SUPPORTED`, `INFERRED`, `ASSUMED`, `UNKNOWN`, `DECISION NEEDED`, `SUPERSEDED`, `RETRACTED`. Evidence-relation detail per source stays in the claim ledger.
- Evidence lists record IDs only (`SRC`, `DAT`, `RUN`, `PRM`, `DEC`), never prose.
- Every statement except a context statement has at least one upstream link; every statement except a conclusion, a limitation, or a delivered implication has at least one downstream link.
- Sync at every Issue checkpoint, after every merge that changes a statement, and before every gate review; record the commit above.
- The validator rejects any ID referenced here that does not exist. `python scripts/coherence_report.py` prints the chain report.

Statement table columns: ID · Statement · Status · Evidence · Upstream · Downstream · Manuscript · Gate · Supersedes.

## Stage 0 — Context (`CTX`)

Mandate, constraints, resources, access to the locus, and the paradigm with its reason. Confirmed again at FG2.

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Paradigm: NOT YET DECIDED. Reason: NOT YET FILLED.

## Stage 1 — Phenomenon (`PHN`)

What is happening, where (locus), since when, and to whom. Evidence comes from the search-online track and registered data records.

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Locus: NOT YET FILLED.

## Stage 2 — Theory (`THR`) and theory gaps (`GAP`)

Grand theory: NOT YET FILLED (original source `SRC`: NOT YET FILLED). Role of theory: NOT YET DECIDED (lens / hypothesis generator / sensitizing concepts). Developments searched with parameter set: NOT YET FILLED.

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Constructs derived from the theory (basis of the Stage 3 keyword sets):

| Construct | Definition (one line) | From `THR` | Keyword parameter set |
|---|---|---|---|

Theory gaps — what the theory has not explained or tested for this phenomenon:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

## Stage 3 — Empirical literature patterns (`LIT`) and research gaps (`GAP`)

Matrix: `literature/literature-review/matrix.md`. Search parameter set: NOT YET FILLED. Screening parameter set: NOT YET FILLED.

Patterns — what the literature agrees on, disputes, or has not examined (three to five statements, not one per article):

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Research gaps — what has not been studied, in which context, with which method:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

## Stage 4 — State of the art, novelty (`NOV`), research questions (`RQ`), contribution (`CTB`), implications promised (`IMP`)

State of the art = Phenomenon × (Theory + Literature): NOT YET FILLED.

Novelty — the position of this study relative to the state of the art; it must answer a theory gap, a research gap, or both:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Research questions — derived from the theoretical review and the novelty; each traces to a named gap; format follows the approach (central question and sub-questions; hypotheses; quantitative, qualitative, and integration questions):

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Contribution statement — one sentence, restated in the title, abstract, end of introduction, and discussion:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Implications promised — theoretical (to Stage 2) and practical (to the locus), each with the actor named; every promised implication is delivered or withdrawn in Stage 7:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Urgency — why now: NOT YET FILLED.

FG1 check — the chain Phenomenon → Theory → Gap → Novelty → RQ is connected without a jump and relevant: NOT ASSESSED.

## Stage 5 — Method (`MTH`)

Method decision record: NOT YET FILLED (status `PROPOSED` / `APPROVED`). Paradigm confirmed against the RQ: NOT ASSESSED. Reporting standard parameter set(s): NOT YET FILLED.

Method statements follow the decision order — approach, method/design, data types, data sources, collection, analysis (including cleaning), ethics — and link the `DEC` and `PRM` records behind them:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Claims this design can support: NOT YET FILLED. Claims this design cannot support: NOT YET FILLED.

## Stage 6 — Findings (`FND`)

A finding is an empirical result that answers a research question. It is not compared with the literature here.

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

RQ ↔ finding ↔ data matrix — every RQ answered, every finding traceable:

| RQ | Answered by (`FND`) | Data and runs (`DAT`, `RUN`) | Interpretation standpoint (theory / participant / researcher) | Answered? |
|---|---|---|---|---|

FG3 check — every RQ is answered by findings traceable to data: NOT ASSESSED. No manuscript outline before this is READY.

## Stage 7 — Discussion (`DIS`), limitations (`LIM`), conclusions (`CCL`), implications delivered (`IMP`)

Findings against theory — for each theory statement: confirmed, extended, or not relevant/contradicted in this context:

| `THR` | Read against (`FND`) | Outcome | `DIS` |
|---|---|---|---|

Discussion statements — dialogue with literature in order: finding → supports which `LIT` → differs where → why → what this study adds → limit of interpretation:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Conclusions — one per research question:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Limitations — each names the conclusion or implication it weakens and what was done about it:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Implications delivered — matched to the implications promised in Stage 4, actor named:

| ID | Statement | Status | Evidence | Upstream | Downstream | Manuscript | Gate | Supersedes |
|---|---|---|---|---|---|---|---|---|

Further research — follows from the limitations: NOT YET FILLED.

## Stage 8 — Manuscript map

Outline: `manuscript/outline.md` (written only after FG3 is READY). Each paragraph in the outline names the statements it carries; this table records where the contribution statement and the research questions appear.

| Statement | Title | Abstract | Introduction | Method | Results | Discussion | Conclusion |
|---|---|---|---|---|---|---|---|

Terminology — one term per concept across all sections:

| Concept | Term used | Rejected variants |
|---|---|---|

## Coherence check

Complete before FG1, FG3, and FG4. Status: PASS / FAIL / NOT ASSESSED, with the IDs affected.

| Check | Rule | Status | IDs affected |
|---|---|---|---|
| Phenomenon feeds forward | every `PHN` has a downstream `THR`, `GAP`, or `NOV` | NOT ASSESSED | |
| Theory does work | every `THR` is used by a `DIS` in Stage 7 or explicitly found not relevant | NOT ASSESSED | |
| Gaps are motivated | every `GAP` has upstream `THR` or `LIT` and downstream `NOV` or `RQ` | NOT ASSESSED | |
| Questions are grounded | every `RQ` has upstream `GAP` and `NOV` | NOT ASSESSED | |
| Questions are answered | every `RQ` has at least one `FND` (FG3) and one `CCL` (FG4) | NOT ASSESSED | |
| Findings have evidence | every `FND` lists at least one `DAT` or `RUN` | NOT ASSESSED | |
| Discussion is a dialogue | every `DIS` has upstream `FND` and `THR` or `LIT` | NOT ASSESSED | |
| Promises are kept | every promised `IMP` has a delivering `IMP` or a recorded withdrawal | NOT ASSESSED | |
| Limitations bite | every `LIM` names the `CCL` or `IMP` it weakens | NOT ASSESSED | |
| Method traces | every `MTH` links a `DEC` or `PRM` | NOT ASSESSED | |
| Manuscript is mapped | every paragraph in the outline maps to at least one statement | NOT ASSESSED | |
| No dangling links | validator passes; coherence report shows no dangling or orphan IDs | NOT ASSESSED | |

A PASS here is a mechanical and structural result. It is not an academic quality gate; those are assessed in `reviews/`.
