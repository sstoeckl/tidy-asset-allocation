---
file: chapters/06-expected-returns.qmd
title: Expected Returns
part: Estimating the Inputs
words: 7565
sections: 5
paragraphs: 57
---

# Chapter

Claim: No history pins an expected return down, so the book sets its strategic vector on the equilibrium where market weights exist and on Bayes-Stein where they do not, and keeps the sample mean only as the benchmark that moves the portfolio most.
Question: How precisely can a mean return be known, and which vector should a long-run policy be set on; cites Merton (1980) in the second sentence.
Why here: Names itself the hard input of chapter 9 against the large one of chapter 7; takes the data from chapter 2, the excess basis and the strategic/tactical vocabulary from chapter 3, the precision formula and the instability figure from chapter 4, the lagged weights and the CAPM from chapter 5; uses chapter 9's problem, tangency and GMV equations throughout as if already read; hands the vector to 8 (cost), 16 (benchmark forecast), 17 (prior), 23 (turnover priced), 26 (derivation). Why it precedes chapter 7 inside the part: not stated.
Does: Build the precision table for any return panel; implement Bayes-Stein and reverse optimization; pass any mean vector into `optimize.portfolio()` through `momentFUN` and assert it was used; compare estimators by how far they move on rolling windows.
Order: Theory (precision, target, shrinkage, equilibrium), implementation (Bayes-Stein, equity equilibrium plus a proxy box, the package route and its traps), application (three tangency portfolios, rolling stability, what is carried forward), takeaways, exercises. Deviations: the theory section runs code and reads numbers twice (the frequency callout, the target subsection); the implementation ends in a run of package caveats rather than an estimator; the application closes with a conclusion subsection the takeaways then repeat; six takeaways, four exercises.

# Sections

## Opening (untitled) — 349

Says: Expected returns are the imprecise input, this chapter is about the strategic vector, and here is the sequence.
Why here: Contract position; the text says the chapter measures first and offers alternatives after.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Every optimizer needs μ; by Merton the standard error falls only with calendar span, so premia stay open.
- ¶2 [method] Strategic μ in chapter 3's sense; forecasts go to 16, views to 17; the chapter's five steps named.
- ¶3 [method] Data: the sixteen class series of chapter 2, in excess of the bill as chapter 3 argued.
- (code: data)
Note: The "packages used" block the contract asks for is hidden (`include: false`), so the reader sees no package list.

## How Precisely a Mean Can Be Known — 2141 (907 before the subsections)

Says: The standard error of a mean depends on calendar span alone, and on this sample most of the sixteen intervals include zero.
Why here: The text says the table these formulas produce "is the right way to begin" a chapter on expected returns; needs eq-04-precision; the target, shrinkage and equilibrium subsections respond to the imprecision measured here.
Paragraphs:
- ¶1 [derivation] Defines μ̂, Σ̂; se = σ/√τ, the 95 percent interval, years to exclude zero; the table begins the chapter.
- (code: precision)
- (code: precision-picks) hidden assertions on the best and worst rows
- (code: tbl-06-precision)
- ¶2 [example] Best case worked with numbers; most intervals include zero; Fama–French agree; chapter 4's rolling mean; estimators manage, not remove.
- ¶3 [method] (callout) Weekly panel: same span, four times the resolution; eq-04-precision predicts a gain for the variance only.
- (code: frequency)
- ¶4 [result] (callout) Mean standard error unchanged, variance's cut as √T predicts; why chapter 7 can estimate from the same history.
Note: The ## title names only the first subsection's topic; the chapter's two estimators sit under a heading about precision. ¶2 does four jobs (worked case, headline count, literature, pointer to chapter 4).

### A target set on a sample mean — 395

Says: A return target set on a sample mean is a constraint on noise that the optimizer honors exactly, and the literature on the consequence is old and consistent.
Why here: Needs the interval width of tbl-06-precision; shows the cost of the imprecision just measured before any remedy; the text says one sentence per citation suffices because chapter 9 already used them; hands the cost to chapters 8 and 26.
Paragraphs:
- ¶1 [method] Chapter 9's target at the upper quartile of sample means is met to solver tolerance on an imprecise input.
- (code: target)
- ¶2 [result] Target held to eight decimals while a mean that size is known only within a band of points.
- ¶3 [evidence] Jobson–Korkie to DeMiguel, one sentence each; Kan–Zhou's three-fund rule previewed; cost measured in 8, derived in 26.
Note: A worked number (¶1–2) and a seven-citation literature paragraph (¶3) share one subsection; ¶3's closing Kan–Zhou pointer is what the next subsection builds on.

### Shrinkage of the mean — 401

Says: Bayes-Stein shrinks every mean toward the minimum-variance return with an intensity the data set, which moves the tangency portfolio toward the minimum-variance portfolio.
Why here: "The response from statistics predates all of that": the first alternative, offered after the cost paragraph; relies on chapter 9's tangency and GMV equations and on chapter 7's shrinkage form.
Paragraphs:
- ¶1 [definition] Stein to Jorion: shrink toward the minimum-variance return μ0 with intensity v; eq-06-bayes-stein.
- ¶2 [claim] v is set by the data: small when means differ, near one when not, zero as T grows; as chapter 7.
- ¶3 [derivation] The map is linear, so the shrunk tangency mixes tangency and GMV directions; other targets cited; this needs only Σ̂.

### Equilibrium returns by reverse optimization — 438

Says: Reverse optimization reads the μ for which the market portfolio is optimal from Σ and market weights; its weakness is that the weights exist for five classes only.
Why here: "The third route asks a different question": ordered as the last alternative; needs appendix B's first-order condition and chapter 5's CAPM; is the prior chapter 17 blends views into; sets up the five-class demonstration and the proxy box.
Paragraphs:
- ¶1 [definition] Sharpe, Black–Litterman, CAPM: the first-order condition gives μ_eq = δΣw_mkt.
- ¶2 [derivation] δ is the market's mean over variance, frequency-free; He–Litterman, Satchell, Idzorek; views deferred to chapter 17.
- ¶3 [claim] Three properties: not a forecast, returns the market by construction; δ sets scale only; `risk_aversion` is δ/2.
- ¶4 [caveat] Roll: the market is unobservable; capitalizations exist for equities only, so a five-class case plus a proxy box.
Note: ¶3 bundles a package convention (γ/2) with two theory properties; the convention returns as its own paragraph and chunk in the implementation.

## Three Estimators in Code — 2733

Says: Bayes-Stein in a function, equilibrium returns from capitalizations, and the `momentFUN` route that puts any vector into `PortfolioAnalytics`.
Why here: Only the opening's sequence sentence ("then implement both and show how the package takes a mean vector it did not compute"); the section itself has no paragraph.
Paragraphs: none of its own.
Note: Heading only. "Three estimators" covers two implementations (the sample mean needs none) and a third subsection that is package plumbing and traps, not an estimator.

### Bayes-Stein in a few lines — 527

Says: The estimator in a function; v near one half removes more than half the distance, halves the spread and keeps every rank.
Why here: eq-06-bayes-stein needs μ̂, Σ̂, N, T "and nothing else", so it comes first, on the data chunk alone.
Paragraphs:
- ¶1 [method] Inputs are μ̂, Σ̂, N, T; Jorion's unbiased scaling of Σ̂ moves v at the second decimal.
- (code: bayes-stein)
- ¶2 [example] v and μ0 read; US_equity with the numbers substituted: more than half the distance removed, every series alike.
- (code: shrinkage-frame)
- (code: fig-06-shrinkage)
- ¶3 [result] Spread roughly halved, rank correlation one because the map is linear with positive slope; differences change, order not.

### Equilibrium returns for the five equity classes — 1139

Says: Lagged capitalization weights give δ and an equilibrium vector that is beta times the market premium, within one standard error of every sample mean; a proxy extends it to sixteen classes.
Why here: "The clean case first": the weights exist for equities; the proxy box follows because the application needs all sixteen.
Paragraphs:
- ¶1 [method] A class's weight is its instruments' capitalization sum, lagged one month as in chapter 5.
- (code: market-weights-equity)
- ¶2 [result] Composition drifts in the US share as chapter 5 found; average composition used; δ from the market's own return.
- (code: equilibrium-equity)
- ¶3 [example] δ with the sample numbers substituted; one equilibrium return per class follows.
- (code: equity-comparison)
- (code: tbl-06-equilibrium-equity)
- ¶4 [result] Each element is beta times the premium, the CAPM as prior; all within one standard error; JP up, US down.
- ¶5 [caveat] (callout, collapsed) World wealth split 40/40/15/5 is an assumption, a placeholder for a capitalization survey.
- (code: market-weights-proxy)
- ¶6 [result] (callout) Bond-heavy proxy doubles δ; US_government assigned far below its sample mean; right only if the split is.
Note: The collapsed box the text calls a placeholder (with an open `SS:` comment) builds `mu_eq`, `delta16` and `W16`, which the γ/2 check, the three-portfolio comparison and the rolling table all run on. ¶4 derives the beta form after the table that it reads.

### The moments as PortfolioAnalytics sees them — 1061

Says: `set.portfolio.moments()` offers four methods, none of them Bayes-Stein; a custom `momentFUN` supplies any vector, and four package behaviors (`maxSR`, `black.litterman()`, `match.call()`, γ/2) are measured.
Why here: After the two vectors exist, the route into the package, "the one chapter 7 used for a shrunk covariance"; the γ/2 check closes the property promised in the theory's ¶3.
Paragraphs:
- ¶1 [method] One function computes every moment; its `method` argument selects the estimator.
- (code: moments-sample)
- ¶2 [caveat] Four methods, routed to chapters 11 and 17; none is Bayes-Stein or takes a weight; `momentFUN` is chapter 7's route.
- (code: momentfun)
- ¶3 [code] The assertion confirms the shrunk moments were used; `maxSR` asks for the tangency directly.
- ¶4 [caveat] (callout) CRAN's `maxSR` discards the supplied mean silently; the book runs the patched build; on CRAN use the frontier; assert.
- ¶5 [method] `black.litterman()` with the prior alone should return the prior; it does, plus an object needing care.
- (code: black-litterman)
- ¶6 [caveat] (callout) Four behaviors of `black.litterman()` are measured rather than documented.
- (code: bl-defaults)
- ¶7 [caveat] (callout) No weights or δ, no τ, a bullish default view lifting every mean, and `BLSigma` at Σ/2 reaching the optimizer.
- ¶8 [caveat] `match.call()` hands `set.portfolio.moments()` the typed expression, not the value.
- (code: bl-matchcall)
- ¶9 [result] Direct call stops on the symbol; through `optimize.portfolio()` the mean is honored, Σ halved; custom `momentFUN` has neither problem.
- ¶10 [method] The γ/2 convention: feeding μ_eq back tests the vector and the convention together.
- (code: gamma-half)
- ¶11 [result] At δ/2 the proxy market returns to solver precision; at δ a weight is off by points.
Note: Eleven paragraphs, six of them caveats, under a title about moments. ¶5–9 (two chunks, one callout) test `black.litterman()`, a function ¶2 has just routed to chapter 17; the γ/2 check (¶10–11) verifies a theory property and uses the proxy vector.

## What the Three Vectors Buy — 1897

Says: On one tangency problem the sample and Bayes-Stein vectors concentrate and churn; the equilibrium returns the market and turns over only as capitalizations drift.
Why here: The opening's last clause ("feed the three vectors to the same tangency problem to see what each buys and how much each moves"); needs `mu_eq` from the proxy box and `make_moments()` from the γ/2 chunk.
Paragraphs: none of its own.
Note: Heading only; the three subsections are comparison, stability, conclusion.

### Three tangency portfolios — 1127

Says: The sample and Bayes-Stein portfolios hold a handful of series, Bayes-Stein the more concentrated in the GMV's series; the equilibrium holds all sixteen and is the market.
Why here: "The same long-only tangency problem that chapter 9 solved" is solved three times with Σ̂ fixed so only μ changes; the assertion is "the guard the callout asked for".
Paragraphs:
- ¶1 [method] Chapter 9's long-only tangency problem solved on three vectors with Σ̂ fixed so only μ changes.
- (code: tangency)
- ¶2 [code] Second assertion: sample and Bayes-Stein differ, so the means were used; third: equilibrium returns the market.
- ¶3 [derivation] (callout, collapsed) Scale invariance: minimize variance at unit return, rescale; one QP, cheap for rolling windows.
- (code: tangency-check)
- ¶4 [result] (callout) Both routes agree in every weight: the check that patched `maxSR` solves the stated problem.
- (code: summary)
- (code: summary-checks) hidden; reads the chapter-25 register from `oos-sweep.csv`
- (code: tbl-06-weights)
- (code: weights-frame)
- (code: fig-06-weights)
- ¶5 [result] Sample holds few series, promises the most by construction; Bayes-Stein more concentrated in the GMV's series: leans on Σ̂.
- ¶6 [result] Equilibrium holds all sixteen; in-sample Sharpe is the wrong yardstick; chapter 9's out-of-sample table; what matters is movement.
Note: Five chunks run between ¶4 and ¶5 with no prose. The collapsed QP box defines `tangency_lo()`, which the rolling subsection depends on, so a box a reader may skip is load-bearing. ¶6's out-of-sample number is borrowed from chapters 9 and 25.

### Which vector moves least — 541

Says: On rolling sixty-month windows the sample mean moves most, Bayes-Stein less and the equilibrium least, and the implied turnover follows the same order.
Why here: ¶6 above: "what matters for a strategic allocation is how much each answer moves when the sample does"; uses chapter 25's window; hands the cost to chapter 23.
Paragraphs:
- ¶1 [method] Re-estimate the three vectors on every sixty-month window, chapter 25's; measure vector moves and turnover; δ fixed.
- (code: rolling)
- (code: tbl-06-rolling)
- ¶2 [result] Sample moves most, Bayes-Stein less, equilibrium least, at the rate capitalizations drift; chapter 23 prices the gap.

### What the book carries forward — 222

Says: The book carries the equilibrium as anchor where weights exist, Bayes-Stein where they do not, and the sample mean as the benchmark.
Why here: Closes the comparison with the decision later chapters use (17's prior, 8's cost, 16's benchmark); no other reason given.
Paragraphs:
- ¶1 [claim] Restates the three: sample unknown and rebuilt monthly; Bayes-Stein leans on the GMV; equilibrium only as good as its weights.
- ¶2 [claim] Two carried: equilibrium as chapter 17's anchor where weights exist, Bayes-Stein otherwise; sample mean as chapter 8's benchmark.
Note: A conclusion subsection directly before Key Takeaways; the sixth takeaway repeats ¶2's decision almost verbatim, and ¶1 repeats the readings of the two subsections before it.

## Key Takeaways — 266

Says: Six bullets.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Precision depends on span alone; most intervals include zero; weekly sampling helps the variance only.
- ¶2 [takeaway] A target on a sample mean is honored to machine precision on noise; chapter 8 measures the cost.
- ¶3 [takeaway] Bayes-Stein shrinks toward the GMV return at a data-set v, keeps the order, moves toward the GMV.
- ¶4 [takeaway] Reverse optimization returns the vector making the market tangent; δ scales only; `risk_aversion` is δ/2.
- ¶5 [takeaway] `black.litterman()` is the formula only: no weights, no τ, bullish default view, halved covariance.
- ¶6 [takeaway] Rolling turnover ranks sample, Bayes-Stein, equilibrium; the book carries equilibrium where weights exist, Bayes-Stein elsewhere.
Note: Six against "around five"; ¶5 is a package trap rather than a chapter claim; ¶6 restates the subsection before.

## Exercises — 179

Says: Four exercises.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Replace μ0 with the plain average of sample means; does the tangency still move toward the GMV?
- ¶2 [exercise] Reverse-optimize the five equity classes on last month's weights; report moves in standard errors by region.
- ¶3 [exercise] Change the proxy split to 60/25/10/5; which μ_eq entries move; is the proxy still the tangency portfolio?
- ¶4 [exercise] Recompute the rolling table on 120-month windows; does the ranking change; does turnover fall as eq-06-se predicts?
Note: Four against "around three"; ¶3 works on the proxy the text calls a placeholder.
