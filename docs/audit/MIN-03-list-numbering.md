---
id: MIN-03
title: Lists are numbered across sections or restart mid-list
severity: minor
area: editorial
volumes: I, II
sections: Vol I §12.8, A.3, A.4, A.5; Vol II §29.0.2
review: Appendix A
status: open
github_issue: 49
---

# MIN-03 · Lists are numbered across sections or restart mid-list

## Passages under review

- **Vol I §12.8, p. 59:** "In the minimal working scheme, six causal obligations are
  distinguished:"; **Vol I §12.8, p. 60:** "6. Current distinction: obtain information relevant
  to the environment and the system itself while preserving significant uncertainty. [...]
  11. Revision of a ground: change an erroneous model or the method by which it is constructed
  and preserve the tested change." Below the list the text says "The Worldview belongs
  primarily to the second obligation; conscious integration to the first and to coordination of
  the current state".
- **Vol I A.3, p. 96:** "12. Tested capability: which result must persist and under which new
  conditions."; **Vol I A.4, p. 97:** "19. Cost of error and depth."; **Vol I A.5, p. 100:**
  "56. Varela, F. G., Maturana, H. R., Uribe, R. (1974)." These are the first items printed in
  the three appendix lists.
- **Vol II §29.0.2, p. 70:** "1. The simulation presents a situation and alternatives under
  limited data." and, in the same paragraph, "2. The training AI or dialogue participant may
  first provide a Formation State [...]"; the list then starts again with "1. The simulation
  reveals consequences and available discriminating evidence."

## Finding

Numbered lists in Volume I continue the numbering of the previous list instead of restarting,
apparently an artefact of the typesetting pipeline. The text then refers to items by their
intended numbers (the "second obligation" in §12.8, "items 15–16" in §7.2), which do not match
what is printed.

## Evidence

- **Vol I §12.8, p. 60:** the six causal obligations are printed as items 6–11; the text refers
  to them as the first, second, and so on.
- **Vol I A.3, pp. 95–96:** the conditions are printed as items 12–18.
- **Vol I A.4, pp. 97–100:** the 37 proposed tests are printed as items 19–55.
- **Vol I A.5, pp. 100–105:** the references are printed as items 56–84.
- **Vol II §29.0.2, p. 70:** the cultivation cycle is numbered 1, 2 (run together in one
  paragraph) and then restarts as 1–4, so it reads as six steps with duplicate numbers.

## Why it matters

Every cross-reference into these lists becomes ambiguous (MIN-04), and readers cannot cite a
test or a reference unambiguously.

## Ideas & possible recommendations

- **Restart the numbering in each list.** Each list would then run from 1, which is the
  numbering the text's own references assume (MIN-04 gives the mapping).
- **Generate cross-references from labels.** References to list items could be produced from
  stable labels instead of typed numbers, so that they stay correct when a list changes.

## Resolved when

- [ ] The printed number of each list item matches the number the text uses for it, and every
      reference to a list item resolves.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-04
