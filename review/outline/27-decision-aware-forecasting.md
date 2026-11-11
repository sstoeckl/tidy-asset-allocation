---
file: chapters/27-decision-aware-forecasting.qmd
title: Decision-Aware Forecasting
part: Advanced Topics
words: 7998
sections: 5
paragraphs: 44
---

# Chapter

Claim: A mean-variance investor pays for forecast error in the metric Σ⁻¹ and not in squared error, so a forecaster trained on mean squared error is trained on the wrong loss; of three corrections, shrinking the mean in risk units adds the most Sharpe ratio on the modeled market, acting on fewer forecast dimensions adds nothing beyond what the forecast was already worth, and tuning on the certainty equivalent gives a worse forecast with a better portfolio inside sampling error, while none of the three beats the rules that use no mean.
Question: Should a return forecaster be trained on mean squared error at all; cites Stöckl and Hanke in the second sentence for the closed-form answer (the certainty equivalent lost is the error in risk units, correctable after the fact) and Elmachtoub and Grigas for the general operations-research form (train on the regret of the decision).
Why here: The text says the chapter sits on neither side of chapter 3's horizon axis: it is about estimation, and the corrections apply to a long-run and to a conditional mean alike. It takes the risk-adjusted forecast error and its Sharpe-gap bound from chapter 26 as given, the investor and the certainty equivalent from chapter 3, Bayes-Stein from chapter 6, the condition number from chapter 7, the Best–Grauer mechanism, the N/T inflation, the plug-in rule and the covariance channel from chapter 8, the minimum-variance formula from chapter 9, the term-spread forecast, the tilt and the elastic net from chapter 16, the parametric policy from chapter 18, per-class costs from chapter 23 and the register from chapter 25. It hands to chapter 28 the case in which the model behind the loss is itself in doubt. That it follows chapter 26 is implied by that borrowing; why it sits in this part is not stated.
Does: Price a forecast error in the investor's units; correct a sample mean toward a target with a constant that needs no tuning; act on a forecast at a chosen granularity, with the number of groups read from an information coefficient; tune a forecaster's penalty on the certainty equivalent of the tilt it implies; score all of it on the register's months.
Order: Opening (question, placement and roadmap, data), theory (the two losses, then one subsection per answer in the order after the forecast, between forecast and decision, inside the training loop), implementation (the same three answers in the same order, the first over two subsections), application (one scoreboard figure and three paragraphs), takeaways, exercises. Deviations: neither the theory nor the implementation heading has a paragraph of its own; all four tables are read in the implementation, including the one the text calls the result the chapter was built to show, so the application computes nothing new and re-reads those numbers from one figure; the theory ends on the failure conditions of all three answers, placed under the third answer's heading; the packages block is the hidden setup chunk and the first visible chunk loads data; no callout and no `PortfolioAnalytics` call anywhere; five takeaways, four exercises.

# Sections

## Opening — 283

Says: A forecast should be judged in the units of the decision it feeds; for a mean-variance investor those units are known in closed form, and the chapter derives three answers to the mismatch, implements each on the sixteen classes and asks which buys most.
Why here: Contract position; ¶2 gives the order (derive, implement, compare) and places the chapter off the horizon axis as an estimation chapter.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] The investor pays in decision units, known exactly under mean-variance [Stöckl–Hanke]; the general form is training on regret [Elmachtoub–Grigas].
- ¶2 [method] Estimation, so neither strategic nor tactical; derive the mismatch and three answers, implement on sixteen classes, ask which buys most.
- (code: data) the sixteen classes in excess of the bill, asserted complete; full-sample mean and covariance; γ = 5
Note: ¶1 gives the answer to its own question in its second sentence; "risk units" is used here and defined two subsections later; γ = 5 is set in code and never argued for in the prose.

## Two Losses for One Forecast — 2151

Says: (heading only)
Why here: Stated in the opening: the mismatch between the statistical and the decision loss is derived first, with the three answers to it.
Paragraphs: none of its own.
Note: Heading only; four subsections without an introducing paragraph; the three-answer roadmap that orders them sits in the last sentence of the first subsection.

### The statistical loss and the decision loss — 515

Says: Squared error and the certainty-equivalent loss are quadratic forms in the same error under the identity and under Σ⁻¹; they rank forecasts differently, by up to the condition number, and a forecaster trained on the first can be reconciled with the second in three places.
Why here: Needs chapter 3's investor and chapter 26's risk-adjusted error, which the text says it takes from there; its last sentence names the three places that the next three subsections take up in that order.
Paragraphs:
- ¶1 [derivation] eq-27-mse, the squared error; chapter 3's investor holds the plug-in position; the certainty-equivalent loss is a perfect square, eq-27-decision.
- ¶2 [definition] The quadratic form is the squared risk-adjusted forecast error [Salcher et al.], taken from chapter 26; it is Elmachtoub–Grigas's regret.
- ¶3 [derivation] Two metrics, one error: per eigen-direction the decision loss divides by the eigenvalue; the ratio is chapter 7's condition number.
- (code: metric) cost of a unit error along the first and the last eigenvector, and the log ratio
- ¶4 [result] Unit costs and ratio; squared error buys accuracy where variance is large [Best–Grauer]; lineage [Granger; Elliott–Timmermann]; three places to reconcile.
Note: ¶4 does four jobs: it reads the number, gives the mechanism, gives the lineage and announces the three answers, which is the roadmap for the rest of the chapter; RAFE appears in eq-27-decision one paragraph before it is named.

### Correcting the mean in risk units — 768

Says: In risk units the sample mean's expected squared error is N/T; shrinking its deviation from a pre-set target by a James-Stein factor has an exact risk, minimized by a constant that depends on N, T and the target's rank alone, and for the grand mean the corrected mean dominates the sample mean whenever T exceeds N.
Why here: Stated at the end of the previous subsection: the first of the three places, after the forecast, with the model left alone. The implementation codes eq-27-corrector and eq-27-constant directly, and the next subsection sets its hard reduction against this soft one.
Paragraphs:
- ¶1 [derivation] Kan–Zhou's setting; whitened, the sample mean is normal with covariance I/T; the expected squared RAFE is N/T, eq-27-price.
- ¶2 [claim] Each dimension costs 1/T whatever signal it carries; this N/T inflates chapter 8's promised Sharpe ratio.
- ¶3 [definition] Stein estimation in risk units toward a fixed target, zero or the grand mean; the square root cancels; eq-27-corrector [Stöckl–Hanke].
- ¶4 [derivation] Grand-mean reading; Wishart ratio and Stein's identity give the exact risk, eq-27-risk; best constant eq-27-constant; dominance for T above N.
- ¶5 [evidence] Lineage: Stein, James–Stein, Efron–Morris, Jorion; new is a non-orthogonal target; Bayes-Stein not covered; zero target rescales only; no-mean rules unranked.
Note: ¶4 runs through two numbered displays and holds the derivation, the optimal constant and the dominance result in one paragraph; ¶5 is two paragraphs in one, the lineage and then three limits of the theorem, and those limits are what the implementation later runs into.

### Using less of the forecast — 431

Says: Acting on a k-dimensional projection of the forecast loses the signal discarded plus k/T of noise retained, so a dimension is worth acting on only if its squared Sharpe ratio exceeds 1/T; the familiar rules are fixed cells of a granularity grid, and the number of rank groups worth forming follows from the information coefficient by a cube-root rule.
Why here: The second of the three places, between forecast and decision; the text says it starts from the same identity and sets hard reduction against the shrinkage of the previous subsection. eq-27-hard and eq-27-groups are what the granularity experiment implements.
Paragraphs:
- ¶1 [derivation] Keep the forecast, act on a k-dimensional projection [Salcher et al.]; loss is signal discarded plus k/T noise retained, eq-27-hard.
- ¶2 [claim] A 1/T threshold per dimension; shrinkage is soft reduction; plug-in, minimum variance, 1/N, sorts and tilts are fixed grid cells.
- ¶3 [derivation] Information coefficient ρ [Grinold], profile linear in rank: the best number of groups is a cube root, eq-27-groups.
- ¶4 [claim] Cattaneo et al.'s rate, but each group costs 1/T however many assets it averages; G* is small, down to 1/N.
Note: The truth in risk units is introduced a second time under new symbols (a, b̂, η), one subsection after m and m̂; ¶2 holds three points (the threshold, soft against hard, the grid of rules) and eight citations; the grid is given in one sentence, with no table or figure.

### The decision loss inside the training loop — 437

Says: The decision-aware estimator maximizes the sample certainty equivalent of the portfolio the forecast implies; with the plug-in map and a known Σ it is least squares reweighted by Σ⁻¹, and without the closed form it still applies to any utility, map and model; what it loses is precision, and each of the three answers has a condition under which it does not help.
Why here: The third of the three places, inside the training loop; the text ties it back to chapter 18's policy as the special case and to the first answer through eq-27-gls. Its closing paragraph sets up the implementation by saying where each answer should fail.
Paragraphs:
- ¶1 [definition] eq-27-loop: maximize the sample certainty equivalent of the implied portfolio; Brandt's policy the special case; GLS equivalence eq-27-gls; generalizes.
- ¶2 [caveat] A realized certainty equivalent is as noisy as a Sharpe ratio [Lo]; the condition under which each answer fails.
Note: ¶1 runs through two displays and does four things (defines the estimator, names the lineage, derives the equivalence, claims generality); ¶2 closes the whole theory section with the failure conditions of all three answers under the third answer's heading, and ends on a forward pointer that one answer will partly fail without saying which.

## Three Corrections on Sixteen Classes — 4069

Says: (heading only)
Why here: Stated in the opening: each answer is implemented on the sixteen class series in excess of the bill and scored out of sample from the first month of model year 11.
Paragraphs: none of its own.
Note: Heading only; four subsections for three answers, the first answer taking two; every subsection also reads its own results table, so the section is implementation and results together and is half the chapter.

### The corrected mean in a few lines — 704

Says: The corrector is one short function; on the full sample the factor keeps only part of each deviation from the grand mean, on shorter windows the constant rises above its oracle value, and on a share of the sixty-month windows the positive part binds and the deviations are removed.
Why here: Stated in its first sentence: the two equations of the theory are a function of five inputs. The function and the Bayes-Stein copy are what the backtest of the next subsection calls.
Paragraphs:
- ¶1 [code] The two equations as a function of mean, covariance, N, T and target, with the positive part taken.
- (code: correct-mean) `correct_mean()`: target, rank, Mahalanobis length, constant, positive-part factor; the full-sample values printed
- ¶2 [example] eq-27-constant and the factor with the full-sample numbers substituted; chapter 6's Bayes-Stein copied as the comparison.
- (code: bayes-stein) `bayes_stein()` as in chapter 6; the full-sample estimate
- ¶3 [result] How far each estimator shrinks on the full sample; only the corrector has an exact risk; exercise 2 checks it.
- (code: tbl-27-intensity) the constant, its ratio to the oracle value, the mean factor and the share of windows at zero, for four window lengths
- ¶4 [result] The constant falls toward N − 3 as T grows; the factor is small throughout; the positive part sometimes binds.
Note: The worked formula follows the chunk that computed its numbers; the exact risk, the theory's central result, is not checked in the chapter and goes to exercise 2; ¶2's last sentence is a transition to the Bayes-Stein chunk, attached to the worked example.

### Four means in the tangency rule — 1010

Says: In the long-only tangency rule on rolling windows the Sharpe ratio rises from the sample mean to Bayes-Stein to the corrected mean at both window lengths and stays below minimum variance, onto which the corrected rule collapses in a share of windows; by certainty equivalent equal weighting leads, because a fully invested tangency portfolio carries less risk than this investor would choose.
Why here: Stated: the correction is scored where chapter 8 scored the sample mean, with that chapter's quadratic program and one covariance matrix for every mean, so that chapter 25's register is reproduced.
Paragraphs:
- ¶1 [method] Score the correction as chapter 8 scored the sample mean: long-only tangency, rolling windows, one covariance matrix, the register reproduced.
- (code: qp-rules) `gmv_qp()`, `tan_qp()` with a minimum-variance fallback, the register's Sharpe ratio, the annual certainty equivalent; out-of-sample months asserted to start in model year 11
- ¶2 [code] Five fully invested rules per window; an assertion states that the zero target only rescales the unconstrained position.
- (code: rolling-means) `run_rules()` at sixty and 120 months; summary by rule; three rules asserted equal to the register's lines
- (code: means-facts) hidden: the Sharpe orderings asserted at both windows; the share of windows with a zero factor; the Sharpe standard error
- (code: tbl-27-means) Sharpe ratio, certainty equivalent and volatility of five rules at two windows
- ¶3 [result] Sharpe ratio: sample below Bayes-Stein below corrected at both windows; corrected stays below minimum variance and sometimes equals it.
- ¶4 [result] Certainty equivalent: equal weighting highest, since full investment fixes the length; the unconstrained position is left to exercise 1.
Note: The heading counts four means, the table scores three, and the fourth, the zero target, appears only as an assertion; the position the theorem prices, unconstrained and of its own length, is never scored in the chapter, only in exercise 1; the Sharpe standard error the next two subsections quote is computed in this subsection's hidden chunk.

### Granularity on the term-spread tilt — 1369

Says: Acted on at every magnitude, in three rank groups, by sign only or in the number of groups the rule picks, the term-spread forecast earns the same small gain over equal weighting; the cells differ by far less than the Sharpe ratio's standard error, and the text reads this as the theory's second failure condition: a near-common shift leaves granularity nothing to decide.
Why here: Stated: the second answer needs a forecast with a cross-section, and the term spread is the one forecast of chapter 16 that survived out of sample. The six other predictors are built here for the next subsection.
Paragraphs:
- ¶1 [method] Chapter 16's term-spread forecast rebuilt: lagged US slope, expanding regression from model year 11; six more predictors built for later.
- (code: term-forecast) curve signals at month ends, momentum, turbulence, all lagged once; `pairs_of()`, `ols_fc()`; the sixteen-column forecast matrix
- ¶2 [method] Chapter 16's tilt and band; the reduction goes in before the clipping; four cells from one function.
- (code: tilt) `tilt_from()` with a `reduce` argument, `steps()`, `sign_only()`, per-class cost rates, `score_W()` with turnover and net certainty equivalent
- ¶3 [method] The moving cell: rank correlation of fitted values with realized returns on past months gives the groups, rounded and capped.
- (code: information-coefficient) `ic_of()` per month, G* and the rounded rule; the same coefficient on the forecasts actually made
- (code: tbl-27-granularity) five cells: dimensions, Sharpe ratio, certainty equivalent gross and net, turnover
- (code: granularity-facts) hidden: gains over equal weighting, the spread across cells and the turnover ordering, asserted
- ¶4 [result] All cells above equal weighting, indistinguishable among themselves; fitted coefficient overstates the realized one; sign trades more; the band decides.
Note: ¶4 is one paragraph with six points (gain over equal weighting, no difference between cells, the rule's choice, fitted against realized coefficient, turnover, the theoretical reading); three chunks stand between the last method paragraph and it; the longest subsection, about two thirds of it code.

### Tuning the elastic net on the certainty equivalent — 986

Says: On the same folds and penalty grid, cross-validated squared error picks the null model in most years while the certainty-equivalent criterion picks a smaller and unstable penalty; out of sample the decision-tuned net has the worse squared error and the better portfolio, at several times the turnover and with a Sharpe gain inside its standard error.
Why here: Stated: the third answer is tried on the forecaster that lost in chapter 16. It reuses the predictors, the tilt and the scoring function built in the previous subsection, and the text calls its table the result the chapter was built to show.
Paragraphs:
- ¶1 [method] Chapter 16's elastic net [Zou–Hastie]; same folds and grid, squared error against the tilt's certainty equivalent; only the penalty chosen.
- (code: enet-tuning) `tune_both()`: out-of-fold forecasts on a grid of penalties, pooled squared error and the tilt's certainty equivalent; re-tuned once a year
- (code: lambda-facts) hidden: the null-model share, the smaller-penalty share and the spread of the chosen penalty, asserted
- ¶2 [result] Squared error mostly picks the null model, as chapter 16 concluded; the certainty-equivalent penalty is smaller and unstable across years.
- (code: enet-forecast) `fc_en()` under each penalty path, the expanding mean; squared error, out-of-sample R² and the tilt's scores
- (code: training-facts) hidden: worse squared error, better Sharpe ratio and net certainty equivalent, the turnover ratio, a gain below one standard error, asserted
- (code: tbl-27-training) the net under two losses and the historical mean: squared error, R², Sharpe ratio, certainty equivalents, turnover
- ¶3 [result] Worse squared error, better portfolio, eq-27-gls without a closed form; qualified by turnover and the standard error: sign, not significance.
Note: ¶3 opens by naming its table the result the chapter was built to show, and it stands at the end of the implementation, as the fourth of four parallel subsections, not in the application; the tilt on the historical mean, the table's third row, is not read in the prose.

## What Each Answer Buys — 838

Says: On one scoreboard with the register, the corrected mean adds the most Sharpe ratio to the rule it corrects and the training loop the most certainty equivalent, while granularity adds nothing; each fails somewhere and none beats the rules that use no mean, so the correction recovers part of the tangency rule's distance to minimum variance and the rest is the covariance matrix's share.
Why here: Stated in the opening as the last step: which of the three buys most on this market, and where each fails. The last paragraph hands the doubt about the model behind the loss to chapter 28.
Paragraphs:
- (code: fig-27-scoreboard) one data frame: the register's lines and this chapter's rules by Sharpe ratio at sixty-month windows, equal weighting as the dashed line
- (code: board-facts) hidden: the register's best line and minimum variance above every forecast-based rule, the corrected tangency best among those, asserted; the three gains
- ¶1 [result] Sharpe gain over the rule corrected: first answer most, third next, second none; by certainty equivalent the loop leads.
- ¶2 [caveat] Where each fails: the correction against no-mean rules, granularity in mattering, the loop in noise, turnover and significance.
- ¶3 [claim] Tangency's shortfall was the sample mean's price; the correction recovers a share; the rest is covariance and level; chapter 28.
Note: The section opens with the figure and computes nothing new: the figure collects numbers already read in the implementation and the three paragraphs regroup them by answer; the three gains are measured over three different base rules; ¶2 is where the theory's forward pointer is redeemed by name; ¶3 states for the first time, without a number of its own, that the level direction carries most of what there is to earn, and ends on the transition to chapter 28.

## Key Takeaways — 294

Says: The Σ⁻¹ metric and its cost ratio; the corrected mean, its constant and its backtest; the 1/T price per dimension and the granularity result; the certainty-equivalent tuning result; and that no answer beats the rules without a mean.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Forecast error is paid in the metric Σ⁻¹, not the identity; the cost ratio between extreme directions on sixteen classes.
- ¶2 [takeaway] Grand-mean shrinkage has an exact risk and a tuning-free constant; it lifts the tangency rule and collapses onto minimum variance.
- ¶3 [takeaway] A dimension acted on costs 1/T; rules are grid cells; cube-root group count; on the term spread the band decides.
- ¶4 [takeaway] Tuning the penalty on the certainty equivalent: worse R², better portfolio, inside sampling error, at a multiple of the turnover.
- ¶5 [takeaway] No answer beats the register's rules that use no mean; the covariance channel holds the rest of the loss.
Note: One bullet per step of the argument, in the chapter's order, the first four each pairing a theory statement with its number and its citations; the reach of the third answer beyond mean-variance does not return.

## Exercises — 230

Says: Four exercises: the zero target and the unconstrained position, the exact risk by simulation and the constant in the backtest, a doubled band, and the realized information coefficient.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Zero target in the backtest: Sharpe ratio equals the sample mean's except at a zero factor; then unconstrained certainty equivalents.
- ¶2 [exercise] Simulate the squared RAFE at four constants against N/T; rerun the backtest; monotone in the constant, and the positive part?
- ¶3 [exercise] Double the band and recompute the granularity table; does granularity matter, does the sign cell still match?
- ¶4 [exercise] Use the trailing realized information coefficient in place of the fitted one; how often does the rule hold 1/N?
Note: Four exercises, two on each of the first two answers and none on the training loop; exercises 1 and 2 carry the two checks the prose defers (the unconstrained position, the exact risk).
