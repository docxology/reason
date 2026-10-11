---
id: MED-15
title: The text is revised faster than evidence accumulates
severity: medium
area: provenance
volumes: I, II
sections: Zenodo concept records 17957561 and 22975036; Vol I A.2
review: §7, §9, §10.1
status: open
github_issue: 23
---

# MED-15 · The text is revised faster than evidence accumulates

**Finding.** The Volume I concept record on Zenodo holds 38 records. Thirty-one are the main
text: 19 distinct revisions, most uploaded separately in English and Russian. The other seven
are spin-off documents (an engineering volume, a one-page specification, a popular
introduction, "Deriving AGI From First Principles", "The Core of Reason 6.7"). The earliest
record was created on 16 December 2025, so the series spans about ten months; the record
labelled v1.4r carries a publication date of 10 January 2025, but Zenodo created it on 10
January 2026, which looks like a year typed wrongly. Seven numbered revisions, 6.0 through
8.0, appeared in the 55 days before the reviewed versions, and the Zenodo title changed at
nearly every revision from 4.5 on: from "A Structural Stability Model for Autonomous Systems
and AI Alignment", through "A Process-Based Model of Life, Reason, and AGI" and "Minimal
Architecture of ASI", to "Superintelligence Technology (ASI)". Volume II went from v2.4 to
v3.5 in thirteen days. The text discloses what changed between revisions, and the changes
documented since 7.0 add experimental distinctions rather than remove them. But the reviewed
versions report no comparative data (MAJ-01), so these are revisions of the theory, not
responses to results.

## Evidence

- `notes/zenodo-history.md`, generated from the Zenodo REST API by `scripts/zenodo_history.py`:
  every record with its creation and publication dates, version label, title and license.
- Zenodo record 18208467 (labelled 1.4r): created 2026-01-10, publication date 2025-01-10.
- **Already in the text (Vol I A.2, p. 94):** "Some older reports analyze the Compass as
  Life-Truth-Diversity. In the present revision, the Compass Phrase is primary [...]
  Conclusions about the earlier operational scheme must therefore be interpreted in relation
  to what has changed."
- The license also changed: the first 30 records were CC BY-NC-ND 4.0; records from 31 August
  2026 onward, including both reviewed volumes, are CC BY-NC 4.0.

## Why it matters

Each revision without new data moves the target for reviewers and makes it harder to cite the
work or know which version a criticism applies to. It is also how a research programme comes
to absorb objections rather than results: in Lakatos's terms, a protective belt that grows by
revision rather than by tested prediction.

## Recommendation

Freeze both volumes at the reviewed versions, make the next revision only after the first
comparative series has run, and attach a change log that maps each change to the evidence or
review comment that prompted it. Correct the publication date of the v1.4r record.

## Resolved when

- [ ] The next version is tied to new evidence and carries a change log.
- [ ] The Zenodo metadata dates are consistent with the records' creation dates.

## Related

- Review: [§7](../../REVIEW.md#weakest), [§9](../../REVIEW.md#9-scientific-status)
- Issues: MAJ-01, MIN-09 (titles and dates)
