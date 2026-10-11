---
id: MIN-06
title: Bibliography errors and incomplete entries
severity: minor
area: references
volumes: I, II
sections: Vol I A.5; Vol II References
review: Appendix A, Appendix B
status: open
github_issue: 52
---

# MIN-06 · Bibliography errors and incomplete entries

**Finding.** Every reference in both bibliographies was checked against the published record
(29 entries in Vol I A.5, 7 in Vol II). All the works exist and every arXiv ID and DOI
resolves to the printed work, which is to the author's credit. The defects are small: one
duplicate, one transposed pair of initials, one incomplete entry, and several entries that
cite a preprint where a peer-reviewed version now exists.

## Evidence

- **Vol I A.5, items 58 and 82:** Russell and Wefald (1991), "Principles of metareasoning",
  appears twice with the same DOI.
- **Vol I A.5, item 57:** "Littman, L. M." should be "Littman, M. L." (Kaelbling, Littman &
  Cassandra 1998).
- **Vol II [R3]:** Franklin et al. (2014), LIDA, omits volume and pages (*IEEE Transactions on
  Autonomous Mental Development*, 6(1), 19–41).
- **Vol II [R5]:** the six-author list follows arXiv v4 of Reflexion; the NeurIPS 2023 version
  lists five authors.
- **Preprints with published versions:** Vol I items 64 (AGI 2021 proceedings, Springer 2022),
  67 (ICLR 2026), 72 (TMLR 2024) and 73 (ICML 2024); Vol II [R6] (Voyager, TMLR 2024).
- **Vol II §34.A, p. 115:** "Additional strong comparisons are provided by NARS and modern
  metareasoning/metacognition approaches"; neither has a Volume II reference, and Letta, the
  Brier score and value of information are used without a source.

Full verification table: `notes/audit-raw/R1-volume-references.md`.

## Why it matters

Small errors in a bibliography are cheap to fix and make citations harder to follow; citing
the peer-reviewed version strengthens the support.

## Recommendation

Remove the duplicate, correct the initials, complete [R3], and cite the published versions.

## Resolved when

- [ ] The listed entries are corrected in the next version.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-07, MIN-03
