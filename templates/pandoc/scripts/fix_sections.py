#!/usr/bin/env python3
"""Give each section of a seminary-paper.docx its page numbering (SBL Student
Supplement §2.3), after Pandoc has run filters/seminary-paper.lua.

Pandoc writes the reference doc's header/footer only on the document's last
section. The filter marks earlier section breaks with rsidSect values; this
script copies the header/footer references onto them and sets numbering:

  title  (00A1A101): no number
  front  (00A1A102): roman, starting at ii; first page bottom centre
  body   (00A1A103): arabic from 1; first page bottom centre, then top right
  last section (bibliography, or the body if there is none): first page
          bottom centre, then top right; continues the arabic numbering

Usage: fix_sections.py paper.docx   (edits in place)
"""
import re
import shutil
import sys
import tempfile
import zipfile

MARK = {"00A1A101": "title", "00A1A102": "front", "00A1A103": "body"}


def main(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
        names = z.namelist()
        files = {n: z.read(n) for n in names}

    sects = list(re.finditer(r"<w:sectPr\b[^>]*>.*?</w:sectPr>", xml, re.S))
    if not sects:
        return
    final = sects[-1].group(0)
    refs = "".join(re.findall(r"<w:(?:header|footer)Reference\b[^>]*/>", final))
    has_body_mark = any('w:rsidSect="00A1A103"' in s.group(0) for s in sects[:-1])

    ORDER = ["headerReference", "footerReference", "footnotePr", "endnotePr", "type",
             "pgSz", "pgMar", "paperSrc", "pgBorders", "lnNumType", "pgNumType", "cols",
             "formProt", "vAlign", "noEndnote", "titlePg", "textDirection", "bidi",
             "rtlGutter", "docGrid", "printerSettings", "sectPrChange"]

    def children(sect):
        body = re.sub(r"^<w:sectPr\b[^>]*>|</w:sectPr>$", "", sect)
        return [(m.group(1), m.group(0)) for m in
                re.finditer(r"<w:(\w+)\b(?:[^>]*?/>|[^>]*>.*?</w:\1>)", body, re.S)]

    def fix(sect, kind):
        keep = [(n, e) for n, e in children(sect)
                if n not in ("headerReference", "footerReference", "titlePg", "pgNumType")]
        add = [("titlePg", "<w:titlePg/>")]
        if kind != "title":
            add += [(m.group(1), m.group(0)) for m in
                    re.finditer(r"<w:(headerReference|footerReference)\b[^>]*/>", refs)]
            if kind == "front":
                add.append(("pgNumType", '<w:pgNumType w:fmt="lowerRoman" w:start="2"/>'))
            elif kind == "body" or not has_body_mark:
                add.append(("pgNumType", '<w:pgNumType w:start="1"/>'))
        items = keep + add
        items.sort(key=lambda t: ORDER.index(t[0]) if t[0] in ORDER else len(ORDER))
        return "<w:sectPr>" + "".join(e for _, e in items) + "</w:sectPr>"

    out, pos = [], 0
    for i, s in enumerate(sects):
        out.append(xml[pos:s.start()])
        text = s.group(0)
        m = re.search(r'w:rsidSect="([0-9A-F]+)"', text)
        kind = MARK.get(m.group(1)) if m else None
        if i == len(sects) - 1:
            kind = "last"
        out.append(fix(text, kind) if kind else text)
        pos = s.end()
    out.append(xml[pos:])
    files["word/document.xml"] = "".join(out).encode("utf-8")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, files[n])
    shutil.move(tmp, path)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
