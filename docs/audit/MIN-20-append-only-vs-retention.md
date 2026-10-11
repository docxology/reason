---
id: MIN-20
title: The log is called append-only, but a retention policy allows deletion
severity: minor
area: definitions
volumes: II
sections: Vol II §21.A, Ch. 24, §29.A, §32.9, §32.25.A
review: Appendix A
status: open
github_issue: 66
---

# MIN-20 · The log is called append-only, but a retention policy allows deletion

**Finding.** Volume II calls its fact log append-only and says it is "neither rolled back nor
deleted", but it also provides a retention policy with "permitted deletion". The qualifier "within
a control series" reconciles the two in Chapter 24, §29.A and §32.9, but it is missing from §21.A,
where the log is introduced, and from §32.25.A, where the guarantee is invoked during rollback.
Read alone, those two passages promise what the retention policy withdraws.

## Evidence

- **Vol II §21.A, p. 13:** "An append-only log is created. Raw facts are not edited
  retrospectively;" with no scope stated.
- **Vol II Ch. 24, p. 19:** "Within a control series, source events remain immutable." The next
  sentence adds "Long-term operation has a retention policy: duration, volume, protected grounds,
  archiving and permitted deletion with the fact of loss recorded."
- **Vol II §29.A, p. 72, and §32.9, p. 88:** the invariants "cannot be canceled by the candidate
  within a control series: raw fact logs may not be rewritten", and "Source events from the
  control series may not be deleted; after the series, the preregistered retention policy applies
  (§23)." Chapter 23 contains no retention policy; the only statement of it is in Chapter 24.
- **Vol II §32.25.A, p. 95:** "The append-only fact log is neither rolled back nor deleted."

## Why it matters

The raw log underpins replay, rollback and audit. If the guarantee is unconditional in one place
and scoped in another, an implementer cannot tell whether deletion after a control series is
allowed.

## Recommendation

State the immutability scope once, in §21.A (immutable during a control series, afterwards only
under the preregistered retention policy, with the loss recorded), make §32.25.A and §29.A refer
to it, and point §32.9 to Chapter 24.

## Resolved when

- [ ] "Append-only" has one stated scope in §§21.A, 24, 29.A, 32.9 and 32.25.A, and the
      retention-policy pointer resolves.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MIN-04
