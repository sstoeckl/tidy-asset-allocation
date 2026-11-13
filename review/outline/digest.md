# Reverse outline, digest: chapters and sections

One block per chapter: its claim, question, placement and order, then every
section with what it says, why it comes there, the outline's note, and the
sequence of its paragraph types (`code` marks a chunk, `+c` a callout). The
paragraph lines themselves are in `NN-slug.md` beside this file.

# Front matter

##  Preface (1463 words, 20 paragraphs)
Claim: The difficulty of asset allocation lives in the chain of implementation decisions rather than in the ideas, so the book states each method in mathematics, attributes it, runs it in R on a fully inspectable modeled market, and measures how much of the textbook answer survives out of sample.
Question: Why can a student who derives the tangency portfolio on paper not produce it from a return matrix; posed as an observation, nobody is cited for it (the first citations are the package, @peterson2026, and the two model books, @scheuch2023 and @coqueret2020).
Why here: Needs nothing from earlier chapters; sends the reader forward to chapters 1 to 3 for setup, notation, data and the strategic/tactical vocabulary, and to the appendices for data, proofs, package notes, the R primer, solutions, colophon and acknowledgements; why it sits first is not stated beyond its being the preface.
Does: Know what the book is and whom it serves, how a chapter and the parts are shaped, what every number is computed on, what can be skipped, the notation and code conventions, and how to rebuild the book.
Order: Why the book exists, who it is for, how a chapter is built, how the parts are organized, the data, what to skip, what the book is not, conventions, reproduction, acknowledgements; the chapter contract (theory, implementation, application, takeaways, exercises) does not apply to front matter and none of its elements appear.

### Why this book exists (324 words)
Says: Asset allocation is easy to derive and hard to produce, the package that does the work is underused and mis-defaulted, and this book is the course text that closes that gap.
Why here: not stated; the page description lists the first three sections in this order and gives no reason.
Paragraphs: claim · claim · method
Note: ¶2 does two things: the package's underuse and wrong defaults, then the book's own program (mathematics, attribution, R, out-of-sample test); that program is the preface's thesis and sits mid-paragraph.

### Who this is for (224 words)
Says: Written first for the master's student, in the same text for the practitioner, and usable by the researcher as a route into the literature.
Why here: takes "course text" from the previous section's ¶2 and names the readers; no reason for the order is given.
Paragraphs: claim · claim · claim
Note: ¶1 already gives the chapter anatomy (question and its source, theory, runnable code, takeaways, exercises, solutions appendix) that the next section repeats.

### How the chapters are built (158 words)
Says: Every chapter runs question, what we do, theory, implementation, application, takeaways and exercises, with the mathematics in the text, proofs sent out except in Part VIII, and package traps in callouts.
Why here: expands the chapter sketch given in the previous section's ¶1; not stated why it comes before the part structure.
Paragraphs: method · method · method
Note: ¶1 restates the previous section's ¶1 almost item by item, down to the same pointer to the solutions appendix; ¶2 uses part numbers before the next section says what the parts are.

### How the book is organized (136 words)
Says: The parts follow the allocation hierarchy from classes down to securities, and a second, orthogonal distinction between strategic and tactical allocation is labeled chapter by chapter.
Why here: not stated; the previous section already refers to Parts II–IV and VIII, which this section is the first to lay out.
Paragraphs: claim · definition
Note: ¶1 places Parts II through VIII and never mentions Part I, which the "What you can skip" section later counts as part of the course.

### The data (112 words)
Says: Every number is computed on a modeled multi-asset market shipped with the companion package, which is what makes the book reproduce offline; real data are used only where a claim is about real markets.
Why here: not stated; the first section's ¶2 promised "a market whose every property can be inspected" and this section names it.
Paragraphs: definition
Note: one paragraph carries four things: the inventory, the three forward pointers, the modeled-not-recorded claim and its payoff, and the real-data exception.

### What you can skip (48 words)
Says: Parts I to VII are the complete course; Part VIII is optional theory that nothing earlier depends on.
Why here: not stated; it needs the part layout of "How the book is organized" and could sit directly under it, but the data section stands between them.
Paragraphs: claim
Note: Part VIII is described for the third time (the chapter-anatomy section ¶2, the organization section ¶1, and here), each time in slightly different words.

### What this book is not (97 words)
Says: The book is neither an R introduction nor an empirical asset-pricing text, and it delegates both, by citation, to three named books.
Why here: not stated.
Paragraphs: caveat · caveat
Note: the two model books return from the first section's ¶3 with the same point ("picks up where the prediction ends" restates "where those books end, this one begins"); the pointer to the R primer repeats "Who this is for" ¶1.

### Conventions (203 words)
Says: Notation, return basis, code naming, the per-chapter setup lines, the asserted alignments, and the typographic rules are fixed here once.
Why here: not stated.
Paragraphs: definition · method · definition
Note: ¶2 mixes what the reader types (the setup lines, the one crossing) with the author's own coding discipline (assertions, one data frame per figure), which the reader never has to act on.

### Reproducing this book (73 words)
Says: The build is pinned: the versions print live, renv restores the dependency set, and deviations and the build record live in two appendices.
Why here: not stated.
Paragraphs: code · method
Note: the section opens with a code chunk and no sentence introducing it; what the chunk prints the colophon appendix records again.

### Acknowledgements (2 words)
Says: A pointer to the acknowledgements appendix.
Why here: not stated.
Paragraphs: transition
Note: a two-word section that does no work of its own.

# Part I: Prerequisites

## Chapter 1: Setting Up Your Environment (3514 words, 45 paragraphs)
Claim: The long table and the date-indexed matrix are both unavoidable, so the crossing between them is made in one explicit call each way and guarded by assertions, because it fails in three ways that nothing downstream reports.
Question: What must be installed, and in what shape must a return series arrive, before any portfolio can be computed; cites @wickham2014 for the tidy table and @zeileis2005 for the ordered, date-indexed matrix.
Why here: First chapter, so it needs nothing earlier; the text says the boundary is crossed in every chapter and is therefore fixed here once; it borrows its notation and its market from ch. 2 ahead of time, says its rule recurs in ch. 9 and ch. 25 and its conventions are fixed in ch. 4, and places itself on ch. 3's horizon axis as allocating nothing.
Does: Install the toolchain, open a chapter with the five standard lines, move a panel between tibble and xts in one call each way, and assert that weights and columns share one index before computing anything.
Order: Opening (question, roadmap, installation, package table, callout), theory (two data models), implementation (the crossing and its three failures), application (code conventions, the data's shape, reproducibility), takeaways, exercises; deviations: five paragraphs and six chunks of installation sit in the opening before the theory, and two of the three application subsections are the book's conventions and pins rather than an application, so no picture opens it.

### Opening (before the first heading) (897 words)
Says: What to install, and that the two canonical shapes of a return series disagree, so the boundary between them is fixed here once.
Why here: The chapter's own roadmap puts installation first, then the data models; no other reason given.
Paragraphs: code · claim · method · method · code · method · code · method · code · code · code · evidence · claim+c · code · caveat+c · code · caveat+c
Note: The chapter's motivation (handing the optimizer the right object) arrives last, inside the callout, after five paragraphs of installation; the callout carries its own `##` heading, which a heading count would take for a sixth section.

### Two Data Models (563 words)
Says: A return panel has two layouts, long for building and wide for computing, neither can be dropped, and the three equations of the wide form name the three ways the crossing fails.
Why here: Second in the roadmap; the text says the equations state what can go wrong before any code does, and the implementation section produces each failure from them.
Paragraphs: definition · definition · definition · claim · claim · claim
Note: ¶3 carries all three numbered equations in one paragraph, in a notation the text says ch. 2 fixes (a forward dependency); the section has no code.

### The Tibble–xts Boundary (991 words)
Says: `tidypm` crosses the boundary in one call each way, the round trip is lossless, and the chapter's assumptions about `R` are asserted where the matrix is built.
Why here: The roadmap's third step; needs the matrix and the three failure modes of the theory section; builds the `R`, `rf` and `few` objects that the subsection and the application reuse.
Paragraphs: method · code · code · code · code · code · code
Note: Three short paragraphs around four chunks; the subsection below carries five-sixths of the section's words.

#### Three ways the boundary breaks (829 words)
Says: Each failure mode is manufactured from the book's data so the reader meets its message here, and the guard in every case is to index by name and assert that the names agree.
Why here: The text says the failures are produced here so their messages are printed first; the order ragged, column order, duplicate keys is the order the equations gave them; the closing rule is said to recur in ch. 9 and ch. 25.
Paragraphs: method · method · code · result · code · result · caveat · code · method · code · result · code · caveat · caveat · code · result · code · claim
Note: The governing rule (¶11) comes after all three demonstrations, not before them; ¶3 does three jobs (column move, `set.portfolio.moments()` trap, ch. 9 pointer); column order gets twice the space of either other case.

### A First Pass Through the Data (698 words)
Says: Every chapter opens with the same five lines, the matrix they build has these dimensions, and three pins make the printed numbers reproducible.
Why here: The roadmap's last item, reading the data once the way every later chapter will; the matrix built in the implementation section is read here. Paragraphs: none before the first subsection.
Note: Of the three subsections only the middle one applies the chapter's content to the data; the first and third are the book's conventions and pins, and no picture opens the section.

#### How the code in this book is written (214 words)
Says: Every chapter opens with the same five lines, and the prose, figures and spelling follow three conventions.
Why here: not stated; the roadmap only says the data are read once the way later chapters will.
Paragraphs: method · code · code · method
Note: Book-wide conventions under an application heading; ¶3's one-frame rule is the column-order guard in another guise, and the text does not connect the two.

#### The shape of the data (340 words)
Says: The matrix is a monthly panel of sixteen series over the model years; a growth figure and an annualized table show the reverse crossing and the wide matrix in use.
Why here: The text says the matrix built above is what ch. 4 describes and every later chapter consumes, so its dimensions are worth reading once.
Paragraphs: transition · code · result · code · code · result · code · result
Note: ¶3 opens with a stranded code convention (omit the theme call) before reading the figure; the figure is read in one sentence.

#### Reproducibility (136 words)
Says: The seed, the package versions and the dataset version are pinned, and the dataset pin matters most because a regenerated market is a different path.
Why here: not stated; it completes the `renv` paragraph of the opening and closes the chapter.
Paragraphs: method
Note: One paragraph does three jobs (the pins, why the dataset pin matters, the toolchain and its sibling-book justification) and repeats the opening's `renv` paragraph.

### Key Takeaways (194 words)
Says: Five bullets restate the two models, the fixed-direction crossing, the three failures, the one guard, and the legacy exports.
Why here: Chapter contract; not stated.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: ¶5 restates the callout and is the only takeaway not about the boundary.

### Exercises (171 words)
Says: Three exercises: the money markets across the boundary both ways, a ragged panel's covariance under two `use` options, and the legacy exports' modern counterparts.
Why here: Chapter contract; not stated.
Paragraphs: exercise · exercise · exercise
Note: The exercises revisit the ragged case and the callout; neither column order nor duplicate keys, the other two failure modes, gets an exercise.

## Chapter 2: Notation and Data (5963 words, 59 paragraphs)
Claim: Every chapter computes on the same four objects, on excess returns, fixed here once, and on one of two data sources: a modeled market with no real data on its own calendar, the default because it reproduces offline, and a free real-data layer with a pinned cutoff and a manifest, used only where a claim must be about real markets.
Question: What do the symbols mean and where do the numbers come from; cites Markowitz for needing the four objects and Coqueret and Scheuch et al. for opening a book this way.
Why here: Needs chapter 1 for `as_xts_pm()` and the tidy-to-`xts` crossing. Fixes the notation so that no later chapter redefines a symbol and describes the data so that no later chapter explains what it computes on; sits on neither side of the strategic–tactical distinction chapter 3 defines but is the ground both stand on. Chapter 9 takes the moments equation, every chapter the three-object data block and the calendar tools, chapters 4, 7, 15, 20, 21, 22 and the appendices the individual tables and caveats.
Does: Read any symbol in the book, build `R`, `rf` and `Re`, annualize two ways and say which applies, read a model-calendar date and an episode, name every shipped table and its trap, and fetch and check the real sleeves.
Order: Notation (with annualizing and the data block), the modeled market in seven subsections, the real-data layer, vocabulary, takeaways, exercises. The theory–implementation–application contract does not apply: a reference chapter with code interleaved as checks throughout and no application section.

### Opening (before the first heading) (255 words)
Says: The book manipulates four objects and two data sources, and both are fixed here once.
Why here: Not a `##` section; the two paragraphs before the first heading.
Paragraphs: code · claim · method · code

### Notation (1304 words)
Says: Bold vectors and matrices, simple total returns, excess over the bill as the default basis, and the portfolio's mean and variance as the equation every later chapter starts from.
Why here: First because no later chapter may redefine a symbol; chapter 9 takes the moments equation as its start, and chapter 3 supplies the argument for the excess basis that is only stated here.
Paragraphs: definition · definition · definition
Note: ¶2 says the reasons for the excess basis belong to chapter 3 and then lists three of them; it half-argues what it says it will not argue.

#### Annualizing (889 words)
Says: Two annualizing conventions, arithmetic for optimizer inputs and compounded for what a series earned, and the three-object data block every chapter opens with.
Why here: Returns arrive monthly and are reported annually, so the conversion is fixed with the symbols; the data block follows because the symbol table's code column is itself a convention.
Paragraphs: definition · method · code · code · code · code · example+c · code · example+c · example+c · code
Note: The data-preparation convention and the `data` chunk sit under the heading "Annualizing", after the symbol table; the subsection carries two topics, and the worked example on annualizing comes after the data block has interrupted it.

### The Modeled Market (2848 words)
Says: The default data is a modeled market with no real data, on its own calendar, shipped inside `tidypm` so that every number reproduces offline; the section lists its tables, says how the series are built, and names the properties a reader must know before modeling on it.
Why here: Notation says what is computed, this says what it is computed on; the calendar precedes the tables because every date in them reads only on it; the caveats come last because they follow from how the series are built.
Paragraphs: definition · claim

#### The model calendar (463 words)
Says: A date is a position on the model calendar, and four functions are the only way any chapter reads, names, selects or plots one.
Why here: Because the data are modeled, dates need translating before any table or figure can be read; the episode table and the time axes of the next subsections depend on these tools.
Paragraphs: definition · code · code · result · code · code · code · result · code · caveat

#### The class universe (567 words)
Says: Sixteen risky class series are the allocation spine, the five money markets ship beside them and are neither cash nor the risk-free rate, and a table places each series by return, volatility and Sharpe ratio.
Why here: The classes are what Parts III to V allocate across, so they come before the instruments beneath them; the money-market point is settled here because Notation declared the bill the risk-free rate.
Paragraphs: definition · code · claim · code · result · method · code · code
Note: `fig-02-indices` follows the table with no sentence pointing to it or reading it; the subsection ends on an unreferenced figure.

#### How the class series are built (202 words)
Says: Equity classes are value-weighted on the previous week's capitalization, the other classes equally weighted, and a monthly class return is the compounded weekly return within the month.
Why here: not stated; it follows the class table and precedes the instruments the classes are built from.
Paragraphs: method · code
Note: One paragraph and one chunk; the chunk's output, the largest monthly discrepancy, is never read in prose, and the subsection ends on it.

#### The instrument universe (236 words)
Says: Beneath the sixteen classes sit the individual instruments, the same market at a finer grain and the universe of the Part VI sleeve chapters.
Why here: Granularity is the book's spine, classes first and instruments after; the sleeve chapters are named as the takers.
Paragraphs: definition · code · code · definition
Note: `tbl-02-instruments` is referenced only from the Vocabulary section, not from the prose around it.

#### Exchange rates, curves, capitalizations and rating changes (391 words)
Says: Four further tables let a chapter show what moved a series: exchange rates with the one-line hedge, the curve factors behind the bond block, the equity capitalizations, and ESG rating changes without a starting level.
Why here: not stated; the tables are listed after the series they explain, and each is handed to the chapter that uses it.
Paragraphs: definition · code · result · definition · code · definition · definition

#### Three caveats, one departure, and a frozen version (763 words)
Says: Currency dominates foreign bonds, the bond block is nearly rank-deficient at instrument level and the equities are single names; euro-area equity carries a deliberate three-point overlay within one standard error; and the dataset is frozen at one version because regenerating redraws the paths.
Why here: The three properties are consequences of how the market is built, so they follow the construction, and a reader should know them before modeling on it; the freeze closes the description.
Paragraphs: transition · caveat · caveat · code · result · caveat · claim · code · result · caveat
Note: The `overlay` chunk builds and solves the long-only tangency portfolio of chapter 9 to justify a data choice, the chapter's heaviest chunk and the only place a reader meets `optimize.portfolio()` before chapter 9; the heading counts three caveats and the freeze in ¶8 is in practice a fourth.

### The Real Data Sleeves (692 words)
Says: Where a claim has to be about real markets, `tidypm` carries a small free-data layer with a registry, one download to a cache at a pinned cutoff, an offline read, and a manifest that names what has moved.
Why here: The modeled market cannot support a claim about real markets and chapters 21 and 25 must make one; the layer is described after the default it supplements.
Paragraphs: claim · definition · code · result · method · code · method · code · caveat · method
Note: ¶3 reads a table it never names and carries two caveats inside a result paragraph; `tbl-02-sources` is referenced nowhere in the prose.

### Asset Class Vocabulary (369 words)
Says: Code uses the data's names and prose uses whichever is clearer; the class level is where Parts III to V work, the instrument level Part VI, and strategic versus tactical is a different axis, defined in chapter 3.
Why here: Both naming systems appear in the book, so the map closes the data description; the granularity–horizon distinction is placed last because the next chapter defines the horizon words.
Paragraphs: definition · caveat · claim
Note: ¶3 introduces the book's two axes, granularity and horizon, under a heading about naming; it is the chapter's only paragraph on the book's structure rather than its data.

### Key Takeaways (294 words)
Says: Six bullets restating notation, annualizing, the calendar, the universe, the caveats and the real-data layer.
Why here: Closes the chapter per the contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway

### Exercises (168 words)
Says: Three exercises on hedging all non-US series, rebuilding the commodity class from its instruments, and rebuilding `US_equity` equally and value-weighted.
Why here: Closes the chapter per the contract; each exercise checks a construction claim of the Modeled Market section.
Paragraphs: exercise · exercise · exercise

# Part II: Foundations of Portfolio Choice

## Chapter 3: Return, Risk, and the Investor's Problem (7987 words, 76 paragraphs)
Claim: The investor's problem is expected utility, approximated by μ_w − (γ/2)σ²_w on returns in excess of the bill, and the approximation is only as good as its conventions for return, horizon, currency and riskless alternative, which are fixed here once.
Question: What does an investor want from a portfolio, and in which units is the answer measured; @markowitz1952 for the first, @vonneumann1944 for the second.
Why here: Needs the sixteen series and symbols of chapter 2 and the environment of chapter 1; says the definitions are fixed here so that no later chapter revisits them; chapter 4 measures the bill against the money markets and the currency split, 9 derives the frontier from the dominance vocabulary, 11 adds moments to the criterion, 16 onward carry the tactical label, 25 applies the reporting rule.
Does: State the objective on excess returns with a γ read in basis points, pass it to PortfolioAnalytics as γ/2, annualize means and Sharpe ratios in a named convention, and sort series into dominated and efficient before any optimizer runs.
Order: Opening, theory in ten subsections, implementation in six, application in four, Key Takeaways, Exercises; the contract holds, except that theory already computes (three chunks, a γ table, an implied γ), the application derives the separation result, the last two theory subsections have no implementation or application counterpart, and there are six takeaways and four exercises.

### Opening (before the first heading) (349 words)
Says: The question, the order of the chapter, and the data it runs on.
Why here: Contract position; says the definitions are fixed here so no later chapter revisits them.
Paragraphs: code · claim · method · method · code

### Returns, Horizons, and the Basis of Comparison (2986 words)
Says: Returns, means, Sharpe ratios and the excess basis are fixed; then the investor's objective, its horizon, dominance and the strategic/tactical labels are defined from them.
Why here: The opening lists this order; the implementation checks each convention and the application runs the objective, so both need the definitions first. Paragraphs: none outside the subsections.
Note: Ten subsections in two groups, six on conventions and four on the investor; the conventions group is the only part of theory with code.

#### Simple returns, log returns, and compounding (148 words)
Says: Simple returns add across assets, log returns across time; the data are simple and stay simple wherever a portfolio is formed.
Why here: First convention in the opening's list; the averages next need compounding, and every weight vector needs simple returns.
Paragraphs: definition · claim

#### Averages, annualization, and the variance drag (267 words)
Says: The arithmetic mean is the input to every objective, the geometric mean is what was earned, and half the variance separates them.
Why here: Needs compounding from the previous subsection; says the application meets a series with the higher arithmetic and the lower geometric mean.
Paragraphs: definition · definition
Note: ¶2 holds a definition and two caveats (geometric times twelve, √12 under autocorrelation) in one paragraph.

#### The Sharpe ratio and its horizon (143 words)
Says: √q scales the ratio only under independence; Lo's correction gives the general factor.
Why here: Needs the annualization rule just given; says the implementation measures the error on this data.
Paragraphs: definition · derivation

#### Excess returns as the basis (395 words)
Says: Every optimized return is in excess of the Treasury bill, for four reasons of rising consequence, and the bill is not a money-market series.
Why here: Reason two needs the Sharpe ratio just defined; the application measures reason three; chapter 4 measures the money-market gap.
Paragraphs: claim · evidence · caveat · claim · claim · code · result · caveat
Note: The first theory subsection to read a number from a chunk; the implementation has not started.

#### Nominal and real (165 words)
Says: The book works in nominal dollars because the market carries no inflation series; a real-liability investor would swap the bill for an indexed bond.
Why here: Not stated; qualifies the bill as riskless in nominal terms only.
Paragraphs: caveat
Note: One paragraph carries a definition, the book's scope decision and the literature.

#### Currency (201 words)
Says: Every series is an unhedged dollar return, and hedging is one subtraction of the matching currency return.
Why here: Not stated; the implementation applies the subtraction to the foreign governments and chapter 4 decomposes the variance.
Paragraphs: definition · method
Note: ¶2 mixes the book's convention with the hedging literature.

#### The investor's objective (839 words)
Says: Expected utility expands to μ_w − (γ/2)σ²_w, a certainty equivalent whose γ is a price with units an investor can read.
Why here: The opening says the problem is stated after the basis; the wealth equation puts the balance in the bill, which needs the basis; dominance and the package call need the criterion.
Paragraphs: definition · definition · derivation · derivation · example · code · claim · code · result · claim
Note: Longest subsection; eight paragraphs and two chunks run from derivation through a units table to the CRRA alternative, which could stand alone.

#### The horizon of the problem (160 words)
Says: Under independent returns the long-lived investor is myopic, so the one-period problem re-solved at each rebalancing is exact; changing opportunities add hedging demands the book does not model.
Why here: Answers the objection that the objective is one-period; refers forward to the horizon axis defined below.
Paragraphs: caveat

#### Dominance, efficiency, and the northwest rule (219 words)
Says: A dominates B with at least as much return and at most as much risk, one strict; a better allocation lies northwest; what nothing dominates is efficient.
Why here: Follows from having two moments per portfolio; says the vocabulary applies before γ is chosen and every later chapter uses it; chapter 9 derives the frontier.
Paragraphs: definition · definition

#### Strategic and tactical allocation (440 words)
Says: Strategic is the long-run policy from unconditional moments, tactical a deviation on conditioning information; the chapters are sorted, and a portfolio is judged by the measure it was chosen by.
Why here: The opening says the chapter closes by defining the terms once; the sort needs the objective, which the strategic chapters solve from full-sample moments.
Paragraphs: claim · definition · transition · claim
Note: ¶4 is a separate rule under a heading about horizon; neither this subsection nor the previous has an implementation or application counterpart.

### Implementation (2230 words)
Says: PerformanceAnalytics implements every convention with a default the reader must know, and PortfolioAnalytics takes γ/2.
Why here: Says the point is to see which convention each function defaults to; the application reuses the specifications and the weight function built here. Paragraphs: none outside the subsections.
Note: The six subsections follow the theory's order (returns, Sharpe, horizon, bill, currency, objective); nominal/real and dominance have no counterpart here.

#### Return conventions in `PerformanceAnalytics` (435 words)
Says: Rebuilt returns match the shipped ones, the two means and the drag come from one series, and the package's annualization default is the compounded one.
Why here: Says the point is to see which convention each function defaults to; needs the return definition, the drag and the annualization rules.
Paragraphs: method · code · result · code · code · example · code · code · result

#### The Sharpe ratio, in two conventions (466 words)
Says: Two package functions default to different Sharpe conventions; the gap is the drag over the volatility, and it swaps pairs of the sixteen series.
Why here: Needs the excess basis, the Sharpe definition and the drag; says the book reports compounded and optimizes arithmetic, as chapter 4 does.
Paragraphs: code · code · code · code · caveat+c · code · code · result
Note: ¶1 checks the excess basis, not a Sharpe convention; it sits here because the bill is needed next.

#### Aggregation over horizons (483 words)
Says: Compounded to quarters and years, the annual ratio falls short of √12 times the monthly; autocorrelation explains the bond series, sampling error the rest.
Why here: The Lo equation says when √12 is right, and the theory promised the error would be measured here.
Paragraphs: method · code · result · code · result
Note: ¶3 reads two chunks' worth of numbers in one long paragraph.

#### The bill is not a seventeenth asset (191 words)
Says: Added as a column, the bill absorbs the minimum-variance portfolio; as a constant it makes Σ singular; it enters through the basis and the budget.
Why here: Says a reader just told the bill is essential will be tempted to add it; Tobin's separate treatment explains why not.
Paragraphs: caveat · code · result

#### Hedging a foreign government bond (199 words)
Says: Subtracting the currency return removes most of a foreign government bond's volatility; for JP_government nearly all of it is exchange rate.
Why here: The currency equation is one subtraction and governments have little local volatility; equities are chapter 4's question.
Paragraphs: method · code · result

#### Where risk aversion enters the package (453 words)
Says: PortfolioAnalytics states the objective as mean plus var with risk_aversion, and that argument is γ/2, verified against a solver that takes γ literally.
Why here: Needs the quadratic-utility equation; says one thing must be known before the objectives are used; the application's sweeps call the functions built here.
Paragraphs: code · caveat · code · method · code · result

### What the Objective Does on Sixteen Assets (1879 words)
Says: Dominance sorts the sixteen before any optimizer runs; raising γ ends at minimum variance under full investment and at the bill without it; the total-return basis overinvests by a fixed share.
Why here: Opens with the picture as the house rule asks; needs the dominance definition, the γ table and the implementation's specifications; chapter 9 takes the frontier from here. Paragraphs: none outside the subsections.
Note: Four subsections serve only the investor half of the theory; the conventions half ends in the implementation, except the drag, which returns in the basis check of the first subsection.

#### The northwest rule applied (790 words)
Says: Most of the sixteen series are dominated on the arithmetic excess basis; the efficient set is the same on the compounded basis, but who dominates whom moves with the drag.
Why here: Says the application opens with the picture and that the count needs no optimizer; chapter 9 draws the same picture on compounded total returns.
Paragraphs: method · code · code · code · result · claim · code · result
Note: Three chunks run before any prose reads them; ¶3–4 return to the drag, the averages topic of the theory, inside the dominance subsection.

#### Raising γ under full investment (342 words)
Says: With weights summing to one, rising γ walks the solution to the minimum-variance portfolio and stops; it cannot reach cash.
Why here: Not stated; it is the first of two budget rules, and the next subsection is the contrast.
Paragraphs: claim · code · code · result

#### Relaxing full investment (526 words)
Says: Without the budget the risky composition is fixed and the invested fraction is proportional to 1/γ, which is Tobin's separation; it survives long-only.
Why here: The contrast to the previous rule; says the same γ gives a different answer under a different budget, and the figure shows both.
Paragraphs: derivation · code · result · code
Note: The only numbered equation outside the theory section; the figure for both rules follows the prose that reads it.

#### The basis, once more, in the invested fraction (212 words)
Says: Fed total returns, the relaxed problem invests a fixed share more in risky assets at every γ, crediting the bill as a reward for risk.
Why here: Says the third argument for excess returns can now be measured, which needs the relaxed problem of the previous subsection.
Paragraphs: method · code · result

### Key Takeaways (305 words)
Says: Six bullets, one per theory topic, with the package trap and the two sweeps folded into one.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six against the contract's "around five"; ¶5 and ¶6 each carry two points.

### Exercises (201 words)
Says: Four exercises: dominance on weekly data, Lo's correction against direct compounding, hedging the foreign equities, the γ of a 60/40 investor.
Why here: Contract position; each reuses a function or table of the chapter by name.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; three are on the conventions and one on the objective.

## Chapter 4: Descriptive Analysis of Asset Returns (4740 words, 47 paragraphs)
Claim: Volatility is the only moment this market lets us estimate with confidence, and the two things that shape every portfolio, tails that arrive as market-wide events and a currency share that belongs to the asset rather than the country, are invisible in a table of moments.
Question: Which of the known regularities of financial returns hold in the modeled market, and which of the numbers the book is about to rely on can be estimated at all; cited to Mandelbrot (1963), Fama (1965) and Cont (2001).
Why here: Every later chapter does something to a return series, the text says, and none of that is interpretable or trustworthy without this one; it takes the modeled market from chapter 2 and the tidy-to-matrix boundary from chapter 1, and it says the mean–variance asymmetry splits chapters 6 and 7, that chapter 10 settles the risk-measure question, chapter 15 the hedge per sleeve, chapter 25 the per-episode reporting, and that Part IV's optimizers are bounded by its two properties.
Does: Compute and read the annualized moments on the modeled market, test normality, compare two expected-shortfall estimators, judge each moment on rolling windows, read drawdown episodes, count joint exceedances, compare the four episodes, and split a foreign series' variance into local and currency parts.
Order: Theory, implementation, application, takeaways, exercises, as the contract has it; but the implementation reads every result it computes and carries both tables and two of the three figures, so it is the first application, the section titled as the application holds the chapter's only derivation outside the theory (@eq-04-fx), and the mean–volatility picture closes the implementation's first subsection instead of opening the application.

### Opening (before the first heading) (354 words)
Says: The chapter asks which known regularities of returns hold in this market and which of its numbers can be estimated at all.
Why here: The text says every later chapter works on a return series and nothing downstream is interpretable or trustworthy without this.
Paragraphs: code · claim · method · definition
Note: The annualization convention (geometric return, volatility scaled by the root of the frequency, Sharpe over the bill) lives only in a comment inside the hidden setup chunk; the prose never states it.

### What Can Be Estimated (545 words)
Says: The four sample moments are not four facts of the same kind, and that difference is the chapter's most consequential point.
Why here: Not stated as such; ¶2 announces the asymmetry as the chapter's most consequential point, which the implementation then measures, and the opening promised theory before computation.
Paragraphs: definition · claim

#### The mean is the moment that does not improve (190 words)
Says: The mean's precision depends on the calendar span, the variance's on the number of observations; the higher moments are worse.
Why here: It rates the moments just defined; the text says this asymmetry is what splits chapter 6 from chapter 7, and the rolling-window subsection later makes it concrete.
Paragraphs: derivation · claim · claim

#### Testing normality rather than assuming it (245 words)
Says: Jarque–Bera tests normality; whether it matters depends on the quantity, and for the tail the Cornish–Fisher correction prices the normal assumption.
Why here: Not stated; it supplies the statistic and the two expected-shortfall estimators that the implementation's distribution test applies.
Paragraphs: definition · definition · definition
Note: ¶2 both defines two risk measures and argues the preference for one; the Sharpe ratio and maximum drawdown, two columns of the next table, are defined nowhere in this section.

### Implementation (1,920 words)
Says: Three package tables carry the book; once in `xts`, the moments table, the normality test, the rolling windows and the drawdown episodes each yield a reading.
Why here: The text says the three tables' shape is what everything else expects and that PortfolioAnalytics needs the matrix form; the boundary is the one chapter 1 establishes.
Paragraphs: method · code · result · caveat · code · method
Note: At about 1,900 words this section is the chapter's analytical centre: it computes and reads every result, holds both tables and two of the three figures, and runs to nearly twice the length of the section titled as the application.

#### The moments (610 words)
Says: Three features of the moments table matter: return and Sharpe rankings differ, the money market is not the risk-free rate, and currency is first-order.
Why here: Not stated; the table is where the three features are read, and ¶2 and ¶6 each defer their question to the application section (¶2 also to chapter 10).
Paragraphs: code · code · code · transition · result · claim · code · result · claim · code · claim · code
Note: The mean–volatility scatter closes the subsection after the three features and no paragraph reads it; the Sharpe ratio and the maximum-drawdown column appear here before either is defined; ¶4 ends in a book-wide convention (the bill as the risk-free rate everywhere) stated inside a result paragraph.

#### Testing the distribution (470 words)
Says: Every series rejects normality, but volatility and non-normality are different properties, and the cost of the Gaussian assumption is concentrated in credit.
Why here: It applies @eq-04-jb from the theory and reads the shape columns of the moments table; the text says the Cornish–Fisher table puts a number on what credit's non-normality costs.
Paragraphs: claim · code · code · result · result · code · result · caveat+c
Note: The callout follows code that already names both methods explicitly, so it explains the code rather than catching the reader before the trap.

#### How well each moment is estimated (450 words)
Says: On sixty-month windows volatility is stable, the mean wanders by more than its own level, and skewness often reverses sign.
Why here: The text calls it the practical counterpart of @eq-04-precision and the statement the book leans on repeatedly.
Paragraphs: method · code · code · result · claim · code
Note: The figure closes the subsection after the claim and no paragraph reads it; the subsection sits third in the implementation although it is the direct empirical counterpart of the theory's first subsection.

#### Drawdowns are episodes, not a number (195 words)
Says: A single maximum drawdown hides what matters, the episodes and their recovery, which the episode table returns for one extra argument.
Why here: Not stated; the text calls maximum drawdown the investor's first question, yet it comes last in the implementation, after the column has already appeared in the moments table.
Paragraphs: claim · code · code · code · result
Note: Maximum drawdown was tabulated as a single number in @tbl-04-moments three subsections earlier; the point made here is that the single number is inadequate.

### Two Properties That Shape Every Portfolio (1,385 words)
Says: Two properties invisible in a moments table, tails as market-wide events and currency as an asset-level share, decide what Part IV's optimizers can achieve.
Why here: The text says neither property is visible in a table of moments, so they come after the tables, and that both bound the optimizers of Part IV.
Paragraphs: transition
Note: The title and the opening promise two properties; the section delivers three subsections, and the middle one, the four episodes and their correlations, is the longest in the chapter.

#### Fat tails are events, not a distribution (340 words)
Says: The market's fat tail is a handful of months in which much of the market moves at once, not sixteen independent fat tails.
Why here: The text ties it to the per-series kurtosis of @tbl-04-moments, which invites the wrong reading, and calls it the joint counterpart of what @eq-04-jb detected.
Paragraphs: claim · code · result · code · result · code
Note: ¶3 places the worst month in the credit crisis and points to the next subsection for it, so an episode is used one subsection before it is introduced; the heat-map closes the subsection unread.

#### The crises are not one crisis (615 words)
Says: The four episodes differ economically, so a diversification rule learned in one reverses in another, and correlation rises in two of them and falls in the equity bear market.
Why here: The text says the book keeps the four episodes apart throughout and that chapter 25 therefore reports them separately; the correlations restate the episode result in the form an optimizer feels.
Paragraphs: method · code · code · result · code · claim · transition · code · code · result · caveat
Note: Two topics in one subsection, episode returns and regime correlations, joined by a one-sentence transition; the correlation half ends in a caveat that discounts its own evidence in favor of the first half's.

#### Currency is not one decision (390 words)
Says: How much of a foreign series is currency depends on the asset, not the country, because local return and currency covary differently for bonds and equities.
Why here: Set up by the moments subsection, which found the same currency inside every foreign series and promised the application would take it apart; the text hands the per-sleeve hedge on to chapter 15.
Paragraphs: claim · code · code · result · derivation · result · evidence
Note: The chapter's only derivation outside the theory section, and it comes after the code that computes the quantities it explains; the columns `fx_share` and `if_indep` are printed and read before ¶3–¶4 say what they are.

### Key Takeaways (265 words)
Says: Six bullets: the moment asymmetry in theory and on rolling windows, non-normality apart from volatility, tails as events, episodes not one crisis, currency as an asset property.
Why here: Not stated (contract position).
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets against the contract's "around five"; the money-market finding and the drawdown subsection have no bullet, and bullets 1 and 2 state one result twice, once in theory and once in measurement.

### Exercises (195 words)
Says: Five exercises: weekly moments, exceedance thresholds, skewness of a combination, hedged correlations, precision by simulation.
Why here: Not stated (contract position).
Paragraphs: exercise · exercise · exercise · exercise · exercise
Note: Five against the contract's "around three"; exercise 3 asks about the skewness of a mixture, which no section of the chapter works through.

## Chapter 5: Factor Models and Beta Estimation (4429 words, 37 paragraphs)
Claim: Most of what a single-factor regression appears to explain about this market does not survive proper measurement: the model fits only the equity blocks, its betas are mostly United States betas, the up/down split survives inference in two cases of sixteen, non-equity betas change sign in about a third of windows, and a global size factor sorts on region.
Question: What do the sixteen series have in common? Cites Sharpe, Lintner and Black for the model and Jensen for the regression form.
Why here: Stated as the continuation of chapter 4, which described the market one series at a time; takes the excess-return basis from chapter 3 and the instrument universe from chapter 2 for the proxy. Forward: chapter 8 is said to exist because a small beta's sign is unknown, chapter 19's regime allocation is said to need the turbulence index, and the appendix carries the package note. Why factor models precede the input estimation of the next part is not stated.
Does: Build a lagged capitalization-weighted market proxy, estimate alphas and betas with Newey-West errors, test an up/down split, construct and inspect a size factor, roll betas, and compute an out-of-sample turbulence index.
Order: Theory (model, variance split, two extensions, inference), implementation (proxy, one-factor fit, split beta, size factor, package callout), application under the title "How Much of This Survives" (rolling betas, turbulence), takeaways, exercises. Deviations: the implementation section already carries the chapter's main findings, one of the two tables and two of the four figures; the application section has no prose of its own and holds two further studies rather than an application of what was implemented; the packages block is a hidden setup chunk before the opening, not a shown block after the plan sentence; six takeaways and five exercises.

### Opening (before the first heading) (208 words)
Says: The chapter asks what the series share, names the single-factor model as the canonical answer, and announces that most of its explanation will not survive measurement.
Why here: Stated: chapter 4 described the market one series at a time; this chapter asks what the series have in common.
Paragraphs: code · claim · method
Note: The setup chunk is hidden and precedes the opening; no visible packages block follows the plan sentence. ¶2 states three results before any is derived.

### The Single-Factor Model (417 words)
Says: The CAPM regression splits each asset's variance into a market part and a residual, so R² is the share of risk the model describes; two extensions let beta differ by market direction and move over time.
Why here: Stated in the opening: the model is set out before it is estimated. Needs the excess-return basis of chapter 3; supplies the four equations the implementation estimates and the table is read through.
Paragraphs: definition · derivation · claim · definition
Note: ¶4 defines both extensions in one paragraph; the second gets one sentence and no equation.

#### Inference is where these models are usually lost (130 words)
Says: OLS standard errors are wrong for monthly returns, so Newey-West errors are used throughout, and sixteen repeated tests need them because repetition manufactures significance.
Why here: Stated: eq-05-asymmetric is estimated sixteen times, so the estimator is fixed before the first regression runs.
Paragraphs: method · claim

### Implementation (2139 words)
Says: The market proxy is built from the 123 equity instruments with lagged capitalization weights, and three studies on it follow: the one-factor fit, the up/down split with its test, and a size factor that turns out to sort on region.
Why here: Stated: a factor model needs a factor, and the market has to be built from the instrument universe of chapter 2 because a capitalization weight exists only there; the proxy's composition is read before any beta is used.
Paragraphs: method · code · caveat · code · result
Note: The section's own prose only builds the proxy; its three subsections hold the chapter's main findings, so the implementation is already the application.

#### One factor, sixteen series (477 words)
Says: The one-factor regression explains the four equity blocks and little else; the only significant alpha, on a government bond, is a sign of missing factors.
Why here: Not stated beyond the opening's plan; it is the first estimate and supplies `fit1` for the figure and the takeaways.
Paragraphs: code · code · result · result · code · code · result
Note: The hidden `-claims` chunks here and below are assertions placed directly before the paragraph they guard. The figure plots the R² column the table already lists.

#### Splitting the beta, and then testing the split (635 words)
Says: Up- and down-market betas can differ in sign where the unconditional beta is zero, but only two of sixteen splits survive a Newey-West test, and the credit one is not among them.
Why here: Stated: a single beta assumes the same slope up and down, so the split follows the single fit; the test follows the split because halving a sample manufactures differences.
Paragraphs: method · code · code · result · claim · code · code · result · caveat · code
Note: ¶3 and ¶5 make the same point, before and after the test; the figure closes the subsection after the reading rather than opening it.

#### What a factor is actually sorting on (666 words)
Says: A global size sort in a five-region universe sorts on region and currency; it raises R² for that reason, while the region-neutral version carries the more reliable premium.
Why here: Stated: size is the second factor everyone reaches for after the market, and here a trap worth walking into deliberately; it reuses the proxy's weight matrix.
Paragraphs: method · code · transition · code · result · transition · code · code · result · claim · code+c · code · caveat
Note: The callout and its chunk sit under the size heading but belong with the conditional betas one subsection back; the callout's `##` title reads as a section in a heading grep. ¶6 reads a result, states the lesson and places the literature in one paragraph.

### How Much of This Survives (1193 words)
Says: Betas move, outside equity they change sign in about a third of windows, and the movement itself can be measured without hindsight as a turbulence index.
Why here: Stated in the opening: after estimating, examine how much of the explanation survives proper measurement.
Note: The section carries no prose of its own; its two subsections are further studies, not an application of the implemented model.

#### A beta is a time series (610 words)
Says: Sixty-month rolling betas travel furthest where they are smallest; every non-equity beta changes sign, the median in about a third of windows, and equity betas never do.
Why here: Stated: eq-05-beta is written as a constant and the conditional CAPM literature says it is not, so a rolling window shows how much it moves; the theory section announced rolling windows as the second extension. Points forward to chapter 8.
Paragraphs: method · code · code · code · transition · result · result · code · claim
Note: ¶2 announces two patterns that ¶3 and ¶4 then carry; the figure follows the reading of the table rather than opening the section.

#### Measuring the instability itself (576 words)
Says: The Mahalanobis turbulence index, estimated out of sample on a trailing window, finds the peak month chapter 4 found by hand, in the credit crisis, and shows it was extreme moves within an ordinary correlation structure.
Why here: Stated: if the moments move, the movement is itself a quantity, so it follows the rolling betas; it asks chapter 4's hand-picked window question continuously, and chapter 19's regime allocation is said to need it.
Paragraphs: definition · code · method · code · code · result · definition · code · code · result · code
Note: The index measures the returns' own instability, not beta's; the section's only link to the factor model is its first sentence. The figure closes the section after both readings.

### Key Takeaways (252 words)
Says: Six bullets restate the chapter's numbers: R² as risk share, the proxy's United States weight, two surviving asymmetries, the size sort's region bet, sign-changing betas, and hindsight-free turbulence.
Why here: not stated.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets against the contract's "around five"; each re-reads a number from the chapter through inline R and carries a citation.

### Exercises (186 words)
Says: Five exercises: an equal-weighted proxy, separate up/down regressions, rolling betas against turbulence, the `s.k` window of `OSturbulence()`, and multiple-testing corrections on the asymmetry p-values.
Why here: not stated.
Paragraphs: exercise · exercise · exercise · exercise · exercise
Note: Five exercises against the contract's "around three"; exercise 3 is the one place the chapter links rolling betas to turbulence.

# Part III: Estimating the Inputs

## Chapter 6: Expected Returns (7565 words, 57 paragraphs)
Claim: No history pins an expected return down, so the book sets its strategic vector on the equilibrium where market weights exist and on Bayes-Stein where they do not, and keeps the sample mean only as the benchmark that moves the portfolio most.
Question: How precisely can a mean return be known, and which vector should a long-run policy be set on; cites Merton (1980) in the second sentence.
Why here: Names itself the hard input of chapter 9 against the large one of chapter 7; takes the data from chapter 2, the excess basis and the strategic/tactical vocabulary from chapter 3, the precision formula and the instability figure from chapter 4, the lagged weights and the CAPM from chapter 5; uses chapter 9's problem, tangency and GMV equations throughout as if already read; hands the vector to 8 (cost), 16 (benchmark forecast), 17 (prior), 23 (turnover priced), 26 (derivation). Why it precedes chapter 7 inside the part: not stated.
Does: Build the precision table for any return panel; implement Bayes-Stein and reverse optimization; pass any mean vector into `optimize.portfolio()` through `momentFUN` and assert it was used; compare estimators by how far they move on rolling windows.
Order: Theory (precision, target, shrinkage, equilibrium), implementation (Bayes-Stein, equity equilibrium plus a proxy box, the package route and its traps), application (three tangency portfolios, rolling stability, what is carried forward), takeaways, exercises. Deviations: the theory section runs code and reads numbers twice (the frequency callout, the target subsection); the implementation ends in a run of package caveats rather than an estimator; the application closes with a conclusion subsection the takeaways then repeat; six takeaways, four exercises.

### Opening (before the first heading) (349 words)
Says: Expected returns are the imprecise input, this chapter is about the strategic vector, and here is the sequence.
Why here: Contract position; the text says the chapter measures first and offers alternatives after.
Paragraphs: code · claim · method · method · code
Note: The "packages used" block the contract asks for is hidden (`include: false`), so the reader sees no package list.

### How Precisely a Mean Can Be Known — 2141 (907 before the subsections) (? words)
Says: The standard error of a mean depends on calendar span alone, and on this sample most of the sixteen intervals include zero.
Why here: The text says the table these formulas produce "is the right way to begin" a chapter on expected returns; needs eq-04-precision; the target, shrinkage and equilibrium subsections respond to the imprecision measured here.
Paragraphs: derivation · code · code · code · example · method+c · code · result+c
Note: The ## title names only the first subsection's topic; the chapter's two estimators sit under a heading about precision. ¶2 does four jobs (worked case, headline count, literature, pointer to chapter 4).

#### A target set on a sample mean (395 words)
Says: A return target set on a sample mean is a constraint on noise that the optimizer honors exactly, and the literature on the consequence is old and consistent.
Why here: Needs the interval width of tbl-06-precision; shows the cost of the imprecision just measured before any remedy; the text says one sentence per citation suffices because chapter 9 already used them; hands the cost to chapters 8 and 26.
Paragraphs: method · code · result · evidence
Note: A worked number (¶1–2) and a seven-citation literature paragraph (¶3) share one subsection; ¶3's closing Kan–Zhou pointer is what the next subsection builds on.

#### Shrinkage of the mean (401 words)
Says: Bayes-Stein shrinks every mean toward the minimum-variance return with an intensity the data set, which moves the tangency portfolio toward the minimum-variance portfolio.
Why here: "The response from statistics predates all of that": the first alternative, offered after the cost paragraph; relies on chapter 9's tangency and GMV equations and on chapter 7's shrinkage form.
Paragraphs: definition · claim · derivation

#### Equilibrium returns by reverse optimization (438 words)
Says: Reverse optimization reads the μ for which the market portfolio is optimal from Σ and market weights; its weakness is that the weights exist for five classes only.
Why here: "The third route asks a different question": ordered as the last alternative; needs appendix B's first-order condition and chapter 5's CAPM; is the prior chapter 17 blends views into; sets up the five-class demonstration and the proxy box.
Paragraphs: definition · derivation · claim · caveat
Note: ¶3 bundles a package convention (γ/2) with two theory properties; the convention returns as its own paragraph and chunk in the implementation.

### Three Estimators in Code (2733 words)
Says: Bayes-Stein in a function, equilibrium returns from capitalizations, and the `momentFUN` route that puts any vector into `PortfolioAnalytics`.
Why here: Only the opening's sequence sentence ("then implement both and show how the package takes a mean vector it did not compute"); the section itself has no paragraph. Paragraphs: none of its own.
Note: Heading only. "Three estimators" covers two implementations (the sample mean needs none) and a third subsection that is package plumbing and traps, not an estimator.

#### Bayes-Stein in a few lines (527 words)
Says: The estimator in a function; v near one half removes more than half the distance, halves the spread and keeps every rank.
Why here: eq-06-bayes-stein needs μ̂, Σ̂, N, T "and nothing else", so it comes first, on the data chunk alone.
Paragraphs: method · code · example · code · code · result

#### Equilibrium returns for the five equity classes (1139 words)
Says: Lagged capitalization weights give δ and an equilibrium vector that is beta times the market premium, within one standard error of every sample mean; a proxy extends it to sixteen classes.
Why here: "The clean case first": the weights exist for equities; the proxy box follows because the application needs all sixteen.
Paragraphs: method · code · result · code · example · code · code · result · caveat · code · result+c
Note: The collapsed box the text calls a placeholder (with an open `SS:` comment) builds `mu_eq`, `delta16` and `W16`, which the γ/2 check, the three-portfolio comparison and the rolling table all run on. ¶4 derives the beta form after the table that it reads.

#### The moments as PortfolioAnalytics sees them (1061 words)
Says: `set.portfolio.moments()` offers four methods, none of them Bayes-Stein; a custom `momentFUN` supplies any vector, and four package behaviors (`maxSR`, `black.litterman()`, `match.call()`, γ/2) are measured.
Why here: After the two vectors exist, the route into the package, "the one chapter 7 used for a shrunk covariance"; the γ/2 check closes the property promised in the theory's ¶3.
Paragraphs: method · code · caveat · code · code · caveat+c · method · code · caveat+c · code · caveat+c · caveat · code · result · method · code · result
Note: Eleven paragraphs, six of them caveats, under a title about moments. ¶5–9 (two chunks, one callout) test `black.litterman()`, a function ¶2 has just routed to chapter 17; the γ/2 check (¶10–11) verifies a theory property and uses the proxy vector.

### What the Three Vectors Buy (1897 words)
Says: On one tangency problem the sample and Bayes-Stein vectors concentrate and churn; the equilibrium returns the market and turns over only as capitalizations drift.
Why here: The opening's last clause ("feed the three vectors to the same tangency problem to see what each buys and how much each moves"); needs `mu_eq` from the proxy box and `make_moments()` from the γ/2 chunk. Paragraphs: none of its own.
Note: Heading only; the three subsections are comparison, stability, conclusion.

#### Three tangency portfolios (1127 words)
Says: The sample and Bayes-Stein portfolios hold a handful of series, Bayes-Stein the more concentrated in the GMV's series; the equilibrium holds all sixteen and is the market.
Why here: "The same long-only tangency problem that chapter 9 solved" is solved three times with Σ̂ fixed so only μ changes; the assertion is "the guard the callout asked for".
Paragraphs: method · code · code · derivation · code · result+c · code · code · code · code · code · result · result
Note: Five chunks run between ¶4 and ¶5 with no prose. The collapsed QP box defines `tangency_lo()`, which the rolling subsection depends on, so a box a reader may skip is load-bearing. ¶6's out-of-sample number is borrowed from chapters 9 and 25.

#### Which vector moves least (541 words)
Says: On rolling sixty-month windows the sample mean moves most, Bayes-Stein less and the equilibrium least, and the implied turnover follows the same order.
Why here: ¶6 above: "what matters for a strategic allocation is how much each answer moves when the sample does"; uses chapter 25's window; hands the cost to chapter 23.
Paragraphs: method · code · code · result

#### What the book carries forward (222 words)
Says: The book carries the equilibrium as anchor where weights exist, Bayes-Stein where they do not, and the sample mean as the benchmark.
Why here: Closes the comparison with the decision later chapters use (17's prior, 8's cost, 16's benchmark); no other reason given.
Paragraphs: claim · claim
Note: A conclusion subsection directly before Key Takeaways; the sixth takeaway repeats ¶2's decision almost verbatim, and ¶1 repeats the readings of the two subsections before it.

### Key Takeaways (266 words)
Says: Six bullets.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six against "around five"; ¶5 is a package trap rather than a chapter claim; ¶6 restates the subsection before.

### Exercises (179 words)
Says: Four exercises.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; ¶3 works on the proxy the text calls a placeholder.

## Chapter 7: The Covariance Matrix (5002 words, 58 paragraphs)
Claim: On more assets than observations the sample covariance matrix is singular by arithmetic; of the four replacements, shrinkage is the one that always runs but earns nothing once the window is long, and the long-only constraint was already doing comparable work.
Question: Why the lowest-risk combination of 123 equities cannot be obtained from the monthly history available; @michaud1989 for the consequence and @chopra1993 for its price.
Why here: Needs the sixteen classes of chapter 4, the factor models of chapter 5, chapter 6's ranking of input errors, the bond block of chapter 2, and the frontier of chapter 9, which lies ahead; sends forward to chapter 8 (method or sample), 15, 17, 19, 21, 28, 10 and appendix D. Stated twice: @chopra1993's ranking makes chapter 6 harder "and this one unavoidable", and the theory section closes by saying class-level allocation never needed it and the equity sleeve will.
Does: Diagnose a singular or ill-conditioned covariance matrix before the solver does, build a factor, shrunk or robust estimate, pass it to `optimize.portfolio()` through `momentFUN`, and score estimators out of sample.
Order: Theory (requirement, singularity, diagnosis, why now), implementation (four routes by cost, the moment-function plumbing, patching, robust estimation), application (out-of-sample race, Sharpe versus volatility with the spectrum, regime dependence of the target, long only as shrinkage), seven takeaways, four exercises; deviations: route four is split around two other subsections, the application heading carries no prose of its own, and the spectrum, the application's named subject, sits inside the Sharpe subsection.

### Opening (before the first heading) (240 words)
Says: The most modest request of an optimizer, the lowest-risk combination of an equity sleeve, cannot be met because the matrix it needs is singular on a realistic universe.
Why here: the opening by contract; its ¶3 lays out the chapter's order (requirement, four responses by cost, out-of-sample payoff).
Paragraphs: code · example · claim · method · code
Note: ¶1 defines the request as the low-volatility end of chapter 9's frontier, a chapter that comes later.

### What the Optimizer Requires (999 words)
Says: The optimizer's only input is Σ, whose sample estimate has rank at most min(N, T−1), so with more assets than observations it is singular whatever the data.
Why here: stated in the opening's plan: first what the optimizer asks for and why the request cannot be met.
Paragraphs: definition · definition · derivation · claim · evidence

#### What singularity claims about portfolios (316 words)
Says: A singular estimate asserts a riskless long-short portfolio, which a minimizer will hold; short of singularity the condition number says how far sampling error is magnified into the weights.
Why here: stated: eq-07-rank is a statement about a matrix, this subsection turns it into a statement about money.
Paragraphs: derivation · claim · definition · evidence

#### Diagnosing it before the solver does (399 words)
Says: Rank, riskless directions and condition number flag the problem without an inverse; the equities are singular on five years, and the full instrument universe is ill-conditioned even with N < T.
Why here: needs the rank bound and the condition number just defined; the reason for diagnosing before solving is in the title, no other reason is given.
Paragraphs: method · code · result · caveat · result · code · code · result
Note: ¶3 defines the condition number a second time, two paragraphs after eq-07-condition did; the hidden chunk asserts ¶4's numbers.

#### Why this book has not needed the chapter until now (93 words)
Says: At class level no sixty-month window is rank deficient; the problem appears only when the portfolio holds securities.
Why here: stated: this is the chapter's own account of its place in the book, allocations so far were across classes.
Paragraphs: claim · code · result
Note: the placement argument sits at the end of the theory section rather than in the opening.

### Four Routes (1408 words)
Says: Four responses, two changing what may be owned and two how it is estimated, each demonstrated and then plugged into the optimizer through a moment function.
Why here: stated in the opening's plan and repeated in ¶1: the routes are taken in order of what they cost.
Paragraphs: method
Note: the announced cost order holds for routes one to three and then breaks: route four is a one-paragraph stub, two subsections on plumbing and patching follow, and route four is done in full last.

#### Route one: hold fewer things (85 words)
Says: Allocate across classes or sleeves and the matrix is estimable on five years; this is what mandates do, but it does not help when the mandate names securities.
Why here: stated: the cheapest fix.
Paragraphs: claim · claim
Note: no code; the only route demonstrated nowhere and absent from the race in the application.

#### Route two: impose a structure (412 words)
Says: A k-factor structure replaces N(N+1)/2 parameters with Nk + N and cannot be singular; six lines do it, while the package's version refuses exactly the windows where it is needed.
Why here: next in the cost order; takes the parameter count from the theory section as its motivation.
Paragraphs: definition · method · code · result · transition · code · caveat

#### Route three: shrink the matrix (205 words)
Says: Pull the sample matrix toward a well-conditioned target with a data-chosen λ; it needs no assumption, cannot fail and is always invertible.
Why here: next in the cost order; not otherwise stated.
Paragraphs: definition · claim · code · result

#### Route four: estimate robustly (38 words)
Says: A robust estimator fixes a matrix badly centered by a few months, a different problem from a short sample, deferred to later in the section.
Why here: stated: it is a different problem and is "taken up below".
Paragraphs: transition
Note: a route announced in one paragraph and deferred past two unrelated subsections; the subsection does no work of its own.

#### Getting any of this into the optimizer (298 words)
Says: The package's moment function offers no shrinkage, but `momentFUN` accepts a function object, so any estimator plugs in without leaving the package's constraints behind.
Why here: needs route three's estimator to have something to plug in; the text gives no reason for its sitting between the two halves of route four.
Paragraphs: caveat · code · result · method · code · claim · caveat+c
Note: the chunk prints holdings, sum and maximum weight of the shrunk minimum-variance portfolio and no paragraph reads them; the callout title is a `##` line, which a count of `##` headings picks up as a sixth section.

#### When the package function is the thing in the way (88 words)
Says: Beyond working around a package function, the right option on open source is to patch it and send the fix back; appendix D lists this book's patches.
Why here: not stated; it argues about route two's `statistical.factor.model()` check, two subsections back.
Paragraphs: claim
Note: sits between the moment-function plumbing and route four, about neither; a general remark on package practice with no code.

#### Route four in full: robust estimation (257 words)
Says: The package's robust estimators, the MCD among them, plug in like shrinkage and report lower volatility by discounting unusual months, which this market's co-arriving extremes argue against.
Why here: stated implicitly: they plug in "exactly where route three did", so the moment-function mechanism had to come first.
Paragraphs: claim · code · definition · transition · code · caveat
Note: the demo runs on the sixteen classes, not the equities the chapter's problem is posed on; the shrinkage-versus-robust contrast in ¶2 repeats the route-four stub and returns as takeaway 4.

### What the Routes Do to the Matrix (1759 words)
Says: Scored out of sample, shrinkage wins only where the sample matrix cannot be computed and ties once it can; the identity target is least true in a crisis; and long only was already shrinking.
Why here: stated in the opening's plan: after the routes, ask which of them pays out of sample. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: the heading names what the routes do to the matrix, but the section opens with portfolio scores and reaches the matrix (the spectrum) only in the middle of its second subsection; four subsections, four topics.

#### Scoring the routes out of sample (598 words)
Says: On identical months, two of four estimators return no portfolio at sixty and one hundred and twenty months; shrinkage runs and has the lower volatility, but at one hundred and eighty months it ties the sample matrix and its λ has fallen.
Why here: stated: the matrix cannot score itself, every estimator flatters itself in sample, only an out-of-sample test is honest.
Paragraphs: method · method · code · code · code · result · result · transition · code · result · result
Note: the race's four estimators are not the chapter's four routes: a diagonal estimator appears here without having been introduced, and routes one and four are never scored; the race lives in a script carrying chapter 5's name.

#### Lower volatility is not a better portfolio (546 words)
Says: Sharpe ratio orders the estimators differently from volatility, and minimum variance beat equal weighting here against the general finding; then every route is shown as one operation on the eigenvalue spectrum.
Why here: a second reading of the race table, stated as "sharpe is not ann_vol"; the spectrum part is justified as "easier to see than to derive", not as belonging here.
Paragraphs: result · result · transition · code · result · code · result
Note: two topics under one heading: ¶1–2 read Sharpe ratios from the race, ¶3–5 and the chapter's only figure show what shrinkage does to the spectrum, which is what the parent section is named for; ¶4 repeats the coin-flip point of the theory section; the heading is a claim sentence rather than a noun phrase.

#### Shrink towards what, when the target moves? (475 words)
Says: The identity target asserts unrelated assets, which is wrong in calm months and far wronger in the credit crisis, exactly when the portfolio depends on it; hence a factor target where available.
Why here: not stated; takes F from route three and the episodes from the data, and hands the choice on to chapter 19.
Paragraphs: claim · code · code · result · claim
Note: switches to the sixteen classes, the universe where the chapter said the problem does not arise; the heading is a question.

#### The shrinkage already in place (140 words)
Says: The long-only constraint acts on the solution as shrinkage acts on the matrix, and had already done work comparable to route three before any estimator changed.
Why here: stated: "one last connection, because it reframes much of this book".
Paragraphs: claim · evidence
Note: "comparable" is asserted, not computed in the chapter; exercise 4 asks the reader to quantify it.

### Key Takeaways (257 words)
Says: Seven bullets: the rank bound, the riskless portfolio, the condition number, the four routes, shrinkage's limits, minimum variance against equal weighting, long only as shrinkage.
Why here: by contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: seven bullets against the contract's "around five"; bullet 6 restates ¶2 of the Sharpe subsection nearly sentence for sentence.

### Exercises (160 words)
Says: Four exercises: a near-singular bond block, a λ grid, factor against shrinkage on rolling windows, and the long-only effect quantified.
Why here: by contract.
Paragraphs: exercise · exercise · exercise · exercise
Note: four against "around three"; exercise 1 follows up the instrument-level diagnosis of the theory section, exercise 4 supplies the computation the last subsection asserts.

## Chapter 8: Estimation Error and Its Cost (7979 words, 51 paragraphs)
Claim: What an input costs is set by how well it can be estimated; the mean cannot be, so the rule that estimates it promises most and delivers least, while the rules that estimate only the covariance keep most of their promise and lead the register.
Question: How much is a better forecast worth, in Sharpe ratio; the opening cites @demiguel2009 for asking it the other way round (none of fourteen optimizing rules beat 1/N reliably), with the line from @jobson1980 to @ledoit2004 behind it.
Why here: The text says ch. 6 and ch. 7 estimate the mean and the covariance separately and this chapter measures what they cost together and which costs more; it takes the objective from ch. 3, the tangency and minimum-variance solutions and their quadratic programs from ch. 9 one chapter ahead, the precision result from ch. 4, the condition number from ch. 7, and the rolling scheme and the register from ch. 25; it says ch. 26 and ch. 27 take the forecast-error measure from it, ch. 14 treats inverse volatility in its own right, and ch. 19 and ch. 28 take up the drift it cannot price.
Does: Measure a rule's Sharpe gap on rolling windows against the equal-weight control; split an estimated portfolio's loss between the mean and the covariance by substitution under a simulated truth; locate the window at which a plug-in rule overtakes 1/N on a given universe; call the two naive rules directly rather than through the rebalancing loop.
Order: Opening (question, roadmap, data), theory (the plug-in rule, the two naive rules, inflation and expected loss with a worked callout, the gap defined), implementation (the naive rules and their trap, the two quadratic programs, the rolling loop with a cross-check against the register, the gap table and figure), application (a simulated truth, the two channels, forecast error in the investor's units, the crossover region, the register line), takeaways, exercises. Deviations: the theory section takes its portfolios and programs from ch. 9 and derives nothing itself; the application opens with a method paragraph and three numbers, not with a picture; the chapter's first result arrives at the end of the implementation section; the forecast-error subsection is a one-paragraph pointer to Part VIII placed between the channel split and the crossover; seven takeaways and four exercises.

### Opening (before the first heading) (493 words)
Says: Estimation error is the oldest problem in portfolio theory, and this chapter measures what it costs a strategic allocator on the sixteen class series.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections and no reason for the chapter's place in the part.
Paragraphs: code · claim · method · method · code
Note: ¶1 is one block of eleven citations, each with its finding, and the chapter's own question returns only in ¶2's roadmap; the data chunk already computes the full-sample moments the application will treat as the truth, two sections before the text says so.

### The Plug-In Rule and the Price of Its Inputs (1729 words)
Says: The plug-in rule substitutes sample moments into ch. 9's solutions; under normality its promise is inflated by N/T and its expected utility falls short by a known formula; the Sharpe gap is the version of that shortfall a backtest can compute.
Why here: The roadmap's first step; the text says the gap needs a definition computable without a truth before the implementation measures it, and distinguishes it from the loss the application measures. Paragraphs: none before the first subsection.
Note: The section's portfolios, equations and programs are ch. 9's, cited ahead; the section defines and interprets but sends the one derivation to @kan2007.

#### What the estimator is asked to do (219 words)
Says: The objective needs μ and Σ, neither observed; the plug-in rule substitutes sample estimates, and the minimum-variance portfolio is the one that needs no mean.
Why here: First in the section; the text says the two portfolios' one difference, whether μ̂ is needed, decides the chapter.
Paragraphs: definition · method
Note: ¶1 does four jobs: the two estimators, the two portfolios, the Merton precision point, and the chapter's position against ch. 6 and ch. 7.

#### Two rules that estimate almost nothing (150 words)
Says: Equal weighting estimates nothing and inverse volatility one moment per asset; both are estimators, and the comparison is a sequence of rules estimating zero, one or all moments.
Why here: not stated; the benchmarks are defined before the mechanism that makes them win.
Paragraphs: definition
Note: The reading rule for the whole comparison (not naive against sophisticated) closes a definition paragraph.

#### Why the promise is inflated and the delivery is not (1045 words)
Says: The inverse covariance amplifies the mean's error; under normality a window manufactures a squared Sharpe ratio of N/T from noise, and the plug-in investor's expected utility is negative on sixty months of sixteen series.
Why here: The text says the Best–Grauer mechanism is visible in eq-08-plugin, so it follows the definition; the box puts this universe's numbers into the formula before the gap is defined.
Paragraphs: claim · derivation · claim · method+c · code · example+c · code · method+c · code · result+c
Note: ¶6 says the draw checks whether non-normality matters at the first decimal, but it draws from a normal, and ¶7 reads the agreement as the algebra working, so the question ¶6 poses is left open; the callout is collapsed and holds the chapter's only worked formula with numbers substituted.

#### The Sharpe gap (315 words)
Says: The gap is the average promised Sharpe ratio on the window minus the realized one out of sample, computable without a truth, with equal weighting's own gap as the control.
Why here: The text says the two formulas' statements (promises more, delivers less) need a definition computable where the truth is unknown; the implementation measures the gap, the application supplies a truth and measures the loss.
Paragraphs: definition · definition
Note: ¶1 states the rolling scheme by reference to eq-25-backtest, seventeen chapters ahead.

### Measuring the Gap on Rolling Windows (2012 words)
Says: On sixty-month windows the rule that estimates the mean promises most and keeps least of its promise; the gaps are ordered by how much each rule estimates and the realizations in the reverse order.
Why here: The roadmap's second step; needs the four rules and the gap definition of the theory section; the text cross-checks its realized numbers against ch. 25's register so that the two chapters agree. Paragraphs: none before the first subsection.
Note: The section's one result arrives in its last subsection, after two subsections of tooling (the naive functions and their trap, the two programs and their check) and one of loop and cross-check; the table opens that last subsection with no prose before it.

#### The naive rules in `PortfolioAnalytics` (378 words)
Says: `equal.weight()` and `inverse.volatility.weight()` are exported, return an `optimize.portfolio` object, and return NA weights without a message when passed by name to the rebalancing loop.
Why here: not stated; the two benchmarks come first, as in the theory section.
Paragraphs: method · code · code · code · result · caveat+c · code · caveat+c
Note: ¶5 bolts the `max_sum` detail onto the dispatch trap; the callout sits where a reader would reach for the loop, as the contract asks.

#### The two optimized rules as quadratic programs (496 words)
Says: The long-only minimum-variance and tangency portfolios are written directly as `quadprog` problems, checked against the package on the full sample, and the full-sample tangency's Sharpe ratio is recorded.
Why here: The text says the loop and the simulation solve thousands of problems, so the programs the package would hand to `quadprog` are written directly, with one check against the package before they are trusted.
Paragraphs: method · code · method · code · result
Note: ¶3 does three jobs (the check, the `maxSR` aside, the full-sample tangency) and calls that Sharpe ratio the promise every shorter window is compared with, but the next two subsections compare promise with realization, and the number returns only in the application as the ceiling.

#### Three hundred and twelve windows (491 words)
Says: The loop forms the four portfolios on every sixty-month window, scores from the first month of model year 11 as the register does, and reproduces the register's realized Sharpe ratios to within a thousandth.
Why here: The text says the realized Sharpe ratio is computed the register's way and from the register's start so that the two chapters compare to the third decimal; the cross-check runs before the table is read.
Paragraphs: method · code · method · code · code · result
Note: The title counts every window, but the table scores only those from the register's start; the section ends on the cross-check and the gap itself is read in the next subsection.

#### The gap, rule by rule (647 words)
Says: The tangency portfolio promises most and keeps least, minimum variance realizes most, and the gaps are ordered by how much each rule estimates, an order the scoring period does not change.
Why here: not stated; the loop's output is tabulated and drawn once the cross-check has passed.
Paragraphs: code · code · result · code · result
Note: The subsection opens on a table with no prose; ¶1 already carries the all-windows comparison, so ¶2 restates ¶1's order with the estimation-count reading; the hidden `gap-facts` chunk asserts the order the prose states.

### Where the Loss Comes From (3065 words)
Says: Under a simulated truth the mean channel accounts for nearly the whole loss, the long-only plug-in rule beats 1/N at every window shown, and the backtest's shortfall against the simulation is drift that a fixed truth cannot price.
Why here: The roadmap's third step; the text says a backtest cannot say which input caused the gap because the truth is unobserved and a simulation can; the register line closes it as every construction chapter is closed. Paragraphs: none before the first subsection.
Note: The longest section, two fifths of the chapter, five subsections; the reconciliation of simulation and backtest, the chapter's answer, sits as the third paragraph of the crossover subsection and is restated in the register line.

#### A truth to score against (232 words)
Says: The full-sample moments serve as the truth, normal draws of T months are estimated and scored under it, and the true long-only tangency's Sharpe ratio is the ceiling.
Why here: The text says a backtest cannot attribute the gap and a simulation can; it needs a truth before the channels are split.
Paragraphs: method · code · result
Note: The application opens with a method paragraph and three numbers, not with a picture; the normality caveat of the theory callout returns here as a pointer to an exercise.

#### The mean channel and the covariance channel (884 words)
Says: Substituting the true moment one at a time, the mean channel costs several times the covariance channel at sixty months, the covariance channel is nearly closed on sixteen series, and the plug-in rule beats 1/N at every window shown.
Why here: The text says the decomposition is Chopra–Ziemba's by substitution, so it follows directly from having a truth; the crossover it notices is located two subsections later.
Paragraphs: method · code · code · code · result · code · result
Note: ¶2 does five jobs in one block (the split, the ratio against Chopra–Ziemba, its rise with T, why the covariance channel is closed, why the mean channel stays open); ¶3 points to the subsection after the next, past the forecast-error paragraph.

#### Forecast error in the investor's units (196 words)
Says: Mean squared error scores a forecast in the wrong units; the loss on the mean channel is the forecast error in Sharpe ratio, which ch. 26 derives and ch. 27 builds on.
Why here: not stated beyond the number it reads from tbl-08-channels; it stands between the channel split and the crossover that the previous paragraph pointed past it to.
Paragraphs: claim
Note: A one-paragraph subsection without code, a forward pointer to Part VIII placed mid-application; it reads a table shown one subsection earlier and the crossover argument resumes after it.

#### When $1/N$ stops winning (1227 words)
Says: On sub-universes of four, eight and sixteen series the long-only rule overtakes 1/N far earlier than the unconstrained one and the required window does not grow with N, because the benefit of optimizing grows with it; the backtest overtakes later than the simulation says, and the difference is drift.
Why here: The text says DeMiguel's thousands of months hold the benefit fixed while the cost grows with N, and on this universe nothing is held fixed; it answers the crossover question the channel subsection's ¶3 deferred.
Paragraphs: method · code · code · code · code · result · claim
Note: ¶3 is the chapter's reconciliation of simulation and backtest and its central claim, placed as the last paragraph of a subsection titled for the crossover, then restated in the register line and in takeaways 5 and 6; ¶2 reads a table and a figure in one block with five citations.

#### The register line (526 words)
Says: On sixty-month windows the rules that estimate no mean occupy the first four places and the tangency portfolio is last; on 120-month windows it is ahead of both naive rules; minimum variance is strongest at every window, and the lesson is that the mean cannot be estimated.
Why here: The text says every construction chapter ends by reading its strategy off ch. 25's register so that no chapter carries a number another could contradict.
Paragraphs: method · code · code · result · claim
Note: ¶3 repeats the sixty-against-120 comparison of the previous subsection's ¶3, standard error included; the chapter's last sentence, that an input's cost is set by how well it can be estimated, is the chapter's claim in its final form and appears here for the first time.

### Key Takeaways (348 words)
Says: Seven bullets: the two Kan–Zhou formulas, the gap and the shares kept, the channel split, the crossover's two determinants, the lower-bound reading, the register order, and the naive-rule trap.
Why here: Chapter contract; not stated.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Seven against the contract's around five; ¶5 and ¶6 both state the sixty-against-120 ranking; ¶7 is the only bullet about the package.

### Exercises (213 words)
Says: Four exercises: the gap on 120-month windows against the register, a block-bootstrap truth for the channel split, the Kan–Zhou thresholds for N = 16 and 50, and a crude mean shrinkage in the loop.
Why here: Chapter contract; not stated.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against around three; the register line already gives the 120-month ranking exercise 1 asks for; exercise 2 is announced twice, in the theory callout's normality caveat and in the application's first paragraph.

# Part IV: Portfolio Optimization

## Chapter 9: Mean-Variance Optimization (10239 words, 101 paragraphs)
Claim: The textbook frontier on the sixteen series is a sequence of quadratic programs whose left end is set by the least volatile asset rather than by diversification, whose right end moves several times as far as the left when the sample is resampled, and whose tangency portfolio keeps the smallest share of its promised Sharpe ratio out of sample while minimum variance, which needs no μ, keeps the most.
Question: How should an investor divide wealth across assets that differ in expected return, volatility and comovement; @markowitz1952.
Why here: Says Markowitz is the point every later method departs from; needs the sixteen series of chapters 2 and 4, the excess basis and dominance vocabulary of chapter 3, the factor finding of chapter 5, the rolling moments of chapter 4 and the estimated inputs of chapters 6 and 7 (chapter 8, on estimation error, is never cited); chapter 10 changes the risk measure, 11 adds moments, 12 prices constraints, 13 the solvers, 15 shrinkage and universe choice, 23 the turnover, 25 the honest out-of-sample version, Part VIII the robust formulations.
Does: Specify and solve minimum-variance, tangency and quadratic-utility problems with a guarded solver call, draw frontier, weights and capital allocation line from one data frame, and test a frontier for stability, source of volatility reduction, constraint cost and out-of-sample record.
Order: Opening, theory in two subsections (one carrying a twelve-paragraph worked callout), implementation in five, application in seven, Key Takeaways, Exercises; the headings keep the contract, but the implementation already reads results (the dominance count, the US_credit asymmetry), the application is half the chapter and runs five experiments on the frontier rather than showing it, and there are six takeaways and five exercises.

### Opening (before the first heading) (311 words)
Says: The question, the strategic label, the full-sample warning, and the data in excess of the bill.
Why here: Contract position; states the chapter's order (derive, implement, ask what was bought and what survives).
Paragraphs: code · claim · method · caveat · method · code

### The Mean-Variance Problem (1647 words)
Says: Portfolio variance carries the covariances, dominance gives the frontier a direction, and the problem has two closed-form anchors and a closed-form frontier that vanish under a short-sale constraint and mislead once the inputs are estimates.
Why here: The opening puts derivation first; says the dominance vocabulary is applied in the implementation before any optimizer runs; its last paragraph hands the rest of the chapter to implementation and application.
Paragraphs: definition · claim · definition · definition · definition
Note: ¶3 restates chapter 3's definition in full before the problem is posed, as the house rule asks.

#### Two anchors with closed forms (1069 words)
Says: Minimum variance needs no μ, the tangency portfolio is Tobin's single risky fund with the highest Sharpe ratio, and Merton's constants give the whole frontier.
Why here: Drops the return constraint from the problem just posed; says μ's absence will do much work later; the two-asset callout follows the formula it reduces; the tangency and the frontier need the risk-free asset Tobin adds.
Paragraphs: derivation · claim · derivation · example+c · code · example+c · method+c · code · result+c · method+c · code · result+c · claim+c · method+c · code · caveat+c · derivation · evidence · derivation
Note: The callout sits between the two anchors the title promises, so the tangency portfolio arrives twelve paragraphs after the first; ¶10 reads a sixteen-asset number before the implementation has begun.

#### Why the closed forms are not what we compute (236 words)
Says: A short-sale constraint turns the problem into a convex quadratic program, and estimated inputs make the closed forms error-maximizers.
Why here: Says every expression above assumed unconstrained weights; frames the rest: compute the textbook answer in the implementation, measure how much is real in the application.
Paragraphs: claim · evidence · transition

### Implementation (2943 words)
Says: Once the inputs have been looked at, each anchor is four lines in PortfolioAnalytics, the tangency is read off a computed frontier, and the solve fails silently in enough ways to need a guard.
Why here: The theory's last paragraph says the textbook answer is computed here; the frontier, the anchors and solve_checked() built here are what the application reuses. Paragraphs: none outside the subsections.
Note: Five subsections; the dominance picture the house rule places at the head of the application sits in the first, and the chapter's first finding (the US_credit asymmetry) is read in the third.

#### Looking at the inputs first (699 words)
Says: The inputs are lopsided in volatility and correlation, the two averages differ by less than the drag, and most of the sixteen series are dominated before any optimizer runs.
Why here: Says the lopsidedness is worth seeing before any optimizer runs; the theory promised the dominance count here; says the application returns to the spread and the correlation.
Paragraphs: method · code · result · claim · code · definition · code · code · result · code
Note: The moments, the table and the figure are on total returns R while every solve uses excess returns Re, and the text does not say so; ¶3 reopens chapter 3's drag; ¶4 defines dominance a second time after the theory's ¶3; the figure follows the prose that reads it.

#### Specifying and solving the problem (330 words)
Says: Minimum variance under long-only holds few series and most of one, and that concentration is a property of the problem, not a symptom of bad inputs.
Why here: First anchor, first solve; the explanation of the concentration reads the least and second-least volatile series from the inputs just tabulated.
Paragraphs: method · code · code · result · evidence

#### The tangency portfolio (995 words)
Says: The tangency portfolio is read off a computed frontier, sits far above 60/40 in sample, and is where US_credit, the most negatively skewed series, enters a frontier whose objective cannot see the asymmetry.
Why here: Second anchor; says the portable route is to compute the frontier and read the best point, which is why the frontier is built here and reused by every later figure; says two things matter later.
Paragraphs: method · code · code · code · result · method · code · result+c · code · result+c · method+c · code · result+c
Note: ¶1 promises a callout on maxSR that no callout in the chapter gives; ¶2 carries the chapter's first finding and two forward references inside the implementation; the hidden frontier-facts chunk asserts what ¶2 says; the closed-form callout is what exercise 2 asks for.

#### Three ways this fails without an error (762 words)
Says: A metaheuristic approximates the quadratic program, a wrong second solver name returns a weightless shell, an exact budget is reported infeasible on CRAN, and a target on the return objective is dropped under CVXR.
Why here: Not stated; follows the first solves; says the guard belongs in anything that solves more than once, which the bootstrap and chapter 25 are.
Paragraphs: claim · caveat · caveat · code · caveat · code · caveat · code · caveat · code · caveat · caveat · code · caveat
Note: The heading counts three and the text walks four (the warning callout, solver names, the budget callout, targets); the budget callout calls itself "a second failure", and the first failure has no numbered place in the sequence.

#### The package's own frontier chart (154 words)
Says: chart.EfficientFrontier() draws the whole picture in one line and locates the tangency by scanning, but two defaults (rf = 0, match.col = "ES") must be known.
Why here: Not stated; closes the implementation with the one-line version of the picture the application then rebuilds by hand.
Paragraphs: code · code · caveat

### What the Frontier Actually Buys (4889 words)
Says: The frontier is a set of separate answers whose weights show where each asset enters and leaves; its right end is poorly determined, its left end is set by the least volatile asset rather than by diversification, each constraint costs where the unconstrained answer was absurd, and out of sample the tangency portfolio keeps least.
Why here: The theory's last paragraph says the application measures how much of the textbook answer is real; the last subsection hands the gap between in sample and out of sample to the rest of the book. Paragraphs: none outside the subsections.
Note: Seven subsections, half the chapter; the first two show the frontier and the last five are experiments on it (resampling, two universes, five hundred universes, a constraint ladder, the register), each with its own method, code and result.

#### The frontier is a set of answers, not an object (1093 words)
Says: Each frontier point is its own quadratic program, and the quadratic-utility diamonds, the capital allocation line through the origin and the scanned tangency are the three places the picture goes wrong.
Why here: Opens the application with the whole picture; says each element is computed because none is as obvious as the theory makes it look; the frontier and the anchors come from the implementation.
Paragraphs: claim · method · code · result · code · method · code · code · claim · claim · caveat · claim · method · code · result+c
Note: ¶5 announces and does no work; ¶8 makes the maxSR point for the third time and points to an explanation the implementation does not contain; the callout's title promises four ways of asking and its table compares two (quadratic utility against the frontier at equal volatility); ¶2 repeats the "read it off" point of the tangency subsection.

#### Reading the frontier through its weights (591 words)
Says: The weights show which assets enter, swell and leave, and the long-only frontier's right end is always one asset.
Why here: Says the frontier figure shows where the answers landed but not why, and the why is in the weights.
Paragraphs: method · code · result · code · code · code · method · code · result+c
Note: ¶3 is one sentence introducing a figure; the corner-solution chunk follows the prose that states it.

#### The left end is stable and the right end is not (519 words)
Says: Resampling the sample in twelve-month blocks moves the tangency portfolio several times as far as the minimum-variance portfolio, because the right end depends on μ.
Why here: Picks up the theory's promise that μ's absence from the minimum-variance portfolio would do work later; needs chapter 4's rolling moments and solve_checked() from the implementation.
Paragraphs: claim · method · code · code · result · claim

#### Diversification effort and diversification payoff are unrelated (698 words)
Says: The equity-only minimum-variance portfolio holds more effective positions and buys a smaller discount than the mixed one, and the non-equity series add only a floor.
Why here: Not stated; questions the other property of the minimum-variance portfolio, its low volatility, after its stability.
Paragraphs: claim · method · code · definition · result · result · code · result
Note: ¶3 defines effective bets after the chunk computes it; the chunk's comment carries the definition first.

#### Five hundred universes, one constant (400 words)
Says: Across random sub-universes the least volatile asset explains almost all of the minimum-variance level and correlation almost none, so the universe fixes the answer before the optimizer runs.
Why here: Says two universes are suggestive and no more; the pattern must hold on universes nobody designed.
Paragraphs: method · code · result · method · code · result · claim
Note: ¶3 is a one-line question introducing a chunk.

#### What each constraint costs (822 words)
Says: Each rung of a four-step constraint ladder moves the frontier south-east, and the cap and the group limits cost mainly where the long-only answer was one position.
Why here: Not stated; reuses the frontier machinery; says the last observation is chapter 12's argument in one picture.
Paragraphs: method · code · code · code · result · claim
Note: Three chunks run between the method and the result; the hidden assertions in the table chunk carry the facts ¶2 reads.

#### And it does not survive contact with the future (759 words)
Says: On the sixty-month register the tangency portfolio keeps the smallest share of its promised Sharpe ratio and finishes last of the three, minimum variance leads in every cell, and the order against equal weighting depends on the window.
Why here: Says everything above is in sample; reads the out-of-sample column from chapter 25's register so the two chapters cannot drift; closes by handing the gap to the rest of the book.
Paragraphs: method · code · code · result · evidence · transition
Note: ¶1 states the result before the table; the hidden oos-ranking chunk asserts the register facts ¶3 reads.

### Key Takeaways (220 words)
Says: Six bullets: the quadratic program, the μ-free anchor, concentration, the two ends, the universe, the out-of-sample record.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six against "around five"; nothing on the silent failures, the solve guard or the constraint ladder.

### Exercises (199 words)
Says: Five exercises: money markets in the universe, the closed form against ROI, block length, the budget encoding, US_credit's asymmetry.
Why here: Contract position; each reuses an object or table of the chapter by name.
Paragraphs: exercise · exercise · exercise · exercise · exercise
Note: Five against "around three"; exercise 2 is the collapsed closed-form callout of the tangency subsection, already worked and read there.

## Chapter 10: Risk Measures Beyond Variance (7637 words, 52 paragraphs)
Claim: Replacing variance by expected shortfall changes little on sixteen class series: the two frontiers are one curve within the width of the line, the minimum-ES portfolio swaps one holding and moves one moment, and out of sample the tail rule realizes the higher shortfall because a 5% tail on sixty months is three observations.
Question: What changes when variance is replaced by a measure that is subadditive; cites Markowitz (1959) for the semi-variance and Artzner et al. (1999) for coherence in the first two sentences.
Why here: Opens on chapter 9's optimizers, which all used variance; takes the data from chapter 2, the excess basis, the strategic label, quadratic utility and the "judge by the measure chosen" rule from chapter 3, the ES definition, the Cornish-Fisher expansion, the ellipticity verdict and the credit non-normality from chapter 4, the problem, the frontier and the `US_credit` holding from chapter 9, and γ/2 from appendix B; hands the comoments to 11 ("here they enter only through the measure"), the convex-versus-search distinction and the ratio normalization to 13, the ES decomposition to 14, the register to 25, the cost of a tail estimate to 26, and two upstream issues to the package notes. That one clause is the only reason given for preceding chapter 11; why it precedes 12: not stated.
Does: Test subadditivity on every pair of a panel; pose minimum ES as the Rockafellar-Uryasev linear program under `ROI`; read any weight vector on every measure with `extract_risk()`; trace two frontiers from one data frame; name the solver each objective needs; set the ratio flags explicitly; recognize an unevaluated `CSM` and a wrong-sign `EQS`; read the register with an error bar.
Order: Theory in six subsections (coherence, value at risk, expected shortfall and its linear program, the modified measure, downside and drawdown and two more coherent measures, what each measure assumes), implementation in three (the four specifications and the package defaults, the mean-ES frontier, `CSM` and `EQS` under `CVXR`), application in three (four portfolios on one table, the cross table, the register), five takeaways, four exercises. Deviations: the theory runs code in two collapsed worked boxes; all three figures and the chapter's central reading (the `US_credit` weight along the two frontiers and the one-month skewness behind it) sit in the implementation, so the application opens on a table rather than a picture; none of the three content sections has prose of its own above its subsections; the fourth of the four portfolios is produced by a chunk whose only introduction is inside a callout about a different trap.

### Opening (before the first heading) (351 words)
Says: Nothing in the data required variance; Artzner asked which properties a risk measure needs, value at risk lacks the one that matters, and the chapter asks what a measure that has it changes.
Why here: Contract position; the text gives the sequence: axioms, value at risk, expected shortfall and its program, the modified measure, the other families, then the package, then one problem under four objectives.
Paragraphs: code · claim · method · method · code · code
Note: The "packages used" block is hidden (`include: false`), so the reader sees no package list; ¶2's register promise is redeemed only by the application's last subsection.

### Coherence, Tails, and What Variance Assumes (1879 words)
Says: A risk measure must be subadditive to respect diversification; value at risk is not, expected shortfall is and is a linear program, the modified version is not convex, and every measure encodes a belief about the investor.
Why here: The opening's first clause ("We first set out the coherence axioms"); the subsections follow the opening's list in order. Paragraphs: none of its own.
Note: Heading only; six subsections, two of which run code in collapsed boxes that later prose and the first takeaway depend on.

#### Four properties of a risk measure (229 words)
Says: Coherence is four axioms, subadditivity is the one that matters for building portfolios, and variance is used despite failing it because under elliptical returns the choice of measure changes no ranking.
Why here: The opening's question is about "that property", so it is defined first; needs chapter 4's verdict that this market is not elliptical; ¶2's "the last axiom is the one that matters here" sets the test the next subsection applies.
Paragraphs: definition · claim

#### Value at risk (450 words)
Says: Value at risk is the regulatory standard, satisfies three axioms and fails subadditivity, on this data for a few credit-government pairs of the same currency.
Why here: Named in the opening as the standard that lacks the property; the text says the failure is "not only in contrived examples", so the box tests it on every pair; the box's "expected shortfall, defined below, fails on none" hands over.
Paragraphs: definition · method · code · code · result+c
Note: The collapsed box defines `loss_var()` and `loss_es()`, which every later chunk that reads a tail uses (`es-by-hand`, `ratio-defaults`, `frontier-frame`, `four-portfolios`), and its `mix` is what the first takeaway counts; a box a reader may skip is load-bearing. The subsection title is the measure; the box carries the finding.

#### Expected shortfall and the linear program (552 words)
Says: Expected shortfall is the smallest coherent measure dominating value at risk, and the Rockafellar-Uryasev representation turns its minimum into a linear program with one variable per month.
Why here: "Defined below" from the box; the text says the dominance property "is why it is the tail measure this book uses", and the representation is "what made expected shortfall usable in an optimizer", which the implementation needs; the box's Cornish-Fisher figure opens the next subsection.
Paragraphs: definition · derivation · method · code · example+c
Note: ¶2 is one sentence chain across two display equations doing six jobs (representation, convexity, the LP, atoms, convex versus search, frontier and STARR). The box's `tail_months` is read again by the credit-tail paragraph of the implementation.

#### The modified expected shortfall (177 words)
Says: The Cornish-Fisher expected shortfall replaces the few tail observations by a four-moment expansion, which makes it depend on every comoment and leaves it non-convex, reachable only by search.
Why here: Follows the box's disagreement between the two figures; the text gives Yamai-Yoshiba's larger standard error as the reason for the alternative; hands non-convexity to the implementation and chapter 13, the tensors to 11, the decomposition to 14.
Paragraphs: definition
Note: One paragraph that defines the measure, routes it to three chapters and ends on a package default already stated in chapter 4.

#### Downside measures, drawdowns, and two more coherent measures (227 words)
Says: Lower partial moments, conditional drawdown at risk and the second-order CSM are the other families, the last a cone program; the package's EQS is documented only by its code.
Why here: "Three further families deserve a place", the oldest first; no other reason given; CSM and EQS are defined here because the implementation solves them, and which tail EQS squares is "measured rather than assumed" there.
Paragraphs: definition
Note: Three families and two display equations in one paragraph; the lower-partial-moment and drawdown families are defined and then never solved, read or mentioned again in the chapter.

#### What the choice of measure assumes (244 words)
Says: Variance is right only under quadratic utility or two-moment returns; a tail measure responds to the skewness that lives in credit, at a cost in estimation; and a portfolio must be judged by the measure it was chosen by.
Why here: Closes the theory on chapter 3's investor; needs eq-03-quadratic-utility and chapter 4's credit finding; the rule in ¶2 is the one the application follows ("sec-10-application does that").
Paragraphs: claim · method
Note: ¶1 does five jobs (utility theory, the credit fact, asset pricing, estimation cost, a pointer to chapter 11). The ellipticity argument of "Four properties" ¶2 is restated here and a third time in the implementation's credit-tail paragraph.

### Implementation (3135 words)
Says: Four specifications on one constraint set go to `ROI`, `DEoptim` and `CVXR`; the package's ratio defaults, its ignored `method`, an unevaluated `CSM` and a wrong-sign `EQS` are measured; and the two frontiers nearly coincide as curves while disagreeing on `US_credit`.
Why here: The opening's second clause ("then show which of these the package can solve, with which solver, and where its defaults do something other than what the specification says"). Paragraphs: none of its own.
Note: Heading only. The section holds all three figures of the chapter and the reading that explains the `US_credit` result (the one-month skewness), which is application rather than implementation; the application section that follows has tables only.

#### The objectives the package knows (1086 words)
Says: The four specifications are solved, three by `ROI` and the modified one by differential evolution, and two defaults are measured: `ROI` ignores `method`, and a mean plus a tail objective is a ratio problem unless told otherwise.
Why here: First because the four specifications "carry the chapter"; needs eq-10-lp, eq-10-var and the γ/2 convention; produces the four weight vectors the application reads.
Paragraphs: method · code · method · code · code · code · result · caveat+c · code · method+c · code · caveat+c · code · code · result+c
Note: Five of the eight paragraphs sit in two callouts. The chunk that produces the fourth chapter portfolio (`solve-modified`) stands between the callouts with no prose of its own; its introduction (¶6) is the last paragraph of a callout about a different trap. The ratio callout builds `spec_mean_es` and `spec_mean_sd`, which the frontier subsection then traces.

#### The mean-ES frontier (1243 words)
Says: The mean-ES and mean-variance frontiers are the same curve within the width of the line and different portfolios in `US_credit`, whose skewness is the work of one month that a 5% historical tail averages away.
Why here: Not stated beyond the function existing; needs the two-objective specifications from the ratio callout; the mean-variance frontier of chapter 9 is "computed beside it on the same constraints", and the `US_credit` holding is the one chapter 9's application traced.
Paragraphs: method · code · code · method · code · code · code · result · code · result · code · result
Note: The package's own chart (`fig-10-native-frontier`) is drawn and never read in prose; its caption does the reading. ¶5 is the chapter's explanation of its main result and the third statement of the ellipticity argument. Two chunks and a figure separate ¶2 from ¶3.

#### Two coherent measures that need a cone solver (806 words)
Says: `CSM` and `EQS` solve under `CVXR` beside the minimum-ES portfolio; a search on `CSM` evaluates nothing and returns its first candidate, and the package's `EQS` squares the gains rather than the losses.
Why here: "Their minimum-risk portfolios sit beside the minimum-ES one" is the only reason given; the two measures were the last defined in the theory, and the EQS question the theory deferred is answered here.
Paragraphs: method · code · caveat+c · code · caveat+c · caveat+c · code · caveat+c · code · result+c
Note: Five of six paragraphs and three of four chunks are two callouts; the subsection is a pair of traps with one method paragraph in front. The `CSM` and `EQS` weights of `csm-eqs` are printed once and never enter the application's four portfolios.

### Four Objectives on One Universe (1639 words)
Says: On one long-only problem only quadratic utility holds `US_credit` in size, the minimum-ES portfolio swaps one holding and moves one moment at a small price, and out of sample the tail rule realizes the higher shortfall at every window.
Why here: The opening's third clause ("then solve one long-only problem under four objectives and read what each bought"); needs the four weight vectors of the implementation. Paragraphs: none of its own.
Note: Heading only; no figure in the section. The portfolios are solved in the implementation, so the application's first act is a table.

#### What each objective bought (727 words)
Says: The quadratic-utility investor holds the most negatively skewed series for its Sharpe ratio, the no-mean objectives hold almost none, minimum ES is the closest to symmetric, and the search did not find its own minimum.
Why here: "The four portfolios of sec-implementation" differ only in what they call risk; the `US_credit` column is read first "for the reason chapter 9 gave".
Paragraphs: method · code · code · code · result · result
Note: ¶2 reads six columns of the table in one paragraph carrying fifteen inline numbers.

#### Each portfolio on every measure (313 words)
Says: Each convex portfolio is best on its own measure, the searched one is not, and the price of choosing the tail is small in the other measures.
Why here: The rule of chapter 3 that the theory's last paragraph promised the application would honor; the table "does that on the diagonal".
Paragraphs: method · code · result
Note: The cross table repeats four columns of the previous table in a second layout; ¶2's "exchanged one holding and moved one moment" restates ¶2 of the previous subsection.

#### Out of sample, read from the register (599 words)
Says: On rolling windows the minimum-ES rule realizes a higher expected shortfall than minimum variance at every window, differs only in the moments it was not asked about, and the thirty-six-month row rests on a two-observation tail.
Why here: "Everything above uses full-sample moments": the opening's strategic claim sends the out-of-sample check to chapter 25's register, read rather than recomputed "so that the two chapters cannot disagree"; hands the cost to chapter 26.
Paragraphs: method · code · code · code · result · caveat
Note: The closing rule ("choose the measure for what it sees, report by the measure chosen") is the fourth statement of chapter 3's rule in this chapter, after the theory's last ¶2, the cross table's ¶1 and the fifth takeaway.

### Key Takeaways (286 words)
Says: Five bullets.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: ¶3 is four package traps in one bullet; ¶4 carries two findings and an inline number; the drawdown, lower-partial-moment and `CSM` measures of the theory have no bullet.

### Exercises (211 words)
Says: Four exercises.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; ¶4 depends on `rp`, built inside the `CSM` callout.

## Chapter 11: Higher Moments (7885 words, 59 paragraphs)
Claim: On the sixteen classes the third and fourth moments move a γ = 5 investor out of credit and into government bonds, the direction the theory predicts, but the gain is a few basis points of certainty equivalent, smaller than the error an unpolished metaheuristic leaves and than the estimation uncertainty of the tensors; and the structured estimator that tames that uncertainty removes the very skewness the tensors were wanted for.
Question: What does an investor lose by describing an asset class with two moments when its returns are skewed and fat-tailed; cites Kraus–Litzenberger (1976) in the second sentence, Harvey–Siddique (2000) and Dittmar (2002) after it.
Why here: Declares itself strategic in chapter 3's sense; takes the expected-utility expansion and CRRA from chapter 3, the shape moments, Cornish–Fisher, expected shortfall and Jarque–Bera from chapter 4, the equity factor from chapter 5, the `momentFUN` route from chapters 6 and 7, the case for structure from chapter 7, the Kan–Zhou loss from chapter 8, the problem, tangency, minimum variance, frontier weights and block bootstrap from chapter 9, and expected shortfall as a risk measure from chapter 10; hands the solver shortfall to chapter 13, conditional dependence to chapter 19, the cost of estimation to chapters 26 and 28, and the convex solvers' moment behavior to appendix D. Why it sits between chapters 10 and 12 inside the part: not stated beyond taking expected shortfall from chapter 10.
Does: Compute coskewness and cokurtosis tensors and contract them to portfolio moments; fit the single-factor structured estimator and decompose what it drops; write a four-moment CRRA objective as a custom `PortfolioAnalytics` objective, supply tensors through `momentFUN`, and assert the objective was evaluated; polish a metaheuristic answer with `slsqp()` and price the solver error as a certainty equivalent; bootstrap a tensor element; measure tail dependence against a Gaussian copula.
Order: Opening with a worked case (credit's shape and its mean-variance weight), theory (expansion, tensors and their structure, CRRA, modified shortfall, copulas), implementation (sample tensors, structured estimator, moment interface, custom objective with two metaheuristics and a polishing box, modified shortfall under two estimators, conditional comoments), application (the shape picture, seven portfolios, bootstrap, tail dependence), takeaways, exercises. Deviations: the opening runs an optimizer and reads a weight before the theory; the implementation carries the chapter's first allocation finding (the shortfall comparison) and its verdict on the structured estimator, which the application re-reads; conditional comoments close the implementation without running and without a return; five takeaways, four exercises.

### Opening (before the first heading) (584 words)
Says: The market prices skewness and kurtosis, a two-moment portfolio ignores them, and `US_credit` is the series on which the difference will show.
Why here: Contract position; the text says "the case for the chapter is one series" and recomputes its two numbers before the theory, so that the question becomes what changes once the optimizer sees more than volatility.
Paragraphs: code · claim · method · method · code · method · code · result
Note: The "packages used" block is hidden (`include: false`), so the reader sees no package list. The opening solves a quadratic-utility problem and reads a weight before any theory, and promises the tangency and frontier comparison for the application.

### Expected Utility Beyond Two Moments (1287 words)
Says: Expected utility through four moments rewards skewness and penalizes kurtosis; the portfolio moments come from tensors too large to estimate freely, and even those tensors miss the tail dependence a copula carries.
Why here: Only the opening's sequence sentence ("first extend the expected-utility expansion ... and define the comoment tensors"); the section has no paragraph of its own. Paragraphs: none of its own.
Note: Heading only; five subsections, the last three one paragraph each.

#### The four-moment expansion (297 words)
Says: A fourth-order Taylor expansion of expected utility adds a skewness term and a kurtosis term whose signs economics fixes.
Why here: "Take the investor of eq-03-expected-utility": the expansion extends chapter 3's; eq-11-taylor is the objective the rest of the chapter solves, and its convergence argument is what the application's size finding returns to.
Paragraphs: derivation · evidence · claim

#### Coskewness and cokurtosis (499 words)
Says: Portfolio skewness and kurtosis are contractions of the coskewness and cokurtosis tensors, which carry thousands of parameters on sixteen assets, so a single-factor structure replaces them at the cost of the cross terms.
Why here: "The portfolio moments in eq-11-taylor are polynomials in the weights": the expansion needs the tensors; their size is what makes structure necessary, as chapter 7 found for the covariance; the implementation is promised to show the cross-term loss on credit.
Paragraphs: definition · claim · code · definition
Note: ¶3 reads the count, defines the structured estimator and states its blind spot in one paragraph; ¶1 carries two numbered equations.

#### The CRRA investor (189 words)
Says: Substituting CRRA derivatives into the expansion gives the objective the chapter codes, reported as a certainty equivalent.
Why here: "The utility function the rest of the literature uses, introduced in chapter 3"; the text says this is the objective "we write into PortfolioAnalytics below", and the certainty equivalent is needed to report it in return units.
Paragraphs: derivation
Note: One paragraph carries two numbered equations, four derivatives, three citations and the certainty-equivalent definition.

#### The modified expected shortfall as a four-moment objective (113 words)
Says: The modified expected shortfall is a function of the same four moments, so the tensor estimator decides its minimum.
Why here: "The other four-moment objective, and the one PortfolioAnalytics uses most"; chapter 10 owns expected shortfall as a risk measure, so only its four-moment form is restated.
Paragraphs: definition

#### Dependence that no moment describes (182 words)
Says: Comoments summarize a joint distribution; a copula is one, and lower-tail dependence is what correlation and a Gaussian copula cannot carry.
Why here: "Coskewness and cokurtosis summarize a joint distribution; they are not the joint distribution": the limit of the chapter's own objects; the cross terms the structure discards are called the shadow of this, and the application measures both on the same pairs.
Paragraphs: definition
Note: Five citations and a numbered equation in one paragraph; the subsection is the theory for the application's last subsection only.

### Comoment Tensors and Custom Objectives (3199 words)
Says: PortfolioAnalytics computes the tensors in one call and feeds them by name to any objective; the structured estimator removes most of credit's skewness, a custom CRRA objective needs a global name and a polishing step, and the minimum-shortfall answer depends on which tensors it is given.
Why here: Only the opening's sequence sentence ("then implement them in PortfolioAnalytics, including the structured estimator, the moment interface and a custom objective"); the section has no paragraph of its own. Paragraphs: none of its own.
Note: Heading only; the longest section at six subsections and 26 of the chapter's 59 paragraphs, and the one that carries the chapter's first allocation finding (the shortfall comparison) and its verdict on the structured estimator.

#### The sample tensors and their shape (308 words)
Says: `set.portfolio.moments()` returns the tensors a specification's objectives need, and their contraction reproduces the portfolio's own moments to machine precision.
Why here: The function that produces the tensors comes first; the text says the identity check is "the first thing to do with them".
Paragraphs: method · code · code · code · result

#### The structured estimator (741 words)
Says: The single-factor fit loads on equities, and its tensors drop the cross terms that carry most of credit's skewness, so the estimator built to cut variance removes the feature the tensor was wanted for.
Why here: Needs the sample tensors to compare against; the theory promised that the implementation "shows that this is the case for credit"; the text says the finding "decides the allocation" in the application.
Paragraphs: method · code · result · caveat+c · code · caveat+c · method · code · result · code · claim
Note: The `match.call()` callout is the same package behavior chapter 6 measured for the Black–Litterman arguments; the text does not say so. ¶7 is the chapter's verdict on the estimator, delivered before the allocation that is said to depend on it.

#### The moment interface (350 words)
Says: A custom `momentFUN` supplies all four moments, and the returned list reaches every objective by name under the metaheuristics only.
Why here: "The same argument carries the tensors" that chapters 6 and 7 used for the first two moments; a moment function of our own avoids passing `method` through `...`, "fragile for the reason the callout above gives"; the custom objective needs the contract stated here.
Paragraphs: method · code · caveat
Note: ¶2 is one dense paragraph that states the whole calling contract and its failure mode; nothing later in the chapter exercises the failure.

#### A custom objective: the CRRA investor (1089 words)
Says: A function named in `add.objective()` becomes the objective; it must be visible from the global environment, the two metaheuristics reach its neighborhood only, and a local solver started from either finishes the job.
Why here: "PortfolioAnalytics has no expected-utility objective beyond the quadratic one", so eq-11-crra is written by hand; needs the contract of the previous subsection. Why the two solver routes and the polishing box sit here rather than in a subsection of their own: not stated.
Paragraphs: method · code · caveat+c · code · method+c · code · caveat+c · method · code · code · method · code · result · method · code · method+c · code · result+c
Note: The candidate set `rp` that every later random-portfolio solve reuses is drawn inside the callout that demonstrates the hidden-objective trap, and the collapsed box defines `polish()`, `turnover()` and `ce_annual()`, which the next subsection and the whole application depend on; a reader who skips both boxes loses the chapter's machinery. The title names the objective; the weight of the subsection is the solvers.

#### One objective, two estimators of the tensors (521 words)
Says: Minimum modified shortfall holds no credit under the sample tensors and buys it under the structured ones, and on the realized tail the structured answer is the worse of the two.
Why here: The theory said the modified shortfall's minimum "depends on which tensors it is given"; needs both estimators from the structured subsection and `rp` and `polish()` from the one before; its table is re-read in the application.
Paragraphs: method · code · code · result
Note: ¶2 does three jobs: reads the table, pronounces the chapter's verdict on the structured estimator, and dismisses a package message in its last sentence. The minimum-variance portfolio the application compares against is built in this chunk.

#### Conditional comoments (183 words)
Says: `CCCgarch.MM()` returns conditional moments under the same four names, with a silent fallback to unconditional volatility for low-`alpha1` series.
Why here: "Everything above is unconditional", stated as the contrast; why it closes the implementation, or belongs in a chapter declared strategic: not stated. Points to chapter 19.
Paragraphs: method · code · caveat
Note: The only subsection whose code does not execute; nothing later uses it, and the application does not return to conditional moments.

### What the Third and Fourth Moments Buy — 2329 (277 before the subsections) (? words)
Says: On the sixteen classes the four-moment investor moves out of credit into government bonds, as the theory predicts, for a gain of a few basis points; the tensors behind the move leave a single element's sign open, and the tail dependence they shadow is measured directly.
Why here: "The application opens with the picture", the house rule; the opening's last step ("compare on the sixteen classes what a two-moment investor, a four-moment investor and a minimum-modified-shortfall investor hold").
Paragraphs: transition · code · result
Note: ¶1 is one sentence announcing the figure.

#### Three investors and what they hold (1180 words)
Says: At γ = 5 the four-moment investor hands credit's weight to government bonds, improves skewness and the realized tail, and gains a few basis points, less than the unpolished solver had lost.
Why here: After the picture; the opening promised to return to the tangency portfolio and the middle of the frontier here; the four-moment optimum is rebuilt by multi-start polishing and asserted equal to the implementation's answer.
Paragraphs: method · code · result · code · code · code · result · claim
Note: The title says three investors; the table holds seven portfolios. ¶3 and ¶4 carry the chapter's two findings, direction and size; ¶4 ends by re-reading the implementation's shortfall table rather than adding to it. Three chunks run between ¶2 and ¶3 with no prose, and the first of them, `four-moment-optima`, is what makes the application's numbers independent of the metaheuristics; nothing in the prose says so.

#### What the tensors are estimated from (355 words)
Says: A block bootstrap leaves the portfolio's skewness negative throughout but leaves the sign of a single coskewness element undetermined, which is why the structured estimator exists.
Why here: "Every tensor above was estimated on" the one sample, and chapter 4 found rolling skewness unstable; the precision question follows the allocation it qualifies; uses chapter 9's bootstrap; sends the four-moment investor on to chapters 8, 26 and 28.
Paragraphs: method · code · result
Note: ¶2 softens the implementation's verdict ("a different estimator, biased") into "a trade rather than a defect" that Martellini–Ziemann say wins out of sample; the chapter holds both readings, and the takeaways carry only the first.

#### Dependence the tensors are a shadow of (517 words)
Says: Three pairs show more joint months in the lower tail than a Gaussian copula allows, two of them asymmetric, and credit with government bonds is the most tail-dependent pair at a modest correlation.
Why here: "tbl-11-decomposition traced the skewness of credit to the co-movement of its residual with the factor"; eq-11-tail-dep measures that directly; closes the thread the theory's last subsection opened; hands the time-series view to chapter 19.
Paragraphs: method · code · result
Note: The subsection measures what the chapter's own objects cannot, and ends by declaring the remedy out of scope.

### Key Takeaways (262 words)
Says: Five bullets.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: Five, on contract; ¶3 and ¶4 are package and solver lessons rather than chapter claims. The shortfall comparison (tbl-11-mes) and the tail-dependence measurement have no bullet.

### Exercises (224 words)
Says: Four exercises.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; ¶4 extends to five regions a pair the chapter measured for one.

## Chapter 12: Portfolio Constraints (6900 words, 55 paragraphs)
Claim: On this universe the constraints are the precondition for a portfolio anyone would hold, not a refinement of the optimization: a binding line is the mandate correcting the estimator (Jagannathan–Ma), the package accepts every constraint but honors only some, and so every solved weight vector has to be audited against the specification it came from.
Question: How does an investment policy statement, written in prose by a committee, become something a solver can read; cites Jagannathan and Ma (2003) in the second sentence and Frost and Savarino (1988) in the third.
Why here: Declares itself strategic allocation in chapter 3's vocabulary and takes chapter 3's quadratic utility and γ/2 convention; the problem, the GMV equation, the two anchors and the group-by-name rule from chapter 9; the shrunk covariance from chapter 7, the estimation error from chapter 8, the betas from chapter 5; borrows chapter 13's `maxSR` verification, its four-line `audit()` and its measurement of heuristics as if already read. Hands the non-convex solver choice to 13, `HHI()` to 14, sleeves to 15, scores to 20, turnover to 23, the transfer coefficient and tracking error to 24, the trap record to the solver matrix and the package notes. Why it follows chapter 11 and precedes chapter 13 inside the part: not stated.
Does: Build every constraint family in `PortfolioAnalytics`, know which solver honors which, audit a weight vector line by line with `audit_spec()`, price each line of a mandate by finite differences, and repair a dropped position limit with a screen.
Order: Theory (feasible set, shadow price, Jagannathan–Ma, transfer coefficient), implementation (anchors and helpers, then one subsection per family, closed by the audit function), application (a mandate solved, audited, repaired, priced line by line, read up a ladder), takeaways, exercises. Deviations: the theory's central equation is verified in a collapsed box inside the implementation; the families are implemented in neither the order of tbl-12-families nor by convexity; four traps are callouts while the two return-target traps are plain prose; the application ends in a conclusion subsection; four exercises.

### Opening (before the first heading) (288 words)
Says: A policy statement is information about which estimates not to trust; this chapter is strategic allocation, and here is the sequence.
Why here: Contract position; the text says theory first, then every constraint type against chapter 9's anchors, then a mandate.
Paragraphs: code · claim · method · code
Note: The "packages used" block the contract asks for is hidden (`include: false`), so the reader sees no package list.

### From Policy Statement to Feasible Set — 940 (366 before the subsections) (? words)
Says: A mandate replaces R^N by a feasible set; every family but the position limit keeps it convex, a binding line has a shadow price, the long-only one is covariance shrinkage, and the cost of binding is read by the transfer coefficient.
Why here: Needs eq-09-problem; the opening's sequence sentence ("first set out what each family does to the feasible set and what a binding constraint is worth") is the only reason given; the implementation's family list and the application's shadow prices rest on it.
Paragraphs: definition · definition · claim
Note: The ## title names the feasible set; the three subsections under it are about what a binding line is worth, not where the set sits.

#### What a binding constraint is worth (175 words)
Says: By complementary slackness a slack line could have been left out, and a binding line's multiplier is its shadow price, the rate at which the optimal variance falls when the bound is relaxed.
Why here: Needs eq-12-problem; the text says the application recovers eq-12-shadow by perturbing each bound, which is what this subsection defines.
Paragraphs: derivation
Note: One paragraph carries two numbered equations, the optimality conditions and the method the application later uses.

#### The Jagannathan--Ma covariance (211 words)
Says: The long-only minimum-variance portfolio is the unconstrained one on a covariance from which each excluded asset's shadow price has been subtracted, so a binding constraint is the mandate correcting the estimator.
Why here: Needs the multipliers just defined and eq-09-gmv; no reason for its position is given, but the opening named this result as the chapter's answer.
Paragraphs: derivation · derivation
Note: ¶2 carries the proof, its element-wise reading, two citations and the chapter's thesis sentence in one paragraph.

#### What constraints cost in information (188 words)
Says: The transfer coefficient is the correlation between the risk-weighted positions the constraints allow and those the forecasts called for; it is one when nothing binds and falls with every line that does.
Why here: "The other side of the ledger": the cost after the benefit; hands the measure and the tracking-error limit to chapter 24.
Paragraphs: definition
Note: Eight citations in one paragraph; eq-12-tc is defined here and computed once, in the application's cost subsection.

### Implementation (3252 words)
Says: Two anchors and a weights-by-name helper, then every constraint family the package offers, each solved against the anchors, four of them with a callout where the solver drops the line, closed by an audit function.
Why here: The opening's sequence sentence only; the section has no paragraph of its own. Paragraphs: none of its own.
Note: Heading only; ten subsections, 47 percent of the chapter.

#### Two anchors and a bookkeeping function (516 words)
Says: Chapter 9's two anchors recomputed through one helper that returns weights by name and asserts the solve succeeded; the minimum-variance anchor's concentration is the reason the chapter exists; a collapsed box checks eq-12-jm on it.
Why here: "Everything below is measured against" the anchors, so they come first; the helper is what every later chunk calls; the Jagannathan–Ma check needs the long-only anchor the theory could not yet solve.
Paragraphs: method · code · result · derivation · code · result+c
Note: The theory's central equation is verified in a collapsed box the reader may skip, two subsections after it was derived; the helper chunk's assertion is the chapter's only guard against a silent `NULL`.

#### Box constraints (150 words)
Says: A per-asset cap turns the one-series anchor into several positions at the cap, raising volatility and lowering the tangency Sharpe ratio.
Why here: Not stated; the families do not follow the order of tbl-12-families.
Paragraphs: method · code · result
Note: The replacement rule ¶1 relies on is explained only in the callout after the group subsection.

#### Group constraints (354 words)
Says: A group constraint bounds class sums; the limits are bound by name and asserted against `split()`'s alphabetical order; the solver reads only the last group constraint in a specification.
Why here: Not stated; the callout's last-group rule is what sends the regional grouping to the linear-exposure subsection.
Paragraphs: method · code · code · code · code · caveat+c
Note: The table of which group bounds bind (`group-binding`) is printed and never read; the figure is the package's base-graphics chart, unstyled.

#### Weight-sum constraints (189 words)
Says: `full_investment` and `dollar_neutral` are the two ends of `weight_sum`; the bare constraint defaults to a one-percent band that a variance objective exploits.
Why here: Not stated.
Paragraphs: method · code · caveat+c · code · result+c
Note: The dollar-neutral output (sum, gross, longs, shorts) is printed and never read in prose.

#### A target return (220 words)
Says: The return constraint is an equality, so a target below the minimum-variance return lands on the dominated branch, and `maxSR = TRUE` ignores it altogether.
Why here: Not stated; "at least" as a floor imposed only where it binds is the rule the mandate applies.
Paragraphs: caveat · code · result
Note: Two package traps (the equality, the `maxSR` override) in plain prose while the next four families get callouts; ¶2 does the reading, the rule and the second trap.

#### Position limits (556 words)
Says: The cardinality limit is accepted everywhere and honored on ROI's two mixed-integer paths and by the repairing searches; the quadratic path drops it without a message, and the Chang screen beats `DEoptim` at a fraction of the cost.
Why here: "The one row of tbl-12-families that is not convex"; the screen introduced here is what the application's repair reuses; chapter 13's point about heuristics on this universe.
Paragraphs: definition · code · caveat+c · method · code · method · code · result
Note: The callout opens with its chunk and explains after; the MILP output is printed without a reading; the screen is introduced in a chunk comment, then cited in ¶5 and reused by the application.

#### Leverage exposure (364 words)
Says: A gross-exposure bound is convex, yet under ROI the package returns the long-only portfolio because `gmv_opt_leverage()` omits the variable bounds, and under CVXR the constraint is not written at all.
Why here: Not stated.
Paragraphs: definition · code · caveat+c
Note: The subsection's only result lives inside the callout; the callout's title names the ROI defect and its paragraph adds a second one on the CVXR path.

#### Linear exposures, not only factor exposures (244 words)
Says: `factor_exposure` bounds B'w for any matrix: an indicator matrix adds a regional cap beside the group constraint, and betas bound market exposure, where a floor of 0.3 binds exactly.
Why here: "How a second grouping enters beside the group constraint above", the route the group callout promised; chapter 5's betas; chapter 20 uses the same constraint with scores.
Paragraphs: method · code · method · code · result
Note: The regional sums the first chunk prints are never read; which region binds is left to exercise 3.

#### Diversification (382 words)
Says: The floor is convex, but the package sends it only to the search solvers, where it is a band around a target rather than a floor, and ROI ignores it; the exact CVXR solve is markedly better on the objective.
Why here: Not stated; `HHI()` and `diversification()` are handed to chapter 14.
Paragraphs: definition · code · caveat+c · code · result
Note: The CVXR solve reuses `w_var` defined inside the leverage callout, so a chunk in the running text depends on a chunk in a callout.

#### Auditing a weight vector against its specification (274 words)
Says: Every failure above has one shape, a constraint present in the object and absent from the answer, and `audit_spec()` reads the specification and checks each line.
Why here: "Every failure above": the remedy after the four traps; extends chapter 13's four-line `audit()`; the application's audit table runs on it.
Paragraphs: method · code · result · code
Note: The closing figure draws the group-constrained tangency from an earlier subsection, not the audited vector, and the implementation ends on a figure with no prose after it.

### A Mandate, Line by Line (2007 words)
Says: An endowment's eight-line mandate is specified, solved on both objectives, audited, repaired where the solver dropped a line, priced line by line, and read up a ladder of its constraints.
Why here: The opening's last clause ("translate a complete mandate line by line ... solve it, audit it, and price each of its lines"); needs `audit_spec()`, the group indices and the Chang screen from the implementation. Paragraphs: none of its own.
Note: Heading only; four subsections.

#### The policy statement (701 words)
Says: Six lines enter directly, the return floor is imposed because it binds on minimum variance, the position limit is dropped by the quadratic path and caught by the audit, and a screen repairs it at a small cost in volatility.
Why here: The mandate has to exist and be solved before any line can be priced; the text says the audit "will say whether" the eighth line matters.
Paragraphs: example · code · result · code · result · code · result · code
Note: The subsection titled for the policy statement also solves, audits and repairs; tbl-12-mandate, the mandate against chapter 9's anchors, closes it with no prose reading it.

#### Which lines bind, and what each is worth (599 words)
Says: Tightening each of the seven read lines by one point and re-solving recovers finite-difference shadow prices: a few lines bind, most are slack in sample, and the return floor is the dearest for minimum variance.
Why here: Complementary slackness from the theory, applied as the theory said the application would; the cardinality line is excluded because the solver does not read it, its price being the repair above.
Paragraphs: method · code · code · code · result
Note: The hidden chunk asserts the takeaways' three claims (two lines bind on both objectives, most are slack, the return floor is dearest), which is where the chapter's prose about its own results is guarded.

#### What the mandate costs, and what it buys (507 words)
Says: In sample the mandate costs some Sharpe ratio and keeps most of it, measured by the transfer coefficient; what it buys is a portfolio instead of one position, and the in-sample cost is partly noise refused.
Why here: Prices the whole mandate after its lines; computes eq-12-tc from the theory; chapter 8's distrust of in-sample numbers and Jagannathan–Ma's point in Sharpe units.
Paragraphs: code · result · code · code
Note: Opens with a chunk, no prose before it; the ladder figure is read only in the next subsection, and its caption carries a reading (the tangency stops changing at rung three) the prose never repeats.

#### Why the constraints come first (193 words)
Says: Unconstrained minimum variance on this universe is degenerate, the cap only pins it, and the class limits alone produce a portfolio a committee would recognize, so the constraints are the precondition rather than a refinement.
Why here: Reads fig-12-ladder from the first rung; Green–Hollifield and chapter 9's volatility ratio explain the degeneracy, chapter 8's estimation error makes the constrained answer the honest one; sleeves follow in chapter 15.
Paragraphs: claim
Note: A conclusion subsection before the takeaways; one paragraph carrying eight inline numbers and the chapter's thesis, and the reading of the figure the previous subsection produced.

### Key Takeaways (241 words)
Says: Five bullets.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: Five, on contract; ¶3 restates the shadow subsection's results in three sentences and is the bullet the hidden `shadow-reading` chunk guards; ¶4 is the trap list.

### Exercises (172 words)
Says: Four exercises.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; ¶3 asks for the reading the `factor-region` chunk printed and never gave; ¶2 extends the theory the chapter checked only for lower bounds.

## Chapter 13: Numerical Optimization and Solvers (3315 words, 49 paragraphs)
Claim: Convexity, not the solver, decides whether a weight vector is the answer: the convex solvers reach an independently computed optimum exactly, every search lands short of it and slower, and three of five solvers return a portfolio that violates a position limit they accepted without a word, so every result has to be audited against its request.
Question: Which of the routines behind `optimize.portfolio()` return the answer rather than a weight vector, and which honor the constraints they accept; cites nobody in the opening — the first citation (Boyd and Vandenberghe) arrives in the theory section's third paragraph.
Why here: Stated only as "every portfolio problem posed so far" ending in a numerical routine. Takes the singular-covariance case from chapter 7, the constraint set from chapter 12 and the budget-encoding failure from chapter 9; hands the accuracy band to chapter 14's risk budgeting (said to have no convex formulation in the package), `HHI()` and `diversification()` to chapter 14, the selection-bias parallel to chapter 25, the patch state to appendix 93. Why it follows 12 and precedes 14 inside the part is implied (12's constraints are what breaks convexity, 14's problem is what forces a heuristic) but never said.
Does: Compute an independent benchmark for a long-only maximum-Sharpe problem in `quadprog`; race six solvers with `run()`; test five under a binding position limit with `feas()`; audit any result with a four-line `audit()`; combine results into one object; choose a solver by three questions.
Order: Theory (convexity, where it is lost, the independent benchmark), implementation (the race, the feasibility test, the audit, combining results), application titled as an explanation (the search budget, seeds, the decision rule), takeaways, exercises. Deviations: the benchmark is computed inside the theory section; the implementation heading has no paragraph of its own; the application runs one more experiment on the race's machinery rather than a result on the modeled market, and two of its three subsections are prose only; the opening carries no citation and no visible packages block; six takeaways, five exercises.

### Opening (before the first heading) (209 words)
Says: Every solver returns a weight vector, only some return the answer, and the chapter measures which, then asks which honors a constraint.
Why here: Contract position; the text says the families are set out first, measured second, and the honoring question comes last.
Paragraphs: code · claim · method · code
Note: No citation in the opening; the packages block is a hidden `setup` chunk and the shown chunk loads data instead. ¶2 already gives the chapter's headline (three of five infeasible), which returns three more times.

### Convexity Is the Whole Question — 606 (260 before the subsections) (? words)
Says: The choice is between convex and non-convex problems, not between solvers; on a convex problem every local minimum is global, so converged means correct.
Why here: Stated in the opening: what distinguishes the two families is set out first. Needs the positive semi-definite Σ and the singular case of chapter 7; the race reads its result through eq-13-convex.
Paragraphs: claim · definition · derivation · evidence
Note: The heading is a sentence, not a noun phrase (so is the application's). ¶3 carries three points (objective convex despite estimation, feasible set convex, the global-minimum consequence) around a display equation; the chapter's first citation arrives here.

#### Where convexity is lost (183 words)
Says: A cardinality constraint turns the feasible set into a union of faces, which needs integer variables; that is what the heuristics exist for, and nothing stops their misuse on convex problems.
Why here: Stated: not every mandate fits the simplex; draws on chapter 12's constraints; supplies eq-13-cardinality to the feasibility test and the misuse premise to the race.
Paragraphs: definition · evidence · claim
Note: ¶3 is the premise of the race in one sentence, with no example for the published misuse it asserts.

#### A problem whose answer we already know (150 words)
Says: The long-only tangency portfolio is solved directly in `quadprog`, outside the package, as the benchmark every comparison is read against.
Why here: Stated: accuracy claims require a benchmark computed outside the system under test; the race needs `w_true` and `sharpe()`.
Paragraphs: method · code · derivation
Note: A computation inside the theory section, and the explanation follows the chunk that already used it.

### Implementation (1333 words)
Says: (heading only)
Why here: Not stated; the opening's sequence sentence is the only link. Paragraphs: none of its own.
Note: Heading only; the four subsections share no introducing paragraph, and the last two (audit, combine) are tools rather than tests.

#### Racing them on a problem with an answer (634 words)
Says: Six solvers on the convex tangency problem: the convex pair hits the known answer exactly, every search falls short and is at least an order of magnitude slower.
Why here: Stated in the opening: the families are measured against a problem with a computed answer; needs `w_true` and `sharpe()` from the truth chunk; the application reuses `run()` and the band `rng`.
Paragraphs: code · code · code · result · claim · caveat+c · caveat+c · code
Note: Opens with a chunk and a table before any prose; the figure arrives after the callout, apart from ¶1 that reads it; the callout quotes the package's message verbatim as a code block.

#### Which solver honors the constraint (430 words)
Says: Under a binding position limit two solvers respect it and three, `ROI` among them, return an infeasible portfolio without a warning.
Why here: Stated in the opening: after which solver accepts a constraint, which one honors it; needs eq-13-cardinality and the benchmark's holdings count for `k_lim`; the callout says the lesson is the reason the section exists.
Paragraphs: transition · code · code · result · caveat+c · caveat+c · claim+c
Note: ¶1 promises an inversion and withdraws it in the next sentence; ¶5 restates ¶2 and the opening and returns as a takeaway; the honoring and ignoring solvers are named only through inline R, never in the prose.

#### Auditing the answer (144 words)
Says: A four-line `audit()` checks budget, sign and position count against what was requested.
Why here: Stated: the habit follows from the violation just shown and is the chapter's whole practical advice; chapter 14 takes the concentration functions.
Paragraphs: claim · code · code
Note: The check runs on the unconstrained `ROI` result, which passes; it is never applied to the violating results one subsection back.

#### Comparing specifications as one object (100 words)
Says: `combine.optimizations()` makes several results one object for the extract and chart functions.
Why here: Not stated.
Paragraphs: method · code · code
Note: A package-API aside: nothing before or after uses the combined object, and the application does not refer to it.

### Why the Searches Fall Short — 787 (341 before the subsections) (? words)
Says: A random search covers a sixteen-dimensional simplex poorly, so more draws close only part of the gap at a growing cost; use a heuristic only when the problem forces it, and report its output as an estimate.
Why here: Contract position; builds on the race's `run()` and band; hands the band to chapter 14, whose risk budgeting is said to force a search.
Paragraphs: claim · claim · code · code · result · claim
Note: An argument with one experiment on the race's machinery, not a result on the modeled market; ¶1 restates the theory section's conclusion; ¶3 already makes Gilli's random-variable point that the next subsection is titled for; the band is read a second time.

#### A heuristic's answer is a random variable (258 words)
Says: A search's output depends on the seed, so it is a distribution to report; three habits: record the seed, report the spread, start from the convex answer.
Why here: Builds on the single draw in tbl-13-race; otherwise not stated, and the parent's ¶3 has already made the point.
Paragraphs: claim · claim · transition · method · caveat · method
Note: ¶2 repeats the parent's ¶3 (Gilli, repeated runs, the spread); no code, so the seed dependence is asserted, not measured, and goes to exercises 3 and 4; ¶3 is a one-sentence transition.

#### Choosing, in three questions (175 words)
Says: Choose by three questions: is the problem convex; is the non-convexity in the objective or in the constraints; what is a heuristic's answer worth.
Why here: Closes the application as a decision rule; reads the band from tbl-13-race a third time and points to chapter 14 for the non-convex objective.
Paragraphs: transition · method · method · result
Note: `Rglpk` and mixed-integer programming enter here as the exact route for cardinality, absent from the feasibility test and without a chapter 12 reference; "nine solvers" counts a set the chapter never lists (six raced, five tested).

### Key Takeaways (212 words)
Says: Convexity separates the families; the searches reach a band of the optimum and more draws close only part of the gap; cardinality is the legitimate reason for a heuristic; three of five violate an accepted limit; audit everything.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets; the band, the budget numbers and the three-of-five count each appear for the fourth time; nothing on the seed habits or the three questions.

### Exercises (144 words)
Says: Five exercises: the race under a box cap, what `optimize.portfolio.parallel()` parallelizes, the violation across seeds, the distribution of a search's Sharpe, and the audit on the reader's own work.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise · exercise
Note: Five exercises; 3 and 4 measure what the random-variable subsection asserts; 2 is a help-page reading with no computation.

## Chapter 14: Risk-Based Allocation (3211 words, 33 paragraphs)
Claim: Allocating risk rather than capital is a convex problem that a six-line fixed point solves to machine precision and a one-line inverse-volatility rule nearly solves, which the package's own risk-budget objective scores correctly and cannot find; what it buys is several times the effective bets for a few percent more volatility, on a covariance matrix that halves those bets in the credit crisis.
Question: Why how much money sits in a position is not how much risk sits there, and what allocating risk instead looks like; @qian2006 and @maillard2010, in the third sentence rather than the first two.
Why here: Stated once, in the first sentence: every portfolio so far was described by its capital, so the chapter follows the capital-allocating optimizers. Needs chapter 9's minimum-variance portfolio and its resampling, chapter 13's convex-versus-heuristic classification and its constraint-ignoring solver, chapter 7's rank bound and regime spectrum; hands hierarchical risk parity to chapter 15 and the estimation problem to chapter 19, and reads chapters 23 and 25 ahead for turnover and the out-of-sample register. Why it closes the part after the solvers is not stated beyond that classification.
Does: Decompose any portfolio's volatility into risk contributions, compute the equal-risk-contribution portfolio by fixed point or by inverse volatility, score a portfolio against the package's objective, use `max_prisk` for a cap, and audit concentration with `HHI()`, `diversification()` and an effective-bets count.
Order: Theory (Euler decomposition, equal risk contribution and its convex program, the inverse-volatility approximation), implementation (the package objective scored, five failed searches, the cap it can enforce, the concentration audit), application (the trade in bets and volatility with the out-of-sample line, the regime dependence of Σ, general budgets, hierarchical risk parity), eight takeaways, four exercises; deviations: the theory section already runs the package (`inverse.volatility.weight()`, an inline minimum-variance optimization) and defines the base spec, the implementation section is the chapter's negative finding rather than its method, and the application closes with two code-free theory subsections, one of which says it belongs in chapter 15.

### Opening (before the first heading) (195 words)
Says: Capital weights and risk weights are different things, and allocating risk has a clean definition, a cheap approximation and a package implementation that does not work.
Why here: the opening by contract; ¶2 lays out the chapter's order (decomposition, exact answer two ways, what the package objective does).
Paragraphs: code · claim · method · code
Note: the seminal citation sits in ¶2, the third sentence; ¶1's promise to measure the minimum-variance portfolio's risk share is met only as an effective-bets count in the audit table.

### Allocating Risk Rather Than Capital (714 words)
Says: Volatility decomposes exactly into risk contributions; equalizing them is a convex problem a fixed point solves in six lines and inverse volatility nearly solves in one.
Why here: stated in the opening's plan: first the decomposition that makes the idea precise, then the exact answer two ways. Paragraphs: none of its own; the section goes straight to its first subsection.

#### The decomposition that makes this precise (180 words)
Says: By Euler's theorem portfolio volatility is exactly the sum of each asset's risk contribution, and on sixteen equal weights one asset carries a multiple of its share.
Why here: stated: the exactness is what makes risk budgeting possible at all; ¶3's gap "is the entire motivation for what follows".
Paragraphs: derivation · claim · code · result

#### Equal risk contribution (335 words)
Says: The equal-risk-contribution portfolio exists, is unique long-only and is convex by @spinu2013; a six-line fixed point reaches it to machine precision and still gives the least volatile series the largest weight.
Why here: needs eq-14-euler to set its terms equal; stated as what the gap of ¶3 motivates; ¶2 and ¶4 point forward to the search.
Paragraphs: definition · claim · method · code · result · code · code · result
Note: ¶2 and ¶4 both send the reader to the application section for the metaheuristic search, which sits in the implementation section; ¶5 runs a full minimum-variance optimization inside an inline expression, and the audit chunk computes the same portfolio again as `w_mv`.

#### The approximation that is nearly free (181 words)
Says: Under equal correlations inverse-volatility weighting is the exact equal-risk solution, and on this universe it lands within a small L1 distance of it for one division per asset.
Why here: stated: a special case worth exploiting; needs the exact answer to measure its distance from.
Paragraphs: definition · code · result
Note: the chunk defines `base`, the spec every later package call reuses, and carries the function's calling convention (wants the spec, returns an `optimize.portfolio` object) in a code comment rather than in prose; the `max_rc_deviation` it prints is not read.

### Implementation (874 words)
Says: The package's risk-budget objective scores the equal-risk problem correctly, none of five metaheuristic searches finds it, a cap on any one contribution it can enforce, and two exported functions audit concentration.
Why here: stated in the opening's plan: after the exact answer, measure what the package's own objective does with it.
Paragraphs: claim · code
Note: the section states its finding before showing it; the heading promises an implementation, the section is the chapter's negative result, the method's own code having already run in the theory section.

#### The objective is right (86 words)
Says: Scored directly, the package's objective is zero at the true equal-risk portfolio and positive at equal weights, so the objective is not what fails.
Why here: stated: before blaming a solver, check what it was asked to minimize; needs `w_eq` and `w_erc` from the theory section to score.
Paragraphs: method · code · result

#### The search does not find it (440 words)
Says: Most of the five solvers hand back the equal-weight start, a tenfold budget changes nothing, and the one-line approximation is closer than a twenty-thousand-evaluation search to a convex problem's answer.
Why here: not stated; follows once misspecification is ruled out; needs `rb_spec`, `w_erc` and `w_iv` from before.
Paragraphs: code · code · code · result · claim · code · claim
Note: opens on code with no lead-in; the hidden comparison chunk defines `p_vol()`, used by the audit, the trade and the takeaways, and asserts in passing that the one-liner beats the search; the heading is a claim sentence.

#### What the machinery does do (106 words)
Says: A ceiling on a single risk contribution is satisfiable by rejection, so the objective works for caps and budgets while equal risk contribution is computed directly.
Why here: stated: "the objective is not useless", the counterpart to the failure just shown; "Budgets that are not equal" refers back to it.
Paragraphs: claim · code · claim
Note: ¶1 says it delivers before the chunk runs, and no paragraph reads the number the chunk prints (largest contribution against the cap); nothing asserts that the cap held.

#### Auditing concentration (184 words)
Says: `HHI()`, `diversification()` and an entropy-based effective-bets count audit four portfolios' concentration in one table.
Why here: not stated; two exported functions introduced because any portfolio in the book, including one from a solver that ignored its constraint (chapter 13), can be audited in one line.
Paragraphs: method · code · code
Note: effective bets is defined in a code comment and the caption, never in the theory section; the table is built here and read only in the next section's first paragraph; `w_mv` recomputes the inline minimum-variance portfolio of the theory section.

### What Risk Parity Buys and Costs (1026 words)
Says: Equal risk contribution buys several times the effective bets for a few percent more volatility and holds its own out of sample at a fraction of the turnover, but the bets are a property of Σ, which halves in the credit crisis; budgets generalize it and hierarchical risk parity is the next question.
Why here: stated by the heading, the buy side then the cost side; its first subsection reads the table the implementation section built. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: four subsections, the last two of which are theory with no code.

#### The trade, in its own units (349 words)
Says: Against minimum variance, equal risk costs a few percent more volatility for many times the effective bets, and out of sample inverse volatility sits between equal weighting and the tangency portfolio at a fraction of its turnover.
Why here: stated: "read the last two rows of the table together", continuing directly from tbl-14-concentration.
Paragraphs: result · claim · evidence · code · result
Note: the out-of-sample line scores inverse volatility, not the equal-risk portfolio the chapter computed, because the register carries only `inverse_vol`; ¶2's "about five percent" is a number typed from chapter 9; ¶3's "conditions this market does not satisfy" is asserted, not shown.

#### The covariance is a regime variable (274 words)
Says: The effective number of bets belongs to Σ, not to the portfolio, and the matrix's independent directions fall by more than half through the credit crisis.
Why here: stated: "one thing risk parity cannot escape", the cost after the buy; sends the estimation problem to chapter 19.
Paragraphs: claim · code · result · caveat
Note: `directions` is the participation ratio of the eigenvalues of Σ, a different measure from the entropy-based effective bets of the audit table, and the prose calls both "bets"; ¶2's "calm windows of the same length still do not reach" is not computed by the chunk; the text says the measurement repeats chapter 7's.

#### Budgets that are not equal (177 words)
Says: Equal risk contribution is the equal case of a risk budget b_i, which is the language mandates speak and the form the package objective can satisfy by rejection.
Why here: stated: equal risk "is the special case of a more general idea"; not stated why it comes after the regime subsection rather than beside the definition in the theory section.
Paragraphs: definition · claim
Note: the general definition arrives after its special case has been used for three sections, in the application section, with no code; ¶2's last two sentences restate the practical rule of "What the machinery does do".

#### Hierarchical risk parity (202 words)
Says: Hierarchical risk parity clusters assets on correlation distance and allocates by recursive bisection without inverting Σ; it belongs with chapter 15 and is the one technique in this area the package lacks.
Why here: stated: the obvious next question once risk contributions are on the table, and the one widely used technique the package does not implement; the text says it belongs in chapter 15.
Paragraphs: definition · claim · transition
Note: no code, and the text itself says the method belongs elsewhere; ¶1's premise that most of the chapter's methods need the inverse sits against a fixed point and a one-liner that invert nothing.

### Key Takeaways (253 words)
Says: Eight bullets: the exact decomposition, equal capital is not equal risk, the equal-risk portfolio's properties, its convexity, the failed searches, the rule for the package objective, the trade and the out-of-sample line, bets as a property of Σ.
Why here: by contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: eight against "around five"; bullet 2 restates the decomposition's ¶3 and bullet 5 the search's ¶1 and ¶3, numbers included; the general budget and hierarchical risk parity have no bullet beyond bullet 6's rule.

### Exercises (124 words)
Says: Four exercises: equal risk fitted on calm months and tested in the credit crisis, a universe where inverse volatility fails, the searches repeated with a cap, and an inverse-Herfindahl bets measure.
Why here: by contract.
Paragraphs: exercise · exercise · exercise · exercise
Note: four against "around three"; each follows one subsection: 1 the regime, 2 the approximation, 3 the searches, 4 the audit table.

# Part V: Allocation Strategies

## Chapter 15: Hierarchical and Sleeve-Based Allocation (6717 words, 49 paragraphs)
Claim: The two-layer organization (classes first, then selection inside a sleeve) is a governance decision whose cost can be measured: in sample the nested portfolio can never beat the flat one, and on sixteen classes it loses out of sample as well, at every window, because the cross-sleeve covariances stage 1 discards are information at this dimension; the case for the hierarchy arrives only where the flat matrix cannot be estimated.
Question: How should an allocation be organized when nobody can hold the whole problem in one head, and what does the organization cost; cites @sharpe1981 for the decentralized investment problem and @brinson1986 for how much the top-level decision explains.
Why here: Stated: this is the chapter in which the book's own structure (Parts III to V across the sixteen classes, Part VI inside a sleeve) is made explicit and priced, as a strategic decision in ch. 3's sense. Takes the flat problem, eq-09-gmv and eq-09-tangency from ch. 9, the shrinkage form and the rank finding from ch. 7, the hedging finding from ch. 4, the out-of-sample claim from ch. 8, the budget constraint from ch. 12, `quadprog` behind `ROI` from ch. 13, the missing HRP from ch. 14, the back-fill from ch. 23, the rolling backtest and the register from ch. 25. Hands the benchmarks to ch. 21 and ch. 22, the hedging instruction to ch. 22, the judging of the manager and the anchored variant to ch. 24. Why it opens Part V rather than closing Part IV is not stated.
Does: Partition the sixteen classes into sleeves, solve the nested problem by hand and with `mult.portfolio.spec()`, reproduce the package's proxy series, race nested against flat on a rolling window and check it against the register, and read a mixed-objective nested policy as a strategic asset allocation with benchmarks for the sleeve managers.
Order: Opening; theory (the two-stage problem, its shrinkage reading with two worked boxes, the benchmark reading, hedging); implementation (the one-asset failure, the package's method, the by-hand reproduction, the `opt.list` machinery); application (in sample, out of sample, the policy view); takeaways; exercises. Deviations: the theory section executes the chapter's solver, reads the in-sample ladder with its numbers inside a collapsed box, carries a 495-word box on a different method and a results table on hedging, and announces the out-of-sample verdict before the race runs; the two main headings have no paragraph of their own; the implementation's last subsection draws two figures no paragraph reads; no picture opens the application; six takeaways and four exercises.

### Opening (before the first heading) (250 words)
Says: Allocation runs in two layers because nobody holds the whole problem; the chapter makes the book's own two layers explicit and prices them.
Why here: Contract position; the text says this is where the book's structure is made explicit, and gives the order: state the problem, read it as shrinkage, implement it, test it out of sample.
Paragraphs: code · claim · method · code
Note: No visible packages block; the setup chunk is hidden and the shown chunk loads data. ¶2 names the out-of-sample test before anything is defined.

### The Two-Stage Problem — 2585 (0 before the subsections) (? words)
Says: (heading only)
Why here: Contract position; the opening's sequence sentence puts the problem and its shrinkage reading first. Paragraphs: none of its own.
Note: Heading only; four subsections of very unequal size (451, 1577, 174, 378), and the second carries the chapter's executed solver, two worked boxes and most of its citations.

#### Sleeves, and what is decided at each level (451 words)
Says: The nested problem solves each sleeve on its own block and then allocates across the sleeve returns; the unrolled result is feasible for the flat problem, so in sample it can never have lower variance, and the gap is the price of decentralization.
Why here: First because the rest of the chapter is the gap between the two problems defined here; needs ch. 9's flat problem; the shrinkage reading takes the blocks and the application the in-sample bound.
Paragraphs: definition · definition · claim · evidence · code · result
Note: ¶4 opens with the chapter's first claim (the in-sample bound) and then spends 130 words on six citations in one block; the sleeves are built in code after the mathematics has used K, and ¶5 is the only prose that reads the chunk.

#### The shrinkage reading — 1577 (728 before the two boxes) (? words)
Says: Stage 1 is the flat problem on the block-diagonal matrix, a shrinkage estimator whose intensity the mandate sets rather than the data; stage 2 restores the cross-sleeve information in K-by-K form; with a diagonal Ω the whole construction collapses to flat minimum variance on Σ_B, so flat, nested and block-diagonal form a ladder, and where nesting sits on it depends on whether the cross-block covariance is signal.
Why here: Stated in the opening: the problem is read as a shrinkage of the covariance matrix before it is implemented; needs eq-07-shrinkage and Ledoit–Wolf from ch. 7; the application reads its ladder and its verdict through this subsection.
Paragraphs: claim · derivation · code · result · method · code · transition · code · result+c · code · result+c · code · result+c · definition · code · result+c · code · result+c
Note: Sixty percent of the theory section, doing four things under one heading: the shrinkage reading, the chapter's solver (¶4 and gmv-qp are implementation), the in-sample ladder read with its numbers in a collapsed box (an application result), and a 495-word box on a different method whose finding, that the data group bonds by currency, is the hedging subsection's point made two subsections early. ¶3 gives the out-of-sample verdict before the race runs; ¶5 is a ten-word lead-in.

#### The class series is the sleeve's benchmark (174 words)
Says: Each class series is an index of the instruments inside it, so the top layer is a policy set on investable proxies and handed down as benchmarks; the sleeve manager is judged against it, and setting the policy on realized sleeve returns would reward past alpha and leave nothing to judge.
Why here: Not stated; the paragraph sends its consequences to ch. 21, ch. 24 and ch. 25 and takes nothing from the subsections before it.
Paragraphs: claim
Note: A one-paragraph subsection without code and with six cross-references; a governance argument between two quantitative subsections, returning as the last takeaway.

#### Hedging is a sleeve decision (378 words)
Says: The optimal hedge differs between bonds and equities, so a hedge is a property of the sleeve: hedging the government sleeve lowers its minimum variance and spreads it over more positions, hedging the equity sleeve changes almost nothing.
Why here: Stated: the sleeve structure settles a question that has no answer at whole-portfolio level; needs ch. 4's hedging finding and the HRP box's currency grouping; ch. 22 takes the bond side.
Paragraphs: claim · code · code · result
Note: A results table inside the theory section; the commodity sleeve is left out of the table without a word; the two classic citations arrive after the result they are said to answer.

### Implementation — 1198 (64 before the subsections) (? words)
Says: The package has a data structure for the nested problem and no documentation of what it does, so the section reads the source and checks it against a by-hand construction.
Why here: Contract position; the opening says the package path and the by-hand path follow the theory.
Paragraphs: method
Note: The by-hand solver and the nested construction already ran in the theory section, so what this section adds is the package path and its reproduction.

#### A sleeve of one asset (112 words)
Says: A one-asset sleeve cannot be optimized under `ROI`, so the commodity sleeve cannot enter `mult.portfolio.spec()` and the package path runs on three sleeves.
Why here: Stated: the sleeves subsection said the single-asset case must be faced rather than assumed; it fixes the three-sleeve universe the rest of the section uses.
Paragraphs: code · caveat+c
Note: A subsection with no running prose: one chunk and one callout.

#### `mult.portfolio.spec()` and `add.sub.portfolio()` (481 words)
Says: `optimize.portfolio()` runs every sleeve through the rolling backtest of `optimize.portfolio.rebalancing()`, takes the realized returns as proxies, and optimizes the top level once on them, back-filled training period included; its defaults do not run and `rolling_window` is silently discarded.
Why here: Stated: the method lives in an unexported loop and nowhere else, so the source is read before the output; the next subsection reproduces what it shows.
Paragraphs: code · method · code · code · caveat+c · code · code · result
Note: ¶1 and ¶2 are one sentence split around the source excerpt; the callout's last sentence cites the by-hand reproduction a subsection later as its evidence, so the claim precedes its proof; ¶1's "three arguments" and the callout's subject are the same point, stated twice.

#### The same thing by hand (196 words)
Says: Sixty months of drifting equal weights followed by rolling minimum variance reproduce the package's proxies to machine precision and the top-level weights to solver tolerance; dropping the back-fill moves the government budget, and the package cannot drop it.
Why here: Stated: the reproduction is the documentation the chapter set out to write, and the evidence the previous callout claimed.
Paragraphs: code · result
Note: The two phases of the by-hand loop are explained only in the code's comments; the one paragraph reads the result and names neither.

#### Holding several optimizations together (345 words)
Says: Stage-1 solutions combine into an `opt.list` whose weight matrix pictures the block-diagonal structure, several top-level policies run in one call on the sleeve series, and the `opt.list` methods need `trace = TRUE`.
Why here: Not stated; the sleeve-cap row it produces is referred to once, in the in-sample paragraph.
Paragraphs: method · code · code · method · code · caveat+c · code
Note: A package-API tour: no paragraph reads either figure or the three policies' weights; only the sleeve-cap row is mentioned later, in one clause; that `risk_aversion` is γ/2 is a code comment, not prose.

### Nested Against Flat — 2171 (0 before the subsections) (? words)
Says: (heading only)
Why here: Contract position; the opening says the question is whether the hierarchy dominates one-stage optimization out of sample on this universe. Paragraphs: none of its own.
Note: Heading only; the in-sample ladder was already read in the theory's worked box, so the first subsection repeats it with two rows added.

#### In sample (246 words)
Says: In sample the ordering is fixed, so the table only measures the gaps; nesting gives up Sharpe ratio and does not diversify, because stage 2 is still a minimum-variance problem.
Why here: Not stated beyond the in-sample bound of the theory; it precedes the out-of-sample test as the thing the test is meant to overturn.
Paragraphs: code · code · result
Note: Repeats the ladder of the theory's worked box with HRP and equal weight added; no picture opens the application.

#### Out of sample (1343 words)
Says: The hierarchy does not dominate out of sample on this universe: nested trails flat at every window and trails equal weighting, the block-diagonal construction trails nested, the gap opens steadily rather than in any episode, and turnover leaves the ranking alone; on sixteen classes the cross-sleeve covariances are information.
Why here: Stated: ch. 8's claim, that a restriction can buy back out of sample what it costs in sample, is the one that matters, and ch. 25's register is what the loop is scored against.
Paragraphs: method · code · code · result · code · code · code · claim · claim · code · code · result
Note: ¶3 restates the verdict the theory's shrinkage reading announced; ¶3 and ¶4 are the chapter's argument in 314 words, and the figure that supports them follows with its reading a chunk later; the sleeve-budget mechanism in ¶5 is the chapter's only explanation of why nested loses and gets two sentences.

#### The policy view (577 words)
Says: A mandate can carry a different objective at each level; a tangency equity sleeve, minimum-variance bond sleeves and a tangency top level read as a strategic asset allocation document whose class weights are the benchmarks the sleeve managers receive.
Why here: Stated: a policy is not usually minimum variance everywhere, and the sleeves subsection promised the application would mix objectives; ch. 21 and ch. 22 receive the benchmarks, ch. 24 the anchored variant.
Paragraphs: method · code · code · code · code · result
Note: Four chunks between the two paragraphs, and ¶2 reads two of policy-summary's four numbers; the policy is in-sample only, directly after a subsection showing that in-sample numbers are not forecasts, and it never enters the out-of-sample race.

### Key Takeaways (281 words)
Says: The nested problem is every allocator's structure and never dominates flat in sample; stage 1 is mandate-set shrinkage and coincides with flat on Σ_B under inverse-variance budgets; the package's method and its four traps; the hierarchy loses out of sample at this dimension; HRP groups bonds by currency, which is the hedging decision; the class series is the benchmark.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets; ¶3 packs four package traps into one; nothing on the policy view (mixed objectives, the tangency QP) or on turnover.

### Exercises (187 words)
Says: Four exercises: currency sleeves in the race, the inverse-variance top level against the block-diagonal line, HRP with complete linkage cut at four, and the back-fill's weight across training windows.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises, all reruns of the chapter's own functions (`race()`, `unroll()`, `hrp()`, `proxy_by_hand()`); none touches the policy view or the hedging table.

## Chapter 16: Signals and Return Forecasts (7301 words, 50 paragraphs)
Claim: Of four signals on sixteen series only the theory-motivated term spread forecasts out of sample, and a restrained tilt on it pays a few tens of basis points of certainty equivalent after costs, inside the Sharpe ratio's sampling error; the signals that data alone motivate, and a regularized seven-signal model, lose to the historical mean and pay more to trade.
Question: Can the excess return on an asset class be forecast, and does a forecast that fits the past help an investor who must act before the future arrives; cites @welch2008 (hardly any predictor helped in real time) and @campbell2008 (a small but meaningful gain under a sign restriction), who between them fixed the two criteria: the out-of-sample R² against the mean and the investor's certainty-equivalent gain.
Why here: The text says it is the book's first tactical chapter in ch. 3's sense, inputs conditioned on information available at the time; it takes the sixteen series from ch. 2, the excess basis, quadratic utility and the certainty equivalent from ch. 3, the Merton bound from ch. 4, Newey–West and the turbulence index from ch. 5, the mean as the strategic input from ch. 6, the equal-weight policy and the estimation-cost lesson from ch. 8, the constrained minimum-variance portfolio from ch. 9, turnover, costs and the back-fill trap from ch. 23 and the register's scoring months and paired test from ch. 25; it hands the view from opinion to ch. 17, the hand-chosen tilt rule to ch. 18 and ch. 19, the value side to ch. 21, the curve state to ch. 22 and the forecast-error question to ch. 26 and ch. 27. Why it follows ch. 15 inside the part is not stated.
Does: Build four signals from the shipped data and lag them with assertions; run single-signal predictive regressions with Newey–West inference; score forecasts on an expanding window by R²OS, Clark–West and Diebold–Mariano; fit a time-ordered, cross-validated elastic net without leakage; turn forecasts into a banded tilt around equal weight and price it with turnover, costs and the certainty equivalent.
Order: Opening (question, tactical label and roadmap, data), theory (the regression and its R², R²OS, DM and CW, why a small R² matters with the CE criterion, the signal families), implementation (signals built and lagged, sixty-four in-sample regressions, out of sample with the elastic net), application (the tilt rule with the utilities callout, accounting and costs, the reading), takeaways, exercises. Deviations: the chapter's main result, the out-of-sample table and its three findings, sits in the implementation section, so the application prices a tilt on a verdict already read; the application opens with a method paragraph and a chunk, not a picture; the one worked formula with numbers substituted is in the theory on hypothetical values; the chapter scores on the register's months but reads no register line; six takeaways and four exercises.

### Opening (before the first heading) (380 words)
Says: Predictability is judged by Welch–Goyal's and Campbell–Thompson's two criteria, and this chapter applies them to four signals on the sixteen class series as the book's first tactical exercise.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections and no reason for the chapter's place in the part.
Paragraphs: code · claim · method · method · code
Note: ¶1 carries both seminal citations inside its first three sentences; ¶2's roadmap is one sentence of four clauses; ¶3's reason for asserting (a plausible table from a misdated signal) returns in the theory and again in the implementation.

### Predictability, In Sample and Out (1703 words)
Says: A predictive regression is scored out of sample against the historical mean by R²OS and the Clark–West statistic, a small R² is worth a lot to a mean-variance investor and the certainty equivalent decides it, and this universe carries momentum, the curve spreads and turbulence but not value.
Why here: The roadmap's first step; the text says the dating and the statistics are settled before any signal is chosen, and that the implementation asserts the alignment the theory demands. Paragraphs: none before the first subsection.
Note: Five subsections, the first three a single paragraph each wrapped around display equations; the chapter's only worked formula with numbers substituted is here, on hypothetical values rather than on the data.

#### The predictive regression (260 words)
Says: The regression and its in-sample R² are defined, and three things are settled before any signal: the dating, the smallness of any R², and the Stambaugh bias; inference is Newey–West and sixty-four regressions are a multiple-testing problem.
Why here: Stated: the three things are settled before any signal is chosen; the implementation asserts the dating this paragraph demands.
Paragraphs: definition
Note: One paragraph does six jobs (two definitions, three caveats, inference with multiple testing); its yardstick, one percent a month as a strong result, is what the in-sample table is later read against.

#### The out-of-sample R² (230 words)
Says: The investor re-estimates each month and competes with the expanding historical mean; R²OS has no floor and is usually negative; the window expands; the sign restriction goes to exercise 2.
Why here: Stated: an in-sample fit scores on the history it was fit on, which an investor cannot do; the expanding window is the scheme the implementation runs.
Paragraphs: definition
Note: The burn-in is called a choice and left to the implementation; the restriction Campbell–Thompson found decisive is deferred to an exercise.

#### Testing one forecast against another (198 words)
Says: The Diebold–Mariano test on the loss differential is biased against a nested model, and the Clark–West correction is the statistic reported, with DM beside it.
Why here: Stated: a regression and the mean are nested, so the correction is needed before any signal is set against the mean below.
Paragraphs: definition
Note: Two statistics, two equations, one paragraph; the promise to show DM beside CW is kept only in the summary table's last column.

#### Why a small R² can matter (477 words)
Says: The gain to a mean-variance investor is R²OS/γ, about a quarter of the expected excess return at half a percent a month against an annual Sharpe ratio of one half, and the certainty equivalent, not the fit, decides the application.
Why here: Stated: in-sample significance and out-of-sample profit are different questions, and the second needs a criterion before the application; it draws ch. 3's utility and certainty equivalent.
Paragraphs: derivation · example · definition
Note: ¶2 is the chapter's one worked formula with numbers substituted, on hypothetical values rather than the data; ¶3 ends on a two-sentence pointer to Part VIII inside a definition paragraph.

#### Which signals this universe can carry (538 words)
Says: Momentum from returns, the term and IG spreads read off the simulated curve, and ch. 5's turbulence index are the signals; value needs fundamentals the market does not carry.
Why here: Stated: the families are set out before the implementation builds them; the text says the bond block was simulated from the curve factors, which the in-sample reading later relies on.
Paragraphs: claim · definition · evidence · definition · definition · method · code · caveat
Note: ¶1's count does not close: four families are named (momentum, value, macro state, dispersion), three are built and one is unsupported, yet dispersion is called "the third"; ¶3 joins momentum's class-level evidence to value's exclusion; ¶4's disclosure that the bond returns were generated from the curve state is what the in-sample reading rests on.

### Building and Testing the Signals (2665 words)
Says: The four signals are built from the shipped data, lagged with assertions, found significant in sample for the term spread and the IG spread, and out of sample only the term spread beats the expanding mean; the combination sits between its parts and the elastic net loses.
Why here: The roadmap's second and third steps; needs the families and the three statistics of the theory section; the application takes its forecasts `fc` from here. Paragraphs: none before the first subsection.
Note: The section carries the chapter's main result, the out-of-sample table and its three findings, in a subsection of 1,416 words that also holds the scheme and the elastic net; the application prices a tilt on a verdict already read here.

#### Signals at month end, lagged once (667 words)
Says: Momentum, the curve signals and turbulence are built at each month end, each with an assertion, and shifted forward one month so that the signal at t sits on the row of the return at t+1.
Why here: Stated: the dating is the whole discipline and the alignment is asserted in code rather than trusted; the regressions run on the frame `pairs_of()` builds here.
Paragraphs: method · code · method · code · result · code · method · code · result · code
Note: ¶3 reads a number and sets up the next chunk in one block; `pairs_of()`, the frame every later chunk uses, is introduced by a code comment rather than by the prose; the subsection ends on a figure no paragraph reads.

#### In sample: sixty-four regressions (582 words)
Says: Over the full sample the term spread is the strongest signal, positive on every bond and credit series, the IG spread second, turbulence weak and momentum nowhere; the largest R² is not small by eq-16-ct.
Why here: Stated in the theory: in sample first, then whether any of it is available in real time; the paragraph ends on that question.
Paragraphs: method · code · code · code · result
Note: ¶2 is one block of about 230 words reading four columns, reconciling momentum with the literature and posing the transition; the summary numbers print raw from `insample` before the formatted table shows them; the hidden chunk asserts the order the prose states.

#### Out of sample: an expanding window from model year 11 (1416 words)
Says: On an expanding window from the first month of model year 11 the term spread keeps a positive R²OS on most series and beats the mean by Clark–West, the IG spread and turbulence lose what an expanding window cannot see, the combination averages, and the elastic net loses more the less it shrinks.
Why here: Stated: the theory says only an out-of-sample score counts, and ch. 25's register scores the same months; the application tilts on the forecasts `fc` produced here.
Paragraphs: method · code · method · method · code · method · code · transition · code · code · code · code · transition · result · result · result
Note: A fifth of the chapter in one subsection: the scheme, the one method the chapter describes at length (¶3, about 200 words on a model it says it does not reproduce), the loop and the chapter's main result; ¶5 and ¶6 are one-sentence transitions; the table and figure sit between the functions and the reading with no prose between them; ¶7's explanation for turbulence (a few crisis months) is asserted, not shown.

### The Economic Value of a Tilt (1874 words)
Says: A banded tilt around equal weight pays after costs on the term spread, by a few tens of basis points of certainty equivalent and inside the Sharpe ratio's sampling error; the combination is a wash, and momentum and the elastic net trade more and lose.
Why here: The roadmap's last step; the text says the certainty equivalent of the theory decides it, and it needs `fc` and the register's months from the implementation and the cost machinery of ch. 23. Paragraphs: none before the first subsection.
Note: Opens with a method paragraph and a chunk, not a picture; the relative-return figure is drawn but never read; the chapter scores on the register's months but reads no register line.

#### A tilt around the policy (701 words)
Says: Equal weight is the anchor because it estimates nothing; a forecast becomes a weight by volatility scaling, demeaning, scaling by κ and clipping to a band of half the policy weight; the term-spread tilt is modest, and the two utilities whose names suggest rolling do not roll.
Why here: Stated: the anchor must estimate nothing so that every difference is the forecast's, and the dating of eq-16-predictive carries over; the callout sits by the `vol60` line where a reader would reach for the utilities.
Paragraphs: method · code · definition · code · result · caveat+c · code
Note: The subsection ends on the callout's chunk, whose output no paragraph reads; ¶1 gives two reasons for the anchor; the band and κ are set by hand in ¶2, which the closing paragraph later concedes when it points to ch. 18.

#### Rebalancing, turnover and costs (695 words)
Says: The monthly accounting is written out, with drifted weights, ch. 23's turnover and cost at the per-class rates, the register's Sharpe ratio and the certainty equivalent at γ = 5, for the policy and five tilts.
Why here: Stated: `Return.portfolio()` back-fills equal weights (ch. 23's trap) and the drifted weights are needed for the cost; the table it produces is read in the next subsection.
Paragraphs: method · code · code · code · code
Note: One paragraph and four chunks; the CE of eq-16-cer is annualized in code without the prose saying so; the figure precedes the table and is never read; the Sharpe ratio's standard error is computed in a hidden chunk and read only in the next subsection.

#### Reading the result (478 words)
Says: The term spread alone pays after costs, by a few tens of basis points inside the sampling error of the Sharpe ratio; momentum and the elastic net trade more and lose; the honest reading is Campbell–Thompson's, and three chapters take the rest.
Why here: Stated: the gain is measured against its own uncertainty before it is called evidence; closes the application with the forward pointers.
Paragraphs: result · claim · transition
Note: ¶2 is the chapter's claim in its final form and the first place the Sharpe advantage meets a standard error; ¶1 reads the table only and never the relative-return figure; the turnover multiple and the cost drag are the chapter's only cost numbers in prose.

### Key Takeaways (286 words)
Says: Six bullets: the scoring statistics, the small-R² arithmetic, the signals the universe carries, the term spread as the only survivor and the net's loss, the tilt's net gain inside sampling error, and the two utilities that do not roll.
Why here: Chapter contract; not stated.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six against around five; ¶4 says the IG spread and turbulence lose to the mean, where the result paragraph keeps them positive on some series; ¶6 is the only bullet about the package.

### Exercises (237 words)
Says: Four exercises: local curves for local series, the Campbell–Thompson sign restriction, the tilt scale κ, and an absolute timing rule for one equity series against eq-16-ct.
Why here: Chapter contract; not stated.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against around three; exercise 2 is announced in the theory; exercise 4 is the only place eq-16-ct is tested on the data rather than on hypothetical numbers.

## Chapter 17: Expressing Views (7975 words, 65 paragraphs)
Claim: A view should enter the optimizer blended with the equilibrium prior at a stated confidence, which makes the portfolio the market plus a position in each view portfolio; entropy pooling buys the same on a skewed history at a price in effective months, a ranking supplies a direction whose size the allocator must still choose, and any view written into μ without the covariance becomes a hedged spread trade.
Question: How does an allocator's opinion become a portfolio weight; cites Black and Litterman (1992) in the second sentence, with Michaud (1989) for why it must not become one directly.
Why here: Names itself tactical in chapter 3's sense, a deviation from the strategic policy chapter 6 anchored on the equilibrium; takes the data from chapter 2 and the excess basis from chapter 3, μ and Σ and the GMV and effective-bets ideas from chapter 9, the equilibrium prior (rebuilt verbatim), `tangency_lo()`, `make_moments()`, the `match.call()` trap and the Σ_μ warning from chapter 6, skewness from chapter 4, the long-only QP from chapter 12, standard errors from chapters 6 and 8; hands forward to chapters 16 and 25 (data-generated views and their backtest), 18 (skipping μ), 19 (a regime as a scenario view through eq-17-entropy) and 28 (confidence as the size of an uncertainty set). Why it follows chapter 16 inside the part: not stated; the closing paragraph relates the two (a signal has a history of views, an opinion does not) without saying why the opinion comes second.
Does: Write the Black–Litterman posterior with an explicit confidence and check it against `black.litterman()`; route views through `set.portfolio.moments()` with the covariance restored; express mean, volatility and ranking views as entropy constraints and price them in effective months; turn a ranking into a centroid, name and scale it, and tell a coherent view from a hedged spread.
Order: Theory (Black–Litterman posterior, entropy pooling, centroid), implementation (prior rebuilt, Black–Litterman with two views, the package route, entropy pooling, ordinal views), application (one opinion three ways), takeaways, exercises. Deviations: the implementation holds 4,551 of 7,975 words, three of the four figures and three of the four labeled tables, and reads results in every subsection, so the application is a fourth worked case rather than the results section; a theory property (a centroid alone is a corner solution at any scale) is argued in the implementation; the chapter's coherence condition (the shift in μ must be Σ times a portfolio) is stated only in the application; four exercises.

### Opening (before the first heading) (257 words)
Says: An opinion must be blended with a prior rather than written into μ, Black–Litterman is the standard way, and two formulations that ask less are set beside it.
Why here: Contract position; ¶2's sequence sentence says mathematics first, then each formulation on the sixteen series, then one opinion three ways.
Paragraphs: code · claim · method · method · code
Note: The packages block is hidden (`include: false`), so no package list is shown; the `data` chunk also builds `mu_s` and `S`, which the entropy and ranking subsections run on unannounced.

### A View as a Bayesian Update (1268 words)
Says: Three formulations of a view: a normal update of the equilibrium mean whose confidence sets the position, a minimum-divergence reweighting of historical scenarios priced in effective months, and a ranking whose centroid is a direction without level or scale.
Why here: The opening's sequence sentence ("first state the three formulations as mathematics"); the subsections run from the standard answer to the two that ask less, the order the opening frames. Paragraphs: none of its own.
Note: Heading only, and it names Black–Litterman's construction; entropy pooling (a minimum-divergence problem) and the centroid (a conditional expectation over a cone) sit under it as the second and third subsections.

#### The Black-Litterman posterior (628 words)
Says: With a normal prior on the equilibrium mean and Meucci's Ω, τ cancels, each view lands at a confidence-weighted average of prior and view, and the posterior portfolio is the market plus one position per view portfolio.
Why here: "The standard answer" of the opening; needs chapter 9's μ and Σ, eq-06-equilibrium and Sharpe's reverse optimization; the entropy subsection opens by removing its two restrictions, the implementation traces the confidence it ends on, and the application shows what happens without eq-17-weights.
Paragraphs: definition · definition · derivation · claim · definition · derivation · claim · derivation · claim
Note: ¶4 does three jobs (the derivation's literature, the ΣP' property, the Σ_μ warning carried from chapter 6); ¶9's closing clause, that eq-17-weights holds only until a weight reaches zero, is what the implementation's ¶8 and the application's ¶4 both rest on.

#### Views on scenarios: entropy pooling (400 words)
Says: A view is a constraint on the probabilities of the sample months, the posterior is the least-divergent probability vector that satisfies it, and the effective number of scenarios prices what the view cost.
Why here: "Black-Litterman is a view on the mean under normality, and Meucci removes both restrictions": placed as the generalization, and it needs Black–Litterman stated to say it reproduces it on normal scenarios; hands eq-17-entropy to chapter 19 and eq-17-cost to the implementation's cost table.
Paragraphs: definition · evidence · claim · definition · derivation · claim
Note: ¶5 derives eq-17-cost in one clause ("to second order") with no pointer to appendix B; ¶2 is a four-citation genealogy standing between the problem and its solution.

#### Views as an ordering: the centroid (232 words)
Says: A ranking defines a cone of mean vectors whose centroid, the expected order statistics of N normals, is the direction to optimize over; it carries no level, no scale and no position size.
Why here: "Both formulations ask for a number": last because it asks for the least, and it needs the two before it as the contrast; its closing sentence (size is unsaid) is what the implementation's centroid portfolios and the application's ¶4 take up.
Paragraphs: definition · claim
Note: The author's own case for rankings (Salcher et al.) opens the subsection before Almgren–Chriss, the method being attributed; two paragraphs carry the only formulation the application later finds wanting.

### Three Ways to Make a Weight — 4551 (447 before the subsections) (? words)
Says: The chapter 6 prior is rebuilt and the two helpers reused, then each formulation is run on the sixteen series with its package route checked against a hand computation.
Why here: The opening's sequence sentence ("then implement each on the sixteen risky class series"); the prior comes first "so that the two chapters cannot disagree", and every subsection runs on the objects it builds.
Paragraphs: method · code · method · code
Note: The heading says three ways and four subsections follow, the second a package route rather than a way; the collapsed box carries the 40/40/15/5 assumption and builds every prior object the chapter runs on (`mu_eq`, `delta16`, `w_mkt`, `mu_eq5`, `S5`); the `helpers` chunk also builds `spec` and asserts the prior buys the market, which ¶2 does not say.

#### Black-Litterman with two views (1361 words)
Says: A hand-written eq-17-posterior reproduces `black.litterman()` at c = ½, moves every covarying mean, buys the market plus the two view positions until long-only binds, and slides from market to views as the confidence rises.
Why here: First, as in the theory; needs the prior box and the helpers; the confidence trace answers the theory's ¶7 ("the implementation traces it"); the package route next needs `bl` and `w_post` from here.
Paragraphs: method · code · code · result · code · code · caveat+c · code · caveat+c · method · code · code · result · code · result · method · code · code · result
Note: ¶2 ("has none") and ¶3 ("at c = ½") state the same fact about the package twice; the callout, whose silent-recycling trap is the gravest in the chapter, is a note where the two later traps are warnings, and it stands between the assertion paragraph and the reading of the means.

#### Through `set.portfolio.moments()` (270 words)
Says: The package route works with views but hands the optimizer Σ_μ as the risk, and `momentargs = list(sigma = S)` is the fix.
Why here: "The route that needs no custom function": the package alternative after the hand function, checked against its `w_post`; carries chapter 6's `match.call()` lesson forward and adds "one more trap".
Paragraphs: method · code · caveat+c
Note: The subsection's only result (the commodity weight and the gap in points) is read inside the warning callout; no paragraph outside it reads the chunk.

#### Entropy pooling on the 372 months (1371 words)
Says: A mean view tilts every month a little, a volatility view discards the shock months and re-rates every left-tailed series, and eq-17-cost prices a view by its distance in standard errors.
Why here: Second, as in the theory; needs T and the sample moments from the `data` chunk and `tangency_lo()`; the cost table answers eq-17-cost; the ranking subsection next reuses `p0`, `Aeq0`, `eff_n()` and the `EntropyProg()` call.
Paragraphs: method · code · caveat+c · result · code · code · result · code · result · code · result · transition · code · code · result
Note: ¶5 does three things (reads the sixteen moved moments, notes the (T−1)/T scaling, introduces the package route); ¶4 and ¶5 each end in the one-sentence method for the next chunk; the title types the month count that the prose carries as inline R.

#### Ordinal views on the five equity classes (1102 words)
Says: As an entropy constraint a ranking holds only as ties, the centroid commits to a spacing but is a corner solution on its own, and added to the prior at a chosen scale it becomes a tilt whose size came from that choice.
Why here: "The last formulation asks for no number": last, as in the theory; needs `eq_classes`, `mu_eq5` and `S5` from the prior box and the entropy machinery of the subsection before; its scaled tilt is the device the application's centroid column reuses.
Paragraphs: method · code · method · code · result · code · caveat+c · method · code · caveat · claim · code · code · result
Note: ¶7 is a theory property argued in the implementation, after the warning callout; the scale rule for "prior + centroid" (the prior's own dispersion, `kappa5`) is set in a code comment and the table caption and never introduced in prose before the chunk.

### One Opinion, Three Formulations (1452 words)
Says: Given the same opinion at the same strength, Black–Litterman and entropy pooling buy nearly the same portfolio, while the centroid written into μ without the covariance becomes a hedged credit–government spread, so coherence with Σ matters more than the formulation.
Why here: The opening's last clause ("finally express one opinion three ways and compare what each formulation committed to"); needs `bl_post()`, the entropy objects, `centroid.buckets()` and `tangency_lo()` from all three implementation subsections; delivers the two measurements the theory promised (what happens without eq-17-weights, by how much entropy pooling and Black–Litterman part).
Paragraphs: method · code · result · code · code · code · result · result · claim · caveat
Note: No subsections; ¶4 carries the chapter's thesis (the coherence condition) together with its result, its cause, its remedy (exercise 3) and a literature verdict; two columns of tbl-17-three ("held", "Sharpe on prior") are never read in prose; ¶6 is the closing caveat and the forward pointers to four chapters in one block.

### Key Takeaways (215 words)
Says: Five bullets.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: Five, as the contract asks; ¶3's second sentence is the application's finding and the only takeaway that is a result rather than a theory statement; ¶2 and ¶5 each carry a package trap.

### Exercises (187 words)
Says: Four exercises.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; exercise 3 is the remedy the application's ¶4 promised, so the chapter's one constructive fix for the centroid is left to the reader.

## Chapter 18: Parametric Portfolio Policies (6589 words, 44 paragraphs)
Claim: Writing each weight as the benchmark weight plus a linear tilt in standardized characteristics, and estimating the few coefficients on realized utility, replaces the moments whose estimation error chapter 8 priced; on the modeled market both policies finish ahead of their benchmarks out of sample, by margins the sample cannot certify, and what pays is the one characteristic whose coefficient stayed stable.
Question: Can an investor skip the forecast and write each asset's weight directly as a function of what is observable about it; cites Brandt, Santa-Clara and Valkanov in the second sentence as the proposers.
Why here: Needs chapter 8's priced estimation error as the motivation, chapter 3's power utility and the strategic/tactical vocabulary, chapter 2's two panels and simple return, chapter 5's capitalization benchmark and region-neutral sort, and chapter 16's signals, equal-weight benchmark and hand-set tilt, which the text names as the contrast (same information, a different loss function). It also leans forward on chapters 23 and 25 as if already read, in the past tense: the net return and turnover definitions, the no-trade region, the register's accounting, burn-in and Sharpe standard error. Hands the long-only equity policy and the value characteristic to chapter 21 and the many-parameter generalization to chapter 27. Why it follows 17 and precedes 19 inside the part is not stated.
Does: Build an aligned, name-indexed characteristics panel with assertions; implement the policy, its estimator, path accounting and inference in four functions; estimate a cross-sectional and a timing policy, free and under a long-only restriction, gross and net of costs; re-estimate on an expanding window and test the result with the register's accounting and a paired Sharpe test.
Order: Theory (policy and estimator, standard errors, long-only and costs, timing), implementation (equity panel, the four functions, inference, the class policy), application (coefficients through time, performance), takeaways, exercises. Deviations: none of the three main headings has a paragraph of its own; the implementation already reads the full-sample results (coefficients, standard errors, the momentum-as-hedge finding, the worked example, the class vertex), so the application holds the out-of-sample test only; the implementation ends on a chunk; the only figure shows coefficients, not performance; six takeaways, four exercises.

### Opening (before the first heading) (372 words)
Says: Weights can be written directly on characteristics and estimated on utility, K parameters instead of N + N(N+1)/2 moments; the chapter sets that out, implements it and tests it twice.
Why here: Contract position; the text says theory first, then forty lines of R and two estimates, then the expanding-window test.
Paragraphs: code · claim · method · method · code
Note: The packages block is the hidden `setup` chunk and the visible chunk loads data instead; γ = 5 is set in code and never argued for in the prose.

### Weights as a Function of Characteristics (1248 words)
Says: (heading only)
Why here: Stated in the opening: the policy, its estimator and standard errors come first, with the long-only, cost and timing variants. Paragraphs: none of its own.
Note: Heading only; four subsections without an introducing paragraph.

#### The policy and its estimator (476 words)
Says: The policy is the benchmark weight plus a tilt linear in standardized characteristics, its coefficients maximize realized power utility without a mean or a covariance, and because the portfolio return is linear in θ the policy is a position in K + 1 portfolios.
Why here: Needs chapter 2's simple return and chapter 3's power utility; eq-18-linear is what the standard errors, the bootstrap and the timing version build on.
Paragraphs: definition · claim · definition · claim · derivation
Note: ¶4 is the opening's arithmetic a second time with the numbers in, and the takeaways give it a third; ¶3 and ¶5 each close with a lineage sentence of three citations.

#### Standard errors (171 words)
Says: The estimate solves K moment conditions, so it carries a GMM sandwich covariance; the t-statistic tests whether a characteristic belongs in the portfolio, not whether it forecasts returns.
Why here: Follows from the concavity and linearity just established; the implementation computes exactly eq-18-avar and the bootstrap named here.
Paragraphs: derivation · claim
Note: ¶2 carries two points (the robustness options and the reading of the test); the second is the result the implementation later calls instructive, stated here before any number.

#### Long-only weights, and costs (295 words)
Says: Truncation at zero buys a long-only mandate at the cost of linearity and differentiability, which the parameter restriction used at class level avoids; trading costs go into the objective and shrink the fastest-moving characteristics most.
Why here: Not stated beyond the observation that eq-18-policy shorts freely; the class policy and the net-return estimates of the application use both devices.
Paragraphs: definition · definition
Note: Two topics under one heading, as the title admits; ¶2 builds on eq-23-net and says chapter 23 "showed" the no-trade region, two parts ahead; the no-trade parameter of Brandt et al. is described and never used.

#### Timing across a few asset classes (306 words)
Says: With sixteen assets the information is in the time series, so the policy takes state variables with a fixed loading pattern per signal, eq-18-timing; what separates it from chapter 16 is that the map from signal to weight is estimated on the investor's objective.
Why here: Stated: the cross-section of sixteen is too thin, so the second policy needs the time-series version; chapter 16's signals and benchmark are reused and chapter 27 generalizes the estimator.
Paragraphs: definition · claim · caveat
Note: ¶3 belongs to the equity policy, not to the timing policy it sits under; it is the data caveat for the implementation, placed at the end of the theory.

### Estimation of Two Policies (2591 words)
Says: (heading only)
Why here: Stated in the opening: the policy in about forty lines of R, estimated on the equities and on the classes. Paragraphs: none of its own.
Note: Heading only; its four subsections also read the full-sample results, so the section is implementation and in-sample results together, and it ends on a chunk.

#### The equity panel (536 words)
Says: The benchmark is chapter 5's capitalization weight, size and momentum are standardized within region so the policy selects stocks and leaves the regional allocation to the benchmark, and the panel is one named array checked against the raw tables.
Why here: Stated: chapter 5 showed that a global size sort is a region sort; the array and its alignment are what the policy functions consume.
Paragraphs: method · code · method · code · result
Note: Two long assertion chunks for three short paragraphs; the one-month check is explained in a code comment, not in the text.

#### The policy in forty lines (388 words)
Says: Four functions (weights, utility, path accounting, estimator) implement eq-18-policy, eq-18-cost and eq-18-estimator, and two optimizers from distant starts agree, as a concave objective requires.
Why here: Stated in the opening ("about forty lines"); needs the panel; everything after calls these functions.
Paragraphs: code · code · code · result
Note: Opens with the chunk and the prose follows it; the accounting convention (trade measured from the drifted position, charged to the month, flat start) lives in a code comment and a forward reference to chapter 25, not in the text.

#### Standard errors two ways (925 words)
Says: Sandwich and block-bootstrap standard errors agree; size enters negative and significant, momentum enters positive although its own portfolio earns nothing, because the first-order condition weighs returns by marginal utility; in sample the policy lifts the certainty equivalent, with leverage.
Why here: Stated: eq-18-avar needs scores and a Hessian, which `numDeriv` supplies, and eq-18-linear makes each bootstrap draw a two-parameter problem; the application's stability question starts from these coefficients.
Paragraphs: method · code · code · code · result · code · example+c · code · result+c
Note: ¶2 is one paragraph with six points (agreement, size, momentum as hedge, why this market has no momentum premium, the in-sample certainty equivalent, leverage); the market-property caveat is the only place the chapter says the momentum result would differ on real data; the worked example is collapsed and its sentence is split by its display equation.

#### The timing policy across sixteen classes (742 words)
Says: On the equal-weight benchmark with signals standardized on their own history, the free estimate drives one class far below zero and the simplex-restricted one sits at a vertex set by the most extreme months; the policy itself lies outside `PortfolioAnalytics`, which lends only `Return.portfolio()` and `turnover()`.
Why here: Stated: the benchmark is chapter 16's because it estimates nothing, and the first 120 months are the register's burn-in, so the application can start where the register starts.
Paragraphs: method · code · method · code · result · caveat+c · code
Note: The section, and with it the implementation, ends on a chunk whose output no prose reads; the callout's three package facts are then demonstrated in code the text never comments on; the equity policy is never estimated under either long-only device, so the two devices are compared only across the two policies.

### The Policies Out of Sample (1824 words)
Says: (heading only)
Why here: Stated in the opening: both policies are re-estimated on an expanding window and held out of sample against their benchmarks, gross and net. Paragraphs: none of its own.
Note: Heading only; the chapter's one figure shows the coefficients, not performance, and no cumulative-return or drawdown picture is drawn.

#### The coefficients through time (565 words)
Says: Re-estimated at every model-year end on an expanding window, the size coefficient keeps its sign throughout, the momentum coefficient does not, costs in the objective shrink the faster-moving characteristic more, and the class coefficients are stable partly because the simplex caps them.
Why here: Stated: both policies are now run as an investor would have run them, from the register's out-of-sample start; the performance paragraph reads the stability back ("the one characteristic whose coefficient was stable").
Paragraphs: method · code · code · code · result
Note: ¶2 reads the figure and the hidden facts at once; the warm start for the free path against the cold start for the restricted one is a code detail the prose never mentions.

#### Performance against the benchmarks (1259 words)
Says: Both policies beat their benchmarks net of costs, neither by a margin the paired test certifies; the equity gain is the size tilt and comes with shorting and a deeper drawdown; costs in the objective cut turnover at an unchanged net Sharpe; the class policy beats chapter 16's tilt but not the register's minimum variance.
Why here: Stated: the coefficients' stability says which characteristic pays; the equal-weight row must reproduce the register's so the comparison shares its accounting; the closing hands the equity policy to chapter 21 and the many-signal version to chapter 27.
Paragraphs: code · code · code · result · result · result · claim
Note: The longest section opens with three chunks and a table before any prose and then reads them in four paragraphs; the register comparison is made for the classes only, the equity sleeve having no register row; the standard error of a single Sharpe ratio and the paired test are both taken from chapter 25, which comes later.

### Key Takeaways (252 words)
Says: The policy and its parameter count, the GMM standard errors and the membership-not-forecasting test, the two long-only devices, the out-of-sample numbers and their insignificance, the stability and cost results, and the package's lack of a policy.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets; the moment count appears for the third time; nothing on the timing version as a managed-portfolio problem or on the class policy against the register.

### Exercises (160 words)
Says: Four exercises: global instead of within-region standardization, the risk-aversion scaling, costs of 10 and 50 basis points, and truncation in place of the simplex restriction.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises, three on the equity policy; 4 is the one test of the theory's derivative-free claim, which the chapter asserts and never runs.

## Chapter 19: Regime-Dependent Allocation (7597 words, 47 paragraphs)
Claim: Switching to a stress portfolio beats the static policy only when the regimes are dated with hindsight; detected in real time by a turbulence threshold or a filtered two-state model the switch keeps little or none of that advantage, neither detector is distinguishable from the static policy by a paired test, and holding the stress portfolio throughout has a higher Sharpe ratio than either, so on this market whether to hold minimum variance matters more than when.
Question: What if the right portfolio depends on the state of the world; @hamilton1989 for the statistical form and @ang2002a for carrying it into portfolio choice, both inside the first two sentences.
Why here: Stated in the opening: the descriptive chapters supplied the reason to ask, chapter 4's episodes of rising correlations and chapter 14's falling effective bets, and the chapter is tactical in chapter 3's sense. Needs chapter 5's turbulence index, chapter 9's tangency portfolio, chapter 8's quadratic program, chapter 16's lag-and-assert discipline, chapter 23's turnover and cost accounting and chapter 25's register; hands the wrong-model question to chapter 28 and the design-leak problem to chapter 25. Why it follows the parametric policies of chapter 18, or sits where it does in this part, is not stated.
Does: Write a Hamilton filter, a Kim smoother and EM for a two-state model, build a turbulence flag and real-time regime probabilities with no look-ahead, run `regime.portfolios()` knowing its seven behaviors, and test a switching strategy against the static policy and against its own constant mix with a paired Sharpe test.
Order: Theory (model, filter and smoother, mixture moments, two rules, dating against detecting, turbulence), implementation (regimes dated with hindsight, the turbulence threshold, the hidden Markov model with its real-time refit and detection table, the package's regime machinery and its quirks), application (six strategies under the register's accounting, the reading, the episode table, three limits), five takeaways, four exercises; deviations: the chapter's central result, the detection figure and table the text calls "the chapter's argument in small", lands inside the implementation section with the package subsection between it and the application, and the application opens with a method subsection whose figure is never read.

### Opening (before the first heading) (294 words)
Says: Whether the portfolio should depend on an unobserved state is a question this market gives reason to ask, and the chapter answers it by stating the model, detecting the regimes two ways and testing a switch out of sample.
Why here: the opening by contract; ¶2 lays out the order (model, filter, mixture; date, detect, package; the out-of-sample test).
Paragraphs: code · claim · method · method · code

### Regimes, Filters, and Mixtures (1213 words)
Says: A regime-switching model is a Markov chain plus a filter; the investor faces mixture moments with a between-regime term, uses the state by mixing or by switching, and must detect the regime rather than date it, with turbulence as the parameter-free detector.
Why here: by contract; the opening's plan names the model, the filter and the mixture moments first. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: six subsections of 120 to 260 words; the chapter's thesis is stated in passing at the end of the filter subsection and again as the one-sentence last paragraph of the two-rules subsection.

#### The regime-switching model (120 words)
Says: Returns are Gaussian within a state that follows a Markov chain whose transition matrix fixes regime durations and long-run shares.
Why here: not stated; the definitions the filter needs.
Paragraphs: definition

#### The Hamilton filter (224 words)
Says: The state is inferred by a prediction and an update step whose normalizer is the likelihood; EM maximizes it with smoothed probabilities, and the filtered–smoothed difference is the chapter's subject.
Why here: stated: the state is never observed, so everything rests on its probability given the returns seen so far.
Paragraphs: derivation · definition
Note: ¶2's last sentence states the chapter's thesis inside a definition.

#### One-step-ahead moments as a mixture (236 words)
Says: Next month's return is a mixture whose covariance carries a between-regime term and whose tails are fat and asymmetric from Gaussian ingredients, jointly across assets.
Why here: stated: the investor at t does not know s_{t+1}, so faces the predicted probabilities' mixture; the between-regime term and the kurtosis are reused by the worked example.
Paragraphs: derivation · claim
Note: ¶2 does four things: interprets the between-regime term, derives the kurtosis, links to chapter 4's stylized facts, and links to chapter 11's co-moments and the correlation-asymmetry literature.

#### Two ways to use the state (261 words)
Says: Given the state probabilities an investor either holds the tangency portfolio of the mixture moments or switches between regime portfolios on the most probable state, and the literature finds both worth something against a static policy.
Why here: stated: "given π there are two rules"; the switching rule (eq-19-switch) is what the package implements and the application tests.
Paragraphs: definition · evidence · transition
Note: ¶2 carries eight citations in one paragraph; ¶3 is one sentence turning the section toward dating and detecting.

#### Dating and detecting (214 words)
Says: Dating uses the whole sample and detecting only the past, so detection lags; a regime backtest leaks through smoothed probabilities, full-sample parameters and a regime definition settled after looking.
Why here: stated by ¶3 of the previous subsection, the estimate is the difficulty; the two coding leaks are "asserted away below" and the design leak is sent to chapter 25.
Paragraphs: definition · caveat

#### Turbulence as a model-free detector (152 words)
Says: The turbulence index of chapter 5 has no parameters to estimate, is persistent and poorly rewarded while it lasts, and a quantile threshold on it is the simplest detector there is.
Why here: stated: a regime model has parameters to estimate before it says anything, so a parameter-free detector is set beside it.
Paragraphs: definition

### Implementation (3270 words)
Says: The four dated episodes are described, two detectors are built without look-ahead and compared against the dated regimes, and the package's regime machinery is shown to be row selection with seven measured behaviors.
Why here: by contract; the opening's plan: date with hindsight, detect two ways, then what the package offers for switching. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: at 3,270 words the chapter's largest section; it carries the chapter's central result, the detection figure and table, before the application begins.

#### Regimes dated with hindsight (396 words)
Says: Inside the four dated episodes equities always lose, government bonds lose only in the rates shock and correlations rise, but a sixteen-by-sixteen matrix from a few months describes and cannot be optimized on.
Why here: stated in the opening's plan: date the regimes first; the table is referred back to twice from the application for the rates shock.
Paragraphs: method · code · code · code · result
Note: ¶2 reads the table and ends in a caveat on rank and on correlation rising mechanically with volatility [@forbes2002]; the "not one stress regime observed four times" point is credited to chapter 4.

#### A detected regime: the turbulence threshold (233 words)
Says: The flag for month t is the index above the 75th percentile of its own expanding history through t−1, verified against a hand-computed Mahalanobis distance and a reversal test for look-ahead.
Why here: not stated beyond the opening's order; the theory called it the simplest detector; the flag feeds the package demonstration and the application.
Paragraphs: method · code · method · code
Note: the no-look-ahead check (reverse the tail, the flags through the cut must not move) lives in a code comment and an assertion; no paragraph reads what the flag finds, which arrives only in the detection table of the next subsection.

#### A detected regime: a two-state hidden Markov model (1547 words)
Says: A two-state model fitted inline to the equal-weighted return finds a volatility regime, not a bear market; with hindsight it is clean, in real time it has nothing to detect the first crisis with and lags the later ones, while the turbulence threshold flags the credit crisis in its first month.
Why here: its place after the threshold is not stated; within it, the summary series is justified by the parameter count and the real-time refit by "those estimates used every month"; the figure and table are "the chapter's argument in small".
Paragraphs: method · code · result · code · example+c · result+c · method · code · code · code · code · code · result
Note: 1,547 words, half the implementation section; its figure and table are the chapter's pivot and sit two subsections before the application; ¶6 reads two detectors, four episodes and the false-alarm rates in one paragraph; the worked callout is collapsed; ¶2 opens on a caveat (the floor) before reading the fit.

#### Regime portfolios in `PortfolioAnalytics` (1091 words)
Says: `regime.portfolios()` with `optimize.portfolio.rebalancing()` reproduces exactly the weights obtained by picking rows from two separate runs, and seven measured behaviors say what it checks and what it does not.
Why here: stated: the package "ships the machinery for the switching rule", and "the backtest needs both portfolios at every month", so the two portfolios the application switches between are built here.
Paragraphs: method · code · method · code · method · code · result · code · transition+c · caveat+c
Note: the package's `maxSR` route runs only on an eighteen-month demonstration stretch to confirm the hand QP; the seven behaviors are measured in one chunk and reported as one bullet list; ¶4's last sentence announces the measurements before the chunk; the 0/1-coding and date-shift behaviors are the chapter's own contribution and reach the takeaways as one bullet.

### Detected Against Dated Regimes, Out of Sample (2290 words)
Says: Dated switching beats the static policy, the two detectors keep little or none of it and neither differs from the static policy by a paired test, and the stress portfolio held throughout beats both detectors.
Why here: by contract; the opening's plan ends with the out-of-sample question "once the regime has to be detected rather than dated". Paragraphs: none of its own; the section goes straight to its first subsection.
Note: two subsections; the first builds the figure and both tables and reads none of them, the second reads everything; the application opens with a method paragraph rather than a picture, and the cumulative-return figure is never referenced in the prose.

#### The strategies and their accounting (1259 words)
Says: Six strategies from observation 121, two static, three switches by dated, turbulence and filtered regimes, and the mixture mean-variance rule, are run under the register's accounting with drift, turnover and per-class costs.
Why here: stated: the register of chapter 25 fixes the start and the accounting, so the numbers are comparable to its rows; chapter 23 supplies turnover and cost.
Paragraphs: method · code · method · code · code · code · code
Note: 1,259 words of which two paragraphs are prose; the strategies chunk also verifies the law of total covariance and reproduces the mixture portfolio through `momentFUN`, neither mentioned in prose; the accounting chunk defines the Jobson–Korkie–Memmel statistic in a code comment, attributed in prose only in the next subsection; the figure built here is never read.

#### Reading the result (1022 words)
Says: The static rows reproduce the register; dated switching works and part of it is timing; turbulence keeps a small part and times no better than a fixed blend, the filtered model none, the mixture rule passes its estimation error to the optimizer; nothing is distinguishable from sampling error, and the stress portfolio throughout beats both detectors.
Why here: stated: "the two static rows are checks before they are results", then each row is read against the constant mix with the same stress share; the episode table "shows where each number comes from".
Paragraphs: result · result · result · claim · code · code · result · caveat
Note: ¶3 reads three strategies against three yardsticks in the chapter's longest paragraph; ¶4's "whether, not when" is the chapter's verdict and arrives before the episode table that explains it; four hidden chunks (dated-, detection-, performance-, episode-facts) assert every ordering the prose states.

### Key Takeaways (261 words)
Says: Five bullets: the model plus the filter, the mixture moments and fat tails, dating against detecting, what `regime.portfolios()` does, and the out-of-sample verdict.
Why here: by contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: five, on contract; bullet 5 restates ¶3, ¶4 and ¶5 of the reading in one sentence; nothing on the mixture rule's out-of-sample result.

### Exercises (228 words)
Says: Four exercises: vary the turbulence threshold, feed the dated regimes through the package's contemporaneous lookup, simulate the chain to separate persistence from fat tails, and a half-invested stress portfolio for the rates shock.
Why here: by contract; ¶6 of the reading says the exercises vary what the chapter chose once.
Paragraphs: exercise · exercise · exercise · exercise
Note: four against "around three"; exercises 1, 2 and 4 each follow one design choice named in the reading's ¶6; exercise 3 is the theory's eq-19-kurtosis; no exercise touches the mixture rule.

## Chapter 20: Sustainable Investing Constraints (7748 words, 40 paragraphs)
Claim: A sustainability constraint that does not bind costs nothing; one that binds costs tracking error and return at the rate its multiplier prices, paid through the priced characteristics the rating is correlated with; it is a cost and never an alpha, so the chapter prices the constraint rather than the names.
Question: What does an exclusion or a rating floor cost a portfolio, and who pays? Cited to @pedersen2021 for the cost (the ESG-efficient frontier) and @pastor2021 for who pays (tastes priced in equilibrium).
Why here: Takes the multiplier and the constraint functions of ch. 12, the shrinkage of ch. 7, the policy of ch. 15 and the strategic/tactical vocabulary of ch. 3; builds on the equity sleeve, its capitalization anchoring and the policy recomputation of ch. 21, a later chapter, and uses the tracking-error and standard-error equations of ch. 24. Forward: ch. 25 (what a screen does to a backtest's error bar) and ch. 28 (stability across windows). Why it closes Allocation Strategies: not stated; the text places it only on the horizon axis, as strategic.
Does: Construct rating levels from a path of changes, impose an exclusion, a floor and a best-in-class floor on an equity sleeve, price each by active share, tracking error and multiplier, audit the solutions, and measure the cost out of sample and across raters.
Order: Theory (five subsections, one paragraph each) → implementation (levels, sleeve, exclusion, floor, multiplier check, audit) → application (out-of-sample costs, then a second rater) → takeaways → exercises. Contract kept; the real-data callout closes the implementation from inside "The audit", and the chapter's closing sentences sit inside the last application subsection.

### Opening (before the first heading) (498 words)
Says: A line in the mandate costs tracking error and expected return only when it binds, at the multiplier's rate, and is never an alpha; the chapter sets out, constructs and prices three such lines.
Why here: Chapter contract: the question with its citations, then the plan; the plan states the order the three sections follow.
Paragraphs: code · claim · method · code

### Tastes, Floors, and Exclusions (1140 words)
Says: A taste and a floor trace one frontier priced by the floor's multiplier; an exclusion is a box at zero with a Jagannathan–Ma price; a tilt is a factor exposure on a score; and the score is an estimate whose taste is priced in equilibrium.
Why here: The opening's plan puts the problem first; the two framing results of the opening are what the section works out, and every object the implementation builds (eq-20-floor, eq-20-exclusion, eq-20-bic) is defined here. Paragraphs: none at this level; the section goes straight to its first subsection.
Note: Five subsections, each a single paragraph of 160 to 300 words; the theory of the chapter is five paragraphs.

#### The investor's problem with a taste for a rating (301 words)
Says: A taste for a rating and a floor on it produce the same portfolio, the floor's multiplier being the taste, so a binding floor costs variance at the shadow price and a slack one costs nothing.
Why here: First because the opening's plan starts with the investor's problem; needs the investor of ch. 3 and the Lagrangian and shadow price of ch. 12; eq-20-floor is what the tilt subsection and the implementation impose.
Paragraphs: derivation
Note: One 300-word paragraph around two display equations makes five moves; the last, that a floor is a preference and not information about the estimates, is a claim of its own.

#### Exclusion as a restriction of the universe (304 words)
Says: An exclusion is a box at zero; for a capitalization-weighted sleeve its active share is the benchmark weight removed, and for an optimized sleeve a binding exclusion is an implicit risk view priced by its multiplier.
Why here: Called the oldest form of the constraint; order as in the opening's plan. Needs eq-12-jm and the tracking error of ch. 24 (later); the implementation's exclusion and exclusion-jm chunks check both readings.
Paragraphs: derivation
Note: One paragraph carries three things: the capitalization-weighted cost, the optimized cost, and the equilibrium evidence.

#### Tilts as a factor-exposure constraint on a score (157 words)
Says: A floor is a factor-exposure constraint on the score, a best-in-class floor is one such row per group in centered scores, and the second costs more because it cannot buy the rating where it is cheapest.
Why here: Third form in the opening's order; needs eq-20-floor and ch. 12's `factor_exposure_constraint()`; eq-20-bic is what `bic_B()` implements.
Paragraphs: definition

#### A rating is an estimate (196 words)
Says: Ratings disagree across raters (0.54 average correlation), so a floor is imposed on an estimate and a different rater excludes different names; carbon is the exception the modeled market cannot run.
Why here: First of the "two facts that complicate all three" named in the opening; comes after the three forms it complicates. Needs ch. 8's estimation error as the analogy; the application's second rater is its test.
Paragraphs: evidence
Note: The carbon-budget sentence is a scope caveat parked at the end of an evidence paragraph.

#### Tastes are priced (182 words)
Says: In equilibrium a taste lowers green assets' expected returns, realized green outperformance reflects taste shifts, and a constraint is a cost, not an alpha; the mixed alpha evidence is not needed to price it.
Why here: "Finally", the second complicating fact; closes with the hand-over: none of the alpha evidence is needed to price the constraint, which the rest of the chapter does.
Paragraphs: claim

### Implementation (3102 words)
Says: The levels are built from the shipped changes under a stated, seeded assumption; a screen, a universe floor and a best-in-class floor are then imposed on ch. 21's sleeve and priced by active share, tracking error and multiplier, with every solution audited.
Why here: The opening's plan: construct levels, then implement the three constructions, auditing with ch. 12's functions. The callout says why levels come first: the market ships changes and no starting grade. Paragraphs: none at this level.
Note: 3,100 words, two fifths of the chapter, most of it code; "A floor on the sleeve's rating" alone is 1,080 words around four chunks.

#### A level from a path of changes (727 words)
Says: The market ships rating changes and no levels, so the chapter draws a seeded starting cross-section and cumulates the changes, which, being mostly upgrades, compress the scale toward the ceiling.
Why here: A screen or a floor needs the level's constant, so the construction precedes every constraint; the drift found here is what the application's slack figure tests.
Paragraphs: caveat+c · method · code · code · result · code · caveat
Note: ¶4 is the premise the application's sector finding rests on; it is stated as an aside after the figure.

#### The sleeve, its benchmark, and its covariance (221 words)
Says: The sleeve is ch. 21's, capitalization weighted within region with equal regional budgets here, and its covariance is shrunk because the sample matrix on 120 months is singular.
Why here: Provides b, S and s to every construction after it; why it follows the levels rather than precedes them: not stated.
Paragraphs: method · code

#### Exclusion (542 words)
Says: The bottom fifth of each region removed and reweighted gives active share equal to the benchmark weight removed; on the minimum-variance sleeve only some exclusions bind, and the Jagannathan–Ma identity reproduces the screened solution.
Why here: Theory's first construction; needs b, S and s from the sleeve; checks eq-20-exclusion and eq-12-jm in code.
Paragraphs: method · code · result · code · result

#### A floor on the sleeve's rating (1082 words)
Says: A floor across the universe costs nothing until the benchmark's own rating and then rises convexly; best-in-class costs more at every floor and binds at once because one region sits below the lowest floor.
Why here: Theory's second and third constructions; the base spec is ch. 12's; the callout says tracking error must be solved by hand, and the `min_te()` defined here is what the application runs monthly.
Paragraphs: method · code · caveat+c · code · code · code · result
Note: Four chunks between ¶2 and ¶3, one hidden; the floor-specs chunk also prints the attainable maximum rating, which no prose reads.

#### The multiplier, checked by perturbation (157 words)
Says: The multiplier quadprog returns matches the finite difference of eq-12-shadow, and up to scale it is the taste an investor would need for the floor to be their free choice.
Why here: Follows the frontier, whose multipliers it verifies; ties the implementation back to θ = λ_s of the theory. Why a subsection of its own: not stated.
Paragraphs: code · result
Note: The subsection opens on code; nothing announces what the chunk does before it runs.

#### The audit (373 words)
Says: Both floor solutions pass every constraint; the universe floor binds once, the best-in-class floor in several regions, which is where its extra cost comes from; on real data the same mechanics apply to industry screens.
Why here: "Every solution above": after all solutions exist, with ch. 12's `audit_spec()`. The real-data callout's placement here: not stated.
Paragraphs: method · code · result · caveat+c · code · claim+c
Note: The real-data callout is about neither the audit nor the floor; it is the implementation's coda, filed under its last subsection.

### What the Constraints Cost Out of Sample (2399 words)
Says: Out of sample the two floors cost active risk but no significant return, and expire once the drift carries the benchmark past them; the screen costs return under every rater because the upgrades cluster in the sectors that earned least.
Why here: The opening's plan: measure what the three cost inside ch. 15's policy, recomputed as ch. 21 recomputed it; needs every function of the implementation and the drift of fig-20-drift.
Paragraphs: method · code · method · code · code · code · code · result · code · result · code · code · claim · code · result
Note: ¶3 reads three table columns and poses the next question in 270 words; ¶3 to ¶6 run a draw → sector → slack argument with no subsection breaks, while the second rater gets one.

#### A second rater (421 words)
Says: At real raters' correlation roughly half an exclusion list is the rater's choice, and closely agreeing raters still disagree substantially; the cost and its sector exposure are not the rater's, which is why the chapter priced the constraint rather than the names.
Why here: "The last question"; needs `second_rater()` from the screen-raters chunk and Berg's 0.54; closes the chapter with the pointers to ch. 25 and ch. 28.
Paragraphs: method · code · code · result
Note: The chapter closes inside this subsection; its last sentences are the pointers to ch. 25 and ch. 28, and there is no closing paragraph at section or chapter level.

### Key Takeaways (301 words)
Says: Five bullets restating the frontier, the exclusion, the floor, the construction and the rater results.
Why here: Chapter contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: ¶4 carries four results in one bullet; the sector mechanism, the chapter's main finding, shares a bullet with the drift.

### Exercises (178 words)
Says: Four exercises: a relative floor, a narrower cross-section, the screen as a box constraint, and the second rater applied to the floor sleeve.
Why here: Chapter contract; exercise 1 is the relative floor that ¶6 of the application promised.
Paragraphs: exercise · exercise · exercise · exercise

# Part VI: Inside the Sleeves

## Chapter 21: The Equity Sleeve (6729 words, 33 paragraphs)
Claim: Selection survives the allocation only in the sense the arithmetic allows: the sleeve's information ratio reaches the total intact while its active return and tracking error arrive scaled by the equity budget ω, and on this market what the total registers is the selected sleeve's lower variance, not an alpha that the out-of-sample months cannot distinguish from zero.
Question: Which stocks should fill an equity sleeve whose budget and benchmark are fixed from above, and is whatever the selection earns still visible once the sleeve is one line of the allocation; @fama1992 and @fama1993 for selection by sorting as a method, @treynor1973 for combining the active sleeve with the passive portfolio.
Why here: Stated: the first chapter to work inside a class rather than across classes, the granularity axis of chapter 3 made concrete on the 123 equities behind the five series that Parts III to V allocated as single numbers. Takes from chapter 2 the capitalization-weighted indices and the independence of the idiosyncratic draws, from chapter 5 the lagged proxy and the within-region lesson, from chapter 7 the rank bound, the repairs and the race, from chapter 12 the dropped position limit, from chapter 15 the policy and the sub-portfolio mechanics, from chapter 18 the parametric estimate of the same characteristics; sends forward to chapter 22 (a duration in place of a characteristic), chapter 23 (the cost of the trading) and chapter 25 (the register). Its mandate, active-weight notation, fundamental law, information-ratio standard error, budget figure and cone solver are all taken from chapter 24, three chapters later, which the text treats throughout as already read.
Does: Rebuild a capitalization-weighted benchmark from its instruments with the right lag, run within-region characteristic sorts with Newey–West inference, build a factor or shrunk covariance on a universe wider than the window, solve a minimum-variance sleeve under a tracking-error budget by a one-parameter quadratic family and a root search, wrap sleeves as sub-portfolios, and trace a sleeve's active return into the total portfolio.
Order: Theory (mandate and the ω arithmetic, sorts, equal weighting, covariance with the cardinality limit and the tracking-error family), implementation (benchmark rebuilt, equal against cap, sorts, covariance race, the budgeted sleeve, the sub-portfolio), application in one undivided section (policy recomputed, three fillers, sleeve rows, total rows, sampling error, the figure), five takeaways, four exercises; deviations: the application opens with code and a table and reaches its only figure last, and the sub-portfolio subsection builds a structure the application then sets aside.

### Opening (before the first heading) (391 words)
Says: An equity sleeve arrives with its budget and benchmark fixed from above, and which names fill it and whether selection is still visible one level up have been one question since Treynor and Black.
Why here: the opening by contract; ¶2 lays out the chapter's order in three steps and places the sleeve on the horizon axis as strategic.
Paragraphs: code · claim · method · code
Note: ¶1 places the chapter on the granularity axis and ¶2 on the horizon axis; the data chunk asserts the equities align with the class series before any theory.

### Selection Inside a Budget (1050 words)
Says: A sleeve is judged against the class index it sits in under a tracking-error budget that scales active return and tracking error but not the information ratio; size and momentum are the sorts this market allows; and 123 names force a covariance repair and turn the budget into a one-parameter family.
Why here: stated in the opening's plan: benchmark and mandate, the arithmetic, the sorts, the estimation problem, before anything is built. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: four subsections on four topics, and the fourth also carries the cardinality limit and the tracking-error family, which its heading does not announce.

#### The benchmark, the mandate, and the arithmetic of a sleeve (314 words)
Says: The benchmark is the regional capitalization-weighted index, the mandate is chapter 24's tracking-error budget, and the sleeve's active return and tracking error reach the total scaled by its budget ω while its information ratio does not.
Why here: stated: budget and benchmark come from above and are fixed before any selection is scored; the application is announced as checking both halves of the arithmetic.
Paragraphs: definition · derivation
Note: ¶2 carries two numbered equations, the worked example and the application's plan in one paragraph; the mandate, the active weights and the information ratio are all chapter 24's, three chapters ahead.

#### Selection by characteristic (231 words)
Says: Size and momentum are the sorts this market can run, within region and averaged across five, because value needs a fundamental the data lack and a global sort sorts on region; breadth is why a sleeve can earn an information ratio from a weak signal.
Why here: not stated; follows the mandate and precedes the equal-weighting case whose gap the sorts are later asked to separate.
Paragraphs: method · claim
Note: ¶1 does three things, defines a sort, surveys the literature and takes the within-region design decision; ¶2 rests on chapter 24's statement of the fundamental law.

#### Equal weighting is an active bet (98 words)
Says: Holding 1/N is a size tilt and a contrarian rebalancing rule at once, long every name smaller than average, and inside a sleeve the question is whether that bet pays.
Why here: not stated; it is the simplest departure from the benchmark and the one the implementation measures first.
Paragraphs: claim
Note: one paragraph; the heading is a claim sentence rather than a noun phrase.

#### The covariance matrix of a sleeve (401 words)
Says: With 123 names any window under 124 months is singular, so the sleeve needs shrinkage or a k-factor structure; a cardinality limit is a mixed-integer problem whose convex substitute is a cap; and the budget on a minimum-variance sleeve is a one-parameter blend of benchmark and minimum variance found by a root search.
Why here: stated: everything the sleeve optimizes needs Σ, and chapter 7's rank bound says the sample estimate cannot deliver it on this universe.
Paragraphs: definition · derivation
Note: ¶2 holds three topics, the within-region parameter count, the cardinality limit and the tracking-error family; the family is the chapter's own device and arrives at the end of a subsection named for the covariance matrix.

### Implementation (2984 words)
Says: The benchmark reproduces from the instruments; equal weighting beats it everywhere at a tracking error most mandates forbid; size is present and momentum absent by construction; factor matrices give the lowest volatility and shrinkage the highest Sharpe ratio; the budgeted sleeve is a blend; and a sub-portfolio can carry its estimator but not its budget.
Why here: stated in the opening's plan: rebuild, measure, sort, race, build, wrap, in that order. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: six subsections, one per step of the plan; the last builds the package's sub-portfolio structure and ends by saying the application cannot use it.

#### The benchmark, rebuilt from its instruments (431 words)
Says: The five regional indices reproduce from previous-week capitalization weights to machine precision, and capitalization weighting is itself concentrated, the US index behaving like a fraction of its names.
Why here: stated: rebuilding the benchmark is the check that it is one the sleeve could have held; the monthly weights it yields are what every later step indexes by name.
Paragraphs: method · code · result · code · code · result
Note: the concentration table is read in one sentence; its ratio and top-five columns are never mentioned, and the largest-weight column is used only two subsections later to set the cap.

#### Equal against capitalization weighting (295 words)
Says: Equal weighting earns more than its benchmark in every region, by one to four points a year, at a tracking error larger than most mandates allow and an information ratio mostly within two standard errors of zero.
Why here: stated in the theory: the question was whether the bet pays; the result hands the sorts the question whether it is size or rebalancing.
Paragraphs: code · code · result
Note: the subsection opens with code and a table and has one paragraph; the chunk asserts the ordering the prose relies on.

#### Sorting on size and momentum (551 words)
Says: Within region, small beats large with a t-statistic above two and the long-only leg keeps part of it; momentum is absent, and absent by construction, because the idiosyncratic draws are independent period by period.
Why here: stated: the sorts separate the equal-weight gap into a size premium and rebalancing; the design, within region and averaged, was fixed in the theory.
Paragraphs: method · code · code · code · result
Note: ¶2 carries the result and the caveat that explains it away; the promised separation of size from rebalancing is not performed here, only the size half is shown, and exercise 3 asks the reader for it.

#### A covariance matrix for one hundred and twenty-three names (753 words)
Says: The package's factor model refuses the window it is needed on, a six-line replacement reproduces it where it runs, and in a rolling race the factor matrices give the lowest volatility while shrinkage gives the highest Sharpe ratio, the sample matrix producing no portfolio on any window.
Why here: stated: the theory said the sleeve needs a repair before it can be optimized at all; the race is chapter 7's, rerun on the sleeve's names.
Paragraphs: code · code · caveat+c · method · code · code · code · result
Note: ¶3 opens by reading a number and then announces the race; the callout repeats chapter 7's route-two caveat on the same function; the race leaves the choice open and the next subsection takes shrinkage without saying why, although the factor matrices won on the number a minimum-variance sleeve minimizes.

#### The selected sleeve (681 words)
Says: Unconstrained minimum variance holds a handful of names with a large weight in one; the cardinality limit is dropped on the variance path, so a cap per name stands in; and under a four percent budget the family picks a blend that buys a stated share of the distance between benchmark and minimum variance.
Why here: stated: the mandate limits the concentration the unconstrained solution shows, and the budget enters through the family because the package cannot express it, for the reasons chapter 24's callout gives.
Paragraphs: method · code · result · code · caveat+c · method · code · result
Note: the position-limit chunk sits inside the callout; the callout's finding repeats chapter 12's trap on a new universe; `select_sleeve()` is built once here and reused monthly in the application.

#### The sleeve as a sub-portfolio (270 words)
Says: `mult.portfolio.spec()` wraps each regional sleeve as a sub-portfolio with its own covariance estimator through `momentFUN`, with chapter 15's three quirks intact, but cannot carry the tracking-error budget, so the application runs its two stages by hand.
Why here: stated: it is the package's structure for a sleeve the allocation layer can consume, and chapter 15 set its arguments; what it cannot do is why the application is built differently.
Paragraphs: method · code · caveat
Note: the chunk prints the top-level weights and no paragraph reads them; the subsection demonstrates a structure the chapter then does not use, and its yearly re-estimation under a flat cap differs from the application's monthly, budgeted sleeve on both counts.

### Selection Under the Allocation Above It (1853 words)
Says: Filling the policy's equity budget three ways, the sleeve's active return and tracking error reach the total scaled by ω and its information ratio intact; neither sleeve's information ratio is two standard errors from zero, and what the total registers is the selected sleeve's lower variance rather than an alpha.
Why here: stated in the opening's plan: fill the equity budget of chapter 15's policy three ways and ask what the total portfolio noticed; the policy is recomputed so the budget is computed rather than quoted.
Paragraphs: method · code · method · code · code · result · code · code · code · result · result · claim · code · result
Note: one undivided section of 1,853 words and seven chunks; the only figure arrives last and is read in the closing paragraph, against the house rule that an application opens with the picture; ¶6 ends on a drawdown sentence unconnected to its sampling-error point; the Sharpe-difference z-tests are computed in a hidden chunk and never tabled.

### Key Takeaways (221 words)
Says: Five bullets: the benchmark and the budget, the ω arithmetic and the Treynor–Black bound, size present and momentum absent by construction, the singular matrix and the race's split verdict, the cardinality trap and the one-parameter family.
Why here: by contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: five bullets, on contract; none states the application's finding, that neither sleeve's information ratio is distinguishable from zero and that the total registers variance rather than alpha, which is the chapter's claim.

### Exercises (180 words)
Says: Four exercises: the budget varied, the momentum signal varied, annual against monthly equal weighting, and the Treynor–Black weight against the policy's budget.
Why here: by contract.
Paragraphs: exercise · exercise · exercise · exercise
Note: four against "around three"; exercise 3 supplies the size-versus-rebalancing separation the sorts subsection promised, and exercise 4 the ω chosen for the ceiling that the theory said the policy does not choose.

## Chapter 22: The Fixed Income Sleeve (7199 words, 52 paragraphs)
Claim: Duration targeting and portfolio optimization are one problem: a bond portfolio is a set of exposures to level, slope, curvature and spread, so a duration target is a `factor_exposure` bound on a minimum-variance program, its level strategic and its term-spread overlay tactical, while abroad the currency, not the duration, carries most of the risk.
Question: What changes in portfolio construction when the asset has a duration; cites @litterman1991 (three curve factors explain nearly all variation in government bond returns, so exposures describe a portfolio better than its list of bonds), with @nelson1987 and @diebold2006 for the form of the curve.
Why here: Stated: the sleeve is the bond part of the allocation, one level below the class series on which ch. 15 allocates, and on ch. 3's horizon axis its duration is strategic and its curve positioning tactical. Takes the data and the hedge identity from ch. 2 and appendix A, the currency share from ch. 4, the bond block's rank deficiency from ch. 7, the home-bond argument, the naming rule and the `full_investment` degeneracy from ch. 9, the quadratic program from ch. 12 and ch. 13, the units, the month-end read and the surviving term spread from ch. 16, the policy and its estimator from ch. 18; it uses ahead of their chapters the per-class costs of ch. 23 and the register's start and backtest of ch. 25, and points to ch. 10 for a skewness it does not compute. Hands the cost of maintaining the exposures to ch. 23, whether one sample is evidence to ch. 25, the ignored exposure bounds to ch. 28 and the loadings to the scenario appendix. Why it follows ch. 21 is not stated: the equity sleeve, its only sibling in the part, is never mentioned.
Does: Split a bond return into carry, rolldown, duration and convexity; read durations and maturities from factor regressions; recognize the shipped factors as one rotation of three yields beside Nelson–Siegel loadings and principal components; build a minimum-variance sleeve under duration and slope bounds while guarding three silent package behaviors; fit and bootstrap a term-spread overlay; backtest sleeves against the class ladder and read them by episode.
Order: Opening (question and claim, roadmap with the strategic and tactical labels, data, one remark on the data chunk); theory in six subsections (return decomposition, three factors, credit, duration target as constraint, currency, predictability); implementation in five (units, exposures and rotations with a worked box, currency and the fit, the constrained sleeve with a warning callout, the overlay); application as one unbroken section (four sleeves defined, backtests, a callout, three tables read in turn, a closing paragraph); takeaways; exercises. Deviations: the theory runs a chunk and reads its result (the currency share) and carries inline sample numbers on credit; the theory orders credit, target, currency, predictability where the implementation orders exposures, currency, sleeve, overlay; the overlay's in-sample fit, a result, sits in the implementation; the credit sleeve is specified only in the application's opening paragraph and its backtest chunk; every sleeve is unhedged although theory and implementation both argue that an unhedged duration target controls a minority of the risk, and the hedged sleeve is exercise 1; the application opens with a method paragraph and four chunks, not a picture, and has no subsections; `fig-22-factors` is never read; five takeaways, four exercises.

### Opening (before the first heading) (440 words)
Says: A bond portfolio is described by its factor exposures rather than its holdings, and the chapter claims that duration targeting and optimization are one problem, on the sleeve one level below ch. 15's class series.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections; the place below ch. 15's class series is stated, the place after ch. 21 is not.
Paragraphs: code · claim · method · method · code · caveat
Note: ¶1 carries the question, three citations, the chapter's place and its claim in one block; no visible packages block; ¶4 is a one-sentence remark that reads an assertion in the data chunk.

### Bonds as Exposures to the Curve (1378 words)
Says: A bond's return is carry plus rolldown minus duration times the yield change, so a portfolio matters only through its loadings on a few curve factors, plus spread and currency; a duration target is a linear constraint on those loadings, and the shape of the curve gives the tactical case.
Why here: The roadmap's first step (why a bond is a set of exposures, and what credit and currency add); the text says the exposure result is the reason the sleeve is specified as exposures; the roadmap does not name the fourth and sixth subsections. Paragraphs: none before the first subsection.
Note: Six subsections, four of them a single paragraph; the chapter's named claim sits in the fourth, in one paragraph with inline mathematics only; one chunk, in the fifth.

#### Price, duration and the return decomposition (354 words)
Says: The log return of a zero-coupon bond splits exactly into carry, rolldown and duration times the yield change; when K factors drive the yields, a portfolio's risk depends on its weights only through K exposures.
Why here: First because every later subsection refers to eq-22-return or eq-22-exposure; the text says the exposure result is why the sleeve below is specified as exposures and not as weights.
Paragraphs: definition · derivation · derivation
Note: ¶2 does five jobs in about 200 words (the identity, the reading of its terms, two attributions, duration and convexity defined, the modeled market's design); convexity is defined in a clause and returns only in the worked box.

#### Three factors of the curve (234 words)
Says: Nelson–Siegel's curve with Diebold–Li's level, slope and curvature, and Litterman–Scheinkman's principal components, describe the same three factors; with three maturities any such description is an exact rotation of the three yields.
Why here: Needs the K-factor exposure just derived; the text defers which rotation the data ship to the implementation, and ties the factor count to ch. 7's rank deficiency.
Paragraphs: definition
Note: One paragraph holds one equation, three literatures and two cross-references; the slope's sign (short minus long) is fixed in a clause and decides the sign of the overlay's term spread later.

#### Credit as a separate exposure (236 words)
Says: A corporate bond adds a fourth term, the spread duration; spread changes share one factor per region, the spread is persistent, and its volatility scales with its level.
Why here: The roadmap's "what credit adds"; the text says two features matter for the sleeve; why it comes before the duration target is not stated.
Paragraphs: definition
Note: A definition, three attributions, the market's construction and two measured facts (inline numbers from the sample) in one block; duration times spread is introduced, and the credit sleeve later bounds spread duration alone.

#### Duration targeting as a constrained optimization (210 words)
Says: A duration target is a linear constraint on the weights, so minimum variance under it stays a quadratic program; in `PortfolioAnalytics` it is a `factor_exposure` constraint, a second column chooses bullet or barbell, the level is strategic and the conditioned deviation tactical.
Why here: Needs eq-22-exposure (a duration target bounds the level loading); sends the program to ch. 12 and ch. 13 and the deviation to the implementation as ch. 18's policy; why it sits between credit and currency is not stated.
Paragraphs: claim
Note: The chapter's named claim is made here, in one paragraph of about 200 words, with the constraint as inline mathematics and no numbered equation; bullet and barbell are explained in a clause and set as terms only in the implementation.

#### Currency, and why the two decisions are not separable abroad (214 words)
Says: For a dollar investor most of the variance of a foreign government bond is currency, so the duration decision and the currency decision cannot be taken one at a time.
Why here: Stated: every series is in dollars, and ch. 4 showed that the currency share depends on the asset; the text hands the effect on the factor fit to the implementation.
Paragraphs: claim · code · result
Note: The theory's only chunk, and a result read inside the theory; ¶2 reads the Japanese number, the European one prints unread; four positions on hedging pass in one sentence.

#### Predictability from the curve (122 words)
Says: The shape of the curve forecasts bond returns, and ch. 16 found the term spread the one signal that survives out of sample on this market, so the overlay conditions on it.
Why here: Stated: the tactical case rests on it; it closes the theory, though the overlay it motivates comes four subsections into the implementation.
Paragraphs: evidence
Note: Four citations and one borrowed result, no equation; the shortest subsection.

### Measuring and Targeting the Exposures (2957 words)
Says: The shipped factors come in mixed units and are an observable rotation of three yields; regressions recover each bond's duration and maturity; duration and slope bounds in `factor_exposure` produce a barbell and a bullet, with three silent package behaviors; the overlay's fitted tilt has the predicted sign and an inconclusive t-statistic.
Why here: The roadmap's second step (measure the exposures, build the constrained sleeve, fit the overlay); needs every equation of the theory; the application takes `sleeve()`, `mat`, `policy_utility()`, `D_bar` and `w_bar` from here. Paragraphs: none before the first subsection.
Note: Two fifths of the chapter (2,957 of 7,199 words, 23 of 52 paragraphs); the second subsection alone runs 1,219 words and does four things (exposures, maturities, three rotations, a worked week).

#### The factor series and their units (288 words)
Says: Level, slope and curvature ship in percentage points and the spreads in decimals; the chunk converts to decimals so that a loading is a duration in years.
Why here: Stated: the units are read from the magnitudes before anything is computed from them; ch. 16 found the same.
Paragraphs: method · code · result · code
Note: The subsection ends on a figure no paragraph reads, here or later; it draws the unconverted series, in percentage points.

#### Factor exposures, and which bond is which (1219 words)
Says: Regressing each instrument on its region's factor changes gives level loadings equal to minus the modified duration, identifies the two-, five- and ten-year bonds, and shows the shipped factors to be the observable rotation of three yields; Nelson–Siegel loadings and principal components describe the same space.
Why here: Stated: the exposures of eq-22-exposure are regression coefficients, and `sim_assets` carries no maturity, so it is inferred through eq-22-return; answers the theory's deferred "which rotation"; `mat` and `id_of()` serve everything after.
Paragraphs: method · code · method · code · code · result · result · code · claim · code · transition · code · result · example+c · code · example+c
Note: Four topics in one subsection; ¶3 finds the modified duration under annual compounding where the theory's bond had duration equal to maturity, and only the worked box bridges the two; the Nelson–Siegel chunk prints loadings no paragraph reads; the worked box checks the theory's first identity at the end of a passage on rotations, collapsed, code before formula.

#### What the currency does to the fit (238 words)
Says: Hedged, foreign government bonds are explained by their own curves as well as US bonds are; unhedged, the mean R² collapses, so a duration target on an unhedged foreign sleeve controls a minority of its risk.
Why here: The measurement the theory's currency subsection handed forward; uses the two R² columns of `expo`; why it comes before the sleeve is not stated.
Paragraphs: transition · code · code · result
Note: The finding that an unhedged target controls little of the risk stands directly before a sleeve that is built unhedged; the table is read without being named.

#### The sleeve as a set of exposures (708 words)
Says: Minimum variance over the fifteen government bonds with duration as a `factor_exposure` constraint gives a barbell at duration five; a slope bound turns it into a bullet; the constraint binds its matrix by position, and a bound that cannot be met returns `NA` weights without a message.
Why here: Realizes the theory's fourth subsection with the loadings of `expo`; ¶1 announces both callouts and their reasons (name binding below, the band in the application); the application's strategies call `sleeve()`.
Paragraphs: method · code · result · caveat+c · code · caveat+c · method · code · result · method · code · caveat
Note: Three package behaviors in three placements: a warning callout, running text, and a callout deferred to the application whose `band` argument already appears in this chunk; ¶2 credits the foreign holdings to currency diversification, one subsection after currency was the risk the target does not control.

#### The duration overlay as a parametric policy (497 words)
Says: The long-end weight is an anchor plus theta times the standardized term spread, theta fitted by maximizing average power utility; the fit has the sign the literature predicts, without the precision to be sure of it.
Why here: Stated: it is the tactical layer, written as ch. 18's policy; the theory's fourth and sixth subsections announced it; the anchor takes the ladder's duration because that is the class series the allocation sees; the application re-estimates it monthly.
Paragraphs: definition · code · code · result
Note: An in-sample result in the implementation, and the number the application later leans on to judge the overlay; two chunks back to back with no prose between; the signal is standardized on the full sample here and recursively in the application.

### The Sleeve Out of Sample (1978 words)
Says: From the register's first out-of-sample month the constant-duration sleeve has the ladder's duration at lower volatility because its US holdings carry little currency; the overlay lost least in the rates shock, which is one episode; credit as a second exposure raises the Sharpe ratio in the table and lost in the credit crisis; the ladder is the sleeve's benchmark.
Why here: The roadmap's last step (run the sleeves out of sample against the class series the allocation sees); needs `sleeve()`, `mat`, the policy and its anchor from the implementation; the text gives its reason for running on instruments: the class ladders share one duration, so no target can be set on them.
Paragraphs: method · code · code · code · code · caveat+c · code · code · result · code · code · result · transition · code · code · result · claim
Note: Seven paragraphs in 1,978 words, more than half of it code, with no subsection; between ¶1 and the next body prose stand four chunks, one of them a figure, then a callout and a table, and the figure is first read in ¶4; ¶1 switches `B` from the estimated loadings to the maturities in a clause and is the only prose that specifies the credit sleeve; the callout's title types "a third of the windows" where its body computes the count; ¶3's first reading is a currency effect by the text's own account; ¶7 does four jobs and tells exercise 4's finding.

### Key Takeaways (228 words)
Says: Five bullets: the return decomposition and exposures, the three factors and their rotation, the duration target as a `factor_exposure` constraint with its three traps, foreign bonds as currency, and the overlay as a one-characteristic policy with thin evidence.
Why here: Chapter contract; not stated.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: Five, as the contract asks; credit, a theory subsection and the fourth sleeve, has no bullet; ¶3 folds three package traps into one bullet; ¶5's "below two" is typed, with no assertion behind it in the fit chunk.

### Exercises (164 words)
Says: Four exercises: the duration-five sleeve on hedged returns, the overlay at other risk aversions, the failed windows under another solver, and the nested sleeves with their proxy returns.
Why here: Chapter contract; not stated.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against around three; exercise 1 holds the hedged sleeve that the chapter's currency argument calls for and the text never builds; exercise 4's finding is told in the application's last paragraph and exercise 3's second question is answered in its callout.

# Part VII: Implementation and Evaluation

## Chapter 23: Rebalancing and Transaction Costs (3281 words, 34 paragraphs)
Claim: Free monthly rebalancing is worth different amounts to different strategies: under per-class linear costs the Sharpe ratio lost to trading is ordered by how much a strategy optimizes, rebalancing less often helps the two rule-based portfolios at every estimation window and moves the three optimized ones by more, in a direction that changes with the window, and theory's answer is a no-trade region or a partial adjustment rather than a return to target.
Question: What the assumption of free monthly rebalancing to target is worth, and to which strategies; posed as a statement about the book so far, not as a question, with @peroldshortfall1988 (the implementation shortfall) in the third sentence rather than the first two.
Why here: Stated in the first sentence only: every portfolio so far was rebalanced monthly at no charge. Draws on chapter 4 (the Sharpe ranks of tbl-04-moments, the wandering rolling mean, the credit crisis), chapter 9 (the optimizers, and maximum Sharpe as that chapter's best portfolio), chapter 14 (inverse volatility) and chapter 18 (costs in the objective by construction); reads every measurement from the out-of-sample runs it attributes to chapter 25, two chapters ahead, said to have been computed with and without costs for this purpose; hands `contribution` to chapter 24 and the sources of the cost rates to appendix 93. Why it opens the part, ahead of the backtesting chapter whose runs it reads, is not stated.
Does: Compute one-way turnover by hand and from `Return.portfolio(verbose = TRUE)`, recognize the equal-weight back-fill and the two meanings of a turnover constraint, and read frequency and cost effects for five strategies off the sweep; charging eq-23-net or running a backtest is not shown in code.
Order: Opening, theory (turnover and the cost model, per-class rates, no-trade region and partial adjustment), implementation (three package behaviors), application (frequency table, cost-bite table and figure, calendar against band rules, limits of the cost model), seven takeaways, four exercises; deviations: the theory opens on a chunk and runs code, the implementation section computes nothing the application reads (the sweep comes from a file, and the chapter runs no backtest and charges no cost), the application opens with a table rather than a picture and ends in two prose-only subsections of literature and caveats, and the packages block is hidden.

### Opening (before the first heading) (167 words)
Says: Free monthly rebalancing is not a small assumption; the chapter defines turnover and costs, sets out the theory on how often to trade and measures both on the out-of-sample runs, with its three findings stated up front.
Why here: the opening by contract; ¶2 gives the order (definitions, theory, measurement) and says the runs of chapter 25 were computed with and without costs for this purpose.
Paragraphs: code · claim · method · code
Note: the citation sits in the third sentence; ¶2 gives all three results before any definition and its plan names no implementation step; ¶1's premise sits against chapters 16 and 18 to 22, which already charge the `pm_costs_default()` rates, four of them citing eq-23-net ahead; no visible packages block.

### Turnover, Costs, and When to Trade (717 words)
Says: Turnover is half the summed absolute weight change, its cost is linear and differs by asset class, and with costs theory replaces the return to target with a no-trade region or a partial adjustment.
Why here: stated in the opening's plan: turnover and the cost model first, then what theory says about how often to trade; the application reads its results through eq-23-partial. Paragraphs: none of its own; the section goes straight to its first subsection.

#### Turnover (305 words)
Says: Turnover is half the L1 distance between drifted and wanted weights, the net return subtracts a per-asset linear charge on the trade, the package's own `turnover()` uses another divisor, and linearity holds at asset-class scale only.
Why here: the plan's first step; no reason beyond the order is stated. eq-23-turnover and eq-23-net are the units of everything measured later.
Paragraphs: code · definition · definition · caveat · code · caveat
Note: opens on a chunk, so the definition appears first as a code comment; the cost model is defined under "Turnover", in the tail of the turnover sentence; the `turnover()` trap is in running prose, not a callout; the function defined here is called once, in the assertion; ¶3 joins two unrelated points (the package divisor, annualization).

#### Costs are not a single number (213 words)
Says: Cost rates differ by asset class, the defaults are arguments rather than constants, and the dearest class to trade is among the three best Sharpe ratios of the sixteen.
Why here: stated in ¶1: the rate in eq-23-net depends on what is traded; needs eq-23-net from the subsection before and tbl-04-moments for the Sharpe rank.
Paragraphs: claim · code · code · result · claim
Note: ¶2's robustness to a factor of two is asserted, not shown, and exercise 1 hands the doubling to the reader; ¶1's examples (high-yield credit, emerging equity) are finer than the class rates the chunk prints; heading is a sentence.

#### What theory says about how often to trade (191 words)
Says: With costs in the objective the optimal policy is a no-trade region around the target or, for a moving target, a partial adjustment toward an aim portfolio at a rate that falls as costs rise.
Why here: the plan's second step; ¶2 says its distinction (a fast target trades partially and often, a stable one drifts) is what the measurements below recover.
Paragraphs: definition · derivation
Note: ¶2 promises that the measurements recover the distinction; the application then reports the optimizers gaining from annual rebalancing at two of three windows and reads the equation as explaining the size of the move, not its sign; heading is a clause.

### Implementation (453 words)
Says: Three package behaviors: a turnover constraint is hard under one backend and a penalty under the other, `Return.portfolio()` back-fills equal weights before the first weight date, and `verbose = TRUE` returns the weights turnover is computed from.
Why here: not stated; the opening's plan goes from the theory to the measurement and does not mention this section. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: nothing here produces what the application reads: no backtest is run, eq-23-net is never applied in code, and `pm_backtest()` is named but not called.

#### A turnover constraint is not a turnover constraint everywhere (127 words)
Says: `turnover_constraint()` is a hard limit under `ROI` and a penalty under `CVXR`, and proportional costs exist only under `ROI`.
Why here: not stated; opens the section with no link back to the theory or forward to the measurements.
Paragraphs: caveat · caveat+c · caveat+c
Note: no code: both behaviors are asserted, and exercise 3 hands the demonstration to the reader; the subsection is one sentence and a callout whose title restates it; heading is a sentence.

#### The accounting that rewrites the start of a backtest (220 words)
Says: `Return.portfolio()` fills the months before the first supplied weights with an equal-weight portfolio and only warns, which in a rolling backtest is the normal case.
Why here: stated in ¶1: it is the obvious way from a weight history to returns, so its behavior should be known before relying on it; ¶3 names `pm_backtest()` as what does the accounting instead.
Paragraphs: caveat · code · result · code · result
Note: the trap gets a subsection of running prose, not a callout; ¶2 quotes the warning in full, and the project renders with `warning: false`; ¶3's line count for `pm_backtest()` is typed.

#### What `verbose = TRUE` returns (103 words)
Says: With `verbose = TRUE` the same call also returns beginning- and end-of-period weights, whose difference is drift turnover, and a per-asset contribution.
Why here: not stated; continues on the objects of the subsection before; ¶3 hands `contribution` to chapter 24, and the band-rule subsection later builds on `EOP.Weight`.
Paragraphs: code · code · code · code · code
Note: the five values the last chunk prints are not read; it recomputes the half-L1 inline rather than calling `turnover()`; the stated portfolio holds one asset, so the positive drift it prints can only come from the back-filled equal-weight months of the subsection before.

### What Rebalancing Costs, Measured (1489 words)
Says: Read from the sweep: rarer rebalancing helps the two rules at every window and moves the optimizers by more in either direction, costs take most from the strategies that optimize most, the width of a band matters more than its trigger, and the linear constant-rate model understates what the optimizers pay.
Why here: stated in the opening's plan as the third step: measure on the runs of chapter 25, computed with and without costs for this purpose. Paragraphs: none of its own; the section goes straight to its first subsection.
Note: the first two subsections read the sweep file, the last two are prose with no code; the section opens on a table, and the chapter's one figure comes in the second subsection.

#### What rebalancing less often does to rules and to optimizers (537 words)
Says: Gross of costs, annual instead of monthly rebalancing raises the Sharpe ratio of equal weighting and inverse volatility at every window, lowers the three optimizers' at sixty months and raises it at the other windows; eq-23-partial is offered as the reason.
Why here: not stated; the first use of the sweep; ¶3 calls on eq-23-partial and ¶4 on the no-trade region of the theory section.
Paragraphs: code · code · code · result · claim · claim
Note: two chunks before any prose; the table is gross, so the subsection measures frequency, not cost, under a section titled for costs; ¶1 is a table key outside the caption; ¶2 carries the whole finding (rules, optimizers at sixty months, the other windows, size against sign) in one paragraph; ¶4's width property of the no-trade region is not stated where the region is defined; heading is a clause.

#### And the cost falls hardest on the strategies that can least afford it (504 words)
Says: Across the nine configurations the Sharpe ratio lost to costs is ordered by how much a strategy optimizes, and maximum Sharpe gives up the largest share of the lowest median gross Sharpe ratio.
Why here: the heading continues the one before with "And"; otherwise not stated; ¶3 turns the result into the case for costs in the objective and points to chapter 18.
Paragraphs: code · code · code · result · result · claim
Note: three chunks before any prose; fig-23-bite is read by its caption alone, no paragraph refers to it; "how much a strategy optimizes" is never defined, the order is a typed list in the assertion; `turnover_objective()` appears here for the first time; ¶3's remedy is named and not run; heading is a sentence.

#### Calendar rules against band rules (259 words)
Says: A band policy trades when a weight leaves its tolerance rather than on a date; the two families fail in opposite ways, and the literature finds the width matters far more than the trigger.
Why here: stated in ¶1: everything measured above rebalances on a calendar, which eq-23-partial suggests is not the natural policy; picks up the no-trade region of the theory and the `EOP.Weight` history of the implementation.
Paragraphs: definition · claim · evidence · caveat
Note: prose only inside the application: no band rule is run on the modeled market, and ¶4 describes the code in words instead of showing it; the material is theory and literature, continuing "What theory says about how often to trade".

#### Where the cost model stops being credible (183 words)
Says: The measured bite is only as good as eq-23-net: linear and symmetric holds for index proxies only, and constant rates make the bite a lower bound for the optimizers.
Why here: stated in ¶1: the numbers above are only as good as eq-23-net, so its two limits are stated after them.
Paragraphs: transition · caveat · caveat
Note: ¶2 repeats ¶4 of "Turnover" with the same two citations, and the first takeaway says it a third time; ¶3's premise that the optimizers' turnover is concentrated in stress episodes is asserted, not measured.

### Key Takeaways (294 words)
Says: Seven bullets: the two linear definitions, per-class costs, the no-trade and partial-adjustment policies, the frequency result, the monotone bite, the two-backend constraint, the back-fill.
Why here: by contract.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: seven against "around five"; the order is theory, application, implementation, not the chapter's; no bullet for band width over trigger, the `turnover()` divisor, the lower-bound reading of the bite or `verbose = TRUE`.

### Exercises (132 words)
Says: Four exercises: doubled cost rates, a flat average rate, a turnover cap under both backends, and the drift of a never-rebalanced equal-weight portfolio.
Why here: by contract.
Paragraphs: exercise · exercise · exercise · exercise
Note: four against "around three"; 1 and 2 ask for net returns under other rates, which the chapter shows no code for (it reads the sweep from a file); 3 is the demonstration the callout leaves out and needs a maximum-Sharpe specification the chapter never builds.

## Chapter 24: Benchmarks and Active Risk (7244 words, 52 paragraphs)
Claim: Whether a portfolio beat its benchmark depends on the benchmark chosen and on what the mandate promised, and whether that was skill cannot be settled at this sample length: against one stated policy the book's minimum-variance manager has a negative information ratio, a positive alpha and a higher Sharpe ratio; a tracking-error budget alone buys dominated portfolios until total risk is bounded as well; the benchmark carries a bet of its own; and the information ratio's interval contains zero.
Question: Did the portfolio beat its benchmark, and if it did, was that skill; cites @grinold1989 for the modern form of the question (the fundamental law) and @grinold2000 for the vocabulary mandates are written in.
Why here: Stated only as a place on the horizon axis of ch. 3: the chapter is about evaluation rather than either horizon, and its one construction, the anchored allocation, is strategic because it tilts from ch. 15's policy. Takes the sixteen series and the hedged series from ch. 2, the dependence finding from ch. 4, the lagged capitalization proxy and the rolling betas from ch. 5, the estimation error from ch. 8, the Merton constants, eq-09-gmv, the frontier, dominance, the variance drag and the minimum-variance portfolio from ch. 9, group constraints from ch. 12, the four sleeves from ch. 15, the equal-weighting question from ch. 21, the back-fill and the turnover formula from ch. 23. Leans forward on ch. 25 five times as if already read: the register that ranks its manager, the rebalancing call, eq-25-brinson, the Ibbotson–Kaplan reminder, the intervals beside every Sharpe ratio. Names nothing a later chapter takes from it; why it stands between ch. 23 and ch. 25 is not stated.
Does: Measure a rebalanced portfolio against a policy with `PerformanceAnalytics` (tracking error, active premium, information ratio, capture ratios, alpha, beta, appraisal ratio, active share) on correctly aligned series; trace the tracking-error frontier in dual form with `PortfolioAnalytics` and under a budget and a total-risk bound with `CVXR`; attribute an active return by sleeve; put an interval on an information ratio.
Order: Opening; theory (the vocabulary and the fundamental law, the budget problem with Roll's solution and Jorion's repair, the Brinson decomposition, the standard error); implementation (the policy and the manager, the two return series, the measures, the package's active constraint, the `CVXR` budget, Jorion's bound); application (attribution by sleeve, two equity benchmarks, the error bar); takeaways; exercises. Deviations: the implementation is 47 percent of the chapter, reads its main results (the manager's three conflicting statistics, the tracking-error frontier, the anchored allocation) and holds its only figure; it turns halfway from measuring an out-of-sample manager to constructing an in-sample tilt without saying so; the implementation and application headings have no paragraph of their own; the application is three topics joined by a title and has no picture; the theory executes one chunk and reads it; six takeaways and four exercises.

### Opening (before the first heading) (292 words)
Says: Whether a portfolio beat its benchmark, and by skill, is the question of the fundamental law and its vocabulary; the chapter defines the vocabulary, implements and extends the measures, attributes the active return and puts an error bar on it.
Why here: Contract position; the sequence sentence gives the order: the vocabulary and what an information ratio estimates, then the measures, the package's gap and the `CVXR` build, then attribution, the benchmark as a bet and the error bar.
Paragraphs: code · claim · method · method · code
Note: No visible packages block: the setup chunk is hidden and the shown chunk loads data. ¶2 is the roadmap and the placement on the horizon axis in two long sentences; for the theory it announces only the vocabulary and the standard error, not Roll's problem or the Brinson decomposition, and it says the budget and an information-ratio objective are both built in `CVXR`.

### Active Weights, Tracking Error, and the Information Ratio — 1269 (466 before the subsections) (? words)
Says: Active weights sum to zero, the tracking error is the volatility of the active return, and the information ratio is the Sharpe ratio with the benchmark in place of the bill; the fundamental law says how much forecasting skill a given ratio needs, and at a breadth of sixteen that is a great deal.
Why here: Stated in the opening: the vocabulary is defined first. Takes ch. 23's turnover formula for active share and sends the beta-adjusted variant to the application, where the beta is treated as an estimate.
Paragraphs: definition · claim · definition
Note: ¶1 is one sentence chain across three numbered equations, ending on two older ratios and four citations; ¶2 does three jobs (the law, the sixteen-class number, Sharpe's arithmetic), and its "thirty times smaller" is typed rather than computed: by eq-24-law the two coefficients differ by √(1000/16), about eight. Active share is defined inline, without a numbered equation, though the implementation computes it.

#### Tracking error as a constraint (321 words)
Says: A mandate sets a tracking-error budget rather than asking for the maximal information ratio; Roll's solution adds the same long-short tilt to any benchmark, so the total portfolio is efficient only if the benchmark was, and the information ratio is constant along the family; Jorion's bound on total risk repairs the first, and the result is a cone program.
Why here: Stated in its first two sentences: mandates give a budget, not a ratio. Needs the Merton constants and eq-09-gmv from ch. 9; hands the cone program to the implementation, on the stated ground that the package lacks it.
Paragraphs: derivation
Note: The whole subsection is one paragraph: a sentence chain of about 320 words across five numbered equations doing six jobs (problem, closed form, the benchmark-free direction, the constant ratio, the repair, the solver class). The derivation is said to be "two lines" and is not shown, with no pointer to the proofs appendix.

#### Where the active return came from (205 words)
Says: The Brinson decomposition splits one period's active return into allocation, selection and an interaction term with no decision behind it; the form used keeps the benchmark's return in the allocation term so that the signs by segment mean something.
Why here: Stated only as sequence: once an active return is earned, the question is which decisions earned it. Why it stands between the budget problem and the standard error is not stated; the application's first subsection applies it.
Paragraphs: definition · definition
Note: ¶2 leans forward on ch. 25 twice (eq-25-brinson, and a reminder "made in" its application) as if already read; the segment benchmark return is written β_s in a chapter whose other betas are regression slopes.

#### What an information ratio is estimating (277 words)
Says: An information ratio has the standard error of a Sharpe ratio, so a ratio of one half needs about sixteen years of monthly data to stand two standard errors from zero, and a beta-adjusted ratio adds the error of the beta.
Why here: Announced in the opening as the theory's second question. Needs ch. 4's dependence finding and ch. 5's rolling betas; the error-bar subsection applies eq-24-se and recomputes the betas. Why it comes after attribution and not after the ratio's definition is not stated.
Paragraphs: definition · code · result
Note: The theory's only chunk, with its result read in place; ¶2 carries the count, two caveats and a forward pointer to the application; ¶1 closes on a four-word verdict sentence that only introduces the chunk. The appraisal ratio, defined in the section's first paragraph as alpha over residual volatility, is said here, and again in the error bar, to divide by a beta.

### Implementation — 3417 (0 before the subsections) (? words)
Says: (heading only)
Why here: Contract position; the opening says the measures, the package's gap and the `CVXR` build follow the theory. Paragraphs: none of its own.
Note: Heading only; six subsections and 47 percent of the chapter. The first three measure a manager out of sample, the last three construct a tilt from full-sample moments, and no sentence marks the turn; the section reads the chapter's main results and holds its only figure.

#### A policy portfolio and a manager (418 words)
Says: The benchmark is a stated four-sleeve policy with equal weights inside each sleeve, and the manager measured against it is the book's rolling long-only minimum-variance portfolio.
Why here: Stated in its first sentence: a benchmark has to be chosen before anything can be measured against it. Needs ch. 15's sleeves and ch. 9's minimum-variance portfolio; takes the manager's rank and its rebalancing call from ch. 25.
Paragraphs: method · code · code · code · method · code
Note: The policy table is shown and no paragraph reads it; the four sleeve weights are typed in code and nowhere argued. The manager is defined through ch. 25 twice (its rank in the register, the call that chapter "dissects"), a chapter not yet reached. ¶1 keeps the policy independent of ch. 15, while the opening and the section's last paragraph call it ch. 15's allocation.

#### Two return series, and the trap between them (259 words)
Says: `Return.portfolio()` back-fills an equally weighted portfolio for the months before the first weight vector, so both series are cut to the months a weight vector precedes and the accounting is asserted by hand.
Why here: Not stated beyond sequence: the weight history has to become a return series before anything is measured. Needs ch. 23's back-fill trap, "met from the other side".
Paragraphs: code · code · caveat+c · code
Note: The two series of the title and the active-return series `a`, the object every later measure is taken on, are built after the callout in a chunk no paragraph reads, and the subsection ends on it.

#### The measures in PerformanceAnalytics (730 words)
Says: Every measure exists as a function of the two series; the default information ratio mixes a compounded numerator with an arithmetic denominator; the manager has a negative information ratio, a positive alpha and appraisal ratio and a higher Sharpe ratio than the policy, because the statistics compare it with different things.
Why here: Stated in the opening (the measures are implemented in `PerformanceAnalytics`); needs the two series just built; its negative ratio is what the attribution and the error bar later work on.
Paragraphs: code · code · caveat+c · result · code · result · code · code · claim · code · claim · code · result
Note: The chapter's central empirical result (¶5, ¶6) is read here, in the implementation; ¶6 calls the benchmark inefficient two subsections before the Jorion table measures it. The `table.CAPM()` table is printed and never referenced by label, its robust rows named only in the caption. ¶3 and ¶6 each end on a sentence that only introduces the next chunk; "a quarter" of the beta is typed beside the computed beta.

#### Active weights in PortfolioAnalytics (512 words)
Says: The package's `active` weight-sum type only sets the sum to zero; with a hand-shifted box and a return target it traces Roll's frontier in dual form, and it cannot express a tracking-error budget, a second quadratic constraint, an information-ratio objective or the benchmark itself.
Why here: Announced in the opening (the package has the constraint but neither budget nor ratio objective); the callout's list is the stated reason for the next subsection, since each missing piece "has to be built".
Paragraphs: caveat · code · method · code · result · caveat+c
Note: Here the chapter turns from measuring the manager to constructing an active portfolio, without a sentence saying so; `mu`, `S` and the helpers every later chunk uses are defined inside the dual chunk, and that they are full-sample moments is said only at the section's end. The callout announces "three things" and lists a fourth.

#### The tracking-error budget, built (786 words)
Says: Roll's problem with a long-only constraint is a few lines of `CVXR`; primal and dual agree, the closed form holds up to the budget at which the first weight reaches zero, and beyond it the information ratio falls with every budget while the gap to the mean-variance frontier measures Roll's inefficiency.
Why here: Stated: the theory handed the cone program to the implementation because the package lacks it, and the callout before it says each missing piece has to be built.
Paragraphs: method · code · method · code · transition · code · result · code · result
Note: The mean-variance frontier that the gap column, the Jorion table and the figure all rest on is built inside a hidden table chunk, and how the gap is computed is said only in the caption. The information-ratio objective the opening announced is not built; the maximal ratio appears as a by-product of the budget problem below the binding budget. ¶5 reads the falling ratio as the transfer coefficient, which no chunk computes.

#### Jorion's repair, and the anchored allocation (709 words)
Says: With total risk bounded at the benchmark's own volatility, a four percent budget buys less active return and a lower information ratio but a higher Sharpe ratio and a portfolio closer to the frontier; this anchored formulation is how a strategic allocation is run in practice, and all of it is in sample.
Why here: Stated in the theory: Jorion's bound repairs the inefficiency, which the previous table has just measured. The title's second half is the construction the opening named as the chapter's one strategic contribution.
Paragraphs: method · code · code · result · code · claim
Note: The chapter's only figure closes the implementation and no sentence reads it: ¶3 mentions it once, to say it is in sample. The anchored allocation, the one construction the opening claims for the chapter, gets this single closing paragraph and never meets the out-of-sample months the manager was measured on. The Jorion table is never referenced by label.

### Attribution, the Benchmark Bet, and the Error Bar — 1748 (0 before the subsections) (? words)
Says: (heading only)
Why here: Contract position; the opening's sequence sentence ends on these three items in this order. Paragraphs: none of its own.
Note: Heading only, and the title is a list: three subsections of similar size that share the manager and the policy but not an argument. No picture opens the application, which has no figure at all.

#### Where the active return came from, by sleeve (624 words)
Says: The manager's shortfall is an allocation result: holding more government bonds and fewer equities than the policy cost more than the whole shortfall and selection gave part of it back; the decomposition sees neither a decision behind the interaction term nor the currency inside each sleeve.
Why here: Not stated beyond the opening's order; needs eq-24-brinson, the sleeves of the policy table, and the weights and active return built in the implementation.
Paragraphs: method · code · code · code · result · caveat
Note: The heading repeats the theory subsection's title with two words added. ¶2 is one block carrying the total, two effects, four weights, the sample explanation and two citations; the Brinson table is referenced by label only from exercise 1; the currency-aware decomposition is named and not run.

#### The benchmark is a bet (559 words)
Says: Equal and capitalization weighting of the same five equity markets are two different yardsticks, with a tracking error against each other larger than most mandates' budgets; the equal-weighted sleeve is a standing underweight of the largest market, so the benchmark carries a bet before the manager makes any.
Why here: Not stated; takes the policy's equity sleeve from the implementation and ch. 5's lagged capitalization weights, uses nothing from the attribution before it, and hands the rebuilt weights to the error bar. Whether the bet is a good one is sent back to ch. 21.
Paragraphs: claim · code · code · code · code · result
Note: Four chunks between two paragraphs. The table's caption describes a last column of overweights by market that the table does not have (the next chunk prints them raw), and exercise 4 cites the table for that bet. The manager is not measured against the second benchmark here, which is left to exercise 4; an information ratio between the two benchmarks is computed and never shown.

#### The error bar (555 words)
Says: Betas move across rolling windows, the manager's beta to the policy among them, so the appraisal ratio divides by a number that is not constant; the information ratio needs no beta, and its interval over the sample contains zero, which is what the standard error says to expect at this length.
Why here: Stated in the theory: the beta numbers are recomputed where the market proxy is rebuilt, so it follows the benchmark subsection; it closes the chapter by applying eq-24-se to the opening's second question.
Paragraphs: claim · code · result · code · result
Note: Two error bars under one heading. The first half recomputes ch. 5's class betas against an equity proxy the manager is never measured against, and the beta the appraisal ratio actually divides by gets one sentence. ¶3 is one block of about 200 words holding the chapter's answer, three justifications and a named test whose outcome ("widens nothing here") no chunk computes.

### Key Takeaways (297 words)
Says: Active weights are long-short and the law prices skill; a budget alone is inefficient and a total-risk bound repairs it; what the package has and lacks; the default information ratio and its disagreement with the Sharpe ratio; the benchmark as a decision; the years an information ratio needs.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets. None covers the attribution result, the back-fill trap, active share or the moving beta behind the appraisal ratio. ¶3 says an information-ratio objective is "a few lines" of `CVXR`, which the chapter never writes; ¶5 cites Cremers–Petajisto, whom the body cites for active share and not for the choice of benchmark; ¶1 and ¶4 each hold two separate points.

### Exercises (175 words)
Says: Four exercises: an equally weighted policy and what it does to the attribution, Jorion's bound at a looser level across three budgets, the information ratio of equal weighting with its interval, and a capitalization-weighted equity sleeve in the policy.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises, each a rerun with one input changed. Exercise 3's second question calls for the test for a difference between two ratios, which the chapter names and does not compute; exercise 4 points to a table column that does not exist; none touches the fundamental law, the dual trace, active share or the capture ratios.

## Chapter 25: Backtesting and Diagnostics (3366 words, 53 paragraphs)
Claim: A backtest is a statistical estimate, not a replay of history: the package's rolling loop completes at full length while storing periods that never solved, those periods fall in the one stretch where the mandate was infeasible, and on the book's register every Sharpe-ratio interval overlaps every other, so what can be kept is what is not an estimate: turnover, cost and the failure count.
Question: Not posed as a question; implied: where the book's out-of-sample lines come from and how much of a backtest to believe; @harvey2015 and @lopezdeprado2018, in the sixth sentence rather than the first two.
Why here: Stated in the first sentence: every construction chapter ends with a line of out-of-sample evidence, and this is where those lines come from. Takes chapter 19's argument against an unchanged world, chapter 4's equity bear market and its non-i.i.d. finding, chapter 23's net figures and per-asset contributions, chapter 24's attribution, chapter 5's lagged market proxy and chapter 2's real-data sleeves; hands the cost of forecast error to chapter 26 and model doubt to chapter 28. Why it closes the part, after rebalancing and benchmarks, is not stated.
Does: Run a rolling backtest with windows of the intended length, find the periods that did not solve with `diagnose_rebalancing()`, carry and count them with `pm_backtest()`, register a parallel backend, put @lo2002's standard error on a Sharpe ratio, and name four kinds of look-ahead.
Order: Opening; theory (the backtest as an estimator, the two window arguments); implementation (the silent failure, its diagnosis, the carry-forward, the parallel backend); application (the register, its error bar, attribution, look-ahead); seven takeaways; four exercises. Deviations: the theory section runs the package and spends three of its four paragraphs on two arguments; the two main headings after it have no paragraph of their own; the implementation ends on run time, with typed timings; the application opens on a table, and the chapter's one figure sits in the implementation; the application's last two subsections are code-free theory placed after the chapter's forward pointer, and neither is in the opening's plan, the takeaways or the exercises; several subsection headings are sentences or imperatives.

### Opening (before the first heading) (188 words)
Says: The out-of-sample lines of the earlier chapters come from here, and the chapter gives its length to what goes wrong, because a backtest is an estimate.
Why here: Contract position; ¶2 says the order is deliberate (failure modes before running, since running is four lines) and ¶3 gives the sequence.
Paragraphs: code · transition · claim · method · code
Note: No question is posed and the first citation arrives in the sixth sentence; no visible packages block; ¶3's plan omits the parallel backend, attribution and look-ahead.

### What a Backtest Estimates (264 words)
Says: A backtest is a loop that may see only the past and its return series is a sample; two arguments of the package's loop decide how much past each step sees.
Why here: Stated in the opening's plan: what a rolling backtest is and what its two window arguments mean come first; eq-25-backtest is what the error bar and the look-ahead taxonomy later refer to.
Paragraphs: definition · code · transition · caveat · definition
Note: The heading names the estimand and three of four paragraphs are about package arguments; no sentence introduces the chunk, and its printed length is read only in the next section; the third-decimal effect is asserted and left to exercise 2.

### Implementation (1089 words)
Says: (heading only)
Why here: Contract position; the opening's plan names the complete-looking run with unsolved periods, not the remedy or the parallel loop. Paragraphs: none of its own.
Note: Heading only; three subsections follow one case (failure, diagnosis, remedy) and the fourth turns to run time.

#### The backtest that looks complete and is not (376 words)
Says: With a required return added, the rebalancing loop returns an object of the right class, length and names in which some periods hold only `NA`, and the functions downstream do not fail on it.
Why here: Stated in the opening's plan as the second step; needs `bt` from the theory section to compare lengths; supplies `bt_mandate` and `n_bad` to the diagnosis.
Paragraphs: method · code · result · code · result · caveat+c · transition · code · result
Note: The chunk tries three functions and ¶6's "neither" reads two; the target's annual size sits in a code comment until the next subsection uses it; the call is wrapped in `suppressWarnings()`, unexplained, above a callout saying nothing warns.

#### Diagnose every period, always (349 words)
Says: The failed periods are not scattered: they fall within one year, beginning in the last month of the equity bear market, so dropping them removes exactly the stretch in which the mandate was impossible.
Why here: Not stated beyond the heading's instruction; needs `bt_mandate` and `n_bad`; ¶1 says the timing is what a count of failures would not have shown.
Paragraphs: code · code · transition · code · result · claim · code
Note: Opens on two chunks; `diagnose_rebalancing()` is never introduced in prose; neither the table nor the figure is referred to in the text, and the figure follows the paragraphs that make its point; the heading is an imperative.

#### What to do about a period that failed (129 words)
Says: No remedy preserves the strategy; carrying the previous weights forward is the least dishonest, and `pm_backtest()` does it, warns and reports the count in every result row.
Why here: Not stated; follows the diagnosis as its remedy; `n_failed` is the column the register table later carries.
Paragraphs: claim · code · claim
Note: `pm_backtest()` and `pm_strategy()` enter with one clause of introduction; the call is wrapped in `suppressWarnings()` one sentence after the prose says it warns; the Sharpe ratio the chunk prints is not read.

#### The parallel loop with no backend (232 words)
Says: The rebalancing function contains a parallel loop and registers no backend, so it runs sequentially; registering eight workers gave identical results 4.5 times faster.
Why here: Not stated; the topic turns from whether the periods solved to how long the loop takes, and the opening's plan does not announce it.
Paragraphs: claim · code · caveat · result · caveat · caveat
Note: The timings are typed, not computed, from a run the chapter does not show; "the same four strategies" has no referent (the register carries five); ¶5 is an aside on a namesake function.

### The Register, and How Much of It to Believe (1423 words)
Says: (heading only)
Why here: Contract position; the opening's plan: assemble the register, then put an error bar on it. Paragraphs: none of its own.
Note: Heading only; the first two subsections carry out the opening's plan, the last two (attribution, look-ahead) are code-free and unannounced.

#### The register, assembled (544 words)
Says: At the sixty-month window the rule that estimates a mean is last and the covariance-only optimizers lead; at every window a rule estimating no mean is ahead of it, by a gap that closes as the window lengthens.
Why here: Stated: every construction chapter contributes one strategy and the table is the book's summary of itself; supplies `reg` and `Tn` to the error bar.
Paragraphs: method · code · code · code · result · claim
Note: ¶3's every-window claim is asserted in code for the best no-mean rule only, and ¶2 has the mean rule off the bottom at 120 months; the register is read from a file written outside the chapter; the `failed` column is never read (zero in every row) and the failing mandate is not among the five.

#### A backtest is a measurement, and it has an error bar (379 words)
Says: With @lo2002's standard error every strategy's Sharpe-ratio interval overlaps every other, so no difference in the register is distinguishable from zero; turnover, cost and the failure count are not estimates and survive.
Why here: Stated in the opening's plan as the last step; needs `reg` and `Tn` from the register, and returns to the theory section's framing of eq-25-backtest as a sample.
Paragraphs: definition · code · result · caveat · claim · claim · transition
Note: ¶2 reads differences off overlapping single intervals, and ¶3 then names the test for a difference without running it; ¶4's failure count is the mandate's, a strategy outside the register; ¶6 is the chapter's send-off, with two subsections still to come.

#### Attribution: where the return came from (255 words)
Says: @brinson1986's decomposition splits an active return into allocation, selection and interaction, the split the book's parts are built on; chapter 24 does the work, and the ninety-percent result answers a narrower question than it is quoted for.
Why here: Not stated why it follows the error bar; ¶1 links it only by contrast (a backtest says what was earned, attribution which decisions earned it), and ¶3 hands the computation back to chapter 24.
Paragraphs: definition · claim · transition · caveat
Note: No code and no number from the modeled market; the decomposition is defined here and the text sends its use to the preceding chapter; absent from the opening's plan, the takeaways and the exercises.

#### A taxonomy of look-ahead (234 words)
Says: Four violations of eq-25-backtest's rule recur (a misaligned window, a universe chosen with hindsight, parameters tuned on the scoring sample, revised vendor data), and only the first is a coding error.
Why here: Not stated; it elaborates the rule the theory section set in eq-25-backtest, and comes after the results and the chapter's forward pointer.
Paragraphs: claim · caveat · caveat · caveat · caveat · claim
Note: Code-free theory as the chapter's last body subsection; "nine configurations" is the first mention of the sweep's size, of which the register subsection showed three windows; absent from the opening's plan, the takeaways and the exercises.

### Key Takeaways (240 words)
Says: Seven bullets: the backtest as an estimate, the inclusive window, the stored failure, the clustered failures, diagnosing and reporting the count, the unregistered backend, and the overlapping intervals against what is not an estimate.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Seven against "around five"; nothing on the register's ranking (the claim the register's ¶3 says the book carries out of the table), on attribution or on look-ahead; bullets 3 to 5 split one finding in three.

### Exercises (128 words)
Says: Four exercises: the mandate at a lower and a higher target, the sixty-one-observation window, the expanding window against the error bar, and a manager's answer to the failed periods.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four against "around three"; all rerun the windows or the mandate; exercise 2 measures the theory section's third-decimal assertion; none touches the register's ranking, attribution or look-ahead.

# Part VIII: Advanced Topics

## Chapter 26: The Cost of Forecast Error (7366 words, 36 paragraphs)
Claim: For a mean-variance investor the cost of a wrong mean forecast is an identity, the squared Mahalanobis distance between forecast and truth (RAFE²/2γ), so the RMSE prices the error in the wrong metric; on the modeled market the RAFE tracks the unconstrained plug-in's Sharpe shortfall where the RMSE does not, which channel costs more depends on the unit, and in the register only the tangency portfolio loses more than a standard error to estimation.
Question: What does an error in a return forecast cost, and in which units should the cost be written; cites Salcher–Stöckl–Hanke in the second sentence for the answer (the optimizer's own risk metric) and Chopra–Ziemba in the third for the older number (means about ten times as costly as variances).
Why here: The text places the chapter on neither side of ch. 3's horizon axis, as measurement for strategic estimates and tactical forecasts alike. It takes the objective from ch. 3, the data from ch. 2, the excess basis and θ from ch. 9, Merton's precision result and the volatility clustering from ch. 4, the three forecasts and the market proxy from ch. 6, eq-08-kz, the inflation, the helper programs, the channel table and the stand-in truth from ch. 8, the term-spread forecast and its tilt from ch. 16, and the register and its standard error from ch. 25. It hands the training of a forecaster on the RAFE to ch. 27 and model error to ch. 28. Why it opens the part is not stated.
Does: Compute the RAFE, the certainty-equivalent loss and the Sharpe shortfall of a forecast or position; score forecasts on rolling train and test windows against the RMSE; split a plug-in rule's expected loss into mean noise, inversion error and amplification and check it by simulation; bound the Sharpe ratio a forecast's R² allows; compute a strategy's perfect-foresight shortfall.
Order: Opening (question, placement and roadmap, data), theory (identity and RAFE, Sharpe bound, RMSE as special case, covariance channel, information bound), implementation (functions and worked box, three forecasts on rolling windows, the covariance channel by simulation, the bound on the term-spread forecast), application (channel shares at three windows, shortfall by episode, the register), takeaways, exercises. Deviations: no main heading has a paragraph of its own; the implementation is 45 percent of the chapter and reads the main results, so the application adds three further cuts and its first subsection re-reads the simulation; the application opens on a table chunk and has no figure; the one figure sits in the implementation and no sentence refers to it; three quantities defined in the theory (C-RAFE, the intermediate nested measures, the multivariate bound) are never computed in the body; the packages block is the hidden `setup` chunk; six takeaways, four exercises.

### Opening (before the first heading) (408 words)
Says: The cost of a forecast error belongs in the investor's own units, the covariance metric of the optimizer, and the chapter derives that measure and applies it to the sixteen classes.
Why here: Contract position; the text places the chapter on neither side of ch. 3's horizon axis and gives the roadmap as a sequence without reasons.
Paragraphs: code · claim · method · method · code
Note: ¶1 cites nine sources in 175 words and already states the chapter's result (the loss is an identity); ¶2's roadmap is one sentence of about ninety words; the packages block is the hidden `setup` chunk and the visible chunk computes the stand-in truth.

### The Loss in Risk Units (1585 words)
Says: In risk units the certainty-equivalent loss of any position is a squared distance to the optimum, and the RAFE, the Sharpe bound, the RMSE as a degenerate metric, the covariance channel and an information ceiling are read off it.
Why here: Stated in the roadmap only as "first"; each function of the implementation carries an equation number from here. Paragraphs: none before the first subsection.
Note: Eight paragraphs carry 1,585 words and twelve numbered displays, four of them running through two or three displays; no code; nine of the section's citations are to the two Salcher–Stöckl–Hanke papers.

#### The certainty equivalent and the plug-in loss (393 words)
Says: Whitening positions and means by the square root of Σ turns the loss of any position into a squared distance, and for a plug-in position with Σ known that distance is the RAFE, the Mahalanobis distance between forecast and truth.
Why here: Roadmap: the identity comes first and the rest is read off it; needs ch. 3's objective and the θ of eq-09-tangency.
Paragraphs: definition · derivation · derivation
Note: ¶3 is 250 words around one display and does five jobs (attribution, the plug-in step, the definition of the RAFE, its three readings with the Michaud and Best–Grauer mechanism, the N/T price tied to eq-08-kz and Merton); the chapter's central term is defined in a "where" clause after its equation.

#### From the certainty equivalent to the Sharpe ratio (197 words)
Says: A Sharpe-ratio investor sees only the angle between forecast and truth in risk units, so the shortfall is θ(1 − cos φ) and is bounded by c₀ times the RAFE.
Why here: First sentence: direction without length turns the identity into a bound; needs eq-26-rafe.
Paragraphs: derivation
Note: The subsection is one sentence chain around two displays; the reason for the case c₀ = 1 follows the display that states it; the squared-Sharpe decomposition arrives in the last sentence and is not used again.

#### The RMSE as a special case (283 words)
Says: The RMSE is the last of a nested sequence of simplifications of Σ, each discarding something the optimizer uses, and the cited correlations with the shortfall fall along the sequence.
Why here: First sentence: the usual score replaces Σ in eq-26-rafe by something simpler; closes on ch. 27, which draws the consequence for training.
Paragraphs: definition · evidence
Note: ¶2 joins the reading of the sequence, the cited numbers, two further sources and the forward pointer in 199 words; the three intermediate measures are defined here and computed only in exercise 2.

#### The covariance channel (419 words)
Says: With Σ estimated a second error enters, bounded path by path by θ times the C-RAFE, and in expectation the loss splits into mean noise, inversion error and noise amplified by the inverse.
Why here: First clause: Σ is now estimated too, which lifts the assumption held since eq-26-rafe; it derives the eq-08-kz that ch. 8 only quoted.
Paragraphs: derivation
Note: One unbroken paragraph of 415 words through three displays: a pathwise bound, an expectation, the reading of three terms, and three caveats (ch. 8's substitution design misses the third term, long-only caps all three, heavy tails raise the constants); the C-RAFE is defined here and computed only in exercise 1.

#### An upper bound from the forecast's information (286 words)
Says: A forecast with explanatory power R² allows at most a conditional squared Sharpe ratio of (S₀² + R²)/(1 − R²), with a multivariate version, tight only for the unconstrained conditional tangency position.
Why here: Stated in its first two sentences: the measures above price a forecast that exists, a bound prices one that could.
Paragraphs: derivation
Note: One paragraph of 278 words through two displays; the multivariate bound is stated and never evaluated in the chapter; the closing caveat (the sample bound inherits eq-08-inflation) does not return where the bound is computed.

### Measuring the Error in the Investor's Units (3280 words)
Says: The measures are a few lines of R; on rolling windows the RAFE tracks the unconstrained plug-in's shortfall where the RMSE does not, simulation confirms the three-term split, and the term-spread forecast's bound lies close to what its tilt earned.
Why here: The roadmap's second step: implement the measures, score three forecasts, check the covariance channel by simulation, bound the term-spread forecast. Paragraphs: none before the first subsection.
Note: 45 percent of the chapter, about 2,000 of its 3,280 words in fourteen chunks around ten paragraphs; each of its last three subsections reads its own result, so the chapter's headline findings are stated here, not in the application.

#### Two functions and a worked box (629 words)
Says: The helper programs are repeated from ch. 8 and ch. 6, four functions implement eq-26-rafe, eq-26-loss-identity and eq-26-cos, and a collapsed box substitutes the first sixty months into the formulas.
Why here: not stated beyond "a few lines each"; every later chunk calls these functions.
Paragraphs: method · code · code · code · example+c
Note: The heading counts two functions and the chunks define eight; the four measures are explained only in code comments; in the box the check chunk precedes the substituted formula, and c₀·RAFE is printed as the RAFE itself without saying which case of eq-26-bound holds.

#### Three forecasts of the mean on rolling windows (1337 words)
Says: On sixty-month training and test windows the RAFE correlates with the unconstrained plug-in's shortfall and the RMSE hardly does; for the long-only tangency portfolio only the RAFE in the investor's own estimated metric keeps its lead.
Why here: Stated: ch. 6 re-estimated these three vectors and ch. 8 measured the gap of portfolios built on the first; here the forecasts themselves are scored.
Paragraphs: method · code · method · code · result · code · code · code · code · result
Note: ¶2 sets every design choice (window lengths, three measures, two rules, the shortfall's benchmark) in one block of 177 words; ¶4 reads the table in 226 words and ends on a finding it says the cited paper does not report; the figure is drawn and never referred to; the truth here is the test window's moments, not the full-sample moments the opening named; the market-proxy chunk repeats ch. 6's data preparation in thirty lines for one of three forecasts.

#### The covariance channel by simulation (637 words)
Says: Three hundred normal draws per window length reproduce eq-26-kz-split to the second decimal; at sixty months the amplification term exceeds the mean channel in certainty-equivalent units, while in Sharpe units the mean channel leads.
Why here: Stated: eq-26-kz-split is an expectation under normality and ch. 8 measured the channels by substitution under a long-only rule; the last sentence says the application returns to it.
Paragraphs: method · code · code · code · result
Note: ¶2 reads one row of six and does not cite the table's label; the unit dependence on which the application's first subsection rests is already stated here.

#### The bound on the term-spread forecast (668 words)
Says: Treated as one asset, the equal-weight policy's term-spread forecast has a small out-of-sample R², the bound allows a timer a few hundredths of Sharpe ratio above the policy, and ch. 16's tilt realized a gain inside it.
Why here: Stated: ch. 16 found one signal that survived out of sample and built a tilt on it; eq-26-bound1 says what the forecast could have earned at most.
Paragraphs: method · code · code · result
Note: ¶2 is 227 words around one display; it sets the tilt against a ceiling the same paragraph calls right for a timer and loose for the tilt, and says the multivariate ceiling is higher without computing it; the per-series R² printed by `term` is not read; the `tilt` chunk has no prose of its own.

### Which Channel Costs More (1571 words)
Says: Which channel costs more depends on the unit; the shortfall is largest for windows ending in the credit crisis (unconstrained) or the rates shock (long only); and in the register only the tangency portfolio's shortfall exceeds a standard error.
Why here: The roadmap's last step: which channel costs more on this market, where the cost is largest, whether the register ranks by how much it estimates. Paragraphs: none before the first subsection.
Note: The heading is phrased as a question and names only the first of three subsections; the section opens on a table chunk and has no figure; none of its three tables is cited by label.

#### The two channels at 36, 60 and 120 months (323 words)
Says: In certainty-equivalent units the covariance channel is the larger at thirty-six and sixty months and the smaller at 120; in Sharpe units the mean channel is the larger at every window, which is how Chopra–Ziemba's ten-to-one is read.
Why here: The simulation subsection said the application returns to this; the table is that simulation filtered to the register's three windows.
Paragraphs: code · result
Note: One paragraph after a table with no introducing prose and no new computation; the opening's Chopra–Ziemba number is resolved here; that the certainty-equivalent share comes from the formula and the Sharpe share from the simulation is said only in the caption.

#### Where the shortfall is largest (535 words)
Says: Sorted by the episode a sixty-month window ends in, the unconstrained rule is worst after the credit crisis and the long-only rule after the rates shock, and equal RAFEs cost different shortfalls because the shortfall reads the angle.
Why here: Stated: the rolling test window cannot reach the last two episodes; against the full-sample truth every estimation window can be scored.
Paragraphs: method · code · code · code · result
Note: The truth changes back from the test window's moments to the full sample, and the text says so; ¶2 reads three episodes with two different explanations (exclusion by sign, length against angle) in 207 words; the liquidity shock is in the table and not read.

#### The register, ranked by what it estimates (707 words)
Says: Ordered by how much they estimate, the register's five strategies have a perfect-foresight shortfall of zero for equal weighting and the largest for the tangency portfolio, with minimum CVaR negative because its benchmark is not a Sharpe ceiling.
Why here: not stated beyond the roadmap; it ties the measure to ch. 25's register and ch. 8's gap figure and closes on ch. 27 and ch. 28.
Paragraphs: method · code · code · code · result
Note: ¶2 is 259 words: four strategies read, the exception explained, the standard-error comparison, and both forward pointers in its last sentence; "shortfall" here has its third ceiling (own perfect foresight over all out-of-sample months) after θ under the truth and the test window's; no error measure is computed in this subsection.

### Key Takeaways (266 words)
Says: The identity, the shortfall bound and the RMSE as special case with the pooled correlations, the long-only metric, the three-term covariance channel and its dependence on the unit, the R² ceiling on the term spread, and the register's shortfalls.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway · takeaway
Note: Six bullets; ¶2 holds three statements; ¶4 counts the mean's noise N/T as a term of the covariance channel, where the theory calls it the mean channel and the application's table leaves it out of the covariance share; nothing on where the shortfall is largest.

### Exercises (199 words)
Says: Four exercises: the minimum-variance rule scored by RAFE and C-RAFE, the two intermediate measures, the window lengths at which the channels cross, and the bound for two values of R².
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises; 1 and 2 are the only places the C-RAFE and the intermediate nested measures are computed; none touches the episodes or the register.

## Chapter 27: Decision-Aware Forecasting (7998 words, 44 paragraphs)
Claim: A mean-variance investor pays for forecast error in the metric Σ⁻¹ and not in squared error, so a forecaster trained on mean squared error is trained on the wrong loss; of three corrections, shrinking the mean in risk units adds the most Sharpe ratio on the modeled market, acting on fewer forecast dimensions adds nothing beyond what the forecast was already worth, and tuning on the certainty equivalent gives a worse forecast with a better portfolio inside sampling error, while none of the three beats the rules that use no mean.
Question: Should a return forecaster be trained on mean squared error at all; cites Stöckl and Hanke in the second sentence for the closed-form answer (the certainty equivalent lost is the error in risk units, correctable after the fact) and Elmachtoub and Grigas for the general operations-research form (train on the regret of the decision).
Why here: The text says the chapter sits on neither side of chapter 3's horizon axis: it is about estimation, and the corrections apply to a long-run and to a conditional mean alike. It takes the risk-adjusted forecast error and its Sharpe-gap bound from chapter 26 as given, the investor and the certainty equivalent from chapter 3, Bayes-Stein from chapter 6, the condition number from chapter 7, the Best–Grauer mechanism, the N/T inflation, the plug-in rule and the covariance channel from chapter 8, the minimum-variance formula from chapter 9, the term-spread forecast, the tilt and the elastic net from chapter 16, the parametric policy from chapter 18, per-class costs from chapter 23 and the register from chapter 25. It hands to chapter 28 the case in which the model behind the loss is itself in doubt. That it follows chapter 26 is implied by that borrowing; why it sits in this part is not stated.
Does: Price a forecast error in the investor's units; correct a sample mean toward a target with a constant that needs no tuning; act on a forecast at a chosen granularity, with the number of groups read from an information coefficient; tune a forecaster's penalty on the certainty equivalent of the tilt it implies; score all of it on the register's months.
Order: Opening (question, placement and roadmap, data), theory (the two losses, then one subsection per answer in the order after the forecast, between forecast and decision, inside the training loop), implementation (the same three answers in the same order, the first over two subsections), application (one scoreboard figure and three paragraphs), takeaways, exercises. Deviations: neither the theory nor the implementation heading has a paragraph of its own; all four tables are read in the implementation, including the one the text calls the result the chapter was built to show, so the application computes nothing new and re-reads those numbers from one figure; the theory ends on the failure conditions of all three answers, placed under the third answer's heading; the packages block is the hidden setup chunk and the first visible chunk loads data; no callout and no `PortfolioAnalytics` call anywhere; five takeaways, four exercises.

### Opening (before the first heading) (283 words)
Says: A forecast should be judged in the units of the decision it feeds; for a mean-variance investor those units are known in closed form, and the chapter derives three answers to the mismatch, implements each on the sixteen classes and asks which buys most.
Why here: Contract position; ¶2 gives the order (derive, implement, compare) and places the chapter off the horizon axis as an estimation chapter.
Paragraphs: code · claim · method · code
Note: ¶1 gives the answer to its own question in its second sentence; "risk units" is used here and defined two subsections later; γ = 5 is set in code and never argued for in the prose.

### Two Losses for One Forecast (2151 words)
Says: (heading only)
Why here: Stated in the opening: the mismatch between the statistical and the decision loss is derived first, with the three answers to it. Paragraphs: none of its own.
Note: Heading only; four subsections without an introducing paragraph; the three-answer roadmap that orders them sits in the last sentence of the first subsection.

#### The statistical loss and the decision loss (515 words)
Says: Squared error and the certainty-equivalent loss are quadratic forms in the same error under the identity and under Σ⁻¹; they rank forecasts differently, by up to the condition number, and a forecaster trained on the first can be reconciled with the second in three places.
Why here: Needs chapter 3's investor and chapter 26's risk-adjusted error, which the text says it takes from there; its last sentence names the three places that the next three subsections take up in that order.
Paragraphs: derivation · definition · derivation · code · result
Note: ¶4 does four jobs: it reads the number, gives the mechanism, gives the lineage and announces the three answers, which is the roadmap for the rest of the chapter; RAFE appears in eq-27-decision one paragraph before it is named.

#### Correcting the mean in risk units (768 words)
Says: In risk units the sample mean's expected squared error is N/T; shrinking its deviation from a pre-set target by a James-Stein factor has an exact risk, minimized by a constant that depends on N, T and the target's rank alone, and for the grand mean the corrected mean dominates the sample mean whenever T exceeds N.
Why here: Stated at the end of the previous subsection: the first of the three places, after the forecast, with the model left alone. The implementation codes eq-27-corrector and eq-27-constant directly, and the next subsection sets its hard reduction against this soft one.
Paragraphs: derivation · claim · definition · derivation · evidence
Note: ¶4 runs through two numbered displays and holds the derivation, the optimal constant and the dominance result in one paragraph; ¶5 is two paragraphs in one, the lineage and then three limits of the theorem, and those limits are what the implementation later runs into.

#### Using less of the forecast (431 words)
Says: Acting on a k-dimensional projection of the forecast loses the signal discarded plus k/T of noise retained, so a dimension is worth acting on only if its squared Sharpe ratio exceeds 1/T; the familiar rules are fixed cells of a granularity grid, and the number of rank groups worth forming follows from the information coefficient by a cube-root rule.
Why here: The second of the three places, between forecast and decision; the text says it starts from the same identity and sets hard reduction against the shrinkage of the previous subsection. eq-27-hard and eq-27-groups are what the granularity experiment implements.
Paragraphs: derivation · claim · derivation · claim
Note: The truth in risk units is introduced a second time under new symbols (a, b̂, η), one subsection after m and m̂; ¶2 holds three points (the threshold, soft against hard, the grid of rules) and eight citations; the grid is given in one sentence, with no table or figure.

#### The decision loss inside the training loop (437 words)
Says: The decision-aware estimator maximizes the sample certainty equivalent of the portfolio the forecast implies; with the plug-in map and a known Σ it is least squares reweighted by Σ⁻¹, and without the closed form it still applies to any utility, map and model; what it loses is precision, and each of the three answers has a condition under which it does not help.
Why here: The third of the three places, inside the training loop; the text ties it back to chapter 18's policy as the special case and to the first answer through eq-27-gls. Its closing paragraph sets up the implementation by saying where each answer should fail.
Paragraphs: definition · caveat
Note: ¶1 runs through two displays and does four things (defines the estimator, names the lineage, derives the equivalence, claims generality); ¶2 closes the whole theory section with the failure conditions of all three answers under the third answer's heading, and ends on a forward pointer that one answer will partly fail without saying which.

### Three Corrections on Sixteen Classes (4069 words)
Says: (heading only)
Why here: Stated in the opening: each answer is implemented on the sixteen class series in excess of the bill and scored out of sample from the first month of model year 11. Paragraphs: none of its own.
Note: Heading only; four subsections for three answers, the first answer taking two; every subsection also reads its own results table, so the section is implementation and results together and is half the chapter.

#### The corrected mean in a few lines (704 words)
Says: The corrector is one short function; on the full sample the factor keeps only part of each deviation from the grand mean, on shorter windows the constant rises above its oracle value, and on a share of the sixty-month windows the positive part binds and the deviations are removed.
Why here: Stated in its first sentence: the two equations of the theory are a function of five inputs. The function and the Bayes-Stein copy are what the backtest of the next subsection calls.
Paragraphs: code · code · example · code · result · code · result
Note: The worked formula follows the chunk that computed its numbers; the exact risk, the theory's central result, is not checked in the chapter and goes to exercise 2; ¶2's last sentence is a transition to the Bayes-Stein chunk, attached to the worked example.

#### Four means in the tangency rule (1010 words)
Says: In the long-only tangency rule on rolling windows the Sharpe ratio rises from the sample mean to Bayes-Stein to the corrected mean at both window lengths and stays below minimum variance, onto which the corrected rule collapses in a share of windows; by certainty equivalent equal weighting leads, because a fully invested tangency portfolio carries less risk than this investor would choose.
Why here: Stated: the correction is scored where chapter 8 scored the sample mean, with that chapter's quadratic program and one covariance matrix for every mean, so that chapter 25's register is reproduced.
Paragraphs: method · code · code · code · code · code · result · result
Note: The heading counts four means, the table scores three, and the fourth, the zero target, appears only as an assertion; the position the theorem prices, unconstrained and of its own length, is never scored in the chapter, only in exercise 1; the Sharpe standard error the next two subsections quote is computed in this subsection's hidden chunk.

#### Granularity on the term-spread tilt (1369 words)
Says: Acted on at every magnitude, in three rank groups, by sign only or in the number of groups the rule picks, the term-spread forecast earns the same small gain over equal weighting; the cells differ by far less than the Sharpe ratio's standard error, and the text reads this as the theory's second failure condition: a near-common shift leaves granularity nothing to decide.
Why here: Stated: the second answer needs a forecast with a cross-section, and the term spread is the one forecast of chapter 16 that survived out of sample. The six other predictors are built here for the next subsection.
Paragraphs: method · code · method · code · method · code · code · code · result
Note: ¶4 is one paragraph with six points (gain over equal weighting, no difference between cells, the rule's choice, fitted against realized coefficient, turnover, the theoretical reading); three chunks stand between the last method paragraph and it; the longest subsection, about two thirds of it code.

#### Tuning the elastic net on the certainty equivalent (986 words)
Says: On the same folds and penalty grid, cross-validated squared error picks the null model in most years while the certainty-equivalent criterion picks a smaller and unstable penalty; out of sample the decision-tuned net has the worse squared error and the better portfolio, at several times the turnover and with a Sharpe gain inside its standard error.
Why here: Stated: the third answer is tried on the forecaster that lost in chapter 16. It reuses the predictors, the tilt and the scoring function built in the previous subsection, and the text calls its table the result the chapter was built to show.
Paragraphs: method · code · code · result · code · code · code · result
Note: ¶3 opens by naming its table the result the chapter was built to show, and it stands at the end of the implementation, as the fourth of four parallel subsections, not in the application; the tilt on the historical mean, the table's third row, is not read in the prose.

### What Each Answer Buys (838 words)
Says: On one scoreboard with the register, the corrected mean adds the most Sharpe ratio to the rule it corrects and the training loop the most certainty equivalent, while granularity adds nothing; each fails somewhere and none beats the rules that use no mean, so the correction recovers part of the tangency rule's distance to minimum variance and the rest is the covariance matrix's share.
Why here: Stated in the opening as the last step: which of the three buys most on this market, and where each fails. The last paragraph hands the doubt about the model behind the loss to chapter 28.
Paragraphs: code · code · result · caveat · claim
Note: The section opens with the figure and computes nothing new: the figure collects numbers already read in the implementation and the three paragraphs regroup them by answer; the three gains are measured over three different base rules; ¶2 is where the theory's forward pointer is redeemed by name; ¶3 states for the first time, without a number of its own, that the level direction carries most of what there is to earn, and ends on the transition to chapter 28.

### Key Takeaways (294 words)
Says: The Σ⁻¹ metric and its cost ratio; the corrected mean, its constant and its backtest; the 1/T price per dimension and the granularity result; the certainty-equivalent tuning result; and that no answer beats the rules without a mean.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: One bullet per step of the argument, in the chapter's order, the first four each pairing a theory statement with its number and its citations; the reach of the third answer beyond mean-variance does not return.

### Exercises (230 words)
Says: Four exercises: the zero target and the unconstrained position, the exact risk by simulation and the constant in the backtest, a doubled band, and the realized information coefficient.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises, two on each of the first two answers and none on the training loop; exercises 1 and 2 carry the two checks the prose defers (the unconstrained position, the exact risk).

## Chapter 28: Robustness and Model Uncertainty (7385 words, 50 paragraphs)
Claim: Guarding against a set of models by its worst case comes out as an increase in effective risk aversion, a shrinkage of the portfolio toward minimum variance in proportion to the size of the set; because that set is a confidence region, on sixty months of sixteen classes it is wide enough at even odds to go most of the way, and out of sample the two maxmin portfolios improve on the tangency portfolio without reaching minimum variance, while resampling buys nothing.
Question: What should an investor do when the doubt is about whether the model behind μ and Σ is the right one, not about their values; cites Garlappi, Uppal and Wang for posing it for the mean-variance investor and Gilboa and Schmeidler for the decision rule, both in the second sentence.
Why here: Stated for the axis, not for the position: the answer is a shrinkage toward minimum variance, so the chapter is strategic in chapter 3's sense. Takes the standard error and Bayes–Stein from chapter 6, the covariance error from chapter 7, the plug-in rule, the quadratic programs and the register reading from chapter 8, the frontier scalars, the tangency and minimum-variance portfolios and the block bootstrap from chapter 9, the cone solvers and `random_portfolios()` as a search from chapter 13, the single factor and turbulence from chapter 5, the left tails from chapter 4, the register from chapter 25. Its relation to its two neighbors is stated: chapter 26 prices the error, chapter 27 corrects the forecast, this one leaves the forecast alone and changes the decision. It is the last chapter; it points forward only to two appendices (the solver matrix, scenario analysis), and that it closes the book, or why, is not stated.
Does: Derive and check the multi-prior portfolio in closed form and as a long-only fixed point, compute the worst-case tilt and the robust portfolio over a Kullback–Leibler ball, build a block-bootstrap resampled frontier, sample the feasible set three ways and audit the draws against a factor-exposure bound, and score the rules out of sample with the register's accounting.
Order: Opening; theory in five subsections (the two uncertainties, the multi-prior portfolio, robust optimization in general, the Kullback–Leibler ball, resampling); implementation in four (resampled frontier, random portfolios with the callout, multi-prior, Kullback–Leibler ball); application undivided; takeaways; exercises. Deviations: the theory heading has no paragraph of its own; the implementation takes the three derived devices in the reverse of the theory's order and adds random portfolios, which have no theory subsection and no row in the application; robust optimization over other sets and smooth ambiguity have theory and no implementation; two subsection titles occur twice, once in the theory and once in the implementation; all three figures and every in-sample result sit in the implementation, so the application is a method paragraph, one table and three paragraphs reading it; five takeaways, four exercises.

### Opening (before the first heading) (264 words)
Says: Doubt about the model, as against doubt about its inputs, is met by a worst case over the models the data cannot rule out, which turns out to be a shrinkage toward minimum variance; the chapter derives it, implements it and tests it.
Why here: Contract position; ¶2 gives the order: separate the two uncertainties and derive three devices, implement four on the sixteen classes, run the robust portfolios out of sample against the register.
Paragraphs: code · claim · method · code
Note: No visible packages block: the setup chunk is hidden and the shown chunk loads data. ¶1 gives the chapter's answer before any method; ¶2 is one sentence that derives three devices and implements "all four", the fourth being random portfolios.

### Parameter Uncertainty and Model Uncertainty — 1745 (0 before the subsections) (? words)
Says: (heading only)
Why here: Stated in the opening: the two uncertainties are separated first and the devices derived before any code. Paragraphs: none of its own.
Note: Heading only; five subsections without an introducing paragraph. The heading names the first subsection's distinction; the other four are devices, sorted by that distinction as they come.

#### Two kinds of not knowing (326 words)
Says: Parameter uncertainty is a distribution over numbers inside a model taken as true and is treated by averaging; model uncertainty is a set of models with no distribution over it and is treated by the worst case.
Why here: Stated: every chapter since chapter 6 has treated the inputs as estimates, and all of that is named parameter uncertainty here; ¶3 says what follows derives what the set's boundary does to the weights.
Paragraphs: definition · definition · transition
Note: ¶1 does three jobs (the recap of five chapters, the definition, the Bayesian remedy with three citations); smooth ambiguity, the case between the average and the worst case, is defined only at the end of the Kullback–Leibler subsection.

#### The multi-prior portfolio (654 words)
Says: With the ambiguity in the mean and the set a confidence ellipsoid, the worst case is a linear penalty on volatility, so the investor scales the tangency portfolio down or, fully invested, holds the mean-variance portfolio of a higher effective risk aversion that converges to minimum variance; the radius is a confidence level.
Why here: It is the answer the opening names and what ¶3 before it announces; needs chapter 3's quadratic utility, chapter 9's tangency, frontier scalars and minimum variance, chapter 6's standard error and Bayes–Stein; the next two subsections each open by generalizing it.
Paragraphs: definition · derivation · derivation · derivation · claim · derivation · claim · definition · claim
Note: ¶2, ¶4 and ¶9 begin mid-sentence after a display equation; ¶7 carries seven points; the reclassification of the opening's answer as a parameter-uncertainty device arrives in ¶9, inside the paragraph on calibrating the radius.

#### Robust optimization over a set (143 words)
Says: The multi-prior inner problem is one case of robust optimization, in which the choice of uncertainty set decides the penalty: a box is a per-asset haircut, an ellipsoid a volatility penalty.
Why here: Stated in its first sentence: the problem just solved is one instance of the general method; nothing in the implementation or the application builds on it.
Paragraphs: definition
Note: One paragraph, a survey with two citations and pointers to chapter 13 and two appendices; the general case follows its special case and is never implemented.

#### The Kullback–Leibler ball (428 words)
Says: Widening the set to every distribution within a fixed relative entropy of a reference lets the worst case reweight the sample toward the portfolio's bad months; the result reads as the risk aversion of an exponential-utility investor, and with a Gaussian reference restricted to mean shifts it is the ellipsoid with ε = 2η.
Why here: Stated in its first sentence: a worst case over means leaves every other feature of the model intact; it relates itself back to the ellipsoid and forward to the implementation, which is to show what the extra room buys.
Paragraphs: definition · derivation · claim · claim · definition
Note: ¶4 does four jobs (the certainty-equivalent reading, the link back to γ*, the equivalence of the two sets, the calibration of η); ¶5 is a third model under the ball's heading, said to be traced through eq-28-epsilon, and is not implemented.

#### Resampling, and what kind of uncertainty it treats (187 words)
Says: Michaud's resampled frontier averages frontier weights rank by rank over draws of the inputs; it averages over parameter draws from one model, so it is a parameter-uncertainty device, and by Scherer's critique not the Bayesian answer either.
Why here: Not stated why last; the heading files it under the first subsection's distinction, and its closing sentence says that measuring it beside the maxmin rules shows averaging against guarding.
Paragraphs: definition · claim
Note: ¶2 opens mid-sentence with the definition of k and then holds the property, the classification, the critique and the forward pointer; random portfolios, the fourth device of the implementation, have no subsection here.

### Four Robustifications on the Sixteen Classes — 3907 (332 before the subsections) (? words)
Says: The quadratic programs are chapter 8's, written out so that the loops run fast, with the `PortfolioAnalytics` specification as the check, at γ = 3 and annualized.
Why here: Stated in the opening: all four devices are implemented on the sixteen classes; the order of the four subsections is not stated.
Paragraphs: method · code
Note: The heading counts four robustifications and the subsections run resampling, random portfolios, multi-prior, ball: the theory's order reversed, plus a device its own heading calls a picture. γ = 3 rests on a package default. Each subsection also reads its in-sample results.

#### The resampled frontier (676 words)
Says: Averaged over two hundred block-bootstrap draws, the resampled tangency is more diversified than the sample tangency, pays for it in in-sample Sharpe ratio, and lies on a frontier dominated at the moments it was averaged under.
Why here: Not stated why first, the theory having treated resampling last; ¶1 ties the bootstrap to chapter 9's, and ¶2 ends by handing the out-of-sample question to the application.
Paragraphs: method · code · code · code · code · result
Note: Four chunks separate the two paragraphs; ¶2 reads the figure, the table and the hidden chunk at once, in seven points; the figure caption gives the result before the prose does; the comparison that the draws sit no closer to the average is the one statement the hidden chunk does not assert.

#### Random portfolios as a picture of the feasible set — 1116 (372 in the callout) (? words)
Says: Three generators sample the same long-only set differently and none comes near its edge, so random portfolios show the set and do not search it; and they ignore a factor-exposure bound at generation and in the objective.
Why here: Not stated beyond the contrast with chapter 13, where the same function was a solver; the opening announced it as the fourth device; no theory subsection precedes it and the application does not use it.
Paragraphs: method · code · code · code · code · code · result · definition+c · code · code · code · caveat+c
Note: The longest implementation subsection belongs to the one device with no theory and no part in the application; a third of it is the callout, which builds its own case (nothing else in the chapter sets a factor-exposure bound) and returns in takeaway 5 and exercise 3.

#### The multi-prior portfolio (1082 words)
Says: The derived closed form matches a direct maximization and is kept over `glPF()`; at even odds the speculative part is already cut to about a fifth; long-only, the fixed point walks from an all-equity plug-in portfolio toward minimum variance; a turbulence-driven radius is largely a volatility-timing rule.
Why here: ¶1 says the theory's closed forms are to be written out and checked; why it follows random portfolios is not stated; the ball's subsection reads itself against these results, and the application calls `eps_of()` and `mp_long_only()`.
Paragraphs: method · code · code · result · method · code · code · code · result · method · code · code · result
Note: Three topics under one heading (the closed-form check, the long-only path, the time-varying radius); the third has no theory subsection, uses the risk-free form while all else is fully invested, and returns nowhere later; the `glPF()` disagreement is in running prose, not in a callout.

#### The Kullback–Leibler ball (701 words)
Says: On the empirical distribution the ball also moves the portfolio toward minimum variance as its radius grows, but the mark-down follows each class's covariance with the portfolio's worst months; the application's radius is set at η = ε/2 so that the two sets differ only in shape.
Why here: It reads its results against the ellipsoid's, so it follows the multi-prior subsection; its last sentence sets the radius the application uses.
Paragraphs: method · code · code · code · result
Note: Two paragraphs around one long routine whose damping and tolerances live in code only; ¶2 carries six points, and its claim about the longest left tails is handed to exercise 4 and then stated as a finding in takeaway 3.

### Robustness Out of Sample (992 words)
Says: On sixty-month windows from model year 11 the two maxmin portfolios improve on the tangency portfolio in Sharpe ratio, turnover and drawdown without reaching minimum variance, the resampled tangency improves on nothing, and equal weighting has the highest certainty equivalent; the worst case bought what a higher risk aversion buys.
Why here: Stated in the opening and prepared by the closing sentences of the resampled and ball subsections; needs every function of the implementation and chapter 25's register for the accounting.
Paragraphs: method · code · code · code · result · result · claim
Note: No subsection and no figure: a method paragraph, one table, three paragraphs; ¶3 reads all six rows in one paragraph; the six are named only in the code and the caption, two of them rules that estimate no mean; random portfolios are absent.

### Key Takeaways (217 words)
Says: The two uncertainties and their treatments, the multi-prior portfolio as higher risk aversion with a confidence-level radius, the ball as a reweighting toward bad months, resampling as averaging that is dominated out of sample, and random portfolios as a picture that ignores factor exposure.
Why here: Contract position.
Paragraphs: takeaway · takeaway · takeaway · takeaway · takeaway
Note: Five bullets: three restate the theory, one the callout; none gives the out-of-sample result for the two maxmin portfolios, minimum variance or equal weighting, nor the time-varying radius; bullet 3's tail claim rests on exercise 4.

### Exercises (219 words)
Says: Four exercises: the multi-prior portfolio at three confidence levels out of sample, the right end of the resampled frontier, the callout's trap repaired by filtering, and the tilt against the ellipsoid class by class.
Why here: Contract position.
Paragraphs: exercise · exercise · exercise · exercise
Note: Four exercises, one per implemented device; none asks for a derivation; exercise 4 is the one the ball's implementation and takeaway 3 lean on for the tail claim.
