---
id: MED-03
title: '"Reason" names both a functional profile and a normative orientation'
severity: medium
area: definitions
volumes: I, II
sections: Vol I Key Definitions, Ch. 2, §12.8, §13.1, A.1, A.3; Vol II §31.0
review: §2.4, §3
status: open
---

# MED-03 · "Reason" names both a functional profile and a normative orientation

**Finding.** The word "Reason" denotes a cognitive organization (self-directed inquiry with
persistent correction) and also a normative orientation (a relation to the Compass): a system
with every function but a different ultimate orientation is, by definition, an "intelligent
self-correcting system", not Reason. The bookkeeping already keeps the two apart, which is to
the author's credit: testing separates cognitive capacity, direction and reliability;
`FormationOutcome` has separate fields; REASON_CLOSURE is defined functionally; divergent
candidates stay in the denominators; and the definition is explicitly not used as a defence.
Two problems remain. The word still covers the conjunction in titles, definitions and
claims. And the normative half is hard to test: Chapter 2 splits the "relation" to the Compass
into four capacities (understanding, representing consequences, accepting, following) without
saying which AR status requires, and says internal acceptance cannot be established by any
procedure, so the testable remainder is behavioural conformance, which a system that behaves
well when observed also satisfies.

## Evidence

- **Vol I Ch. 2, p. 22:** a system with strong cognition and a "different closed ultimate
  orientation belongs to the class of intelligent self-correcting systems"; "Status as Reason
  in this model additionally requires that the highest level of navigation be related to the
  Compass."
- **Vol I Ch. 2, p. 23:** "Internal acceptance of the Compass cannot be guaranteed by a
  procedure."
- **Already in the text (Vol I §13.1, p. 62):** "Testing distinguishes cognitive capacity,
  direction, and reliability."
- **Already in the text (Vol II §31.0, p. 79):** "REASON_CLOSURE denotes a change in the source of
  the further trajectory"; `SELF_NAVIGATING_OTHER_ORIENTATION` "is not removed from metric
  denominators and is not turned into success merely by applying the definition 'this is not
  AR'".

## Why it matters

When one word carries both a capability and a value commitment, results about the capability
are read as claims about the values, and objections to the values are read as objections to
the capability. An untestable normative clause in the definition of the target system also
weakens the claim that AR status is empirically assessed.

## Recommendation

Use two terms: one for the functional profile (for example "reasoning organization" or
"self-directed inquiry") and one for the normatively anchored case (for example
"Compass-aligned AR"). Define "related to the Compass" behaviourally, as choice that follows
the Compass in preregistered conflicts with local advantage, including unobserved episodes,
and say which `compass_relation` values are compatible with admission.

## Resolved when

- [ ] Distinct terms are used for the functional organization and its normative orientation.
- [ ] The Compass relation required for AR status has a behavioural test.

## Related

- Review: [§2.4](../../REVIEW.md#24-reason-currently-means-two-different-things)
- Issues: MED-02, MED-05, MAJ-06 (observed versus unobserved behaviour)
