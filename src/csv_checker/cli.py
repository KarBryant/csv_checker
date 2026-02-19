import typer
from rich.table import Table
from rich.console import Console
from pathlib import Path
from typing import Annotated
from csv_checker.core.orchestrator import Orchestrator

app = typer.Typer(help="CSV_Checker: A tool for analyzing csv files")
console = Console()


@app.command()
def metrics(
    path: Annotated[Path, typer.Argument(help="file to be actioned upon")],
    has_headers: Annotated[
        bool,
        typer.Option(
            "--has-headers/--no-headers", help="provide if the csv has headers or not"
        ),
    ] = True,
):

    output_table = Table(title="CSV Metrics")
    output_table.add_column("Metric")
    output_table.add_column("Value(s)")
    result = Orchestrator.profile(path=path, has_header=has_headers)

    output_table.add_row("Headers", str(result.headers))
    output_table.add_row("Column Count", str(result.column_count))
    output_table.add_row("Row Count", str(result.row_count))
    output_table.add_row("Minimum Field Count", str(result.min_field_count))
    output_table.add_row("Maximum Field Count", str(result.max_field_count))
    output_table.add_row("Empty Header Columns", str(result.empty_header_columns))
    output_table.add_row("Duplicate Headers", str(result.duplicate_headers))
    output_table.add_row("Empty Row Count", str(result.empty_row_count))
    output_table.add_row("Empty Cell Count", str(result.empty_cell_count))
    output_table.add_row("Blank Count By Column", str(result.blank_count_by_column))
    output_table.add_row("Rows With Extra Fields", str(result.rows_with_extra_fields))
    output_table.add_row(
        "Rows With Missing Fields", str(result.rows_with_missing_fields)
    )
    output_table.add_row("Generated At", str(result.generated_at.ctime()))

    console.print(output_table)


def main():
    app()


if __name__ == "__main__":
    main()
