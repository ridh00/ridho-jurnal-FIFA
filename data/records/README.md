# Data records

One record per data item that enters the project, named by its ID: `DAT-###.md`, with an optional descriptive suffix. Use the [data record](../../templates/data-record.md) template. No data item has been registered yet.

A record is metadata: what the item is, where it came from (a source, a search run, a cleaning run, a field activity), which parameters produced it, where it is stored safely, its sensitivity class and permission status, and which statements in [`brain.md`](../../brain.md) it supports. The record is always committed. The data itself enters Git only under `data/safe/` after a recorded review; raw, processed participant-level, consent, and linkage material never does.

Every finding cites at least one `DAT` or `RUN`. A data item that nothing cites is reported as an orphan by the coherence report.
