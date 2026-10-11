---
id: MED-13
title: The one-step stopping test recurs where §28.D says it fails
severity: medium
area: formal
volumes: I, II
sections: Vol I Operational Core, §12.6; Vol II §28.C, §28.D, §28.E, §29.0, App. A.1
review: §5.2(f)
status: open
github_issue: 21
---

# MED-13 · The one-step stopping test recurs where §28.D says it fails

## Claims under review

- **Vol II §28.D, p. 64:** "For a sequence of tests, finite planning with budget B is used" and,
  among the mandatory controls, "two tests useful only in sequence".
- **Vol I §12.6, p. 59:** "The ground is sufficient for the current step when the remaining
  material uncertainty can no longer change the best admissible alternative, or when the
  expected improvement from the next test becomes smaller than its cost, risk, and delay."
- **Vol I Operational Core, p. 15:** "For an inquiry plan p in a task where the relevant
  quantities admit a common operational loss scale, define: [...] Inquiry continues while there
  exists an admissible test with NetVOI(p) > 0 within the deadline, authority, and other hard
  constraints."
- **Vol II §28.C, p. 58:** step 4 of `assess_sufficiency`, "estimate the expected benefit of the
  next test relative to its cost". **Vol II §29.0, p. 67:** "A ground is sufficient for a
  particular step when remaining uncertainty no longer changes the selected class of
  continuation, or when the next test has lower expected value than its cost, risk, and delay."

## Finding

Volume II §28.D gives an exact, non-myopic policy and adds a mandatory control, "two tests
useful only in sequence", for the case where single tests are worthless and combinations are
valuable. Volume I §12.6 points to §28.D as its "finite computable version", and its
sufficiency rule has a non-myopic first clause (stop when residual uncertainty can no longer
change the best alternative). But the second clause, the reference heuristic of §28.C and the
definition of sufficiency in §29.0 all use a one-step test: compare the next test's expected
benefit with its cost. The Operational Core is ambiguous between the two: it defines NetVOI
over an inquiry plan p, which need not be myopic, but states its stopping rule in terms of "an
admissible test". A Core built from the reference heuristic stops in exactly the cases where
the exact policy continues. Appendix A.1 presents Vol I's plan-level NetVOI and Vol II's
single-test VOI and recursion as one counterpart, which hides the difference. Neither volume
discusses the cost of the exact rule: optimal test sequencing is NP-hard in general (Hyafil &
Rivest 1976), and §28.E's degradation order is not an approximation with a guarantee.

## Evidence

- **Already in the text (Vol I §12.6, p. 59):** "A finite computable version of this rule is
  given in engineering §§28.D and 33.C.1."
- **Vol II Appendix A.1, p. 116:** a table row pairs Vol I's "VOI(p), NetVOI(p)" with one
  counterpart, "local value of information VOI(q), separate [...] accounting of cost/delay/risk,
  and final policy V(b,B)" (the omitted words belong to the neighbouring column of the table).

## Why it matters

Premature sufficiency is the failure the programme exists to detect
(`premature_sufficiency_rate` is a Core metric). A stopping rule that produces it in the
joint-information case would make the Core fail its own control, and an implementer reading
Volume I or the reference heuristic would build that rule.

## Ideas & possible recommendations

- **State one stopping rule.** Both volumes could say that the ground is sufficient when no test
  sequence within the budget has positive expected net value, computed by V(b,B) or to a stated
  lookahead depth.
- **Call it from the Core.** `assess_sufficiency` could call that rule when the model is closed.
- **Name the one-step rule as an approximation.** The one-step test could stay as a named
  approximation, with a statement of when it is acceptable.
- **Give §28.D its complexity and a scalable approximation.** The section could state the cost
  of the exact rule and an approximation with a guarantee (EC²/DRD-style adaptive submodular
  selection).

## Resolved when

- [ ] The Operational Core, §12.6, §28.C and §29.0 state the same non-myopic rule as §28.D, or
      name their one-step test as an approximation and say when it is acceptable.
- [ ] §28.D states its complexity and names the approximation used at scale.

## Related

- Review: [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-03 (closed-world decision rule), MED-26 (Operational Core formulas)
