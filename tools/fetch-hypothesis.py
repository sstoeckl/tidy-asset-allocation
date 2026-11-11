"""Pull the Hypothesis annotations made on the book and print them with their
anchors, the way tools/extract-docx-comments.py does for Word comments.

Reviewers annotate the rendered book in the browser (select text, "Annotate",
post to the reviewers' group). Hypothesis stores each note with the exact
passage it was made on, and the search API returns both, so a comment arrives
here as the sentence plus what the reviewer said about it.

Usage
-----
    python tools/fetch-hypothesis.py                      # everything in the group
    python tools/fetch-hypothesis.py --since 2026-11-01   # created on or after
    python tools/fetch-hypothesis.py --chapter 09-mean-variance
    python tools/fetch-hypothesis.py --markdown           # rows for REVIEW-LOG.md

Needs
-----
HYPOTHESIS_TOKEN  a personal API token (hypothes.is > Settings > Developer),
                  from the environment or from review/.hypothesis.token
                  (gitignored). A private group's annotations are only
                  visible to a member's token.
HYPOTHESIS_GROUP  the group id from the group's URL (hypothes.is/groups/<id>/...),
                  from the environment, from review/.hypothesis.group, or
                  --group. Defaults to the public layer (__world__).

The book is served at two hosts (the GitHub Pages origin and the tidy-pm.com
proxy); both are searched, and the chapter is read from the path.
"""
import argparse, io, json, os, sys, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.hypothes.is/api/search"
HOSTS = ["https://www.tidy-pm.com/dev/", "https://sstoeckl.github.io/tidy-asset-allocation/"]


def _secret(env, fname, default=None):
    v = os.environ.get(env)
    if v:
        return v.strip()
    p = os.path.join(ROOT, "review", fname)
    if os.path.exists(p):
        return io.open(p, encoding="utf-8").read().strip()
    return default


def search(token, group, host, since):
    """Every annotation under host, oldest first, following search_after."""
    out, after = [], None
    while True:
        q = {"wildcard_uri": host + "*", "group": group, "limit": 200,
             "sort": "created", "order": "asc"}
        if after:
            q["search_after"] = after
        req = urllib.request.Request(API + "?" + urllib.parse.urlencode(q),
                                     headers={"Authorization": "Bearer " + token,
                                              "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            rows = json.loads(r.read().decode("utf-8")).get("rows", [])
        if not rows:
            return out
        for a in rows:
            if since and a["created"][:10] < since:
                continue
            out.append(a)
        after = rows[-1]["created"]
        if len(rows) < 200:
            return out


def flatten(a):
    quote = ""
    for t in a.get("target", []):
        for s in t.get("selector", []):
            if s.get("type") == "TextQuoteSelector":
                quote = s.get("exact", "")
    path = urllib.parse.urlparse(a["uri"]).path
    chapter = os.path.splitext(os.path.basename(path))[0] or "index"
    return {
        "id": a["id"],
        "chapter": chapter,
        "user": a["user"].replace("acct:", "").split("@")[0],
        "date": a["created"][:16].replace("T", " "),
        "anchor": " ".join(quote.split()),
        "comment": " ".join(a.get("text", "").split()),
        "tags": a.get("tags", []),
        "reply": bool(a.get("references")),
        "link": a.get("links", {}).get("incontext", ""),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group")
    ap.add_argument("--since", help="YYYY-MM-DD")
    ap.add_argument("--chapter", help="slug, e.g. 09-mean-variance")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    token = _secret("HYPOTHESIS_TOKEN", ".hypothesis.token")
    if not token:
        sys.exit("no token: set HYPOTHESIS_TOKEN or write it to review/.hypothesis.token")
    group = args.group or _secret("HYPOTHESIS_GROUP", ".hypothesis.group", "__world__")

    seen, notes = set(), []
    for host in HOSTS:
        for a in search(token, group, host, args.since):
            if a["id"] in seen:
                continue
            seen.add(a["id"])
            notes.append(flatten(a))
    if args.chapter:
        notes = [n for n in notes if n["chapter"] == args.chapter]
    notes.sort(key=lambda n: (n["chapter"], n["date"]))

    if args.json:
        print(json.dumps(notes, indent=2, ensure_ascii=False))
        return
    by = {}
    for n in notes:
        by.setdefault(n["chapter"], []).append(n)
    for chapter, ns in by.items():
        if args.markdown:
            print("\n### %s — Hypothesis\n" % chapter)
            for n in ns:
                who = n["user"]
                print("- [ ] **%s** (%s)%s — %s" % (n["date"], who, " reply" if n["reply"] else "", n["comment"] or "(highlight only)"))
                print("      > %s" % (n["anchor"][:200] or "(no anchor)"))
        else:
            print("\n=== %s: %d annotation%s ===" % (chapter, len(ns), "" if len(ns) == 1 else "s"))
            for n in ns:
                print("\n[%s] %s  %s%s" % (n["id"][:8], n["user"], n["date"], "  (reply)" if n["reply"] else ""))
                print("  on: %s" % (n["anchor"][:180] or "(no anchor)"))
                print("  says: %s" % (n["comment"] or "(highlight only)"))
                if n["tags"]:
                    print("  tags: %s" % ", ".join(n["tags"]))
    print("\n%d annotation%s in group %s" % (len(notes), "" if len(notes) == 1 else "s", group), file=sys.stderr)


if __name__ == "__main__":
    main()
