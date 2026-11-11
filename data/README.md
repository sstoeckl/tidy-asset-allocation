# The data layer

Decisions, sources and known gaps. This file is the specification; `tidypm`
implements it and chapter 2 explains it.

## Settled

| Decision | Value |
|---|---|
| Base currency | **USD** |
| Tier 1 start | **1990**, with documented splices where a sleeve cannot reach back |
| Tier 1 frequency | Monthly |
| Sleeves | **12** — ten core plus currency-hedged Developed ex-US and Emerging |
| Credentials | **None.** Everything in Tier 1 is free and scriptable. |
| Heavy compute | Server; `_freeze` is committed and is the handoff |

## Why not ETFs

The obvious approach — SPY, EFA, EEM, AGG, TLT, LQD, HYG, GLD, VNQ — does not
survive a 1990 start. SPY begins in 1993, EFA in 2001, HYG in 2007. An
ETF-based universe silently becomes a post-2007 universe, which throws away the
1990s emerging-market crises and the entire pre-GFC credit cycle: exactly the
periods where correlations break down and diversification fails, and therefore
exactly what an allocation book needs.

So Tier 1 is built at **index level**, and two sleeves are **constructed from
yields** rather than downloaded. That is not a workaround. Building a bond
return from a yield curve is the subject of chapter 19, and having done it in
chapter 2 makes that chapter easier rather than redundant.

## Sources

| # | Sleeve | Source | Coverage | Note |
|---|---|---|---|---|
| 1 | US equity | Kenneth French, `Mkt-RF` + `RF` | 1926– | |
| 2 | Developed ex-US equity | Kenneth French, *Developed ex US* | **1990-07–** | Exact fit to the start date |
| 3 | Emerging equity | Kenneth French, *Emerging Markets* | **1990-07–** | Exact fit |
| 4 | Cash | Kenneth French, `RF` (1-month T-bill) | 1926– | |
| 5 | Government, short | Constructed from FRED `DGS1`, month-end | 1962– | See below |
| 6 | Government, long | Constructed from FRED `DGS10`, month-end | 1962– | See below |
| 7 | Investment-grade credit | Constructed from Moody's `AAA` / `BAA` | 1919– | Documented maturity and loss assumption |
| 8 | High yield | **gap — see below** | | |
| 9 | Commodities | AQR, *Commodities for the Long Run* | 1877– | Free monthly index level |
| 10 | Listed real estate | FTSE Nareit All Equity REITs | 1972– | Free monthly from reit.com |
| 11 | Developed ex-US, hedged | Constructed via covered interest parity | 1990-07– | From FRED short rates |
| 12 | Emerging, hedged | Constructed via covered interest parity | 1990-07– | Same |

## Constructed bond sleeves, and how they were checked

`tidypm::bond_total_return()` prices a par bond exactly rather than using a
duration approximation: each month the sleeve buys a fresh par bond, and one
month later that bond is repriced at the new yield with one month less to run.
Return is price change plus accrued coupon.

Validated against years a bond desk would recognise:

| Year | Realised 10y UST | Monthly average (`GS10`) | **Month-end (`DGS10`)** |
|---|---|---|---|
| 1995 | +23.5% | +24.1% | +25.4% |
| 2014 | +10.7% | +8.9% | +10.6% |
| 2021 | −4.4% | −3.6% | −4.1% |
| 2022 | −17.0% | −14.9% | **−16.4%** |
| 2023 | +3.9% | +0.5% | **+3.8%** |
| | *mean abs. error* | *1.53 pp* | **0.85 pp** |

**Decision: month-end daily yields, not monthly averages.** The `GS`-prefixed
series are monthly averages of daily yields, and the averaging smooths away
intra-month moves — which dampened both the 2022 drawdown and the 2023
recovery, the two years where a bond sleeve most needs to be right. The
`DGS`-prefixed daily series sampled at month-end fixes both and reaches back to
1962, comfortably before the 1990 start.

Residual error is around one percentage point a year, which is the par-bond and
frictionless-roll assumption showing. Stated in chapter 2; revisited properly in
chapter 19, where the curve is the subject rather than an input.

### Rejected sources

**FRED ICE BofA total return indices** (`BAMLCC0A0CMTRIV`,
`BAMLHYH0A0HYM2TRIV`) look ideal and are not usable: FRED serves them on a
rolling three-year window under licence. Verified — the endpoint returns 796
daily rows regardless of the requested start date. Anything built on them would
silently become a three-year book.

**S&P GSCI and Bloomberg Commodity total return** are not on FRED and are not
free.

## Why free-only is a feature, not a constraint

Neither reference book can offer what this one can, and it is worth saying so in
the preface.

**Tidy Finance** builds its empirical chapters on WRDS, a paid institutional
subscription. Readers without it get pseudo data, and the authors are admirably
blunt about what that means: the pseudo tables "do not allow you to replicate any
results of the book", contain "no samples of the original data", and are drawn as
"independent random numbers", so any estimate from them is "pure noise and not
economically interpretable". The code runs; not one number reproduces.

**Machine Learning for Factor Investing** ships a single dataset on GitHub —
1,207 stocks, 93 characteristics, 1998–2019 — and says nothing at all about its
provenance, vendor or licence. Readers can reproduce everything, because a
commercial snapshot was redistributed. Whether that was permitted is not
addressed.

|  | Reproducible for everyone? | Licensing clear? |
|---|---|---|
| Tidy Finance | No — noise without WRDS | Yes |
| MLFI | Yes | Unstated |
| **This book (Tier 1 and 1b)** | **Yes** | **Yes** |

Free sources, rebuilt on the reader's machine, every number traceable. Tier 3
(CRSP and Compustat, chapter 18) shares Tidy Finance's limitation because no free
substitute exists — but the allocation chapters, which are the heart of the book,
depend on nothing anyone has to buy.

**Rule:** no commercial data source is a hard dependency anywhere in Parts I–VII.
Where one would help, it is an optional upgrade that changes no printed number.

## Status: eight sleeves, and that is enough to start

| Sleeve | Source | Coverage | 1990-07 to 2025-12 |
|---|---|---|---|
| US equity | French market | 1926– | +10.98%, vol 15.16% |
| Emerging equity | French | 1989-07– | +7.93%, vol 20.33% |
| Developed ex-US equity | French | 1990-07– | +6.12%, vol 16.29% |
| IG credit | Moody's BAA, constructed | 1950– | +7.46%, vol 7.83% |
| High yield | VWEHX fund proxy | 1980– | +6.84%, vol 7.14% |
| Government long | FRED DGS10, constructed | 1962– | +5.06%, vol 7.36% |
| Government short | FRED DGS1, constructed | 1962– | +3.09%, vol 0.99% |
| Cash | French RF | 1926– | +2.64%, vol 0.63% |

**Cutoff: 2025-12-31.** Sources publish at different speeds — French runs a
couple of months behind FRED — so without a cutoff the final rows carry fewer
assets than the rest, silently. A calendar year end removes that and keeps every
annual table a complete year. `pm_init(cutoff = NULL)` returns everything the
sources have, which is how chapter 22 demonstrates what a ragged tail does to a
backtest.

Consequence worth stating: **the panel is now rectangular** — 426 months from
1990-07, all complete. The ragged-panel material has no natural home in Tier 1
until a late-starting sleeve is added, so chapter 5 uses `pm_universe()` and an
uncut panel to make the same point deliberately.

### Deferred, not blocked

Commodities, listed real estate and the two currency-hedged variants are
declared in `pm_sources()` with `implemented = FALSE`. Each needs a fetch
function and one flag flipped.

Commodities is the interesting one: no free source reaches 1990. AQR's long-run
index does, but costs an xlsx parser, an excess-return adjustment and a
dependency on a corporate file whose format and continued existence are outside
our control — for twelve years (1990–2002) in which little happened to
commodities. The practical alternative is `DBC` from 2006 through the existing
`yahoo_fund()` machinery, which needs nothing new. Neither is urgent.

## High yield: spliced, not folded — decided

No free total-return series reaches 1990, so the sleeve **enters the panel late**
rather than being dropped or merged into investment-grade credit.

The consequence is deliberate: Tier 1 is a **ragged panel**, and every chapter
that estimates a moment has to say what it does about that. Chapter 2 introduces
it, chapter 5 shows what an unequal history does to a covariance estimate, and
chapter 22 shows what it does to a backtest that ignores it.

The rejected alternative — one credit sleeve back to 1919 — would have produced
a rectangular panel and quietly removed a genuinely distinct risk. Tidiness at
the cost of the thing being taught.

**Rule that follows:** no function in the data layer may pad a missing sleeve
with zeros, carry the last value forward, or drop incomplete rows without
saying so. `as_xts_pm()` already warns on ragged input; the loaders must not
create raggedness the reader cannot see.

## Tier 1b — optimisation universes

Twelve sleeves is the allocation spine, and twelve is a comfortable number.
Comfortable numbers hide the problems several chapters are about, so there is a
second set of universes from the same source, reached through
`tidypm::pm_universe()`.

The variable that matters is **N relative to T**, and the easiest way to teach it
is to move it. Measured on a sixty-month window:

| Universe | N | Sample covariance at T = 60 | Smallest eigenvalue |
|---|---|---|---|
| `industries10` | 10 | invertible | 2.0e-04 |
| `industries49` | 49 | invertible, barely | 5.8e-06 |
| `size_bm100` | 100 | **singular — `solve()` fails** | **−4.0e-04** |

The hundred-portfolio case is not merely ill-conditioned: its smallest
eigenvalue is *negative*, so the estimate is not even positive semi-definite. A
covariance matrix that cannot be a covariance matrix is a better argument for
shrinkage than any amount of prose, and it is three lines of code away.

`industries49` also names its columns — `Agric`, `Food`, `Beer`, `Smoke`,
`Guns`, `Coal`, `Oil`, `Mines` — so an exclusion screen is a set of column names
rather than a mapping from SIC codes. `pm_screen("sin" | "fossil" | "weapons")`
returns them; all are present in the universe. That removes the only fiddly part
of chapter 10.

### Why not individual stocks

Individual equities are the obvious choice for a large universe and the wrong
one for the spine. Yahoo Finance is undocumented, rate-limited and revises
without notice, so a book built on it stops reproducing the moment a ticker
changes. These portfolios have a real covariance structure, a century of
history, and no survivorship problem in the demonstration.

Named stocks and ETFs keep a role where recognisability is worth more than
reproducibility — what a trade actually costs, what a sleeve actually holds —
fetched with `tidyquant::tq_get()`. They are illustration, never foundation, and
the book says which is which. If Yahoo breaks, an illustration breaks; no
chapter's numbers move.

## Tier 2 — long-run macro

Jordà–Schularick–Taylor Macrohistory, 18 countries, annual, ~1870–. Free, but
the licence forbids redistribution, so it is fetched and never committed. Used
in one section of chapter 7.

## Tier 3 — single assets

US equity cross-section and factors via `tidyfinance` (CRSP, Compustat, Ken
French, JKP). Treasury constant-maturity curve via FRED for chapter 19.

WRDS-backed, so `tidypm::pm_pseudo_data()` provides a synthetic fallback that
lets the book render without credentials.

## Which package pulls what

Four packages overlap here and none of them covers the whole job. Chapter 2 has
to say which to reach for and why, because the obvious guess is wrong at least
once.

### What each actually offers

**`FFdownload` 1.2.0** — the complete Kenneth French library. Four functions:
`FFlist()` inventories what is available, `FFmatch()` previews how a name would
be fuzzy-matched *before* anything is downloaded, `FFget()` pulls one dataset
straight into the session, and `FFdownload()` does bulk retrieval with
`cache_days` control. Returns **every sub-table** of a dataset — value-weighted
returns, equal-weighted returns, number of firms, average size — not just the
headline table. Handles French's `-99.99` / `-999` missing-value sentinels.

**`tidyfinance` 0.8.0** — 329 datasets behind one `download_data()` verb. 297 of
them mirror French; the remaining 32 are the reason to use it: Goyal–Welch macro
predictors, WRDS (CRSP, Compustat, CCM links, FISD, TRACE), JKP global factors,
Open Source Asset Pricing, q5 factors, FRED, index constituents, and — crucially
for us — **pseudo-data generators** that stand in for WRDS when there are no
credentials. Also ships estimation helpers: `estimate_betas()`,
`estimate_fama_macbeth()`, `assign_portfolio()`, `compute_breakpoints()`,
`implement_portfolio_sort()`, `winsorize()`, `trim()`.

**`tidyquant` 1.0.12** — `tq_get()` over thirteen sources: Yahoo prices,
dividends, splits, FRED (`economic.data`), Quandl, Tiingo, Alpha Vantage, and
Bloomberg via `rblpapi`. Plus the tidy wrappers `tq_transmute()`, `tq_mutate()`
and `tq_portfolio()` around xts and PerformanceAnalytics.

**`PortfolioAnalytics` 2.1.2** — **no data facilities whatsoever.** One bundled
dataset (`indexes`), zero download functions. It consumes an `xts` matrix and
returns weights. Worth stating plainly in chapter 1, because a package this
large invites the assumption that it handles its own inputs, and it does not.

### The choice, and the overlap

`tidyfinance` mirrors most of the French library, so there is a real overlap.
Tier 1 uses `FFdownload` anyway, for three reasons: it returns every sub-table
rather than the headline one, `FFmatch()` gives a pre-download reproducibility
check nothing else offers, and `cache_days` makes re-download an explicit
decision rather than a side effect.

| Need | Call | Note |
|---|---|---|
| Anything from Kenneth French | `FFdownload::FFget(name, frequency = "monthly", na_values = c(-99, -999, -99.99), format = "tbl")` | Verify first with `FFmatch()` |
| FRED yield series | `tidyfinance::download_data("fred", series = "DGS10")` | No API key needed |
| Goyal–Welch macro predictors | `tidyfinance::download_data("macro_predictors_monthly")` | Chapter 14 |
| CRSP / Compustat | `tidyfinance::download_data("wrds_crsp_monthly")` | Tier 3, needs credentials |
| Credential-free fallback | `tidyfinance::download_data("crsp_monthly")` | The pseudo generator |
| JKP / OSAP factors | `tidyfinance::download_data("jkp" \| "osap")` | Chapter 18 |
| AQR commodities, NAREIT, JST | `tidypm::` loaders | Nobody wraps these |
| Bloomberg / Refinitiv | `tidyquant::tq_get(get = "rblpapi")` | Mentioned, never used — the book stays credential-free |

Verified live: `FFmatch()` resolves `F-F_Research_Data_Factors`,
`Developed_ex_US_3_Factors` and `Emerging_5_Factors` at similarity 1.0, and
`FFget()` returns 1926-07 onward for the US factors and **1990-07 onward** for
Developed ex US — an exact fit to the start date.

## Rules

1. **Nothing downloaded is committed.** The snapshot date is pinned; the cache
   is Parquet under `data/cache/` and gitignored.
2. **`data/fallback/` is committed.** A small synthetic dataset with the same
   shape as Tier 1, so a clone renders offline.
3. **A pinned snapshot is not a reproducible pipeline.** Both are needed: the
   pin fixes the numbers in the text, the pipeline proves they can be rebuilt.
4. **Every constructed series carries its assumption in the code**, not in a
   comment — the duration used, the parity relation, the splice date.

## Layout

```
data/
  README.md      this file
  cache/         Parquet, gitignored, rebuilt from the pinned snapshot
  fallback/      committed synthetic dataset, renders without network
  raw/           gitignored scratch for downloads
```

---

## Second universe: the simulated market

Alongside the free real-data sleeves above, a **calibrated simulated market** is available at
`../simulated_data/`. It is generated from a factor model fitted to real index and yield history,
and it exists to do the one thing the real-data layer cannot: supply a counterfactual.

Five regions — US, Europe, UK, Switzerland, Japan — each with equities, government bonds, credit and
a money-market rate, plus eight commodities. 181 instruments, weekly and monthly from December 1991
to December 2022, **all in US dollars**. Licence-free: no series is the history of any real
security, and nothing licensed is redistributed.

| File | What |
|---|---|
| `assets.csv` | metadata: region, currency, class, sector, credit grade |
| `assets_weekly` / `assets_monthly` | weekly and monthly **total** returns, decimal, long form |
| `classes_weekly` / `classes_monthly` | 21 region x class series, `return` and a `index` rebased to 100 |

Each data file exists as `.csv` and `.parquet`. The monthly class file matches the shape `pm_data()`
returns — month-end dates, decimal simple returns — so the two universes are interchangeable in a
chapter.

Why it earns a place. Through the 2008/09 window, read as a dollar investor: US equities fall 43.6 %
while Treasuries rally 9.6 %; the yen surges, so Japanese government bonds *gain* 13.3 %; sterling
collapses, so gilts lose 15.7 % and sterling credit 31.6 % despite gilts rising in pounds. In 2022
both bond classes lose together, because that was a rates shock rather than a credit event. Credit
is negatively skewed where currency does not dominate — US credit at −1.30 against a volatility of
7.2 % but a drawdown of 18.5 %, which is the concrete case for why variance is the wrong risk
measure for credit.

Chapters that need a counterfactual — stress testing, backtesting failure modes, risk beyond
variance — should use this. Chapters about real markets should use the real sleeves. For credit
specifically, prefer the **US series**: elsewhere the unhedged currency dominates the third moment.

Three things to know before using it, all detailed in `../simulated_data/README.md`. Returns are
**total**, not excess. Everything is **unhedged dollars**, so a non-US bond carries roughly
two-thirds exchange-rate risk and a foreign money-market series is essentially a pure currency
position. And the factor paths are fixed, so this is one realised history rather than a distribution
over histories.
