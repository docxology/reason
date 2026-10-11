---
id: MED-33
title: Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment
severity: medium
area: safety
volumes: I, II
sections: Vol I Ch. 13, §13.3, §14.3, §20.4, Conclusion; Vol II §28.C.3, §28.D, §29.C, §31.10
review: §4.3, §8
status: open
github_issue: 41
---

# MED-33 · Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment

## Claims under review

- **Vol II §28.C.3, p. 62:** "Within one transaction, simultaneous rewriting of the tested
  object and the sole criterion by which its versions are compared is prohibited."; "Every
  internal procedure thus remains potentially revisable, but each particular revision has a
  temporarily stable comparison point." **Vol I §13.3, p. 65:** "Safe general plasticity is
  implemented as a sequence of local changes with a temporarily stable point of comparison.";
  "if doubt concerns the assessment rule itself, that rule becomes the object of the next
  cycle, which relies on preserved context and independent consequences"
- **Vol I §20.4, p. 88:** "The technological hypothesis of the project is that AR capabilities
  can be scaled while preserving causal organization, the Compass, and openness to correction."
  **Vol I Conclusion, p. 89:** "It is retained as the best-found orientation and remains open
  to revision if a more fundamental and more coherent ground appears."
- **Vol II §29.C, p. 73:** "One AR is a full participant in such dialogue and provides its own
  model, but a change of the constitutive ground is formalized as a decision at the level of
  shared architecture and civilizational governance."
- **Vol I §14.3, p. 70:** "Mature Reason moves this function inside one continuing process: it
  replaces an erroneous ground while preserving the subject. In this sense, self-correction is
  a more precise alternative to coarse replacement of the carrier." **Vol I Ch. 13, p. 62:** "A
  closed loop can sustain a delusion if all tests inherit a shared defect."

## Finding

Revision is specified per transaction: the tested object and the criterion may not be rewritten
together. Nothing bounds a sequence of such steps. One transaction can revise a criterion and
the next the object it judges, and the Compass that scaling must preserve is itself open to
revision. The stated check, the council of §29.C, is external to the architecture. On the
converse risk, §14.3 says a persistent Reason can renew itself, yet Ch. 13 concedes that a
closed loop can sustain a shared-defect delusion, and no mechanism or test addresses a defect
that every available check shares.

## Evidence

- **Vol II §28.D, p. 64; §31.10, p. 82:** the guard is worded differently elsewhere: "one pass
  may not rewrite both the tested object and the rule by which its alternatives are compared";
  "The tested element and the sole criterion for evaluating it are not changed simultaneously
  within one transaction."
- **Already in the text (Vol II §31.10, p. 82):** requirements for "independent testing, a
  preserved control version, rollback, and transfer to new cases" rise with the level.

## Why it matters

Valid steps can add up to a change no step authorized, and a persistent system with no renewal
path can keep a shared defect. No A.4 test or defined metric tracks either over many revision
cycles.

## Ideas & possible recommendations

- **State what is held fixed.** The text could say which part of the Compass is held fixed
  under scaling, or that nothing internal is.
- **Bound cumulative change.** Cumulative change of criteria could be bounded by independent
  audit, and the guard could be given one wording (§28.D differs).
- **A council-disabled drift series.** A series with the council disabled could apply many
  validated revisions and measure movement from the original criteria.
- **An entrenchment case.** A case that only a restarted or differently formed instance can
  detect would address the converse risk; until it has been run, §14.3 could be marked a
  hypothesis.

## Resolved when

- [ ] The text states what is held fixed under scaling and bounds cumulative criterion change.
- [ ] A drift series over many validated revisions and an entrenchment test are specified.

## Related

- Review: [§4.3](../../REVIEW.md#43-toward-asi-no-path-is-given), [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-02, MED-08, MED-37
