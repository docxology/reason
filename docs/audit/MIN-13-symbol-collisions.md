---
id: MIN-13
title: Symbols collide across formulas, and the formulas are not typeset
severity: minor
area: formal
volumes: I, II
sections: Vol I guide §3, Operational Core; Vol II Ch. 27, §28.0, §28.A, §28.B, §28.D, §29.0.1, Ch. 30, App. A.1
review: Appendix A
status: open
github_issue: 59
---

# MIN-13 · Symbols collide across formulas, and the formulas are not typeset

## Claims under review

- **Vol I Operational Core, p. 14:** "The formulas below provide a minimal language for
  engineering comparison and connect the philosophical foundation with measurable causal
  relations. Different implementations may satisfy these relations."
- **Vol II A.1, p. 117:** "The notation of the fundamental volume does not introduce a new
  parallel algorithm. It serves as a compact language for the same measurable transitions and
  allows them to be tested independently of particular structure names."

## Finding

The formulas are offered as a language for comparing implementations, yet both volumes reuse
single letters for unrelated quantities, sometimes in adjacent formulas, and set their formulas
as plain-text code instead of typeset mathematics. With no symbol table, a reader must keep
track of which meaning a letter has in each formula: D, A, C, E, b and H are each defined where
they are used, but they mean different things in different sections, and "N / M",
"( W,N,M,P,H )" and the bare-letter tags in QuestionTask are not defined where they appear.
Volume II re-maps Volume I's notation in Appendix A.1.

## Evidence

- **Vol I guide §3, p. 4, and Operational Core, pp. 14–15:** D is a hypothesis
  ("D The command was not delivered") and a decision ("D the dependent decision"). A is an
  actuator hypothesis, "A_t the selected action" and "class A". C is "C the Compass" and, in
  "C_obs", a cost; E is "E_t the evidence" and the expectation in "E[ΔL | p]".
- **Vol II §28.D, p. 64, and §29.0.1, p. 68:** b is a belief in "R(b) = min[a∈A] E[L(a,H) | b]"
  and an alternative action in "b an alternative". H is "known hypotheses H" in §28.D and
  "H is the horizon" in §29.0.1.
- **Vol II §28.0, p. 53:** QuestionTask tags fields with bare letters
  ("required_distinction # R", "constraints[] # L"), although R and L also denote expected loss
  and loss in §28.D. K is a count in "after K corrections" (§28.B, p. 55) and
  "the scale of conditional points" (§29.0.1, p. 68). "N / M" (§28.A, p. 54) and
  "( W,N,M,P,H )" (Ch. 30, p. 74) are not defined where they appear.
- **Already in the text (Vol I Operational Core, pp. 14–15; Vol II §28.D, p. 64, and §29.0.1,
  p. 68):** D, A, C, E, b and H are each defined where they are used, for example
  "E_t the evidence, and A_t the selected action" (p. 14), "where G is the gap, D the dependent
  decision" [...] "and C the Compass" (p. 15), "under current distribution b" (p. 64) and
  "H is the horizon" (p. 68).
- **Formulas as printed, Vol I pp. 14–15 and Vol II pp. 64, 68:** "X_{t+1}" and
  "sum_i(w_i * Delta_i)" are ASCII, and in "VOI(q) = R(b) − E[y | b,q] R(b after y)." the
  expectation names no variable, so it reads as E[y] times R.

## Why it matters

Volume II's tests and metrics are defined over these symbols. When a letter changes meaning
between neighbouring formulas, a reader or implementer must check the local definition each
time to know what a formula constrains, and for the undefined symbols there is none to check.

## Ideas & possible recommendations

- **Add a symbol table.** A table in each volume listing every symbol, its meaning and the
  sections where it applies would show at a glance where D, A, C, E, b and H change meaning,
  and would define the symbols that are not defined where they appear. It could also carry the
  mapping from Volume I notation to Volume II structures that Appendix A.1 already gives.
- **Rename colliding symbols.** Giving each quantity its own letter, for example h for
  hypotheses and d for decisions, would remove the collisions at the source.
- **Write each expectation with its distribution.** Naming the variable and its distribution
  under each expectation would settle how to read "E[y | b,q] R(b after y)", which can now be
  taken as E[y] times R.
- **Typeset the formulas.** Every formula could be set as typeset mathematics instead of
  plain-text code.

## Resolved when

- [ ] In each volume every symbol is defined where it is used or in a symbol table, no letter
      has two meanings, and all formulas are typeset.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MED-26
