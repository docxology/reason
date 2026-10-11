---
id: MIN-11
title: Contents pages disagree with the headings they list
severity: minor
area: editorial
volumes: I, II
sections: Vol II Contents (pp. 7–10) against Chs. 25–34
review: Appendix A
status: open
github_issue: 57
---

# MIN-11 · Contents pages disagree with the headings they list

## Passages under review

- **Vol II contents, p. 10:** "Modeling Environment and recursive Core ↔ Intelligence cycle";
  **Vol II §28.C heading, p. 57:** "Modeling Workspace and the recursive Core ↔ Intelligence
  cycle".
- **Vol II contents, p. 10:** "Compass, values, and action admission"; **Vol II Ch. 29
  heading, p. 65:** "Compass, Values and Action Authorization".
- **Vol II contents, p. 10:** "Dialogue and independent distinction"; **Vol II Ch. 30
  heading, p. 74:** "Dialogue and Independent Discrimination".

## Finding

20 of the 82 numbered entries in Volume II's contents differ in wording from the headings they
point to. Several differences change a key term rather than style, which suggests the contents
and the body were translated separately.

## Evidence

| Section | Contents | Heading in the body |
|---|---|---|
| 28.C | Modeling **Environment** and recursive Core ↔ Intelligence cycle | Modeling **Workspace** and the recursive Core ↔ Intelligence cycle |
| 29 | Compass, values, and action **admission** | Compass, Values and Action **Authorization** |
| 33 | Assembly, cultivation, launch, and **admission** | Assembly, Cultivation, Launch and **Authorization** |
| 30 | Dialogue and independent **distinction** | Dialogue and Independent **Discrimination** |
| 33.B | Minimal **program framework** of **test bench** v0 | Minimal **Software Scaffold** of **Proving Ground** v0 |
| 28 / 28.B | regulation of **thinking** | Regulation of **Thought** |
| 28.D | Selection of an **inquiry** channel and stopping condition | Selection of a **research** channel and stopping condition |
| 25.A | From an observed **signal** to a significant gap | From an Observed **Change** to a Gap Candidate and FoundationGap |
| 26.0.2 | AI mentor as a source of **prompting** | AI Mentor as a Source of **Guidance** |
| 30.C | **Robustness** to adversarial inputs and data provenance | **Resistance** to adversarial inputs and data provenance |

The remaining ten differ only in articles or capitalization (25.B.1, 25.C, 28.C.2, 28.C.3,
28.E, 29.A, 31, 33.C, 34, and 28.B's capitalization). Reproduce by comparing the contents (text
lines 425–535) with the numbered headings after line 662 of `text/engineering-3.5.txt`. Volume
I has the same problem on a smaller scale: its contents omit "Open Research Directions", carry
no page numbers, run several parts together into single paragraphs, and word the Conclusion and
A.1 entries differently from their headings. Volume II's contents also omit §§27.1–27.7,
31.1–31.12, 32.1–32.62 and 33.A.1–33.A.14, although the text sends readers to §31.11 and tells
them to "go directly to" a failure card, and leave out the unnumbered closing section "On
Verification of the Model" (p. 114).

## Why it matters

"Modeling Environment" is a component of the Volume I architecture and `ModelingWorkspace` is a
Volume II record; "admission" and "authorization" name different stages in the formation
protocol. Readers navigating by the contents will meet different terms in the body.

## Ideas & possible recommendations

- **Generate the contents from the headings.** A build step that writes the contents from the
  numbered headings would keep the two in step through later revisions.
- **One English term per concept.** A short list of fixed translations (Environment or
  Workspace, admission or authorization, distinction or discrimination), applied across both
  volumes, would settle the key terms; MIN-05 and MIN-15 list further candidates.
- **List what the text points to.** The contents could include §31.11 and the failure cards of
  Chapter 32, since the text sends readers directly to them.

## Resolved when

- [ ] The contents of Volume II match its headings verbatim, and each concept has one English
      term.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MIN-05
