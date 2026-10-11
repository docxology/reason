---
id: MAJ-03
title: The Core's only committed decision rule covers closed, fully specified problems
severity: major
area: architecture
volumes: I, II
sections: Vol I guide Step 7, Operational Core; Vol II §28.0, §28.B, §28.C, §28.C.2, §28.D, §33.C.1
review: §5.2(f), §5.3
status: open
github_issue: 3
---

# MAJ-03 · The Core's only committed decision rule covers closed, fully specified problems

## Claims under review

- **Vol II §28.D, p. 64:** "Given known hypotheses H, outcome probabilities and comparable
  losses, define admissible actions A and particular test plans Q." Later in the same section:
  "Under unknown probabilities or an incomplete model, the result remains UNRESOLVED; interval
  estimates, limited exploration, safe action, or pause are permitted."
- **Vol I Operational Core, item 3, p. 15:** "For an inquiry plan p in a task where the
  relevant quantities admit a common operational loss scale, define: [...] where VOI(p) is the
  expected reduction in decision loss due to the result of the test; [...] Inquiry continues
  while there exists an admissible test with NetVOI(p) > 0 within the deadline, authority, and
  other hard constraints. Incommensurable consequences are compared through partial ordering,
  explicit constraints, and preserved uncertainty."
- **Vol II §28.C, p. 58:** "The contract is supplemented by a procedure sufficient for an
  independent first implementation in an open environment. It permits routine Intelligence to
  generate content while preserving the Core's observable function of selecting a significant
  distinction." Its `assess_sufficiency` step tells the Core to "compare expected value
  balance" among admissible alternatives, to "test whether residual uncertainty can change the
  best admissible option" and to "estimate the expected benefit of the next test relative to
  its cost". The text adds: "This procedure is heuristic, not a proof of optimality."
- **Vol II §28.0, p. 52:** "When several candidates exist, the Core compares: consequences of
  possible error; urgency and reversibility; [...] and transferability of the result to future
  tasks. These factors permit lexicographic, Pareto, probabilistic, or hybrid selection. The
  universal requirement is a causal trace, not a particular scalar utility function."

## Finding

Volume II specifies the Core at three levels: a reference heuristic (§28.C), labelled
"heuristic, not a proof of optimality"; an exact, non-myopic Bayes policy for the formalizable
part (§28.D); and an explicit statement that generation and control may share one model
(§28.C.2). That is more than the review first credited. The exact policy, though, applies only
when the hypotheses, outcome probabilities and losses are known and comparable (first claim
above), and returns UNRESOLVED otherwise. The cases where the Core is meant to differ from a
strong agent (an unknown factor, a hidden cause that mimics a known one, a channel of unknown
reliability) are exactly the cases the policy does not cover. There the heuristic names
comparisons (expected value balance, whether residual uncertainty can change the best option,
the benefit of the next test) without saying how they are computed, so in a language-model
implementation the judgments fall to the model. The executable example shows the consequence:
with one listed alternative left, it commits the repair.

## Evidence

- **Vol II §28.D, p. 64:** the policy for a sequence of tests is "V(b,B) = min(R(b), min[q:
  c(q)≤B] {C(q) + E[y] V(b after y, B−c(q))})". No complexity or approximation is discussed;
  the only remark on size is "A finite set of plans and a finite budget exclude an infinite
  branch."
- **Vol II §28.C, p. 58:** steps 3 and 4 of `refine_gap_and_required_distinction` read "group
  versions that lead to the same admissible continuation" and "find an observable distinction
  separating groups with different decisions".
- **Vol I guide, p. 4:** "A single remaining version means only that it is unique within the
  accepted set. The completeness of the set requires its own ground."
  **Vol II §33.C.1, p. 109:** "Initial hypotheses, loss functions and the sufficiency criterion
  are set by the designer"; run on an emulated hidden cause, the restored listing commits
  `REPAIR_D` after one probe.
- **Already in the text (Vol II §28.D, p. 63):** "Hard constraints of safety, authority and
  irreversibility apply first." The invariant of determinate continuation adds: "Every class of
  incompleteness must have at least one admissible next transition that preserves causal
  history and later corrigibility" (§28.B, p. 56).
- **Already in the text (Vol II §28.C.2, p. 61):** "Generation and control may therefore use
  the same computational substrates and even one model if the causal roles are experimentally
  distinguishable."
- **Already in the text (Vol II §33.C.1, p. 109):** the listing's docstring says it makes "no
  LLM or open-world claims", and the text adds: "The next v0.2 implementation must replace the
  terminal reaction MODEL_MISMATCH → DEFER with preservation of an UnknownFactor and launch of
  bounded MODEL_EXPANSION". **Vol II §33.C.1, p. 111:** "The next mandatory version of the
  diagnostic test closes a harder open-world case"; there "the single remaining alternative
  among D/A/S has status only LOCAL_SUFFICIENT_WITHIN_MODEL until the declared coverage
  condition is satisfied", and "if no channel exists, it must preserve a limitation of scope
  rather than claim completeness of the list".

## Why it matters

Without a committed rule for the open-world case, a negative result can be blamed on an
implementation choice, and a positive result cannot be attributed to the organization rather
than to the model's judgment. The formalizable parts already have algorithms with guarantees:
grouping hypotheses by admissible continuation and finding a distinction that separates groups
with different decisions (§28.C steps 3–4) is Equivalence Class Determination (Golovin, Krause
& Ray 2010) and Decision Region Determination (Javdani et al. 2014). Exact test sequencing is
NP-hard in general (Hyafil & Rivest 1976).

## Ideas & possible recommendations

- **Extend the committed rule to the open world.** The rule could add an explicit catch-all
  hypothesis whose prior mass is tied to `EpistemicMargin`, give frame-expansion tests a value
  in the same recursion, and use an EC²/DRD-style approximation (the algorithms named under Why
  it matters) beyond small instances.
- **Or declare model judgment to be the rule.** The volumes could instead state that, outside
  closed models, the language model's judgment is the decision rule, and test the scaffold as
  such.
- **Mark computed and model-filled fields.** Under either option, the significance trace could
  mark which of its fields are computed and which the model fills.
- **Start with the coverage test.** A cheaper first step would be to implement in the
  executable example the `HiddenCauseCoverageTest` that §33.C.1 already specifies, so that the
  example no longer commits a repair on a single listed alternative.

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
