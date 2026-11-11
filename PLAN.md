# The claim register

What each chapter will assert, the number that proves it, and whether that
number exists yet. This is the coordinating document: the `PLANNING NOTE` in
each stub is the local pointer and is deleted when the chapter is written, but
the entry here survives and becomes the record of what the book claims.

> **Status 2026-11-11.** All 28 chapters and the ten appendices are written on
> dataset 6.2.0 and the model calendar; every chapter and solutions file
> executes (`tools/run-chapter.R`) and was read against a knit with its inline
> numbers (`tools/knit-chapter.R`). **The chapters are now the authority on
> every number**; this register has not been re-pinned claim by claim and its
> figures are stale. The 6.2.0 register (window 60, monthly, gross, out of
> sample from observation 121): min-CVaR 0.89, min-variance 0.83, 1/N 0.63,
> inverse-vol 0.57, tangency 0.55; at 120 months the tangency portfolio is third.
>
> **Read this first (2026-11-09).** The numbers below were measured on older
> exports (4.3.0, some on 5.1.0) and are **stale** until the final re-pin on
> dataset 6.2.0: treat every one as a claim to recompute, never as a number to
> copy. The market runs on a model calendar (`CLAUDE.md`, "The calendar rule"):
> no calendar years, no dated events, episodes from `sim_episodes`.

**Status marks**

| | |
|---|---|
| `[ok]` | measured and independently checked. The number is quoted here as it will be printed. |
| `[open]` | a bet. Plausible, not yet computed. Everything here can still die. |
| `[drop]` | died, with the reason, so it does not come back. |

Arrows (`→`) mark where a claim is set up in one chapter and resolved in
another. Those are the dependencies worth checking before writing anything.

All numbers are on the simulated market, version 4.3.0, 21 class series over
372 months, model years 1 to 31, USD unhedged. The risky set is the 16 series
after dropping the money markets.

**Renumbered 2026-09-12** onto the table of contents in `RESTRUCTURE.md`.
Claims are carried verbatim; only headings, order and the `→` arrows moved.
A restructured export is coming in which the 16 risky series are the file
and the money market is the risk-free rate beside it: the claims that die
with it are listed in `CLAUDE.md`.

---

## Part I · Prerequisites


### 01 · Setting Up Your Environment

**Q** What do you need installed, and how do tibbles and xts coexist?
**M** tidyverse, xts, zoo, `as_pm()`, `as_xts_pm()`

- `[ok]` `PortfolioAnalytics` has 115 exports, one bundled dataset and no download
  function whatsoever. A package this large invites the assumption that it
  handles its own inputs; it does not.
- `[ok]` About twelve of those exports are `_v1`/`_v2` legacy shims
  (`add.objective_v1`, `constraint_v2`, `optimize.portfolio_v1`,
  `update_constraint_v1tov2`). This is why old Stack Overflow answers fail.
- `[open]` The tibble/xts boundary has exactly three failure modes worth naming:
  ragged padding, column order, duplicate keys. All three are documented in
  `?pm-coercion`; the chapter needs a worked instance of each.
- `[open]` Beat 4: why a returns matrix with a date index is the natural object.


---

### 02 · Notation and Data — **new**
**Q** What are the symbols, and what is in the data?

- `[open]` New chapter, agreed 2026-09-12. Fixes notation once, describes both
  universes, and carries the asset-class naming table.
- `[open]` The class universe is 5 currencies x (government, corporate, equity)
  plus alternatives in USD = 16 risky series, with the money market carried
  separately as the risk-free rate. → 03


## Part II · Foundations of Portfolio Choice


### 03 · Return, Risk, and the Investor's Problem

**Q** Whose money, over what horizon, in which currency, nominal or real?
**M** PerformanceAnalytics, `quadratic_utility_objective()`, `to_real()`, `hedge_currency()`

- `[ok]` `risk_aversion` in `PortfolioAnalytics` is **γ/2**, not γ. The source
  builds `Q = 2·lambda·Sigma` into an objective ROI reads as `½x'Qx`. Verified by
  numerical fit: ratio exactly 2.000 at every level. Undocumented upstream. → 09
- `[ok]` Raising γ under full investment converges to GMV, not to cash: volatility
  falls 24.1% → 0.68% and stops at the GMV level. Relax full investment and the
  invested fraction scales as 1/γ — 36.5% at γ=100, 0.04% at γ=100,000.
- `[ok]` A constant risk-free column makes Σ singular. That is why two-fund
  separation treats the risk-free asset separately instead of as another column,
  and it is a mistake every reader makes once.
- `[open]` **This chapter carries more weight than its stub suggests.** The user's
  point: SAA is the investor's objective applied to long-run assumptions.
  Constraints are guardrails, not the driver. → 09, 12, 11
- `[open]` Excess returns are the right basis, and not only for tidiness: with
  total returns the objective treats uninvested money as earning zero, which is
  false. With excess returns it earns exactly zero excess, which is true. Under
  rebalancing the rate moves, so only the excess formulation is time-consistent.
- `[open]` The measure must match the objective. Optimise CVaR, report Sharpe, and
  you have misreported. → 10, 24, 25


### 04 · Descriptive Analysis of Asset Returns — **written**

**Q** What does this market look like, and which of its properties can you rely on?

- `[ok]` The Sharpe ranking is not the return ranking. `US_credit` earns 5.67%
  against `US_equity`'s 7.76% and ranks above it, 0.493 to 0.382.
- `[ok]` `US_money_market` is not cash: negative in 38% of months, −10.5%
  drawdown, Sharpe −1.42 against the bill. → 03, 09
- `[ok]` 20 of 21 series reject normality. The survivor is `JP_equity`, the most
  volatile risky series in the set (JB p = 0.0503).
- `[ok]` Cornish-Fisher against historical ES at 95%: `US_credit` 2.2× apart,
  `US_equity` 1.15×. A Gaussian risk model is roughly right for equities and
  roughly half right for credit. → 10
- `[ok]` Fat tails are events, not a distribution. Months with ≥5 of 16 series
  beyond 2.5 sd: 5 observed, 0.01 expected under independence. The worst month of the credit crisis puts
  13 of 16 over the line.
- `[ok]` Volatility is the only estimable moment: rolling IQR ≈ 30% of level,
  zero sign flips in 313 windows. The mean wanders by more than its own level;
  skewness flips sign in ~34% of windows. → 08
- `[ok]` Credit crisis: `US_government` +7.5%, `JP_government` +14.2%, `US_equity` −45.6%.
  Rates shock: every risky series negative except `GLOBAL_commodity` at +11.8%. A book
  that teaches diversification from the credit crisis alone teaches a rule that reverses in a
  third of the sample. → 25
- `[ok]` Average pairwise correlation: calm 0.302, credit crisis 0.511, rates shock 0.635, liquidity shock
  0.721. Stated with degrees of freedom, because 3- and 7-month windows are
  descriptions, not estimates. → 19
- `[ok]` Currency is asset-specific, not country-specific. `JP_equity` measures a
  0.9% currency share against 19.6% if independent — the exporters hedge it for
  you. `JP_government` is 91.8%. Hedging takes `JP_government` from 10.72% to
  3.07% volatility and `JP_equity` from 22.79% to 22.68%. → 15, 22
- `[ok]` Beat 3: `table.Drawdowns()` gives the episodes, not just the depth. Seven
  of 21 series end the sample still inside their deepest drawdown.


### 05 · Factor Models and Beta Estimation — **written**

**Q** What explains these returns, and how much of that explanation survives being measured?

- `[ok]` The "global" market proxy is 57% US on average and 70% at the end of the sample. Every
  beta in the book is largely a US beta; say so or the concentration is invisible.
- `[ok]` One factor explains four series and fails on seventeen. Median R² 0.096;
  `JP_government` at 0.000015. Bonds with significant alpha against an equity
  market is the model announcing it has the wrong factors. → 06
- `[ok]` The unconditional beta of `JP_government` is −0.002 because +0.181 up and
  −0.331 down cancel. A single number destroys the only interesting property.
- `[ok]` Only 3 of 21 asymmetries survive Newey-West inference. `US_credit`, the
  one an allocator most wants, does not: t = 0.83, p = 0.41. Present bull/bear
  splits as a diagnostic, never as evidence. → 10
- `[ok]` A global capitalisation sort is a region bet: the big leg is 70% US, the
  small leg 10%. Median R² 0.096 → 0.155 with global SMB, → 0.101 region-neutral.
  A factor is defined by its construction. → 21
- `[ok]` A small beta is not a stable beta. Sign flips across 313 windows:
  `JP_money_market` 51%, `JP_government` 49%, all five equity classes 0%. → 08, 24
- `[ok]` Excursus: turbulence peaks at 2.23 in the worst month of the credit crisis, more than twice the
  next month — the same month the outlier count picked out, but as one number
  and without hindsight. → 19
- `[open]` Momentum: WML earns 5.9% p.a. (t = 2.56) on its own, but no class
  series loads on it with |t| > 2. An instrument-level phenomenon that does not
  survive aggregation. Report and drop.


---

## Part III · Estimating the Inputs


### 06 · Expected Returns

**Q** Where do the numbers in mu come from?
**M** `set.portfolio.moments()`, `black.litterman()`, `equilibrium_returns()`

- `[open]` Sample means over 372 months still have standard errors large enough
  that the rolling estimate wanders by more than its own level (measured in 02).
  Quantify what that does to a target return.
- `[open]` Reverse optimisation: what expected returns make the current market
  portfolio optimal? Needs capitalisation weights for all assets — we have them
  for equities only. **Blocking issue for a full multi-asset equilibrium.** → 17
- `[open]` Black-Litterman as a shrinkage device rather than a view device.
- `[open]` Beat 3: one unused capability in `set.portfolio.moments()`.


### 07 · The Covariance Matrix

**Q** Sigma has far too many free parameters. What do you do about it?
**M** `statistical.factor.model()`, `custom.covRob.*()`, `CCCgarch.MM()`, `extractCovariance()`

- `[ok]` At class level the problem does not exist: 16 assets, 372 months,
  smallest eigenvalue 1.1e-06, every rolling window invertible.
- `[ok]` At instrument level it is fatal. 123 equities over a 120-month window
  give rank ≤ 120: minimum variance has no solution, and the sweep failed in all
  twelve instrument configurations for exactly this reason. **This chapter must
  introduce shrinkage before chapter 18 needs it.** → 21, 22, 25
- `[ok]` The commodity block was rank 1 of 8 in export 4.1.0 and is rank 8 of 8 in
  4.2.1. A covariance matrix can be singular for reasons that have nothing to do
  with N and T.
- `[open]` Ledoit-Wolf against sample against a factor structure, on the 123
  equities, scored out of sample rather than in.
- `[open]` Eigenvalue concentration moves: PC1 share 0.385 calm, 0.602 crisis;
  effective bets 7.05 → 3.98. Shrinkage towards what, when the target moves? → 19


### 08 · Estimation Error and Its Cost

**Q** A better forecast is worth how much, in Sharpe ratio?
**M** `equal.weight()`, `inverse.volatility.weight()`, `sharpe_gap()`

- `[ok]` 1/N sets a hard benchmark: OOS Sharpe 0.387 from model year 11, and it is
  identical across estimation windows because it estimates nothing. That row is
  the control that reveals a confounded comparison.
- `[ok]` Only one optimiser beats it, and only with a long window: minimum
  variance at 120 months, 0.440. Max-Sharpe never gets close — best 0.292.
- `[ok]` More data helps the optimisers: min-variance 0.360 → 0.440 and
  max-Sharpe 0.232 → 0.292 going from 60 to 120 months.
- `[open]` **RAFE belongs here, stated intuitively with one number.** The user's
  position: if estimation error decides outcomes, the measure of it cannot be
  optional. The formal treatment stays in 23. → 26, 27
- `[open]` R² and out-of-sample R² against economic value: a better fit is not a
  better portfolio. Needs a forecasting example — depends on 14.


---

## Part IV · Portfolio Optimization


### 09 · Mean-Variance Optimization — **written; first chapter on the new contract**

**Q** What does the textbook answer look like on the asset classes?

- `[ok]` GMV holds 4 positions at 4.14% volatility, 84% of it `US_government`.
  The tangency holds 6, still 59% `US_government`.
- `[ok]` The optimiser buys the asymmetry: the tangency holds 13.6% `US_credit`,
  the series with skewness −1.49 and the single worst month in the data. Variance
  cannot see it. → 10
- `[ok]` The tangency comes from the frontier, never from `maxSR`. Best frontier
  point matches the analytic long-only tangency to L1 0.0019; `maxSR` with a
  `momentFUN` on unpatched CRAN gives 0.1173 against an attainable 0.2058, and
  `NA` if the inputs are already excess returns. → 13, 93
- `[ok]` `full_investment` fails in 37 of 312 rolling windows on CRAN, silently,
  returning NA weights. Fixed on the fork. → 93
- `[ok]` OOS preview: tangency 0.232 against 1/N 0.387. The most beautiful picture
  in finance is the worst backtest in the book. → 08, 25
- `[ok]` The left end is stable and the right is not. Block bootstrap, 200 draws,
  zero solver failures: mean turnover from the full-sample answer is 0.054 for
  minimum variance and 0.293 for the tangency — **a factor of 5.5**, against a bet
  of 3. In the worst twentieth of draws the tangency asks to trade 67% of the
  portfolio; minimum variance never exceeds 10%.
- `[ok]` **Diversification effort and diversification payoff are unrelated.**
  Across the sixteen mixed classes (mean correlation 0.35) minimum variance holds
  1.41 effective positions, because 84% of it is `US_government`. Among the five
  equity classes (0.57), where nothing is quiet, it holds 3.09 of five. Twice the
  diversification, and the same discount: 12.5% below the quietest constituent
  against 13.4%. → 14, 15
- `[ok]` The claim generalises. 521 random sub-universes of size 3 to 16: median
  discount 11.7%, and **not one** of the 521 leaves the band 1% to 28%. The
  quietest available asset alone explains **98%** of the variation in the log
  minimum-variance level; average correlation alone explains **7%**; both plus the
  size of the universe reach 99%. Choose the universe and you have chosen the
  answer to within about an eighth. → 07, 08, 15
- `[ok]` The equity frontier is the mixed frontier's top-right stub, not a smaller
  copy. Both terminate at the same point, because the highest-return asset in the
  mixed universe is an equity market. The eleven non-equity series add nothing
  above; they extend the left end from 15.8% volatility down to 4.1%.
- `[ok]` The out-of-sample column of @tbl-07-oos is read from
  `output/tables/oos-sweep.csv` rather than recomputed, so 07 and 22 cannot drift.
  The tangency keeps 32% of its promised Sharpe, equal weighting keeps 93% and
  finishes first. → 25
- `[ok]` `ef$frontier` carries a class attribute, so `as.data.frame()` returns one
  column of 3,762 numbers instead of 198 rows of 19. Documented in the chapter —
  I reproduced this bug while rewriting the chapter that documents it.
- `[ok]` **Contrast universe: the five equity classes.** Settled by the user, no
  longer provisional; the ten French industries are dropped so the chapter stays
  inside one universe.
- `[drop]` "The naive `maxSR` call beats the careful one." Measured against the
  excess-return tangency when the naive call correctly targets the total-return
  one. Retracted.
- `[coord]` **Overlap with 11.** The CVXR/CLARABEL silent failure and the
  two-element `optimize_method` currently sit in 07's beat 2, but they are solver
  material and 11 owns solvers. Either 07 shortens to a pointer, or 11 takes a
  different beat 2. **Decide before writing 11.**


### 10 · Risk Measures Beyond Variance

**Q** Variance is a choice. What changes if you pick something else?
**M** ES, ETL, CVaR, VaR, mES, CSM, EQS, `meanetl.efficient.frontier()`

- `[ok]` Same data, same constraints, four objectives, and the `US_credit` weight
  runs 0.0% / 48.2% / 9.3% / 0.0%. Minimum-ES is the only one with positive
  portfolio skewness; quadratic utility at λ=2 gives skewness −1.43 and a −37%
  drawdown. → 03, 11
- `[ok]` **Minimum CVaR loses to minimum variance on CVaR itself**, out of sample:
  ES₉₅ 3.51% against 2.82%. Matching the metric to the objective is not the same
  as winning on it.
- `[ok]` A 95% expected shortfall over a 36-month window is estimated from about
  two observations. The 0.509 Sharpe that window produces is luck, and belongs in
  the chapter as a warning rather than a finding.
- `[open]` `CSM` unavailable in the metaheuristics — empty block in
  `constrained_objective.R`, upstream issue #51. **Verify before printing.**
- `[open]` `EQS` ratio not normalised post-solve, so box and group constraints may
  not bind. **Verify.**


### 11 · Higher Moments

**Q** What breaks when asset classes are skewed and fat-tailed?
**M** `extractCoskewness()`, `extractCokurtosis()`, Boudt moments, `CCCgarch.MM()`, `crra_objective()`, `copula_moments()`

- `[ok]` The data supports this: `US_credit` skewness −1.49 with excess kurtosis
  12.7, and the tangency portfolio buys it. → 09, 10
- `[open]` **Placement problem.** This is nominally an optional extension, but 03
  and 08 both depend on the argument that variance is the wrong risk measure for
  credit. An extension the earlier chapters lean on is misplaced. **Decide.**


### 12 · Portfolio Constraints

**Q** How does a policy statement become something a solver can read?
**M** `group_constraint()`, `box_constraint()`, `position_limit_constraint()`, `leverage_exposure_constraint()`, `factor_exposure_constraint()`, `extractGroups()`, `chart.GroupWeights()`

- `[ok]` Unconstrained optimisation on this universe is degenerate: 84% in one
  series. Group constraints are not an exercise here, they are the precondition
  for a portfolio anyone would hold. → 03, 15
- `[ok]` Position limits are silently dropped by the ROI quadratic path — no
  cardinality formulation exists, `max_pos = 5` returned 6 holdings with weights
  identical to the unconstrained answer, and nothing warned. Fixed on the fork to
  error instead. → 13, 93
- `[ok]` `pso` and `GenSA` accept a position limit and violate it: 16 holdings
  under a limit of 5, no warning. `DEoptim` (4) and random portfolios (2) respect
  it. Three of five solvers return an infeasible answer. → 13
- `[open]` The diversification constraint exists only under metaheuristics.
- `[open]` Beat 4: why a constraint is a statement about the world, not about the
  optimiser.


### 13 · Numerical Optimization and Solvers

**Q** Nine solvers. Which one, and how do you know it converged?
**M** CVXR, ROI, osqp, Rglpk, DEoptim, GenSA, pso, mco

- `[ok]` On a convex problem with a known answer, ROI and CVXR reach 100% in 4 s
  and 31 s. Random portfolios with 100,000 draws reach 71.9% in 1,266 s; DEoptim
  60.9%, pso 54.9%, GenSA 52.6%. Five times more draws buys ten percentage points
  at four times the cost.
- `[ok]` The appendix table people want is not which solver *supports* a
  constraint but which one *honours* it. → 92
- `[ok]` `maxSR` defaults to `FALSE`: a mean-plus-StdDev specification is not a
  maximum-Sharpe problem unless you say so.
- `[ok]` The searches complain that an exact `full_investment` constraint is
  "restrictive" and advise `min_sum = 0.99, max_sum = 1.01`. That is the same
  encoding that makes quadprog report infeasibility — one degeneracy, two solver
  families, two different symptoms, neither about the portfolio.
- `[ok]` Beat 3 is `combine.optimizations()`: several results as one object, so
  `extractWeights()` returns a matrix and `chart.RiskReward()` plots them
  together. Almost every published comparison builds that matrix by hand.
- `[open]` `maxSTARR`, `CSMratio`, `EQSratio` default to `TRUE`. Verify.
- `[open]` `optimize_method` as a two-element vector, and what it actually selects.
- `[coord]` **Resolved with 07.** 07 keeps the short guard (`solve_checked()`) and
  the CLARABEL instance because it optimises; 11 owns the family comparison and
  the feasibility table. No duplication in the written text.


### 14 · Risk-Based Allocation

**Q** What if you allocate risk instead of capital?
**M** `risk_budget_objective()`, `weight_concentration_objective()`, `HHI()`, `diversification()`, `chart.RiskBudget()`

- `[ok]` Inverse volatility is exported as `inverse.volatility.weight()` and
  almost nobody knows. OOS Sharpe 0.366 at 60 months, 0.389 at annual rebalancing
  — competitive with everything, at a sixth of max-Sharpe's turnover.
- `[open]` Risk budgeting has no convex solver at all, so every result in this
  chapter comes from a metaheuristic — whose accuracy 11 has just measured at
  53–72%. **That tension has to be stated, not hidden.** → 13
- `[open]` `HHI()` and `diversification()` are exported and can audit any returned
  portfolio, including one from a solver that ignored the constraint. → 12
- `[open]` Effective number of bets falls 7.05 → 3.98 into crisis. Risk parity
  allocates to a covariance that is itself a regime variable. → 19


---

## Part V · Allocation Strategies


### 15 · Hierarchical and Sleeve-Based Allocation

**Q** How do you optimise sleeves and then optimise across them?
**M** `mult.portfolio.spec()`, `add.sub.portfolio()`, `combine.portfolios()`, `combine.optimizations()`

- `[open]` **The book's spine, and the user's structure.** Hierarchical allocation
  is not a compromise: forcing cross-block covariances to zero is shrinkage with
  an economic rather than a statistical justification. Testable — does the
  hierarchy beat one-stage optimisation out of sample? → 07, 25
- `[open]` The class series is the sleeve's *benchmark*, not its result. SAA is
  set on investable index proxies; the sleeve manager beats the proxy or does
  not. Anything else is circular and poisons the backtest. → 24
- `[ok]` Hedging is a different decision for the bond sleeve than for the equity
  sleeve of the same country. → 04, 22
- `[open]` The anchored variant — optimise around the policy portfolio with a
  tracking-error budget — is a different animal and belongs in 21, not here.


### 16 · Signals and Return Forecasts

**Q** Where do tactical signals come from, and do they survive out of sample?
**M** tidyfinance macro predictors, tidymodels, `applyFUN()`, `trailingFUN()`

- `[open]` Momentum is constructible from returns; value is not, without
  fundamentals. Say which signals this universe can and cannot support. → 06, 21
- `[open]` The bond curve factors are the macro state of this market and are
  shipped: level, slope, curvature per region plus ten credit spreads. A tactical
  signal built from them stays inside the universe. → 22
- `[open]` Evaluation belongs to 06, not here. This chapter builds; 06 judges.


### 17 · Expressing Views

**Q** You have an opinion. How does it become a weight?
**M** `black.litterman()`, `meucci.moments()`, `meucci.ranking()`, `ac.ranking()`, `centroid.*()`

- `[open]` **Blocking issue:** Black-Litterman needs market weights for every
  asset. We have capitalisations for equities only. Either a documented proxy for
  bond and commodity weights, or the chapter uses equity-only equilibrium and
  says so. → 06
- `[open]` `centroid.buckets()`, `centroid.sign()`, `ac.ranking()` turn an ordinal
  view into a return vector. Almost unused, and the natural fit for "I think
  European credit will underperform" without inventing a number.


### 18 · Parametric Portfolio Policies

**Q** What if you skip forecasting and parameterise the weights directly?
**M** `ppp_fit()`, `ppp_weights()`, `applyFUN()`

- `[open]` Brandt-Santa-Clara-Valkanov needs characteristics: size ✓ (market
  caps), momentum ✓ (returns), value ✗ (no fundamentals). Two of the classic
  three. → 06
- `[open]` The policy is estimated on the objective directly, so it is the
  cleanest example of decision-aware estimation in the book. → 27


### 19 · Regime-Dependent Allocation

**Q** What if the right portfolio depends on the state of the world?
**M** `regime.portfolios()`, `combine.portfolios()`, `detect_regime()`

- `[ok]` The regimes are real and economically distinct: the credit crisis and the liquidity shock are flights
  to quality, the last model year is a rates shock in which the only winner is the class that
  lost most in the other two. → 04
- `[ok]` Turbulence gives a continuous, out-of-sample regime signal, and `cturb`
  separates correlation breakdown from mere volatility. → 05
- `[open]` Does a regime-switching allocation beat a static one out of sample,
  once the regime has to be *detected* rather than dated? This is the chapter's
  whole risk.


### 20 · Sustainable Investing Constraints — **blocked**

**Q** Exclusions, tilts and carbon budgets. What do they cost?

- `[ok]` **Blocked on data.** The export carries 1,113 ESG rating *changes* and no
  starting level, so cumulating gives a level up to an unknown constant. You
  cannot screen on a level you do not know.
- `[open]` Route agreed: simulate ESG levels calibrated to the real
  cross-sectional distribution, anchored on the existing change path. Cheaper
  than the fundamentals and unblocks the whole chapter.


---

## Part VI · Inside the Sleeves


### 21 · The Equity Sleeve — **partly blocked**

**Q** The sleeve has a budget. Which stocks, and does selection survive the allocation above it?

- `[ok]` 123 equities, capitalisation-weighted lagged one week — verified against
  the shipped class series to 3.5e-17. The construction is the investable one.
- `[ok]` Capitalisation concentration: largest to smallest 55:1, top five hold
  55% of US capitalisation, effective names 18 of 35 (US) and 5.9 of 17 (CH).
- `[ok]` Equal versus capitalisation weighting is a live choice: CH 7.78% against
  11.08%, JP 4.62% against 2.30%. Equal weighting is itself an active bet. → 24
- `[ok]` Needs shrinkage to run at all — 123 assets, any window shorter than 124
  months is singular. → 07
- `[open]` **Blocked on fundamentals** for anything value-flavoured. → 06, 18


### 22 · The Fixed Income Sleeve

**Q** Bonds are not just another return series. What changes when the asset has a duration?
**M** `curve_pca()`, `diebold_li()`, `duration_overlay()`, `factor_exposure_constraint()`

- `[ok]` The curve factors ship: level, slope, curvature per region plus ten
  credit spreads, weekly. The chapter can decompose rather than assume.
- `[ok]` For a dollar investor a foreign government bond is 92% currency
  (`JP_government`) — the duration decision and the currency decision are not
  separable here. → 04, 15
- `[ok]` Government bonds are zero-coupon at 2, 5 and 10 years, so duration is
  known rather than estimated. That is a gift for teaching and a limitation for
  realism; say both.
- `[open]` Credit as a separate risk: the credit factor has AR(1) 0.992, so a
  crisis spread stays wide for as long as the credit cycle does. → 10


---

## Part VII · Implementation and Evaluation


### 23 · Rebalancing and Transaction Costs

**Q** The paper portfolio is free. What does the real one cost?
**M** `turnover_constraint()`, `turnover_objective()`, `transaction_cost_constraint()`, `turnover()`, `rebalance_bands()`

- `[ok]` Rebalancing less often helps the rules and hurts the optimisers. 1/N
  0.387 → 0.401 and inverse-vol 0.366 → 0.389 going monthly to annual;
  max-Sharpe collapses 0.232 → 0.079 and min-CVaR 0.358 → 0.195.
- `[ok]` The cost bite is monotone in how much you optimise. Median Sharpe lost:
  max-Sharpe 0.021, min-CVaR 0.012, min-variance 0.007, inverse-vol 0.003, 1/N
  0.003. Max-Sharpe loses 16% of its own Sharpe.
- `[ok]` Costs are per asset class, not a flat rate: government 2 bp, equity
  10 bp, credit 25 bp. The dearest class is also the one with the highest Sharpe.
- `[ok]` Turnover is a penalty under CVXR and a hard constraint under ROI.
  Proportional transaction costs exist only under ROI.
- `[ok]` `Return.portfolio()` back-fills equal weights for every period before
  the first weight vector, and warns. Measured: 12 of 24 months in a test run
  were an equal-weighted portfolio nobody specified. Because a rolling estimation
  window always consumes the start of the sample, this is the normal case rather
  than an edge case. → 25
- `[drop]` "…and rewrites the index while doing it." Not reproduced: input and
  output indices are both `Date` and the dates match. Removed rather than printed.


### 24 · Benchmarks and Active Risk

**Q** Did you beat the benchmark, and was it skill?
**M** active weight sum, `return_constraint()`, PerformanceAnalytics, `max_ir()`, `te_constraint()`, `attribute_active()`

- `[ok]` `InformationRatio()`, `TrackingError()`, `ActivePremium()`,
  `UpDownRatios()`, `table.CaptureRatios()` all exist already. The machinery
  `tidypm` still owes is `max_ir()`, `te_constraint()`, `attribute_active()`.
- `[ok]` Betas are the input, and they are unstable: rolling beta of `JP_equity`
  travels 1.30, and every near-zero beta changes sign in about half of all
  windows. An information ratio computed on such a beta needs an error bar. → 05
- `[open]` The anchored formulation: optimise around a policy portfolio under a
  tracking-error budget. This is the user's "variant B" and it lives here. → 15
- `[open]` Choosing equal over capitalisation weighting for the benchmark embeds a
  size bet in the yardstick. → 21


### 25 · Backtesting and Diagnostics

**Q** Did it work, and would you have known if it had not?
**M** `optimize.portfolio.rebalancing()`, `optimize.portfolio.parallel()`, `extractWeights()`, `extractObjectiveMeasures()`, `backtest.plot()`, `diagnose_rebalancing()`

- `[ok]` `optimize.portfolio.rebalancing()` calls `foreach` with
  `.errorhandling = "pass"`. A failed period comes back as a condition object in
  the result list and the backtest looks complete. This is upstream issue #45 and
  it is the chapter's centre.
- `[ok]` It contains `%dopar%` but registers no backend, so it runs on one core
  and says so only in a warning that reads like noise. With a registered cluster:
  273 s → 61 s, 4.46×, results bit-identical.
- `[ok]` `optimize.portfolio.parallel()` is a different function for a different
  job — repeated runs of one optimisation, not the rebalancing loop.
- `[ok]` The full register, OOS from model year 11: 1/N 0.387, min-variance 0.360,
  inverse-vol 0.366, min-CVaR 0.358, max-Sharpe 0.232. Nine configurations, zero
  solver failures on the patched package.
- `[open]` The strategy register itself: every construction chapter contributes
  one strategy and one line; this chapter runs them all and diagnoses them. The
  device that makes the book cumulative.
- `[open]` A backtest is a measurement with an error bar. Which error bar?


---

## Part VIII · Advanced Topics


### 26 · The Cost of Forecast Error

**Q** Formally: what does forecast error cost, and which channel is to blame?
**M** `rafe()`, `c_rafe()`

- `[open]` The derivation, with 06 carrying the intuition. **Placement decided:**
  RAFE is introduced in 06 as a number and derived here.
- `[open]` Which channel — mean or covariance — costs more on this data. 02
  measured that the mean is the unstable moment; this quantifies the price.


### 27 · Decision-Aware Forecasting

**Q** Should a forecaster be trained on mean squared error at all?
**M** `trafe_loss()`, `correct_moments()`

- `[open]` Depends on 14 and 16 existing first.


### 28 · Robustness and Model Uncertainty

**Q** What if you do not trust your model, not just your parameters?
**M** `random_portfolios()`, `rp_sample()`, `rp_simplex()`, `rp_grid()`, `resample_frontier()`, `kl_ball()`

- `[ok]` `random_portfolios()` ignores factor-exposure bounds.
- `[open]` Garlappi-Uppal-Wang multi-prior minimax is implemented in
  `uncertaintymeasures` alongside the turbulence measures. Same package, already
  a dependency. → 05
- `[open]` Resampled frontiers against the bootstrap in 07.


---

## Appendices


### 92 · Solver Capability Matrix

- `[ok]` Not which solver supports a constraint — which one honours it. ROI and
  CVXR exact and fast; the metaheuristics at 53–72% of the attainable optimum;
  three of five returning infeasible portfolios under a position limit. → 12, 13


### 93 · Package Notes

- `[ok]` Two non-CRAN dependencies, both deliberate: `tidypm` and
  `uncertaintymeasures`.
- `[ok]` The fork of `PortfolioAnalytics` carrying three fixes — the `maxSR`
  mean, the degenerate `full_investment` encoding, and constraints accepted then
  dropped. Recorded here while the pull request is open.
- `[ok]` Which package to reach for: PerformanceAnalytics as the engine,
  tidyquant at the tibble boundary, tidyfinance for data access only.


### 95 · Coverage Ledger

- `[open]` Generate by walking the `PortfolioAnalytics` namespace against this
  register. A capability with no chapter is either a deliberate omission or an
  oversight, and the table forces the distinction.


---

## Chapters on the new contract

| Chapter | State |
|---|---|
| 09 Mean-Variance Optimization | **done** 2026-09-12. 5,448 words, 18 distinct citations, 5 numbered equations, proofs in appendix B. The reference chapter; the remaining seven follow its pattern. |
| 04, 05, 07, 13, 14, 23, 25 | written to the retired four-beat contract, awaiting rewrite |

## Open decisions

1. ~~**Chapter 26's placement**~~ — **settled 2026-09-12.** Higher moments moved
   forward to chapter 11, inside Part IV, because chapters 03 and 10 both lean
   on the argument that variance is the wrong risk measure for credit. No
   forward reference remains.
2. **ESG levels** — simulate and unblock chapter 20, or drop the chapter?
3. **Market weights for non-equities** — needed for Black-Litterman in 17.
   Documented proxy, or equity-only equilibrium?
4. **PRIX citation** — the package cites Garlappi-Uppal-Wang and Garthwaite-Koch
   but not the user's own paper. Details needed for 05 and 28.
5. **The restructured export.** 16 risky series with the money market as the
   risk-free rate, instrument level retained. Until it lands, every number here
   is on version 4.3.0 and the claims listed in `CLAUDE.md` are the ones that
   die with the change.
6. **Bibliography build-out.** 17 entries today against a target of 15–30
   citations per chapter. Assemble per chapter as each is written, or build the
   reference set up front? Not yet decided.
