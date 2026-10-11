---
id: MED-26
title: The Operational Core formulas are incomplete and inconsistent with Vol II
severity: medium
area: formal
volumes: I, II
sections: Vol I Operational Core §1–§5; Vol II §28.D, App. A.1
review: §2.1, §5.2(f)
status: open
github_issue: 34
---

# MED-26 · The Operational Core formulas are incomplete and inconsistent with Vol II

## Claims under review

- **Vol I Operational Core, p. 14:** "The formulas below provide a minimal language for
  engineering comparison and connect the philosophical foundation with measurable causal
  relations. Different implementations may satisfy these relations." The cycle is given as
  "(X_t, W_t, F_t, M_t) → G_t → H_t → p_t → E_t → (W'_t, F'_t, M'_t) → A_t → X_{t+1}."
- **Vol I Operational Core §3, p. 15:** "For an inquiry plan p in a task where the relevant
  quantities admit a common operational loss scale, define: VOI(p) = E[ΔL | p], NetVOI(p) =
  VOI(p) − C_obs(p) − C_comp(p) − C_delay(p) − R_irrev(p), where VOI(p) is the expected
  reduction in decision loss due to the result of the test; C_obs is the cost of obtaining
  data; C_comp the computational cost; C_delay the cost of delay; and R_irrev the expected cost
  of irreversible consequences caused by the test itself." The stopping rule follows: "Inquiry
  continues while there exists an admissible test with NetVOI(p) > 0 within the deadline,
  authority, and other hard constraints."
- **Vol I Operational Core §§4–5, p. 15:** "The causal status of the carrier of a correction is
  supported when removing it, with subsequent data held equal, restores the behavioral or
  outcome difference associated with it."; "TG_(A→B) = Y_(B | learned A) − Y_(B | matched
  control),"; "RG = Y_(old,before) − Y_(old,after)."
- **Vol II §28.D, p. 64:** "VOI(q) = R(b) − E[y | b,q] R(b after y)."; "Under this local
  criterion, a test is justified if VOI(q) exceeds its cost of obtaining and processing data
  plus additional loss from delay."; "V(b,B) = min(R(b), min[q: c(q)≤B] {C(q) + E[y] V(b after
  y, B−c(q))})."; **Vol II Appendix A.1, p. 116:** "Causal model 8.0 introduces a compact
  operational notation for comparative tests. The engineering structures of this volume already
  provide its observable counterparts:"

## Finding

The Operational Core is offered as "a minimal language for engineering comparison". As written
it is incomplete: ΔL is undefined (VOI is described only as "the expected reduction in decision
loss") and VOI is conditioned on a plan; the cycle has no term for the required distinction or
the sufficiency verdict; and the transfer, regression and carrier-removal quantities leave
their controls open. Vol II §28.D gives a working form, but it differs from Vol I: its local
criterion names the cost of obtaining and processing data and the loss from delay and places
harm "exactly once in costs or in the transition model", and its recursion folds cost and delay
into one C(q), instead of Vol I's four terms (C_obs, C_comp, C_delay, R_irrev). For sequences of
tests it uses a budgeted recursion rather than a stop-while-positive rule, and Appendix A.1 maps
both onto one counterpart.

## Evidence

- **Vol I Operational Core §§1, 3–5, pp. 14–15:** the primed variables W'_t, F'_t and M'_t of
  the cycle are not defined, and no term stands for the required distinction or the sufficiency
  verdict. VOI is defined for a plan, the stopping rule for a test. The carrier-removal
  criterion says that removal "restores" the difference associated with the correction, which
  is ambiguous, and "matched control" and "old" are not defined.
- **Vol II §28.D, p. 64:** C(q) does not depend on the hypothesis and no transition model is
  given, although harm may be placed "in the transition model".
- **Already in the text (Vol II §28.D, p. 64):** "Harm caused by the test itself is included
  exactly once in costs or in the transition model."; "Here c(q)>0 is expenditure of a limited
  resource, and C(q) is cost plus the additional price of delay on the loss scale."
- **Vol II Appendix A.1, p. 116:** "VOI(p), NetVOI(p)" is mapped to "local value of information
  VOI(q)" and a "final policy".
- **Already in the text (Vol I Operational Core §3, p. 15):** "These formalisms are not claimed
  as original." Vol II §28.D defines R(b) and VOI(q).

## Why it matters

Ablations and metrics intervene on these objects. If they are missing or differ between
volumes, an implementation can satisfy the equations without being a Core.

## Ideas & possible recommendations

- **State the rule once.** The rule could be stated once, in the Vol II form, saying whether
  the stopping rule uses VOI(q) or V(b,B).
- **Complete the cycle.** The cycle formula could gain terms for the required distinction and
  the sufficiency verdict.
- **Define the transfer and regression quantities.** Y, its horizon, "matched control" and
  "old" could be defined.
- **A quantity for false analogy.** A quantity for rejecting false analogy could be added,
  since the same section asks for transfer with "rejection of false analogy".

## Resolved when

- [ ] One notation for VOI, costs and the stopping rule is used in both volumes, or Appendix
      A.1 lists the formulations separately.
- [ ] Every object the A.3 ablations intervene on has a named variable; each quantity has
      defined controls.

## Related

- Review: [§2.1](../../REVIEW.md#21-the-functional-cycle-holds-together),
  [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-13, MAJ-03, MED-19
