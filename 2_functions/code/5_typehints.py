"""
Type Hints: Typ-hinweise für
- Editor
- statische Typ-Analyse


pip install mypy

im Editor: mypy Extension von Microsoft

dict[str, int]  => Dict von String und Int
tuple[float, floats, floats] => Tuple aus 3 floats

im Typing-Modul finden sich weitere Datentypen bzw.
Datenstrukturen, die für das Typing genutzt werden können.
"""

from typing import Iterable


def summe(a: float, b: float) -> float:
    """Berechne Summe von a und b."""
    return a + b


def alter_input(value: str | int) -> str | int:
    """mit dem |-Symbol lassen sich mehrere Datentypen angeben."""
    return 1


def print_values(values: Iterable[int]) -> None:
    """Liste von Ints."""
    for value in values:
        print(value)


x = summe(1, 3.2)
summe("a", "a")  # Fehler, da summe ein Float erwartet
# summe([1, 2], [2, 5])

print_values([1, 2, 3, 5])
print_values((1, 2, 3, 5))
