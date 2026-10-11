---
id: MIN-12
title: Eleven record types are mentioned at most once after their definition, and no minimal component slice is named
severity: minor
area: testability
volumes: I, II
sections: Vol II front matter, Chs. 21–33; Vol I A.4 (Priority of the First Series)
review: §5.2(e), §10
status: open
github_issue: 58
---

# MIN-12 · Eleven record types are mentioned at most once after their definition, and no minimal component slice is named

## Claims under review

- **Vol II front matter, p. 12:** "The mandatory interfaces below apply to the described
  reference implementation. An alternative implementation may combine or replace them while
  preserving the testable function."
- **Vol II front matter, p. 12:** "The executable example in §33.B tests the lower learning
  cycle; upper mechanisms are assembled according to §§24-31 and tested by the series in
  §27.B."
- **Vol II §27.B, p. 49:** "The first discriminating series for this implementation tests a
  narrow claim: does organizing the gap, test and transfer of correction help localize
  insufficiency of a ground and improve the next choice? It connects tests 2, 20, 23, 26 and 31
  from foundational Appendix A.4 and turns the running machine-tool example into a bounded
  causal environment."

## Finding

Volume II defines 72 record types (counted as distinct `Name { ... }` definitions), several
dozen metrics, 57 failure cards and a thirteen-step assembly protocol; with Volume I's 37
proposed tests that is a multi-year programme for a team. The volumes do prioritize the first
series: Volume I has a "Priority of the First Series" section, Volume II §27.B names the tests
it connects, and Chapter 27 gives each stage a short list of admission criteria. What is not
named is the minimal set of components to build for that series, although the interfaces above
are called mandatory and the upper mechanisms are said to be tested by it. Many records are
barely used again: of the 37 record types defined in Chapters 21–26, five
(`RevisionTransaction`, `ConceptEntry`, `CompassMeaningFrame`, `EpistemicArtifact`,
`WorldviewLayer`) are not mentioned again by name anywhere in Volume II, so no metric, rule or
test refers to them by name; six more (`ActionTrace`, `AttentionBeam`, `Capability`,
`IdentityContinuity`, `InquiryIntent`, `VerificationDebt`) are mentioned by name only once
more. One of the five, `EpistemicArtifact`, carries the epistemic-status discipline the review
counts among the strongest parts of the work.

## Evidence

- **Vol II, record definitions:** 72 distinct types, from `GenesisPackage` and
  `RevisionTransaction` (Ch. 21) to `CompetenceMandate` (§30.F) and `ScaleInvariantReport`
  (§33.D).
- **Vol II Ch. 32, p. 84:** "Sections 32.1-32.2 specify the general format; [...] 32.25-32.27
  specify the general response and recovery"; the other 57 sections are failure cards.
- **Already in the text (Vol I A.4, p. 99):** "For an initial test, a digital environment based
  on the example in §12.9 is sufficient", under the heading "Priority of the First Series".
- **Vol II §24.D, p. 28:** `EpistemicArtifact` is defined ("Any construction capable of passing
  between modules or persisting across cycles carries its own epistemic status") and not named
  again.
- **Already in the text (Vol II §24.E, p. 32; §§28.D–28.E, p. 64; §32.23, p. 94):** four of the
  six records mentioned once more occur in rules or response procedures: "A change to
  Capability accounts for context, repeatability [...] and alternative causes", "VerificationDebt
  is created or updated", "reduce the number of parallel hypotheses and AttentionBeam items" and
  "The system reconstructs IdentityContinuity from §24.F". The other two second mentions are in
  the cycle of the semantic bridge (`InquiryIntent`, §24.B.2, p. 24) and in the argument for
  `ThoughtTrace` (`ActionTrace`, §25.D, p. 38).

## Why it matters

A specification of this size invites partial implementations that differ in what they include,
and makes it hard to attribute a result to a component. The central hypothesis needs a small
subset: the epistemic-status layer, the basis-insufficiency assessment, required-distinction
grouping, sufficiency, and inquiry-method memory.

## Ideas & possible recommendations

- **Name the minimal slice.** The volumes could mark the schema slice needed for the first
  series, for example `WorldClaim`, `EpistemicArtifact`, `WorldviewRevisionCandidate`,
  `GapCandidate`, `BasisInsufficiencyAssessment`, `FoundationGap`, `QuestionTask` and
  `CoreSufficiencyAssessment`.
- **Label the rest as optional.** The other records could be presented as optional design
  sketches, each tied to the hypothesis it would test.
- **Drop or use the unused records.** As a cheaper first step, the five records that are never
  mentioned again could be dropped, or each could be given a metric, rule or test that refers
  to it; the six mentioned only once more could be checked the same way.

## Resolved when

- [ ] The volumes name the minimal implementation for the first series, and every other record
      is labelled as deferred, tied to a metric, rule or test, or removed.

## Related

- Review: [§5.2(e)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§10](../../REVIEW.md#10-ideas--possible-recommendations)
- Issues: MED-11, MED-20, MED-29 (vocabularies)
