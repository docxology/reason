# Verify and render the review

## Local evidence gate

Use Python 3.11 or newer, Make, and `shasum`. CI uses Python 3.14. From the
repository root, run:

```sh
make verify
```

The gate checks the printed listings against their restored copies and runs
both local examples. It compares the derived values against the full review,
checks the audit register and triage map, verifies quotations and cited
pages, and checks the source PDF digests. It uses the committed PDFs and text.
Rerunning it does not require a publication-history refresh or model services.

The default receipts are under `$TMPDIR/reason-verify/`, or
`/tmp/reason-verify/` when `TMPDIR` is unset. To keep each run separate, use
`make verify OUT="$(mktemp -d)"`. The example trace is about 27 MB.

For a source-text lookup, supply one of the committed
[layout extracts](../text/README.md) and a literal quotation:

```sh
python3 -I scripts/locate.py text/engineering-3.5.txt "The example does not implement the Core"
```

The [source archive](../sources/README.md) identifies the editions and digests.
`make text` regenerates the extracts using Poppler's `pdftotext`. The existing
[publication history](../notes/zenodo-history.md) is an archival receipt.
The separate `make zenodo` operation fetches a new history from Zenodo.

## Pinned Template render

Install uv, Python 3.14, Pandoc 3.14, pandoc-crossref v0.3.26b, and XeLaTeX
with the [Template TeX packages](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/README.md#L565-L574).
Set `REASON_CHECKOUT` to the absolute path of your checkout.

```sh
git clone https://github.com/docxology/template.git reason-template-runner
cd reason-template-runner
git checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
uv sync --locked --python 3.14
project=projects/working/reason
mkdir -p projects/working
git -C "$REASON_CHECKOUT" worktree add --detach "$PWD/$project" HEAD
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/reason
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/reason
```

The [manuscript configuration](manuscript/config.yaml) sets PDF and HTML as the
render formats. Inspect `$project/output/pdf/reason_combined.pdf`,
`$project/output/web/index.html`, and `$project/output/reports/` for validation
and provenance. The [full referee report](review.md) remains the source for
the detailed findings.

Check local documentation links from the repository root:

```sh
lychee --offline README.md AGENTS.md 'docs/**/*.md'
git diff --check
```
