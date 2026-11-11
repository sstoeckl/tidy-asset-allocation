---
file: chapters/03-return-risk-and-the-investor.qmd
title: Return, Risk, and the Investor's Problem
part: Foundations of Portfolio Choice
words: 7987
sections: 5
paragraphs: 76
---

# Chapter

Claim: The investor's problem is expected utility, approximated by μ_w − (γ/2)σ²_w on returns in excess of the bill, and the approximation is only as good as its conventions for return, horizon, currency and riskless alternative, which are fixed here once.
Question: What does an investor want from a portfolio, and in which units is the answer measured; @markowitz1952 for the first, @vonneumann1944 for the second.
Why here: Needs the sixteen series and symbols of chapter 2 and the environment of chapter 1; says the definitions are fixed here so that no later chapter revisits them; chapter 4 measures the bill against the money markets and the currency split, 9 derives the frontier from the dominance vocabulary, 11 adds moments to the criterion, 16 onward carry the tactical label, 25 applies the reporting rule.
Does: State the objective on excess returns with a γ read in basis points, pass it to PortfolioAnalytics as γ/2, annualize means and Sharpe ratios in a named convention, and sort series into dominated and efficient before any optimizer runs.
Order: Opening, theory in ten subsections, implementation in six, application in four, Key Takeaways, Exercises; the contract holds, except that theory already computes (three chunks, a γ table, an implied γ), the application derives the separation result, the last two theory subsections have no implementation or application counterpart, and there are six takeaways and four exercises.

# Sections

## Opening, before the first section — 349

Says: The question, the order of the chapter, and the data it runs on.
Why here: Contract position; says the definitions are fixed here so no later chapter revisits them.
Paragraphs:
- (code: setup)
- ¶1 [claim] Investors want two numbers per portfolio (Markowitz); units question older (von Neumann); mean-variance approximates expected utility, quality depends on definitions.
- ¶2 [method] What the chapter does, in order; it is neither strategic nor tactical but where the terms are defined.
- ¶3 [method] Data: the sixteen series of chapter 2 in its symbols, the bill, the excess; environment of chapter 1.
- (code: data)

## Returns, Horizons, and the Basis of Comparison — 2986

Says: Returns, means, Sharpe ratios and the excess basis are fixed; then the investor's objective, its horizon, dominance and the strategic/tactical labels are defined from them.
Why here: The opening lists this order; the implementation checks each convention and the application runs the objective, so both need the definitions first.
Paragraphs: none outside the subsections.
Note: Ten subsections in two groups, six on conventions and four on the investor; the conventions group is the only part of theory with code.

### Simple returns, log returns, and compounding — 148

Says: Simple returns add across assets, log returns across time; the data are simple and stay simple wherever a portfolio is formed.
Why here: First convention in the opening's list; the averages next need compounding, and every weight vector needs simple returns.
Paragraphs:
- ¶1 [definition] Simple return with income, and its log.
- ¶2 [claim] Simple adds across assets (portfolio return), log across time (compounding); log only where a horizon is aggregated.

### Averages, annualization, and the variance drag — 267

Says: The arithmetic mean is the input to every objective, the geometric mean is what was earned, and half the variance separates them.
Why here: Needs compounding from the previous subsection; says the application meets a series with the higher arithmetic and the lower geometric mean.
Paragraphs:
- ¶1 [definition] Two averages answer different questions; drag ≈ σ²/2; small for a bond, not for equity; rankings can cross.
- ¶2 [definition] Annualization of μ, σ and g; the first two from independence; two mistakes from mixing them.
Note: ¶2 holds a definition and two caveats (geometric times twelve, √12 under autocorrelation) in one paragraph.

### The Sharpe ratio and its horizon — 143

Says: √q scales the ratio only under independence; Lo's correction gives the general factor.
Why here: Needs the annualization rule just given; says the implementation measures the error on this data.
Paragraphs:
- ¶1 [definition] Sharpe ratio, attributed to Sharpe 1966 and 1994.
- ¶2 [derivation] Numerator scales with T, denominator with √T; Lo's autocorrelation formula; sign of the naive error.

### Excess returns as the basis — 395

Says: Every optimized return is in excess of the Treasury bill, for four reasons of rising consequence, and the bill is not a money-market series.
Why here: Reason two needs the Sharpe ratio just defined; the application measures reason three; chapter 4 measures the money-market gap.
Paragraphs:
- ¶1 [claim] Excess return defined; four reasons follow in increasing order of consequence.
- ¶2 [evidence] Tangency portfolio and market equilibrium exist only relative to a riskless rate (Tobin, Sharpe).
- ¶3 [caveat] PortfolioAnalytics has no riskless-rate argument; excess returns make its ratio the Sharpe ratio.
- ¶4 [claim] An uninvested balance earns zero in the objective, true only for excess returns; the application measures it.
- ¶5 [claim] The bill moves, so only the excess formulation is consistent through time.
- (code: bill-path)
- ¶6 [result] The bill's first and lowest annual rates; comparing against zero is wrong in at least one.
- ¶7 [caveat] The riskless rate is the bill, not the money markets, which carry duration; chapter 4 measures.
Note: The first theory subsection to read a number from a chunk; the implementation has not started.

### Nominal and real — 165

Says: The book works in nominal dollars because the market carries no inflation series; a real-liability investor would swap the bill for an indexed bond.
Why here: Not stated; qualifies the bill as riskless in nominal terms only.
Paragraphs:
- ¶1 [caveat] Fisher relation; no inflation series so nominal throughout; real investor's safe asset is the indexed bond (Campbell); machinery unchanged.
Note: One paragraph carries a definition, the book's scope decision and the literature.

### Currency — 201

Says: Every series is an unhedged dollar return, and hedging is one subtraction of the matching currency return.
Why here: Not stated; the implementation applies the subtraction to the foreign governments and chapter 4 decomposes the variance.
Paragraphs:
- ¶1 [definition] Dollar return compounds local return and currency return; hedged return is the difference.
- ¶2 [method] Hedge as spot subtraction, no interest differential; Perold, Black, Campbell on whether to hedge; pointers to chapters 15, 22, 4.
Note: ¶2 mixes the book's convention with the hedging literature.

### The investor's objective — 839

Says: Expected utility expands to μ_w − (γ/2)σ²_w, a certainty equivalent whose γ is a price with units an investor can read.
Why here: The opening says the problem is stated after the basis; the wealth equation puts the balance in the bill, which needs the basis; dominance and the package call need the criterion.
Paragraphs:
- ¶1 [definition] Wealth, weights, balance in the bill; maximize expected utility of terminal wealth (von Neumann–Morgenstern).
- ¶2 [definition] Concavity is risk aversion; Arrow–Pratt coefficients; premium ≈ ½γσ².
- ¶3 [derivation] Second-order expansion gives the mean-variance criterion; Markowitz's exactness conditions; Levy–Markowitz evidence; chapter 11 adds moments.
- ¶4 [derivation] Two readings: a certainty equivalent, and γ as the price of variance along an indifference curve.
- ¶5 [example] The price in units: volatility accepted for one point at γ = 2 and 10; cost of ten percent at γ = 4.
- (code: tbl-03-gamma)
- ¶6 [claim] The table to keep in mind; customary range two to ten; an all-equity investor's implied γ by the first-order condition.
- (code: implied-gamma)
- ¶7 [result] The implied γ on this sample.
- ¶8 [claim] CRRA as the alternative; equivalent to mean-variance in log returns under lognormality; tails differ, chapter 11.
Note: Longest subsection; eight paragraphs and two chunks run from derivation through a units table to the CRRA alternative, which could stand alone.

### The horizon of the problem — 160

Says: Under independent returns the long-lived investor is myopic, so the one-period problem re-solved at each rebalancing is exact; changing opportunities add hedging demands the book does not model.
Why here: Answers the objection that the objective is one-period; refers forward to the horizon axis defined below.
Paragraphs:
- ¶1 [caveat] Samuelson–Merton myopia; hedging demands when opportunities move (Campbell 2002); the book's myopic policy; horizon chapters are about inputs.

### Dominance, efficiency, and the northwest rule — 219

Says: A dominates B with at least as much return and at most as much risk, one strict; a better allocation lies northwest; what nothing dominates is efficient.
Why here: Follows from having two moments per portfolio; says the vocabulary applies before γ is chosen and every later chapter uses it; chapter 9 derives the frontier.
Paragraphs:
- ¶1 [definition] Dominance in the volatility–return plane.
- ¶2 [definition] The northwest rule; efficient; weaker than the utility criterion (a partial order) and stronger (holds for any γ).

### Strategic and tactical allocation — 440

Says: Strategic is the long-run policy from unconditional moments, tactical a deviation on conditioning information; the chapters are sorted, and a portfolio is judged by the measure it was chosen by.
Why here: The opening says the chapter closes by defining the terms once; the sort needs the objective, which the strategic chapters solve from full-sample moments.
Paragraphs:
- ¶1 [claim] Two cuts: granularity orders the parts; horizon needs two terms defined here.
- ¶2 [definition] Strategic and tactical defined; orthogonal to granularity; Brinson, Ibbotson, Sharpe 1987, Ang, DeMiguel.
- ¶3 [transition] Chapters 9–15 strategic, 16–19 tactical, 23–25 implementation and evaluation; each chapter says which.
- ¶4 [claim] The measure judged by must be the measure chosen by; Artzner, Acerbi; chapters 10 and 25.
Note: ¶4 is a separate rule under a heading about horizon; neither this subsection nor the previous has an implementation or application counterpart.

## Implementation — 2230

Says: PerformanceAnalytics implements every convention with a default the reader must know, and PortfolioAnalytics takes γ/2.
Why here: Says the point is to see which convention each function defaults to; the application reuses the specifications and the weight function built here.
Paragraphs: none outside the subsections.
Note: The six subsections follow the theory's order (returns, Sharpe, horizon, bill, currency, objective); nominal/real and dominance have no counterpart here.

### Return conventions in `PerformanceAnalytics` — 435

Says: Rebuilt returns match the shipped ones, the two means and the drag come from one series, and the package's annualization default is the compounded one.
Why here: Says the point is to see which convention each function defaults to; needs the return definition, the drag and the annualization rules.
Paragraphs:
- ¶1 [method] The package implements every convention; rebuild prices from the shipped index and check the return.
- (code: prices)
- ¶2 [result] First observation NA; log return smaller than simple when positive, larger in magnitude when negative.
- ¶3 [code] `Return.annualized()` with scale one returns the geometric monthly mean, so both averages come from one series.
- (code: means)
- ¶4 [example] (callout, collapsed) Drag on US_equity with the numbers substituted; agrees to the third-order term; in basis points and percentage points.
- ¶5 [code] Three annualization conventions give three numbers; the default is the compounded one.
- (code: annualized)
- ¶6 [result] A dollar's terminal value is the compounded figure; the arithmetic figure is the right input and the wrong answer.

### The Sharpe ratio, in two conventions — 466

Says: Two package functions default to different Sharpe conventions; the gap is the drag over the volatility, and it swaps pairs of the sixteen series.
Why here: Needs the excess basis, the Sharpe definition and the drag; says the book reports compounded and optimizes arithmetic, as chapter 4 does.
Paragraphs:
- ¶1 [code] `Return.excess()` reproduces the data block's subtraction exactly.
- (code: excess)
- ¶2 [code] `table.AnnualizedReturns()` and `SharpeRatio.annualized()` disagree on the same series.
- (code: sharpe-two-ways)
- ¶3 [caveat] (callout) geometric TRUE against FALSE; gap grows with volatility and can reorder; report compounded, optimize arithmetic.
- ¶4 [code] Both rankings from one function with the convention as an argument.
- (code: sharpe-rank)
- ¶5 [result] Top and US_credit's rank agree; the rest move in swapped pairs, the faller the more volatile.
Note: ¶1 checks the excess basis, not a Sharpe convention; it sits here because the bill is needed next.

### Aggregation over horizons — 483

Says: Compounded to quarters and years, the annual ratio falls short of √12 times the monthly; autocorrelation explains the bond series, sampling error the rest.
Why here: The Lo equation says when √12 is right, and the theory promised the error would be measured here.
Paragraphs:
- ¶1 [method] Direct test: compound to quarters and years, compute the ratio at each horizon.
- (code: sharpe-horizon)
- ¶2 [result] US_government's shortfall and positive first-lag autocorrelation; US_equity's shortfall unexplained by its own; Lo's correction next.
- (code: lo-correction)
- ¶3 [result] Overstated for most series, led by government and credit; the residual is sampling imprecision; √12 stays, with the caveat.
Note: ¶3 reads two chunks' worth of numbers in one long paragraph.

### The bill is not a seventeenth asset — 191

Says: Added as a column, the bill absorbs the minimum-variance portfolio; as a constant it makes Σ singular; it enters through the basis and the budget.
Why here: Says a reader just told the bill is essential will be tempted to add it; Tobin's separate treatment explains why not.
Paragraphs:
- ¶1 [caveat] The temptation, the two failures, and why Tobin keeps the riskless asset out of Σ.
- (code: bill-column)
- ¶2 [result] The optimizer's weight on the bill and the rank of the constant-column covariance.

### Hedging a foreign government bond — 199

Says: Subtracting the currency return removes most of a foreign government bond's volatility; for JP_government nearly all of it is exchange rate.
Why here: The currency equation is one subtraction and governments have little local volatility; equities are chapter 4's question.
Paragraphs:
- ¶1 [method] Four foreign governments are where the subtraction matters most.
- (code: hedge)
- ¶2 [result] Range of volatility removed; the JP_government numbers; equities answered in chapter 4.

### Where risk aversion enters the package — 453

Says: PortfolioAnalytics states the objective as mean plus var with risk_aversion, and that argument is γ/2, verified against a solver that takes γ literally.
Why here: Needs the quadratic-utility equation; says one thing must be known before the objectives are used; the application's sweeps call the functions built here.
Paragraphs:
- ¶1 [code] Two objectives on one specification, or the constructor; one thing to know first.
- ¶2 [caveat] (callout, warning) Q = 2λΣ meets ROI's half; pass γ/2; undocumented upstream; proof in appendix B; every call halves.
- (code: spec)
- ¶3 [method] quadprog takes γ literally; the budget is relaxed so the scale difference shows.
- (code: gamma-check)
- ¶4 [result] risk_aversion = 5 matches γ = 10 to machine precision and misses γ = 5 by a named gap.

## What the Objective Does on Sixteen Assets — 1879

Says: Dominance sorts the sixteen before any optimizer runs; raising γ ends at minimum variance under full investment and at the bill without it; the total-return basis overinvests by a fixed share.
Why here: Opens with the picture as the house rule asks; needs the dominance definition, the γ table and the implementation's specifications; chapter 9 takes the frontier from here.
Paragraphs: none outside the subsections.
Note: Four subsections serve only the investor half of the theory; the conventions half ends in the implementation, except the drag, which returns in the basis check of the first subsection.

### The northwest rule applied — 790

Says: Most of the sixteen series are dominated on the arithmetic excess basis; the efficient set is the same on the compounded basis, but who dominates whom moves with the drag.
Why here: Says the application opens with the picture and that the count needs no optimizer; chapter 9 draws the same picture on compounded total returns.
Paragraphs:
- ¶1 [method] One point per series, arithmetic excess mean vertical, one data frame so no mismatched pairs.
- (code: moments)
- (code: tbl-03-dominance)
- (code: fig-03-northwest)
- ¶2 [result] Number dominated; the efficient set; the most-dominated series; one sample, no test; chapter 9 picks the combination.
- ¶3 [claim] On compounded total returns the efficient set holds and the relation beneath it changes.
- (code: basis-dominance)
- ¶4 [result] Same efficient series; some gain a dominator; the largest-drag case's lead is smaller than its drag; both statements true.
Note: Three chunks run before any prose reads them; ¶3–4 return to the drag, the averages topic of the theory, inside the dominance subsection.

### Raising γ under full investment — 342

Says: With weights summing to one, rising γ walks the solution to the minimum-variance portfolio and stops; it cannot reach cash.
Why here: Not stated; it is the first of two budget rules, and the next subsection is the contrast.
Paragraphs:
- ¶1 [claim] Full investment leaves no cash to reach; the left end is the minimum-variance portfolio of chapter 9.
- (code: sweep-full)
- (code: tbl-03-sweep-full)
- ¶2 [result] Volatility reaches the minimum-variance level by γ = 10,000; Jagannathan–Ma on needing no μ; the other end is one series.

### Relaxing full investment — 526

Says: Without the budget the risky composition is fixed and the invested fraction is proportional to 1/γ, which is Tobin's separation; it survives long-only.
Why here: The contrast to the previous rule; says the same γ gives a different answer under a different budget, and the figure shows both.
Paragraphs:
- ¶1 [derivation] First-order condition gives w* = Σ⁻¹μ/γ; composition independent of γ; survives long-only; the cap only binds at small γ.
- (code: sweep-relaxed)
- ¶2 [result] The cap binds up to a γ; beyond it invested = constant/γ; same risky portfolio, the long-only maximum-Sharpe one.
- (code: fig-03-gamma)
Note: The only numbered equation outside the theory section; the figure for both rules follows the prose that reads it.

### The basis, once more, in the invested fraction — 212

Says: Fed total returns, the relaxed problem invests a fixed share more in risky assets at every γ, crediting the bill as a reward for risk.
Why here: Says the third argument for excess returns can now be measured, which needs the relaxed problem of the previous subsection.
Paragraphs:
- ¶1 [method] Same relaxed problem on total returns, where the optimizer believes the alternative earns zero.
- (code: basis-invested)
- ¶2 [result] The overinvestment share, constant across γ; an arithmetic error about the alternative; why every data block subtracts the bill.

## Key Takeaways — 305

Says: Six bullets, one per theory topic, with the package trap and the two sweeps folded into one.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Simple adds across assets, log across time; arithmetic in, geometric earned, drag between; √12 assumes independence (Lo).
- ¶2 [takeaway] Excess of the bill for four reasons; the money markets are not the bill.
- ¶3 [takeaway] Mean-variance is a second-order approximation; a certainty equivalent; γ is a price, with the γ = 4 number.
- ¶4 [takeaway] Dominance, northwest, efficient; the count of dominated series on this sample.
- ¶5 [takeaway] risk_aversion is γ/2; full investment ends at minimum variance, the relaxed budget is two-fund separation.
- ¶6 [takeaway] Strategic and tactical defined; the chapter sort; judged by the measure chosen by.
Note: Six against the contract's "around five"; ¶5 and ¶6 each carry two points.

## Exercises — 201

Says: Four exercises: dominance on weekly data, Lo's correction against direct compounding, hedging the foreign equities, the γ of a 60/40 investor.
Why here: Contract position; each reuses a function or table of the chapter by name.
Paragraphs:
- ¶1 [exercise] Recompute the dominance table on weekly data; which series change status and why.
- ¶2 [exercise] Lo's correction at q = 3 and 12 against direct quarterly and annual ratios; which assumption fails.
- ¶3 [exercise] Hedge the four foreign equity markets; what happens to JP_equity and which covariance sign it needs.
- ¶4 [exercise] The γ matching a 60/40 portfolio's volatility under the relaxed budget; read the γ table.
Note: Four against "around three"; three are on the conventions and one on the objective.
