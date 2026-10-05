# Working templates

Copy a template into its working location only when that stage begins. Replace `NOT YET FILLED` with information supported by evidence; empty tables intentionally contain no example data. Direction is reported to the researcher in [`GRO.md`](../GRO.md) under the [GRO rules](../docs/gro.md). Records and statements follow the [data structure](../docs/data-structure.md) and the [provenance model](../docs/provenance.md); the stage order follows the [research flow](../docs/research-workflow.md). Every statement a template produces is registered in [`brain.md`](../brain.md).

| Stage | Template | Working location | IDs produced or used |
|---|---|---|---|
| any | [GRO section](gro-entry.md) | GRO.md (one section per part of the outline) | cites all IDs |
| any | [Session checkpoint](session-checkpoint.md) | Issue comment and body snapshot; temporary local file if GitHub is unavailable | — |
| 1–4 | [Problem memo](problem-memo.md) (framing memo) | research/problem-memo.md | `PHN`, `GAP`, `NOV`, `RQ`, `CTB`, `IMP` |
| 1–3 | [Parameter set](parameter-set.md) | parameters/PRM-###.md | `PRM` |
| 1–3 | [Search log](search-log.md) | literature/searches/ | `RUN`, `PRM` |
| 1–3 | [Source note](source-note.md) | literature/search-online/, literature/theory/, literature/literature-review/ (one note per `SRC`) | `SRC`, `STUDY` |
| 2 | [Theory map and contribution audit](theory-contribution.md) | literature/theory/theory-map.md | `THR`, `GAP`, `CTB` |
| 3 | [Review protocol](review-protocol.md) | research/review-protocol.md | `PRM` |
| 3 | [Screening log](screening-log.md) | literature/screening/ | `PRM`, `RUN` |
| 3 | [Literature matrix](literature-matrix.md) | literature/literature-review/matrix.md | `LIT`, `GAP` |
| 3–8 | [Claim ledger](claim-ledger.md) | literature/claim-ledger.md | any statement, `SRC`, `DAT`, `RUN` |
| 5 | [Method decision record](method-decision-record.md) | research/method-decision-record.md | `MTH`, `DEC`, `PRM` |
| 5 | [Design matrix](design-matrix.md) | research/design-matrix.md | `RQ`, `MTH`, `PRM` |
| 5 | [Analysis plan](analysis-plan.md) | analysis/analysis-plan.md | `PRM`, `RUN`, `DAT`, `FND` |
| 5 | [Ethics and data plan](ethics-data-plan.md) | research/ethics-data-plan.md | `DAT` |
| 5, 8 | [Reporting checklist](reporting-checklist.md) | parameters/PRM-###-reporting-\<standard\>.md | `PRM` |
| 5–6 | [Data record](data-record.md) | data/records/DAT-###.md | `DAT` |
| 5–6 | [Data dictionary](data-dictionary.md) | data/dictionary/ | `DAT` |
| 6 | [Run record](run-record.md) | analysis/runs/RUN-###.md | `RUN` |
| 8 | [Manuscript outline](manuscript-outline.md) | manuscript/outline.md | all statements; outlet limits, drafting order, title, abstract, keywords |
| 8 | [Chapter plan](chapter-plan.md) | manuscript/ | statements |
| any | [Gate review](gate-review.md) | reviews/ | `REV` |
| 9 | [Revision table](revision-table.md) | reviews/YYYY-MM-DD-revision-round-N.md | `REV`, plus statements and records changed |
| 9 | [Review response](review-response.md) | reviews/YYYY-MM-DD-response-round-N.md | `REV` |

The identifiers are local traceability conventions, not external academic standards. Reporting-standard checklists are copied from [`parameters/presets/reporting/`](../parameters/presets/README.md); search defaults from [`parameters/presets/search/`](../parameters/presets/README.md).
