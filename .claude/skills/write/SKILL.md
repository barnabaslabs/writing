---
name: write
description: Use whenever Jack asks to start, resume, plan, draft, review or check the status of a paper, article, essay, post or resource, or says "let's write", "next piece", or names a folder in barnabaslabs/writing pieces/. Not for book-length work, which goes to bookwright's book-pipeline.
---

# Write (orchestrator)

This skill decides **what stage a piece is in and what happens next**. It holds the rules every stage obeys. Read `lessons.md` first, then `STATUS.md` and the piece's `piece.yaml`.

## Where things live

```
pieces/<yyyy>-<slug>/
  piece.yaml     # templates/piece.yaml
  brief.md       # thesis skill (templates/brief.md is its shape)
  research.md    # links into barnabaslabs/research + open requests (templates/research.md)
  outline.md
  draft.md       # Markdown, Pandoc citations, Hugo/Pandoc front matter
  reviews/       # reader-test.md, substance.md, gate reports, baseline notes
  build/         # gitignored
```
Genre rules: `genres/<genre>.md`. Venue rules: `venues/<venue>.md` (they override the genre). Voice: `voice/`. Stories: `illustrations/`.

## Stages

| # | Stage | Output | Who | Model |
|---|---|---|---|---|
| 0 | Intake | `piece.yaml`, row in `STATUS.md` | this skill | Haiku/Sonnet |
| 1 | Thesis | `brief.md` | `thesis` | Opus |
| 2 | Research check | `research.md`; issues in barnabaslabs/research | this skill (until `research-request` exists) | Sonnet |
| 3 | Outline | `outline.md` | this skill (until `outline` exists) | Opus |
| 4 | Draft | `draft.md` | one writer per piece | Opus |
| 5 | Review | `reviews/` | separate agents (below) | see below |
| 6 | Revise | new draft, one commit per pass | this skill: first decide which level the review findings belong to (thesis, structure, evidence, reader) and fix the highest level first; then bookwright's `book-revise/references/prose-patterns.md` and `prose_lint.py` | Opus for the level decision, Sonnet for patterns |
| 7 | Export | `build/` | `templates/pandoc/scripts/build.sh <target> pieces/<slug>/draft.md` (targets: `seminary-paper`, `blog`, `blog-mla`; see `templates/pandoc/README.md`); write `references.bib` from Zotero through the connector first; confirm the translation's permission notice and the venue's fields | Haiku |

**Intake** (stage 0). Ask one question at a time, only what `piece.yaml` lacks: genre, reader (a specific person, not "Christians"), venue, length, deadline, mode, source in the research repo. Unattended: take the most reasonable reading, write it in `piece.yaml` with `# assumed`, and carry on to the thesis.

**Modes.** `agent-draft`: Claude drafts stage 4, Jack edits after review. `author`: Jack writes `draft.md`; Claude does stages 0–3 as briefing, then reviews and gives a fix list as suggestions; never rewrites his sentences unless he says "apply them."

**Status values** for `piece.yaml` and `STATUS.md`: `intake`, `thesis (awaiting Jack)`, `waiting on research#N`, `outline`, `draft N`, `review`, `revise`, `ready to export`, `published`. Two stops wait for Jack even when unattended: thesis approval, and anything that would publish or upload.

**Research check** (stage 2; the thesis skill may call it early when the research has no thesis or meaning statement). Before outlining, list in `research.md` every claim the brief rests on and where the research holds it (file + line or section). Search `barnabaslabs/research` (`index/README.md`, then `grep -ril` across `passages/ words/ topics/ doctrine/ sources/`). For each gap: if it blocks the piece, file an issue in barnabaslabs/research (labels `request`, `from:writing`, `blocking`) with the question, the passage or topic, the depth wanted and a link to the piece, then set the piece to `waiting on research#N` in `STATUS.md` and stop that piece. Don't poll; check open issues at the next session. Non-blocking gaps are noted and the piece goes on without the claim.

**Outline** (stage 3). Each section: its one claim, the evidence (research line), the explanation move it needs (define, show from the text, example, analogy, story, contrast), and the transition. Mark every claim a reader is likely to resist or misread. One main move per section; a section carrying three quotations and a doctrine is two sections.

## Rules for every draft (from the 1 Pet 2:4–10 baseline; see lessons.md)

1. **Every quotation names its source.** Scripture: the dossier's own translation (only for the verses it translated), or a named version fetched with the OpenTabs Logos plugin (`opentabs__logos__get_bible_text`), never from memory. A closing note (popular genres) or the first footnote (academic genres) names the translations used. Other authors: Pandoc citation with a verified page.
2. **Use the research; don't restate it from memory.** Keep `research.md` open while drafting and take each claim from the line it cites. If the research doesn't hold a claim, it doesn't go in, or it goes to stage 2 as a gap.
3. **Keep the research's certainty and time-frame.** A claim the research labels *plausible* or *possible* stays hedged in plain words ("probably," "Peter seems to"), or is left out if the piece doesn't need it; it is never promoted to certain. Keep the tense of promises: present honor and future vindication are both said when the research says both.
4. **Read for what a placement implies.** A true fact set next to a passage can suggest a reading the research rejects (Acts 4:11's builders before 1 Pet 2:7–9 suggested replacement). Say the limiting sentence.
5. **Background details need a source.** Colorful details about the first readers (feasts, frequency of abuse, what Peter "could not imagine") come from a verse or a cited source, or they go.
6. **Applications carry their authority.** Stated by the text, derived (H17 principle → specific), or illustrative. Derived ones are worded as such ("this is part of…"), not as the text's own words.
7. **No invented personal stories.** Look in `illustrations/` first. If it has nothing that fits, ask Jack one specific question before drafting; unattended, leave a `%% JL: … %%` marker saying what kind of story fits where.
8. **One term, one definition** across the piece.
9. **Lay pieces define every technical term** the first time (elect, Zion, Gentile, covenant…) and keep references within the genre profile's limits.

## Review (stage 5)

Each check is a separate agent that has not seen the drafting. Brief it with the files only.
- **Reader test** (Sonnet): sees only `draft.md`; brief it with `templates/reader-test.md`. A question it answers wrongly is a BLOCK; PARTLY answers, confusion, resistance, overload and undefined terms are FIX.
- **Substance check** (Opus): draft + the research files listed in `research.md` + barnabaslabs/research `method/hermeneutics.md` (H14 certainty labels, H17 application, H18 Israel) and `doctrine/`; checks claim fidelity, certainty and tense, H17/H18, implications of placement, and the source of every quotation; findings BLOCK / FIX / NOTE; verdict PASS / REVISE / RETHINK.
- Academic genres also run research-review gates 1–4 (from barnabaslabs/research) and an adversarial reviewer (Opus).
Merge findings into one fix list; fix blocks first. Re-run a check only when its findings touched the argument.

## Ending a session

Update `piece.yaml` status and `STATUS.md`. Add 1–3 dated lines to this skill's `lessons.md` (or the relevant skill's) when something failed or Jack corrected something. Commit with the session's attribution lines and push. Tell Jack where the piece stands and the single next step.
