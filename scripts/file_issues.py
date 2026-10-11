#!/usr/bin/env python3
"""Create or update one GitHub issue per audit file, and record its number in the file.

Usage:
    python3 -I scripts/file_issues.py --dry-run   # show what would be created or updated
    python3 -I scripts/file_issues.py             # create missing labels and issues
    python3 -I scripts/file_issues.py --sync      # also rewrite existing titles, bodies and labels

Idempotent: an issue is matched by the "[ID]" prefix of its title, so re-running never
creates duplicates. Requires an authenticated `gh` CLI with access to the repository.
"""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditlib import BLOB, REPO, absolutize, labels_for, load_all  # noqa: E402

LABELS = {
    "audit": ("5319e7", "Finding from the audit of Foundations of Reason 8.0 / Engineering of Reason 3.5"),
    "severity: major": ("b60205", "Undermines a central claim, testability, or safety"),
    "severity: medium": ("d93f0b", "Affects a component claim, key construct, or the experimental design"),
    "severity: minor": ("fbca04", "Editorial, citation or formatting"),
    "vol I": ("1d76db", "Foundations of Reason 8.0"),
    "vol II": ("0e8a16", "Engineering of Reason 3.5"),
}
AREA_COLOR = "c5def5"


def gh(*args, capture=True):
    result = subprocess.run(["gh", *args], check=True, text=True,
                            stdout=subprocess.PIPE if capture else None)
    return result.stdout if capture else ""


def ensure_labels(audits, dry_run):
    wanted = dict(LABELS)
    for a in audits:
        for label in labels_for(a):
            wanted.setdefault(label, (AREA_COLOR, f"Audit area: {label.split(': ', 1)[-1]}"))
    existing = {row["name"] for row in json.loads(
        gh("label", "list", "-R", REPO, "--limit", "200", "--json", "name"))}
    for name, (color, description) in sorted(wanted.items()):
        if name in existing:
            continue
        print(f"label + {name}")
        if not dry_run:
            gh("label", "create", name, "-R", REPO, "--color", color, "--description", description)


def body_for(audit, audits):
    source = f"{BLOB}/docs/audit/{audit.path.name}"
    footer = (f"\n---\n\nSource of truth: [`docs/audit/{audit.path.name}`]({source}). "
              f"Severity **{audit.meta['severity']}**, area **{audit.meta['area']}**, "
              f"volumes {audit.meta['volumes']}. Review sections: {audit.meta['review']}.\n")
    body = audit.body
    if body.startswith("# "):  # the issue title already carries the heading
        body = body.split("\n", 1)[1].lstrip("\n")
    return absolutize(body, audits) + footer


def main(argv):
    dry_run, sync = "--dry-run" in argv, "--sync" in argv
    audits = load_all()
    ensure_labels(audits, dry_run)
    issues = json.loads(gh("issue", "list", "-R", REPO, "--state", "all", "--limit", "500",
                           "--json", "number,title,labels"))
    by_id, labels_by_number = {}, {}
    for issue in issues:
        title = issue["title"]
        labels_by_number[issue["number"]] = {label["name"] for label in issue["labels"]}
        if title.startswith("[") and "]" in title:
            by_id.setdefault(title[1:title.index("]")], issue["number"])

    for audit in audits:
        title = f"[{audit.id}] {audit.meta['title']}"
        number = by_id.get(audit.id)
        if number is None:
            print(f"create {title}")
            if dry_run:
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as handle:
                handle.write(body_for(audit, audits))
            args = ["issue", "create", "-R", REPO, "--title", title, "--body-file", handle.name]
            for label in labels_for(audit):
                args += ["--label", label]
            url = gh(*args).strip().splitlines()[-1]
            number = int(url.rstrip("/").rsplit("/", 1)[-1])
            time.sleep(1.5)  # stay well under GitHub's secondary rate limit
        if audit.number != number:
            audit.set_meta("github_issue", number)
            print(f"  {audit.id} -> #{number}")

    if sync and not dry_run:
        audits = load_all()  # reload so cross-references resolve to issue numbers
        for audit in audits:
            with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as handle:
                handle.write(body_for(audit, audits))
            args = ["issue", "edit", str(audit.number), "-R", REPO,
                    "--title", f"[{audit.id}] {audit.meta['title']}", "--body-file", handle.name]
            wanted = set(labels_for(audit))
            have = labels_by_number.get(audit.number, set())
            ours = {label for label in have
                    if label == "audit" or label.startswith(("severity: ", "area: ", "vol "))}
            for label in sorted(wanted - have):
                args += ["--add-label", label]
            for label in sorted(ours - wanted):  # only labels this register manages
                args += ["--remove-label", label]
            gh(*args)
            print(f"synced #{audit.number} {audit.id}")
            time.sleep(1.0)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
