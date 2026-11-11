---
file: chapters/12-constraints.qmd
title: Portfolio Constraints
part: Portfolio Optimization
words: 6900
sections: 5
paragraphs: 55
---

# Chapter

Claim: On this universe the constraints are the precondition for a portfolio anyone would hold, not a refinement of the optimization: a binding line is the mandate correcting the estimator (Jagannathan–Ma), the package accepts every constraint but honors only some, and so every solved weight vector has to be audited against the specification it came from.
Question: How does an investment policy statement, written in prose by a committee, become something a solver can read; cites Jagannathan and Ma (2003) in the second sentence and Frost and Savarino (1988) in the third.
Why here: Declares itself strategic allocation in chapter 3's vocabulary and takes chapter 3's quadratic utility and γ/2 convention; the problem, the GMV equation, the two anchors and the group-by-name rule from chapter 9; the shrunk covariance from chapter 7, the estimation error from chapter 8, the betas from chapter 5; borrows chapter 13's `maxSR` verification, its four-line `audit()` and its measurement of heuristics as if already read. Hands the non-convex solver choice to 13, `HHI()` to 14, sleeves to 15, scores to 20, turnover to 23, the transfer coefficient and tracking error to 24, the trap record to the solver matrix and the package notes. Why it follows chapter 11 and precedes chapter 13 inside the part: not stated.
Does: Build every constraint family in `PortfolioAnalytics`, know which solver honors which, audit a weight vector line by line with `audit_spec()`, price each line of a mandate by finite differences, and repair a dropped position limit with a screen.
Order: Theory (feasible set, shadow price, Jagannathan–Ma, transfer coefficient), implementation (anchors and helpers, then one subsection per family, closed by the audit function), application (a mandate solved, audited, repaired, priced line by line, read up a ladder), takeaways, exercises. Deviations: the theory's central equation is verified in a collapsed box inside the implementation; the families are implemented in neither the order of tbl-12-families nor by convexity; four traps are callouts while the two return-target traps are plain prose; the application ends in a conclusion subsection; four exercises.

# Sections

## Opening (untitled) — 288

Says: A policy statement is information about which estimates not to trust; this chapter is strategic allocation, and here is the sequence.
Why here: Contract position; the text says theory first, then every constraint type against chapter 9's anchors, then a mandate.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] The question; Jagannathan–Ma: a binding no-short constraint is covariance shrinkage, hence information; Frost–Savarino's earlier evidence.
- ¶2 [method] Strategic in chapter 3's sense, Brinson cited; theory, every family against chapter 9's anchors, then a mandate.
- (code: data) the sixteen classes less the bill, asserted
Note: The "packages used" block the contract asks for is hidden (`include: false`), so the reader sees no package list.

## From Policy Statement to Feasible Set — 940 (366 before the subsections)

Says: A mandate replaces R^N by a feasible set; every family but the position limit keeps it convex, a binding line has a shadow price, the long-only one is covariance shrinkage, and the cost of binding is read by the transfer coefficient.
Why here: Needs eq-09-problem; the opening's sequence sentence ("first set out what each family does to the feasible set and what a binding constraint is worth") is the only reason given; the implementation's family list and the application's shadow prices rest on it.
Paragraphs:
- ¶1 [definition] A constraint picks admissible weights; chapter 9's problem over R^N becomes eq-12-problem over a feasible set.
- ¶2 [definition] Markowitz's critical line, Perold, Kolm; the nine families with their sets and `add.constraint()` types, tbl-12-families.
- ¶3 [claim] Seven rows are half-spaces, the floor a ball, so convex and unique; only the position limit breaks it.
Note: The ## title names the feasible set; the three subsections under it are about what a binding line is worth, not where the set sits.

### What a binding constraint is worth — 175

Says: By complementary slackness a slack line could have been left out, and a binding line's multiplier is its shadow price, the rate at which the optimal variance falls when the bound is relaxed.
Why here: Needs eq-12-problem; the text says the application recovers eq-12-shadow by perturbing each bound, which is what this subsection defines.
Paragraphs:
- ¶1 [derivation] Lagrangian eq-12-lagrangian; Kuhn–Tucker conditions; complementary slackness; the shadow price eq-12-shadow, recoverable by perturbing a bound.
Note: One paragraph carries two numbered equations, the optimality conditions and the method the application later uses.

### The Jagannathan--Ma covariance — 211

Says: The long-only minimum-variance portfolio is the unconstrained one on a covariance from which each excluded asset's shadow price has been subtracted, so a binding constraint is the mandate correcting the estimator.
Why here: Needs the multipliers just defined and eq-09-gmv; no reason for its position is given, but the opening named this result as the chapter's answer.
Paragraphs:
- ¶1 [derivation] Under w ≥ 0 the constrained solution is chapter 9's GMV on a modified covariance, eq-12-jm.
- ¶2 [derivation] Two-line proof; excluded assets' covariances shrink by their shadow price; matches chapter 7's shrinkage; DeMiguel generalizes; thesis sentence.
Note: ¶2 carries the proof, its element-wise reading, two citations and the chapter's thesis sentence in one paragraph.

### What constraints cost in information — 188

Says: The transfer coefficient is the correlation between the risk-weighted positions the constraints allow and those the forecasts called for; it is one when nothing binds and falls with every line that does.
Why here: "The other side of the ledger": the cost after the benefit; hands the measure and the tracking-error limit to chapter 24.
Paragraphs:
- ¶1 [definition] Grinold's law with Clarke's transfer coefficient, eq-12-tc; Best–Grauer's switching mechanism; five more citations; tracking error to chapter 24.
Note: Eight citations in one paragraph; eq-12-tc is defined here and computed once, in the application's cost subsection.

## Implementation — 3252

Says: Two anchors and a weights-by-name helper, then every constraint family the package offers, each solved against the anchors, four of them with a callout where the solver drops the line, closed by an audit function.
Why here: The opening's sequence sentence only; the section has no paragraph of its own.
Paragraphs: none of its own.
Note: Heading only; ten subsections, 47 percent of the chapter.

### Two anchors and a bookkeeping function — 516

Says: Chapter 9's two anchors recomputed through one helper that returns weights by name and asserts the solve succeeded; the minimum-variance anchor's concentration is the reason the chapter exists; a collapsed box checks eq-12-jm on it.
Why here: "Everything below is measured against" the anchors, so they come first; the helper is what every later chunk calls; the Jagannathan–Ma check needs the long-only anchor the theory could not yet solve.
Paragraphs:
- ¶1 [method] Anchors recomputed, not retyped; `maxSR = TRUE` as chapter 13 verified.
- (code: helpers) `weights_of()`, `min_var()`, `tangency()`, `stats_of()`, `base_spec`, both anchors
- ¶2 [result] The minimum-variance anchor's share in one series is the reason the chapter exists; the application returns to it.
- ¶3 [derivation] (callout, collapsed) Multipliers read off the first-order condition; λ0 is the portfolio variance because w'δ is zero.
- (code: jm-check)
- ¶4 [result] (callout) Multipliers zero on held series, positive on excluded; eq-12-jm reproduces the solver; largest prices named; matrix stays positive definite.
Note: The theory's central equation is verified in a collapsed box the reader may skip, two subsections after it was derived; the helper chunk's assertion is the chapter's only guard against a silent `NULL`.

### Box constraints — 150

Says: A per-asset cap turns the one-series anchor into several positions at the cap, raising volatility and lowering the tangency Sharpe ratio.
Why here: Not stated; the families do not follow the order of tbl-12-families.
Paragraphs:
- ¶1 [method] `min` and `max` scalar or named by asset; a later box replaces an earlier one, layering a cap over `long_only`.
- (code: box)
- ¶2 [result] The cap binds on minimum variance: several positions at exactly 25 percent, higher volatility; the tangency Sharpe ratio falls.
Note: The replacement rule ¶1 relies on is explained only in the callout after the group subsection.

### Group constraints — 354

Says: A group constraint bounds class sums; the limits are bound by name and asserted against `split()`'s alphabetical order; the solver reads only the last group constraint in a specification.
Why here: Not stated; the callout's last-group rule is what sends the regional grouping to the linear-exposure subsection.
Paragraphs:
- ¶1 [method] Index vectors and limits in the same order, unenforced; `split()` is alphabetical, so limits are named and asserted, as chapter 9.
- (code: group)
- ¶2 [code] `extractGroups()` returns the sums by name; the chart is one call.
- (code: fig-12-group-weights)
- (code: group-binding)
- ¶3 [caveat] (callout) `get_constraints()` keeps only the last group and box constraint; a second grouping must be a linear exposure.
Note: The table of which group bounds bind (`group-binding`) is printed and never read; the figure is the package's base-graphics chart, unstyled.

### Weight-sum constraints — 189

Says: `full_investment` and `dollar_neutral` are the two ends of `weight_sum`; the bare constraint defaults to a one-percent band that a variance objective exploits.
Why here: Not stated.
Paragraphs:
- ¶1 [method] `full_investment` and `dollar_neutral` are `weight_sum` at one and zero; the long-short example needs chapter 3's quadratic utility.
- (code: weight-sum)
- ¶2 [caveat] (callout) The bare constraint defaults to a 0.99–1.01 band for the sampler; a variance objective uses the room.
- (code: weight-sum-default)
- ¶3 [result] (callout) The weights sum to 0.99, a cash position nobody asked for; write `full_investment` or both bounds.
Note: The dollar-neutral output (sum, gross, longs, shorts) is printed and never read in prose.

### A target return — 220

Says: The return constraint is an equality, so a target below the minimum-variance return lands on the dominated branch, and `maxSR = TRUE` ignores it altogether.
Why here: Not stated; "at least" as a floor imposed only where it binds is the rule the mandate applies.
Paragraphs:
- ¶1 [caveat] `return_constraint()` fixes the return; under ROI an equality, so a low target lands on the lower branch.
- (code: return-target)
- ¶2 [result] The 5% target is efficient, the 2.5% one dominated; a floor only where it binds; `maxSR = TRUE` overrides the target.
Note: Two package traps (the equality, the `maxSR` override) in plain prose while the next four families get callouts; ¶2 does the reading, the rule and the second trap.

### Position limits — 556

Says: The cardinality limit is accepted everywhere and honored on ROI's two mixed-integer paths and by the repairing searches; the quadratic path drops it without a message, and the Chang screen beats `DEoptim` at a fraction of the cost.
Why here: "The one row of tbl-12-families that is not convex"; the screen introduced here is what the application's repair reuses; chapter 13's point about heuristics on this universe.
Paragraphs:
- ¶1 [definition] At most k non-zero weights, the non-convex row; Bienstock: mixed-integer; accepted everywhere, honored in three places.
- (code: poslimit-roi) (callout)
- ¶2 [caveat] (callout) The variance path reads the limit and drops it, as on CRAN; honored only on the two `Rglpk` paths; `pos_limit_fail()` checks.
- ¶3 [method] The two honoring paths are linear mixed-integer programs; minimum expected shortfall shows it.
- (code: poslimit-milp)
- ¶4 [method] No exact variance route; `DEoptim` and random portfolios repair, `pso` and `GenSA` penalize and return everything; a seeded run.
- (code: poslimit-deoptim)
- ¶5 [result] `DEoptim` honors the limit; the Chang screen reaches lower volatility; neither certified; the search is worse and slower.
Note: The callout opens with its chunk and explains after; the MILP output is printed without a reading; the screen is introduced in a chunk comment, then cited in ¶5 and reused by the application.

### Leverage exposure — 364

Says: A gross-exposure bound is convex, yet under ROI the package returns the long-only portfolio because `gmv_opt_leverage()` omits the variable bounds, and under CVXR the constraint is not written at all.
Why here: Not stated.
Paragraphs:
- ¶1 [definition] Bounds the ℓ1 norm, the 130/30 constraint; linear once each weight splits into long and short parts.
- (code: leverage-roi) (callout) three routes: the package under ROI, under CVXR, and CVXR by hand
- ¶2 [caveat] (callout) ROI returns the long-only anchor: `gmv_opt_leverage()` omits `bounds`, so x ≥ 0 by default; CVXR ignores the line; write it by hand.
Note: The subsection's only result lives inside the callout; the callout's title names the ROI defect and its paragraph adds a second one on the CVXR path.

### Linear exposures, not only factor exposures — 244

Says: `factor_exposure` bounds B'w for any matrix: an indicator matrix adds a regional cap beside the group constraint, and betas bound market exposure, where a floor of 0.3 binds exactly.
Why here: "How a second grouping enters beside the group constraint above", the route the group callout promised; chapter 5's betas; chapter 20 uses the same constraint with scores.
Paragraphs:
- ¶1 [method] Any B with one row per asset; betas are one use, an indicator matrix the second grouping.
- (code: factor-region)
- ¶2 [method] Chapter 5's betas recomputed in one line against an equal-weighted equity composite.
- (code: factor-beta)
- ¶3 [result] The anchor's beta is below 0.3; the floor forces equity and binds exactly; chapter 20 swaps scores for betas.
Note: The regional sums the first chunk prints are never read; which region binds is left to exercise 3.

### Diversification — 382

Says: The floor is convex, but the package sends it only to the search solvers, where it is a band around a target rather than a floor, and ROI ignores it; the exact CVXR solve is markedly better on the objective.
Why here: Not stated; `HHI()` and `diversification()` are handed to chapter 14.
Paragraphs:
- ¶1 [definition] 1 − w'w ≥ d, one minus the Herfindahl index; convex, yet routed only to the searches, with two undocumented behaviors.
- (code: div-roi) (callout)
- ¶2 [caveat] (callout) ROI never reads the target; the searches penalize outside a ±5 percent band, so a target, not a floor.
- (code: div-deoptim) `DEoptim` against the exact CVXR floor
- ¶3 [result] The search lands in the band below the target, above the exact floor's volatility; Gilli's warning; chapter 14 reuses the functions.
Note: The CVXR solve reuses `w_var` defined inside the leverage callout, so a chunk in the running text depends on a chunk in a callout.

### Auditing a weight vector against its specification — 274

Says: Every failure above has one shape, a constraint present in the object and absent from the answer, and `audit_spec()` reads the specification and checks each line.
Why here: "Every failure above": the remedy after the four traps; extends chapter 13's four-line `audit()`; the application's audit table runs on it.
Paragraphs:
- ¶1 [method] Every failure above: in the object, absent from the answer; read the specification and check each line, extending chapter 13's `audit()`.
- (code: audit-spec) `audit_spec()`; the return line read as a floor
- ¶2 [result] The dropped limit is now a `FALSE` in a table; `chart.Weights()` draws the box bounds for one optimization.
- (code: fig-12-chart-weights)
Note: The closing figure draws the group-constrained tangency from an earlier subsection, not the audited vector, and the implementation ends on a figure with no prose after it.

## A Mandate, Line by Line — 2007

Says: An endowment's eight-line mandate is specified, solved on both objectives, audited, repaired where the solver dropped a line, priced line by line, and read up a ladder of its constraints.
Why here: The opening's last clause ("translate a complete mandate line by line ... solve it, audit it, and price each of its lines"); needs `audit_spec()`, the group indices and the Chang screen from the implementation.
Paragraphs: none of its own.
Note: Heading only; four subsections.

### The policy statement — 701

Says: Six lines enter directly, the return floor is imposed because it binds on minimum variance, the position limit is dropped by the quadratic path and caught by the audit, and a screen repairs it at a small cost in volatility.
Why here: The mandate has to exist and be solved before any line can be priced; the text says the audit "will say whether" the eighth line matters.
Paragraphs:
- ¶1 [example] The committee's eight lines; six linear, the seventh a floor only where it binds, the eighth non-convex and left to the audit.
- (code: mandate-spec) seven lines built; the floor tested without it
- ¶2 [result] Minimum variance under six lines earns below the floor, so it binds and enters as an equality; maximum Sharpe is checked after.
- (code: mandate-solve) both objectives solved and audited
- ¶3 [result] The tangency passes every line, the two unread included; minimum variance fails the limit, as the callout said; the Chang screen repairs.
- (code: mandate-repair) `build()` on any subset; eight largest kept, re-solved
- ¶4 [result] The repaired portfolio passes; the eighth line's cost in volatility is an upper bound because the screen is a heuristic.
- (code: tbl-12-mandate)
Note: The subsection titled for the policy statement also solves, audits and repairs; tbl-12-mandate, the mandate against chapter 9's anchors, closes it with no prose reading it.

### Which lines bind, and what each is worth — 599

Says: Tightening each of the seven read lines by one point and re-solving recovers finite-difference shadow prices: a few lines bind, most are slack in sample, and the return floor is the dearest for minimum variance.
Why here: Complementary slackness from the theory, applied as the theory said the application would; the cardinality line is excluded because the solver does not read it, its price being the repair above.
Paragraphs:
- ¶1 [method] Slack lines price at zero; eq-12-shadow by tightening each line one point and re-solving; the eighth line's price is the repair.
- (code: shadow) seven tightened specifications, both objectives
- (code: tbl-12-shadow)
- (code: shadow-reading) hidden; asserts the binding lines match the slacks and what the takeaways claim
- ¶2 [result] Which lines bind on each objective; slack lines are insurance, not free; the dearest line on each objective, with its price.
Note: The hidden chunk asserts the takeaways' three claims (two lines bind on both objectives, most are slack, the return floor is dearest), which is where the chapter's prose about its own results is guarded.

### What the mandate costs, and what it buys — 507

Says: In sample the mandate costs some Sharpe ratio and keeps most of it, measured by the transfer coefficient; what it buys is a portfolio instead of one position, and the in-sample cost is partly noise refused.
Why here: Prices the whole mandate after its lines; computes eq-12-tc from the theory; chapter 8's distrust of in-sample numbers and Jagannathan–Ma's point in Sharpe units.
Paragraphs:
- (code: cost) Sharpe ratios and the transfer coefficient
- ¶1 [result] Sharpe cost and share kept, the transfer coefficient; the largest position capped; the in-sample cost is partly noise refused, chapter 8.
- (code: ladder) five rungs of the mandate, both objectives, asserted
- (code: fig-12-ladder)
Note: Opens with a chunk, no prose before it; the ladder figure is read only in the next subsection, and its caption carries a reading (the tangency stops changing at rung three) the prose never repeats.

### Why the constraints come first — 193

Says: Unconstrained minimum variance on this universe is degenerate, the cap only pins it, and the class limits alone produce a portfolio a committee would recognize, so the constraints are the precondition rather than a refinement.
Why here: Reads fig-12-ladder from the first rung; Green–Hollifield and chapter 9's volatility ratio explain the degeneracy, chapter 8's estimation error makes the constrained answer the honest one; sleeves follow in chapter 15.
Paragraphs:
- ¶1 [claim] Rung by rung: one series, then a pinned cap still mostly government, then a recognizable portfolio; constraints are the precondition; chapter 15.
Note: A conclusion subsection before the takeaways; one paragraph carrying eight inline numbers and the chapter's thesis, and the reading of the figure the previous subsection produced.

## Key Takeaways — 241

Says: Five bullets.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Feasible set; every family but the position limit convex; choosing a constraint chooses the solver, chapter 13.
- ¶2 [takeaway] A binding long-only constraint shrinks the covariance by its shadow prices, eq-12-jm: the mandate correcting the estimator.
- ¶3 [takeaway] Shadow prices by tightening; here the equity floor and the cap bind on both, the return floor is dearest, cardinality is screened.
- ¶4 [takeaway] The package accepts every constraint and honors some: position limit, diversification, return target under `maxSR`, leverage, each on a named path.
- ¶5 [takeaway] Audit every returned vector: the package's checkers or `audit_spec()`.
Note: Five, on contract; ¶3 restates the shadow subsection's results in three sentences and is the bullet the hidden `shadow-reading` chunk guards; ¶4 is the trap list.

## Exercises — 172

Says: Four exercises.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] A 25 percent cap in the mandate: which lines bind, the equity floor's cost, tbl-12-shadow rebuilt.
- ¶2 [exercise] Jagannathan–Ma with upper bounds: recover both multiplier vectors from `w_gmv_box` and verify eq-09-gmv on the modified matrix.
- ¶3 [exercise] A 40 percent regional cap through `B_region` on both objectives: which region binds, how the Sharpe ratio moves.
- ¶4 [exercise] The exact diversification floor at four levels in CVXR, plotted; one `DEoptim` run at 0.6 placed on the chart.
Note: Four against "around three"; ¶3 asks for the reading the `factor-region` chunk printed and never gave; ¶2 extends the theory the chapter checked only for lower bounds.
