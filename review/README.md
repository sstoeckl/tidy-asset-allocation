# Review round-trip

Chapters come out as Word documents, comments go back in as Word comments, and
the comments are extracted, worked, and logged. Settled with Sebastian
2026-09-13.

## Out

```bash
python tools/make-review-docx.py 23-rebalancing
python tools/make-review-docx.py --all
```

**Never** `quarto render <chapter> --to docx --output-dir review`. Two reasons,
both learned by doing it.

This is a *book* project, so a book is one document: naming a single chapter
still renders all twenty-eight, in whatever format is asked for. That takes half
an hour and produces one enormous file.

And `--output-dir` does not merely redirect the output, it **cleans the target
directory first**. Pointed at `review/`, it deleted this file.

The tool instead reads the executed markdown Quarto has already cached in
`_freeze/chapters/<slug>/execute-results/html.json`, where every code result and
inline number is already substituted, and hands it to pandoc. Nothing is
re-executed and a chapter takes about a second.

It translates the two things pandoc does not know about Quarto. Cross-references
become readable labels, `ch. 25 § What a Backtest Estimates` rather than a link
that would be dead in Word anyway. Callout boxes become block quotes with a bold
heading. Citations and the bibliography resolve through citeproc against
`assets/bib/references.bib`.

**The cached result must be current.** The tool builds from the last render, so a
chapter edited since then produces a stale document. Render the book first.

The Word file will not look like the book. Figures are embedded and code survives
plainly. That is accepted: the file exists to be commented on, not read for
pleasure.

## Back

Comment in Word as normal. Save the file in this directory, keeping the chapter
name. Then:

```bash
python tools/extract-docx-comments.py review/09-mean-variance.docx
python tools/extract-docx-comments.py review/*.docx --markdown   # for the log
```

The tool reads `word/comments.xml` for the comments and walks `word/document.xml`
to recover the passage each one is anchored to, so every comment arrives with the
sentence it is about.

## Then

Every comment lands in `REVIEW-LOG.md` with what was done about it. A comment
that is about this chapter only is closed there. A comment that would apply to
any chapter is promoted into `CLAUDE.md` as a rule, and the log records that it
was. That promotion is the point of the log: the second time the same note
arrives, something was missed the first time.
