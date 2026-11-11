---
file: chapters/17-expressing-views.qmd
title: Expressing Views
part: Allocation Strategies
words: 7975
sections: 5
paragraphs: 65
---

# Chapter

Claim: A view should enter the optimizer blended with the equilibrium prior at a stated confidence, which makes the portfolio the market plus a position in each view portfolio; entropy pooling buys the same on a skewed history at a price in effective months, a ranking supplies a direction whose size the allocator must still choose, and any view written into μ without the covariance becomes a hedged spread trade.
Question: How does an allocator's opinion become a portfolio weight; cites Black and Litterman (1992) in the second sentence, with Michaud (1989) for why it must not become one directly.
Why here: Names itself tactical in chapter 3's sense, a deviation from the strategic policy chapter 6 anchored on the equilibrium; takes the data from chapter 2 and the excess basis from chapter 3, μ and Σ and the GMV and effective-bets ideas from chapter 9, the equilibrium prior (rebuilt verbatim), `tangency_lo()`, `make_moments()`, the `match.call()` trap and the Σ_μ warning from chapter 6, skewness from chapter 4, the long-only QP from chapter 12, standard errors from chapters 6 and 8; hands forward to chapters 16 and 25 (data-generated views and their backtest), 18 (skipping μ), 19 (a regime as a scenario view through eq-17-entropy) and 28 (confidence as the size of an uncertainty set). Why it follows chapter 16 inside the part: not stated; the closing paragraph relates the two (a signal has a history of views, an opinion does not) without saying why the opinion comes second.
Does: Write the Black–Litterman posterior with an explicit confidence and check it against `black.litterman()`; route views through `set.portfolio.moments()` with the covariance restored; express mean, volatility and ranking views as entropy constraints and price them in effective months; turn a ranking into a centroid, name and scale it, and tell a coherent view from a hedged spread.
Order: Theory (Black–Litterman posterior, entropy pooling, centroid), implementation (prior rebuilt, Black–Litterman with two views, the package route, entropy pooling, ordinal views), application (one opinion three ways), takeaways, exercises. Deviations: the implementation holds 4,551 of 7,975 words, three of the four figures and three of the four labeled tables, and reads results in every subsection, so the application is a fourth worked case rather than the results section; a theory property (a centroid alone is a corner solution at any scale) is argued in the implementation; the chapter's coherence condition (the shift in μ must be Σ times a portfolio) is stated only in the application; four exercises.

# Sections

## Opening (untitled) — 257

Says: An opinion must be blended with a prior rather than written into μ, Black–Litterman is the standard way, and two formulations that ask less are set beside it.
Why here: Contract position; ¶2's sequence sentence says mathematics first, then each formulation on the sixteen series, then one opinion three ways.
Paragraphs:
- (code: setup) hidden; sources `R/_common.R`, loads `tidypm` and `knitr`
- ¶1 [claim] An opinion should not become a weight directly (Michaud); Black–Litterman blend it with a prior; two cheaper alternatives named.
- ¶2 [method] Tactical in chapter 3's sense, deviating from chapter 6's equilibrium policy; theory, then implementation, then one opinion three ways.
- ¶3 [method] Data: the sixteen class series of chapter 2, in excess of the bill as chapter 3 argued.
- (code: data)
Note: The packages block is hidden (`include: false`), so no package list is shown; the `data` chunk also builds `mu_s` and `S`, which the entropy and ranking subsections run on unannounced.

## A View as a Bayesian Update — 1268

Says: Three formulations of a view: a normal update of the equilibrium mean whose confidence sets the position, a minimum-divergence reweighting of historical scenarios priced in effective months, and a ranking whose centroid is a direction without level or scale.
Why here: The opening's sequence sentence ("first state the three formulations as mathematics"); the subsections run from the standard answer to the two that ask less, the order the opening frames.
Paragraphs: none of its own.
Note: Heading only, and it names Black–Litterman's construction; entropy pooling (a minimum-divergence problem) and the centroid (a conditional expectation over a cone) sit under it as the second and third subsections.

### The Black-Litterman posterior — 628

Says: With a normal prior on the equilibrium mean and Meucci's Ω, τ cancels, each view lands at a confidence-weighted average of prior and view, and the posterior portfolio is the market plus one position per view portfolio.
Why here: "The standard answer" of the opening; needs chapter 9's μ and Σ, eq-06-equilibrium and Sharpe's reverse optimization; the entropy subsection opens by removing its two restrictions, the implementation traces the confidence it ends on, and the application shows what happens without eq-17-weights.
Paragraphs:
- ¶1 [definition] μ and Σ as in chapter 9; the prior on μ is normal, centered on chapter 6's equilibrium vector; eq-17-prior.
- ¶2 [definition] τ scales the prior's uncertainty; a view is K linear statements on μ with error covariance Ω; eq-17-views.
- ¶3 [derivation] Absolute and relative rows of P; normal prior and likelihood give a normal posterior; eq-17-posterior mean and covariance.
- ¶4 [claim] Derivation cited to four papers; two features: the update moves only along ΣP', and Σ_μ is never a risk input.
- ¶5 [definition] τ and Ω have no data behind them; τ conventions surveyed, τ cancels; Ω conventions surveyed, Meucci's closed form eq-17-omega.
- ¶6 [derivation] Substituting eq-17-omega, τ cancels and each view portfolio's posterior is a weighted average of prior and view; eq-17-pooling.
- ¶7 [claim] c = ½ weighs both equally, 1 imposes the view, 0 ignores it; the confidence is the position's size.
- ¶8 [derivation] He–Litterman's result: with the market's risk aversion the posterior weights are w_mkt + P'Λ; eq-17-weights.
- ¶9 [claim] Market plus one position per view portfolio; unnamed assets keep their weight, unlike under a hand-written μ; long-only clips.
Note: ¶4 does three jobs (the derivation's literature, the ΣP' property, the Σ_μ warning carried from chapter 6); ¶9's closing clause, that eq-17-weights holds only until a weight reaches zero, is what the implementation's ¶8 and the application's ¶4 both rest on.

### Views on scenarios: entropy pooling — 400

Says: A view is a constraint on the probabilities of the sample months, the posterior is the least-divergent probability vector that satisfies it, and the effective number of scenarios prices what the view cost.
Why here: "Black-Litterman is a view on the mean under normality, and Meucci removes both restrictions": placed as the generalization, and it needs Black–Litterman stated to say it reproduces it on normal scenarios; hands eq-17-entropy to chapter 19 and eq-17-cost to the implementation's cost table.
Paragraphs:
- ¶1 [definition] Meucci drops normality and the mean-only restriction: the prior is T uniform scenarios, a view any constraint on expectations; eq-17-entropy.
- ¶2 [evidence] Rows of H and F are view functions; Kullback, Jaynes, Csiszár, Robertson cited; the solution is an exponential tilt, eq-17-tilt.
- ¶3 [claim] One multiplier per view; the tilt reproduces Black–Litterman on normal scenarios and parts from it otherwise, measured in the application.
- ¶4 [definition] A concentrated posterior has thrown history away; the diagnostic is the effective number of scenarios, eq-17-effective.
- ¶5 [derivation] Chapter 9's effective-bets construction; T under the uniform prior, falling toward one; a k-standard-error view costs k²/2T; eq-17-cost.
- ¶6 [claim] Near views cost almost nothing, far ones leave a fraction of the history; opinion pooling of probabilities gives eq-17-pooling's form.
Note: ¶5 derives eq-17-cost in one clause ("to second order") with no pointer to appendix B; ¶2 is a four-citation genealogy standing between the problem and its solution.

### Views as an ordering: the centroid — 232

Says: A ranking defines a cone of mean vectors whose centroid, the expected order statistics of N normals, is the direction to optimize over; it carries no level, no scale and no position size.
Why here: "Both formulations ask for a number": last because it asks for the least, and it needs the two before it as the contrast; its closing sentence (size is unsaid) is what the implementation's centroid portfolios and the application's ¶4 take up.
Paragraphs:
- ¶1 [definition] Salcher: an allocator honestly has only an ordering; Almgren–Chriss: the ranking defines a cone, the optimum maximizes w'c; eq-17-centroid.
- ¶2 [claim] The centroid is the expected order statistics of N normals: no level, no scale; Herold, Grinold; position size is unsaid.
Note: The author's own case for rankings (Salcher et al.) opens the subsection before Almgren–Chriss, the method being attributed; two paragraphs carry the only formulation the application later finds wanting.

## Three Ways to Make a Weight — 4551 (447 before the subsections)

Says: The chapter 6 prior is rebuilt and the two helpers reused, then each formulation is run on the sixteen series with its package route checked against a hand computation.
Why here: The opening's sequence sentence ("then implement each on the sixteen risky class series"); the prior comes first "so that the two chapters cannot disagree", and every subsection runs on the objects it builds.
Paragraphs:
- ¶1 [method] The prior is chapter 6's class-level equilibrium rebuilt verbatim; the eleven non-equity weights are that chapter's proxy.
- (code: prior) inside a collapsed callout holding the chunk and a title, no prose
- ¶2 [method] Two chapter 6 functions reused: `tangency_lo()` for the long-only tangency QP, `make_moments()` to pass a mean vector.
- (code: helpers)
Note: The heading says three ways and four subsections follow, the second a package route rather than a way; the collapsed box carries the 40/40/15/5 assumption and builds every prior object the chapter runs on (`mu_eq`, `delta16`, `w_mkt`, `mu_eq5`, `S5`); the `helpers` chunk also builds `spec` and asserts the prior buys the market, which ¶2 does not say.

### Black-Litterman with two views — 1361

Says: A hand-written eq-17-posterior reproduces `black.litterman()` at c = ½, moves every covarying mean, buys the market plus the two view positions until long-only binds, and slides from market to views as the confidence rises.
Why here: First, as in the theory; needs the prior box and the helpers; the confidence trace answers the theory's ¶7 ("the implementation traces it"); the package route next needs `bl` and `w_post` from here.
Paragraphs:
- ¶1 [method] Two views: US over EU credit by two points, commodities four percent over the bill; rows of P, monthly units.
- (code: views)
- (code: tbl-17-views)
- ¶2 [result] The prior disagrees with each view by a read gap; only a hand-written eq-17-posterior carries a confidence parameter.
- (code: bl-post)
- ¶3 [code] Four assertions: the package is eq-17-posterior at c = ½, τ leaves the mean untouched, views land midway.
- ¶4 [caveat] (callout) Ω is the full PΣP' with off-diagonals, not He–Litterman's diagonal; P must be a matrix; a short `Views` recycles silently.
- (code: bl-recycle)
- ¶5 [caveat] (callout) The `stopifnot()` in `bl_post()` is the guard the package lacks.
- ¶6 [method] What the views do to the sixteen means comes first, from one frame.
- (code: bl-means-frame)
- (code: fig-17-bl-means)
- ¶7 [result] A view on two credit series moved several means, EU_equity among them through covariance; eq-17-weights says what it buys.
- (code: bl-tangency)
- ¶8 [result] Unconstrained, eq-17-weights holds exactly; long-only cannot short EU_credit, so US_government takes the money as the least volatile home.
- ¶9 [method] The confidence sizes all of this; tracing it slides the weights from the market to the views' own portfolio.
- (code: confidence-trace)
- (code: fig-17-confidence)
- ¶10 [result] At 0.01 the market, at 0.99 the views; nothing in the data chose a point; chapter 28 reads c differently.
Note: ¶2 ("has none") and ¶3 ("at c = ½") state the same fact about the package twice; the callout, whose silent-recycling trap is the gravest in the chapter, is a note where the two later traps are warnings, and it stands between the assertion paragraph and the reading of the means.

### Through `set.portfolio.moments()` — 270

Says: The package route works with views but hands the optimizer Σ_μ as the risk, and `momentargs = list(sigma = S)` is the fix.
Why here: "The route that needs no custom function": the package alternative after the hand function, checked against its `w_post`; carries chapter 6's `match.call()` lesson forward and adds "one more trap".
Paragraphs:
- ¶1 [method] The package route, `method = "black_litterman"`, must travel through `optimize.portfolio()` because of `match.call()` (chapter 6); one more trap.
- (code: spm-route)
- ¶2 [caveat] (callout) With views `BLSigma` is Σ_μ and the tangency is solved on the wrong risk, silently; `momentargs` restores Σ.
Note: The subsection's only result (the commodity weight and the gap in points) is read inside the warning callout; no paragraph outside it reads the chunk.

### Entropy pooling on the 372 months — 1371

Says: A mean view tilts every month a little, a volatility view discards the shock months and re-rates every left-tailed series, and eq-17-cost prices a view by its distance in standard errors.
Why here: Second, as in the theory; needs T and the sample moments from the `data` chunk and `tangency_lo()`; the cost table answers eq-17-cost; the ranking subsection next reuses `p0`, `Aeq0`, `eff_n()` and the `EntropyProg()` call.
Paragraphs:
- ¶1 [method] Uniform prior, T months, US_equity; views: mean two points up, volatility twenty percent down; each a row of H.
- (code: entropy-views)
- ¶2 [caveat] (callout) `EntropyProg()`: no default `Aeq`/`beq`, prior must sum to one, checker messages, `p_` is a matrix, unsatisfiable views die misleadingly.
- ¶3 [result] The mean view keeps most effective months, the volatility view fewer; the probabilities are the object to look at.
- (code: entropy-frame)
- (code: fig-17-entropy)
- ¶4 [result] The mean view tilts every month a little; the volatility view nearly removes the liquidity-shock months; `meucci.moments()` makes moments.
- (code: meucci-moments)
- ¶5 [result] One series named, sixteen moved (EU_equity, UK_equity) through shared bad months; the (T−1)/T scaling; `method = "meucci"` works directly.
- (code: meucci-portfolio)
- ¶6 [result] US_credit's weight changes under a view about US_equity's volatility, through its skewness (chapter 4) and shared worst months.
- ¶7 [transition] Where the step bites is a matter of distance; eq-17-cost measures it.
- (code: entropy-cost)
- (code: tbl-17-entropy-cost)
- ¶8 [result] Five standard errors keep most months, forty few; the volatility view is dearer in stated units, not in standard errors.
Note: ¶5 does three things (reads the sixteen moved moments, notes the (T−1)/T scaling, introduces the package route); ¶4 and ¶5 each end in the one-sentence method for the next chunk; the title types the month count that the prose carries as inline R.

### Ordinal views on the five equity classes — 1102

Says: As an entropy constraint a ranking holds only as ties, the centroid commits to a spacing but is a corner solution on its own, and added to the prior at a chosen scale it becomes a tilt whose size came from that choice.
Why here: "The last formulation asks for no number": last, as in the theory; needs `eq_classes`, `mu_eq5` and `S5` from the prior box and the entropy machinery of the subsection before; its scaled tilt is the device the application's centroid column reuses.
Paragraphs:
- ¶1 [method] No number: Japan to lead, the other four in sample order; `order` is built by name, lowest to highest.
- (code: ranking)
- ¶2 [method] `meucci.ranking()` writes adjacent pairs as inequality rows of eq-17-entropy, returns moments, discards probabilities; `EntropyProg()` recovers them.
- (code: meucci-ranking)
- ¶3 [result] Ranking holds as ties, Japan level with the two highest at almost no cost; the centroid commits to a spacing.
- (code: ac-ranking)
- ¶4 [caveat] (callout) `ac.ranking()` ignores `max.value`, maps onto ±5 percent per period, returns no names; name and scale it yourself.
- ¶5 [method] Three other centroid functions encode less than a complete sort, each returning an unnamed vector in index order.
- (code: centroid-family) a `kable` with no table label or caption
- ¶6 [caveat] Monte Carlo averages, seed-dependent; the sector variant centers each sector at zero; the bucket variant equalizes members.
- ¶7 [claim] A centroid is a direction: alone, a tangency solver takes only the top asset, since the Sharpe ratio is scale-invariant.
- (code: centroid-portfolios)
- (code: tbl-17-ranking)
- ¶8 [result] Ties let variance sort (eq-09-gmv); centroid alone is a corner; prior plus centroid lifts Japan and EU; size a choice.
Note: ¶7 is a theory property argued in the implementation, after the warning callout; the scale rule for "prior + centroid" (the prior's own dispersion, `kappa5`) is set in a code comment and the table caption and never introduced in prose before the chunk.

## One Opinion, Three Formulations — 1452

Says: Given the same opinion at the same strength, Black–Litterman and entropy pooling buy nearly the same portfolio, while the centroid written into μ without the covariance becomes a hedged credit–government spread, so coherence with Σ matters more than the formulation.
Why here: The opening's last clause ("finally express one opinion three ways and compare what each formulation committed to"); needs `bl_post()`, the entropy objects, `centroid.buckets()` and `tangency_lo()` from all three implementation subsections; delivers the two measurements the theory promised (what happens without eq-17-weights, by how much entropy pooling and Black–Litterman part).
Paragraphs:
- ¶1 [method] US credit expensive, Japan cheap, said three ways: a relative view at half confidence, an entropy view, a bucket ranking.
- (code: application-views)
- ¶2 [result] All three posteriors put the spread at the same midpoint, so the opinion's own strength is identical; everything else differs.
- (code: application-portfolios)
- (code: tbl-17-three)
- (code: fig-17-three)
- ¶3 [result] Black–Litterman and entropy pooling agree on tracking error and JP_equity; the first touches nothing else, the second little (low skewness).
- ¶4 [result] Centroid committed least, moved most: without Σ it read as a credit–government spread; coherent shifts are Σ times a portfolio.
- ¶5 [claim] Two chapter 8 readings: the view is within one standard error; a ranking escapes magnitude error (Chopra–Ziemba, Salcher).
- ¶6 [caveat] Not out of sample: no record of beliefs exists; data-generated views go to chapters 16 and 25; 18, 19 named.
Note: No subsections; ¶4 carries the chapter's thesis (the coherence condition) together with its result, its cause, its remedy (exercise 3) and a literature verdict; two columns of tbl-17-three ("held", "Sharpe on prior") are never read in prose; ¶6 is the closing caveat and the forward pointers to four chapters in one block.

## Key Takeaways — 215

Says: Five bullets.
Why here: Contract position.
Paragraphs:
- ¶1 [takeaway] Black–Litterman is eq-17-posterior: a normal prior on the equilibrium, linear views with error, every asset moved by covariance.
- ¶2 [takeaway] Meucci's Ω cancels τ and lands each view at (1−c) prior plus c view; the package fixes c = ½.
- ¶3 [takeaway] The posterior tangency is market plus a position per view (eq-17-weights); a hand-written μ becomes a hedged spread trade.
- ¶4 [takeaway] Entropy pooling: T scenarios, views as probability constraints; a near mean view is free, a volatility view discards shock months.
- ¶5 [takeaway] A ranking is a direction, the centroid its expected value; no level, no scale; `ac.ranking()` misscales; size is a choice.
Note: Five, as the contract asks; ¶3's second sentence is the application's finding and the only takeaway that is a result rather than a theory statement; ¶2 and ¶5 each carry a package trap.

## Exercises — 187

Says: Four exercises.
Why here: Contract position.
Paragraphs:
- ¶1 [exercise] Replace eq-17-omega with He–Litterman's diagonal Ω; does eq-17-pooling still hold per view; what the off-diagonal carries.
- ¶2 [exercise] Volatility view at 50 and 150 percent of sample; effective months, heaviest months, what the tangency does with US_credit.
- ¶3 [exercise] Write the bucket ranking as two absolute views in `bl_post()`; compare with the centroid column; which weights stop moving.
- ¶4 [exercise] Reverse the five equity classes' sample order; count `meucci.ranking()` ties, read `ac.ranking()`; which to hand over, at what scale.
Note: Four against "around three"; exercise 3 is the remedy the application's ¶4 promised, so the chapter's one constructive fix for the centroid is left to the reader.
