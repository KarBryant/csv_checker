# csv-checker

`csv-checker` is a lightweight command-line tool for inspecting and
analyzing CSV files.

It focuses strictly on **structural and data-quality metrics**, not
transformation, normalization, or ETL.

The goal is to provide fast, dependency-light inspection of CSV
structure and common quality issues.

------------------------------------------------------------------------

## Current Features

The `metrics` command analyzes a CSV file and reports:

### Structure

-   Header values (optional)
-   Column count
-   Row count (data rows only; header excluded)
-   Minimum field count per row
-   Maximum field count per row

### Header Issues (if `--has-headers`)

-   Empty header columns (by index)
-   Duplicate header names (with occurrence counts)

### Data Quality

-   Empty row count (rows where all parsed cells are blank)
-   Empty cell count (blank cells across all rows)
-   Blank count by column (tuple indexed by column position)
-   Rows with extra fields (more fields than schema column count)
-   Rows with missing fields (fewer fields than schema column count)

### Metadata

-   UTC timestamp indicating when metrics were generated

------------------------------------------------------------------------

## Installation (development)

Currently intended for local development use.

``` bash
pip install -e .
```

------------------------------------------------------------------------

## Usage

``` bash
csv_checker metrics <file.csv>
```

### Options

``` bash
--has-headers / --no-headers
```

Defaults to `--has-headers`.

Example:

``` bash
csv_checker metrics data.csv
csv_checker metrics --no-headers data.csv
```

------------------------------------------------------------------------

## Metric Definitions

To avoid ambiguity, here is the exact behavior:

-   **row_count**\
    Counts all data rows processed.\
    If `--has-headers` is enabled, the header row is not included.

-   **empty_row_count**\
    Rows where every parsed cell is blank after stripping whitespace.\
    An empty line parsed as `[]` is also counted as an empty row.

-   **empty_cell_count**\
    Counts blank cells (`""` after `.strip()`) within the first
    `column_count` fields of each row.\
    Rows with fewer fields than the schema contribute additional blank
    cells for missing columns.

-   **rows_with_extra_fields**\
    Rows with more fields than the inferred column count.

-   **rows_with_missing_fields**\
    Rows with fewer fields than the inferred column count.

-   **column_count**\
    Determined from:

    -   The header row (if `--has-headers`)
    -   The first non-blank data row (if `--no-headers`)

------------------------------------------------------------------------

## Design Goals

-   No pandas dependency
-   No automatic type inference
-   No transformation or normalization logic
-   Keep core logic isolated from CLI rendering
-   Deterministic metrics output

------------------------------------------------------------------------

## Project Structure

    src/csv_checker/
    ├── adapters/        # I/O layer (Reader)
    ├── core/            # Profiler and Orchestrator
    ├── models/          # Immutable metrics model
    └── cli.py           # Typer CLI entry point

Architecture layers:

Reader → Profiler → Orchestrator → CLI

------------------------------------------------------------------------

## Roadmap

Planned improvements:

-   JSON export with stable schema
-   Improved formatting / output polish
-   Unit tests for metrics logic
-   Additional CSV dialect configuration
-   Optional JSON serializer for metrics

------------------------------------------------------------------------

## Status

Early release.\
Usable for structural inspection of CSV files.\

------------------------------------------------------------------------

## License

MIT
