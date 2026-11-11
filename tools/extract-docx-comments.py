"""Read the comments out of a commented .docx and print them with their anchors.

A .docx is a zip. `word/comments.xml` holds every comment; `word/document.xml`
holds the body, with `commentRangeStart` / `commentRangeEnd` markers carrying the
same ids. Walking the body in document order and collecting the text between a
matching pair gives the passage each comment attaches to, which is what makes a
comment actionable rather than a note saying "this is unclear".

Usage
-----
    python tools/extract-docx-comments.py review/09-mean-variance.docx
    python tools/extract-docx-comments.py review/*.docx --markdown

`--markdown` emits rows ready to paste into REVIEW-LOG.md.
"""
import argparse, glob, os, re, sys, zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _text_of(el):
    """All w:t descendants of an element, in order, joined."""
    return "".join(t.text or "" for t in el.iter(W + "t"))


def read_comments(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        if "word/comments.xml" not in names:
            return []
        comments = {}
        root = ET.fromstring(z.read("word/comments.xml"))
        for c in root.iter(W + "comment"):
            cid = c.get(W + "id")
            comments[cid] = {
                "id": cid,
                "author": c.get(W + "author") or "",
                "initials": c.get(W + "initials") or "",
                "date": (c.get(W + "date") or "")[:16].replace("T", " "),
                "comment": " ".join(_text_of(c).split()),
                "anchor": "",
                "para": "",
            }

        # walk the body in document order, tracking which ranges are open
        body = ET.fromstring(z.read("word/document.xml"))
        open_ids, buf = set(), {}
        last_para = ""
        for el in body.iter():
            tag = el.tag
            if tag == W + "p":
                last_para = " ".join(_text_of(el).split())
            elif tag == W + "commentRangeStart":
                cid = el.get(W + "id")
                open_ids.add(cid)
                buf.setdefault(cid, [])
                if cid in comments:
                    comments[cid]["para"] = last_para
            elif tag == W + "commentRangeEnd":
                open_ids.discard(el.get(W + "id"))
            elif tag == W + "t" and open_ids:
                for cid in open_ids:
                    buf[cid].append(el.text or "")
        for cid, parts in buf.items():
            if cid in comments:
                comments[cid]["anchor"] = " ".join("".join(parts).split())

        # a comment anchored to a zero-length range gets its paragraph instead
        for c in comments.values():
            if not c["anchor"]:
                c["anchor"] = c["para"][:160]
        return sorted(comments.values(), key=lambda c: int(c["id"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()

    files = []
    for pat in args.paths:
        files.extend(sorted(glob.glob(pat)) or [pat])

    total = 0
    for f in files:
        if not os.path.exists(f):
            print("missing: %s" % f, file=sys.stderr)
            continue
        cs = read_comments(f)
        chapter = os.path.splitext(os.path.basename(f))[0]
        total += len(cs)
        if args.markdown:
            if not cs:
                continue
            print("\n### %s\n" % chapter)
            for c in cs:
                print("- [ ] **%s** — %s" % (c["date"] or "?", c["comment"]))
                print("      > %s" % (c["anchor"][:200] or "(no anchor)"))
        else:
            print("\n=== %s: %d comment%s ==="
                  % (chapter, len(cs), "" if len(cs) == 1 else "s"))
            for c in cs:
                print("\n[%s] %s  %s" % (c["id"], c["author"] or "?", c["date"]))
                print("  on: %s" % (c["anchor"][:180] or "(no anchor)"))
                print("  says: %s" % c["comment"])
    print("\n%d comment%s across %d file%s"
          % (total, "" if total == 1 else "s", len(files),
             "" if len(files) == 1 else "s"), file=sys.stderr)


if __name__ == "__main__":
    main()
