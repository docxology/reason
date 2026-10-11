# Review of *Foundations of Reason 8.0* and *Engineering of Reason 3.5*

A referee-style scientific review, requested by the author, of Mihail Tkalic's two-volume
work on Artificial Reason:

- Vol I. *Superintelligence Technology (ASI): Foundations of Reason 8.0 — From the Meaning
  of Life to Artificial Reason*. Zenodo, 2026.
  [10.5281/zenodo.23271702](https://doi.org/10.5281/zenodo.23271702)
- Vol II. *Engineering of Reason 3.5: ASI Technology*. Zenodo, 2026.
  [10.5281/zenodo.23271781](https://doi.org/10.5281/zenodo.23271781)

## Verdict

A pre-empirical research programme with an unusually strong evaluation plan, embedded in a
speculative natural philosophy. It is not pseudoscience: it states its own failure
conditions and keeps unfavourable outcomes in its denominators. It is not yet a tested
theory either, because nothing in it is evidence that the architecture works. It deserves
experimental development. The review's ideas for that begin with a preregistered experiment
comparing the Core against a strong agent stack at equal compute, with a stated effect size
and a stated condition under which the Core is abandoned, and a pause in revising the text
until such an experiment has run.

## What is here

| Path | Contents |
|---|---|
| [`REVIEW.md`](REVIEW.md) | The full review: answers to the author's seven questions, a reconstruction of the architecture, the prior-art comparison including active inference, a safety analysis, the scientific status, and ideas and possible recommendations, including a concrete first experiment. Each section opens with the claims it responds to, quoted from the volumes with volume, section and page |
| [`docs/audit/`](docs/audit/README.md) | The issue register: 66 issues (8 major, 38 medium, 20 minor), each mirrored by a GitHub issue with the same ID. Every file opens with the claims under review, quoted with volume, section and page, then gives the finding, evidence, ideas and possible recommendations, and a resolution criterion |
| [`repro/`](repro/README.md) | The two Python listings from Vol II with their indentation restored, and the duplicate-paragraph check |
| [`scripts/`](scripts/) | Quote locator, quotation and page-citation checks, number check, audit-register index and issue filing |
| [`notes/`](notes/) | Reading notes, the Zenodo publication history, and the raw outputs of the independent audit passes |
| [`sources/`](sources/README.md) | The two English PDFs under review (CC BY-NC 4.0, unmodified) with SHA-256 checksums |
| [`text/`](text/README.md) | Text extracted from the PDFs; every quotation, page and line number is taken from it |

## Reproduce the checks

```sh
make verify
```

This checks the restored listings against the printed code, runs them and the
duplicate-paragraph check, and then fails if any number quoted in `REVIEW.md` disagrees
with what the scripts produce; if any quotation in `REVIEW.md`, the register or the raw
audit files is not in the volumes, or a quotation in `REVIEW.md` or the register is not on
the page it cites; if a register file does not open with its quoted claims or offers fewer
than two ideas; if the register's index is stale or a raw finding is not mapped to a
register issue; or if the PDFs do not match their checksums. Outputs go to
`$TMPDIR/reason-verify/`. Python 3.10 or later, standard library only. `make text` regenerates `text/` (needs poppler's `pdftotext`); `make zenodo`
refreshes the publication history (needs network).

To find any quotation in the volumes:

```sh
python3 -I scripts/locate.py text/engineering-3.5.txt "The example does not implement the Core"
# text/engineering-3.5.txt:7506 page 105 §33.B: The example does not implement the Core
```

## How the review was made

Both English PDFs were read in full. The review was then audited in independent passes:
five section-by-section readers covering every page of both volumes (217 raw findings), a
cross-vendor fact-check of 119 of the review's claims, an "author's advocate" pass that
searched the volumes for rebuttals to each criticism, verification of every reference
in the volumes' bibliographies and in the review's own, and a second cross-vendor pass that
re-read every quotation in the issue register against its surrounding text (176 findings,
each checked against the volumes before it was applied). The review and the register were
corrected wherever those passes showed them wrong or unfair. The raw outputs are kept unedited in
`notes/audit-raw/`, with `TRIAGE.md` mapping every raw finding to the register issue that
acknowledges it; quotations, page numbers and computed numbers are re-checked by the
scripts above.

The review was prepared with AI assistance (Anthropic's Claude for reading, drafting and
the audit passes; an OpenAI model for the cross-vendor fact-check).

## Status

Draft review, open for the author's response. The issues stay open until the author responds
or a later version of the volumes addresses them.
