"""Point the rendered pages at the theme CSS that actually ships in site_libs.

With `output-dir` outside the project (deliberate here: the project tree is
synced by SharePoint, which fights a render), Quarto 1.9 warns that it "did not
expect the path configuration" and leaves every page's theme stylesheet linked
to a session-temporary path:

    href="../.quarto/quarto-session-temp<id>/<prefix>-<hash>.css"

while the file it means is written, correctly, to

    site_libs/bootstrap/bootstrap-<hash>.min.css        (or bootstrap-dark-...)

so the book renders unstyled. This script rewrites those links in every HTML
page of the output directory. Run it after every render:

    python tools/fix-theme-links.py            # default: D:/tmp/tidyaa_book
    python tools/fix-theme-links.py <dir>

Idempotent: a page that is already right is left alone.
"""
import io, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else r"D:\tmp\tidyaa_book"
LIBS = os.path.join(OUT, "site_libs", "bootstrap")
if not os.path.isdir(LIBS):
    raise SystemExit("no site_libs/bootstrap under %s -- is this the rendered book?" % OUT)

have = set(os.listdir(LIBS))
PAT = re.compile(r'href="((?:\.\./)*)\.quarto/quarto-session-temp[^/"]+/[0-9a-f]+-([0-9a-f]{32})\.css"')

def target(hash_):
    for name in ("bootstrap-%s.min.css" % hash_, "bootstrap-dark-%s.min.css" % hash_):
        if name in have:
            return name
    return None

pages = fixed = missing = 0
for base, _, files in os.walk(OUT):
    if os.sep + "site_libs" in base or os.sep + ".quarto" in base:
        continue
    for f in files:
        if not f.endswith(".html"):
            continue
        p = os.path.join(base, f)
        s = io.open(p, encoding="utf-8", newline="").read()
        n = 0
        def sub(m):
            global missing
            t = target(m.group(2))
            if t is None:
                missing += 1
                return m.group(0)
            return 'href="%ssite_libs/bootstrap/%s"' % (m.group(1), t)
        s2, n = PAT.subn(sub, s)
        pages += 1
        if n:
            io.open(p, "w", encoding="utf-8", newline="").write(s2)
            fixed += 1
print("%d pages scanned, %d rewritten, %d links without a matching stylesheet" % (pages, fixed, missing))
if missing:
    sys.exit(1)
