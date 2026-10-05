---
name: research-evidence
description: Design or conduct a transparent literature review through search, selection, extraction, appraisal, and claim-level evidence tracking.
---

# Evidence Search and Evaluation

Read the [academic integrity rules](../../../docs/academic-integrity.md), [research workflow](../../../docs/research-workflow.md), [standards register](../../../docs/standards.md), and the project brief. Select the mode: protocol only, search, selection, extraction/appraisal, or update. Do not perform stages that were not requested.

## Before structured searching

Use the [review protocol](../../../templates/review-protocol.md). Match the review form to the research question. Define concepts/terms, search sources, justified limits, inclusion/exclusion criteria, deduplication, appraisal, synthesis, and reviewer checks. Exploratory searching may refine the protocol; record those changes.

## While collecting evidence

- Record the exact query, platform/database, date, filters, actual counts, export files, and access limits in the [search log](../../../templates/search-log.md).
- Do not treat the number displayed by a platform as the number actually exported. Do not guess PRISMA counts.
- Distinguish bibliographic records, reports/publications, and studies. Link multiple reports from the same study so the sample/evidence is not double-counted.
- Store selection decisions and reasons in the [screening log](../../../templates/screening-log.md). Record how reviewers actually worked and how disagreements were actually resolved.
- Open the original source when accessible; use a [source note](../../../templates/source-note.md) for metadata, locators, context, design, sample/corpus, findings, and limitations.
- Findings from an abstract are limited to what the abstract reports. Unreported methods are unknown, not assumed to be sound.
- Choose appraisal tools according to design/tradition; name the tool and version or justify a custom framework. Assess by domain using evidence. Do not create arbitrary total scores or substitute journal reputation for appraisal.
- Add only verified metadata to the bibliography. Record corrections, retractions, and source versions.
- Link claims to supporting, contradicting, limiting, and contextualizing evidence in the [claim ledger](../../../templates/claim-ledger.md).

## Synthesis and closure

Group studies by debate, concept, design, context, and inferential boundary. Do not vote-count based on the number of statistically significant results. Meta-analysis requires compatibility of questions, effects, designs, and dependency handling; do not automatically pool every numeric result.

State the coverage actually achieved, unavailable sources, open decisions, and the rationale for stopping or updating the search. Do not exclude opposing evidence because it weakens the preferred model. AI output must be checked against source material; two AI runs are not two independent human reviewers.

## Place in the research flow

This skill serves Stages 1–3 of the [research flow](../../../docs/research-workflow.md) through three literature tracks with separate folders, parameter presets, windows, and outputs:

| Track | Folder | Preset | Default window | Output |
|---|---|---|---|---|
| search-online (Stage 1) | `literature/search-online/` | locus evidence | as the phenomenon requires | `PHN` evidence |
| theory (Stage 2) | `literature/theory/` | theory development | ten years; grand theory exempt | `THR`, theory `GAP` |
| literature-review (Stage 3) | `literature/literature-review/` | empirical literature | five years | matrix, `LIT`, research `GAP` |

- Every search step uses a registered `PRM` of type search and is logged with a `RUN` ID; screening criteria are a `PRM` of type screening.
- A journal quartile is a priority order for reading, never an eligibility or quality criterion; appraisal is per source. Canonical works outside a window may be included with a recorded reason.
- Keyword sets are generated per construct and per relation between constructs from the Stage 2 theory map.
- Stage 3 ends with the literature matrix, three to five `LIT` pattern statements, and research `GAP` statements — not with one summary per article.
- One source note per report, named by its `SRC` ID, in the folder of its track.

## Execution discipline

Apply the cross-skill principles in `research-rigor`: do not silently resolve uncertainty, use the minimum sufficient complexity, keep changes within task scope, and verify outcomes against explicit acceptance criteria. For high-impact claims or decisions, inspect counterevidence and alternative explanations before strengthening the conclusion.

## Evidence provenance

Use the [provenance model](../../../docs/provenance.md) to distinguish report/source (SRC), underlying study (STUDY), claim (CLM), decision (DEC), and review finding (REV). One report is not the same as one study. Every evidence–claim relation should record relation type, directness, access status, locator, and limits of use.
