-- blog-final.lua: runs after citeproc. Removes citation settings from the
-- front matter and makes the Works Cited heading level 2 (the post title is
-- the page's level 1).
function Meta(m)
  m["suppress-bibliography"] = nil
  m["reference-section-title"] = nil
  for _, k in ipairs({ "nocite", "bibliography", "csl", "references",
      "citation-abbreviations", "link-citations", "lang" }) do
    m[k] = nil
  end
  return m
end

function Header(h)
  if h.level == 1 and pandoc.utils.stringify(h) == "Works Cited" then
    h.level = 2
    return h
  end
end
