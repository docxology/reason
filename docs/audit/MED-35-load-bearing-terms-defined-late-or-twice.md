---
id: MED-35
title: Load-bearing terms are defined late, inconsistently or not at all
severity: medium
area: definitions
volumes: I
sections: Vol I Key Definitions, guide §1, §6, §12.4, Ch. 6, Ch. 14, Ch. 15, §20.1.1
review: §2.1, Appendix A
status: open
---

# MED-35 · Load-bearing terms are defined late, inconsistently or not at all

**Finding.** The Key Definitions of Vol I are mostly used steadily, but a few terms that the
argument leans on are missing from them or drift within them. "Ground", "gap", "required
distinction", "sufficiency", "carrier", REASON_CLOSURE, the Incubator and external admission
have no entry, and the last two appear before they are introduced; "trajectory", "death" and
"ethics" are each defined in more than one way.

## Evidence

- **Vol I guide §1, p. 2; §12.4, p. 54:** "A ground here means what a conclusion or action
  actually relies on." Section 12.4 widens it to any "observation, claim, causal relation"
  and more, and ties questions to a "significant insufficiency of a ground" with no stated
  threshold.
- **Vol I Key Definitions, p. 11; Ch. 6, p. 35:** "Trajectory - a sequence of causally
  connected states actually realized by a process among available continuations", yet "Choice
  is the temporary preference of one of the available trajectories".
- **Vol I guide §6, p. 6; Vol II §31.0, p. 78:** "REASON_CLOSURE is the name of a testable
  state". Vol II: "AR emerges at REASON_CLOSURE". The Key Definitions (p. 12) define only
  "Causal closure".
- **Vol I §14.1, p. 70; Ch. 14 box, p. 71:** "Death is the loss by a living system of the
  capacity to preserve its own causal continuity as a whole"; the box has "the irreversible
  loss of the capacity of that carrier to maintain its own causal continuity".
- **Vol I §20.1.1, p. 85; Ch. 15, p. 74:** "External protection by the Incubator remains
  separate" and "engineering constraints of external admission" are used before §20.2 and §20.3
  introduce them; neither is a Key Definition.
- **Vol I Key Definitions, p. 13; Ch. 15, p. 74:** ethics is "a system of rules for evaluating
  permissible and required choices" in one place and "a layer of compressed evaluations and
  rules of choice" in another.

## Why it matters

These terms carry tests: the Core fires on a "significant" insufficiency, REASON_CLOSURE
defines AR, and the death definition decides whether a pause or rollback destroys a candidate.

## Recommendation

Add Key Definitions entries for ground, gap, required distinction, sufficiency, carrier,
REASON_CLOSURE, Incubator and external admission, with a criterion for "significant" that
separates an insufficient ground from an uncertain one. Keep one definition each of
trajectory, death (with a reversibility clause) and ethics.

## Resolved when

- [ ] The Key Definitions define the terms above once each.
- [ ] Chapter boxes quote the Key Definitions, and death has a reversibility clause.

## Related

- Review: [§2.1](../../REVIEW.md#21-the-functional-cycle-holds-together),
  [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-03, MED-18, MIN-15
