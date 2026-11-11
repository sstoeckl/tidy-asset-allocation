# Chapter 5: does shrinkage pay, measured out of sample rather than argued?
#
# Minimum variance on the 123 equities, long only and fully invested, with the
# covariance estimated four ways on a rolling window and the portfolio held for
# one month. Scored on what was actually realised, not on the in-sample number
# each estimator reports about itself.
setwd("D:/University of Liechtenstein/DTM Sebastian - Dokumente/80_Tidy_Portfoliomanagement_Book/Tidy_Asset_Allocation")
stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
suppressPackageStartupMessages({
  library(tidypm); library(PortfolioAnalytics); library(xts); library(quadprog)
})

ins <- as_xts_pm(sim_asset_returns_monthly, date, asset, return)
eq  <- ins[, colnames(ins) %in% sim_assets$asset_id[sim_assets$asset_class == "equity"]]
N   <- ncol(eq)
rf  <- sim_riskfree_monthly$return

# Minimum variance, long only, fully invested, solved directly so that a
# singular Sigma fails loudly here rather than somewhere downstream.
min_var_w <- function(S) {
  n <- ncol(S)
  Dmat <- 2 * S
  # quadprog needs positive definiteness; a singular sample matrix is exactly
  # what this chapter is about, so do not patch it. Let it refuse.
  sol <- try(solve.QP(Dmat = Dmat, dvec = rep(0, n),
                      Amat = cbind(rep(1, n), diag(n)),
                      bvec = c(1, rep(0, n)), meq = 1), silent = TRUE)
  if (inherits(sol, "try-error")) return(NULL)
  w <- sol$solution; w[w < 0] <- 0; w / sum(w)
}

estimators <- list(
  sample   = function(X) stats::cov(X),
  shrunk   = function(X) { S <- corpcor::cov.shrink(X, verbose = FALSE)
                           attributes(S)[setdiff(names(attributes(S)), c("dim","dimnames"))] <- NULL
                           as.matrix(S) },
  diagonal = function(X) diag(apply(X, 2, stats::var)),
  factor3  = function(X) {
    m <- try(statistical.factor.model(xts::xts(X, order.by = Sys.Date() - rev(seq_len(nrow(X)))), k = 3),
             silent = TRUE)
    if (inherits(m, "try-error")) return(NULL)
    as.matrix(extractCovariance(m))
  }
)

# Every window must be scored on the same months, or a longer window is being
# credited for starting later. FIRST_OOS is fixed by the longest window.
FIRST_OOS <- 181L

run <- function(W) {
  idx <- seq.int(FIRST_OOS, nrow(eq))
  out <- list()
  for (nm in names(estimators)) {
    rets <- rep(NA_real_, length(idx)); fails <- 0L; lam <- c()
    nbets <- rep(NA_real_, length(idx))
    for (j in seq_along(idx)) {
      i <- idx[j]
      X <- zoo::coredata(eq[(i - W):(i - 1L), ])
      S <- tryCatch(estimators[[nm]](X), error = function(e) NULL)
      if (is.null(S)) { fails <- fails + 1L; next }
      if (nm == "shrunk") lam <- c(lam, attr(corpcor::cov.shrink(X, verbose = FALSE), "lambda"))
      w <- min_var_w(S)
      if (is.null(w)) { fails <- fails + 1L; next }
      rets[j] <- sum(w * zoo::coredata(eq[i, ]))
      nbets[j] <- 1 / sum(w^2)
    }
    ok <- !is.na(rets)
    ex <- rets[ok] - rf[idx][ok]
    out[[nm]] <- data.frame(
      window = W, estimator = nm,
      periods = length(idx), failed = fails,
      ann_vol = if (any(ok)) stats::sd(rets[ok]) * sqrt(12) else NA_real_,
      ann_ret = if (any(ok)) mean(rets[ok]) * 12 else NA_real_,
      sharpe  = if (any(ok)) mean(ex) / stats::sd(ex) * sqrt(12) else NA_real_,
      eff_bets = if (any(ok)) mean(nbets, na.rm = TRUE) else NA_real_,
      lambda  = if (length(lam)) mean(lam) else NA_real_)
  }
  do.call(rbind, out)
}

cat("### minimum variance on", N, "equities, rolling window, monthly rebalance\n\n")
res <- do.call(rbind, lapply(c(60L, 120L, 180L), run))
res$failed_pct <- round(100 * res$failed / res$periods, 1)
print(res[, c("window","estimator","periods","failed","failed_pct",
              "ann_vol","sharpe","eff_bets","lambda")], row.names = FALSE, digits = 4)

# The control: equal weight estimates nothing.
for (W in c(60L, 120L, 180L)) {
  idx <- seq.int(FIRST_OOS, nrow(eq))
  r <- rowMeans(zoo::coredata(eq[idx, ]))
  ex <- r - rf[idx]
  cat(sprintf("\n  equal weight, window %3d: vol %.4f  sharpe %.3f  (estimates nothing)\n",
              W, stats::sd(r) * sqrt(12), mean(ex)/stats::sd(ex)*sqrt(12)))
}
saveRDS(res, "output/tables/ch05-estimator-race.rds")
cat("\nsaved output/tables/ch05-estimator-race.rds\n")
