# The out-of-sample sweep.
#
# Runs the book's strategy register across every combination of universe,
# estimation window and rebalancing frequency that a chapter might cite, and
# writes one row per (universe, window, frequency, strategy, basis).
#
# This is the source of the single out-of-sample line each construction chapter
# carries, and the whole of chapters 20 to 22. It is expensive -- the
# instrument-level universe is 176 assets over 372 months -- so it is meant to
# be run once, overnight, and committed as its result table.
#
#   Set-Location "...\Tidy_Asset_Allocation"
#   & "C:\R\R-4.6.1\bin\Rscript.exe" R/oos-sweep.R
#
# Incremental: every configuration is written to disk as it finishes and skipped
# on a re-run, so an interrupted sweep resumes where it stopped.

stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
suppressPackageStartupMessages({
  library(tidypm); library(PortfolioAnalytics); library(xts); library(dplyr)
})

OUT <- "output/tables/oos"
LOG <- "output/logs/oos-sweep.log"
dir.create(OUT, recursive = TRUE, showWarnings = FALSE)
dir.create(dirname(LOG), recursive = TRUE, showWarnings = FALSE)
say <- function(...) {
  line <- sprintf(...)
  cat(line, "\n", sep = "")
  cat(format(Sys.time(), "%H:%M:%S "), line, "\n", sep = "", file = LOG, append = TRUE)
}

WORKERS <- max(1L, min(8L, parallel::detectCores() - 4L))
say("sweep starting, %d workers, PortfolioAnalytics %s",
    WORKERS, as.character(packageVersion("PortfolioAnalytics")))

# ---- universes ---------------------------------------------------------------

classes <- as_xts_pm(sim_class_returns_monthly, date, class, return)

mm_ids  <- sim_assets$asset_id[sim_assets$asset_class == "money_market"]
instr   <- as_xts_pm(sim_asset_returns_monthly, date, asset, return)
instr   <- instr[, !colnames(instr) %in% mm_ids]

equity_ids <- sim_assets$asset_id[sim_assets$asset_class == "equity"]
equities   <- instr[, colnames(instr) %in% equity_ids]

# The allocation spine is the asset classes. Chapters 7 to 17 never leave them:
# strategic and tactical allocation happen across classes, and the descent into
# individual instruments belongs to the sleeve chapters, 18 and 19.
#
# The instrument-level universes are therefore deferred rather than dropped.
# They cannot run against this register in any case: a sample covariance over
# 123 equities has rank at most T, so a 120-month window is already singular and
# minimum variance has no solution. Fixing that is what shrinkage is for, and
# shrinkage is introduced in chapter 5 -- before the sleeve chapters need it,
# not after. Re-enable these once that estimator exists.
universes <- list(classes = classes)
deferred  <- list(equities = equities, instruments = instr)
for (u in names(universes)) say("  universe %-12s %3d assets", u, ncol(universes[[u]]))
for (u in names(deferred))
  say("  deferred to ch. 18-19: %-12s %3d assets", u, ncol(deferred[[u]]))

# Costs are per asset class, so the instrument-level universes need a per-asset
# vector rather than the class-keyed default.
cost_vec <- function(R) {
  d <- pm_costs_default()
  cl <- sim_assets$asset_class[match(colnames(R), sim_assets$asset_id)]
  if (all(is.na(cl))) return(d)              # class-level universe: names match already
  setNames(unname(d[cl]), colnames(R))
}

# ---- the grid ----------------------------------------------------------------

WINDOWS <- c(36L, 60L, 120L)

grid <- tidyr::expand_grid(
  universe  = names(universes),
  window    = WINDOWS,
  frequency = c("months", "quarters", "years")
)

say("%d configurations", nrow(grid))

# Hold the out-of-sample period fixed across estimation windows.
#
# Without this the comparison is confounded: a longer estimation window pushes
# the first out-of-sample month later, so the three windows are scored on three
# different histories. The control that reveals it is equal weighting, which
# estimates nothing at all and still moved by 0.09 in Sharpe across "windows".
#
# Feeding each run a panel that starts `window` months before the common first
# out-of-sample month makes every configuration score the same months.
FIRST_OOS <- max(WINDOWS) + 1L
say("out-of-sample begins at observation %d for every window (%s)",
    FIRST_OOS, format(zoo::index(classes)[FIRST_OOS]))

trim_to_common_oos <- function(R, window) R[(FIRST_OOS - window):nrow(R), ]

# ---- run ---------------------------------------------------------------------

for (i in seq_len(nrow(grid))) {
  g   <- grid[i, ]
  tag <- sprintf("%s_w%d_%s", g$universe, g$window, g$frequency)
  f   <- file.path(OUT, paste0(tag, ".csv"))
  if (file.exists(f)) { say("[%2d/%2d] %-28s cached", i, nrow(grid), tag); next }

  R <- trim_to_common_oos(universes[[g$universe]], g$window)
  t0 <- Sys.time()
  bt <- tryCatch(
    pm_backtest(R,
                riskfree          = sim_riskfree_monthly,
                estimation_window = g$window,
                rebalance_on      = g$frequency,
                costs             = cost_vec(R),
                workers           = WORKERS,
                verbose           = FALSE),
    error = function(e) e
  )
  el <- as.numeric(difftime(Sys.time(), t0, units = "mins"))

  if (inherits(bt, "error")) {
    say("[%2d/%2d] %-28s FAILED after %.1f min: %s", i, nrow(grid), tag, el,
        sub("\n.*", "", conditionMessage(bt)))
    writeLines(conditionMessage(bt), file.path(OUT, paste0(tag, ".error.txt")))
    next
  }

  res <- bt$metrics |>
    mutate(universe = g$universe, n_assets = ncol(R),
           window = g$window, frequency = g$frequency,
           minutes = round(el, 2), .before = 1)
  readr::write_csv(res, f)

  fails <- sum(res$n_failed[res$basis == "gross"])
  say("[%2d/%2d] %-28s done in %5.1f min, %d solver failure%s",
      i, nrow(grid), tag, el, fails, if (fails == 1) "" else "s")
}

# ---- assemble ----------------------------------------------------------------

files <- list.files(OUT, pattern = "[.]csv$", full.names = TRUE)
all <- lapply(files, readr::read_csv, show_col_types = FALSE) |> bind_rows()
readr::write_csv(all, "output/tables/oos-sweep.csv")
say("wrote %d rows over %d configurations to output/tables/oos-sweep.csv",
    nrow(all), length(files))

say("")
say("=== headline: monthly rebalancing, 60-month window ===")
all |>
  filter(window == 60L, frequency == "months", basis == "gross") |>
  select(universe, n_assets, strategy, ann_return, ann_vol, sharpe,
         es_95, max_drawdown, ann_turnover, n_failed) |>
  as.data.frame() |>
  print(digits = 3, row.names = FALSE)

say("")
say("=== what the estimation window does, classes, monthly ===")
all |>
  filter(universe == "classes", frequency == "months", basis == "gross") |>
  select(window, strategy, sharpe, ann_vol, ann_turnover, n_failed) |>
  tidyr::pivot_wider(names_from = window, values_from = c(sharpe, ann_vol),
                     id_cols = strategy) |>
  as.data.frame() |>
  print(digits = 3, row.names = FALSE)

say("")
say("=== the cost bite, everywhere ===")
all |>
  select(universe, window, frequency, strategy, basis, sharpe) |>
  tidyr::pivot_wider(names_from = basis, values_from = sharpe) |>
  mutate(bite = gross - net) |>
  group_by(strategy) |>
  summarise(median_gross = median(gross), median_net = median(net),
            median_bite = median(bite), worst_bite = max(bite)) |>
  as.data.frame() |>
  print(digits = 3, row.names = FALSE)
