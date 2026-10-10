---
id: MED-33
title: Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment
severity: medium
area: safety
volumes: I, II
sections: Vol I Ch. 13, §13.3, §14.3, §20.4, Conclusion; Vol II §28.C.3, §28.D, §29.C, §31.10
review: §4.3, §8
status: open
---

# MED-33 · Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment

**Finding.** Revision is specified per transaction: the tested object and the criterion may
not be rewritten together. Nothing bounds a sequence of such steps. One transaction can revise
a criterion and the next the object it judges, and the Compass that scaling must preserve is
itself open to revision. The stated check, the council of §29.C, is external to the
architecture. On the converse risk, §14.3 says a persistent Reason can renew itself, yet Ch.
13 concedes that a closed loop can sustain a shared-defect delusion, and no mechanism or test
addresses a defect that every available check shares.

## Evidence

- **Vol I §13.3, p. 65:** "The object under test and the rule by which it is assessed are
  changed in successive cycles; if doubt concerns the assessment rule itself, that rule becomes
  the object of the next cycle"
- **Vol II §28.C.3, p. 62:** "Within one transaction, simultaneous rewriting of the tested
  object and the sole criterion by which its versions are compared is prohibited."
- **Vol I §20.4, p. 88; Conclusion, p. 89:** scaling is to preserve "causal organization,
  the Compass, and openness to correction"; the Compass "remains open to revision if a more
  fundamental and more coherent ground appears".
- **Vol I §14.3, p. 70; Ch. 13, p. 62:** "Mature Reason moves this function inside one
  continuing process"; "A closed loop can sustain a delusion if all tests inherit a shared
  defect."
- **Already in the text (Vol II §31.10, p. 82):** requirements for "independent testing, a
  preserved control version, rollback, and transfer to new cases" rise with the level.

## Why it matters

Valid steps can add up to a change no step authorized, and a persistent system with no
renewal path can keep a shared defect. No A.4 test or defined metric tracks either over many
revision cycles.

## Recommendation

State which part of the Compass is held fixed under scaling, or that nothing internal is.
Bound cumulative change of criteria with independent audit, and give the guard one wording
(§28.D differs). Run a council-disabled series that applies many validated revisions and
measures movement from the original criteria, plus an entrenchment case that only a restarted
or differently formed instance can detect. Mark §14.3 a hypothesis until then.

## Resolved when

- [ ] The text states what is held fixed under scaling and bounds cumulative criterion change.
- [ ] A council-disabled drift series and an entrenchment test are specified.

## Related

- Review: [§4.3](../../REVIEW.md#43-toward-asi-no-path-is-given), [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-02, MED-08, MED-37
