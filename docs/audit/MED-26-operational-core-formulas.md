---
id: MED-26
title: The Operational Core formulas are incomplete and inconsistent with Vol II
severity: medium
area: formal
volumes: I, II
sections: Vol I Operational Core §1–§5; Vol II §28.D, App. A.1
review: §2.1, §5.2(f)
status: open
---

# MED-26 · The Operational Core formulas are incomplete and inconsistent with Vol II

**Finding.** The Operational Core is offered as "a minimal language for engineering
comparison". As written it is incomplete: ΔL is undefined and VOI is conditioned on a plan;
the cycle has no term for the required distinction or the sufficiency verdict; and the
transfer, regression and carrier-removal quantities leave their controls open. Vol II §28.D
gives a working form, but it differs from Vol I (one cost term instead of four, a budgeted
recursion instead of a stop-while-positive rule), and Appendix A.1 maps both onto one
counterpart.

## Evidence

- **Vol I Operational Core §3, p. 15:** "VOI(p) = E[ΔL | p],"; "Inquiry continues while there
  exists an admissible test with NetVOI(p) > 0". VOI is defined for a plan, the rule for a
  test.
- **Vol I Operational Core §1, p. 14:** "(X_t, W_t, F_t, M_t) → G_t → H_t → p_t → E_t →
  (W'_t, F'_t, M'_t) → A_t → X_{t+1}." No term stands for the required distinction or the
  sufficiency verdict, and the primed variables are undefined.
- **Vol I Operational Core §4 and §5, p. 15:** carrier removal "restores the behavioral or
  outcome difference associated with it" (ambiguous); "TG_(A→B) = Y_(B | learned A) −
  Y_(B | matched control)," and "RG = Y_(old,before) − Y_(old,after)." leave "matched
  control" and "old" undefined.
- **Vol II §28.D, p. 64:** "V(b,B) = min(R(b), min[q: c(q)≤B] {C(q) + E[y] V(b after y,
  B−c(q))})." C(q) does not depend on the hypothesis and no transition model is given, although
  harm may be placed "in the transition model".
- **Vol II App. A.1, p. 116:** "VOI(p) , NetVOI(p)" is mapped to "local value of information
  VOI(q)" and a "final policy".
- **Already in the text (Vol I Operational Core §3, p. 15):** "These formalisms are not
  claimed as original." Vol II §28.D defines R(b) and VOI(q).

## Why it matters

Ablations and metrics intervene on these objects. If they are missing or differ between
volumes, an implementation can satisfy the equations without being a Core.

## Recommendation

State the rule once in the Vol II form, saying whether the stopping rule uses VOI(q) or
V(b,B). Add the required distinction and the sufficiency verdict to the cycle, define Y, its
horizon, "matched control" and "old", and add a quantity for rejecting false analogy.

## Resolved when

- [ ] One notation for VOI, costs and the stopping rule is used in both volumes, and
      Appendix A.1 lists the formulations separately.
- [ ] Every object the A.3 ablations intervene on has a named variable; each quantity has
      defined controls.

## Related

- Review: [§2.1](../../REVIEW.md#21-the-functional-cycle-holds-together),
  [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-13, MAJ-03, MED-19
