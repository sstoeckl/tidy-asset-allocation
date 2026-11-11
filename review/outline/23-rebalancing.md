---
file: chapters/23-rebalancing.qmd
title: Rebalancing and Transaction Costs
part: Implementation and Evaluation
words: 3281
sections: 5
paragraphs: 34
---

# Chapter

Claim: Free monthly rebalancing is worth different amounts to different strategies: under per-class linear costs the Sharpe ratio lost to trading is ordered by how much a strategy optimizes, rebalancing less often helps the two rule-based portfolios at every estimation window and moves the three optimized ones by more, in a direction that changes with the window, and theory's answer is a no-trade region or a partial adjustment rather than a return to target.
Question: What the assumption of free monthly rebalancing to target is worth, and to which strategies; posed as a statement about the book so far, not as a question, with @peroldshortfall1988 (the implementation shortfall) in the third sentence rather than the first two.
Why here: Stated in the first sentence only: every portfolio so far was rebalanced monthly at no charge. Draws on chapter 4 (the Sharpe ranks of tbl-04-moments, the wandering rolling mean, the credit crisis), chapter 9 (the optimizers, and maximum Sharpe as that chapter's best portfolio), chapter 14 (inverse volatility) and chapter 18 (costs in the objective by construction); reads every measurement from the out-of-sample runs it attributes to chapter 25, two chapters ahead, said to have been computed with and without costs for this purpose; hands `contribution` to chapter 24 and the sources of the cost rates to appendix 93. Why it opens the part, ahead of the backtesting chapter whose runs it reads, is not stated.
Does: Compute one-way turnover by hand and from `Return.portfolio(verbose = TRUE)`, recognize the equal-weight back-fill and the two meanings of a turnover constraint, and read frequency and cost effects for five strategies off the sweep; charging eq-23-net or running a backtest is not shown in code.
Order: Opening, theory (turnover and the cost model, per-class rates, no-trade region and partial adjustment), implementation (three package behaviors), application (frequency table, cost-bite table and figure, calendar against band rules, limits of the cost model), seven takeaways, four exercises; deviations: the theory opens on a chunk and runs code, the implementation section computes nothing the application reads (the sweep comes from a file, and the chapter runs no backtest and charges no cost), the application opens with a table rather than a picture and ends in two prose-only subsections of literature and caveats, and the packages block is hidden.

# Sections

## Opening — 167

Says: Free monthly rebalancing is not a small assumption; the chapter defines turnover and costs, sets out the theory on how often to trade and measures both on the out-of-sample runs, with its three findings stated up front.
Why here: the opening by contract; ¶2 gives the order (definitions, theory, measurement) and says the runs of chapter 25 were computed with and without costs for this purpose.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Every portfolio so far returned to target monthly at no charge; @peroldshortfall1988's implementation shortfall matters more to some strategies.
- ¶2 [method] The plan in three steps, then the finding: rules gain from rarer rebalancing, optimizers' sign varies, bite grows with optimizing.
- (code: data) reads `output/tables/oos-sweep.csv`; the sixteen class returns as xts
Note: the citation sits in the third sentence; ¶2 gives all three results before any definition and its plan names no implementation step; ¶1's premise sits against chapters 16 and 18 to 22, which already charge the `pm_costs_default()` rates, four of them citing eq-23-net ahead; no visible packages block.

## Turnover, Costs, and When to Trade — 717

Says: Turnover is half the summed absolute weight change, its cost is linear and differs by asset class, and with costs theory replaces the return to target with a no-trade region or a partial adjustment.
Why here: stated in the opening's plan: turnover and the cost model first, then what theory says about how often to trade; the application reads its results through eq-23-partial.
Paragraphs: none of its own; the section goes straight to its first subsection.

### Turnover — 305

Says: Turnover is half the L1 distance between drifted and wanted weights, the net return subtracts a per-asset linear charge on the trade, the package's own `turnover()` uses another divisor, and linearity holds at asset-class scale only.
Why here: the plan's first step; no reason beyond the order is stated. eq-23-turnover and eq-23-net are the units of everything measured later.
Paragraphs:
- (code: turnover-def)
- ¶1 [definition] Turnover as half the summed absolute difference between drifted and wanted weights (eq-23-turnover).
- ¶2 [definition] Finishes ¶1's sentence (halved: one trade, not two), then the net return under per-asset one-way costs (eq-23-net).
- ¶3 [caveat] The package's `turnover()` divides by the asset count, an eighth here; annualized, a hundred percent means replaced once.
- (code: turnover-pa) asserts the package's figure times N over two equals the function's
- ¶4 [caveat] eq-23-net is linear: fine for asset classes, not single securities (@kyle1985, @almgren2001); @amihud2002 and @novymarx2016 on illiquidity and costs.
Note: opens on a chunk, so the definition appears first as a code comment; the cost model is defined under "Turnover", in the tail of the turnover sentence; the `turnover()` trap is in running prose, not a callout; the function defined here is called once, in the assertion; ¶3 joins two unrelated points (the package divisor, annualization).

### Costs are not a single number — 213

Says: Cost rates differ by asset class, the defaults are arguments rather than constants, and the dearest class to trade is among the three best Sharpe ratios of the sixteen.
Why here: stated in ¶1: the rate in eq-23-net depends on what is traded; needs eq-23-net from the subsection before and tbl-04-moments for the Sharpe rank.
Paragraphs:
- ¶1 [claim] The rate depends on the asset; one average overcharges cheap sleeves and undercharges dear ones, most where trading is heaviest.
- (code: costs) prints `pm_costs_default()`
- (code: credit-rank) hidden; asserts `US_credit` in the top three Sharpe ratios and credit the dearest class
- ¶2 [result] One-way rates, government against credit in basis points; defaults sourced in appendix 93; conclusions said to survive halving or doubling.
- ¶3 [claim] Credit is dearest to trade and `US_credit` ranks near the top by Sharpe: what chapter 9's optimizers want costs most.
Note: ¶2's robustness to a factor of two is asserted, not shown, and exercise 1 hands the doubling to the reader; ¶1's examples (high-yield credit, emerging equity) are finer than the class rates the chunk prints; heading is a sentence.

### What theory says about how often to trade — 191

Says: With costs in the objective the optimal policy is a no-trade region around the target or, for a moving target, a partial adjustment toward an aim portfolio at a rate that falls as costs rise.
Why here: the plan's second step; ¶2 says its distinction (a fast target trades partially and often, a stable one drifts) is what the measurements below recover.
Paragraphs:
- ¶1 [definition] @constantinides1986 and @davis1990: a no-trade region; inside it do nothing, outside it trade back to the boundary only.
- ¶2 [derivation] @garleanu2013: partial adjustment toward a cost-weighted aim portfolio (eq-23-partial); fast targets trade partially and often, stable ones drift.
Note: ¶2 promises that the measurements recover the distinction; the application then reports the optimizers gaining from annual rebalancing at two of three windows and reads the equation as explaining the size of the move, not its sign; heading is a clause.

## Implementation — 453

Says: Three package behaviors: a turnover constraint is hard under one backend and a penalty under the other, `Return.portfolio()` back-fills equal weights before the first weight date, and `verbose = TRUE` returns the weights turnover is computed from.
Why here: not stated; the opening's plan goes from the theory to the measurement and does not mention this section.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: nothing here produces what the application reads: no backtest is run, eq-23-net is never applied in code, and `pm_backtest()` is named but not called.

### A turnover constraint is not a turnover constraint everywhere — 127

Says: `turnover_constraint()` is a hard limit under `ROI` and a penalty under `CVXR`, and proportional costs exist only under `ROI`.
Why here: not stated; opens the section with no link back to the theory or forward to the measurements.
Paragraphs:
- ¶1 [caveat] The package accepts the constraint under both solver families, and they mean different things by it.
- ¶2 [caveat] (callout) Hard under `ROI`; a penalty under `CVXR`, so an attractive enough portfolio buys its way past the limit.
- ¶3 [caveat] (callout) The same split for costs: `transaction_cost_constraint()` only under `ROI`; under `CVXR` nothing is applied or reported.
Note: no code: both behaviors are asserted, and exercise 3 hands the demonstration to the reader; the subsection is one sentence and a callout whose title restates it; heading is a sentence.

### The accounting that rewrites the start of a backtest — 220

Says: `Return.portfolio()` fills the months before the first supplied weights with an equal-weight portfolio and only warns, which in a rolling backtest is the normal case.
Why here: stated in ¶1: it is the obvious way from a weight history to returns, so its behavior should be known before relying on it; ¶3 names `pm_backtest()` as what does the accounting instead.
Paragraphs:
- ¶1 [caveat] `Return.portfolio()` is the obvious route from weights to returns and has a behavior to know first.
- (code: backfill) weights dated at months 12 and 18 of a 24-month slice, all in `US_government`
- ¶2 [result] The call warns: first weights fall after the data start, earlier periods are set to equal weight.
- (code: backfill-evidence)
- ¶3 [result] The first months track equal weight, not the stated portfolio; a rolling window always creates the gap; `pm_backtest()` accounts explicitly.
Note: the trap gets a subsection of running prose, not a callout; ¶2 quotes the warning in full, and the project renders with `warning: false`; ¶3's line count for `pm_backtest()` is typed.

### What `verbose = TRUE` returns — 103

Says: With `verbose = TRUE` the same call also returns beginning- and end-of-period weights, whose difference is drift turnover, and a per-asset contribution.
Why here: not stated; continues on the objects of the subsection before; ¶3 hands `contribution` to chapter 24, and the band-rule subsection later builds on `EOP.Weight`.
Paragraphs:
- ¶1 [code] `Return.portfolio(verbose = TRUE)` returns considerably more than a return series.
- (code: verbose)
- ¶2 [code] `BOP.Weight` and `EOP.Weight` are the weights before and after drift; their difference gives eq-23-turnover directly.
- (code: turnover-from-verbose)
- ¶3 [code] `contribution` splits the return by asset, the raw material for chapter 24; most users take `$returns` only.
Note: the five values the last chunk prints are not read; it recomputes the half-L1 inline rather than calling `turnover()`; the stated portfolio holds one asset, so the positive drift it prints can only come from the back-filled equal-weight months of the subsection before.

## What Rebalancing Costs, Measured — 1489

Says: Read from the sweep: rarer rebalancing helps the two rules at every window and moves the optimizers by more in either direction, costs take most from the strategies that optimize most, the width of a band matters more than its trigger, and the linear constant-rate model understates what the optimizers pay.
Why here: stated in the opening's plan as the third step: measure on the runs of chapter 25, computed with and without costs for this purpose.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: the first two subsections read the sweep file, the last two are prose with no code; the section opens on a table, and the chapter's one figure comes in the second subsection.

### What rebalancing less often does to rules and to optimizers — 537

Says: Gross of costs, annual instead of monthly rebalancing raises the Sharpe ratio of equal weighting and inverse volatility at every window, lowers the three optimizers' at sixty months and raises it at the other windows; eq-23-partial is offered as the reason.
Why here: not stated; the first use of the sweep; ¶3 calls on eq-23-partial and ¶4 on the no-trade region of the theory section.
Paragraphs:
- (code: frequency) the sixty-month gross table, and assertions on the sign of annual minus monthly at every window
- (code: tbl-23-frequency)
- ¶1 [code] Key to the table: three Sharpe columns, then three turnover columns.
- ¶2 [result] Rules gain when left alone at every window; optimizers lose at sixty months, gain elsewhere; size stable, sign not.
- ¶3 [claim] eq-23-partial as the reason: a rule's target is fixed, an optimizer's is a moving estimate; chapter 4 measured the decay.
- ¶4 [claim] Optimizers either pay to chase an unstable estimate or hold a stale one; hence @davis1990's region widens with target volatility.
Note: two chunks before any prose; the table is gross, so the subsection measures frequency, not cost, under a section titled for costs; ¶1 is a table key outside the caption; ¶2 carries the whole finding (rules, optimizers at sixty months, the other windows, size against sign) in one paragraph; ¶4's width property of the no-trade region is not stated where the region is defined; heading is a clause.

### And the cost falls hardest on the strategies that can least afford it — 504

Says: Across the nine configurations the Sharpe ratio lost to costs is ordered by how much a strategy optimizes, and maximum Sharpe gives up the largest share of the lowest median gross Sharpe ratio.
Why here: the heading continues the one before with "And"; otherwise not stated; ¶3 turns the result into the case for costs in the objective and points to chapter 18.
Paragraphs:
- (code: bite) gross minus net Sharpe per configuration, medians per strategy, the accessors for the takeaways, assertions on the order
- (code: tbl-23-bite)
- (code: fig-23-bite)
- ¶1 [result] Median bite ordered by degree of optimizing; in every configuration both rules lose less than any optimizer; top two swap.
- ¶2 [result] Maximum Sharpe surrenders the largest share of the lowest median gross Sharpe; unseen in chapter 9; @novymarx2016 on anomalies agree.
- ¶3 [claim] So costs belong in the objective, not in an audit afterwards: two package functions, eq-23-partial, chapter 18's policy.
Note: three chunks before any prose; fig-23-bite is read by its caption alone, no paragraph refers to it; "how much a strategy optimizes" is never defined, the order is a typed list in the assertion; `turnover_objective()` appears here for the first time; ¶3's remedy is named and not run; heading is a sentence.

### Calendar rules against band rules — 259

Says: A band policy trades when a weight leaves its tolerance rather than on a date; the two families fail in opposite ways, and the literature finds the width matters far more than the trigger.
Why here: stated in ¶1: everything measured above rebalances on a calendar, which eq-23-partial suggests is not the natural policy; picks up the no-trade region of the theory and the `EOP.Weight` history of the implementation.
Paragraphs:
- ¶1 [definition] Everything above uses a calendar; a band policy trades when a weight leaves its tolerance, the no-trade region in practice.
- ¶2 [claim] Opposite failures: a calendar ignores what happened; a band has unpredictable turnover and can trade repeatedly across a boundary.
- ¶3 [evidence] @tokat2007: family matters less than width; @donohue2003 recover the no-trade region by dynamic programming; the width is the decision.
- ¶4 [caveat] The package has no band policy; a few lines around `EOP.Weight` would compare drifted weights to target each month.
Note: prose only inside the application: no band rule is run on the modeled market, and ¶4 describes the code in words instead of showing it; the material is theory and literature, continuing "What theory says about how often to trade".

### Where the cost model stops being credible — 183

Says: The measured bite is only as good as eq-23-net: linear and symmetric holds for index proxies only, and constant rates make the bite a lower bound for the optimizers.
Why here: stated in ¶1: the numbers above are only as good as eq-23-net, so its two limits are stated after them.
Paragraphs:
- ¶1 [transition] Two limits are worth stating, because the numbers above are only as good as eq-23-net.
- ¶2 [caveat] Linear and symmetric: defensible for the index proxies here, not for a single security (@kyle1985, @almgren2001).
- ¶3 [caveat] Rates are constant while real spreads widen in stress, as in chapter 4's credit crisis; a lower bound for optimizers.
Note: ¶2 repeats ¶4 of "Turnover" with the same two citations, and the first takeaway says it a third time; ¶3's premise that the optimizers' turnover is concentrated in stress episodes is asserted, not measured.

## Key Takeaways — 294

Says: Seven bullets: the two linear definitions, per-class costs, the no-trade and partial-adjustment policies, the frequency result, the monotone bite, the two-backend constraint, the back-fill.
Why here: by contract.
Paragraphs:
- [takeaway] Turnover is eq-23-turnover and its cost eq-23-net; both linear, defensible at asset-class scale, not for a single security.
- [takeaway] Costs are per class, government against credit in basis points; the dearest class carries a top-three Sharpe ratio.
- [takeaway] With costs, trade back only to the edge of a no-trade region, or adjust partially toward a moving aim (eq-23-partial).
- [takeaway] Rarer rebalancing helps the rules at every window; for the optimizers the sign depends on the window; the sixty-month numbers.
- [takeaway] The cost bite is monotone in how much a strategy optimizes: maximum Sharpe's median against equal weighting's.
- [takeaway] A turnover constraint is hard under `ROI` and a penalty under `CVXR`; proportional costs exist only under `ROI`.
- [takeaway] `Return.portfolio()` back-fills equal weights before the first weight vector and only warns; a rolling window always creates that gap.
Note: seven against "around five"; the order is theory, application, implementation, not the chapter's; no bullet for band width over trigger, the `turnover()` divisor, the lower-bound reading of the bite or `verbose = TRUE`.

## Exercises — 132

Says: Four exercises: doubled cost rates, a flat average rate, a turnover cap under both backends, and the drift of a never-rebalanced equal-weight portfolio.
Why here: by contract.
Paragraphs:
- [exercise] 1. Double every rate, recompute tbl-23-bite; does the order change, and what multiple brings maximum Sharpe's net Sharpe to zero?
- [exercise] 2. Replace the per-class rates with one flat average; which strategies does the simplification flatter, and why?
- [exercise] 3. Cap annual turnover at 25 percent on the maximum-Sharpe specification under `ROI` and `CVXR`; measure realized turnover; which bound?
- [exercise] 4. With `verbose = TRUE`: drift turnover of a never-rebalanced equal-weight portfolio over 31 model years; which series it becomes.
Note: four against "around three"; 1 and 2 ask for net returns under other rates, which the chapter shows no code for (it reads the sweep from a file); 3 is the demonstration the callout leaves out and needs a maximum-Sharpe specification the chapter never builds.
