---
file: chapters/20-sustainability.qmd
title: Sustainable Investing Constraints
part: Allocation Strategies
words: 7748
sections: 5
paragraphs: 40
---

# Chapter

Claim: A sustainability constraint that does not bind costs nothing; one that binds costs tracking error and return at the rate its multiplier prices, paid through the priced characteristics the rating is correlated with; it is a cost and never an alpha, so the chapter prices the constraint rather than the names.
Question: What does an exclusion or a rating floor cost a portfolio, and who pays? Cited to @pedersen2021 for the cost (the ESG-efficient frontier) and @pastor2021 for who pays (tastes priced in equilibrium).
Why here: Takes the multiplier and the constraint functions of ch. 12, the shrinkage of ch. 7, the policy of ch. 15 and the strategic/tactical vocabulary of ch. 3; builds on the equity sleeve, its capitalization anchoring and the policy recomputation of ch. 21, a later chapter, and uses the tracking-error and standard-error equations of ch. 24. Forward: ch. 25 (what a screen does to a backtest's error bar) and ch. 28 (stability across windows). Why it closes Allocation Strategies: not stated; the text places it only on the horizon axis, as strategic.
Does: Construct rating levels from a path of changes, impose an exclusion, a floor and a best-in-class floor on an equity sleeve, price each by active share, tracking error and multiplier, audit the solutions, and measure the cost out of sample and across raters.
Order: Theory (five subsections, one paragraph each) → implementation (levels, sleeve, exclusion, floor, multiplier check, audit) → application (out-of-sample costs, then a second rater) → takeaways → exercises. Contract kept; the real-data callout closes the implementation from inside "The audit", and the chapter's closing sentences sit inside the last application subsection.

# Sections

## Opening (before the first heading) — 498

Says: A line in the mandate costs tracking error and expected return only when it binds, at the multiplier's rate, and is never an alpha; the chapter sets out, constructs and prices three such lines.
Why here: Chapter contract: the question with its citations, then the plan; the plan states the order the three sections follow.
Paragraphs:
- (code: setup)
- ¶1 [claim] A mandate line costs what, paid by whom; two results fix the answer: nothing unless it binds, never alpha.
- ¶2 [method] The plan: theory in five pieces, then levels and three constructions on the sleeve, then out-of-sample costs; strategic.
- (code: data)

## Tastes, Floors, and Exclusions — 1140

Says: A taste and a floor trace one frontier priced by the floor's multiplier; an exclusion is a box at zero with a Jagannathan–Ma price; a tilt is a factor exposure on a score; and the score is an estimate whose taste is priced in equilibrium.
Why here: The opening's plan puts the problem first; the two framing results of the opening are what the section works out, and every object the implementation builds (eq-20-floor, eq-20-exclusion, eq-20-bic) is defined here.
Paragraphs: none at this level; the section goes straight to its first subsection.
Note: Five subsections, each a single paragraph of 160 to 300 words; the theory of the chapter is five paragraphs.

### The investor's problem with a taste for a rating — 301

Says: A taste for a rating and a floor on it produce the same portfolio, the floor's multiplier being the taste, so a binding floor costs variance at the shadow price and a slack one costs nothing.
Why here: First because the opening's plan starts with the investor's problem; needs the investor of ch. 3 and the Lagrangian and shadow price of ch. 12; eq-20-floor is what the tilt subsection and the implementation impose.
Paragraphs:
- ¶1 [derivation] Taste term and ESG-efficient frontier; floor traces it, θ = λ_s; slackness prices it; convex QP; preference, not information.
Note: One 300-word paragraph around two display equations makes five moves; the last, that a floor is a preference and not information about the estimates, is a claim of its own.

### Exclusion as a restriction of the universe — 304

Says: An exclusion is a box at zero; for a capitalization-weighted sleeve its active share is the benchmark weight removed, and for an optimized sleeve a binding exclusion is an implicit risk view priced by its multiplier.
Why here: Called the oldest form of the constraint; order as in the opening's plan. Needs eq-12-jm and the tracking error of ch. 24 (later); the implementation's exclusion and exclusion-jm chunks check both readings.
Paragraphs:
- ¶1 [derivation] Pro-rata reweighting gives active share b_E and a tracking error; JM identity with excluded names' multipliers; Hong–Kacperczyk and Heinkel equilibrium.
Note: One paragraph carries three things: the capitalization-weighted cost, the optimized cost, and the equilibrium evidence.

### Tilts as a factor-exposure constraint on a score — 157

Says: A floor is a factor-exposure constraint on the score, a best-in-class floor is one such row per group in centered scores, and the second costs more because it cannot buy the rating where it is cheapest.
Why here: Third form in the opening's order; needs eq-20-floor and ch. 12's `factor_exposure_constraint()`; eq-20-bic is what `bic_B()` implements.
Paragraphs:
- ¶1 [definition] Floor as factor exposure; best-in-class floor linearized per group; across-universe buys the rating cheapest, best-in-class spreads it and costs more.

### A rating is an estimate — 196

Says: Ratings disagree across raters (0.54 average correlation), so a floor is imposed on an estimate and a different rater excludes different names; carbon is the exception the modeled market cannot run.
Why here: First of the "two facts that complicate all three" named in the opening; comes after the three forms it complicates. Needs ch. 8's estimation error as the analogy; the application's second rater is its test.
Paragraphs:
- ¶1 [evidence] Berg et al. divergence; floor on s+e; Avramov and Gibson on priced uncertainty; carbon is a quantity, no emissions here.
Note: The carbon-budget sentence is a scope caveat parked at the end of an evidence paragraph.

### Tastes are priced — 182

Says: In equilibrium a taste lowers green assets' expected returns, realized green outperformance reflects taste shifts, and a constraint is a cost, not an alpha; the mixed alpha evidence is not needed to price it.
Why here: "Finally", the second complicating fact; closes with the hand-over: none of the alpha evidence is needed to price the constraint, which the rest of the chapter does.
Paragraphs:
- ¶1 [claim] Pástor equilibrium; realized green returns as taste shifts; constraint vs alpha; mixed evidence (Friede, Serafeim, Zerbib) not needed.

## Implementation — 3102

Says: The levels are built from the shipped changes under a stated, seeded assumption; a screen, a universe floor and a best-in-class floor are then imposed on ch. 21's sleeve and priced by active share, tracking error and multiplier, with every solution audited.
Why here: The opening's plan: construct levels, then implement the three constructions, auditing with ch. 12's functions. The callout says why levels come first: the market ships changes and no starting grade.
Paragraphs: none at this level.
Note: 3,100 words, two fifths of the chapter, most of it code; "A floor on the sleeve's rating" alone is 1,080 words around four chunks.

### A level from a path of changes — 727

Says: The market ships rating changes and no levels, so the chapter draws a seeded starting cross-section and cumulates the changes, which, being mostly upgrades, compress the scale toward the ceiling.
Why here: A screen or a floor needs the level's constant, so the construction precedes every constraint; the drift found here is what the application's slack figure tests.
Paragraphs:
- ¶1 [caveat] (callout) Changes but no starting level are shipped; the chapter constructs levels under an assumption exposed as a function argument.
- ¶2 [method] Seven-point scale, normal start at the midpoint with sd 1.2, whole-grade changes, clipped; a different distribution is a different rater.
- (code: esg-levels)
- (code: tbl-20-cross-section)
- ¶3 [result] Most changes are upgrades; a rated name ends above where it started; the cross-section compresses toward the top grade.
- (code: fig-20-drift)
- ¶4 [caveat] Changes have no effect on returns, so any cost below is a universe and constraint effect, not a priced factor.
Note: ¶4 is the premise the application's sector finding rests on; it is stated as an aside after the figure.

### The sleeve, its benchmark, and its covariance — 221

Says: The sleeve is ch. 21's, capitalization weighted within region with equal regional budgets here, and its covariance is shrunk because the sample matrix on 120 months is singular.
Why here: Provides b, S and s to every construction after it; why it follows the levels rather than precedes them: not stated.
Paragraphs:
- ¶1 [method] Chapter 21's sleeve; one fifth per region here, the policy's split later; shrinkage on 120 months because of eq-07-rank.
- (code: sleeve)

### Exclusion — 542

Says: The bottom fifth of each region removed and reweighted gives active share equal to the benchmark weight removed; on the minimum-variance sleeve only some exclusions bind, and the Jagannathan–Ma identity reproduces the screened solution.
Why here: Theory's first construction; needs b, S and s from the sleeve; checks eq-20-exclusion and eq-12-jm in code.
Paragraphs:
- ¶1 [method] Screen: bottom fifth per region by score, ties by position, survivors reweighted within region.
- (code: exclusion)
- ¶2 [result] Names and benchmark weight removed, equal to active share; tracking error; score lift; then the optimized price via multipliers.
- (code: exclusion-jm)
- ¶3 [result] How many exclusions bind; identity reproduced; multiplier as covariance rise; volatility cost to the minimum-variance sleeve.

### A floor on the sleeve's rating — 1082

Says: A floor across the universe costs nothing until the benchmark's own rating and then rises convexly; best-in-class costs more at every floor and binds at once because one region sits below the lowest floor.
Why here: Theory's second and third constructions; the base spec is ch. 12's; the callout says tracking error must be solved by hand, and the `min_te()` defined here is what the application runs monthly.
Paragraphs:
- ¶1 [method] Floor via `factor_exposure_constraint()`, score as B, on a min-variance sleeve with cap and regional groups; best-in-class via eq-20-bic.
- (code: floor-specs)
- ¶2 [caveat] (callout) No tracking-error objective in the package; the min-TE sleeve is written in quadprog, which returns multipliers; routes cross-checked.
- (code: min-te)
- (code: fig-20-frontier)
- (code: frontier-reading)
- ¶3 [result] Slack floors cost nothing; cost rises convexly; best-in-class dearer, binding at the lowest floor; min-variance panel tells the same.
Note: Four chunks between ¶2 and ¶3, one hidden; the floor-specs chunk also prints the attainable maximum rating, which no prose reads.

### The multiplier, checked by perturbation — 157

Says: The multiplier quadprog returns matches the finite difference of eq-12-shadow, and up to scale it is the taste an investor would need for the floor to be their free choice.
Why here: Follows the frontier, whose multipliers it verifies; ties the implementation back to θ = λ_s of the theory. Why a subsection of its own: not stated.
Paragraphs:
- (code: shadow)
- ¶1 [result] Agreement to within a few percent; monthly active variance per grade of floor; up to scale, this is θ.
Note: The subsection opens on code; nothing announces what the chunk does before it runs.

### The audit — 373

Says: Both floor solutions pass every constraint; the universe floor binds once, the best-in-class floor in several regions, which is where its extra cost comes from; on real data the same mechanics apply to industry screens.
Why here: "Every solution above": after all solutions exist, with ch. 12's `audit_spec()`. The real-data callout's placement here: not stated.
Paragraphs:
- ¶1 [method] `audit_spec()` of ch. 12, restricted to this chapter's constraint types; slack read off directly.
- (code: audit)
- ¶2 [result] All lines pass; universe floor binds once; best-in-class binds in several regions, explaining the frontier gap.
- ¶3 [caveat] (callout) No industries or emissions in the modeled market; `pm_screen()` gives the industries a sin, fossil or weapons screen removes.
- (code: real-data)
- ¶4 [claim] (callout) Screens are conventions; the chapter prices the line, not where it is drawn.
Note: The real-data callout is about neither the audit nor the floor; it is the implementation's coda, filed under its last subsection.

## What the Constraints Cost Out of Sample — 2399

Says: Out of sample the two floors cost active risk but no significant return, and expire once the drift carries the benchmark past them; the screen costs return under every rater because the upgrades cluster in the sectors that earned least.
Why here: The opening's plan: measure what the three cost inside ch. 15's policy, recomputed as ch. 21 recomputed it; needs every function of the implementation and the drift of fig-20-drift.
Paragraphs:
- ¶1 [method] The sleeve sits inside ch. 15's policy, recomputed so that ω and the regional split are computed, not quoted.
- (code: policy)
- ¶2 [method] Policy's names and split; three constructions re-estimated monthly; floor fixed at 5 because strategic; the unconstrained sleeve is the benchmark.
- (code: rolling)
- (code: scores)
- (code: tbl-20-oos)
- (code: oos-reading)
- ¶3 [result] Three readings: tracking errors; turnover and the screen's reset months; returns, floors insignificant, screen significantly negative; the draw?
- (code: screen-raters)
- ¶4 [result] Not the draw: under twenty independent starting draws the screen's IR stays negative; what raters share is the change path.
- (code: sectors)
- (code: tbl-20-sectors)
- ¶5 [claim] Upgrades cluster by sector; most-upgraded sectors earned least; a rating is partly a sector label; the general case, per Berg.
- (code: fig-20-slack)
- ¶6 [result] Floor binds until the benchmark's rating reaches 5, then costs nothing; an absolute floor on a drifting scale expires.
Note: ¶3 reads three table columns and poses the next question in 270 words; ¶3 to ¶6 run a draw → sector → slack argument with no subsection breaks, while the second rater gets one.

### A second rater — 421

Says: At real raters' correlation roughly half an exclusion list is the rater's choice, and closely agreeing raters still disagree substantially; the cost and its sector exposure are not the rater's, which is why the chapter priced the constraint rather than the names.
Why here: "The last question"; needs `second_rater()` from the screen-raters chunk and Berg's 0.54; closes the chapter with the pointers to ch. 25 and ch. 28.
Paragraphs:
- ¶1 [method] Second rater: start correlated at ρ, same changes, same screen; the flipped share is Berg's disagreement in mandate units.
- (code: disagreement)
- (code: disagreement-reading)
- ¶2 [result] Flip shares by ρ at start and end; names are the rater's, cost is not; pointers to ch. 25, 28.
Note: The chapter closes inside this subsection; its last sentences are the pointers to ch. 25 and ch. 28, and there is no closing paragraph at section or chapter level.

## Key Takeaways — 301

Says: Five bullets restating the frontier, the exclusion, the floor, the construction and the rater results.
Why here: Chapter contract.
Paragraphs:
- ¶1 [takeaway] Taste and floor trace one frontier; multiplier equals taste; a binding floor costs at the shadow price; cost, not alpha.
- ¶2 [takeaway] Exclusion is a box at zero; active share is weight removed; JM identity with excluded multipliers; binding exclusion raises covariances.
- ¶3 [takeaway] Floor is `factor_exposure_constraint()` with the score; best-in-class is eq-20-bic and dearer; TE objective solved by hand, checked.
- ¶4 [takeaway] Levels are a seeded construction; returns do not respond; fixed floor expires; screen costs return via sector clustering.
- ¶5 [takeaway] A rating is an estimate; half an exclusion list is the rater's; price the constraint, not the names.
Note: ¶4 carries four results in one bullet; the sector mechanism, the chapter's main finding, shares a bullet with the drift.

## Exercises — 178

Says: Four exercises: a relative floor, a narrower cross-section, the screen as a box constraint, and the second rater applied to the floor sleeve.
Why here: Chapter contract; exercise 1 is the relative floor that ¶6 of the application promised.
Paragraphs:
- ¶1 [exercise] Relative floor, the sleeve's own rating plus half a grade; does it bind throughout, at what TE and turnover?
- ¶2 [exercise] Redraw the start with sd 0.6 and rebuild the frontier; explain via eq-20-floor why a narrower cross-section raises every cost.
- ¶3 [exercise] Impose the screen as max = 0 in PortfolioAnalytics, audit against w_mvx; exclude the bottom tenth and count binding exclusions.
- ¶4 [exercise] Second rater for the floor sleeve: active share and tracking error between raters' portfolios; relate to Gibson et al.
