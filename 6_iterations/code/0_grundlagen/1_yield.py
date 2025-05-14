"""
Funktionen mit `yield` sind sogenannte Generatorfunktionen.
Statt mit `return` einen Wert zurückzugeben und zu beenden, liefern
sie mit `yield` einen Wert und pausieren ihren Zustand – beim nächsten
Aufruf wird der Code direkt nach dem `yield` fortgesetzt.

Generatorfunktionen erzeugen automatisch einen Iterator und sind
speichereffizient, da sie Werte bei Bedarf liefern (Lazy Evaluation).

Typische Anwendungen:
- Große Datenmengen sequentiell verarbeiten
- Unendliche Sequenzen generieren
- Zustandsbehaftete Abläufe abbilden

Dieses Skript zeigt verschiedene Anwendungsbeispiele für `yield`.
"""

from typing import Iterator


def filter_data(data: list[int]) -> list:
    """klassische Filterfunktion."""
    result = []
    for value in data:
        if value > 3:
            result.append(value)

    return result


def new_filter_data(data: list[int]) -> Iterator:
    """Generator-Funktion zum Filtern von data"""
    for value in data:
        if value > 3:
            yield value


def infinite_generator(i: int):
    counter = i
    while True:
        yield counter
        counter += 1


iterator = new_filter_data([2, 45, 24, 34])
for i in iterator:
    print(i)


for value in infinite_generator(i=10):
    print(value)
    if value > 30:
        break
