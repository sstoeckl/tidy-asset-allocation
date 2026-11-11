---
file: chapters/24-benchmarks-and-active-risk.qmd
title: Benchmarks and Active Risk
part: Implementation and Evaluation
words: 7244
sections: 5
paragraphs: 52
---

# Chapter

Claim: Whether a portfolio beat its benchmark depends on the benchmark chosen and on what the mandate promised, and whether that was skill cannot be settled at this sample length: against one stated policy the book's minimum-variance manager has a negative information ratio, a positive alpha and a higher Sharpe ratio; a tracking-error budget alone buys dominated portfolios until total risk is bounded as well; the benchmark carries a bet of its own; and the information ratio's interval contains zero.
Question: Did the portfolio beat its benchmark, and if it did, was that skill; cites @grinold1989 for the modern form of the question (the fundamental law) and @grinold2000 for the vocabulary mandates are written in.
Why here: Stated only as a place on the horizon axis of ch. 3: the chapter is about evaluation rather than either horizon, and its one construction, the anchored allocation, is strategic because it tilts from ch. 15's policy. Takes the sixteen series and the hedged series from ch. 2, the dependence finding from ch. 4, the lagged capitalization proxy and the rolling betas from ch. 5, the estimation error from ch. 8, the Merton constants, eq-09-gmv, the frontier, dominance, the variance drag and the minimum-variance portfolio from ch. 9, group constraints from ch. 12, the four sleeves from ch. 15, the equal-weighting question from ch. 21, the back-fill and the turnover formula from ch. 23. Leans forward on ch. 25 five times as if already read: the register that ranks its manager, the rebalancing call, eq-25-brinson, the Ibbotson–Kaplan reminder, the intervals beside every Sharpe ratio. Names nothing a later chapter takes from it; why it stands between ch. 23 and ch. 25 is not stated.
Does: Measure a rebalanced portfolio against a policy with `PerformanceAnalytics` (tracking error, active premium, information ratio, capture ratios, alpha, beta, appraisal ratio, active share) on correctly aligned series; trace the tracking-error frontier in dual form with `PortfolioAnalytics` and under a budget and a total-risk bound with `CVXR`; attribute an active return by sleeve; put an interval on an information ratio.
Order: Opening; theory (the vocabulary and the fundamental law, the budget problem with Roll's solution and Jorion's repair, the Brinson decomposition, the standard error); implementation (the policy and the manager, the two return series, the measures, the package's active constraint, the `CVXR` budget, Jorion's bound); application (attribution by sleeve, two equity benchmarks, the error bar); takeaways; exercises. Deviations: the implementation is 47 percent of the chapter, reads its main results (the manager's three conflicting statistics, the tracking-error frontier, the anchored allocation) and holds its only figure; it turns halfway from measuring an out-of-sample manager to constructing an in-sample tilt without saying so; the implementation and application headings have no paragraph of their own; the application is three topics joined by a title and has no picture; the theory executes one chunk and reads it; six takeaways and four exercises.

# Sections

## Opening — 292

Says: Whether a portfolio beat its benchmark, and by skill, is the question of the fundamental law and its vocabulary; the chapter defines the vocabulary, implements and extends the measures, attributes the active return and puts an error bar on it.
Why here: Contract position; the sequence sentence gives the order: the vocabulary and what an information ratio estimates, then the measures, the package's gap and the `CVXR` build, then attribution, the benchmark as a bet and the error bar.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] Did it beat the benchmark, and was that skill; Grinold's law, and the vocabulary Grinold–Kahn fixed for every mandate.
- ¶2 [method] Order: vocabulary and standard error; measures, package gap, `CVXR` build; attribution, benchmark bet, error bar; evaluation, with one strategic construction.
- ¶3 [method] The sixteen classes of ch. 2: excess returns for moments, total returns for series, because compounding differs.
- (code: data) `R`, `rf`, `Re`; sixteen columns, no missing values and matching lengths asserted
Note: No visible packages block: the setup chunk is hidden and the shown chunk loads data. ¶2 is the roadmap and the placement on the horizon axis in two long sentences; for the theory it announces only the vocabulary and the standard error, not Roll's problem or the Brinson decomposition, and it says the budget and an information-ratio objective are both built in `CVXR`.

## Active Weights, Tracking Error, and the Information Ratio — 1269 (466 before the subsections)

Says: Active weights sum to zero, the tracking error is the volatility of the active return, and the information ratio is the Sharpe ratio with the benchmark in place of the bill; the fundamental law says how much forecasting skill a given ratio needs, and at a breadth of sixteen that is a great deal.
Why here: Stated in the opening: the vocabulary is defined first. Takes ch. 23's turnover formula for active share and sends the beta-adjusted variant to the application, where the beta is treated as an estimate.
Paragraphs:
- ¶1 [definition] Active weights sum to zero (eq-24-active); active return, alpha, tracking error (eq-24-te); information ratio (eq-24-ir); appraisal ratio as beta-adjusted cousin.
- ¶2 [claim] The fundamental law (eq-24-law) with the transfer coefficient; breadth sixteen demands a high coefficient; Sharpe's arithmetic of active management.
- ¶3 [definition] Active share measures the deviation in holdings: ch. 23's turnover formula against the benchmark; it can disagree with tracking error.
Note: ¶1 is one sentence chain across three numbered equations, ending on two older ratios and four citations; ¶2 does three jobs (the law, the sixteen-class number, Sharpe's arithmetic), and its "thirty times smaller" is typed rather than computed: by eq-24-law the two coefficients differ by √(1000/16), about eight. Active share is defined inline, without a numbered equation, though the implementation computes it.

### Tracking error as a constraint — 321

Says: A mandate sets a tracking-error budget rather than asking for the maximal information ratio; Roll's solution adds the same long-short tilt to any benchmark, so the total portfolio is efficient only if the benchmark was, and the information ratio is constant along the family; Jorion's bound on total risk repairs the first, and the result is a cone program.
Why here: Stated in its first two sentences: mandates give a budget, not a ratio. Needs the Merton constants and eq-09-gmv from ch. 9; hands the cone program to the implementation, on the stated ground that the package lacks it.
Paragraphs:
- ¶1 [derivation] Roll's problem and closed form; the tilt ignores the benchmark; the ratio is constant; Jorion's total-risk bound; a cone program.
Note: The whole subsection is one paragraph: a sentence chain of about 320 words across five numbered equations doing six jobs (problem, closed form, the benchmark-free direction, the constant ratio, the repair, the solver class). The derivation is said to be "two lines" and is not shown, with no pointer to the proofs appendix.

### Where the active return came from — 205

Says: The Brinson decomposition splits one period's active return into allocation, selection and an interaction term with no decision behind it; the form used keeps the benchmark's return in the allocation term so that the signs by segment mean something.
Why here: Stated only as sequence: once an active return is earned, the question is which decisions earned it. Why it stands between the budget problem and the standard error is not stated; the application's first subsection applies it.
Paragraphs:
- ¶1 [definition] Segment weights and returns; Brinson's decomposition of one period's active return into allocation, selection and interaction (eq-24-brinson).
- ¶2 [definition] What each term rewards; ch. 25 writes allocation differently, same total; Brinson's pension study; the Ibbotson–Kaplan reminder.
Note: ¶2 leans forward on ch. 25 twice (eq-25-brinson, and a reminder "made in" its application) as if already read; the segment benchmark return is written β_s in a chapter whose other betas are regression slopes.

### What an information ratio is estimating — 277

Says: An information ratio has the standard error of a Sharpe ratio, so a ratio of one half needs about sixteen years of monthly data to stand two standard errors from zero, and a beta-adjusted ratio adds the error of the beta.
Why here: Announced in the opening as the theory's second question. Needs ch. 4's dependence finding and ch. 5's rolling betas; the error-bar subsection applies eq-24-se and recomputes the betas. Why it comes after attribution and not after the ratio's definition is not stated.
Paragraphs:
- ¶1 [definition] An information ratio has a Sharpe ratio's standard error; Lo's formula (eq-24-se); Goodwin on the ratios reported in practice.
- (code: months-needed) `months_needed()`: months until a t-statistic of two; printed for an annual ratio of one half
- ¶2 [result] One half needs about sixteen years of months; dependence widens that; the appraisal ratio adds an unstable beta.
Note: The theory's only chunk, with its result read in place; ¶2 carries the count, two caveats and a forward pointer to the application; ¶1 closes on a four-word verdict sentence that only introduces the chunk. The appraisal ratio, defined in the section's first paragraph as alpha over residual volatility, is said here, and again in the error bar, to divide by a beta.

## Implementation — 3417 (0 before the subsections)

Says: (heading only)
Why here: Contract position; the opening says the measures, the package's gap and the `CVXR` build follow the theory.
Paragraphs: none of its own.
Note: Heading only; six subsections and 47 percent of the chapter. The first three measure a manager out of sample, the last three construct a tilt from full-sample moments, and no sentence marks the turn; the section reads the chapter's main results and holds its only figure.

### A policy portfolio and a manager — 418

Says: The benchmark is a stated four-sleeve policy with equal weights inside each sleeve, and the manager measured against it is the book's rolling long-only minimum-variance portfolio.
Why here: Stated in its first sentence: a benchmark has to be chosen before anything can be measured against it. Needs ch. 15's sleeves and ch. 9's minimum-variance portfolio; takes the manager's rank and its rebalancing call from ch. 25.
Paragraphs:
- ¶1 [method] A policy over ch. 15's four sleeves, equal weights inside; stated rather than estimated, and not imported from ch. 15.
- (code: policy) `sleeve_of()`; sleeve weights 50/30/15/5; `b` indexed by name; sum and names asserted
- (code: tbl-24-policy) hidden; sleeve, members, sleeve weight, weight per class
- (code: register-rank) hidden; reads ch. 25's register; minimum variance asserted second by Sharpe ratio
- ¶2 [method] The manager: ch. 9's long-only minimum variance on sixty trailing months; active because it ignores means; solver failures asserted.
- (code: active-portfolio) `optimize.portfolio.rebalancing()` monthly on a sixty-month window; convergence asserted in every period; rebalance count and first date
Note: The policy table is shown and no paragraph reads it; the four sleeve weights are typed in code and nowhere argued. The manager is defined through ch. 25 twice (its rank in the register, the call that chapter "dissects"), a chapter not yet reached. ¶1 keeps the policy independent of ch. 15, while the opening and the section's last paragraph call it ch. 15's allocation.

### Two return series, and the trap between them — 259

Says: `Return.portfolio()` back-fills an equally weighted portfolio for the months before the first weight vector, so both series are cut to the months a weight vector precedes and the accounting is asserted by hand.
Why here: Not stated beyond sequence: the weight history has to become a return series before anything is measured. Needs ch. 23's back-fill trap, "met from the other side".
Paragraphs:
- ¶1 [code] `Return.portfolio()` turns weights into returns; the first weight vector is dated month sixty, the data begin at month one.
- (code: backfill) the warning from `Return.portfolio()` on the full sample, caught and printed
- ¶2 [caveat] (callout) Ch. 23's trap again: the first months are an equal-weight portfolio nobody chose; cut both series, assert the accounting.
- (code: returns) `R_oos`, `rf_oos`; `Rp`, `Rb`; both asserted against weights times returns; the active return `a`; months and first date
Note: The two series of the title and the active-return series `a`, the object every later measure is taken on, are built after the callout in a chunk no paragraph reads, and the subsection ends on it.

### The measures in PerformanceAnalytics — 730

Says: Every measure exists as a function of the two series; the default information ratio mixes a compounded numerator with an arithmetic denominator; the manager has a negative information ratio, a positive alpha and appraisal ratio and a higher Sharpe ratio than the policy, because the statistics compare it with different things.
Why here: Stated in the opening (the measures are implemented in `PerformanceAnalytics`); needs the two series just built; its negative ratio is what the attribution and the error bar later work on.
Paragraphs:
- ¶1 [code] Everything in eq-24-te and eq-24-ir exists as a function taking the two series.
- (code: measures) `TrackingError()`, `ActivePremium()`, `InformationRatio()` default and arithmetic; by-hand ratio asserted equal; negative sign asserted
- ¶2 [caveat] (callout) Default: a compounded premium over an arithmetic volatility; `geometric = FALSE` gives eq-24-ir; the gap grows with volatility differences.
- ¶3 [result] Tracking error beyond any mandate's budget; a negative information ratio; the manager earned less than the policy.
- (code: capture) `table.CaptureRatios()`, `UpDownRatios()`: up and down capture, shares of months
- ¶4 [result] Up and down capture read as a low-volatility portfolio against an equity-heavy one; both say what the beta says.
- (code: capm) `CAPM.beta()`, `CAPM.alpha()`, `AppraisalRatio()` against the policy; the three signs asserted
- (code: tbl-24-capm) hidden; `table.CAPM()` against the policy
- ¶5 [claim] Positive alpha and appraisal ratio, negative information ratio: two questions; which answer counts depends on the mandate.
- (code: sharpe-both) `table.AnnualizedReturns()` for both series; the manager's Sharpe ratio asserted higher
- ¶6 [claim] A higher Sharpe ratio with a negative information ratio is Roll read backwards: the benchmark is not efficient.
- (code: active-share) active share at each rebalance against `b`; mean, lowest, highest
- ¶7 [result] Average active share on Cremers–Petajisto's scale: the portfolio shares a universe with its benchmark and little else.
Note: The chapter's central empirical result (¶5, ¶6) is read here, in the implementation; ¶6 calls the benchmark inefficient two subsections before the Jorion table measures it. The `table.CAPM()` table is printed and never referenced by label, its robust rows named only in the caption. ¶3 and ¶6 each end on a sentence that only introduces the next chunk; "a quarter" of the beta is typed beside the computed beta.

### Active weights in PortfolioAnalytics — 512

Says: The package's `active` weight-sum type only sets the sum to zero; with a hand-shifted box and a return target it traces Roll's frontier in dual form, and it cannot express a tracking-error budget, a second quadratic constraint, an information-ratio objective or the benchmark itself.
Why here: Announced in the opening (the package has the constraint but neither budget nor ratio objective); the callout's list is the stated reason for the next subsection, since each missing piece "has to be built".
Paragraphs:
- ¶1 [caveat] `type = "active"` only zeroes the weight sum, like `dollar_neutral`; the box is shifted by hand to stay long-only.
- (code: active-sum) `spec_active`: active sum, box shifted by `b`, variance objective; the constraint's type and sums printed
- ¶2 [method] A return target on top minimizes tracking error at that active return: eq-24-roll in dual form, traced over targets.
- (code: roll-dual) `mu`, `S` and four helper functions; `min_te_at()`; eight targets; target, zero sum and zero minimum weight asserted
- ¶3 [result] Every target hit, active weights sum to zero, the long-only bound binds throughout; the closed form "will explain".
- ¶4 [caveat] (callout) Missing: a budget constraint, a second quadratic constraint, an information-ratio objective; and the package never knows the benchmark.
Note: Here the chapter turns from measuring the manager to constructing an active portfolio, without a sentence saying so; `mu`, `S` and the helpers every later chunk uses are defined inside the dual chunk, and that they are full-sample moments is said only at the section's end. The callout announces "three things" and lists a fourth.

### The tracking-error budget, built — 786

Says: Roll's problem with a long-only constraint is a few lines of `CVXR`; primal and dual agree, the closed form holds up to the budget at which the first weight reaches zero, and beyond it the information ratio falls with every budget while the gap to the mean-variance frontier measures Roll's inefficiency.
Why here: Stated: the theory handed the cone program to the implementation because the package lacks it, and the callout before it says each missing piece has to be built.
Paragraphs:
- ¶1 [method] eq-24-roll, long-only, optionally with eq-24-jorion, in `CVXR`; status asserted, since a failed solve still returns numbers.
- (code: te-tilt) `te_tilt()` with `CLARABEL`, status asserted; ten budgets; `te_frontier` with ratio, volatility, holdings, active share
- ¶2 [method] Primal and dual are one problem: at the dual's tracking error the primal must reach the same target.
- (code: primal-dual-check) the third dual row; primal active return asserted equal to the target
- ¶3 [transition] The closed form can be checked the same way, and the check says how far it reaches.
- (code: closed-form) `A`, `B`, `C`; Roll's direction, dollar-neutral asserted; the maximal ratio; binding budget and class; closed form against solver asserted
- ¶4 [result] Below the binding budget both deliver the maximal ratio; there one class reaches zero; beyond it the ratio falls.
- (code: tbl-24-te-frontier) hidden; builds the long-only mean-variance frontier and `frontier_ret_at()`; the gap column; falling ratio and shrinking holdings asserted
- ¶5 [result] Down the table the ratio falls with the transfer coefficient, holdings shrink to a corner; the gap is Roll's inefficiency.
Note: The mean-variance frontier that the gap column, the Jorion table and the figure all rest on is built inside a hidden table chunk, and how the gap is computed is said only in the caption. The information-ratio objective the opening announced is not built; the maximal ratio appears as a by-product of the budget problem below the binding budget. ¶5 reads the falling ratio as the transfer coefficient, which no chunk computes.

### Jorion's repair, and the anchored allocation — 709

Says: With total risk bounded at the benchmark's own volatility, a four percent budget buys less active return and a lower information ratio but a higher Sharpe ratio and a portfolio closer to the frontier; this anchored formulation is how a strategic allocation is run in practice, and all of it is in sample.
Why here: Stated in the theory: Jorion's bound repairs the inefficiency, which the previous table has just measured. The title's second half is the construction the opening named as the chapter's one strategic contribution.
Paragraphs:
- ¶1 [method] Add eq-24-jorion with the bound at the benchmark's volatility: a four percent budget that may not raise total risk.
- (code: jorion) `w_roll` and `w_jorion` at a four percent budget
- (code: tbl-24-jorion) hidden; `describe()`; policy, Roll, Jorion; the benchmark's inefficiency and three orderings asserted
- ¶2 [result] The benchmark is not efficient; the budget alone raises Sharpe ratio and volatility; Jorion's bound lands nearer the frontier.
- (code: fig-24-te-frontier) hidden; one data frame; both frontiers, the anchor, the two four-percent solutions, the total-risk bound
- ¶3 [claim] The anchored formulation is how strategic allocation runs in practice: anchor, budget, total-risk bound; all of it in sample.
Note: The chapter's only figure closes the implementation and no sentence reads it: ¶3 mentions it once, to say it is in sample. The anchored allocation, the one construction the opening claims for the chapter, gets this single closing paragraph and never meets the out-of-sample months the manager was measured on. The Jorion table is never referenced by label.

## Attribution, the Benchmark Bet, and the Error Bar — 1748 (0 before the subsections)

Says: (heading only)
Why here: Contract position; the opening's sequence sentence ends on these three items in this order.
Paragraphs: none of its own.
Note: Heading only, and the title is a list: three subsections of similar size that share the manager and the policy but not an argument. No picture opens the application, which has no figure at all.

### Where the active return came from, by sleeve — 624

Says: The manager's shortfall is an allocation result: holding more government bonds and fewer equities than the policy cost more than the whole shortfall and selection gave part of it back; the decomposition sees neither a decision behind the interaction term nor the currency inside each sleeve.
Why here: Not stated beyond the opening's order; needs eq-24-brinson, the sleeves of the policy table, and the weights and active return built in the implementation.
Paragraphs:
- ¶1 [method] What eq-24-brinson needs each month: sleeve weights held, sleeve returns as held and at policy weights; four sleeves.
- (code: brinson) `brinson_month()`; the identity asserted every month against `a`; annualized average effects; average holdings by sleeve
- (code: tbl-24-brinson) hidden; held, policy, allocation, selection, interaction, total, by sleeve and overall
- (code: attribution-readout) hidden; the assertions behind the prose: the total, allocation beyond the total, selection positive and smaller in every sleeve
- ¶2 [result] Allocation cost more than the shortfall, selection returned part; more government, fewer equities; Brinson's result, the Ibbotson–Kaplan warning.
- ¶3 [caveat] Interaction has no decision behind it; unhedged series book currency under the sleeve; Karnosky–Singer's form would separate it.
Note: The heading repeats the theory subsection's title with two words added. ¶2 is one block carrying the total, two effects, four weights, the sample explanation and two citations; the Brinson table is referenced by label only from exercise 1; the currency-aware decomposition is named and not run.

### The benchmark is a bet — 559

Says: Equal and capitalization weighting of the same five equity markets are two different yardsticks, with a tracking error against each other larger than most mandates' budgets; the equal-weighted sleeve is a standing underweight of the largest market, so the benchmark carries a bet before the manager makes any.
Why here: Not stated; takes the policy's equity sleeve from the implementation and ch. 5's lagged capitalization weights, uses nothing from the attribution before it, and hands the rebuilt weights to the error bar. Whether the bet is a good one is sent back to ch. 21.
Paragraphs:
- ¶1 [claim] Equal or capitalization weights is a decision the yardstick makes first; weights lagged one month, as ch. 5's proxy.
- (code: cap-weights) equity instruments and weekly market values; weights from the last value before each month; regional shares, averaged
- (code: two-benchmarks) both equity series; return, volatility, Sharpe ratio; tracking error between them; the size bet by market; four orderings asserted
- (code: tbl-24-two-benchmarks) hidden; the two benchmarks and the tracking error between them
- (code: size-bet) the equal-weighted sleeve's overweight by market
- ¶2 [result] Their mutual tracking error exceeds typical budgets; capitalization weighting earned more; equal weighting bets permanently against the largest market.
Note: Four chunks between two paragraphs. The table's caption describes a last column of overweights by market that the table does not have (the next chunk prints them raw), and exercise 4 cites the table for that bet. The manager is not measured against the second benchmark here, which is left to exercise 4; an information ratio between the two benchmarks is computed and never shown.

### The error bar — 555

Says: Betas move across rolling windows, the manager's beta to the policy among them, so the appraisal ratio divides by a number that is not constant; the information ratio needs no beta, and its interval over the sample contains zero, which is what the standard error says to expect at this length.
Why here: Stated in the theory: the beta numbers are recomputed where the market proxy is rebuilt, so it follows the benchmark subsection; it closes the chapter by applying eq-24-se to the opening's second question.
Paragraphs:
- ¶1 [claim] The rebuilt proxy is ch. 5's and mostly one market, so a beta on it is too; it moves.
- (code: beta-instability) the proxy; `roll_beta()`; one class beta's travel, two classes' sign flips; the manager's rolling beta to the policy
- ¶2 [result] Class betas travel and flip sign, Blume's regularity; the manager's beta ranges too, so the appraisal ratio's divisor moves.
- (code: error-bar) the monthly ratio, Lo's standard error, the 95 percent interval; a negative ratio and an interval containing zero asserted
- ¶3 [result] The interval contains zero and understates the truth; no evidence of skill either way; the test for a difference named.
Note: Two error bars under one heading. The first half recomputes ch. 5's class betas against an equity proxy the manager is never measured against, and the beta the appraisal ratio actually divides by gets one sentence. ¶3 is one block of about 200 words holding the chapter's answer, three justifications and a named test whose outcome ("widens nothing here") no chunk computes.

## Key Takeaways — 297

Says: Active weights are long-short and the law prices skill; a budget alone is inefficient and a total-risk bound repairs it; what the package has and lacks; the default information ratio and its disagreement with the Sharpe ratio; the benchmark as a decision; the years an information ratio needs.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Active weights sum to zero, hence long-short; tracking error, the ratio, the law; sixteen classes need a high coefficient.
- ¶2 [takeaway] A budget alone gives inefficient portfolios, the tilt ignoring the benchmark; a total-risk bound repairs it, near the frontier.
- ¶3 [takeaway] The `active` type only zeroes the sum; the dual gives Roll's frontier; budget, second constraint, ratio objective need `CVXR`.
- ¶4 [takeaway] Default `InformationRatio()` mixes compounded and arithmetic; a higher Sharpe ratio and a negative information ratio can describe one portfolio.
- ¶5 [takeaway] The benchmark is a decision: equal and capitalization weights differ by a large tracking error and a standing bet.
- ¶6 [takeaway] A ratio of one half needs about sixteen years of months; this manager's interval still contains zero.
Note: Six bullets. None covers the attribution result, the back-fill trap, active share or the moving beta behind the appraisal ratio. ¶3 says an information-ratio objective is "a few lines" of `CVXR`, which the chapter never writes; ¶5 cites Cremers–Petajisto, whom the body cites for active share and not for the choice of benchmark; ¶1 and ¶4 each hold two separate points.

## Exercises — 175

Says: Four exercises: an equally weighted policy and what it does to the attribution, Jorion's bound at a looser level across three budgets, the information ratio of equal weighting with its interval, and a capitalization-weighted equity sleeve in the policy.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Equal weight over the sixteen as policy; recompute tracking error, ratio and attribution; why the change lands in allocation.
- ¶2 [exercise] Jorion's bound at 1.1 times benchmark volatility for three budgets; position against the frontier; where the bound stops binding.
- ¶3 [exercise] Equal weighting's information ratio against the policy with its interval; distinguishable from zero, and from the manager's.
- ¶4 [exercise] Rebuild the policy with a capitalization-weighted equity sleeve; does the manager's ratio improve; who bears the size bet.
Note: Four exercises, each a rerun with one input changed. Exercise 3's second question calls for the test for a difference between two ratios, which the chapter names and does not compute; exercise 4 points to a table column that does not exist; none touches the fundamental law, the dual trace, active share or the capture ratios.
