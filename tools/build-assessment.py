"""Assemble the structural assessment (review/assessment/*.md: a synthesis and
the reviewers' reports) into one page for reading and commenting, published as
a Claude Artifact like the reverse outline.

    python tools/build-assessment.py        # writes review/assessment/index.html

Markdown is converted by the pandoc that ships with Quarto.
"""
import html, io, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "review", "assessment")
PAGE = os.path.join(DIR, "index.html")
QUARTO = r"C:\R\RStudio\resources\app\bin\quarto\bin\quarto.exe"

DOCS = [
    ("00-synthesis.md", "synthesis", "Synthesis"),
    ("01-architecture.md", "architecture", "Report 1 · Order and dependencies"),
    ("02-audience.md", "audience", "Report 2 · Readers and teachability"),
    ("03-chapter-form.md", "build", "Report 3 · The build of a chapter"),
]


def pandoc(path):
    out = subprocess.run([QUARTO, "pandoc", path, "-f", "gfm+tex_math_dollars", "-t", "html",
                          "--mathml", "--wrap=none", "--no-highlight"],
                         capture_output=True)
    if out.returncode != 0:
        sys.exit("pandoc failed on %s: %s" % (path, out.stderr.decode("utf-8", "replace")[:400]))
    return out.stdout.decode("utf-8")


def process(frag, slug, label):
    """Demote headings by one, give the sections ids, wrap tables, and return
    the fragment with its list of (id, title) sections."""
    frag = re.sub(r"<h1[^>]*>.*?</h1>", "", frag, count=1, flags=re.S)       # the page sets its own title
    sections = []

    def h2(m):
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        sid = "%s-%d" % (slug, len(sections) + 1)
        sections.append((sid, html.unescape(title)))
        return '<h3 id="%s">%s</h3>' % (sid, m.group(2))

    frag = re.sub(r"<h4([^>]*)>(.*?)</h4>", r"<h5>\2</h5>", frag, flags=re.S)
    frag = re.sub(r"<h3([^>]*)>(.*?)</h3>", r"<h4>\2</h4>", frag, flags=re.S)
    frag = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2, frag, flags=re.S)
    frag = frag.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    return frag, sections


CSS = r"""
:root {
  /* Layout: a fixed left rail with the four documents and their sections; one
     reading column. The book's own palette and face, as on the outline. */
  --bg: #FFFFFF; --surface: #F6F8FA; --fg: #212529; --muted: #6C757D; --rule: #DEE2E6;
  --accent: #2E77A6; --accent-soft: #EAF2F8; --accent-deep: #1B4F6F; --warn: #9A6B00; --warn-soft: #FBF3DC;
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
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--fg); font-family: var(--font); font-size: 17px; line-height: 1.55; margin: 0; }
a { color: var(--accent); text-decoration: none; } a:hover { text-decoration: underline; }
code { font-family: var(--mono); font-size: 0.85em; background: var(--accent-soft); padding: 0.05em 0.3em; border-radius: 3px; }
pre { background: var(--surface); border: 1px solid var(--rule); border-radius: 4px; padding: 0.7rem 0.9rem; overflow-x: auto; }
pre code { background: none; padding: 0; }
.shell { display: grid; grid-template-columns: 270px minmax(0, 1fr); min-height: 100%; }
nav.rail { position: sticky; top: env(safe-area-inset-top, 0px); align-self: start; height: calc(100vh - env(safe-area-inset-top, 0px)); overflow-y: auto;
  border-right: 1px solid var(--rule); background: var(--surface); padding-block: 1rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: 12px; font-size: 0.88rem; }
nav.rail h1 { font-size: 1rem; margin: 0 0 0.25rem; letter-spacing: -0.01em; }
nav.rail h1::before { content: ""; display: block; width: 2.4rem; height: 4px; background: var(--accent); margin-bottom: 0.5rem; }
nav.rail .sub { color: var(--muted); font-size: 0.8rem; margin: 0 0 0.8rem; }
nav.rail .doc { font-weight: 600; margin: 0.9rem 0 0.2rem; }
nav.rail .doc a { color: var(--fg); }
nav.rail ul { list-style: none; margin: 0; padding: 0; }
nav.rail li a { display: block; padding: 0.12rem 0.4rem; border-radius: 3px; color: var(--muted); }
nav.rail li a:hover { background: var(--accent-soft); color: var(--fg); text-decoration: none; }
main { padding-block: 1.4rem 5rem; padding-left: 2.2rem; padding-right: max(16px, env(safe-area-inset-right, 0px)); max-width: 82ch; min-width: 0; }
article { margin: 0 0 3.5rem; }
article > h2 { font-size: 1.75rem; letter-spacing: -0.02em; line-height: 1.15; margin: 0 0 0.3rem; padding-top: 0.9rem; position: relative; text-wrap: balance; }
article > h2::before { content: ""; position: absolute; top: 0; left: 0; width: 3.25rem; height: 4px; background: var(--accent); }
article .kicker { color: var(--muted); font-size: 0.85rem; margin: 0 0 1.4rem; }
article.report { border-top: 1px solid var(--rule); padding-top: 1.6rem; }
h3 { font-size: 1.3rem; margin: 2.2rem 0 0.7rem; letter-spacing: -0.01em; text-wrap: balance; }
h4 { font-size: 1.05rem; margin: 1.6rem 0 0.5rem; }
h5 { font-size: 0.95rem; margin: 1.3rem 0 0.4rem; }
p { margin: 0 0 0.9rem; }
ul, ol { padding-left: 1.3rem; margin: 0 0 0.9rem; }
li { margin-bottom: 0.3rem; }
blockquote { margin: 0 0 0.9rem; padding: 0.5rem 0.9rem; border-left: 3px solid var(--accent); background: var(--accent-soft); border-radius: 0 4px 4px 0; }
blockquote p:last-child { margin-bottom: 0; }
.tablewrap { overflow-x: auto; margin: 0 0 1.1rem; }
table { border-collapse: collapse; font-size: 0.9rem; font-variant-numeric: tabular-nums; min-width: 100%; }
th, td { padding: 0.4rem 0.6rem; border-bottom: 1px solid var(--rule); text-align: left; vertical-align: top; }
thead th { border-bottom: 1.5px solid var(--fg); font-weight: 600; white-space: nowrap; }
article.synthesis ol > li { margin-bottom: 0.8rem; }
article.synthesis ol > li em { color: var(--accent-deep); }
@media (max-width: 880px) {
  .shell { grid-template-columns: 1fr; }
  nav.rail { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--rule); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
  main { padding-left: max(16px, env(safe-area-inset-left, 0px)); }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
"""


def main():
    nav, body = [], []
    for fname, slug, label in DOCS:
        path = os.path.join(DIR, fname)
        if not os.path.exists(path):
            continue
        frag, sections = process(pandoc(path), slug, label)
        nav.append('<p class="doc"><a href="#%s">%s</a></p><ul>%s</ul>' % (
            slug, html.escape(label),
            "".join('<li><a href="#%s">%s</a></li>' % (sid, html.escape(t)) for sid, t in sections)))
        cls = "synthesis" if slug == "synthesis" else "report"
        kicker = ("What the three reports say taken together, and what has to be decided."
                  if slug == "synthesis" else "Unabridged, as the reviewer wrote it.")
        body.append('<article class="%s" id="%s"><h2>%s</h2><p class="kicker">%s</p>%s</article>' % (
            cls, slug, html.escape(label), kicker, frag))
    page = (
        '<title>Tidy Asset Allocation Assessment</title>\n'
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap">\n'
        '<style>%s</style>\n'
        '<div class="shell">\n<nav class="rail"><h1>Tidy Asset Allocation in R</h1>'
        '<p class="sub">Structural assessment, 13 November 2026 · three independent reviews of order, readers and chapter build. Select any passage to comment on it.</p>%s</nav>\n'
        '<main>\n%s\n</main>\n</div>\n'
    ) % (CSS, "\n".join(nav), "\n".join(body))
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(page)
    print("assessment page: %d documents, %d KB -> %s" % (len(body), len(page.encode("utf-8")) // 1024, os.path.relpath(PAGE, ROOT)))


if __name__ == "__main__":
    main()
