-- blog.lua: tidy a draft for Hugo.
--  * drops %% author notes %% (Obsidian comments) so they never publish;
--  * keeps only front-matter keys Hugo uses (title, subtitle, author, date,
--    draft, tags, categories, summary, description, slug), so citation
--    settings and piece notes don't leak into the page.
local keep = { title = 1, subtitle = 1, author = 1, date = 1, draft = 1, tags = 1,
  categories = 1, summary = 1, description = 1, slug = 1,
  ["reference-section-title"] = 1, ["suppress-bibliography"] = 1, nocite = 1,
  bibliography = 1, csl = 1, references = 1, ["citation-abbreviations"] = 1,
  ["link-citations"] = 1, lang = 1 }

function Meta(m)
  for k, _ in pairs(m) do
    if not keep[k] then m[k] = nil end
  end
  return m
end

local function strip_comments(blocks)
  local out, inside = {}, false
  for _, b in ipairs(blocks) do
    local t = pandoc.utils.stringify(b)
    if b.t == "Para" or b.t == "Plain" then
      local starts = t:match("^%%%%")
      local ends = t:match("%%%%$")
      if starts and ends then goto continue end
      if starts then inside = true; goto continue end
      if inside then
        if ends then inside = false end
        goto continue
      end
    end
    table.insert(out, b)
    ::continue::
  end
  return out
end

function Pandoc(doc)
  doc.blocks = strip_comments(doc.blocks)
  return doc
end
