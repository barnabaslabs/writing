# Baseline run: what went wrong without writing skills

Piece: 1 Pet 2:4–10 blog article, draft 1, written 2026-11-12 with no writing skills loaded (only the research dossier, bookwright's linter, and judgment). Each failure names the skill that should prevent it. This file is the "failing test" the skills are written against.

## Observed in drafting (orchestrator)

| # | Failure | Skill that must prevent it |
|---|---|---|
| D1 | **Translation provenance.** The draft labels all Scripture "the author's translation," but only 1 Pet 2:4–10 comes from the dossier's own translation. Exod 19:6, Isa 43:20–21, Acts 4:11 and 1 Pet 4:4 were rendered ad hoc with no source in the research. | `draft`: every quotation needs a source (dossier translation, a named version checked in Logos, or flagged). `writing-review` gate 1 must check Scripture wording, not only citekeys. |
| D2 | **No illustration bank.** The only place for a personal story became a `%% JL %%` placeholder. Correct (no invented anecdote), but the piece has no concrete human story. | `explain` + `illustrations/`: look in the bank first; if empty, ask Jack one targeted question before drafting, not after. |
| D3 | **No genre profile or voice file to draft against.** Length, reference density, register and how to cite on the blog were guessed. | `genres/blog.md`, `voice/` samples. |
| D4 | **Linter false positive.** "that very stone" flagged as W4 padding. | `revise` pass 2: hits are prompts, not verdicts (already in book-revise); consider an allow-list. |
| D5 | **Front matter guessed.** Hugo fields (`draft`, `tags`) and the target site are assumed. | `export` blog target + venue file for the site. |

## From the reader test (fresh agent, Sonnet) — reviews/reader-test.md

| # | Failure | Skill |
|---|---|---|
| R1 | **The hardest sentence was left unexplained.** "God decided what would happen to those who refuse it" made the reader ask whether God caused the refusal. The draft stated a doctrine without the define/contrast move. | `explain`: every claim the outline marks as hard gets a move; `outline` must mark it. |
| R2 | **Terms used without definition** for a lay reader: elect, priesthood (why priests matter), Zion, Gentile, head of the corner. | `explain` define move + a lay-reader glossary check in the reader gate. |
| R3 | **Reference density.** Eight books cited in 1,100 words; the reader skimmed the citations. | `genres/blog.md`: limit visible references; put secondary ones in a note or link. |
| R4 | **Resistance from absolute or scolding lines:** "There is no third way," "Peter cannot imagine a Christian who is a stone in a field," "Sunday morning is not a spectator event," "Tell someone how." | `revise`: new pattern for unearned absolutes and scolding application (tie it to book-revise A2/A5). |
| R5 | **Overload in one section.** "Honor or stumbling" carries three OT quotations and a doctrine in four short paragraphs. | `outline`: one main move per section; `revise` level diagnosis (reader level). |
| R6 | **Hosea paragraph confusing:** the Hosea quotation was paraphrased, not shown, and the reader could not tell what "Not my people" referred to. | `explain` show-from-the-text move. |
| R7 | **Asides that confuse on a phone:** "(Peter uses the same word in 4:17 …)". | `revise` pass 3 copyedit; blog genre rule: no exegetical asides in parentheses. |

What worked (keep): the hook landed; the cornerstone was clear; the Israel guardrail was understood correctly; the remembered lines were the closing image and "The cross was the builders' verdict. The empty tomb was God's."

## From the substance check (separate agent, Opus) — reviews/substance.md

Verdict REVISE: no RETHINK; the exegesis and the Israel guardrail held.

| # | Failure | Skill |
|---|---|---|
| S1 | **BLOCK: five quotations labelled "author's translation" had no source** (Exod 19:6, Isa 43:20–21, Acts 4:11, 1 Pet 4:4, 4:17). Same as D1, caught independently. | `draft` + gate 1 (see D1) |
| S2 | **Right conclusion, wrong text.** The foundation sense of the cornerstone was credited to Ps 118:22; the dossier gets it from Isa 28:16. | `draft` must cite the dossier decision it is using, not restate from memory |
| S3 | **Plausible stated as certain.** "If you belong to him, the same words describe you": the dossier rates the chosen-stone → chosen-people link *plausible*, and "precious" is never said of believers. | `writing-review` claim fidelity must carry the dossier's H14 labels into popular prose (soften, don't drop) |
| S4 | **A true fact that invites a wrong reading.** Acts 4:11 (the council as "builders") placed just before 2:7–9 lets a lay reader rebuild the "Israel stumbles, Gentiles replace" reading the dossier rejects. | `explain` contrast move + gate 4 reading for implications, not only statements |
| S5 | **Tense of a promise flattened.** "Never put to shame" given only as present; the dossier has present honor and future vindication. | claim fidelity |
| S6 | **Unsourced color.** "temple feasts," "shamed every week," "Peter cannot imagine." | `draft`: background details need a verse or a source |
| S7 | **Two definitions of one term** ("spiritual sacrifices") in the same piece, one unsourced. | `revise` pass 1 consistency check |
| S8 | **Derived application worded as if stated** ("Sunday morning … is the temple at work"). | H17 authority level carried into `draft` |

## Draft 2 (same day)

All BLOCK and FIX items resolved: non-2:4–10 Scripture now quoted from the LSB, checked in Logos (OpenTabs) and labelled; foundation sense moved to Isa 28:16; builders widened to "people"; "now and on the last day"; the 2:8 line explained (cause = disobedience; what is appointed = the result); elect, priesthood, Zion, head of the corner defined; Hosea shown, not paraphrased; absolutes and scolding lines removed; the 2:6–8 section split in two. 1,296 words (target 1,200). Still open: Jack's story at the `%% JL %%` marker; the target site; LSB permission line for the site.

## Lessons for the skills (summary)

1. Quotation provenance is the most likely failure, and both checkers caught it. Make it a hard rule in `draft` and a gate-1 item.
2. A gated dossier does not stop drift: the drafter restated decisions from memory and got one wrong. `draft` should link each claim to the dossier line it uses.
3. Popular prose needs the dossier's certainty labels translated, not dropped.
4. The reader test found what the substance check could not (undefined terms, resistance, overload), and the substance check found what the reader could not (wrong source, misleading juxtaposition). Keep both gates.
5. Sonnet was adequate for the reader test; Opus earned its cost on the substance check.
