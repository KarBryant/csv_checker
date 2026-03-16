import json
from dataclasses import asdict
from csv_checker.models.csv_metrics import CsvMetrics


class JSONSerializer:

    @staticmethod
    def serialize(data: CsvMetrics) -> str:
        return json.dumps(asdict(data), indent=2, default=str)
