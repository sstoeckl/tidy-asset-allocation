# Knit one chapter to plain markdown, with every inline `r ...` evaluated.
#
# `tools/run-chapter.R` runs the chunks and stops at the first error, which is
# what tells you a chapter executes. It does not evaluate inline expressions,
# and the prose of this book is made of them. This script knits the chapter
# with knitr alone -- no Quarto, no book, about as long as the chapter takes to
# run -- and writes the result outside the project, so that the sentences can
# be read with their numbers in them and checked against what they claim.
#
#   Set-Location "...\Tidy_Asset_Allocation"
#   & "C:\R\R-4.6.1\bin\Rscript.exe" tools/knit-chapter.R chapters/09-mean-variance.qmd
#
# The path of the markdown file is printed at the end. Cross-references
# (`@sec-`, `@fig-`, `@eq-`) and citations stay as written: this is a check of
# the numbers, not a preview of the page. A chunk that errors does not stop the
# knit; its error is printed into the output and counted in the summary, so one
# pass shows every problem. Exit status 0 when nothing errored, 1 otherwise.

stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1L) stop("usage: Rscript tools/knit-chapter.R chapters/<file>.qmd")
qmd <- args[[1]]
stopifnot(file.exists(qmd))

out_dir <- file.path(dirname(tempdir()), "tidyaa-knit")
slug    <- sub("[.]qmd$", "", gsub("[/\\\\]", "_", sub("^chapters[/\\\\]", "", qmd)))
fig_dir <- file.path(out_dir, paste0(slug, "_figs"))
dir.create(fig_dir, recursive = TRUE, showWarnings = FALSE)
out <- file.path(out_dir, paste0(slug, ".md"))

n_err <- 0L
knitr::opts_knit$set(root.dir = getwd())
knitr::opts_chunk$set(
  fig.path = paste0(normalizePath(fig_dir, winslash = "/"), "/"),
  dev = "png", dpi = 72, comment = "#>", collapse = TRUE,
  warning = FALSE, message = FALSE, error = TRUE, cache = FALSE
)
# An inline expression that fails must not stop the knit either: show it.
knitr::knit_hooks$set(
  error = function(x, options) {
    n_err <<- n_err + 1L
    paste0("\n\n**!!! CHUNK ERROR in `", options$label, "`:** ", x, "\n\n")
  },
  inline = function(x) {
    if (is.numeric(x)) x <- format(x, digits = 4)
    paste(as.character(x), collapse = ", ")
  }
)
knitr::opts_knit$set(progress = FALSE, verbose = FALSE)
# A chunk may ask for a cache; never write one into the project from here.
knitr::opts_hooks$set(cache = function(options) { options$cache <- FALSE; options })

t0  <- Sys.time()
res <- tryCatch(
  knitr::knit(qmd, output = out, quiet = TRUE, envir = new.env(parent = globalenv())),
  error = function(e) {
    # knitr stops on a failing inline expression; report where.
    cat("\nKNIT STOPPED:", conditionMessage(e), "\n")
    NULL
  }
)
el <- round(as.numeric(difftime(Sys.time(), t0, units = "mins")), 1)

if (is.null(res)) {
  cat(sprintf("\nno output: an inline expression failed after %.1f min (see the message above)\n", el))
  quit(status = 1L)
}
txt <- readLines(out, warn = FALSE, encoding = "UTF-8")
cat(sprintf("\nknitted %s in %.1f min: %d lines, %d chunk error%s\n%s\n",
            qmd, el, length(txt), n_err, if (n_err == 1L) "" else "s",
            normalizePath(out, winslash = "/")))
quit(status = if (n_err > 0L) 1L else 0L)
