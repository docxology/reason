---
id: MED-12
title: The failure condition for the Core is stated only qualitatively
severity: medium
area: testability
volumes: I, II
sections: Vol I Ch. 12, §12.8, §12.9, §13.2, Common Rules (p. 91), A.3, A.4; Vol II §25.D, §27.6, §27.B, §31.5, §34.A
review: §5.2(d), §9, §10.2
status: open
github_issue: 20
---

# MED-12 · The failure condition for the Core is stated only qualitatively

## Claims under review

- **Vol I A.3, p. 97:** "Insufficient precision of a comparison does not prove equality of
  systems. After a pilot, a meaningful effect and the required amount of testing are specified;
  the criterion may not be changed after examining the held-out results."
- **Vol I Common Rules, p. 91:** "A reproducible equivalent causal profile refutes the necessity
  of a particular decomposition while simultaneously supporting the functional criterion."
- **Vol II §27.B, p. 50:** "Operation of a strong equivalent refines the form of the
  architecture." **Vol II §31.5, p. 80:** "Success is measurable degradation specifically in
  those decisions for which the corresponding component was causally necessary; absence of an
  effect permits a more compact implementation of conscious assembly."
- **Vol I §12.8, p. 59:** "In the minimal working scheme, six causal obligations are
  distinguished" **Vol I §12.8, p. 60:** "An architecture with a different internal
  decomposition is considered functionally equivalent with respect to the corresponding duties
  if interventions show the same causal profile: detection of significant incompleteness,
  acquisition of a distinction, revision of grounds, and transfer of correction."

## Finding

The volumes do say what would count against the Core's added value, more often than the review
first credited: if inquiry management without explicit gap typing achieves the same transfer
and cost, "no independent advantage of this implementation is established" (A.3, p. 96); if
explicit organization does not outperform the strong control, "its additional usefulness is not
established" (A.4, p. 100); a strong null that reproduces the profile means the decomposition is
"reduced or eliminated" (§34.A, p. 115); and §27.B has the report status `CLAIM_NOT_SUPPORTED`
and adds that "a sound protocol without the target effect does not confirm the advantage of this
implementation" and that "failure with sound relations and an adequate test requires revision of
the functional claim" (p. 50). What is missing is the number: no equivalence margin or sample
size is fixed, and although §27.B names a principal outcome (the share of new diagnostic tasks
with a correct action or justified irresolvability under a fixed budget), neither volume says
which outcome decides the Core-versus-null comparison. A.3 adds that "insufficient precision of
a comparison does not prove equality of systems" (p. 97), so an underpowered null can never
count. Other passages pull the other way: Vol I's Common Rules say an equivalent profile
"simultaneously" supports the functional criterion, §27.B says a strong equivalent "refines the
form of the architecture", and §31.5 says, of the ablations of components of conscious assembly,
that "absence of an effect permits a more compact implementation of conscious assembly" (p. 80),
a stage criterion rather than a ruling on the Core. The set of duties against which equivalence
is judged is also stated three ways: six obligations (§12.8, p. 59), a four-item causal profile
(§12.8, p. 60) and fourteen conditional grounds that §13.2 says "define the causal duties of
§12.8" (p. 63), with no explicit mapping between the lists.

## Evidence

- **Already in the text (Vol I A.3, p. 96):** "inquiry management without explicit typing of
  the gap achieves the same transfer and cost: no independent advantage of this
  implementation is established"; "Functional equivalence must not be defined retrospectively
  by success."
- **Already in the text (Vol I A.4, p. 100):** "If explicit organization does not outperform the
  strong control, its additional usefulness is not established."; "The primary measures are
  correct localization, verification cost, actual action, transfer, and regression."
- **Already in the text (Vol II §27.B, p. 50):** "The principal outcome of the first series is
  the share of new diagnostic tasks with a correct action or justified irresolvability under a
  fixed budget. Secondary outcomes are cost of discrimination, false sufficiency, transfer,
  regression and use of stale grounds."; "A sound protocol without the target effect does not
  confirm the advantage of this implementation."; "Failure with sound relations and an adequate
  test requires revision of the functional claim."
- **Vol I §13.2, p. 63:** after fourteen conditional grounds, "These propositions define the
  causal duties of §12.8."

## Why it matters

The rule that would let the Core fail exists, but without a margin and with competing
phrasings it is easy to read every outcome as support. A research programme earns standing
by fixing in advance the result that would count against its distinctive claim.

## Ideas & possible recommendations

- **Fix the decisive comparison.** The preregistration could name one comparison: an agent with
  the Vol II epistemic layer but without gap typing, required-distinction grouping and
  inquiry-method memory, against the full Core, at equal total resources.
- **Name the deciding outcome and set the margin.** The preregistration could say which of the
  named outcomes decides the comparison, and set the equivalence margin and a power calculation
  in advance.
- **State the abandonment rule.** The volumes could say that equivalence within the margin means
  the Core is dropped as a distinct contribution, in the same words in both.
- **Reconcile the passages and publish one duty list.** The Common Rules sentence and §27.B
  could be brought into line with A.3, and a single list of duties, or an explicit mapping among
  the three lists, could take the place of the three formulations.

## Resolved when

- [ ] The deciding outcome, a quantitative equivalence margin and the sample size are
      preregistered for the decisive comparison.
- [ ] Both volumes state the abandonment rule in the same words.

## Related

- Review: [§5.2(d)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§9](../../REVIEW.md#9-scientific-status)
- Issues: MAJ-01, MAJ-03, MED-10 (process-conformance metrics), MED-11 (preregistration)
