#!/usr/bin/env python3
"""Validate the audit files in docs/audit/ and write their index, docs/audit/README.md.

Usage:
    python3 -I scripts/audit_index.py           # validate, then rewrite the index
    python3 -I scripts/audit_index.py --check   # validate; fail if the index is stale

The same run regenerates the body of the "## Appendix C: Issue register" section of
REVIEW.md, from its heading to the next level-two heading.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditlib import AUDIT_DIR, REPO, ROOT, SEVERITIES, broken_links, load_all  # noqa: E402

HEADER = """# Audit register

Every issue found in the audit of *Foundations of Reason 8.0* (Vol I) and *Engineering of
Reason 3.5* (Vol II) has a standalone file in this directory and a GitHub issue with the
same ID. The files are the source of truth; this index and the issues are generated from
them by `scripts/audit_index.py` and `scripts/file_issues.py`. The full argument is in
[`REVIEW.md`](../../REVIEW.md).

**Severity scale**

- **Major**: undermines a central claim, the testability of the programme, or safety. It
  should be resolved before the work is presented as a tested theory or before any stage
  beyond simulation.
- **Medium**: affects a component claim, the clarity of a key construct, or the
  experimental design. It should be resolved before the first comparative experiment or
  journal submission.
- **Minor**: editorial, citation or formatting. It does not change the substance, but
  it costs readers time.

Page and line numbers refer to the English PDFs in `sources/` and the `-layout` text in
`text/`.
"""

TITLES = {"major": "Major", "medium": "Medium", "minor": "Minor"}


def render(audits):
    counts = {s: sum(a.meta["severity"] == s for a in audits) for s in SEVERITIES}
    lines = [HEADER]
    lines.append(
        f"**{len(audits)} issues:** {counts['major']} major, {counts['medium']} medium, "
        f"{counts['minor']} minor.\n"
    )
    for severity in SEVERITIES:
        group = [a for a in audits if a.meta["severity"] == severity]
        if not group:
            continue
        lines.append(f"## {TITLES[severity]} ({len(group)})\n")
        lines.append("| ID | Issue | Area | Volumes | Review | GitHub |")
        lines.append("|---|---|---|---|---|---|")
        for a in group:
            issue = (f"[#{a.number}](https://github.com/{REPO}/issues/{a.number})"
                     if a.number else "pending")
            lines.append(
                f"| [{a.id}]({a.path.name}) | {a.meta['title']} | {a.meta['area']} | "
                f"{a.meta['volumes']} | {a.meta['review']} | {issue} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


APPENDIX = "## Appendix C: Issue register"
INTRO = ("Each issue has a standalone file in [`docs/audit/`](docs/audit/README.md) with evidence, "
         "page references and a resolution criterion, and a GitHub issue with the same ID. "
         "The section references in parentheses point back into this review.")


def review_block(audits):
    """The body of the register appendix in REVIEW.md: one line per issue, linked to its file."""
    lines = [APPENDIX, "", INTRO, ""]
    for severity in SEVERITIES:
        group = [a for a in audits if a.meta["severity"] == severity]
        if not group:
            continue
        lines.append(f"**{TITLES[severity]} ({len(group)})**")
        lines.append("")
        for a in group:
            lines.append(f"- [{a.id}](docs/audit/{a.path.name}) {a.meta['title']} ({a.meta['review']})")
        lines.append("")
    return "\n".join(lines)


BARE_ID = re.compile(r"(?<![\[\w/-])(M(?:AJ|ED|IN)-\d\d)(?![\w\]-])")


def link_ids(review_text, audits):
    """Turn bare register IDs in the review body (before Appendix C) into links to their files."""
    files = {a.id: a.path.name for a in audits}
    head, sep, tail = review_text.partition(APPENDIX)

    def repl(match):
        ident = match.group(1)
        return f"[{ident}](docs/audit/{files[ident]})" if ident in files else ident

    return BARE_ID.sub(repl, head) + sep + tail


def with_review_block(review_text, audits):
    if APPENDIX not in review_text:
        raise SystemExit(f"REVIEW.md lacks the heading '{APPENDIX}'")
    head, rest = review_text.split(APPENDIX, 1)
    following = rest.find("\n## ")
    tail = rest[following + 1:] if following >= 0 else ""
    return head + review_block(audits) + ("\n" + tail if tail else "")


def main(argv):
    audits = load_all()
    errors, seen = [], set()
    for a in audits:
        errors += [f"{a.path.name}: {p}" for p in a.problems()]
        errors += [f"{a.path.name}: broken link {t}" for t in broken_links(a)]
        if a.id in seen:
            errors.append(f"{a.path.name}: duplicate id {a.id}")
        seen.add(a.id)
    if errors:
        print("\n".join(errors))
        return 1
    index = AUDIT_DIR / "README.md"
    review = ROOT / "REVIEW.md"
    text = render(audits)
    review_text = review.read_text(encoding="utf-8")
    new_review = link_ids(with_review_block(review_text, audits), audits)
    if "--check" in argv:
        stale = []
        if not index.exists() or index.read_text(encoding="utf-8") != text:
            stale.append("docs/audit/README.md")
        if new_review != review_text:
            stale.append("REVIEW.md register appendix")
        if stale:
            print(" and ".join(stale) + " stale; run scripts/audit_index.py")
            return 1
        print(f"audit register OK: {len(audits)} files, index and review appendix current")
        return 0
    index.write_text(text, encoding="utf-8")
    review.write_text(new_review, encoding="utf-8")
    print(f"wrote docs/audit/README.md and the REVIEW.md register appendix ({len(audits)} issues)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
