#!/usr/bin/env python3
"""Mechanical integrity checks for Better Research.

These checks validate repository structure only. Passing them does not imply
academic validity, source support, ethical approval, or quality-gate readiness.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".py", ".sh", ".bib", ".tex", ".json"
}

STALE_EXCLUDE = {
    "CHANGELOG.md",
    "scripts/validate_repository.py",
}
STALE_EXCLUDE_PREFIXES = (
    "docs/migrations/",
)

SENSITIVE_PREFIXES = (
    "private/",
    "secrets/",
    "data/raw/",
    "data/processed/",
    "data/linkage/",
    "data/consent/",
    "literature/pdfs/",
)

LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
FRONTMATTER_LINE_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")

# --- Coherence model (see docs/data-structure.md) ---------------------------

STATEMENT_TYPES = (
    "CTX", "PHN", "THR", "LIT", "GAP", "NOV", "RQ", "CTB",
    "MTH", "FND", "DIS", "LIM", "CCL", "IMP",
)
RECORD_TYPES = ("SRC", "DAT", "PRM", "RUN", "DEC")
UNCHECKED_TYPES = ("STUDY", "REV", "CLM")

ID_RE = re.compile(
    r"\b(" + "|".join(STATEMENT_TYPES + RECORD_TYPES + UNCHECKED_TYPES)
    + r")-(?:[A-Z0-9]+-)?(\d{3,})\b"
)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

BRAIN = ROOT / "brain.md"
GRO = ROOT / "GRO.md"
GRO_ENTRY_RE = re.compile(r"^##\s+(GRO-(\d{2,}))\b(.*)$")
GRO_FIELD_RE = re.compile(r"^-\s*([A-Za-z][A-Za-z /]*?)\s*:\s*(.*)$")
GRO_STATUSES = {"NOT YET REACHED", "REPORTED", "VERIFIED", "REVISED", "SUPERSEDED"}
GRO_PARAGRAPH_MAX_WORDS = 120
PLACEHOLDERS = ("NOT YET FILLED", "AWAITING RESEARCHER", "NOT YET DECIDED", "—", "-")
RECORD_DIRS = {
    "DAT": ROOT / "data" / "records",
    "PRM": ROOT / "parameters",
    "RUN": ROOT / "analysis" / "runs",
}
DECISION_LOG = ROOT / "research" / "decision-log.md"
REFERENCE_SCAN_DIRS = (
    ROOT / "literature",
    ROOT / "analysis",
    ROOT / "research",
    ROOT / "manuscript",
    ROOT / "reviews",
)
SKIP_SCAN_PREFIXES = ("examples/", "templates/", "parameters/presets/", "docs/")


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/"):
            continue
        yield path, rel


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_markdown_links(errors: list[str]) -> None:
    for path, rel in iter_files():
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        if text is None:
            continue
        for raw in LINK_RE.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{rel}: missing relative link target: {raw}")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        match = FRONTMATTER_LINE_RE.match(line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    return {}


def check_skills(errors: list[str]) -> None:
    skills_root = ROOT / ".agents" / "skills"
    if not skills_root.is_dir():
        errors.append(".agents/skills directory is missing")
        return
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        expected = skill_dir.name
        if fm.get("name") != expected:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: frontmatter name "
                f"{fm.get('name')!r} != directory {expected!r}"
            )
        if not fm.get("description"):
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")


def check_stale_skill_names(errors: list[str]) -> None:
    needle = "dissertation-"
    for path, rel in iter_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if rel in STALE_EXCLUDE or rel.startswith(STALE_EXCLUDE_PREFIXES):
            continue
        text = read_text(path)
        if text is not None and needle in text.lower():
            errors.append(f"{rel}: contains stale skill prefix '{needle}'")


def check_bibliography(errors: list[str]) -> None:
    bib = ROOT / "literature" / "references.bib"
    if not bib.is_file():
        errors.append("literature/references.bib is missing")
        return
    text = bib.read_text(encoding="utf-8").strip()
    if not text:
        return
    if text.count("{") != text.count("}"):
        errors.append("literature/references.bib: unbalanced braces")
    keys = BIB_ENTRY_RE.findall(text)
    at_count = len(re.findall(r"(?m)^\s*@", text))
    if at_count != len(keys):
        errors.append(
            "literature/references.bib: one or more BibTeX entries "
            "do not match '@type{citation-key,'"
        )
    duplicates = sorted({k for k in keys if keys.count(k) > 1})
    if duplicates:
        errors.append(
            "literature/references.bib: duplicate citation keys: "
            + ", ".join(duplicates)
        )


def check_sensitive_paths(errors: list[str]) -> None:
    for path, rel in iter_files():
        if rel == ".env" or (rel.startswith(".env.") and rel != ".env.example"):
            errors.append(f"{rel}: environment secret file must not be committed")
        if rel.startswith(SENSITIVE_PREFIXES):
            errors.append(f"{rel}: sensitive/private path must not be committed")


# --- Coherence: every referenced ID must exist -------------------------------

def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def id_type(identifier: str) -> str:
    return identifier.split("-", 1)[0]


def find_ids(text: str) -> set[str]:
    return {m.group(0) for m in ID_RE.finditer(strip_code(text))}


def table_rows(text: str):
    """Yield (first_cell, row_text) for Markdown table body rows."""
    for line in strip_code(text).splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not cells or set(cells[0]) <= {"-", ":", " "}:
            continue
        yield cells[0], stripped


def defined_statements() -> set[str]:
    text = read_text(BRAIN) if BRAIN.is_file() else None
    if text is None:
        return set()
    defined = set()
    for first_cell, _ in table_rows(text):
        match = ID_RE.fullmatch(first_cell)
        if match and id_type(first_cell) in STATEMENT_TYPES:
            defined.add(first_cell)
    return defined


def record_files() -> dict[str, Path]:
    """Map record IDs to the file that defines them."""
    records: dict[str, Path] = {}
    for prefix, folder in RECORD_DIRS.items():
        if not folder.is_dir():
            continue
        for path in folder.rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("parameters/presets/"):
                continue
            match = ID_RE.search(path.stem)
            if match and id_type(match.group(0)) == prefix:
                records[match.group(0)] = path
    literature = ROOT / "literature"
    if literature.is_dir():
        for path in literature.rglob("*.md"):
            match = ID_RE.search(path.stem)
            if match and id_type(match.group(0)) == "SRC":
                records[match.group(0)] = path
    if DECISION_LOG.is_file():
        text = read_text(DECISION_LOG) or ""
        for first_cell, _ in table_rows(text):
            if ID_RE.fullmatch(first_cell) and id_type(first_cell) == "DEC":
                records[first_cell] = DECISION_LOG
    return records


def scanned_sources() -> list[tuple[str, str]]:
    """Files whose ID references must resolve: brain.md and record files."""
    sources: list[tuple[str, str]] = []
    if BRAIN.is_file():
        sources.append(("brain.md", read_text(BRAIN) or ""))
    if GRO.is_file():
        sources.append(("GRO.md", read_text(GRO) or ""))
    for prefix, folder in RECORD_DIRS.items():
        if not folder.is_dir():
            continue
        for path in sorted(folder.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("parameters/presets/") or path.name == "README.md":
                continue
            sources.append((rel, read_text(path) or ""))
    return sources


def reference_corpus() -> str:
    """Text in which a record may legitimately be referenced (for orphan warnings)."""
    parts = [text for _, text in scanned_sources()]
    for folder in REFERENCE_SCAN_DIRS:
        if not folder.is_dir():
            continue
        for path in folder.rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith(SKIP_SCAN_PREFIXES):
                continue
            parts.append(read_text(path) or "")
    return "\n".join(parts)


def check_coherence_links(errors: list[str], warnings: list[str]) -> None:
    if not BRAIN.is_file():
        errors.append("brain.md is missing at the repository root")
        return
    statements = defined_statements()
    records = record_files()
    for rel, text in scanned_sources():
        for identifier in sorted(find_ids(text)):
            kind = id_type(identifier)
            if kind in STATEMENT_TYPES:
                if identifier not in statements:
                    errors.append(
                        f"{rel}: references statement {identifier} that is not "
                        "defined in a brain.md table"
                    )
            elif kind in RECORD_TYPES:
                if identifier not in records:
                    errors.append(
                        f"{rel}: references {identifier} but no record file or "
                        "decision-log row defines it"
                    )
    corpus = reference_corpus()
    for identifier, path in sorted(records.items()):
        if id_type(identifier) == "DEC":
            continue
        rel = path.relative_to(ROOT).as_posix()
        own_text = read_text(path) or ""
        outside = corpus.replace(own_text, "", 1)
        if identifier not in find_ids(outside):
            warnings.append(f"{rel}: {identifier} is not referenced anywhere (orphan)")


def parse_gro_entries(text: str) -> list[dict]:
    """Split GRO.md into entries with their fields and prose paragraph."""
    entries: list[dict] = []
    current: dict | None = None
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = GRO_ENTRY_RE.match(line)
        if heading:
            current = {
                "id": heading.group(1),
                "number": int(heading.group(2)),
                "fields": {},
                "prose": [],
            }
            entries.append(current)
            continue
        if current is None:
            continue
        if line.startswith("#"):
            current = None
            continue
        field = GRO_FIELD_RE.match(line)
        if field:
            current["fields"][field.group(1).strip().lower()] = field.group(2).strip()
            continue
        if line.strip():
            current["prose"].append(line.strip())
    return entries


def check_gro(errors: list[str], warnings: list[str]) -> None:
    """GRO sections follow the research outline: fixed numbers, one paragraph
    each, verified by the researcher and never by the agent."""
    if not GRO.is_file():
        errors.append("GRO.md is missing at the repository root")
        return
    text = read_text(GRO) or ""
    entries = parse_gro_entries(text)
    if not entries:
        errors.append("GRO.md defines no sections; the research outline must be visible")
        return
    seen: set[int] = set()
    awaiting: list[str] = []
    for entry in entries:
        eid = entry["id"]
        if entry["number"] in seen:
            errors.append(f"GRO.md: duplicate section number {eid}")
        seen.add(entry["number"])
        fields = entry["fields"]
        raw_status = fields.get("status", "")
        status = raw_status.split("—")[0].split("--")[0].strip().upper()
        if status not in GRO_STATUSES:
            errors.append(
                f"GRO.md: {eid} has Status {raw_status!r}; expected one of "
                + ", ".join(sorted(GRO_STATUSES))
            )
        if status == "VERIFIED":
            verified = fields.get("verified by / date", "").strip()
            if not verified or any(ph in verified.upper() for ph in PLACEHOLDERS):
                errors.append(
                    f"GRO.md: {eid} is VERIFIED but names no verifier and date; "
                    "only the researcher verifies a section"
                )
        if status in {"REPORTED", "REVISED"}:
            awaiting.append(eid)
        if status not in {"NOT YET REACHED", ""}:
            words = len(" ".join(entry["prose"]).split())
            if words > GRO_PARAGRAPH_MAX_WORDS:
                warnings.append(
                    f"GRO.md: {eid} paragraph is {words} words (limit "
                    f"{GRO_PARAGRAPH_MAX_WORDS}); the decision may not be clear enough yet"
                )
    if awaiting:
        warnings.append(
            "GRO.md: awaiting researcher verification: " + ", ".join(awaiting)
        )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    check_markdown_links(errors)
    check_skills(errors)
    check_stale_skill_names(errors)
    check_bibliography(errors)
    check_sensitive_paths(errors)
    check_coherence_links(errors, warnings)
    check_gro(errors, warnings)

    if warnings:
        print("Warnings (not failures):")
        for warning in sorted(set(warnings)):
            print(f"  - {warning}")

    if errors:
        print("Repository integrity checks FAILED:")
        for error in sorted(set(errors)):
            print(f"  - {error}")
        return 1

    print("Repository integrity checks passed.")
    print(
        "Scope: mechanical repository integrity only; "
        "this is not an academic quality assessment."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
