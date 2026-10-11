---
id: MED-15
title: The text is revised faster than evidence accumulates
severity: medium
area: provenance
volumes: I, II
sections: Zenodo concept records 17957561 and 22975036; Vol I title page, Common Rules, A.2; Vol II title page
review: §7, §9, §10.1
status: open
github_issue: 23
---

# MED-15 · The text is revised faster than evidence accumulates

## Claims under review

- **Vol I title page, p. 8:** "Version 8.0"; "Causal-process and experimentally oriented
  edition"; "Date: October 10, 2026".
- **Vol II title page, p. 9:** "Version: 3.5"; "Edition date: October 10, 2026"; "Causal
  foundation: Foundations of Reason, Volume I, version 8.0".

## Finding

The two title pages above fix the reviewed versions: Volume I version 8.0 and Volume II version
3.5, both dated 10 October 2026. The Volume I concept record on Zenodo holds 38 records.
Thirty-one are the main text: 19 distinct revisions, most uploaded separately in English and
Russian. The other seven are spin-off documents (an engineering volume, a one-page specification,
a popular introduction, *Deriving AGI From First Principles*, *The Core of Reason 6.7*). The
earliest record was created on 16 December 2025, so the series spans about ten months; the record
labelled v1.4r carries a publication date of 10 January 2025, but Zenodo created it on 10
January 2026, which looks like a year typed wrongly. Seven numbered revisions, 6.0 through 8.0
(the last being the reviewed Volume I), appeared in the 55 days from 15 August to 9 October 2026,
and the Zenodo title changed at nearly every revision from 4.5 on: from *A Structural Stability
Model for Autonomous Systems and AI Alignment*, through *A Process-Based Model of Life, Reason,
and AGI* and *Minimal Architecture of ASI*, to *Superintelligence Technology (ASI)*. Volume II
went from v2.4 to v3.5 in thirteen days. Appendix A.2 gives a short history of selected
revisions (2.1R, 5.8H, 7.0) and says the Compass Phrase is primary "in the present revision"; it
does not itemise the changes in 7.2, 7.5 or 8.0. The documented 7.0 changes add experimental
distinctions rather than remove them, and the Common Rules state that "Both volumes are revised
according to" the results of the first discriminating series (Common Rules, p. 92). But the
reviewed versions report no comparative data (MAJ-01), so these are revisions of the theory, not
responses to results.

## Evidence

- `notes/zenodo-history.md`, generated from the Zenodo REST API by `scripts/zenodo_history.py`:
  every record with its creation and publication dates, version label, title and license.
- Zenodo record 18208467 (labelled 1.4r): created 2026-01-10, publication date 2025-01-10.
- **Already in the text (Vol I A.2, p. 94):** "Revision 7.0 preserves separation of definitions,
  philosophical justification, and implementation testing, permits functional substitutions,
  and specifies experimental distinctions."; "Some older reports analyze the Compass as
  Life-Truth-Diversity. In the present revision, the Compass Phrase is primary [...]
  Conclusions about the earlier operational scheme must therefore be interpreted in relation to
  what has changed."
- **Already in the text (Vol I Common Rules, p. 92):** "The program of the first discriminating
  series is given in Appendix A.4. Both volumes are revised according to its results."
- The license also changed: the first 30 records were CC BY-NC-ND 4.0; records from 31 August
  2026 onward, including both reviewed volumes, are CC BY-NC 4.0.

## Why it matters

Each revision without new data moves the target for reviewers and makes it harder to cite the
work or know which version a criticism applies to. It is also how a research programme comes
to absorb objections rather than results: in Lakatos's terms, a protective belt that grows by
revision rather than by tested prediction.

## Ideas & possible recommendations

- **Freeze the reviewed versions.** Both volumes could be held at the reviewed versions, with the
  next revision made only after the first comparative series has run (see MAJ-01).
- **Attach a change log.** Each revision could carry a log that maps every change to the
  evidence or review comment that prompted it.
- **Correct the Zenodo date.** The publication date of the v1.4r record (18208467) could be
  corrected to match its creation date.

## Resolved when

- [ ] The next version is tied to new evidence and carries a change log.
- [ ] The Zenodo metadata dates are consistent with the records' creation dates.

## Related

- Review: [§7](../../REVIEW.md#weakest), [§9](../../REVIEW.md#9-scientific-status)
- Issues: MAJ-01, MIN-09 (titles and dates)
