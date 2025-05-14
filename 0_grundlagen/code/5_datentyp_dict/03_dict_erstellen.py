"""
Erstellen von Dictionaries in Python

Dictionaries können auf verschiedene Arten erstellt werden. Python bietet
flexible Möglichkeiten wie Literale, den `dict`-Konstruktor oder die Verwendung
von `zip`, um Schlüssel-Wert-Paare zu definieren.

Themenübersicht:
1. Erstellung mit Literalen
2. Erstellung mit dem `dict`-Konstruktor
3. Erstellung mit `zip`
"""

from pprint import pprint

a = {"a": 3}  # Literal

b = dict(a=1, b=3)  # mit Dict-Konstruktor

# Dict erstellen (klassisch)
names = ["Bob", "alice", "Grumpy"]
grades = [1, 2, 3]
d = {}

for index, name in enumerate(names):
    d[name] = grades[index]

print(d)

# ------------------------------------------------------------------------
# Zip-Funktion (erstellt ein Zip-Objekt, über das lässt sich iterieren)
for name, grade in zip(names, grades):
    print(name, grade)

# ------------------------------------------------------------------------
# Dict erstellen (pythonisch)
d = dict(zip(names, grades))
print(d)


# ------------------------------------------------------------------------
cities = {
    "hamburg": {"population": 1_900_000, "lang": "hanseatisch"},
    "dortmund": {"population": 600_000, "lang": "de"},
}

# Pretty Print
pprint(cities, width=21, sort_dicts=False)
