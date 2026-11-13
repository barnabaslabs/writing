-- Stop the build if the draft still holds an unverified citation flag ([@? ...]).
local function check(text)
  if text:find("%[@%?") or text:find("@%?") then
    io.stderr:write("block-unverified: unresolved [@? flag found; verify the citation first\n")
    os.exit(1)
  end
end
function Str(s) check(s.text) end
function Cite(c)
  for _, x in ipairs(c.citations) do
    if x.id:sub(1, 1) == "?" then check("@?") end
  end
end
