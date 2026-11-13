--[[
seminary-paper.lua: term-paper layout from the Student Supplement for the
SBL Handbook of Style, 2nd ed. (rev. 2015), Parts 2-3. Docx output only.

Metadata it reads (YAML front matter of the draft):
  title, author, date            -- as usual
  institution                    -- e.g. "Liberty University" (title page)
  professor                      -- "Dr. Jane Smith"
  course                         -- "BIBL 8xx: Course Title"
  contents: true                 -- add a CONTENTS page (papers of 15+ pages, §2.7)
  bibliography-title             -- default "Bibliography"

What it does:
  * builds the title page (§2.8, sample 3.1): all caps, centred, four
    elements spread down the page with 2-inch top and bottom margins; no
    page number (§2.3);
  * optional contents page with a TOC field, numbered in lower-case roman
    starting at ii (§2.3, sample 3.2);
  * opens the text with the title as the primary heading (sample 3.3);
  * puts the bibliography in its own section with its own heading (§2.11).
Section breaks carry marker rsids; scripts/fix_sections.py then gives each
section its page-number header/footer. The build script runs both.
Draft headings are shifted down one level by the defaults file, so
"#" in the draft = first-level subheading (centred bold).
]]

local stringify = pandoc.utils.stringify

local function esc(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

local function para(lines, style)
  local runs = {}
  for i, l in ipairs(lines) do
    if i > 1 then table.insert(runs, "<w:r><w:br/></w:r>") end
    table.insert(runs, '<w:r><w:t xml:space="preserve">' .. esc(l) .. "</w:t></w:r>")
  end
  return '<w:p><w:pPr><w:pStyle w:val="' .. (style or "TitlePage") ..
         '"/></w:pPr>' .. table.concat(runs) .. "</w:p>"
end

-- marker rsids read by fix_sections.py
local MARK = { title = "00A1A101", front = "00A1A102", body = "00A1A103" }

local function section_break(kind, extra)
  return '<w:p><w:pPr><w:sectPr w:rsidSect="' .. MARK[kind] .. '">' ..
         '<w:type w:val="nextPage"/>' ..
         '<w:pgSz w:w="12240" w:h="15840"/>' ..
         (extra or '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>') ..
         "</w:sectPr></w:pPr></w:p>"
end

local function raw(x) return pandoc.RawBlock("openxml", x) end

function Pandoc(doc)
  if FORMAT ~= "docx" then return doc end
  local m = doc.meta
  local title = m.title and stringify(m.title) or "Untitled"
  local author = m.author and stringify(m.author) or ""
  local date = m.date and stringify(m.date) or os.date("%B %-d, %Y")
  local inst = m.institution and stringify(m.institution) or ""
  local prof = m.professor and stringify(m.professor) or ""
  local course = m.course and stringify(m.course) or ""
  local bibtitle = m["bibliography-title"] and stringify(m["bibliography-title"]) or "Bibliography"

  local head = {}
  -- title page (sample 3.1)
  local tp = {}
  if inst ~= "" then table.insert(tp, para({ inst })) end
  table.insert(tp, para({ title }))
  local sub = {}
  if prof ~= "" then table.insert(sub, "Submitted to " .. prof) end
  if course ~= "" then
    table.insert(sub, "in partial fulfillment of")
    table.insert(sub, course)
  end
  if #sub > 0 then table.insert(tp, para(sub)) end
  table.insert(tp, para({ "by", author, date }))
  table.insert(head, raw(table.concat(tp) .. section_break("title",
    '<w:pgMar w:top="2880" w:right="1440" w:bottom="2880" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/><w:vAlign w:val="both"/>')))

  -- contents page (sample 3.2)
  if m.contents and stringify(m.contents) == "true" then
    table.insert(head, raw(
      '<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Contents</w:t></w:r></w:p>' ..
      '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>' ..
      '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>' ..
      '<w:r><w:fldChar w:fldCharType="separate"/></w:r>' ..
      '<w:r><w:t>Right-click and choose Update Field to build the contents.</w:t></w:r>' ..
      '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>' ..
      section_break("front")))
  end

  -- primary heading: the paper's title (sample 3.3)
  table.insert(head, pandoc.Header(1, pandoc.Str(title), { id = "title-heading", class = "unnumbered" }))

  local blocks = {}
  for _, b in ipairs(head) do table.insert(blocks, b) end
  for _, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.identifier == "refs" then
      table.insert(blocks, raw(section_break("body")))
      table.insert(blocks, pandoc.Header(1, pandoc.Str(bibtitle), { id = "bibliography", class = "unnumbered" }))
    end
    table.insert(blocks, b)
  end

  -- Pandoc would print its own title block; the title page replaces it.
  m.title, m.subtitle, m.author, m.date = nil, nil, nil, nil
  return pandoc.Pandoc(blocks, m)
end
