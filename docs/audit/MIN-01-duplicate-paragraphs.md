---
id: MIN-01
title: Near-duplicate paragraphs in Volume I
severity: minor
area: editorial
volumes: I
sections: Vol I Abstract, Ch. 5, §9.3, §11.1, §12.3, §12.4, §12.5, §12.9, §13.3, §13.4, Ch. 15, Ch. 16, Ch. 17
review: Appendix A
status: open
github_issue: 47
---

# MIN-01 · Near-duplicate paragraphs in Volume I

## Passages under review

- **Vol I Abstract, p. 8:** "The technological hypothesis is that available mechanisms of
  Intelligence can be organized into a causally closed cycle: current state → significant gap →
  alternatives → discriminating test → evidence → revision of grounds → action → consequences →
  next state." The next paragraph restates it: "The technological hypothesis is that available
  intellectual mechanisms can be organized into a causally closed cycle: current state →
  significant insufficiency of a ground → required distinction → alternatives → discriminating
  test → evidence → revision of the ground → action → consequences → next state."
- **Vol I §12.9, p. 61:** "Priorities determine urgency and admissibility of continuation. The
  Core opens the gap [...] Intelligence constructs versions and available tests. The Modeling
  Environment maintains their different expectations:" The next paragraph reads: "Priorities
  determine urgency and whether continuation is admissible. The Core opens the gap [...]
  Intelligence constructs versions and available tests. The Modeling Environment holds their
  differing expectations:"
- **Vol I Ch. 17, p. 77:** "civilization preserves authorship and the causal trace of
  significant contribution, linking recognition, learning, and additional resources to
  verifiable useful results"; **Vol I Ch. 17, p. 78:** "civilization preserves authorship and
  the causal trace of significant contribution, connecting recognition, learning, and
  additional resources with verifiable useful results".

## Finding

Volume I prints at least a dozen paragraphs twice in slightly different wording, usually one
directly after the other, as if two edit or translation passes had been merged without removing
the older copy. The passages above are three of them. An automated check
(`repro/dup_paragraphs.py`: paragraphs over 120 characters, `difflib` similarity above 0.80
within a window of three) confirms eleven pairs; the Abstract's repeated statement of the
technological hypothesis and the truncated first copies in §12.3, §13.4 and Chapter 18 (MIN-02)
are further instances. The same check finds none in Volume II.

## Evidence

| Similarity | Location (first copy) | Opening words |
|---|---|---|
| 0.87 | Ch. 5, p. 32 | "Procedural memory preserves learned rules of prioritization" |
| 0.86 | §9.3, p. 43 | "Intelligence constructs hypotheses and alternative" |
| 0.87 | §11.1, p. 50 | "The Worldview is a long-term causal-semantic" |
| 0.89 | §12.4, p. 55 | "Selection of an investigative approach begins with experience" |
| 0.91 | §12.5, p. 57 | "Values are formed and refined during the life of the system" |
| 0.98 | §13.3, p. 65 | "Procedural plasticity changes the way of thinking" |
| 0.90 | Ch. 15, p. 73 | "The strength of ethics is simultaneously its limit" |
| 0.99 | Ch. 15, p. 73 | "After the Compass appears, ethics remains in practical navigation" |
| 0.91 | Ch. 16, p. 75 | "Reason operates in an environment that cannot be" (chapter opening) |
| 0.91 | Ch. 16, p. 75 | "The process view allows a working map of scientific levels" |
| 0.82 | Ch. 17, p. 77 | "Coordinated autonomy preserves an environment" |

In each case the second copy follows within a few lines. Reproduce with
`python3 -I repro/dup_paragraphs.py text/foundations-8.0.txt`.

Reading the text rather than thresholding it finds more: seven pairs in the front matter and
Chapters 1–10 (including two drafts of the Abstract's technological hypothesis and an orphan
fragment at the end of the Chapter 8 conclusion) and twenty in Chapters 11–20, which add §11.4
(p. 52), §12.7 (p. 59), §12.9 (p. 61), §20.2 (p. 86) and a doubled list item in Chapter 17
(pp. 77–78) to the table above. The raw locations are in `notes/audit-raw/V1A.md` (V1A-38) and
`notes/audit-raw/V1B.md` (V1B-29).

## Why it matters

Readers meet the same idea twice in different words and must work out whether the
difference is meaningful. It lengthens the volume and signals that the text has not had a
final editorial pass, which lowers reviewers' confidence in the rest.

## Ideas & possible recommendations

- **Keep one copy of each pair.** The later, fuller copy is usually the better one to keep.
  Where the two copies differ in substance, as in the two statements of the technological
  hypothesis in the Abstract, the author would choose the wording he intends.
- **Run a similarity check before each release.** A check such as `repro/dup_paragraphs.py`
  could be run on every release candidate, so that a merge of drafts that leaves both copies in
  place is caught before publication.

## Resolved when

- [ ] `repro/dup_paragraphs.py` reports no pairs above 0.80 for the next version.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-02, MED-20
