# Restructuring proposal — aligning with Tidy Finance and ML for Factor Investing

Written 2026-09-12. **Settled the same day and implemented.** `CLAUDE.md`,
`PLAN.md`, `_quarto.yml` and every chapter file now follow what is below. This
file is kept as the record of why, not as a live proposal.

The brief: *Aufbau, Sprache und Inhalt* should sit in the same category as
@scheuch2023 (*Tidy Finance with R*) and @coqueret2020 (*Machine Learning for
Factor Investing*) — not in subject matter, but in how the book is built,
written and referenced.

---

## 1 · What the two reference books actually do

Both were inspected at source rather than from memory.

### Tidy Finance — the design is almost nothing

The entire theme file is three declarations: the stock `cosmo` Bootstrap theme,
`$link-color: #3b9ab2`, `$navbar-bg: #3b9ab2`. A small `global.css` removes link
underlines and heading borders, sets four heading sizes and gives code blocks a
soft grey gradient. There is no bespoke typeface pairing, no callout system, no
dark mode. Identity comes from one accent colour and the cover.

### Tidy Finance — the chapter anatomy

Every chapter runs the same way:

1. YAML with `title`, `metadata.pagetitle` and a `description-meta` line for search.
2. An opening paragraph that states the question the chapter answers, with the
   seminal citation attached to it. Modern Portfolio Theory opens on
   "How should an investor allocate their wealth across assets…" and cites
   @Markowitz1952 in the first sentence.
3. A sentence saying what the chapter will do: "we first derive the optimal
   portfolio decisions and implement the mean-variance approach".
4. The packages used, as a code block.
5. The theory, with display mathematics in the running text —
   $\mu_\omega = \omega'\mu$, $\sigma^2_\omega = \omega'\Sigma\omega$, the
   optimisation problem, then its closed-form solution.
6. The implementation in tidyverse code, results, figures, tables.
7. **Key Takeaways** — around five bullets.
8. **Exercises** — around three, numbered.

### ML for Factor Investing — what it adds

- A **notation chapter first**. Symbols, conventions for vectors and matrices,
  and the dataset are fixed before any content: "Bold notations indicate vectors
  and matrices. We use capital letters for matrices and lower case letters for
  vectors."
- **Citation density far above a handbook's.** Roughly 700 references; nearly
  every empirical claim carries one.
- **Coding exercises** closing each chapter.
- **Solutions to exercises** as an appendix.

### The shared DNA, in one line

Explain what is being done, state it in mathematics, attribute it to the
literature, implement it in R, then hand the reader takeaways and exercises.

---

## 2 · Where this book currently stands

Measured, not asserted:

| | This book | Tidy Finance | MLFI |
|---|---|---|---|
| Display equations in written chapters | **0** | many per chapter | many per chapter |
| Bibliography entries | **17** | several hundred | ~700 |
| Written chapters citing nothing at all | **6 of 8** | none | none |
| Exercises | none written | every chapter | every chapter |
| Key takeaways | none | every chapter | — |
| Stylesheet length | 338 lines | 3 + ~150 lines of CSS | bookdown default |
| Chapter voice | second person, aphoristic | first person plural, plain | first person plural, plain |

Three rules in `CLAUDE.md` actively push the book away from the target and have
to be reversed:

- **"No derivations in Parts I–VI."** Both reference books put the mathematics in
  the main text. Only *proofs* are exiled, and Tidy Finance exiles them to a
  `proofs.qmd` appendix rather than to a late chapter.
- **"Chapter length 3,000–5,000 words."** Too tight once theory, citations,
  takeaways and exercises are added. Tidy Finance chapters run longer.
- **The four beats.** "What you need / How to actually do it / What else is in
  there / Why it works" is a magazine device. No textbook is built this way, and
  it is the single most visible difference.

## 3 · What should *not* be thrown away

The book's genuine contribution is the part neither reference book has: the
documented behaviour of `PortfolioAnalytics` where it defaults wrongly, fails
silently or drops a constraint. Ten such traps are already measured and recorded
in `CLAUDE.md`.

This material survives the restructure. It stops being the organising principle
of a chapter and becomes a recurring, clearly marked element inside a normal
textbook chapter — a callout box titled by the trap, placed where the reader
would otherwise walk into it. Tidy Finance uses callouts the same way.

---

## 4 · Proposed table of contents

Renamed to descriptive textbook titles. The subject matter is unchanged; the
order changes in three places, each noted.

### Part I · Prerequisites
| New | Was | Note |
|---|---|---|
| 1 Setting Up Your Environment | 01 Tools of the Trade | R, `renv`, the package set |
| 2 Notation and Data | — | **new**, MLFI's opening move: fix every symbol once, describe both data universes |

### Part II · Foundations of Portfolio Choice
| New | Was | Note |
|---|---|---|
| 3 Return, Risk and the Investor's Problem | 03 Returns and the Investor | utility, excess returns, horizon, currency |
| 4 Descriptive Analysis of Asset Returns | 02 The Market | |
| 5 Factor Models and Beta Estimation | 02b Models for This Market | |

### Part III · Estimating the Inputs
| New | Was | Note |
|---|---|---|
| 6 Expected Returns | 04 | |
| 7 The Covariance Matrix | 05 | |
| 8 Estimation Error and Its Cost | 06 Why Estimates Matter | RAFE introduced here |

### Part IV · Portfolio Optimisation
| New | Was | Note |
|---|---|---|
| 9 Mean-Variance Optimisation | 07 | |
| 10 Risk Measures Beyond Variance | 08 | |
| 11 Higher Moments | 26 | **moved forward** — settles open decision 1: chapters 3 and 10 both lean on it |
| 12 Portfolio Constraints | 09 | |
| 13 Numerical Optimisation and Solvers | 11 | |
| 14 Risk-Based Allocation | 12 | |

### Part V · Allocation Strategies
| New | Was | Note |
|---|---|---|
| 15 Hierarchical and Sleeve-Based Allocation | 13 | |
| 16 Signals and Return Forecasts | 14 | |
| 17 Expressing Views | 15 | Black-Litterman, entropy pooling |
| 18 Parametric Portfolio Policies | 16 | |
| 19 Regime-Dependent Allocation | 17 | |
| 20 Sustainable Investing Constraints | 10 | **moved back** — it is an allocation constraint, and it is data-blocked |

### Part VI · Inside the Sleeves
| New | Was |
|---|---|
| 21 The Equity Sleeve | 18 |
| 22 The Fixed Income Sleeve | 19 |

### Part VII · Implementation and Evaluation
| New | Was |
|---|---|
| 23 Rebalancing and Transaction Costs | 20 |
| 24 Benchmarks and Active Risk | 21 |
| 25 Backtesting and Diagnostics | 22 |

### Part VIII · Advanced Topics
| New | Was |
|---|---|
| 26 The Cost of Forecast Error | 23 The Sharpe Gap |
| 27 Decision-Aware Forecasting | 24 |
| 28 Robustness and Model Uncertainty | 25 |

### Appendices
| New | Was | Note |
|---|---|---|
| A Data Description | — | **new**, MLFI has exactly this |
| B Proofs | — | **new**, Tidy Finance has exactly this; receives what the chapters no longer carry |
| C Solver Capability Matrix | 90 | |
| D Package Notes | 91 | |
| E An R Refresher | 92 | |
| F Coverage Ledger | 93 | |
| G Solutions to Exercises | 94 | |
| H Colophon and Changelog | — | **new**, both books have one |
| I Acknowledgements | 95 | |

---

## 5 · The new chapter contract

Replaces the four beats. Every chapter, without exception:

```
---
title: Descriptive Noun Phrase
metadata:
  pagetitle: ...
  description-meta: one sentence, for search
---

[Opening paragraph: the question this chapter answers, with the seminal
 citation in the first two sentences.]

[One sentence: what we do in this chapter, in order.]

[The packages used, as a code block.]

## Theory / The <name> problem
   Display mathematics. Every symbol as fixed in chapter 2. Every method
   attributed on first use.

## Implementation
   The R code, run, with real output.

## <Results / Application / Empirical section>
   Figures and tables on the simulated market.

## [Callout: what PortfolioAnalytics gets wrong here]
   Placed where the reader would walk into it.

## Key Takeaways
   Around five bullets.

## Exercises
   Around three, numbered.
```

## 6 · The new language rules

| Rule | Now | Proposed |
|---|---|---|
| Person | second person, "you" | **first person plural**, "we estimate", "we show" |
| Register | aphoristic, opinionated | **plain academic**, claim then evidence |
| Openings | slogans ("the first thing anybody learns and the last thing anybody trusts") | **the question, and who first asked it** |
| Mathematics | forbidden in Parts I–VI | **in the running text**; proofs to appendix B |
| Citations | 17 entries, 6 of 8 chapters cite nothing | **15–30 distinct citations per chapter**, every method attributed on first use |
| Section headings | questions and slogans | **noun phrases** |
| Chapter close | none | **Key Takeaways, then Exercises** |
| Numbers in prose | inline R, already correct | unchanged — keep |
| Package names | `code font` | unchanged — keep, functions always with `()` |

---

## 7 · What was settled

All with the user on 2026-09-12.

| Question | Decision |
|---|---|
| Spelling | **American.** Applied across the book's prose in one sweep; code untouched, because ggplot2's argument really is `colour`. |
| How far the restructure goes | **The full table of contents in §4.** Implemented: 19 stubs converted, 14 written files renamed, 4 new files created, `_freeze` carried across. |
| Depth of mathematics | **Mixed by part.** Parts II–IV at Tidy Finance depth, with proofs in appendix B. Part VIII derives in place. |
| The eight written chapters | **One first.** Chapter 9, mean-variance, is rewritten to the new contract as the reference chapter. The other seven follow once it is approved. |
| The bibliography | **Not yet settled.** Carried as open decision 6 in `PLAN.md`. |

### And two questions the restructure raised

| Question | Decision |
|---|---|
| Strategic and tactical as part names? | **No.** The parts are named for granularity, because that is the axis the book is actually built on: classes first, then inside the sleeves. Strategic and tactical are a second, orthogonal axis. They are defined once in chapter 3 and then used to label what each chapter does. Confusing the two axes was what made the first proposal feel wrong. |
| Asset class vocabulary | **Deferred to the new export.** The next dataset is 5 currencies × (government, corporate, equity) plus alternatives in USD, with the money market carried separately as the risk-free rate. The naming table belongs in chapter 2 when that lands. |

## 8 · What implementing it cost

- 19 stub chapters rewritten to the new skeleton. Every TODO from the retired
  four-beat plan is carried into the `PLANNING NOTE`, so nothing was lost.
- 14 written chapters and appendices renamed, prose untouched.
- 4 new files: chapter 2 *Notation and Data*, appendix A *Data Description*,
  appendix B *Proofs*, appendix H *Colophon and Changelog*.
- 15 cross-references repointed; a check for dangling `@sec-` references now
  returns zero.
- `PLAN.md` reordered and renumbered. 132 claims in, 134 out, the two new ones
  belonging to chapter 2. Nothing dropped.
- `_freeze` results moved with their chapters, so no computation was thrown away
  by the rename itself.
- Open decision 1, on where higher moments belong, is closed by the move to
  chapter 11.
