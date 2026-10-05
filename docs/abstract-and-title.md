# Title, Abstract, and Keywords

The title, abstract, and keywords are the only parts of a manuscript that most readers will ever see, and the only parts that indexing services use to make the work findable. They are written **last**, after the argument is settled, and they are assembled from the statements already registered in [`brain.md`](../brain.md) — never rewritten from memory.

The rules below follow the conventions applied by Scopus and Web of Science indexing and by reputable journals in most fields. The target outlet's own author guidelines override them and are recorded in the project brief.

---

# Title

## What a title has to do

Three jobs at once, in this order of priority:

1. **Be accurate.** It states what the study found or examined, within the limits the design supports. A title that promises more than the design can deliver is the first claim a reviewer checks.
2. **Be findable.** Indexing services and search engines weight title terms heavily. The terms a reader would actually type must appear in it.
3. **Be readable.** An editor decides in seconds whether to send the manuscript out for review.

## Length

Ten to fifteen words is the working target. Most journals cap between 12 and 20 words; some cap characters instead, commonly 100 to 250 including spaces. Verify the cap for the target outlet before drafting and record it in the [manuscript outline](../templates/manuscript-outline.md).

Titles beyond about twenty words lose their key terms in the middle, where neither a reader scanning results nor a search ranking gives them weight.

## Structure

| Pattern | Form | Use when |
|---|---|---|
| **Descriptive** | *Coordination routines and role clarity in district health offices* | the study examines a relationship without a single headline result; the safest default |
| **Declarative** | *Coordination routines improve role clarity in district health offices* | the finding is unambiguous **and** the design supports the verb used; never use a causal verb from an observational design |
| **Compound with a design subtitle** | *Coordination routines and role clarity in district health offices: a qualitative case study* | a reporting standard or the journal requires the design to be named |
| **Interrogative** | *Do coordination routines improve role clarity?* | rarely — common in some medical and education journals, discouraged in most social-science outlets; check the outlet |

A declarative title is a claim. It is audited at FG4 against the boundaries of inference recorded in the method decision record, exactly like any other claim.

## Naming the design

Several reporting standards require the design in the title or abstract, and journals enforce it:

| Design | Requirement |
|---|---|
| Randomized trial | CONSORT: identify as randomized in the title |
| Systematic review | PRISMA 2020 item 1: identify the report as a systematic review |
| Observational study | STROBE item 1(a): indicate the design with a commonly used term in the title or abstract |
| Qualitative study | SRQR item S1: identify the study as qualitative or indicate the approach |
| Mixed methods | JARS-Mixed: identify as mixed methods and name the design where possible |

When the standard requires it, the design goes in a subtitle after a colon rather than being forced into the main clause.

## What gets a title rejected or buried

- **Abbreviations and acronyms** that are not universally understood in the field. They do not index reliably and they stop a non-specialist editor.
- **Empty openings** — *A study of*, *An investigation into*, *An analysis of*, *Towards an understanding of*, *Some notes on*. They consume the highest-weighted position in the title and say nothing.
- **Puns and allusions** that carry no searchable term. They may read well to a colleague and be invisible to the index.
- **Question marks and exclamation marks** where the field does not use them.
- **Formulae, chemical symbols, superscripts, and special characters**, which can break in indexing and citation export.
- **Place names as the whole contribution** — *…: evidence from Indonesia* is legitimate as a scope marker; it is not itself the novelty.
- **Trailing series markers** — *Part I*, *Part II*. Many journals refuse them; they also fragment citation.

## Building the title

1. Take the contribution statement (`CTB`) registered at Stage 4.
2. Extract its core terms: the phenomenon, the constructs, the population or context, and the design when a standard requires it.
3. Order them so the most distinctive term sits early.
4. Remove every word that carries no information — articles at the start, empty openings, redundant qualifiers.
5. Check the claim verb against the design's boundaries of inference.
6. Check the length against the outlet's cap.
7. Check that the terms differ from the keywords, so the two together widen coverage rather than repeat it.

## Running title

Many journals require a short running head, commonly 50 to 70 characters. It carries the two most distinctive terms of the title and nothing else.

---

# Abstract

## What it is

A self-contained summary of the whole study. It is read, indexed, and cited by people who never open the full text. It contains nothing that is not in the manuscript, and every number in it matches the number in the results.

## Written last, assembled from the brain

The abstract is written after the manuscript is complete, and every sentence in it corresponds to a registered statement:

| Abstract move | Statement it comes from |
|---|---|
| Background and problem | `PHN`, `THR` |
| Gap and objective | `GAP`, `NOV` |
| Research questions or aims | `RQ` |
| Design and methods | `MTH`, with `PRM` for the parameters worth naming |
| Results | `FND`, with the numbers taken from the `RUN` output |
| Conclusion and implications | `CCL`, `IMP` |
| Limitations, where the standard requires it | `LIM` |

An abstract written from memory rather than from the statements is how a manuscript acquires a finding that appears nowhere in its own results section. Writing it from `brain.md` makes that error structurally difficult.

## Which checklist applies

A reporting standard that has its own abstract checklist governs the abstract. It is registered as a parameter of type `reporting` at Stage 5 alongside the main checklist and verified at FG4. See [reporting standards](reporting-standards.md).

| Design | Abstract checklist | Preset |
|---|---|---|
| Systematic or structured review | **PRISMA 2020 for Abstracts**, 12 items (Page et al. 2021) | [preset](../parameters/presets/reporting/prisma-abstracts-2020.md) |
| Randomized trial | **CONSORT for Abstracts** (Hopewell et al. 2008; CONSORT 2010 item 1b) | [preset](../parameters/presets/reporting/consort-abstracts-2008.md) |
| Observational or survey | STROBE item 1(b): an informative and balanced summary of what was done and what was found | in the [STROBE preset](../parameters/presets/reporting/strobe-2007.md) |
| Quantitative, psychology and adjacent | JARS-Quant abstract requirements | in the [JARS-Quant preset](../parameters/presets/reporting/jars-quant-2018.md) |
| Qualitative | SRQR item S2 or JARS-Qual abstract requirements | in the [SRQR](../parameters/presets/reporting/srqr-2014.md) and [JARS-Qual](../parameters/presets/reporting/jars-qual-2018.md) presets |
| Mixed methods | JARS-Mixed abstract requirements; report both strands and the integration | in the [JARS-Mixed preset](../parameters/presets/reporting/jars-mixed-2018.md) |

When no standard applies to the design, use the generic structure below.

## Structured and unstructured

A **structured abstract** carries explicit headings — commonly Background, Objective, Methods, Results, Conclusions; sometimes Design, Setting, Participants, Main outcome measures. Most medical, health, and many social-science journals require it. The headings are fixed by the journal, not chosen by the author.

An **unstructured abstract** is a single paragraph with no headings, common in humanities, management, and some social-science outlets. It follows the same sequence without the labels.

Check which the outlet requires before drafting; converting between them late costs more than it looks.

## Generic structure, when no standard governs

| Move | Content | Share of the abstract |
|---|---|---|
| Background | the phenomenon and why it matters; one or two sentences at most | ~15% |
| Gap and objective | what is not known, and what this study set out to do | ~15% |
| Methods | design, setting, participants or corpus, data, analysis | ~25% |
| Results | the actual findings, with numbers or themes; the core of the abstract | ~30% |
| Conclusion | what the findings mean, within the limits of the design | ~15% |

The results move is the largest. An abstract that spends half its words on background and ends with "implications are discussed" tells the reader nothing and is a common desk-rejection signal.

## Word budget

150 to 300 words covers most outlets; structured abstracts commonly run 250 to 350. Record the exact limit from the author guidelines in the manuscript outline before drafting. Write to the limit, not under it — unused words are lost coverage.

## Rules

1. **Self-contained.** No citations, unless the outlet explicitly allows them. No cross-references to figures, tables, or sections.
2. **No abbreviation on first use** unless it is universally known in the field. An abbreviation defined in the abstract must be defined again in the body.
3. **Numbers match.** Every value matches the results section and the run that produced it. A mismatch between abstract and results is treated as a data-integrity finding, not a typo.
4. **No claim absent from the manuscript.** Every sentence traces to a registered statement.
5. **Claim verbs calibrated.** The same audit as the body: causal verbs only where the design permits.
6. **Uncertainty survives.** Effect sizes with intervals where the design reports them; qualitative claims bounded by their context. An abstract is where hedges are most often dropped and where dropping them does most damage.
7. **Nothing promised that is not delivered.** "Implications are discussed" is not a conclusion.
8. **Limitations** where the standard requires them — PRISMA for Abstracts requires a limitations-of-evidence item.
9. **Registration and funding** where the standard requires them.

---

# Keywords

Scopus and Web of Science index keywords separately from the title and abstract, so keywords that repeat title words waste the slot.

- **Count:** typically four to eight; the outlet sets the limit.
- **Complement, do not duplicate.** Choose terms a reader would search that are *not* already in the title.
- **Use controlled vocabulary** where the field has one — MeSH in health, ERIC thesaurus in education, the outlet's own list where it provides one. A controlled term is what the index actually matches against.
- **Include the design** as one keyword when the title does not name it.
- **Include the context or population** when it bounds the contribution.
- **Avoid** very broad single words that return millions of records, invented compound phrases nobody searches, and abbreviations.
- **Match the language of the manuscript.** For an Indonesian-language output aimed at a national index, give the Indonesian terms and, where the outlet allows, the English equivalents.

Record the final set in the manuscript outline with the reason for each term.

---

# Verification at FG4

The gate review inspects:

- the title against the length cap, the design-naming requirement of the reporting standard, and the boundaries of inference;
- the abstract against its checklist, item by item, or against the generic structure when none applies;
- every number in the abstract against the results section and the run that produced it;
- every abstract sentence against a registered statement;
- the keywords against the title, for duplication, and against the outlet's limit.

A complete checklist is a transparency result, not evidence that the abstract is good.

## Sources

- Hopewell, S., Clarke, M., Moher, D., Wager, E., Middleton, P., Altman, D. G., & Schulz, K. F. (2008). CONSORT for reporting randomised trials in journal and conference abstracts. *The Lancet*, 371(9609), 281–283.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372, n71 (PRISMA 2020 for Abstracts checklist).
- Schulz, K. F., Altman, D. G., & Moher, D. (2010). CONSORT 2010 statement. *BMJ*, 340, c332 (item 1b).
- von Elm, E., et al. (2007). STROBE statement. *PLoS Medicine*, 4(10), e296 (item 1).
- O'Brien, B. C., et al. (2014). SRQR. *Academic Medicine*, 89(9), 1245–1251 (items S1, S2).
- Appelbaum, M., et al. (2018) and Levitt, H. M., et al. (2018). APA JARS. *American Psychologist*, 73(1).
