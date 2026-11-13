# Pandoc templates

Build any piece from the repo root:

```
templates/pandoc/scripts/build.sh <target> pieces/<slug>/draft.md
```

The script reads `pieces/<slug>/references.bib` if present (written from Zotero through the connector; never hand-edited) and writes to `pieces/<slug>/build/`. Every target stops on an unresolved `[@?` flag.

| Target | Output | Citations | Formatting |
|---|---|---|---|
| `seminary-paper` | `paper.docx` | SBL notes, Student Supplement variant (`csl/sbl-student-supplement.csl`: "City: Publisher") | SBL Student Supplement Part 2 (below) |
| `blog` | `index.md` (Hugo) | SBL notes as Goldmark footnotes (`csl/sbl-fullnote-research.csl`, current SBL: no place) | Front matter limited to Hugo keys; `%% notes %%` stripped |
| `blog-mla` | `index.md` (Hugo) | MLA 9 in-text, "Works Cited" list (`csl/modern-language-association.csl`) | As `blog` |

## seminary-paper

Follows the *Student Supplement for The SBL Handbook of Style, Second Edition* (Nogalski et al., rev. SBL Press 2015), in Zotero as an attachment to `collinsSBLHandbookStyle2014`. Front matter:

```yaml
title: "…"
author: Jack Lamb
date: November 13, 2026
institution: Liberty University
professor: Dr. …
course: "BIBL …: …"
contents: true        # optional; papers of 15+ pages (§2.7)
```

| Supplement rule | How the template does it |
|---|---|
| §2.1 margins 1 in., ragged right, tabs 0.5 in. | reference.docx page setup; left-aligned styles |
| §2.2 double-spaced; block quotes single, indented 0.5 in., blank line around | Body Text / Block Text styles (`>` in Markdown) |
| §2.3 no number on title page; first page of a section bottom centre, then top right; roman front matter from ii | `filters/seminary-paper.lua` section breaks + `scripts/fix_sections.py` |
| §2.4 12-pt font, title page in text font, bold only in subheadings | Times New Roman 12 throughout (Hebrew: SBL Hebrew if installed) |
| §2.5 first paragraph of a section flush left, later ones indented | First Paragraph / Body Text styles |
| §2.6 headings | primary (the title, Bibliography): centred caps · `#` first-level: centred bold · `##` second: centred · `###` third: left bold italic · `####` fourth: left plain |
| §2.8 / 3.1 title page all caps, centred, 2-in. top and bottom | filter builds it from front matter; elements spread with Word's vertical justification |
| §2.9 footnotes 10 pt, single, first line indented 0.5 in., blank line between | Footnote Text style (`make_reference_docx.py --footnote-size 12` where 12 pt is required) |
| §2.11 / 3.5 bibliography on its own page, single-spaced entries, hanging indent, blank line between | own section; Bibliography style |
| 3.3 2-in. top margin on a section's first page; two blank lines before subheadings | heading spacing |

Check in Word before submitting: the title page relies on vertical justification (LibreOffice ignores it and stacks the elements at the top); the contents page needs right-click → Update Field.

Not built: abbreviations page (§1.5), appendixes (sample 3.4), SBL series and journal abbreviations (needs a `citation-abbreviations` file).

**Publisher places.** SBL dropped places of publication for general use on 2025-12-05 ([Zotero forum](https://forums.zotero.org/discussion/comment/507246)); the 2015 Supplement, which Liberty follows, still uses "City, ST: Publisher." Keep places in Zotero with state postal codes (§2.12).

## Files

```
defaults/              one Pandoc defaults file per target
reference-docs/        seminary-paper.docx (rebuild: python3 scripts/make_reference_docx.py)
csl/                   sbl-student-supplement, sbl-fullnote-research (copy of barnabaslabs/research csl/), MLA 9
filters/               seminary-paper.lua, blog.lua, blog-final.lua, block-unverified.lua
scripts/               build.sh, fix_sections.py, make_reference_docx.py
test/                  sample-paper.md, sample-blog.md, references.bib (from Zotero)
```

Test: `templates/pandoc/scripts/build.sh seminary-paper templates/pandoc/test/sample-paper.md --bibliography templates/pandoc/test/references.bib`
