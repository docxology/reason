---
id: MIN-02
title: Truncated sentences in Volume I
severity: minor
area: editorial
volumes: I
sections: Vol I §12.3, §13.4, Ch. 18, Conclusion
review: Appendix A
status: open
github_issue: 48
---

# MIN-02 · Truncated sentences in Volume I

## Passages under review

- **Vol I §12.3, p. 54:** "For example, if models A and B differ on feature X, direct"
- **Vol I §13.4, p. 66:** "In the next episode the probe uses this change without renewed
  prompting. It is the influence of an acquired ground"
- **Vol I Ch. 18, p. 81:** "Until these functions close into stable self-navigation relative
  to the Compass, AGI is not considered a formed AR. This intermediate state"
- **Vol I Conclusion, p. 90:** "Immortality of an organism is not postulated here as an
  achieved result; it appears as a limiting engineering question: can a continuing Reason make
  internal renewal"

## Finding

Four sentences in Volume I, quoted above, stop mid-clause. Two are the first copy of a
duplicated paragraph (MIN-01) whose revised version follows, which supports the reading that
two drafts were merged; the other two have no complete version anywhere in the volume.

## Evidence

- **Vol I §12.3, p. 54:** the paragraph is then repeated in full: "[...] direct observation of
  X is unavailable, but the models predict different changes in observable Y, Intelligence can
  construct a test through Y."
- **Vol I §13.4, p. 66:** the revised copy of the "Probe example — close the loop" paragraph
  follows and ends: "It is the influence of the acquired ground on subsequent operation,
  including selection of the test, that distinguishes completed correction from an isolated
  successful answer."
- **Vol I Ch. 18, p. 81:** the next paragraph opens with a different sentence, "The
  technological path of the project therefore does not consist in simple scaling of AI (SI) →
  AGI → ASI."; the cut-off sentence has no complete copy elsewhere in the volume.
- **Vol I Conclusion, p. 90:** the next paragraph opens "The result of this work is a set of
  fundamental foundations for the technology of AR [...]"; the cut-off sentence has no complete
  copy elsewhere in the volume.

Locate any of these with `python3 -I scripts/locate.py text/foundations-8.0.txt "<quote>"`.

## Why it matters

A truncated sentence in a definition or argument leaves the reader to guess the claim.

## Ideas & possible recommendations

- **Remove the truncated first copies.** In §12.3 and §13.4 a complete, revised copy of the
  paragraph follows, so deleting the cut-off copy would settle both (see MIN-01).
- **Complete the two remaining sentences.** In Chapter 18 and the Conclusion no complete
  version exists, so the author would need to supply the end of each sentence.
- **Check paragraph endings before release.** A scripted test for body paragraphs that end
  without closing punctuation would flag all four passages, along with some table cells and
  headings that it would have to skip.

## Resolved when

- [ ] No sentence in the next version ends mid-clause.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-01
