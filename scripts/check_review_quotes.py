#!/usr/bin/env python3
"""Check that every quotation of the volumes in REVIEW.md is verbatim and cited to its page.

Usage: python3 -I scripts/check_review_quotes.py

Scope: REVIEW.md from "## The short answer" up to "## Appendix C" (the header gives the
Zenodo titles, Appendix C is generated, and the references quote titles of other works).
A quotation is a double-quoted fragment (straight or curly). Quotation marks are reserved for
words from the volumes; titles of other works and terms this review proposes are in italics.

Every quotation must occur in a volume. A quotation of 25 characters or more needs a citation
that gives a page, such as (Vol. I §13.2, p. 63): the parenthesis that encloses the quotation,
or else the first citation after it in the same paragraph, so several quotations may share one.
The quotation must occur on a page it cites. Exit status 1 lists every miss.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_audit_quotes", ROOT / "scripts" / "check_audit_quotes.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

START, STOP = "## The short answer", "## Appendix C"
CITATION = re.compile(r"\(([^()]*(?:§|\bCh\.|\bChapter|\bA\.\d|\bApp\.|\bp\.|\bpp\.|front matter|"
                      r"Key Definitions|guide|Common Rules|title page|contents|Abstract)[^()]*)\)")
LINK_TARGET = re.compile(r"\]\([^)]*\)")


def quotations(line):
    for pattern in (r'"([^"]*)"', r"“([^”]*)”"):
        for match in re.finditer(pattern, line):
            yield match.group(1).strip(), match.start(), match.end()


def enclosing(line, start, end):
    """The text inside the parenthesis that encloses line[start:end], if there is one."""
    depth = 0
    for i in range(start - 1, -1, -1):
        if line[i] == ")":
            depth += 1
        elif line[i] == "(" and depth:
            depth -= 1
        elif line[i] == "(":
            depth = 0
            for j in range(end, len(line)):
                if line[j] == "(":
                    depth += 1
                elif line[j] == ")" and depth:
                    depth -= 1
                elif line[j] == ")":
                    return line[i + 1:j]
            return None
    return None


def citation_for(line, start, end):
    """The citation governing a quotation: its enclosing parenthesis, else the next citation."""
    inside = enclosing(line, start, end)
    if inside is not None and CITATION.search(f"({inside})"):
        return inside
    after = CITATION.search(line, end)
    return after.group(1) if after else None


def main():
    text = (ROOT / "REVIEW.md").read_text(encoding="utf-8")
    body = text[text.index(START):text.index(STOP)]
    offset = text[:text.index(START)].count("\n")
    total = misses = 0
    for number, line in enumerate(body.splitlines(), start=offset + 1):
        line = LINK_TARGET.sub("]", line)  # link targets are not citations
        for quote, start, end in quotations(line):
            if not quote:
                continue
            total += 1
            miss = None
            if not audit.raw.found(quote):
                miss = "NOT FROM THE VOLUMES"
            elif len(quote) >= 25:
                citation = citation_for(line, start, end)
                if not citation:
                    miss = "NO CITATION"
                elif not audit.cited_pages(citation):
                    miss = f"NO PAGE in ({citation[:40]})"
                else:
                    miss = audit.check(quote, None, citation)
            if miss:
                misses += 1
                print(f"{miss} REVIEW.md:{number}: {' '.join(quote.split())[:90]}")
    print(f"\n{total - misses}/{total} quotations in REVIEW.md verbatim and cited to their page")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
