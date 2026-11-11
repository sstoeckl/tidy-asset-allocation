---
file: chapters/10-risk-measures.qmd
title: Risk Measures Beyond Variance
part: Portfolio Optimization
words: 7637
sections: 5
paragraphs: 52
---

# Chapter

Claim: Replacing variance by expected shortfall changes little on sixteen class series: the two frontiers are one curve within the width of the line, the minimum-ES portfolio swaps one holding and moves one moment, and out of sample the tail rule realizes the higher shortfall because a 5% tail on sixty months is three observations.
Question: What changes when variance is replaced by a measure that is subadditive; cites Markowitz (1959) for the semi-variance and Artzner et al. (1999) for coherence in the first two sentences.
Why here: Opens on chapter 9's optimizers, which all used variance; takes the data from chapter 2, the excess basis, the strategic label, quadratic utility and the "judge by the measure chosen" rule from chapter 3, the ES definition, the Cornish-Fisher expansion, the ellipticity verdict and the credit non-normality from chapter 4, the problem, the frontier and the `US_credit` holding from chapter 9, and γ/2 from appendix B; hands the comoments to 11 ("here they enter only through the measure"), the convex-versus-search distinction and the ratio normalization to 13, the ES decomposition to 14, the register to 25, the cost of a tail estimate to 26, and two upstream issues to the package notes. That one clause is the only reason given for preceding chapter 11; why it precedes 12: not stated.
Does: Test subadditivity on every pair of a panel; pose minimum ES as the Rockafellar-Uryasev linear program under `ROI`; read any weight vector on every measure with `extract_risk()`; trace two frontiers from one data frame; name the solver each objective needs; set the ratio flags explicitly; recognize an unevaluated `CSM` and a wrong-sign `EQS`; read the register with an error bar.
Order: Theory in six subsections (coherence, value at risk, expected shortfall and its linear program, the modified measure, downside and drawdown and two more coherent measures, what each measure assumes), implementation in three (the four specifications and the package defaults, the mean-ES frontier, `CSM` and `EQS` under `CVXR`), application in three (four portfolios on one table, the cross table, the register), five takeaways, four exercises. Deviations: the theory runs code in two collapsed worked boxes; all three figures and the chapter's central reading (the `US_credit` weight along the two frontiers and the one-month skewness behind it) sit in the implementation, so the application opens on a table rather than a picture; none of the three content sections has prose of its own above its subsections; the fourth of the four portfolios is produced by a chunk whose only introduction is inside a callout about a different trap.

# Sections

## Opening (untitled) — 351

Says: Nothing in the data required variance; Artzner asked which properties a risk measure needs, value at risk lacks the one that matters, and the chapter asks what a measure that has it changes.
Why here: Contract position; the text gives the sequence: axioms, value at risk, expected shortfall and its program, the modified measure, the other families, then the package, then one problem under four objectives.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Chapter 9's optimizers used variance unforced; Markowitz's semi-variance; Artzner's axioms; value at risk lacks the one that matters; the question.
- ¶2 [method] The sequence; the allocation is strategic in chapter 3's sense: full-sample moments, no timing, out of sample read from chapter 25's register.
- ¶3 [method] Data: the sixteen class series of chapter 2, in excess of the bill as chapter 3 argued, loaded as chapter 9 loads them.
- (code: data)
- (code: credit-facts) hidden; asserts `US_credit`'s Sharpe rank and that it is the most negatively skewed, for the prose to name
Note: The "packages used" block is hidden (`include: false`), so the reader sees no package list; ¶2's register promise is redeemed only by the application's last subsection.

## Coherence, Tails, and What Variance Assumes — 1879

Says: A risk measure must be subadditive to respect diversification; value at risk is not, expected shortfall is and is a linear program, the modified version is not convex, and every measure encodes a belief about the investor.
Why here: The opening's first clause ("We first set out the coherence axioms"); the subsections follow the opening's list in order.
Paragraphs: none of its own.
Note: Heading only; six subsections, two of which run code in collapsed boxes that later prose and the first takeaway depend on.

### Four properties of a risk measure — 229

Says: Coherence is four axioms, subadditivity is the one that matters for building portfolios, and variance is used despite failing it because under elliptical returns the choice of measure changes no ranking.
Why here: The opening's question is about "that property", so it is defined first; needs chapter 4's verdict that this market is not elliptical; ¶2's "the last axiom is the one that matters here" sets the test the next subsection applies.
Paragraphs:
- ¶1 [definition] X and ρ(X) in loss units; monotonicity, translation invariance, positive homogeneity, subadditivity; eq-10-subadditive.
- ¶2 [claim] Subadditivity is diversification; variance and standard deviation fail; under elliptical returns every such measure is a function of σ (McNeil); chapter 4 said not elliptical.

### Value at risk — 450

Says: Value at risk is the regulatory standard, satisfies three axioms and fails subadditivity, on this data for a few credit-government pairs of the same currency.
Why here: Named in the opening as the standard that lacks the property; the text says the failure is "not only in contrived examples", so the box tests it on every pair; the box's "expected shortfall, defined below, fails on none" hands over.
Paragraphs:
- ¶1 [definition] VaR_α = −q_α, eq-10-var; α = 0.05 throughout, `p = 0.95` in the package; Jorion; fails eq-10-subadditive because a quantile ignores what lies beyond it.
- ¶2 [method] (callout, collapsed) Test every pair equally weighted; homogeneity makes it one comparison per pair; `invert = FALSE` returns losses as positives.
- (code: subadditivity)
- (code: subadditivity-facts) hidden; asserts no ES violation and that every VaR violation is a credit series with its own government bond
- ¶3 [result] (callout) Fails on a few of the 120 pairs, each credit with its currency's government bond; ES on none; violations small, near-elliptical; chapter 4 located non-normality in credit.
Note: The collapsed box defines `loss_var()` and `loss_es()`, which every later chunk that reads a tail uses (`es-by-hand`, `ratio-defaults`, `frontier-frame`, `four-portfolios`), and its `mix` is what the first takeaway counts; a box a reader may skip is load-bearing. The subsection title is the measure; the box carries the finding.

### Expected shortfall and the linear program — 552

Says: Expected shortfall is the smallest coherent measure dominating value at risk, and the Rockafellar-Uryasev representation turns its minimum into a linear program with one variable per month.
Why here: "Defined below" from the box; the text says the dominance property "is why it is the tail measure this book uses", and the representation is "what made expected shortfall usable in an optimizer", which the implementation needs; the box's Cornish-Fisher figure opens the next subsection.
Paragraphs:
- ¶1 [definition] ES is the expected loss beyond VaR, eq-04-es; three names the package accepts; coherent (Acerbi-Tasche); smallest coherent measure dominating VaR.
- ¶2 [derivation] eq-10-ru; convex jointly in (w, ζ); the empirical LP eq-10-lp with N+T+1 variables; atoms; local is global (Boyd), chapter 13; the frontier row; STARR.
- ¶3 [method] (callout, collapsed) The sample ES averages the tail; αT is not an integer; `PerformanceAnalytics` averages strictly below the quantile.
- (code: es-by-hand)
- ¶4 [example] (callout) The tail months' range; the formula with the numbers in it; ES over VaR; the Cornish-Fisher figure roughly twice, as chapter 4 said, because skewness pushes the expansion past the observed tail.
Note: ¶2 is one sentence chain across two display equations doing six jobs (representation, convexity, the LP, atoms, convex versus search, frontier and STARR). The box's `tail_months` is read again by the credit-tail paragraph of the implementation.

### The modified expected shortfall — 177

Says: The Cornish-Fisher expected shortfall replaces the few tail observations by a four-moment expansion, which makes it depend on every comoment and leaves it non-convex, reachable only by search.
Why here: Follows the box's disagreement between the two figures; the text gives Yamai-Yoshiba's larger standard error as the reason for the alternative; hands non-convexity to the implementation and chapter 13, the tensors to 11, the decomposition to 14.
Paragraphs:
- ¶1 [definition] Historical ES uses αT observations, with the larger standard error (Yamai-Yoshiba); Favre-Galeano, Boudt et al.: modified ES from four moments; not convex; search; `ES()` defaults to it.
Note: One paragraph that defines the measure, routes it to three chapters and ends on a package default already stated in chapter 4.

### Downside measures, drawdowns, and two more coherent measures — 227

Says: Lower partial moments, conditional drawdown at risk and the second-order CSM are the other families, the last a cone program; the package's EQS is documented only by its code.
Why here: "Three further families deserve a place", the oldest first; no other reason given; CSM and EQS are defined here because the implementation solves them, and which tail EQS squares is "measured rather than assumed" there.
Paragraphs:
- ¶1 [definition] Roy's safety first, Markowitz's semi-variance, Bawa's LPM eq-10-lpm, Sortino; Chekhlov's CDaR as an LP; Krokhmal's CSM eq-10-csm, coherent, a cone program; EQS, undocumented.
Note: Three families and two display equations in one paragraph; the lower-partial-moment and drawdown families are defined and then never solved, read or mentioned again in the chapter.

### What the choice of measure assumes — 244

Says: Variance is right only under quadratic utility or two-moment returns; a tail measure responds to the skewness that lives in credit, at a cost in estimation; and a portfolio must be judged by the measure it was chosen by.
Why here: Closes the theory on chapter 3's investor; needs eq-03-quadratic-utility and chapter 4's credit finding; the rule in ¶2 is the one the application follows ("sec-10-application does that").
Paragraphs:
- ¶1 [claim] Each measure encodes a belief; variance is symmetric, Markowitz's two cases, Levy-Markowitz; a tail sees the skewness in credit: `US_credit`'s rank and skewness; Ang et al.; estimation cost; chapter 11.
- ¶2 [method] Chapter 3's rule: judge by the measure chosen, show every portfolio on every measure; the application does that.
Note: ¶1 does five jobs (utility theory, the credit fact, asset pricing, estimation cost, a pointer to chapter 11). The ellipticity argument of "Four properties" ¶2 is restated here and a third time in the implementation's credit-tail paragraph.

## Implementation — 3135

Says: Four specifications on one constraint set go to `ROI`, `DEoptim` and `CVXR`; the package's ratio defaults, its ignored `method`, an unevaluated `CSM` and a wrong-sign `EQS` are measured; and the two frontiers nearly coincide as curves while disagreeing on `US_credit`.
Why here: The opening's second clause ("then show which of these the package can solve, with which solver, and where its defaults do something other than what the specification says").
Paragraphs: none of its own.
Note: Heading only. The section holds all three figures of the chapter and the reading that explains the `US_credit` result (the one-month skewness), which is application rather than implementation; the application section that follows has tables only.

### The objectives the package knows — 1086

Says: The four specifications are solved, three by `ROI` and the modified one by differential evolution, and two defaults are measured: `ROI` ignores `method`, and a mean plus a tail objective is a ratio problem unless told otherwise.
Why here: First because the four specifications "carry the chapter"; needs eq-10-lp, eq-10-var and the γ/2 convention; produces the four weight vectors the application reads.
Paragraphs:
- ¶1 [method] Objectives are named for their functions; `VaR` is search-only, `CSM` and `EQS` are `CVXR`-only; the four specifications; `risk_aversion = 2` is γ = 4.
- (code: specs)
- ¶2 [method] The three convex ones go to `ROI`: a quadratic program for the two variance objectives, the LP for the shortfall.
- (code: solve-convex)
- ¶3 [code] Two ways to read risk: `extractObjectiveMeasures()` reports what was minimized, `extract_risk()` recomputes every measure for any weights.
- (code: read-back)
- ¶4 [result] Both ES figures are the LP's value, interpolated between two adjacent worst months, differing from `ES()`'s tail average at the fourth decimal.
- ¶5 [caveat] (callout) The LP is the only formulation `ROI` has; `method = "modified"` returns the historical solution without a message.
- (code: roi-ignores-method)
- ¶6 [method] (callout) The modified measure needs a black-box solver; none carries a guarantee; differential evolution with a small budget, and the application shows what it bought.
- (code: solve-modified)
- ¶7 [caveat] (callout) `maxSR` defaults `FALSE` and gives quadratic utility at `risk_aversion = 1`; `maxSTARR`, `CSMratio`, `EQSratio` default `TRUE`; `FALSE` makes it minimum ES with the return merely reported.
- (code: ratio-defaults)
- (code: tbl-10-ratio-defaults)
- ¶8 [result] (callout) The two default rows overlap only partly, one mostly `US_government`, the other only equity; the object does not say which was solved; state the flags in both directions.
Note: Five of the eight paragraphs sit in two callouts. The chunk that produces the fourth chapter portfolio (`solve-modified`) stands between the callouts with no prose of its own; its introduction (¶6) is the last paragraph of a callout about a different trap. The ratio callout builds `spec_mean_es` and `spec_mean_sd`, which the frontier subsection then traces.

### The mean-ES frontier — 1243

Says: The mean-ES and mean-variance frontiers are the same curve within the width of the line and different portfolios in `US_credit`, whose skewness is the work of one month that a 5% historical tail averages away.
Why here: Not stated beyond the function existing; needs the two-objective specifications from the ratio callout; the mean-variance frontier of chapter 9 is "computed beside it on the same constraints", and the `US_credit` holding is the one chapter 9's application traced.
Paragraphs:
- ¶1 [method] `create.EfficientFrontier()` with `type = "mean-ETL"` solves the LP at the extremes and at return targets; `chart.EfficientFrontier()`; the variance frontier beside it.
- (code: frontiers)
- (code: fig-10-native-frontier)
- ¶2 [method] Two frontiers on a common axis; every coordinate into one data frame first so no point pairs with another portfolio's return.
- (code: frontier-frame)
- (code: fig-10-frontiers)
- (code: frontier-gap) asserts the curves lie within a tenth of a point and that the credit gap runs both ways
- ¶3 [result] Two statements: as curves the frontiers nearly coincide, saving and paying within the line's width; as portfolios they differ, and the next figure shows where.
- (code: fig-10-credit-weight)
- ¶4 [result] Peak `US_credit` weight on each frontier; at a matched target either holds more; the tail measure did not sell the asset chapter 9 traced; once a target binds both buy it.
- (code: credit-tail)
- ¶5 [result] The skewness is one month in the credit crisis; without it near zero; a 5% tail averages it with the rest, so historical ES ranks the series low and Cornish-Fisher high; McNeil on sixteen assets: weakly determined weights.
Note: The package's own chart (`fig-10-native-frontier`) is drawn and never read in prose; its caption does the reading. ¶5 is the chapter's explanation of its main result and the third statement of the ellipticity argument. Two chunks and a figure separate ¶2 from ¶3.

### Two coherent measures that need a cone solver — 806

Says: `CSM` and `EQS` solve under `CVXR` beside the minimum-ES portfolio; a search on `CSM` evaluates nothing and returns its first candidate, and the package's `EQS` squares the gains rather than the losses.
Why here: "Their minimum-risk portfolios sit beside the minimum-ES one" is the only reason given; the two measures were the last defined in the theory, and the EQS question the theory deferred is answered here.
Paragraphs:
- ¶1 [method] `CSM` and `EQS` under `CVXR` only, through eq-10-csm and its squared counterpart; their frontier functions; minimum-risk portfolios beside the minimum-ES one.
- (code: csm-eqs)
- ¶2 [caveat] (callout) `constrained_objective()`'s `CSM` branch is empty, issue #51; a search scores every candidate at zero and returns the first.
- (code: csm-metaheuristic)
- ¶3 [caveat] (callout) Weights, an empty measure list, no warning; use `CVXR`; an empty `extractObjectiveMeasures()` is the signature.
- ¶4 [caveat] (callout) Ratio problems are solved normalized and rescaled; earlier builds skipped the rescaling, this build binds the limits, measured; the `EQS` value does not survive the rescaling.
- (code: eqs-ratio-box)
- ¶5 [caveat] (callout) The squared quantity is the positive part of the return, not of the loss; `EQS` is the tail average of squared gains.
- (code: eqs-sign)
- ¶6 [result] (callout) Minimizing `EQS` penalizes gains, so its portfolio is more negatively skewed than minimum ES; pose it on `-Re` and read the figure from the weights.
Note: Five of six paragraphs and three of four chunks are two callouts; the subsection is a pair of traps with one method paragraph in front. The `CSM` and `EQS` weights of `csm-eqs` are printed once and never enter the application's four portfolios.

## Four Objectives on One Universe — 1639

Says: On one long-only problem only quadratic utility holds `US_credit` in size, the minimum-ES portfolio swaps one holding and moves one moment at a small price, and out of sample the tail rule realizes the higher shortfall at every window.
Why here: The opening's third clause ("then solve one long-only problem under four objectives and read what each bought"); needs the four weight vectors of the implementation.
Paragraphs: none of its own.
Note: Heading only; no figure in the section. The portfolios are solved in the implementation, so the application's first act is a table.

### What each objective bought — 727

Says: The quadratic-utility investor holds the most negatively skewed series for its Sharpe ratio, the no-mean objectives hold almost none, minimum ES is the closest to symmetric, and the search did not find its own minimum.
Why here: "The four portfolios of sec-implementation" differ only in what they call risk; the `US_credit` column is read first "for the reason chapter 9 gave".
Paragraphs:
- ¶1 [method] Same problem, four names for risk; each reported on every measure, tails on the excess returns optimized, drawdown on the total-return path.
- (code: four-portfolios)
- (code: tbl-10-four)
- (code: four-facts) hidden; asserts the orders and names the next two paragraphs state
- ¶2 [result] Quadratic utility holds `US_credit` in size, the rest equity, with the most negative skewness and the deepest drawdown; minimum ES closest to symmetric; the two risk-only portfolios share `US_government` and swap one series.
- ¶3 [result] The search's modified ES exceeds what a convex portfolio reaches unasked; it did not find its own minimum, as chapter 13 measures; convex solutions are the result, the search an illustration.
Note: ¶2 reads six columns of the table in one paragraph carrying fifteen inline numbers.

### Each portfolio on every measure — 313

Says: Each convex portfolio is best on its own measure, the searched one is not, and the price of choosing the tail is small in the other measures.
Why here: The rule of chapter 3 that the theory's last paragraph promised the application would honor; the table "does that on the diagonal".
Paragraphs:
- ¶1 [method] Chapter 3's rule; the cross table shows the diagonal and everything beside it.
- (code: tbl-10-cross)
- ¶2 [result] Three of four bold cells carry the asterisk; the fourth is won by a convex portfolio; minimum ES gives up a little volatility for a little shortfall; the honest size of the effect.
Note: The cross table repeats four columns of the previous table in a second layout; ¶2's "exchanged one holding and moved one moment" restates ¶2 of the previous subsection.

### Out of sample, read from the register — 599

Says: On rolling windows the minimum-ES rule realizes a higher expected shortfall than minimum variance at every window, differs only in the moments it was not asked about, and the thirty-six-month row rests on a two-observation tail.
Why here: "Everything above uses full-sample moments": the opening's strategic claim sends the out-of-sample check to chapter 25's register, read rather than recomputed "so that the two chapters cannot disagree"; hands the cost to chapter 26.
Paragraphs:
- ¶1 [method] Full-sample so far; the register runs the two risk-only rules on rolling windows; this chapter reads its lines.
- (code: oos)
- (code: tbl-10-oos)
- (code: oos-facts) hidden; asserts the orders and the Sharpe spread against Lo's standard error
- ¶2 [result] At sixty months minimum ES realizes the higher shortfall, same sign at all windows; three observations; chapter 26; its edge in skewness and Sharpe does not survive 120 months.
- ¶3 [caveat] The thirty-six-month row is a warning: the highest Sharpe ratio from a two-month tail; Lo's error bar; all six ratios inside it; the closing rule.
Note: The closing rule ("choose the measure for what it sees, report by the measure chosen") is the fourth statement of chapter 3's rule in this chapter, after the theory's last ¶2, the cross table's ¶1 and the fifth takeaway.

## Key Takeaways — 286

Says: Five bullets.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Coherence is four axioms; VaR fails subadditivity on a few pairs here, ES never; variance ranks correctly under elliptical returns.
- ¶2 [takeaway] Rockafellar-Uryasev turns minimum ES into an LP solved exactly by `ROI`; modified ES is non-convex and reached only by search.
- ¶3 [takeaway] The ratio defaults differ by measure; `ROI` ignores `method`; `CSM` is unevaluated by search; `EQS` squares the gains.
- ¶4 [takeaway] Two frontiers, one curve, different `US_credit` weights both ways; a 5% tail misses a one-month skewness; only quadratic utility holds it in size.
- ¶5 [takeaway] Report by the measure optimized, show all on all; out of sample minimum ES realizes the higher shortfall; sixty months is three observations, thirty-six is two.
Note: ¶3 is four package traps in one bullet; ¶4 carries two findings and an inline number; the drawdown, lower-partial-moment and `CSM` measures of the theory have no bullet.

## Exercises — 211

Says: Four exercises.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Re-solve minimum ES at `p = 0.90` and `0.99`; tail sizes, `US_credit`, largest holding; why the LP is harder to trust as `p` rises.
- ¶2 [exercise] Rebuild the two frontiers on the weekly series; does the largest `US_credit` gap widen or narrow, and is it the estimator or the quantity that changed?
- ¶3 [exercise] Locate maximum STARR by scanning `mean / ES` as chapter 9 scanned for the tangency; compare with `maxSTARR = TRUE` and the tangency; which would the γ = 4 investor prefer?
- ¶4 [exercise] Run the modified-ES search with random portfolios and differential evolution at two budgets; relate the gaps to the fraction chapter 13 reports.
Note: Four against "around three"; ¶4 depends on `rp`, built inside the `CSM` callout.
