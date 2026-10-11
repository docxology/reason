---
id: MIN-09
title: Each volume carries different titles in the PDF, on Zenodo and in the author's references
severity: minor
area: provenance
volumes: I, II
sections: Vol I title page and guide; Vol II title page and running head; Zenodo records 23271702 and 23271781
review: Header, §10.5
status: open
github_issue: 55
---

# MIN-09 · Each volume carries different titles in the PDF, on Zenodo and in the author's references

## Claims under review

- **Vol I title page, p. 8:** "FOUNDATIONS OF REASON VOLUME I. THE CAUSAL MODEL OF REASON
  Fundamental Foundations of the Technology of Reason Version 8.0"
- **Vol II title page, p. 9:** "FOUNDATIONS OF REASON — VOLUME II THE ENGINEERING ARCHITECTURE
  OF REASON FROM A CAUSAL MODEL TO AN OPERATING SYSTEM TECHNOLOGY FOR CREATING ARTIFICIAL
  REASON AND SCALING TO ASI (ASR) Version: 3.5"
- **Vol II running head, p. 9:** "ENGINEERING OF REASON · 3.5"; **Vol I guide, p. 2:**
  "Based on Foundations of Reason 8.0 and Engineering of Reason, Volume II, 3.5."
- **Vol I title page, p. 8:** "Date: October 10, 2026"; **Vol II title page, p. 9:**
  "Edition date: October 10, 2026"; **Vol I guide, p. 2:** "Short guide, edition 1.1 ·
  October 10, 2026".

## Finding

The same document appears under several titles, and its dates disagree with the publication
record.

## Evidence

| | Vol I | Vol II |
|---|---|---|
| Zenodo record title | *Superintelligence Technology (ASI): Foundations of Reason 8.0 — From the Meaning of Life to Artificial Reason* | *Engineering of Reason 3.5: ASI Technology* |
| PDF title page | as quoted above (p. 8) | as quoted above (p. 9) |
| Author's request to reviewers | *Foundations of Reason 8.0: From the Meaning of Life to Superintelligence Technology (ASI)* | *Engineering of Reason 3.5: ASI Technology* |

- Both Zenodo records were published on 9 October 2026, a day before the date printed in the
  PDFs and in the shared guide.
- Volume II's title page gives the series title first and the volume title second, while its
  running head and the shared guide call the volume Engineering of Reason (all quoted above).

## Why it matters

A work with several titles is hard to cite and to find, and readers cannot tell whether two
titles refer to the same version.

## Ideas & possible recommendations

- **One title per volume.** The same title could appear on the title page, in the running head
  and the shared guide, in the Zenodo metadata and in citations. MAJ-02 discusses which title
  to choose.
- **One edition date.** The edition date printed in the PDFs and the guide could be aligned
  with the publication record.

## Resolved when

- [ ] Each volume has one title and one date across PDF, Zenodo and the author's citations.

## Related

- Review: [§10](../../REVIEW.md#10-ideas--possible-recommendations)
- Issues: MAJ-02, MED-15
