---
file: index.qmd
title: Preface
part: Front matter
words: 1463
sections: 10
paragraphs: 20
---

# Chapter

Claim: The difficulty of asset allocation lives in the chain of implementation decisions rather than in the ideas, so the book states each method in mathematics, attributes it, runs it in R on a fully inspectable modeled market, and measures how much of the textbook answer survives out of sample.
Question: Why can a student who derives the tangency portfolio on paper not produce it from a return matrix; posed as an observation, nobody is cited for it (the first citations are the package, @peterson2026, and the two model books, @scheuch2023 and @coqueret2020).
Why here: Needs nothing from earlier chapters; sends the reader forward to chapters 1 to 3 for setup, notation, data and the strategic/tactical vocabulary, and to the appendices for data, proofs, package notes, the R primer, solutions, colophon and acknowledgements; why it sits first is not stated beyond its being the preface.
Does: Know what the book is and whom it serves, how a chapter and the parts are shaped, what every number is computed on, what can be skipped, the notation and code conventions, and how to rebuild the book.
Order: Why the book exists, who it is for, how a chapter is built, how the parts are organized, the data, what to skip, what the book is not, conventions, reproduction, acknowledgements; the chapter contract (theory, implementation, application, takeaways, exercises) does not apply to front matter and none of its elements appear.

# Sections

(code: setup)

## Why this book exists — 324

Says: Asset allocation is easy to derive and hard to produce, the package that does the work is underused and mis-defaulted, and this book is the course text that closes that gap.
Why here: not stated; the page description lists the first three sections in this order and gives no reason.
Paragraphs:
- ¶1 [claim] Allocation is taught as a few ideas and practiced as a chain of decisions; the gap is the difficulty.
- ¶2 [claim] The package is broad, underused and wrongly defaulted; the book is a course text built on it.
- ¶3 [method] The models are Tidy Finance and Coqueret–Guida; this book begins where their factors and forecasts end.
Note: ¶2 does two things: the package's underuse and wrong defaults, then the book's own program (mathematics, attribution, R, out-of-sample test); that program is the preface's thesis and sits mid-paragraph.

## Who this is for — 224

Says: Written first for the master's student, in the same text for the practitioner, and usable by the researcher as a route into the literature.
Why here: takes "course text" from the previous section's ¶2 and names the readers; no reason for the order is given.
Paragraphs:
- ¶1 [claim] Written first for a master's student; one chapter per session, its anatomy sketched, prerequisites named.
- ¶2 [claim] Also for the practitioner; one track serves both, and the callouts carry what the package makes hard.
- ¶3 [claim] Not aimed at researchers, but the references are complete enough to serve as a route into the literature.
Note: ¶1 already gives the chapter anatomy (question and its source, theory, runnable code, takeaways, exercises, solutions appendix) that the next section repeats.

## How the chapters are built — 158

Says: Every chapter runs question, what we do, theory, implementation, application, takeaways and exercises, with the mathematics in the text, proofs sent out except in Part VIII, and package traps in callouts.
Why here: expands the chapter sketch given in the previous section's ¶1; not stated why it comes before the part structure.
Paragraphs:
- ¶1 [method] Every chapter: question and its source, what we do, theory, implementation, application, takeaways, exercises, solutions in appendix.
- ¶2 [method] Mathematics in the running text; Parts II–IV send proofs to the appendix, Part VIII derives in place.
- ¶3 [method] Package traps go in callouts where the reader would meet them; skippable worked examples in collapsible boxes.
Note: ¶1 restates the previous section's ¶1 almost item by item, down to the same pointer to the solutions appendix; ¶2 uses part numbers before the next section says what the parts are.

## How the book is organized — 136

Says: The parts follow the allocation hierarchy from classes down to securities, and a second, orthogonal distinction between strategic and tactical allocation is labeled chapter by chapter.
Why here: not stated; the previous section already refers to Parts II–IV and VIII, which this section is the first to lay out.
Paragraphs:
- ¶1 [claim] Parts follow the allocation hierarchy: classes in II–V, securities in VI, implementation in VII, theory in VIII.
- ¶2 [definition] Strategic versus tactical runs across the parts; defined in chapter 3, then labeled chapter by chapter.
Note: ¶1 places Parts II through VIII and never mentions Part I, which the "What you can skip" section later counts as part of the course.

## The data — 112

Says: Every number is computed on a modeled multi-asset market shipped with the companion package, which is what makes the book reproduce offline; real data are used only where a claim is about real markets.
Why here: not stated; the first section's ¶2 promised "a market whose every property can be inspected" and this section names it.
Paragraphs:
- ¶1 [definition] The modeled market: its size and span, three pointers, why modeled not recorded, and when real data are used.
Note: one paragraph carries four things: the inventory, the three forward pointers, the modeled-not-recorded claim and its payoff, and the real-data exception.

## What you can skip — 48

Says: Parts I to VII are the complete course; Part VIII is optional theory that nothing earlier depends on.
Why here: not stated; it needs the part layout of "How the book is organized" and could sit directly under it, but the data section stands between them.
Paragraphs:
- ¶1 [claim] Parts I–VII are the course and complete alone; Part VIII is theory nothing earlier depends on.
Note: Part VIII is described for the third time (the chapter-anatomy section ¶2, the organization section ¶1, and here), each time in slightly different words.

## What this book is not — 97

Says: The book is neither an R introduction nor an empirical asset-pricing text, and it delegates both, by citation, to three named books.
Why here: not stated.
Paragraphs:
- ¶1 [caveat] Not an introduction to R or to empirical asset pricing; those are cited rather than reproduced.
- ¶2 [caveat] (list) Three delegations: data and factors to Tidy Finance, prediction to Coqueret–Guida, R to Wickham and the primer.
Note: the two model books return from the first section's ¶3 with the same point ("picks up where the prediction ends" restates "where those books end, this one begins"); the pointer to the R primer repeats "Who this is for" ¶1.

## Conventions — 203

Says: Notation, return basis, code naming, the per-chapter setup lines, the asserted alignments, and the typographic rules are fixed here once.
Why here: not stated.
Paragraphs:
- ¶1 [definition] Notation: bold vectors and matrices fixed in chapter 2; simple returns in excess of the bill; code names mirror symbols.
- ¶2 [method] Chapter setup: project root, one setup file, tidypm, the explicit long-to-wide crossing, alignment asserted, figures from one frame.
- ¶3 [definition] Numbers computed, never typed; American spelling in prose, package spelling in code; functions in code font with parentheses.
Note: ¶2 mixes what the reader types (the setup lines, the one crossing) with the author's own coding discipline (assertions, one data frame per figure), which the reader never has to act on.

## Reproducing this book — 73

Says: The build is pinned: the versions print live, renv restores the dependency set, and deviations and the build record live in two appendices.
Why here: not stated.
Paragraphs:
- (code: colophon)
- ¶1 [method] renv.lock pins the dependencies; deviations listed in the package-notes appendix, the build recorded in the colophon.
Note: the section opens with a code chunk and no sentence introducing it; what the chunk prints the colophon appendix records again.

## Acknowledgements — 2

Says: A pointer to the acknowledgements appendix.
Why here: not stated.
Paragraphs:
- ¶1 [transition] Points to the acknowledgements appendix.
Note: a two-word section that does no work of its own.
