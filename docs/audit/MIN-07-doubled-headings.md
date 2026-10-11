---
id: MIN-07
title: Headings printed twice and lists collapsed
severity: minor
area: editorial
volumes: I
sections: Vol I Contents, Key Definitions, Part II, Ch. 16, Open Research Directions
review: Appendix A
status: open
github_issue: 53
---

# MIN-07 · Headings printed twice and lists collapsed

## Passages under review

- **Vol I Contents, p. 9:** "CONTENTS" followed by "CONTENTS Introduction Key Definitions of
  the Model [...]".
- **Vol I Key Definitions, p. 11:** "KEY DEFINITIONS OF THE MODEL" followed by "KEY DEFINITIONS
  OF THE MODEL Life - an autonomous physical process [...]".
- **Vol I Part II, p. 26:** "PART II. FROM LIFE TO REASON: FUNCTIONAL TRANSITIONS" alone at
  the foot of the page; **Vol I Part II, p. 27:** "PART II. FROM LIFE TO REASON: FUNCTIONAL
  TRANSITIONS The transitions in this part are built on the principle of inheritance of
  results."
- **Vol I Open Research Directions, p. 91:** "OPEN RESEARCH DIRECTIONS" followed by "OPEN
  RESEARCH DIRECTIONS The model of Reason provides a common foundation for further research in
  [...]".

## Finding

Several headings in Volume I are printed twice, either on one line or on consecutive pages,
apparently from the same merge of drafts that produced the duplicate paragraphs.

## Evidence

- **Ch. 16, p. 75:** the chapter heading "Chapter 16. Science and Self-Correction" is repeated
  with its opening paragraph (see MIN-01).
- **Operational Core, p. 14:** "OPERATIONAL CORE OF THE MODEL" is repeated as the first words
  of the following paragraph, and the map's items 1–6 are set as headings while item 7 is body
  text.
- **Part II, p. 27:** the arrow chain "observation → memory → patterns and procedures → [...]"
  is printed twice in consecutive boxes, and the second box swallows the next paragraph.
- **§20.3, p. 87:** the heading absorbs its first sentence ("Four events are distinguished:"
  appears twice) and the four-item list collapses into one run-in paragraph; in Chapter 17
  (pp. 77–78) a list of principles starts with a stray dash and repeats one item.

## Why it matters

Minor on its own, but together with MIN-01 and MIN-02 it signals an unedited text.

## Ideas & possible recommendations

- **Remove the repeated headings.** The editorial pass proposed in MED-20 could delete each
  repeated heading.
- **Restore the collapsed lists.** In the same pass, the list items that run together (§20.3,
  item 7 of the Operational Core map, and the principles in Chapter 17) could be set as
  separate items.
- **Check for repeated headings mechanically.** A script that flags a heading reappearing as
  the first words of the text below it finds the Contents, Key Definitions and Open Research
  Directions cases, and could run beside the similarity check proposed in MIN-01.

## Resolved when

- [ ] No heading is printed twice in the next version.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-01, MED-20
