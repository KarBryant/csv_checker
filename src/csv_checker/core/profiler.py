from csv_checker.models.csv_metrics import CsvMetrics
from csv_checker.adapters.reader import Reader
from pathlib import Path
from datetime import datetime, timezone


class Profiler:
    """
    Collects metric data about a provided CSV file.
    """

    @staticmethod
    def collect_metrics(path: Path, has_header: bool = True) -> CsvMetrics:
        """
        Reads a csv file and computes structural and data quality metrics.

        If has_header is True, the first row is treated as headers
        and excluded from the data row count.
        """
        rows = Reader.read(path)

        headers = None
        headers_consumed = False
        column_count = 0
        row_count = 0
        min_field_count = float("inf")
        max_field_count = 0

        empty_header_columns = set()
        duplicate_headers = {}

        empty_row_count = 0
        empty_cell_count = 0
        blank_count_by_column = []
        rows_with_extra_fields = 0
        rows_with_missing_fields = 0

        for row in rows:
            field_count = len(row)
            if has_header and not headers_consumed:
                headers = []
                seen_headers = set()
                for index, item in enumerate(row):
                    item = item.strip()
                    headers.append(item)
                    if item == "":
                        empty_header_columns.add(index)
                        continue

                    if item not in seen_headers:
                        seen_headers.add(item)
                    elif item not in duplicate_headers:
                        duplicate_headers[item] = 2
                    else:
                        duplicate_headers[item] += 1

                column_count = field_count
                min_field_count = field_count
                max_field_count = field_count
                headers_consumed = True
                blank_count_by_column = [0] * column_count
                continue

            if column_count == 0 and not has_header:
                if all(cell.strip() == "" for cell in row):
                    # don't infer schema from a fully blank row
                    empty_row_count += 1
                    row_count += 1
                    continue
                column_count = field_count
                min_field_count = field_count
                max_field_count = field_count
                blank_count_by_column = [0] * column_count

            if all(cell.strip() == "" for cell in row):
                empty_row_count += 1

            row_count += 1

            if field_count > max_field_count:
                max_field_count = field_count

            if field_count < min_field_count:
                min_field_count = field_count

            if field_count > column_count:
                rows_with_extra_fields += 1

            if field_count < column_count:
                rows_with_missing_fields += 1
                difference = column_count - field_count
                empty_cell_count += difference
                for index in range(field_count, column_count):
                    blank_count_by_column[index] += 1

            for index, cell in enumerate(row[:column_count]):
                if cell.strip() == "":
                    empty_cell_count += 1
                    blank_count_by_column[index] += 1

        if min_field_count == float("inf"):
            min_field_count = 0

        metrics = CsvMetrics(
            headers=headers,
            column_count=column_count,
            row_count=row_count,
            min_field_count=min_field_count,
            max_field_count=max_field_count,
            empty_header_columns=sorted(empty_header_columns),
            duplicate_headers=duplicate_headers,
            empty_row_count=empty_row_count,
            empty_cell_count=empty_cell_count,
            blank_count_by_column=tuple(blank_count_by_column),
            rows_with_extra_fields=rows_with_extra_fields,
            rows_with_missing_fields=rows_with_missing_fields,
            generated_at=datetime.now(timezone.utc),
        )

        return metrics
