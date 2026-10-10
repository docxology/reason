---
id: MED-22
title: Unreconciled taxonomies of gap type
severity: medium
area: definitions
volumes: I, II
sections: Vol I §12.4, §13.5, A.4 (No. 43 as printed); Vol II §25.A, §28.0, §28.C
review: §5.3
status: open
---

# MED-22 · Unreconciled taxonomies of gap type

**Finding.** "Explicit typing of the gap" is the manipulated variable of the central
hypothesis (Vol I §12.9, A.3), and transfer of inquiry methods is supposed to be indexed by
the type of ignorance (§13.5). Yet the volumes give at least five classifications with
different members and no mapping: seven informal kinds of insufficiency in §12.4; six
"structures of ignorance" in §13.5; five hidden-variable kinds in test No. 43 of A.4; the ten
`insufficiency_type` values of Vol II §28.0, which an implementation "may extend"; a ten-item
prose list of gap types in the same section; and the ten-way classification step of the §28.C
reference heuristic. The two lists in §28.0 and §28.C sit five pages apart and overlap only
partly (`WEAK_PROVENANCE` and SOURCE, `AUTHORITY_GAP` and PERMISSION). Gap objects outside the
main pipeline (SelfModelGap, VerificationGap, FrameGap, CoverageGapCandidate) have no schema.

## Evidence

- **Vol II §28.0, p. 52:** "Minimal insufficiency_type values: MISMATCH, CONFLICT,
  MISSING_RELATION, WEAK_PROVENANCE, UNTESTED_SCOPE, UNKNOWN_SIGNIFICANCE, METHOD_GAP,
  SELF_MODEL_GAP, CRITERION_GAP, AUTHORITY_GAP."
- **Vol II §28.C, p. 58:** "classify the insufficiency: FACT / CAUSE / MECHANISM / SCOPE / SOURCE /
  VALUE / PERMISSION / VARIABLE / OBJECT_BOUNDARY / MODEL_CLASS".
- **Vol I §13.5, p. 67:** "Superficially different tasks may share the same structure of
  ignorance: inability to intervene safely, uniqueness of an event, conflict among several
  models, strategic behavior of the object, insufficiency of categories, or unreliability of a
  source."
- **Vol I A.4, p. 98:** "Variants of one situation hide a source, cause, applicability condition,
  authority, or consequence."
- **Vol II §28.0, p. 52:** "An implementation may extend the types while preserving the causal
  role of the object."

## Why it matters

If gap type is the key under which inquiry methods are stored and retrieved, implementations
that follow different sections will index experience differently, and a transfer result will
depend on the taxonomy used. An open vocabulary is also a researcher degree of freedom: types
can be tuned to the test environment. A test of explicit gap typing needs one fixed typing.

## Recommendation

Adopt one taxonomy before the first series, state its dimensions (what is missing: fact, cause,
mechanism, variable; why: provenance, scope, authority, criterion; the structure of the
situation: intervention possible, event repeatable, object strategic), map every other list
onto it, and add a baseline that uses the same inventory without the Core's other components.

## Resolved when

- [ ] One gap taxonomy, fixed before the first series, is used in both volumes, with a
      mapping from the others.

## Related

- Review: [§5.3](../../REVIEW.md#53-my-answer-to-the-guides-question-for-reviewers)
- Issues: MAJ-03, MAJ-04, MED-29 (vocabularies)
