---
file: chapters/13-solvers.qmd
title: Numerical Optimization and Solvers
part: Portfolio Optimization
words: 3315
sections: 5
paragraphs: 49
---

# Chapter

Claim: Convexity, not the solver, decides whether a weight vector is the answer: the convex solvers reach an independently computed optimum exactly, every search lands short of it and slower, and three of five solvers return a portfolio that violates a position limit they accepted without a word, so every result has to be audited against its request.
Question: Which of the routines behind `optimize.portfolio()` return the answer rather than a weight vector, and which honor the constraints they accept; cites nobody in the opening — the first citation (Boyd and Vandenberghe) arrives in the theory section's third paragraph.
Why here: Stated only as "every portfolio problem posed so far" ending in a numerical routine. Takes the singular-covariance case from chapter 7, the constraint set from chapter 12 and the budget-encoding failure from chapter 9; hands the accuracy band to chapter 14's risk budgeting (said to have no convex formulation in the package), `HHI()` and `diversification()` to chapter 14, the selection-bias parallel to chapter 25, the patch state to appendix 93. Why it follows 12 and precedes 14 inside the part is implied (12's constraints are what breaks convexity, 14's problem is what forces a heuristic) but never said.
Does: Compute an independent benchmark for a long-only maximum-Sharpe problem in `quadprog`; race six solvers with `run()`; test five under a binding position limit with `feas()`; audit any result with a four-line `audit()`; combine results into one object; choose a solver by three questions.
Order: Theory (convexity, where it is lost, the independent benchmark), implementation (the race, the feasibility test, the audit, combining results), application titled as an explanation (the search budget, seeds, the decision rule), takeaways, exercises. Deviations: the benchmark is computed inside the theory section; the implementation heading has no paragraph of its own; the application runs one more experiment on the race's machinery rather than a result on the modeled market, and two of its three subsections are prose only; the opening carries no citation and no visible packages block; six takeaways, five exercises.

# Sections

## Opening (untitled) — 209

Says: Every solver returns a weight vector, only some return the answer, and the chapter measures which, then asks which honors a constraint.
Why here: Contract position; the text says the families are set out first, measured second, and the honoring question comes last.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Every problem so far ended in a routine's weight vector; all solvers return one, only some the answer.
- ¶2 [method] Three steps: convexity separates the families, a race against an independent answer, then which solver honors a constraint.
- (code: data) the sixteen classes in excess of the bill; Σ and μ
Note: No citation in the opening; the packages block is a hidden `setup` chunk and the shown chunk loads data instead. ¶2 already gives the chapter's headline (three of five infeasible), which returns three more times.

## Convexity Is the Whole Question — 606 (260 before the subsections)

Says: The choice is between convex and non-convex problems, not between solvers; on a convex problem every local minimum is global, so converged means correct.
Why here: Stated in the opening: what distinguishes the two families is set out first. Needs the positive semi-definite Σ and the singular case of chapter 7; the race reads its result through eq-13-convex.
Paragraphs:
- ¶1 [claim] Two families, not nine solvers; what separates them is a property of the problem, not the software.
- ¶2 [definition] A convex set and a convex function; eq-13-convex.
- ¶3 [derivation] Minimum variance is convex however Σ is estimated; the simplex is convex; local minimum is global, so converged means correct.
- ¶4 [evidence] Goldfarb–Idnani active set under `quadprog`/`ROI`, operator splitting under `OSQP`/`CVXR`; Nocedal–Wright for both.
Note: The heading is a sentence, not a noun phrase (so is the application's). ¶3 carries three points (objective convex despite estimation, feasible set convex, the global-minimum consequence) around a display equation; the chapter's first citation arrives here.

### Where convexity is lost — 183

Says: A cardinality constraint turns the feasible set into a union of faces, which needs integer variables; that is what the heuristics exist for, and nothing stops their misuse on convex problems.
Why here: Stated: not every mandate fits the simplex; draws on chapter 12's constraints; supplies eq-13-cardinality to the feasibility test and the misuse premise to the race.
Paragraphs:
- ¶1 [definition] Chapter 12's constraints mostly stay convex; cardinality eq-13-cardinality is a union of faces, needs binary variables, NP-hard.
- ¶2 [evidence] Differential evolution, particle swarm, simulated annealing attributed; no guarantee, coverage for certainty; Ardia brought DE in; Gilli.
- ¶3 [claim] Nothing stops a user applying the searches to a convex problem, and many published examples do.
Note: ¶3 is the premise of the race in one sentence, with no example for the published misuse it asserts.

### A problem whose answer we already know — 150

Says: The long-only tangency portfolio is solved directly in `quadprog`, outside the package, as the benchmark every comparison is read against.
Why here: Stated: accuracy claims require a benchmark computed outside the system under test; the race needs `w_true` and `sharpe()`.
Paragraphs:
- ¶1 [method] Accuracy claims need a benchmark computed outside the system under test.
- (code: truth) long-only tangency solved in `quadprog` directly; `w_true`, `sharpe()`, the holdings count
- ¶2 [derivation] The trick: fix μ′w = 1, minimize variance, rescale; Sharpe is scale-invariant, so the rescaled QP answer maximizes it.
Note: A computation inside the theory section, and the explanation follows the chunk that already used it.

## Implementation — 1333

Says: (heading only)
Why here: Not stated; the opening's sequence sentence is the only link.
Paragraphs: none of its own.
Note: Heading only; the four subsections share no introducing paragraph, and the last two (audit, combine) are tools rather than tests.

### Racing them on a problem with an answer — 634

Says: Six solvers on the convex tangency problem: the convex pair hits the known answer exactly, every search falls short and is at least an order of magnitude slower.
Why here: Stated in the opening: the families are measured against a problem with a computed answer; needs `w_true` and `sharpe()` from the truth chunk; the application reuses `run()` and the band `rng`.
Paragraphs:
- (code: race) the specification, `run()`, six solvers under `maxSR = TRUE`
- (code: tbl-13-race)
- (code: race-claims) hidden assertions: convex pair exact, every search below 95 percent and ten times slower
- ¶1 [result] `ROI` and `CVXR` exact, as eq-13-convex guarantees; the searches reach a band of the Sharpe, an order of magnitude slower.
- ¶2 [claim] Not a criticism of the searches, which explore because that is all they do; the fault is the default advice.
- ¶3 [caveat] (callout) Running the race prints the samplers' warning that the exact budget is restrictive; relax to 0.99–1.01.
- ¶4 [caveat] (callout) A draw rarely sums to one; the suggested slack is what breaks `quadprog` in chapter 9; a degeneracy of the encoding.
- (code: fig-13-race) share against relative time, log x, the two families colored
Note: Opens with a chunk and a table before any prose; the figure arrives after the callout, apart from ¶1 that reads it; the callout quotes the package's message verbatim as a code block.

### Which solver honors the constraint — 430

Says: Under a binding position limit two solvers respect it and three, `ROI` among them, return an infeasible portfolio without a warning.
Why here: Stated in the opening: after which solver accepts a constraint, which one honors it; needs eq-13-cardinality and the benchmark's holdings count for `k_lim`; the callout says the lesson is the reason the section exists.
Paragraphs:
- ¶1 [transition] Add eq-13-cardinality, which no QP expresses; the picture inverts, but not as the previous section implies.
- (code: poslimit) `k_lim` one below the benchmark's holdings; `feas()` on five solvers; a verdict column
- (code: poslimit-claims) hidden: `ROI` violates with the unconstrained holdings; three violate; the ignorers hold nearly everything
- ¶2 [result] Two solvers respect the limit; the others accept it, ignore it, return nearly the whole universe, converge to a non-solution.
- ¶3 [caveat] (callout) The package's QPs carry no cardinality formulation; the limit is dropped without comment on every released version.
- ¶4 [caveat] (callout) Making the call fail would break old code, so it is proposed separately; the pinned build lacks it; appendix 93.
- ¶5 [claim] (callout) Three of five return an infeasible portfolio and none says so; the constraint prints but has no effect.
Note: ¶1 promises an inversion and withdraws it in the next sentence; ¶5 restates ¶2 and the opening and returns as a takeaway; the honoring and ignoring solvers are named only through inline R, never in the prose.

### Auditing the answer — 144

Says: A four-line `audit()` checks budget, sign and position count against what was requested.
Why here: Stated: the habit follows from the violation just shown and is the chapter's whole practical advice; chapter 14 takes the concentration functions.
Paragraphs:
- ¶1 [claim] The habit is the chapter's whole practical advice: never accept weights without checking they satisfy the request.
- (code: audit) `audit()`: budget, sign, position count; applied to the `ROI` result
- ¶2 [code] Four lines; `HHI()` and `diversification()` cover concentration, and chapter 14 uses them.
Note: The check runs on the unconstrained `ROI` result, which passes; it is never applied to the violating results one subsection back.

### Comparing specifications as one object — 100

Says: `combine.optimizations()` makes several results one object for the extract and chart functions.
Why here: Not stated.
Paragraphs:
- ¶1 [method] `combine.optimizations()` takes a named list and returns one object the chart and extract functions treat as one.
- (code: combine) `ROI` and `CVXR` combined; the first six weights printed
- ¶2 [code] `extractWeights()` gives a matrix, `extractObjectiveMeasures()` the objectives, `chart.RiskReward()` shared axes; published comparisons build it by hand.
Note: A package-API aside: nothing before or after uses the combined object, and the application does not refer to it.

## Why the Searches Fall Short — 787 (341 before the subsections)

Says: A random search covers a sixteen-dimensional simplex poorly, so more draws close only part of the gap at a growing cost; use a heuristic only when the problem forces it, and report its output as an estimate.
Why here: Contract position; builds on the race's `run()` and band; hands the band to chapter 14, whose risk budgeting is said to force a search.
Paragraphs:
- ¶1 [claim] One minimum and every downhill path reaches it; a search substitutes coverage for certainty, and the space is large.
- ¶2 [claim] The simplex's volume shrinks with N while directions grow, so coverage falls geometrically and each draw buys less.
- (code: budget) `random` at 20,000 and 100,000 draws; share and relative time
- (code: budget-claims) hidden: gap narrowed, more than one point still open, time rose
- ¶3 [result] Fivefold draws cost multiples of the time and closed part of the gap; darts on a wall; Gilli: report the spread.
- ¶4 [claim] Use a metaheuristic only when forced and treat it as an estimate; chapter 14's risk budgeting is forced, at this band.
Note: An argument with one experiment on the race's machinery, not a result on the modeled market; ¶1 restates the theory section's conclusion; ¶3 already makes Gilli's random-variable point that the next subsection is titled for; the band is read a second time.

### A heuristic's answer is a random variable — 258

Says: A search's output depends on the seed, so it is a distribution to report; three habits: record the seed, report the spread, start from the convex answer.
Why here: Builds on the single draw in tbl-13-race; otherwise not stated, and the parent's ¶3 has already made the point.
Paragraphs:
- ¶1 [claim] Convex solvers are deterministic; `DEoptim`, `pso`, `GenSA` start from a seeded random population, so the table's number is one draw.
- ¶2 [claim] Two specifications on one run each may differ only by seed; Gilli: ten or twenty runs, quote a range.
- ¶3 [transition] Three habits follow, none costing anything.
- ¶4 [method] Set and record the seed; an unreproducible backtest is not evidence.
- ¶5 [caveat] Report the spread, not the best draw; best-of-twenty is chapter 25's selection bias applied to solver runs.
- ¶6 [method] Seed the initial population with the convex answer; a global hunt becomes local refinement; not the package default.
Note: ¶2 repeats the parent's ¶3 (Gilli, repeated runs, the spread); no code, so the seed dependence is asserted, not measured, and goes to exercises 3 and 4; ¶3 is a one-sentence transition.

### Choosing, in three questions — 175

Says: Choose by three questions: is the problem convex; is the non-convexity in the objective or in the constraints; what is a heuristic's answer worth.
Why here: Closes the application as a decision rule; reads the band from tbl-13-race a third time and points to chapter 14 for the non-convex objective.
Paragraphs:
- ¶1 [transition] The decision needs no table of nine solvers.
- ¶2 [method] Convex objective and set: `ROI` for quadratic, `CVXR` for disciplined convex; exact, in seconds.
- ¶3 [method] Non-convex constraints: a mixed-integer solver via `Rglpk` certifies optimality; a non-convex objective, chapter 14's, leaves the heuristics.
- ¶4 [result] A heuristic is worth the race's band, with a spread to be measured; often good enough, never the same as solved.
Note: `Rglpk` and mixed-integer programming enter here as the exact route for cardinality, absent from the feasibility test and without a chapter 12 reference; "nine solvers" counts a set the chapter never lists (six raced, five tested).

## Key Takeaways — 212

Says: Convexity separates the families; the searches reach a band of the optimum and more draws close only part of the gap; cardinality is the legitimate reason for a heuristic; three of five violate an accepted limit; audit everything.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Convexity, not speed, separates the families; `ROI` and `CVXR` exact, a search can only approach.
- ¶2 [takeaway] Against the independent benchmark the searches reach the band, an order of magnitude slower.
- ¶3 [takeaway] Fivefold budget closed part of the gap at multiples of the cost; a sampler approaches, does not reach.
- ¶4 [takeaway] Cardinality constraints are genuinely non-convex and the legitimate reason for a heuristic [Bienstock].
- ¶5 [takeaway] Three of five violate the position limit they accepted, none warns; accepting and honoring differ.
- ¶6 [takeaway] Audit every result; four lines of checking stand between a specification and a portfolio that ignores it.
Note: Six bullets; the band, the budget numbers and the three-of-five count each appear for the fourth time; nothing on the seed habits or the three questions.

## Exercises — 144

Says: Five exercises: the race under a box cap, what `optimize.portfolio.parallel()` parallelizes, the violation across seeds, the distribution of a search's Sharpe, and the audit on the reader's own work.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Repeat the race with a 20 percent box cap; does the convex advantage survive, does the gap narrow.
- ¶2 [exercise] Read what `optimize.portfolio.parallel()` parallelizes; not the rebalancing loop of chapter 25.
- ¶3 [exercise] Run `pso` on the limited problem ten times with different seeds; is the violation deterministic.
- ¶4 [exercise] Following Gilli, `DEoptim` twenty times; report the distribution of the Sharpe against the gap.
- ¶5 [exercise] Put `audit()` into your own workflow and apply it to your last optimization.
Note: Five exercises; 3 and 4 measure what the random-variable subsection asserts; 2 is a help-page reading with no computation.
