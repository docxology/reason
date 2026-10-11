#!/usr/bin/env python3
"""Check that the quotations in docs/audit/ occur in the volumes, on the pages cited.

Usage: python3 -I scripts/check_audit_quotes.py [ID ...]

Checked: every quotation in the first section (Claims under review or Passages under
review), and every quotation of at least 25 characters in Finding, Evidence and Why it
matters. A quotation is a double-quoted fragment (straight or curly); in the first section,
a backtick span containing a space counts too. Titles of other works are set in italics, not
quoted. Matching normalizes whitespace, typographic punctuation and hyphenated line breaks,
ignores case, and treats "[...]" as a gap.

A quotation that follows a bold label such as **Vol II §29.0.1, p. 68:** must also occur in
that volume and on one of the pages cited in the label, unless it is followed directly by
its own citation in parentheses, such as "..." (§29.A, p. 71), which then applies instead. A
quotation that runs over a page break counts for both pages. With IDs, only those files are
checked, and their structure problems are listed too. Exit status 1 lists every miss.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from auditlib import FIRST_SECTIONS, LABEL, items, load_all  # noqa: E402

spec = importlib.util.spec_from_file_location("check_raw_quotes", ROOT / "scripts" / "check_raw_quotes.py")
raw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(raw)

VOLUME_TEXT = {"I": "foundations-8.0", "II": "engineering-3.5"}
VOLUME = re.compile(r"\bVol(?:ume)?s?\.? (I{1,2})\b")
RANGE = r"\d+(?:\s*[–-]\s*\d+)?"
PAGES = re.compile(rf"\bpp?\. ?({RANGE}(?:\s*(?:,|and)\s*{RANGE})*)")
RUNNING_HEAD = re.compile(r"\s*(FOUNDATIONS|ENGINEERING) OF REASON · \d\.\d\s*")
CHECKED = ("Finding", "Evidence", "Why it matters")


def page_variants(volume):
    """Per PDF page, the canonical lower-case text without running head and page number."""
    text = (ROOT / "text" / f"{VOLUME_TEXT[volume]}.txt").read_text(encoding="utf-8")
    pages = []
    for page in text.split("\f"):
        lines = [line for line in page.splitlines() if line.strip()]
        if lines and RUNNING_HEAD.fullmatch(lines[0]):
            lines = lines[1:]
        if lines and lines[-1].strip().isdigit():
            lines = lines[:-1]
        flat = raw.canon(raw.locate.normalize("\n".join(lines))).lower()
        pages.append(flat)
    return pages


PAGE_TEXT = {volume: page_variants(volume) for volume in VOLUME_TEXT}


def pages_of(part, volume):
    """PDF pages on which a canonical piece of a quotation occurs (both pages if it spans a break)."""
    part = part.lower()
    texts = PAGE_TEXT[volume]
    hits = {i + 1 for i, t in enumerate(texts) if part in t or part in t.replace("- ", "-")}
    if not hits:
        for i in range(len(texts) - 1):
            joined = texts[i] + " " + texts[i + 1]
            if part in joined or part in joined.replace("- ", "-"):
                hits |= {i + 1, i + 2}
    return hits


INLINE = re.compile(r"\s*\(([^()]*\bpp?\. ?\d+[^()]*)\)")


def fragments(text, minimum, backticks):
    """(quotation, inline citation) pairs; quotes pair in order, so prose between two is never taken."""
    patterns = [(r'"([^"]*)"', 0), (r"“([^”]*)”", 0)]
    if backticks:
        patterns.append((r"`([^`]*)`", 12))
    found = []
    for pattern, floor in patterns:
        for match in re.finditer(pattern, text):
            quote = match.group(1).strip()
            if len(quote) < max(minimum, floor) or (floor and " " not in quote):
                continue
            inline = INLINE.match(text, match.end())
            found.append((quote, inline.group(1) if inline else None))
    return found


def segments(text):
    """(label, text) pieces: each bold 'label:' governs the text up to the next label."""
    marks = list(LABEL.finditer(text))
    if not marks:
        return [(None, text)]
    out = [(None, text[:marks[0].start()])]
    for i, mark in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out.append((mark.group(1), text[mark.end():end]))
    return out


def cited_pages(label):
    pages = set()
    for match in PAGES.finditer(label or ""):
        for start, end in re.findall(r"(\d+)(?:\s*[–-]\s*(\d+))?", match.group(1)):
            pages |= set(range(int(start), int(end or start) + 1))
    return pages


def check(fragment, label, inline=None):
    """None if the quotation is where its citation says, else a description of the miss."""
    hits = raw.found(fragment)
    if not hits:
        return "NOT FOUND"
    if inline:  # an inline citation names its own pages, and its own volume if it gives one
        label = inline if VOLUME.search(inline) else " ".join(
            [f"Vol {v}" for v in VOLUME.findall(label or "")] + [inline])
    volumes = set(VOLUME.findall(label or ""))
    if volumes and not hits & volumes:
        return f"not in Vol {'/'.join(sorted(volumes))} (found in Vol {'/'.join(sorted(hits))})"
    cited = cited_pages(label)
    if not cited:
        return None
    located = set()
    for volume in (hits & volumes) or hits:
        for part in raw.parts(fragment):
            located |= pages_of(part, volume)
    if located and not located & cited:
        shown = ", ".join(str(p) for p in sorted(located)[:6])
        return f"cited p. {min(cited)}{'-' + str(max(cited)) if len(cited) > 1 else ''}, found on p. {shown}"
    return None


def units(audit):
    """(section, label, text, minimum length) for every stretch of the file that is checked."""
    sections = audit.sections()
    out = []
    if sections and sections[0][0] in FIRST_SECTIONS:
        for item in items(sections[0][1]):
            out += [(sections[0][0], label, text, 8) for label, text in segments(item)]
    preamble = audit.body.split("\n## ", 1)[0]  # the Finding paragraph in the older layout
    if "**Finding.**" in preamble:
        out.append(("Finding", None, preamble, 25))
    for name, text in sections:
        if name in CHECKED:
            for item in items(text) or [text]:
                out += [(name, label, piece, 25) for label, piece in segments(item)]
    return out


def main(argv):
    wanted = set(argv)
    audits = [a for a in load_all() if not wanted or a.id in wanted]
    total = misses = paged = 0
    problems = []
    for audit in audits:
        if wanted:
            problems += [f"STRUCTURE {audit.id}: {p}" for p in audit.structure_problems()]
        for section, label, text, minimum in units(audit):
            for fragment, inline in fragments(text, minimum, backticks=section in FIRST_SECTIONS):
                total += 1
                paged += bool(cited_pages(inline or label))
                miss = check(fragment, label, inline)
                if miss:
                    misses += 1
                    print(f"{miss} {audit.id} [{section}]: {' '.join(fragment.split())[:100]}")
    for problem in problems:
        print(problem)
    print(f"\n{total - misses}/{total} quotations in docs/audit/ found in the volumes "
          f"({paged} checked against the cited volume and page)")
    return 1 if misses or problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
