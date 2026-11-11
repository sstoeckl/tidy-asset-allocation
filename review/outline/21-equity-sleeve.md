---
file: chapters/21-equity-sleeve.qmd
title: The Equity Sleeve
part: Inside the Sleeves
words: 6729
sections: 5
paragraphs: 33
---

# Chapter

Claim: Selection survives the allocation only in the sense the arithmetic allows: the sleeve's information ratio reaches the total intact while its active return and tracking error arrive scaled by the equity budget ω, and on this market what the total registers is the selected sleeve's lower variance, not an alpha that the out-of-sample months cannot distinguish from zero.
Question: Which stocks should fill an equity sleeve whose budget and benchmark are fixed from above, and is whatever the selection earns still visible once the sleeve is one line of the allocation; @fama1992 and @fama1993 for selection by sorting as a method, @treynor1973 for combining the active sleeve with the passive portfolio.
Why here: Stated: the first chapter to work inside a class rather than across classes, the granularity axis of chapter 3 made concrete on the 123 equities behind the five series that Parts III to V allocated as single numbers. Takes from chapter 2 the capitalization-weighted indices and the independence of the idiosyncratic draws, from chapter 5 the lagged proxy and the within-region lesson, from chapter 7 the rank bound, the repairs and the race, from chapter 12 the dropped position limit, from chapter 15 the policy and the sub-portfolio mechanics, from chapter 18 the parametric estimate of the same characteristics; sends forward to chapter 22 (a duration in place of a characteristic), chapter 23 (the cost of the trading) and chapter 25 (the register). Its mandate, active-weight notation, fundamental law, information-ratio standard error, budget figure and cone solver are all taken from chapter 24, three chapters later, which the text treats throughout as already read.
Does: Rebuild a capitalization-weighted benchmark from its instruments with the right lag, run within-region characteristic sorts with Newey–West inference, build a factor or shrunk covariance on a universe wider than the window, solve a minimum-variance sleeve under a tracking-error budget by a one-parameter quadratic family and a root search, wrap sleeves as sub-portfolios, and trace a sleeve's active return into the total portfolio.
Order: Theory (mandate and the ω arithmetic, sorts, equal weighting, covariance with the cardinality limit and the tracking-error family), implementation (benchmark rebuilt, equal against cap, sorts, covariance race, the budgeted sleeve, the sub-portfolio), application in one undivided section (policy recomputed, three fillers, sleeve rows, total rows, sampling error, the figure), five takeaways, four exercises; deviations: the application opens with code and a table and reaches its only figure last, and the sub-portfolio subsection builds a structure the application then sets aside.

# Sections

## (opening) — 391

Says: An equity sleeve arrives with its budget and benchmark fixed from above, and which names fill it and whether selection is still visible one level up have been one question since Treynor and Black.
Why here: the opening by contract; ¶2 lays out the chapter's order in three steps and places the sleeve on the horizon axis as strategic.
Paragraphs:
- (code: setup)
- ¶1 [claim] Budget and benchmark are given; which names, and does selection survive one level up; @fama1992, @fama1993, @treynor1973; first chapter inside a class.
- ¶2 [method] The plan in three steps; on the horizon axis the sleeve is strategic, conditioning only on a rolling covariance and benchmark weights.
- (code: data)
Note: ¶1 places the chapter on the granularity axis and ¶2 on the horizon axis; the data chunk asserts the equities align with the class series before any theory.

## Selection Inside a Budget — 1050

Says: A sleeve is judged against the class index it sits in under a tracking-error budget that scales active return and tracking error but not the information ratio; size and momentum are the sorts this market allows; and 123 names force a covariance repair and turn the budget into a one-parameter family.
Why here: stated in the opening's plan: benchmark and mandate, the arithmetic, the sorts, the estimation problem, before anything is built.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: four subsections on four topics, and the fourth also carries the cardinality limit and the tracking-error family, which its heading does not announce.

### The benchmark, the mandate, and the arithmetic of a sleeve — 314

Says: The benchmark is the regional capitalization-weighted index, the mandate is chapter 24's tracking-error budget, and the sleeve's active return and tracking error reach the total scaled by its budget ω while its information ratio does not.
Why here: stated: budget and benchmark come from above and are fixed before any selection is scored; the application is announced as checking both halves of the arithmetic.
Paragraphs:
- ¶1 [definition] Benchmark is chapter 2's regional index via chapter 15; b, v, x = v − b; mandate: maximal active return within τ, scored by the IR.
- ¶2 [derivation] Active return and TE scale by ω, the IR does not (eq-21-omega); @treynor1973's bound (eq-21-treynor-black); a worked number; the application checks both.
Note: ¶2 carries two numbered equations, the worked example and the application's plan in one paragraph; the mandate, the active weights and the information ratio are all chapter 24's, three chapters ahead.

### Selection by characteristic — 231

Says: Size and momentum are the sorts this market can run, within region and averaged across five, because value needs a fundamental the data lack and a global sort sorts on region; breadth is why a sleeve can earn an information ratio from a weak signal.
Why here: not stated; follows the mandate and precedes the equal-weighting case whose gap the sorts are later asked to separate.
Paragraphs:
- ¶1 [method] A sort defined and attributed; value impossible without a fundamental; premia local, so sorts run within region (@griffin2002); chapter 18 estimates the same two.
- ¶2 [claim] Breadth: the fundamental law (@grinold1989, eq-24-law) buys the same IR from a smaller IC over hundreds of names; @clarke2002's long-only cost.
Note: ¶1 does three things, defines a sort, surveys the literature and takes the within-region design decision; ¶2 rests on chapter 24's statement of the fundamental law.

### Equal weighting is an active bet — 98

Says: Holding 1/N is a size tilt and a contrarian rebalancing rule at once, long every name smaller than average, and inside a sleeve the question is whether that bet pays.
Why here: not stated; it is the simplest departure from the benchmark and the one the implementation measures first.
Paragraphs:
- ¶1 [claim] 1/N is a size tilt plus monthly contrarian rebalancing (@plyakha2021, @demiguel2009); chapter 24 saw it as a benchmark; here a bet against the largest names.
Note: one paragraph; the heading is a claim sentence rather than a noun phrase.

### The covariance matrix of a sleeve — 401

Says: With 123 names any window under 124 months is singular, so the sleeve needs shrinkage or a k-factor structure; a cardinality limit is a mixed-integer problem whose convex substitute is a cap; and the budget on a minimum-variance sleeve is a one-parameter blend of benchmark and minimum variance found by a root search.
Why here: stated: everything the sleeve optimizes needs Σ, and chapter 7's rank bound says the sample estimate cannot deliver it on this universe.
Paragraphs:
- ¶1 [definition] eq-07-rank: singular under 124 months; shrinkage (@ledoit2003, @ledoit2004) or BB' + D (eq-21-factor-cov); @connor1993, @bai2002; settled out of sample.
- ¶2 [derivation] Within region estimable but thin; cardinality is MIP (@bienstock1996), a cap its substitute (@jagannathan2003); the budget's Lagrangian gives v(θ) (eq-21-family); @roll1992.
Note: ¶2 holds three topics, the within-region parameter count, the cardinality limit and the tracking-error family; the family is the chapter's own device and arrives at the end of a subsection named for the covariance matrix.

## Implementation — 2984

Says: The benchmark reproduces from the instruments; equal weighting beats it everywhere at a tracking error most mandates forbid; size is present and momentum absent by construction; factor matrices give the lowest volatility and shrinkage the highest Sharpe ratio; the budgeted sleeve is a blend; and a sub-portfolio can carry its estimator but not its budget.
Why here: stated in the opening's plan: rebuild, measure, sort, race, build, wrap, in that order.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: six subsections, one per step of the plan; the last builds the package's sub-portfolio structure and ends by saying the application cannot use it.

### The benchmark, rebuilt from its instruments — 431

Says: The five regional indices reproduce from previous-week capitalization weights to machine precision, and capitalization weighting is itself concentrated, the US index behaving like a fraction of its names.
Why here: stated: rebuilding the benchmark is the check that it is one the sleeve could have held; the monthly weights it yields are what every later step indexes by name.
Paragraphs:
- ¶1 [method] Class series are weighted on the previous week's capitalization, chapter 5's lag; rebuilding checks the benchmark was holdable.
- (code: benchmark)
- ¶2 [result] The five series reproduce to machine precision; the monthly weight is the last capitalization before the month began.
- (code: cap-month)
- (code: tbl-21-concentration)
- ¶3 [result] Capitalization weighting is concentrated: the US index behaves like a fraction of its names, the Swiss like fewer.
Note: the concentration table is read in one sentence; its ratio and top-five columns are never mentioned, and the largest-weight column is used only two subsections later to set the cap.

### Equal against capitalization weighting — 295

Says: Equal weighting earns more than its benchmark in every region, by one to four points a year, at a tracking error larger than most mandates allow and an information ratio mostly within two standard errors of zero.
Why here: stated in the theory: the question was whether the bet pays; the result hands the sorts the question whether it is size or rebalancing.
Paragraphs:
- (code: ew-cw)
- (code: tbl-21-ew-cw)
- ¶1 [result] Equal beats cap in every region at a large TE; IRs mostly within two standard errors (eq-24-se) of zero; size or rebalancing is for the sorts.
Note: the subsection opens with code and a table and has one paragraph; the chunk asserts the ordering the prose relies on.

### Sorting on size and momentum — 551

Says: Within region, small beats large with a t-statistic above two and the long-only leg keeps part of it; momentum is absent, and absent by construction, because the idiosyncratic draws are independent period by period.
Why here: stated: the sorts separate the equal-weight gap into a size premium and rebalancing; the design, within region and averaged, was fixed in the theory.
Paragraphs:
- ¶1 [method] Size is the benchmark weight; momentum t−12 to t−2 (@jegadeesh1993); terciles within region, averaged; long-short and long-only; @newey1987 at six lags.
- (code: sorts)
- (code: tbl-21-sorts)
- (code: sorts-verdict)
- ¶2 [result] Size present at t above two, the long-only leg keeps part; momentum absent by construction, the idiosyncratic draws being independent; a real market has it.
Note: ¶2 carries the result and the caveat that explains it away; the promised separation of size from rebalancing is not performed here, only the size half is shown, and exercise 3 asks the reader for it.

### A covariance matrix for one hundred and twenty-three names — 753

Says: The package's factor model refuses the window it is needed on, a six-line replacement reproduces it where it runs, and in a rolling race the factor matrices give the lowest volatility while shrinkage gives the highest Sharpe ratio, the sample matrix producing no portfolio on any window.
Why here: stated: the theory said the sleeve needs a repair before it can be optimized at all; the race is chapter 7's, rerun on the sleeve's names.
Paragraphs:
- ¶1 [code] `statistical.factor.model()` and `extractCovariance()` fit eq-21-factor-cov; they run on the full sample, not on the ten-year window.
- (code: factor-models)
- ¶2 [caveat] (callout) The function stops when T < N, the window it exists for; `factor_covs()` is its body without the check, asserted equal where both run.
- ¶3 [method] The first component's variance share read; the race is chapter 7's: minimum variance, long only, 120-month window, from observation 121; the sample matrix fails everywhere.
- (code: race)
- (code: race-check)
- (code: tbl-21-race)
- ¶4 [result] Shrinkage row reproduces chapter 7's; factor matrices give the lowest volatility, shrinkage the highest Sharpe; which is better depends on what the mandate scores.
Note: ¶3 opens by reading a number and then announces the race; the callout repeats chapter 7's route-two caveat on the same function; the race leaves the choice open and the next subsection takes shrinkage without saying why, although the factor matrices won on the number a minimum-variance sleeve minimizes.

### The selected sleeve — 681

Says: Unconstrained minimum variance holds a handful of names with a large weight in one; the cardinality limit is dropped on the variance path, so a cap per name stands in; and under a four percent budget the family picks a blend that buys a stated share of the distance between benchmark and minimum variance.
Why here: stated: the mandate limits the concentration the unconstrained solution shows, and the budget enters through the family because the package cannot express it, for the reasons chapter 24's callout gives.
Paragraphs:
- ¶1 [method] Built for the US at the first out-of-sample month, chapter 7's shrinkage moments through `momentFUN`.
- (code: us-setup)
- ¶2 [result] Unconstrained minimum variance holds few names with a large share in one; a mandate limits that, and the package has two ways of writing the limit.
- (code: position-limit)
- ¶3 [caveat] (callout) Under variance `ROI` drops the position limit and returns the unconstrained weights, as chapter 12 measured; under ES `Rglpk` honors it; @chang2000; the cap substitutes.
- ¶4 [method] Cap of ten percent or the benchmark's own weight; budget of four percent as chapter 24 spent; enters through eq-21-family, solved hundreds of times.
- (code: select-sleeve)
- ¶5 [result] The sleeve holds its names, spends the budget exactly, sits between benchmark and minimum variance by a stated share: eq-21-family read as a blend.
Note: the position-limit chunk sits inside the callout; the callout's finding repeats chapter 12's trap on a new universe; `select_sleeve()` is built once here and reused monthly in the application.

### The sleeve as a sub-portfolio — 270

Says: `mult.portfolio.spec()` wraps each regional sleeve as a sub-portfolio with its own covariance estimator through `momentFUN`, with chapter 15's three quirks intact, but cannot carry the tracking-error budget, so the application runs its two stages by hand.
Why here: stated: it is the package's structure for a sleeve the allocation layer can consume, and chapter 15 set its arguments; what it cannot do is why the application is built differently.
Paragraphs:
- ¶1 [method] `mult.portfolio.spec()` after chapter 15; each regional sleeve a sub-portfolio, minimum variance under the cap, re-estimated yearly; the top level allocates across five proxies.
- (code: sub-portfolio)
- ¶2 [caveat] Three quirks carry over from chapter 15; `momentFUN` passes through the dots, so a sleeve carries its estimator; the budget does not, so the application runs by hand.
Note: the chunk prints the top-level weights and no paragraph reads them; the subsection demonstrates a structure the chapter then does not use, and its yearly re-estimation under a flat cap differs from the application's monthly, budgeted sleeve on both counts.

## Selection Under the Allocation Above It — 1853

Says: Filling the policy's equity budget three ways, the sleeve's active return and tracking error reach the total scaled by ω and its information ratio intact; neither sleeve's information ratio is two standard errors from zero, and what the total registers is the selected sleeve's lower variance rather than an alpha.
Why here: stated in the opening's plan: fill the equity budget of chapter 15's policy three ways and ask what the total portfolio noticed; the policy is recomputed so the budget is computed rather than quoted.
Paragraphs:
- ¶1 [method] The allocation above is chapter 15's policy, recomputed so the budget handed down is computed rather than quoted.
- (code: policy)
- ¶2 [method] ω and its US/EU split; three fillers; ten basis points on each sleeve's trades as eq-23-net; the benchmark pays to track its own weights; class rebalancing uncharged.
- (code: fill)
- (code: omega-check)
- ¶3 [result] The ratio of the two tracking errors is ω to four decimals and the two IRs coincide: eq-21-omega in the data.
- (code: scores)
- (code: tbl-21-fill)
- (code: fill-verdict)
- ¶4 [result] Sleeve rows: both IRs within two standard errors of zero, as chapter 24 said in advance; the selected sleeve delivers lower volatility, a TE near budget, a higher Sharpe.
- ¶5 [result] Total rows: three Sharpe ratios; net within a hundredth of gross; equal weighting adds return, the selected sleeve takes half a point off volatility; total TEs.
- ¶6 [claim] Nothing established against sampling error (@jobson1981, @memmel2003); selection survived as eq-21-omega allows: IR intact, α and TE scaled, variance the visible part; drawdowns close.
- (code: fig-21-active)
- ¶7 [result] The figure: two panels, the lower the upper times ω; manager above, policy owner below; chapter 22 next, chapters 25 and 23 for the IR's reality and the trading.
Note: one undivided section of 1,853 words and seven chunks; the only figure arrives last and is read in the closing paragraph, against the house rule that an application opens with the picture; ¶6 ends on a drawdown sentence unconnected to its sampling-error point; the Sharpe-difference z-tests are computed in a hidden chunk and never tabled.

## Key Takeaways — 221

Says: Five bullets: the benchmark and the budget, the ω arithmetic and the Treynor–Black bound, size present and momentum absent by construction, the singular matrix and the race's split verdict, the cardinality trap and the one-parameter family.
Why here: by contract.
Paragraphs:
- [takeaway] The benchmark is the class index, reproduced from the instruments with a one-week lag; the sleeve is judged under a tracking-error budget (@grinold2000, @roll1992).
- [takeaway] Active return and TE scale by ω, the IR does not (eq-21-omega); eq-21-treynor-black bounds the total's gain (@treynor1973).
- [takeaway] Size present, momentum absent by construction, value unbuildable; equal weighting is a size tilt and a contrarian rule (@plyakha2021).
- [takeaway] 123 names make the sample matrix singular under 124 months; factor matrices give the lowest volatility and shrinkage the highest Sharpe (@ledoit2004, @bai2002).
- [takeaway] The cardinality limit is dropped on the variance path and honored on ES; the cap substitutes; the budget is eq-21-family; a sub-portfolio carries its estimator, not the budget.
Note: five bullets, on contract; none states the application's finding, that neither sleeve's information ratio is distinguishable from zero and that the total registers variance rather than alpha, which is the chapter's claim.

## Exercises — 180

Says: Four exercises: the budget varied, the momentum signal varied, annual against monthly equal weighting, and the Treynor–Black weight against the policy's budget.
Why here: by contract.
Paragraphs:
- [exercise] 1. The US sleeve at two, four and eight percent budgets, re-estimated monthly; realized TE, IR, volatility; whether realized TE stays inside the budget and why not.
- [exercise] 2. Momentum over t−6 to t−2 in quintiles; recompute the sorts; whether momentum appears and what its appearance would have to mean.
- [exercise] 3. Equal weighting rebalanced annually: turnover and net Sharpe against monthly; attribute the gap to size tilt and rebalancing as @plyakha2021 do.
- [exercise] 4. Appraisal ratio of the equal-weighted US sleeve and the ω* of eq-21-treynor-black against the policy's budget; what the comparison does and does not say.
Note: four against "around three"; exercise 3 supplies the size-versus-rebalancing separation the sorts subsection promised, and exercise 4 the ω chosen for the ceiling that the theory said the policy does not choose.
