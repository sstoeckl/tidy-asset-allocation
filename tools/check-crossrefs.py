"""Check that chapters actually refer to each other, and that no reference dangles.

Two separate failures. A dangling reference is broken and Quarto reports it only
at render time, after an hour of computation. A chapter that refers to nothing
and is referred to by nothing is not broken, and is worse: it reads as a chapter
from a different book.

Usage
-----
    python tools/check-crossrefs.py            # report
    python tools/check-crossrefs.py --strict   # exit 1 if a rule is violated
"""
import argparse, io, os, re, sys

CH = "chapters"
MIN_BACK, MIN_FORWARD, MIN_INBOUND = 3, 2, 3


def chapter_number(slug):
    m = re.match(r"(\d+)", slug)
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    files = sorted(f for f in os.listdir(CH) if f.endswith(".qmd"))
    slugs = [f[:-4] for f in files]
    written, defined, refs = {}, set(), {}

    for f in files:
        slug = f[:-4]
        t = io.open(os.path.join(CH, f), encoding="utf-8").read()
        t_nocode = re.sub(r"^```.*?^```", "", t, flags=re.S | re.M)
        written[slug] = "TODO" not in t_nocode
        defined |= set(re.findall(r"\{[^}]*#(sec-[a-z0-9-]+)[^}]*\}", t))
        refs[slug] = set(re.findall(r"@(sec-[a-z0-9-]+)", t_nocode))

    index = io.open("index.qmd", encoding="utf-8").read()
    defined |= set(re.findall(r"\{[^}]*#(sec-[a-z0-9-]+)[^}]*\}", index))
    refs["index"] = set(re.findall(r"@(sec-[a-z0-9-]+)", index))

    # --- dangling ----------------------------------------------------------
    dangling = {}
    for src, rs in refs.items():
        for r in rs:
            if r not in defined:
                dangling.setdefault(r, []).append(src)
    print("dangling references: %d" % len(dangling))
    for r, srcs in sorted(dangling.items()):
        print("   %s  <- %s" % (r, ", ".join(sorted(srcs))))

    # --- density, written chapters only ------------------------------------
    def target_slug(ref):
        for sl in slugs:
            if ref.startswith("sec-" + sl):
                return sl
        return None

    inbound = {sl: 0 for sl in slugs}
    rows = []
    for src in slugs:
        if not written.get(src):
            continue
        n = chapter_number(src)
        # appendices (90+) and the bare reference list are not narrative
        # chapters and are exempt from the density rule, not from the
        # dangling check.
        if n is None or n >= 90:
            continue
        back = fwd = 0
        for r in refs.get(src, ()):
            tgt = target_slug(r)
            if tgt is None or tgt == src:
                continue
            inbound[tgt] += 1
            m = chapter_number(tgt)
            if m is None or n is None:
                continue
            if m < n:
                back += 1
            elif m > n:
                fwd += 1
        rows.append((src, back, fwd))

    print("\n%-30s %8s %8s %8s" % ("written chapter", "back", "forward", "inbound"))
    bad = []
    for src, back, fwd in rows:
        ib = inbound[src]
        flag = ""
        # chapter 3 has only two predecessors to reach back to
        if back < MIN_BACK and chapter_number(src) > 4:
            flag += " back<%d" % MIN_BACK
        if fwd < MIN_FORWARD:
            flag += " fwd<%d" % MIN_FORWARD
        if ib < MIN_INBOUND:
            flag += " inbound<%d" % MIN_INBOUND
        if flag:
            bad.append((src, flag.strip()))
        print("%-30s %8d %8d %8d %s" % (src, back, fwd, ib, flag))

    print("\nrule: a written chapter refers back to >=%d, forward to >=%d, and is"
          " referred to by >=%d others" % (MIN_BACK, MIN_FORWARD, MIN_INBOUND))
    if dangling or bad:
        print("\nVIOLATIONS: %d dangling, %d chapters under the density rule"
              % (len(dangling), len(bad)))
        if args.strict:
            sys.exit(1)
    else:
        print("\nall clear")


if __name__ == "__main__":
    main()
