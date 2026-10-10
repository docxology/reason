#!/usr/bin/env python3
"""Locate quotes in an extracted volume text and report the PDF page and text line.

Usage:
    python3 -I scripts/locate.py text/foundations-8.0.txt "quote one" ["quote two" ...]
    python3 -I scripts/locate.py text/engineering-3.5.txt --line 1234

The text files come from pdftotext, which writes a form feed at every page break, so
the page of an offset is one plus the number of form feeds before it. Whitespace,
curly quotes, dashes and ligatures are normalized on both sides, so a quote that wraps
across lines or uses typographic punctuation still matches. Exit status is 1 if any
quote is not found.
"""
import re
import sys

TRANSLATE = str.maketrans({
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "−": "-", "­": None,
    "ﬁ": "fi", "ﬂ": "fl",
})


def normalize_with_offsets(text):
    """Collapse whitespace and normalize punctuation, keeping a map to original offsets."""
    chars, offsets = [], []
    previous_space = False
    for i, ch in enumerate(text):
        if ch.isspace():
            if not previous_space:
                chars.append(" ")
                offsets.append(i)
            previous_space = True
            continue
        previous_space = False
        for out in ch.translate(TRANSLATE):
            chars.append(out)
            offsets.append(i)
    return "".join(chars), offsets


def normalize(quote):
    return re.sub(r"\s+", " ", quote.translate(TRANSLATE)).strip()


def page_and_line(text, offset):
    before = text[:offset]
    return before.count("\f") + 1, before.count("\n") + 1


SUBSECTION = re.compile(r"^\s{0,3}(\d{1,2}\.[0-9A-Z]{1,3}(?:\.[0-9A-Z]{1,3}){0,3})\.\s+[A-Z\u2018\u201c\"]")
CHAPTER_I = re.compile(r"^\s{0,3}Chapter (\d{1,2})\.\s+[A-Z]")
CHAPTER_II = re.compile(r"^(2[1-9]|3[0-4])\.\s+[A-Z]\S*(?:\s+\S+){2,}")
APPENDIX_SECTION = re.compile(r"^\s{0,3}(A\.[1-5](?:\.\d)?)\.\s+[A-Z]")
UPPER = re.compile(r"^\s{0,3}(CONCLUSION|OPEN RESEARCH DIRECTIONS|REFERENCES|APPENDIX [AB])\b")


def section_index(text):
    """(line, label) for chapter, section and appendix headings in the body.

    The contents pages repeat every heading, so the body is taken to start at the last
    occurrence of the first chapter heading; everything before it is front matter.
    """
    rows = text.split("\n")
    volume_two = "ENGINEERING OF REASON" in text[:20000]
    chapter = CHAPTER_II if volume_two else CHAPTER_I
    first = [n for n, row in enumerate(rows, 1)
             if (m := chapter.match(row)) and int(m.group(1)) == (21 if volume_two else 1)]
    body_start = first[-1] if first else 1
    index = []
    for number, row in enumerate(rows[body_start - 1:], start=body_start):
        if len(row.strip()) > 110:
            continue
        if m := chapter.match(row):
            index.append((number, "Ch. " + m.group(1)))
        elif m := SUBSECTION.match(row):
            index.append((number, "§" + m.group(1)))
        elif m := APPENDIX_SECTION.match(row):
            index.append((number, m.group(1)))
        elif m := UPPER.match(row):
            index.append((number, m.group(1).title()))
    return index


def enclosing(index, line):
    label = "front matter"
    for start, name in index:
        if start > line:
            break
        label = name
    return label


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    path = argv[1]
    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    if argv[2] == "--line":
        line = int(argv[3])
        offset = sum(len(row) + 1 for row in text.split("\n")[: line - 1])
        page, _ = page_and_line(text, offset)
        print(f"{path}:{line} page {page} {enclosing(section_index(text), line)}")
        return 0

    index = section_index(text)
    flat, offsets = normalize_with_offsets(text)
    lowered = flat.lower()
    status = 0
    for quote in argv[2:]:
        needle = normalize(quote)
        hits = [m.start() for m in re.finditer(re.escape(needle), flat)]
        note = ""
        if not hits:
            hits = [m.start() for m in re.finditer(re.escape(needle.lower()), lowered)]
            note = " (case-insensitive)"
        if not hits:
            print(f"NOT FOUND: {needle[:90]}")
            status = 1
            continue
        for hit in hits:
            page, line = page_and_line(text, offsets[hit])
            print(f"{path}:{line} page {page} {enclosing(index, line)}{note}: {needle[:90]}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv))
