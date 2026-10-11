---
id: MIN-10
title: No statement of the tools used for drafting, translation and typesetting
severity: minor
area: provenance
volumes: I, II
sections: Vol I A.2; PDF metadata of both volumes
review: Appendix B
status: open
github_issue: 56
---

# MIN-10 · No statement of the tools used for drafting, translation and typesetting

**Finding.** The volumes are published in English, Russian and (for v7.5) Chinese editions,
and Volume I reports that novelty and priority were assessed with an AI literature tool
(Elicit). Neither volume states which tools were used to draft, translate or typeset the
text. The document metadata of both PDFs names the producer as "OpenAI / PyMuPDF". Many
journals and conferences now require a statement of AI assistance in writing and
translation, and readers use it to calibrate how to read the text.

## Evidence

- **PDF metadata** (`pdfinfo`): `Producer: OpenAI / PyMuPDF` for both
  `Foundations_of_Reason_8.0_EN.pdf` and `Engineering_of_Reason_3.5_EN.pdf`.
- **Vol I A.2, p. 94:** three Elicit reports listed among the "historical materials".
- No acknowledgement or methods statement about drafting, translation or typesetting tools
  appears in either volume.

## Why it matters

A disclosure costs one paragraph and pre-empts speculation. It also helps readers interpret
editorial artefacts such as merged duplicate paragraphs (MIN-01) and untranslated
identifiers (MIN-05).

## Recommendation

Add a short statement to each volume describing the tools used for drafting, translation,
literature search and typesetting, and what was checked by hand.

## Resolved when

- [ ] Each volume carries a tool-use statement.

## Related

- Review: [Appendix B](../../REVIEW.md#appendix-b-what-i-verified-and-how)
- Issues: MED-23, MIN-01
