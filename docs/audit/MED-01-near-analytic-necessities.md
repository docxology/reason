---
id: MED-01
title: The model's necessities are mostly near-analytic, and its two substantive ones overreach
severity: medium
area: theory
volumes: I, II
sections: Vol I title page, Introduction, Key Definitions, Ch. 4, §12.8, §13.2, §20.1.2, A.2, A.2.1, A.3; Vol II §27.6, §31.1, §31.A
review: §2.2
status: open
github_issue: 9
---

# MED-01 · The model's necessities are mostly near-analytic, and its two substantive ones overreach

## Claims under review

- **Vol I §13.2, p. 63:** "If an acquired distinction must change the future after the signal
  disappears, a persistent trace is required." The last bullet of the same list, called item 14
  below, reads: "If the system is not yet able to sustain its own learning, inquiry, and
  preservation of trajectory, but these functions must arise through experience, an earlier
  loop is required to guide formation until these functions are causally transferred to the
  internal organization."
- **Vol I Ch. 4, pp. 28–29 (Principle of Pre-Rational Significance):** "Mature values cannot be
  the sole cause of their own emergence. [...] Therefore the path toward autonomous Reason
  requires an earlier function that makes states non-equivalent for continuation and learning.
  [...] In an artificial system it may be implemented by the RFL, an AI mentor, an automatic
  system of guiding states, properties of the learning environment, or another functionally
  equivalent organization." Then: "The necessity applies precisely to the function. If a
  candidate without feelings, an external mentor, or any other layer of pre-rational
  significance reproducibly reaches autonomous self-navigation under comparable conditions, the
  strong form of this hypothesis must be revised."
- **Vol I A.2.1, p. 95:** in the evidence table, the status of the "Functional relations" row
  ends with "counterexamples are given".
- **Vol I title page, p. 8:** "VOLUME I. THE CAUSAL MODEL OF REASON".
  **Vol I Introduction, p. 10:** "The philosophical foundation is evaluated by the coherence of
  its argument; the functional architecture is evaluated by causal counterexamples,
  interventions, and comparative tests."

## Finding

The author sorts the volumes' statements into definitions, philosophical foundations, conditional
functional inferences and empirical hypotheses (A.2), and calls the §12.8 list "conditional
functional necessities", so the status of most of §13.2 is disclosed. Most of those necessities
are true but nearly true by definition: a system that must change its future after a signal
disappears must store something. Two are offered as substantive and overreach: item 14, and the
Principle of Pre-rational Significance, which Key Definitions classes as "a functional
inference" but to which Chapter 4 and §20.1.2 attach an empirical refutation arm and an
experiment.

Item 14 (first claim above) says that a system not yet able to sustain its own learning,
inquiry, and preservation of trajectory, which must acquire them through experience, needs an
earlier loop to guide formation until they are transferred to its internal organization. If
that means only that some guiding signal is needed, it is near-trivial. §13.2 calls the RFL
"the reference artificial implementation" of that function, and Chapter 4 says "The necessity
applies precisely to the function" (p. 29), so the substantive reading is that a separate
guiding layer is needed. That is not entailed (self-play and intrinsically rewarded learners
acquire exploratory behaviour without an external guide), and §20.1.2 tests it.

The Principle has a refutation arm (second claim above), but its realizer class includes
"properties of the learning environment" and "another functionally equivalent organization",
and Chapter 4 fixes no class of such layers in advance, so as worded there the refutation arm
names no case that could occur. A.3 (p. 96) requires equivalents to be "specified in advance"
and says that equivalence "must not be defined retrospectively by success", but Chapter 4's
statement of the Principle does not apply that rule to its own list.

The evidence table says that for functional relations "counterexamples are given" without
saying counterexamples to what. Volume I states the results that would count against its
necessity claims (A.3, p. 96: seven "grounds for revision") and one worked situation (A.2,
p. 95), but it presents no case in which a functional claim is shown to fail. In causal
inference a causal model predicts the effects of interventions, including magnitudes; the
volumes give a functional decomposition with predicted directions of ablation effects.

## Evidence

- **Already in the text (Vol I A.2, p. 95):** "a conditional functional inference links a
  capability to a necessary condition"; the worked example is "two histories produce the same
  current observation but require different actions".
- **Already in the text (Vol I §12.8, p. 60):** "These are conditional functional necessities.
  The memory format, mode of common integration, and Core algorithm remain open implementation
  hypotheses."
- **Vol I §13.2, p. 63:** "Stronger requirements — a common conscious picture, explicit typing
  of gaps, detailed provenance of knowledge, and a particular organization of the Core — remain
  hypotheses about implementation and its advantages."
- **Vol I Key Definitions, p. 12:** the principle is defined as "a functional inference of the
  model about the origin of Reason"; its argument is "otherwise there is nothing to choose what
  to preserve, what to avoid, what to investigate, and what to learn".
- **Already in the text (Vol I Key Definitions, p. 12; §13.2, p. 63):** "What is necessary is
  the function of early significance itself, not any particular biological form of its
  implementation"; the RFL "is the reference artificial implementation" of that function.
- **Already in the text (Vol I A.3, pp. 96–97):** the items fixed before each discriminating
  test include "which alternative mechanisms are specified in advance as fulfilling the same
  obligation"; "Functional equivalence must not be defined retrospectively by success"; seven
  "grounds for revision" are listed for the central hypotheses; and "After a pilot, a meaningful
  effect and the required amount of testing are specified".
- **Already in the text (Vol I §20.1.2, p. 85):** the comparison includes "NO_KSR: the
  additional guiding layer is absent except for necessary physical constraints of the
  Incubator", and "If the NO_KSR regime reaches the same autonomous navigation with comparable
  resources, the necessity of a separate pre-rational layer is weakened."
- **Already in the text (Vol II §27.6, p. 47; §31.1, p. 79):** for each claimed necessary
  arrow, "the expected functional loss is specified in advance"; a transition requires that
  "intentional disruption of the mechanism produces the predicted loss of function"; and
  "Numerical thresholds are set before the control series."

## Why it matters

Calling the whole a "causal model" invites readers to expect predictions of intervention
effects, including their size. The volumes state the direction of a predicted effect (a
"predicted loss of function" when a mechanism is disrupted, Vol II §31.1) and leave sizes to
thresholds and effect sizes fixed before each series (Vol I A.3; Vol II §31.A), so a reader who
expects magnitudes will not find them in the text. A principle whose refuting case, as Chapter 4
words it, cannot occur cannot carry the formation programme (MAJ-05); only the narrower
§20.1.2 claim can.

## Ideas & possible recommendations

- **Separate definitional from empirical necessities.** §13.2 could distinguish the
  definitional necessities from the empirical hypotheses, and cite the cybernetic results that
  cover the former (Conant & Ashby 1970; Ashby 1956).
- **Relabel item 14 and the Principle as design hypotheses.** The text already defines an arm
  without the additional guiding layer (NO_KSR, §20.1.2, p. 85) and says its success would
  weaken "the necessity of a separate pre-rational layer". Item 14 and the Principle could be
  tied to that arm and could state in advance which signals count as a layer, since an
  intrinsic-reward or self-play learner could otherwise fall inside the realizer list of
  Chapter 4.
- **Fix the A.2.1 cell.** The cell could say that refutation conditions are given (A.3) or
  point to actual counterexamples.
- **Attach predictions to the ablations.** The transition rule already requires a predicted
  loss of function (Vol II §31.1); the text could also state, per ablation, the minimum effect
  that would count, instead of leaving it to the preregistered profile.

## Resolved when

- [ ] §13.2 distinguishes definitional necessities from empirical hypotheses.
- [ ] Chapter 4 and item 14 state in advance which signals count as a layer of pre-rational
      significance, so that a NO_KSR result (§20.1.2) bears on the Principle and not only on a
      separate layer.

## Related

- Review: [§2.2](../../REVIEW.md#22-the-necessities-are-close-to-analytic-the-substance-is-in-untested-hypotheses)
- Issues: MAJ-01, MAJ-05 (formation experiment), MED-12 (failure condition)
