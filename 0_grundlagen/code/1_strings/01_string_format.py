"""
f-Strings und die Methode `format()` in Python

Python bietet leistungsfähige Möglichkeiten zur String-Formatierung. Zwei
häufig verwendete Ansätze sind f-Strings (seit Python 3.6) und die Methode
`format()`. Beide erlauben das Einfügen von Werten in Strings und das
Anpassen des Ausgabeformats.

Themenübersicht:
1. Grundlagen von f-Strings
2. Platzhalter und Formatierung mit `format()`
3. Darstellung von Zahlensystemen
4. Darstellung großer Zahlen mit Tausendertrenner
"""

name = "Alice"
age = 30

m = 3.12
print("ich bin", m, "Meter gesprungen")  # alt
print(f"ich bin {m} Meter gesprungen")  # F-String

res = "ich bin {} Meter {} gesprungen".format(3.34, "yx")
print(res)

# Formatierung von Zahlen
pi = 3.14159265359
print(f"Formatierung von PI: {pi:.5f}")

# Integer-Repräsentationen
print("int: {0:d} hex:{0:x} okt:{0:o} bin:{0:b}".format(42))

# Keyword-Argument
coords = "Coords: {latitude} {longitude}".format(latitude=4, longitude=62)
print(coords)

x = 3
y = 83
print(f"{x=}")
print(f"{y=}")
print(f"{x / y=}")

# Prozentuales Verhältnis
points = 19
total = 22
print("Correct answers: {:.2f}".format(points / total))
print("Correct answers: {:.2%}".format(points / total))

long_number = 1_000_000
print(f"{long_number:_}")  # ausgabe mit _
print(f"{long_number:,}")  # ausgabe mit ,
