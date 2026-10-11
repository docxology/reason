---
id: MAJ-01
title: No comparative evidence yet for the central hypothesis
severity: major
area: evidence
volumes: I, II
sections: Vol I A.2, A.2.1, A.4; Vol II §27.B
review: §5.2(a), §7, §9
status: open
github_issue: 1
---

# MAJ-01 · No comparative evidence yet for the central hypothesis

**Finding.** Neither volume reports a comparison between the proposed organization (the
Core plus the epistemic layer) and any baseline. The only empirical activity is a
benchmark-construction pilot: four of five task packages were rejected, no candidate system
was evaluated, and the work stopped before any comparative run. Every claim that the
organization improves fault localization, sufficiency judgments, persistence of corrections
or transfer is therefore a hypothesis, not a result. The author says so plainly, which is to
his credit; the issue is that the titles, the abstract and the "technology" framing read as
if the work were further along.

## Evidence

- **Vol II §27.B, p. 49:** "For 005, a G0 report is preserved showing 89 checks passed; in
  the reviewed materials there is no completed external admission of this package and no
  comparative C0/C1/C2 run. [...] Its results do not establish autonomy of the Core or an
  architectural advantage."
- **Vol II §27.B, p. 49:** "P0-SET-001 and 002 were rejected because of alignment and
  dataset-quality errors; machine-aligned 003 and 004 were rejected because confirmed
  shortcut methods allowed guessing." The pilot ran "in a dialogue loop with the author's
  participation".
- **Vol I A.2.1, p. 95** (evidence table): the row is labelled "Inquiry-loop pilot", although
  the pilot evaluated no inquiry loop; for the "Central discriminating test" the status is
  "Program and controls are formulated", and the next step is "Run a preregistered series
  under equal total resources". For ASI the status is "Scaling direction only".
- **Vol I A.4, p. 99:** the first series is described as "proposed variants, not
  implemented results".

## Why it matters

The scientific status of the programme turns on this gap. Without a comparative run the
work cannot be classified as progressive or degenerating in Lakatos's sense, the functional
decomposition cannot be told apart from a strong agent stack that lacks it, and none of the
37 proposed tests has a result. Each further revision of the text without data moves the
target for reviewers (MED-15).

## Recommendation

Run the single preregistered comparison described in review §10: the same model, tools and
token and call budget for four arms (a strong agent stack, the stack plus the Vol II
epistemic layer only, the stack plus the full Core, and the exact dynamic-programming
oracle where tractable), on generated diagnosis families with perturbations and at least one
external benchmark. Rename the A.2.1 row "benchmark-construction pilot" and state in it that
no candidate was evaluated. Freeze the text until the result exists.

## Resolved when

- [ ] A preregistration (hypotheses, primary outcomes, effect size, sample size, analysis,
      stopping rule, abandonment condition) is public before data collection.
- [ ] At least one comparative run against a strong null at equal total resources is
      reported, with code and logs, whatever the outcome.
- [ ] The A.2.1 evidence table is updated to cite that result.

## Related

- Review: [§5.2(a)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§9](../../REVIEW.md#9-scientific-status),
  [§10](../../REVIEW.md#10-recommendations-in-priority-order)
- Issues: MED-11 (no preregistered instance), MED-12 (failure condition), MED-09 (ceiling
  risk), MED-15 (version churn), MED-23 (unpublished pilot materials)
