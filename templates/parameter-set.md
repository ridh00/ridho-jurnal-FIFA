# Parameter Set

One record per set of parameters used by a research step. See [parameters](../parameters/README.md) and the [data structure](../docs/data-structure.md). A value without a justification is not accepted at the method gate.

## Identity

- PRM ID: NOT YET FILLED
- Type: search / screening / sampling / instrument / cleaning / analysis / reporting / export (choose one)
- Stage and artifact it configures: NOT YET FILLED
- Created from preset: NOT APPLICABLE / `parameters/presets/` NOT YET FILLED
- Registered on / by: NOT YET FILLED
- Status: DRAFT / ACTIVE / SUPERSEDED
- Supersedes / superseded by: NOT APPLICABLE

## Parameters

| Parameter | Value | Justification | Source (`SRC`, standard, or `DEC`) | Notes |
|---|---|---|---|---|

Record every value that shaped a result, including defaults adopted without change. A changed default needs a reason in the justification column.

## Used by

| Run (`RUN`) or artifact | Date | Result or output |
|---|---|---|

## Statements this parameter set underlies

| Statement ID | How the parameter affects it |
|---|---|

## Change history

Changing a parameter after related results were seen is a protocol deviation: record it in the deviation log and create a new parameter set that supersedes this one.

| Date | Change | Reason | Results already seen? | Deviation ID |
|---|---|---|---|---|
