# Local Skill Index

Open this repository in an AI development/research environment that can read project files. Skills are stored with the builder; no global installation is required. If automatic skill discovery is unavailable, open the linked SKILL.md manually and follow it.

| Skill | Use when | Typical output |
|---|---|---|
| [research-workflow](../.agents/skills/research-workflow/SKILL.md) | Starting/continuing an Issue, preserving context, preparing a PR, or closing work | Issue, checkpoint, branch/PR, integration trail |
| [research-rigor](../.agents/skills/research-rigor/SKILL.md) | Applying cross-stage guardrails for assumptions, parsimony, scope, falsification, and verification | Success criteria, scope boundaries, pass/blocked status, decision trail |
| [research-framing](../.agents/skills/research-framing/SKILL.md) | Clarifying the problem, questions, scope, or feasibility | Project brief/problem memo with explicit open decisions |
| [research-evidence](../.agents/skills/research-evidence/SKILL.md) | Designing or conducting search, screening, extraction, or appraisal | Protocol, logs, source notes, claim ledger |
| [research-theory](../.agents/skills/research-theory/SKILL.md) | Synthesizing debates and testing contribution candidates | Argument map, alternative explanations, novelty/contribution audit |
| [research-design](../.agents/skills/research-design/SKILL.md) | Selecting methodology, design, measurement, analysis, and execution requirements using the Creswell-first [`method/`](../method/README.md) decision layer | Methodological recommendation, design matrix, analysis plan, ethics/data plan |
| [research-writing](../.agents/skills/research-writing/SKILL.md) | Drafting or revising an evidence-based manuscript, including the title, abstract, and keywords | Manuscript outline, manuscript, title/abstract/keywords, completed reporting and abstract checklists |
| [research-audit](../.agents/skills/research-audit/SKILL.md) | Assessing quality, readiness, examination preparation, or a closed round of revision | Location/evidence-based review and follow-up actions |

A skill may be invoked by name, for example `$research-evidence`, when the environment supports it. A skill does not search databases or assess a manuscript merely by existing in the repository; it must be used within an actual task.

## Combining skills and respecting limits

Use `research-workflow` for coordination, apply `research-rigor` as the cross-stage execution discipline, and select the academic skill that matches the required output. The academic flow follows the ten stages of the [research flow](research-workflow.md): framing (context, phenomenon) → theory (theoretical review) → evidence (empirical literature review) → framing (state of the art, novelty, RQ) → design (method, results) → theory and writing (discussion, conclusion) → writing and audit (outline, manuscript) → writing and audit (revision), with iteration when evidence changes earlier decisions. Every skill registers the statements it produces in `brain.md`.

Do not load every skill at once. Read only what the active task requires.

Environment-specific document/PDF/spreadsheet capabilities may be used for artifacts that require them. Deep-research or scholarly connectors, when available and explicitly appropriate, may extend access; their outputs still require project-level verification and appraisal.

If a tool or source is unavailable, report the access limit and continue only the parts that can be performed honestly. Never claim a Scopus, Web of Science, ProQuest, or other database search that did not actually occur.
