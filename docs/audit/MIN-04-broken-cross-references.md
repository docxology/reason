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

**Finding.** Several references point to targets that do not exist or whose content does not
match the stated purpose. The largest group is the references into the A.4 test list. Under the
printed numbering (A.4 prints as items 19–55, MIN-03) they do not fit: "items 2, 20, 23, 26 and
31" are said to make up the first discriminating series, but item 2 is not in A.4 at all and
printed No. 31 is "Conflict of consequences relative to the Compass"; "A.4 No. 28" is given for
current-state integration, but printed No. 28 is "Limited launch". All eighteen such references
in Volume I and the five in Volume II resolve to the tests they describe if the printed number
is reduced by 18 up to printed No. 37 and by 20 from printed No. 40 on. The five first-series
items then become Method correction, Selection of a discriminating test, Gap type and question,
Mentor and criterion error, and Transfer of an inquiry approach, exactly the three tasks the
sentence lists, and "No. 28" becomes Current integration (printed 48). The pattern suggests the
references predate the insertion of printed Nos. 38 and 39.

## Evidence

- **Vol I A.4, p. 100:** "In this way items 2, 20, 23, 26, and 31 are connected."; **Vol II §27.B,
  p. 49:** "It connects tests 2, 20, 23, 26 and 31 from foundational Appendix A.4".
- **Vol I A.5, p. 105:** "A.4 No. 28" for current-state integration; the comparative map on p. 104
  also cites "A.4 No. 20, No. 21, No. [...] 33" (printed: Method correction, Correction of thinking
  mode, Stopping and authorization) for selection by value of information.
- **Vol I §7.2, p. 37:** "examples of RAG and ReAct are given in Appendix A.5, items 15–16"; they
  are printed as items 70 and 71.
- **Vol II §33.A.2, p. 103:** "Use fundamental §11.8 and engineering §§25.B, 28.C and 33.C." Chapter
  11 has sections 11.1–11.4; §12.8, the causal obligations, was probably meant.
- **Vol II Ch. 23, p. 18:** "The exact-match rule in §32.3 applies to a declared deterministic or
  log-reproducible mode"; §32.3 states no exact-match rule.
- **Vol II §24.A.1, p. 21:** "SemanticMediator.relation_candidates[]" is a field of
  `SemanticInterpretation`, not of the mediator; **§28.B:** "Every execution separately passes
  §28" refers to its own chapter (§30.A seems intended); **Vol I guide §8, p. 7:** the location
  given for "the interface and diagnostic code" is the Operational Core, which contains
  neither.

## Why it matters

The cross-references are how the engineering volume claims to operationalize the foundational
tests. When they do not resolve, a reader cannot tell which tests make up the first series.

## Recommendation

Restart numbering in each list (MIN-03), give every test a stable identifier, re-derive the
references with the mapping above, and check all references mechanically before release.

## Resolved when

- [ ] Every section and item reference in both volumes resolves to a target whose content
      matches the stated purpose.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-03
