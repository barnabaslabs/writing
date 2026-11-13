# writing

Skills, templates and pieces for turning research from [barnabaslabs/research](https://github.com/barnabaslabs/research) into papers, articles, essays, blog posts and counseling resources. Books keep their own repos and publish through [bookwright](https://github.com/barnabaslabs/bookwright).

Plan: the "Writing System Plan" Claude doc (https://claude.ai/artifact/3haLRjxiXWXsX7FjVXrS5R).

| Folder | Contents |
|---|---|
| `.claude/skills/` | Writing skills (built test-first against `pieces/*/reviews/baseline-failures.md`) |
| `genres/` | One profile per genre |
| `venues/` | One file per journal, publisher, class or site |
| `voice/` | Voice notes, prose patterns, writing samples |
| `illustrations/` | Jack's own stories, tagged by theme and passage |
| `templates/pandoc/` | Defaults files, reference.docx, CSL, Lua filters |
| `pieces/<yyyy>-<slug>/` | One folder per piece: piece.yaml, brief, outline, draft, reviews |

Conventions: Markdown with Pandoc citations `[@citekey, page]`, keys from Zotero via the connector; every quotation names its source; research notes are linked, not copied; new findings go back to research by PR.
