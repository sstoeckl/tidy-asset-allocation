---
file: chapters/19-regimes.qmd
title: Regime-Dependent Allocation
part: Allocation Strategies
words: 7597
sections: 5
paragraphs: 47
---

# Chapter

Claim: Switching to a stress portfolio beats the static policy only when the regimes are dated with hindsight; detected in real time by a turbulence threshold or a filtered two-state model the switch keeps little or none of that advantage, neither detector is distinguishable from the static policy by a paired test, and holding the stress portfolio throughout has a higher Sharpe ratio than either, so on this market whether to hold minimum variance matters more than when.
Question: What if the right portfolio depends on the state of the world; @hamilton1989 for the statistical form and @ang2002a for carrying it into portfolio choice, both inside the first two sentences.
Why here: Stated in the opening: the descriptive chapters supplied the reason to ask, chapter 4's episodes of rising correlations and chapter 14's falling effective bets, and the chapter is tactical in chapter 3's sense. Needs chapter 5's turbulence index, chapter 9's tangency portfolio, chapter 8's quadratic program, chapter 16's lag-and-assert discipline, chapter 23's turnover and cost accounting and chapter 25's register; hands the wrong-model question to chapter 28 and the design-leak problem to chapter 25. Why it follows the parametric policies of chapter 18, or sits where it does in this part, is not stated.
Does: Write a Hamilton filter, a Kim smoother and EM for a two-state model, build a turbulence flag and real-time regime probabilities with no look-ahead, run `regime.portfolios()` knowing its seven behaviors, and test a switching strategy against the static policy and against its own constant mix with a paired Sharpe test.
Order: Theory (model, filter and smoother, mixture moments, two rules, dating against detecting, turbulence), implementation (regimes dated with hindsight, the turbulence threshold, the hidden Markov model with its real-time refit and detection table, the package's regime machinery and its quirks), application (six strategies under the register's accounting, the reading, the episode table, three limits), five takeaways, four exercises; deviations: the chapter's central result, the detection figure and table the text calls "the chapter's argument in small", lands inside the implementation section with the package subsection between it and the application, and the application opens with a method subsection whose figure is never read.

# Sections

## (opening) — 294

Says: Whether the portfolio should depend on an unobserved state is a question this market gives reason to ask, and the chapter answers it by stating the model, detecting the regimes two ways and testing a switch out of sample.
Why here: the opening by contract; ¶2 lays out the order (model, filter, mixture; date, detect, package; the out-of-sample test).
Paragraphs:
- (code: setup)
- ¶1 [claim] Hamilton's switching series and Ang–Bekaert's bear regime; chapters 4 and 14 showed correlations rise and bets fall together.
- ¶2 [method] A tactical chapter in chapter 3's sense; the plan: theory, dating and two detectors, the package, the out-of-sample test.
- ¶3 [method] The sixteen risky classes in excess of the bill, per chapters 2 and 3.
- (code: data)

## Regimes, Filters, and Mixtures — 1213

Says: A regime-switching model is a Markov chain plus a filter; the investor faces mixture moments with a between-regime term, uses the state by mixing or by switching, and must detect the regime rather than date it, with turbulence as the parameter-free detector.
Why here: by contract; the opening's plan names the model, the filter and the mixture moments first.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: six subsections of 120 to 260 words; the chapter's thesis is stated in passing at the end of the filter subsection and again as the one-sentence last paragraph of the two-rules subsection.

### The regime-switching model — 120

Says: Returns are Gaussian within a state that follows a Markov chain whose transition matrix fixes regime durations and long-run shares.
Why here: not stated; the definitions the filter needs.
Paragraphs:
- ¶1 [definition] @hamilton1989's model (eq-19-model); expected duration and long-run share from P; @turner1989's two-state version, @ang2012's survey.

### The Hamilton filter — 224

Says: The state is inferred by a prediction and an update step whose normalizer is the likelihood; EM maximizes it with smoothed probabilities, and the filtered–smoothed difference is the chapter's subject.
Why here: stated: the state is never observed, so everything rests on its probability given the returns seen so far.
Paragraphs:
- ¶1 [derivation] Notation ξ and η; prediction (eq-19-predict) and update (eq-19-update); log-likelihood from the denominator; EM by @dempster1977, @baum1970, @hamilton1990.
- ¶2 [definition] EM needs smoothed probabilities, @kim1994's backward recursion (eq-19-smooth); filtered against smoothed is the chapter's subject.
Note: ¶2's last sentence states the chapter's thesis inside a definition.

### One-step-ahead moments as a mixture — 236

Says: Next month's return is a mixture whose covariance carries a between-regime term and whose tails are fat and asymmetric from Gaussian ingredients, jointly across assets.
Why here: stated: the investor at t does not know s_{t+1}, so faces the predicted probabilities' mixture; the between-regime term and the kurtosis are reused by the worked example.
Paragraphs:
- ¶1 [derivation] With π the predicted probabilities, mixture mean and covariance (eq-19-mixture).
- ¶2 [claim] Between-regime term; non-normal mixture, kurtosis (eq-19-kurtosis), skewness [@timmermann2000]; chapter 4's tails from Gaussian parts; joint switching, chapter 11, @ang2002.
Note: ¶2 does four things: interprets the between-regime term, derives the kurtosis, links to chapter 4's stylized facts, and links to chapter 11's co-moments and the correlation-asymmetry literature.

### Two ways to use the state — 261

Says: Given the state probabilities an investor either holds the tangency portfolio of the mixture moments or switches between regime portfolios on the most probable state, and the literature finds both worth something against a static policy.
Why here: stated: "given π there are two rules"; the switching rule (eq-19-switch) is what the package implements and the application tests.
Paragraphs:
- ¶1 [definition] Mixture rule: tangency of eq-09-tangency on eq-19-mixture, weights move continuously; switching rule: one of K portfolios on the argmax (eq-19-switch).
- ¶2 [evidence] Compromise against bet; @clarke1998, @ang2002a, @ang2004, @guidolin2007, @guidolin2008, @tu2010, @bulla2011, @nystrup2015 on costs of ignoring regimes and simple switches.
- ¶3 [transition] All condition on an estimated state, and the estimate is where the difficulty lies.
Note: ¶2 carries eight citations in one paragraph; ¶3 is one sentence turning the section toward dating and detecting.

### Dating and detecting — 214

Says: Dating uses the whole sample and detecting only the past, so detection lags; a regime backtest leaks through smoothed probabilities, full-sample parameters and a regime definition settled after looking.
Why here: stated by ¶3 of the previous subsection, the estimate is the difficulty; the two coding leaks are "asserted away below" and the design leak is sent to chapter 25.
Paragraphs:
- ¶1 [definition] Dating (peaks and troughs [@pagan2003], named episodes, smoothed probabilities) against detecting (filtered, parameters through t); the lag [@chauvet2008].
- ¶2 [caveat] Three leaks: smoothed probabilities, full-sample parameters, the regime definition; two are chapter 16's coding errors, one chapter 25's design problem.

### Turbulence as a model-free detector — 152

Says: The turbulence index of chapter 5 has no parameters to estimate, is persistent and poorly rewarded while it lasts, and a quantile threshold on it is the simplest detector there is.
Why here: stated: a regime model has parameters to estimate before it says anything, so a parameter-free detector is set beside it.
Paragraphs:
- ¶1 [definition] Eq-05-turbulence needs only trailing moments; @chow1999's blend is eq-19-mixture's first sum; @kritzman2010, @kritzman2012; threshold at a quantile of its past.

## Implementation — 3270

Says: The four dated episodes are described, two detectors are built without look-ahead and compared against the dated regimes, and the package's regime machinery is shown to be row selection with seven measured behaviors.
Why here: by contract; the opening's plan: date with hindsight, detect two ways, then what the package offers for switching.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: at 3,270 words the chapter's largest section; it carries the chapter's central result, the detection figure and table, before the application begins.

### Regimes dated with hindsight — 396

Says: Inside the four dated episodes equities always lose, government bonds lose only in the rates shock and correlations rise, but a sixteen-by-sixteen matrix from a few months describes and cannot be optimized on.
Why here: stated in the opening's plan: date the regimes first; the table is referred back to twice from the application for the rates shock.
Paragraphs:
- ¶1 [method] `sim_episodes` and `in_episode()` assign months; the moments per state are one grouped computation.
- (code: dated)
- (code: tbl-19-dated)
- (code: dated-facts)
- ¶2 [result] Equities lose in all four, bonds only in the rates shock, correlations rise; 136 entries from few months; describes, cannot be optimized on.
Note: ¶2 reads the table and ends in a caveat on rank and on correlation rising mechanically with volatility [@forbes2002]; the "not one stress regime observed four times" point is credited to chapter 4.

### A detected regime: the turbulence threshold — 233

Says: The flag for month t is the index above the 75th percentile of its own expanding history through t−1, verified against a hand-computed Mahalanobis distance and a reversal test for look-ahead.
Why here: not stated beyond the opening's order; the theory called it the simplest detector; the flag feeds the package demonstration and the application.
Paragraphs:
- ¶1 [method] Same call as chapter 5; the package returns sqrt(d_t)/N from month t and the sixty before.
- (code: turbulence)
- ¶2 [method] Flag above the 75th percentile [@kritzman2010], expanding window ending the month before; known at end of t, acts in t+1.
- (code: turbulence-flag)
Note: the no-look-ahead check (reverse the tail, the flags through the cut must not move) lives in a code comment and an assertion; no paragraph reads what the flag finds, which arrives only in the detection table of the next subsection.

### A detected regime: a two-state hidden Markov model — 1547

Says: A two-state model fitted inline to the equal-weighted return finds a volatility regime, not a bear market; with hindsight it is clean, in real time it has nothing to detect the first crisis with and lags the later ones, while the turbulence threshold flags the credit crisis in its first month.
Why here: its place after the threshold is not stated; within it, the summary series is justified by the parameter count and the real-time refit by "those estimates used every month"; the figure and table are "the chapter's argument in small".
Paragraphs:
- ¶1 [method] Full model has hundreds of parameters against 372 months; fit the equal-weighted series with six; filter, smoother and EM as loops.
- (code: hmm)
- ¶2 [result] The volatility floor and why; two states differ in volatility, hardly in mean; their average durations.
- (code: mixture-scalar)
- ¶3 [example] (callout) Long-run shares and regime volatilities substituted into the scalar eq-19-mixture and eq-19-kurtosis; within and between terms shown.
- ¶4 [result] (callout) Two regimes give about half the sample's excess kurtosis and none of its skewness; a volatility regime, not a bear market.
- ¶5 [method] In real time parameters are refit once a year on an expanding window; nothing after t enters the probability for t.
- (code: hmm-realtime)
- (code: detection)
- (code: fig-19-probabilities)
- (code: tbl-19-detection)
- (code: detection-facts)
- ¶6 [result] Smoothed clean; real time has no stress regime to learn before the credit crisis, lags after; turbulence flags it first month; equity bear unseen.
Note: 1,547 words, half the implementation section; its figure and table are the chapter's pivot and sit two subsections before the application; ¶6 reads two detectors, four episodes and the false-alarm rates in one paragraph; the worked callout is collapsed; ¶2 opens on a caveat (the floor) before reading the fit.

### Regime portfolios in `PortfolioAnalytics` — 1091

Says: `regime.portfolios()` with `optimize.portfolio.rebalancing()` reproduces exactly the weights obtained by picking rows from two separate runs, and seven measured behaviors say what it checks and what it does not.
Why here: stated: the package "ships the machinery for the switching rule", and "the backtest needs both portfolios at every month", so the two portfolios the application switches between are built here.
Paragraphs:
- ¶1 [method] `combine.portfolios()`, `regime.portfolios()`, `optimize.portfolio.rebalancing()`; calm is long-only tangency, stress is long-only minimum variance.
- (code: specs)
- ¶2 [method] A `portfolio.list` solves specification by specification; stress by rebalancing as chapter 25, calm as chapter 8's single QP since `maxSR` is slow.
- (code: two-portfolios)
- ¶3 [method] Regime object from the turbulence flags coded 1 and 2; run over a short stretch starting with the credit crisis.
- (code: regime-run)
- ¶4 [result] At each date the package read that date's regime, solved its specification, returned rows of the two separate runs; switching is row selection.
- (code: quirks)
- ¶5 [transition] (callout) Each line is one of the measurements above.
- ¶6 [caveat] (callout) Seven behaviors: regime as list index, contemporaneous lookup, exact dates, values match specifications, only assets agree, `...` reaches all, extractors label differently.
Note: the package's `maxSR` route runs only on an eighteen-month demonstration stretch to confirm the hand QP; the seven behaviors are measured in one chunk and reported as one bullet list; ¶4's last sentence announces the measurements before the chunk; the 0/1-coding and date-shift behaviors are the chapter's own contribution and reach the takeaways as one bullet.

## Detected Against Dated Regimes, Out of Sample — 2290

Says: Dated switching beats the static policy, the two detectors keep little or none of it and neither differs from the static policy by a paired test, and the stress portfolio held throughout beats both detectors.
Why here: by contract; the opening's plan ends with the out-of-sample question "once the regime has to be detected rather than dated".
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: two subsections; the first builds the figure and both tables and reads none of them, the second reads everything; the application opens with a method paragraph rather than a picture, and the cumulative-return figure is never referenced in the prose.

### The strategies and their accounting — 1259

Says: Six strategies from observation 121, two static, three switches by dated, turbulence and filtered regimes, and the mixture mean-variance rule, are run under the register's accounting with drift, turnover and per-class costs.
Why here: stated: the register of chapter 25 fixes the start and the accounting, so the numbers are comparable to its rows; chapter 23 supplies turnover and cost.
Paragraphs:
- ¶1 [method] Static calm, static stress; switches on dated (month-ahead label, infeasible), turbulence and predicted HMM; mixture tangency on expanding weighted moments.
- (code: strategies)
- ¶2 [method] Register accounting: weights set at t earn t+1, drift, trade back at eq-23-turnover and eq-23-net; a switch is a trade.
- (code: accounting)
- (code: fig-19-cumulative)
- (code: tbl-19-performance)
- (code: performance-facts)
Note: 1,259 words of which two paragraphs are prose; the strategies chunk also verifies the law of total covariance and reproduces the mixture portfolio through `momentFUN`, neither mentioned in prose; the accounting chunk defines the Jobson–Korkie–Memmel statistic in a code comment, attributed in prose only in the next subsection; the figure built here is never read.

### Reading the result — 1022

Says: The static rows reproduce the register; dated switching works and part of it is timing; turbulence keeps a small part and times no better than a fixed blend, the filtered model none, the mixture rule passes its estimation error to the optimizer; nothing is distinguishable from sampling error, and the stress portfolio throughout beats both detectors.
Why here: stated: "the two static rows are checks before they are results", then each row is read against the constant mix with the same stress share; the episode table "shows where each number comes from".
Paragraphs:
- ¶1 [result] Static Sharpe equals the register's `max_sharpe`, stress equals its `min_variance`; the accounting is the register's.
- ¶2 [result] Dated switching raises Sharpe, cuts drawdown; against the same-share constant mix part is timing, the rest holding a better portfolio.
- ¶3 [result] Turbulence keeps part, times no better than a blend; HMM below static, in stress where smoothing marks nothing; mixture passes estimation error on.
- ¶4 [claim] None distinguishable from sampling error: eq-25-se, paired z [@memmel2003]; the stress portfolio throughout beats both detectors; whether, not when.
- (code: tbl-19-episodes)
- (code: episode-facts)
- ¶5 [result] Credit crisis: turbulence captures most, the filter almost none after two months; rates shock: nothing to capture, detectors lose more entering and leaving.
- ¶6 [caveat] Three limits: one path, four episodes; design choices made once, varied in the exercises; the stress portfolio is itself a model, chapter 28.
Note: ¶3 reads three strategies against three yardsticks in the chapter's longest paragraph; ¶4's "whether, not when" is the chapter's verdict and arrives before the episode table that explains it; four hidden chunks (dated-, detection-, performance-, episode-facts) assert every ordering the prose states.

## Key Takeaways — 261

Says: Five bullets: the model plus the filter, the mixture moments and fat tails, dating against detecting, what `regime.portfolios()` does, and the out-of-sample verdict.
Why here: by contract.
Paragraphs:
- [takeaway] Eq-19-model plus a filter; filtered probabilities from data through t, smoothed from the whole sample; only the first is available [@hamilton1989; @kim1994].
- [takeaway] Eq-19-mixture with its between-regime term; fat tails by eq-19-kurtosis; the two-state model gives about half the kurtosis, none of the skewness.
- [takeaway] Dating and detecting differ; smoothed probabilities and full-sample parameters leak; before the first stress regime a model cannot detect one.
- [takeaway] `regime.portfolios()` is row selection; reads the rebalancing date's regime, uses the value as a list index, checks neither coding nor timing.
- [takeaway] Dated switch well ahead; turbulence keeps a small part, the filter none, neither distinguishable; stress throughout beats both; rates shock defeats every switch.
Note: five, on contract; bullet 5 restates ¶3, ¶4 and ¶5 of the reading in one sentence; nothing on the mixture rule's out-of-sample result.

## Exercises — 228

Says: Four exercises: vary the turbulence threshold, feed the dated regimes through the package's contemporaneous lookup, simulate the chain to separate persistence from fat tails, and a half-invested stress portfolio for the rates shock.
Why here: by contract; ¶6 of the reading says the exercises vary what the chapter chose once.
Paragraphs:
- [exercise] 1. Recompute the turbulence switch at the 50th and 90th percentiles; stress share, Sharpe, same-share constant mix; which threshold times its months?
- [exercise] 2. Feed the dated episodes through the rebalancing-date lookup, a one-month delay; how much of the dated advantage is lost, where?
- [exercise] 3. Simulate a two-state chain; compare sample kurtosis with eq-19-kurtosis; autocorrelation of squared returns; which chapter 4 property does persistence add?
- [exercise] 4. Half the stress budget in the bill (`weight_sum` 0.5); redo the dated switch by episode; does leaving help in the rates shock?
Note: four against "around three"; exercises 1, 2 and 4 each follow one design choice named in the reading's ¶6; exercise 3 is the theory's eq-19-kurtosis; no exercise touches the mixture rule.
