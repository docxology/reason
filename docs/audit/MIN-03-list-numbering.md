---
id: MIN-03
title: Lists are numbered across sections or restart mid-list
severity: minor
area: editorial
volumes: I, II
sections: Vol I §12.8, A.3, A.4, A.5
review: Appendix A
status: open
---

# MIN-03 · Lists are numbered across sections or restart mid-list

**Finding.** Numbered lists in Volume I continue the numbering of the previous list instead
of restarting, apparently an artefact of the typesetting pipeline. The text then refers to
items by their intended numbers ("the first obligation", "items 15–16"), which do not match
what is printed.

## Evidence

- **§12.8, p. 60:** the six causal obligations are printed as items 6–11; the text refers to
  them as the first, second, and so on.
- **A.3, pp. 95–96:** the conditions are printed as items 12–18.
- **A.4, pp. 97–100:** the 37 proposed tests are printed as items 19–55.
- **A.5, pp. 100–105:** the references are printed as items 56–84.
- **Vol II §29.0.2, p. 70:** the cultivation cycle is numbered 1, 2 (run together in one
  paragraph) and then restarts as 1–4, so it reads as six steps with duplicate numbers.

## Why it matters

Every cross-reference into these lists becomes ambiguous (MIN-04), and readers cannot cite a
test or a reference unambiguously.

## Recommendation

Restart numbering in each list, and regenerate every cross-reference from labels rather than
typed numbers.

## Resolved when

- [ ] Each list starts at 1, and every reference to a list item resolves.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-04
