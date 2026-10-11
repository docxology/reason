---
id: MED-23
title: The pilot log, task packages and AI priority audits are cited but not published
severity: medium
area: provenance
volumes: I, II
sections: Vol I A.2, A.2.1, A.5; Vol II §27.B, §33.C.1
review: §6, §7
status: open
github_issue: 31
---

# MED-23 · The pilot log, task packages and AI priority audits are cited but not published

## Claims under review

- **Vol I A.2, p. 94:** "The project archive preserves repeated studies using Elicit: a
  comparative review of 5.3b, a critical novelty assessment of 6.1, a separate priority audit,
  and thematic collections on reflective architectures, goal revision, external criticism, and
  memory of errors." Further on, a list reads "Historical materials: 'Elicit - Review of the
  manuscript Foundations of Reason 5.3b: comparative test'; 'Elicit - Critical assessment of
  novelty of Foundations of Reason'; 'Elicit - Independent priority audit of Foundations of
  Reason';" and continues "reason-kernel-experiment.md; decisions on P0-SET-001-004 and the
  archive p0-set-005-package.zip."
- **Vol I A.2, p. 94:** "The priority audit reports that, within the surveyed literature, the
  search did not identify a single earlier source functionally equivalent to the whole
  integration considered here."
- **Vol I A.2, p. 94:** "These failures led to changes in the builder and the verification
  procedure; a positive machine-control report is preserved for P0-SET-005. In the materials
  reviewed, the final comparison of subjects remains an open stage."; **Vol II §27.B, p. 49:**
  "The reason-kernel-experiment.md log contains cycles 1-15. [...] For 005, a G0 report is
  preserved showing 89 checks passed; in the reviewed materials there is no completed external
  admission of this package and no comparative C0/C1/C2 run. This is a documented
  methodological pilot of procedure development with human participation and external
  reviewers."

## Finding

Volume I lists the "historical materials" behind the pilot and the literature search: three
Elicit reports (a manuscript review, a novelty assessment and a "priority audit"), the pilot
log `reason-kernel-experiment.md`, decisions on P0-SET-001 to 004, and the archive
`p0-set-005-package.zip`. Volume II cites the same log and a G0 report with "89 checks
passed". None of these is published or linked, so a reader cannot inspect the Elicit reports,
the queries behind the priority search, or how the pilot was conducted. Volume I presents them
as research history that "supplements the primary scientific comparisons in A.5" (Vol I A.2,
p. 94), where the primary publications are listed and referenced.

Two of the three Elicit studies are tied to earlier versions (a comparative review of 5.3b and
a critical novelty assessment of 6.1); Volume I does not say which version the priority audit
covered. A.2 dates the clarification of self-preservation to revision 7.0 and says that
"older reports analyze the Compass as Life-Truth-Diversity", which the present revision treats
differently. The two volumes word the pilot differently (a "positive machine-control report"
in Volume I, a "G0 report" showing 89 checks passed in Volume II; "external reviewers" appear
only in Volume II) but agree on the date, cycles 1-15, the rejection of P0-SET-001 to 004 and
the absence of a final comparison, and Volume I refers the reader to §27.B for the pilot's
"status and limitations". The labels P0, G0 and C0/C1/C2 are never defined. The author is
careful to say the AI audit is "not proof of novelty or priority".

## Evidence

- **Already in the text (Vol I A.2, p. 94):** "These are materials of scientific search and
  AI-assisted analysis that can be checked against the cited sources; their status belongs to
  the author's research process and is separate from journal decisions."
- **Already in the text (Vol I A.2, p. 94):** "This is a result of a limited search process,
  not proof of novelty or priority; its role is to indicate directions for subsequent
  verification in primary sources."
- **Already in the text (Vol I A.2, p. 94):** closing the account of the revision sequence,
  "historical priority of any particular proposition is established by the corresponding dated
  source"; after the list of historical materials, "Research history supplements the primary
  scientific comparisons in A.5."
- **Already in the text (Vol I A.5, p. 100):** "Below is a selective map of primary
  publications for comparison of individual functions and the nearest architectures.
  Functional overlap, independent derivation, historical priority, and implementation
  advantage are treated as different questions."
- **Vol I A.2, pp. 93–94:** "Revision 7.0 separately clarifies self-preservation", and "Some
  older reports analyze the Compass as Life-Truth-Diversity. In the present revision, the
  Compass Phrase is primary, while Truth and Diversity are treated as conditions for applying
  the highest orientation." A.2 gives a revision for the first change only; for the Compass it
  says only that older reports read it differently from the present revision.
- **Already in the text (Vol I A.2, p. 94):** "Conclusions about the earlier operational scheme
  must therefore be interpreted in relation to what has changed."
- **Already in the text (Vol I A.2, p. 94):** "The methodological result of the pilot is
  traceable development of the procedure itself, including negative results; its status and
  limitations are disclosed in Section 27.B of the engineering volume."
- **Already in the text (Vol II §27.B, p. 49):** "Its results do not establish autonomy of the
  Core or an architectural advantage."
- **Vol I A.2.1, p. 95:** the evidence table reports two activities with results: the "Lower
  executable loop" (a limited example of learning from consequences has been completed) and
  the "Inquiry-loop pilot" ("Methodological results have been obtained"). The front matter
  says "completed lower-level and methodological pilots are separated from the still-open
  integrated upper-loop test" (p. 8).
- **Vol II §33.C.1, p. 109:** the "Executable Diagnostic Cycle" is a further executable
  example, and its text says "Derivation of values, subjective experience and scaling to ASI
  are not tested by this code."
- Neither volume gives a URL, DOI or repository for these materials.

## Why it matters

The priority audit is cited for a limited search result ("did not identify a single earlier
source functionally equivalent to the whole integration"). The author calls it "not proof of
novelty or priority" and says that historical priority "is established by the corresponding
dated source". Unpublished outputs cannot be evaluated even in that limited role. The volume
also does not say which version the audit covered: if it predates 8.0, it does not speak to
the current version, and the author's own rule applies, that conclusions "must therefore be
interpreted in relation to what has changed".

Beyond two limited executable examples (the lower-loop example in the A.2.1 evidence table and
the diagnostic cycle of §33.C.1), the pilot is the only empirical activity reported. The author
states that its results "do not establish autonomy of the Core or an architectural advantage"
(Vol II §27.B, p. 49) and that its methodological result is "traceable development of the
procedure itself, including negative results" (Vol I A.2, p. 94). It therefore documents the
development of the test procedure rather than support for the architecture, and a reader can
trace that development only with the log and the packages.

## Ideas & possible recommendations

- **Publish the materials.** The pilot log, task packages, G0 report and Elicit outputs could
  be published with persistent identifiers, for example as a Zenodo supplement.
- **State the version, or re-run the priority search.** Volume I could say which version the
  priority audit covered, or the search could be re-run on the current version with documented
  queries.
- **One vocabulary for the pilot.** Both volumes could use the same terms for the pilot and its
  reports, and define P0, G0 and C0/C1/C2.
- **A cheaper variant.** If some materials cannot be released, the claims that depend on them
  could be removed or marked as unsupported.

## Resolved when

- [ ] Every cited historical material is available at a stable link, or the claims that depend
      on it are removed.
- [ ] Both volumes use the same terms for the pilot and its reports.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures)
- Issues: MAJ-01, MAJ-07
