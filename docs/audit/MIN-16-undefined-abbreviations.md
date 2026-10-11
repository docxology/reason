---
id: MIN-16
title: Abbreviations and names are used without definition
severity: minor
area: definitions
volumes: I, II
sections: Vol I Key Definitions; Vol II title page, §21, §§24.B.2, 24.D, 24.D.1, 25.C, 26.C, §33.D, App. A.2
review: Appendix A
status: open
github_issue: 62
---

# MIN-16 · Abbreviations and names are used without definition

## Claims under review

- **Vol I Key Definitions, p. 13:** "AI (SI) - an artificial intelligent system capable of
  perceiving information [...] In the notation of this work, SI is used as an alternative label
  for the same class and does not constitute a separate developmental stage." and "ASI (ASR) -
  an artificial system at a superhuman level [...] In this work, ASI retains its meaning as a
  level of superhuman capability, while ASR is used as a more precise label for the case in
  which those capabilities belong to an already formed Artificial Reason."
- **Vol II title page, p. 9:** "TECHNOLOGY FOR CREATING ARTIFICIAL REASON AND SCALING TO ASI
  (ASR)";
  **Vol II §21, p. 13:** "This order defines the path AGI -> AR -> ASI / ASR."
- **Vol II A.2, p. 117:** "ASI / ASR denotes the superhuman scale of a formed Reason.";
  **Vol II §33.D, p. 112:** "Within the proposed path, ASI is scaled Artificial Reason".
- **Vol II §24.D.1, p. 28:** "For an irreversible external action, dependence on an untested
  overlay raises the verification class and may block ALLOW."

## Finding

As the passages above show, "SI" and "ASR" are never expanded in either volume, and ASR is also
the standard abbreviation for automatic speech recognition. Volume I gives ASI (a capability
level) and ASR (that level reached by a formed AR) different meanings but writes them as one
token, "ASI (ASR)", and Volume II treats them as one stage. Six Volume II names occur once,
with no definition or schema; one of them appears in a rule that can block an irreversible
action.

## Evidence

- **Vol II A.2, p. 117, and §33.D, p. 112:** both identify ASI/ASR with a scaled formed Reason
  (§33.D: "Within the proposed path, ASI is scaled Artificial Reason"). §33.D keeps two
  profiles, one for capabilities and one for preservation of the organization of Reason, says
  that "A high result in one profile does not replace the other", and says that until the
  profile is filled and verified "ASI remains a scaling objective rather than an assigned
  experimental status". A.2 names the two records `reason_organization_profile` and
  `capability_profile` and glosses both in one sentence; the identifiers occur nowhere else and
  neither has a schema. Neither section names a system that has ASI-level capabilities but an
  unverified organization of Reason.
- **Vol II, names that occur once:** "-> DialogueRequest" (§24.B.2, p. 23);
  "-> RetrievedFragment" (§24.D, p. 27); "ModelingWorkspaceSnapshot restored" (§26.C, p. 43);
  "integrate_consequences() has no right to attribute automatically" (§25.C, p. 38); "the
  current revision epoch" (§24.D.1, p. 29); and the "verification class" of §24.D.1, p. 28,
  quoted above.

## Why it matters

A reader cannot tell what ASR stands for, and the shared token hides a distinction Volume I
draws on purpose, between a capability level and a formed organization. An undefined
"verification class" that can block an irreversible action is a rule that an implementer has to
invent.

## Ideas & possible recommendations

- **Expand or drop SI and ASR.** Each abbreviation could be expanded once at first use, or
  dropped, which would also remove the clash with automatic speech recognition.
- **Keep ASI and ASR apart, or merge them explicitly.** The volumes could use ASI for the
  capability level and ASR only for that level reached by a formed AR, or state that the two
  are one and use a single term.
- **Define each Volume II name.** Each of the six names could be given a schema or glossary
  entry, or be removed; the two profile records `reason_organization_profile` and
  `capability_profile` could be given a schema that matches the two profiles of §33.D.

## Resolved when

- [ ] Every abbreviation is expanded at first use, and every name used in a rule or record has
      a definition.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-02, MED-35, MIN-15
