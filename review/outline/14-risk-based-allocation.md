---
file: chapters/14-risk-based-allocation.qmd
title: Risk-Based Allocation
part: Portfolio Optimization
words: 3211
sections: 5
paragraphs: 33
---

# Chapter

Claim: Allocating risk rather than capital is a convex problem that a six-line fixed point solves to machine precision and a one-line inverse-volatility rule nearly solves, which the package's own risk-budget objective scores correctly and cannot find; what it buys is several times the effective bets for a few percent more volatility, on a covariance matrix that halves those bets in the credit crisis.
Question: Why how much money sits in a position is not how much risk sits there, and what allocating risk instead looks like; @qian2006 and @maillard2010, in the third sentence rather than the first two.
Why here: Stated once, in the first sentence: every portfolio so far was described by its capital, so the chapter follows the capital-allocating optimizers. Needs chapter 9's minimum-variance portfolio and its resampling, chapter 13's convex-versus-heuristic classification and its constraint-ignoring solver, chapter 7's rank bound and regime spectrum; hands hierarchical risk parity to chapter 15 and the estimation problem to chapter 19, and reads chapters 23 and 25 ahead for turnover and the out-of-sample register. Why it closes the part after the solvers is not stated beyond that classification.
Does: Decompose any portfolio's volatility into risk contributions, compute the equal-risk-contribution portfolio by fixed point or by inverse volatility, score a portfolio against the package's objective, use `max_prisk` for a cap, and audit concentration with `HHI()`, `diversification()` and an effective-bets count.
Order: Theory (Euler decomposition, equal risk contribution and its convex program, the inverse-volatility approximation), implementation (the package objective scored, five failed searches, the cap it can enforce, the concentration audit), application (the trade in bets and volatility with the out-of-sample line, the regime dependence of Σ, general budgets, hierarchical risk parity), eight takeaways, four exercises; deviations: the theory section already runs the package (`inverse.volatility.weight()`, an inline minimum-variance optimization) and defines the base spec, the implementation section is the chapter's negative finding rather than its method, and the application closes with two code-free theory subsections, one of which says it belongs in chapter 15.

# Sections

## (opening) — 195

Says: Capital weights and risk weights are different things, and allocating risk has a clean definition, a cheap approximation and a package implementation that does not work.
Why here: the opening by contract; ¶2 lays out the chapter's order (decomposition, exact answer two ways, what the package objective does).
Paragraphs:
- (code: setup)
- ¶1 [claim] Portfolios so far were described by capital; the minimum-variance portfolio of chapter 9 holds most capital and nearly all risk in one series.
- ¶2 [method] An old idea with a clean definition, a cheap approximation and a package objective that scores the optimum and cannot find it; the plan.
- (code: data)
Note: the seminal citation sits in ¶2, the third sentence; ¶1's promise to measure the minimum-variance portfolio's risk share is met only as an effective-bets count in the audit table.

## Allocating Risk Rather Than Capital — 714

Says: Volatility decomposes exactly into risk contributions; equalizing them is a convex problem a fixed point solves in six lines and inverse volatility nearly solves in one.
Why here: stated in the opening's plan: first the decomposition that makes the idea precise, then the exact answer two ways.
Paragraphs: none of its own; the section goes straight to its first subsection.

### The decomposition that makes this precise — 180

Says: By Euler's theorem portfolio volatility is exactly the sum of each asset's risk contribution, and on sixteen equal weights one asset carries a multiple of its share.
Why here: stated: the exactness is what makes risk budgeting possible at all; ¶3's gap "is the entire motivation for what follows".
Paragraphs:
- ¶1 [derivation] Volatility is homogeneous of degree one, so Euler's theorem gives additive contributions (eq-14-euler).
- ¶2 [claim] The shares sum to the total by construction, @qian2006's point; divided by σ they sum to one, which the code computes.
- (code: risk-contribution)
- ¶3 [result] Equal weights: the largest series carries a multiple of its one-sixteenth of the capital; the gap is the whole motivation.

### Equal risk contribution — 335

Says: The equal-risk-contribution portfolio exists, is unique long-only and is convex by @spinu2013; a six-line fixed point reaches it to machine precision and still gives the least volatile series the largest weight.
Why here: needs eq-14-euler to set its terms equal; stated as what the gap of ¶3 motivates; ¶2 and ¶4 point forward to the search.
Paragraphs:
- ¶1 [definition] Every term of eq-14-euler set equal (eq-14-erc).
- ¶2 [claim] @maillard2010: exists, unique long-only, volatility between minimum variance and equal weight; no closed form but not hard; @spinu2013's convex log-barrier program (eq-14-spinu), @bai2016; the package uses a metaheuristic on it.
- ¶3 [method] A fixed-point iteration converges in milliseconds.
- (code: erc)
- ¶4 [result] Six lines reach equal contributions to machine precision; remember it when the search spends twenty thousand evaluations.
- (code: erc-weights)
- (code: erc-claims)
- ¶5 [result] `US_government` still gets the largest weight, being least volatile; far from the share minimum variance gives it, computed inline.
Note: ¶2 and ¶4 both send the reader to the application section for the metaheuristic search, which sits in the implementation section; ¶5 runs a full minimum-variance optimization inside an inline expression, and the audit chunk computes the same portfolio again as `w_mv`.

### The approximation that is nearly free — 181

Says: Under equal correlations inverse-volatility weighting is the exact equal-risk solution, and on this universe it lands within a small L1 distance of it for one division per asset.
Why here: stated: a special case worth exploiting; needs the exact answer to measure its distance from.
Paragraphs:
- ¶1 [definition] @maillard2010's special case: a common correlation makes inverse volatility exact (eq-14-inverse-vol); correlations here are unequal but not wild.
- (code: inverse-vol)
- ¶2 [result] `inverse.volatility.weight()` is exported and rarely used; close in L1 and in weight correlation to the exact answer; the approximation does almost all the work.
Note: the chunk defines `base`, the spec every later package call reuses, and carries the function's calling convention (wants the spec, returns an `optimize.portfolio` object) in a code comment rather than in prose; the `max_rc_deviation` it prints is not read.

## Implementation — 874

Says: The package's risk-budget objective scores the equal-risk problem correctly, none of five metaheuristic searches finds it, a cap on any one contribution it can enforce, and two exported functions audit concentration.
Why here: stated in the opening's plan: after the exact answer, measure what the package's own objective does with it.
Paragraphs:
- ¶1 [claim] The purpose-built objective accepts the problem, scores it correctly and cannot solve it.
- (code: spec)
Note: the section states its finding before showing it; the heading promises an implementation, the section is the chapter's negative result, the method's own code having already run in the theory section.

### The objective is right — 86

Says: Scored directly, the package's objective is zero at the true equal-risk portfolio and positive at equal weights, so the objective is not what fails.
Why here: stated: before blaming a solver, check what it was asked to minimize; needs `w_eq` and `w_erc` from the theory section to score.
Paragraphs:
- ¶1 [method] The package exposes its objective function, so two portfolios can be scored directly.
- (code: objective-values)
- ¶2 [result] Positive at equal weights, exactly zero at the equal-risk solution; the objective knows which portfolio it wants.

### The search does not find it — 440

Says: Most of the five solvers hand back the equal-weight start, a tenfold budget changes nothing, and the one-line approximation is closer than a twenty-thousand-evaluation search to a convex problem's answer.
Why here: not stated; follows once misspecification is ruled out; needs `rb_spec`, `w_erc` and `w_iv` from before.
Paragraphs:
- (code: searches)
- (code: tbl-14-searches)
- (code: searches-claims)
- ¶1 [result] Most of five return the equal-weight start exactly; ten times the budget changes nothing; `pso` moves, and away from the answer.
- ¶2 [claim] The finding: the search sits at a positive score for two hundred thousand evaluations while a zero-scoring portfolio is six lines away.
- (code: tbl-14-comparison)
- ¶3 [claim] The one-liner beats the search; a statement about heuristics on a problem chapter 13 would call convex, not about risk parity.
Note: opens on code with no lead-in; the hidden comparison chunk defines `p_vol()`, used by the audit, the trade and the takeaways, and asserts in passing that the one-liner beats the search; the heading is a claim sentence.

### What the machinery does do — 106

Says: A ceiling on a single risk contribution is satisfiable by rejection, so the objective works for caps and budgets while equal risk contribution is computed directly.
Why here: stated: "the objective is not useless", the counterpart to the failure just shown; "Budgets that are not equal" refers back to it.
Paragraphs:
- ¶1 [claim] Asked for a cap rather than an equalization, the objective delivers.
- (code: max-prisk)
- ¶2 [claim] A cap needs only a violation recognized, not an optimum located; the rule: the objective for budgets and bounds, equal risk directly.
Note: ¶1 says it delivers before the chunk runs, and no paragraph reads the number the chunk prints (largest contribution against the cap); nothing asserts that the cap held.

### Auditing concentration — 184

Says: `HHI()`, `diversification()` and an entropy-based effective-bets count audit four portfolios' concentration in one table.
Why here: not stated; two exported functions introduced because any portfolio in the book, including one from a solver that ignored its constraint (chapter 13), can be audited in one line.
Paragraphs:
- ¶1 [method] The two functions take a weight vector; any portfolio can be audited for concentration in a line.
- (code: concentration)
- (code: tbl-14-concentration)
Note: effective bets is defined in a code comment and the caption, never in the theory section; the table is built here and read only in the next section's first paragraph; `w_mv` recomputes the inline minimum-variance portfolio of the theory section.

## What Risk Parity Buys and Costs — 1026

Says: Equal risk contribution buys several times the effective bets for a few percent more volatility and holds its own out of sample at a fraction of the turnover, but the bets are a property of Σ, which halves in the credit crisis; budgets generalize it and hierarchical risk parity is the next question.
Why here: stated by the heading, the buy side then the cost side; its first subsection reads the table the implementation section built.
Paragraphs: none of its own; the section goes straight to its first subsection.
Note: four subsections, the last two of which are theory with no code.

### The trade, in its own units — 349

Says: Against minimum variance, equal risk costs a few percent more volatility for many times the effective bets, and out of sample inverse volatility sits between equal weighting and the tangency portfolio at a fraction of its turnover.
Why here: stated: "read the last two rows of the table together", continuing directly from tbl-14-concentration.
Paragraphs:
- ¶1 [result] Minimum variance: lowest volatility, few effective bets; equal risk: somewhat more volatility, exactly sixteen.
- ¶2 [claim] The trade in its own units; worth taking depends on trusting Σ, which chapter 9's resampling measured; the concentration is at least stable.
- ¶3 [evidence] @asness2012's leverage-aversion argument for taking it; @clarke2013 on when risk parity, maximum diversification and minimum variance coincide.
- (code: oos-line)
- ¶4 [result] Out of sample inverse volatility trails minimum variance and equal weighting, leads the tangency portfolio, at a fraction of its turnover (chapters 25, 23); competitive, cheaper, easier to explain.
Note: the out-of-sample line scores inverse volatility, not the equal-risk portfolio the chapter computed, because the register carries only `inverse_vol`; ¶2's "about five percent" is a number typed from chapter 9; ¶3's "conditions this market does not satisfy" is asserted, not shown.

### The covariance is a regime variable — 274

Says: The effective number of bets belongs to Σ, not to the portfolio, and the matrix's independent directions fall by more than half through the credit crisis.
Why here: stated: "one thing risk parity cannot escape", the cost after the buy; sends the estimation problem to chapter 19.
Paragraphs:
- ¶1 [claim] The number of effective bets is a property of Σ, not of the portfolio, and Σ moves.
- (code: regime-spectrum)
- ¶2 [result] Outside the episodes the first component carries less and the matrix spans more directions; through the credit crisis the count more than halves, so sixteen equal contributions become a handful of bets when it matters.
- ¶3 [caveat] Risk parity measures risk more honestly and then allocates against an estimate that halves when tested; @roncalli2013; chapter 19 confronts it.
Note: `directions` is the participation ratio of the eigenvalues of Σ, a different measure from the entropy-based effective bets of the audit table, and the prose calls both "bets"; ¶2's "calm windows of the same length still do not reach" is not computed by the chunk; the text says the measurement repeats chapter 7's.

### Budgets that are not equal — 177

Says: Equal risk contribution is the equal case of a risk budget b_i, which is the language mandates speak and the form the package objective can satisfy by rejection.
Why here: stated: equal risk "is the special case of a more general idea"; not stated why it comes after the regime subsection rather than beside the definition in the theory section.
Paragraphs:
- ¶1 [definition] A budget b_i summing to one (eq-14-budget), reducing to eq-14-erc at 1/N; @roncalli2013; eq-14-spinu and the fixed point both generalize by weighting with b_i.
- ¶2 [claim] A mandate speaks in risk shares, not capital shares, and only the former survives a volatility change; the form the package objective can satisfy, as `max_prisk` showed.
Note: the general definition arrives after its special case has been used for three sections, in the application section, with no code; ¶2's last two sentences restate the practical rule of "What the machinery does do".

### Hierarchical risk parity — 202

Says: Hierarchical risk parity clusters assets on correlation distance and allocates by recursive bisection without inverting Σ; it belongs with chapter 15 and is the one technique in this area the package lacks.
Why here: stated: the obvious next question once risk contributions are on the table, and the one widely used technique the package does not implement; the text says it belongs in chapter 15.
Paragraphs:
- ¶1 [definition] The methods here need Σ and mostly its inverse, weakest by chapter 7; @lopezdeprado2016 clusters, orders and bisects recursively instead.
- ¶2 [claim] No inversion, so defined even when Σ is singular (eq-07-rank); claimed more stable out of sample because a clustering is coarser than an inverse.
- ¶3 [transition] Belongs with the sleeve structure of chapter 15; mentioned here as the next question and as the package's gap.
Note: no code, and the text itself says the method belongs elsewhere; ¶1's premise that most of the chapter's methods need the inverse sits against a fixed point and a one-liner that invert nothing.

## Key Takeaways — 253

Says: Eight bullets: the exact decomposition, equal capital is not equal risk, the equal-risk portfolio's properties, its convexity, the failed searches, the rule for the package objective, the trade and the out-of-sample line, bets as a property of Σ.
Why here: by contract.
Paragraphs:
- [takeaway] Volatility decomposes exactly by eq-14-euler; the shares sum by construction [@qian2006].
- [takeaway] Equal capital is not equal risk: one of sixteen equal weights carries a multiple of its share.
- [takeaway] The equal-risk portfolio exists, is unique long-only, and sits between minimum variance and equal weight in volatility [@maillard2010].
- [takeaway] Not a hard problem: eq-14-spinu is convex and six lines reach machine precision; the package routes it to a metaheuristic.
- [takeaway] Most of five solvers return their start, a tenfold budget changes nothing, and the one-liner beats a twenty-thousand-evaluation search.
- [takeaway] Use the risk-budget objective for caps and budgets, satisfiable by rejection; compute equal risk directly.
- [takeaway] Several times the effective bets for a few percent more volatility; out of sample inverse volatility sits between equal weight and tangency at a fraction of the turnover.
- [takeaway] Effective bets is a property of Σ, not of the portfolio, and falls by more than half into the credit crisis.
Note: eight against "around five"; bullet 2 restates the decomposition's ¶3 and bullet 5 the search's ¶1 and ¶3, numbers included; the general budget and hierarchical risk parity have no bullet beyond bullet 6's rule.

## Exercises — 124

Says: Four exercises: equal risk fitted on calm months and tested in the credit crisis, a universe where inverse volatility fails, the searches repeated with a cap, and an inverse-Herfindahl bets measure.
Why here: by contract.
Paragraphs:
- [exercise] 1. Run `erc()` on a covariance from the months outside the episodes, apply it through the credit crisis; how equal are the realized contributions?
- [exercise] 2. Build a universe where ignoring correlations is catastrophic, two near-identical series and one independent; report what `inverse.volatility.weight()` does.
- [exercise] 3. Repeat tbl-14-searches with `max_prisk` instead of `min_concentration`; do the solvers agree, does the budget bind?
- [exercise] 4. Replace entropy with the inverse Herfindahl of the risk shares and recompute tbl-14-concentration; which ranks change, which measure to defend to a client.
Note: four against "around three"; each follows one subsection: 1 the regime, 2 the approximation, 3 the searches, 4 the audit table.
