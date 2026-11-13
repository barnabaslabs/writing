#!/usr/bin/env python3
"""Build reference-docs/seminary-paper.docx from Pandoc's default reference.docx.

Formatting follows the Student Supplement for The SBL Handbook of Style, 2nd ed.
(Nogalski et al., rev. SBL Press 2015), Part 2 (term papers):
  2.1 1-inch margins, ragged right, tabs at 0.5 in.
  2.2 double-spaced text; block quotations single-spaced, indented 0.5 in.,
      set off by a blank line, no quotation marks.
  2.3 page number bottom centre on a section's first page, top right after;
      title page unnumbered (handled by filters/seminary-paper.lua).
  2.4 12-point font, title page in the text font, bold only in subheadings.
  2.5 first paragraph of a section flush left; later paragraphs indented 0.5 in.
  2.6 headings: primary centred all caps; 1st level centred bold;
      2nd centred plain; 3rd left bold italic; 4th left plain.
  2.9 footnotes 10 pt (12 pt where an institution requires it), single-spaced,
      first line indented 0.5 in., a blank line between notes.
  2.11 bibliography single-spaced entries, hanging indent, blank line between.
  3.3 two blank lines between text and any subheading; 2-inch top margin on a
      chapter's (and the bibliography's) first page.

Usage: python3 make_reference_docx.py [--footnote-size 12]
"""
import argparse
import copy
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "reference-docs" / "seminary-paper.docx"
FONT = "Times New Roman"
HEBREW = "SBL Hebrew"


def set_font(style, size=12, bold=False, italic=False, caps=False):
    f = style.font
    f.name = FONT
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.all_caps = caps
    f.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    for k in ("w:ascii", "w:hAnsi", "w:eastAsia"):
        fonts.set(qn(k), FONT)
    fonts.set(qn("w:cs"), HEBREW)
    for k in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if fonts.get(qn(k)) is not None:
            del fonts.attrib[qn(k)]
    # complex-script size matches (Hebrew)
    for tag in ("w:szCs",):
        el = rpr.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            rpr.append(el)
        el.set(qn("w:val"), str(size * 2))


def para(style, align=WD_ALIGN_PARAGRAPH.LEFT, double=True, first=None,
         left=None, hanging=None, before=0, after=0, keep_next=False):
    pf = style.paragraph_format
    pf.alignment = align
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE if double else WD_LINE_SPACING.SINGLE
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.first_line_indent = first
    pf.left_indent = left
    if hanging is not None:
        pf.left_indent = hanging
        pf.first_line_indent = -hanging
    pf.keep_with_next = keep_next
    pf.widow_control = True


def page_field(paragraph):
    """Append a PAGE field to a paragraph."""
    run = paragraph.add_run()
    for kind, text in (("begin", None), (None, " PAGE "), ("end", None)):
        if kind:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            run._r.append(fc)
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = text
            run._r.append(it)
    run.font.name = FONT
    run.font.size = Pt(12)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--footnote-size", type=int, default=10, choices=[10, 12])
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as td:
        base = Path(td) / "ref.docx"
        subprocess.run(["pandoc", "-o", str(base), "--print-default-data-file",
                        "reference.docx"], check=True)
        doc = Document(str(base))

    raw = doc.styles

    class St:
        def __getitem__(self, name):
            for sty in raw:
                if sty.name == name or sty.style_id == name.replace(" ", ""):
                    return sty
            raise KeyError(name)

        def __iter__(self):
            return iter(raw)

        def add_style(self, *a):
            return raw.add_style(*a)

    st = St()
    for name in ("Normal", "Body Text", "First Paragraph", "Compact", "Block Text",
                 "Footnote Text", "Bibliography", "Title", "Subtitle", "Author",
                 "Date", "Heading 1", "Heading 2", "Heading 3", "Heading 4",
                 "Heading 5", "Heading 6", "Table Caption", "Image Caption",
                 "Definition Term", "Definition", "Abstract", "Abstract Title"):
        try:
            set_font(st[name])
        except KeyError:
            pass

    # body text (2.2, 2.5)
    para(st["Normal"], double=True)
    para(st["Body Text"], first=Inches(0.5))
    para(st["First Paragraph"], first=Inches(0))
    para(st["Compact"], first=Inches(0))
    # block quotation (2.2): single, indented 0.5 in, blank line above and below
    para(st["Block Text"], double=False, left=Inches(0.5), first=Inches(0),
         before=12, after=24)
    st["Block Text"].paragraph_format.right_indent = Inches(0)
    # footnotes (2.9)
    set_font(st["Footnote Text"], size=args.footnote_size)
    para(st["Footnote Text"], double=False, first=Inches(0.5), after=args.footnote_size)
    # bibliography (2.11, 3.5)
    para(st["Bibliography"], double=False, hanging=Inches(0.5), after=12)
    # headings (2.6, 3.3)
    set_font(st["Heading 1"], caps=True)            # primary
    para(st["Heading 1"], align=WD_ALIGN_PARAGRAPH.CENTER, double=False,
         before=72, after=48, keep_next=True)       # 2-in top (1 in margin + 72 pt)
    set_font(st["Heading 2"], bold=True)            # first-level
    para(st["Heading 2"], align=WD_ALIGN_PARAGRAPH.CENTER, before=24, keep_next=True)
    set_font(st["Heading 3"])                       # second-level
    para(st["Heading 3"], align=WD_ALIGN_PARAGRAPH.CENTER, before=24, keep_next=True)
    set_font(st["Heading 4"], bold=True, italic=True)  # third-level
    para(st["Heading 4"], before=24, keep_next=True)
    set_font(st["Heading 5"])                       # fourth-level
    para(st["Heading 5"], before=24, keep_next=True)
    # title-page style used by the filter
    try:
        st["Title Page"]
    except KeyError:
        tp = st.add_style("Title Page", 1)
        tp.base_style = st["Normal"]
    set_font(st["Title Page"], caps=True)
    para(st["Title Page"], align=WD_ALIGN_PARAGRAPH.CENTER, first=Inches(0))
    # contents heading
    try:
        set_font(st["TOC Heading"], caps=True)
        para(st["TOC Heading"], align=WD_ALIGN_PARAGRAPH.CENTER, double=False, after=24)
    except KeyError:
        pass

    # page setup (2.1) and numbering (2.3) for the main-text section
    sec = doc.sections[-1]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(sec, side, Inches(1))
    sec.header_distance = sec.footer_distance = Inches(0.5)
    sec.different_first_page_header_footer = True
    hp = sec.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    page_field(hp)
    fp = sec.first_page_footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    page_field(fp)
    sec.first_page_header.paragraphs[0].text = ""
    sec.footer.paragraphs[0].text = ""
    pg = sec._sectPr.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType")
        sec._sectPr.append(pg)
    pg.set(qn("w:start"), "1")

    # ragged right is the default (left alignment); default tab stop 0.5 in
    settings = doc.settings.element
    tab = settings.find(qn("w:defaultTabStop"))
    if tab is None:
        tab = OxmlElement("w:defaultTabStop")
        settings.append(tab)
    tab.set(qn("w:val"), "720")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
