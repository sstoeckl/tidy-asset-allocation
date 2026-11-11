---
file: chapters/04-descriptive-analysis.qmd
title: Descriptive Analysis of Asset Returns
part: Foundations of Portfolio Choice
words: 4740
sections: 5
paragraphs: 47
---

# Chapter

Claim: Volatility is the only moment this market lets us estimate with confidence, and the two things that shape every portfolio, tails that arrive as market-wide events and a currency share that belongs to the asset rather than the country, are invisible in a table of moments.
Question: Which of the known regularities of financial returns hold in the modeled market, and which of the numbers the book is about to rely on can be estimated at all; cited to Mandelbrot (1963), Fama (1965) and Cont (2001).
Why here: Every later chapter does something to a return series, the text says, and none of that is interpretable or trustworthy without this one; it takes the modeled market from chapter 2 and the tidy-to-matrix boundary from chapter 1, and it says the mean–variance asymmetry splits chapters 6 and 7, that chapter 10 settles the risk-measure question, chapter 15 the hedge per sleeve, chapter 25 the per-episode reporting, and that Part IV's optimizers are bounded by its two properties.
Does: Compute and read the annualized moments on the modeled market, test normality, compare two expected-shortfall estimators, judge each moment on rolling windows, read drawdown episodes, count joint exceedances, compare the four episodes, and split a foreign series' variance into local and currency parts.
Order: Theory, implementation, application, takeaways, exercises, as the contract has it; but the implementation reads every result it computes and carries both tables and two of the three figures, so it is the first application, the section titled as the application holds the chapter's only derivation outside the theory (@eq-04-fx), and the mean–volatility picture closes the implementation's first subsection instead of opening the application.

# Sections

## Opening (untitled, before the first heading) — 354

Says: The chapter asks which known regularities of returns hold in this market and which of its numbers can be estimated at all.
Why here: The text says every later chapter works on a return series and nothing downstream is interpretable or trustworthy without this.
Paragraphs:
- (code: setup)
- ¶1 [claim] Later chapters all act on return series; returns are non-Gaussian since Mandelbrot and Fama; which regularities hold here?
- ¶2 [method] Set out the moments and their precision, compute them, then two properties: tails as events, currency as asset property.
- ¶3 [definition] The data: chapter 2's modeled market, sixteen risky classes, 372 months, dollars unhedged, money markets beside, bill as risk-free.
Note: The annualization convention (geometric return, volatility scaled by the root of the frequency, Sharpe over the bill) lives only in a comment inside the hidden setup chunk; the prose never states it.

## What Can Be Estimated — 545

Says: The four sample moments are not four facts of the same kind, and that difference is the chapter's most consequential point.
Why here: Not stated as such; ¶2 announces the asymmetry as the chapter's most consequential point, which the implementation then measures, and the opening promised theory before computation.
Paragraphs:
- ¶1 [definition] Defines r_t and the four sample moments: mean, variance, skewness, excess kurtosis (@eq-04-moments12, @eq-04-moments34).
- ¶2 [claim] Reported side by side as if alike; they are not, and the difference is the chapter's most consequential point.

### The mean is the moment that does not improve — 190

Says: The mean's precision depends on the calendar span, the variance's on the number of observations; the higher moments are worse.
Why here: It rates the moments just defined; the text says this asymmetry is what splits chapter 6 from chapter 7, and the rolling-window subsection later makes it concrete.
Paragraphs:
- ¶1 [derivation] Under independence, standard errors of mean and variance over span τ at interval Δ (@eq-04-precision).
- ¶2 [claim] Finer sampling helps the variance, not the mean; Merton's point; why chapters 6 and 7 differ in difficulty.
- ¶3 [claim] Skewness and kurtosis are worse: one extreme observation can outweigh the rest of the sample.

### Testing normality rather than assuming it — 245

Says: Jarque–Bera tests normality; whether it matters depends on the quantity, and for the tail the Cornish–Fisher correction prices the normal assumption.
Why here: Not stated; it supplies the statistic and the two expected-shortfall estimators that the implementation's distribution test applies.
Paragraphs:
- ¶1 [definition] The Jarque–Bera statistic (@eq-04-jb); a specification test, not a model; rejection says only that shape exceeds sampling error.
- ¶2 [definition] Normality hardly matters for variance, decides a tail quantile; VaR and ES (@eq-04-es); ES preferred as coherent (Artzner, Acerbi).
- ¶3 [definition] ES from the sample tail or a Cornish–Fisher quantile (@eq-04-cornish-fisher; Favre, Boudt); the package default; the gap prices normality.
Note: ¶2 both defines two risk measures and argues the preference for one; the Sharpe ratio and maximum drawdown, two columns of the next table, are defined nowhere in this section.

## Implementation — 1,920

Says: Three package tables carry the book; once in `xts`, the moments table, the normality test, the rolling windows and the drawdown episodes each yield a reading.
Why here: The text says the three tables' shape is what everything else expects and that PortfolioAnalytics needs the matrix form; the boundary is the one chapter 1 establishes.
Paragraphs:
- ¶1 [method] Three tables carry the whole book, and their shape is what everything else expects.
- (code: universe)
- ¶2 [result] Sixteen risky series, 372 complete months, no gaps; 181 instruments underneath, the universe of Part VI's sleeve chapters.
- ¶3 [caveat] PortfolioAnalytics wants a wide `xts` matrix and will not convert on the reader's behalf.
- (code: to-xts)
- ¶4 [method] That is chapter 1's tidy-to-matrix boundary; the book crosses it explicitly every time, never through a helper.
Note: At about 1,900 words this section is the chapter's analytical centre: it computes and reads every result, holds both tables and two of the three figures, and runs to nearly twice the length of the section titled as the application.

### The moments — 610

Says: Three features of the moments table matter: return and Sharpe rankings differ, the money market is not the risk-free rate, and currency is first-order.
Why here: Not stated; the table is where the three features are read, and ¶2 and ¶6 each defer their question to the application section (¶2 also to chapter 10).
Paragraphs:
- (code: moments)
- (code: tbl-04-moments)
- (code: moments-claims)
- ¶1 [transition] Three features of the table matter for what follows.
- ¶2 [result] US credit earns under half US equity's return yet ranks third on Sharpe; whether that is better waits for chapter 10.
- ¶3 [claim] The money market is not the risk-free rate; it is a three-month instrument marked off a fitted curve.
- (code: mm-not-bill)
- ¶4 [result] Tracks the bill but loses in a fifth of months; hence money markets are assets and the bill is the risk-free rate.
- ¶5 [claim] Currency is a first-order driver: the four foreign money markets have volatilities near ten percent.
- (code: mm-currency)
- ¶6 [claim] Unhedged, a three-month instrument is nearly pure currency, and that currency sits inside every foreign series; taken apart later.
- (code: fig-04-risk-return)
Note: The mean–volatility scatter closes the subsection after the three features and no paragraph reads it; the Sharpe ratio and the maximum-drawdown column appear here before either is defined; ¶4 ends in a book-wide convention (the bill as the risk-free rate everywhere) stated inside a result paragraph.

### Testing the distribution — 470

Says: Every series rejects normality, but volatility and non-normality are different properties, and the cost of the Gaussian assumption is concentrated in credit.
Why here: It applies @eq-04-jb from the theory and reads the shape columns of the moments table; the text says the Cornish–Fisher table puts a number on what credit's non-normality costs.
Paragraphs:
- ¶1 [claim] Jarque–Bera gives one verdict and sixteen very different statistics, in an order intuition does not suggest.
- (code: normality)
- (code: normality-claims)
- ¶2 [result] All sixteen reject; JP equity, second most volatile, is second nearest Gaussian; US credit, half as volatile, far from it.
- ¶3 [result] The three largest statistics are credit series; the Cornish–Fisher expansion prices what that costs.
- (code: tbl-04-tails)
- ¶4 [result] Historical and modified ES disagree widely for US credit, barely for US equity; and credit ranked third on Sharpe.
- ¶5 [caveat] (callout) `ES()` defaults to the Cornish–Fisher estimate, a defensible default rarely noticed; check which estimator a reported figure used.
Note: The callout follows code that already names both methods explicitly, so it explains the code rather than catching the reader before the trap.

### How well each moment is estimated — 450

Says: On sixty-month windows volatility is stable, the mean wanders by more than its own level, and skewness often reverses sign.
Why here: The text calls it the practical counterpart of @eq-04-precision and the statement the book leans on repeatedly.
Paragraphs:
- ¶1 [method] @eq-04-precision holds under independence; the practical counterpart is what a rolling window would have told an investor.
- (code: instability)
- (code: instability-claims)
- ¶2 [result] Rolling volatility never flips sign and moves little; the rolling mean moves by more than its level; skewness flips sign often.
- ¶3 [claim] That is the precision result made concrete: volatility is estimable, the mean is not, skewness regularly reports the opposite.
- (code: fig-04-instability)
Note: The figure closes the subsection after the claim and no paragraph reads it; the subsection sits third in the implementation although it is the direct empirical counterpart of the theory's first subsection.

### Drawdowns are episodes, not a number — 195

Says: A single maximum drawdown hides what matters, the episodes and their recovery, which the episode table returns for one extra argument.
Why here: Not stated; the text calls maximum drawdown the investor's first question, yet it comes last in the implementation, after the column has already appeared in the moments table.
Paragraphs:
- ¶1 [claim] Maximum drawdown is asked for first; the one-call answer discards most of what the reader needs.
- (code: drawdowns)
- ¶2 [code] `table.Drawdowns()` returns each episode's start, trough, end and recovery length; NA means never recovered.
- (code: unrecovered)
- ¶3 [result] Several series end the sample inside their deepest drawdown; a depth alone cannot separate them from a quickly recovered one.
Note: Maximum drawdown was tabulated as a single number in @tbl-04-moments three subsections earlier; the point made here is that the single number is inadequate.

## Two Properties That Shape Every Portfolio — 1,385

Says: Two properties invisible in a moments table, tails as market-wide events and currency as an asset-level share, decide what Part IV's optimizers can achieve.
Why here: The text says neither property is visible in a table of moments, so they come after the tables, and that both bound the optimizers of Part IV.
Paragraphs:
- ¶1 [transition] Neither property shows in a moments table; both decide what the optimizers of Part IV can achieve.
Note: The title and the opening promise two properties; the section delivers three subsections, and the middle one, the four episodes and their correlations, is the longest in the chapter.

### Fat tails are events, not a distribution — 340

Says: The market's fat tail is a handful of months in which much of the market moves at once, not sixteen independent fat tails.
Why here: The text ties it to the per-series kurtosis of @tbl-04-moments, which invites the wrong reading, and calls it the joint counterpart of what @eq-04-jb detected.
Paragraphs:
- ¶1 [claim] Per-series kurtosis invites reading each tail as independent; wrong, and it matters because shared tails do not diversify.
- (code: clustering)
- ¶2 [result] Months with five or more series beyond 2.5 standard deviations far exceed the independence count; a different phenomenon.
- (code: worst-month)
- ¶3 [result] The worst month, in the credit crisis, moved most of the market at once; hence Longin and Solnik's tail correlations.
- (code: fig-04-outliers)
Note: ¶3 places the worst month in the credit crisis and points to the next subsection for it, so an episode is used one subsection before it is introduced; the heat-map closes the subsection unread.

### The crises are not one crisis — 615

Says: The four episodes differ economically, so a diversification rule learned in one reverses in another, and correlation rises in two of them and falls in the equity bear market.
Why here: The text says the book keeps the four episodes apart throughout and that chapter 25 therefore reports them separately; the correlations restate the episode result in the form an optimizer feels.
Paragraphs:
- ¶1 [method] Four episodes kept apart throughout the book, shipped as `sim_episodes`, named for what happens, tabulated in appendix A.
- (code: episodes)
- (code: episodes-claims)
- ¶2 [result] Credit fell with equity in one decline and rose with bonds in the other; every bond lost in the rates shock.
- (code: rates-winners)
- ¶3 [claim] The commodity index, a rates-shock winner, had lost in the credit crisis; a rule from one episode reverses in another.
- ¶4 [transition] The correlation matrix says the same thing in the form an optimizer will feel.
- (code: regime-correlations)
- (code: regime-claims)
- ¶5 [result] Correlation rises in the credit crisis and rates shock, falls in the equity bear market; calm diversification fails when needed.
- ¶6 [caveat] Short episodes give descriptions, not estimates; the rise is partly mechanical (Forbes–Rigobon); cumulative returns carry more weight.
Note: Two topics in one subsection, episode returns and regime correlations, joined by a one-sentence transition; the correlation half ends in a caveat that discounts its own evidence in favor of the first half's.

### Currency is not one decision — 390

Says: How much of a foreign series is currency depends on the asset, not the country, because local return and currency covary differently for bonds and equities.
Why here: Set up by the moments subsection, which found the same currency inside every foreign series and promised the application would take it apart; the text hands the per-sleeve hedge on to chapter 15.
Paragraphs:
- ¶1 [claim] Everything is unhedged in dollars; the currency share depends on the asset rather than the country, the non-obvious part.
- (code: currency)
- (code: currency-claims)
- ¶2 [result] Hedging the Japanese government bond removes most of its volatility; hedging Japanese equity removes nothing and adds a little.
- ¶3 [derivation] Unhedged return as local return plus currency; the variance splits into local, currency and twice their covariance (@eq-04-fx).
- ¶4 [result] Independence would give the `if_indep` share; Japanese equity falls short of it (negative covariance), EU credit exceeds it.
- ¶5 [evidence] Campbell et al. find the same bond–equity split; hedging is chapter 15's per-sleeve question; Perold–Schulman and Black oppose.
Note: The chapter's only derivation outside the theory section, and it comes after the code that computes the quantities it explains; the columns `fx_share` and `if_indep` are printed and read before ¶3–¶4 say what they are.

## Key Takeaways — 265

Says: Six bullets: the moment asymmetry in theory and on rolling windows, non-normality apart from volatility, tails as events, episodes not one crisis, currency as an asset property.
Why here: Not stated (contract position).
Paragraphs:
- ¶1 [takeaway] The four moments differ in kind: mean precision from the calendar span, variance from the observation count (Merton).
- ¶2 [takeaway] On rolling windows volatility never flips sign and moves little; the mean moves more than its level; skewness reverses often.
- ¶3 [takeaway] Non-normality and volatility are unrelated: all series reject, JP equity nearly Gaussian, US credit's two ES estimates far apart.
- ¶4 [takeaway] Fat tails are events: joint exceedances independence would produce once in many samples; shared tails do not diversify.
- ¶5 [takeaway] The four episodes are not one crisis; correlation rises in two, falls in the equity bear; short-window rises partly mechanical (Forbes).
- ¶6 [takeaway] The currency share belongs to the asset: hedging the Japanese bond removes most volatility, Japanese equity none (Campbell).
Note: Six bullets against the contract's "around five"; the money-market finding and the drawdown subsection have no bullet, and bullets 1 and 2 state one result twice, once in theory and once in measurement.

## Exercises — 195

Says: Five exercises: weekly moments, exceedance thresholds, skewness of a combination, hedged correlations, precision by simulation.
Why here: Not stated (contract position).
Paragraphs:
- ¶1 [exercise] Recompute the moments table on weekly data; which columns change and why, via @eq-04-precision.
- ¶2 [exercise] Repeat the joint-exceedance count at thresholds 2, 3 and 4; where does the dependence live.
- ¶3 [exercise] Combine two similar-volatility, opposite-skew series equally; is the skewness the average, and why not.
- ¶4 [exercise] Hedge all sixteen series and recompute average correlation by regime; does hedging change diversification or only volatility.
- ¶5 [exercise] Verify @eq-04-precision by simulation at monthly and weekly frequency, 1,000 draws.
Note: Five against the contract's "around three"; exercise 3 asks about the skewness of a mixture, which no section of the chapter works through.
