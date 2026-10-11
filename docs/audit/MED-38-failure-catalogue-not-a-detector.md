---
id: MED-38
title: The failure catalogue cannot be applied as a detector
severity: medium
area: safety
volumes: II
sections: Vol II Ch. 32, §32.1, §32.2, §32.12, §32.15, §32.18, §32.19, §32.20–§32.23, §32.31, §32.33, §32.56
review: §8
status: open
github_issue: 46
---

# MED-38 · The failure catalogue cannot be applied as a detector

## Claims under review

- **Vol II Ch. 32 introduction, p. 84:** "The chapter is organized as an operational catalog
  rather than a linear narrative." It then defines its subject: "A failure point is an
  observable state in which one or more system loops cease to perform their function or create
  the appearance of improvement without an actual increase in correspondence with reality."
- **Vol II §32.1, p. 85:** "Every failure point receives a severity level:"
- **Vol II §32.2, p. 85:** "Every failure event is written to the log as a separate object:
  [...] severity [...] trigger_metrics [...] recovery_conditions [...]"

## Finding

Chapter 32 gives 57 failure cards in a declared event format (§32.2), and §32.33 treats any
capacity to delay stopping as a critical failure. That is substantial work. The chapter calls
itself an operational catalog and defines a failure point as an observable state, but as
written the catalogue is a taxonomy with responses and cannot yet detect failures. No card
states a severity, although §32.1 says that every failure point receives one (WARNING,
DEGRADED and CRITICAL occur only in §32.1); triggers are verbal; K and L have no values; only
five cards name a Chapter 27 metric, so `trigger_metrics` is nearly empty; and 35 cards have no
recovery condition. For irreversible actions the two main action-safety cards fire only after
the harm, and several cards overlap.

## Evidence

- **Vol II §32.12, p. 89; §32.15, p. 91:** "After the specified number of failed local
  corrections, the system must raise correction_level :"; "After L windows without progress,
  the system must test the framing".
- **Vol II §32.19, p. 92:** "Actions regularly pass simulate , but actual consequences are
  substantially more dangerous than predicted." The thresholds are verbal.
- **Vol II §32.18, p. 92; §32.56, p. 100:** the sign is "Under high uncertainty, actions are
  permitted that cause irreversible harm or destroy the causal cycle"; the response
  "recovers from the last confirmed state" restores internal state only, the case §32.56 titles
  "False recovery through internal rollback".
- **Vol II §§32.20, 32.21, 32.31:** "Substitution of a local metric for the Compass" (§32.20,
  p. 93), "Metric capture" (§32.21, p. 93) and "Capture of the Compass by a scalar metric"
  (§32.31, p. 97) all describe optimizing a proxy, with three different responses.
- **Already in the text (Vol II §32.33, p. 97):** "Any capacity of the candidate to delay
  stopping [...] is a critical infrastructure failure."

## Why it matters

An unattended safety response (SAFE_MODE, autonomy restriction, ending a run) needs a trigger
that two implementations would apply the same way.

## Ideas & possible recommendations

- **One format for every card.** Each card could carry the same fields: severity, trigger
  metric, window, threshold, false-alarm budget and recovery condition, with K and L valued. A
  cheaper first step would be to do this only for the cards that guard irreversible actions.
- **Split bundled cards, merge overlapping ones.** The bundled cards (§§32.18, 32.22, 32.23)
  could be split, and overlapping cards merged or ranked; the three cards on optimizing a proxy
  (§§32.20, 32.21, 32.31) are one candidate group.
- **A pre-action indicator for irreversible actions.** Risk-simulation calibration on
  reversible probes is one option, so that the card can fire before the harm and not only
  after it.
- **Link §32.18 to §32.56.** §32.18 could invoke the PostImpactAssessment of §32.56, since the
  internal rollback it prescribes restores internal state only.

## Resolved when

- [ ] Every card has severity, trigger metric, window, threshold and recovery condition in one
      format, with K and L valued.
- [ ] Overlapping cards are merged or ranked, and the cards for irreversible actions can fire
      before the harm occurs.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MED-24, MED-30, MED-36
