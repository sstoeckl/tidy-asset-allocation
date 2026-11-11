# Review log

Every comment Sebastian makes on a chapter, what was done about it, and whether
it became a rule. Nothing is deleted; items are checked off.

The process is in `review/README.md`. The short version: chapters go out as Word
documents, comments come back in the Word file, `tools/extract-docx-comments.py`
pulls each comment out together with the passage it is anchored to.

## Why this file exists

A comment that is fixed and forgotten will arrive again. This log exists so that
the second occurrence of a note is visible as the second occurrence, at which
point it stops being a fix and becomes a rule in `CLAUDE.md`.

Rules that came from review comments rather than from planning:

- **Figures are built from one data frame** — after three figures were found
  plotting one asset's volatility against another's return.
- **Assert that things fit together** — Sebastian's rule, after two silent
  ordering bugs in two days.
- **Cross-references in both directions** — every chapter reaches back to at
  least three and forward to at least two, and is reached by at least three.
  Checked by `tools/check-crossrefs.py`.
- **Data preparation is not chapter content**, **dominance vocabulary from
  chapter 3 onward**, **no "quiet" for low volatility**, **worked examples as
  formulas with the numbers in them** — all from the first Word round on
  chapter 9, 2026-09-13, logged below and promoted the same day.

## Open

*(nothing)*

## Done

### Found by the slide-deck agents, 2026-11-11

Each deck reuses its chapter's chunks by label, so building the decks read
every chapter's code once more. What came back, and what was done:

- [x] **09** — the two-asset table printed `NaN` at ρ = −1: the variance is
      zero to machine precision and came out as a tiny negative number under
      the square root. Floored at zero.
- [x] **01** — two inline expressions printed raw model dates into prose
      (`format(start(R), "%Y-%m")` and `format(date[5])`), against the
      calendar rule. Now `fmt_model()`.
- [x] **01** — `code/01-setting-up.R` read `renv.lock` from the project root
      and failed from `code/`. The lockfile now ships with the code downloads.
- [x] **04** — the caption of the tails table called the Cornish-Fisher
      figure "Gaussian-corrected"; reworded. The drawdown sentence read as a
      run-on; a colon. The clustering chunk assigned `exp`, masking
      `base::exp` for the rest of the chapter; renamed `expct`.
- [ ] **04** — the instability paragraph says rolling volatility never
      disagrees in sign, "which it cannot": true by construction, so the
      sign-flip column for volatility carries no information. Left as is; a
      sentence to reconsider when the chapter is read.
- [ ] **03** — "Chapters 9 to 14 and chapter 15" in the strategic/tactical
      paragraph; read as intended (Part IV, then the hierarchical chapter)
      and left.
- [x] **15** — the last `cache: true` (chunk `mult-run`) removed, so the
      chapter re-executes on every render like the others.
- [x] **code downloads** — section headings were written before the chunk
      header, so `read_chunk()` attached each to the previous chunk; a
      callout's own `## Title` was taken for a section; an exercise's inline
      R expression was printed raw; an exercise file pointed at a solutions
      file that does not exist. All four fixed in `tools/build-code.py`.

Open, for the restructuring pass that follows the reverse outline
(`review/outline/`, 2026-11-11); none of these blocks a render:

- [ ] **05** — "`US_credit` comes next … and both return later" is unclear;
      "at 1.93, 1.95 times the next one" reads like a typo though both
      numbers are right.
- [ ] **06** — an open `<!-- SS: -->` note on the market-weight proxy (line
      589); exercise 4's "the factor that the se equation predicts" does not
      say which factor; takeaway 1 states a measured median as if a law.
- [ ] **07** — `tbl-07-race` and `the-tie` print row names as a first column
      (`row.names = FALSE`); `rank-by-level` prints the smallest eigenvalue as
      a long decimal; the long-only "comparable work for nothing" claim is
      asserted, not computed (exercise 4 computes it).
- [ ] **08** — the `usable` column of the rebalancing-trap table mixes types;
      the worked callout says its simulation checks non-normality and draws
      from a normal.
- [ ] **09** — three pointers to a callout explaining why `maxSR = TRUE` is
      avoided ("the callout below explains why"), and no such callout exists;
      the inputs subsection plots total returns while every solve uses excess
      returns, without saying so; "Three ways this fails" walks four.
- [ ] **10** — "Three of the four bold cells carry the asterisk" is typed,
      not computed, and goes false if the search ever wins its own column.
- [ ] **12** — a code comment counts seven constraint lines where `build()`
      sets six; the group-weights figure uses a 20% equity floor and the
      mandate 40% without saying they differ; exercise 1 needs `build()` and
      `tighten` from the mandate chunks.
- [ ] **14** — the takeaway on "effective bets" halving uses the
      participation ratio of the eigenvalues, while the chapter defines
      effective bets by the entropy of risk shares: two measures under one
      name.
- [ ] **19** — "None of this is distinguishable from sampling error" holds
      for the two detected strategies only (the dated switch has a paired z of
      2.78); "about half" of the excess kurtosis is typed, not inline.
- [ ] **21** — the observation-check callout never says the pinned build
      lifts the check with `allow.fewer.obs = TRUE`; several captions type
      their numbers ("372 month-starts", "123 equities", "observation 121").

### 09 · Mean-Variance Optimization — first Word round, 2026-09-13

Five comments on the first part of the chapter, extracted 2026-09-13 20:35.
Sebastian's summary: "relatively okay with it, except some language things".

- [x] **2026-09-13 20:30** — *"The data prep should be outside of the chapter,
  right? Maybe start with the mu-sigma plot. Was the efficient frontier
  described before?"*
  > `R <- as_xts_pm(sim_class_returns_monthly, ...); R <- R[, !grepl("money_market", ...)]; rf <- ...`

  Done, in three parts. (i) The money-market split is now taken once, in the
  `tidypm` import: `sim_class_returns_monthly` ships the sixteen risky series
  and `sim_money_market_monthly` the five money markets, so no chapter drops
  anything in its first code block. The remaining two lines — load, and
  subtract the bill — stay, each pointing at the chapter that explains it
  (2 for the universe, 3 for excess returns). (ii) The mean–volatility
  scatter of the sixteen series is the first figure of the implementation
  section, with the dominance vocabulary applied to it. (iii) The efficient
  frontier is defined in the theory section before any code uses it, and the
  definition now distinguishes the minimum-variance frontier from its
  efficient upper branch. **Promoted to a rule** ("Data preparation is not
  chapter content", `CLAUDE.md`), and applied to all eight written chapters.

- [x] **2026-09-13 20:32** — *"I dont think I wanted that as R but as formula
  based calculations with the real numbers from the example. But it may stay
  like this, not sure"*
  > `pair <- c("US_equity", "US_government") ... s1 <- stats::sd(X[, 1]) * sqrt(12)`

  Done both ways. The two-asset weight and the portfolio volatility are now
  display equations with the sample moments substituted in (via inline R, so
  the numbers are computed rather than typed), and the code that follows is
  the check that reproduces them. **Promoted to a rule** ("Worked examples
  show the formula with the numbers in it").

- [x] **2026-09-13 20:32** — *"Quiet?"*
  > quieter

  Done. Every "quiet", "quieter", "quietest" used for low volatility is gone
  from chapters 9, 7, 14 and 25, in prose and in variable names
  (`lowest_vol_asset`, not `quietest_asset`). **Promoted to a rule** (language
  table, `CLAUDE.md`).

- [x] **2026-09-13 20:33** — *"How about dominant and dominated and efficient
  assets? Do we want to mention that? Like better allocation always lies to
  the northwest?"*
  > It is the portfolio with the highest Sharpe ratio (Sharpe 1966), the point at which a ray from the risk-free rate touches the frontier.

  Done. The theory section of chapter 9 now defines dominance, efficiency
  and the northwest rule right after the two moments, attributes them to
  Markowitz, and points to chapter 3 where the criterion is introduced as
  the investor's problem. The implementation section applies the vocabulary
  to the sixteen series (which are dominated, by how many, and which are
  efficient) before any optimizer runs. Chapter 3, being written now, carries
  the definition. **Promoted to a rule** ("Dominance vocabulary from chapter
  3 onward").

- [x] **2026-09-13 20:35** — *"Say 'dominated' not 'beaten'. Closes my
  previous comment"*
  > 12 of 16 series are beaten on both axes by at least one other, and JP_equity is beaten by

  Done. "Beaten" is gone; the count of dominating alternatives is computed
  rather than typed ("eleven of the fifteen" was a hard-coded number, which
  the data restart would have made false). Same rule as above.
