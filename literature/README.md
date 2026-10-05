# Literature and evidence

[references.bib](references.bib) is the canonical store for verified bibliographic metadata. It starts empty so the builder does not introduce fictional references.

Use the [provenance model](../docs/provenance.md) to distinguish **report/source (SRC)**, **study (STUDY)**, **claim (CLM)**, **decision (DEC)**, and **review finding (REV)**.

Create these only when needed:

- `searches/`: search logs and permitted search exports.
- `screening/`: selection decisions and record–report–study relationships.
- `notes/`: one note per SRC using the source-note template.
- `claim-ledger.md`: claim–evidence relationships based on the template.

Licensed PDFs should be stored locally under `literature/pdfs/` (ignored by Git) or in approved institutional storage. Possessing a file does not imply permission to redistribute it.

## Identity and deduplication

One publication/report receives one SRC. Multiple reports may come from the same STUDY.

Example:

```text
STUDY-012
├── SRC-041 preprint
├── SRC-052 journal article
└── SRC-063 correction
```

Do not count these reports as three independent studies.

During deduplication, inspect at least DOI/identifier, title, authors, year, version, and the report–study relationship. Normalize DOI values without the `https://doi.org/` prefix and compare them case-insensitively.

## Citation keys

Default convention:

```text
authorYYYYshorttitle
```

Use lowercase ASCII without spaces. Add suffixes such as `a`, `b`, and so on only when collisions remain after making the short title sufficiently distinctive.

A citation key is a working identifier; it is not proof that two records are identical or different.

## Version lifecycle

A preprint, published article, correction, expression of concern, and retraction may be separate SRC records. Record the version actually read and link related reports in the source note.

If a published version supersedes a preprint, do not erase the preprint’s provenance. Reassess whether claims, locators, or appraisal need to be updated.

## Verification rule

Metadata enters `references.bib` only after it has been verified from a source that was actually accessed. The presence of a DOI or citation key does not prove that the source content supports a claim.

Human-readable reference lists should be generated from the bibliography once an export tool is configured. Do not maintain the same bibliographic metadata manually in multiple places.
