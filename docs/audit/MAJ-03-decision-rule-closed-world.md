---
id: MAJ-03
title: The Core's only committed decision rule covers closed, fully specified problems
severity: major
area: architecture
volumes: I, II
sections: Vol I guide Step 7, Operational Core; Vol II §28.0, §28.B, §28.C, §28.C.2, §28.D, §33.C.1
review: §5.2(f), §5.3
status: open
---

# MAJ-03 · The Core's only committed decision rule covers closed, fully specified problems

**Finding.** Volume II specifies the Core at three levels: a reference heuristic (§28.C),
labelled "heuristic, not a proof of optimality"; an exact, non-myopic Bayes policy for the
formalizable part (§28.D); and an explicit statement that generation and control may share
one model (§28.C.2). That is more than the review first credited. The exact policy, though,
applies only "given known hypotheses H, outcome probabilities and comparable losses", and
returns UNRESOLVED otherwise. The cases where the Core is meant to differ from a strong agent
(an unknown factor, a hidden cause that mimics a known one, a channel of unknown
reliability) are exactly the cases the policy does not cover. There the heuristic names
comparisons (expected value balance, whether residual uncertainty can change the best
option, the benefit of the next test) without saying how they are computed, so in a
language-model implementation the judgments fall to the model. The executable example shows
the consequence: with one listed alternative left, it commits the repair.

## Evidence

- **Vol II §28.D, p. 64:** "Given known hypotheses H, outcome probabilities and comparable
  losses"; "Under unknown probabilities or an incomplete model, the result remains
  UNRESOLVED"; the policy "V(b,B) = min(R(b), min[q: c(q)≤B] {C(q) + E[y] V(b after y,
  B−c(q))})". No complexity or approximation is discussed.
- **Vol II §28.0, p. 52:** "These factors permit lexicographic, Pareto, probabilistic, or
  hybrid selection. The universal requirement is a causal trace, not a particular scalar
  utility function."
- **Vol II §28.C, p. 58:** the reference procedure "permits routine Intelligence to generate
  content while preserving the Core's observable function of selecting a significant
  distinction"; "This procedure is heuristic, not a proof of optimality."
- **Vol I guide, p. 4:** "A single remaining version means only that it is unique within the
  accepted set." **Vol II §33.C.1, p. 109:** "Initial hypotheses, loss functions and the
  sufficiency criterion are set by the designer"; run on an emulated hidden cause, the
  restored listing commits `REPAIR_D` after one probe.
- **Already in the text (Vol II §28.D, p. 63):** "Hard constraints of safety, authority and
  irreversibility apply first." §28.B adds an invariant that every class of incompleteness
  has an admissible next transition.

## Why it matters

Without a committed rule for the open-world case, a negative result can be blamed on an
implementation choice, and a positive result cannot be attributed to the organization rather
than to the model's judgment. The formalizable parts already have algorithms with
guarantees: grouping hypotheses by admissible continuation and finding a distinction that
separates groups with different decisions (§28.C steps 3–4) is Equivalence Class
Determination (Golovin, Krause & Ray 2010) and Decision Region Determination (Javdani et al.
2014). Exact test sequencing is NP-hard in general (Hyafil & Rivest 1976).

## Recommendation

Extend the committed rule to the open world: add an explicit catch-all hypothesis whose prior
mass is tied to `EpistemicMargin`, give frame-expansion tests a value in the same recursion,
and use an EC²/DRD-style approximation beyond small instances. Otherwise state that, outside
closed models, the language model's judgment is the decision rule, and test the scaffold as
such. In both cases mark which fields of the significance trace are computed and which the
model fills.

## Resolved when

- [ ] The volumes name one rule for candidate selection and sufficiency in the open-world
      case, or declare model judgment to be the rule there.
- [ ] §28.D states its complexity and the approximation used at scale.
- [ ] The diagnostic example implements the hidden-cause coverage test before committing a
      repair.

## Related

- Review: [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-13 (one-step stopping test), MED-19 (model-filled significance), MED-22 (gap
  taxonomies), MED-25 (Core ablation), MED-28 (EpistemicMargin)
