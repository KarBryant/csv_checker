from pathlib import Path
from csv_checker.core.profiler import Profiler
from csv_checker.models.csv_metrics import CsvMetrics


class Orchestrator:
    """
    Coordinates CSV profiling and validation of input by calling the appropriate services.
    """
    @staticmethod
    def profile(path: Path, has_header: bool = True) -> CsvMetrics:
        """
        Validates input path and collects CSV metric data, returning a CsvMetrics object.

        If has_header is true, the first row will not be counted towards row count.
        """
        path = path.expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"{path} was not found")
        if not path.is_file():
            raise ValueError(f"{path} is not a regular file")
        if path.suffix.lower() != ".csv":
            raise ValueError(f"{path} is not a .csv file")
        return Profiler.collect_metrics(path=path, has_header=has_header)
