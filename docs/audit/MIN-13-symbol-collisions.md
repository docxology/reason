---
id: MIN-13
title: Symbols collide across formulas, and the formulas are not typeset
severity: minor
area: formal
volumes: I, II
sections: Vol I guide §3, Operational Core; Vol II §28.0, §28.A, §28.B, §28.D, §29.0.1, Ch. 30
review: Appendix A
status: open
github_issue: 59
---

# MIN-13 · Symbols collide across formulas, and the formulas are not typeset

**Finding.** Both volumes reuse single letters for unrelated quantities, sometimes in adjacent
formulas, and set their formulas as plain-text code instead of typeset mathematics. With no symbol
table, a reader must infer from context what D, A, C, E, b or H denotes, and Volume II re-maps
Volume I's notation in Appendix A.1.

## Evidence

- **Vol I guide §3, p. 4, and Operational Core, pp. 14–15:** D is a hypothesis ("D The command was
  not delivered") and a decision ("D the dependent decision"). A is an actuator hypothesis, "A_t
  the selected action" and "class A". C is "C the Compass" and, in "C_obs", a cost; E is "E_t the
  evidence" and the expectation in "E[ΔL | p]".
- **Vol II §28.D, p. 64, and §29.0.1, p. 68:** b is a belief in "R(b) = min[a∈A] E[L(a,H) | b]"
  and an alternative action in "b an alternative". H is "known hypotheses H" in §28.D and "H is
  the horizon" in §29.0.1.
- **Vol II §28.0, p. 53:** QuestionTask tags fields with bare letters ("required_distinction # R",
  "constraints[] # L"), although R and L also denote expected loss and loss in §28.D. K is a count
  in "after K corrections" (§28.B, p. 55) and "the scale of conditional points" (§29.0.1). "N / M"
  (§28.A, p. 54) and "( W,N,M,P,H )" (Ch. 30, p. 74) are not defined where they appear.
- **Formulas as printed, Vol I pp. 14–15 and Vol II pp. 64, 68:** "X_{t+1}" and "sum_i(w_i *
  Delta_i)" are ASCII, and in "VOI(q) = R(b) − E[y | b,q] R(b after y)." the expectation names no
  variable, so it reads as E[y] times R.

## Why it matters

Volume II's tests and metrics are defined over these symbols. When a letter changes meaning
between neighbouring formulas, a reader or implementer cannot tell what a formula constrains.

## Recommendation

Add a symbol table to each volume, rename colliding symbols (for example h for hypotheses and d
for decisions), write each expectation with its distribution, and typeset every formula.

## Resolved when

- [ ] Each volume has a symbol table, no letter has two meanings, and all formulas are typeset.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MED-26
