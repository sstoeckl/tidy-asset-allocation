---
file: chapters/02-notation-and-data.qmd
title: Notation and Data
part: Prerequisites
words: 5963
sections: 6
paragraphs: 59
---

# Chapter

Claim: Every chapter computes on the same four objects, on excess returns, fixed here once, and on one of two data sources: a modeled market with no real data on its own calendar, the default because it reproduces offline, and a free real-data layer with a pinned cutoff and a manifest, used only where a claim must be about real markets.
Question: What do the symbols mean and where do the numbers come from; cites Markowitz for needing the four objects and Coqueret and Scheuch et al. for opening a book this way.
Why here: Needs chapter 1 for `as_xts_pm()` and the tidy-to-`xts` crossing. Fixes the notation so that no later chapter redefines a symbol and describes the data so that no later chapter explains what it computes on; sits on neither side of the strategic–tactical distinction chapter 3 defines but is the ground both stand on. Chapter 9 takes the moments equation, every chapter the three-object data block and the calendar tools, chapters 4, 7, 15, 20, 21, 22 and the appendices the individual tables and caveats.
Does: Read any symbol in the book, build `R`, `rf` and `Re`, annualize two ways and say which applies, read a model-calendar date and an episode, name every shipped table and its trap, and fetch and check the real sleeves.
Order: Notation (with annualizing and the data block), the modeled market in seven subsections, the real-data layer, vocabulary, takeaways, exercises. The theory–implementation–application contract does not apply: a reference chapter with code interleaved as checks throughout and no application section.

# Sections

## Opening — 255

Says: The book manipulates four objects and two data sources, and both are fixed here once.
Why here: Not a `##` section; the two paragraphs before the first heading.
Paragraphs:
- (code: setup, hidden)
- ¶1 [claim] Four objects every chapter uses, Markowitz needed all four; notation and data fixed once, after Coqueret and Scheuch.
- ¶2 [method] The chapter's order in one sentence; it sits on neither side of strategic–tactical but under both.
- (code: packages used)

## Notation — 1304

Says: Bold vectors and matrices, simple total returns, excess over the bill as the default basis, and the portfolio's mean and variance as the equation every later chapter starts from.
Why here: First because no later chapter may redefine a symbol; chapter 9 takes the moments equation as its start, and chapter 3 supplies the argument for the excess basis that is only stated here.
Paragraphs:
- ¶1 [definition] Typographic conventions, N assets over T periods, simple total return defined; simple over log because of cross-asset linearity.
- ¶2 [definition] The bill is the risk-free rate; excess returns the default basis everywhere; chapter 3 argues why, here only stated.
- ¶3 [definition] Weights, the ones vector, μ and Σ with hats for estimates; portfolio mean and variance; Sharpe ratio needs no subtraction.
Note: ¶2 says the reasons for the excess basis belong to chapter 3 and then lists three of them; it half-argues what it says it will not argue.

### Annualizing — 889

Says: Two annualizing conventions, arithmetic for optimizer inputs and compounded for what a series earned, and the three-object data block every chapter opens with.
Why here: Returns arrive monthly and are reported annually, so the conversion is fixed with the symbols; the data block follows because the symbol table's code column is itself a convention.
Paragraphs:
- ¶1 [definition] Arithmetic scaling for optimizer inputs, compounded return for sample tables; gap is half the variance, the drag.
- (table: tbl-02-symbols)
- ¶2 [method] The code column is a convention; every chapter's first block builds three objects, nothing else.
- (code: data)
- ¶3 [code] `as_xts_pm()` is the tidy-to-`xts` boundary, chapter 1 explains; `stopifnot()` is the book's habit, not decoration.
- ¶4 [code] The two conventions as two lines of code, used by every table.
- (code: conventions)
- ¶5 [example] (callout) Take `US_equity`; its monthly mean and standard deviation follow.
- (code: worked-inputs)
- ¶6 [example] (callout) Arithmetic annual mean, annual volatility and compounded return with the sample numbers substituted.
- ¶7 [example] (callout) Monthly gap equals half the variance; annual gap smaller because compounding earns return on return.
- (code: worked-check)
Note: The data-preparation convention and the `data` chunk sit under the heading "Annualizing", after the symbol table; the subsection carries two topics, and the worked example on annualizing comes after the data block has interrupted it.

## The Modeled Market — 2848

Says: The default data is a modeled market with no real data, on its own calendar, shipped inside `tidypm` so that every number reproduces offline; the section lists its tables, says how the series are built, and names the properties a reader must know before modeling on it.
Why here: Notation says what is computed, this says what it is computed on; the calendar precedes the tables because every date in them reads only on it; the caveats come last because they follow from how the series are built.
Paragraphs:
- ¶1 [definition] Factor models estimated on market data (states the estimation period), factors replayed, paths reassembled; own calendar; named episodes; shockable.
- ¶2 [claim] Ships inside the package and reproduces offline; estimation buys realism of structure, which chapter 4 relies on.

### The model calendar — 463

Says: A date is a position on the model calendar, and four functions are the only way any chapter reads, names, selects or plots one.
Why here: Because the data are modeled, dates need translating before any table or figure can be read; the episode table and the time axes of the next subsections depend on these tools.
Paragraphs:
- ¶1 [definition] Dates stored as `Date` but years are model years; four tools from `tidypm` and `R/_common.R` translate.
- ¶2 [code] `model_year()` gives the model year, `fmt_model()` writes a date as the prose does.
- (code: calendar-years)
- ¶3 [result] Sample length and model-year span; a point is named like the worst `US_equity` month; episodes are `sim_episodes` rows.
- (code: tbl-02-episodes)
- ¶4 [code] `in_episode()` returns a logical so that no chapter types a window.
- (code: calendar-episode)
- ¶5 [result] Over the credit crisis equity loses and government gains; `scale_x_model()` labels the time axis.
- (code: fig-02-calendar)
- ¶6 [caveat] The convention applies to the modeled market only; the literature and the real sleeves keep their dates.

### The class universe — 567

Says: Sixteen risky class series are the allocation spine, the five money markets ship beside them and are neither cash nor the risk-free rate, and a table places each series by return, volatility and Sharpe ratio.
Why here: The classes are what Parts III to V allocate across, so they come before the instruments beneath them; the money-market point is settled here because Notation declared the bill the risk-free rate.
Paragraphs:
- ¶1 [definition] Sixteen series, five currencies times three classes plus one commodity, all dollars unhedged; weekly counterpart at native frequency.
- (code: classes)
- ¶2 [claim] Five money markets ship beside the universe, deliberately out: marked-to-market short bonds, not bills, not risk-free.
- (code: money-market)
- ¶3 [result] `US_money_market` tracks the bill yet goes negative far more often; foreign money markets are currency positions.
- ¶4 [method] The class table gives return, volatility and Sharpe; chapter 4 carries the full table.
- (code: tbl-02-classes)
- (code: fig-02-indices)
Note: `fig-02-indices` follows the table with no sentence pointing to it or reading it; the subsection ends on an unreferenced figure.

### How the class series are built — 202

Says: Equity classes are value-weighted on the previous week's capitalization, the other classes equally weighted, and a monthly class return is the compounded weekly return within the month.
Why here: not stated; it follows the class table and precedes the instruments the classes are built from.
Paragraphs:
- ¶1 [method] Lagged capitalization weights, no look-ahead; non-equity classes equal-weighted; monthly is weekly-rebalanced observed at month ends; check it.
- (code: monthly-from-weekly)
Note: One paragraph and one chunk; the chunk's output, the largest monthly discrepancy, is never read in prose, and the subsection ends on it.

### The instrument universe — 236

Says: Beneath the sixteen classes sit the individual instruments, the same market at a finer grain and the universe of the Part VI sleeve chapters.
Why here: Granularity is the book's spine, classes first and instruments after; the sleeve chapters are named as the takers.
Paragraphs:
- ¶1 [definition] Instruments described in `sim_assets`, carried at both frequencies; the universe chapters 21 and 22 select within.
- (code: tbl-02-instruments)
- (code: instrument-metadata)
- ¶2 [definition] What each instrument type is: sector-tagged equities, credit by maturity and grade, zero-coupon governments, commodity sub-indices; anonymized identifiers.
Note: `tbl-02-instruments` is referenced only from the Vocabulary section, not from the prose around it.

### Exchange rates, curves, capitalizations and rating changes — 391

Says: Four further tables let a chapter show what moved a series: exchange rates with the one-line hedge, the curve factors behind the bond block, the equity capitalizations, and ESG rating changes without a starting level.
Why here: not stated; the tables are listed after the series they explain, and each is handed to the chapter that uses it.
Paragraphs:
- ¶1 [definition] FX quoted as dollars per local unit; hedged return is unhedged minus `fx_return`; whether to hedge: chapters 4, 15.
- (code: hedge)
- ¶2 [result] Hedging cuts `JP_government` volatility sharply and `JP_equity` not at all; chapter 4 explains the difference.
- ¶3 [definition] `sim_curve_weekly`: Nelson–Siegel level, slope, curvature in Diebold–Li form, plus two credit spreads per region.
- (code: curve)
- ¶4 [definition] `sim_marketcap_weekly` holds the equity capitalizations a capitalization-weighted benchmark needs; chapter 21 builds one.
- ¶5 [definition] ESG rating changes, one row per change, no starting level, no effect on returns; chapter 20 works with them.

### Three caveats, one departure, and a frozen version — 763

Says: Currency dominates foreign bonds, the bond block is nearly rank-deficient at instrument level and the equities are single names; euro-area equity carries a deliberate three-point overlay within one standard error; and the dataset is frozen at one version because regenerating redraws the paths.
Why here: The three properties are consequences of how the market is built, so they follow the construction, and a reader should know them before modeling on it; the freeze closes the description.
Paragraphs:
- ¶1 [transition] Three properties follow from the construction; know them before modeling.
- ¶2 [caveat] Currency dominates foreign bonds: hedging removes most of their dollar volatility; only `US` and `GLOBAL` are free of it.
- ¶3 [caveat] Three maturities on a three-factor curve and two grades on one credit factor make the instrument covariance practically singular.
- (code: conditioning)
- ¶4 [result] The instrument condition number makes unconstrained mean-variance nonsense there; the sleeves shrink or constrain; no problem at class level.
- ¶5 [caveat] Equity series are single securities; a portfolio of them diversifies more readily than a real index would.
- ¶6 [claim] One deliberate departure: a three-point drift on euro-area equity, a capital-market assumption, stated as a parameter.
- (code: overlay)
- ¶7 [result] Without it `EU_equity` is a dead column in the tangency portfolio; the overlay is within one standard error.
- ¶8 [caveat] Frozen at version 6.2.0: a regenerated export is a different path; a script names the numbers that moved.
Note: The `overlay` chunk builds and solves the long-only tangency portfolio of chapter 9 to justify a data choice, the chapter's heaviest chunk and the only place a reader meets `optimize.portfolio()` before chapter 9; the heading counts three caveats and the freeze in ¶8 is in practice a fourth.

## The Real Data Sleeves — 692

Says: Where a claim has to be about real markets, `tidypm` carries a small free-data layer with a registry, one download to a cache at a pinned cutoff, an offline read, and a manifest that names what has moved.
Why here: The modeled market cannot support a claim about real markets and chapters 21 and 25 must make one; the layer is described after the default it supplements.
Paragraphs:
- ¶1 [claim] The modeled market cannot speak for real markets; chapters 21 and 25 must; the layer adds cutoff and manifest.
- ¶2 [definition] `pm_sources()` is the registry, data not state; calling it downloads nothing.
- (code: tbl-02-sources)
- ¶3 [result] Which sleeves are built and from where; high yield is a mutual fund, with two caveats stated in place.
- ¶4 [method] `pm_init()` downloads, joins on month ends, writes panel and manifest to the cache; stops at a pinned cutoff.
- (code: cutoff)
- ¶5 [method] The cutoff is a year end so no table carries a stub year; run once, read forever.
- (code: real-data-layer)
- ¶6 [caveat] `pm_data()` never touches the network and never pads a ragged panel; a filled gap is an estimate in disguise.
- ¶7 [method] The manifest is reproducibility for data not ours to redistribute; `pm_check()` names sleeves that moved; nothing downloaded is committed.
Note: ¶3 reads a table it never names and carries two caveats inside a result paragraph; `tbl-02-sources` is referenced nowhere in the prose.

## Asset Class Vocabulary — 369

Says: Code uses the data's names and prose uses whichever is clearer; the class level is where Parts III to V work, the instrument level Part VI, and strategic versus tactical is a different axis, defined in chapter 3.
Why here: Both naming systems appear in the book, so the map closes the data description; the granularity–horizon distinction is placed last because the next chapter defines the horizon words.
Paragraphs:
- ¶1 [definition] Two naming systems; the rule: code uses the data's names, prose whichever is clearer.
- (table: tbl-02-vocabulary)
- ¶2 [caveat] "Alternatives" normally covers four asset types; this market has only commodities.
- ¶3 [claim] Classes are Parts III to V and where Brinson locates most variation; instruments are Part VI; granularity is not horizon.
Note: ¶3 introduces the book's two axes, granularity and horizon, under a heading about naming; it is the chapter's only paragraph on the book's structure rather than its data.

## Key Takeaways — 294

Says: Six bullets restating notation, annualizing, the calendar, the universe, the caveats and the real-data layer.
Why here: Closes the chapter per the contract.
Paragraphs:
- ¶1 [takeaway] Typographic conventions, the matrix, the moments of excess returns; chapter 3 says why excess.
- ¶2 [takeaway] Arithmetic for optimizer inputs, compounded for what a series earned; the gap is half the variance.
- ¶3 [takeaway] No real data, model years, the four calendar tools, the four episodes.
- ¶4 [takeaway] Sixteen series, the instruments beneath, money markets beside and neither cash nor risk-free.
- ¶5 [takeaway] Three caveats, the euro-area overlay within one standard error, frozen at 6.2.0.
- ¶6 [takeaway] The four real-data functions and when the layer is used.

## Exercises — 168

Says: Three exercises on hedging all non-US series, rebuilding the commodity class from its instruments, and rebuilding `US_equity` equally and value-weighted.
Why here: Closes the chapter per the contract; each exercise checks a construction claim of the Modeled Market section.
Paragraphs:
- ¶1 [exercise] Hedge all twelve non-US series, tabulate the variance removed by class; why bonds and not equities.
- ¶2 [exercise] Rebuild `GLOBAL_commodity` weekly from its eight instruments and compare with the shipped monthly series.
- ¶3 [exercise] Rebuild `US_equity` equally and value-weighted; confirm the second matches; which should a benchmark use.
