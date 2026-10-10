---
id: MIN-09
title: Each volume carries different titles in the PDF, on Zenodo and in the author's references
severity: minor
area: provenance
volumes: I, II
sections: Vol I title page and guide; Vol II title page; Zenodo records 23271702 and 23271781
review: Header, §10.5
status: open
---

# MIN-09 · Each volume carries different titles in the PDF, on Zenodo and in the author's references

**Finding.** The same document appears under several titles, and its dates disagree with the
publication record.

## Evidence

| | Vol I | Vol II |
|---|---|---|
| Zenodo record title | *Superintelligence Technology (ASI): Foundations of Reason 8.0 — From the Meaning of Life to Artificial Reason* | *Engineering of Reason 3.5: ASI Technology* |
| PDF title page | *Foundations of Reason. Volume I. The Causal Model of Reason. Fundamental Foundations of the Technology of Reason. Version 8.0* (p. 8) | *Foundations of Reason — Volume II. The Engineering Architecture of Reason. From a Causal Model to an Operating System. Technology for Creating Artificial Reason and Scaling to ASI (ASR). Version 3.5* (p. 8) |
| Author's request to reviewers | *Foundations of Reason 8.0: From the Meaning of Life to Superintelligence Technology (ASI)* | *Engineering of Reason 3.5: ASI Technology* |

- Both PDFs and the shared guide are dated "October 10, 2026"; both Zenodo records were
  published on 9 October 2026.
- Volume II's running head reads "ENGINEERING OF REASON · 3.5" while its title page reads "The
  Engineering Architecture of Reason"; the shared guide is "Short guide, edition 1.1 · October
  10, 2026".

## Why it matters

A work with several titles is hard to cite and to find, and readers cannot tell whether two
titles refer to the same version.

## Recommendation

Use one title per volume, identical on the title page, in the Zenodo metadata and in
citations, and align the edition date with the publication record. See MAJ-02 for which
title to choose.

## Resolved when

- [ ] Each volume has one title and one date across PDF, Zenodo and the author's citations.

## Related

- Review: [§10](../../REVIEW.md#10-recommendations-in-priority-order)
- Issues: MAJ-02, MED-15
