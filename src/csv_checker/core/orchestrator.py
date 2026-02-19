from pathlib import Path
from csv_checker.core.profiler import Profiler
from csv_checker.models.csv_metrics import CsvMetrics


class Orchestrator:

    @staticmethod
    def profile(path: Path, has_header: bool = True) -> CsvMetrics:
        path = path.expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"{path} was not found")
        if not path.is_file():
            raise ValueError(f"{path} is not a regular file")
        if path.suffix.lower() != ".csv":
            raise ValueError(f"{path} is not a .csv file")
        return Profiler.collect_metrics(path=path, has_header=has_header)
