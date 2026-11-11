-- A one-line banner under the title of every numbered chapter, HTML only:
-- the chapter's review status (review/status.csv), the code downloads that
-- tools/build-code.py writes into code/, and the slide deck when
-- slides/<slug>.qmd exists. Appendices and the preface get nothing.
--
-- Registered project-wide in _quarto.yml (`filters:`), so it runs on every
-- file and returns early unless the file is chapters/NN-slug.qmd. The chapters
-- stay untouched; the banner is assembled here so that a status change is one
-- line in the CSV rather than an edit in twenty-eight files.

local pdir  = quarto.project.directory
local input = quarto.doc.input_file or ""
local slug  = input:match("chapters[/\\](%d%d%-[%w%-]+)%.qmd$")

if not slug or not quarto.doc.is_format("html") then
  return {}
end

local LABEL = {
  draft = "Draft",
  alpha = "Alpha review",
  beta  = "Beta review",
  final = "Final",
}
local EXPLAIN = {
  draft = "complete, awaiting the author's read",
  alpha = "with the alpha reviewers",
  beta  = "with the beta readers",
  final = "reviewed and settled",
}

local function exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

local function status_row()
  local f = io.open(pdir .. "/review/status.csv", "r")
  if not f then return nil end
  local row, first = nil, true
  for line in f:lines() do
    if first then
      first = false
    else
      local file, status, since, note = line:match("^([^,]*),([^,]*),([^,]*),?(.*)$")
      if file == slug then
        row = { status = status, since = since, note = note or "" }
      end
    end
  end
  f:close()
  return row
end

local function esc(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

function Pandoc(doc)
  local st = status_row() or { status = "draft", since = "", note = "" }
  local status = LABEL[st.status] and st.status or "draft"
  local title = EXPLAIN[status]
  if st.since ~= "" then title = title .. " (since " .. st.since .. ")" end
  if st.note ~= "" then title = title .. ": " .. st.note end

  local parts = {}
  parts[#parts + 1] = string.format(
    '<span class="banner-status status-%s" title="%s">%s</span>',
    status, esc(title), LABEL[status])

  local code = {}
  if exists(pdir .. "/code/" .. slug .. ".R") then
    code[#code + 1] = string.format('<a href="../code/%s.R" download>script</a>', slug)
  end
  if exists(pdir .. "/code/" .. slug .. "-exercises.R") then
    code[#code + 1] = string.format('<a href="../code/%s-exercises.R" download>exercises</a>', slug)
  end
  if exists(pdir .. "/code/" .. slug .. "-solutions.R") then
    code[#code + 1] = string.format('<a href="../code/%s-solutions.R" download>solutions</a>', slug)
  end
  if #code > 0 then
    parts[#parts + 1] = '<span class="banner-code">Code: ' .. table.concat(code, " &middot; ") ..
      ' &middot; <a href="../code/tidy-asset-allocation-code.zip" download>all chapters</a></span>'
  end

  if exists(pdir .. "/slides/" .. slug .. ".qmd") then
    parts[#parts + 1] = string.format('<span class="banner-slides"><a href="../slides/%s.html">Slides</a></span>', slug)
  end

  parts[#parts + 1] = '<span class="banner-annotate">To comment, select a passage and annotate it; see ' ..
    '<a href="https://github.com/sstoeckl/tidy-asset-allocation/blob/main/REVIEWING.md">how reviews work</a>.</span>'

  local html = '<div class="chapter-banner">' .. table.concat(parts, '<span class="banner-sep">|</span>') .. '</div>'
  table.insert(doc.blocks, 1, pandoc.RawBlock("html", html))
  return doc
end
