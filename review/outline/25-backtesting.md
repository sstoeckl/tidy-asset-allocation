---
file: chapters/25-backtesting.qmd
title: Backtesting and Diagnostics
part: Implementation and Evaluation
words: 3366
sections: 5
paragraphs: 53
---

# Chapter

Claim: A backtest is a statistical estimate, not a replay of history: the package's rolling loop completes at full length while storing periods that never solved, those periods fall in the one stretch where the mandate was infeasible, and on the book's register every Sharpe-ratio interval overlaps every other, so what can be kept is what is not an estimate: turnover, cost and the failure count.
Question: Not posed as a question; implied: where the book's out-of-sample lines come from and how much of a backtest to believe; @harvey2015 and @lopezdeprado2018, in the sixth sentence rather than the first two.
Why here: Stated in the first sentence: every construction chapter ends with a line of out-of-sample evidence, and this is where those lines come from. Takes chapter 19's argument against an unchanged world, chapter 4's equity bear market and its non-i.i.d. finding, chapter 23's net figures and per-asset contributions, chapter 24's attribution, chapter 5's lagged market proxy and chapter 2's real-data sleeves; hands the cost of forecast error to chapter 26 and model doubt to chapter 28. Why it closes the part, after rebalancing and benchmarks, is not stated.
Does: Run a rolling backtest with windows of the intended length, find the periods that did not solve with `diagnose_rebalancing()`, carry and count them with `pm_backtest()`, register a parallel backend, put @lo2002's standard error on a Sharpe ratio, and name four kinds of look-ahead.
Order: Opening; theory (the backtest as an estimator, the two window arguments); implementation (the silent failure, its diagnosis, the carry-forward, the parallel backend); application (the register, its error bar, attribution, look-ahead); seven takeaways; four exercises. Deviations: the theory section runs the package and spends three of its four paragraphs on two arguments; the two main headings after it have no paragraph of their own; the implementation ends on run time, with typed timings; the application opens on a table, and the chapter's one figure sits in the implementation; the application's last two subsections are code-free theory placed after the chapter's forward pointer, and neither is in the opening's plan, the takeaways or the exercises; several subsection headings are sentences or imperatives.

# Sections

## Opening — 188

Says: The out-of-sample lines of the earlier chapters come from here, and the chapter gives its length to what goes wrong, because a backtest is an estimate.
Why here: Contract position; ¶2 says the order is deliberate (failure modes before running, since running is four lines) and ¶3 gives the sequence.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [transition] Every construction chapter ends with an out-of-sample line; here they are produced and the machinery taken apart.
- ¶2 [claim] Failure modes get the length, running gets four lines; @harvey2015, @lopezdeprado2018: a backtest is an estimate, not simulated history.
- ¶3 [method] Plan: rolling backtest and two window arguments, a complete-looking run with unsolved periods, the register and its error bar.
- (code: data) the sixteen classes in excess of the bill; `win` set to sixty
Note: No question is posed and the first citation arrives in the sixth sentence; no visible packages block; ¶3's plan omits the parallel backend, attribution and look-ahead.

## What a Backtest Estimates — 264

Says: A backtest is a loop that may see only the past and its return series is a sample; two arguments of the package's loop decide how much past each step sees.
Why here: Stated in the opening's plan: what a rolling backtest is and what its two window arguments mean come first; eq-25-backtest is what the error bar and the look-ahead taxonomy later refer to.
Paragraphs:
- ¶1 [definition] A loop estimating strictly before t, holding one period (eq-25-backtest); the returns are a sample, each statistic an estimate.
- (code: basic) a minimum-variance specification through `optimize.portfolio.rebalancing()` with both window arguments; prints the number of periods
- ¶2 [transition] Two arguments deserve suspicion.
- ¶3 [caveat] `training_period` sets the first window; `rolling_window` is inclusive at both ends, sixty gives sixty-one; few published results say which.
- ¶4 [definition] An expanding window is `rolling_window = NULL`: more data, assuming an unchanged world, which chapter 19 disputes.
Note: The heading names the estimand and three of four paragraphs are about package arguments; no sentence introduces the chunk, and its printed length is read only in the next section; the third-decimal effect is asserted and left to exercise 2.

## Implementation — 1089

Says: (heading only)
Why here: Contract position; the opening's plan names the complete-looking run with unsolved periods, not the remedy or the parallel loop.
Paragraphs: none of its own.
Note: Heading only; three subsections follow one case (failure, diagnosis, remedy) and the fourth turns to run time.

### The backtest that looks complete and is not — 376

Says: With a required return added, the rebalancing loop returns an object of the right class, length and names in which some periods hold only `NA`, and the functions downstream do not fail on it.
Why here: Stated in the opening's plan as the second step; needs `bt` from the theory section to compare lengths; supplies `bt_mandate` and `n_bad` to the diagnosis.
Paragraphs:
- ¶1 [method] Give the specification what a real mandate contains: a required return.
- (code: mandate) the return-target specification; the backtest wrapped in `suppressWarnings()`; prints the number of periods
- ¶2 [result] As many periods as before; right class, length and names; the contents are another matter.
- (code: inside) classes of the entries, the count without weights, two assertions, one failed entry printed
- ¶3 [result] Every entry has a solved portfolio's class, some hold none: `NA` weights and objective, the verdict in an unread `$solver_status`.
- ¶4 [caveat] (callout) Not a bug: an infeasible `ROI` solution is copied through unread, a thrown error is stored by design; nothing warns.
- ¶5 [transition] What happens next depends on which function is reached for.
- (code: downstream) `summary()`, `extractWeights()` and `Return.portfolio()` tried on the result
- ¶6 [result] Neither fails: `NA` weight rows, `NA` returns from the first failure to the sample's end, behind a rounding-like warning.
Note: The chunk tries three functions and ¶6's "neither" reads two; the target's annual size sits in a code comment until the next subsection uses it; the call is wrapped in `suppressWarnings()`, unexplained, above a callout saying nothing warns.

### Diagnose every period, always — 349

Says: The failed periods are not scattered: they fall within one year, beginning in the last month of the equity bear market, so dropping them removes exactly the stretch in which the mandate was impossible.
Why here: Not stated beyond the heading's instruction; needs `bt_mandate` and `n_bad`; ¶1 says the timing is what a count of failures would not have shown.
Paragraphs:
- (code: diagnose) `diagnose_rebalancing()`; the status table; failed dates located in the sample and asserted against `n_bad`
- (code: tbl-25-failures) hidden; the failed periods with status and message
- ¶1 [transition] Now the part a count of failures would not have shown.
- (code: clustering) prints the failed dates; asserts a span within one year, the first inside the equity bear market, the rest after it
- ¶2 [result] Failures lie close together: the bear market's last month and the year after, when no long-only mix reached the target.
- ¶3 [claim] Dropping them loses the impossible stretch and averages the easy months: survivorship, the optimism @harvey2015 warn of.
- (code: fig-25-failures) hidden; an equal-weighted market index with the failed periods marked
Note: Opens on two chunks; `diagnose_rebalancing()` is never introduced in prose; neither the table nor the figure is referred to in the text, and the figure follows the paragraphs that make its point; the heading is an imperative.

### What to do about a period that failed — 129

Says: No remedy preserves the strategy; carrying the previous weights forward is the least dishonest, and `pm_backtest()` does it, warns and reports the count in every result row.
Why here: Not stated; follows the diagnosis as its remedy; `n_failed` is the column the register table later carries.
Paragraphs:
- ¶1 [claim] No answer preserves the strategy; carrying weights forward is least dishonest, still another strategy; `pm_backtest()` does it, warns, counts.
- (code: report) `pm_backtest()` on the mandate through `pm_strategy()`; Sharpe ratio, periods and failures by basis
- ¶2 [claim] `n_failed` is not decoration: a result with failures is a different object; a table omitting the count misreports the run.
Note: `pm_backtest()` and `pm_strategy()` enter with one clause of introduction; the call is wrapped in `suppressWarnings()` one sentence after the prose says it warns; the Sharpe ratio the chunk prints is not read.

### The parallel loop with no backend — 232

Says: The rebalancing function contains a parallel loop and registers no backend, so it runs sequentially; registering eight workers gave identical results 4.5 times faster.
Why here: Not stated; the topic turns from whether the periods solved to how long the loop takes, and the opening's plan does not announce it.
Paragraphs:
- ¶1 [claim] `optimize.portfolio.rebalancing()` already contains a parallel loop.
- (code: unlabelled excerpt of the package's `foreach` loop, not run)
- ¶2 [caveat] It registers no backend, unlike `optimize.portfolio()`; `%dopar%` falls back to sequential behind a warning that reads like noise.
- (table: wall clock, no backend against eight workers; typed in Markdown)
- ¶3 [result] A 4.5-fold speedup on the same four strategies, results identical; `pm_backtest(workers = 8)` registers and restores the backend.
- ¶4 [caveat] Messages and warnings on a worker are lost, errors return as conditions; diagnose sequentially, then re-run in parallel.
- ¶5 [caveat] `optimize.portfolio.parallel()` is another function: it spreads repeated runs of one stochastic optimization, not the rebalancing loop.
Note: The timings are typed, not computed, from a run the chapter does not show; "the same four strategies" has no referent (the register carries five); ¶5 is an aside on a namesake function.

## The Register, and How Much of It to Believe — 1423

Says: (heading only)
Why here: Contract position; the opening's plan: assemble the register, then put an error bar on it.
Paragraphs: none of its own.
Note: Heading only; the first two subsections carry out the opening's plan, the last two (attribution, look-ahead) are code-free and unannounced.

### The register, assembled — 544

Says: At the sixty-month window the rule that estimates a mean is last and the covariance-only optimizers lead; at every window a rule estimating no mean is ahead of it, by a gap that closes as the window lengthens.
Why here: Stated: every construction chapter contributes one strategy and the table is the book's summary of itself; supplies `reg` and `Tn` to the error bar.
Paragraphs:
- ¶1 [method] Every construction chapter contributes one strategy; run over the same sample they are the book's summary of itself.
- (code: sweep) reads `output/tables/oos-sweep.csv`
- (code: tbl-25-register) hidden; sixty-month window, monthly, gross, sorted by Sharpe ratio, with turnover and failed periods
- (code: register-ranking) hidden; ratios for the prose, the out-of-sample length, assertions on the ranking at each window
- ¶2 [result] From the bottom: the mean-estimating rule is last, with multiples of turnover and drawdown; covariance-only rules lead; the window matters.
- ¶3 [claim] At every window no-mean rules lead and the gap closes with W; @demiguel2009, @jagannathan2003; added: an inspectable market, failures counted.
Note: ¶3's every-window claim is asserted in code for the best no-mean rule only, and ¶2 has the mean rule off the bottom at 120 months; the register is read from a file written outside the chapter; the `failed` column is never read (zero in every row) and the failing mandate is not among the five.

### A backtest is a measurement, and it has an error bar — 379

Says: With @lo2002's standard error every strategy's Sharpe-ratio interval overlaps every other, so no difference in the register is distinguishable from zero; turnover, cost and the failure count are not estimates and survive.
Why here: Stated in the opening's plan as the last step; needs `reg` and `Tn` from the register, and returns to the theory section's framing of eq-25-backtest as a sample.
Paragraphs:
- ¶1 [definition] The Sharpe ratios are point estimates; under i.i.d. returns @lo2002 gives the asymptotic standard error (eq-25-se), annualized below.
- (code: error-bar) standard error and interval per strategy; asserts that all intervals overlap
- ¶2 [result] Every interval overlaps every other; no difference among the five, best against worst included, is distinguishable from zero.
- ¶3 [caveat] Chapter 4 rejects i.i.d., so intervals are wider (@ledoit2008; @jobson1981, @memmel2003); five strategies need little multiple-testing correction (@white2000, @sullivan1999, @bailey2014).
- ¶4 [claim] Two things survive: turnover and cost are arithmetic on observed trades, and the failure count is no estimate.
- ¶5 [claim] The conclusions worth keeping do not hang on a Sharpe ratio's third decimal; most useful ones do not.
- ¶6 [transition] Chapter 26 measures the cost of forecast error directly; chapter 28 asks what to do when the model is doubted.
Note: ¶2 reads differences off overlapping single intervals, and ¶3 then names the test for a difference without running it; ¶4's failure count is the mandate's, a strategy outside the register; ¶6 is the chapter's send-off, with two subsections still to come.

### Attribution: where the return came from — 255

Says: @brinson1986's decomposition splits an active return into allocation, selection and interaction, the split the book's parts are built on; chapter 24 does the work, and the ninety-percent result answers a narrower question than it is quoted for.
Why here: Not stated why it follows the error bar; ¶1 links it only by contrast (a backtest says what was earned, attribution which decisions earned it), and ¶3 hands the computation back to chapter 24.
Paragraphs:
- ¶1 [definition] A backtest says what was earned, attribution which decisions earned it; @brinson1986, @brinson1991; allocation, selection, interaction (eq-25-brinson).
- ¶2 [claim] The terms separate overweighting a segment from choosing inside it: the book's split, Parts IV and V against Part VI.
- ¶3 [transition] The inputs exist: chapter 23's per-asset contributions are the equation's terms; chapter 24 does the work.
- ¶4 [caveat] The ninety-percent claim: @ibbotson2000 show it is variance over time for one fund, not differences between funds.
Note: No code and no number from the modeled market; the decomposition is defined here and the text sends its use to the preceding chapter; absent from the opening's plan, the takeaways and the exercises.

### A taxonomy of look-ahead — 234

Says: Four violations of eq-25-backtest's rule recur (a misaligned window, a universe chosen with hindsight, parameters tuned on the scoring sample, revised vendor data), and only the first is a coding error.
Why here: Not stated; it elaborates the rule the theory section set in eq-25-backtest, and comes after the results and the chapter's forward pointer.
Paragraphs:
- ¶1 [claim] eq-25-backtest lets the weights see only the past; violations are the commonest defect and rarely obvious; four kinds recur.
- ¶2 [caveat] A misaligned window uses data through t; chapter 5's one-period lag in the market proxy exists for this.
- ¶3 [caveat] A universe chosen with hindsight: every modeled asset survives to the sample's end, unlike chapter 2's real-data sleeves.
- ¶4 [caveat] Parameters tuned on the scoring sample make it in-sample [@harvey2015]; hence the sweep reports all nine configurations.
- ¶5 [caveat] Vendor data are revised; the current vintage of a macroeconomic series holds numbers nobody had then.
- ¶6 [claim] The first is a coding error, the rest design decisions; @lo2004: a same-history test measures the regime, not the rule.
Note: Code-free theory as the chapter's last body subsection; "nine configurations" is the first mention of the sweep's size, of which the register subsection showed three windows; absent from the opening's plan, the takeaways and the exercises.

## Key Takeaways — 240

Says: Seven bullets: the backtest as an estimate, the inclusive window, the stored failure, the clustered failures, diagnosing and reporting the count, the unregistered backend, and the overlapping intervals against what is not an estimate.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] A backtest is eq-25-backtest, an estimate from a rule seeing only the past; every statistic has a standard error [@harvey2015].
- ¶2 [takeaway] `rolling_window` is inclusive at both ends, so 60 gives 61 observations; almost no published result names its convention.
- ¶3 [takeaway] The loop stores a failed period as `NA` weights or a condition object and completes: right class, length and names.
- ¶4 [takeaway] The failures are not random: all within one year around the bear market's end; dropping them averages the easy months.
- ¶5 [takeaway] Always diagnose every period and carry the failure count into the result table; failures make a different object.
- ¶6 [takeaway] `%dopar%` without a registered backend runs on one core; eight workers cut 273 seconds to 61, results identical.
- ¶7 [takeaway] Under eq-25-se every interval overlaps every other; the differences in turnover, cost and feasibility are not estimates.
Note: Seven against "around five"; nothing on the register's ranking (the claim the register's ¶3 says the book carries out of the table), on attribution or on look-ahead; bullets 3 to 5 split one finding in three.

## Exercises — 128

Says: Four exercises: the mandate at a lower and a higher target, the sixty-one-observation window, the expanding window against the error bar, and a manager's answer to the failed periods.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Rerun the mandate at monthly targets 0.002 and 0.005; count and date failures; where does it stop being a strategy?
- ¶2 [exercise] Set `rolling_window = win` and confirm sixty-one observations; how far does minimum variance's Sharpe ratio move?
- ¶3 [exercise] Run the expanding window; better or worse, and is the difference larger than the error bar?
- ¶4 [exercise] Ask what a manager would have done in failed periods; implement it, rerun, say how it differs from the specification.
Note: Four against "around three"; all rerun the windows or the mandate; exercise 2 measures the theory section's third-decimal assertion; none touches the register's ranking, attribution or look-ahead.
