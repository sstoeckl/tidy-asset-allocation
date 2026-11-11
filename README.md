# Tidy Asset Allocation in R

The source of the book *Tidy Asset Allocation in R* by Sebastian Stöckl: a
course text on building, constraining and testing multi-asset portfolios with
`PortfolioAnalytics` and the tidyverse, in the category of *Tidy Finance with
R* and *Machine Learning for Factor Investing* — the question first, the
mathematics in the running text, the method attributed to the literature, the
code executed, and takeaways and exercises at the end of every chapter.

The rendered book is at <https://www.tidy-pm.com/dev/> while it is being
written; the earlier book, *Tidy Portfoliomanagement in R*, stays at the root
of that site until this one replaces it.

## Building the book

Every number in the book is computed from a modeled multi-asset market that
ships with the companion package [`tidypm`](https://github.com/sstoeckl/tidypm),
so the whole book reproduces offline.

```r
renv::restore()                    # the pinned package set, PortfolioAnalytics included
```

```bash
quarto render --to html            # about an hour: every chapter executes its code
python tools/fix-theme-links.py    # see CLAUDE.md, "After every render"
```

The chapters are in `chapters/`, their exercise solutions in
`chapters/solutions/`, the bibliography in `assets/bib/references.bib`, and
the tools that check them (execution, inline numbers, cross-references,
DOIs) in `tools/`. `CLAUDE.md` is the editorial contract the chapters are
written to.

The code of every chapter is in `code/`, one script per chapter with the
exercises and solutions beside it, built by `tools/build-code.py` and served
with the book.

## Reviewing

The book is in review. `REVIEWING.md` says how to comment (annotations on the
page, a discussion thread under it, issues for the code), who reads what and
when, and what happens to every comment. `review/status.csv` carries each
chapter's stage.

## Citing

`CITATION.cff`, or the BibTeX entry in the book's colophon.

## Licence

To be decided. Code CC-BY or MIT; prose CC-BY-NC-SA is the likely split.
