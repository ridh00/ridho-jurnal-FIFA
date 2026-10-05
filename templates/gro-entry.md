# GRO Section

One section per part of the research outline, kept in [`GRO.md`](../GRO.md). Rules: [docs/gro.md](../docs/gro.md). The numbering is fixed by the outline — `GRO-06` is always the method — so a section is written or rewritten in place, never appended as a new number.

```markdown
## GRO-0# · <section name>

- Status: NOT YET REACHED / REPORTED / VERIFIED / REVISED
- Flow stage / gate: NOT YET FILLED
- Version: N · updated by PR #NN on YYYY-MM-DD
- Basis: <typed statement IDs in brain.md> · <DEC / PRM / SRC / DAT / RUN>
- Verified by / date: AWAITING RESEARCHER

<One paragraph, at most ~120 words, no lists, written for someone who has not
read the repository. State the direction this part of the research takes and
the reasoning behind it. The reasoning is what the researcher verifies; a
paragraph that says what was decided without saying why has reported nothing.>

- What this forecloses: NOT YET FILLED
- Not yet settled: NOT YET FILLED
```

## Filling the fields

**Status.** The AI writes `REPORTED` and stops on the work that depends on this part. **The AI never writes `VERIFIED`** — only the researcher does, with a name and a date, as with `PROPOSED` → `APPROVED` in the method decision record. `REVISED` means the direction changed: rewrite the paragraph, raise the version, move the old paragraph into the revision history with its reason, and set the status back to `REPORTED`.

**Version and PR.** Every pull request that advances or changes this part of the research updates this section in the same pull request and records itself here. A pull request that touches no part of the outline changes nothing in `GRO.md`.

**Basis.** Cite IDs only. The statement text lives in `brain.md`, the evidence in the claim ledger and the record files. A section that restates them is in the wrong document.

**The paragraph.** Direction plus reasoning. If it does not fit in a paragraph, the decision is not yet clear enough to be verified.

**What this forecloses.** What the choice rules out — the designs not taken, the claims no longer available, the questions now out of scope. This is often what the researcher reacts to.

## After rewriting a section

Update the snapshot at the top of `GRO.md`: current stage and gate, destination, which sections await verification, how many are verified. Add a row to the revision history, and name the downstream sections the change puts in question — revising the theory in `GRO-02` puts `GRO-03` through `GRO-05` back in play.
