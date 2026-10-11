---
id: MED-23
title: The pilot log, task packages and AI priority audits are cited but not published
severity: medium
area: provenance
volumes: I, II
sections: Vol I A.2; Vol II §27.B
review: §6, §7
status: open
github_issue: 31
---

# MED-23 · The pilot log, task packages and AI priority audits are cited but not published

**Finding.** Volume I lists the "historical materials" behind the pilot and the novelty claim:
three Elicit reports (a manuscript review, a novelty assessment and a "priority audit"), the
pilot log `reason-kernel-experiment.md`, decisions on P0-SET-001 to 004, and the archive
`p0-set-005-package.zip`. Volume II cites the same log and a G0 report with "89 checks passed".
None of these is published or linked, so neither the pilot's conduct nor the basis of the
novelty claim can be checked. The audits concern versions 5.3b and 6.1, not the reviewed 8.0,
whose Compass and self-preservation sections A.2 says changed at 7.0. The two volumes also
describe the pilot differently (a "positive machine-control report" against a "G0 report";
"external reviewers" appear only in Volume II), and the labels P0, G0 and C0/C1/C2 are never
defined. The author is careful to say the AI audit is "not proof of novelty or priority".

## Evidence

- **Vol I A.2, p. 94:** "Historical materials: "Elicit - Review of the manuscript Foundations of
  Reason 5.3b: comparative test"; "Elicit - Critical assessment of novelty of Foundations of
  Reason"; "Elicit - Independent priority audit of Foundations of Reason";
  reason-kernel-experiment.md; decisions on P0-SET-001-004 and the archive
  p0-set-005-package.zip."
- **Vol I A.2, p. 94:** "a comparative review of 5.3b, a critical novelty assessment of 6.1, a
  separate priority audit"; "a positive machine- control report is preserved for P0-SET-005".
- **Vol II §27.B, p. 49:** "The reason-kernel-experiment.md log contains cycles 1-15 [...] For
  005, a G0 report is preserved showing 89 checks passed".
- **Already in the text (Vol I A.2, p. 94):** the priority audit "is a result of a limited search
  process, not proof of novelty or priority".
- Neither volume gives a URL, DOI or repository for these materials.

## Why it matters

The audits are offered in support of priority ("did not identify a single earlier source
functionally equivalent to the whole integration"), and the pilot is the only empirical
activity reported. Unpublished support cannot be evaluated, and an audit of an earlier version
does not speak to the current one.

## Recommendation

Publish the pilot log, task packages, G0 report and Elicit outputs with persistent identifiers
(for example a Zenodo supplement), re-run any priority search on the current version with
documented queries, use one description of the pilot in both volumes, and define P0, G0 and
C0/C1/C2.

## Resolved when

- [ ] Every cited historical material is available at a stable link, or the claims that depend
      on it are removed.
- [ ] Both volumes describe the pilot identically.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures)
- Issues: MAJ-01, MAJ-07
