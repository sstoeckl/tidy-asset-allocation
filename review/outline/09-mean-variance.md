---
file: chapters/09-mean-variance.qmd
title: Mean-Variance Optimization
part: Portfolio Optimization
words: 10239
sections: 5
paragraphs: 101
---

# Chapter

Claim: The textbook frontier on the sixteen series is a sequence of quadratic programs whose left end is set by the least volatile asset rather than by diversification, whose right end moves several times as far as the left when the sample is resampled, and whose tangency portfolio keeps the smallest share of its promised Sharpe ratio out of sample while minimum variance, which needs no μ, keeps the most.
Question: How should an investor divide wealth across assets that differ in expected return, volatility and comovement; @markowitz1952.
Why here: Says Markowitz is the point every later method departs from; needs the sixteen series of chapters 2 and 4, the excess basis and dominance vocabulary of chapter 3, the factor finding of chapter 5, the rolling moments of chapter 4 and the estimated inputs of chapters 6 and 7 (chapter 8, on estimation error, is never cited); chapter 10 changes the risk measure, 11 adds moments, 12 prices constraints, 13 the solvers, 15 shrinkage and universe choice, 23 the turnover, 25 the honest out-of-sample version, Part VIII the robust formulations.
Does: Specify and solve minimum-variance, tangency and quadratic-utility problems with a guarded solver call, draw frontier, weights and capital allocation line from one data frame, and test a frontier for stability, source of volatility reduction, constraint cost and out-of-sample record.
Order: Opening, theory in two subsections (one carrying a twelve-paragraph worked callout), implementation in five, application in seven, Key Takeaways, Exercises; the headings keep the contract, but the implementation already reads results (the dominance count, the US_credit asymmetry), the application is half the chapter and runs five experiments on the frontier rather than showing it, and there are six takeaways and five exercises.

# Sections

## Opening, before the first section — 311

Says: The question, the strategic label, the full-sample warning, and the data in excess of the bill.
Why here: Contract position; states the chapter's order (derive, implement, ask what was bought and what survives).
Paragraphs:
- (code: setup)
- ¶1 [claim] Markowitz: a portfolio is judged by covariances, not asset by asset; the point every later method departs from.
- ¶2 [method] Strategic allocation; derive the problem and two anchors, implement on sixteen series, ask what survives unseen data.
- ¶3 [caveat] Every moment is full-sample; descriptive, not implementable; chapter 25 does the honest version.
- ¶4 [method] Sixteen series of chapter 2 in excess of the bill, for chapter 3's reasons; the package has no rate argument.
- (code: data)

## The Mean-Variance Problem — 1647

Says: Portfolio variance carries the covariances, dominance gives the frontier a direction, and the problem has two closed-form anchors and a closed-form frontier that vanish under a short-sale constraint and mislead once the inputs are estimates.
Why here: The opening puts derivation first; says the dominance vocabulary is applied in the implementation before any optimizer runs; its last paragraph hands the rest of the chapter to implementation and application.
Paragraphs:
- ¶1 [definition] Symbols w, μ, Σ, ι; portfolio mean and variance (eq-09-moments).
- ¶2 [claim] The variance line is Markowitz; off-diagonals enter and can be negative; a portfolio can undercut every constituent.
- ¶3 [definition] Dominance in the plane, from chapter 3; northwest rule; efficient; applies to single assets, implementation does so.
- ¶4 [definition] For each target return, the least-variance fully invested portfolio (eq-09-problem).
- ¶5 [definition] Traced over targets: the minimum-variance frontier; upper branch efficient, lower branch never chosen.
Note: ¶3 restates chapter 3's definition in full before the problem is posed, as the house rule asks.

### Two anchors with closed forms — 1069

Says: Minimum variance needs no μ, the tangency portfolio is Tobin's single risky fund with the highest Sharpe ratio, and Merton's constants give the whole frontier.
Why here: Drops the return constraint from the problem just posed; says μ's absence will do much work later; the two-asset callout follows the formula it reduces; the tangency and the frontier need the risk-free asset Tobin adds.
Paragraphs:
- ¶1 [derivation] Dropping the return constraint gives the minimum-variance portfolio (eq-09-gmv).
- ¶2 [claim] μ is absent; the one frontier point needing no return view; will do work later.
- ¶3 [derivation] (callout, collapsed) With two assets the formula collapses to a scalar expression (eq-09-two-asset).
- ¶4 [example] (callout) US_equity and US_government, one volatile and one not; their annualized sample moments.
- (code: two-asset-inputs)
- ¶5 [example] (callout) Moments substituted into the weight formula, then into the portfolio volatility.
- ¶6 [method] (callout) The same arithmetic in code, so the numbers are computed, not typed.
- (code: two-asset-weights)
- ¶7 [result] (callout) Portfolio volatility below either asset; diversification in one number; the cross term subtracts.
- ¶8 [method] (callout) Vary the correlation with both volatilities fixed.
- (code: two-asset-rho)
- ¶9 [result] (callout) At ρ = ±1 volatility is zero, short at +1; benefit shrinks as ρ rises; measured ρ leaves little.
- ¶10 [claim] (callout) Two lessons: a singular Σ gives a zero-variance combination (eq-07-riskless); the closed form shorts, here as on sixteen.
- ¶11 [method] (callout) Scalar and matrix formula must agree.
- (code: two-asset-check)
- ¶12 [caveat] (callout) The stopifnot() guards against drift and fails the render.
- ¶13 [derivation] Tobin: with a risk-free asset every efficient portfolio mixes it with one risky fund, the tangency portfolio (eq-09-tangency).
- ¶14 [evidence] Highest Sharpe ratio (Sharpe 1966); lets Sharpe 1964 reach equilibrium; Roll 1977 on identifying it.
- ¶15 [derivation] Merton's A, B, C give the frontier (eq-09-frontier); vertex 1/A; maximum Sharpe √C; proofs in appendix B.
Note: The callout sits between the two anchors the title promises, so the tangency portfolio arrives twelve paragraphs after the first; ¶10 reads a sixteen-asset number before the implementation has begun.

### Why the closed forms are not what we compute — 236

Says: A short-sale constraint turns the problem into a convex quadratic program, and estimated inputs make the closed forms error-maximizers.
Why here: Says every expression above assumed unconstrained weights; frames the rest: compute the textbook answer in the implementation, measure how much is real in the application.
Paragraphs:
- ¶1 [claim] Short-sale constraint removes the closed form; a convex QP solved in milliseconds (Boyd); chapter 13 for machinery.
- ¶2 [evidence] μ and Σ are estimates (chapters 6, 7); Jobson–Korkie, Best–Grauer's mechanism, Chopra–Ziemba's price, Michaud's error-maximizer.
- ¶3 [transition] That literature frames the chapter: compute, then measure.

## Implementation — 2943

Says: Once the inputs have been looked at, each anchor is four lines in PortfolioAnalytics, the tangency is read off a computed frontier, and the solve fails silently in enough ways to need a guard.
Why here: The theory's last paragraph says the textbook answer is computed here; the frontier, the anchors and solve_checked() built here are what the application reuses.
Paragraphs: none outside the subsections.
Note: Five subsections; the dominance picture the house rule places at the head of the application sits in the first, and the chapter's first finding (the US_credit asymmetry) is read in the third.

### Looking at the inputs first — 699

Says: The inputs are lopsided in volatility and correlation, the two averages differ by less than the drag, and most of the sixteen series are dominated before any optimizer runs.
Why here: Says the lopsidedness is worth seeing before any optimizer runs; the theory promised the dominance count here; says the application returns to the spread and the correlation.
Paragraphs:
- ¶1 [method] Two numbers per asset, one per pair; lopsided; see how lopsided first.
- (code: moments)
- ¶2 [result] Volatility spread and mean pairwise correlation; both constrain the frontier; the application returns to them.
- ¶3 [claim] Arithmetic mean enters μ, compounded is what is earned; the gap falls short of half the variance; top series' numbers.
- (code: tbl-09-drag)
- ¶4 [definition] Diagnostic: how many assets could be held; dominated in sample defined.
- (code: dominance)
- (code: dominance-count)
- ¶5 [result] How many are dominated, by whom most; the efficient set; a sample statement, visible without an optimizer.
- (code: fig-09-mu-sigma)
Note: The moments, the table and the figure are on total returns R while every solve uses excess returns Re, and the text does not say so; ¶3 reopens chapter 3's drag; ¶4 defines dominance a second time after the theory's ¶3; the figure follows the prose that reads it.

### Specifying and solving the problem — 330

Says: Minimum variance under long-only holds few series and most of one, and that concentration is a property of the problem, not a symptom of bad inputs.
Why here: First anchor, first solve; the explanation of the concentration reads the least and second-least volatile series from the inputs just tabulated.
Paragraphs:
- ¶1 [method] Specification separated from solution; portfolio.spec() collects, optimize.portfolio() solves; minimum variance in four lines.
- (code: spec)
- (code: portfolio-stats)
- ¶2 [result] Few series held, most in one; because the least volatile series sits far below the next.
- ¶3 [evidence] Concentration is not bad estimates: Green–Hollifield's common factor, which chapter 5 found; Clarke et al. on few names.

### The tangency portfolio — 995

Says: The tangency portfolio is read off a computed frontier, sits far above 60/40 in sample, and is where US_credit, the most negatively skewed series, enters a frontier whose objective cannot see the asymmetry.
Why here: Second anchor; says the portable route is to compute the frontier and read the best point, which is why the frontier is built here and reused by every later figure; says two things matter later.
Paragraphs:
- ¶1 [method] Ray touches frontier; maxSR = TRUE exists, "the callout below" says why not; compute the frontier, read the best point.
- (code: tangency)
- (code: tbl-09-anchors)
- (code: frontier-facts)
- ¶2 [result] Tangency Sharpe above 60/40, in sample; US_credit enters at the tangency and grows rightward; one month's skewness; chapters 10, 11.
- ¶3 [method] (callout, collapsed) Evaluate the closed form with Merton's constants and compare.
- (code: closed-form-gmv)
- ¶4 [result] (callout) The closed form shorts several series, most heavily one; the solver could not; that is the whole difference.
- (code: closed-form-compare)
- ¶5 [result] (callout) Unconstrained volatility genuinely lower, via many positions and shorts; Michaud named, Jagannathan–Ma showed the constraint suppresses.
- ¶6 [method] (callout) Check the vertex identity and the maximum Sharpe ratio against √C.
- (code: closed-form-identities)
- ¶7 [result] (callout) Vertex agrees to machine precision; Sharpe does not; the gap is the long-only cost at the tangency.
Note: ¶1 promises a callout on maxSR that no callout in the chapter gives; ¶2 carries the chapter's first finding and two forward references inside the implementation; the hidden frontier-facts chunk asserts what ¶2 says; the closed-form callout is what exercise 2 asks for.

### Three ways this fails without an error — 762

Says: A metaheuristic approximates the quadratic program, a wrong second solver name returns a weightless shell, an exact budget is reported infeasible on CRAN, and a target on the return objective is dropped under CVXR.
Why here: Not stated; follows the first solves; says the guard belongs in anything that solves more than once, which the bootstrap and chapter 25 are.
Paragraphs:
- ¶1 [claim] Each failure returns an object that looks solved.
- ¶2 [caveat] (callout, warning) DEoptim in published examples approximates a QP; chapter 13 measures it; use ROI unless non-convex.
- ¶3 [caveat] Second failure: the two-element optimize_method vector is not read as it looks.
- (code: unlabelled excerpt of optimize.portfolio(), not run)
- ¶4 [caveat] First element discarded; dispatch on the second against a hard-coded list.
- (code: cvxr-whitelist)
- ¶5 [caveat] CLARABEL is installed, CVXR's default, and not listed; asking raises nothing.
- (code: silent-failure)
- ¶6 [caveat] A shell with a class and no weights; a NULL period in a loop (chapter 25); the guard belongs everywhere.
- (code: solve-checked)
- ¶7 [caveat] (callout, important) On CRAN an exact budget is two dependent rows; quadprog says infeasible; 30 of 312 windows; fix in appendix D.
- ¶8 [caveat] Third failure: a return target on the constraint or on the objective; backends disagree.
- (code: target-trap)
- ¶9 [caveat] ROI honors the objective's target; CVXR drops it on a direct call and solves quadratic utility; use the constraint.
Note: The heading counts three and the text walks four (the warning callout, solver names, the budget callout, targets); the budget callout calls itself "a second failure", and the first failure has no numbered place in the sequence.

### The package's own frontier chart — 154

Says: chart.EfficientFrontier() draws the whole picture in one line and locates the tangency by scanning, but two defaults (rf = 0, match.col = "ES") must be known.
Why here: Not stated; closes the implementation with the one-line version of the picture the application then rebuilds by hand.
Paragraphs:
- ¶1 [code] One call draws frontier, assets, line and tangency; tangency by highest Sharpe, not maxSR.
- (code: fig-09-native-frontier)
- ¶2 [caveat] rf = 0 is the default, harmless here, wrong elsewhere; match.col defaults to ES, so pass StdDev.

## What the Frontier Actually Buys — 4889

Says: The frontier is a set of separate answers whose weights show where each asset enters and leaves; its right end is poorly determined, its left end is set by the least volatile asset rather than by diversification, each constraint costs where the unconstrained answer was absurd, and out of sample the tangency portfolio keeps least.
Why here: The theory's last paragraph says the application measures how much of the textbook answer is real; the last subsection hands the gap between in sample and out of sample to the rest of the book.
Paragraphs: none outside the subsections.
Note: Seven subsections, half the chapter; the first two show the frontier and the last five are experiments on it (resampling, two universes, five hundred universes, a constraint ladder, the register), each with its own method, code and result.

### The frontier is a set of answers, not an object — 1093

Says: Each frontier point is its own quadratic program, and the quadratic-utility diamonds, the capital allocation line through the origin and the scanned tangency are the three places the picture goes wrong.
Why here: Opens the application with the whole picture; says each element is computed because none is as obvious as the theory makes it look; the frontier and the anchors come from the implementation.
Paragraphs:
- ¶1 [claim] No single problem has the frontier as its solution; as many problems as points.
- ¶2 [method] Frontier from create.EfficientFrontier(), tangency read off it, utility from risk_aversion, no CAL function; compute each.
- (code: utility-portfolios)
- ¶3 [result] Raising risk_aversion walks leftward; appendix B's statement made numerically; monotone.
- (code: allocation-line)
- ¶4 [method] Every point into one data frame; parallel vectors mismatch; a mistake this chapter made.
- (code: frontier-points)
- (code: fig-09-frontier)
- ¶5 [claim] Three things worth stating, each easy in theory and not in implementation.
- ¶6 [claim] Diamonds lie on the frontier; the check that the objective was specified correctly.
- ¶7 [caveat] The line passes through the origin because returns are excess; total returns move the tangent; the commonest error.
- ¶8 [claim] Tangency found by scanning; maxSR = TRUE is unreliable, "the implementation's subject".
- ¶9 [method] (callout, collapsed) The same portfolios asked for several ways coincide; confirming it guards against misspecification.
- (code: equivalences)
- ¶10 [result] (callout) The gap column is the diagnostic; fourth-decimal values are discretization.
Note: ¶5 announces and does no work; ¶8 makes the maxSR point for the third time and points to an explanation the implementation does not contain; the callout's title promises four ways of asking and its table compares two (quadratic utility against the frontier at equal volatility); ¶2 repeats the "read it off" point of the tangency subsection.

### Reading the frontier through its weights — 591

Says: The weights show which assets enter, swell and leave, and the long-only frontier's right end is always one asset.
Why here: Says the frontier figure shows where the answers landed but not why, and the why is in the weights.
Paragraphs:
- ¶1 [method] Plot the whole weight vector against the target to see who enters, leaves and gives up.
- (code: fig-09-ef-weights)
- ¶2 [result] US_government at the left; US_equity and US_credit swell through the middle; one series at the right, a corner solution.
- (code: frontier-corner)
- ¶3 [code] The package draws this too, in one line.
- (code: fig-09-ef-weights-native)
- ¶4 [method] (callout, collapsed) Over what range of risk is each asset held.
- (code: entry-exit)
- ¶5 [result] (callout) Narrow bands; several series never held, dominance in weights; peak weights concentrate at both ends.
Note: ¶3 is one sentence introducing a figure; the corner-solution chunk follows the prose that states it.

### The left end is stable and the right end is not — 519

Says: Resampling the sample in twelve-month blocks moves the tangency portfolio several times as far as the minimum-variance portfolio, because the right end depends on μ.
Why here: Picks up the theory's promise that μ's absence from the minimum-variance portfolio would do work later; needs chapter 4's rolling moments and solve_checked() from the implementation.
Paragraphs:
- ¶1 [claim] Left end depends on Σ, right end on μ; means are estimated worse (chapter 4); Best–Grauer; a resampling test.
- ¶2 [method] Block bootstrap, twelve-month blocks (Künsch, Politis–Romano); re-optimize; measure distance from the full-sample answer.
- (code: bootstrap)
- (code: tbl-09-bootstrap)
- ¶3 [result] Tangency moves several times as far; worst twentieth asks a large trade; minimum variance never exceeds a small one.
- ¶4 [claim] Only the sample changed; less determined, not more aggressive; chapter 23 prices turnover; Michaud; chapter 15 and Part VIII.

### Diversification effort and diversification payoff are unrelated — 698

Says: The equity-only minimum-variance portfolio holds more effective positions and buys a smaller discount than the mixed one, and the non-equity series add only a floor.
Why here: Not stated; questions the other property of the minimum-variance portfolio, its low volatility, after its stability.
Paragraphs:
- ¶1 [claim] Tempting to credit diversification; mostly it is not.
- ¶2 [method] Same construction on a heterogeneous and a homogeneous universe: sixteen classes, five equities.
- (code: diversification)
- ¶3 [definition] Effective bets: reciprocal Herfindahl; the simplest concentration measure (Choueifaty–Coignard, Meucci).
- ¶4 [result] Correlations far apart; few effective positions across classes because of US_government; more among equities.
- ¶5 [result] Discounts below the least volatile constituent; the portfolio with more positions buys the smaller discount.
- (code: fig-09-two-frontiers)
- ¶6 [result] Both frontiers end in the same equity market; the non-equity series extend the frontier leftward only.
Note: ¶3 defines effective bets after the chunk computes it; the chunk's comment carries the definition first.

### Five hundred universes, one constant — 400

Says: Across random sub-universes the least volatile asset explains almost all of the minimum-variance level and correlation almost none, so the universe fixes the answer before the optimizer runs.
Why here: Says two universes are suggestive and no more; the pattern must hold on universes nobody designed.
Paragraphs:
- ¶1 [method] If the level is set by what is available, it should hold on undesigned universes.
- (code: subuniverses)
- ¶2 [result] Median, smallest and largest discount; the discount depends on selection, the level's source does not.
- ¶3 [method] Which input decides the level.
- (code: what-explains-it)
- ¶4 [result] The least volatile asset's R²; correlation's; all three together.
- ¶5 [claim] The free lunch is not the combining; the universe fixes the ceiling; first argument for universe choice; chapter 15.
Note: ¶3 is a one-line question introducing a chunk.

### What each constraint costs — 822

Says: Each rung of a four-step constraint ladder moves the frontier south-east, and the cap and the group limits cost mainly where the long-only answer was one position.
Why here: Not stated; reuses the frontier machinery; says the last observation is chapter 12's argument in one picture.
Paragraphs:
- ¶1 [method] A mandate is a sequence of restrictions; run the problem four times to see each cost.
- (code: constraint-ladder)
- (code: tbl-09-ladder)
- (code: fig-09-ladder)
- ¶2 [result] Shorting lowers the left end; the cap costs both ends; group limits cost little, nothing at best Sharpe, bind right.
- ¶3 [claim] Chapter 12's argument in one picture; a constraint that binds where the answer was absurd costs little; Jagannathan–Ma.
Note: Three chunks run between the method and the result; the hidden assertions in the table chunk carry the facts ¶2 reads.

### And it does not survive contact with the future — 759

Says: On the sixty-month register the tangency portfolio keeps the smallest share of its promised Sharpe ratio and finishes last of the three, minimum variance leads in every cell, and the order against equal weighting depends on the window.
Why here: Says everything above is in sample; reads the out-of-sample column from chapter 25's register so the two chapters cannot drift; closes by handing the gap to the rest of the book.
Paragraphs:
- ¶1 [method] Same portfolios on a sixty-month rolling window, monthly rebalanced; the column is read from chapter 25's register.
- (code: tbl-09-oos)
- (code: oos-ranking)
- ¶2 [result] Shares kept by each; above 100% possible, the record starts in model year 11; the rule estimating the mean fails.
- ¶3 [evidence] At 120 months tangency passes equal weight; every cell: minimum variance leads, tangency keeps least; DeMiguel et al., Jagannathan–Ma.
- ¶4 [transition] At sixty months the chapter's best portfolio is last in chapter 25's register; the gap is the book's subject.
Note: ¶1 states the result before the table; the hidden oos-ranking chunk asserts the register facts ¶3 reads.

## Key Takeaways — 220

Says: Six bullets: the quadratic program, the μ-free anchor, concentration, the two ends, the universe, the out-of-sample record.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Closed form only unconstrained; a short-sale constraint makes a quadratic program.
- ¶2 [takeaway] Minimum variance has no μ; no forecast needed; far more stable than tangency.
- ¶3 [takeaway] Concentration is not a symptom; a dominant factor produces it with perfect inputs (Green–Hollifield, Clarke).
- ¶4 [takeaway] Left end Σ, right end μ; the bootstrap moves tangency several times as far.
- ¶5 [takeaway] The level is set by the least volatile asset; universe selection over weighting machinery.
- ¶6 [takeaway] In sample tangency first; out of sample it keeps least; behind equal weight at 60 months, not 120 (DeMiguel, Jagannathan–Ma).
Note: Six against "around five"; nothing on the silent failures, the solve guard or the constraint ladder.

## Exercises — 199

Says: Five exercises: money markets in the universe, the closed form against ROI, block length, the budget encoding, US_credit's asymmetry.
Why here: Contract position; each reuses an object or table of the chapter by name.
Paragraphs:
- ¶1 [exercise] Add the five money markets and recompute the anchors; what near-cash does to variance minimization.
- ¶2 [exercise] Compute the closed form, compare with ROI; which constraint and which assets account for the difference.
- ¶3 [exercise] Rerun the bootstrap with blocks of 1, 3 and 24 months; which looks most stable and why.
- ¶4 [exercise] weight_sum bounded 0.99–1.01 against exactly one on every rolling window; count failures.
- ¶5 [exercise] US_credit's skewness and worst month; would a loss-averse investor hold it; chapter 10 answers.
Note: Five against "around three"; exercise 2 is the collapsed closed-form callout of the tangency subsection, already worked and read there.
