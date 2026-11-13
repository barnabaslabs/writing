---
genre: blog
status: draft 1 (2026-11-12), from the 1 Pet 2:4–10 baseline
---

# Blog article

| Field | Rule |
|---|---|
| Reader | A church member or student reading on a phone; no Greek, no seminary. Name the specific reader in `piece.yaml`. |
| Length | 800–1,800 words; default 1,200. |
| Claim | One big idea in one sentence (thesis skill, popular). |
| Register | Read `voice/` first (samples of Jack's writing, when added). Plain, warm, direct; "you" and "we"; short paragraphs (1–4 sentences). Book-revise named patterns apply. |
| Structure | Hook (a scene, question or tension from life) → the text, in 3–5 sections with plain headings, each one move → application tied to phrases in the text → close that returns to the hook. |
| Original languages | None on the page. Explain the point a Greek or Hebrew word carries in English. |
| References | Scripture references in parentheses. At most about one reference per 150 words; cross-references only when the reader needs them. No parenthetical exegetical asides ("Peter uses the same word in 4:17…"). |
| Citations | At most three scholarly citations, and only when the reader gains from the name; always written as Pandoc keys in the draft. Style is set per piece with `citations:` in `piece.yaml`: `sbl` (default; footnotes, build target `blog`) or `mla` (MLA 9 in-text with a Works Cited list, build target `blog-mla`; the simpler option). |
| Scripture | Quotations follow the write skill's rule 1; a closing italic note names the translations used. |
| Definitions | Define every technical term at first use (elect, Zion, Gentile, covenant, priesthood…). |
| Application | Central and specific, tied to a phrase in the text; carry its authority (write rule 6). Avoid absolutes and scolding lines the text doesn't earn ("there is no third way," "Sunday is not a spectator event"). |
| Illustration | At least one concrete story or image. From Scripture, history (cited) or Jack's `illustrations/`; never invented. Empty bank: ask Jack one specific question before drafting; unattended, a `%% JL %%` marker saying what fits (write rule 7). |
| Reviews | Reader test (Sonnet) and substance check (Opus), both required. |
| Export | `templates/pandoc/scripts/build.sh blog` (or `blog-mla`) → `build/index.md`, Hugo Markdown with YAML front matter (title, subtitle, author, date, draft, tags, categories, summary, description, slug only) and Goldmark footnotes; `%% author notes %%` are stripped. Site-specific fields come from the venue file. Venue: undecided (candidate: Renewing Grace). |
