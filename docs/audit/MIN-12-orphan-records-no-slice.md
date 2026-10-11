---
id: MIN-12
title: Many record types are never used, and no minimal component slice is named
severity: minor
area: testability
volumes: I, II
sections: Vol II Chs. 21–33; Vol I A.4 (Priority of the First Series)
review: §5.2(e), §10
status: open
github_issue: 58
---

# MIN-12 · Many record types are never used, and no minimal component slice is named

**Finding.** Volume II defines 72 record types (counted as distinct `Name { ... }` definitions),
several dozen metrics, 57 failure cards and a thirteen-step assembly protocol; with Volume I's
37 proposed tests that is a multi-year programme for a team. The volumes do prioritize the first
series: Volume I has a "Priority of the First Series" section, Volume II §27.B names the tests it
connects, and Chapter 27 gives each stage a short list of admission criteria. What is not named
is the minimal set of components to build for that series. Many records are never used again:
of the 37 record types defined in Chapters 21–26, five (`RevisionTransaction`, `ConceptEntry`,
`CompassMeaningFrame`, `EpistemicArtifact`, `WorldviewLayer`) are not mentioned again by name
anywhere in Volume II, and six more only once, so no metric, rule or test refers to them. One of
the unused five, `EpistemicArtifact`, carries the epistemic-status discipline the review counts
among the strongest parts of the work.

## Evidence

- **Vol II, record definitions:** 72 distinct types, from `GenesisPackage` and `RevisionTransaction`
  (Ch. 21) to `CompetenceMandate` (§30.F) and `ScaleInvariantReport` (§33.D).
- **Vol II Ch. 32, p. 84:** "Sections 32.1-32.2 specify the general format; [...] 32.25-32.27
  specify the general response and recovery"; the other 57 sections are failure cards.
- **Already in the text (Vol I A.4, p. 99):** "For an initial test, a digital environment based on
  the example in §12.9 is sufficient", under the heading "Priority of the First Series".
- **Vol II §24.D, p. 28:** `EpistemicArtifact` is defined ("Any construction capable of passing
  between modules or persisting across cycles carries its own epistemic status") and not named
  again.

## Why it matters

A specification of this size invites partial implementations that differ in what they include,
and makes it hard to attribute a result to a component. The central hypothesis needs a small
subset: the epistemic-status layer, the basis-insufficiency assessment, required-distinction
grouping, sufficiency, and inquiry-method memory.

## Recommendation

Mark the minimal schema slice for the first series (for example `WorldClaim`, `EpistemicArtifact`,
`WorldviewRevisionCandidate`, `GapCandidate`, `BasisInsufficiencyAssessment`, `FoundationGap`,
`QuestionTask`, `CoreSufficiencyAssessment`) and label the other records as optional design
sketches, each tied to the hypothesis it would test.

## Resolved when

- [ ] The volumes name the minimal implementation for the first series and label the rest as
      deferred.

## Related

- Review: [§5.2(e)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§10](../../REVIEW.md#10-recommendations-in-priority-order)
- Issues: MED-11, MED-20, MED-29 (vocabularies)
