"""Assemble the reverse outline (review/outline/NN-slug.md, one per chapter, in
the format of review/outline/FORMAT.md) into one page for reading top down:
parts and chapters, then sections, then paragraphs, with a switch for the
level shown. The page is published as a Claude Artifact so that comments can
be anchored to any line.

    python tools/build-outline.py            # writes review/outline/index.html
"""
import html, io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "review", "outline")
PAGE = os.path.join(OUT, "index.html")

TYPES = ["claim", "evidence", "definition", "derivation", "method", "code", "result",
         "caveat", "transition", "example", "takeaway", "exercise"]


def read(p):
    return io.open(p, encoding="utf-8").read().replace("\r\n", "\n")


# --- the book's order --------------------------------------------------------

def book_order():
    """[(part, [(slug, file)])] from _quarto.yml, the preface first."""
    yml = read(os.path.join(ROOT, "_quarto.yml"))
    parts, part, items = [], "Front matter", []
    in_chapters = False
    for line in yml.split("\n"):
        if re.match(r"^\s*chapters:\s*$", line) and not in_chapters:
            in_chapters = True
            continue
        if in_chapters and re.match(r"^\s*appendices:", line):
            break
        if not in_chapters:
            continue
        m = re.match(r'^\s*-\s*part:\s*"?(.+?)"?\s*$', line)
        if m:
            if items:
                parts.append((part, items))
            part, items = m.group(1), []
            continue
        m = re.match(r"^\s*-\s*(index\.qmd|chapters/(\d\d)-[\w-]+\.qmd)\s*$", line)
        if m:
            f = m.group(1)
            slug = "00-preface" if f == "index.qmd" else os.path.basename(f)[:-4]
            if not slug.startswith("99"):
                items.append((slug, f))
    if items:
        parts.append((part, items))
    return parts


# --- parsing one outline file -----------------------------------------------------

def parse_outline(text):
    """A dict: meta, chapter (fields), sections (list of dicts with level,
    title, words, says, why, paras, note)."""
    lines = text.split("\n")
    meta, i = {}, 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m = re.match(r"^([\w-]+):\s*(.*)$", lines[i])
            if m:
                meta[m.group(1)] = m.group(2).strip().strip('"')
            i += 1
        i += 1
    chapter, sections, cur, mode = {}, [], None, None
    fields = ("Claim", "Question", "Why here", "Does", "Order", "Says", "Note")
    for line in lines[i:]:
        s = line.rstrip()
        if re.match(r"^# Chapter\s*$", s):
            mode, cur = "chapter", None
            continue
        if re.match(r"^# Sections\s*$", s):
            mode, cur = "sections", None
            continue
        m = re.match(r"^(##|###)\s+(.*?)\s*(?:[—–-]+\s*([\d,.~ ]+)\s*(?:words)?)?\s*$", s)
        if m and mode == "sections":
            title = m.group(2).strip()
            if re.match(r"^\(?opening\b", title, re.I):
                title = "Opening (before the first heading)"
            cur = {"level": len(m.group(1)), "title": title, "words": (m.group(3) or "").strip(),
                   "says": "", "why": "", "paras": [], "note": ""}
            sections.append(cur)
            continue
        fm = re.match(r"^(Claim|Question|Why here|Does|Order|Says|Note):\s*(.*)$", s)
        if fm:
            key, val = fm.group(1), fm.group(2).strip()
            if mode == "chapter" or cur is None:
                chapter[key] = (chapter.get(key, "") + " " + val).strip()
            else:
                k = {"Says": "says", "Why here": "why", "Note": "note"}.get(key, key.lower())
                cur[k] = (cur.get(k, "") + " " + val).strip()
            last = ("chapter", key) if (mode == "chapter" or cur is None) else ("section", k)
            continue
        if re.match(r"^Paragraphs:\s*$", s):
            last = None
            continue
        pre = re.match(r"^\s*-?\s*\(code:\s*([^)]+)\)\s*$", s)
        if pre and cur is None:
            # a chunk that sits before the first section, e.g. the setup chunk
            chapter.setdefault("Code before the first section", "")
            chapter["Code before the first section"] = (chapter["Code before the first section"] + " `" + pre.group(1).strip() + "`").strip()
            last = None
            continue
        bm = re.match(r"^\s*-\s+(.*)$", s)
        if bm and cur is not None:
            item = bm.group(1).strip()
            cm = re.match(r"^\(code:\s*([^)]+)\)[\s,;:]*(.*)$", item)
            if cm:
                cur["paras"].append({"kind": "code", "label": cm.group(1).strip(), "note": cm.group(2).strip()})
                last = None
                continue
            am = re.match(r"^\((table|figure|none|callout)\b:?\s*([^)]*)\)\s*(.*)$", item)
            if am:
                cur["paras"].append({"kind": "aside", "what": am.group(1),
                                     "text": (am.group(2) + " " + am.group(3)).strip()})
                last = None
                continue
            pm = re.match(r"^¶?\s*(\d+)?\s*\[(\w+)\]\s*(\(callout\))?\s*(.*)$", item)
            if pm:
                cur["paras"].append({"kind": "para", "n": pm.group(1) or "", "type": pm.group(2).lower(),
                                     "callout": bool(pm.group(3)), "text": pm.group(4).strip()})
            else:
                cur["paras"].append({"kind": "para", "n": "", "type": "", "callout": False, "text": item})
            last = None
            continue
        # continuation of a wrapped field
        if s.strip() and cur is not None and cur["paras"] and not s.startswith("#"):
            p = cur["paras"][-1]
            if p["kind"] == "para" and "last" in dir() and last is None:
                p["text"] = (p["text"] + " " + s.strip()).strip()
                continue
        if s.strip() and "last" in dir() and last:
            where, key = last
            if where == "chapter":
                chapter[key] = (chapter.get(key, "") + " " + s.strip()).strip()
            elif cur is not None:
                cur[key] = (cur.get(key, "") + " " + s.strip()).strip()
    return {"meta": meta, "chapter": chapter, "sections": sections}


# --- the book and part level (review/outline/parts.md) ------------------------------

def parse_parts(text):
    """`# Book` and `# Part: <name>` blocks, each with `Key: value` fields
    (continuation lines allowed) and bullet lists under a `Key:` line that
    has no value. Returns {"book": {...}, "parts": {name: {...}}}; a field is
    a string, a list field a list of strings."""
    out = {"book": {}, "parts": {}}
    cur, key = None, None
    for line in text.split("\n"):
        s = line.rstrip()
        if re.match(r"^# Book\s*$", s):
            cur, key = out["book"], None
            continue
        m = re.match(r"^# Part:\s*(.+?)\s*$", s)
        if m:
            cur = out["parts"].setdefault(m.group(1), {})
            key = None
            continue
        if cur is None or not s.strip():
            continue
        m = re.match(r"^([A-Z][\w ]{1,40}):\s*(.*)$", s)
        if m and not s.startswith("- "):
            key = m.group(1)
            cur[key] = m.group(2).strip() if m.group(2).strip() else []
            continue
        b = re.match(r"^\s*-\s+(.*)$", s)
        if b and key is not None and isinstance(cur.get(key), list):
            cur[key].append(b.group(1).strip())
            continue
        if key is not None:
            if isinstance(cur[key], list) and cur[key]:
                cur[key][-1] = (cur[key][-1] + " " + s.strip()).strip()
            elif isinstance(cur[key], str):
                cur[key] = (cur[key] + " " + s.strip()).strip()
    return out


def render_fields(block, order):
    rows = []
    for key in order:
        val = block.get(key)
        if not val:
            continue
        if isinstance(val, list):
            items = "".join("<li>%s</li>" % inline(v) for v in val)
            rows.append('<dt>%s</dt><dd><ul class="plain">%s</ul></dd>' % (esc(key), items))
        else:
            cls = ' class="unstated"' if (key == "Why here" and val.lower().startswith("not stated")) else ""
            rows.append('<dt>%s</dt><dd%s>%s</dd>' % (esc(key), cls, inline(val)))
    return '<dl class="fields">%s</dl>' % "".join(rows) if rows else ""


# --- rendering -----------------------------------------------------------------------

def esc(s):
    return html.escape(s or "", quote=True)


def inline(s):
    """Backticks to code, nothing else."""
    s = esc(s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def type_counts(sections):
    counts = {}
    for sec in sections:
        for p in sec["paras"]:
            if p["kind"] == "para" and p["type"]:
                counts[p["type"]] = counts.get(p["type"], 0) + 1
    return counts


def render_chapter(num, slug, title, data, missing):
    cid = "ch-" + slug[:2]
    if missing:
        return ('<article class="chapter missing" id="%s"><header><h3><span class="num">%s</span> %s</h3>'
                '<p class="muted">Not outlined yet.</p></header></article>' % (cid, num, esc(title)))
    ch, secs, meta = data["chapter"], data["sections"], data["meta"]
    counts = type_counts(secs)
    chips = "".join('<span class="chip t-%s">%s %d</span>' % (t, t, counts[t]) for t in TYPES if t in counts)
    stats = []
    if meta.get("words"):
        stats.append("%s words" % meta["words"])
    if meta.get("sections"):
        stats.append("%s sections" % meta["sections"])
    if meta.get("paragraphs"):
        stats.append("%s paragraphs" % meta["paragraphs"])
    out = ['<article class="chapter" id="%s">' % cid,
           '<header><h3><span class="num">%s</span> %s</h3>' % (num, esc(meta.get("title") or title)),
           '<p class="stats">%s</p>' % " · ".join(stats),
           '<dl class="fields">']
    for key in ("Claim", "Question", "Why here", "Does", "Order", "Code before the first section"):
        if ch.get(key):
            label = "Code first" if key.startswith("Code") else key
            out.append('<dt>%s</dt><dd>%s</dd>' % (label, inline(ch[key])))
    out.append('</dl>')
    if chips:
        out.append('<p class="chips">%s</p>' % chips)
    out.append('</header>')
    for sec in secs:
        lvl = "sub" if sec["level"] == 3 else "top"
        out.append('<section class="section %s">' % lvl)
        words = (' <span class="words">%s words</span>' % esc(sec["words"])) if sec["words"] else ""
        out.append('<h4>%s%s</h4>' % (esc(sec["title"]), words))
        out.append('<dl class="fields">')
        if sec["says"]:
            out.append('<dt>Says</dt><dd>%s</dd>' % inline(sec["says"]))
        if sec["why"]:
            cls = ' class="unstated"' if sec["why"].lower().startswith("not stated") else ""
            out.append('<dt>Why here</dt><dd%s>%s</dd>' % (cls, inline(sec["why"])))
        out.append('</dl>')
        if sec["paras"]:
            out.append('<ol class="paras">')
            for p in sec["paras"]:
                if p["kind"] == "code":
                    note = (' <span class="codenote">%s</span>' % inline(p["note"])) if p.get("note") else ""
                    out.append('<li class="code-line"><span class="chip t-code">code</span> <span><code>%s</code>%s</span></li>' % (esc(p["label"]), note))
                elif p["kind"] == "aside":
                    out.append('<li class="code-line"><span class="chip">%s</span> <span>%s</span></li>' % (esc(p["what"]), inline(p["text"])))
                else:
                    t = p["type"] or "untyped"
                    co = ' <span class="callout">callout</span>' if p["callout"] else ""
                    n = ('<span class="pn">¶%s</span> ' % esc(p["n"])) if p["n"] else ""
                    out.append('<li class="para"><span class="chip t-%s">%s</span>%s %s%s</li>' % (t, t, co, n, inline(p["text"])))
            out.append('</ol>')
        if sec["note"]:
            out.append('<p class="note"><span class="note-label">Note</span> %s</p>' % inline(sec["note"]))
        out.append('</section>')
    out.append('</article>')
    return "\n".join(out)


CSS = r"""
:root {
  /* Layout: a fixed left rail with the parts and chapters; one reading column
     with a level switch pinned at the top. The book's own palette and face. */
  --bg: #FFFFFF; --surface: #F6F8FA; --fg: #212529; --muted: #6C757D; --rule: #DEE2E6;
  --accent: #2E77A6; --accent-soft: #EAF2F8; --accent-deep: #1B4F6F; --warn: #D6A419; --warn-soft: #FBF3DC;
  --font: "Source Sans 3", "Source Sans Pro", -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mono: "IBM Plex Mono", SFMono-Regular, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #15191E; --surface: #1C2229; --fg: #E6E9ED; --muted: #9AA4AE; --rule: #2E3741;
  --accent: #6FB1DC; --accent-soft: #1E3346; --accent-deep: #BFE0F5; --warn: #E2B64A; --warn-soft: #3A3119; color-scheme: dark; } }
:root[data-theme="dark"] {
  --bg: #15191E; --surface: #1C2229; --fg: #E6E9ED; --muted: #9AA4AE; --rule: #2E3741;
  --accent: #6FB1DC; --accent-soft: #1E3346; --accent-deep: #BFE0F5; --warn: #E2B64A; --warn-soft: #3A3119; color-scheme: dark; }
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--fg); font-family: var(--font); font-size: 16px; line-height: 1.5; margin: 0; }
a { color: var(--accent); text-decoration: none; } a:hover { text-decoration: underline; }
code { font-family: var(--mono); font-size: 0.86em; background: var(--accent-soft); padding: 0.05em 0.3em; border-radius: 3px; }
.shell { display: grid; grid-template-columns: 260px minmax(0, 1fr); min-height: 100%; }
nav.rail { position: sticky; top: env(safe-area-inset-top, 0px); align-self: start; height: calc(100vh - env(safe-area-inset-top, 0px)); overflow-y: auto;
  border-right: 1px solid var(--rule); background: var(--surface); padding-block: 1rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: 12px; font-size: 0.9rem; }
nav.rail h1 { font-size: 1rem; margin: 0 0 0.25rem; letter-spacing: -0.01em; }
nav.rail h1::before { content: ""; display: block; width: 2.4rem; height: 4px; background: var(--accent); margin-bottom: 0.5rem; }
nav.rail .sub { color: var(--muted); font-size: 0.8rem; margin: 0 0 1rem; }
nav.rail .part { font-size: 0.72rem; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); margin: 0.9rem 0 0.25rem; }
nav.rail ul { list-style: none; margin: 0; padding: 0; }
nav.rail li a { display: block; padding: 0.15rem 0.4rem; border-radius: 3px; color: var(--fg); }
nav.rail li a:hover { background: var(--accent-soft); text-decoration: none; }
nav.rail li a .n { color: var(--muted); font-variant-numeric: tabular-nums; display: inline-block; width: 1.6em; }
nav.rail li.missing a { color: var(--muted); }
main { padding-block: 1rem 4rem; padding-left: 2rem; padding-right: max(16px, env(safe-area-inset-right, 0px)); max-width: 78ch; }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--rule);
  display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; align-items: center; padding: 0.6rem 0; margin-bottom: 1.5rem; }
.bar .label { font-size: 0.72rem; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); }
.bar button { font: inherit; font-size: 0.88rem; padding: 0.3rem 0.8rem; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); border-radius: 4px; cursor: pointer; }
.bar button[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: #fff; }
.bar button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.bar .hint { color: var(--muted); font-size: 0.85rem; }
h2.part { font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 2.5rem 0 0.8rem; padding-top: 0.6rem; border-top: 1px solid var(--rule); }
h2.part .roman { color: var(--accent); margin-right: 0.5rem; }
article.chapter { margin: 0 0 2.2rem; }
article.chapter > header h3 { font-size: 1.35rem; margin: 0 0 0.2rem; letter-spacing: -0.015em; text-wrap: balance; }
article.chapter > header h3 .num { color: var(--accent); font-variant-numeric: tabular-nums; margin-right: 0.35rem; }
.stats { color: var(--muted); font-size: 0.85rem; margin: 0 0 0.6rem; font-variant-numeric: tabular-nums; }
dl.fields { display: grid; grid-template-columns: 6.2em minmax(0, 1fr); gap: 0.25rem 0.8rem; margin: 0 0 0.6rem; }
dl.fields dt { font-size: 0.72rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); padding-top: 0.25em; }
dl.fields dd { margin: 0; }
dl.fields dd.unstated { color: var(--warn); }
dl.fields dd.unstated::before { content: "▲ "; font-size: 0.8em; }
.chips { margin: 0.2rem 0 0; display: flex; flex-wrap: wrap; gap: 0.3rem; }
.chip { display: inline-block; font-size: 0.7rem; letter-spacing: 0.04em; text-transform: uppercase; padding: 0.08em 0.45em; border-radius: 3px;
  background: var(--surface); color: var(--muted); border: 1px solid var(--rule); white-space: nowrap; font-variant-numeric: tabular-nums; }
.chip.t-claim, .chip.t-takeaway { background: var(--accent-soft); color: var(--accent-deep); border-color: transparent; }
.chip.t-evidence, .chip.t-result { background: var(--accent-soft); color: var(--accent-deep); border-color: transparent; opacity: 0.85; }
.chip.t-transition { background: var(--warn-soft); color: var(--warn); border-color: transparent; }
.chip.t-caveat { border-color: var(--warn); color: var(--warn); }
.chip.t-code { font-family: var(--mono); text-transform: none; }
section.section { margin: 1.1rem 0 0 0; padding-left: 0.9rem; border-left: 2px solid var(--rule); }
section.section.sub { margin-left: 1.2rem; border-left-style: dotted; }
section.section h4 { font-size: 1.02rem; margin: 0 0 0.35rem; }
section.section h4 .words { color: var(--muted); font-weight: 400; font-size: 0.8rem; margin-left: 0.5rem; font-variant-numeric: tabular-nums; }
ol.paras { list-style: none; margin: 0.3rem 0 0.4rem; padding: 0; display: grid; gap: 0.3rem; }
ol.paras li { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.5rem; align-items: baseline; font-size: 0.95rem; }
ol.paras li .pn { color: var(--muted); font-variant-numeric: tabular-nums; margin-right: 0.3rem; }
ol.paras li .callout { font-size: 0.7rem; color: var(--warn); letter-spacing: 0.04em; text-transform: uppercase; margin-right: 0.3rem; }
ol.paras li.code-line { color: var(--muted); font-size: 0.85rem; }
.note { background: var(--warn-soft); border-radius: 4px; padding: 0.4rem 0.7rem; font-size: 0.92rem; margin: 0.4rem 0 0; }
.note .note-label { font-size: 0.7rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--warn); margin-right: 0.4rem; }
.muted { color: var(--muted); }
article.book { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px; padding: 1rem 1.1rem; margin: 0 0 1rem; }
article.book h3 { font-size: 1.2rem; margin: 0 0 0.6rem; letter-spacing: -0.01em; }
.partblock { margin: 0 0 1.4rem; padding: 0.2rem 0 0.2rem 0.9rem; border-left: 3px solid var(--accent); }
ul.plain { margin: 0; padding-left: 1.1rem; display: grid; gap: 0.3rem; }
html[data-level="chapters"] section.section { display: none; }
html[data-level="chapters"] .chips { display: none; }
html[data-level="sections"] ol.paras { display: none; }
html[data-level="sections"] li.code-line { display: none; }
.legend { color: var(--muted); font-size: 0.85rem; margin: 0 0 1rem; }
@media (max-width: 860px) {
  .shell { grid-template-columns: 1fr; }
  nav.rail { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--rule); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
  main { padding-left: max(16px, env(safe-area-inset-left, 0px)); }
}
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; } }
html { scroll-behavior: smooth; }
"""

JS = r"""
(function () {
  var root = document.documentElement;
  var buttons = document.querySelectorAll('.bar button[data-level]');
  function setLevel(l, store) {
    root.setAttribute('data-level', l);
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-level') === l ? 'true' : 'false'); });
    if (store) { try { localStorage.setItem('outline-level', l); } catch (e) {} }
  }
  var saved = null;
  try { saved = localStorage.getItem('outline-level'); } catch (e) {}
  setLevel(saved || 'sections', false);
  buttons.forEach(function (b) { b.addEventListener('click', function () { setLevel(b.getAttribute('data-level'), true); }); });
})();
"""

ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def main():
    parts = book_order()
    nav, body = [], []
    done, total = 0, 0
    pn = 0
    top_path = os.path.join(OUT, "parts.md")
    top = parse_parts(read(top_path)) if os.path.exists(top_path) else {"book": {}, "parts": {}}
    if top["book"]:
        nav.append('<ul><li><a href="#book"><span class="n"></span>The book as a whole</a></li></ul>')
        body.append('<article class="book" id="book"><h3>The book as a whole</h3>%s</article>' % render_fields(
            top["book"], ("Claim", "What the chapters jointly argue", "Order", "Why this order",
                          "Dependencies against the order", "Patterns across chapters", "Open at the top level")))
    for part, items in parts:
        is_front = part == "Front matter"
        if not is_front:
            pn += 1
        nav.append('<p class="part">%s</p><ul>' % esc(("%s · " % ROMAN[pn] if not is_front else "") + part))
        body.append('<h2 class="part" id="part-%d">%s%s</h2>' % (pn, ('<span class="roman">%s</span>' % ROMAN[pn]) if not is_front else "", esc(part)))
        if part in top["parts"]:
            body.append('<div class="partblock">%s</div>' % render_fields(top["parts"][part], ("Says", "Why here", "Chapters", "Note")))
        for slug, f in items:
            total += 1
            num = "" if slug == "00-preface" else str(int(slug[:2]))
            title = "Preface"
            if slug != "00-preface":
                src = read(os.path.join(ROOT, f))
                m = re.search(r'^title:\s*"?(.+?)"?\s*$', src, re.M)
                title = m.group(1) if m else slug
            p = os.path.join(OUT, slug + ".md")
            missing = not os.path.exists(p)
            data = None if missing else parse_outline(read(p))
            if not missing:
                done += 1
            nav.append('<li%s><a href="#ch-%s"><span class="n">%s</span>%s</a></li>' % (
                ' class="missing"' if missing else "", slug[:2], esc(num), esc(title)))
            body.append(render_chapter(num, slug, title, data, missing))
        nav.append('</ul>')

    page = (
        '<title>Tidy Asset Allocation Outline</title>\n'
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap">\n'
        '<style>%s</style>\n'
        '<div class="shell">\n<nav class="rail"><h1>Tidy Asset Allocation in R</h1><p class="sub">Reverse outline · %d of %d chapters · what each part, chapter, section and paragraph does, as the text stands</p>%s</nav>\n'
        '<main>\n<div class="bar"><span class="label">Level</span>'
        '<button type="button" id="lvl-chapters" data-level="chapters" aria-pressed="false">Parts and chapters</button>'
        '<button type="button" id="lvl-sections" data-level="sections" aria-pressed="true">Sections</button>'
        '<button type="button" id="lvl-paragraphs" data-level="paragraphs" aria-pressed="false">Paragraphs</button>'
        '<span class="hint">Select any line to comment on it.</span></div>\n'
        '<p class="legend">Each unit says what it <em>says</em> and <em>why it comes here</em>, as the text itself gives the reason; a ▲ marks an order the text never justifies. Paragraph chips name what a paragraph does: claim, evidence, definition, derivation, method, code, result, caveat, transition, example, takeaway, exercise.</p>\n'
        '%s\n</main>\n</div>\n<script>%s</script>\n'
    ) % (CSS, done, total, "\n".join(nav), "\n".join(body), JS)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(page)
    print("outline page: %d of %d chapters outlined, %d KB -> %s" % (done, total, len(page.encode("utf-8")) // 1024, os.path.relpath(PAGE, ROOT)))


if __name__ == "__main__":
    main()
