#!/usr/bin/env python3
"""Print the brain.md chain report: statement counts, ID index, dangling and
orphan identifiers, RQ coverage, and statements missing links.

A clean report is a mechanical result. It is not an academic quality gate.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_repository as v  # noqa: E402


def brain_rows() -> list[dict[str, str]]:
    """Statement rows of brain.md as dicts keyed by the standard columns."""
    columns = [
        "ID", "Statement", "Status", "Evidence", "Upstream",
        "Downstream", "Manuscript", "Gate", "Supersedes",
    ]
    text = v.read_text(v.BRAIN) or ""
    rows = []
    for first_cell, line in v.table_rows(text):
        if not (v.ID_RE.fullmatch(first_cell) and v.id_type(first_cell) in v.STATEMENT_TYPES):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < len(columns):
            continue
        rows.append(dict(zip(columns, cells)))
    return rows


def main() -> int:
    if not v.BRAIN.is_file():
        print("brain.md is missing at the repository root")
        return 1

    rows = brain_rows()
    statements = {r["ID"] for r in rows}
    records = v.record_files()

    print("# Coherence report\n")

    print("## Statements per type")
    for kind in v.STATEMENT_TYPES:
        count = sum(1 for r in rows if v.id_type(r["ID"]) == kind)
        print(f"- {kind}: {count}")
    print()

    print("## Records")
    for kind in v.RECORD_TYPES:
        ids = sorted(i for i in records if v.id_type(i) == kind)
        print(f"- {kind}: {len(ids)}")
        for identifier in ids:
            print(f"    {identifier}  {records[identifier].relative_to(v.ROOT).as_posix()}")
    print()

    errors: list[str] = []
    warnings: list[str] = []
    v.check_coherence_links(errors, warnings)
    print("## Dangling references")
    print("\n".join(f"- {e}" for e in sorted(set(errors))) or "- none")
    print()
    print("## Orphan records")
    print("\n".join(f"- {w}" for w in sorted(set(warnings))) or "- none")
    print()

    rq_ids = sorted(i for i in statements if v.id_type(i) == "RQ")
    fnd_rows = [r for r in rows if v.id_type(r["ID"]) == "FND"]
    ccl_rows = [r for r in rows if v.id_type(r["ID"]) == "CCL"]
    print("## Research-question coverage")
    if not rq_ids:
        print("- no RQ registered")
    for rq in rq_ids:
        answered = [r["ID"] for r in fnd_rows if rq in v.find_ids(r["Upstream"])]
        concluded = [r["ID"] for r in ccl_rows if rq in v.find_ids(r["Upstream"])]
        print(f"- {rq}: findings {answered or 'NONE'}; conclusions {concluded or 'NONE'}")
    print()

    print("## Findings without DAT or RUN evidence")
    missing = [
        r["ID"] for r in fnd_rows
        if not any(v.id_type(i) in ("DAT", "RUN") for i in v.find_ids(r["Evidence"]))
    ]
    print("\n".join(f"- {i}" for i in missing) or "- none")
    print()

    print("## Statements missing links")
    no_upstream = [
        r["ID"] for r in rows
        if v.id_type(r["ID"]) != "CTX" and not v.find_ids(r["Upstream"])
    ]
    terminal = ("CCL", "LIM")
    no_downstream = [
        r["ID"] for r in rows
        if v.id_type(r["ID"]) not in terminal
        and v.id_type(r["ID"]) != "IMP"
        and not v.find_ids(r["Downstream"])
    ]
    print(f"- without upstream: {no_upstream or 'none'}")
    print(f"- without downstream: {no_downstream or 'none'}")
    print()

    print("## Status distribution")
    statuses: dict[str, int] = {}
    for r in rows:
        statuses[r["Status"]] = statuses.get(r["Status"], 0) + 1
    print("\n".join(f"- {k}: {n}" for k, n in sorted(statuses.items())) or "- no statements")
    print("\nThis report is mechanical. Academic readiness is assessed through the quality gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
