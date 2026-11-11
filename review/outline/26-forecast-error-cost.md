---
file: chapters/26-forecast-error-cost.qmd
title: The Cost of Forecast Error
part: Advanced Topics
words: 7366
sections: 5
paragraphs: 36
---

# Chapter

Claim: For a mean-variance investor the cost of a wrong mean forecast is an identity, the squared Mahalanobis distance between forecast and truth (RAFE²/2γ), so the RMSE prices the error in the wrong metric; on the modeled market the RAFE tracks the unconstrained plug-in's Sharpe shortfall where the RMSE does not, which channel costs more depends on the unit, and in the register only the tangency portfolio loses more than a standard error to estimation.
Question: What does an error in a return forecast cost, and in which units should the cost be written; cites Salcher–Stöckl–Hanke in the second sentence for the answer (the optimizer's own risk metric) and Chopra–Ziemba in the third for the older number (means about ten times as costly as variances).
Why here: The text places the chapter on neither side of ch. 3's horizon axis, as measurement for strategic estimates and tactical forecasts alike. It takes the objective from ch. 3, the data from ch. 2, the excess basis and θ from ch. 9, Merton's precision result and the volatility clustering from ch. 4, the three forecasts and the market proxy from ch. 6, eq-08-kz, the inflation, the helper programs, the channel table and the stand-in truth from ch. 8, the term-spread forecast and its tilt from ch. 16, and the register and its standard error from ch. 25. It hands the training of a forecaster on the RAFE to ch. 27 and model error to ch. 28. Why it opens the part is not stated.
Does: Compute the RAFE, the certainty-equivalent loss and the Sharpe shortfall of a forecast or position; score forecasts on rolling train and test windows against the RMSE; split a plug-in rule's expected loss into mean noise, inversion error and amplification and check it by simulation; bound the Sharpe ratio a forecast's R² allows; compute a strategy's perfect-foresight shortfall.
Order: Opening (question, placement and roadmap, data), theory (identity and RAFE, Sharpe bound, RMSE as special case, covariance channel, information bound), implementation (functions and worked box, three forecasts on rolling windows, the covariance channel by simulation, the bound on the term-spread forecast), application (channel shares at three windows, shortfall by episode, the register), takeaways, exercises. Deviations: no main heading has a paragraph of its own; the implementation is 45 percent of the chapter and reads the main results, so the application adds three further cuts and its first subsection re-reads the simulation; the application opens on a table chunk and has no figure; the one figure sits in the implementation and no sentence refers to it; three quantities defined in the theory (C-RAFE, the intermediate nested measures, the multivariate bound) are never computed in the body; the packages block is the hidden `setup` chunk; six takeaways, four exercises.

# Sections

## Opening — 408

Says: The cost of a forecast error belongs in the investor's own units, the covariance metric of the optimizer, and the chapter derives that measure and applies it to the sixteen classes.
Why here: Contract position; the text places the chapter on neither side of ch. 3's horizon axis and gives the roadmap as a sequence without reasons.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Cost in investor's units [Salcher–Stöckl–Hanke]; Chopra–Ziemba's ten-to-one lacks its formula; the loss is an identity; RMSE-type scores discard its metric.
- ¶2 [method] On neither side of ch. 3's horizon axis: measurement; roadmap: the identity and four readings, three measurements, three questions.
- ¶3 [method] Sixteen risky classes of ch. 2, excess of the bill; full-sample moments serve as truth, as in ch. 8.
- (code: data) excess returns, full-sample `mu`, `S` and `theta2`; asserts sixteen series, no NA, observation 121 in model year 11
Note: ¶1 cites nine sources in 175 words and already states the chapter's result (the loss is an identity); ¶2's roadmap is one sentence of about ninety words; the packages block is the hidden `setup` chunk and the visible chunk computes the stand-in truth.

## The Loss in Risk Units — 1585

Says: In risk units the certainty-equivalent loss of any position is a squared distance to the optimum, and the RAFE, the Sharpe bound, the RMSE as a degenerate metric, the covariance channel and an information ceiling are read off it.
Why here: Stated in the roadmap only as "first"; each function of the implementation carries an equation number from here.
Paragraphs: none before the first subsection.
Note: Eight paragraphs carry 1,585 words and twelve numbered displays, four of them running through two or three displays; no code; nine of the section's citations are to the two Salcher–Stöckl–Hanke papers.

### The certainty equivalent and the plug-in loss — 393

Says: Whitening positions and means by the square root of Σ turns the loss of any position into a squared distance, and for a plug-in position with Σ known that distance is the RAFE, the Mahalanobis distance between forecast and truth.
Why here: Roadmap: the identity comes first and the rest is read off it; needs ch. 3's objective and the θ of eq-09-tangency.
Paragraphs:
- ¶1 [definition] CE, optimum and CE* = θ²/2γ from ch. 3's objective (eq-26-ce); positions and means in risk units (eq-26-whiten).
- ¶2 [derivation] a lists the Sharpe ratios of N orthogonal directions; any position's loss is a squared distance, eq-26-loss-identity.
- ¶3 [derivation] Klein–Bawa and Kan–Zhou's loss; Σ known gives eq-26-rafe; RAFE defined; three readings; error maximization; the sample mean costs N/T.
Note: ¶3 is 250 words around one display and does five jobs (attribution, the plug-in step, the definition of the RAFE, its three readings with the Michaud and Best–Grauer mechanism, the N/T price tied to eq-08-kz and Merton); the chapter's central term is defined in a "where" clause after its equation.

### From the certainty equivalent to the Sharpe ratio — 197

Says: A Sharpe-ratio investor sees only the angle between forecast and truth in risk units, so the shortfall is θ(1 − cos φ) and is bounded by c₀ times the RAFE.
Why here: First sentence: direction without length turns the identity into a bound; needs eq-26-rafe.
Paragraphs:
- ¶1 [derivation] eq-26-cos: the shortfall depends on the angle only; geometry gives RAFE ≥ θ sin φ, hence eq-26-bound; the squared-Sharpe version.
Note: The subsection is one sentence chain around two displays; the reason for the case c₀ = 1 follows the display that states it; the squared-Sharpe decomposition arrives in the last sentence and is not used again.

### The RMSE as a special case — 283

Says: The RMSE is the last of a nested sequence of simplifications of Σ, each discarding something the optimizer uses, and the cited correlations with the shortfall fall along the sequence.
Why here: First sentence: the usual score replaces Σ in eq-26-rafe by something simpler; closes on ch. 27, which draws the consequence for training.
Paragraphs:
- ¶1 [definition] Salcher–Stöckl–Hanke's nested sequence, eq-26-nested: full Σ, constant correlation, zero correlation, one volatility, identity.
- ¶2 [evidence] What each step discards; their error–shortfall correlations fall from RAFE to RMSE; Kandel–Stambaugh, Cenesizoglu–Timmermann; ch. 27 draws the consequence.
Note: ¶2 joins the reading of the sequence, the cited numbers, two further sources and the forward pointer in 199 words; the three intermediate measures are defined here and computed only in exercise 2.

### The covariance channel — 419

Says: With Σ estimated a second error enters, bounded path by path by θ times the C-RAFE, and in expectation the loss splits into mean noise, inversion error and noise amplified by the inverse.
Why here: First clause: Σ is now estimated too, which lifts the assumption held since eq-26-rafe; it derives the eq-08-kz that ch. 8 only quoted.
Paragraphs:
- ¶1 [derivation] Ĉ and the triangle inequality give eq-26-crafe; Wishart moments (eq-26-wishart) give the three-term split eq-26-kz-split; terms read; three caveats.
Note: One unbroken paragraph of 415 words through three displays: a pathwise bound, an expectation, the reading of three terms, and three caveats (ch. 8's substitution design misses the third term, long-only caps all three, heavy tails raise the constants); the C-RAFE is defined here and computed only in exercise 1.

### An upper bound from the forecast's information — 286

Says: A forecast with explanatory power R² allows at most a conditional squared Sharpe ratio of (S₀² + R²)/(1 − R²), with a multivariate version, tight only for the unconstrained conditional tangency position.
Why here: Stated in its first two sentences: the measures above price a forecast that exists, a bound prices one that could.
Paragraphs:
- ¶1 [derivation] One asset: Campbell–Thompson's ceiling eq-26-bound1; multivariate eq-26-boundn; tight for the unconstrained conditional tangency, slack for restrained uses; estimated with inflation.
Note: One paragraph of 278 words through two displays; the multivariate bound is stated and never evaluated in the chapter; the closing caveat (the sample bound inherits eq-08-inflation) does not return where the bound is computed.

## Measuring the Error in the Investor's Units — 3280

Says: The measures are a few lines of R; on rolling windows the RAFE tracks the unconstrained plug-in's shortfall where the RMSE does not, simulation confirms the three-term split, and the term-spread forecast's bound lies close to what its tilt earned.
Why here: The roadmap's second step: implement the measures, score three forecasts, check the covariance channel by simulation, bound the term-spread forecast.
Paragraphs: none before the first subsection.
Note: 45 percent of the chapter, about 2,000 of its 3,280 words in fourteen chunks around ten paragraphs; each of its last three subsections reads its own result, so the chapter's headline findings are stated here, not in the application.

### Two functions and a worked box — 629

Says: The helper programs are repeated from ch. 8 and ch. 6, four functions implement eq-26-rafe, eq-26-loss-identity and eq-26-cos, and a collapsed box substitutes the first sixty months into the formulas.
Why here: not stated beyond "a few lines each"; every later chunk calls these functions.
Paragraphs:
- ¶1 [method] The measures are a few lines; long-only programs and Sharpe ratio repeated from ch. 8, Bayes–Stein from ch. 6.
- (code: helpers) `gmv_qp()`, `tan_qp()`, `sharpe_of()`, `bayes_stein()`
- (code: measures) `rafe()`, `rmse()`, `ce_loss2()`, `sharpe_shortfall()`
- (code: worked) (callout) first window's sample mean against the truth; asserts eq-26-rafe and eq-26-cos to 1e-12
- ¶2 [example] (callout) First window against the truth: RAFE² beside N·RMSE², cos φ, shortfall inside its bound, share of CE lost, N/T.
Note: The heading counts two functions and the chunks define eight; the four measures are explained only in code comments; in the box the check chunk precedes the substituted formula, and c₀·RAFE is printed as the RAFE itself without saying which case of eq-26-bound holds.

### Three forecasts of the mean on rolling windows — 1337

Says: On sixty-month training and test windows the RAFE correlates with the unconstrained plug-in's shortfall and the RMSE hardly does; for the long-only tangency portfolio only the RAFE in the investor's own estimated metric keeps its lead.
Why here: Stated: ch. 6 re-estimated these three vectors and ch. 8 measured the gap of portfolios built on the first; here the forecasts themselves are scored.
Paragraphs:
- ¶1 [method] Ch. 6's sample mean, Bayes–Stein and equilibrium are scored; the equilibrium needs ch. 6's market-weight proxy, repeated.
- (code: market-proxy) regional equity capitalization weights, the assumed block split, `W16`, `delta16`; row sums and column names asserted
- ¶2 [method] Salcher–Stöckl–Hanke's train/test design, test lengthened to sixty months; three error measures; two position rules; shortfall against own perfect foresight.
- (code: rolling) per window and forecast: three errors, two shortfalls, the known-covariance loss; asserts loss equals squared RAFE on every window
- ¶3 [result] The assertion is eq-26-rafe on data: loss equals squared RAFE on every window; the shortfall is where measures compare.
- (code: cor-frame) one long frame of error against shortfall; correlations by forecast, rule and measure, and pooled
- (code: tbl-26-correlations)
- (code: cor-facts) hidden; asserts the orderings the prose states
- (code: fig-26-error-shortfall)
- ¶4 [result] Unconstrained: RMSE nearly uncorrelated, both RAFEs above; long-only: realized-covariance RAFE falls below RMSE for two forecasts; the constraint's metric explains.
Note: ¶2 sets every design choice (window lengths, three measures, two rules, the shortfall's benchmark) in one block of 177 words; ¶4 reads the table in 226 words and ends on a finding it says the cited paper does not report; the figure is drawn and never referred to; the truth here is the test window's moments, not the full-sample moments the opening named; the market-proxy chunk repeats ch. 6's data preparation in thirty lines for one of three forecasts.

### The covariance channel by simulation — 637

Says: Three hundred normal draws per window length reproduce eq-26-kz-split to the second decimal; at sixty months the amplification term exceeds the mean channel in certainty-equivalent units, while in Sharpe units the mean channel leads.
Why here: Stated: eq-26-kz-split is an expectation under normality and ch. 8 measured the channels by substitution under a long-only rule; the last sentence says the application returns to it.
Paragraphs:
- ¶1 [method] Unconstrained plug-in drawn from a normal with this market's moments at six window lengths; three terms checked in both units.
- (code: mc) six window lengths, 300 draws; losses and shortfalls with both inputs, mean only, covariance only; the formula's terms; four assertions
- (code: tbl-26-kz)
- (code: mc-facts) hidden; an accessor only
- ¶2 [result] Agreement at sixty months; inversion small, amplification above the mean channel; Sharpe units put the mean first: scaling keeps direction.
Note: ¶2 reads one row of six and does not cite the table's label; the unit dependence on which the application's first subsection rests is already stated here.

### The bound on the term-spread forecast — 668

Says: Treated as one asset, the equal-weight policy's term-spread forecast has a small out-of-sample R², the bound allows a timer a few hundredths of Sharpe ratio above the policy, and ch. 16's tilt realized a gain inside it.
Why here: Stated: ch. 16 found one signal that survived out of sample and built a tilt on it; eq-26-bound1 says what the forecast could have earned at most.
Paragraphs:
- ¶1 [method] Ch. 16's term-spread forecast rebuilt: month-end spread, expanding regression after a 120-month burn-in, R²OS against the expanding mean.
- (code: term) lagged spread from `sim_curve_weekly`; forecasts and expanding means for sixteen series; R²OS; the policy as one asset; the bound
- (code: tilt) ch. 16's banded tilt on the forecasts; Sharpe ratios of policy and tilt; asserts the tilt's gain inside the bound
- ¶2 [result] Weak forecast, close bound: numbers in eq-26-bound1; tilt's gain inside; one-asset ceiling loose for the tilt; the price of restraint.
Note: ¶2 is 227 words around one display; it sets the tilt against a ceiling the same paragraph calls right for a timer and loose for the tilt, and says the multivariate ceiling is higher without computing it; the per-series R² printed by `term` is not read; the `tilt` chunk has no prose of its own.

## Which Channel Costs More — 1571

Says: Which channel costs more depends on the unit; the shortfall is largest for windows ending in the credit crisis (unconstrained) or the rates shock (long only); and in the register only the tangency portfolio's shortfall exceeds a standard error.
Why here: The roadmap's last step: which channel costs more on this market, where the cost is largest, whether the register ranks by how much it estimates.
Paragraphs: none before the first subsection.
Note: The heading is phrased as a question and names only the first of three subsections; the section opens on a table chunk and has no figure; none of its three tables is cited by label.

### The two channels at 36, 60 and 120 months — 323

Says: In certainty-equivalent units the covariance channel is the larger at thirty-six and sixty months and the smaller at 120; in Sharpe units the mean channel is the larger at every window, which is how Chopra–Ziemba's ten-to-one is read.
Why here: The simulation subsection said the application returns to this; the table is that simulation filtered to the register's three windows.
Paragraphs:
- (code: tbl-26-channels) channel sizes and the covariance share in both units, from `mc`; asserts the order of the shares
- ¶1 [result] Unit decides: covariance larger in CE at 36 and 60, mean larger in Sharpe throughout; Chopra–Ziemba's is the Sharpe reading.
Note: One paragraph after a table with no introducing prose and no new computation; the opening's Chopra–Ziemba number is resolved here; that the certainty-equivalent share comes from the formula and the Sharpe share from the simulation is said only in the caption.

### Where the shortfall is largest — 535

Says: Sorted by the episode a sixty-month window ends in, the unconstrained rule is worst after the credit crisis and the long-only rule after the rates shock, and equal RAFEs cost different shortfalls because the shortfall reads the angle.
Why here: Stated: the rolling test window cannot reach the last two episodes; against the full-sample truth every estimation window can be scored.
Paragraphs:
- ¶1 [method] Rolling test window cannot reach the last two episodes; against the full-sample truth every estimation window is scored by episode.
- (code: episodes) RAFE and both shortfalls per window end; means by `sim_episodes` label; asserts the worst episode for each rule
- (code: tbl-26-episodes)
- (code: ep-facts) hidden; an accessor only
- ¶2 [result] Credit crisis worst unconstrained; rates shock worst long-only, dropping the truth's largest holding; equity bear: equal RAFE, smaller shortfall (angle).
Note: The truth changes back from the test window's moments to the full sample, and the text says so; ¶2 reads three episodes with two different explanations (exclusion by sign, length against angle) in 207 words; the liquidity shock is in the table and not read.

### The register, ranked by what it estimates — 707

Says: Ordered by how much they estimate, the register's five strategies have a perfect-foresight shortfall of zero for equal weighting and the largest for the tangency portfolio, with minimum CVaR negative because its benchmark is not a Sharpe ceiling.
Why here: not stated beyond the roadmap; it ties the measure to ch. 25's register and ch. 8's gap figure and closes on ch. 27 and ch. 28.
Paragraphs:
- ¶1 [method] Five strategies ordered by what they estimate; ch. 8's gap followed that order; the perfect-foresight shortfall is a different quantity.
- (code: register) reads `output/tables/oos-sweep.csv`; perfect-foresight weights on the out-of-sample months; shortfall and eq-25-se; asserts the order the prose states
- (code: tbl-26-register)
- (code: reg-facts) hidden; an accessor only
- ¶2 [result] Zero for 1/N, largest for tangency; minimum CVaR negative, a wrong ceiling; only tangency exceeds one standard error; pointers forward.
Note: ¶2 is 259 words: four strategies read, the exception explained, the standard-error comparison, and both forward pointers in its last sentence; "shortfall" here has its third ceiling (own perfect foresight over all out-of-sample months) after θ under the truth and the test window's; no error measure is computed in this subsection.

## Key Takeaways — 266

Says: The identity, the shortfall bound and the RMSE as special case with the pooled correlations, the long-only metric, the three-term covariance channel and its dependence on the unit, the R² ceiling on the term spread, and the register's shortfalls.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] For a mean-variance investor the CE loss of a wrong mean is RAFE²/2γ, a squared Mahalanobis distance; an identity.
- ¶2 [takeaway] Shortfall is θ(1 − cos φ), bounded by c₀·RAFE; RMSE is RAFE with Σ = I; pooled correlations, unconstrained plug-in.
- ¶3 [takeaway] Long-only: the RAFE in the metric the position was built in explains the shortfall; realized-covariance RAFE trails RMSE twice.
- ¶4 [takeaway] Covariance channel in three terms; larger in CE units at 36 and 60 months, smaller in Sharpe units always (Chopra–Ziemba).
- ¶5 [takeaway] R² allows at most θ_c² = (S₀² + R²)/(1 − R²); the term spread's allowance and what the tilt took.
- ¶6 [takeaway] Register shortfalls follow the order of estimation at both ends; minimum CVaR the exception, its benchmark minimizing a tail.
Note: Six bullets; ¶2 holds three statements; ¶4 counts the mean's noise N/T as a term of the covariance channel, where the theory calls it the mean channel and the application's table leaves it out of the covariance share; nothing on where the shortfall is largest.

## Exercises — 199

Says: Four exercises: the minimum-variance rule scored by RAFE and C-RAFE, the two intermediate measures, the window lengths at which the channels cross, and the bound for two values of R².
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Score long-only minimum variance on the rolling windows; correlate its shortfall with RAFE and C-RAFE; which explains a Σ-only rule.
- ¶2 [exercise] Add RAFE-CC₀ and RAFE-CV to the rolling frame; where they sit between RMSE and RAFE; which simplification costs more.
- ¶3 [exercise] From eq-26-kz-split, the window where the covariance share falls below half and amplification below inversion; again for N = 50.
- ¶4 [exercise] By eq-26-bound1, the Sharpe ratio an R² of one and of five percent could add to the policy; against eq-25-se.
Note: Four exercises; 1 and 2 are the only places the C-RAFE and the intermediate nested measures are computed; none touches the episodes or the register.
