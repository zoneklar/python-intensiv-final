"""
Aufgabe – Generator‑Funktion chunked(iterable, size)

Schreibe eine Funktion chunked(iterable, size), die mithilfe von
yield aufeinanderfolgende Teilstücke («Chunks») der Länge size liefert.
Der letzte Chunk darf kürzer sein, wenn die Elemente nicht aufgehen.

    >>> list(chunked("abcdefg", 3))
    ['abc', 'def', 'g']

Regeln:
    • Keine Listen in voller Länge anlegen – iteriere einmalig.
    • size > 0 voraussetzen, sonst ValueError werfen.
    • Nur Standard‑Bibliothek, kein itertools.chunked verwenden.
"""

from typing import Sequence, Iterator


def chunked(iterable: Sequence, size: int) -> Iterator:
    if size <= 0:
        raise ValueError("size muss > 0 sein")

    for i in range(0, len(iterable), size):
        yield iterable[i : i + size]


# Mini‑Demo
if __name__ == "__main__":
    print(list(chunked("abcdefg", 3)))  # ['abc', 'def', 'g']
    print(list(chunked(list(range(7)), 2)))  # [[0, 1], [2, 3], [4, 5], [6]]
