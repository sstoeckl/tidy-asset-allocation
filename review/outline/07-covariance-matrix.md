---
file: chapters/07-covariance-matrix.qmd
title: The Covariance Matrix
part: Estimating the Inputs
words: 5002
sections: 5
paragraphs: 58
---

# Chapter

Claim: On more assets than observations the sample covariance matrix is singular by arithmetic; of the four replacements, shrinkage is the one that always runs but earns nothing once the window is long, and the long-only constraint was already doing comparable work.
Question: Why the lowest-risk combination of 123 equities cannot be obtained from the monthly history available; @michaud1989 for the consequence and @chopra1993 for its price.
Why here: Needs the sixteen classes of chapter 4, the factor models of chapter 5, chapter 6's ranking of input errors, the bond block of chapter 2, and the frontier of chapter 9, which lies ahead; sends forward to chapter 8 (method or sample), 15, 17, 19, 21, 28, 10 and appendix D. Stated twice: @chopra1993's ranking makes chapter 6 harder "and this one unavoidable", and the theory section closes by saying class-level allocation never needed it and the equity sleeve will.
Does: Diagnose a singular or ill-conditioned covariance matrix before the solver does, build a factor, shrunk or robust estimate, pass it to `optimize.portfolio()` through `momentFUN`, and score estimators out of sample.
Order: Theory (requirement, singularity, diagnosis, why now), implementation (four routes by cost, the moment-function plumbing, patching, robust estimation), application (out-of-sample race, Sharpe versus volatility with the spectrum, regime dependence of the target, long only as shrinkage), seven takeaways, four exercises; deviations: route four is split around two other subsections, the application heading carries no prose of its own, and the spectrum, the application's named subject, sits inside the Sharpe subsection.

# Sections

## (opening) — 240

Says: The most modest request of an optimizer, the lowest-risk combination of an equity sleeve, cannot be met because the matrix it needs is singular on a realistic universe.
Why here: the opening by contract; its ¶3 lays out the chapter's order (requirement, four responses by cost, out-of-sample payoff).
Paragraphs:
- (code: setup)
- ¶1 [example] An equity sleeve of 123 names and 31 model years of monthly returns; the request is only the lowest-risk combination.
- ¶2 [claim] The request cannot be met: on a realistic universe the sample matrix is singular, and singular means meaningless; @michaud1989, @chopra1993.
- ¶3 [method] The plan: why the requirement fails, four responses by cost, which pays out of sample; the answer is unflattering.
- (code: data)
Note: ¶1 defines the request as the low-volatility end of chapter 9's frontier, a chapter that comes later.

## What the Optimizer Requires — 999

Says: The optimizer's only input is Σ, whose sample estimate has rank at most min(N, T−1), so with more assets than observations it is singular whatever the data.
Why here: stated in the opening's plan: first what the optimizer asks for and why the request cannot be met.
Paragraphs:
- ¶1 [definition] Minimum variance minimizes w'Σw; the matrix is the optimizer's entire input, nothing else about the assets enters.
- ¶2 [definition] A symmetric Σ holds N(N+1)/2 numbers, estimated from T observations by the sample formula (eq-07-sample).
- ¶3 [derivation] A sum of T rank-one outer products has rank at most min(N, T−1) (eq-07-rank).
- ¶4 [claim] With N > T−1 the estimate is singular whatever the data; arithmetic, not a property of markets.
- ¶5 [evidence] Sixteen classes need 136 numbers; 123 equities need thousands from 372 months, more parameters than observations.

### What singularity claims about portfolios — 316

Says: A singular estimate asserts a riskless long-short portfolio, which a minimizer will hold; short of singularity the condition number says how far sampling error is magnified into the weights.
Why here: stated: eq-07-rank is a statement about a matrix, this subsection turns it into a statement about money.
Paragraphs:
- ¶1 [derivation] A singular estimate admits a non-zero portfolio with zero variance (eq-07-riskless); a minimizer finds it and holds it.
- ¶2 [claim] Such portfolios are long-short cancellations peculiar to the estimation months; @michaud1989's "error maximizer" is exact.
- ¶3 [definition] Short of singularity the condition number (eq-07-condition) governs error magnification; the smallest eigenvalues are noise, @laloux1999, @marchenko1967.
- ¶4 [evidence] @chopra1993 rank the errors: means, then variances, then covariances; why chapter 6 is harder and this chapter unavoidable.

### Diagnosing it before the solver does — 399

Says: Rank, riskless directions and condition number flag the problem without an inverse; the equities are singular on five years, and the full instrument universe is ill-conditioned even with N < T.
Why here: needs the rank bound and the condition number just defined; the reason for diagnosing before solving is in the title, no other reason is given.
Paragraphs:
- ¶1 [method] Two numbers, neither requiring an inverse.
- (code: diagnose)
- ¶2 [result] Rank below assets means singular; riskless_directions counts free portfolios; five years on the equities yields dozens.
- ¶3 [caveat] A finite but huge condition number is more dangerous than an infinite one; past 10^8 the inverse reads noise.
- ¶4 [result] All instruments on the full sample: N < T−1, yet rank deficient, condition 10^12; the bond block nearly replicates itself.
- (code: diagnose-claims)
- (code: rank-by-level)
- ¶5 [result] The singular rows show a negative smallest eigenvalue: floating-point noise around zero, a world with negative variance.
Note: ¶3 defines the condition number a second time, two paragraphs after eq-07-condition did; the hidden chunk asserts ¶4's numbers.

### Why this book has not needed the chapter until now — 93

Says: At class level no sixty-month window is rank deficient; the problem appears only when the portfolio holds securities.
Why here: stated: this is the chapter's own account of its place in the book, allocations so far were across classes.
Paragraphs:
- ¶1 [claim] Every allocation so far was across classes, where the problem does not arise.
- (code: windows-invertible)
- ¶2 [result] No sixty-month class-level window is rank deficient; once chapter 21 descends to securities it is the only question.
Note: the placement argument sits at the end of the theory section rather than in the opening.

## Four Routes — 1408

Says: Four responses, two changing what may be owned and two how it is estimated, each demonstrated and then plugged into the optimizer through a moment function.
Why here: stated in the opening's plan and repeated in ¶1: the routes are taken in order of what they cost.
Paragraphs:
- ¶1 [method] Four routes, two changing what may be owned and two how it is estimated, taken in order of cost.
Note: the announced cost order holds for routes one to three and then breaks: route four is a one-paragraph stub, two subsections on plumbing and patching follow, and route four is done in full last.

### Route one: hold fewer things — 85

Says: Allocate across classes or sleeves and the matrix is estimable on five years; this is what mandates do, but it does not help when the mandate names securities.
Why here: stated: the cheapest fix.
Paragraphs:
- ¶1 [claim] The cheapest fix is not to have the problem: allocate across classes or sleeves, estimable on five years.
- ¶2 [claim] Not a dodge: mandates sit there and chapter 15 treats sleeves as a decision; useless once the mandate names securities.
Note: no code; the only route demonstrated nowhere and absent from the race in the application.

### Route two: impose a structure — 412

Says: A k-factor structure replaces N(N+1)/2 parameters with Nk + N and cannot be singular; six lines do it, while the package's version refuses exactly the windows where it is needed.
Why here: next in the cost order; takes the parameter count from the theory section as its motivation.
Paragraphs:
- ¶1 [definition] Factor structure (eq-07-factor): Nk + N numbers, never singular since D is positive; @fan2008, @bai2002, @connor1993 for convergence and k.
- ¶2 [method] Factors may be economic, as in chapter 5, or statistical principal components; the latter is six lines.
- (code: factor-covariance)
- ¶3 [result] Full rank and a finite condition number where the sample matrix has dozens of riskless directions; structure does the work.
- ¶4 [transition] The package ships this as `statistical.factor.model()`, with one constraint worth knowing.
- (code: factor-model-package)
- ¶5 [caveat] The package function demands T ≥ N, exactly when unneeded; the body does not; appendix D records the patch.

### Route three: shrink the matrix — 205

Says: Pull the sample matrix toward a well-conditioned target with a data-chosen λ; it needs no assumption, cannot fail and is always invertible.
Why here: next in the cost order; not otherwise stated.
Paragraphs:
- ¶1 [definition] Shrinkage (eq-07-shrinkage) pulls the sample toward a well-conditioned target; @stein1956, @ledoit2003, @ledoit2004, @schafer2005, @ledoit2017 attributed.
- ¶2 [claim] The workhorse: no assumption about what drives returns, cannot fail, invertible whenever F is and λ > 0.
- (code: shrunk)
- ¶3 [result] lambda is the weight on the target, here a stated share of the way toward independence.

### Route four: estimate robustly — 38

Says: A robust estimator fixes a matrix badly centered by a few months, a different problem from a short sample, deferred to later in the section.
Why here: stated: it is a different problem and is "taken up below".
Paragraphs:
- ¶1 [transition] A robust estimator addresses a badly centered matrix, not a short sample; a different problem, taken up below.
Note: a route announced in one paragraph and deferred past two unrelated subsections; the subsection does no work of its own.

### Getting any of this into the optimizer — 298

Says: The package's moment function offers no shrinkage, but `momentFUN` accepts a function object, so any estimator plugs in without leaving the package's constraints behind.
Why here: needs route three's estimator to have something to plug in; the text gives no reason for its sitting between the two halves of route four.
Paragraphs:
- ¶1 [caveat] The package routes every moment estimate through one function, and the released version offers no shrinkage.
- (code: moment-methods)
- ¶2 [result] The four methods: sample, boudt, and the view-blending black_litterman and meucci of chapter 17; none is route three.
- ¶3 [method] Users compute weights outside the package and lose its constraints; unnecessary, since `momentFUN` accepts a function object.
- (code: momentfun-takes-a-function)
- ¶4 [claim] As a function, settings can be baked in, one per intensity or factor model; nothing in the global environment.
- ¶5 [caveat] (callout) A moment function must set mu/sigma and mean/var, and return a plain matrix with dimnames.
Note: the chunk prints holdings, sum and maximum weight of the shrunk minimum-variance portfolio and no paragraph reads them; the callout title is a `##` line, which a count of `##` headings picks up as a sixth section.

### When the package function is the thing in the way — 88

Says: Beyond working around a package function, the right option on open source is to patch it and send the fix back; appendix D lists this book's patches.
Why here: not stated; it argues about route two's `statistical.factor.model()` check, two subsections back.
Paragraphs:
- ¶1 [claim] Better than a workaround: patch the package and send it back; route two's check is the case; appendix D lists patches.
Note: sits between the moment-function plumbing and route four, about neither; a general remark on package practice with no code.

### Route four in full: robust estimation — 257

Says: The package's robust estimators, the MCD among them, plug in like shrinkage and report lower volatility by discounting unusual months, which this market's co-arriving extremes argue against.
Why here: stated implicitly: they plug in "exactly where route three did", so the moment-function mechanism had to come first.
Paragraphs:
- ¶1 [claim] The package ships robust covariance estimators almost nobody uses and no current textbook covers.
- (code: robust-family)
- ¶2 [definition] Shrinkage repairs a short sample, robustness a contaminated one; the MCD estimator keeps the h-subset of smallest determinant, @rousseeuw1984, @rousseeuw1999.
- ¶3 [transition] They plug in where route three did.
- (code: robust-demo)
- ¶4 [caveat] The robust estimate's lower volatility discounts unusual months; chapter 4's co-arriving extremes argue against that; chapters 28 and 10 continue.
Note: the demo runs on the sixteen classes, not the equities the chapter's problem is posed on; the shrinkage-versus-robust contrast in ¶2 repeats the route-four stub and returns as takeaway 4.

## What the Routes Do to the Matrix — 1759

Says: Scored out of sample, shrinkage wins only where the sample matrix cannot be computed and ties once it can; the identity target is least true in a crisis; and long only was already shrinking.
Why here: stated in the opening's plan: after the routes, ask which of them pays out of sample.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: the heading names what the routes do to the matrix, but the section opens with portfolio scores and reaches the matrix (the spectrum) only in the middle of its second subsection; four subsections, four topics.

### Scoring the routes out of sample — 598

Says: On identical months, two of four estimators return no portfolio at sixty and one hundred and twenty months; shrinkage runs and has the lower volatility, but at one hundred and eighty months it ties the sample matrix and its λ has fallen.
Why here: stated: the matrix cannot score itself, every estimator flatters itself in sample, only an out-of-sample test is honest.
Paragraphs:
- ¶1 [method] The matrix cannot score itself; the honest test estimates on a window, holds a month, scores what happened.
- ¶2 [method] The race script: four estimators, three windows, long only, monthly rebalancing, scored on identical months.
- (code: equal-weight-control)
- (code: tbl-07-race)
- (code: race-claims)
- ¶3 [result] At 60 and 120 months two estimators return no portfolio on any date: eq-07-rank arriving as an empty result.
- ¶4 [result] Where the sample fails, shrinkage has lower volatility than the diagonal target and than equal weighting at 120 months.
- ¶5 [transition] The row that keeps this from being an advertisement.
- (code: the-tie)
- ¶6 [result] At 180 months sample and shrinkage tie and the factor model trails; shrinkage merely exists when others do not.
- ¶7 [result] lambda falls as the window lengthens: the procedure asks for less help as it needs less, the Ledoit–Wolf content.
Note: the race's four estimators are not the chapter's four routes: a diagonal estimator appears here without having been introduced, and routes one and four are never scored; the race lives in a script carrying chapter 5's name.

### Lower volatility is not a better portfolio — 546

Says: Sharpe ratio orders the estimators differently from volatility, and minimum variance beat equal weighting here against the general finding; then every route is shown as one operation on the eigenvalue spectrum.
Why here: a second reading of the race table, stated as "sharpe is not ann_vol"; the spectrum part is justified as "easier to see than to derive", not as belonging here.
Paragraphs:
- ¶1 [result] Sharpe ratio does not rank like volatility: at 180 months the sample has lowest volatility, shrinkage the highest Sharpe.
- ¶2 [result] Minimum variance cut volatility by a third and beat equal weighting on Sharpe; @demiguel2009 disagree in general; chapter 8 decides.
- ¶3 [transition] Every route is one operation on the eigenvalues, easier to see than derive.
- (code: spectrum)
- ¶4 [result] Many sample eigenvalues are exactly zero: the riskless portfolios from the other side, present even for coin flips, by eq-07-rank.
- (code: fig-07-spectrum)
- ¶5 [result] Shrinkage lowers the largest and raises the smallest eigenvalue, the @laloux1999 reading; a factor model reaches the same place differently.
Note: two topics under one heading: ¶1–2 read Sharpe ratios from the race, ¶3–5 and the chapter's only figure show what shrinkage does to the spectrum, which is what the parent section is named for; ¶4 repeats the coin-flip point of the theory section; the heading is a claim sentence rather than a noun phrase.

### Shrink towards what, when the target moves? — 475

Says: The identity target asserts unrelated assets, which is wrong in calm months and far wronger in the credit crisis, exactly when the portfolio depends on it; hence a factor target where available.
Why here: not stated; takes F from route three and the episodes from the data, and hands the choice on to chapter 19.
Paragraphs:
- ¶1 [claim] The identity target is chosen for being unlike the noise rather than true; how untrue depends on when.
- (code: regimes)
- (code: regimes-claims)
- ¶2 [result] In the credit crisis the first component's share rises and directions collapse beyond most equal-length calm windows; correlation rises too.
- ¶3 [claim] The diagonal target is wrong in calm and far wronger in crisis, when it matters most; prefer a factor target.
Note: switches to the sixteen classes, the universe where the chapter said the problem does not arise; the heading is a question.

### The shrinkage already in place — 140

Says: The long-only constraint acts on the solution as shrinkage acts on the matrix, and had already done work comparable to route three before any estimator changed.
Why here: stated: "one last connection, because it reframes much of this book".
Paragraphs:
- ¶1 [claim] @jagannathan2003: long only acts like shrinkage, forbidding the offsetting positions eq-07-riskless invites, improving out-of-sample risk; @frost1988 agree.
- ¶2 [evidence] Held against the race table: route three took a third off; long only had done comparable work for free.
Note: "comparable" is asserted, not computed in the chapter; exercise 4 asks the reader to quantify it.

## Key Takeaways — 257

Says: Seven bullets: the rank bound, the riskless portfolio, the condition number, the four routes, shrinkage's limits, minimum variance against equal weighting, long only as shrinkage.
Why here: by contract.
Paragraphs:
- [takeaway] Sample matrix singular when assets exceed observations, by eq-07-rank; on the equities and five years, short by over sixty.
- [takeaway] A singular estimate asserts a zero-variance portfolio, eq-07-riskless, and a minimizer will hold it.
- [takeaway] The condition number measures error magnification; the smallest eigenvalues are largely noise, @laloux1999, @marchenko1967.
- [takeaway] Four responses: fewer assets, factor structure, shrinkage, robust estimation; three address conditioning, the fourth contamination.
- [takeaway] Shrinkage wins where the sample cannot be computed and ties once the window is long; λ falls with the window.
- [takeaway] Minimum variance cut volatility by a third and beat equal weighting on Sharpe here; chapter 8 asks whether that survives.
- [takeaway] The long-only constraint is shrinkage and was already doing comparable work, @jagannathan2003.
Note: seven bullets against the contract's "around five"; bullet 6 restates ¶2 of the Sharpe subsection nearly sentence for sentence.

## Exercises — 160

Says: Four exercises: a near-singular bond block, a λ grid, factor against shrinkage on rolling windows, and the long-only effect quantified.
Why here: by contract.
Paragraphs:
- [exercise] 1. `covariance_health()` on the government and credit instruments alone; find the near-singularity's cause from eigenvectors.
- [exercise] 2. Fix lambda on a grid and plot out-of-sample volatility; locate the minimum against the analytic choice.
- [exercise] 3. A `factor_covariance()` moment function against shrinkage on rolling windows; where the structure stops helping.
- [exercise] 4. Unconstrained versus long-only minimum variance on the shrunk matrix; quantify the @jagannathan2003 effect.
Note: four against "around three"; exercise 1 follows up the instrument-level diagnosis of the theory section, exercise 4 supplies the computation the last subsection asserts.
