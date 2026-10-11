"""Shared helpers for the audit register in docs/audit/.

Each audit file is markdown with a small front-matter block of `key: value` lines:

    ---
    id: MAJ-01
    title: No comparative evidence yet for the central hypothesis
    severity: major
    area: evidence
    volumes: I, II
    sections: Vol I A.2, A.2.1; Vol II §27.B
    review: §5.2(a), §7
    status: open
    github_issue: 12
    ---

The body opens with "# ID · title" and then has these level-two sections, in order:

    ## Claims under review      the author's claims the issue responds to, quoted verbatim, one
                                list item each, labelled **Vol I|II <section>, p. N:** (an issue
                                about how the text is printed uses "## Passages under review")
    ## Finding                  what is wrong or missing, in prose
    ## Evidence                 further passages, data and credits ("Already in the text")
    ## Why it matters
    ## Ideas & possible recommendations   at least two options, offered rather than prescribed
    ## Resolved when            checklist
    ## Related                  links into REVIEW.md and other issues

The files are the single source of truth: the index (docs/audit/README.md) and the
GitHub issues are generated from them.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = ROOT / "docs" / "audit"
REPO = "docxology/reason"
BLOB = f"https://github.com/{REPO}/blob/main"

SEVERITIES = {"major": "MAJ", "medium": "MED", "minor": "MIN"}
AREAS = {
    "framing", "theory", "definitions", "formal", "evidence", "testability",
    "architecture", "prior-art", "safety", "editorial", "references", "code",
    "provenance",
}
REQUIRED = ("id", "title", "severity", "area", "volumes", "sections", "review", "status")
STATUSES = {"open", "acknowledged", "resolved", "wontfix"}

FIRST_SECTIONS = ("Claims under review", "Passages under review")
SECTIONS = ("Finding", "Evidence", "Why it matters", "Ideas & possible recommendations",
            "Resolved when", "Related")
LABEL = re.compile(r"\*\*([^*]+?):\*\*")
CITATION = re.compile(r"\bVol(?:ume)?s? I{1,2}\b.*\bpp?\. ?\d+")
QUOTATION = re.compile(r'"[^"]{4,}"|\u201c[^\u201d]{4,}\u201d|`[^`]*\s[^`]*`')

FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def items(section_text):
    """Top-level list items of a section, each with its indented continuation lines."""
    return [chunk for chunk in re.split(r"\n(?=- )", "\n" + section_text) if chunk.startswith("- ")]


class AuditFile:
    def __init__(self, path):
        self.path = Path(path)
        text = self.path.read_text(encoding="utf-8")
        match = FRONT.match(text)
        if not match:
            raise ValueError(f"{self.path.name}: missing front matter")
        self.meta = {}
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            key, _, value = line.partition(":")
            value = value.strip()
            if len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1]
            self.meta[key.strip()] = value
        self.body = text[match.end():].lstrip("\n")

    @property
    def id(self):
        return self.meta["id"]

    @property
    def number(self):
        value = self.meta.get("github_issue", "")
        return int(value) if value.isdigit() else None

    def sections(self):
        """The level-two sections of the body, in order, as (heading, text) pairs."""
        chunks = re.split(r"^## (.+)\n", self.body, flags=re.M)
        return [(chunks[i].strip(), chunks[i + 1]) for i in range(1, len(chunks), 2)]

    def section(self, heading):
        return next((text for name, text in self.sections() if name == heading), "")

    def sort_key(self):
        order = list(SEVERITIES).index(self.meta["severity"])
        return order, self.id

    def problems(self):
        found = [f"missing field '{key}'" for key in REQUIRED if not self.meta.get(key)]
        severity = self.meta.get("severity")
        if severity not in SEVERITIES:
            found.append(f"severity '{severity}' not in {sorted(SEVERITIES)}")
        elif not self.id.startswith(SEVERITIES[severity] + "-"):
            found.append(f"id '{self.id}' does not match severity '{severity}'")
        if self.meta.get("area") not in AREAS:
            found.append(f"area '{self.meta.get('area')}' not in {sorted(AREAS)}")
        if self.meta.get("status") not in STATUSES:
            found.append(f"status '{self.meta.get('status')}' not in {sorted(STATUSES)}")
        if not self.path.name.startswith(self.id + "-"):
            found.append(f"file name does not start with '{self.id}-'")
        if not self.body.startswith(f"# {self.id} "):
            found.append(f"body must open with '# {self.id} ...'")
        found += self.structure_problems()
        return found

    def structure_problems(self):
        found = []
        sections = self.sections()
        names = [name for name, _ in sections]
        if not names or names[0] not in FIRST_SECTIONS:
            return [f"first section must be one of {FIRST_SECTIONS}, found {names[:1]}"]
        if tuple(names[1:]) != SECTIONS:
            found.append(f"sections after '{names[0]}' must be {list(SECTIONS)}, found {names[1:]}")
        if self.body.split("\n## ", 1)[0].strip() != self.body.splitlines()[0].strip():
            found.append("nothing may stand between the title and the first section")
        claims = items(sections[0][1])
        if not claims:
            found.append(f"'{names[0]}' has no list items")
        for item in claims:
            labels = [" ".join(label.split()) for label in LABEL.findall(item)]
            head = " ".join(item.split())[:70]
            if not labels or not all(CITATION.search(label) for label in labels):
                found.append(f"item needs a bold 'Vol I|II <section>, p. N:' label: {head}")
            if not QUOTATION.search(item):
                found.append(f"item quotes nothing from the volumes: {head}")
        if len(items(self.section("Ideas & possible recommendations"))) < 2:
            found.append("'Ideas & possible recommendations' needs at least two list items")
        return found

    def set_meta(self, key, value):
        self.meta[key] = str(value)
        lines = [f"{k}: {v}".rstrip() for k, v in self.meta.items()]
        text = "---\n" + "\n".join(lines) + "\n---\n\n" + self.body
        self.path.write_text(text, encoding="utf-8")


def github_anchor(heading):
    """The fragment GitHub generates for a markdown heading."""
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")


def anchors(path):
    """All heading anchors of a markdown file, with GitHub's -1, -2 suffixes for repeats."""
    seen, found = {}, set()
    in_code = False
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code or not line.startswith("#"):
            continue
        slug = github_anchor(line.lstrip("#"))
        count = seen.get(slug, 0)
        found.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1
    return found


def broken_links(audit):
    """Relative links in an audit file whose target file or heading anchor does not exist."""
    broken = []
    for target in re.findall(r"\]\(([^)\s]+)\)", audit.body):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, fragment = target.partition("#")
        resolved = (audit.path.parent / path).resolve() if path else audit.path
        if not resolved.exists():
            broken.append(target)
        elif fragment and resolved.suffix == ".md" and fragment not in anchors(resolved):
            broken.append(target)
    return broken


def load_all():
    files = [AuditFile(p) for p in sorted(AUDIT_DIR.glob("M[AIE][JDN]-[0-9][0-9]-*.md"))]
    return sorted(files, key=AuditFile.sort_key)


def labels_for(audit):
    labels = ["audit", f"severity: {audit.meta['severity']}", f"area: {audit.meta['area']}"]
    for volume in (v.strip() for v in audit.meta["volumes"].split(",")):
        if volume in ("I", "II"):
            labels.append(f"vol {volume}")
    return labels


def absolutize(markdown, audits):
    """Rewrite repository-relative links for use outside the repository (issue bodies)."""
    def repl(match):
        target = match.group(1)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        if target.startswith("../../"):
            path = target[len("../../"):]
        else:
            path = "docs/audit/" + target
        return f"]({BLOB}/{path})"

    text = re.sub(r"\]\(([^)\s]+)\)", repl, markdown)
    numbers = {a.id: a.number for a in audits if a.number}

    def link_id(match):
        ident = match.group(0)
        return f"{ident} (#{numbers[ident]})" if ident in numbers else ident

    # Link bare register IDs that are not already inside a markdown link or heading.
    out = []
    for line in text.splitlines():
        if line.startswith("#"):
            out.append(line)
            continue
        out.append(re.sub(r"(?<![\[\w/-])M(?:AJ|ED|IN)-\d\d(?![\w\]-])", link_id, line))
    return "\n".join(out) + "\n"
