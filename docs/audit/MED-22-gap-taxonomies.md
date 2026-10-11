---
id: MED-22
title: Unreconciled taxonomies of gap type
severity: medium
area: definitions
volumes: I, II
sections: Vol I §12.4, §12.9, §13.5, A.3, A.4 (No. 43 as printed); Vol II §24.D.3, §24.E, §25.A, §26.D, §28.0, §28.C
review: §5.3
status: open
github_issue: 30
---

# MED-22 · Unreconciled taxonomies of gap type

## Claims under review

- **Vol I §12.9, p. 61:** "Testable hypothesis of the model: explicit linking of gap type,
  expected outcomes of a test, and dependent corrections improves transfer of the investigative
  method under comparable resources."; **Vol I A.3, p. 96:** "inquiry management without
  explicit typing of the gap achieves the same transfer and cost: no independent advantage of
  this implementation is established".
- **Vol I §12.4, p. 54:** "Insufficiency can appear in several ways: expectation diverges from
  observation; two grounds yield incompatible conclusions; a decision depends on an unknown
  relation; a claim has unclear provenance; a known rule is applied in a new domain without
  checking its conditions; a recurring error indicates an insufficient method; a new phenomenon
  is noticed but its significance and relations are unknown."; **Vol I §13.5, p. 67:**
  "Superficially different tasks may share the same structure of ignorance: inability to
  intervene safely, uniqueness of an event, conflict among several models, strategic behavior
  of the object, insufficiency of categories, or unreliability of a source. Recognizing such a
  structure permits transfer of a previously successful investigative method, but only together
  with testing its conditions of applicability."; **Vol I A.4, test No. 43, p. 98:** "Variants
  of one situation hide a source, cause, applicability condition, authority, or consequence."
- **Vol II §28.0, pp. 52–53:** "Minimal insufficiency_type values: MISMATCH, CONFLICT,
  MISSING_RELATION, WEAK_PROVENANCE, UNTESTED_SCOPE, UNKNOWN_SIGNIFICANCE, METHOD_GAP,
  SELF_MODEL_GAP, CRITERION_GAP, AUTHORITY_GAP. An implementation may extend the types while
  preserving the causal role of the object." Further on: "gap_type must not be the single
  category UNKNOWN. At different stages, it is useful to distinguish at least: a missing fact;
  an unknown causal relation; conflict among sources; an insufficient self-model; an uncertain
  criterion; a conflict of goals; absence of authority; an insufficient current coordinate; a
  recurring method error; and a gap in the mode of testing itself."
- **Vol II §28.C, p. 58:** step 2 of `form_preliminary_gap`: "classify the insufficiency: FACT
  / CAUSE / MECHANISM / SCOPE / SOURCE / VALUE / PERMISSION / VARIABLE / OBJECT_BOUNDARY /
  MODEL_CLASS".

## Finding

The manipulated variable of the central hypothesis is "explicit typing of the gap" (Vol I
§12.9, A.3), and transfer of inquiry methods is supposed to be indexed by the type of ignorance
(§13.5). Yet the volumes give at least five classifications with different members and no
mapping: seven informal kinds of insufficiency in §12.4; six structures of ignorance in §13.5;
five hidden-variable kinds in test No. 43 of A.4; the ten `insufficiency_type` values of Vol II
§28.0, which an implementation "may extend"; a ten-item prose list of gap types in the same
section; and the ten-way classification step of the §28.C reference heuristic. The two lists in
§28.0 and §28.C sit five pages apart and overlap only partly (`WEAK_PROVENANCE` and SOURCE,
`AUTHORITY_GAP` and PERMISSION). Gap objects outside the main pipeline (SelfModelGap,
VerificationGap, FrameGap, CoverageGapCandidate) have no schema.

## Evidence

- **Vol II §24.E, p. 32:** "SelfModelGap is created with affected claims, references to
  successive coordinates, type and persistence of the discrepancy, candidate causes and
  required evidence"; the other three also appear only in running text (`VerificationGap` in
  §24.D.3, p. 31; `CoverageGapCandidate` in §25.A, p. 34; `FrameGap` in §26.D, p. 43).

## Why it matters

If gap type is the key under which inquiry methods are stored and retrieved, implementations
that follow different sections will index experience differently, and a transfer result will
depend on the taxonomy used. An open vocabulary is also a researcher degree of freedom: types
can be tuned to the test environment. A test of explicit gap typing needs one fixed typing.

## Ideas & possible recommendations

- **One fixed taxonomy before the first series.** The volumes could adopt one taxonomy and fix
  it before the first series, so that explicit typing of the gap is tested with a single
  typing.
- **State its dimensions.** The taxonomy could name its dimensions: what is missing (fact,
  cause, mechanism, variable); why (provenance, scope, authority, criterion); and the structure
  of the situation (intervention possible, event repeatable, object strategic).
- **Map the other lists onto it.** Every other list in both volumes could be mapped onto the
  chosen taxonomy.
- **A typing-only baseline.** One option is a baseline that uses the same inventory of gap
  types without the Core's other components, so that the effect of typing can be read apart
  from the rest of the Core.

## Resolved when

- [ ] One gap taxonomy, fixed before the first series, is used in both volumes, with a mapping
      from the others.

## Related

- Review: [§5.3](../../REVIEW.md#53-my-answer-to-the-guides-question-for-reviewers)
- Issues: MAJ-03, MAJ-04, MED-29 (vocabularies)
