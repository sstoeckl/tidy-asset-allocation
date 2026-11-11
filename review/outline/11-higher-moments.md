---
file: chapters/11-higher-moments.qmd
title: Higher Moments
part: Portfolio Optimization
words: 7885
sections: 5
paragraphs: 59
---

# Chapter

Claim: On the sixteen classes the third and fourth moments move a γ = 5 investor out of credit and into government bonds, the direction the theory predicts, but the gain is a few basis points of certainty equivalent, smaller than the error an unpolished metaheuristic leaves and than the estimation uncertainty of the tensors; and the structured estimator that tames that uncertainty removes the very skewness the tensors were wanted for.
Question: What does an investor lose by describing an asset class with two moments when its returns are skewed and fat-tailed; cites Kraus–Litzenberger (1976) in the second sentence, Harvey–Siddique (2000) and Dittmar (2002) after it.
Why here: Declares itself strategic in chapter 3's sense; takes the expected-utility expansion and CRRA from chapter 3, the shape moments, Cornish–Fisher, expected shortfall and Jarque–Bera from chapter 4, the equity factor from chapter 5, the `momentFUN` route from chapters 6 and 7, the case for structure from chapter 7, the Kan–Zhou loss from chapter 8, the problem, tangency, minimum variance, frontier weights and block bootstrap from chapter 9, and expected shortfall as a risk measure from chapter 10; hands the solver shortfall to chapter 13, conditional dependence to chapter 19, the cost of estimation to chapters 26 and 28, and the convex solvers' moment behavior to appendix D. Why it sits between chapters 10 and 12 inside the part: not stated beyond taking expected shortfall from chapter 10.
Does: Compute coskewness and cokurtosis tensors and contract them to portfolio moments; fit the single-factor structured estimator and decompose what it drops; write a four-moment CRRA objective as a custom `PortfolioAnalytics` objective, supply tensors through `momentFUN`, and assert the objective was evaluated; polish a metaheuristic answer with `slsqp()` and price the solver error as a certainty equivalent; bootstrap a tensor element; measure tail dependence against a Gaussian copula.
Order: Opening with a worked case (credit's shape and its mean-variance weight), theory (expansion, tensors and their structure, CRRA, modified shortfall, copulas), implementation (sample tensors, structured estimator, moment interface, custom objective with two metaheuristics and a polishing box, modified shortfall under two estimators, conditional comoments), application (the shape picture, seven portfolios, bootstrap, tail dependence), takeaways, exercises. Deviations: the opening runs an optimizer and reads a weight before the theory; the implementation carries the chapter's first allocation finding (the shortfall comparison) and its verdict on the structured estimator, which the application re-reads; conditional comoments close the implementation without running and without a return; five takeaways, four exercises.

# Sections

## Opening (untitled) — 584

Says: The market prices skewness and kurtosis, a two-moment portfolio ignores them, and `US_credit` is the series on which the difference will show.
Why here: Contract position; the text says "the case for the chapter is one series" and recomputes its two numbers before the theory, so that the question becomes what changes once the optimizer sees more than volatility.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] What two moments miss on a skewed, fat-tailed class; Kraus–Litzenberger, Harvey–Siddique, Dittmar say the market prices it.
- ¶2 [method] Strategic in chapter 3's sense; the three steps: expand to four moments, implement, compare three investors.
- ¶3 [method] Data: the sixteen class series of chapter 2, in excess of the bill as chapter 9.
- (code: data)
- ¶4 [method] The case is one series: chapter 4 singled out `US_credit`; recompute its shape and its mean-variance weight.
- (code: credit-shape)
- ¶5 [result] Most negative skewness, near-highest kurtosis, yet the γ = 5 investor holds it; the optimizer sees volatility only.
Note: The "packages used" block is hidden (`include: false`), so the reader sees no package list. The opening solves a quadratic-utility problem and reads a weight before any theory, and promises the tangency and frontier comparison for the application.

## Expected Utility Beyond Two Moments — 1287

Says: Expected utility through four moments rewards skewness and penalizes kurtosis; the portfolio moments come from tensors too large to estimate freely, and even those tensors miss the tail dependence a copula carries.
Why here: Only the opening's sequence sentence ("first extend the expected-utility expansion ... and define the comoment tensors"); the section has no paragraph of its own.
Paragraphs: none of its own.
Note: Heading only; five subsections, the last three one paragraph each.

### The four-moment expansion — 297

Says: A fourth-order Taylor expansion of expected utility adds a skewness term and a kurtosis term whose signs economics fixes.
Why here: "Take the investor of eq-03-expected-utility": the expansion extends chapter 3's; eq-11-taylor is the objective the rest of the chapter solves, and its convergence argument is what the application's size finding returns to.
Paragraphs:
- ¶1 [derivation] Terminal wealth, central moments, the Taylor expansion through the fourth order; eq-11-taylor.
- ¶2 [evidence] Two terms is chapter 3; Markowitz, Samuelson, Levy–Markowitz on when that is close; not for credit's fourth moment.
- ¶3 [claim] Scott–Horvath fix the signs: skewness sought, kurtosis avoided; Jondeau–Rockinger, Athayde–Flôres, Mitton–Vorkink built on it.

### Coskewness and cokurtosis — 499

Says: Portfolio skewness and kurtosis are contractions of the coskewness and cokurtosis tensors, which carry thousands of parameters on sixteen assets, so a single-factor structure replaces them at the cost of the cross terms.
Why here: "The portfolio moments in eq-11-taylor are polynomials in the weights": the expansion needs the tensors; their size is what makes structure necessary, as chapter 7 found for the covariance; the implementation is promised to show the cross-term loss on credit.
Paragraphs:
- ¶1 [definition] Centered returns, M3 and M4 by Kronecker product, element indexing, the contractions; eq-11-tensors, eq-11-portfolio-moments; the representation PerformanceAnalytics uses.
- ¶2 [claim] The price is size: the number of distinct elements in Σ, M3 and M4.
- (code: parameter-count)
- ¶3 [definition] The counts against the months; Martellini–Ziemann's single-factor structure, eq-11-single-factor; Boudt's k-factor form; the cross terms it zeroes.
Note: ¶3 reads the count, defines the structured estimator and states its blind spot in one paragraph; ¶1 carries two numbered equations.

### The CRRA investor — 189

Says: Substituting CRRA derivatives into the expansion gives the objective the chapter codes, reported as a certainty equivalent.
Why here: "The utility function the rest of the literature uses, introduced in chapter 3"; the text says this is the objective "we write into PortfolioAnalytics below", and the certainty equivalent is needed to report it in return units.
Paragraphs:
- ¶1 [derivation] CRRA derivatives, eq-11-crra; truncated it is chapter 3's quadratic utility; Brandt, Jondeau–Rockinger, Harvey cited; eq-11-ce.
Note: One paragraph carries two numbered equations, four derivatives, three citations and the certainty-equivalent definition.

### The modified expected shortfall as a four-moment objective — 113

Says: The modified expected shortfall is a function of the same four moments, so the tensor estimator decides its minimum.
Why here: "The other four-moment objective, and the one PortfolioAnalytics uses most"; chapter 10 owns expected shortfall as a risk measure, so only its four-moment form is restated.
Paragraphs:
- ¶1 [definition] Favre–Galeano, Boudt: Cornish–Fisher quantile with the portfolio's own skewness and kurtosis; inputs are μ, Σ, M3, M4 and weights.

### Dependence that no moment describes — 182

Says: Comoments summarize a joint distribution; a copula is one, and lower-tail dependence is what correlation and a Gaussian copula cannot carry.
Why here: "Coskewness and cokurtosis summarize a joint distribution; they are not the joint distribution": the limit of the chapter's own objects; the cross terms the structure discards are called the shadow of this, and the application measures both on the same pairs.
Paragraphs:
- ¶1 [definition] Sklar's copula; tail dependence, eq-11-tail-dep; Embrechts on the Gaussian copula; Longin–Solnik, Ang–Chen, Patton on asymmetry.
Note: Five citations and a numbered equation in one paragraph; the subsection is the theory for the application's last subsection only.

## Comoment Tensors and Custom Objectives — 3199

Says: PortfolioAnalytics computes the tensors in one call and feeds them by name to any objective; the structured estimator removes most of credit's skewness, a custom CRRA objective needs a global name and a polishing step, and the minimum-shortfall answer depends on which tensors it is given.
Why here: Only the opening's sequence sentence ("then implement them in PortfolioAnalytics, including the structured estimator, the moment interface and a custom objective"); the section has no paragraph of its own.
Paragraphs: none of its own.
Note: Heading only; the longest section at six subsections and 26 of the chapter's 59 paragraphs, and the one that carries the chapter's first allocation finding (the shortfall comparison) and its verdict on the structured estimator.

### The sample tensors and their shape — 308

Says: `set.portfolio.moments()` returns the tensors a specification's objectives need, and their contraction reproduces the portfolio's own moments to machine precision.
Why here: The function that produces the tensors comes first; the text says the identity check is "the first thing to do with them".
Paragraphs:
- ¶1 [method] One call computes every moment the objectives need; which ones depends on the specification.
- (code: spec-moments)
- ¶2 [code] Variance gives `mu`, `sigma`; modified ES adds `m3`, `m4` from `M3.MM()`, `M4.MM()`; no dimnames; confirm the contraction.
- (code: tensor-identity)
- ¶3 [result] `portm3()`, `portm4()` agree with the series; the γ = 5 portfolio is more skewed than any equity market.

### The structured estimator — 741

Says: The single-factor fit loads on equities, and its tensors drop the cross terms that carry most of credit's skewness, so the estimator built to cut variance removes the feature the tensor was wanted for.
Why here: Needs the sample tensors to compare against; the theory promised that the implementation "shows that this is the case for credit"; the text says the finding "decides the allocation" in the application.
Paragraphs:
- ¶1 [method] `method = "boudt"` fits principal components and builds the tensors from eq-11-single-factor; the pieces are exported.
- (code: factor-fit)
- ¶2 [result] One factor, loading on equities as chapter 5 found; its variance share, credit's loading and residual share read.
- ¶3 [caveat] (callout) `k` is recovered by `match.call()`, so a variable in place of a literal fails with an odd message.
- (code: k-trap)
- ¶4 [caveat] (callout) Fit with `statistical.factor.model()`, where `k` is ordinary, and extract the tensors.
- ¶5 [method] One element shows the difference: a standardized coskewness triple and credit's own third moment.
- (code: triple)
- ¶6 [result] Structured own moment a fraction of the sample's; tensor-wide gap; the four-term identity the structure keeps two of.
- (code: tbl-11-decomposition)
- ¶7 [claim] Cross terms carry most of credit's skewness; a structure with independent residuals cannot hold it; the bias half of Martellini–Ziemann.
Note: The `match.call()` callout is the same package behavior chapter 6 measured for the Black–Litterman arguments; the text does not say so. ¶7 is the chapter's verdict on the estimator, delivered before the allocation that is said to depend on it.

### The moment interface — 350

Says: A custom `momentFUN` supplies all four moments, and the returned list reaches every objective by name under the metaheuristics only.
Why here: "The same argument carries the tensors" that chapters 6 and 7 used for the first two moments; a moment function of our own avoids passing `method` through `...`, "fragile for the reason the callout above gives"; the custom objective needs the contract stated here.
Paragraphs:
- ¶1 [method] `momentFUN` defaults to `set.portfolio.moments`; chapters 6 and 7 replaced it; the same route carries the tensors.
- (code: four-moments-fun)
- ¶2 [caveat] The contract: called once, list matched to objective formals by name, missing names fail late, convex solvers read two.
Note: ¶2 is one dense paragraph that states the whole calling contract and its failure mode; nothing later in the chapter exercises the failure.

### A custom objective: the CRRA investor — 1089

Says: A function named in `add.objective()` becomes the objective; it must be visible from the global environment, the two metaheuristics reach its neighborhood only, and a local solver started from either finishes the job.
Why here: "PortfolioAnalytics has no expected-utility objective beyond the quadratic one", so eq-11-crra is written by hand; needs the contract of the previous subsection. Why the two solver routes and the polishing box sit here rather than in a subsection of their own: not stated.
Paragraphs:
- ¶1 [method] Any function by name; returns the negative of eq-11-crra; an `order` argument truncates it for comparison.
- (code: crra-fun)
- ¶2 [caveat] (callout) `match.fun()` from the solver's frame misses a function defined in `local()`; the objective is skipped, weights returned without a value.
- (code: hidden-objective)
- ¶3 [method] (callout) Put the function in the global environment and assert after every solve that it was evaluated.
- (code: expose-objective)
- ¶4 [caveat] (callout) `momentFUN` is unaffected: resolved once from the caller's frame, and a function object can be passed.
- ¶5 [method] Differential evolution, Storn–Price and Ardia; population from `search_size`, `itermax`; the solver prints, so output is hidden.
- (code: crra-deoptim) results hidden
- (code: crra-deoptim-out)
- ¶6 [method] The random-portfolio route; `simplex` is fast; one candidate set reused so comparisons share candidates.
- (code: crra-random)
- ¶7 [result] Neither route converged; smooth objective on a simplex, so a local solver finishes; two starts agreeing is the evidence.
- ¶8 [method] (callout, collapsed) Worked: `nloptr::slsqp()` with bounds and the budget equality; a wrapper closes over the moments.
- (code: polish)
- ¶9 [method] (callout) Two checks: the polished two-moment optimum must match ROI's; the four-moment optimum from both starts must coincide.
- (code: polish-check)
- ¶10 [result] (callout) DEoptim sits basis points of certainty equivalent below the polished answer; on a flat objective solver error exceeds the effect.
Note: The candidate set `rp` that every later random-portfolio solve reuses is drawn inside the callout that demonstrates the hidden-objective trap, and the collapsed box defines `polish()`, `turnover()` and `ce_annual()`, which the next subsection and the whole application depend on; a reader who skips both boxes loses the chapter's machinery. The title names the objective; the weight of the subsection is the solvers.

### One objective, two estimators of the tensors — 521

Says: Minimum modified shortfall holds no credit under the sample tensors and buys it under the structured ones, and on the realized tail the structured answer is the worse of the two.
Why here: The theory said the modified shortfall's minimum "depends on which tensors it is given"; needs both estimators from the structured subsection and `rp` and `polish()` from the one before; its table is re-read in the application.
Paragraphs:
- ¶1 [method] Minimize the modified shortfall twice on the same candidates, sample and structured tensors, and polish both.
- (code: mes-two-estimators)
- (code: tbl-11-mes)
- ¶2 [result] Sample tensors: credit out, near minimum variance; structured: credit in, worse realized tail; biased estimator, not shrinkage; solver message deferred.
Note: ¶2 does three jobs: reads the table, pronounces the chapter's verdict on the structured estimator, and dismisses a package message in its last sentence. The minimum-variance portfolio the application compares against is built in this chunk.

### Conditional comoments — 183

Says: `CCCgarch.MM()` returns conditional moments under the same four names, with a silent fallback to unconditional volatility for low-`alpha1` series.
Why here: "Everything above is unconditional", stated as the contrast; why it closes the implementation, or belongs in a chapter declared strategic: not stated. Points to chapter 19.
Paragraphs:
- ¶1 [method] CCC-GARCH of Bollerslev: GARCH(1,1) per series, constant correlation, rescaled residual tensors; Jondeau–Rockinger, Guidolin–Timmermann; `fGarch` absent, so not run.
- (code: ccc-garch) not run
- ¶2 [caveat] Same names, drops into `momentFUN`; a series with `alpha1` below 0.01 silently gets its unconditional volatility.
Note: The only subsection whose code does not execute; nothing later uses it, and the application does not return to conditional moments.

## What the Third and Fourth Moments Buy — 2329 (277 before the subsections)

Says: On the sixteen classes the four-moment investor moves out of credit into government bonds, as the theory predicts, for a gain of a few basis points; the tensors behind the move leave a single element's sign open, and the tail dependence they shadow is measured directly.
Why here: "The application opens with the picture", the house rule; the opening's last step ("compare on the sixteen classes what a two-moment investor, a four-moment investor and a minimum-modified-shortfall investor hold").
Paragraphs:
- ¶1 [transition] The application opens with the picture: the sixteen series in the plane eq-11-taylor cares about.
- (code: fig-11-shape)
- ¶2 [result] Chapter 4's rejections are not of one kind: equities near the Gaussian origin, credit far out, where eq-11-crra has work.
Note: ¶1 is one sentence announcing the figure.

### Three investors and what they hold — 1180

Says: At γ = 5 the four-moment investor hands credit's weight to government bonds, improves skewness and the realized tail, and gains a few basis points, less than the unpolished solver had lost.
Why here: After the picture; the opening promised to return to the tangency portfolio and the middle of the frontier here; the four-moment optimum is rebuilt by multi-start polishing and asserted equal to the implementation's answer.
Paragraphs:
- ¶1 [method] Seven portfolios: chapter 9's tangency, quadratic utility at two γ, four moments at both, the two shortfall minima.
- (code: tangency)
- ¶2 [result] The tangency holds a trace of credit; chapter 9's frontier showed it peaking mid-frontier, where γ = 5 sits.
- (code: four-moment-optima)
- (code: tbl-11-portfolios)
- (code: fig-11-weights)
- ¶3 [result] By pairs: credit out, government in, at both γ; skewness and historical shortfall improve; the chapter's message on direction.
- ¶4 [claim] Size: a few basis points, Levy–Markowitz restated; less than the DEoptim error; the shortfall investor re-read from tbl-11-mes.
Note: The title says three investors; the table holds seven portfolios. ¶3 and ¶4 carry the chapter's two findings, direction and size; ¶4 ends by re-reading the implementation's shortfall table rather than adding to it. Three chunks run between ¶2 and ¶3 with no prose, and the first of them, `four-moment-optima`, is what makes the application's numbers independent of the metaheuristics; nothing in the prose says so.

### What the tensors are estimated from — 355

Says: A block bootstrap leaves the portfolio's skewness negative throughout but leaves the sign of a single coskewness element undetermined, which is why the structured estimator exists.
Why here: "Every tensor above was estimated on" the one sample, and chapter 4 found rolling skewness unstable; the precision question follows the allocation it qualifies; uses chapter 9's bootstrap; sends the four-moment investor on to chapters 8, 26 and 28.
Paragraphs:
- ¶1 [method] Chapter 4's sign flips; chapter 9's twelve-month block bootstrap on the γ = 5 quadratic-utility portfolio.
- (code: bootstrap)
- ¶2 [result] Skewness interval wide but negative; one element's sign open; the structured bias therefore a trade; chapter 8 at its limit.
Note: ¶2 softens the implementation's verdict ("a different estimator, biased") into "a trade rather than a defect" that Martellini–Ziemann say wins out of sample; the chapter holds both readings, and the takeaways carry only the first.

### Dependence the tensors are a shadow of — 517

Says: Three pairs show more joint months in the lower tail than a Gaussian copula allows, two of them asymmetric, and credit with government bonds is the most tail-dependent pair at a modest correlation.
Why here: "tbl-11-decomposition traced the skewness of credit to the co-movement of its residual with the factor"; eq-11-tail-dep measures that directly; closes the thread the theory's last subsection opened; hands the time-series view to chapter 19.
Paragraphs:
- ¶1 [method] Ranks with `copula::pobs()`, joint worst-decile counts, the Gaussian benchmark, a t copula fitted for its degrees of freedom.
- (code: tail-dependence)
- ¶2 [result] Two pairs asymmetric, equity–credit symmetric; every pair above Gaussian; credit–government the heaviest tail; modeling it is beyond the strategic setting.
Note: The subsection measures what the chapter's own objects cannot, and ends by declaring the remedy out of scope.

## Key Takeaways — 262

Says: Five bullets.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Four moments reward skewness and penalize kurtosis with Scott–Horvath's signs; `portm3()`, `portm4()` contract the tensors.
- ¶2 [takeaway] Thousands of parameters; the single-factor structure cuts them and removes most of credit's skewness through the cross terms.
- ¶3 [takeaway] A custom objective is a named function fed by name, visible globally, skipped silently otherwise; assert it ran.
- ¶4 [takeaway] Metaheuristics find the neighborhood; the DEoptim gap exceeded the effect; a local solver is part of the method.
- ¶5 [takeaway] Credit to government bonds, worth a few basis points; direction as theory, size as Levy–Markowitz; a single element's sign open.
Note: Five, on contract; ¶3 and ¶4 are package and solver lessons rather than chapter claims. The shortfall comparison (tbl-11-mes) and the tail-dependence measurement have no bullet.

## Exercises — 224

Says: Four exercises.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Three-asset equal weights: skewness from the tensor, split into own and cross terms; compare with chapter 4's exercise.
- ¶2 [exercise] Four-moment and quadratic optima at four values of γ; tabulate the credit weight and the gain; why not monotone.
- ¶3 [exercise] Refit with two and three factors; does the shortfall minimum's credit weight approach the sample answer; which term is unrecoverable.
- ¶4 [exercise] Lower-tail exceedance of credit against government for all five regions against the Gaussian; does the ranking follow correlation.
Note: Four against "around three"; ¶4 extends to five regions a pair the chapter measured for one.
