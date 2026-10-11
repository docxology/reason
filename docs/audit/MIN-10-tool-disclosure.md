---
id: MIN-10
title: No statement of the tools used for drafting, translation and typesetting
severity: minor
area: provenance
volumes: I, II
sections: Vol I A.2, title page; Vol II title page; PDF metadata of both volumes
review: Appendix B
status: open
github_issue: 56
---

# MIN-10 · No statement of the tools used for drafting, translation and typesetting

## Claims under review

- **Vol I A.2, p. 94:** "The project archive preserves repeated studies using Elicit: [...]
  and memory of errors. These are materials of scientific search and AI-assisted analysis that
  can be checked against the cited sources; their status belongs to the author's research
  process and is separate from journal decisions."
- **Vol I A.2, p. 93:** "Comparisons with scientific literature were carried out after the
  author's propositions had been formed."
- **Vol I title page, p. 8:** "Author: Mihail Tkalic"; **Vol II title page, p. 9:** "Author:
  Mihail Tkalic".

## Finding

The volumes are published in English, Russian and (for v7.5) Chinese editions. Volume I
describes the order of its research, with the comparisons with the scientific literature made
after the author's propositions had been formed, and reports that novelty and priority were
assessed with an AI literature tool (Elicit), both as quoted above. Neither volume states which
tools were used to draft, translate or typeset the text, and each title page names the author
alone. The document metadata of both PDFs names the producer as `OpenAI / PyMuPDF`. Many
journals and conferences now require a statement of AI assistance in writing and translation,
and readers use it to calibrate how to read the text.

## Evidence

- **PDF metadata** (`pdfinfo`): `Producer: OpenAI / PyMuPDF` for both
  `Foundations_of_Reason_8.0_EN.pdf` and `Engineering_of_Reason_3.5_EN.pdf`.
- **Vol I A.2, p. 94:** three Elicit reports are listed among the "Historical materials".
- No acknowledgement or methods statement about drafting, translation or typesetting tools
  appears in either volume.

## Why it matters

A disclosure costs one paragraph and pre-empts speculation. It also helps readers interpret
editorial artefacts such as merged duplicate paragraphs (MIN-01) and untranslated
identifiers (MIN-05).

## Ideas & possible recommendations

- **A short tool-use statement in each volume.** It could describe the tools used for
  drafting, translation, literature search and typesetting, and what was checked by hand.
- **One statement in the shared guide.** Both volumes open with the same short guide, so a
  single statement there would reach both.
- **Say how the PDFs were produced.** The statement could also explain why the PDF metadata
  names `OpenAI / PyMuPDF` as the producer.

## Resolved when

- [ ] Each volume carries a tool-use statement.

## Related

- Review: [Appendix B](../../REVIEW.md#appendix-b-what-i-verified-and-how)
- Issues: MED-23, MIN-01
