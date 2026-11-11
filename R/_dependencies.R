# Not sourced by the book. This file exists so that renv can discover the full
# dependency set while the chapters are still stubs: renv scans for library()
# calls, and TODO sections contain none.
#
# Delete a line here only when the corresponding chapter genuinely stops using
# the package -- renv::snapshot() takes this file as the declaration of intent.

# --- core -------------------------------------------------------------------
library(tidyverse)
library(xts)
library(zoo)
library(timetk)
library(tsibble)
library(slider)

# --- portfolio machinery -----------------------------------------------------
library(PortfolioAnalytics)
library(PerformanceAnalytics)

# --- solvers and backends ----------------------------------------------------
library(CVXR)
library(ROI)
library(ROI.plugin.quadprog)
library(ROI.plugin.glpk)
library(osqp)
library(Rglpk)
library(clarabel)
library(DEoptim)
library(GenSA)
library(pso)
library(mco)
library(nloptr)
library(quadprog)

# --- moments, robustness, dependence -----------------------------------------
library(corpcor)
library(robustbase)
library(rrcov)
library(copula)
library(rmgarch)

# --- data --------------------------------------------------------------------
library(tidyquant)
library(tidyfinance)
library(FFdownload)
library(frenchdata)
library(fredr)
library(arrow)
library(readxl)

# --- modelling (chapters 14, 16) ---------------------------------------------
library(tidymodels)

# --- authoring ---------------------------------------------------------------
library(knitr)
library(rmarkdown)
library(quarto)
library(kableExtra)
library(gt)
library(downlit)
library(xml2)

# Used by the generated appendices: 91-package-notes reads renv.lock and prints
# session information for the packages the book actually depends on.
library(jsonlite)
library(sessioninfo)

# --- the companion package ----------------------------------------------------
# Installed from the sibling directory, not from CRAN. See CLAUDE.md.
# library(tidypm)
