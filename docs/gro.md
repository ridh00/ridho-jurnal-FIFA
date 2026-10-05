# Grand Research Outline (GRO)

`GRO.md` is the report the AI writes for the researcher: one numbered section per part of the research outline, each stating **where that part is going and why**. The researcher reads it and verifies the direction. It is a live document — a section is rewritten whenever that part of the research changes, and the new version is verified again.

## What it is for

The researcher should never have to read the repository to find out where the research is heading. They read one file, top to bottom, and see the whole study as a sequence of reasoned decisions:

```text
GRO-01  Introduction ........ the study addresses this, at this locus, because …
GRO-02  Grand theory ........ this theory was chosen because …
GRO-03  Literature and gap .. the literature shows this pattern, so the gap is …
GRO-04  Novelty ............. this study stands here because …
GRO-05  Research questions ... the questions are phrased this way because …
GRO-06  Method .............. this design was chosen because …
GRO-07  Data and analysis ... the data comes from here and is analyzed this way because …
GRO-08  Findings ............ the data shows this …
GRO-09  Discussion .......... against theory and literature this means …
GRO-10  Conclusion .......... the answer to the questions is …
GRO-11  Manuscript .......... the argument is arranged this way because …
```

The reasoning is the part that matters. A section that says *what* was decided without *why* has not been reported, and the researcher has nothing to verify.

## Relationship to the other files

| File | Question | Audience |
|---|---|---|
| **`GRO.md`** | Where is the research going, and why? | the researcher |
| [`brain.md`](../brain.md) | Is the research internally consistent? | the agent and the validator |
| Issue | What is being done now, and is it finished? | whoever continues the work |

`brain.md` holds the statements as structured rows; `GRO.md` explains them as prose. GRO cites IDs and never restates statement text. A project can be perfectly consistent in `brain.md` and still be heading somewhere the researcher never intended — that is what GRO catches.

## The sections

The numbering follows the research outline, so it is fixed and predictable: `GRO-06` is always the method. Each section corresponds to stages of the [research flow](research-workflow.md).

| # | Section | Flow stage | Reports |
|---|---|---|---|
| GRO-01 | Introduction | 0–1 | the phenomenon, the locus, the paradigm, and why the study is being done |
| GRO-02 | Grand theory | 2 | which theory explains the phenomenon, why that one, what role it plays |
| GRO-03 | Literature and gap | 3 | what the literature shows, and the gap that follows from it |
| GRO-04 | Novelty | 4 | where this study stands against the state of the art |
| GRO-05 | Research questions | 4 | the questions, and why they are phrased and bounded this way |
| GRO-06 | Method | 5 | the approach and design, and why they fit the questions |
| GRO-07 | Data and analysis | 5–6 | where the data comes from, how it is cleaned and analyzed, and why |
| GRO-08 | Findings | 6 | what the data shows and how it answers each question |
| GRO-09 | Discussion | 7 | what the findings mean against the theory and the literature |
| GRO-10 | Conclusion and implications | 7 | the answers, the limits, and what follows |
| GRO-11 | Manuscript | 8 | how the argument is arranged and why |

A project may add a section when it genuinely has a part these do not cover; it does not renumber the existing ones. A section that has not been reached yet stays in the document as `NOT YET REACHED`, so the researcher always sees the whole shape of the study.

## Anatomy of a section

```markdown
## GRO-06 · Method

- Status: REPORTED — awaiting verification
- Flow stage / gate: Stage 5 · FG2
- Version: 1 · updated by PR #44 on 2026-09-17
- Basis: MTH-001, MTH-002 · DEC-011 · PRM-006, PRM-007
- Verified by / date: AWAITING RESEARCHER

<one paragraph: the direction this part takes, and why>

- What this forecloses: <what the choice rules out>
- Not yet settled: <what remains open and what would settle it>
```

Everything outside the paragraph is metadata. The paragraph is what the researcher reads.

## The one-paragraph rule

One paragraph per section, at most about 120 words, no lists inside it, written for someone who has not read the repository. It says what direction this part of the research takes and the reasoning behind it, and stops.

The limit is not a style preference. It is what keeps the whole study readable in one sitting, which is the only reason the document works. If a part cannot be explained in a paragraph, the decision behind it is not yet clear enough to be verified.

## Status and verification

```text
NOT YET REACHED ──the AI works on this part──> REPORTED
                                                 │
                    researcher agrees ───────────┼──> VERIFIED
                    researcher wants it changed ─┘
                                                 ↓
                                             REVISED  (new version, re-reported)
```

- The AI writes `REPORTED` and stops on the work that depends on that part.
- **The AI never writes `VERIFIED`.** Only the researcher does, with a name and a date — the same rule as `PROPOSED` → `APPROVED` in the method decision record.
- `REVISED` means the researcher asked for a different direction, or new evidence changed it. The section is rewritten as a new version; the previous version moves into the section's revision history with the reason.

Verification is per section, not for the document as a whole. A study can have GRO-01 through GRO-05 verified while GRO-06 is still awaiting the researcher.

## Live updating

A section is rewritten whenever that part of the research changes — a new source overturns the gap, the design is revised, a finding contradicts an expectation. When that happens:

1. the paragraph is rewritten to the current direction;
2. the version number increases and the previous version moves into the section's revision history with the date, the PR, and the reason;
3. the status returns to `REPORTED`;
4. sections downstream that depended on it are marked for review — changing the theory in `GRO-02` puts `GRO-03` through `GRO-05` in question.

The revision history is never deleted. A study whose direction changed is normal; a study whose history was tidied so it looks as if it never changed is not.

## When to write

Whenever a pull request advances or changes a part of the research, the corresponding section is written or updated in the same pull request, and the PR is recorded in the section's version line. A pull request that touches no part of the research outline — formatting, tooling, link fixes — changes nothing in `GRO.md`.

## Reading protocol

The researcher reads `GRO.md` top to bottom and sees the whole study. To check only what needs them, they read the snapshot at the top, which lists the sections currently `REPORTED` and awaiting verification.

## What never goes in GRO

Evidence, data, quotations, tables of results, statement text, file change lists, or tool output. GRO cites those by ID and explains the reasoning. It holds direction and the reasons for it, nothing else.

## Mechanical checks

`python scripts/validate_repository.py` checks that section numbers are unique, that statuses use the defined vocabulary, that a `VERIFIED` section names a verifier and a date, and that every ID cited resolves. It warns about sections awaiting verification and about paragraphs over the word limit.

Whether the direction is a good one is the researcher's judgment. That is the whole point of the document.
