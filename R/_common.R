# Sourced at the top of every chapter. Keep it small: anything that belongs to
# one chapter belongs in that chapter.

suppressPackageStartupMessages({
  library(tidyverse)
  library(xts)
  library(PortfolioAnalytics)
  library(PerformanceAnalytics)
})

# --- deterministic output -----------------------------------------------------
# Every chapter starts from the same seed so that figures and numbers are stable
# across renders. Chapters that need a different seed set it explicitly and say
# so in the text.
set.seed(1602)

# Month names in prose come from format(date, "%B"), which follows the machine
# locale: on a German Windows a chapter printed "Oktober" for October. The book is in
# English, so the time locale is fixed here, once.
invisible(Sys.setlocale("LC_TIME", "C"))

options(
  digits = 4,
  scipen = 999,
  dplyr.summarise.inform = FALSE,
  pillar.min_title_chars = Inf,
  readr.show_col_types = FALSE
)

# --- plotting -----------------------------------------------------------------
# One theme for the whole book, matched to _brand.yml.

tidyaa_colors <- c(
  ink      = "#212529",
  ink_soft = "#6C757D",
  rule     = "#DEE2E6",
  blue     = "#2E77A6",
  blue_lit = "#5FA8D3",
  good     = "#2C6A4C",
  caution  = "#D6A419",
  broken   = "#C0392B"
)

# _brand.yml pulls Source Sans 3 from Google for the page text, but a graphics
# device can only use a font that is installed locally. If it is not, ggplot
# falls back silently and emits one warning per text element -- hundreds per
# render. Resolve the family once, here, and let the figures use the device
# default when the real face is missing.
tidyaa_family <- function(preferred) {
  ok <- tryCatch(
    requireNamespace("systemfonts", quietly = TRUE) &&
      preferred %in% systemfonts::system_fonts()$family,
    error = function(e) FALSE
  )
  if (ok) preferred else ""
}

tidyaa_sans <- tidyaa_family("Source Sans 3")

if (!nzchar(tidyaa_sans) && interactive()) {
  message("Source Sans 3 is not installed; figures use the device default. ",
          "Install it to match the body text.")
}

theme_tidyaa <- function(base_size = 11) {
  ggplot2::theme_minimal(base_size = base_size, base_family = tidyaa_sans) +
    ggplot2::theme(
      plot.title       = ggplot2::element_text(face = "bold", size = base_size * 1.2,
                                               margin = ggplot2::margin(b = 6)),
      plot.subtitle    = ggplot2::element_text(colour = tidyaa_colors[["ink_soft"]],
                                               margin = ggplot2::margin(b = 12)),
      plot.caption     = ggplot2::element_text(colour = tidyaa_colors[["ink_soft"]],
                                               size = base_size * 0.8, hjust = 0),
      panel.grid.minor = ggplot2::element_blank(),
      panel.grid.major = ggplot2::element_line(colour = tidyaa_colors[["rule"]],
                                               linewidth = 0.3),
      axis.title       = ggplot2::element_text(colour = tidyaa_colors[["ink_soft"]],
                                               size = base_size * 0.9),
      legend.position  = "bottom",
      legend.title     = ggplot2::element_blank(),
      strip.text       = ggplot2::element_text(face = "bold", hjust = 0)
    )
}

ggplot2::theme_set(theme_tidyaa())

# Discrete scale for up to eight series, built around the accent rather than
# around a rainbow.
scale_colour_tidyaa <- function(...) {
  ggplot2::scale_colour_manual(
    values = unname(c(tidyaa_colors[c("blue", "broken", "caution", "good",
                                      "ink", "blue_lit", "ink_soft")])),
    ...
  )
}
scale_color_tidyaa <- scale_colour_tidyaa

scale_fill_tidyaa <- function(...) {
  ggplot2::scale_fill_manual(
    values = unname(c(tidyaa_colors[c("blue", "broken", "caution", "good",
                                      "ink", "blue_lit", "ink_soft")])),
    ...
  )
}

# CRAN 2.1.2 and the patched build both call themselves 2.1.2, and that
# collision has already cost this project a day. Tell them apart by a formal
# that only the patch adds, and say so once rather than letting the chapters
# quietly produce different numbers.
tidyaa_pa_patched <- function() {
  tryCatch(
    "target_mean" %in% names(formals(
      utils::getFromNamespace("gmv_opt", "PortfolioAnalytics"))),
    error = function(e) NA
  )
}

if (isFALSE(tidyaa_pa_patched())) {
  warning(
    "PortfolioAnalytics is the unpatched build. Chapters 9, 13 and 25 will ",
    "differ: maxSR ignores a supplied mean, and full_investment fails ",
    "silently in some rolling windows. See appendix D (93-package-notes).",
    call. = FALSE
  )
}

# --- the model calendar -------------------------------------------------------
# The modelled market runs on model years 1 to 31 (tidypm::model_year()), so a
# date axis labels model years and the prose names a month as "March of model
# year 17". No chapter prints a calendar year for the simulated market.
scale_x_model <- function(by = 5, name = "model year", ...) {
  ggplot2::scale_x_date(
    name   = name,
    breaks = function(lim) {
      b <- as.Date(sprintf("%d-01-01", 2100L + seq(by, 35L, by = by)))
      b[b >= lim[1] & b <= lim[2]]
    },
    labels = function(d) tidypm::model_year(d),
    ...
  )
}

fmt_model <- function(d, month = TRUE) {
  d <- as.Date(d)
  if (month) paste(format(d, "%B"), "of model year", tidypm::model_year(d))
  else paste("model year", tidypm::model_year(d))
}
