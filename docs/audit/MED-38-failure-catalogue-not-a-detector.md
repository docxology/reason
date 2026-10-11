---
id: MED-38
title: The failure catalogue cannot be applied as a detector
severity: medium
area: safety
volumes: II
sections: Vol II §32.1, §32.2, §32.12, §32.15, §32.18, §32.19, §32.20–§32.23, §32.31, §32.33, §32.56
review: §8
status: open
github_issue: 46
---

# MED-38 · The failure catalogue cannot be applied as a detector

**Finding.** Chapter 32 gives 57 failure cards in a declared event format (§32.2), and §32.33
treats any capacity to delay stopping as a critical failure. That is substantial work. As
written, the catalogue is a taxonomy with responses and cannot yet detect failures. No card
states a severity (WARNING, DEGRADED and CRITICAL occur only in §32.1); triggers are verbal; K
and L have no values; only five cards name a Chapter 27 metric, so `trigger_metrics` is nearly
empty; and 35 cards have no recovery condition. For irreversible actions the two main
action-safety cards fire only after the harm, and several cards overlap.

## Evidence

- **Vol II §32.1, p. 85:** "Every failure point receives a severity level:" followed by
  WARNING, DEGRADED and CRITICAL, which appear in no card.
- **Vol II §32.12, p. 89; §32.15, p. 91:** "After the specified number of failed local
  corrections, the system must raise correction_level :"; "After L windows without progress,
  the system must test the framing".
- **Vol II §32.19, p. 92:** "Actions regularly pass simulate , but actual consequences are
  substantially more dangerous than predicted." The thresholds are verbal.
- **Vol II §32.18, p. 92; §32.56, p. 100:** the sign is "Under high uncertainty, actions are
  permitted that cause irreversible harm or destroy the causal cycle"; the response
  "recovers from the last confirmed state" restores internal state only, the case §32.56 titles
  "False recovery through internal rollback".
- **Vol II §§32.20, 32.21, 32.31, pp. 93, 97:** "Substitution of a local metric for the
  Compass", "Metric capture" and "Capture of the Compass by a scalar metric" all describe
  optimizing a proxy, with three different responses.
- **Already in the text (Vol II §32.33, p. 97):** "Any capacity of the candidate to delay
  stopping [...] is a critical infrastructure failure."

## Why it matters

An unattended safety response (SAFE_MODE, autonomy restriction, ending a run) needs a trigger
that two implementations would apply the same way.

## Recommendation

Give every card the same fields: severity, trigger metric, window, threshold, false-alarm
budget and recovery condition, with K and L valued. Split bundled cards (§§32.18, 32.22,
32.23) and merge overlapping ones. For irreversible actions add a pre-action indicator, such
as risk-simulation calibration on reversible probes, and have §32.18 invoke the
PostImpactAssessment of §32.56.

## Resolved when

- [ ] Every card has severity, trigger metric, window, threshold and recovery condition in one
      format, with K and L valued.
- [ ] Overlapping cards are merged or ranked, and irreversible-action cards have a pre-action
      indicator.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MED-24, MED-30, MED-36
