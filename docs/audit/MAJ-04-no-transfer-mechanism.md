---
id: MAJ-04
title: No mechanism that produces transfer of corrections and inquiry methods
severity: major
area: architecture
volumes: I, II
sections: Vol I front matter (guide, Principle of escaping error), §12.4, §12.7, §13.5; Vol II §24.B.1, §27.B, §33.C.1, Ch. 34
review: §5.3, §7
status: open
github_issue: 4
---

# MAJ-04 · No mechanism that produces transfer of corrections and inquiry methods

## Claims under review

- **Vol I front matter, p. 12 (Principle of escaping error):** "a correction is considered
  stable when the cause reproducing the error has been removed and this is confirmed by
  transfer of the correction to a new situation whose structural similarity was specified
  before testing in terms of causal roles and dependencies rather than declared after the fact
  to fit the result."
- **Vol I §13.5, p. 67:** "Superficially different tasks may share the same structure of
  ignorance: [...] Recognizing such a structure permits transfer of a previously successful
  investigative method, but only together with testing its conditions of applicability." Also:
  "When no suitable analogue exists, Intelligence constructs a new investigative move from the
  required distinction and available channels of observation."
- **Vol II §24.B.1, p. 22:** "ConceptBridge allows Intelligence to test an analogy—such as
  transfer of a flow, feedback or stability mechanism between different domains—without
  declaring the objects identical. An inference obtained through such a bridge initially has
  hypothetical status and retains the conditions of transfer."
- **Vol II Ch. 34, p. 114:** "The engineering unit of this technology is a retained transition
  from a question to a changed next step." **Vol I guide, p. 7:** "Question for the reviewer:
  with comparable Intelligence and the full resource budget, does the organization 'significant
  gap → discriminating test → revision of a ground → transfer of the correction' produce the
  reproducible result claimed in the test? If not, which specific link, condition, or
  explanation is wrong?"

## Finding

Transfer carries the programme's distinctive claim (first two claims above): a correction
counts only if it carries over to a case whose structural similarity was fixed before testing,
and inquiry methods are reused across tasks that share a "structure of ignorance". The volumes
specify rigorously how to *test* transfer, and describe in prose what a retained method should
contain (conditions of applicability, ground for the choice, required distinction, result,
boundary). They give no record or algorithm that abstracts such a schema from episodes and maps
it to a new case; that step is left to Intelligence. In the only executable example the
retained "method" is a plan cache keyed on the exact probe table, order and budget: with a warm
memory the decisions are identical and only the count of evaluated states changes, and renaming
a probe gives a full cache miss.

## Evidence

- **Already in the text (Vol I §12.4, p. 55):** "Memory retrieves a causal pattern: conditions
  of applicability, ground for the choice, required distinction, obtained result, and boundary
  of applicability." **Vol I §12.7, p. 59:** "Investigative experience records which structure
  of ignorance was encountered, why a method was chosen, which distinction it produced, and
  where transfer proved erroneous."
- **Already in the text (Vol II §27.B, p. 50):** "Before a run, the experimenter specifies a
  StructuralSimilarityProfile: which causal roles, dependencies, gap type, admissible
  interventions, and required distinction must be preserved between families A and B, and which
  surface features must change."
- **Already in the text (Vol II Ch. 34, p. 114):** the crystal table names the next limitation
  after inquiry into a ground: "Transfer beyond the episode is required".
- **Vol II §24.B.1, p. 22:** `ConceptBridge` records `mapped_features[]`, `unmapped_features[]`
  and `transfer_conditions[]`. It records a mapping; it does not compute one.
- **Vol II §33.C.1, p. 109:** "Memory retains episodes and computed conditional plans. The plan
  key includes test predictions, cost, hypothesis versions and the budget in their current
  representation. A changed table does not use the previous plan. In this small example, this
  is memoization of the inquiry procedure rather than autonomous invention of a new method. A
  repeated episode demonstrates the effect of retention but does not prove cross-domain
  transfer."

## Why it matters

Of the four links the guide asks reviewers to test (significant gap → discriminating test →
revision of a ground → transfer of the correction), this is the one with no proposed mechanism,
and the one most likely to make the full Core lose to a strong agent stack: if the mapping is
left to the model's in-context analogy, a baseline with the same model gets the same
capability. Abstracting an inquiry schema over causal roles is the problem studied in
analogical reasoning (structure-mapping: Gentner 1983; Falkenhainer, Forbus & Gentner 1989) and
case-based reasoning (Kolodner 1993; Aamodt & Plaza 1994).

## Ideas & possible recommendations

- **Specify the transfer mechanism first.** Before any transfer series, the volumes could give
  a representation of an inquiry method abstracted over causal roles (gap type, required
  distinction, the probe-to-hypothesis partition structure, the cost profile), an algorithm
  that retrieves and maps it to a new task, and the condition under which a mapping is rejected
  as a false analogy.
- **Test it against in-context analogy.** The mechanism could be compared with the same model
  doing in-context analogy without the representation, at equal resources.
- **Add an isomorphic-table variant.** §33.C.1 could gain a variant with renamed probes, so
  that the example tests more than a repeat of the same table.

## Resolved when

- [ ] An inquiry-method representation and a mapping algorithm are specified independently
      of the language model.
- [ ] The transfer series compares that mechanism with in-context analogy by the same model
      at equal resources, on preregistered isomorphic and look-alike families.

## Related

- Review: [§5.3](../../REVIEW.md#53-my-answer-to-the-guides-question-for-reviewers),
  [§7](../../REVIEW.md#in-need-of-development)
- Issues: MAJ-03 (decision rule), MED-22 (gap taxonomies), MIN-08 (code listings)
