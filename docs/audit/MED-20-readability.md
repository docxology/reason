---
id: MED-20
title: Coined vocabulary and length are the main barrier to review
severity: medium
area: editorial
volumes: I, II
sections: Vol I guide, Key Definitions, A.5; Vol II front matter, Appendix A; both volumes throughout
review: §7, §10.9, Appendix A
status: open
github_issue: 28
---

# MED-20 · Coined vocabulary and length are the main barrier to review

## Claims under review

- **Vol II front matter, p. 12:** "Terms are defined by the causal model in Volume I, version
  8.0; technical correspondence is given in Appendix A. Numbering is continuous: Volume I
  contains Chapters 1-20, and the engineering volume continues with Chapters 21-34."
- **Vol II Appendix A, p. 115:** "The fundamental volume defines causal functions and their
  boundaries, while the engineering volume separates those same functions into data structures,
  authorization decisions and execution operations. Correspondence between terms does not mean
  identity: one semantic function may be implemented by a sequence of several technical
  stages."

## Finding

The author reports that earlier reviewers could not reconstruct the architecture. The text
explains that better than the readers do. Two volumes of 105 and 118 pages introduce a large
private vocabulary (Compass, Current Coordinate, Core of Reason, Formation States, RFL,
REASON_CLOSURE, Factor X, structure of ignorance, 72 record types), much of which has a
standard equivalent. Volume I's mapping of its terms to standard ones, a good piece of work, is
its last section (A.5's terminological correspondence map). Volume II's bridge glossary
promises "technical correspondence" with Volume I but covers 3 of Volume I's 33 Key
Definitions; nine of its sixteen terms do not occur in Volume I, and the Core of Reason,
Worldview, Value Map, Compass, RFL and Formation State have no entry. Editorial defects (MIN-01
to MIN-08, MIN-14) compound the difficulty, and continuous chapter numbering means a reader of
Volume II meets references to Volume I sections without context.

## Evidence

- **Already in the text (Vol I A.5, p. 103):** a "TERMINOLOGICAL CORRESPONDENCE MAP" setting
  each coined term against its nearest existing concepts, at the end of the volume.
- **Already in the text (Vol I guide, p. 2):** "This text is an entry point into the two
  volumes."
- **Vol II Appendix A, pp. 115–116:** sixteen glossary entries, of which "consciousness",
  "current coordinate" and "self-navigation" are among Volume I's Key Definitions.
- The near-duplicate paragraphs, truncations and broken numbering catalogued in MIN-01 to
  MIN-04.

## Why it matters

A reader who cannot map a term to something they know cannot evaluate the claim it carries.
Once reconstructed, the architecture is coherent and the testable core modest and clear; the
barrier is presentational, and it is the main reason the work has not been reviewed.

## Ideas & possible recommendations

- **A glossary at the front of each volume.** Each volume could open with a one-page glossary
  that maps every coined term to its nearest standard term and says what differs; A.5's map is
  a good start.
- **Rebuild Volume II's Appendix A.** The appendix could be rebuilt around Volume I's Key
  Definitions, so that the Core of Reason, Worldview, Value Map, Compass, RFL and Formation
  State have entries.
- **A short entry-point paper.** The 10–12 page paper of review §10 could serve as the entry
  point, presenting the testable core without the full vocabulary.
- **An editorial pass.** A careful human editorial pass could address the defects catalogued in
  MIN-01 to MIN-08 and MIN-14.

## Resolved when

- [ ] Each volume opens with a mapping of coined terms to standard ones (for example a
      glossary).
- [ ] A short text (for example a paper) presents the testable core without the full
      vocabulary.

## Related

- Review: [§7](../../REVIEW.md#weakest), [§10](../../REVIEW.md#10-ideas--possible-recommendations),
  [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-04, MED-35, MIN-01, MIN-02, MIN-03, MIN-04, MIN-07, MIN-15
