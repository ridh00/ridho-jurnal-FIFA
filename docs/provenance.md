# Provenance Model

Better Research uses local identifiers to keep the path **source → study → claim → decision → change/review** traceable. This model is a workspace convention, not an external bibliographic standard.

## Units and identifiers

| ID | Unit | Meaning |
|---|---|---|
| `SRC-###` | Source/report | One readable manifestation: article, preprint, chapter, document, dataset documentation, and so on |
| `STUDY-###` | Study | The underlying research/analysis represented by one or more reports |
| `CLM-###` | Claim | A statement used or tested in the project |
| `DEC-###` | Decision | A substantive project decision |
| `REV-###` | Review finding | An audit/review finding requiring a response |
| `RQ-###` | Research question | A research question with a stable identifier |
| `DAT-###` | Data record | One data item that entered the project: primary, secondary, locus evidence, derived, or export |
| `PRM-###` | Parameter set | The parameters used by a search, screening, sampling, instrument, cleaning, analysis, reporting, or export step |
| `RUN-###` | Execution record | One execution of a search, cleaning, or analysis step |
| typed statements | Statement in `brain.md` | `CTX`, `PHN`, `THR`, `LIT`, `GAP`, `NOV`, `CTB`, `MTH`, `FND`, `DIS`, `LIM`, `CCL`, `IMP` — claims typed by the research stage that produces them; see the [data structure](data-structure.md) |

Create an ID when a real unit enters the workspace. Do not create IDs merely to populate examples. A typed statement is a claim in the sense of this model; wherever a `CLM` ID is accepted, a typed statement ID is accepted. An optional uppercase tag may sit between the type and the number (`SRC-SYN-001`) for sub-projects or synthetic examples.

## Minimum relations

```text
SRC ──reports/derives-from──> STUDY
SRC ──supports/contradicts/limits/contextualizes──> CLM
CLM ──informs/challenges──> DEC
REV ──challenges/requires-change──> CLM / DEC / artifact
DEC ──changes──> RQ / protocol / design / manuscript / gate
PRM ──configures──> RUN ──produces──> DAT ──supports──> FND
GAP ──motivates──> NOV ──motivates──> RQ ──answered by──> FND ──read as──> DIS ──concludes──> CCL
```

The second and third lines are the statement chain of the [research flow](research-workflow.md); `brain.md` records every link. A reporting standard is a `PRM` of type `reporting`.

Every substantive relation should have a locator or an inspectable rationale.

## Claim status

Use one of these statuses in the claim ledger:

- `DRAFT` — candidate claim; insufficiently checked.
- `UNVERIFIED` — required source/support has not yet been verified.
- `SUPPORTED` — relevant support has been inspected and limits are recorded.
- `MIXED` — materially mixed support and counterevidence/heterogeneity.
- `CONTRADICTED` — inspected evidence materially contradicts the claim as currently stated.
- `RETRACTED` — the project has withdrawn the claim; it must not remain an active premise.

These statuses are not universal truth scores. They describe the evidence state **within the scope and corpus actually inspected**.

## Evidence-relation types

For every SRC/STUDY → CLM relation, use:

- `SUPPORTS`
- `CONTRADICTS`
- `LIMITS`
- `CONTEXTUALIZES`

Do not treat the number of SUPPORTS rows as a substitute for appraisal quality, design compatibility, or inferential strength.

## Directness and access status

**Directness**

- `DIRECT` — the referenced evidence/result directly bears on the claim.
- `INDIRECT` — relevance depends on an intermediate construct, context, or inference.
- `SECONDARY` — information is obtained through a secondary source.

**Access**

- `FULL_TEXT`
- `PARTIAL`
- `ABSTRACT_ONLY`
- `METADATA_ONLY`
- `UNAVAILABLE`

Do not upgrade directness because the result happens to support the preferred argument.

## Report versus study

One STUDY may have several reports:

```text
STUDY-012
├── SRC-041 preprint
├── SRC-052 journal article
└── SRC-063 correction
```

Do not count these as three independent studies. If two reports are discovered to represent the same study, keep both SRC records, link them to the same STUDY, and correct any synthesis affected by prior double counting.

## Version, correction, and retraction

Each source note records:

- the version actually read;
- verified DOI/URL or identifier;
- access date when relevant;
- relationship to preprint/published version/related report;
- known correction, expression of concern, or retraction status.

A new version does not erase the provenance of the old one. Record which report supersedes or corrects another.

## Citation identity

`literature/references.bib` is the canonical bibliographic metadata store. Default citation-key convention:

```text
authorYYYYshorttitle
```

Use lowercase ASCII without spaces. Add suffixes such as `a`, `b`, and so on only when a collision cannot be resolved through a clearer short title.

Example format only, not a real reference:

```text
santoso2025institutionaltrust
```

Identity rules:

1. Normalize DOI values without the `https://doi.org/` prefix and compare them case-insensitively.
2. A citation key is not proof of identity; DOI, title, author, year, and provenance still require verification.
3. A preprint and published article may have different citation keys/SRC records while mapping to the same STUDY.
4. A correction/retraction receives its own SRC record and relationship.
5. Metadata is not added to `references.bib` before it is verified from a source that was actually accessed.

## Decision provenance

A substantive decision records at least:

- the problem;
- alternatives;
- decision/status;
- supporting SRC/STUDY/CLM/REV identifiers;
- remaining assumptions/unknowns;
- affected artifacts and quality gates;
- the DEC it supersedes, if any.

A new decision **supersedes** an earlier decision; it does not erase it.

## Review provenance

A review finding uses `REV-###` and records location, evidence, impact, action, and closure verification. Closing a REV means that defined finding has been rechecked; it does not imply that the entire manuscript or gate is READY.

## Statement provenance

Every typed statement in `brain.md` records its status, the record IDs that support it (`SRC`, `DAT`, `RUN`, `PRM`, `DEC`), its upstream statements, its downstream statements, its manuscript location, and the gate that assesses it. A materially changed statement receives a new ID with a `supersedes` link; the old statement stays. The validator rejects a reference to an ID that does not exist; the coherence report lists dangling and orphan IDs.

## Rules of use

- Do not create an evidence relation without opening evidence consistent with the access status claimed.
- Do not change `UNVERIFIED` to `SUPPORTED` based only on an AI summary or bibliographic metadata.
- If a claim changes materially, retain the same CLM only when its intellectual identity is still the same; otherwise create a new CLM and record the supersedes/replaces relationship.
- Provenance changes that affect the argument, design, or inference must be reflected in the decision log and affected gates.
