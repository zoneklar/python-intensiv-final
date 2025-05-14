"""
Datentyp String in Python

In Python repräsentiert der Datentyp `str` Zeichenketten (Strings). Strings
sind immutable, d. h., sie können nach ihrer Erstellung nicht verändert
werden. Python bietet zahlreiche Methoden zur Verarbeitung und Analyse
von Strings.

Themenübersicht:
1. Eigenschaften von Strings
2. Die Funktion `len`
3. Wichtige String-Methoden
   - Methoden zur Prüfung: `.isxxx()`
   - Suche innerhalb von Strings: `.index()`, `.find()`, `.rfind()`
4. Indexierung und Slicing
5. Konkatenierung und Maskierung
6. Zusätzliche String-Methoden
"""

number = 1

x = "asjddsajjö"
y = 'hello "world" '
print(y)

print(x[0])  # String

# Iteration über einen String
for char in x:
    print("char:", char)

# Auf eine Sequenz lässt sich in der Regel die len-Funktion
print(len(y))  # Anzahl Zeichen laut Unicode, y.__len__()

name = "bob"
# find und index haben gleiche Funktionalität
print(name.find("o"))  # -1 falls nicht gefunden wird
# print(name.index("r"))  # ValueError

# Strings verbinden
city = "Hamburg" + "Hafen"  # Konkatenation
print(type(city))

# replace
city = city.replace("am", "te")
print(city)


# Liste von Strings
p = "####".join(["hi", "ads", "ziu"])
print(p)

m = 3.12
print("ich bin", m, "Meter gesprungen")
