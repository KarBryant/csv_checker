from typer.testing import CliRunner
from csv_checker.cli import app, main
from pathlib import Path
import pytest

runner = CliRunner()

def test_help():
    result = runner.invoke(app, ["--help"])
    assert "metrics" in result.stdout

def test_metrics(csv_file):
    result = runner.invoke(app, [str(csv_file)])

    assert "Headers" in result.stdout
    assert "Row Count" in result.stdout

def test_bad_file():
    result = runner.invoke(app, ["file.txt"])

    assert result.exit_code != 0
    assert result.exception is not None
    assert "was not found" in str(result.exception)

def test_on_dir(test_dir):
    result = runner.invoke(app, [str(test_dir)])

    assert result.exit_code != 0
    assert "not a regular file" in str(result.exception)

def test_wrong_file_type(test_dir):
    file:Path = test_dir / "test.txt"
    result = runner.invoke(app, [str(file)])

    assert result.exit_code != 0
    assert "not a .csv" in str(result.exception)
