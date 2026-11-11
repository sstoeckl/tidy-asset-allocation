# Recompute every load-bearing number the book and CLAUDE.md assert.
#
# Run after any change to the simulated market, or before trusting a claim that
# was measured on an earlier export:
#
#   Set-Location "...\Tidy_Asset_Allocation"
#   & "C:\R\R-4.6.1\bin\Rscript.exe" R/verify-claims.R
#
# Every claim is stated with the value it was measured at, and flagged when the
# new value moves outside the tolerance. Nothing here decides anything; it only
# tells you which sentences in the book have stopped being true.
#
# Expected values are pinned to dataset 6.2.0 (2026-11-09). The 4.3.0 values are
# kept in the comments where a claim moved, so that the history of a number is
# visible.

stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
suppressPackageStartupMessages({
  library(xts); library(PortfolioAnalytics); library(PerformanceAnalytics)
})

PKG <- "../tidypm/data"
for (f in c("sim_assets", "sim_class_returns_monthly", "sim_money_market_monthly",
            "sim_asset_returns_monthly", "sim_riskfree_monthly", "sim_fx_monthly",
            "sim_marketcap_weekly", "sim_asset_returns_weekly")) {
  load(file.path(PKG, paste0(f, ".rda")))
}

# --- reporting ---------------------------------------------------------------

results <- list()
claim <- function(id, what, expected, actual, tol, unit = "") {
  ok <- is.na(expected) || abs(actual - expected) <= tol
  results[[length(results) + 1L]] <<- data.frame(
    id = id, claim = what, was = expected, now = actual,
    moved = ifelse(is.na(expected), NA, !ok), stringsAsFactors = FALSE)
  cat(sprintf("%-4s %-52s was %8s   now %8s  %s\n", id, substr(what, 1, 52),
              ifelse(is.na(expected), "-", sprintf("%.3f", expected)),
              sprintf("%.3f", actual),
              ifelse(is.na(expected), "", ifelse(ok, "ok", "<< MOVED"))))
  invisible(ok)
}

wide <- function(df, id, val = "return") {
  w <- reshape(as.data.frame(df[, c("date", id, val)]), idvar = "date",
               timevar = id, direction = "wide")
  names(w) <- sub(paste0(val, "."), "", names(w), fixed = TRUE)
  w <- w[order(w$date), ]
  xts(as.matrix(w[, -1]), order.by = as.Date(w$date))
}

ann <- function(x, p = 12) prod(1 + x)^(p / length(x)) - 1
mdd <- function(x) { i <- cumprod(1 + x); min(i / cummax(i)) - 1 }

R   <- wide(sim_class_returns_monthly, "class")        # the sixteen risky classes
MM  <- wide(sim_money_market_monthly, "class")         # the five money markets
rf  <- sim_riskfree_monthly$return
rfa <- ann(rf)
risky <- R
stopifnot(ncol(risky) == 16L, ncol(MM) == 5L, identical(index(R), index(MM)))

cat("\n=== panel ===\n")
cat(sprintf("%d months, %d risky class series + %d money markets, %d instruments, %s to %s\n",
            nrow(R), ncol(R), ncol(MM), length(unique(sim_asset_returns_monthly$asset)),
            format(min(index(R))), format(max(index(R)))))
cat(sprintf("risk-free annualised %.2f%%, negative in %d of %d months\n\n",
            100 * rfa, sum(rf < 0), length(rf)))

# --- 1. the money market is a duration asset, not the bill -------------------
#
# 4.3.0 had US_money_market negative in 38% of months with a -10.5% drawdown,
# because the source model omitted the rolldown. 5.0.0 credits it and the
# drawdown collapses to under one percent. The argument for shipping the bill
# separately survives in a weaker form: the money market is marked to market
# and carries duration, so its sign pattern differs from the bill's.

cat("=== 1. the money market is not the bill (ch. 2, 3, 4) ===\n")
mm <- as.numeric(MM[, "US_money_market"])
claim("1a", "share of months US_money_market is negative", 0.188, mean(mm < 0), 0.03)   # was 0.384
claim("1b", "US_money_market max drawdown",               -0.009, mdd(mm),      0.01)   # was -0.105
claim("1c", "share of months the bill is negative",        0.003, mean(rf < 0), 0.01)
claim("1d", "correlation US_money_market with the bill",   0.930, cor(mm, rf),  0.03)

gmv <- function(S) {
  n <- ncol(S); A <- cbind(rep(1, n), diag(n)); b <- c(1, rep(0, n))
  f <- tryCatch(quadprog::solve.QP(2 * S, rep(0, n), A, b, meq = 1), error = function(e) NULL)
  if (is.null(f)) NULL else setNames(pmax(f$solution, 0), colnames(S))
}
# Informational: what minimum variance over all 21 would do. 4.3.0 put 99.3%
# into US_money_market. Not a claim the book makes any more, since the money
# markets are no longer in the class universe.
w_all <- gmv(cov(cbind(R, MM)) * 12)
cat(sprintf("     (info) GMV over all 21: %.1f%% in %s\n",
            100 * max(w_all), names(which.max(w_all))))

# --- 2. concentration without constraints ------------------------------------

cat("\n=== 2. unconstrained optimisation is degenerate (ch. 9, 12) ===\n")
w_r <- gmv(cov(risky) * 12)
claim("2a", "GMV on the risky set: largest weight", 0.818, max(w_r), 0.10)   # was 0.832
cat("     largest is:", names(which.max(w_r)), "\n")

# --- 3. the objective moves the portfolio ------------------------------------

cat("\n=== 3. the investor's objective moves the SAA (ch. 3, 10, 11) ===\n")
base <- add.constraint(add.constraint(portfolio.spec(colnames(risky)),
                                      "full_investment"), "long_only")
specs <- list(
  min_variance = add.objective(base, type = "risk", name = "var"),
  quad_lambda2 = add.objective(add.objective(base, type = "return", name = "mean"),
                               type = "risk", name = "var", risk_aversion = 2),
  min_ES_95    = add.objective(base, type = "risk", name = "ES",
                               arguments = list(p = 0.95))
)
wts <- lapply(specs, function(s) {
  o <- tryCatch(optimize.portfolio(risky, s, optimize_method = "ROI", trace = FALSE),
                error = function(e) NULL)
  if (is.null(o)) NULL else extractWeights(o)
})
if (!any(vapply(wts, is.null, logical(1)))) {
  cr <- vapply(wts, function(w) unname(w["US_credit"]), numeric(1))
  claim("3a", "US_credit weight under quadratic utility, lambda 2", 0.095, cr[["quad_lambda2"]], 0.10)
  claim("3b", "US_credit weight under minimum ES",                  0.000, cr[["min_ES_95"]],   0.05)
  claim("3c", "spread in US_credit weight across objectives",       0.095, max(cr) - min(cr),   0.10)
  pr_es <- as.numeric(risky %*% wts$min_ES_95)
  pr_q2 <- as.numeric(risky %*% wts$quad_lambda2)
  claim("3d", "skewness of the minimum-ES portfolio",  -0.060, skewness(pr_es), 0.30)
  claim("3e", "skewness of the lambda-2 portfolio",    -0.618, skewness(pr_q2), 0.30)
  claim("3f", "max drawdown of the lambda-2 portfolio", -0.418, mdd(pr_q2),     0.08)
} else {
  cat("     one or more objectives failed to solve -- investigate before trusting ch. 3\n")
}

# --- 4. credit is the asset variance cannot see ------------------------------

cat("\n=== 4. credit's skew is the point (ch. 10, 11) ===\n")
claim("4a", "US_credit annualised Sharpe over the bill", 0.560,
      (ann(as.numeric(R[, "US_credit"])) - rfa) / (sd(R[, "US_credit"]) * sqrt(12)), 0.10)  # was 0.481
claim("4b", "US_credit skewness", -1.449, skewness(as.numeric(R[, "US_credit"])), 0.25)     # was -1.298
sh <- sapply(colnames(risky), function(s)
  (ann(as.numeric(risky[, s])) - rfa) / (sd(risky[, s]) * sqrt(12)))
cat("     best Sharpe in the risky set:", names(which.max(sh)),
    sprintf("(%.3f); US_credit ranks %d of %d\n", max(sh), rank(-sh)[["US_credit"]], length(sh)))

# --- 5. estimation error, out of sample --------------------------------------

cat("\n=== 5. 1/N against optimisation out of sample (ch. 8, 25) ===\n")
maxsr <- function(S, mu) {
  n <- ncol(S); A <- cbind(mu, diag(n)); b <- c(1, rep(0, n))
  f <- tryCatch(quadprog::solve.QP(2 * S, rep(0, n), A, b, meq = 1), error = function(e) NULL)
  if (is.null(f) || sum(pmax(f$solution, 0)) <= 0) NULL
  else setNames(pmax(f$solution, 0) / sum(pmax(f$solution, 0)), colnames(S))
}
Tn <- nrow(risky); win <- 60; n <- ncol(risky)
oos <- matrix(NA_real_, Tn, 3, dimnames = list(NULL, c("equal", "gmv", "maxsr")))
for (t in (win + 1):Tn) {
  est <- risky[(t - win):(t - 1), ]
  Se <- cov(est) * 12; mue <- colMeans(est) * 12 - mean(rf[(t - win):(t - 1)]) * 12
  cand <- list(equal = rep(1 / n, n), gmv = gmv(Se), maxsr = maxsr(Se, mue))
  for (s in colnames(oos)) if (!is.null(cand[[s]])) oos[t, s] <- sum(cand[[s]] * risky[t, ])
}
oos <- oos[(win + 1):Tn, ]; rfo <- rf[(win + 1):Tn]
shp <- apply(oos, 2, function(x) (ann(x) - ann(rfo)) / (sd(x) * sqrt(12)))
claim("5a", "1/N Sharpe, 60m rolling, out of sample",   0.536, shp[["equal"]], 0.08)   # was 0.302
claim("5b", "max-Sharpe Sharpe, same window",           0.527, shp[["maxsr"]], 0.08)   # was 0.135
claim("5c", "GMV Sharpe, same window",                  0.654, shp[["gmv"]],   0.08)   # was 0.353
claim("5d", "1/N advantage over max-Sharpe", -0.002, shp[["equal"]] - shp[["maxsr"]], 0.10)  # was 0.167

# --- 6. currency ---------------------------------------------------------------

cat("\n=== 6. currency is a first-order driver (ch. 3, 4, 15, 22) ===\n")
hedged <- function(x, rg) {
  fx <- sim_fx_monthly[sim_fx_monthly$region == rg, ]
  as.numeric(x) - fx$fx_return[match(index(x), fx$date)]
}
claim("6a", "JP money market vol, unhedged", 0.101, sd(MM[, "JP_money_market"]) * sqrt(12), 0.02)
claim("6b", "JP money market vol, hedged",   0.003, sd(hedged(MM[, "JP_money_market"], "JP")) * sqrt(12), 0.02)
claim("6c", "EU government vol, hedged",     0.039, sd(hedged(R[, "EU_government"], "EU")) * sqrt(12), 0.02)  # was 0.045
claim("6d", "JP government vol, unhedged",   0.108, sd(R[, "JP_government"]) * sqrt(12), 0.02)
claim("6e", "JP government vol, hedged",     0.032, sd(hedged(R[, "JP_government"], "JP")) * sqrt(12), 0.02)

# --- 7. conditioning -----------------------------------------------------------

cat("\n=== 7. the instrument covariance is ill-conditioned (ch. 7, 21) ===\n")
Ra <- wide(sim_asset_returns_monthly, "asset")
ev <- eigen(cov(Ra), symmetric = TRUE, only.values = TRUE)$values
claim("7a", "log10 condition number, all instruments", 12.4,
      log10(max(ev) / min(ev)), 1.5)                                   # was 12.2
cmd <- sim_assets$asset_id[sim_assets$asset_class == "commodity"]
claim("7b", "rank of the commodity covariance", 8, qr(cov(Ra[, cmd]))$rank, 0)
ev16 <- eigen(cov(R), symmetric = TRUE, only.values = TRUE)$values
claim("7c", "log10 condition number, sixteen classes", 4.1, log10(max(ev16) / min(ev16)), 1.0)

# --- 8. the equity benchmark ---------------------------------------------------

cat("\n=== 8. equal versus capitalisation weighting (ch. 21, 24) ===\n")
klag <- sim_marketcap_weekly[order(sim_marketcap_weekly$asset, sim_marketcap_weekly$date), ]
klag$cap_lag <- ave(klag$market_cap, klag$asset, FUN = function(z) c(NA, head(z, -1)))
for (rg in c("US", "UK", "EU", "CH", "JP")) {
  ids <- sim_assets$asset_id[sim_assets$region == rg & sim_assets$asset_class == "equity"]
  r <- sim_asset_returns_weekly[sim_asset_returns_weekly$asset %in% ids, ]
  d <- merge(r, klag[, c("date", "asset", "cap_lag")], by = c("date", "asset"))
  d <- d[!is.na(d$cap_lag), ]
  ew <- tapply(d$return, d$date, mean)
  vw <- tapply(seq_len(nrow(d)), d$date, function(i)
    sum(d$return[i] * d$cap_lag[i]) / sum(d$cap_lag[i]))
  cat(sprintf("     %s equity: equal weighted %.2f%%  cap weighted %.2f%%  gap %+.2f pp\n",
              rg, 100 * ann(ew, 52), 100 * ann(vw, 52),
              100 * (ann(vw, 52) - ann(ew, 52))))
}

# --- 9. the class moments, for the record --------------------------------------

cat("\n=== 9. class moments, annualised from monthly (ch. 4) ===\n")
mom <- data.frame(
  ret    = sapply(colnames(R), function(s) ann(as.numeric(R[, s]))),
  vol    = sapply(colnames(R), function(s) sd(R[, s]) * sqrt(12)),
  skew   = sapply(colnames(R), function(s) skewness(as.numeric(R[, s]))),
  mdd    = sapply(colnames(R), function(s) mdd(as.numeric(R[, s])))
)
mom$sharpe <- (mom$ret - rfa) / mom$vol
print(round(mom[order(-mom$sharpe), ], 3))

# --- summary -------------------------------------------------------------------

res <- do.call(rbind, results)
moved <- res[!is.na(res$moved) & res$moved, ]
unpinned <- res[is.na(res$moved), ]
cat("\n", strrep("-", 78), "\n", sep = "")
if (nrow(moved) == 0) {
  cat("All", sum(!is.na(res$moved)), "pinned claims still hold within tolerance.\n")
} else {
  cat(nrow(moved), "of", sum(!is.na(res$moved)), "pinned claims have moved:\n\n")
  print(moved[, c("id", "claim", "was", "now")], row.names = FALSE)
  cat("\nEvery sentence in the book resting on these needs rewriting.\n")
}
if (nrow(unpinned) > 0) {
  cat("\n", nrow(unpinned), "claims are measured but not yet pinned -- pin them once the chapter prints them:\n\n")
  print(unpinned[, c("id", "claim", "now")], row.names = FALSE)
}
