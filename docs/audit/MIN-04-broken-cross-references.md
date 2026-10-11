---
id: MIN-04
title: Cross-references that do not resolve
severity: minor
area: editorial
volumes: I, II
sections: Vol I guide §8, Operational Core, §7.2, A.4, A.5; Vol II Ch. 23, §24.A.1, §24.B.2, §27.B, §28.B, §30.A, §32.3, §33.A.2, §33.C, §33.C.1
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
  Volume I column with "Operational Core of the Model" and in the Volume II column with
  "§§33.C-33.C.1".

## Finding

Several of the references quoted above point to targets that do not exist, whose content does
not match the stated purpose, or whose wording is loose (Chapter 23's "exact-match rule",
§24.A.1's "SemanticMediator.relation_candidates[]"). The largest group is the references into
the A.4 test list. Under the printed numbering (A.4 prints as items 19–55, MIN-03) they do not
fit: items 2, 20, 23, 26 and 31 are said to make up the first discriminating series, but item
2 is not in A.4 at all and printed No. 31 is "Conflict of consequences relative to the
Compass"; "A.4 No. 28" is given for current-state integration, but printed No. 28 is "Limited
launch". All eighteen such references in Volume I and the five in Volume II resolve to the
tests they describe if the printed number is reduced by 18 up to printed No. 37 and by 20 from
printed No. 40 on. The five first-series items then become Method correction, Selection of a
discriminating test, Gap type and question, Mentor and criterion error, and Transfer of an
inquiry approach, exactly the three tasks the sentence lists, and "No. 28" becomes Current
integration (printed 48). The pattern suggests the references predate the insertion of printed
Nos. 38 and 39.

## Evidence

- **Vol I A.4, pp. 97–98:** the references in the A.5 map land on the wrong tests. Printed
  No. 28 is "Limited launch"; printed Nos. 20, 21 and 33 are "Method correction", "Correction
  of thinking mode" and "Stopping and authorization", not tests of selection by value of
  information.
- **Vol I A.5, p. 102:** the entries for RAG and ReAct are printed as items 70 and 71.
- **Vol II §33.A.2, p. 103:** Chapter 11 of Vol I has sections 11.1–11.4, the last headed "The
  Unknown and Significance" (Vol I §11.4, p. 51); §12.8, "Minimal Relations of the Core" (Vol I
  §12.8, p. 59), the causal obligations, was probably meant.
- **Vol II §32.3, p. 85:** the card is headed "Breakdown of reproducibility" and its sign is
  "The same configuration, seed and action sequence lead to different causally significant
  trajectories", which is the failure of a deterministic run. The reference points to the
  right card, but the card never uses the term "exact-match" or says which modes it covers.
- **Vol II §24.B.2, p. 23:** `relation_candidates[]` is a field of `SemanticInterpretation`,
  which `SemanticMediator.interpret` returns. The reference points to the right section; only
  the qualified name `SemanticMediator.relation_candidates[]` is loose.
- **Vol II §30.A, p. 74:** the section is headed "External Authorization of Significant
  Operations"; the sentence in §28.B refers to its own chapter, and §30.A seems intended.
- **Vol I Operational Core of the Model, p. 14:** the section opens with "A short map of how
  Reason works" and then gives formulas; it contains neither the interface nor the diagnostic
  code.
- **Already in the text (Vol II §33.C, p. 107; §33.C.1, p. 109):** the Volume II column of the
  same guide row (p. 7) gives "§§33.C-33.C.1", and those sections are headed "Minimum Interface
  of the Upper AR Loop" and "Executable Diagnostic Cycle". The Volume II entry is the right
  target, so only the Volume I entry is mismatched.

## Why it matters

The cross-references are how the engineering volume claims to operationalize the foundational
tests. When they do not resolve, a reader cannot tell which tests make up the first series.

## Ideas & possible recommendations

- **Restart the numbering in each list.** MIN-03 describes the change. In §12.8 and A.5 the
  references would then match the numbers the text uses. In A.4 they match only up to No. 19
  (two of the eighteen references in Volume I), because the references from No. 20 on skip
  printed Nos. 38 and 39 (restarted Nos. 20 and 21). A plain restart would send "No. 20" to
  "Divergence of the limiting direction" instead of "Selection of a discriminating test", so
  either those two tests are moved to the end of the list or the references are changed by the
  mapping in the Finding.
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
