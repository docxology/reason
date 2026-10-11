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

Two volumes of 105 and 118 pages introduce a large coined vocabulary (Compass, Current
Coordinate, Core of Reason, Formation States, RFL, REASON_CLOSURE, Factor X, structure of
ignorance, 72 record types), much of which has a standard equivalent. Volume I's terminological
correspondence map, a good piece of work, sets eight of its terms against standard ones; it
stands in A.5, the last section of the volume. Volume II's front matter says "technical
correspondence is given in Appendix A" (p. 12), but the sixteen-entry glossary that opens the
appendix covers 3 of Volume I's 33 Key Definitions (consciousness, current coordinate and
self-navigation), and ten of its sixteen entry phrases do not occur in Volume I. A.1 (Volume
I's operational notation set against engineering structures) and A.2 (AI, AGI, AR and ASI
(ASR)) add some correspondence, but the Value Map, RFL and Formation State do not occur in
Appendix A at all, and the Core of Reason, Worldview and Compass have no entry of their own.
Both volumes already open with a short guide (a worked example, a list of what to test and a
reading map), and Volume II gives a first-reading route (p. 12), but the guide is written in
the coined vocabulary and does not map it to standard terms. Editorial defects (MIN-01 to
MIN-08, MIN-14) compound the difficulty, and continuous chapter numbering means a reader of
Volume II meets references to Volume I sections without context.

## Evidence

- **Already in the text (Vol I A.5, pp. 103–104):** a "TERMINOLOGICAL CORRESPONDENCE MAP"
  setting eight terms of the work (Procedural Memory, Worldview, Core of Reason, Value Map,
  Consciousness, Modeling Environment, Factor X and structural multilevel thinking) against
  their nearest existing concepts, with the essential difference for each. It has no row for
  the Compass, Current Coordinate, RFL or Formation State. The "COMPARATIVE MAP FOR TESTING
  NOVELTY" that follows it sets nearby lines of work, not terms, against what remains a
  separate claim of the model. Two further rows in the same three-column format are
  flattened into running text on p. 105 (MIN-14).
- **Already in the text (Vol I guide, pp. 2–7):** "This text is an entry point into the two
  volumes." The guide, *Foundations of Reason in 15 Minutes*, opens both volumes. It works
  through one example, lists "What to test and where to direct criticism" (section 7, p. 6)
  and gives a reading map (section 8, pp. 6–7).
- **Already in the text (Vol II front matter, p. 12):** a first-reading route: "For a first
  reading: purpose → Chapter 21 → §§22.A and 24.B.2 → Chapters 25, 28, 29 → §31.0 and
  §§31.9-31.12 → §§27.B and 33.A → Chapter 34." The same page says what the correspondence is
  for: the technical objects "are reference implementations of the functions in Volume I and
  permit functionally equivalent replacement".
- **Vol II Appendix A, pp. 115–116:** sixteen glossary entries, of which "consciousness",
  "current coordinate" and "self-navigation" are among Volume I's Key Definitions. The ten
  entry phrases that do not occur in Volume I are: attention and early weight; connection of
  a distinction to a decision or trajectory; Worldview query key; active Worldview fragment;
  temporary working hypothesis; Worldview update; WorldviewRevisionCandidate; COMMIT;
  rechecking an old ground; and propagation of revision.
- **Already in the text (Vol II Appendix A, A.1 and A.2, pp. 116–117):** A.1 is a table
  setting Volume I's operational notation (for example the chain G → D → T → V → C) against
  engineering structures (`FoundationGap`, `NavigationDependency`,
  `ContinuationSet/ImpactAssessment`, Values and Compass). A.2 distinguishes AI, AGI, AR and
  ASI (ASR) and says that "The Current Coordinate, Worldview, Compass, values, and open
  commitments become sources of the next significant process" at REASON_CLOSURE.
- The near-duplicate paragraphs, truncations and broken numbering catalogued in MIN-01 to
  MIN-04.

## Why it matters

A reader who cannot map a term to something they know cannot evaluate the claim it carries.
Once reconstructed, the architecture is coherent and the testable core modest and clear; the
barrier is presentational, and it raises the cost of reviewing the work.

## Ideas & possible recommendations

- **A glossary at the front of each volume.** Each volume could open with a one-page glossary
  that maps every coined term to its nearest standard term and says what differs; A.5's
  eight-row map is a good start.
- **Rebuild Volume II's Appendix A.** The appendix could be rebuilt around Volume I's Key
  Definitions, so that the Core of Reason, Worldview, Value Map, Compass, RFL and Formation
  State have entries.
- **A short entry-point paper.** The 10–12 page paper of review §10 could serve as the entry
  point, presenting the testable core in standard terms rather than in the coined vocabulary.
- **An editorial pass.** A careful human editorial pass could address the defects catalogued in
  MIN-01 to MIN-08 and MIN-14.

## Resolved when

- [ ] Each volume opens with a mapping of coined terms to standard ones (for example a
      glossary).
- [ ] A short text (for example a paper) presents the testable core in standard terms (the
      existing guide uses the coined vocabulary).

## Related

- Review: [§7](../../REVIEW.md#weakest), [§10](../../REVIEW.md#10-ideas--possible-recommendations),
  [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-04, MED-35, MIN-01, MIN-02, MIN-03, MIN-04, MIN-07, MIN-14, MIN-15
