# Data Structure and Coherence Anchor

Everything that enters a Better Research project is recorded, identified, and linked. Nothing is used in a statement without a record, and no statement enters the manuscript without being registered in [`brain.md`](../brain.md). This document defines the records, the identifiers, the folders, and the linking rules. It is a workspace convention.

## The brain model

The structure mirrors how information moves through a mind: it is perceived, stored, reasoned about, decided on, and expressed. Each layer has one home.

| Layer | What it holds | Home |
|---|---|---|
| Perception | Every data item that enters (`DAT`), every parameter used (`PRM`), every execution (`RUN`) | `data/records/`, `parameters/`, `analysis/runs/`, `literature/searches/` |
| Memory | Sources (`SRC`) in three literature tracks; theory map; literature matrix | `literature/` |
| Reasoning | Typed statements with upstream and downstream links | `brain.md` |
| Decision | Decisions (`DEC`), deviations, gate assessments (`REV`) | `research/`, `reviews/` |
| Expression | Manuscript outline and manuscript, each paragraph mapped to statements | `manuscript/` |

`brain.md` is the anchor. It does not hold the data; it holds the statements the data support and the links between them. Coherence is a property of the links: a statement with no upstream came from nowhere, and a statement with no downstream leads nowhere.

## Identifier grammar

```text
<TYPE>-<###>          e.g. a third finding is FND-003
<TYPE>-<TAG>-<###>    optional uppercase tag for sub-projects or synthetic examples
```

Numbers are zero-padded to at least three digits and are never reused. A materially changed statement receives a new ID and a `supersedes` link; the old statement stays, marked `RETRACTED` or `SUPERSEDED`. Create an ID only when a real unit enters the workspace.

### Statement types (live in `brain.md`)

| Prefix | Statement | Stage | Manuscript home |
|---|---|---|---|
| `CTX` | Context: mandate, constraint, paradigm | 0 | method (approach), statements |
| `PHN` | Phenomenon: what happens, where, since when, to whom | 1 | introduction opening |
| `THR` | Theory: what the grand theory or its developments assert about the phenomenon | 2 | introduction, literature review, discussion |
| `LIT` | Empirical literature pattern: what studies agree, dispute, or leave unexamined | 3 | introduction, literature review, discussion |
| `GAP` | Gap, with kind `theory` or `research` | 2–3 | introduction |
| `NOV` | State-of-the-art position and novelty of this study | 4 | introduction |
| `RQ` | Research question (existing identifier) | 4 | introduction, results, conclusion |
| `CTB` | Contribution statement | 4 | title, abstract, introduction, discussion |
| `MTH` | Method statement: a design decision expressed as a claim about how the RQ is answered | 5 | method |
| `FND` | Finding: an empirical result that answers an RQ | 6 | results |
| `DIS` | Discussion statement: a finding read against theory or literature | 7 | discussion |
| `LIM` | Limitation, naming the inference it weakens | 7 | discussion, conclusion |
| `CCL` | Conclusion: the answer to an RQ | 7 | conclusion, abstract |
| `IMP` | Implication, promised (Stage 4) or delivered (Stage 7), with the actor named | 4, 7 | introduction, discussion |
| `CLM` | Generic claim outside the chain (existing identifier) | any | any |

Every typed statement is a claim in the sense of the [provenance model](provenance.md). Wherever a template asks for a `CLM` ID, a typed statement ID is accepted.

### Record types (live as files named by their ID)

| Prefix | Record | Folder | Template |
|---|---|---|---|
| `SRC` | Source note: one per report read | `literature/theory/`, `literature/literature-review/`, `literature/search-online/` (or `literature/notes/` when no track applies) | [source note](../templates/source-note.md) |
| `DAT` | Data record: one per data item that enters the project | `data/records/` | [data record](../templates/data-record.md) |
| `PRM` | Parameter set: one per set of parameters used by a search, screening, sampling, instrument, cleaning, analysis, reporting, or export step | `parameters/` | [parameter set](../templates/parameter-set.md), [reporting checklist](../templates/reporting-checklist.md) |
| `RUN` | Execution record: one per search run, cleaning run, or analysis run | `analysis/runs/` (analysis and cleaning); search runs may remain rows in the search log | [run record](../templates/run-record.md) |
| `STUDY`, `DEC`, `REV` | Existing identifiers | source notes, decision log, reviews | see [provenance](provenance.md) |

The filename contains the ID: `data/records/DAT-001.md`, `parameters/PRM-004-reporting-coreq.md`, `analysis/runs/RUN-012.md`, `literature/theory/SRC-003.md`. A descriptive suffix after the ID is allowed.

## Folder layout

```text
.
├── brain.md                          coherence anchor: statements + links + chain checks
├── research/                         brief, status, decision/deviation/AI-use logs, framing memo
├── literature/
│   ├── search-online/                Stage 1: locus evidence (SRC notes, grey sources)
│   ├── theory/                       Stage 2: grand theory + developments (SRC notes, theory map)
│   ├── literature-review/            Stage 3: empirical sources (SRC notes, matrix)
│   ├── searches/                     search logs (RUN rows) and permitted exports
│   ├── screening/                    selection decisions
│   ├── claim-ledger.md               statement ↔ evidence relations
│   └── references.bib                verified bibliographic metadata
├── parameters/
│   ├── PRM-###*.md                   every parameter set actually used
│   └── presets/                      default parameter sets to copy (search windows, reporting checklists)
├── data/
│   ├── records/                      DAT-###.md — metadata for every data item (always in Git)
│   ├── dictionary/                   codebooks and data dictionaries
│   ├── safe/                         reviewed non-sensitive data only
│   ├── raw/  processed/  linkage/  consent/     NOT in Git (ignored and rejected by the validator)
├── analysis/
│   ├── analysis-plan.md
│   └── runs/                         RUN-###.md — cleaning and analysis executions
├── method/                           Creswell-first decision layer (builder-maintained)
├── manuscript/                       outline, chapter plans, canonical manuscript
├── reviews/                          gate reviews, review responses
├── exports/                          rendered outputs
├── templates/                        working forms
└── docs/                             workflow, standards, provenance, Git, migrations
```

## What each record must carry

### `DAT` — data record

Identity (ID, title, type: primary/secondary/locus-evidence/export/derived), origin (source or `RUN` that produced it), date, version, safe location (path outside Git when sensitive), sensitivity class, access and permission status, parameters used to obtain it (`PRM`), cleaning applied (`RUN`), dictionary (`data/dictionary/`), and the statements it supports. A data record is metadata; the data itself enters Git only under `data/safe/` after a recorded review.

### `PRM` — parameter set

Type, scope (which stage and artifact), and a table of parameters, each with **value, justification, source**. A value without a justification is not accepted at FG2. Types:

| Type | Typical parameters |
|---|---|
| `search` | databases, keyword sets per construct and relation, time window, quartile priority filter, language, document types |
| `screening` | inclusion/exclusion criteria, reviewer process, disagreement rule |
| `sampling` | population, frame, strategy, size logic, stopping logic |
| `instrument` | source instrument, adaptation, scale, validity/reliability targets |
| `cleaning` | exclusion rules, missing-data rule, outlier rule, focus rule ("within RQ scope") |
| `analysis` | software and version, model, estimator, thresholds (alpha, reliability cut-offs, fit indices), seed |
| `reporting` | reporting standard, version, and its item list as checklist rows |
| `export` | style, template, tool version |

**A reporting standard is a parameter.** Selecting COREQ, STROBE, PRISMA, or another standard is a Stage 5 decision recorded as a `PRM` of type `reporting`, created from the matching preset under `parameters/presets/reporting/`. Its rows become the checklist that FG4 verifies. See the [reporting standards](reporting-standards.md).

### `RUN` — execution record

What was executed (search, cleaning, analysis), when, by whom, with which `PRM`, on which input `DAT` or corpus version, producing which output `DAT` or result, with which check and any deviation. A `RUN` is the only legitimate origin of a derived `DAT` and of a quantitative or qualitative result cited by an `FND`.

## Linking rules

```text
PRM ──configures──> RUN ──produces──> DAT ──supports──> FND
SRC ──supports/contradicts/limits/contextualizes──> THR / LIT / DIS / any statement
GAP ──motivates──> NOV ──motivates──> RQ ──answered by──> FND ──read as──> DIS ──concludes──> CCL
CTB ──restated in──> title / abstract / introduction / discussion
IMP (promised) ──delivered by──> IMP (delivered)
DEC ──changes──> MTH / RQ / protocol / gate
LIM ──weakens──> a named CCL or IMP
```

Rules:

1. Every statement except `CTX` has at least one upstream link. Every statement except `CCL`, `LIM`, and delivered `IMP` has at least one downstream link.
2. Every `FND` lists at least one `DAT` or `RUN` as evidence and at least one `RQ` upstream.
3. Every `RQ` has at least one `FND` downstream before FG3 and at least one `CCL` before FG4.
4. Every `DIS` has at least one `FND` and at least one `THR` or `LIT` upstream.
5. Every `IMP` promised in Stage 4 is matched by a delivering `IMP` in Stage 7 or explicitly withdrawn.
6. Every `LIM` names the `CCL` or `IMP` it weakens.
7. Every manuscript paragraph in the outline maps to at least one statement.
8. An ID referenced anywhere in `brain.md` or in a record must exist. The validator rejects dangling references.

## `brain.md` protocol

- **One sentence per statement.** If it needs two sentences, it is two statements.
- **Status** uses the epistemic vocabulary: `KNOWN`, `SUPPORTED`, `INFERRED`, `ASSUMED`, `UNKNOWN`, `DECISION NEEDED`, plus `RETRACTED` and `SUPERSEDED` for withdrawn statements. Evidence-relation detail per source or data item stays in the claim ledger.
- **Evidence column** lists record IDs (`SRC`, `DAT`, `RUN`, `PRM`, `DEC`), never prose.
- **Sync** the brain at every Issue checkpoint, after every merge that changes a statement, and before every gate review. Record the commit in the header.
- **Coherence check** at the end of the file is completed before FG1, FG3, and FG4. It is a table, not a narrative.
- The brain is written in the project's research language; its structure and IDs stay as defined here.

## Mechanical checks

`python scripts/validate_repository.py` fails when an ID referenced in `brain.md`, a data record, a parameter set, or a run record does not resolve to a defined statement or an existing record file. It warns about records that nothing references.

`python scripts/coherence_report.py` prints the statement counts per stage, the ID index, dangling and orphan IDs, RQ coverage by findings, findings without evidence, and statements missing upstream or downstream links. A clean report is a mechanical result; it is not an academic quality gate.

## What must stay outside Git

Raw participant data, processed participant-level data, consent records, linkage keys, licensed PDFs, secrets. The data record points to their safe location; the record itself is committed. A private repository is not permission to commit them. Synthetic data used for examples is labeled as such and kept apart from empirical records.
