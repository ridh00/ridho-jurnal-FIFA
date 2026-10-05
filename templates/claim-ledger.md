# Claim and Evidence Ledger

One row in the evidence-relations table represents **one evidence → statement relationship**, not an entire statement. A single statement may have many evidence rows and many sources. Statements are registered in `brain.md` with typed IDs (`PHN`, `THR`, `LIT`, `GAP`, `NOV`, `RQ`, `CTB`, `MTH`, `FND`, `DIS`, `LIM`, `CCL`, `IMP`); `CLM-###` remains for claims outside the chain. See the [provenance model](../docs/provenance.md).

## Claim registry (claims outside the brain chain)

| `CLM` | Exact claim | Claim type | Claim status | Manuscript location | Supersedes/replaced by | Notes |
|---|---|---|---|---|---|---|

Claim status: DRAFT / UNVERIFIED / SUPPORTED / MIXED / CONTRADICTED / RETRACTED.

Claim type: empirical, theoretical, conceptual, normative, or researcher inference.

## Evidence relations

| Statement or `CLM` | Evidence (`SRC`, `DAT`, or `RUN`) | `STUDY` | Relation | Directness | Access | Locator | Appraisal / evidence quality & limits | Source version/status | Action |
|---|---|---|---|---|---|---|---|---|---|

Relation: SUPPORTS / CONTRADICTS / LIMITS / CONTEXTUALIZES.

Directness: DIRECT / INDIRECT / SECONDARY.

Access: FULL_TEXT / PARTIAL / ABSTRACT_ONLY / METADATA_ONLY / UNAVAILABLE (for `DAT` and `RUN`, record the safe location instead).

Action: retain, qualify, seek more evidence, split the statement, or retract.

## Statement-level synthesis

For a substantive statement, summarize after inspecting the evidence relations:

| Statement or `CLM` | Supporting pattern | Counterevidence | Alternative explanation | Boundary conditions | Remaining unknown | Decision/`DEC` |
|---|---|---|---|---|---|---|

Do not treat the number of sources as an automatic measure of evidence strength. A real source may still fail to support the statement, and several reports may belong to the same STUDY.
