#!/usr/bin/env bash
# Build a piece with a named target. Run from the repo root.
#   templates/pandoc/scripts/build.sh <target> pieces/<slug>/draft.md [extra pandoc args]
# Bibliography: pieces/<slug>/references.bib (written from Zotero through the
# connector by the export step; never hand-edited).
set -euo pipefail
target=$1; draft=$2; shift 2
dir=$(dirname "$draft"); out="$dir/build"; mkdir -p "$out"
bib=(); [ -f "$dir/references.bib" ] && bib=(--bibliography "$dir/references.bib")
case $target in
  seminary-paper)
    pandoc -d templates/pandoc/defaults/seminary-paper.yaml "${bib[@]}" "$draft" -o "$out/paper.docx" "$@"
    python3 templates/pandoc/scripts/fix_sections.py "$out/paper.docx"
    echo "$out/paper.docx" ;;
  blog|blog-mla)
    pandoc -d "templates/pandoc/defaults/$target.yaml" "${bib[@]}" "$draft" -o "$out/index.md" "$@"
    echo "$out/index.md" ;;
  *) echo "unknown target: $target" >&2; exit 2 ;;
esac
