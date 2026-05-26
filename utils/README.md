# Runtime Display Configuration

This directory contains lightweight startup scripts that apply display settings
matching the defaults of a standard Jupyter / R Notebook environment.  Without
these settings, some runtimes (playground, challenge cards, code blocks) may
print every row of a large DataFrame instead of truncating it with an ellipsis.

---

## Python – pandas and polars

**File:** `python_display_config.py`

| Setting | Value | Effect |
|---|---|---|
| `pd.display.max_rows` | 60 | DataFrames with more than 60 rows are truncated |
| `pd.display.min_rows` | 10 | Truncated DataFrames show 5 rows from each end |
| `pd.display.max_columns` | 20 | DataFrames with more than 20 columns are truncated |
| `pd.display.max_colwidth` | 50 | String values are truncated at 50 characters |
| `pd.display.precision` | 6 | Floating-point numbers show 6 decimal places |
| `pl.Config.set_tbl_rows` | 10 | Polars DataFrames show at most 10 rows |
| `pl.Config.set_tbl_cols` | 10 | Polars DataFrames show at most 10 columns |

### Usage

```python
# At the top of a notebook or script:
import utils.python_display_config  # noqa: F401
```

To use it as a kernel startup script (applies to every notebook automatically):

```bash
# Copy or symlink into the IPython startup directory
cp utils/python_display_config.py ~/.ipython/profile_default/startup/
```

---

## R – data.frame, tibble, and data.table

**File:** `r_display_config.R`

| Setting | Value | Effect |
|---|---|---|
| `max.print` | 1000 | Base R limits total elements printed |
| `tibble.print_max` | 10 | Tibbles with more than 10 rows are truncated |
| `tibble.print_min` | 5 | Truncated tibbles show 5 rows from the top |
| `datatable.print.nrows` | 10 | data.tables show at most 10 rows |
| `datatable.print.topn` | 5 | Truncated data.tables show 5 rows from each end |

### Usage

```r
# At the top of a script or notebook:
source("utils/r_display_config.R")
```

To apply it automatically for every R session in the project, add the `source`
call to a project-level `.Rprofile` file:

```r
# .Rprofile (project root)
source(file.path(getwd(), "utils", "r_display_config.R"))
```

---

## Why these defaults?

Both pandas and tibble are designed to display only a manageable subset of a
large table so that notebook output stays readable.  The exact defaults used
here match what a user would see in a standard Jupyter Notebook or R Notebook:

- **pandas** (Jupyter): first 30 rows + `…` + last 30 rows when `len(df) > 60`
- **polars** (Jupyter): first 5 rows + `…` + last 5 rows when `len(df) > 10`
- **tibble** (R Notebook): first 10 rows + footer summary
- **data.table** (R): first 5 rows + `---` separator + last 5 rows
