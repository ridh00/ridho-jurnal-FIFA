# Parameters

Every parameter used in this project is recorded here as a parameter set (`PRM`). A parameter is any value that configures a research step: a search window, a keyword set, an inclusion criterion, a sample-size assumption, a reliability threshold, a cleaning rule, a bootstrap count, a reporting checklist. If a value shaped a result and is not in this folder, the result is not reproducible.

No parameter sets exist yet. Create one when a step that needs parameters begins, using the [parameter set](../templates/parameter-set.md) template (or the [reporting checklist](../templates/reporting-checklist.md) for type `reporting`). Name the file by its ID with an optional descriptive suffix:

```text
parameters/PRM-001-search-theory.md
parameters/PRM-002-search-empirical.md
parameters/PRM-003-screening.md
parameters/PRM-004-reporting-coreq.md
```

Each parameter carries a **value**, a **justification**, and a **source** (a `SRC`, a standard, or a recorded decision `DEC`). A value without a justification is not accepted at the method gate. Defaults exist to be adopted or changed with a reason, not to be followed silently.

## Types

| Type | Used by | Typical parameters |
|---|---|---|
| `search` | Stages 1–3 | databases, keyword sets, window, quartile priority filter, language, document types |
| `screening` | Stage 3 | inclusion/exclusion criteria, reviewer process, disagreement rule |
| `sampling` | Stage 5 | population, frame, strategy, size logic, stopping logic |
| `instrument` | Stage 5 | source instrument, adaptation, scale, validity/reliability targets |
| `cleaning` | Stages 5–6 | exclusion rules, missing-data rule, outlier rule, "within RQ focus" rule |
| `analysis` | Stages 5–6 | software and version, model, estimator, thresholds, seed |
| `reporting` | Stages 5, 8 | reporting standard and its item list as a checklist |
| `export` | Stage 8 | style, template, tool version |

## Presets

[`presets/`](presets/README.md) holds default parameter sets to copy: the three search tracks of the flow and the reporting-standard checklists. Copying a preset creates a `PRM` record; the preset itself is never edited in a research project.

## Linking

A `PRM` is referenced by the runs that use it (`RUN`), by the method decision record and design matrix (Stage 5), by the analysis plan, and by `MTH` statements in [`brain.md`](../brain.md). The validator rejects references to a `PRM` that does not exist. Changing a parameter after results were seen is a deviation: record it in the deviation log and create a new `PRM` that supersedes the old one.
