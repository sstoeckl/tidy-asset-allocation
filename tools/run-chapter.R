# Execute one chapter's R code without rendering the book.
#
# `quarto render chapters/NN.qmd` in this project renders all 39 files, so it
# is no way to check a single chapter. This script reads the R chunks of one
# chapter straight from the fences, runs them in order from the project root in
# a fresh environment, and reports the first error with the chunk label it came
# from. Inline `r ...` expressions are not evaluated; a render still has to
# confirm those.
#
#   Set-Location "...\Tidy_Asset_Allocation"
#   & "C:\R\R-4.6.1\bin\Rscript.exe" tools/run-chapter.R chapters/03-return-risk-and-the-investor.qmd
#
# Exit status 0 when every chunk ran, 1 otherwise. Figures go to a null device,
# so nothing is written into the project. Chunks with `eval: false` are
# skipped, as they are in a render.

stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1L) stop("usage: Rscript tools/run-chapter.R chapters/<file>.qmd")
qmd <- args[[1]]
stopifnot(file.exists(qmd))

lines  <- readLines(qmd, warn = FALSE, encoding = "UTF-8")
open   <- grep("^```\\{r[^}]*\\}\\s*$", lines)
close  <- grep("^```\\s*$", lines)
chunks <- list()
for (o in open) {
  c_ <- close[close > o][1]
  if (is.na(c_)) stop("unclosed chunk at line ", o)
  body <- lines[(o + 1):(c_ - 1)]
  opts <- sub("^#\\|\\s*", "", grep("^#\\|", body, value = TRUE))
  body <- body[!grepl("^#\\|", body)]
  lab  <- sub("^label:\\s*", "", grep("^label:", opts, value = TRUE))
  ev   <- sub("^eval:\\s*", "", grep("^eval:", opts, value = TRUE))
  # header-style label, e.g. ```{r label, eval=FALSE}
  hdr <- sub("^```\\{r,?\\s*([^,}]*).*$", "\\1", lines[o])
  if (!length(lab) && nzchar(hdr) && !grepl("=", hdr)) lab <- hdr
  if (!length(ev) && grepl("eval\\s*=\\s*F", lines[o])) ev <- "false"
  chunks[[length(chunks) + 1L]] <- list(
    label = if (length(lab)) lab[1] else sprintf("(line %d)", o),
    eval  = !length(ev) || !tolower(ev[1]) %in% c("false", "f"),
    code  = body)
}

cat(sprintf("%s: %d chunks\n", qmd, length(chunks)))
grDevices::pdf(NULL)
env <- new.env(parent = globalenv())
t_all <- Sys.time()
ok <- TRUE
for (ch in chunks) {
  if (!ch$eval) { cat(sprintf("  skip  %-36s (eval: false)\n", ch$label)); next }
  t0 <- Sys.time()
  res <- tryCatch({
    withCallingHandlers(
      eval(parse(text = ch$code, keep.source = FALSE), envir = env),
      warning = function(w) invokeRestart("muffleWarning"))
    NULL
  }, error = function(e) e)
  el <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  if (is.null(res)) {
    cat(sprintf("  ok    %-36s %6.1fs\n", ch$label, el))
  } else {
    cat(sprintf("  ERROR %-36s %6.1fs\n        %s\n", ch$label, el,
                sub("\n.*", "", conditionMessage(res))))
    ok <- FALSE
    break
  }
}
invisible(grDevices::dev.off())
cat(sprintf("%s in %.1f min\n", if (ok) "all chunks ran" else "STOPPED at first error",
            as.numeric(difftime(Sys.time(), t_all, units = "mins"))))
quit(status = if (ok) 0L else 1L)
