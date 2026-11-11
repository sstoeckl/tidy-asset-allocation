---
file: chapters/28-robustness.qmd
title: Robustness and Model Uncertainty
part: Advanced Topics
words: 7385
sections: 5
paragraphs: 50
---

# Chapter

Claim: Guarding against a set of models by its worst case comes out as an increase in effective risk aversion, a shrinkage of the portfolio toward minimum variance in proportion to the size of the set; because that set is a confidence region, on sixty months of sixteen classes it is wide enough at even odds to go most of the way, and out of sample the two maxmin portfolios improve on the tangency portfolio without reaching minimum variance, while resampling buys nothing.
Question: What should an investor do when the doubt is about whether the model behind μ and Σ is the right one, not about their values; cites Garlappi, Uppal and Wang for posing it for the mean-variance investor and Gilboa and Schmeidler for the decision rule, both in the second sentence.
Why here: Stated for the axis, not for the position: the answer is a shrinkage toward minimum variance, so the chapter is strategic in chapter 3's sense. Takes the standard error and Bayes–Stein from chapter 6, the covariance error from chapter 7, the plug-in rule, the quadratic programs and the register reading from chapter 8, the frontier scalars, the tangency and minimum-variance portfolios and the block bootstrap from chapter 9, the cone solvers and `random_portfolios()` as a search from chapter 13, the single factor and turbulence from chapter 5, the left tails from chapter 4, the register from chapter 25. Its relation to its two neighbors is stated: chapter 26 prices the error, chapter 27 corrects the forecast, this one leaves the forecast alone and changes the decision. It is the last chapter; it points forward only to two appendices (the solver matrix, scenario analysis), and that it closes the book, or why, is not stated.
Does: Derive and check the multi-prior portfolio in closed form and as a long-only fixed point, compute the worst-case tilt and the robust portfolio over a Kullback–Leibler ball, build a block-bootstrap resampled frontier, sample the feasible set three ways and audit the draws against a factor-exposure bound, and score the rules out of sample with the register's accounting.
Order: Opening; theory in five subsections (the two uncertainties, the multi-prior portfolio, robust optimization in general, the Kullback–Leibler ball, resampling); implementation in four (resampled frontier, random portfolios with the callout, multi-prior, Kullback–Leibler ball); application undivided; takeaways; exercises. Deviations: the theory heading has no paragraph of its own; the implementation takes the three derived devices in the reverse of the theory's order and adds random portfolios, which have no theory subsection and no row in the application; robust optimization over other sets and smooth ambiguity have theory and no implementation; two subsection titles occur twice, once in the theory and once in the implementation; all three figures and every in-sample result sit in the implementation, so the application is a method paragraph, one table and three paragraphs reading it; five takeaways, four exercises.

# Sections

## Opening — 264

Says: Doubt about the model, as against doubt about its inputs, is met by a worst case over the models the data cannot rule out, which turns out to be a shrinkage toward minimum variance; the chapter derives it, implements it and tests it.
Why here: Contract position; ¶2 gives the order: separate the two uncertainties and derive three devices, implement four on the sixteen classes, run the robust portfolios out of sample against the register.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Doubt about the model, not its inputs; Garlappi et al. answer with Gilboa–Schmeidler's maxmin: shrinkage toward minimum variance, so strategic.
- ¶2 [method] Order: separate the two uncertainties, derive three devices, implement four (random portfolios as a picture), test against the register.
- (code: data) the sixteen classes, the bill, excess returns with an assertion; `N`, `Tn`, the dates, sample mean and covariance
Note: No visible packages block: the setup chunk is hidden and the shown chunk loads data. ¶1 gives the chapter's answer before any method; ¶2 is one sentence that derives three devices and implements "all four", the fourth being random portfolios.

## Parameter Uncertainty and Model Uncertainty — 1745 (0 before the subsections)

Says: (heading only)
Why here: Stated in the opening: the two uncertainties are separated first and the devices derived before any code.
Paragraphs: none of its own.
Note: Heading only; five subsections without an introducing paragraph. The heading names the first subsection's distinction; the other four are devices, sorted by that distinction as they come.

### Two kinds of not knowing — 326

Says: Parameter uncertainty is a distribution over numbers inside a model taken as true and is treated by averaging; model uncertainty is a set of models with no distribution over it and is treated by the worst case.
Why here: Stated: every chapter since chapter 6 has treated the inputs as estimates, and all of that is named parameter uncertainty here; ¶3 says what follows derives what the set's boundary does to the weights.
Paragraphs:
- ¶1 [definition] Chapters 6 to 8, 26, 27 recapped as parameter uncertainty: model true, distribution over inputs; the tool is averaging.
- ¶2 [definition] Model uncertainty: a set of models, no prior over it; Knight, Ellsberg; Gilboa–Schmeidler's rule takes the worst case.
- ¶3 [transition] A distribution has a mean, a set has a boundary where the worst case sits; the derivation follows.
Note: ¶1 does three jobs (the recap of five chapters, the definition, the Bayesian remedy with three citations); smooth ambiguity, the case between the average and the worst case, is defined only at the end of the Kullback–Leibler subsection.

### The multi-prior portfolio — 654

Says: With the ambiguity in the mean and the set a confidence ellipsoid, the worst case is a linear penalty on volatility, so the investor scales the tangency portfolio down or, fully invested, holds the mean-variance portfolio of a higher effective risk aversion that converges to minimum variance; the radius is a confidence level.
Why here: It is the answer the opening names and what ¶3 before it announces; needs chapter 3's quadratic utility, chapter 9's tangency, frontier scalars and minimum variance, chapter 6's standard error and Bayes–Stein; the next two subsections each open by generalizing it.
Paragraphs:
- ¶1 [definition] Garlappi et al. keep Σ and put the ambiguity in the mean: a confidence ellipsoid, the maxmin problem eq-28-multiprior.
- ¶2 [derivation] Inner problem by Lagrangian: the worst mean lies along Σw at the binding radius; eq-28-worst-mean.
- ¶3 [derivation] The expected return is marked down by √ε standard deviations; the outer problem, eq-28-robust-objective.
- ¶4 [derivation] A linear penalty on volatility; with a risk-free asset the weights stay proportional to the tangency direction; eq-28-rf.
- ¶5 [claim] The plug-in investor's risky portfolio, scaled by one minus √ε over the maximum Sharpe ratio; nothing risky beyond that.
- ¶6 [derivation] Fully invested: the budget multiplier, effective risk aversion γ* defined, solved with chapter 9's scalars; eq-28-fully-invested.
- ¶7 [claim] Higher risk aversion; speculative part shrinks by γ/γ*, minimum variance in the limit; a fixed point, quadratic program if long-only.
- ¶8 [definition] The radius is a confidence level: an F quantile scaled by N and T, eq-28-epsilon.
- ¶9 [claim] A confidence region, hence a parameter-uncertainty device; shrinks the portfolio where Bayes–Stein shrinks the estimate; chapter 27 changes the forecast.
Note: ¶2, ¶4 and ¶9 begin mid-sentence after a display equation; ¶7 carries seven points; the reclassification of the opening's answer as a parameter-uncertainty device arrives in ¶9, inside the paragraph on calibrating the radius.

### Robust optimization over a set — 143

Says: The multi-prior inner problem is one case of robust optimization, in which the choice of uncertainty set decides the penalty: a box is a per-asset haircut, an ellipsoid a volatility penalty.
Why here: Stated in its first sentence: the problem just solved is one instance of the general method; nothing in the implementation or the application builds on it.
Paragraphs:
- ¶1 [definition] Robust optimization: Goldfarb–Iyengar's factor sets as a cone program, Tütüncü–Koenig's boxes; the set does the work; two appendices.
Note: One paragraph, a survey with two citations and pointers to chapter 13 and two appendices; the general case follows its special case and is never implemented.

### The Kullback–Leibler ball — 428

Says: Widening the set to every distribution within a fixed relative entropy of a reference lets the worst case reweight the sample toward the portfolio's bad months; the result reads as the risk aversion of an exponential-utility investor, and with a Gaussian reference restricted to mean shifts it is the ellipsoid with ε = 2η.
Why here: Stated in its first sentence: a worst case over means leaves every other feature of the model intact; it relates itself back to the ellipsoid and forward to the implementation, which is to show what the extra room buys.
Paragraphs:
- ¶1 [definition] Hansen–Sargent's robust control: all distributions within relative entropy η of a reference model; eq-28-kl-ball.
- ¶2 [derivation] Tails, correlations and skewness may move; a Lagrangian in the probabilities gives the exponential tilt, eq-28-tilt.
- ¶3 [claim] The tilt reweights toward the portfolio's bad months; assets sharing them are marked down most; multiplier preference, eq-28-multiplier.
- ¶4 [claim] An exponential-utility certainty equivalent; Maenhout: robustness as risk aversion; Gaussian case equals the ellipsoid; η calibrated by detection probability.
- ¶5 [definition] Smooth ambiguity (Klibanoff et al.): a concave φ over a second-order distribution spans Bayesian average to maxmin.
Note: ¶4 does four jobs (the certainty-equivalent reading, the link back to γ*, the equivalence of the two sets, the calibration of η); ¶5 is a third model under the ball's heading, said to be traced through eq-28-epsilon, and is not implemented.

### Resampling, and what kind of uncertainty it treats — 187

Says: Michaud's resampled frontier averages frontier weights rank by rank over draws of the inputs; it averages over parameter draws from one model, so it is a parameter-uncertainty device, and by Scherer's critique not the Bayesian answer either.
Why here: Not stated why last; the heading files it under the first subsection's distinction, and its closing sentence says that measuring it beside the maxmin rules shows averaging against guarding.
Paragraphs:
- ¶1 [definition] Michaud: draw inputs from the sampling distribution, solve the frontier on each, average the weights by rank; eq-28-resampled.
- ¶2 [claim] More diversified and more stable than chapter 9's tangency; a parameter-uncertainty device; Scherer: not Bayesian, pulled to the simplex center.
Note: ¶2 opens mid-sentence with the definition of k and then holds the property, the classification, the critique and the forward pointer; random portfolios, the fourth device of the implementation, have no subsection here.

## Four Robustifications on the Sixteen Classes — 3907 (332 before the subsections)

Says: The quadratic programs are chapter 8's, written out so that the loops run fast, with the `PortfolioAnalytics` specification as the check, at γ = 3 and annualized.
Why here: Stated in the opening: all four devices are implemented on the sixteen classes; the order of the four subsections is not stated.
Paragraphs:
- ¶1 [method] Chapter 8's quadratic programs written out for speed, the package kept as check; γ = 3; annualized from monthly moments.
- (code: helpers) `qp_simplex()` and four portfolio solvers; annualized return, volatility, Sharpe ratio, `turnover()`; minimum variance and tangency; the `ROI` minimum variance asserted equal
Note: The heading counts four robustifications and the subsections run resampling, random portfolios, multi-prior, ball: the theory's order reversed, plus a device its own heading calls a picture. γ = 3 rests on a package default. Each subsection also reads its in-sample results.

### The resampled frontier — 676

Says: Averaged over two hundred block-bootstrap draws, the resampled tangency is more diversified than the sample tangency, pays for it in in-sample Sharpe ratio, and lies on a frontier dominated at the moments it was averaged under.
Why here: Not stated why first, the theory having treated resampling last; ¶1 ties the bootstrap to chapter 9's, and ¶2 ends by handing the out-of-sample question to the application.
Paragraphs:
- ¶1 [method] Twelve-month blocks as in chapter 9; long-only frontier at 25 targets per draw; weights averaged by rank; tangency averaged too.
- (code: resample) `block_index()`, `frontier_of()`; 25 targets, 200 draws; the sample frontier, the averaged frontier and tangency; shape assertions
- (code: fig-28-resampled) sample frontier, the two hundred bootstrap frontiers and their average, all at full-sample moments, from one frame
- (code: resample-claims) hidden: mean distances of the draws, the best Sharpe ratio on the averaged frontier; four assertions
- (code: tbl-28-resampled-weights) weights above one percent, Sharpe ratio and positions, sample against resampled
- ¶2 [result] More classes held; distances between draws, sample and average; the mean diversifies, does not center; Sharpe ratio lost; Scherer's dominance.
Note: Four chunks separate the two paragraphs; ¶2 reads the figure, the table and the hidden chunk at once, in seven points; the figure caption gives the result before the prose does; the comparison that the draws sit no closer to the average is the one statement the hidden chunk does not assert.

### Random portfolios as a picture of the feasible set — 1116 (372 in the callout)

Says: Three generators sample the same long-only set differently and none comes near its edge, so random portfolios show the set and do not search it; and they ignore a factor-exposure bound at generation and in the objective.
Why here: Not stated beyond the contrast with chapter 13, where the same function was a solver; the opening announced it as the fourth device; no theory subsection precedes it and the application does not use it.
Paragraphs:
- ¶1 [method] Chapter 13's solver reused as a sample of the feasible set; three engines: sample, simplex with `fev`, grid.
- (code: random-portfolios) three engines, two thousand permutations each; the row counts printed
- (code: clouds) `cloud()`: volatility, return, distance to the tangency and positions, columns placed by name; one frame
- (code: tbl-28-random) per engine: portfolios, best Sharpe ratio as a share of the tangency's, nearest member, median positions
- (code: fig-28-random) three clouds with the long-only frontier, the nearest member and the tangency marked
- (code: random-claims) hidden: the nearest engine, positions falling in `fev`, the grid's size
- ¶2 [result] No member nears the tangency in distance or Sharpe ratio: samples miss the edge; simplex toward faces, grid a lattice.
- ¶3 [definition] (callout) A factor-exposure constraint bounds B'w; betas on chapter 5's equal-weighted factor, capped below the tangency's.
- (code: factor-exposure) (callout) betas, the bounded specification, sample and simplex draws, the share of each breaching
- (code: factor-exposure-optimizer) (callout) maximum Sharpe ratio under the cap by `random` and by `ROI`; three betas printed
- (code: factor-exposure-claims) (callout) hidden: the breach shares, `ROI` at the cap, no exposure term in the objective function
- ¶4 [caveat] (callout) Generators check five constraint types, not this one; every sample draw breaches; no penalty either; `random` breaches silently, `ROI` binds.
Note: The longest implementation subsection belongs to the one device with no theory and no part in the application; a third of it is the callout, which builds its own case (nothing else in the chapter sets a factor-exposure bound) and returns in takeaway 5 and exercise 3.

### The multi-prior portfolio — 1082

Says: The derived closed form matches a direct maximization and is kept over `glPF()`; at even odds the speculative part is already cut to about a fifth; long-only, the fixed point walks from an all-equity plug-in portfolio toward minimum variance; a turbulence-driven radius is largely a volatility-timing rule.
Why here: ¶1 says the theory's closed forms are to be written out and checked; why it follows random portfolios is not stated; the ball's subsection reads itself against these results, and the application calls `eps_of()` and `mp_long_only()`.
Paragraphs:
- ¶1 [method] Closed forms written out, checked against a direct maximization of eq-28-robust-objective and against `glPF()`.
- (code: multi-prior-closed) frontier scalars, `eps_of()`, `mp_closed()` by root-finding, `robust_objective()`, a BFGS check, `glPF()`; shrinkage and gaps printed
- (code: multi-prior-checks) hidden: agreement with the direct maximum and with `glPF()` at zero radius; a higher objective than `glPF()`
- ¶2 [result] At the median radius the shrinkage factor is about a fifth; brute force agrees; `glPF()` differs and attains less.
- ¶3 [method] Long-only: no closed form; iterate the quadratic program at γ*, read the volatility, update.
- (code: multi-prior-long-only) `mp_long_only()`; six confidence levels from 0 to 0.9999; radius, γ*, distance to minimum variance and to plug-in
- (code: fig-28-multiprior) stacked weights against the radius, small classes pooled
- (code: multi-prior-claims) hidden: monotone distance and γ*, all equity at zero radius
- ¶4 [result] Distance to minimum variance falls monotonically; the largest move comes first, since the plug-in portfolio is all equity.
- ¶5 [method] Stöckl's time-varying radius: the confidence level replaced by the p-value of chapter 5's turbulence; `OSminimax_one()`.
- (code: ambiguity-measure) loads `uncertaintymeasures`; rolling radius, turbulence, cross-sectional dispersion; rank correlation, R², share of months with nothing risky
- (code: ambiguity-claims) hidden
- ¶6 [result] Radius is a transform of turbulence, mostly dispersion; often nothing risky; largely volatility timing; undecidable on a modeled market.
Note: Three topics under one heading (the closed-form check, the long-only path, the time-varying radius); the third has no theory subsection, uses the risk-free form while all else is fully invested, and returns nowhere later; the `glPF()` disagreement is in running prose, not in a callout.

### The Kullback–Leibler ball — 701

Says: On the empirical distribution the ball also moves the portfolio toward minimum variance as its radius grows, but the mark-down follows each class's covariance with the portfolio's worst months; the application's radius is set at η = ε/2 so that the two sets differ only in shape.
Why here: It reads its results against the ellipsoid's, so it follows the multi-prior subsection; its last sentence sets the radius the application uses.
Paragraphs:
- ¶1 [method] Empirical reference; the tilt is a one-dimensional root in θ; the robust portfolio by Newton steps on a concave problem.
- (code: kl-tilt) `kl_tilt()`, `kl_robust()` with damped steps on the simplex; three radii; the plug-in portfolio
- (code: tbl-28-kl) per radius: θ, distance from plug-in and from minimum variance, Sharpe ratio, the class marked down most
- (code: kl-claims) hidden: monotone θ, distance and mark-down; convergence; sets the radius for the application
- ¶2 [result] Toward minimum variance as with the ellipsoid, by another route: bad-month covariance; the smallest radius moves half; η = ε/2.
Note: Two paragraphs around one long routine whose damping and tolerances live in code only; ¶2 carries six points, and its claim about the longest left tails is handed to exercise 4 and then stated as a finding in takeaway 3.

## Robustness Out of Sample — 992

Says: On sixty-month windows from model year 11 the two maxmin portfolios improve on the tangency portfolio in Sharpe ratio, turnover and drawdown without reaching minimum variance, the resampled tangency improves on nothing, and equal weighting has the highest certainty equivalent; the worst case bought what a higher risk aversion buys.
Why here: Stated in the opening and prepared by the closing sentences of the resampled and ball subsections; needs every function of the implementation and chapter 25's register for the accounting.
Paragraphs:
- ¶1 [method] Six portfolios on sixty-month windows from model year 11, the register's metrics; draws, ridge, radii and certainty equivalent specified.
- (code: rolling) six rules per window, names asserted; `score()`: Sharpe ratio, certainty equivalent, turnover, drawdown; the register's rows joined
- (code: tbl-28-oos) six rows: Sharpe ratio, certainty equivalent, turnover, drawdown, the register's Sharpe ratio
- (code: oos-claims) hidden: the register reproduced within tolerance; every ordering the prose states asserted
- ¶2 [result] Register rows reproduce; minimum variance differs slightly, fitted there on total returns; the Sharpe order listed inline.
- ¶3 [result] Maxmin rules improve on tangency in Sharpe, turnover, drawdown; minimum variance first; resampling buys nothing; equal weight's certainty equivalent highest.
- ¶4 [claim] The lesson: a worst case over means is higher risk aversion; the confidence region is already wide at even odds.
Note: No subsection and no figure: a method paragraph, one table, three paragraphs; ¶3 reads all six rows in one paragraph; the six are named only in the code and the caption, two of them rules that estimate no mean; random portfolios are absent.

## Key Takeaways — 217

Says: The two uncertainties and their treatments, the multi-prior portfolio as higher risk aversion with a confidence-level radius, the ball as a reweighting toward bad months, resampling as averaging that is dominated out of sample, and random portfolios as a picture that ignores factor exposure.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Parameter uncertainty is averaged, model uncertainty met by a worst case [Gilboa–Schmeidler]: the estimate shrinks, or the portfolio does.
- ¶2 [takeaway] Multi-prior investor [Garlappi et al.]: effective risk aversion γ*, converging to minimum variance; a confidence-level radius, so a parameter-uncertainty device.
- ¶3 [takeaway] The ball reweights toward bad months [Hansen–Sargent]; Gaussian reference gives the ellipsoid; worst tails marked down, not highest volatility.
- ¶4 [takeaway] Resampling averages parameter draws: more diversified in sample, dominated out of sample, not robust in this chapter's sense [Scherer].
- ¶5 [takeaway] `random_portfolios()` pictures the feasible set, does not search it, ignores a factor-exposure constraint; that bound belongs on the convex path.
Note: Five bullets: three restate the theory, one the callout; none gives the out-of-sample result for the two maxmin portfolios, minimum variance or equal weighting, nor the time-varying radius; bullet 3's tail claim rests on exercise 4.

## Exercises — 219

Says: Four exercises: the multi-prior portfolio at three confidence levels out of sample, the right end of the resampled frontier, the callout's trap repaired by filtering, and the tilt against the ellipsoid class by class.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] The rolling exercise at p = 0.1, 0.5, 0.9: Sharpe ratio, turnover, distance to minimum variance; where they become indistinguishable.
- ¶2 [exercise] Expected return of the top-ranked resampled portfolio against the highest sample mean; explain by the long-only constraint.
- ¶3 [exercise] Filter two thousand `rp_sample()` draws to the beta band; how many survive; the best survivor against `ROI`.
- ¶4 [exercise] Gaussian worst-case mean at ε = 2η against the tilted mean, class by class; which classes, and why (chapter 4).
Note: Four exercises, one per implemented device; none asks for a derivation; exercise 4 is the one the ball's implementation and takeaway 3 lean on for the tail claim.
