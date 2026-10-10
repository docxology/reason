#!/usr/bin/env python3
"""Check that every quotation in the Evidence sections of docs/audit/ occurs in the volumes.

Usage: python3 -I scripts/check_audit_quotes.py

A quotation is a double-quoted fragment (straight or curly) of at least 25 characters in an
Evidence section. Matching normalizes whitespace, typographic punctuation and hyphenated line
breaks, ignores case, and treats "[...]" as a gap. Exit status 1 lists every miss.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_raw_quotes", ROOT / "scripts" / "check_raw_quotes.py")
raw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(raw)


def evidence(text):
    match = re.search(r"^## Evidence\n(.*?)(?=^## )", text, re.S | re.M)
    return match.group(1) if match else ""


def main():
    total = misses = 0
    for path in sorted((ROOT / "docs" / "audit").glob("M*-*.md")):
        body = evidence(path.read_text(encoding="utf-8"))
        # Pair every quotation mark in order, then keep the long ones, so that text between two
        # separate quotations is never mistaken for a quotation.
        fragments = [f for f in re.findall(r'"([^"]*)"', body) if len(f.strip()) >= 25]
        fragments += [f for f in re.findall(r"\u201c([^\u201d]*)\u201d", body) if len(f.strip()) >= 25]
        for fragment in fragments:
            total += 1
            if not raw.found(fragment):
                misses += 1
                print(f"NOT FOUND {path.name}: {' '.join(fragment.split())[:110]}")
    print(f"\n{total - misses}/{total} quotations in docs/audit/ found in the volumes")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
