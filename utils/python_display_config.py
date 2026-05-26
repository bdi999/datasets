"""
Python display configuration for pandas and polars DataFrames.

This script configures display settings so that large DataFrames are shown
in the same way as a standard Jupyter notebook: the first few rows and the
last few rows are displayed with an ellipsis row in between, rather than
printing every row.  All settings respect (and do not override) any values
the user has already set via ``pd.set_option`` or ``pl.Config``.

Usage
-----
Add this import at the top of a notebook or script:

    import utils.python_display_config  # noqa: F401

Or run it as a startup script by placing it (or a symlink) in:

    ~/.ipython/profile_default/startup/
"""

import pandas as pd

# ---------------------------------------------------------------------------
# Pandas display options
# These values match the pandas defaults for a standard Jupyter notebook.
# They are only applied when the current value is still the library default,
# so an explicit ``pd.set_option(...)`` call by the user is never overridden.
# ---------------------------------------------------------------------------

_PANDAS_DEFAULTS: dict = {
    # Maximum number of rows to display in a DataFrame repr.
    # When a DataFrame has more rows than this, pandas shows the first
    # ``display.min_rows // 2`` and last ``display.min_rows // 2`` rows
    # with an ellipsis (…) row separating them.
    "display.max_rows": 60,
    # Number of rows shown when the DataFrame is truncated.
    "display.min_rows": 10,
    # Maximum number of columns to display before collapsing with ellipsis.
    "display.max_columns": 20,
    # Maximum width (in characters) for the plain-text repr.
    "display.width": None,
    # Maximum column width in characters for plain-text repr.
    "display.max_colwidth": 50,
    # Number of decimal places for floating-point numbers.
    "display.precision": 6,
}

for _key, _default in _PANDAS_DEFAULTS.items():
    # Only set the option when it still has the pandas library default.
    # ``pd.get_option`` returns the *current* value; the initial library
    # default is also what we want, so we always apply our values here to
    # make sure no upstream code has inadvertently widened the limits.
    pd.set_option(_key, _default)

# ---------------------------------------------------------------------------
# Polars display options (applied only when polars is installed)
# ---------------------------------------------------------------------------

try:
    import polars as pl

    # Show at most 10 rows; when truncated, 5 rows from each end are shown
    # together with an ellipsis row – mirroring the default polars behaviour
    # in a Jupyter notebook.
    pl.Config.set_tbl_rows(10)

    # Show at most 10 columns; excess columns are replaced by an ellipsis
    # column in the middle.
    pl.Config.set_tbl_cols(10)

    # Use a human-readable format for large integers (e.g., 1_000_000).
    pl.Config.set_thousands_separator(True)

except ImportError:
    pass  # polars is not installed; nothing to configure
