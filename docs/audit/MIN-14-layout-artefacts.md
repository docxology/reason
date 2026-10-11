---
id: MIN-14
title: Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables
severity: minor
area: editorial
volumes: I, II
sections: Vol I Ch. 7, Ch. 10, A.5, throughout; Vol II §28.A, §30.C, §31.10–31.11, Ch. 32, §33.A
review: Appendix A
status: open
github_issue: 60
---

# MIN-14 · Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables

## Passages under review

- **Vol II §28.A, pp. 54–55:** "stateDiagram-v2 [*] --> INIT INIT --> LEARNING: Data available
  [...] RECOVERY --> DRIFT: Recovery not confirmed";
  **Vol II §30.C, p. 76:** "--- 30.D. Model of source reliability and causal independence".
- **Vol I Ch. 7, p. 38:** "by organizing **what, why, and relative to which trajectory** should
  become the object of revision";
  **Vol II §32.35, p. 97:** "Correction: restore `WorldviewCoverage`, introduce control tasks
  with a hidden critical ground".
- **Vol I A.5, p. 105:** "Proposed next level at which whole products of Reason and semantic
  metareasoning, metarepresentation, spaces become objects of comparison, Meta-Thinking
  (working hypothesis) conceptual integration transformation, and compression; a distinct
  established cognitive level is not yet claimed";
  **Vol I Ch. 10, p. 48:** "Principle of escaping error - a correction is considered stable
  [...] Reflection - investigation and modification of broader internal models [...] Dialogue -
  an external loop for comparing differing grounds".
- **Vol II §33.A, p. 102:** "33.A. Protocol for Assembly, Cultivation and Launch of an AR
  Candidate";
  **Vol II §33.A, p. 103:** "Chapter 31 defines capability criteria; this section lists the
  work and its outputs."

## Finding

Both PDFs carry residue of a Markdown-style source, as the passages above show: a diagram
printed as source code, literal rules and asterisks, flattened tables and definitions, stray
spaces after hyphens and uneven headings. None changes the content, but each hampers reading
and citation.

## Evidence

- **Vol II §28.A, pp. 54–55, and §30.C, p. 76:** the mode diagram is printed as raw Mermaid
  source, and a literal rule precedes the heading of §30.D. The line occurs 27 times in the
  volume, 26 of them in Chapter 32 (pp. 85–99), where it separates some cards and not others.
- **Vol II §33.A, pp. 102–103:** the heading is stranded near the top of p. 102, with the rest
  of the page blank, and the introduction is set as a chapter-style heading on p. 103.
- **Vol II §§31.10–31.11, p. 82, and §32.35, p. 97:** heading punctuation changes mid-sequence
  ("31.10. Stage 8—reflection" against "31.11. Stage 9 - Closure of Reason"), and literal
  backticks are printed around an identifier in §32.35.
- **Vol I Ch. 7, p. 38, and Ch. 10, p. 48:** the asterisks around the phrase are literal, and
  three definitions run together in one paragraph.
- **Vol I A.5, p. 105:** two table rows are flattened into running text. One carries the label
  "Meta-Thinking (working hypothesis)", which conflicts with Chapter 10. The other reads
  "Self-referential integration of the global workspace/current-state current state and
  accessible situation Consciousness integration, self-model access into one present;
  phenomenal experience is not separately claimed".
- **Vol I, 14 places on pp. 8–100:** a space follows a hyphen (search `[A-Za-z]- [a-z]`), as in
  "causal- semantic" (p. 8) and "inference- time" (p. 100). Vol II has none.

## Why it matters

Raw source, literal markup and stray rules read as unfinished text, and the flattened rows
carry a label that conflicts with Chapter 10. Spaces after hyphens also defeat a search for
terms such as self-navigation.

## Ideas & possible recommendations

- **Render the diagram.** The mode diagram in §28.A could be rendered as a figure instead of
  being printed as Mermaid source.
- **Remove stray rules and markup.** The literal "---" lines, asterisks and backticks could be
  deleted or turned into formatting; a search of the source for these leftovers before export
  would find most of them.
- **Restore the flattened text.** The two A.5 rows could be rebuilt as table rows, and the
  definitions run together in Chapter 10 could be set as separate entries.
- **Tidy headings and hyphens.** The 14 spaces after hyphens could be removed, each heading
  kept with its text, and one heading style used throughout.

## Resolved when

- [ ] Neither PDF contains raw diagram source, literal rules, asterisks or backticks, flattened
      table rows, or spaces after hyphens.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MIN-07, MIN-11, MIN-13
