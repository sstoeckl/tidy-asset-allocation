# Writing brief for a chapter

Read this, then `CLAUDE.md` (the governing document), then
`chapters/09-mean-variance.qmd` (the reference chapter: its voice, its shape and
its code discipline are the standard), then `PLAN.md` for your chapter's claims,
then your chapter's stub with its `PLANNING NOTE`. Only then write.

## What a chapter is

A textbook chapter in the category of *Tidy Finance with R* and *Machine
Learning for Factor Investing*: explain what is being done, state it in
mathematics, attribute it to the literature, implement it in R, then hand the
reader takeaways and exercises. The primary reader is a master's student meeting
the material in a course; the chapter must be teachable in one session. A
practitioner reads the same text for the working implementation; a doctoral
student uses the references as a route into the literature.

The skeleton is fixed (`CLAUDE.md`, "The chapter contract"): YAML with `title`,
`metadata.pagetitle`, `description-meta`; opening paragraph that states the
question and carries the seminal citation in its first two sentences; one
sentence on what we do, in order, naming the chapter's place on the horizon axis
(strategic, tactical, or neither — chapter 3 defines the terms); a setup chunk;
theory with display mathematics; implementation with executed code; application
on the simulated market; **Key Takeaways** (about five bullets); **Exercises**
(about three, numbered). Headings are noun phrases named for the problem.

Length **2,500–8,000 words** including code. Citations: **15–30 distinct keys**
for a chapter with substantial theory, **8–15** for a focused one. First person
plural, plain academic register, American spelling. The language table in
`CLAUDE.md` is binding — in particular *dominated* not "beaten", *lower
volatility* not "quiet", and worked examples as formulas with the sample numbers
substituted in (inline R inside the display equation) followed by the code as a
check.

Package traps — where `PortfolioAnalytics` defaults wrongly, fails silently or
drops something — go in a `::: {.callout-note}` placed where the reader would
walk into it. Never a section of their own. Collapsible worked examples use
`::: {.callout-note collapse="true"}` with a `## Worked: ...` heading.

## Anchors, and the cross-reference rule

Your chapter's three main sections keep the anchor ids of the stub exactly, even
though the headings change:

```
## <Theory heading>          {#sec-NN-<slug>-theory}
## <Implementation heading>  {#sec-NN-<slug>-implementation}
## <Application heading>     {#sec-NN-<slug>-application}
```

Every other chapter has the same three anchors, so you can refer to any chapter
now, written or not: `@sec-03-return-risk-and-the-investor-theory`,
`@sec-25-backtesting-application`, and so on. The full list is in
`tools/check-crossrefs.py`'s output; the slugs are the file names without number
and extension. Appendices: `@sec-90-data-description`, `@sec-91-proofs`,
`@sec-92-solver-matrix`, `@sec-93-package-notes`, `@sec-94-r-primer`,
`@sec-95-coverage-ledger`, `@sec-96-solutions`.

**Refer back to at least three earlier chapters and forward to at least two
later ones**, each reference inside the clause that needs it, never as "see
also". Equations `{#eq-NN-name}`, figures `#| label: fig-NN-name`, tables
`#| label: tbl-NN-name`; reference them with `@eq-`, `@fig-`, `@tbl-`.

## Data, and the calendar rule

The modeled market ships in `tidypm` (`?sim-market`, `?model_year`). Load it
as chapter 9 does, and nothing more — data preparation is not chapter content:

```r
R  <- as_xts_pm(sim_class_returns_monthly, date, class, return)   # 16 risky classes
rf <- sim_riskfree_monthly$return                                  # the bill
Re <- R - rf                                                       # excess returns
```

Objects: `sim_class_returns_monthly` / `_weekly` (16 risky classes: `US`, `UK`,
`EU`, `CH`, `JP` × `_equity`, `_government`, `_credit`, plus
`GLOBAL_commodity`), `sim_money_market_monthly` / `_weekly` (5 money markets,
beside the universe), `sim_asset_returns_monthly` / `_weekly` (181
instruments), `sim_assets` (metadata), `sim_riskfree_*`, `sim_fx_monthly` /
`_weekly` (dollars per unit of local currency; hedged = unhedged − `fx_return`),
`sim_curve_weekly` (level, slope, curvature per region plus ten spreads),
`sim_marketcap_weekly` (123 equities), `sim_esg_changes_quarterly` (rating
changes, no levels), `sim_episodes` (the four named episodes). 372 months, all
in USD unhedged, dataset version 6.2.0.

**The market is modeled and runs on a model calendar.** (The book's term is *the modeled market*, American spelling; the package help pages keep their British *modelled*.) Read `CLAUDE.md`,
"The modeled market" and "The calendar rule"; they are binding. In short:

- The data are *modeled*: factor models estimated by historical simulation on
  market data from 1992 to 2022, replayed with fresh idiosyncratic draws. No
  series is a real history. Only chapter 2 and appendix A say this; your
  chapter refers to them.
- Dates are model dates: model years 1 to 31 (`model_year(d)`). **Never write
  a calendar year, a dated event or a historical name for anything in the
  modeled market** — no "2008", no "global financial crisis", no "COVID", no
  "from 2002". Say "model year 17", "the credit crisis", "the last ten model
  years".
- Episodes: `in_episode(zoo::index(R), "credit_crisis")`, with keys
  `equity_bear`, `credit_crisis`, `liquidity_shock`, `rates_shock`; the labels
  for the text are in `sim_episodes$label`. Never type a window.
- No date literal in code. Derive positions: `zoo::index(R)[121]` (the first
  out-of-sample month of the register, the first month of model year 11),
  `model_year(d) >= 11`.
- Time axes: `+ scale_x_model()`. A date in prose: `fmt_model(d)` gives
  "August of model year 17". Never `format(d, "%Y")`.
- The literature keeps its dates; so do the real-data sleeves of `pm_data()`.

Facts verified on 6.2.0 that no chapter may contradict are tabled in
`CLAUDE.md` ("Pinned to dataset 6.2.0"). Numbers in `PLAN.md` are older than
that and are stale: recompute, never copy. Out-of-sample numbers come from
`output/tables/oos-sweep.csv` (columns `universe, window, frequency, strategy,
basis, sharpe, ann_return, ann_vol, es_95, max_drawdown, ann_turnover,
n_periods, n_failed`; strategies `equal_weight, inverse_vol, min_variance,
max_sharpe, min_cvar`; windows 36/60/120; frequencies months/quarters/years;
basis gross/net; out of sample from observation 121 for every window) — read
them, never retype them, and **never assert an out-of-sample ranking in
prose**: compute it, and `stopifnot()` any order the argument depends on.

## Code discipline

- **Every number in the prose is inline R.** Never type a number a chunk could
  produce. A count, a percentage, a name of a series — all computed.
- **Assert that things fit together.** `stopifnot()` wherever two objects must
  align; index by name, never by position; `w <- w[colnames(R)]`.
- **Figures are built from one tidy data frame**, one row per plotted thing,
  with a `kind` column. Use `theme_tidyaa()` (set already), `tidyaa_colors`,
  `scale_colour_tidyaa()`; never hard-code a color.
- Use `PortfolioAnalytics` functions wherever they exist, and show them: this
  book covers most of the package, and appendix F ledgers which chapter uses
  which function. The 115 exports are listed by
  `getNamespaceExports("PortfolioAnalytics")`. `PerformanceAnalytics` is the
  engine for moments, drawdowns and charts. `tidypm` functions that do not
  exist yet (`to_real()`, `hedge_currency()`, `equilibrium_returns()`,
  `sharpe_gap()`, `ppp_fit()` and the rest of the roadmap in
  `../tidypm/R/tidypm-package.R`) **are not to be called** — write the few
  lines inline in the chapter instead. Do not add functions to `tidypm`.
- The `PortfolioAnalytics` build is a fork with three fixes; `R/_common.R`
  warns if it is not. `risk_aversion` is γ/2 (appendix B). `maxSR` defaults to
  `FALSE`. `ES()` defaults to Cornish-Fisher. Read `chapters/93-package-notes.qmd`.
- Keep chunks fast. A bootstrap, a sweep or a metaheuristic run should finish
  in well under a minute per chunk; reuse `output/tables/*.csv` where the
  number already exists. No chunk may write into the project except through
  `output/tables/` and only if you must.
- Chunk labels are unique within the chapter, kebab-case, no spaces.

**Execute before you write prose.** Run

```
& "C:\R\R-4.6.1\bin\Rscript.exe" tools/run-chapter.R chapters/NN-slug.qmd
```

from the project root (renv activates only from there). It purls the chunks and
runs them in order, reporting the first error by chunk label. The chapter is
not written until this exits 0. Inline expressions are not executed by it —
check each one by eye against the objects that exist at that point, and make
sure every object an inline expression uses is created by an earlier chunk.
**Then read your own sentences with their numbers in them.** Run

```
& "C:\R\R-4.6.1\bin\Rscript.exe" tools/knit-chapter.R chapters/NN-slug.qmd
```

which knits the chapter to a markdown file outside the project with every
inline expression evaluated, and prints its path. Read that file from top to
bottom: every sentence that states a number, an order, a sign or a name must
be true of what the code produced. A sentence whose claim the data do not
support is rewritten, not softened. Do the same for the solutions file.

Do **not** run `quarto render`: in this project it renders all 39 files and
takes half an hour; the orchestrator renders.

## Citations

Keys live in `assets/bib/references.bib` (about 260 today). Cite what exists
first — read the file. To add an entry, **append** it with `cat >>` in Bash
(never rewrite the file; other chapters are being written in parallel), after
`grep -c "{key," assets/bib/references.bib` shows 0. Every article entry
carries a `doi`; then run `python tools/check-bib.py <key> ...` and fix anything
that fails. A DOI you are not sure of is looked up, not guessed. Books carry
publisher and year; working papers carry an URL and year. Key format:
`surname` + `year` (`markowitz1952`), a letter suffix on collision.

## Exercises and solutions

Three to five exercises, numbered, each answerable with the chapter's code and
data. Write short solutions (a paragraph each, code where it settles the
question, executed) into `chapters/solutions/NN-slug.qmd` — create the file with
a `### Chapter NN: <title> {.unnumbered}` heading and `#### Exercise 1` etc.;
appendix G includes these fragments. Solutions must also pass
`tools/run-chapter.R`.

## What to leave behind

Delete the `PLANNING NOTE` and every `TODO`. Do not edit any other chapter, any
tool, `_quarto.yml`, `R/_common.R` or `renv`. Do not install packages. If
something in the plan cannot be done with the data (fundamentals, ESG levels,
market weights for bonds), say so in one plain sentence in the chapter, do the
nearest thing that can be done, and report it.

Report back, in this order: word count (`wc -w`), number of distinct citation
keys and which are new, the `PortfolioAnalytics` functions demonstrated, the
cross-references made (back and forward), the run-chapter result, and anything
left undone or decided on your own that Sebastian should look at.
