---
file: chapters/15-hierarchical-allocation.qmd
title: Hierarchical and Sleeve-Based Allocation
part: Allocation Strategies
words: 6717
sections: 5
paragraphs: 49
---

# Chapter

Claim: The two-layer organization (classes first, then selection inside a sleeve) is a governance decision whose cost can be measured: in sample the nested portfolio can never beat the flat one, and on sixteen classes it loses out of sample as well, at every window, because the cross-sleeve covariances stage 1 discards are information at this dimension; the case for the hierarchy arrives only where the flat matrix cannot be estimated.
Question: How should an allocation be organized when nobody can hold the whole problem in one head, and what does the organization cost; cites @sharpe1981 for the decentralized investment problem and @brinson1986 for how much the top-level decision explains.
Why here: Stated: this is the chapter in which the book's own structure (Parts III to V across the sixteen classes, Part VI inside a sleeve) is made explicit and priced, as a strategic decision in ch. 3's sense. Takes the flat problem, eq-09-gmv and eq-09-tangency from ch. 9, the shrinkage form and the rank finding from ch. 7, the hedging finding from ch. 4, the out-of-sample claim from ch. 8, the budget constraint from ch. 12, `quadprog` behind `ROI` from ch. 13, the missing HRP from ch. 14, the back-fill from ch. 23, the rolling backtest and the register from ch. 25. Hands the benchmarks to ch. 21 and ch. 22, the hedging instruction to ch. 22, the judging of the manager and the anchored variant to ch. 24. Why it opens Part V rather than closing Part IV is not stated.
Does: Partition the sixteen classes into sleeves, solve the nested problem by hand and with `mult.portfolio.spec()`, reproduce the package's proxy series, race nested against flat on a rolling window and check it against the register, and read a mixed-objective nested policy as a strategic asset allocation with benchmarks for the sleeve managers.
Order: Opening; theory (the two-stage problem, its shrinkage reading with two worked boxes, the benchmark reading, hedging); implementation (the one-asset failure, the package's method, the by-hand reproduction, the `opt.list` machinery); application (in sample, out of sample, the policy view); takeaways; exercises. Deviations: the theory section executes the chapter's solver, reads the in-sample ladder with its numbers inside a collapsed box, carries a 495-word box on a different method and a results table on hedging, and announces the out-of-sample verdict before the race runs; the two main headings have no paragraph of their own; the implementation's last subsection draws two figures no paragraph reads; no picture opens the application; six takeaways and four exercises.

# Sections

## Opening — 250

Says: Allocation runs in two layers because nobody holds the whole problem; the chapter makes the book's own two layers explicit and prices them.
Why here: Contract position; the text says this is where the book's structure is made explicit, and gives the order: state the problem, read it as shrinkage, implement it, test it out of sample.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Nobody holds the whole problem; Sharpe's decentralized problem, Brinson's measurement; two layers are every allocator's organization.
- ¶2 [method] The book's two layers made explicit, a strategic decision; order: state, read as shrinkage, implement, test out of sample.
- (code: data) the sixteen classes, the bill, excess returns; `N`
Note: No visible packages block; the setup chunk is hidden and the shown chunk loads data. ¶2 names the out-of-sample test before anything is defined.

## The Two-Stage Problem — 2585 (0 before the subsections)

Says: (heading only)
Why here: Contract position; the opening's sequence sentence puts the problem and its shrinkage reading first.
Paragraphs: none of its own.
Note: Heading only; four subsections of very unequal size (451, 1577, 174, 378), and the second carries the chapter's executed solver, two worked boxes and most of its citations.

### Sleeves, and what is decided at each level — 451

Says: The nested problem solves each sleeve on its own block and then allocates across the sleeve returns; the unrolled result is feasible for the flat problem, so in sample it can never have lower variance, and the gap is the price of decentralization.
Why here: First because the rest of the chapter is the gap between the two problems defined here; needs ch. 9's flat problem; the shrinkage reading takes the blocks and the application the in-sample bound.
Paragraphs:
- ¶1 [definition] Flat is Markowitz over all N; stage 1 solves each block, stage 2 allocates across sleeve returns; eq-15-stage1, eq-15-stage2.
- ¶2 [definition] The resulting weight is sleeve budget times within-sleeve weight; eq-15-unroll.
- ¶3 [claim] Objectives may differ by stage; what matters is that stage 1 sees one sleeve and stage 2 only K series.
- ¶4 [evidence] Unroll is flat-feasible, so nested is never lower in sample; the gap priced by five citations, Brinson's ninety percent restated.
- (code: sleeves) `sleeve_of()`; `split()` is alphabetical, everything indexes by name; the four sleeves and their sizes
- ¶5 [result] Four sleeves, three of five series and one of one; the single-asset case must be faced.
Note: ¶4 opens with the chapter's first claim (the in-sample bound) and then spends 130 words on six citations in one block; the sleeves are built in code after the mathematics has used K, and ¶5 is the only prose that reads the chunk.

### The shrinkage reading — 1577 (728 before the two boxes)

Says: Stage 1 is the flat problem on the block-diagonal matrix, a shrinkage estimator whose intensity the mandate sets rather than the data; stage 2 restores the cross-sleeve information in K-by-K form; with a diagonal Ω the whole construction collapses to flat minimum variance on Σ_B, so flat, nested and block-diagonal form a ladder, and where nesting sits on it depends on whether the cross-block covariance is signal.
Why here: Stated in the opening: the problem is read as a shrinkage of the covariance matrix before it is implemented; needs eq-07-shrinkage and Ledoit–Wolf from ch. 7; the application reads its ladder and its verdict through this subsection.
Paragraphs:
- ¶1 [claim] Stage 1 is flat on Σ_B (eq-15-block): eq-07-shrinkage with intensity one off-block, set by the mandate; Stein, Michaud.
- ¶2 [derivation] Stage 2 restores K(K−1)/2 covariances; diagonal Ω collapses to flat on Σ_B (eq-15-identity); the three-rung ladder.
- (code: cross-block) `S`, the same-sleeve mask, `S_block`; cross-block share of the squared mass, mean within and cross correlation
- ¶3 [result] Cross-sleeve entries carry a share of the squared mass; the race decides, and its answer follows Jagannathan–Ma.
- ¶4 [method] All of it is ch. 9's long-only QP, solved over a thousand times; `quadprog` called directly, checked once against `ROI`.
- (code: gmv-qp) `gmv_qp()`, `gmv_spec()`; `w_flat` from `ROI` asserted equal; `mu`, `p_vol()`, `p_ret()`, `p_sr()`, `eff_bets()`; the flat weights
- ¶5 [transition] (callout, collapsed) Lead-in: stage 1, stage 2 with diagonal Ω, and the unroll.
- (code: identity-check) `within_gmv()` with the one-asset case, `unroll()` asserting name order; inverse-variance budgets equal flat on `S_block`
- ¶6 [result] (callout) Inverse-variance budgets and flat on Σ_B agree to machine precision under long-only; nested proper uses the full Ω.
- (code: nested-in-sample) `sleeve_returns()`, `Omega`, `b_nest`, `w_nested`; the one negative sleeve correlation asserted
- ¶7 [result] (callout) Sleeve correlations: government–credit positive, equity–government the one negative; stage 2 can act on it, stage 1 could not.
- (code: ladder-in-sample) the three volatilities, Sharpe ratios and bets; the ordering asserted
- ¶8 [result] (callout) Ordering as guaranteed; nesting costs some volatility in sample, dropping every cross-sleeve covariance costs more.
- ¶9 [definition] (callout, collapsed) López de Prado's HRP: correlation tree, quasi-diagonalization, recursive bisection, nothing inverted; ch. 14 raised it; Raffinot, Mantegna, Tola.
- (code: hrp) correlation distance, single linkage, `hrp()`; each country's credit beside its government asserted with one exception; the order
- ¶10 [result] (callout) The tree groups fixed income by currency, not class, as ch. 4 measured: unhedged, a foreign bond is its currency.
- (code: hrp-summary) the largest HRP weight is the lowest-variance series, asserted; top five, volatility, bets
- ¶11 [result] (callout) HRP still puts most weight in the lowest-variance series; it changes how the hierarchy is found, not its effect.
Note: Sixty percent of the theory section, doing four things under one heading: the shrinkage reading, the chapter's solver (¶4 and gmv-qp are implementation), the in-sample ladder read with its numbers in a collapsed box (an application result), and a 495-word box on a different method whose finding, that the data group bonds by currency, is the hedging subsection's point made two subsections early. ¶3 gives the out-of-sample verdict before the race runs; ¶5 is a ten-word lead-in.

### The class series is the sleeve's benchmark — 174

Says: Each class series is an index of the instruments inside it, so the top layer is a policy set on investable proxies and handed down as benchmarks; the sleeve manager is judged against it, and setting the policy on realized sleeve returns would reward past alpha and leave nothing to judge.
Why here: Not stated; the paragraph sends its consequences to ch. 21, ch. 24 and ch. 25 and takes nothing from the subsections before it.
Paragraphs:
- ¶1 [claim] Class series are indices, so the policy is set on proxies (Sharpe 1992) and handed down as benchmarks; Roll, Grinold–Kahn.
Note: A one-paragraph subsection without code and with six cross-references; a governance argument between two quantitative subsections, returning as the last takeaway.

### Hedging is a sleeve decision — 378

Says: The optimal hedge differs between bonds and equities, so a hedge is a property of the sleeve: hedging the government sleeve lowers its minimum variance and spreads it over more positions, hedging the equity sleeve changes almost nothing.
Why here: Stated: the sleeve structure settles a question that has no answer at whole-portfolio level; needs ch. 4's hedging finding and the HRP box's currency grouping; ch. 22 takes the bond side.
Paragraphs:
- ¶1 [claim] Ch. 4: hedging strips a Japanese bond's volatility, not Japanese equity's; Campbell et al. say why; a hedge belongs to the sleeve.
- (code: hedge-sleeves) hedged = unhedged − fx by region; `He`; `sleeve_vol()`; `hedge_tab` for three sleeves; government asserted lower and more spread
- (code: tbl-15-hedge) hidden
- ¶2 [result] Hedged government sleeve: lower minimum variance, more effective bets; equity barely moves; Perold–Schulman and Black made unnecessary; ch. 22.
Note: A results table inside the theory section; the commodity sleeve is left out of the table without a word; the two classic citations arrive after the result they are said to answer.

## Implementation — 1198 (64 before the subsections)

Says: The package has a data structure for the nested problem and no documentation of what it does, so the section reads the source and checks it against a by-hand construction.
Why here: Contract position; the opening says the package path and the by-hand path follow the theory.
Paragraphs:
- ¶1 [method] The package has the structure and no documentation of its method; the section reads the source and checks by hand.
Note: The by-hand solver and the nested construction already ran in the theory section, so what this section adds is the package path and its reproduction.

### A sleeve of one asset — 112

Says: A one-asset sleeve cannot be optimized under `ROI`, so the commodity sleeve cannot enter `mult.portfolio.spec()` and the package path runs on three sleeves.
Why here: Stated: the sleeves subsection said the single-asset case must be faced rather than assumed; it fixes the three-sleeve universe the rest of the section uses.
Paragraphs:
- (code: one-asset) `optimize.portfolio()` on the commodity alone, asserted to fail; the message
- ¶1 [caveat] (callout) One asset loses a constraint dimension at `ROI::L_constraint()`; commodity cannot enter `mult.portfolio.spec()`; by hand keeps it.
Note: A subsection with no running prose: one chunk and one callout.

### `mult.portfolio.spec()` and `add.sub.portfolio()` — 481

Says: `optimize.portfolio()` runs every sleeve through the rolling backtest of `optimize.portfolio.rebalancing()`, takes the realized returns as proxies, and optimizes the top level once on them, back-filled training period included; its defaults do not run and `rolling_window` is silently discarded.
Why here: Stated: the method lives in an unexported loop and nowhere else, so the source is read before the output; the next subsection reproduces what it shows.
Paragraphs:
- (code: mult-spec) three sleeves; `gmv_spec()` on top; `add.sub.portfolio()` with `ROI`, monthly, 60 training, 59 trailing; the object's classes and slots
- ¶1 [method] Three arguments every sub-portfolio needs; `optimize.portfolio()` calls the unexported `proxy.mult.portfolio()`, whose loop is the method.
- (code: unlabelled) excerpt of `proxy.mult.portfolio()`: rebalancing per sleeve, `Return.portfolio()`, proxies bound and `na.omit()`
- ¶2 [code] Then `R` becomes the proxies and the top portfolio runs: each sleeve through ch. 25's rolling backtest, top level once.
- ¶3 [caveat] (callout) `rebalance_on = NULL` fails; `training_period` NULL is 36; `rolling_window` silently overwritten into an expanding window; proven by reproduction below.
- (code: mult-default) the default specification asserted to fail; its message
- (code: mult-run) the optimization with `trace = TRUE`; weights; proxy rows and columns, first and last model year
- ¶4 [result] Weights named `proxy.1` to `proxy.3`, names ignored; proxies visible only with `trace = TRUE`; rows from month one, ch. 23's back-fill.
Note: ¶1 and ¶2 are one sentence split around the source excerpt; the callout's last sentence cites the by-hand reproduction a subsection later as its evidence, so the claim precedes its proof; ¶1's "three arguments" and the callout's subject are the same point, stated twice.

### The same thing by hand — 196

Says: Sixty months of drifting equal weights followed by rolling minimum variance reproduce the package's proxies to machine precision and the top-level weights to solver tolerance; dropping the back-fill moves the government budget, and the package cannot drop it.
Why here: Stated: the reproduction is the documentation the chapter set out to write, and the evidence the previous callout claimed.
Paragraphs:
- (code: mult-by-hand) `proxy_by_hand()`: equal weights drifting for W months, then rolling GMV; asserted equal to `o_mp$R` and `o_mp$weights`; weights with and without the back-fill
- ¶1 [result] Proxies reproduced to 1e-10, weights to 1e-6; dropping the back-fill moves the government budget; the package cannot drop it.
Note: The two phases of the by-hand loop are explained only in the code's comments; the one paragraph reads the result and names neither.

### Holding several optimizations together — 345

Says: Stage-1 solutions combine into an `opt.list` whose weight matrix pictures the block-diagonal structure, several top-level policies run in one call on the sleeve series, and the `opt.list` methods need `trace = TRUE`.
Why here: Not stated; the sleeve-cap row it produces is referred to once, in the in-sample paragraph.
Paragraphs:
- ¶1 [method] Stage-1 problems are ordinary portfolio objects; `combine.optimizations()`; `extractWeights()` is a matrix picturing eq-15-block.
- (code: sleeve-stage-list) the three sleeve optimizations combined; row names asserted; the weight matrix in sleeve order
- (code: fig-15-sleeve-weights) `chart.Weights()` on the `opt.list`, line plot
- ¶2 [method] The top level takes the sleeve series; `combine.portfolios()` specifies several policies, solved in one call.
- (code: top-list) minimum variance, a 50 percent sleeve cap, quadratic utility at `risk_aversion` 10; names re-set; weights and objective measures
- ¶3 [caveat] (callout) `extractObjectiveMeasures()` re-evaluates every objective from each `$R`; without `trace = TRUE` it fails; `chart.RiskReward()` likewise.
- (code: fig-15-top-riskreward) `chart.RiskReward()` on the `opt.list` with the sleeves as points, monthly units
Note: A package-API tour: no paragraph reads either figure or the three policies' weights; only the sleeve-cap row is mentioned later, in one clause; that `risk_aversion` is γ/2 is a code comment, not prose.

## Nested Against Flat — 2171 (0 before the subsections)

Says: (heading only)
Why here: Contract position; the opening says the question is whether the hierarchy dominates one-stage optimization out of sample on this universe.
Paragraphs: none of its own.
Note: Heading only; the in-sample ladder was already read in the theory's worked box, so the first subsection repeats it with two rows added.

### In sample — 246

Says: In sample the ordering is fixed, so the table only measures the gaps; nesting gives up Sharpe ratio and does not diversify, because stage 2 is still a minimum-variance problem.
Why here: Not stated beyond the in-sample bound of the theory; it precedes the out-of-sample test as the thing the test is meant to overturn.
Paragraphs:
- (code: in-sample) five constructions: flat, nested, block-diagonal, HRP, equal weight; volatility, return, Sharpe, bets, largest; nested Sharpe asserted below flat
- (code: tbl-15-insample) hidden
- ¶1 [result] Order fixed by construction; nesting gives up Sharpe, holds fewer bets, most in one series; a budget cap is ch. 12's.
Note: Repeats the ladder of the theory's worked box with HRP and equal weight added; no picture opens the application.

### Out of sample — 1343

Says: The hierarchy does not dominate out of sample on this universe: nested trails flat at every window and trails equal weighting, the block-diagonal construction trails nested, the gap opens steadily rather than in any episode, and turnover leaves the ranking alone; on sixteen classes the cross-sleeve covariances are information.
Why here: Stated: ch. 8's claim, that a restriction can buy back out of sample what it costs in sample, is the one that matters, and ch. 25's register is what the loop is scored against.
Paragraphs:
- ¶1 [method] Ch. 8's claim: a restriction helps if it forbids mostly error; four constructions, sixty months, monthly, from the register's first month.
- (code: oos-loop) `FIRST_OOS` derived from model year 11; `race()`: four weight rows per month, returns, register-style turnover, nested sleeve budgets; `oos_stats()`; the sixty-month table
- (code: oos-check) the register read and filtered; flat and equal-weight Sharpe asserted within 0.05
- ¶2 [result] Flat within 0.05 of the register's minimum-variance line, equal weight exact; the loop scores the same months the same way.
- (code: oos-windows) windows 36, 60, 120; `by_window`; the register's flat line asserted at each
- (code: tbl-15-oos) hidden
- (code: oos-verdict) hidden assertions: nested never wins; flat lower volatility at 60; nested below equal weight; block-diagonal below nested everywhere; stage-1 loss exceeds stage-2 recovery
- ¶3 [claim] The hierarchy does not dominate, against DeMiguel's rule; nested behind flat and equal weight at every window; block-diagonal behind nested.
- ¶4 [claim] Shrinkage confirmed from the other side: no conditioning problem at this dimension (ch. 7); the case for discarding is ch. 21's.
- (code: fig-15-oos-cumulative) hidden; growth of one unit of excess return, log scale; episode share of the flat–nested gap asserted below half
- (code: sleeve-budget-path) mean sleeve budgets of the nested construction
- ¶5 [result] The gap opens steadily, no episode dominant; the nested budgets favor government, chosen blind to equities; turnover leaves the ranking.
Note: ¶3 restates the verdict the theory's shrinkage reading announced; ¶3 and ¶4 are the chapter's argument in 314 words, and the figure that supports them follows with its reading a chunk later; the sleeve-budget mechanism in ¶5 is the chapter's only explanation of why nested loses and gets two sentences.

### The policy view — 577

Says: A mandate can carry a different objective at each level; a tangency equity sleeve, minimum-variance bond sleeves and a tangency top level read as a strategic asset allocation document whose class weights are the benchmarks the sleeve managers receive.
Why here: Stated: a policy is not usually minimum variance everywhere, and the sleeves subsection promised the application would mix objectives; ch. 21 and ch. 22 receive the benchmarks, ch. 24 the anchored variant.
Paragraphs:
- ¶1 [method] Each level its own objective: tangency where forecastable, minimum variance elsewhere; long-only tangency as one QP, checked against a frontier scan.
- (code: tangency-qp) `tan_qp()`; a forty-point scan on the sleeve series; asserted that no frontier point beats it; both Sharpe ratios annualized
- (code: policy) `v_policy` per sleeve; sleeve returns; tangency budgets; `w_policy`; the policy tibble of sleeve, within, budget, weight; asserted consistent
- (code: tbl-15-policy) hidden
- (code: policy-summary) policy Sharpe, flat tangency Sharpe, policy volatility, sleeves held
- ¶2 [result] The table as Ang's policy document: budgets and regional splits handed to ch. 21's and ch. 22's managers; in-sample Sharpe, not a forecast.
Note: Four chunks between the two paragraphs, and ¶2 reads two of policy-summary's four numbers; the policy is in-sample only, directly after a subsection showing that in-sample numbers are not forecasts, and it never enters the out-of-sample race.

## Key Takeaways — 281

Says: The nested problem is every allocator's structure and never dominates flat in sample; stage 1 is mandate-set shrinkage and coincides with flat on Σ_B under inverse-variance budgets; the package's method and its four traps; the hierarchy loses out of sample at this dimension; HRP groups bonds by currency, which is the hedging decision; the class series is the benchmark.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Nested is every allocator's structure; Sharpe's question; never dominates flat in sample because the unroll is feasible.
- ¶2 [takeaway] Stage 1 is flat on the block-diagonal matrix, mandate-set shrinkage; inverse-variance budgets make the two coincide exactly.
- ¶3 [takeaway] The package runs sleeves through the rolling backtest, back-fills, optimizes once; defaults fail, `rolling_window` discarded, one-asset fails, trace needed.
- ¶4 [takeaway] On sixteen classes the hierarchy loses out of sample at every window, block-diagonal by more; discarding pays at instrument level.
- ¶5 [takeaway] HRP groups fixed income by currency: Campbell's hedging decision seen from the data; a hedge is a sleeve property.
- ¶6 [takeaway] The class series is the sleeve's benchmark; policy set on proxies, handed down; the manager judged against it.
Note: Six bullets; ¶3 packs four package traps into one; nothing on the policy view (mixed objectives, the tangency QP) or on turnover.

## Exercises — 187

Says: Four exercises: currency sleeves in the race, the inverse-variance top level against the block-diagonal line, HRP with complete linkage cut at four, and the back-fill's weight across training windows.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Currency sleeves as the HRP tree suggests; rerun `race(60L)`; does either hierarchy dominate the flat construction.
- ¶2 [exercise] Inverse-variance top level in `race()`; confirm it matches the block-diagonal line; say what the nested–block-diagonal gap measures.
- ¶3 [exercise] HRP with complete linkage, cut at four clusters; does it recover the sleeves; cross-tabulate clusters against sleeves.
- ¶4 [exercise] Vary the training period in `proxy_by_hand()` over 36, 60, 120; how far top-level weights move without the back-fill.
Note: Four exercises, all reruns of the chapter's own functions (`race()`, `unroll()`, `hrp()`, `proxy_by_hand()`); none touches the policy view or the hedging table.
