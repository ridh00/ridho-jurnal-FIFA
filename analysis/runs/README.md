# Run records

One record per execution of a cleaning or analysis step, named by its ID: `RUN-###.md`. Use the [run record](../../templates/run-record.md) template. Search runs are logged as rows in the search log and may use a run record when their parameters and outputs deserve one. No run has been recorded yet.

A run names the parameter set it used (`PRM`), the input data or corpus version (`DAT`), the software and version, the output it produced (a derived `DAT` or a result), the check performed, and any deviation. A run is the only legitimate origin of a derived data item and of a result cited by a finding.
