# Data governance

No research data has been added yet. Complete the [ethics/data plan](../templates/ethics-data-plan.md) before introducing data into the project.

Default policy: raw data, processed participant-level data, consent records, and linkage keys are not tracked in Git. Use approved institutional storage and keep only non-sensitive documentation and safe version identifiers in the repository.

Public or non-sensitive data may be tracked only after usage rights, re-identification risk, and versioning requirements have been reviewed. Any exception to the default policy must be recorded in the decision log.

Never overwrite raw data. Document transformations, codebooks, units, missing-value conventions, access conditions, and provenance. Synthetic data used for training or demonstration must be clearly labeled and stored separately from empirical data.

A `.gitignore` rule does not remove data that has already entered Git history; pre-commit review is still required.
