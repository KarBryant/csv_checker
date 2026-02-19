from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CsvMetrics:
    # Structure
    headers: list[str] | None
    column_count: int
    row_count: int
    min_field_count: int
    max_field_count: int

    # Header issues
    empty_header_columns: list[int]
    duplicate_headers: dict[str, int]

    # Data quality
    empty_row_count: int
    empty_cell_count: int
    blank_count_by_column: tuple[int, ...]
    rows_with_extra_fields: int
    rows_with_missing_fields: int

    # Metadata
    generated_at: datetime
