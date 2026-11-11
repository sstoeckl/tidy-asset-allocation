---
file: chapters/08-estimation-error.qmd
title: Estimation Error and Its Cost
part: Estimating the Inputs
words: 7979
sections: 5
paragraphs: 51
---

# Chapter

Claim: What an input costs is set by how well it can be estimated; the mean cannot be, so the rule that estimates it promises most and delivers least, while the rules that estimate only the covariance keep most of their promise and lead the register.
Question: How much is a better forecast worth, in Sharpe ratio; the opening cites @demiguel2009 for asking it the other way round (none of fourteen optimizing rules beat 1/N reliably), with the line from @jobson1980 to @ledoit2004 behind it.
Why here: The text says ch. 6 and ch. 7 estimate the mean and the covariance separately and this chapter measures what they cost together and which costs more; it takes the objective from ch. 3, the tangency and minimum-variance solutions and their quadratic programs from ch. 9 one chapter ahead, the precision result from ch. 4, the condition number from ch. 7, and the rolling scheme and the register from ch. 25; it says ch. 26 and ch. 27 take the forecast-error measure from it, ch. 14 treats inverse volatility in its own right, and ch. 19 and ch. 28 take up the drift it cannot price.
Does: Measure a rule's Sharpe gap on rolling windows against the equal-weight control; split an estimated portfolio's loss between the mean and the covariance by substitution under a simulated truth; locate the window at which a plug-in rule overtakes 1/N on a given universe; call the two naive rules directly rather than through the rebalancing loop.
Order: Opening (question, roadmap, data), theory (the plug-in rule, the two naive rules, inflation and expected loss with a worked callout, the gap defined), implementation (the naive rules and their trap, the two quadratic programs, the rolling loop with a cross-check against the register, the gap table and figure), application (a simulated truth, the two channels, forecast error in the investor's units, the crossover region, the register line), takeaways, exercises. Deviations: the theory section takes its portfolios and programs from ch. 9 and derives nothing itself; the application opens with a method paragraph and three numbers, not with a picture; the chapter's first result arrives at the end of the implementation section; the forecast-error subsection is a one-paragraph pointer to Part VIII placed between the channel split and the crossover; seven takeaways and four exercises.

# Sections

## Opening, before the first section — 493

Says: Estimation error is the oldest problem in portfolio theory, and this chapter measures what it costs a strategic allocator on the sixteen class series.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections and no reason for the chapter's place in the part.
Paragraphs:
- (code: setup)
- ¶1 [claim] The question; DeMiguel's thousands of months; ten citations trace the line from Jobson–Korkie to Ledoit–Wolf.
- ¶2 [method] Strategic allocation, unconditional moments; roadmap: benchmarks and known loss, the gap on rolling windows, a simulation splitting the loss.
- ¶3 [method] The data: the sixteen risky class series of ch. 2, in excess of the bill as ch. 3 argues.
- (code: data)
Note: ¶1 is one block of eleven citations, each with its finding, and the chapter's own question returns only in ¶2's roadmap; the data chunk already computes the full-sample moments the application will treat as the truth, two sections before the text says so.

## The Plug-In Rule and the Price of Its Inputs — 1729

Says: The plug-in rule substitutes sample moments into ch. 9's solutions; under normality its promise is inflated by N/T and its expected utility falls short by a known formula; the Sharpe gap is the version of that shortfall a backtest can compute.
Why here: The roadmap's first step; the text says the gap needs a definition computable without a truth before the implementation measures it, and distinguishes it from the loss the application measures.
Paragraphs: none before the first subsection.
Note: The section's portfolios, equations and programs are ch. 9's, cited ahead; the section defines and interprets but sends the one derivation to @kan2007.

### What the estimator is asked to do — 219

Says: The objective needs μ and Σ, neither observed; the plug-in rule substitutes sample estimates, and the minimum-variance portfolio is the one that needs no mean.
Why here: First in the section; the text says the two portfolios' one difference, whether μ̂ is needed, decides the chapter.
Paragraphs:
- ¶1 [definition] Sample moments; plug-in tangency and minimum variance; only the second skips μ̂, the input Merton says cannot be estimated.
- ¶2 [method] Long only, both become quadratic programs (ch. 9); everything below is long only; the application shows the constraint matters.
Note: ¶1 does four jobs: the two estimators, the two portfolios, the Merton precision point, and the chapter's position against ch. 6 and ch. 7.

### Two rules that estimate almost nothing — 150

Says: Equal weighting estimates nothing and inverse volatility one moment per asset; both are estimators, and the comparison is a sequence of rules estimating zero, one or all moments.
Why here: not stated; the benchmarks are defined before the mechanism that makes them win.
Paragraphs:
- ¶1 [definition] 1/N and inverse volatility defined; ch. 14 treats the latter properly; here benchmarks estimating zero, one or all moments.
Note: The reading rule for the whole comparison (not naive against sophisticated) closes a definition paragraph.

### Why the promise is inflated and the delivery is not — 1045

Says: The inverse covariance amplifies the mean's error; under normality a window manufactures a squared Sharpe ratio of N/T from noise, and the plug-in investor's expected utility is negative on sixty months of sixteen series.
Why here: The text says the Best–Grauer mechanism is visible in eq-08-plugin, so it follows the definition; the box puts this universe's numbers into the formula before the gap is defined.
Paragraphs:
- ¶1 [claim] Weights are linear in μ̂ through Σ̂⁻¹; the mean's error, volatility over √5 on sixty months, matches the premium.
- ¶2 [derivation] Two consequences: the promised squared Sharpe ratio inflated by order N/T (eq-08-inflation); expected utility of the plug-in rule (eq-08-kz).
- ¶3 [claim] Reads eq-08-kz's shape: inflated return, variance from noise; loss falls with T, rises with N, negative at small T (Klein–Bawa).
- ¶4 [method] (callout) θ² is the only data quantity in eq-08-kz; computed on the full sample.
- (code: kz-numbers)
- ¶5 [example] (callout) θ² and its annualized maximum; N=16, T=60 substituted: negative, worse than cash; shares recovered at longer T.
- (code: tbl-08-kz)
- ¶6 [method] (callout) The formula assumes normality and independence, violated per ch. 4; check by drawing sixty normal months two thousand times.
- (code: kz-check)
- ¶7 [result] (callout) Simulation and formula agree to the second decimal; the sixty-month promise against the truth, annualized.
Note: ¶6 says the draw checks whether non-normality matters at the first decimal, but it draws from a normal, and ¶7 reads the agreement as the algebra working, so the question ¶6 poses is left open; the callout is collapsed and holds the chapter's only worked formula with numbers substituted.

### The Sharpe gap — 315

Says: The gap is the average promised Sharpe ratio on the window minus the realized one out of sample, computable without a truth, with equal weighting's own gap as the control.
Why here: The text says the two formulas' statements (promises more, delivers less) need a definition computable where the truth is unknown; the implementation measures the gap, the application supplies a truth and measures the loss.
Paragraphs:
- ¶1 [definition] Promised and realized Sharpe ratios; the gap, annualized, belongs to a rule on a universe; equal weighting's is the control.
- ¶2 [definition] Gap is not loss: loss needs a truth, gap compares a rule with itself; Broadie's three frontiers; two sections ahead.
Note: ¶1 states the rolling scheme by reference to eq-25-backtest, seventeen chapters ahead.

## Measuring the Gap on Rolling Windows — 2012

Says: On sixty-month windows the rule that estimates the mean promises most and keeps least of its promise; the gaps are ordered by how much each rule estimates and the realizations in the reverse order.
Why here: The roadmap's second step; needs the four rules and the gap definition of the theory section; the text cross-checks its realized numbers against ch. 25's register so that the two chapters agree.
Paragraphs: none before the first subsection.
Note: The section's one result arrives in its last subsection, after two subsections of tooling (the naive functions and their trap, the two programs and their check) and one of loop and cross-check; the table opens that last subsection with no prose before it.

### The naive rules in `PortfolioAnalytics` — 378

Says: `equal.weight()` and `inverse.volatility.weight()` are exported, return an `optimize.portfolio` object, and return NA weights without a message when passed by name to the rebalancing loop.
Why here: not stated; the two benchmarks come first, as in the theory section.
Paragraphs:
- ¶1 [method] Both benchmarks are exported, documented, rarely used; same signature and return class as `optimize.portfolio()`.
- (code: naive-rules)
- ¶2 [code] The object carries weights, returns and specification, so `extractWeights()` and everything downstream work unchanged.
- (code: naive-weights)
- ¶3 [result] The assertion confirms eq-08-iv; `US_government`, least volatile, takes the largest weight against 1/N's share.
- ¶4 [caveat] (callout) Passing the rule's name to `optimize.portfolio.rebalancing()` looks natural, does not run it, and does not say so.
- (code: naive-in-rebalancing)
- ¶5 [caveat] (callout) By name, NA weights from string dispatch; as a function, an error; call directly, as `pm_backtest()` does; `max_sum` aside.
Note: ¶5 bolts the `max_sum` detail onto the dispatch trap; the callout sits where a reader would reach for the loop, as the contract asks.

### The two optimized rules as quadratic programs — 496

Says: The long-only minimum-variance and tangency portfolios are written directly as `quadprog` problems, checked against the package on the full sample, and the full-sample tangency's Sharpe ratio is recorded.
Why here: The text says the loop and the simulation solve thousands of problems, so the programs the package would hand to `quadprog` are written directly, with one check against the package before they are trusted.
Paragraphs:
- ¶1 [method] Thousands of solves justify direct programs; minimum variance from eq-09-problem; tangency by change of variable, needing one positive mean.
- (code: qp-rules)
- ¶2 [method] Checked against the package on one problem before four thousand.
- (code: qp-check)
- ¶3 [result] Agreement below one basis point; `maxSR` works only on the patched build (app. D); full-sample tangency weights and Sharpe ratio.
Note: ¶3 does three jobs (the check, the `maxSR` aside, the full-sample tangency) and calls that Sharpe ratio the promise every shorter window is compared with, but the next two subsections compare promise with realization, and the number returns only in the application as the ceiling.

### Three hundred and twelve windows — 491

Says: The loop forms the four portfolios on every sixty-month window, scores from the first month of model year 11 as the register does, and reproduces the register's realized Sharpe ratios to within a thousandth.
Why here: The text says the realized Sharpe ratio is computed the register's way and from the register's start so that the two chapters compare to the third decimal; the cross-check runs before the table is read.
Paragraphs:
- ¶1 [method] Each window estimates, forms four portfolios, records the promised Sharpe ratio and next month's return; weights asserted by name.
- (code: rolling-gap)
- ¶2 [method] Realized Sharpe ratio as the register computes it; scoring from the register's start so longer windows earn no credit.
- (code: realized-sharpe)
- (code: gap-check)
- ¶3 [result] `pm_backtest()` gives the same numbers, minimum variance within a thousandth (total against excess returns); agreement is not a formality.
Note: The title counts every window, but the table scores only those from the register's start; the section ends on the cross-check and the gap itself is read in the next subsection.

### The gap, rule by rule — 647

Says: The tangency portfolio promises most and keeps least, minimum variance realizes most, and the gaps are ordered by how much each rule estimates, an order the scoring period does not change.
Why here: not stated; the loop's output is tabulated and drawn once the cross-check has passed.
Paragraphs:
- (code: tbl-08-gap)
- (code: gap-facts)
- ¶1 [result] From the bottom: tangency keeps least, finishes last; equal weighting's gap is the control; all windows reorder ranks, not gaps.
- (code: fig-08-gap)
- ¶2 [result] The chapter's first result: gap order equals estimation order, realization order reversed; statistical distinguishability deferred to ch. 25's tests.
Note: The subsection opens on a table with no prose; ¶1 already carries the all-windows comparison, so ¶2 restates ¶1's order with the estimation-count reading; the hidden `gap-facts` chunk asserts the order the prose states.

## Where the Loss Comes From — 3065

Says: Under a simulated truth the mean channel accounts for nearly the whole loss, the long-only plug-in rule beats 1/N at every window shown, and the backtest's shortfall against the simulation is drift that a fixed truth cannot price.
Why here: The roadmap's third step; the text says a backtest cannot say which input caused the gap because the truth is unobserved and a simulation can; the register line closes it as every construction chapter is closed.
Paragraphs: none before the first subsection.
Note: The longest section, two fifths of the chapter, five subsections; the reconciliation of simulation and backtest, the chapter's answer, sits as the third paragraph of the crossover subsection and is restated in the register line.

### A truth to score against — 232

Says: The full-sample moments serve as the truth, normal draws of T months are estimated and scored under it, and the true long-only tangency's Sharpe ratio is the ceiling.
Why here: The text says a backtest cannot attribute the gap and a simulation can; it needs a truth before the channels are split.
Paragraphs:
- ¶1 [method] Backtest cannot attribute, simulation can; full-sample moments as truth, normal draws, tangency scored under it; bootstrap left to exercise 2.
- (code: truth)
- ¶2 [result] True Sharpe ratios of tangency, equal weight, minimum variance; the first is the ceiling; the mean shortfall is the loss.
Note: The application opens with a method paragraph and three numbers, not with a picture; the normality caveat of the theory callout returns here as a pointer to an exercise.

### The mean channel and the covariance channel — 884

Says: Substituting the true moment one at a time, the mean channel costs several times the covariance channel at sixty months, the covariance channel is nearly closed on sixteen series, and the plug-in rule beats 1/N at every window shown.
Why here: The text says the decomposition is Chopra–Ziemba's by substitution, so it follows directly from having a truth; the crossover it notices is located two subsections later.
Paragraphs:
- ¶1 [method] Chopra–Ziemba by substitution: both estimated, mean estimated with true covariance, covariance estimated with true mean.
- (code: channels)
- (code: tbl-08-channels)
- (code: channel-facts)
- ¶2 [result] Sixty-month split and ratio, below Chopra–Ziemba's eleven since long only caps it, rising with T; covariance closed, mean open.
- (code: fig-08-channels)
- ¶3 [result] Unlike DeMiguel, estimated tangency beats 1/N at every window shown; the ceiling's lead over 1/N comes from bonds beside equities.
Note: ¶2 does five jobs in one block (the split, the ratio against Chopra–Ziemba, its rise with T, why the covariance channel is closed, why the mean channel stays open); ¶3 points to the subsection after the next, past the forecast-error paragraph.

### Forecast error in the investor's units — 196

Says: Mean squared error scores a forecast in the wrong units; the loss on the mean channel is the forecast error in Sharpe ratio, which ch. 26 derives and ch. 27 builds on.
Why here: not stated beyond the number it reads from tbl-08-channels; it stands between the channel split and the crossover that the previous paragraph pointed past it to.
Paragraphs:
- ¶1 [claim] MSE says how far, not what it cost; the mean-channel loss is the error in investor's units; Salcher; ch. 26–27.
Note: A one-paragraph subsection without code, a forward pointer to Part VIII placed mid-application; it reads a table shown one subsection earlier and the crossover argument resumes after it.

### When $1/N$ stops winning — 1227

Says: On sub-universes of four, eight and sixteen series the long-only rule overtakes 1/N far earlier than the unconstrained one and the required window does not grow with N, because the benefit of optimizing grows with it; the backtest overtakes later than the simulation says, and the difference is drift.
Why here: The text says DeMiguel's thousands of months hold the benefit fixed while the cost grows with N, and on this universe nothing is held fixed; it answers the crossover question the channel subsection's ¶3 deferred.
Paragraphs:
- ¶1 [method] DeMiguel holds the benefit fixed; here sub-universes of 4, 8, 16, ten windows; long only, unconstrained, 1/N under each truth.
- (code: region)
- (code: tbl-08-crossover)
- (code: fig-08-region)
- (code: region-facts)
- ¶2 [result] Unconstrained loses at short windows; long only crosses far earlier (shrinkage); crossover falls with N as benefit rises; Tu–Zhou, Kirby–Ostdiek.
- ¶3 [claim] Simulation: sixty months suffice; backtest: overtakes only by 120, realizes less; sampling error plus drift; fixed truth, a lower bound.
Note: ¶3 is the chapter's reconciliation of simulation and backtest and its central claim, placed as the last paragraph of a subsection titled for the crossover, then restated in the register line and in takeaways 5 and 6; ¶2 reads a table and a figure in one block with five citations.

### The register line — 526

Says: On sixty-month windows the rules that estimate no mean occupy the first four places and the tangency portfolio is last; on 120-month windows it is ahead of both naive rules; minimum variance is strongest at every window, and the lesson is that the mean cannot be estimated.
Why here: The text says every construction chapter ends by reading its strategy off ch. 25's register so that no chapter carries a number another could contradict.
Paragraphs:
- ¶1 [method] Every construction chapter closes on the register of ch. 25 so that chapters cannot contradict each other.
- (code: register)
- (code: register-facts)
- ¶2 [result] Sixty-month order, min-CVaR on top; holds at thirty-six, not 120, where tangency leads both naive rules; minimum variance strongest (Jagannathan–Ma).
- ¶3 [claim] 1/N not the winner, yet consistent with DeMiguel: their claim concerns the mean; covariance estimable on sixteen series; the lesson.
Note: ¶3 repeats the sixty-against-120 comparison of the previous subsection's ¶3, standard error included; the chapter's last sentence, that an input's cost is set by how well it can be estimated, is the chapter's claim in its final form and appears here for the first time.

## Key Takeaways — 348

Says: Seven bullets: the two Kan–Zhou formulas, the gap and the shares kept, the channel split, the crossover's two determinants, the lower-bound reading, the register order, and the naive-rule trap.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [takeaway] A plug-in portfolio promises more and delivers less; eq-08-inflation and eq-08-kz, both driven by N/T; negative utility on sixty months.
- ¶2 [takeaway] The gap needs no truth; shares kept by tangency and minimum variance; equal weighting's gap is what the window manufactures.
- ¶3 [takeaway] Mean channel costs a multiple of the covariance channel at sixty months, still open at a thousand; covariance nearly closed.
- ¶4 [takeaway] Crossover depends on cost N/T and the universe's benefit; long only shortens it; the window need not lengthen with N.
- ¶5 [takeaway] Fixed-truth error is a lower bound; simulated tangency beats 1/N in most sixty-month draws; the actual one trailed until 120.
- ¶6 [takeaway] The register's sixty-month order; tangency's rank at 120, ahead of both naive rules; minimum variance strongest at every window.
- ¶7 [takeaway] The naive functions are exported and return `optimize.portfolio` objects; by name in the rebalancing loop, NA weights and no error.
Note: Seven against the contract's around five; ¶5 and ¶6 both state the sixty-against-120 ranking; ¶7 is the only bullet about the package.

## Exercises — 213

Says: Four exercises: the gap on 120-month windows against the register, a block-bootstrap truth for the channel split, the Kan–Zhou thresholds for N = 16 and 50, and a crude mean shrinkage in the loop.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [exercise] Rerun the loop at 120 months, same start; compare with the register's 120-month rows; does the tangency gap close.
- ¶2 [exercise] Replace the normal draw with ch. 9's block bootstrap; redo the split at T=60; does the mean channel still dominate.
- ¶3 [exercise] From eq-08-kz, the T where expected utility turns positive and reaches ninety percent, for N=16 and N=50; scaling with N.
- ¶4 [exercise] Shrink μ̂ halfway to its cross-sectional mean (Jorion, ch. 6); remeasure the tangency gap; more help than long only gave.
Note: Four against around three; the register line already gives the 120-month ranking exercise 1 asks for; exercise 2 is announced twice, in the theory callout's normality caveat and in the application's first paragraph.
