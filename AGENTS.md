# AGENTS.md — reason

Guidance for agents working in this repository.

## What this repository is

A referee-style review of Tkalic's two-volume *Foundations of Reason* and *Engineering of
Reason*. The review is the deliverable: `REVIEW.md` and the material in `text/`. What makes it
checkable is `repro/` — the review's claims are tied back to the source volumes, and the
build re-derives the quotations, figures and numbers from those sources rather than retyping
them.

Python 3.10 or newer, standard library only.

## Layout

| Path | Role |
|---|---|
| `sources/` | The source volumes the review is written against |
| `text/` | The review's prose |
| `repro/` | Reproduction scripts: quotation extraction, listings, derived numbers |
| `notes/` | Working notes |
| `scripts/` | Build and release helpers |
| `assets/` | Figures and other binary material |
| `docs/` | Documentation |
| `REVIEW.md` | The review itself, and the entry point for a reader |

## Commands

```bash
make verify
```

`verify` is the gate, and it chains the whole chain: `listings`, `repro`, `numbers`, `audit`,
`quotes`, `sha`. Other targets — `text`, `zenodo` — build output rather than check it. Run
`make verify` before claiming any change to the review is sound; there is no other check.

## Working here

- **Never hand-edit a derived artifact.** A quotation, a listing or a number that appears in
  the review is produced by `repro/` and checked by `verify`. Change the reproduction source and
  regenerate; editing the output breaks the link between the claim and the volume and leaves
  `verify` failing.
- **Quotations must match the source exactly.** Editing one to read better is a correctness bug,
  and it is the failure this repository is built to prevent.
- The review is referee-style: it argues about someone else's work. Keep that register. Do not
  rewrite it as an endorsement or as an attack.
- Standard library only. Adding a dependency to a reproducibility script makes the review
  harder to check, which is the opposite of the point.
- There is no CI workflow, so `make verify` is only as real as your last run of it. Report its
  actual output, including any target that did not pass.
