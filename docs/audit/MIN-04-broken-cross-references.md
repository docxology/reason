---
id: MIN-04
title: Cross-references that do not resolve
severity: minor
area: editorial
volumes: I, II
sections: Vol I guide §8, §7.2, A.4, A.5; Vol II Ch. 23, §24.A.1, §27.B, §28.B, §33.A.2, Appendix B
review: Appendix A
status: open
github_issue: 50
---

# MIN-04 · Cross-references that do not resolve

## Claims under review

- **Vol I A.4, p. 100:** "In this way items 2, 20, 23, 26, and 31 are connected.";
  **Vol II §27.B, p. 49:** "It connects tests 2, 20, 23, 26 and 31 from foundational Appendix
  A.4"; **Vol I A.5, p. 104:** "A.4 No. 20, No. 21, No. [...] 33", cited for selection by value
  of information; **Vol I A.5, p. 105:** "A.4 No. 28", cited for current-state integration.
- **Vol I §7.2, p. 37:** "examples of RAG and ReAct are given in Appendix A.5, items 15–16";
  **Vol II §33.A.2, p. 103:** "Use fundamental §11.8 and engineering §§25.B, 28.C and 33.C."
- **Vol II Ch. 23, p. 18:** "The exact-match rule in §32.3 applies to a declared deterministic
  or log-reproducible mode."; **Vol II §24.A.1, p. 21:**
  "SemanticMediator.relation_candidates[] from §24.B.2"; **Vol II §28.B, p. 56:** "Every
  execution separately passes §28".
- **Vol I guide §8, p. 7:** "Where are the interface and diagnostic code?", answered in the
  Volume I column with "Operational Core of the Model".

## Finding

Several of the references quoted above point to targets that do not exist or whose content
does not match the stated purpose. The largest group is the references into the A.4 test list.
Under the printed numbering (A.4 prints as items 19–55, MIN-03) they do not fit: items 2, 20,
23, 26 and 31 are said to make up the first discriminating series, but item 2 is not in A.4 at
all and printed No. 31 is "Conflict of consequences relative to the Compass"; "A.4 No. 28" is
given for current-state integration, but printed No. 28 is "Limited launch". All eighteen such
references in Volume I and the five in Volume II resolve to the tests they describe if the
printed number is reduced by 18 up to printed No. 37 and by 20 from printed No. 40 on. The five
first-series items then become Method correction, Selection of a discriminating test, Gap type
and question, Mentor and criterion error, and Transfer of an inquiry approach, exactly the
three tasks the sentence lists, and "No. 28" becomes Current integration (printed 48). The
pattern suggests the references predate the insertion of printed Nos. 38 and 39.

## Evidence

- **Vol I A.4, pp. 97–98:** the references in the A.5 map land on the wrong tests. Printed
  No. 28 is "Limited launch"; printed Nos. 20, 21 and 33 are "Method correction", "Correction
  of thinking mode" and "Stopping and authorization", not tests of selection by value of
  information.
- **Vol I A.5, p. 102:** the entries for RAG and ReAct are printed as items 70 and 71.
- **Vol II §33.A.2, p. 103:** Chapter 11 of Vol I has sections 11.1–11.4, the last headed "The
  Unknown and Significance" (Vol I §11.4, p. 51); §12.8, "Minimal Relations of the Core" (Vol I
  §12.8, p. 59), the causal obligations, was probably meant.
- **Vol II §32.3, p. 85:** the card is headed "Breakdown of reproducibility" and states no
  exact-match rule.
- **Vol II §24.B.2, p. 23:** `relation_candidates[]` is a field of `SemanticInterpretation`,
  not of the mediator.
- **Vol II §30.A, p. 74:** the section is headed "External Authorization of Significant
  Operations"; the sentence in §28.B refers to its own chapter, and §30.A seems intended.
- **Vol I Operational Core of the Model, p. 14:** the section opens with "A short map of how
  Reason works" and then gives formulas; it contains neither the interface nor the diagnostic
  code.

## Why it matters

The cross-references are how the engineering volume claims to operationalize the foundational
tests. When they do not resolve, a reader cannot tell which tests make up the first series.

## Ideas & possible recommendations

- **Restart the numbering in each list.** MIN-03 describes the change; the references would
  then match the numbers the text uses.
- **Give every test a stable identifier.** Tests could be cited by an identifier that stays
  fixed when a test is inserted, which is the likely cause of the shift (printed Nos. 38 and
  39).
- **Re-derive the references.** The mapping in the Finding (reduce the printed number by 18 up
  to printed No. 37 and by 20 from printed No. 40 on) would give the intended targets of the
  A.4 references. The other broken references would each need the author to confirm the
  intended target.
- **Check references mechanically.** A script that resolves every section and item reference
  in both volumes could run before each release.

## Resolved when

- [ ] Every section and item reference in both volumes resolves to a target whose content
      matches the stated purpose.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-03
