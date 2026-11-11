---
file: chapters/18-parametric-policies.qmd
title: Parametric Portfolio Policies
part: Allocation Strategies
words: 6589
sections: 5
paragraphs: 44
---

# Chapter

Claim: Writing each weight as the benchmark weight plus a linear tilt in standardized characteristics, and estimating the few coefficients on realized utility, replaces the moments whose estimation error chapter 8 priced; on the modeled market both policies finish ahead of their benchmarks out of sample, by margins the sample cannot certify, and what pays is the one characteristic whose coefficient stayed stable.
Question: Can an investor skip the forecast and write each asset's weight directly as a function of what is observable about it; cites Brandt, Santa-Clara and Valkanov in the second sentence as the proposers.
Why here: Needs chapter 8's priced estimation error as the motivation, chapter 3's power utility and the strategic/tactical vocabulary, chapter 2's two panels and simple return, chapter 5's capitalization benchmark and region-neutral sort, and chapter 16's signals, equal-weight benchmark and hand-set tilt, which the text names as the contrast (same information, a different loss function). It also leans forward on chapters 23 and 25 as if already read, in the past tense: the net return and turnover definitions, the no-trade region, the register's accounting, burn-in and Sharpe standard error. Hands the long-only equity policy and the value characteristic to chapter 21 and the many-parameter generalization to chapter 27. Why it follows 17 and precedes 19 inside the part is not stated.
Does: Build an aligned, name-indexed characteristics panel with assertions; implement the policy, its estimator, path accounting and inference in four functions; estimate a cross-sectional and a timing policy, free and under a long-only restriction, gross and net of costs; re-estimate on an expanding window and test the result with the register's accounting and a paired Sharpe test.
Order: Theory (policy and estimator, standard errors, long-only and costs, timing), implementation (equity panel, the four functions, inference, the class policy), application (coefficients through time, performance), takeaways, exercises. Deviations: none of the three main headings has a paragraph of its own; the implementation already reads the full-sample results (coefficients, standard errors, the momentum-as-hedge finding, the worked example, the class vertex), so the application holds the out-of-sample test only; the implementation ends on a chunk; the only figure shows coefficients, not performance; six takeaways, four exercises.

# Sections

## Opening (untitled) — 372

Says: Weights can be written directly on characteristics and estimated on utility, K parameters instead of N + N(N+1)/2 moments; the chapter sets that out, implements it and tests it twice.
Why here: Contract position; the text says theory first, then forty lines of R and two estimates, then the expanding-window test.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Skip the forecast: weights on observables, K parameters however large N; Brandt, Santa-Clara and Valkanov; chapter 8's priced moments.
- ¶2 [method] Theory, then forty lines and two estimates, then the expanding-window test; tactical positions under a strategic rule.
- ¶3 [method] Chapter 2's two panels as total returns: fully invested, utility on gross wealth.
- (code: data) the sixteen classes, the bill, the 123 equities; alignment assertions; γ = 5
Note: The packages block is the hidden `setup` chunk and the visible chunk loads data instead; γ = 5 is set in code and never argued for in the prose.

## Weights as a Function of Characteristics — 1248

Says: (heading only)
Why here: Stated in the opening: the policy, its estimator and standard errors come first, with the long-only, cost and timing variants.
Paragraphs: none of its own.
Note: Heading only; four subsections without an introducing paragraph.

### The policy and its estimator — 476

Says: The policy is the benchmark weight plus a tilt linear in standardized characteristics, its coefficients maximize realized power utility without a mean or a covariance, and because the portfolio return is linear in θ the policy is a position in K + 1 portfolios.
Why here: Needs chapter 2's simple return and chapter 3's power utility; eq-18-linear is what the standard errors, the bootstrap and the timing version build on.
Paragraphs:
- ¶1 [definition] Benchmark weight plus a tilt linear in K standardized characteristics; eq-18-policy.
- ¶2 [claim] One θ for all assets and months; tilts sum to zero; 1/N_t caps the active position; θ = 0 is the benchmark.
- ¶3 [definition] eq-18-estimator: average power utility, whole distribution, no μ̂ or Σ̂; Brandt, Aït-Sahalia and Brandt, Brandt's survey.
- ¶4 [claim] Dimension is the gain: 123 means and 7,626 covariances against two coefficients; Michaud, Kan–Zhou, DeMiguel et al., Jagannathan–Ma.
- ¶5 [derivation] Return linear in θ, eq-18-linear: benchmark plus K long-short portfolios; Hjalmarsson–Manchev, Brandt–Santa-Clara.
Note: ¶4 is the opening's arithmetic a second time with the numbers in, and the takeaways give it a third; ¶3 and ¶5 each close with a lineage sentence of three citations.

### Standard errors — 171

Says: The estimate solves K moment conditions, so it carries a GMM sandwich covariance; the t-statistic tests whether a characteristic belongs in the portfolio, not whether it forecasts returns.
Why here: Follows from the concavity and linearity just established; the implementation computes exactly eq-18-avar and the bootstrap named here.
Paragraphs:
- ¶1 [derivation] Concave objective; FOC eq-18-foc as K moment conditions; exactly identified GMM [Hansen]; sandwich eq-18-avar.
- ¶2 [claim] Newey–West for serial correlation, block bootstrap [Künsch] as the check; the t-test is membership, not forecasting.
Note: ¶2 carries two points (the robustness options and the reading of the test); the second is the result the implementation later calls instructive, stated here before any number.

### Long-only weights, and costs — 295

Says: Truncation at zero buys a long-only mandate at the cost of linearity and differentiability, which the parameter restriction used at class level avoids; trading costs go into the objective and shrink the fastest-moving characteristics most.
Why here: Not stated beyond the observation that eq-18-policy shorts freely; the class policy and the net-return estimates of the application use both devices.
Paragraphs:
- ¶1 [definition] Truncation eq-18-longonly loses linearity and the gradient; the alternative restricts θ by linear inequalities; Ammann et al.
- ¶2 [definition] Net return eq-18-cost on drifted weights shrinks fast-moving characteristics; chapter 23's no-trade region; DeMiguel et al. on costs.
Note: Two topics under one heading, as the title admits; ¶2 builds on eq-23-net and says chapter 23 "showed" the no-trade region, two parts ahead; the no-trade parameter of Brandt et al. is described and never used.

### Timing across a few asset classes — 306

Says: With sixteen assets the information is in the time series, so the policy takes state variables with a fixed loading pattern per signal, eq-18-timing; what separates it from chapter 16 is that the map from signal to weight is estimated on the investor's objective.
Why here: Stated: the cross-section of sixteen is too thin, so the second policy needs the time-series version; chapter 16's signals and benchmark are reused and chapter 27 generalizes the estimator.
Paragraphs:
- ¶1 [definition] Brandt–Santa-Clara managed portfolios; one coefficient per signal with zero-sum loadings, eq-18-timing; term, credit, momentum.
- ¶2 [claim] Unlike chapter 16, the signal-to-weight map is estimated on the investor's objective; chapter 27 generalizes to Gu–Kelly–Xiu.
- ¶3 [caveat] Brandt et al.'s three characteristics; the market carries size and momentum, value waits for chapter 21.
Note: ¶3 belongs to the equity policy, not to the timing policy it sits under; it is the data caveat for the implementation, placed at the end of the theory.

## Estimation of Two Policies — 2591

Says: (heading only)
Why here: Stated in the opening: the policy in about forty lines of R, estimated on the equities and on the classes.
Paragraphs: none of its own.
Note: Heading only; its four subsections also read the full-sample results, so the section is implementation and in-sample results together, and it ends on a chunk.

### The equity panel — 536

Says: The benchmark is chapter 5's capitalization weight, size and momentum are standardized within region so the policy selects stocks and leaves the regional allocation to the benchmark, and the panel is one named array checked against the raw tables.
Why here: Stated: chapter 5 showed that a global size sort is a region sort; the array and its alignment are what the policy functions consume.
Paragraphs:
- ¶1 [method] Chapter 5's capitalization benchmark; log size and eq-16-mom momentum standardized within region, so the policy selects stocks only.
- (code: characteristics) `held`/`known` indices, `lag_rows()`, `zscore()`, `mom_12_1()`, capitalization matched to month ends, `within_region()`
- ¶2 [method] One named array, months by assets by characteristics, each row what was known a month earlier; assertions check alignment.
- (code: panel) `panel()`; the equity array and benchmark weights; one month verified against `sim_marketcap_weekly` and the raw returns; `dim(X_eq)`
- ¶3 [result] The panel's length and first month, set by momentum's twelve months and one lag; all 123 present throughout.
Note: Two long assertion chunks for three short paragraphs; the one-month check is explained in a code comment, not in the text.

### The policy in forty lines — 388

Says: Four functions (weights, utility, path accounting, estimator) implement eq-18-policy, eq-18-cost and eq-18-estimator, and two optimizers from distant starts agree, as a concave objective requires.
Why here: Stated in the opening ("about forty lines"); needs the panel; everything after calls these functions.
Paragraphs:
- (code: policy) `ppp_weights()`, `crra()`, `path_returns()`, `ppp_utility()`, `ppp_estimate()` with BFGS or `constrOptim()` under the simplex restriction
- ¶1 [code] `path_returns()` follows the register's accounting; `ppp_estimate()` maximizes eq-18-estimator by BFGS or under the simplex restriction.
- (code: estimate) full-sample equity estimate from zero; `nlminb()` from (2, 2); the two agree within 0.01
- ¶2 [result] A second optimizer from a distant start reaches the same coefficients, as a concave objective requires.
Note: Opens with the chunk and the prose follows it; the accounting convention (trade measured from the drifted position, charged to the month, flat start) lives in a code comment and a forward reference to chapter 25, not in the text.

### Standard errors two ways — 925

Says: Sandwich and block-bootstrap standard errors agree; size enters negative and significant, momentum enters positive although its own portfolio earns nothing, because the first-order condition weighs returns by marginal utility; in sample the policy lifts the certainty equivalent, with leverage.
Why here: Stated: eq-18-avar needs scores and a Hessian, which `numDeriv` supplies, and eq-18-linear makes each bootstrap draw a two-parameter problem; the application's stability question starts from these coefficients.
Paragraphs:
- ¶1 [method] `numDeriv` supplies scores and Hessian; blocks of twelve as in chapter 9; eq-18-linear makes each draw a three-series problem.
- (code: inference) scores, Hessian, sandwich; benchmark and characteristic-portfolio returns with linearity asserted; 400 block-bootstrap draws
- (code: tbl-18-theta) coefficients, both standard errors, t, sign agreement across draws, each portfolio's premium and t
- (code: theta-facts) hidden: marginal-utility-weighted momentum mean, in-sample weights, certainty equivalent; sign and significance assertions
- ¶2 [result] Both standard errors agree; size negative and significant; momentum positive with no premium, a hedge by eq-18-foc; in-sample certainty equivalent; leverage.
- (code: worked) (callout) the ten largest names in the last month: benchmark, characteristics, tilt, policy weight, checked against `W_eq`
- ¶3 [example] (callout) eq-18-policy with the sample numbers for the largest name; the code checks all ten.
- (code: tbl-18-worked) (callout)
- ¶4 [result] (callout) The largest holding is cut and several of the ten go below zero.
Note: ¶2 is one paragraph with six points (agreement, size, momentum as hedge, why this market has no momentum premium, the in-sample certainty equivalent, leverage); the market-property caveat is the only place the chapter says the momentum result would differ on real data; the worked example is collapsed and its sentence is split by its display equation.

### The timing policy across sixteen classes — 742

Says: On the equal-weight benchmark with signals standardized on their own history, the free estimate drives one class far below zero and the simplex-restricted one sits at a vertex set by the most extreme months; the policy itself lies outside `PortfolioAnalytics`, which lends only `Return.portfolio()` and `turnover()`.
Why here: Stated: the benchmark is chapter 16's because it estimates nothing, and the first 120 months are the register's burn-in, so the application can start where the register starts.
Paragraphs:
- ¶1 [method] Chapter 16's equal-weight benchmark; curve signals standardized on their own history and clipped; times a standardized class indicator, eq-18-timing.
- (code: class-panel) class groups; term and credit spread from `sim_curve_weekly`; `expanding_z()` with a no-look-ahead assertion; `loading()`; the class array, equal weights, per-class costs
- ¶2 [method] First estimate on the register's 120-month burn-in, free and with no in-sample weight negative.
- (code: class-estimate) free and simplex estimates, a second start, the weights held at zero; coefficients and lowest weight printed
- ¶3 [result] Free: one class deeply short; restricted: three small positive coefficients at a vertex with K zero weights; truncation backs it out of sample.
- ¶4 [caveat] (callout) No policy interface in `optimize.portfolio()`; the rolling helpers roll nothing; `Return.portfolio()` back-fill, `turnover()` divides by N; the register compares.
- (code: pa-reuse) `Return.portfolio()` reproduces the gross path; the back-fill warning on the whole burn-in; `turnover()` reconciled to eq-23-turnover
Note: The section, and with it the implementation, ends on a chunk whose output no prose reads; the callout's three package facts are then demonstrated in code the text never comments on; the equity policy is never estimated under either long-only device, so the two devices are compared only across the two policies.

## The Policies Out of Sample — 1824

Says: (heading only)
Why here: Stated in the opening: both policies are re-estimated on an expanding window and held out of sample against their benchmarks, gross and net.
Paragraphs: none of its own.
Note: Heading only; the chapter's one figure shows the coefficients, not performance, and no cumulative-return or drawdown picture is drawn.

### The coefficients through time — 565

Says: Re-estimated at every model-year end on an expanding window, the size coefficient keeps its sign throughout, the momentum coefficient does not, costs in the objective shrink the faster-moving characteristic more, and the class coefficients are stable partly because the simplex caps them.
Why here: Stated: both policies are now run as an investor would have run them, from the register's out-of-sample start; the performance paragraph reads the stability back ("the one characteristic whose coefficient was stable").
Paragraphs:
- ¶1 [method] Estimate through the burn-in, re-estimate each model-year end on all data, weights from the latest estimate; gross and net objectives.
- (code: oos-estimates) `refit` dates asserted to be model years 11 to 31; `theta_path()` warm-started on the free path; four coefficient paths
- (code: fig-18-theta) coefficient paths by policy, gross solid and net dashed, from one data frame
- (code: theta-path-facts) hidden: signs, momentum's negative early dates, the shrinkage ordering
- ¶2 [result] Size negative at all 21 dates; momentum changes sign; costs shrink momentum more, as eq-18-cost says; class coefficients stable within the cap.
Note: ¶2 reads the figure and the hidden facts at once; the warm start for the free path against the cold start for the restricted one is a code detail the prose never mentions.

### Performance against the benchmarks — 1259

Says: Both policies beat their benchmarks net of costs, neither by a margin the paired test certifies; the equity gain is the size tilt and comes with shorting and a deeper drawdown; costs in the objective cut turnover at an unchanged net Sharpe; the class policy beats chapter 16's tilt but not the register's minimum variance.
Why here: Stated: the coefficients' stability says which characteristic pays; the equal-weight row must reproduce the register's so the comparison shares its accounting; the closing hands the equity policy to chapter 21 and the many-signal version to chapter 27.
Paragraphs:
- (code: oos-performance) `policy_path()`, the breach count, six weight paths, the register's Sharpe, `perf()`; the equal-weight row asserted equal to the register's
- (code: tbl-18-oos) six rows beside three register rows: Sharpe gross and net, certainty equivalents, turnover, drawdown
- (code: oos-facts) hidden: eq-25-se, the Jobson–Korkie/Memmel paired test, the short side; every ordering in the prose asserted
- ¶1 [result] Equity: net Sharpe and certainty equivalent above the benchmark; paired z suggestive, not significant; short and deeper drawdown; the size tilt pays.
- ¶2 [result] Costs in the objective cut turnover at an unchanged net Sharpe: the avoided trades were worth what they cost.
- ¶3 [result] Classes: Sharpe and certainty equivalent up, shallower drawdown, more turnover; paired z lifted by correlation; minimum variance in the register still ahead.
- ¶4 [claim] Beats chapter 16's tilt on the same information plus momentum; the scale was estimated, not chosen; chapters 27 and 21 follow.
Note: The longest section opens with three chunks and a table before any prose and then reads them in four paragraphs; the register comparison is made for the classes only, the equity sleeve having no register row; the standard error of a single Sharpe ratio and the paired test are both taken from chapter 25, which comes later.

## Key Takeaways — 252

Says: The policy and its parameter count, the GMM standard errors and the membership-not-forecasting test, the two long-only devices, the out-of-sample numbers and their insignificance, the stability and cost results, and the package's lack of a policy.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Benchmark plus linear tilt, coefficients by realized utility: two parameters for 123 equities instead of 7,749 moments [Brandt et al.].
- ¶2 [takeaway] A moment condition gives a sandwich covariance [Hansen], the bootstrap agrees; membership not forecasting: momentum enters as a hedge.
- ¶3 [takeaway] Truncation costs differentiability; restricting θ keeps the objective smooth and is set by the most extreme months.
- ¶4 [takeaway] Both out-of-sample net Sharpe ratios above their benchmarks; paired z-statistics short of significance.
- ¶5 [takeaway] Size keeps its sign, momentum does not; costs shrink the faster-moving characteristic and cut turnover at unchanged net Sharpe.
- ¶6 [takeaway] No parametric policy in `PortfolioAnalytics`; `Return.portfolio()` needs a path starting with the data; `turnover()` divides by N.
Note: Six bullets; the moment count appears for the third time; nothing on the timing version as a managed-portfolio problem or on the class policy against the register.

## Exercises — 160

Says: Four exercises: global instead of within-region standardization, the risk-aversion scaling, costs of 10 and 50 basis points, and truncation in place of the simplex restriction.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Standardize across all 123 rather than within region; the coefficients and the US weight; relate to chapter 5.
- ¶2 [exercise] γ = 2 and 10; do coefficients scale as 1/γ like eq-03-separation; what happens to the short side.
- ¶3 [exercise] Costs of 10 and 50 basis points in the objective; which coefficient shrinks more, explained by each portfolio's turnover.
- ¶4 [exercise] Truncation in place of the simplex, derivative-free from two starts on the burn-in; the scale of θ and why.
Note: Four exercises, three on the equity policy; 4 is the one test of the theory's derivative-free claim, which the chapter asserts and never runs.
