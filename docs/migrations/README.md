# Builder Migrations

Better Research projects pin the builder version they were created from. A research repository does not automatically become compatible with the latest builder merely because upstream changed.

## Rules

1. Record the builder version in `research/project-brief.md`.
2. Never overwrite local research decisions, source notes, data-governance rules, or manuscript changes during a builder upgrade.
3. Upgrade through an explicit Issue and PR in the **research repository**.
4. Read every migration note between the current and target versions.
5. Treat changed skill behavior, quality gates, provenance schema, templates, and canonical status vocabulary as potentially substantive.
6. Reopen affected quality gates when a migration changes assumptions or criteria used by an earlier assessment.
7. Keep the old builder version in Git history; do not rewrite history to make the project appear as if it always used the new rules.
8. A documentation-language migration does **not** require translating empirical research artifacts unless the project itself chooses to do so.

## Available migrations

- [Unversioned snapshot → 0.1.0](unversioned-to-0.1.0.md)
- [0.1.0 → 0.1.1](0.1.0-to-0.1.1.md)
- [0.1.1 → 0.2.0](0.1.1-to-0.2.0.md)
- [0.2.0 → 0.3.0](0.2.0-to-0.3.0.md)

A builder upgrade is a workflow/configuration change. It is not evidence that the underlying research has improved.
