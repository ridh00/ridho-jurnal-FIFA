# Decision Log

Record substantive decisions when they occur. Proposed decisions that have not been accepted should use status PROPOSED.

| ID | Date | Problem | Alternatives | Decision/status | Evidence basis | SRC/STUDY/CLM/REV | Remaining unknowns/assumptions | Responsible | Affected files/gates | Supersedes |
|---|---|---|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-09-07 | Builder identity and reuse model | Project-specific name or reusable builder identity | SUPERSEDED: initial builder identity used “Publion Dissertation Builder”; later renamed Better Research for general research use | User direction during builder development |  |  | User | README, project brief, standards register | superseded by later repository rename |
| DEC-002 | 2026-09-07 | Finite AI context and integration of final outputs | Conversation memory / optional Issue vs required bounded Issue with checkpoints and PR | DECIDED: RESEARCH projects require Issues; file outputs move through branch, PR, review, and merge | User direction; historical issue #1 |  |  | User | AGENTS, README, Git/session guidance, templates, workflow skill |  |
| DEC-003 | 2026-09-07 | Whether workflow rules also bind the upstream builder | Issue/PR for the entire repo vs only copied research projects | CLARIFICATION of DEC-002: TEMPLATE maintenance may be direct when explicitly authorized; RESEARCH projects require Issue/PR | Explicit user clarification |  |  | User | Workspace-mode rules and workflow guidance |  |
| DEC-004 | 2026-09-07 | Duplicate agent-instruction entrypoints | Multiple rule files vs one canonical entrypoint | DECIDED: `AGENTS.md` is the canonical instruction source; environment-specific files are thin adapters only | User direction and later portability design |  |  | User | AGENTS, adapters, README |  |
| DEC-005 | 2026-09-07 | Repository documentation language | Indonesian documentation vs globally portable English documentation | DECIDED: repository documentation, skills, templates, examples, and scaffolding are written in English; research-output language remains project-configurable | Explicit user direction |  | Research outputs may need Indonesian or multilingual formats | User | Repository-wide documentation; project language policy |  |

## Decision-provenance rules

See the [provenance model](../docs/provenance.md). A new decision does not erase an old one. Use **Supersedes** when a later decision replaces an earlier one, and link supporting SRC/STUDY/CLM/REV identifiers when available.
