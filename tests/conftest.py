import pytest
from pathlib import Path

@pytest.fixture
def csv_file(tmp_path:Path) -> Path:
    file = tmp_path / "file.csv"
    file.write_text(
        "id,name,age\n"
        "101,joe,30\n"
        "102,jane,31"
    )
    return file

@pytest.fixture
def bad_csv_file(tmp_path:Path) -> Path:
    file = tmp_path / "file.csv"
    file.write_text(
        "id,name,age,,age,age\n"
        "101,,30,male\n"
        ",,,\n"
        "102,jane,31,female,artist\n"
        "103,jack\n"
        "104,bob,20,male,artist,brown hair, brown eyes, 1 dog, gaming"
    )
    return file

@pytest.fixture
def empty_csv_file(tmp_path:Path) -> Path:
    file = tmp_path / "file.csv"
    file.write_text("")
    return file

@pytest.fixture
def no_header_csv_file(tmp_path:Path) -> Path:
    file = tmp_path / "file.csv"
    file.write_text(
        "101,karson,30\n"
        "102,danielle,31"
    )
    return file

@pytest.fixture
def no_header_with_empty_first_row(tmp_path:Path) -> Path:
    file = tmp_path / "file.csv"
    file.write_text(
        ",,\n"
        "101,karson,30\n"
        "102,danielle,31"
    )
    return file

@pytest.fixture
def test_dir(tmp_path:Path) -> Path:
    dir = tmp_path / "testdir"
    dir.mkdir()
    file = dir / "test.txt"
    file.write_text("fubar")

    return dir