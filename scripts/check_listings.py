#!/usr/bin/env python3
"""Fail if a restored listing in repro/ differs from the PDF text by more than whitespace.

Usage: python3 -I scripts/check_listings.py

Each listing is cut from text/engineering-3.5.txt between its first and last printed line,
page furniture (running header, page number, form feeds, blank lines) is dropped, and both
sides are compared line by line after collapsing whitespace. Leading `#` comment lines at
the top of a restored file (the provenance note) are the only permitted addition.
"""
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = ROOT / "text" / "engineering-3.5.txt"
LISTINGS = [
    # (restored file, regex for the first printed line, regex for the last printed line)
    ("repro/v0_lower_loop.py", r'^\s*"""Lower-loop demonstration', r"^\s*run\(\)\s*$"),
    ("repro/diagnostic_cycle.py", r'^\s*"""Finite diagnostic controller', r"^\s*verify\(\)\s*$"),
]


def squash(line):
    return re.sub(r"\s+", " ", line).strip()


def printed(rows, first, last):
    start = next(i for i, row in enumerate(rows) if re.search(first, row))
    end = next(i for i, row in enumerate(rows) if i > start and re.search(last, row))
    kept = []
    for row in rows[start:end + 1]:
        row = row.replace("\f", "")
        if "ENGINEERING OF R" in row or re.fullmatch(r"\s*\d{1,3}\s*", row) or not row.strip():
            continue
        kept.append(squash(row))
    return kept


def restored(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    while lines and lines[0].startswith("#"):
        lines.pop(0)
    return [squash(line) for line in lines if line.strip()]


def main():
    rows = TEXT.read_text(encoding="utf-8").split("\n")
    failed = 0
    for name, first, last in LISTINGS:
        diff = list(difflib.unified_diff(printed(rows, first, last), restored(ROOT / name),
                                         "pdf", name, n=0, lineterm=""))
        if diff:
            failed += 1
            print(f"DIFFERS  {name}")
            print("\n".join(line[:150] for line in diff[:40]))
        else:
            print(f"ok       {name} matches the printed listing up to whitespace")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
