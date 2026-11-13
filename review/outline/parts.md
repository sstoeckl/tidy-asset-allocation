# Book

Claim: As the preface argues it, asset allocation is hard in the chain of implementation decisions (data, estimation, solver, costs) and not in the ideas, so the book states each method, attributes it, runs it on a modeled market, and measures how much of the textbook answer survives out of sample.
What the chapters jointly argue:
- The mean cannot be estimated and the covariance can, so the rules that estimate no mean lead the out-of-sample register (chapters 4, 6, 8, 9, 25).
- On sixteen classes almost every refinement changes little or cannot be told from sampling error: expected shortfall for variance (10), higher moments (11), signals other than the term spread (16), regimes detected in real time (19), robustness sets (28), and the nested allocation loses to the flat one (15).
- Constraints are the precondition for a portfolio anyone would hold, and a binding constraint is a cost with a price (12, 20, 22).
- The package accepts what it does not honor, so every solved weight vector is audited (9, 10, 12, 13, 22, 23, 25).
- Forecast error should be priced in the investor's metric and not in squared error (26, 27).
Order: Prerequisites (1–2), Foundations of Portfolio Choice (3–5), Estimating the Inputs (6–8), Portfolio Optimization (9–14), Allocation Strategies (15–20), Inside the Sleeves (21–22), Implementation and Evaluation (23–25), Advanced Topics (26–28).
Why this order: One sentence in the preface: the parts follow the allocation hierarchy, classes in Parts II to V, securities in VI, implementation in VII, theory in VIII; strategic versus tactical is a second axis labeled chapter by chapter. Part I is never placed, no part has an introduction of its own, and no text says why the inputs (III) come before the optimizer (IV) or why evaluation (VII) comes after the strategies it scores.
Dependencies against the order:
- Chapter 1 borrows its notation and its market from chapter 2.
- Chapter 2 runs chapter 9's long-only tangency portfolio to justify the euro-area overlay, before the reader has met an optimizer.
- Chapters 6, 7 and 8 use chapter 9's problem, its tangency and minimum-variance equations and its frontier as if already read.
- Chapter 6 already reads the out-of-sample register, chapter 8 takes its rolling scheme and its Sharpe gap from chapter 25, and some fourteen chapters close on a line of that register before chapter 25 explains it. The register itself is computed by a script outside the chapters (`R/oos-sweep.R`); no chapter builds it.
- Chapters 9, 10 and 11 teach solver behavior before chapter 13, and chapters 14, 15, 16 and 22 use chapter 23's costs and chapter 25's backtest before either arrives.
- Chapter 12 borrows chapter 13's `maxSR` verification and its `audit()` function, and the fundamental law from chapter 24.
- Chapter 18 uses chapter 23's net return and turnover and chapter 25's Sharpe standard error and paired test, in the past tense.
- Chapter 19 needs chapter 23's cost accounting and chapter 25's register.
- Chapter 20 is built on chapter 21's equity sleeve and on chapter 24's tracking-error and standard-error equations.
- Chapter 21 imports its whole scoring apparatus from chapter 24: active weights, information ratio, the fundamental law, the standard error of the ratio.
- Chapter 23 computes none of its numbers; it reads them from the runs of chapter 25, and its opening premise (every portfolio so far was rebalanced for free) is contradicted by chapters 16 and 18 to 22, which already charge costs.
- Chapter 24 leans on chapter 25 five times and defines its manager by a register rank.
- Three cycles: 24 and 25 (Brinson attribution defined in both, each handing it to the other), 12 and 13 (each takes the other's tools), 18 and 23 (costs in the objective one way, the no-trade region the other).
Patterns across chapters:
- The section called Implementation carries the results, and the section meant as the application re-reads them or adds one more case: at least fifteen chapters (4, 5, 9, 10, 11, 13, 16, 17, 18, 19, 22, 24, 26, 27, 28). Measured over the 27 narrative chapters the implementation holds 38 percent of the words and the application 28, and the implementation is the longer of the two in 20. In 15 the theory does the application's work in advance; in 14 each section does the next one's job.
- The chapter's central claim sits in a late paragraph and not under a heading or in the theory: 8 (last paragraph of a subsection), 17 (application, fourth paragraph), 22 (one theory paragraph without an equation), 27 (end of the implementation).
- Objects the later code depends on are defined inside collapsed worked boxes or callouts: 6, 10, 11.
- Theory that is defined and then never used in the body: lower partial moments and drawdown measures (10), conditional comoments (11), C-RAFE and the nested measures (26, exercises only), robust optimization and smooth ambiguity (28).
- Theory sections that already compute or run the package: 3, 13, 14, 15.
- Results stated three or four times: the two numbers of chapter 13, the reporting rule in chapter 10, the answer of chapter 8, the chapter anatomy in the preface.
- Figures that the prose never reads, or reads only through the caption (2, 4, 10, 12, 15, 16, 19, 22, 23, 24, 25, 26), or reads before they appear (3, 5, 9, 13, 15, 21); tables printed and never read (7, 12, 17). Only four applications open with a picture (3, 9, 11, 27), and chapter 14 has no figure.
- Main section headings with no paragraph of their own in at least sixteen chapters (6, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28), so one roadmap sentence in the opening carries every transition.
- Two chapters inside one frame: 1 (toolchain and the boundary argument, interleaved), 3 (the conventions, then the investor), 9 (the frontier, a catalogue of solver failures, five studies on the frontier), 15 (the economics of two layers, a source reading of the package), 24 (measuring a manager out of sample, then constructing a tilt in sample, with no sentence marking the turn). Fragments: 13, 14, 23 and 25; chapters 23 and 25 are one chapter cut in two. Chapter 2 is a reference chapter with no theory, implementation and application at all.
- Counts that do not close: chapter 9 points three times to a callout on `maxSR` that does not exist; "three ways" that are four in 9 and 17; a signal count in 16 that names four families and claims three.
- Takeaways and exercises run over the contract almost everywhere (six to eight takeaways, four or five exercises), and in 11 and 21 the takeaways omit the application's finding.
- Lengths differ by a factor of three: chapters 13, 14, 23 and 25 have about 3,300 words, chapter 9 has 10,239, most others 6,500 to 8,000.
Revised: 2026-11-13, after three independent assessments (`review/assessment/`) checked this block against the outline. They confirmed the dependencies and the patterns and corrected four things, now entered above: the register is read from chapter 6 on and built outside the book; three cycles; the counts for results in the implementation, heading-only sections and unread figures were too low; the order inside Part VIII is stated.
Open at the top level:
- Evaluation is used before it is taught. Should the accounting of Part VII (net return, turnover, the register, the Sharpe standard error, the information ratio) come before the strategies that are scored with it?
- The inputs are estimated for an optimizer the reader has not met. Should chapter 9 precede Part III, or should Part III stop using its equations?
- Is "Implementation" the method and "Application" the result? Ten chapters put the result into the implementation.
- Does the book want parts with a text of their own, saying what the part argues and why it sits where it does?

# Part: Front matter

Says: The preface says why the book exists, whom it serves, how a chapter is built, how the parts are ordered, what the data are, and how to rebuild the book.
Why here: Not stated beyond its being the preface.
Note: The chapter anatomy is told in full twice, Part VIII is described three times, and part numbers are used one section before the parts are laid out; that layout never mentions Part I.

# Part: Prerequisites

Says: The tools and the data are fixed once: the crossing between the long table and the date-indexed matrix, guarded by assertions (1), and the notation, the modeled market with its calendar, and the real-data layer (2).
Why here: Stated in the chapters only: the boundary "is crossed in every chapter and is therefore fixed here once" (1), and the notation is fixed "so that no later chapter redefines a symbol" (2). The preface's account of the parts leaves Part I out.
Note: Chapter 1 interleaves two subjects, the toolchain and the boundary argument, and borrows its market from chapter 2. Chapter 2 is a reference chapter; nearly half of it is the modeled-market section, and its caveats subsection runs an optimizer from chapter 9.

# Part: Foundations of Portfolio Choice

Says: The investor's problem and the conventions it rests on (3), what the sixteen series look like and which moment can be trusted (4), and how little a single factor explains once it is measured properly (5).
Why here: Chapter 3 says its definitions are fixed here so that no later chapter revisits them; chapter 4 says nothing later is interpretable without it; chapter 5 calls itself the continuation of chapter 4. Why factor models come before the inputs is not stated.
Note: Chapter 3 is two chapters in one frame and close to 8,000 words. In chapters 4 and 5 the section called Implementation holds the results, and the section meant as the application holds a derivation (4) or two further studies (5).

# Part: Estimating the Inputs

Says: No history pins a mean down, so the strategic vector is the equilibrium or a shrunk mean (6); the covariance is singular at instrument level and four routes repair it (7); estimation error costs most where the mean is estimated (8).
Why here: Stated through the ranking of input errors: the mean is the hard input, the covariance the large one, and chapter 8 "measures what they cost together". The part still precedes the optimizer it serves and uses chapter 9's equations throughout.
Note: Chapter 6's conclusions rest on a class-level equilibrium built inside a collapsed box the text calls a placeholder. Chapter 7's four routes break off halfway, and its race scores an estimator the chapter never introduced. Chapter 8's answer has no heading of its own.

# Part: Portfolio Optimization

Says: The textbook frontier and how far resampling moves it (9), then five variations: another risk measure (10), more moments (11), constraints (12), solvers (13), risk instead of capital (14). Two of the five change little (10, 11); the other three say the answer depends on constraints, convexity and an audit.
Why here: Chapter 9 calls itself the point every later method departs from; chapters 10, 13 and 14 each give one opening sentence ("every portfolio so far…"). Why constraints (12) come before the solvers (13) whose audit they borrow is not stated.
Note: Chapter 9 runs to 10,239 words, 4,889 of them application, and points to a callout that is not there. Chapter 12's implementation is a catalogue of ten constraint families, 47 percent of the chapter. Chapters 13 and 14 are less than half as long as their neighbors.

# Part: Allocation Strategies

Says: Six ways to organize or to deviate from the policy: nesting (15), signals (16), views (17), parametric policies (18), regimes (19), sustainability constraints (20). Their common result is that little of the deviation survives out of sample or can be told from sampling error.
Why here: Each chapter places itself only on the strategic or tactical side of chapter 3's axis. Why these six stand in this order, why 15 opens the part and why 20 closes it, is not stated anywhere.
Note: Chapters 18, 19 and 20 depend on Parts VI and VII, which come later. In 16, 17, 18 and 19 the main result sits in the implementation. Chapter 15's theory announces the out-of-sample verdict before the race is run.

# Part: Inside the Sleeves

Says: Selection inside the equity budget reaches the total scaled by that budget, and what the total registers is the sleeve's lower variance (21); a duration target is a factor-exposure constraint on a minimum-variance program (22).
Why here: Stated: this is the granularity axis made concrete, one level below the class series on which Parts III to V allocated.
Note: Chapter 21 scores everything with chapter 24's measures. Chapter 22 argues twice that an unhedged duration target controls a minority of a foreign bond's risk and then builds every sleeve unhedged; the hedged sleeve is exercise 1.

# Part: Implementation and Evaluation

Says: What trading costs take from each strategy (23), what beating a benchmark means and why skill cannot be settled at this sample length (24), and a backtest as a statistical estimate with an error bar (25).
Why here: Each chapter says it in its first sentence: every portfolio so far was rebalanced at no charge (23); this is where the lines of out-of-sample evidence come from (25). The part's accounting is nevertheless used by chapters 8 and 15 to 22 before it arrives.
Note: Chapter 23 runs no backtest and reads every number from chapter 25's runs. Chapter 25 ends twice: after its application come two theory subsections without code that the opening never announced. Chapters 23 and 25 have about 3,300 words each, chapter 24 has 7,244.

# Part: Advanced Topics

Says: The cost of a wrong forecast is a distance in the investor's metric (26), a forecaster should be trained on that loss (27), and guarding against a set of models is a shrinkage toward minimum variance (28).
Why here: The preface says only that Part VIII is theory. Chapters 26 and 27 place themselves on neither side of the horizon axis, chapter 28 calls itself strategic. The order inside the part is stated in chapter 28: 26 prices the forecast error, 27 corrects the forecast, 28 changes the decision.
Note: In 26 and 27 the implementation is about half the chapter and already states every headline finding. In 28 the four robustifications run in the reverse of the theory's order, the longest of them has no theory and no out-of-sample row, and two theory subsections are never implemented.
