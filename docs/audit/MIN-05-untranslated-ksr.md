---
id: MIN-05
title: Untranslated abbreviation "KSR" and inconsistent RFL mode names
severity: minor
area: editorial
volumes: I, II
sections: Vol I §20.1.2; Vol II §26.0.3, §31.0, §33.A
review: Appendix A
status: open
---

# MIN-05 · Untranslated abbreviation "KSR" and inconsistent RFL mode names

**Finding.** The English text calls the formation scaffold the Reason Formation Loop (RFL),
but its experimental modes keep a different, undefined abbreviation, KSR (apparently the
Russian name of the loop), in `TRAINER_KSR`, `AUTO_KSR`, `NO_KSR`, `WITH_KSR`, `REDUCED_KSR` and
`DELAYED_KSR`. "KSR" occurs 6 times in Volume I and 26 times in Volume II, and is never
defined. Volume II also has the identifier `no_krs_status`, with the letters transposed, and names the
full-assistance mode `FULL_KSR` in the Chapter 31 field definition but `WITH_KSR` everywhere
else; Volume I's arms (`TRAINER_KSR`, `AUTO_KSR`, `NO_KSR`) are a different set with no mapping.

## Evidence

- **Vol I §20.1.2, p. 85:** "TRAINER_KSR: Formation States and assistance stages are generated
  by an external AI mentor; AUTO_KSR [...]; NO_KSR".
- **Vol II §26.0.3, p. 41:** `WITH_KSR`, `REDUCED_KSR`, `DELAYED_KSR`, `NO_KSR`.
- **Vol II §31.0, p. 79:** `no_krs_status`.
- **Vol II Ch. 31, p. 78:** "formation_support = FULL_KSR / REDUCED_KSR / DELAYED_KSR / NO_KSR".

## Why it matters

A reader of the English edition cannot connect KSR to the RFL without guessing, and an
implementation that follows the identifiers literally will carry the typo into code.

## Recommendation

Rename the modes `TRAINER_RFL`, `AUTO_RFL`, `NO_RFL` and so on, and correct the typo.

## Resolved when

- [ ] "KSR" no longer appears in the English editions, and `no_krs_status` is corrected.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-05, MED-20
