---
id: MIN-02
title: Truncated sentences in Volume I
severity: minor
area: editorial
volumes: I
sections: Vol I §12.3, §13.4, Ch. 18, Conclusion
review: Appendix A
status: open
---

# MIN-02 · Truncated sentences in Volume I

**Finding.** Four sentences in Volume I stop mid-clause. Two are the first copy of a
duplicated paragraph (MIN-01) whose revised version follows, which supports the reading that
two drafts were merged; the other two have no complete version anywhere in the volume.

## Evidence

- **§12.3, p. 54:** "For example, if models A and B differ on feature X, direct" (the
  paragraph is then repeated in full: "... direct observation of X is unavailable, but the
  models predict different changes in observable Y").
- **§13.4, p. 66:** the first copy of the "Probe example — close the loop" paragraph ends at
  "It is the influence of an acquired ground"; a revised copy of the paragraph follows.
- **Ch. 18, p. 81:** "Until these functions close into stable self-navigation relative to the
  Compass, AGI is not considered a formed AR. This intermediate state" ends the paragraph,
  with no complete copy elsewhere.
- **Conclusion, p. 90:** "it appears as a limiting engineering question: can a continuing
  Reason make internal renewal" breaks off, with no complete copy elsewhere.

Locate any of these with `python3 -I scripts/locate.py text/foundations-8.0.txt "<quote>"`.

## Why it matters

A truncated sentence in a definition or argument leaves the reader to guess the claim.

## Recommendation

Remove the truncated first copies and complete the remaining sentences.

## Resolved when

- [ ] No sentence in the next version ends mid-clause.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-01
