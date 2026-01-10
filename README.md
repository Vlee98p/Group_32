# Welcome to Our DataFrame Memory Optimizer

This is a collaborative project developed as part of DSCI 524: Collaborate Softwware Development. 

## Project Summary

DataFrame Memory Optimizer is a lightweight Python package that reduces the memory footprint of pandas DataFrames by automatically selecting more efficient data types. It analyzes each column in a DataFrame and applies safe, transparent optimizations such as numeric downcasting and categorical conversion while preserving the original data values. This will allow users to work more efficiently with large datasets in data analysis, machine learning pipelines, and resource-constrained environments.

## Planned Functions 

The package is designed around a simple, reproducible workflow: users call optimize_dataframe() once, and the function applies a consistent set of memory-saving steps while keeping the original DataFrame unchanged.

`optimize_dataframe(df)`
The main user-facing entry point. It creates a copy of `df` and coordinates the full optimization pipeline by (1) downcasting numeric columns, (2) converting low-cardinality text columns to `category`, and (3) running a diagnostics pass to report columns that were intentionally left unchanged (e.g., IDs). Returns the optimized DataFrame.

`optimize_numeric(df)`
Numeric optimizer used by `optimize_dataframe()`. It reduces memory usage by downcasting integer columns to the smallest safe integer dtype and optionally downcasting floating-point columns (e.g., float64 → float32) with minimal expected precision impact.

`optimize_categorical(df, max_unique_ratio=0.5)`
Categorical optimizer used by `optimize_dataframe()`. It converts low-cardinality string/object columns to pandas category dtype based on the ratio of unique values to total rows. This is especially effective for repeated labels like status codes, regions, or categories.

`analyze_special_columns(df)`
Diagnostics and transparency helper used by `optimize_dataframe()`. It identifies columns that may require special handling (e.g., high-cardinality IDs, coordinate columns, free-text fields) and reports them to help users understand optimization decisions. This function does not modify the DataFrame.

## How the package fits in the Python Ecosystem

Pandas provides low-level tools related to memory optimization, such as pd.to_numeric(..., downcast=...), DataFrame.convert_dtypes(), and DataFrame.memory_usage(deep=True). However, these tools require manual orchestration and do not provide a unified, opinionated workflow or clear diagnostics.

DataFrame Memory Optimizer builds on these ideas by combining them into a single, reusable interface that applies consistent heuristics and reports its decisions, making DataFrame memory optimization easier, safer, and more reproducible.

## Contributers

Mohammed Ibrahim

Roganci Fontelera

Wai Yan Lee

William Chong

## Copyright

- Copyright © 2026 UBC MDS.
- Free software distributed under the [MIT License](./LICENSE).
