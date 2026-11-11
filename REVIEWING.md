# Reviewing this book

How comments on *Tidy Asset Allocation in R* are made, who reads what and
when, and what happens to every comment afterwards. For reviewers, and for the
sessions that process their comments.

The rendered book is at <https://www.tidy-pm.com/dev/>. Every chapter carries
a banner under its title with its review status, its code downloads and, where
one exists, its slide deck.

## Three ways to comment

**On a passage: annotate the page.** The book loads the
[Hypothesis](https://web.hypothes.is/) client. Select any text on a page, click
*Annotate*, write, and post. The note is stored with the exact sentence it was
made on, which is what makes it actionable. Reviewers need a free Hypothesis
account and a place in the reviewers' group, *tidy-asset-allocation*; the
invitation link comes from the author, and a note posted to that group is
visible to its members only. Choose
the group in the sidebar before posting; the default is *Public*. Highlights
without text are fine for "this sentence does not read well". Tags are
optional; `theory`, `code`, `citation`, `language`, `teaching` help the sorting.

**On a page: the discussion box.** The bottom of every page carries a
GitHub Discussions thread (through giscus) for remarks that are about the
chapter as a whole: what is missing, what belongs elsewhere, whether it teaches.
It needs a GitHub account.

**On the code or the package: an issue.** Anything that fails, prints a wrong
number, or should be a function goes to the issue tracker of the
[book](https://github.com/sstoeckl/tidy-asset-allocation/issues) or of
[`tidypm`](https://github.com/sstoeckl/tidypm/issues).

The author's own reviews run through Word (`review/README.md`); the result
lands in the same log as everything else.

## Who reads what, and when

Four levels, in the order they happen. Each chapter shows its level in its
banner; the colophon lists all of them.

| Level | Who | Reads | Asked to answer |
|---|---|---|---|
| **Draft** | the author | every chapter, in Word or on the page | structure, voice, direction; what to cut |
| **Alpha** | two or three colleagues who teach or research the subject | one part at a time | Is the theory right and the notation consistent? Is the literature fairly attributed, and is anything load-bearing missing? Would this chapter teach in one session? |
| **Beta** | students in the course, chapter by chapter in the semester's rhythm | the chapter of the week, with its exercises | Where did you stop understanding? Which exercise could you not start, and why? What did the code do that the text did not say? |
| **Code** | package users and anyone who runs the scripts | `code/` and `tidypm` | what fails, what is wrong, what should be a function |

**Order for the alpha round.** Chapters 9 and 25 first, because every other
chapter refers to them; then Parts I to IV in order; then Parts V to VII; Part
VIII last. A chapter moves from *draft* to *alpha* when the author has read it
once and to *beta* when the alpha comments are closed; *final* means a
semester's beta readers have been through it. The status lives in
`review/status.csv`, one line per chapter.

## What happens to a comment

Everything ends in `REVIEW-LOG.md`, nothing is deleted, and items are checked
off rather than removed.

```bash
python tools/fetch-hypothesis.py --since 2026-11-01 --markdown   # annotations, with their anchors
python tools/extract-docx-comments.py review/*.docx --markdown   # Word comments, the same shape
```

A comment about one chapter is fixed and closed in the log. A comment that
would apply to any chapter is promoted into `CLAUDE.md` as a rule, and the log
records that it was. The second arrival of the same note is the signal that
something was missed the first time; the log exists to make that second
arrival visible.

Comments are answered in the log, not on the page: the page changes instead.
A reviewer who wants to know what became of a note finds it there, with the
date and what was done.
