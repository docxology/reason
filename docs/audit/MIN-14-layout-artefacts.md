---
id: MIN-14
title: Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables
severity: minor
area: editorial
volumes: I, II
sections: Vol I Ch. 7, Ch. 10, A.5, throughout; Vol II §28.A, §30.C, §31.10–31.11, Ch. 32, §33.A
review: Appendix A
status: open
---

# MIN-14 · Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables

**Finding.** Both PDFs carry residue of a Markdown-style source: a diagram printed as source code,
literal rules and asterisks, flattened tables and definitions, stray spaces after hyphens and
uneven headings. None changes the content, but each hampers reading and citation.

## Evidence

- **Vol II §28.A, pp. 54–55, and §30.C, p. 76:** the mode diagram is printed as raw Mermaid source
  ("stateDiagram-v2"), and a literal "---" precedes "30.D. Model of source reliability". The line
  occurs 27 times in the volume, 26 of them in Chapter 32, where it separates some cards and not
  others.
- **Vol II §33.A, pp. 102–103:** the heading "33.A. Protocol for Assembly, Cultivation and Launch"
  is stranded at the top of p. 102, and the introduction is set as a chapter-style heading on
  p. 103: "Chapter 31 defines capability criteria; this section lists the work and its outputs."
- **Vol II §§31.10–31.11, p. 82, and §32.35, p. 97:** heading punctuation changes mid-sequence
  ("31.10. Stage 8—reflection" against "31.11. Stage 9 - Closure of Reason"), and literal
  backticks are printed ("restore `WorldviewCoverage`").
- **Vol I Ch. 7, p. 38, and Ch. 10, p. 48:** literal asterisks ("**what, why, and relative to
  which trajectory**"), and three definitions run together in one paragraph ("Principle of
  escaping error - [...] Reflection -").
- **Vol I A.5, p. 105:** two table rows are flattened into running text, one labelled
  "Meta-Thinking (working hypothesis)", which conflicts with Chapter 10.
- **Vol I, 14 places on pp. 8–100:** a space follows a hyphen (search `[A-Za-z]- [a-z]`), as in
  "causal- semantic" (p. 8) and "inference- time" (p. 100). Vol II has none.

## Why it matters

Raw source, literal markup and stray rules read as unfinished text, and the flattened rows carry a
label that conflicts with Chapter 10. Spaces after hyphens also defeat a search for terms such as
self-navigation.

## Recommendation

Render the diagram, delete stray rules and markup, restore the flattened rows, remove the spaces
after hyphens, keep headings with their text and use one heading style.

## Resolved when

- [ ] Neither PDF contains raw diagram source, literal rules, asterisks or backticks, flattened
      table rows, or spaces after hyphens.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MIN-07, MIN-11, MIN-13
