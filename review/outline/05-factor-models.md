---
file: chapters/05-factor-models.qmd
title: Factor Models and Beta Estimation
part: Foundations of Portfolio Choice
words: 4429
sections: 5
paragraphs: 37
---

# Chapter

Claim: Most of what a single-factor regression appears to explain about this market does not survive proper measurement: the model fits only the equity blocks, its betas are mostly United States betas, the up/down split survives inference in two cases of sixteen, non-equity betas change sign in about a third of windows, and a global size factor sorts on region.
Question: What do the sixteen series have in common? Cites Sharpe, Lintner and Black for the model and Jensen for the regression form.
Why here: Stated as the continuation of chapter 4, which described the market one series at a time; takes the excess-return basis from chapter 3 and the instrument universe from chapter 2 for the proxy. Forward: chapter 8 is said to exist because a small beta's sign is unknown, chapter 19's regime allocation is said to need the turbulence index, and the appendix carries the package note. Why factor models precede the input estimation of the next part is not stated.
Does: Build a lagged capitalization-weighted market proxy, estimate alphas and betas with Newey-West errors, test an up/down split, construct and inspect a size factor, roll betas, and compute an out-of-sample turbulence index.
Order: Theory (model, variance split, two extensions, inference), implementation (proxy, one-factor fit, split beta, size factor, package callout), application under the title "How Much of This Survives" (rolling betas, turbulence), takeaways, exercises. Deviations: the implementation section already carries the chapter's main findings, one of the two tables and two of the four figures; the application section has no prose of its own and holds two further studies rather than an application of what was implemented; the packages block is a hidden setup chunk before the opening, not a shown block after the plan sentence; six takeaways and five exercises.

# Sections

## Opening — 208

Says: The chapter asks what the series share, names the single-factor model as the canonical answer, and announces that most of its explanation will not survive measurement.
Why here: Stated: chapter 4 described the market one series at a time; this chapter asks what the series have in common.
Paragraphs:
- (code: setup)
- ¶1 [claim] Chapter 4 did series one at a time; the shared part has a canonical answer: Sharpe-Lintner-Black, estimated as Jensen's regression.
- ¶2 [method] Plan in three steps, then the headline: most does not survive; sign flips, two asymmetries, a mislabeled factor.
Note: The setup chunk is hidden and precedes the opening; no visible packages block follows the plan sentence. ¶2 states three results before any is derived.

## The Single-Factor Model — 417

Says: The CAPM regression splits each asset's variance into a market part and a residual, so R² is the share of risk the model describes; two extensions let beta differ by market direction and move over time.
Why here: Stated in the opening: the model is set out before it is estimated. Needs the excess-return basis of chapter 3; supplies the four equations the implementation estimates and the table is read through.
Paragraphs:
- ¶1 [definition] Notation; excess returns throughout, per chapter 3; the regression (eq-05-capm) and the population beta (eq-05-beta).
- ¶2 [derivation] Alpha is zero under the theory, a residual as description; the variance split and R² (eq-05-variance-split).
- ¶3 [claim] R² is not decoration: it is the share of risk the model claims; low R² means nothing to say.
- ¶4 [definition] Two extensions: an up/down beta (Bawa-Lindenberg, Ang et al.; eq-05-asymmetric) and a time-varying beta (conditional CAPM), done by rolling windows.
Note: ¶4 defines both extensions in one paragraph; the second gets one sentence and no equation.

### Inference is where these models are usually lost — 130

Says: OLS standard errors are wrong for monthly returns, so Newey-West errors are used throughout, and sixteen repeated tests need them because repetition manufactures significance.
Why here: Stated: eq-05-asymmetric is estimated sixteen times, so the estimator is fixed before the first regression runs.
Paragraphs:
- ¶1 [method] Serial dependence and heteroskedasticity break OLS errors; the Newey-West estimator (eq-05-neweywest) with six lags is used throughout.
- ¶2 [claim] Sixteen repetitions will produce apparent differences regardless; Harvey, Liu and Zhu's argument applies to a table of betas.

## Implementation — 2139

Says: The market proxy is built from the 123 equity instruments with lagged capitalization weights, and three studies on it follow: the one-factor fit, the up/down split with its test, and a size factor that turns out to sort on region.
Why here: Stated: a factor model needs a factor, and the market has to be built from the instrument universe of chapter 2 because a capitalization weight exists only there; the proxy's composition is read before any beta is used.
Paragraphs:
- ¶1 [method] A factor needs building; the market comes from the instrument universe (chapter 2), since capitalization weights exist only there.
- (code: proxy)
- ¶2 [caveat] Weights are lagged one month on purpose: a weight observed at month end is not investable that month.
- (code: proxy-composition)
- ¶3 [result] The proxy is mostly United States by weight; every beta is largely a United States beta; Roll's joint-hypothesis reminder.
Note: The section's own prose only builds the proxy; its three subsections hold the chapter's main findings, so the implementation is already the application.

### One factor, sixteen series — 477

Says: The one-factor regression explains the four equity blocks and little else; the only significant alpha, on a government bond, is a sign of missing factors.
Why here: Not stated beyond the opening's plan; it is the first estimate and supplies `fit1` for the figure and the takeaways.
Paragraphs:
- (code: single-factor)
- (code: tbl-05-single-factor)
- ¶1 [result] Reads the table through the variance split: four series above one half, several near zero, one at nothing.
- ¶2 [result] The median R² is low; a one-factor model is an equity model applied to everything else.
- (code: fig-05-model-fit)
- (code: alpha-claims)
- ¶3 [result] Only US_government's alpha clears t = 2, US_credit next; a bond alpha against equity means wrong factors (Fama-French).
Note: The hidden `-claims` chunks here and below are assertions placed directly before the paragraph they guard. The figure plots the R² column the table already lists.

### Splitting the beta, and then testing the split — 635

Says: Up- and down-market betas can differ in sign where the unconditional beta is zero, but only two of sixteen splits survive a Newey-West test, and the credit one is not among them.
Why here: Stated: a single beta assumes the same slope up and down, so the split follows the single fit; the test follows the split because halving a sample manufactures differences.
Paragraphs:
- ¶1 [method] A single beta assumes one slope both ways; PerformanceAnalytics estimates both halves of eq-05-asymmetric in one call.
- (code: conditional-betas)
- (code: conditional-claims)
- ¶2 [result] JP_government's beta near zero hides a positive up beta and a negative down beta; the average destroys it.
- ¶3 [claim] The usually skipped step: an asymmetry must survive a test, since halving a sample produces differences by itself.
- (code: asymmetry-test)
- (code: asymmetry-claims)
- ¶4 [result] Two of sixteen survive, both government bonds; the Japanese one is real, the credit one is not.
- ¶5 [caveat] With this many down months, sixteen split betas will differ regardless; report the split, hedge only after the test.
- (code: fig-05-asymmetric)
Note: ¶3 and ¶5 make the same point, before and after the test; the figure closes the subsection after the reading rather than opening it.

### What a factor is actually sorting on — 666

Says: A global size sort in a five-region universe sorts on region and currency; it raises R² for that reason, while the region-neutral version carries the more reliable premium.
Why here: Stated: size is the second factor everyone reaches for after the market, and here a trap worth walking into deliberately; it reuses the proxy's weight matrix.
Paragraphs:
- ¶1 [method] Size is the second factor everyone reaches for (Fama-French); here a trap entered on purpose.
- (code: smb)
- ¶2 [transition] Before using either sort, look at what the global one placed in each leg.
- (code: smb-legs)
- ¶3 [result] The big leg is mostly United States, the small leg barely; the sort is on region, hence currency.
- ¶4 [transition] The consequence is measurable.
- (code: smb-r2)
- (code: smb-claims)
- ¶5 [result] The global factor lifts median R² more than the neutral one; the gain was regional composition, not size.
- ¶6 [claim] The neutral factor earns the more reliable premium; a factor is its construction; Griffin, Hou et al. on country factors.
- ¶7 [code] (callout) `table.CAPM()` returns alphas, betas, bull and bear betas, R² and ratios for many series at once.
- (code: table-capm)
- ¶8 [caveat] Use the table for the survey, the functions for the argument; it reports no error on the bull-bear gap.
Note: The callout and its chunk sit under the size heading but belong with the conditional betas one subsection back; the callout's `##` title reads as a section in a heading grep. ¶6 reads a result, states the lesson and places the literature in one paragraph.

## How Much of This Survives — 1193

Says: Betas move, outside equity they change sign in about a third of windows, and the movement itself can be measured without hindsight as a turbulence index.
Why here: Stated in the opening: after estimating, examine how much of the explanation survives proper measurement.
Paragraphs:
- (none: the heading is followed directly by its first subsection)
Note: The section carries no prose of its own; its two subsections are further studies, not an application of the implemented model.

### A beta is a time series — 610

Says: Sixty-month rolling betas travel furthest where they are smallest; every non-equity beta changes sign, the median in about a third of windows, and equity betas never do.
Why here: Stated: eq-05-beta is written as a constant and the conditional CAPM literature says it is not, so a rolling window shows how much it moves; the theory section announced rolling windows as the second extension. Points forward to chapter 8.
Paragraphs:
- ¶1 [method] Beta is written as constant; Ferson-Harvey and Jagannathan-Wang say otherwise; a rolling window shows the movement directly.
- (code: rolling-betas)
- (code: tbl-05-rolling)
- (code: rolling-claims)
- ¶2 [transition] Two patterns emerge; the second is the one to carry forward.
- ¶3 [result] The furthest-traveling betas are the smallest; US_equity near one barely moves and never flips (Blume).
- ¶4 [result] Every non-equity beta changes sign, the median in about a third of windows; US_government alone reliably negative.
- (code: fig-05-rolling-betas)
- ¶5 [claim] A small beta has an unknown sign; hence chapter 8, and a hedge ratio needs an error bar first.
Note: ¶2 announces two patterns that ¶3 and ¶4 then carry; the figure follows the reading of the table rather than opening the section.

### Measuring the instability itself — 576

Says: The Mahalanobis turbulence index, estimated out of sample on a trailing window, finds the peak month chapter 4 found by hand, in the credit crisis, and shows it was extreme moves within an ordinary correlation structure.
Why here: Stated: if the moments move, the movement is itself a quantity, so it follows the rolling betas; it asks chapter 4's hand-picked window question continuously, and chapter 19's regime allocation is said to need it.
Paragraphs:
- ¶1 [definition] Turbulence as Mahalanobis distance (eq-05-turbulence); Chow et al., Kritzman-Li; the implementation is a non-CRAN package, see appendix.
- (code: turbulence)
- ¶2 [method] `OSturbulence()` estimates moments strictly before each month, so the index never sees the month scored; the in-sample gap is look-ahead.
- (code: turbulence-peaks)
- (code: turbulence-claims)
- ¶3 [result] The peak lies in the credit crisis, far above the next; it is chapter 4's exceedance month, found without hindsight.
- ¶4 [definition] The correlation component is the ratio of the full distance to the variance-only distance.
- (code: correlation-turbulence)
- (code: correlation-turbulence-claims)
- ¶5 [result] The peak's ratio is ordinary: extreme moves, usual correlations (Forbes-Rigobon); chapter 4 chose windows by hand; chapter 19 needs this.
- (code: fig-05-turbulence)
Note: The index measures the returns' own instability, not beta's; the section's only link to the factor model is its first sentence. The figure closes the section after both readings.

## Key Takeaways — 252

Says: Six bullets restate the chapter's numbers: R² as risk share, the proxy's United States weight, two surviving asymmetries, the size sort's region bet, sign-changing betas, and hindsight-free turbulence.
Why here: not stated.
Paragraphs:
- ¶1 [takeaway] R² is the share of risk the model describes; the median is low; a one-factor model is an equity model.
- ¶2 [takeaway] The proxy is mostly United States by weight, so every beta is largely a United States beta (Roll).
- ¶3 [takeaway] Conditional betas: worth computing, rarely worth believing; two of sixteen survive, not the credit one.
- ¶4 [takeaway] A factor is its construction; the global size sort is a region bet under a size label (Griffin; Hou).
- ¶5 [takeaway] Betas move; equity betas keep their sign, non-equity betas flip in a third of windows (Blume).
- ¶6 [takeaway] Instability is measurable without hindsight; turbulence picks the credit-crisis peak and separates correlation from volatility (Chow; Kritzman).
Note: Six bullets against the contract's "around five"; each re-reads a number from the chapter through inline R and carries a citation.

## Exercises — 186

Says: Five exercises: an equal-weighted proxy, separate up/down regressions, rolling betas against turbulence, the `s.k` window of `OSturbulence()`, and multiple-testing corrections on the asymmetry p-values.
Why here: not stated.
Paragraphs:
- ¶1 [exercise] Rebuild the proxy with equal weights; which betas move, does the rolling ranking survive, what "the market" means.
- ¶2 [exercise] Replace the interaction term with separate up and down regressions; same estimates, different errors; which is honest.
- ¶3 [exercise] Plot the two most sign-flipping betas against turbulence; does beta move with turbulence or independently.
- ¶4 [exercise] Vary `OSturbulence()`'s `s.k` from 1 to 12; describe what the index measures at each end.
- ¶5 [exercise] Apply Bonferroni and Benjamini-Hochberg to the sixteen asymmetry p-values (Harvey et al.); how many survive.
Note: Five exercises against the contract's "around three"; exercise 3 is the one place the chapter links rolling betas to turbulence.
