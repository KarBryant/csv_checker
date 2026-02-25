#from tests.conftest import csv_file
import pytest
from csv_checker.models.csv_metrics import CsvMetrics
from csv_checker.core.profiler import Profiler


def test_basic_profile(csv_file):
    data = Profiler.collect_metrics(csv_file)
    assert isinstance(data,CsvMetrics)
    assert len(data.headers) == 3
    assert data.column_count == 3
    assert data.row_count == 2


def test_profile_bad_data(bad_csv_file):
    data = Profiler.collect_metrics(bad_csv_file)
    assert isinstance(data,CsvMetrics)
    assert data.blank_count_by_column[1] == 2
    assert data.empty_cell_count == 14
    assert data.empty_row_count == 1
    assert len(data.empty_header_columns) == 1
    assert data.duplicate_headers == {"age": 3}
    assert data.max_field_count == 5
    assert data.min_field_count == 2
    assert data.rows_with_extra_fields == 1

def test_empty_csv_file(empty_csv_file):
    data = Profiler.collect_metrics(empty_csv_file, has_header=False)
    assert data.column_count == 0
    assert data.row_count == 0
    assert data.empty_row_count == 0

def test_no_header_csv_profile(no_header_csv_file):
    data = Profiler.collect_metrics(no_header_csv_file, has_header=False)
    assert data.headers == None
    assert data.row_count == 2

def test_no_header_empty_first_row_csv_profile(no_header_with_empty_first_row):
    data = Profiler.collect_metrics(no_header_with_empty_first_row, has_header=False)
    assert data.empty_row_count == 1
    assert data.row_count == 3