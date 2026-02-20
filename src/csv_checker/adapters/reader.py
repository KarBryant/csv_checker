import csv
from pathlib import Path


class Reader:
    """
    Reads a CSV file and yeilds its rows.
    """
    @staticmethod
    def read(datafile: Path):
        """
        Yields rows from the CSV file as lists of strings.
        """
        with datafile.open(mode="r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                yield row
