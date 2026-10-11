---
id: MED-01
title: The model's necessities are mostly near-analytic, and its two empirical ones overreach
severity: medium
area: theory
volumes: I
sections: Vol I Key Definitions, Ch. 4, §12.8, §13.2, A.2, A.2.1
review: §2.2
status: open
github_issue: 9
---

# MED-01 · The model's necessities are mostly near-analytic, and its two empirical ones overreach

**Finding.** The author sorts his statements into definitions, philosophical foundations,
conditional functional inferences and empirical hypotheses (A.2), and calls the §12.8 list
"conditional functional necessities", so the status of most of §13.2 is disclosed. Most of
those necessities are true but nearly true by definition: a system that must change its
future after a signal disappears must store something. Two are offered as substantive and
overreach. Item 14 says an earlier guiding loop is required for any capability that must
arise through experience; read as "some learning signal", that is trivial, and read as the
RFL's separate hint channel, it is not entailed (self-play and intrinsically rewarded learners
acquire exploratory behaviour without one). The Principle of Pre-rational Significance has a
refutation arm, but its realizer class includes "properties of the learning environment" and
"another functionally equivalent organization", so the refuting case cannot occur. The
evidence table also says counterexamples to functional claims "are given"; I found none in
Volume I. In causal inference a causal model predicts the effects of interventions,
including magnitudes; the volumes give a functional decomposition with predicted directions
of ablation effects.

## Evidence

- **Already in the text (Vol I A.2, p. 95):** "a conditional functional inference links a
  capability to a necessary condition".
- **Vol I §13.2, p. 63:** "If an acquired distinction must change the future after the signal
  disappears, a persistent trace is required"; item 14: "If the system is not yet able to
  sustain its own learning, inquiry, and preservation of trajectory, but these functions must
  arise through experience, an earlier loop is required to guide formation".
- **Vol I §13.2, p. 63:** "Stronger requirements — a common conscious picture, explicit typing
  of gaps, detailed provenance of knowledge, and a particular organization of the Core —
  remain hypotheses about implementation and its advantages."
- **Vol I Ch. 4, p. 28:** the pre-rational layer "may be implemented by the RFL, an AI mentor,
  an automatic system of guiding states, properties of the learning environment, or another
  functionally equivalent organization".
- **Vol I A.2.1, p. 95:** the evidence table's "Functional relations" row reads "Conditional
  causal arguments and [...] counterexamples are given".

## Why it matters

Calling the whole a "causal model" invites readers to expect intervention-level predictions
and then to judge the work by a standard it does not aim at. A principle whose refuting case
cannot occur cannot carry the formation programme (MAJ-05); only the narrower §20.1.2 claim
can.

## Recommendation

Separate the definitional necessities from the empirical hypotheses in §13.2 and cite the
cybernetic results that cover the former (Conant & Ashby 1970; Ashby 1956). Relabel item 14
and the Principle of Pre-rational Significance as design hypotheses, name the baseline whose
success would refute them (an intrinsic-reward or self-play learner without a hint channel),
point the A.2.1 cell to actual counterexamples or reword it, and attach a predicted direction
and minimum effect to each ablation.

## Resolved when

- [ ] §13.2 distinguishes definitional necessities from empirical hypotheses.
- [ ] The pre-rational-significance claim names a refuting baseline that can occur.

## Related

- Review: [§2.2](../../REVIEW.md#22-the-necessities-are-close-to-analytic-the-substance-is-in-untested-hypotheses)
- Issues: MAJ-01, MAJ-05 (formation experiment), MED-12 (failure condition)
