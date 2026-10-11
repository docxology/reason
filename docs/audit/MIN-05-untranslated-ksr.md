---
id: MIN-05
title: Untranslated abbreviation "KSR" and inconsistent RFL mode names
severity: minor
area: editorial
volumes: I, II
sections: Vol I Key Definitions, §20.1.2; Vol II §26.0.3, Ch. 31, §31.0, §33.A
review: Appendix A
status: open
github_issue: 51
---

# MIN-05 · Untranslated abbreviation "KSR" and inconsistent RFL mode names

## Passages under review

- **Vol I Key Definitions, p. 12:** "Reason Formation Loop (RFL) - a temporary guiding system
  that implements the function of pre-rational significance for an artificial candidate.";
  **Vol I §20.1.2, p. 85:** "TRAINER_KSR: Formation States and assistance stages are generated
  by an external AI mentor" and "The external or automatic RFL is then removed, and all
  candidates are tested on held-out new situations without current guiding assistance."
- **Vol II §26.0.3, p. 41:** "WITH_KSR - the full assistance ladder is available; [...]
  NO_KSR - the external RFL is disabled during the control series."
- **Vol II Ch. 31, p. 78:** "formation_support = FULL_KSR / REDUCED_KSR / DELAYED_KSR /
  NO_KSR"; **Vol II §31.0, p. 79:** "cognitive_capability_status self_navigation_status
  no_krs_status correction_transfer_status"

## Finding

The English text calls the formation scaffold the Reason Formation Loop (RFL), but its
experimental modes keep a different, undefined abbreviation, KSR (apparently the Russian name
of the loop), in `TRAINER_KSR`, `AUTO_KSR`, `NO_KSR`, `WITH_KSR`, `REDUCED_KSR` and
`DELAYED_KSR`. "KSR" occurs 6 times in Volume I and 26 times in Volume II, and is never
defined. Volume II also has the identifier `no_krs_status`, with the letters transposed, and
names the full-assistance mode `FULL_KSR` in the Chapter 31 field definition but `WITH_KSR`
everywhere else; Volume I's arms (`TRAINER_KSR`, `AUTO_KSR`, `NO_KSR`) are a different set with
no mapping.

## Evidence

- The abbreviation occurs 6 times in Vol I, all in §20.1.2 (p. 85), and 26 times in Vol II.
  Reproduce with `rg -o KSR text/foundations-8.0.txt | wc -l` and the same command on
  `text/engineering-3.5.txt`.
- The two volumes share one mode name. Vol I tests three arms (`TRAINER_KSR`, `AUTO_KSR`,
  `NO_KSR`) and Vol II four modes (`WITH_KSR`, `REDUCED_KSR`, `DELAYED_KSR`, `NO_KSR`), with
  `FULL_KSR` in the Chapter 31 definition of `formation_support`.

## Why it matters

A reader of the English edition cannot connect KSR to the RFL without guessing, and an
implementation that follows the identifiers literally will carry the typo into code.

## Ideas & possible recommendations

- **Rename the modes after the RFL.** `TRAINER_RFL`, `AUTO_RFL`, `NO_RFL` and so on, in both
  volumes, would make the identifiers match the name the English text uses for the loop.
- **Correct the typo.** `no_krs_status` has the letters of the abbreviation transposed, and
  could be corrected in the same pass as the rename.
- **State how the two mode sets relate.** A short table could map the three arms of Vol I to
  the modes of Vol II, and one name could be used for the full-assistance mode instead of both
  `WITH_KSR` and `FULL_KSR`.
- **Define KSR if the identifiers stay.** A one-line definition next to the RFL entry in the
  Key Definitions would at least remove the guesswork.

## Resolved when

- [ ] "KSR" is either gone from the English editions or defined where it is first used, and
      `no_krs_status` is corrected.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-05, MED-20
