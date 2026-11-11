"""Build a commentable Word document for one chapter, without re-executing it.

Why not `quarto render <chapter> --to docx`: this is a *book* project, so a book
is one document and Quarto renders all 28 chapters whatever file you name. That
costs half an hour and produces one enormous file.

Instead we take the executed markdown Quarto already cached in
`_freeze/chapters/<slug>/execute-results/html.json`, which has every code result
and every inline number already substituted, and hand it to pandoc. Nothing is
re-run, so a review document takes about a second.

Two things have to be translated on the way, because they are Quarto features
pandoc does not know:

* cross-references (`@sec-`, `@eq-`, `@fig-`, `@tbl-`) would otherwise print
  raw. They become short readable labels, which is better for a reviewer than a
  link they cannot click in Word anyway.
* callout divs become block quotes with a bold heading.

Usage
-----
    python tools/make-review-docx.py 23-rebalancing
    python tools/make-review-docx.py --all
"""
import argparse, io, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
FREEZE = os.path.join(ROOT, "_freeze", "chapters")
REVIEW = os.path.join(ROOT, "review")
BIB = os.path.join(ROOT, "assets", "bib", "references.bib")
QUARTO_BIN = r"C:\R\RStudio\resources\app\bin\quarto\bin"


def pandoc():
    for c in (shutil.which("pandoc"), os.path.join(QUARTO_BIN, "tools", "pandoc.exe"),
              os.path.join(QUARTO_BIN, "pandoc.exe")):
        if c and os.path.exists(c):
            return c
    for base, _, files in os.walk(os.path.dirname(QUARTO_BIN)):
        for f in files:
            if f.lower() == "pandoc.exe":
                return os.path.join(base, f)
    return None


def label_map():
    """anchor -> readable label, built from every chapter's headings."""
    out = {}
    for f in sorted(os.listdir(CH)):
        if not f.endswith(".qmd"):
            continue
        slug = f[:-4]
        num = re.match(r"(\d+)", slug)
        num = num.group(1).lstrip("0") if num else slug
        t = io.open(os.path.join(CH, f), encoding="utf-8").read()
        m = re.search(r'^title:\s*"(.*?)"', t, re.M)
        title = m.group(1) if m else slug
        for line in t.splitlines():
            m = re.match(r"#+\s+(.*?)\s*\{#(sec-[a-z0-9-]+)[^}]*\}", line)
            if m:
                out[m.group(2)] = "ch. %s § %s" % (num, m.group(1))
        for a in re.findall(r"\{#(eq-[a-z0-9-]+)\}", t):
            out[a] = "eq. " + a[3:]
        for a in re.findall(r"label:\s*(fig-[a-z0-9-]+)", t):
            out[a] = "fig. " + a[4:]
        for a in re.findall(r"label:\s*(tbl-[a-z0-9-]+)", t):
            out[a] = "tbl. " + a[4:]
    return out


CALLOUT = re.compile(
    r"^:::+\s*\{\.callout-(\w+)[^}]*\}\s*\n(?:##\s*(.*?)\n)?(.*?)^:::+\s*$",
    re.S | re.M)


def to_markdown(slug, labels):
    p = os.path.join(FREEZE, slug, "execute-results", "html.json")
    if not os.path.exists(p):
        raise SystemExit("no cached result for %s -- render the book first" % slug)
    md = json.load(io.open(p, encoding="utf-8"))["result"]["markdown"]

    # callouts -> block quotes, so they survive as visibly set-apart text
    def cb(m):
        kind, title, body = m.group(1), (m.group(2) or "").strip(), m.group(3)
        head = "> **%s%s**\n>\n" % (kind.upper(), (": " + title) if title else "")
        return head + "\n".join("> " + l for l in body.strip().splitlines())
    md = CALLOUT.sub(cb, md)

    # cross-references -> readable labels
    def rb(m):
        a = m.group(1)
        return "[%s]" % labels.get(a, a)
    md = re.sub(r"@((?:sec|eq|fig|tbl)-[a-z0-9-]+)", rb, md)

    # figures live beside the cached result
    md = re.sub(r"\]\(" + re.escape(slug) + r"_files/", "](figure-src/", md)
    md = md.replace("](figure-html/", "](figure-src/figure-html/")

    # citeproc only emits a bibliography where it is told to put one
    md += "\n\n# References {.unnumbered}\n\n::: {#refs}\n:::\n"
    return md


def build(slug, pd, labels):
    os.makedirs(REVIEW, exist_ok=True)
    # the scratch directory goes outside the project: this tree is synced by
    # SharePoint, which takes a handle on new folders and then refuses the
    # delete. Only the finished .docx is written into the project.
    work = tempfile.mkdtemp(prefix="tidyaa-review-")

    src = os.path.join(FREEZE, slug, "figure-html")
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join(work, "figure-src", "figure-html"))

    md_path = os.path.join(work, slug + ".md")
    io.open(md_path, "w", encoding="utf-8").write(to_markdown(slug, labels))

    out = os.path.join(REVIEW, slug + ".docx")
    cmd = [pd, md_path, "-o", out, "--from",
           "markdown+tex_math_dollars+raw_attribute", "--to", "docx",
           "--citeproc", "--bibliography", BIB,
           "--resource-path", work, "--metadata", "link-citations=true"]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=work)
    if r.returncode != 0:
        print(r.stdout[-2000:]); print(r.stderr[-2000:], file=sys.stderr)
        raise SystemExit("pandoc failed for %s" % slug)
    shutil.rmtree(work, ignore_errors=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    pd = pandoc()
    if not pd:
        raise SystemExit("pandoc not found")

    slugs = args.slugs
    if args.all:
        slugs = [d for d in sorted(os.listdir(FREEZE))
                 if os.path.exists(os.path.join(FREEZE, d, "execute-results",
                                                "html.json"))]
    if not slugs:
        raise SystemExit("name a chapter, or pass --all")

    labels = label_map()
    for s in slugs:
        out = build(s, pd, labels)
        print("%-34s %8.0f KB" % (os.path.basename(out),
                                  os.path.getsize(out) / 1024))


if __name__ == "__main__":
    main()
