"""Build the code downloads: one R script per chapter, an exercise scaffold, the
solutions, a setup script, and a zip with everything.

    python tools/build-code.py            # writes code/ and code/tidy-asset-allocation-code.zip

The chapter order comes from _quarto.yml. For every chapter chapters/NN-slug.qmd:

    code/NN-slug.R             every R chunk, in the order it runs in the book,
                               under a `## ---- label ----` header that
                               knitr::read_chunk() understands; a chunk the book
                               does not run (eval: false) is commented out
    code/NN-slug-exercises.R   the chapter's exercises as comments, each with a
                               place to work, after the chapter's data setup
    code/NN-slug-solutions.R   the chunks of chapters/solutions/NN-slug.qmd,
                               when that fragment exists

plus code/_common.R (a copy of R/_common.R), code/tables/ (the tables chapters
read), code/00-setup.R (installs the packages, pinned where the book pins them),
and code/README.md. The scripts run from the folder that holds them:
`source("R/_common.R")` becomes `source("_common.R")` and `"output/tables/"`
becomes `"tables/"`.

The zip is derived and gitignored; build it before a render, because Quarto
copies code/ into the site as a resource. The chapter banner
(tools/chapter-banner.lua) links to these files.
"""
import io, json, os, re, shutil, sys, textwrap, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE = os.path.join(ROOT, "code")
SITE = "https://www.tidy-pm.com/dev/"
ZIPNAME = "tidy-asset-allocation-code.zip"
WIDTH = 78


def read(path):
    return io.open(path, encoding="utf-8").read().replace("\r\n", "\n")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8", newline="\n").write(text)


# --- chapters in book order ---------------------------------------------------

def chapter_files():
    """chapters/NN-slug.qmd in the order of _quarto.yml, numbered chapters only."""
    yml = read(os.path.join(ROOT, "_quarto.yml"))
    files = re.findall(r"^\s*-\s*(chapters/\d\d-[\w-]+\.qmd)\s*$", yml, re.M)
    return [f for f in files if not f.startswith("chapters/9")]


def front_title(path):
    m = re.search(r"^title:\s*\"?(.+?)\"?\s*$", read(path), re.M)
    return m.group(1) if m else os.path.basename(path)


# --- chunk parsing (the same reading as tools/run-chapter.R) -------------------

FENCE_OPEN = re.compile(r"^```\{r([^}]*)\}\s*$")
FENCE_CLOSE = re.compile(r"^```\s*$")


def chunks(lines):
    """Yield dicts: label, eval, caption, code (list of lines), heading (the
    last markdown heading seen before the chunk)."""
    out, i, heading = [], 0, ""
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        h = re.match(r"^(#{1,6})\s+(.*?)\s*(\{.*\})?\s*$", lines[i])
        if h and not m:
            heading = h.group(2)
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not FENCE_CLOSE.match(lines[j]):
            j += 1
        body = lines[i + 1:j]
        opts = {}
        code = []
        for ln in body:
            o = re.match(r"^#\|\s*([\w-]+):\s*(.*)$", ln)
            if o:
                opts[o.group(1)] = o.group(2).strip().strip('"')
            elif ln.startswith("#|"):
                pass
            else:
                code.append(ln)
        hdr = m.group(1).strip().lstrip(",").strip()
        label = opts.get("label")
        if not label and hdr and "=" not in hdr.split(",")[0]:
            label = hdr.split(",")[0].strip()
        ev = opts.get("eval", "").lower()
        if not ev and re.search(r"eval\s*=\s*F", hdr):
            ev = "false"
        out.append({
            "label": label or "chunk-%d" % (len(out) + 1),
            "eval": ev not in ("false", "f"),
            "caption": opts.get("fig-cap") or opts.get("tbl-cap") or "",
            "code": code,
            "heading": heading,
        })
        i = j + 1
    return out


def relocate(line):
    return (line.replace('source("R/_common.R")', 'source("_common.R")')
                .replace('"output/tables/', '"tables/'))


def comment_block(text, prefix="# "):
    return "\n".join(prefix + l if l else prefix.rstrip() for l in text.split("\n"))


def render_chunk(ch):
    lines = ["## ---- %s ----" % ch["label"]]
    if ch["caption"]:
        cap = textwrap.fill(ch["caption"], WIDTH - 2)
        lines.append(comment_block(cap))
    code = [relocate(l) for l in ch["code"]]
    while code and not code[-1].strip():
        code.pop()
    if not ch["eval"]:
        lines.append("# Not run in the book; shown for the reader to try.")
        lines.extend("# " + l if l.strip() else "#" for l in code)
    else:
        lines.extend(code)
    return "\n".join(lines) + "\n\n"


def header(title, what, page):
    return (
        "# Tidy Asset Allocation in R\n"
        "# %s\n"
        "# %s\n"
        "#\n"
        "# %s\n"
        "# Run 00-setup.R once, then this file from the folder that holds it;\n"
        "# generated by tools/build-code.py from the book's source.\n\n"
    ) % (title, page, what)


# --- exercises ------------------------------------------------------------------

def strip_markdown(s):
    s = re.sub(r"@(sec|tbl|fig|eq)-(\d+)-([\w-]+)",
               lambda m: {"sec": "section", "tbl": "table", "fig": "figure",
                          "eq": "equation"}[m.group(1)]
               + " “%s” of chapter %d" % (m.group(3).replace("-", " "), int(m.group(2))), s)
    s = re.sub(r"\[?@([A-Za-z]\w+\d{4}\w*)\]?", r"\1", s)
    s = s.replace("`", "")
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    return " ".join(s.split())


def exercises(lines):
    """The numbered items of the `## Exercises` section, as plain text."""
    start = next((i for i, l in enumerate(lines) if re.match(r"^## Exercises", l)), None)
    if start is None:
        return []
    items, cur = [], None
    for l in lines[start + 1:]:
        if l.startswith("## "):
            break
        m = re.match(r"^(\d+)\.\s+(.*)$", l)
        if m:
            if cur:
                items.append(cur)
            cur = [m.group(2)]
        elif cur is not None and l.strip():
            cur.append(l.strip())
        elif cur is not None and not l.strip():
            cur.append("")
    if cur:
        items.append(cur)
    return [strip_markdown(" ".join(x for x in it if x)) for it in items]


def setup_chunks(chs):
    """The chapter's setup and data chunks: everything up to and including the
    first chunk whose label mentions data or load, else the first chunk."""
    cut = 1
    for k, ch in enumerate(chs):
        if re.search(r"data|load", ch["label"]):
            cut = k + 1
            break
    return [c for c in chs[:cut] if c["eval"]]


# --- main -----------------------------------------------------------------------

def main():
    # Clear the files, not the folders: the synced drive holds a folder handle
    # open now and then and rmdir fails with "access denied".
    for dirpath, _, names in os.walk(CODE):
        for name in names:
            os.remove(os.path.join(dirpath, name))
    os.makedirs(CODE, exist_ok=True)

    files = chapter_files()
    index = []
    for f in files:
        slug = os.path.basename(f)[:-4]
        num = int(slug[:2])
        title = front_title(os.path.join(ROOT, f))
        page = SITE + "chapters/%s.html" % slug
        lines = read(os.path.join(ROOT, f)).split("\n")
        chs = chunks(lines)

        # the chapter's code
        body = header("Chapter %d: %s" % (num, title), "The R code of the chapter, in the order it runs there.", page)
        last_heading = None
        for ch in chs:
            if ch["heading"] != last_heading and ch["heading"]:
                body += "# ===== %s =====\n\n" % ch["heading"]
                last_heading = ch["heading"]
            body += render_chunk(ch)
        write(os.path.join(CODE, slug + ".R"), body.rstrip("\n") + "\n")

        # the exercises
        exs = exercises(lines)
        ex = header("Chapter %d: %s" % (num, title) + " — exercises",
                    "The chapter's exercises, each with room to work. Solutions: %s-solutions.R and appendix G of the book." % slug, page)
        for ch in setup_chunks(chs):
            ex += render_chunk(ch)
        for k, text in enumerate(exs, 1):
            ex += "## ---- exercise-%d ----\n" % k
            ex += comment_block(textwrap.fill("%d. %s" % (k, text), WIDTH - 2, subsequent_indent="   ")) + "\n"
            ex += "\n# Your code:\n\n\n\n"
        write(os.path.join(CODE, slug + "-exercises.R"), ex.rstrip("\n") + "\n")

        # the solutions, when the fragment exists
        sol_path = os.path.join(ROOT, "chapters", "solutions", slug + ".qmd")
        has_sol = os.path.exists(sol_path)
        if has_sol:
            slines = read(sol_path).split("\n")
            sol = header("Chapter %d: %s" % (num, title) + " — solutions",
                         "The code of the worked solutions; the discussion is in appendix G of the book.", page)
            last_heading = None
            for ch in chunks(slines):
                if ch["heading"] != last_heading and ch["heading"]:
                    sol += "# ===== %s =====\n\n" % ch["heading"]
                    last_heading = ch["heading"]
                sol += render_chunk(ch)
            write(os.path.join(CODE, slug + "-solutions.R"), sol.rstrip("\n") + "\n")
        index.append((num, slug, title, len(chs), len(exs), has_sol))

    # shared files
    shutil.copy(os.path.join(ROOT, "R", "_common.R"), os.path.join(CODE, "_common.R"))
    tables = os.path.join(ROOT, "output", "tables")
    os.makedirs(os.path.join(CODE, "tables"), exist_ok=True)
    for name in os.listdir(tables):
        p = os.path.join(tables, name)
        if os.path.isfile(p) and name.lower().endswith((".csv", ".rds")):
            shutil.copy(p, os.path.join(CODE, "tables", name))

    # 00-setup.R: the CRAN list from chapter 1, the GitHub pins from renv.lock
    lock = json.loads(read(os.path.join(ROOT, "renv.lock")))
    ch1 = chunks(read(os.path.join(ROOT, "chapters", "01-setting-up.qmd")).split("\n"))
    cran = next((c for c in ch1 if c["label"] == "install-cran"), None)
    pins = []
    for pkg in ("tidypm", "PortfolioAnalytics", "uncertaintymeasures"):
        rec = lock["Packages"].get(pkg) or {}
        if rec.get("RemoteSha") and rec.get("RemoteUsername"):
            pins.append((pkg, "%s/%s@%s" % (rec["RemoteUsername"], rec["RemoteRepo"], rec["RemoteSha"])))
        elif pkg == "tidypm":
            # installed from the sibling checkout while the book is written;
            # readers take the public repository
            pins.append((pkg, "sstoeckl/tidypm"))
    setup = header("Setup", "Installs what the chapter scripts need. Run once.", SITE + "chapters/01-setting-up.html")
    setup += "# CRAN packages, as listed in chapter 1.\n"
    setup += "\n".join(cran["code"]).rstrip() + "\n\n" if cran else ""
    setup += 'install.packages("pak")\n\n'
    setup += ("# The companion package, the book's build of PortfolioAnalytics (the CRAN\n"
              "# release plus the fixes appendix D lists; CRAN's own build runs the scripts\n"
              "# too, with the traps the book documents), and the package chapter 28 uses.\n")
    for pkg, spec in pins:
        setup += 'pak::pak("%s")%s\n' % (spec, "" if pkg != "uncertaintymeasures" else "   # chapter 28 only")
    write(os.path.join(CODE, "00-setup.R"), setup)

    # README
    rows = "\n".join("| %d | %s | `%s.R` | `%s-exercises.R` (%d) | %s |" % (
        n, t, s, s, e, "`%s-solutions.R`" % s if hs else "—") for n, s, t, c, e, hs in index)
    readme = (
        "# Tidy Asset Allocation in R — the code\n\n"
        "One R script per chapter with the chapter's code in the order it runs in the\n"
        "book, an exercise file with room to work, and the solutions where the book has\n"
        "them. Everything runs on the modeled market that ships with the companion\n"
        "package, so no data download is needed.\n\n"
        "1. Run `00-setup.R` once. It installs the CRAN packages and the book's pinned\n"
        "   builds from GitHub.\n"
        "2. Open any chapter script and run it from this folder (`_common.R` and\n"
        "   `tables/` sit beside it).\n"
        "3. Work the exercises in `NN-slug-exercises.R`; compare with the solutions.\n\n"
        "The book is at <%s>. Generated by `tools/build-code.py` from the book's\n"
        "source; the scripts are derived files, so report a problem against the book.\n\n"
        "| Chapter | Title | Code | Exercises | Solutions |\n|---|---|---|---|---|\n%s\n"
    ) % (SITE, rows)
    write(os.path.join(CODE, "README.md"), readme)

    # the zip
    zpath = os.path.join(CODE, ZIPNAME)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, names in os.walk(CODE):
            for name in sorted(names):
                p = os.path.join(dirpath, name)
                if p == zpath:
                    continue
                arc = os.path.join("tidy-asset-allocation-code", os.path.relpath(p, CODE)).replace("\\", "/")
                z.write(p, arc)
    n_sol = sum(1 for r in index if r[5])
    print("code/: %d chapters, %d with solutions, %d exercises in all; %s is %.0f KB"
          % (len(index), n_sol, sum(r[4] for r in index), ZIPNAME, os.path.getsize(zpath) / 1024))


if __name__ == "__main__":
    sys.exit(main())
