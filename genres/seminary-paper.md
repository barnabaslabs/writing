---
genre: seminary-paper
status: draft 2 (2026-11-13); Liberty papers follow the SBL Student Supplement (Jack, 2026-11-13)
---

# Seminary paper (exegesis or research paper)

| Field | Rule |
|---|---|
| Reader | The professor, then a scholar in the field. Assume Greek and Hebrew. |
| Length | Set by the course (`venues/<course>.md`). Idestrom's handout: 12–15 pages, 3,000–3,750 words, 7–10+ secondary sources [@idestromExegesisPaperGuidelines, practical note]. |
| Claim | An arguable thesis with an argument map (thesis skill, academic). |
| Register | Formal, first person sparingly, every claim supported. Book-revise patterns apply; no devotional asides. |
| Structure (exegesis paper) | Idestrom's ten sections, which the research repo's passage dossier already follows: 1 Introduction; 2 Textual matters and translation; 3 Compositional history; 4 Genre and structure; 5 Historical context; 6 Literary context and canonical placement; 7 Literary analysis; 8 Main themes and theological message; 9 Theological implications and application; 10 Conclusion [@idestromExegesisPaperGuidelines]. Present conclusions, integrated, not the story of the study. |
| Structure (research paper) | Introduction with problem and thesis → the conversation (literature) → argument in steps (argument map) → objections answered → conclusion. |
| Original languages | Greek and Hebrew in their scripts, with English gloss at first use. |
| Citations | Footnotes, Pandoc keys from Zotero via the connector, every page verified (research R5). Style: `sbl-student-supplement.csl` — SBL fullnote with "City: Publisher" as the Student Supplement shows (SBL dropped publisher places for general use on 2025-12-05; the Supplement, which Liberty follows, keeps them). Places carry state postal codes (Supplement §2.12): fix them in Zotero. Abbreviate journals and series per *SBLHS* 8.4 (Supplement §1.5). |
| Scripture | Own translation of the passage (from the dossier); other Scripture from a named version checked in Logos. Version abbreviation in parentheses after the first quotation only when one version is used throughout; after every quotation when more than one (Supplement §1.2, §2.10). SBL book abbreviations with chapter:verse and en dashes (*SBLHS* 8.3.13; Supplement §1.2). Greek and Hebrew in their scripts; Hebrew consonantal unless pointing matters (§1.7). |
| Application | Idestrom §9: principles first, then recontextualized application; mark authority (H17). Some professors want it brief or omitted; follow the course. |
| Reviews | Research-review gates 1–4, an adversarial reviewer (Opus), the substance check against the dossier, and the venue gate (length, sources count, format). Reader test optional. |
| Export | `templates/pandoc/scripts/build.sh seminary-paper pieces/<slug>/draft.md` → Word, formatted per Student Supplement Part 2: title page (institution, title, professor, course, author, date in front matter), Times 12, 1-inch margins, ragged right, double-spaced text, single-spaced block quotes and footnotes (10 pt), page numbers bottom centre on first pages and top right after, the heading levels of §2.6, bibliography in its own section. `contents: true` adds a contents page (papers of 15+ pages). In the draft, `#` = first-level subheading; the paper title becomes the primary heading. Not built yet: abbreviations page; appendixes (format by hand per sample 3.4). |
