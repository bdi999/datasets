# R display configuration for data.frame, tibble, and data.table
#
# Source this file at the top of a script or notebook to apply display
# settings that mirror the default output of an R Notebook or R Markdown
# document.  Large tables are truncated – showing only the first few rows
# and a summary of the remaining rows – rather than printing every row.
#
# Usage
# -----
# Add this line at the top of your R script or notebook:
#
#   source("utils/r_display_config.R")
#
# Or place it in a project-level .Rprofile so it is applied automatically.

# ---------------------------------------------------------------------------
# Base R data.frame / matrix display
# ---------------------------------------------------------------------------

options(
  # Maximum number of elements (cells) to print for vectors and data.frames.
  # The default in R is 1000; setting it explicitly here keeps behaviour
  # consistent across environments that may have altered the global option.
  max.print = 1000
)

# ---------------------------------------------------------------------------
# tibble display (requires the tibble package)
# ---------------------------------------------------------------------------

if (requireNamespace("tibble", quietly = TRUE)) {
  options(
    # Maximum rows to print before truncating the output.
    tibble.print_max = 10,

    # Number of rows to print (from the top) when the tibble is truncated.
    # The footer will show how many additional rows exist.
    tibble.print_min = 5,

    # Maximum number of columns to display; additional columns are listed
    # in the footer.  NULL means use the console width.
    tibble.width = NULL,

    # Maximum characters to display per column value before truncating.
    tibble.max_extra_cols = 100
  )
}

# ---------------------------------------------------------------------------
# data.table display (requires the data.table package)
# ---------------------------------------------------------------------------

if (requireNamespace("data.table", quietly = TRUE)) {
  options(
    # Number of rows to show from each end when the table is large.
    # The default in data.table is 5 (top) + 5 (bottom).
    datatable.print.nrows = 10,

    # Number of rows shown from the top and bottom when truncating.
    datatable.print.topn  = 5,

    # Print the class of each column below the column name.
    datatable.print.class = TRUE,

    # Print a row count footer ("... with N more rows").
    datatable.print.keys  = TRUE
  )
}
