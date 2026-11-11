---
file: chapters/16-signals-and-forecasts.qmd
title: Signals and Return Forecasts
part: Allocation Strategies
words: 7301
sections: 5
paragraphs: 50
---

# Chapter

Claim: Of four signals on sixteen series only the theory-motivated term spread forecasts out of sample, and a restrained tilt on it pays a few tens of basis points of certainty equivalent after costs, inside the Sharpe ratio's sampling error; the signals that data alone motivate, and a regularized seven-signal model, lose to the historical mean and pay more to trade.
Question: Can the excess return on an asset class be forecast, and does a forecast that fits the past help an investor who must act before the future arrives; cites @welch2008 (hardly any predictor helped in real time) and @campbell2008 (a small but meaningful gain under a sign restriction), who between them fixed the two criteria: the out-of-sample R² against the mean and the investor's certainty-equivalent gain.
Why here: The text says it is the book's first tactical chapter in ch. 3's sense, inputs conditioned on information available at the time; it takes the sixteen series from ch. 2, the excess basis, quadratic utility and the certainty equivalent from ch. 3, the Merton bound from ch. 4, Newey–West and the turbulence index from ch. 5, the mean as the strategic input from ch. 6, the equal-weight policy and the estimation-cost lesson from ch. 8, the constrained minimum-variance portfolio from ch. 9, turnover, costs and the back-fill trap from ch. 23 and the register's scoring months and paired test from ch. 25; it hands the view from opinion to ch. 17, the hand-chosen tilt rule to ch. 18 and ch. 19, the value side to ch. 21, the curve state to ch. 22 and the forecast-error question to ch. 26 and ch. 27. Why it follows ch. 15 inside the part is not stated.
Does: Build four signals from the shipped data and lag them with assertions; run single-signal predictive regressions with Newey–West inference; score forecasts on an expanding window by R²OS, Clark–West and Diebold–Mariano; fit a time-ordered, cross-validated elastic net without leakage; turn forecasts into a banded tilt around equal weight and price it with turnover, costs and the certainty equivalent.
Order: Opening (question, tactical label and roadmap, data), theory (the regression and its R², R²OS, DM and CW, why a small R² matters with the CE criterion, the signal families), implementation (signals built and lagged, sixty-four in-sample regressions, out of sample with the elastic net), application (the tilt rule with the utilities callout, accounting and costs, the reading), takeaways, exercises. Deviations: the chapter's main result, the out-of-sample table and its three findings, sits in the implementation section, so the application prices a tilt on a verdict already read; the application opens with a method paragraph and a chunk, not a picture; the one worked formula with numbers substituted is in the theory on hypothetical values; the chapter scores on the register's months but reads no register line; six takeaways and four exercises.

# Sections

## Opening, before the first section — 380

Says: Predictability is judged by Welch–Goyal's and Campbell–Thompson's two criteria, and this chapter applies them to four signals on the sixteen class series as the book's first tactical exercise.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections and no reason for the chapter's place in the part.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] The two questions; Welch–Goyal found nothing survived, Campbell–Thompson a small gain; together they fixed R²OS and the CE gain as the terms.
- ¶2 [method] The first tactical chapter in ch. 3's sense; roadmap: the statistics, the signals built, tests singly and combined, a priced tilt.
- ¶3 [method] The sixteen classes of ch. 2 in excess of the bill (ch. 3); the first assertion, because a misdated signal gives a plausible table.
- (code: data) asserts sixteen series, no NA, bill dates equal to return dates
Note: ¶1 carries both seminal citations inside its first three sentences; ¶2's roadmap is one sentence of four clauses; ¶3's reason for asserting (a plausible table from a misdated signal) returns in the theory and again in the implementation.

## Predictability, In Sample and Out — 1703

Says: A predictive regression is scored out of sample against the historical mean by R²OS and the Clark–West statistic, a small R² is worth a lot to a mean-variance investor and the certainty equivalent decides it, and this universe carries momentum, the curve spreads and turbulence but not value.
Why here: The roadmap's first step; the text says the dating and the statistics are settled before any signal is chosen, and that the implementation asserts the alignment the theory demands.
Paragraphs: none before the first subsection.
Note: Five subsections, the first three a single paragraph each wrapped around display equations; the chapter's only worked formula with numbers substituted is here, on hypothetical values rather than on the data.

### The predictive regression — 260

Says: The regression and its in-sample R² are defined, and three things are settled before any signal: the dating, the smallness of any R², and the Stambaugh bias; inference is Newey–West and sixty-four regressions are a multiple-testing problem.
Why here: Stated: the three things are settled before any signal is chosen; the implementation asserts the dating this paragraph demands.
Paragraphs:
- ¶1 [definition] eq-16-predictive and eq-16-r2; dating is the discipline; R² small by ch. 4's Merton bound; persistent signals bias the slope; Newey–West; sixty-four tests.
Note: One paragraph does six jobs (two definitions, three caveats, inference with multiple testing); its yardstick, one percent a month as a strong result, is what the in-sample table is later read against.

### The out-of-sample R² — 230

Says: The investor re-estimates each month and competes with the expanding historical mean; R²OS has no floor and is usually negative; the window expands; the sign restriction goes to exercise 2.
Why here: Stated: an in-sample fit scores on the history it was fit on, which an investor cannot do; the expanding window is the scheme the implementation runs.
Paragraphs:
- ¶1 [definition] Real-time forecast against the mean through t, ch. 6's input re-estimated; eq-16-r2os; negative is the common case (three citations); expanding window chosen; CT restriction to exercise 2.
Note: The burn-in is called a choice and left to the implementation; the restriction Campbell–Thompson found decisive is deferred to an exercise.

### Testing one forecast against another — 198

Says: The Diebold–Mariano test on the loss differential is biased against a nested model, and the Clark–West correction is the statistic reported, with DM beside it.
Why here: Stated: a regression and the mean are nested, so the correction is needed before any signal is set against the mean below.
Paragraphs:
- ¶1 [definition] Loss differential and DM t-test with Newey–West variance, eq-16-dm; the nesting bias; Clark–West adds back the estimation noise, eq-16-cw, one-sided; DM shown beside it.
Note: Two statistics, two equations, one paragraph; the promise to show DM beside CW is kept only in the summary table's last column.

### Why a small R² can matter — 477

Says: The gain to a mean-variance investor is R²OS/γ, about a quarter of the expected excess return at half a percent a month against an annual Sharpe ratio of one half, and the certainty equivalent, not the fit, decides the application.
Why here: Stated: in-sample significance and out-of-sample profit are different questions, and the second needs a criterion before the application; it draws ch. 3's utility and certainty equivalent.
Paragraphs:
- ¶1 [derivation] Kandel–Stambaugh: decisions respond to weak predictability; under ch. 3's utility the conditional position earns Var(μ_t)/(γσ²) more, the R²; eq-16-ct.
- ¶2 [example] Half a percent a month at a Sharpe of one half and γ = 5, substituted inline: a quarter of the premium, basis points a month; fit and profit differ; Pesaran–Timmermann.
- ¶3 [definition] CE and Δ, eq-16-cer, from realized returns, decide the application; it does not score the forecast itself, which is ch. 8's and ch. 26's risk-adjusted error and ch. 27's question.
Note: ¶2 is the chapter's one worked formula with numbers substituted, on hypothetical values rather than the data; ¶3 ends on a two-sentence pointer to Part VIII inside a definition paragraph.

### Which signals this universe can carry — 538

Says: Momentum from returns, the term and IG spreads read off the simulated curve, and ch. 5's turbulence index are the signals; value needs fundamentals the market does not carry.
Why here: Stated: the families are set out before the implementation builds them; the text says the bond block was simulated from the curve factors, which the in-sample reading later relies on.
Paragraphs:
- ¶1 [claim] Three families; the shipped data support two.
- ¶2 [definition] Momentum needs only returns; Jegadeesh–Titman; skip the last month; eq-16-mom.
- ¶3 [evidence] Moskowitz–Ooi–Pedersen at the class level, Asness et al. everywhere; value is the family the universe cannot support, left to ch. 21.
- ¶4 [definition] Macro state: the Welch–Goyal set; Fama–French's term and default spreads; the curve's Nelson–Siegel factors and credit spreads; term spread is minus the slope; the bond block was generated from them (ch. 22), equity is open.
- ¶5 [definition] Cross-sectional dispersion: ch. 5's turbulence index (eq-05-turbulence), Chow et al., Kritzman–Li, two Stöckl papers; one market-wide value with a series-specific slope.
- ¶6 [method] The real macro signals one `tidyfinance` call away, `tms` and `dfy`, on the real calendar.
- (code: goyal-welch) not evaluated
- ¶7 [caveat] Nothing depends on it; every signal is built from shipped data so the chapter reproduces offline.
Note: ¶1's count does not close: four families are named (momentum, value, macro state, dispersion), three are built and one is unsupported, yet dispersion is called "the third"; ¶3 joins momentum's class-level evidence to value's exclusion; ¶4's disclosure that the bond returns were generated from the curve state is what the in-sample reading rests on.

## Building and Testing the Signals — 2665

Says: The four signals are built from the shipped data, lagged with assertions, found significant in sample for the term spread and the IG spread, and out of sample only the term spread beats the expanding mean; the combination sits between its parts and the elastic net loses.
Why here: The roadmap's second and third steps; needs the families and the three statistics of the theory section; the application takes its forecasts `fc` from here.
Paragraphs: none before the first subsection.
Note: The section carries the chapter's main result, the out-of-sample table and its three findings, in a subsection of 1,416 words that also holds the scheme and the elastic net; the application prices a tilt on a verdict already read here.

### Signals at month end, lagged once — 667

Says: Momentum, the curve signals and turbulence are built at each month end, each with an assertion, and shifted forward one month so that the signal at t sits on the row of the return at t+1.
Why here: Stated: the dating is the whole discipline and the alignment is asserted in code rather than trusted; the regressions run on the frame `pairs_of()` builds here.
Paragraphs:
- ¶1 [method] Momentum as a ratio of lagged index values; the assertion checks it against the product.
- (code: momentum)
- ¶2 [method] Weekly curve to month end, last observation on or before; the sign checked: level minus term spread must track the bill.
- (code: curve)
- ¶3 [result] The implied short rate's correlation with the bill; a sign error fails the render; turbulence is ch. 5's call unchanged, sixty-month trailing window.
- (code: turbulence)
- ¶4 [method] Shift the block forward one month; the assertion states what the shift did.
- (code: lag) `pairs_of()`, the frame the regression runs on; `first_row()`
- ¶5 [result] The first row carries no signal; the months momentum and turbulence begin, inline.
- (code: fig-16-signals)
Note: ¶3 reads a number and sets up the next chunk in one block; `pairs_of()`, the frame every later chunk uses, is introduced by a code comment rather than by the prose; the subsection ends on a figure no paragraph reads.

### In sample: sixty-four regressions — 582

Says: Over the full sample the term spread is the strongest signal, positive on every bond and credit series, the IG spread second, turbulence weak and momentum nowhere; the largest R² is not small by eq-16-ct.
Why here: Stated in the theory: in sample first, then whether any of it is available in real time; the paragraph ends on that question.
Paragraphs:
- ¶1 [method] Each series on each signal, full sample, Newey–West at six lags as in ch. 5.
- (code: insample) prints the summary tibble `ins_sum`
- (code: tbl-16-insample)
- (code: insample-facts) hidden: term positive on every bond, strongest column, IG second, momentum clears two nowhere
- ¶2 [result] By column: the term spread's counts and largest t (Fama–French on modeled data); IG second where the state was built in; turbulence; momentum negative on equities, why Moskowitz's premium is absent; the largest R² by eq-16-ct; real time?
Note: ¶2 is one block of about 230 words reading four columns, reconciling momentum with the literature and posing the transition; the summary numbers print raw from `insample` before the formatted table shows them; the hidden chunk asserts the order the prose states.

### Out of sample: an expanding window from model year 11 — 1416

Says: On an expanding window from the first month of model year 11 the term spread keeps a positive R²OS on most series and beats the mean by Clark–West, the IG spread and turbulence lose what an expanding window cannot see, the combination averages, and the elastic net loses more the less it shrinks.
Why here: Stated: the theory says only an out-of-sample score counts, and ch. 25's register scores the same months; the application tilts on the forecasts `fc` produced here.
Paragraphs:
- ¶1 [method] Expanding window with burn-in; `rsample::rolling_origin()` describes the same splits, asserted to match.
- (code: oos-setup) burn-in of 120 months, the first forecast month asserted to be model year 11; `ols_fc()`
- ¶2 [method] Burn-in and forecast months, the register's; at each month fit on pairs before it, forecast it, record the mean through the month before.
- ¶3 [method] One signal at a time is Welch–Goyal, not practice; seven predictors fit noise; the elastic net (Zou–Hastie, Gu–Kelly–Xiu, Coqueret–Guida); tuning is where the future leaks; two λ kept.
- (code: enet)
- ¶4 [method] The loop's outputs: the mean, four single forecasts, their average (Rapach et al.), two net forecasts.
- (code: forecasts)
- ¶5 [transition] The three statistics as three short functions.
- (code: oos-stats)
- (code: tbl-16-oos-summary)
- (code: oos-facts) hidden: term survives best, the net short of it, `lambda.1se` above `lambda.min`, the combination between its parts
- (code: fig-16-oos)
- ¶6 [transition] Three findings in decreasing order of comfort.
- ¶7 [result] The term spread survives: counts, median, CW count, best series; DM's lower count is the nesting bias in one column; IG and turbulence keep fewer, their fit concentrated in credit and a few crisis months.
- ¶8 [result] The combination helps and does not rescue: between its best and worst constituent.
- ¶9 [result] The elastic net loses at both λ, short of the single term spread; Gu–Kelly–Xiu's same ranking; the more it fits, the more burn-in noise; ch. 8's lesson for a conditional mean.
Note: A fifth of the chapter in one subsection: the scheme, the one method the chapter describes at length (¶3, about 200 words on a model it says it does not reproduce), the loop and the chapter's main result; ¶5 and ¶6 are one-sentence transitions; the table and figure sit between the functions and the reading with no prose between them; ¶7's explanation for turbulence (a few crisis months) is asserted, not shown.

## The Economic Value of a Tilt — 1874

Says: A banded tilt around equal weight pays after costs on the term spread, by a few tens of basis points of certainty equivalent and inside the Sharpe ratio's sampling error; the combination is a wash, and momentum and the elastic net trade more and lose.
Why here: The roadmap's last step; the text says the certainty equivalent of the theory decides it, and it needs `fc` and the register's months from the implementation and the cost machinery of ch. 23.
Paragraphs: none before the first subsection.
Note: Opens with a method paragraph and a chunk, not a picture; the relative-return figure is drawn but never read; the chapter scores on the register's months but reads no register line.

### A tilt around the policy — 701

Says: Equal weight is the anchor because it estimates nothing; a forecast becomes a weight by volatility scaling, demeaning, scaling by κ and clipping to a band of half the policy weight; the term-spread tilt is modest, and the two utilities whose names suggest rolling do not roll.
Why here: Stated: the anchor must estimate nothing so that every difference is the forecast's, and the dating of eq-16-predictive carries over; the callout sits by the `vol60` line where a reader would reach for the utilities.
Paragraphs:
- ¶1 [method] Equal weight (eq-08-ew, `equal.weight()`) as the policy: it estimates nothing, and ch. 9's constrained minimum variance leaves no room to tilt.
- (code: policy)
- ¶2 [definition] Three steps: divide by trailing sixty-month volatility, remove the cross-sectional mean, scale by κ and clip to ±δ; eq-16-tilt; δ = 1/(2N); κ fills the band at a forecast Sharpe of one half.
- (code: tilt) `tilt_weights()`; the term tilt's mean absolute move and the share at the band
- ¶3 [result] The average move against the band and the share where the band binds; modest forecasts, modest tilt.
- ¶4 [caveat] (callout) `applyFUN()` scores weight vectors on the whole history, `trailingFUN()` evaluates once on the last n + 1 rows; neither rolls; `zoo::rollapply()` or a loop does; both run so the behavior is measured.
- (code: applyfun)
Note: The subsection ends on the callout's chunk, whose output no paragraph reads; ¶1 gives two reasons for the anchor; the band and κ are set by hand in ¶2, which the closing paragraph later concedes when it points to ch. 18.

### Rebalancing, turnover and costs — 695

Says: The monthly accounting is written out, with drifted weights, ch. 23's turnover and cost at the per-class rates, the register's Sharpe ratio and the certainty equivalent at γ = 5, for the policy and five tilts.
Why here: Stated: `Return.portfolio()` back-fills equal weights (ch. 23's trap) and the drifted weights are needed for the cost; the table it produces is read in the next subsection.
Paragraphs:
- ¶1 [method] Monthly rebalancing written out, not `Return.portfolio()`; the drift formula; eq-23-turnover and eq-23-net at `pm_costs_default()` rates mapped by class suffix, as ch. 23 uses on the register.
- (code: accounting) `run_path()`, `sharpe_realized()` as the register, γ = 5 and the CE, `summarise_path()`; the policy and five tilts; the CE gain
- (code: tilt-facts) hidden: term pays most and alone above ten basis points, shallower drawdown, momentum and the least-penalized net negative, the Sharpe advantage inside its standard error
- (code: fig-16-relative)
- (code: tbl-16-tilt)
Note: One paragraph and four chunks; the CE of eq-16-cer is annualized in code without the prose saying so; the figure precedes the table and is never read; the Sharpe ratio's standard error is computed in a hidden chunk and read only in the next subsection.

### Reading the result — 478

Says: The term spread alone pays after costs, by a few tens of basis points inside the sampling error of the Sharpe ratio; momentum and the elastic net trade more and lose; the honest reading is Campbell–Thompson's, and three chapters take the rest.
Why here: Stated: the gain is measured against its own uncertainty before it is called evidence; closes the application with the forward pointers.
Paragraphs:
- ¶1 [result] How many tilts pay; the term tilt's net Sharpe against the policy's, CE gain, drawdown, turnover and cost; the combination a wash; momentum's loss; the net's turnover multiple and loss; ch. 23's relation.
- ¶2 [claim] Lo's standard error of the Sharpe ratio over the forecast months; the advantage inside it; ch. 25's paired test not enough; theory-motivated signals worth a little, data-motivated ones nothing; Sharpe 1987.
- ¶3 [transition] Not done here: views from opinion (ch. 17); the hand-chosen tilt against ch. 18's parametric policies (Brandt et al.) and ch. 19's regimes; the loss function (ch. 26).
Note: ¶2 is the chapter's claim in its final form and the first place the Sharpe advantage meets a standard error; ¶1 reads the table only and never the relative-return figure; the turnover multiple and the cost drag are the chapter's only cost numbers in prose.

## Key Takeaways — 286

Says: Six bullets: the scoring statistics, the small-R² arithmetic, the signals the universe carries, the term spread as the only survivor and the net's loss, the tilt's net gain inside sampling error, and the two utilities that do not roll.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [takeaway] Judged out of sample by eq-16-r2os against the mean and by Clark–West's correction of Diebold–Mariano for the nested benchmark.
- ¶2 [takeaway] A small R² is not a small effect; eq-16-ct; half a percent against a Sharpe of one half is a quarter of the premium.
- ¶3 [takeaway] Momentum, the curve spreads and turbulence are supported; value is not.
- ¶4 [takeaway] The term spread is the only signal with out-of-sample evidence (counts inline); the others lose; the seven-signal net loses on most, the more the less it shrinks.
- ¶5 [takeaway] A tilt of at most half the policy weight pays on the term spread (basis points inline), inside the Sharpe's sampling error; the combination a few; momentum and the net lose.
- ¶6 [takeaway] `applyFUN()` and `trailingFUN()` do not roll; `zoo::rollapply()` or a loop does.
Note: Six against around five; ¶4 says the IG spread and turbulence lose to the mean, where the result paragraph keeps them positive on some series; ¶6 is the only bullet about the package.

## Exercises — 237

Says: Four exercises: local curves for local series, the Campbell–Thompson sign restriction, the tilt scale κ, and an absolute timing rule for one equity series against eq-16-ct.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [exercise] Replace the US curve signals with each non-US series' own region (US for the commodity); recompute the term-spread points of fig-16-oos; does a local curve forecast a local bond better.
- ¶2 [exercise] Campbell–Thompson's sign restriction on the five equity series' term-spread forecasts; recompute R²OS and CW; which series gain, and what it says of the slope's sign.
- ¶3 [exercise] Double and halve κ; recompute tbl-16-tilt for the term and momentum tilts; does the CE gain scale with κ, which tilt a larger κ hurts more.
- ¶4 [exercise] Campbell–Thompson's timing rule on `US_equity` alone, weight in [0, 1.5], γ = 5; CE against a constant weight of one; does the absolute view earn what eq-16-ct predicts.
Note: Four against around three; exercise 2 is announced in the theory; exercise 4 is the only place eq-16-ct is tested on the data rather than on hypothetical numbers.
