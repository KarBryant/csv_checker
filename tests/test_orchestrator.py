from csv_checker.core.orchestrator import Orchestrator
from csv_checker.models.csv_metrics import CsvMetrics
import pytest
from pathlib import Path

def test_good_csv_file(csv_file):
    data = Orchestrator.profile(csv_file)
    assert isinstance(data,CsvMetrics)

def test_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        Orchestrator.profile(tmp_path / "bad_file.csv")

def test_profile_directory(test_dir):
    with pytest.raises(ValueError):
        Orchestrator.profile(test_dir)

def test_profile_non_csv(test_dir):
    with pytest.raises(ValueError):
        file:Path = test_dir / "test.txt"
        Orchestrator.profile(file)