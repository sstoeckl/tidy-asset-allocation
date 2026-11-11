# The cover of "Tidy Asset Allocation in R", drawn from the book's own data.
#
# Three variants, each written at 1600 x 2400 px (the portrait proportion that
# Quarto's `cover-image` and the sidebar thumbnail use) and as a 600 px preview:
#
#   A  the textbook picture: the sixteen classes in the volatility-return plane,
#      the long-only frontier and the capital allocation line
#   B  typographic: the accent bar, the title at display size, one small
#      frontier glyph
#   C  data as texture: the frontier's weight transition map, full bleed
#
# and, on B, which Sebastian chose, three layouts (B-highlow, B-oneline,
# B-column), three palettes (B-navy, B-amber, B-wash), and two reflows of B for
# the social preview and a slide title card (B-square 1:1, B-wide 16:9).
#
# Chosen 2026-11-11: the book cover is B-wash (B-wash-gold beside it for
# comparison), the amber palette keeps the light-blue bar (B-amber2), and the
# title card and social preview are built in navy and in amber2
# (card-<palette>-wide, card-<palette>-square). The finals are also written
# under stable names: cover.png, cover-social.png, cover-wide.png.
#
# Run from the project root, once (about a minute, most of it the frontier):
#
#     & "C:\R\R-4.6.1\bin\Rscript.exe" assets/cover/make-cover.R
#
# Nothing here is wired into _quarto.yml. Once a variant is chosen, its PNG is
# referenced as `cover-image` there.

stopifnot(grepl("Tidy_Asset_Allocation", .libPaths()[1], fixed = TRUE))
source("R/_common.R")
suppressPackageStartupMessages({
  library(tidypm)
  library(grid)
})

# --- typeface -----------------------------------------------------------------
# The site sets Source Sans 3 from Google; a graphics device needs the file. The
# OFL-licensed faces sit beside this script (assets/cover/fonts, licence
# included) and are registered under their own family names, so that a thin
# system copy of the font cannot shadow them. "bold" maps to Semibold (600),
# the heading weight of _brand.yml; the display family carries the true Bold
# (700), which custom.scss uses for the title block.
font_dir <- "assets/cover/fonts"
ttf <- function(face) file.path(font_dir, sprintf("SourceSans3-%s.ttf", face))
if (all(file.exists(ttf(c("Regular", "It", "Semibold", "Bold", "BoldIt"))))) {
  systemfonts::register_font("Cover Sans", plain = ttf("Regular"), italic = ttf("It"),
                             bold = ttf("Semibold"), bolditalic = ttf("BoldIt"))
  systemfonts::register_font("Cover Display", plain = ttf("Bold"), bold = ttf("Bold"),
                             italic = ttf("BoldIt"), bolditalic = ttf("BoldIt"))
  sans <- "Cover Sans"; display <- "Cover Display"
  font_used <- "Source Sans 3 (bundled TTF, OFL)"
} else {
  sans <- display <- "Segoe UI"
  font_used <- "Segoe UI: the Source Sans 3 TTFs are missing from assets/cover/fonts"
}
message("typeface: ", font_used)

# --- palette, from _brand.yml -------------------------------------------------
ink       <- tidyaa_colors[["ink"]]
ink_soft  <- tidyaa_colors[["ink_soft"]]
rule      <- tidyaa_colors[["rule"]]
blue      <- tidyaa_colors[["blue"]]
blue_lit  <- tidyaa_colors[["blue_lit"]]
blue_deep <- "#1B4F6F"
blue_pale <- "#EAF2F8"

title_1  <- "Tidy Asset Allocation"
title_2  <- "in R"
subtitle <- "A course text on building, constraining\nand testing multi-asset portfolios"
author   <- "Sebastian St\u00f6ckl"

# --- data: the sixteen risky classes, as chapter 9 loads them -----------------
R  <- as_xts_pm(sim_class_returns_monthly, date, class, return)
rf <- sim_riskfree_monthly$return
Re <- R - rf
stopifnot(ncol(Re) == 16L, !anyNA(Re))

# one row per asset, built by name: a volatility can never meet another
# asset's return
pretty_name <- function(x) sub("^GLOBAL", "Global", gsub("_", " ", x))
assets <- tibble::tibble(
  asset = colnames(Re),
  label = pretty_name(colnames(Re)),
  vol   = apply(Re, 2, stats::sd) * sqrt(12),
  ret   = colMeans(Re) * 12,
  group = dplyr::case_when(
    grepl("_government$", colnames(Re)) ~ "government",
    grepl("_credit$",     colnames(Re)) ~ "credit",
    grepl("_equity$",     colnames(Re)) ~ "equity",
    TRUE                                ~ "commodity"
  )
)

# the long-only frontier, exactly as chapter 9 builds it
ef_spec <- portfolio.spec(assets = colnames(Re)) |>
  add.constraint(type = "full_investment") |>
  add.constraint(type = "long_only") |>
  add.objective(type = "return", name = "mean") |>
  add.objective(type = "risk",   name = "StdDev")

ef <- suppressWarnings(
  create.EfficientFrontier(Re, ef_spec, type = "mean-StdDev", n.portfolios = 120)
)
fr <- as.data.frame(unclass(ef$frontier))
stopifnot(ncol(fr) == ncol(Re) + 3L, !is.unsorted(fr$mean), !is.unsorted(fr$StdDev))

frontier <- tibble::tibble(
  i      = seq_len(nrow(fr)),
  vol    = fr$StdDev * sqrt(12),
  ret    = fr$mean * 12,
  sharpe = ret / vol                      # excess returns: no rate to subtract
)
i_tan <- which.max(frontier$sharpe)
anchors <- tibble::tibble(
  label = c("minimum variance", "tangency"),
  vol   = c(frontier$vol[1], frontier$vol[i_tan]),
  ret   = c(frontier$ret[1], frontier$ret[i_tan])
)
ret_end <- 1.08 * max(assets$ret)
cal <- tibble::tibble(ret = c(0, ret_end), vol = c(0, ret_end / frontier$sharpe[i_tan]))

# the weight transition map: one row per frontier portfolio and asset
wcols <- grep("^w[.]", colnames(fr))
weights <- fr[, wcols]
colnames(weights) <- sub("^w[.]", "", colnames(weights))
stopifnot(setequal(colnames(weights), colnames(Re)),
          all(abs(rowSums(weights) - 1) < 1e-6))
wmap <- tibble::as_tibble(weights) |>
  dplyr::mutate(i = frontier$i, ret = frontier$ret) |>
  tidyr::pivot_longer(-c(i, ret), names_to = "asset", values_to = "w") |>
  dplyr::left_join(assets[, c("asset", "group")], by = "asset")

# --- labels that do not collide ----------------------------------------------
# Labels sit to the right of their point. Two points close in volatility and
# closer in return than a line of text would print on top of each other, so
# the later label (in return order) is lifted until it clears, and a thin
# leader joins it to its point when it had to move.
lift_labels <- function(df, x_tol, y_min) {
  df <- df[order(df$ret), ]
  df$ly <- df$ret
  for (k in seq_len(nrow(df))[-1]) {
    near <- which(abs(df$vol[seq_len(k - 1)] - df$vol[k]) < x_tol)
    if (length(near)) {
      top <- max(df$ly[near])
      if (df$ly[k] - top < y_min) df$ly[k] <- top + y_min
    }
  }
  df
}
# Three points in the crowded middle take their label on the left, by name;
# everything else labels to the right. Then each side is lifted on its own.
left_side <- c("UK_government", "CH_government", "CH_credit")
stopifnot(all(left_side %in% assets$asset))
spread_labels <- function(df, x_tol, y_min) {
  df$side <- ifelse(df$asset %in% left_side, "left", "right")
  df <- dplyr::bind_rows(lapply(split(df, df$side), lift_labels, x_tol = x_tol, y_min = y_min))
  df$dx    <- ifelse(df$side == "left", -0.0035, 0.0035)
  df$hjust <- ifelse(df$side == "left", 1, 0)
  df$moved <- abs(df$ly - df$ret) > 1e-9
  df
}

# --- the three figures --------------------------------------------------------
theme_cover <- function(base_size) {
  theme_tidyaa(base_size = base_size) +
    ggplot2::theme(
      text             = ggplot2::element_text(family = sans),
      panel.grid.major = ggplot2::element_line(colour = rule, linewidth = 0.35),
      axis.title       = ggplot2::element_text(colour = ink_soft, family = sans),
      axis.text        = ggplot2::element_text(colour = ink_soft, family = sans),
      legend.position  = "none",
      plot.margin      = ggplot2::margin(4, 4, 4, 4)
    )
}

# A: the textbook picture
lab_a <- spread_labels(assets, x_tol = 0.03, y_min = 0.0054)
fig_picture <- ggplot2::ggplot() +
  ggplot2::geom_line(data = cal, ggplot2::aes(vol, ret), linetype = "22",
                     colour = ink_soft, linewidth = 0.55) +
  ggplot2::geom_line(data = frontier, ggplot2::aes(vol, ret),
                     colour = blue, linewidth = 1.4) +
  ggplot2::geom_segment(data = dplyr::filter(lab_a, moved),
                        ggplot2::aes(x = vol, y = ret, xend = vol + dx, yend = ly),
                        colour = rule, linewidth = 0.4) +
  ggplot2::geom_point(data = lab_a, ggplot2::aes(vol, ret),
                      size = 3.2, colour = blue_lit) +
  ggplot2::geom_text(data = lab_a, ggplot2::aes(vol + dx, ly, label = label, hjust = hjust),
                     size = 3.6, vjust = 0.5, colour = ink_soft, family = sans) +
  ggplot2::geom_point(data = anchors, ggplot2::aes(vol, ret), shape = 21,
                      size = 5.2, fill = "white", colour = blue, stroke = 1.5) +
  ggplot2::geom_text(data = anchors,
                     ggplot2::aes(vol, ret, label = label,
                                  hjust = c(1, 0), vjust = c(0.5, -1.1)),
                     nudge_x = c(-0.009, -0.004),
                     size = 3.9, colour = ink, family = sans, fontface = "bold") +
  ggplot2::scale_x_continuous(labels = scales::label_percent(accuracy = 1),
                              expand = ggplot2::expansion(mult = c(0.11, 0.30))) +
  ggplot2::scale_y_continuous(labels = scales::label_percent(accuracy = 1),
                              expand = ggplot2::expansion(mult = c(0.06, 0.10))) +
  ggplot2::labs(x = "annualized volatility", y = "annualized excess return") +
  theme_cover(13)

# B: the glyph, the same picture with nothing on it
fig_glyph <- ggplot2::ggplot() +
  ggplot2::geom_line(data = cal, ggplot2::aes(vol, ret), linetype = "22",
                     colour = ink_soft, linewidth = 0.5) +
  ggplot2::geom_line(data = frontier, ggplot2::aes(vol, ret),
                     colour = blue, linewidth = 1.6) +
  ggplot2::geom_point(data = assets, ggplot2::aes(vol, ret),
                      size = 2.8, colour = blue_lit) +
  ggplot2::geom_point(data = anchors[anchors$label == "tangency", ],
                      ggplot2::aes(vol, ret), shape = 21, size = 5,
                      fill = "white", colour = blue, stroke = 1.5) +
  ggplot2::scale_x_continuous(expand = ggplot2::expansion(mult = c(0.02, 0.06))) +
  ggplot2::scale_y_continuous(expand = ggplot2::expansion(mult = c(0.06, 0.08))) +
  ggplot2::theme_void() +
  ggplot2::theme(legend.position = "none", plot.margin = ggplot2::margin(0, 0, 0, 0))

# C: the weight transition map as texture. Government bands in the pale blues,
# credit in the mid blues, equity in the deep ones, the commodity in grey, so
# the map runs from light at the minimum-variance end to dark at the
# maximum-return end. The first level stacks on top.
ramp <- function(from, to, n) grDevices::colorRampPalette(c(from, to))(n)
region_order <- c("US", "EU", "UK", "CH", "JP")
by_group <- function(g, cols) {
  a <- assets$asset[assets$group == g]
  a <- a[order(match(sub("_.*$", "", a), region_order))]
  stats::setNames(cols, a)
}
pal <- c(
  by_group("commodity",  "#8A949C"),
  by_group("equity",     ramp(blue, "#143A52", 5)),
  by_group("credit",     ramp("#8FC3E0", "#4A90BE", 5)),
  by_group("government", ramp("#DCE9F3", "#A9C7DE", 5))
)
stopifnot(setequal(names(pal), colnames(Re)))
wmap$asset <- factor(wmap$asset, levels = names(pal))

fig_map <- ggplot2::ggplot(wmap, ggplot2::aes(ret, w, fill = asset)) +
  ggplot2::geom_area(position = "stack", colour = "white", linewidth = 0.3) +
  ggplot2::scale_fill_manual(values = pal) +
  ggplot2::scale_x_continuous(expand = c(0, 0)) +
  ggplot2::scale_y_continuous(expand = c(0, 0)) +
  ggplot2::theme_void() +
  ggplot2::theme(legend.position = "none", plot.margin = ggplot2::margin(0, 0, 0, 0))

# --- page composition in grid, on an 8 x 12 inch canvas -----------------------
txt <- function(label, x, y, size, family = sans, face = "plain", col = ink,
                just = c("left", "top"), lineheight = 1.12) {
  grid.text(label, x = unit(x, "in"), y = unit(y, "in"), just = just,
            gp = gpar(fontfamily = family, fontface = face, fontsize = size,
                      col = col, lineheight = lineheight))
}
bar <- function(x, y, w = 0.9, h = 0.075, col = blue_lit) {
  grid.rect(x = unit(x, "in"), y = unit(y, "in"), width = unit(w, "in"),
            height = unit(h, "in"), just = c("left", "bottom"),
            gp = gpar(fill = col, col = NA))
}
# the largest point size at which a line fits a width
fit <- function(label, width_in, family, face, max_pt) {
  s <- max_pt
  while (s > 8) {
    w <- convertWidth(grobWidth(textGrob(label, gp = gpar(fontfamily = family,
                                                            fontface = face,
                                                            fontsize = s))),
                      "in", valueOnly = TRUE)
    if (w <= width_in) break
    s <- s - 0.5
  }
  s
}
place <- function(p, x, y, w, h, just = c("left", "bottom")) {
  print(p, vp = viewport(x = unit(x, "in"), y = unit(y, "in"),
                         width = unit(w, "in"), height = unit(h, "in"), just = just))
}

draw_A <- function() {
  m <- 0.8
  s <- fit(title_1, 8 - 2 * m, display, "bold", 60)
  lh <- s / 72 * 1.12
  bar(m, 11.0)
  txt(title_1, m, 10.85, s, display, "bold")
  txt(title_2, m, 10.85 - lh, s, display, "bold")
  txt(subtitle, m, 10.85 - 2 * lh - 0.22, 18, sans, "plain", ink_soft, lineheight = 1.3)
  place(fig_picture, 0.42, 1.45, 7.2, 6.75)
  txt(author, m, 0.9, 22, sans, "bold", ink, just = c("left", "bottom"))
}

draw_B <- function() {
  m <- 0.9
  s <- fit("Allocation", 8 - 2 * m, display, "bold", 104)
  lh <- s / 72 * 1.04
  bar(m, 9.55, w = 1.15, h = 0.09)
  txt("Tidy Asset", m, 9.35, s, display, "bold")
  txt("Allocation", m, 9.35 - lh, s, display, "bold")
  txt("in R",       m, 9.35 - 2 * lh, s, display, "bold")
  txt(subtitle, m, 9.35 - 3 * lh - 0.3, 19, sans, "plain", ink_soft, lineheight = 1.3)
  place(fig_glyph, 8 - m, 1.15, 3.3, 2.5, just = c("right", "bottom"))
  txt(author, m, 1.15, 22, sans, "bold", ink, just = c("left", "bottom"))
}

draw_C <- function() {
  m <- 0.8
  place(fig_map, 0, 0, 8, 6.6)
  s <- fit(title_1, 8 - 2 * m, display, "bold", 60)
  lh <- s / 72 * 1.12
  bar(m, 11.0)
  txt(title_1, m, 10.85, s, display, "bold")
  txt(title_2, m, 10.85 - lh, s, display, "bold")
  txt(subtitle, m, 10.85 - 2 * lh - 0.22, 18, sans, "plain", ink_soft, lineheight = 1.3)
  txt(author, 8 - m, 0.75, 22, sans, "bold", "white", just = c("right", "bottom"))
}

render <- function(draw, file, px_w, px_h = px_w * 1.5, res = 200) {
  ragg::agg_png(file, width = px_w, height = px_h, units = "px", res = res,
                background = "white")
  on.exit(grDevices::dev.off())
  grid.newpage()
  draw()
  invisible(file)
}

# --- variations on B ----------------------------------------------------------
# The same idea every time: white space, the bar as the mark, the title large,
# the author small, one axis-free frontier glyph. The layouts move the pieces;
# the palettes recolor them; the two reflows fit them to a square and to 16:9.

# which assets nothing dominates (weakly higher return at weakly lower
# volatility), for the palette that accents a few points
assets$efficient <- !vapply(seq_len(nrow(assets)), function(i) {
  any(assets$ret >= assets$ret[i] & assets$vol <= assets$vol[i] &
      seq_len(nrow(assets)) != i)
}, logical(1))

palettes <- list(
  brand = list(bg = "white", title = ink, sub = ink_soft, author = ink, bar = blue_lit,
               line = blue, pts = blue_lit, ring = blue, ring_fill = "white",
               cal = ink_soft, accent_pts = NULL),
  navy  = list(bg = "#143A52", title = "white", sub = "#BFD7E8", author = "white",
               bar = blue_lit, line = blue_lit, pts = "#EAF2F8", ring = "white",
               ring_fill = "#143A52", cal = "#7FAECB", accent_pts = NULL),
  # amber on the bar, the tangency ring and the efficient assets only; swap
  # "#D6A419" for "#C0392B" here to see the brick version
  amber = list(bg = "white", title = ink, sub = ink_soft, author = ink, bar = "#D6A419",
               line = blue, pts = blue_lit, ring = "#D6A419", ring_fill = "white",
               cal = ink_soft, accent_pts = "#D6A419"),
  wash  = list(bg = c("#143A52", "#1B4F6F", "#2E77A6", "#9CC6E0", "#EAF2F8"),
               title = "white", sub = "#DCE9F3", author = ink, bar = blue_lit,
               line = "white", pts = "#EAF2F8", ring = "white", ring_fill = "#2E77A6",
               cal = "#BFD7E8", accent_pts = NULL)
)
# the corrected amber: the bar back to the light blue of B, amber only on the
# tangency ring and the efficient classes
palettes$amber2 <- modifyList(palettes$amber, list(bar = blue_lit))
# the wash with the same two amber touches, for comparison with the plain wash
palettes$wash_gold <- modifyList(palettes$wash, list(ring = "#D6A419", accent_pts = "#D6A419"))

make_glyph <- function(p) {
  pts <- assets
  pts$col <- if (is.null(p$accent_pts)) p$pts else ifelse(pts$efficient, p$accent_pts, p$pts)
  ggplot2::ggplot() +
    ggplot2::geom_line(data = cal, ggplot2::aes(vol, ret), linetype = "22",
                       colour = p$cal, linewidth = 0.5) +
    ggplot2::geom_line(data = frontier, ggplot2::aes(vol, ret),
                       colour = p$line, linewidth = 1.6) +
    ggplot2::geom_point(data = pts, ggplot2::aes(vol, ret, colour = col), size = 2.8) +
    ggplot2::scale_colour_identity() +
    ggplot2::geom_point(data = anchors[anchors$label == "tangency", ],
                        ggplot2::aes(vol, ret), shape = 21, size = 5,
                        fill = p$ring_fill, colour = p$ring, stroke = 1.5) +
    ggplot2::scale_x_continuous(expand = ggplot2::expansion(mult = c(0.02, 0.06))) +
    ggplot2::scale_y_continuous(expand = ggplot2::expansion(mult = c(0.06, 0.08))) +
    ggplot2::theme_void() +
    ggplot2::theme(legend.position = "none", plot.margin = ggplot2::margin(0, 0, 0, 0),
                   plot.background = ggplot2::element_blank(),
                   panel.background = ggplot2::element_blank())
}

# the ground: one color, or a vertical wash from the first color at the top
ground <- function(p) {
  if (length(p$bg) == 1L) {
    grid.rect(gp = gpar(fill = p$bg, col = NA))
  } else {
    grid.raster(matrix(grDevices::colorRampPalette(p$bg)(512), ncol = 1),
                width = unit(1, "npc"), height = unit(1, "npc"), interpolate = TRUE)
  }
}

# the title in three lines, bar above, subtitle below; returns the y where
# the block ends
title_block <- function(p, x, top, width_in, max_pt, sub_pt = 19, bar_w = 1.15) {
  s  <- fit("Allocation", width_in, display, "bold", max_pt)
  lh <- s / 72 * 1.04
  bar(x, top + 0.2, w = bar_w, h = 0.09, col = p$bar)
  txt("Tidy Asset", x, top,          s, display, "bold", p$title)
  txt("Allocation", x, top - lh,     s, display, "bold", p$title)
  txt("in R",       x, top - 2 * lh, s, display, "bold", p$title)
  y_sub <- top - 3 * lh - 0.3
  txt(subtitle, x, y_sub, sub_pt, sans, "plain", p$sub, lineheight = 1.3)
  y_sub - 2 * sub_pt / 72 * 1.3
}

# B as drawn above, with a palette and a canvas: the geometry of draw_B
draw_B_layout <- function(p, W = 8, H = 12) {
  m <- 0.9
  ground(p)
  title_block(p, m, 9.35, W - 2 * m, 104)
  place(make_glyph(p), W - m, 1.15, 3.3, 2.5, just = c("right", "bottom"))
  txt(author, m, 1.15, 22, sans, "bold", p$author, just = c("left", "bottom"))
}

# layout 1: the bar and title high, the glyph low and large
draw_highlow <- function(p, W = 8, H = 12) {
  m <- 0.9
  ground(p)
  title_block(p, m, H - 1.25, W - 2 * m, 104)
  place(make_glyph(p), m, 1.6, W - 2 * m, 3.6)
  txt(author, m, 0.95, 22, sans, "bold", p$author, just = c("left", "bottom"))
}

# layout 2: the title in two weights on one line, the glyph bleeding off the
# right edge
draw_oneline <- function(p, W = 8, H = 12) {
  m <- 0.7
  ground(p)
  s <- fit(paste(title_1, title_2), W - 2 * m, display, "bold", 60)
  top <- H - 1.55
  bar(m, top + 0.2, w = 1.0, h = 0.085, col = p$bar)
  txt(title_1, m, top, s, display, "bold", p$title)
  w1 <- convertWidth(grobWidth(textGrob(paste0(title_1, " "),
                                        gp = gpar(fontfamily = display, fontface = "bold",
                                                  fontsize = s))), "in", valueOnly = TRUE)
  txt(title_2, m + w1, top, s, sans, "plain", p$title)
  txt(subtitle, m, top - s / 72 * 1.12 - 0.28, 18, sans, "plain", p$sub, lineheight = 1.3)
  place(make_glyph(p), 1.9, 2.3, W + 0.4, 5.6)       # runs past the right edge
  txt(author, m, 0.95, 22, sans, "bold", p$author, just = c("left", "bottom"))
}

# layout 3: a left-aligned column, a generous bottom margin, the glyph as a
# small device beside the author
draw_column <- function(p, W = 8, H = 12) {
  m <- 1.0
  ground(p)
  title_block(p, m, 9.6, W - 2 * m - 0.6, 90, sub_pt = 18)
  txt(author, m, 2.0, 22, sans, "bold", p$author, just = c("left", "bottom"))
  wa <- convertWidth(grobWidth(textGrob(author, gp = gpar(fontfamily = sans, fontface = "bold",
                                                          fontsize = 22))), "in", valueOnly = TRUE)
  place(make_glyph(p), m + wa + 0.45, 1.88, 1.55, 1.0)
}

# the two reflows of B: a square for the social preview, 16:9 for a slide
draw_square <- function(p, W = 8, H = 8) {
  m <- 0.8
  ground(p)
  title_block(p, m, H - 1.1, W - 2 * m - 0.4, 84, sub_pt = 17)
  place(make_glyph(p), W - m, 0.85, 3.4, 2.5, just = c("right", "bottom"))
  txt(author, m, 0.85, 20, sans, "bold", p$author, just = c("left", "bottom"))
}

draw_wide <- function(p, W = 9.6, H = 5.4) {
  m <- 0.65
  ground(p)
  title_block(p, m, H - 0.95, 4.3, 58, sub_pt = 15, bar_w = 0.95)
  txt(author, m, 0.45, 17, sans, "bold", p$author, just = c("left", "bottom"))
  place(make_glyph(p), W - m, 0.55, 3.9, 3.9, just = c("right", "bottom"))
}

# --- write everything ---------------------------------------------------------
outputs <- list(
  A           = list(draw = draw_A,                                    w = 1600, h = 2400),
  B           = list(draw = draw_B,                                    w = 1600, h = 2400),
  C           = list(draw = draw_C,                                    w = 1600, h = 2400),
  "B-highlow" = list(draw = function() draw_highlow(palettes$brand),   w = 1600, h = 2400),
  "B-oneline" = list(draw = function() draw_oneline(palettes$brand),   w = 1600, h = 2400),
  "B-column"  = list(draw = function() draw_column(palettes$brand),    w = 1600, h = 2400),
  "B-navy"    = list(draw = function() draw_B_layout(palettes$navy),   w = 1600, h = 2400),
  "B-amber"   = list(draw = function() draw_B_layout(palettes$amber),  w = 1600, h = 2400),
  "B-wash"    = list(draw = function() draw_B_layout(palettes$wash),   w = 1600, h = 2400),
  "B-square"  = list(draw = function() draw_square(palettes$brand),    w = 1600, h = 1600),
  "B-wide"    = list(draw = function() draw_wide(palettes$brand),      w = 1920, h = 1080),
  # the finals
  "B-wash-gold"       = list(draw = function() draw_B_layout(palettes$wash_gold), w = 1600, h = 2400),
  "B-amber2"          = list(draw = function() draw_B_layout(palettes$amber2),    w = 1600, h = 2400),
  "card-navy-wide"    = list(draw = function() draw_wide(palettes$navy),          w = 1920, h = 1080),
  "card-navy-square"  = list(draw = function() draw_square(palettes$navy),        w = 1600, h = 1600),
  "card-amber2-wide"  = list(draw = function() draw_wide(palettes$amber2),        w = 1920, h = 1080),
  "card-amber2-square"= list(draw = function() draw_square(palettes$amber2),      w = 1600, h = 1600)
)
# the finals under stable names, for _quarto.yml and the slides: to switch the
# cards to amber2, change the two names on the right
finals <- c(cover = "B-wash", "cover-social" = "card-navy-square", "cover-wide" = "card-navy-wide")
only <- commandArgs(trailingOnly = TRUE)       # optional: names of the variants to write
if (length(only)) outputs <- outputs[only]

for (v in names(outputs)) {
  o <- outputs[[v]]
  render(o$draw, sprintf("assets/cover/cover-%s.png", v), o$w, o$h, res = 200)
  render(o$draw, sprintf("assets/cover/cover-%s-preview.png", v), 600,
         round(600 * o$h / o$w), res = 200 * 600 / o$w)
  message("cover-", v, ": written")
}
for (f in names(finals)) {
  for (suffix in c("", "-preview")) {
    src <- sprintf("assets/cover/cover-%s%s.png", finals[[f]], suffix)
    if (file.exists(src)) file.copy(src, sprintf("assets/cover/%s%s.png", f, suffix), overwrite = TRUE)
  }
}
message("finals: ", paste(sprintf("%s.png <- %s", names(finals), finals), collapse = "; "))
message("tangency portfolio at ", sprintf("%.1f%% volatility, %.1f%% excess return",
        100 * anchors$vol[2], 100 * anchors$ret[2]),
        "; labels moved: ", paste(lab_a$label[lab_a$moved], collapse = ", "),
        "; efficient assets: ", paste(assets$label[assets$efficient], collapse = ", "))
