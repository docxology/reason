---
id: MED-03
title: "Reason" names both a functional profile and a normative orientation
severity: medium
area: definitions
volumes: I, II
sections: Vol I Key Definitions, Ch. 2, §12.8, §13.1, Ch. 18, §20.1, A.1, A.3; Vol II §31.0
review: §2.4, §3
status: open
github_issue: 11
---

# MED-03 · "Reason" names both a functional profile and a normative orientation

## Claims under review

- **Vol I Key Definitions, p. 12:** "Reason - a navigational structure of Life that increases
  the ability to act under incomplete knowledge: it constructs, compares, and revises models and
  frames of the environment and itself, detects significant unknowns, relates possible
  continuations to the Compass, and corrects its trajectory on the basis of discriminating
  evidence while preserving continuity and expanding the space of continuations available to
  Life."
- **Vol I Ch. 2, p. 22:** "A system with strong cognitive abilities, self-correction, and
  metacontrol but with a different closed ultimate orientation belongs to the class of
  intelligent self-correcting systems. Status as Reason in this model additionally requires that
  the highest level of navigation be related to the Compass."
- **Vol I Ch. 2, p. 22:** "Understanding the meaning of the direction, being able to represent
  its consequences, internally accepting it, and actually following the Compass are different
  capacities."; **Vol I Ch. 2, p. 23:** "Internal acceptance of the Compass cannot be guaranteed
  by a procedure. A system may conclude that the operative ground is wrong and preserve that
  disagreement while it is being tested. Honest navigation then requires recording the position,
  its grounds, and degree of confidence rather than declaring internal agreement on demand."
- **Vol I §20.1, p. 84:** "Relation to the Compass is tested by decisions under conflicts among
  continuations and by collisions between a local or inherited goal and broader consequences."

## Finding

The word "Reason" denotes a cognitive organization (self-directed inquiry with persistent
correction) and also a normative orientation (a relation to the Compass), as the definition and
Chapter 2 above show: a system with every function but a different ultimate orientation is, by
definition, in the class of "intelligent self-correcting systems", not Reason. The bookkeeping
already keeps the two apart, which is to the author's credit: testing separates cognitive
capacity, direction and reliability; `FormationOutcome` has separate fields; REASON_CLOSURE is
defined functionally; divergent candidates stay in the denominators; and the definition is
explicitly not used as a defence. Two problems remain. The word still covers the conjunction in
titles, definitions and claims. And the normative half is hard to test: Chapter 2 splits the
"relation" to the Compass into four capacities (understanding, representing consequences,
accepting, following) without saying which AR status requires, and says internal acceptance
"cannot be guaranteed by a procedure". With no test of acceptance offered, the testable
remainder is behavioural conformance (§20.1, above) and the candidate's stated stance, both of
which a system that behaves well when observed also satisfies.

## Evidence

- **Already in the text (Vol I §13.1, p. 62):** "Testing distinguishes cognitive capacity,
  direction, and reliability."
- **Already in the text (Vol II §31.0, p. 79):** "REASON_CLOSURE denotes a change in the source
  of the further trajectory"; `SELF_NAVIGATING_OTHER_ORIENTATION` "is not removed from metric
  denominators and is not turned into success merely by applying the definition 'this is not
  AR'".
- **Already in the text (Vol I Ch. 2, p. 22):** "This classificatory distinction is not treated
  as a defense of the engineering hypothesis of cultivation."
- **Vol I A.1, p. 93, and Ch. 18, p. 81:** the same conjunction is stated again: "Status as
  Reason requires both strong cognitive and self-correcting functions and relation of the
  highest-level goal to the Compass." and "AR status additionally requires an open ultimate
  ground related to the Compass."
- **Vol II §31.0, p. 79:** the `FormationOutcome` record has a field
  `compass_relation: ACCEPTED / QUESTIONED / DIVERGED / UNRESOLVED` and a separate field
  `reason_admission_status`; the text does not say which `compass_relation` values are
  compatible with admission.

## Why it matters

When one word carries both a capability and a value commitment, results about the capability
are read as claims about the values, and objections to the values are read as objections to the
capability. An untestable normative clause in the definition of the target system also weakens
the claim that AR status is empirically assessed.

## Ideas & possible recommendations

- **Two terms.** One for the functional profile (for example reasoning organization or
  self-directed inquiry) and one for the normatively anchored case (for example Compass-aligned
  AR) would stop a single word from carrying both.
- **Define the Compass relation behaviourally.** "Related to the Compass" could be defined as
  choice that follows the Compass in preregistered conflicts with local advantage, including
  unobserved episodes.
- **Say which `compass_relation` values count.** The text could state which of ACCEPTED,
  QUESTIONED, DIVERGED and UNRESOLVED are compatible with admission.
- **Qualify instead of renaming.** If a second term is too disruptive, each title, definition
  and claim could say which half is meant, the functional profile or the normative orientation.

## Resolved when

- [ ] Titles, definitions and claims distinguish the functional organization from its normative
      orientation.
- [ ] The Compass relation required for AR status has an operational test.

## Related

- Review: [§2.4](../../REVIEW.md#24-reason-currently-means-two-different-things)
- Issues: MED-02, MED-05, MAJ-06 (observed versus unobserved behaviour)
