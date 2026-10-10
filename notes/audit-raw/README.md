# Raw outputs of the audit passes

These files are the unedited outputs of the independent passes that audited the volumes and
this review. They are kept for provenance. They are raw: severities are the pass's proposal,
some findings overlap, and a few were judged against the text and narrowed or merged. The
curated result is the register in [`docs/audit/`](../../docs/audit/README.md), and
[`TRIAGE.md`](TRIAGE.md) maps every raw finding to the register issue that acknowledges it.

| File | Pass | Scope |
|---|---|---|
| `V1A.md` | Section reader | Vol I front matter, guide, Key Definitions, Operational Core, Chapters 1–10 (46 findings) |
| `V1B.md` | Section reader | Vol I Chapters 11–20, Conclusion, Open Research Directions, Appendix A (37 findings) |
| `V2A.md` | Section reader | Vol II front matter and Chapters 21–26 (43 findings) |
| `V2B.md` | Section reader | Vol II Chapters 27–30 (46 findings) |
| `V2C.md` | Section reader | Vol II Chapters 31–34, References, Appendices A–B (45 findings) |
| `F1-forge-factcheck.json` | Cross-vendor fact-check | 119 checkable claims in an earlier draft of `REVIEW.md` (94 confirmed, 21 imprecise, 2 wrong, 2 unverifiable); all corrections were applied |
| `A1-advocate.md` | Author's advocate | Each criticism in the earlier draft tested against the volumes for rebuttals and omissions |
| `R1-volume-references.md` | Reference check | Every entry in both volumes' bibliographies |
| `R2a-review-references.md`, `R2b-review-references.md` | Reference check | Every entry in the review's own reference list, and works it named without listing |

Line numbers in the reader files refer to `text/*.txt`; page numbers are PDF pages. All 817
quoted fragments in the five reader files match the texts verbatim, which `make verify`
re-checks with `scripts/check_raw_quotes.py`. Line references to `REVIEW.md` in `F1` and `A1`
refer to the earlier draft they audited.
