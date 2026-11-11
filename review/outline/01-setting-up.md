---
file: chapters/01-setting-up.qmd
title: Setting Up Your Environment
part: Prerequisites
words: 3514
sections: 5
paragraphs: 45
---

# Chapter

Claim: The long table and the date-indexed matrix are both unavoidable, so the crossing between them is made in one explicit call each way and guarded by assertions, because it fails in three ways that nothing downstream reports.
Question: What must be installed, and in what shape must a return series arrive, before any portfolio can be computed; cites @wickham2014 for the tidy table and @zeileis2005 for the ordered, date-indexed matrix.
Why here: First chapter, so it needs nothing earlier; the text says the boundary is crossed in every chapter and is therefore fixed here once; it borrows its notation and its market from ch. 2 ahead of time, says its rule recurs in ch. 9 and ch. 25 and its conventions are fixed in ch. 4, and places itself on ch. 3's horizon axis as allocating nothing.
Does: Install the toolchain, open a chapter with the five standard lines, move a panel between tibble and xts in one call each way, and assert that weights and columns share one index before computing anything.
Order: Opening (question, roadmap, installation, package table, callout), theory (two data models), implementation (the crossing and its three failures), application (code conventions, the data's shape, reproducibility), takeaways, exercises; deviations: five paragraphs and six chunks of installation sit in the opening before the theory, and two of the three application subsections are the book's conventions and pins rather than an application, so no picture opens it.

# Sections

## Opening, before the first section — 897

Says: What to install, and that the two canonical shapes of a return series disagree, so the boundary between them is fixed here once.
Why here: The chapter's own roadmap puts installation first, then the data models; no other reason given.
Paragraphs:
- (code: setup)
- ¶1 [claim] Poses two questions, installation and data shape; the second has two canonical answers that disagree, fixed here once.
- ¶2 [method] Roadmap: install, the two models, cross and break the boundary three ways, read the data once; allocates nothing.
- ¶3 [method] Three programs: R from 4.4, an editor, Quarto only to render; the CRAN packages install in one call.
- (code: install-cran)
- ¶4 [method] `tidypm` is off CRAN: the modeled market, the two coercion functions, what the package lacks; installs from GitHub.
- (code: install-tidypm)
- ¶5 [method] `renv.lock` pins every version; `renv` restores it so printed numbers reproduce to the last digit.
- (code: restore)
- (code: packages)
- (code: tbl-01-packages)
- ¶6 [evidence] Attributes each table row to its citation; solvers are backends picked by name, ch. 13 and app. C say which.
- ¶7 [claim] (callout) `PortfolioAnalytics` exports more names than it has functions.
- (code: namespace)
- ¶8 [caveat] (callout) The `_v1`/`_v2` exports are a legacy interface, why old forum answers fail; the book uses only three unsuffixed functions.
- (code: namespace-data)
- ¶9 [caveat] (callout) The package fetches no data and bundles almost none; it optimizes what it is handed, which is this chapter's subject.
Note: The chapter's motivation (handing the optimizer the right object) arrives last, inside the callout, after five paragraphs of installation; the callout carries its own `##` heading, which a heading count would take for a sixth section.

## Two Data Models — 563

Says: A return panel has two layouts, long for building and wide for computing, neither can be dropped, and the three equations of the wide form name the three ways the crossing fails.
Why here: Second in the roadmap; the text says the equations state what can go wrong before any code does, and the implementation section produces each failure from them.
Paragraphs:
- ¶1 [definition] A return panel is numbers indexed by date and asset; two layouts, each makes some operations natural, others awkward.
- ¶2 [definition] The tidy layout: one observation per row; filter, join, grouped mutate apply directly; how sleeves, screens and figures are built.
- ¶3 [definition] The wide layout: a T×N matrix with ordered dates; defines R, r_t, portfolio return and sample moments in three equations.
- ¶4 [claim] `zoo` made the layout an object, `xts` specialized it to time; both analytics packages accept it and nothing else.
- ¶5 [claim] Neither layout can be dropped; the crossing has a fixed direction; `timetk` and `tsibble` hide it and are avoided.
- ¶6 [claim] The three equations yield three failure modes: ragged panel, weights paired by position, duplicate keys; the next section produces each.
Note: ¶3 carries all three numbered equations in one paragraph, in a notation the text says ch. 2 fixes (a forward dependency); the section has no code.

## The Tibble–xts Boundary — 991

Says: `tidypm` crosses the boundary in one call each way, the round trip is lossless, and the chapter's assumptions about `R` are asserted where the matrix is built.
Why here: The roadmap's third step; needs the matrix and the three failure modes of the theory section; builds the `R`, `rf` and `few` objects that the subsection and the application reuse.
Paragraphs:
- ¶1 [method] `as_xts_pm()` takes a long table and three column names to the matrix; `as_pm()` takes it back; the data ship long.
- (code: long-form)
- (code: data)
- ¶2 [code] The assertions state what the chapter assumes about `R` and fail here, naming the condition, not chapters later.
- (code: wide-form)
- ¶3 [code] The reverse crossing returns a three-column tibble, and the round trip changes nothing.
- (code: back-again)
Note: Three short paragraphs around four chunks; the subsection below carries five-sixths of the section's words.

### Three ways the boundary breaks — 829

Says: Each failure mode is manufactured from the book's data so the reader meets its message here, and the guard in every case is to index by name and assert that the names agree.
Why here: The text says the failures are produced here so their messages are printed first; the order ragged, column order, duplicate keys is the order the equations gave them; the closing rule is said to recur in ch. 9 and ch. 25.
Paragraphs:
- ¶1 [method] Each failure is manufactured from the class returns so its message is printed here before the reader meets it.
- ¶2 [method] A ragged panel: drop one row, one asset's first observation, and cross.
- (code: ragged-build)
- ¶3 [result] The coercion pads and warns; the asset's column moves; mean and covariance use different samples; the optimizer accepts it silently.
- (code: ragged-optimizer)
- ¶4 [result] Weights barely move here; in ch. 25's windows and ch. 21's sleeve the gap matters; handle it before crossing.
- ¶5 [caveat] Column order: the table's sort order becomes the matrix's column order, so a join or `arrange()` reorders the columns.
- (code: column-order)
- ¶6 [method] Apply a 60/40 weight vector built in the original order to the reordered matrix; `Return.portfolio()` pairs by position.
- (code: column-order-cost)
- ¶7 [result] The positional portfolio holds two wrong assets and nothing says so; the guard is the shared index of @eq-01-portfolio-return.
- (code: column-order-assert)
- ¶8 [caveat] The same holds leaving the optimizer: `extractWeights()` is ordered by the fitted matrix; applied by position elsewhere, every entry mis-pairs.
- ¶9 [caveat] Duplicate keys: a repeated date–asset pair describes no matrix, and the failure surfaces in two steps.
- (code: duplicate-keys)
- ¶10 [result] The warning names the cause, the error only the symptom; the check belongs in the long table, before crossing.
- (code: duplicate-check)
- ¶11 [claim] The book's rule, stated here: index by name, then assert agreement, failing the render; recurs in ch. 9 and 25.
Note: The governing rule (¶11) comes after all three demonstrations, not before them; ¶3 does three jobs (column move, `set.portfolio.moments()` trap, ch. 9 pointer); column order gets twice the space of either other case.

## A First Pass Through the Data — 698

Says: Every chapter opens with the same five lines, the matrix they build has these dimensions, and three pins make the printed numbers reproducible.
Why here: The roadmap's last item, reading the data once the way every later chapter will; the matrix built in the implementation section is read here.
Paragraphs: none before the first subsection.
Note: Of the three subsections only the middle one applies the chapter's content to the data; the first and third are the book's conventions and pins, and no picture opens the section.

### How the code in this book is written — 214

Says: Every chapter opens with the same five lines, and the prose, figures and spelling follow three conventions.
Why here: not stated; the roadmap only says the data are read once the way later chapters will.
Paragraphs:
- ¶1 [method] Every chapter opens with the same lines, run from the project root.
- (code: every-chapter)
- ¶2 [code] `R/_common.R` attaches packages, seed, options, theme, and checks the `PortfolioAnalytics` build; two lines load, one subtracts the bill; nothing more.
- ¶3 [method] Three conventions: inline numbers, figures from one long frame, British `colour` in code; the R primer for the language.
Note: Book-wide conventions under an application heading; ¶3's one-frame rule is the column-order guard in another guise, and the text does not connect the two.

### The shape of the data — 340

Says: The matrix is a monthly panel of sixteen series over the model years; a growth figure and an annualized table show the reverse crossing and the wide matrix in use.
Why here: The text says the matrix built above is what ch. 4 describes and every later chapter consumes, so its dimensions are worth reading once.
Paragraphs:
- ¶1 [transition] The matrix built above is what ch. 4 describes and every later chapter consumes; its dimensions deserve one reading.
- (code: dimensions)
- ¶2 [result] Reads the dimensions: months, series, span in model years, monthly grid; a three-series figure will show the reverse crossing.
- (code: fig-01-growth)
- (code: growth-end)
- ¶3 [result] Later chapters omit `theme_tidyaa()`; one dollar in US equity, US government and global commodity ends at three different amounts.
- (code: tbl-01-annualized)
- ¶4 [result] The table annualizes the bill itself; return is compounded, Sharpe is excess over volatility; ch. 4 fixes the conventions.
Note: ¶3 opens with a stranded code convention (omit the theme call) before reading the figure; the figure is read in one sentence.

### Reproducibility — 136

Says: The seed, the package versions and the dataset version are pinned, and the dataset pin matters most because a regenerated market is a different path.
Why here: not stated; it completes the `renv` paragraph of the opening and closes the chapter.
Paragraphs:
- ¶1 [method] Three pins, seed, lockfile, dataset, the last mattering most; the toolchain is the sibling books', so numbers can be checked.
Note: One paragraph does three jobs (the pins, why the dataset pin matters, the toolchain and its sibling-book justification) and repeats the opening's `renv` paragraph.

## Key Takeaways — 194

Says: Five bullets restate the two models, the fixed-direction crossing, the three failures, the one guard, and the legacy exports.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [takeaway] Two data models are unavoidable: the long table to build, the matrix every analytics function consumes.
- ¶2 [takeaway] The boundary is crossed in a fixed direction, one call each way.
- ¶3 [takeaway] It fails three ways, none reported downstream: padding, reordering, duplicate keys.
- ¶4 [takeaway] The guard is always the same: index by name, then `stopifnot()` that the names agree.
- ¶5 [takeaway] The `_v1`/`_v2` exports are shims; the package fetches no data.
Note: ¶5 restates the callout and is the only takeaway not about the boundary.

## Exercises — 171

Says: Three exercises: the money markets across the boundary both ways, a ragged panel's covariance under two `use` options, and the legacy exports' modern counterparts.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [exercise] Attach the five money-market series to `R` by `merge()` and by `bind_rows()`; which route makes the alignment check unnecessary.
- ¶2 [exercise] Remove one asset's first three model years; compare complete and pairwise covariance, test positive definiteness, say which the package uses.
- ¶3 [exercise] For each legacy export, find whether an unsuffixed counterpart exists; what `update_constraint_v1tov2()` says about the interface change.
Note: The exercises revisit the ragged case and the callout; neither column order nor duplicate keys, the other two failure modes, gets an exercise.
