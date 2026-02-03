# csv-checker

csv-verify is a small command-line tool for inspecting CSV files.

This project is in its early stages. The goal is to build a simple utility that focuses on **analysis/inspection**, not data transformation or heavy ETL.

Planned features:
- Compute quick metrics and summaries about a CSV file (rows, columns, empty cells, inconsistent rows, etc.)
- Export the metrics report to a JSON file (stable schema)

## Planned usage (subject to change)

- `csvchecker metrics <file.csv>`  
  Prints metrics to stdout

- `csvchecker metrics <file.csv> --json-out report.json`  
  Writes the metrics report to JSON

## Notes / non-goals (for now)

- No pandas dependency
- No automatic type inference
- No per-file schema configuration

## License

MIT
