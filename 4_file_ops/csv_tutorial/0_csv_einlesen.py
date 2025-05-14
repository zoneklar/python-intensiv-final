"""
CSV Dateien einlesen:
- CSV Reader (oldschool)

"""

from pathlib import Path
import csv

NAME = 0
AGE = 1


def read_csv(file: str) -> None:
    """CSV Datei auslesen."""
    with open(Path(__file__).parent / file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)  # rückt den iterator einen schritt weiter
        for row in reader:
            print(row[NAME], row[AGE])


def read_csv_advanced(file: str) -> None:
    """CSV DAtei auslesen mit einem Dict-reader."""
    with open(Path(__file__).parent / file, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            print(row["name"])


read_csv_advanced(file="data.csv")
