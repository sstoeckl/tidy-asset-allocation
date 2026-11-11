"""Check every bibliography entry that carries a DOI against Crossref.

Two DOIs written from memory once resolved to real but different papers, which
is the one citation error nothing else catches: the entry looks fine, the DOI
resolves, and the reader lands on the wrong article. So every DOI is resolved
and the title Crossref returns is compared with the title the entry claims.

Usage
-----
    python tools/check-bib.py                 # every entry with a DOI
    python tools/check-bib.py green1992 ...   # named keys only
    python tools/check-bib.py --new           # entries added since the last run

A cache in tools/.bib-cache.json keeps Crossref answers so a re-run is free;
delete a key from it to force a fresh lookup. Exit status 1 if any DOI fails
to resolve or its title does not match.
"""
import io, json, os, re, sys, time, urllib.request, urllib.parse, difflib
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "assets", "bib", "references.bib")
CACHE = os.path.join(ROOT, "tools", ".bib-cache.json")
UA = "tidy-asset-allocation-bib-check (mailto:sebastian.stoeckl@uni.li)"


def parse_bib(text):
    """key -> {field: value}. Tolerant of braces and quotes; enough for this file."""
    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
        kind, key, body = m.group(1), m.group(2), m.group(3)
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)", body):
            val = fm.group(2).strip().strip("{}\"")
            fields[fm.group(1).lower()] = re.sub(r"\s+", " ", val)
        fields["_type"] = kind.lower()
        entries[key] = fields
    return entries


def norm(s):
    s = re.sub(r"\{|\}|\\[a-zA-Z]+", "", s or "")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        msg = json.load(r)["message"]
    title = " ".join(msg.get("title") or [])
    container = " ".join(msg.get("container-title") or [])
    year = None
    for k in ("published-print", "published-online", "issued"):
        dp = (msg.get(k) or {}).get("date-parts") or [[None]]
        if dp[0][0]:
            year = dp[0][0]
            break
    return {"title": title, "container": container, "year": year}


def main():
    argv = sys.argv[1:]
    only_new = "--new" in argv
    keys = [a for a in argv if not a.startswith("--")]

    text = io.open(BIB, encoding="utf-8").read()
    entries = parse_bib(text)
    cache = json.load(io.open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

    todo = []
    for key, f in entries.items():
        if keys and key not in keys:
            continue
        if "doi" not in f:
            continue
        if only_new and key in cache:
            continue
        todo.append(key)

    bad = 0
    for key in todo:
        f = entries[key]
        doi = f["doi"].replace("https://doi.org/", "")
        rec = cache.get(key) if cache.get(key, {}).get("doi") == doi else None
        if rec is None:
            try:
                rec = crossref(doi)
                rec["doi"] = doi
                time.sleep(0.2)
            except Exception as e:  # noqa: BLE001
                rec = {"doi": doi, "error": str(e)}
            cache[key] = rec
        if rec.get("error"):
            print("FAIL  %-26s DOI does not resolve: %s" % (key, rec["error"]))
            bad += 1
            continue
        claimed, found = norm(f.get("title")), norm(rec["title"])
        ratio = difflib.SequenceMatcher(None, claimed, found).ratio()
        ok = ratio >= 0.8 or claimed in found or found in claimed
        flag = "ok  " if ok else "FAIL"
        if not ok:
            bad += 1
        print("%s  %-26s %.2f  %s" % (flag, key, ratio, rec["title"][:70]))
        if not ok:
            print("      claimed: %s" % (f.get("title") or "")[:90])
        yr = str(f.get("year", ""))
        if rec.get("year") and yr and abs(int(rec["year"]) - int(yr)) > 1:
            print("      year: entry says %s, Crossref says %s" % (yr, rec["year"]))

    json.dump(cache, io.open(CACHE, "w", encoding="utf-8"), indent=1, sort_keys=True)
    no_doi = [k for k, f in entries.items() if "doi" not in f and (not keys or k in keys)]
    print("\n%d entries checked, %d failed; %d entries carry no DOI (books, working papers): %s"
          % (len(todo), bad, len(no_doi), ", ".join(sorted(no_doi))[:400]))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
