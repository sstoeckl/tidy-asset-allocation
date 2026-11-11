---
file: chapters/22-fixed-income-sleeve.qmd
title: The Fixed Income Sleeve
part: Inside the Sleeves
words: 7199
sections: 5
paragraphs: 52
---

# Chapter

Claim: Duration targeting and portfolio optimization are one problem: a bond portfolio is a set of exposures to level, slope, curvature and spread, so a duration target is a `factor_exposure` bound on a minimum-variance program, its level strategic and its term-spread overlay tactical, while abroad the currency, not the duration, carries most of the risk.
Question: What changes in portfolio construction when the asset has a duration; cites @litterman1991 (three curve factors explain nearly all variation in government bond returns, so exposures describe a portfolio better than its list of bonds), with @nelson1987 and @diebold2006 for the form of the curve.
Why here: Stated: the sleeve is the bond part of the allocation, one level below the class series on which ch. 15 allocates, and on ch. 3's horizon axis its duration is strategic and its curve positioning tactical. Takes the data and the hedge identity from ch. 2 and appendix A, the currency share from ch. 4, the bond block's rank deficiency from ch. 7, the home-bond argument, the naming rule and the `full_investment` degeneracy from ch. 9, the quadratic program from ch. 12 and ch. 13, the units, the month-end read and the surviving term spread from ch. 16, the policy and its estimator from ch. 18; it uses ahead of their chapters the per-class costs of ch. 23 and the register's start and backtest of ch. 25, and points to ch. 10 for a skewness it does not compute. Hands the cost of maintaining the exposures to ch. 23, whether one sample is evidence to ch. 25, the ignored exposure bounds to ch. 28 and the loadings to the scenario appendix. Why it follows ch. 21 is not stated: the equity sleeve, its only sibling in the part, is never mentioned.
Does: Split a bond return into carry, rolldown, duration and convexity; read durations and maturities from factor regressions; recognize the shipped factors as one rotation of three yields beside Nelson–Siegel loadings and principal components; build a minimum-variance sleeve under duration and slope bounds while guarding three silent package behaviors; fit and bootstrap a term-spread overlay; backtest sleeves against the class ladder and read them by episode.
Order: Opening (question and claim, roadmap with the strategic and tactical labels, data, one remark on the data chunk); theory in six subsections (return decomposition, three factors, credit, duration target as constraint, currency, predictability); implementation in five (units, exposures and rotations with a worked box, currency and the fit, the constrained sleeve with a warning callout, the overlay); application as one unbroken section (four sleeves defined, backtests, a callout, three tables read in turn, a closing paragraph); takeaways; exercises. Deviations: the theory runs a chunk and reads its result (the currency share) and carries inline sample numbers on credit; the theory orders credit, target, currency, predictability where the implementation orders exposures, currency, sleeve, overlay; the overlay's in-sample fit, a result, sits in the implementation; the credit sleeve is specified only in the application's opening paragraph and its backtest chunk; every sleeve is unhedged although theory and implementation both argue that an unhedged duration target controls a minority of the risk, and the hedged sleeve is exercise 1; the application opens with a method paragraph and four chunks, not a picture, and has no subsections; `fig-22-factors` is never read; five takeaways, four exercises.

# Sections

## Opening — 440

Says: A bond portfolio is described by its factor exposures rather than its holdings, and the chapter claims that duration targeting and optimization are one problem, on the sleeve one level below ch. 15's class series.
Why here: Chapter contract; the roadmap (¶2) gives the order of the three sections; the place below ch. 15's class series is stated, the place after ch. 21 is not.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] The question; Litterman–Scheinkman's three factors; Nelson–Siegel and Diebold–Li; the sleeve sits below ch. 15; duration targeting is optimization.
- ¶2 [method] Roadmap: derive exposures, credit, currency; measure, constrain, fit the overlay; run out of sample; duration strategic, curve positioning tactical.
- ¶3 [method] Weekly curve factors and bond instruments (ch. 2, appendix A); monthly series later; dollars, unhedged; hedging subtracts `fx_return`.
- (code: data) 45 bond instruments weekly and monthly, 25 curve series, currency returns, sixteen classes, the bill; asserts counts, date alignment, no NA
- ¶4 [caveat] The curve table starts a week earlier, so a factor change exists for the first return.
Note: ¶1 carries the question, three citations, the chapter's place and its claim in one block; no visible packages block; ¶4 is a one-sentence remark that reads an assertion in the data chunk.

## Bonds as Exposures to the Curve — 1378

Says: A bond's return is carry plus rolldown minus duration times the yield change, so a portfolio matters only through its loadings on a few curve factors, plus spread and currency; a duration target is a linear constraint on those loadings, and the shape of the curve gives the tactical case.
Why here: The roadmap's first step (why a bond is a set of exposures, and what credit and currency add); the text says the exposure result is the reason the sleeve is specified as exposures; the roadmap does not name the fourth and sixth subsections.
Paragraphs: none before the first subsection.
Note: Six subsections, four of them a single paragraph; the chapter's named claim sits in the fourth, in one paragraph with inline mathematics only; one chunk, in the fifth.

### Price, duration and the return decomposition — 354

Says: The log return of a zero-coupon bond splits exactly into carry, rolldown and duration times the yield change; when K factors drive the yields, a portfolio's risk depends on its weights only through K exposures.
Why here: First because every later subsection refers to eq-22-return or eq-22-exposure; the text says the exposure result is why the sleeve below is specified as exposures and not as weights.
Paragraphs:
- ¶1 [definition] Price of a zero-coupon bond at a continuously compounded yield; eq-22-price.
- ¶2 [derivation] One holding period: carry, rolldown, duration times yield change, eq-22-return; Ilmanen, Koijen et al.; Macaulay duration, convexity; constant-maturity zeros.
- ¶3 [derivation] K factors drive yields; eq-22-exposure; equal exposures mean equal risk; K = 3 is Litterman–Scheinkman; hence a sleeve of exposures.
Note: ¶2 does five jobs in about 200 words (the identity, the reading of its terms, two attributions, duration and convexity defined, the modeled market's design); convexity is defined in a clause and returns only in the worked box.

### Three factors of the curve — 234

Says: Nelson–Siegel's curve with Diebold–Li's level, slope and curvature, and Litterman–Scheinkman's principal components, describe the same three factors; with three maturities any such description is an exact rotation of the three yields.
Why here: Needs the K-factor exposure just derived; the text defers which rotation the data ship to the implementation, and ties the factor count to ch. 7's rank deficiency.
Paragraphs:
- ¶1 [definition] eq-22-ns; loadings read as level, slope, curvature; the fixed decay; observable proxies; principal components; exact rotation; ch. 7's rank deficiency.
Note: One paragraph holds one equation, three literatures and two cross-references; the slope's sign (short minus long) is fixed in a clause and decides the sign of the overlay's term spread later.

### Credit as a separate exposure — 236

Says: A corporate bond adds a fourth term, the spread duration; spread changes share one factor per region, the spread is persistent, and its volatility scales with its level.
Why here: The roadmap's "what credit adds"; the text says two features matter for the sleeve; why it comes before the duration target is not stated.
Paragraphs:
- ¶1 [definition] Spread duration; Merton, Elton et al., Collin-Dufresne et al.; one credit factor per region; persistence, half-life; duration times spread.
Note: A definition, three attributions, the market's construction and two measured facts (inline numbers from the sample) in one block; duration times spread is introduced, and the credit sleeve later bounds spread duration alone.

### Duration targeting as a constrained optimization — 210

Says: A duration target is a linear constraint on the weights, so minimum variance under it stays a quadratic program; in `PortfolioAnalytics` it is a `factor_exposure` constraint, a second column chooses bullet or barbell, the level is strategic and the conditioned deviation tactical.
Why here: Needs eq-22-exposure (a duration target bounds the level loading); sends the program to ch. 12 and ch. 13 and the deviation to the implementation as ch. 18's policy; why it sits between credit and currency is not stated.
Paragraphs:
- ¶1 [claim] Fisher–Weil immunization; the target as a linear constraint, still a quadratic program; `factor_exposure`; slope column; Campbell–Viceira: level strategic, deviation tactical.
Note: The chapter's named claim is made here, in one paragraph of about 200 words, with the constraint as inline mathematics and no numbered equation; bullet and barbell are explained in a clause and set as terms only in the implementation.

### Currency, and why the two decisions are not separable abroad — 214

Says: For a dollar investor most of the variance of a foreign government bond is currency, so the duration decision and the currency decision cannot be taken one at a time.
Why here: Stated: every series is in dollars, and ch. 4 showed that the currency share depends on the asset; the text hands the effect on the factor fit to the implementation.
Paragraphs:
- ¶1 [claim] A foreign bond carries local return and currency together (ch. 4); for a bond it is mostly currency.
- (code: currency-share) share of variance removed by hedging, `JP_government` and `EU_government`
- ¶2 [result] Hedging removes most of `JP_government`'s variance; Campbell et al., Perold–Schulman, Black, Karnosky–Singer; the two decisions go together.
Note: The theory's only chunk, and a result read inside the theory; ¶2 reads the Japanese number, the European one prints unread; four positions on hedging pass in one sentence.

### Predictability from the curve — 122

Says: The shape of the curve forecasts bond returns, and ch. 16 found the term spread the one signal that survives out of sample on this market, so the overlay conditions on it.
Why here: Stated: the tactical case rests on it; it closes the theory, though the overlay it motivates comes four subsections into the implementation.
Paragraphs:
- ¶1 [evidence] Fama–Bliss, Campbell–Shiller, Cochrane–Piazzesi, Fama–French; ch. 16's term spread survived; the overlay conditions on it.
Note: Four citations and one borrowed result, no equation; the shortest subsection.

## Measuring and Targeting the Exposures — 2957

Says: The shipped factors come in mixed units and are an observable rotation of three yields; regressions recover each bond's duration and maturity; duration and slope bounds in `factor_exposure` produce a barbell and a bullet, with three silent package behaviors; the overlay's fitted tilt has the predicted sign and an inconclusive t-statistic.
Why here: The roadmap's second step (measure the exposures, build the constrained sleeve, fit the overlay); needs every equation of the theory; the application takes `sleeve()`, `mat`, `policy_utility()`, `D_bar` and `w_bar` from here.
Paragraphs: none before the first subsection.
Note: Two fifths of the chapter (2,957 of 7,199 words, 23 of 52 paragraphs); the second subsection alone runs 1,219 words and does four things (exposures, maturities, three rotations, a worked week).

### The factor series and their units — 288

Says: Level, slope and curvature ship in percentage points and the spreads in decimals; the chunk converts to decimals so that a loading is a duration in years.
Why here: Stated: the units are read from the magnitudes before anything is computed from them; ch. 16 found the same.
Paragraphs:
- ¶1 [method] A column of numbers does not state its unit; read it from the magnitudes first.
- (code: units) median and maximum by kind; asserts the level above one and the spreads below one; divides level, slope, curvature by 100
- ¶2 [result] The level's maximum can only be percentage points, the spreads' only decimals (as ch. 16); all to decimals.
- (code: fig-22-factors) hidden code; US level, slope and curvature, the four episodes shaded
Note: The subsection ends on a figure no paragraph reads, here or later; it draws the unconverted series, in percentage points.

### Factor exposures, and which bond is which — 1219

Says: Regressing each instrument on its region's factor changes gives level loadings equal to minus the modified duration, identifies the two-, five- and ten-year bonds, and shows the shipped factors to be the observable rotation of three yields; Nelson–Siegel loadings and principal components describe the same space.
Why here: Stated: the exposures of eq-22-exposure are regression coefficients, and `sim_assets` carries no maturity, so it is inferred through eq-22-return; answers the theory's deferred "which rotation"; `mat` and `id_of()` serve everything after.
Paragraphs:
- ¶1 [method] Each instrument's weekly return on its region's level, slope, curvature changes, plus spread for credit; hedged and unhedged.
- (code: exposures) `exposure()`; the table `expo` with four loadings and both R²
- ¶2 [method] No maturity in `sim_assets`; infer it from the level loading; assert implied durations within ten percent.
- (code: maturities) ranks the loadings within region, class and grade; asserts; `mat`, `id_of()`
- (code: tbl-22-exposures) hidden code; the nine US instruments
- ¶3 [result] Level loadings are minus modified duration; credit adds an equal spread duration; the factors span every US bond (ch. 7).
- ¶4 [result] Slope and curvature columns show the rotation: ten-year on level alone, two-year adds slope, five-year half of each.
- (code: loading-matrix) loadings relative to the level loading, asserted against `B_emp`
- ¶5 [claim] The shipped factors are Diebold–Li's observable ones; latent Nelson–Siegel loadings are another rotation; exposures transform, risk does not.
- (code: nelson-siegel) `ns_load()`, `yields()`; prints the latent loadings at 2, 5 and 10 years
- ¶6 [transition] Principal components are the third description, the one without a functional form.
- (code: pca) variance shares and rotation; asserts the sign patterns of a level, a slope and a curvature
- ¶7 [result] First component moves all yields together, second opposes the ends, third the middle; shares near Litterman–Scheinkman's.
- ¶8 [example] (callout) eq-22-return checked on the week the US ten-year yield moved most; yields continuously compounded.
- (code: worked-week) carry, duration, convexity, first- and second-order sums beside the actual return
- ¶9 [example] (callout) Numbers substituted into eq-22-return: duration is the move, convexity returns a little, the rest is rolldown and error.
Note: Four topics in one subsection; ¶3 finds the modified duration under annual compounding where the theory's bond had duration equal to maturity, and only the worked box bridges the two; the Nelson–Siegel chunk prints loadings no paragraph reads; the worked box checks the theory's first identity at the end of a passage on rotations, collapsed, code before formula.

### What the currency does to the fit — 238

Says: Hedged, foreign government bonds are explained by their own curves as well as US bonds are; unhedged, the mean R² collapses, so a duration target on an unhedged foreign sleeve controls a minority of its risk.
Why here: The measurement the theory's currency subsection handed forward; uses the two R² columns of `expo`; why it comes before the sleeve is not stated.
Paragraphs:
- ¶1 [transition] Outside the US the same regressions tell two stories.
- (code: tbl-22-regions) hidden code; implied durations and mean R², hedged and unhedged, by region
- (code: r2-facts) hidden; asserts the hedged mean above 0.9 and the unhedged below 0.3
- ¶2 [result] Hedged mean R² over four regions and the lowest instrument; unhedged mean; an unhedged target controls a minority of risk.
Note: The finding that an unhedged target controls little of the risk stands directly before a sleeve that is built unhedged; the table is read without being named.

### The sleeve as a set of exposures — 708

Says: Minimum variance over the fifteen government bonds with duration as a `factor_exposure` constraint gives a barbell at duration five; a slope bound turns it into a bullet; the constraint binds its matrix by position, and a bound that cannot be met returns `NA` weights without a message.
Why here: Realizes the theory's fourth subsection with the loadings of `expo`; ¶1 announces both callouts and their reasons (name binding below, the band in the application); the application's strategies call `sleeve()`.
Paragraphs:
- ¶1 [method] Fifteen government bonds, weekly, unhedged; `B` from the level loadings; names bound and asserted; bounds widened by a millionth.
- (code: sleeve) `B`, `sleeve()`, `exposures()`, `ann_vol()`; unconstrained and duration-five weights, exposures and volatility
- ¶2 [result] Unconstrained: the US two-year almost alone (ch. 9's argument); at duration five a barbell with foreign ten-years, no five-year.
- ¶3 [caveat] (callout) The constructor checks only the row count of `B`; a reordered `B` is accepted and hits the wrong bonds.
- (code: positional) `B` reversed; the duration the solver believed beside the true one
- ¶4 [caveat] (callout) Reported five, true value inline; `sleeve()` refuses a misnamed `B` (ch. 9's rule); `random_portfolios()` ignores the bounds (ch. 28).
- ¶5 [method] A second column of `B` bounds the slope exposure, which places the duration on the curve.
- (code: bullet) slope bound between 2 and 2.5 at duration five; barbell beside bullet
- ¶6 [result] The slope bound forces the five-year, a bullet; same shift exposure, another twist exposure; the ends hedged each other better.
- ¶7 [method] Last case: a duration of twelve, which no long-only mix of these bonds reaches.
- (code: infeasible) class, `NA` weights and solver status of the result
- ¶8 [caveat] No error, no warning: usual class, `NA` weights, message stored; ch. 25's failure; hence `pm_backtest()` in the application.
Note: Three package behaviors in three placements: a warning callout, running text, and a callout deferred to the application whose `band` argument already appears in this chunk; ¶2 credits the foreign holdings to currency diversification, one subsection after currency was the risk the target does not control.

### The duration overlay as a parametric policy — 497

Says: The long-end weight is an anchor plus theta times the standardized term spread, theta fitted by maximizing average power utility; the fit has the sign the literature predicts, without the precision to be sure of it.
Why here: Stated: it is the tactical layer, written as ch. 18's policy; the theory's fourth and sixth subsections announced it; the anchor takes the ladder's duration because that is the class series the allocation sees; the application re-estimates it monthly.
Paragraphs:
- ¶1 [definition] eq-18-policy with one characteristic, the standardized US term spread; eq-22-overlay; power utility; anchor strategic, theta tactical; month-end curve.
- (code: overlay-data) month-end curve index, asserted; term spread as minus the slope; long and short returns; `D_bar`, `w_bar`
- (code: overlay-fit) `policy_utility()`, `fit_theta()`, 500 block-bootstrap draws, certainty equivalent; prints theta, standard error, t and annual gain
- ¶2 [result] Theta in weight and in duration; Cochrane–Piazzesi's direction; Künsch block-bootstrap error and t; certainty-equivalent gain; sign without precision, Welch–Goyal.
Note: An in-sample result in the implementation, and the number the application later leans on to judge the overlay; two chunks back to back with no prose between; the signal is standardized on the full sample here and recursively in the application.

## The Sleeve Out of Sample — 1978

Says: From the register's first out-of-sample month the constant-duration sleeve has the ladder's duration at lower volatility because its US holdings carry little currency; the overlay lost least in the rates shock, which is one episode; credit as a second exposure raises the Sharpe ratio in the table and lost in the credit crisis; the ladder is the sleeve's benchmark.
Why here: The roadmap's last step (run the sleeves out of sample against the class series the allocation sees); needs `sleeve()`, `mat`, the policy and its anchor from the implementation; the text gives its reason for running on instruments: the class ladders share one duration, so no target can be set on them.
Paragraphs:
- ¶1 [method] Observation 121, sixty-month window, monthly; class ladders share one duration, so sleeves run on instruments; four sleeves defined.
- (code: overlay-path) theta and tilt re-estimated at each date; long-end weight clipped to [0, 1]; `D_path`; prints its range and the share at a bound
- (code: fig-22-duration) hidden code; the overlay's target against the constant one, episodes shaded
- (code: backtests) four `pm_strategy()` definitions, `B_cre` for credit, four `pm_backtest()` runs; asserts no failed period and the start at observation 121
- (code: exact-target) the same windows with `band = 0`; counts the failures
- ¶2 [caveat] (callout) With `band = 0` the equality reaches `quadprog` as opposing inequalities (ch. 9); failures counted inline; `n_failed` asserted zero.
- (code: tbl-22-oos) hidden code; Sharpe ratio gross and net, volatility, drawdown, turnover for five lines
- (code: oos-facts) hidden; asserts the constant-duration volatility below equal weight's; the average US share
- ¶3 [result] Three readings: same duration, lower volatility through US holdings; the overlay's Sharpe ratio and turnover; credit's Sharpe ratio, skewness unshown.
- (code: tbl-22-episodes) hidden code; cumulative return of each sleeve in the four episodes
- (code: episode-facts) hidden; asserts that all lose in the rates shock, in the order overlay, constant, equal weight
- ¶4 [result] Rates shock: all lose, the overlay least, the curve having flattened first; one episode; elsewhere a high target for nothing.
- ¶5 [transition] The credit crisis is the opposite case, and the spreads say why.
- (code: tbl-22-spreads) hidden code; yield and spread changes and ten-year returns over the credit crisis and the rates shock
- (code: spread-facts) hidden; asserts the signs
- ¶6 [result] Credit crisis: yields fell, spreads widened; duration paid the government bond, spread duration cost credit; rates shock: both hurt.
- ¶7 [claim] The ladder is the benchmark, the sleeve exposures relative to it; nesting by `mult.portfolio.spec()`; scenarios; ch. 23, ch. 25.
Note: Seven paragraphs in 1,978 words, more than half of it code, with no subsection; between ¶1 and the next body prose stand four chunks, one of them a figure, then a callout and a table, and the figure is first read in ¶4; ¶1 switches `B` from the estimated loadings to the maturities in a clause and is the only prose that specifies the credit sleeve; the callout's title types "a third of the windows" where its body computes the count; ¶3's first reading is a currency effect by the text's own account; ¶7 does four jobs and tells exercise 4's finding.

## Key Takeaways — 228

Says: Five bullets: the return decomposition and exposures, the three factors and their rotation, the duration target as a `factor_exposure` constraint with its three traps, foreign bonds as currency, and the overlay as a one-characteristic policy with thin evidence.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [takeaway] Return is carry plus rolldown minus duration times yield change; equal exposures, equal interest-rate risk; Litterman–Scheinkman.
- ¶2 [takeaway] Three factors; the market ships Diebold–Li's observable ones, a rotation of three yields; principal components recover the shapes.
- ¶3 [takeaway] A duration target is a `factor_exposure` constraint; a second column picks barbell or bullet; still a quadratic program; three traps.
- ¶4 [takeaway] For a dollar investor a foreign government bond is mostly currency; duration and currency are decided together; Campbell et al.
- ¶5 [takeaway] The overlay is ch. 18's policy with one characteristic: predicted sign, t below two, smallest rates-shock loss, one episode.
Note: Five, as the contract asks; credit, a theory subsection and the fourth sleeve, has no bullet; ¶3 folds three package traps into one bullet; ¶5's "below two" is typed, with no assertion behind it in the fit chunk.

## Exercises — 164

Says: Four exercises: the duration-five sleeve on hedged returns, the overlay at other risk aversions, the failed windows under another solver, and the nested sleeves with their proxy returns.
Why here: Chapter contract; not stated.
Paragraphs:
- ¶1 [exercise] Repeat the duration-five sleeve on hedged returns; holdings, volatility against unhedged; where the lowest-cost duration is bought.
- ¶2 [exercise] Refit eq-22-overlay at risk aversion two and ten; how theta and the bootstrap t move; who should run an overlay.
- ¶3 [exercise] Solve a dozen failed `band = 0` windows with CVXR and OSQP; is the exact target met; what `pm_backtest()` does.
- ¶4 [exercise] Nest constant-duration and equal-weighted credit sleeves with `mult.portfolio.spec()`; read the proxy returns: months before the first rebalance, their weights.
Note: Four against around three; exercise 1 holds the hedged sleeve that the chapter's currency argument calls for and the text never builds; exercise 4's finding is told in the application's last paragraph and exercise 3's second question is answered in its callout.
