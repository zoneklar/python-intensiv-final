from pathlib import Path
from typing import NamedTuple, TextIO, Generator


class Datapoint(NamedTuple):
    x: int
    y: int
    z: int


def reader(file: TextIO) -> Generator:
    """Iteriere über Filehandle und erzeuge Datapoints."""
    for row in file:
        d = Datapoint(*[int(i) for i in row.strip().split(",")])
        yield d


def file_reader(filename: str) -> list[Datapoint]:
    """Öffne Datei und erzeuge Liste von Datapoints."""
    result = []
    with open(Path(__file__).parent / filename) as f:
        for datapoint in reader(f):
            result.append(datapoint)
    return result


print(file_reader("datapoints.csv"))
