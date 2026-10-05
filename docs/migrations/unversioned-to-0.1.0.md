# Migration: unversioned snapshot → 0.1.0

Use this only for research repositories copied from Better Research before a `VERSION` file existed.

## Before starting

Create an Issue in the research repository with:

- current commit and known builder age/source;
- local modifications to `AGENTS.md`, skills, templates, and docs;
- affected active Issues/PRs;
- acceptance criteria for migration;
- rollback plan.

Do not replace the repository wholesale.

## Changes introduced by 0.1.0

### Issue schema
New Issues distinguish KNOWN, SUPPORTED, INFERRED, ASSUMED, UNKNOWN, and DECISION NEEDED and require evidence, scope, success criteria, verification, and falsification/alternatives where relevant.

Existing Issues do not need cosmetic rewrites. Upgrade an active Issue when its current context is insufficient for reliable continuation.

### Pull Requests
PRs record an epistemic delta, provenance IDs, layered verification, and surgical-change checks.

### Provenance
The builder formalizes:

- SRC — report/source;
- STUDY — underlying study;
- CLM — claim;
- DEC — decision;
- REV — review finding.

Existing source notes and claim ledgers may remain until touched. When migrated, preserve old IDs and history.

### Quality gates
Gate reviews add evidence scope, critical-failure logic, and reopen triggers. Do not automatically convert prior READY assessments. Reassess only when the migration changes relevant evidence or criteria.

### Mechanical checks
GitHub Actions validate internal links, skill frontmatter, stale `dissertation-*` skill references, basic BibTeX structure, and prohibited sensitive paths. A mechanical PASS is not an academic PASS.

## Completion

Migration is complete when:

- `research/project-brief.md` records Builder: Better Research and Builder version: 0.1.0;
- required local customizations have been preserved;
- repository integrity checks pass;
- affected active Issues use enough of the new bounded-context schema to continue reliably;
- migration PR is merged and verified.

Record any intentionally deferred conversion work in a follow-up Issue rather than silently claiming full migration.
