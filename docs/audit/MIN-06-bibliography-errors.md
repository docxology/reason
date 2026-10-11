---
id: MIN-06
title: Bibliography errors and incomplete entries
severity: minor
area: references
volumes: I, II
sections: Vol I A.5; Vol II §34.A, References
review: Appendix A, Appendix B
status: open
github_issue: 52
---

# MIN-06 · Bibliography errors and incomplete entries

## Claims under review

- **Vol I A.5, p. 100:** "57. Kaelbling, L. P., Littman, L. M., Cassandra, A. R. (1998)." and
  "58. Russell, S., Wefald, E. (1991). Principles of metareasoning."; **Vol I A.5, p. 103:**
  "82. Russell, S. J., Wefald, E. H. (1991). Principles of Metareasoning. Artificial
  Intelligence, 49(1-3), 361-395."
- **Vol II [R3], p. 115:** "Franklin, S., Madl, T., D’Mello, S., Snaider, J. (2014). LIDA: A
  Systems-level Architecture for Cognition, Emotion, and Learning. IEEE Transactions on
  Autonomous Mental Development. DOI: 10.1109/TAMD.2013.2277589."; **Vol II [R5], p. 115:**
  "Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., Yao, S. (2023). Reflexion:
  Language Agents with Verbal Reinforcement Learning. arXiv:2303.11366."
- **Vol II §34.A, p. 115:** "Additional strong comparisons are provided by NARS and modern
  metareasoning/metacognition approaches."
- **Vol I A.5, p. 101:** "64. Hahm, C., Xu, B., Wang, P. (2021). Goal Generation and
  Management in NARS." and "67. Zhang, J. et al. (2025). Darwin Gödel Machine: Open-Ended
  Evolution of Self-Improving Agents."; **Vol I A.5, p. 102:** "72. Sumers, T. R., Yao, S.,
  Narasimhan, K., Griffiths, T. L. (2023). Cognitive Architectures for Language Agents
  (CoALA)." and "73. Morris, M. R. et al. (2023). Levels of AGI for Operationalizing Progress
  on the Path to AGI."; **Vol II [R6], p. 115:** "Wang, G., Xie, Y., Jiang, Y., Mandlekar, A.,
  Xiao, C., Zhu, Y., Fan, L., Anandkumar, A. (2023). Voyager: An Open-Ended Embodied Agent with
  Large Language Models. arXiv:2305.16291."

## Finding

Every reference in both bibliographies was checked against the published record (29 entries in
Vol I A.5, 7 in Vol II). All the works exist and every arXiv ID and DOI resolves to the printed
work, which is to the author's credit. The defects are small: one duplicate, one transposed
pair of initials, one incomplete entry, and several entries that cite a preprint where a
peer-reviewed version now exists.

## Evidence

- **Vol I A.5, pp. 100, 103:** items 58 and 82, Russell and Wefald (1991), *Principles of
  Metareasoning*, are the same work, and both entries end with the same DOI link,
  "https://doi.org/10.1016/0004-3702(91)90015-C".
- **Vol I A.5, item 57 (p. 100):** the second author's initials are transposed; the entry
  should read Littman, M. L. (Kaelbling, Littman & Cassandra 1998).
- **Vol II [R3] (p. 115):** Franklin et al. (2014), LIDA, omits volume and pages (*IEEE
  Transactions on Autonomous Mental Development*, 6(1), 19–41).
- **Vol II [R5] (p. 115):** the six-author list follows arXiv v4 of Reflexion; the NeurIPS 2023
  version lists five authors.
- **Preprints with published versions:** Vol I items 64 (AGI 2021 proceedings, Springer 2022),
  67 (ICLR 2026), 72 (TMLR 2024) and 73 (ICML 2024); Vol II [R6] (Voyager, TMLR 2024).
- **Vol II §34.A (p. 115):** neither NARS nor modern metareasoning approaches has a Volume II
  reference, and the Brier score and value of information are used without a source. (Letta
  is covered: [R7] notes that MemGPT was renamed Letta.)

Full verification table: `notes/audit-raw/R1-volume-references.md`.

## Why it matters

Small errors in a bibliography are cheap to fix and make citations harder to follow; citing
the peer-reviewed version strengthens the support.

## Ideas & possible recommendations

- **Fix the wrong and incomplete entries.** The duplicate (items 58 and 82) could be removed,
  the initials in item 57 corrected, and [R3] completed with volume and pages.
- **Cite the published versions.** Where a peer-reviewed version now exists (items 64, 67, 72
  and 73 in Vol I; [R6] in Vol II), the entry could cite it instead of the preprint. For [R5]
  this would also settle the author list, since the NeurIPS 2023 version lists five authors.
- **Add the missing sources in Vol II.** Vol II could cite works that Vol I A.5 already lists:
  NARS goal management (item 64) and metareasoning (item 82) for the §34.A comparison, and
  value of information (item 79). The Brier score could get a reference of its own.

## Resolved when

- [ ] The listed entries are corrected in the next version.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-07, MIN-03
