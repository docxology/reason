---
id: MIN-16
title: Abbreviations and names are used without definition
severity: minor
area: definitions
volumes: I, II
sections: Vol I Key Definitions; Vol II title page, §21, §§24.B.2, 24.D, 25.C, 26.C, §33.D, App. A.2
review: Appendix A
status: open
github_issue: 62
---

# MIN-16 · Abbreviations and names are used without definition

**Finding.** "SI" and "ASR" are never expanded in either volume, and ASR is also the standard
abbreviation for automatic speech recognition. Volume I gives ASI (a capability level) and ASR
(that level reached by a formed AR) different meanings but writes them as one token, "ASI (ASR)",
and Volume II treats them as one stage. Six Volume II names occur once, with no definition or
schema.

## Evidence

- **Vol I Key Definitions, p. 13:** "AI (SI) - an artificial intelligent system capable of
  perceiving information" and "ASI (ASR) - an artificial system at a superhuman level", with "ASR
  is used as a more precise label for the case in which those capabilities belong to an already
  formed Artificial Reason."
- **Vol II title page, p. 9, and §21, p. 13:** "TECHNOLOGY FOR CREATING ARTIFICIAL REASON AND
  SCALING TO ASI (ASR)"; "This order defines the path AGI -> AR -> ASI / ASR."
- **Vol II A.2, p. 117, and §33.D, p. 112:** "ASI / ASR denotes the superhuman scale of a formed
  Reason." and "ASI is scaled Artificial Reason" leave no way to express an ASI that is not an AR.
  A.2 also names `reason_organization_profile` and `capability_profile`, which occur nowhere else.
- **Vol II, names that occur once:** "-> DialogueRequest" (§24.B.2, p. 23); "-> RetrievedFragment"
  (§24.D, p. 27); "ModelingWorkspaceSnapshot restored" (§26.C, p. 43); "integrate_consequences()
  has no right to attribute automatically" (§25.C, p. 38); "raises the verification class and may
  block ALLOW" (§24.D.1, p. 28); "the current revision epoch" (§24.D.1, p. 29).

## Why it matters

A reader cannot tell what ASR stands for, and the shared token hides a distinction Volume I draws
on purpose, between a capability level and a formed organization. An undefined "verification
class" that can block an irreversible action is a rule that an implementer has to invent.

## Recommendation

Expand SI and ASR once or drop them, keep ASI and ASR separate or merge them explicitly, and
define each Volume II name, including the two profile records, in a schema or glossary entry, or
remove it.

## Resolved when

- [ ] Every abbreviation is expanded at first use, and every name used in a rule or record has a
      definition.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MAJ-02, MED-35, MIN-15
