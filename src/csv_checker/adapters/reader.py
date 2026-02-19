import csv
from pathlib import Path


class Reader:

    @staticmethod
    def read(datafile: Path):
        with datafile.open(mode="r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                yield row
