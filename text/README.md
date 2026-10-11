# Extracted text

Plain-text conversions of the two PDFs in `../sources/`, made with poppler's `pdftotext`
(version 26.10.0). They are adaptations of works by Mihail Tkalic licensed
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); the only change is the
conversion to text.

| File | Command |
|---|---|
| `foundations-8.0.txt` | `pdftotext -layout sources/foundations-8.0/Foundations_of_Reason_8.0_EN.pdf` |
| `engineering-3.5.txt` | `pdftotext -layout sources/engineering-3.5/Engineering_of_Reason_3.5_EN.pdf` |
| `foundations-8.0.raw.txt` | `pdftotext` (default reading-order mode) on the same PDF |
| `engineering-3.5.raw.txt` | `pdftotext` (default reading-order mode) on the same PDF |

`make text` regenerates all four. Each form feed (`\f`) marks a PDF page break, so the
page of any line is one plus the number of form feeds before it. Line and page numbers in
`docs/audit/` refer to the `-layout` files; `scripts/locate.py` finds a quote and prints
both.
