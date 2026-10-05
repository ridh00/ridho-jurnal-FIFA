# Better Research

Builder version: **0.3.0** · [Changelog](CHANGELOG.md) · [Migration policy](docs/migrations/README.md) · [MIT License](LICENSE)

> **Do not ask AI to remember your entire research project. Build a system that makes research context recoverable.**

**Better Research** is a Git-based research workspace for designing, conducting, writing, and defending research with AI — without treating chat history as the project's memory.

Research runs through ten stages, each answering one question whose answer is the next stage's input:

```text
Context → Phenomenon → Theory → Gap → Novelty → RQ → Method → Findings → Dialogue → Conclusion → Manuscript → Revision
```

Six gates stop the work from running ahead of its evidence. Two anchors keep it inspectable: [`GRO.md`](GRO.md) reports **where the research is going and why**, for you to verify; [`brain.md`](brain.md) keeps every statement linked to the record that supports it. Everything enters `main` through a Pull Request that a validator has checked.

This repository is the reusable **builder**. Initial state: **ready to use; no substantive research has started.**

---

## Why it exists

AI context is finite. Serious research is not. A project can span years and accumulate hundreds of sources, decisions, revisions, analyses, and changes of direction. If that state lives only inside conversations, some of it will be lost, mixed together, or reconstructed wrongly.

The main failure mode of AI-assisted research is not only hallucination. It is **context drift**. Across a long project an agent may forget earlier decisions, mix evidence from different sources or versions, change theories or variables without tracking the consequences, strengthen a claim because it sounds plausible, add complexity that nothing requires, rewrite whole sections when one argument needed revision, or call work "complete" while evidence, ethics, or review remain unresolved.

Better Research does not try to fix this with a longer prompt. It changes the **architecture of the work**:

> One task has one bounded context. One substantive change has one reason. One claim has a traceable evidence path. One decision has a history. One output enters `main` only after it can be inspected.

---

## How it works

### The flow — ten stages

Each stage answers one question. When a link in the chain is missing, the manuscript reads as disconnected: a theory that explains nothing, a gap no question addresses, a finding no conclusion uses.

| Stage | Question it answers | Main artifact | Statements | Gate |
|---|---|---|---|---|
| **0** Context | What are the mandate, constraints, resources, and paradigm? | Project brief | `CTX` | FG0 |
| **1** Phenomenon | What is happening, where (locus), since when, to whom? | Locus evidence | `PHN` | |
| **2** Theoretical review | Which theory explains it, and what has it not explained? | Theory map | `THR`, theory `GAP` | |
| **3** Empirical literature review | What has been studied, where, how, with what result? | Literature matrix | `LIT`, research `GAP` | |
| **4** State of the art, novelty, RQ | Where does this study stand, and what does it ask? | Problem memo | `NOV`, `RQ`, `CTB`, `IMP` | FG1 |
| **5** Method | How will the questions be answered defensibly? | Method decision record, design matrix, analysis plan, ethics plan | `MTH` | FG2 |
| **6** Results | What did the data show, and does it answer every question? | RQ ↔ finding ↔ data matrix | `FND` | FG3 |
| **7** Discussion and conclusion | What do the findings mean against theory and literature? | Dialogue with the literature | `DIS`, `LIM`, `CCL`, `IMP` | |
| **8** Outline and writing | Can the argument be traced and defended? | Outline, manuscript, title, abstract, keywords | mapping | FG4 |
| **9** Revision | What do the reviewers actually want, and what answers it? | Revision table, response letter | `REV` | FG5 |

Three separations the flow enforces rather than leaving to discipline:

- The **theoretical review** looks for theory (ten-year window); the **empirical literature review** looks for studies (five-year window). Different tracks, different folders, different outputs — mixing them is how two distinct gaps become one vague gap.
- **Research questions derive from the theoretical review *and* the novelty.** The theory supplies the questions worth asking; the novelty decides which this study can answer. Each traces to a named gap.
- **Findings are not compared with the literature until Stage 7.** That separation is what keeps Results and Discussion from merging into each other.

Stages repeat when evidence changes an earlier decision. Full detail: [`docs/research-workflow.md`](docs/research-workflow.md).

### The gates — six hard stops

Flow gates bundle the quality gates G0–G7 into stops you cannot work past:

| Before this can happen | This must have passed |
|---|---|
| selecting a method, designing an instrument, collecting data | **FG1** framing |
| running an analysis | **FG2** method |
| writing a manuscript outline or any results prose | **FG3** findings |
| submitting | **FG4** manuscript |
| resubmitting after review | **FG5** revision |

A flow gate takes the most conservative status among the gates it bundles, and reopening any of them reopens every stage after it. An agent cannot mark a gate itself: a gate is assessed against evidence, recorded in `reviews/`, and its earlier assessment is never overwritten.

### The two anchors

They answer different questions, and a project can pass one while failing the other.

**[`GRO.md`](GRO.md) — the Grand Research Outline — answers *is the research going where I want it to go?*** It is the report the AI writes for you: one numbered section per part of the research outline, each a single paragraph stating where that part is going **and why**.

```text
GRO-01  Introduction ......... the study addresses this, at this locus, because …
GRO-02  Grand theory ......... this theory was chosen because …
GRO-03  Literature and gap ... the literature shows this, so the gap is …
GRO-04  Novelty .............. this study stands here because …
GRO-05  Research questions ... the questions are phrased this way because …
GRO-06  Method ............... this design was chosen because …
GRO-07  Data and analysis .... the data comes from here, analyzed this way, because …
GRO-08  Findings ............. the data shows this …
GRO-09  Discussion ........... against theory and literature this means …
GRO-10  Conclusion ........... the answer to the questions is …
GRO-11  Manuscript ........... the argument is arranged this way because …
```

The reasoning is the part that matters, because it is what you verify. A section that says *what* was decided without *why* has reported nothing. The agent marks a section `REPORTED`; **only you mark it `VERIFIED`**, with your name and the date. Read top to bottom, the file is the whole study as a sequence of reasoned decisions. See [`docs/gro.md`](docs/gro.md).

**[`brain.md`](brain.md) answers *is the research internally consistent?*** Every statement the research makes is registered with a typed ID, its status, the records that support it, and its links up and down the chain. Every data item that enters has a `DAT` record, every parameter a `PRM` record, every execution a `RUN` record.

```text
PRM ──configures──> RUN ──produces──> DAT ──supports──> FND
GAP ──motivates──> NOV ──motivates──> RQ ──answered by──> FND ──read as──> DIS ──concludes──> CCL
```

The manuscript may only say what the brain holds, and the brain may only hold what a record supports. The validator rejects any link to an identifier that does not exist. See [`docs/data-structure.md`](docs/data-structure.md).

### The mechanism

```text
you ask for work on a stage
        ↓
agent reads GRO.md (where the research is going)
           brain.md (what it has established)
           the Issue (what this task is)
        ↓
agent works inside one stage, within the Issue scope
        ↓
registers statements in brain.md, each linked to the records behind it
        ↓
writes or rewrites the GRO section for that part:
   the direction, and why  →  REPORTED
        ↓
opens a PR — the validator checks that every identifier resolves
        ↓
YOU read one paragraph and either VERIFY it or ask for a different direction
        ↓
at a flow gate, an audit assesses the bundled quality gates against evidence
        ↓
gate passes → next stage        gate fails → back to this stage
```

Four properties fall out of this, and they are the whole point:

**Nothing is claimed without a record.** A finding cites the run that produced it; a parameter carries its justification and source; a statement with no evidence stays `UNKNOWN` rather than being written confidently.

**You see direction before it becomes work.** The GRO section for a part is written as that part is decided, not after the chapter is drafted, so a wrong turn costs a paragraph instead of a month.

**Changing your mind is cheap and visible.** A revised section raises its version, keeps the old paragraph with the reason, and names the downstream sections it puts back in question. A study whose direction changed is normal; one whose history was tidied to look as if it never changed is not.

**Reviewer comments can change the research, not only the text.** In Stage 9 each comment is decomposed into points, given the concern behind its wording, and routed to the layer it hits. A point that challenges the design reopens FG2 and goes back to Stage 5 — treating it as an editing task is the most common way a revision fails twice.

---

## Methodology decisions

Methodology is not chosen at the start, and it is not chosen from a technique. The decision runs in this order, and each step constrains the next:

```text
research problem
        ↓
purpose / study aim
        ↓
research questions
        ↓
philosophical worldview
        ↓
approach — qualitative / quantitative / mixed methods
        ↓
research design
        ↓
sampling · data collection · analysis
        ↓
validity / validation / integration
        ↓
method section
```

### The checklist

Every recommendation is tested against these before it reaches you:

- **The problem comes first.** A requested technique — SEM, PLS-SEM, interviews, thematic analysis, mixed methods — is a *proposal*, not an approved design. It is restated as one and diagnosed from the research problem.
- **A design is not an analysis technique.** A nonexperimental survey is a design; SEM is a technique applied within it, and it needs its own justification and its own specialist source.
- **Minimum sufficient complexity.** The least complex design that can answer the question. Complexity is not a quality signal.
- **Causal language only where the design earns it.** Observational evidence supports association, prediction, description, or interpretation. Good model fit is not evidence of causation.
- **Qualitative labels must have procedural consequences.** No phenomenology without a lived-experience aim, no grounded theory without theory generation, no ethnography without a culture-sharing focus, no case study without a bounded case.
- **Mixed methods requires integration.** A reason one strand is insufficient, an integration point, a procedure, and an expected meta-inference. Two datasets that never interact analytically are not mixed methods.
- **Alignment is explained, never asserted.** A worldview, design, or method is called aligned only when the relationship can be stated.
- **Unknowns stay unknown.** Missing fields are surfaced, not filled with plausible academic prose.
- **The recommendation stops at `PROPOSED`.** Only you move a methodological decision to `APPROVED`. An agent never approves its own recommendation.
- **Every threshold is a parameter** with a value, a justification, and a source. A cut-off without a source is a habit, not a decision.

The operational decision layer — the full flow, the selection protocol, the qualitative, quantitative, and mixed-methods logic, the method-chapter blueprint, and the sources it rests on — lives in [`method/`](method/README.md). Where a study moves past design architecture into a technical procedure, the [methodology sources register](docs/methodology-sources.md) names the authority to use and the parameters that family must register.

---

## Evidence and provenance

### Three literature tracks

Each has its own folder, search preset, default window, and output:

| Track | Looks for | Window | Produces |
|---|---|---|---|
| `literature/search-online/` | evidence the phenomenon exists at the locus | as the phenomenon requires | `PHN` evidence |
| `literature/theory/` | the grand theory and its developments | ten years; the grand theory itself exempt | `THR`, theory `GAP` |
| `literature/literature-review/` | empirical studies of the phenomenon | five years | matrix, `LIT`, research `GAP` |

Every search is configured by a registered parameter set and logged as a run — query verbatim, date, filters, counts displayed and exported. A journal quartile is a **priority order for reading, never an eligibility or quality criterion**; appraisal stays per source.

### Identifiers

```text
SRC (report/source)  ──reports/derives from──>  STUDY
SRC / DAT / RUN      ──supports · contradicts · limits · contextualizes──>  a statement
statement            ──informs / challenges──>  DEC (decision)
DEC                  ──changes──>  RQ / protocol / design / manuscript / gate
REV (review finding) ──challenges──>  a statement, a decision, or an artifact
```

Statements are typed by the stage that produced them (`PHN`, `THR`, `LIT`, `GAP`, `NOV`, `RQ`, `CTB`, `MTH`, `FND`, `DIS`, `LIM`, `CCL`, `IMP`) and carry a status: `KNOWN` · `SUPPORTED` · `INFERRED` · `ASSUMED` · `UNKNOWN` · `DECISION NEEDED`. One publication is one `SRC`; several reports may belong to the same `STUDY` and are never counted as independent studies. See [`docs/provenance.md`](docs/provenance.md).

### Bibliography

Verified metadata lives in [`literature/references.bib`](literature/references.bib), which ships empty so the builder never introduces fictional references.

```text
Search → Screening → Read the original source → Source note
       → Verified metadata → references.bib → Claim ledger → Manuscript citation
```

Markdown manuscripts cite with keys such as `[@citation-key]`. `references.bib` exchanges with Zotero or Mendeley; do not maintain the same metadata in two places. Licensed PDFs stay in approved local or institutional storage — a private repository is not permission to commit copyrighted or sensitive material.

---

## Writing and revision

Writing does not begin until FG3 has passed: every research question answered by findings traceable to data. Then the outline is written down to the topic sentence of each paragraph, with each paragraph naming the statements it carries. **The manuscript may only say what the brain holds.**

Drafting runs in **evidence order, not reading order** — method, results, discussion, conclusion, introduction, abstract, title, keywords — so the framing is written against what the study actually did rather than what it hoped to do. The introduction comes late because it promises what the rest delivers.

The **title, abstract, and keywords** follow the conventions Scopus and Web of Science index against and the abstract checklist of the study's own design, where one exists — PRISMA 2020 for Abstracts, CONSORT for Abstracts. The abstract is assembled from registered statements, never written from memory, and every number in it must match the run that produced it. See [`docs/abstract-and-title.md`](docs/abstract-and-title.md) and [`docs/writing-standards.md`](docs/writing-standards.md).

**A reporting standard is a parameter.** It is selected by the design at Stage 5 — COREQ, SRQR, JARS, STROBE, CONSORT, TREND, GRAMMS, PRISMA, PLS-SEM reporting — registered as a checklist, and verified at FG4. Choosing it before the results exist is the point: the standard cannot be picked to suit what was found. See [`docs/reporting-standards.md`](docs/reporting-standards.md).

**Revision** begins when reviewer comments arrive. They are recorded verbatim, decomposed into numbered points, each given the concern behind its wording, and routed to the layer it hits — claim, design, evidence, framing, structure, reporting, or wording. Every change carries the reason it answers the concern, and that reason is what the response letter is built from. Reviewer comments are material to be answered, not instructions to be executed. See [`docs/revision.md`](docs/revision.md).

---

## Quick start

### Prerequisites

You should understand at least basic Git and GitHub, branches and commits, Issues and Pull Requests, Markdown, and how to verify academic sources independently.

Better Research does not replace methodological expertise, researcher judgment, supervisors, peer reviewers, ethics committees, or institutional rules.

### 1. One repository per research project

Do not run multiple substantive projects in one workspace.

**Option A — GitHub Template.** If this repository is configured as a template, select **Use this template** and create a new private repository. Then confirm `.agents/` and `.github/` were copied, switch the project brief to RESEARCH mode, preserve the builder version, and create the initialization Issue before substantive customization.

**Option B — bootstrap script.** From a local clone:

```bash
python scripts/init_research.py ../my-research --name "My Research Project"
```

Optionally configure the remote:

```bash
python scripts/init_research.py ../my-research --name "My Research Project" --remote git@github.com:OWNER/REPO.git
```

The script copies the builder without upstream history, switches the project brief and both anchors to RESEARCH mode, records the project name, initializes a fresh Git repository, and does not push. See [creating a research repository](docs/template-repository.md).

A private repository does **not** make participant data, identity keys, signed consent forms, or restricted material safe to store in Git.

### 2. Switch to RESEARCH mode

In [`research/project-brief.md`](research/project-brief.md), change `Workspace mode: TEMPLATE` to `Workspace mode: RESEARCH`, and set `Mode: RESEARCH` in `GRO.md` and `brain.md`.

| Mode | Purpose | Workflow rule |
|---|---|---|
| `TEMPLATE` | Maintain the upstream builder | Direct maintenance allowed when explicitly authorized |
| `RESEARCH` | Conduct an actual research project | Issue + branch + PR required for substantive work |

Do not switch modes to bypass the research workflow.

### 3. Start the first session

Give the agent:

> Read AGENTS.md, GRO.md, brain.md, research/project-brief.md, research/status.md, and docs/skills.md. Verify the owner/repository and confirm the workspace is in RESEARCH mode. Use research-workflow to find or create the project-brief initialization Issue, then use research-framing. Start only from information and sources that are actually available. Do not choose a method, theory, variable, or novelty claim without evidence. Record unknowns, decisions, evidence requirements, success criteria, verification, and checkpoints in the Issue. Report GRO-01 for my verification. Route every file change through a branch and Pull Request.

Then complete the project brief incrementally. You do **not** need a final title, method, theoretical model, or output language before starting. Leave unresolved fields as `NOT YET FILLED`, `NOT YET DECIDED`, or `NOT YET VERIFIED` — visible uncertainty is better than premature certainty.

---

## Working day to day

Do not start with *"AI, continue my dissertation."* Start with a reviewable research task:

> "Does the theoretical-gap argument in section X actually follow from the sources we have inspected?"

### The loop

```text
1  Find or create the Issue          9   Make the minimum justified change
2  Define the objective              10  Verify
3  Record the epistemic state        11  Save a checkpoint
4  Define scope                      12  Report or rewrite the GRO section
5  Define evidence required          13  Open or update the PR
6  Define success criteria           14  Review
7  Define verification               15  Merge and verify main
8  Create or continue the branch     16  Close the Issue when its conditions are met
```

See the full [Git workflow](docs/git-workflow.md).

### What makes a good Issue

One Issue is one **independently reviewable decision or output**.

```text
Good                                          Bad
#31 Verify theoretical mechanism for RQ2      #31 Do my dissertation
#32 Audit measurement validity for construct X #32 Continue the research
#33 Revise discussion against contradictions  #33 Make it better
```

Clarifying questions within an active task stay on that Issue. Large stages use a parent Issue with children. A good Issue preserves the objective, the epistemic state, scope and out-of-scope boundaries, evidence required, success criteria, a verification plan, decisions, blockers, checkpoints, and the related branch, commit, and PR. The agent loads that Issue and only the artifacts the task needs — not the whole project.

An example, abbreviated:

```markdown
## Objective
Determine whether institutional trust should remain a moderator of X → Y.

## Epistemic state
KNOWN      RQ2 currently specifies moderation; three sources discuss institutional trust.
SUPPORTED  No moderation mechanism has yet been verified.
UNKNOWN    Whether the closest prior studies already test the same mechanism.
           Whether moderation is theoretically necessary.
           Whether the design can identify moderation.

## Scope
In      theory memo · relevant source notes · claim ledger · the affected paragraphs
Out     redesigning the methodology · adding constructs · rewriting other chapters

## Success criteria
[ ] Construct definition verified.        [ ] Alternative explanations inspected.
[ ] Closest prior studies compared.       [ ] Retain / narrow / defer / reject recorded.
[ ] Counterevidence inspected.
```

The canonical form is [`.github/ISSUE_TEMPLATE/research-task.md`](.github/ISSUE_TEMPLATE/research-task.md).

### Continuing in a later session

You should not need to ask *"do you remember what we discussed last week?"*

> Read AGENTS.md and continue Issue #[number] in [owner/repo]. Read GRO.md and brain.md, then the Issue snapshot, latest checkpoint, decisions, dependencies, linked records, PRs, and open review findings. Reconcile them with the actual branch and commit state. Summarize the current position, state remaining unknowns or blockers, and continue only work that has not yet satisfied the success criteria. Save a checkpoint before the session ends.

The project should be recoverable from the repository, not from chat memory.

### Definition of done

A file-producing task is complete **for delivery** when the Issue's success criteria are PASS, the changes are on the right branch, the actual checks are recorded, the PR was reviewed and merged into `main`, the resulting commit was verified, and the Issue closure matches the evidence.

```text
MERGED ≠ scientifically valid       MERGED ≠ supervisor approval
MERGED ≠ ethics approval            MERGED ≠ research completed
```

Academic quality remains an evidence, method, review, and quality-gate decision.

---

## Skills

Eight skills live under [`.agents/skills/`](.agents/skills/) and are indexed in [`docs/skills.md`](docs/skills.md). Each states its place in the research flow.

| Skill | Purpose |
|---|---|
| `research-workflow` | Issues, checkpoints, branches, PRs, GRO sections, brain synchronization, cross-session recovery |
| `research-rigor` | Cross-stage guardrails for uncertainty, parsimony, scope, falsification, and verification |
| `research-framing` | Stages 0, 1, and 4: context, phenomenon, state of the art, novelty, research questions |
| `research-evidence` | Stages 1–3: search, screening, extraction, appraisal, source notes, claim evidence |
| `research-theory` | Stage 2 and the contribution test: theory map, mechanisms, closest studies, alternatives |
| `research-design` | Stages 5–6: methodology selection, parameters, ethics, analysis, findings |
| `research-writing` | Stages 7–9: outline, manuscript, title and abstract, revision table |
| `research-audit` | Flow-gate audits, consistency checks, examination and review preparation |

```text
Use research-evidence to verify whether CLM-014 is actually
supported by the available source notes.
```

Where an environment supports direct invocation: `$research-evidence`. Do not load every skill at once.

---

## Research rigor

`research-rigor` adapts execution ideas from [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) to research.

**Think before claiming.** Do not silently convert uncertainty into certainty.

```text
few search results → "this is the research gap"          ✗ not valid reasoning

few search results → check query design, databases, synonyms, adjacent
                     literature, citation chasing, access limits
                   → decide what can actually be claimed  ✓
```

**Parsimony first.** Complexity is not quality. Do not build `3 theories + 8 constructs + 4 mediators + 2 moderators + SEM` when a simpler design answers the question more defensibly.

**Surgical changes.** Every substantive change traces to the Issue, evidence, a decision, a review finding, or a success criterion. Do not rewrite unrelated sections because an agent sees an opportunity to improve them.

**Goal-driven research.** Replace *"improve the literature review"* with inspectable goals:

```text
Objective: Determine whether the literature review establishes a defensible
           unresolved theoretical problem.
Criteria:  [ ] Core constructs defined.      [ ] Major claims traceable to sources.
           [ ] Closest prior studies compared. [ ] Unsupported claims removed or flagged.
           [ ] Counterevidence represented.    [ ] Gap stated without novelty inflation.
```

**Falsification before affirmation.** For important claims: candidate claim → supporting evidence → **contradictory evidence** → alternative explanations → boundary conditions → claim strength. Do not search only for confirmation.

---

## Quality gates G0–G7

A complete set of files does not mean the research is academically ready.

```text
Delivery status  (Issue / PR complete)   ≠   Academic readiness  (gate READY)
```

| Gate | Assesses | Gate | Assesses |
|---|---|---|---|
| G0 | Context and research mandate | G4 | Research design |
| G1 | Problem and research questions | G5 | Execution readiness |
| G2 | Literature protocol and evidence | G6 | Results and interpretation |
| G3 | Theory and contribution | G7 | Manuscript and examination/review readiness |

Statuses: `NOT ASSESSED` · `REVISION REQUIRED` · `READY` · `NOT APPLICABLE`. Every assessment records the commit, the evidence inspected, **the evidence not inspected**, the assessor, any critical failure, closure conditions, and reopen triggers. Flow gates FG0–FG5 bundle these into the hard stops above.

Full criteria: [`docs/quality-gates.md`](docs/quality-gates.md). An agent's assessment is not supervisor approval, ethics approval, peer review, or institutional approval.

---

## Checks and validation

GitHub Actions runs mechanical checks on Pull Requests and pushes to `main`:

- relative Markdown links;
- skill frontmatter and names;
- `references.bib` structure and duplicate citation keys;
- prohibited sensitive and private paths;
- every identifier referenced in `brain.md`, `GRO.md`, or a record resolves to a defined statement or an existing record;
- GRO section numbering, status vocabulary, and the rule that a `VERIFIED` section must name a verifier and a date — an agent cannot verify its own report.

```bash
python scripts/validate_repository.py
```

```bash
python scripts/coherence_report.py
```

The coherence report prints statement counts, the record index, dangling and orphan identifiers, research-question coverage, findings without evidence, and statements missing links.

A PASS means **mechanical repository integrity**. It does not mean the claims are valid, the method is appropriate, or a quality gate is READY. Workflow: [`.github/workflows/repository-integrity.yml`](.github/workflows/repository-integrity.yml).

---

## Repository map

```text
.
├── AGENTS.md            canonical agent rules
├── GRO.md               where the research is going, and why
├── brain.md             statements, links, coherence checks
├── CLAUDE.md  .cursor/  .github/copilot-instructions.md    thin adapters
├── research/            brief, status, decision · deviation · AI-use logs
├── method/              methodology decision layer
├── literature/          three tracks, searches, screening, claim ledger, bibliography
├── parameters/          every parameter set used, plus presets
├── data/                records, dictionaries, safe data
├── analysis/            analysis plan and run records
├── manuscript/          outline and canonical manuscript
├── reviews/             gate reviews, revision tables, responses
├── exports/             rendered outputs
├── templates/           working forms
├── docs/                workflow, anchors, standards, integrity, Git, migrations
├── scripts/             bootstrap, validation, coherence report
├── examples/            synthetic example
└── VERSION  CHANGELOG.md  LICENSE  NOTICE.md
```

| Location | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical agent rules; every adapter redirects here |
| [`GRO.md`](GRO.md) | The research reported section by section, with its reasoning, for you to verify |
| [`brain.md`](brain.md) | Coherence anchor: typed statements, links, chain checks |
| [`research/`](research/project-brief.md) | Project brief, status, decisions, deviations, AI-use log |
| [`method/`](method/README.md) | Methodology selection, design logic, AI rules, method-chapter blueprint, sources |
| [`literature/`](literature/README.md) | Three tracks, search trail, screening, claim ledger, bibliography |
| [`parameters/`](parameters/README.md) | Parameter sets in use, plus search and reporting presets |
| [`data/`](data/README.md) | Data records, dictionaries, safe data, governance |
| [`analysis/`](analysis/README.md) | Analysis plan and run records |
| [`manuscript/`](manuscript/README.md) | Outline and canonical manuscript |
| [`reviews/`](reviews/README.md) | Gate reviews, revision tables, responses |
| [`templates/`](templates/README.md) | Working research forms |
| [`docs/`](docs/research-workflow.md) | Flow, anchors, standards, integrity, Git, Issues, PRs, migrations |
| [`examples/`](examples/toy-research/) | Synthetic example |

---

## Templates

Twenty-five forms, each copied only when its stage begins:

| Stage | Templates |
|---|---|
| any | GRO section · session checkpoint · claim ledger · gate review |
| 1–4 | problem memo · parameter set · search log · source note |
| 2–3 | theory map and contribution audit · review protocol · screening log · literature matrix |
| 5 | method decision record · design matrix · analysis plan · ethics and data plan · reporting checklist |
| 5–6 | data record · data dictionary · run record |
| 8 | manuscript outline · chapter plan |
| 9 | revision table · review response |

See [`templates/README.md`](templates/README.md). An incomplete template stays visibly incomplete rather than being filled with invented content.

---

## Versioning and migration

Every research repository **pins the builder version** it was created from and does not silently inherit later changes.

```text
research project vX → upstream builder changes → NO automatic sync
                    → read migration notes → migration Issue
                    → branch + verification + PR → version updated
```

This protects reproducibility: research rules, skill behavior, the provenance schema, and the gates must not change invisibly mid-project. See [`VERSION`](VERSION), [`CHANGELOG.md`](CHANGELOG.md), and the [migration policy](docs/migrations/README.md).

---

## Portability across AI agents

[`AGENTS.md`](AGENTS.md) is the **single canonical instruction source**. Thin adapters exist for environments that read a different file — `CLAUDE.md` for Claude Code, `.cursor/rules/better-research.mdc` for Cursor, `.github/copilot-instructions.md` for Copilot — and environments that support `AGENTS.md` read it directly. **Adapters must never become independent copies of the research rules.**

---

## Language policy

The **repository itself is written in English** so researchers and AI systems globally can use the same builder.

**Research outputs are also written in English by default**, because the default target is an international, indexed outlet. Another language — an Indonesian dissertation, a bilingual report, multilingual field materials — is used when you ask for it explicitly, or when the institution, outlet, or participants require it. Record that instruction in [`research/project-brief.md`](research/project-brief.md) before drafting; an agent does not switch the output language on its own initiative and does not infer it from the language of the conversation.

Source material, transcripts, and documents stay in their original language whatever the output language. Translation must preserve claim strength, uncertainty, technical meaning, quotations, attribution, and the distinction between source content and researcher interpretation.

---

## Non-negotiable rules

1. Do not fabricate sources, DOI values, quotations, pages, data, results, permissions, approvals, or research activities.
2. Do not state that a source supports a claim before checking the support.
3. Do not select a method merely because it is popular or sophisticated.
4. Do not hide contradictory evidence.
5. Do not describe two AI agents or runs as two independent human reviewers.
6. Do not store sensitive participant data in Git.
7. Do not claim ethics approval, pilot work, fieldwork, analysis, or human review that did not occur.
8. Do not treat citation count, manuscript length, statistical significance, or low text similarity as proof of quality.
9. Do not perform broad unrelated rewrites when only a narrow change is required.
10. Do not use chat history as the only source of project decisions.

See [`docs/academic-integrity.md`](docs/academic-integrity.md).

---

## What Better Research does not do

It is a **research operating system**, not a truth machine. It does not automatically provide access to Scopus, Web of Science, ProQuest, or paid databases; read sources that were not provided; turn AI into a human reviewer; issue ethics approval; choose the correct design without project information; prove novelty from a short search; run valid analysis without suitable data and assumptions; guarantee acceptance or examination success; or replace researcher, supervisor, reviewer, or institutional judgment.

A strong workflow reduces avoidable failure. It does not remove the need for research judgment.

The synthetic example in [`examples/toy-research/`](examples/toy-research/) still demonstrates only the pre-0.3.0 provenance cycle; worked examples for the full flow are tracked in issue #7.

---

## Philosophy

Large research projects should not depend on one AI session remembering everything.

```text
every important claim has evidence,
every decision has a reason,
every change has a diff,
every task has a scope,
every session has a checkpoint,
and every contribution can be defended.
```

**Better Research does not try to make AI remember the entire project. It makes the project recoverable, inspectable, and continuable.**

---

## Key documentation

| | |
|---|---|
| [Agent rules](AGENTS.md) | the canonical instruction source |
| [Research flow](docs/research-workflow.md) | the ten stages and the flow gates |
| [Grand Research Outline](docs/gro.md) | how direction is reported and verified |
| [Data structure](docs/data-structure.md) | statements, records, identifiers, folders |
| [Quality gates](docs/quality-gates.md) | criteria, critical failures, reopen triggers |
| [Methodology decision layer](method/README.md) | the full selection logic |
| [Method selection protocol](method/05-method-selection-protocol.md) | the eleven-step protocol an agent runs |
| [Methodology sources](docs/methodology-sources.md) | specialist authorities by technique family |
| [Reporting standards](docs/reporting-standards.md) | checklists as parameters |
| [Writing standards](docs/writing-standards.md) | what distinguishes a publishable manuscript |
| [Title, abstract, keywords](docs/abstract-and-title.md) | indexing conventions and abstract checklists |
| [Revision](docs/revision.md) | reviewer comments, routing, and FG5 |
| [Provenance model](docs/provenance.md) | source → study → claim → decision |
| [Academic integrity](docs/academic-integrity.md) | evidence, uncertainty, privacy, AI use |
| [Standards register](docs/standards.md) | external standards this builder references |
| [Git workflow](docs/git-workflow.md) · [Issues](docs/issues.md) · [Pull requests](docs/pull-requests.md) · [Session continuity](docs/session-continuity.md) | the operational layer |
| [Skill index](docs/skills.md) · [Migration policy](docs/migrations/README.md) · [Attribution](NOTICE.md) | reference |
