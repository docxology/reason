---
id: MED-38
title: The failure catalogue cannot be applied as a detector
severity: medium
area: safety
volumes: II
sections: Vol II §28.B, Ch. 29, Ch. 32, §32.1, §32.2, §32.12, §32.15, §32.18, §32.19, §32.20–§32.23, §32.25.A, §32.26, §32.31, §32.33, §32.47, §32.48, §32.56
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

Chapter 32 gives 57 failure cards and a declared log format for failure events (§32.2), and
§32.33 treats any capacity to delay stopping as a critical failure. That is substantial work.
The chapter calls itself an operational catalog and defines a failure point as an observable
state, but as written the catalogue is a taxonomy with responses and cannot yet detect
failures. No card uses the §32.1 severity labels (WARNING, DEGRADED and CRITICAL occur only in
§32.1), although §32.1 says that every failure point receives a severity level; §32.33 states
one in words. Triggers are verbal; the number of failed local corrections in §32.12 (K in
§28.B, where it is "set by profile") and L in §32.15 have no values; only five cards name a
Chapter 27 metric, so `trigger_metrics` is nearly empty; and 35 cards have no
recovery-condition section (§32.26 gives one set of control conditions for every failure, and
a few cards, such as §32.47 and §32.48, state a success criterion in a sentence). For
irreversible actions the two main action-safety cards fire only after the harm, and several
cards overlap.

## Evidence

- **Vol II §32.12, p. 89; §32.15, p. 91:** "After the specified number of failed local
  corrections, the system must raise correction_level :"; "After L windows without progress,
  the system must test the framing".
- **Vol II §32.19, p. 92:** "Actions regularly pass simulate , but actual consequences are
  substantially more dangerous than predicted." The thresholds are verbal.
- **Vol II §32.18, p. 92; §32.56, p. 100:** the sign is "Under high uncertainty, actions are
  permitted that cause irreversible harm or destroy the causal cycle"; the response is "The
  system immediately enters SAFE_MODE, reduces the action set and recovers from the last
  confirmed state." Nothing in §32.18 addresses harm already done outside the system, the
  situation that §32.56 covers under the title "False recovery through internal rollback".
- **Vol II §§32.20, 32.21, 32.31:** "Substitution of a local metric for the Compass" (§32.20,
  p. 93) and "Metric capture" (§32.21, p. 93) both describe optimizing a proxy, with different
  responses. "Capture of the Compass by a scalar metric" (§32.31, p. 97) is related but
  describes a different mechanism, in which "one aggregate quantity permits violation of a
  critical ground to be compensated by a high value on another"; its response is "disable
  aggregate authorization, restore vector assessment, test red lines and compare alternatives
  again".
- **Already in the text (Vol II §28.B, p. 55):** "Repeated failure after K corrections opens a
  higher level; K and the escalation rule are set by profile." The L rule appears there too
  (p. 56). The volume gives neither K nor L a value; the K of §29.0.1 (p. 68) is another
  quantity, the scale of conditional points.
- **Already in the text (Vol II §32.25.A, p. 95; Ch. 29, p. 66):** the rollback procedure
  restores working state from a snapshot and "reconciles it again with the current
  environment", and Chapter 29 states the limit itself: "Internal rollback restores the state
  of the computing system, while PostImpactAssessment preserves changes that have already
  occurred in the external world."
- **Already in the text (Vol II §32.26, p. 95):** "A failure is considered eliminated not when
  code or a model changes but after these control conditions are met". The eight conditions,
  among them "the error is not reproducible after correction" and "principal metrics return to
  an admissible range", apply to every failure.
- **Already in the text (Vol II §32.47, p. 99; §32.48, p. 99):** two of the 35 cards without a
  "Recovery condition" section end with a criterion of their own: "Success is discovery of new
  distinctions without growth in dangerous external trials." and "Success is a reduction in
  critical debt without stopping all current work."
- **Already in the text (Vol II §32.33, p. 97):** "Any capacity of the candidate to delay
  stopping [...] is a critical infrastructure failure."
- **Already in the text (Vol II §32.1, p. 85):** "Severity is determined not only by the magnitude
  of the current error but also by its reversibility, propagation into other loops and
  probability of losing recoverability", which explains why no card carries a fixed severity,
  though no rule maps those factors to a label.

## Why it matters

An unattended safety response (SAFE_MODE, autonomy restriction, ending a run) needs a trigger
that two implementations would apply the same way.

## Ideas & possible recommendations

- **One format for every card.** Each card could carry the same fields: severity, trigger
  metric, window, threshold, false-alarm budget and recovery condition, with K (§§28.B, 32.12)
  and L (§§28.B, 32.15) valued. A cheaper first step would be to do this only for the cards
  that guard irreversible actions.
- **Split bundled cards, merge overlapping ones.** The bundled cards (§§32.18, 32.22, 32.23)
  could be split, and overlapping cards merged or ranked; the two cards on optimizing a proxy
  (§§32.20, 32.21) are one candidate pair, and §32.31 (compensation by an aggregate score)
  could cross-refer to them.
- **A pre-action indicator for irreversible actions.** Risk-simulation calibration on
  reversible probes is one option, so that the card can fire before the harm and not only
  after it.
- **Link §32.18 to §32.56.** §32.18 could invoke the PostImpactAssessment (defined in Chapter
  29 and used in §32.56), since a rollback to the last confirmed state cannot undo irreversible
  harm already done outside the system.

## Resolved when

- [ ] Every card has severity, trigger metric, window, threshold and recovery condition in one
      format, with K (§§28.B, 32.12) and L (§§28.B, 32.15) valued.
- [ ] Overlapping cards are merged or ranked, and the cards for irreversible actions can fire
      before the harm occurs.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MED-24, MED-30, MED-36
