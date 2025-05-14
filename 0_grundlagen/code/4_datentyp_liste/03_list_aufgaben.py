# leicht bis mittel

# 1. Iteration über Liste (leicht)
"""
Iteriere über die Liste und gebe die Elemente aus!

Banane
Apfel
Kirsche

Zusatzaufgabe: gebe zusätzlich den enstprechenden Index aus,
zb. für Banane den Index 0

0 Banane
1 Apfel
2 Kirsche
"""

fruits = ["Banane", "Apfel", "Kirsche"]

for indx, fruit in enumerate(fruits):
    print(indx, fruits)

# 2. Filtern einer Liste 1 (leicht)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_fruits. Die neue
Liste darf nur Elemente enthalten, die mit einem großen B anfangen.

Tip: Nutze dazu die string-Methode startswith oder
den Index-Operator [].

Result: filtered_fruits = ["Banane", "Birne"]
"""
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]
fruits_filtered = []
for fruit in fruits:
    if fruit.startswith("B"):
        fruits_filtered.append(fruit)


# 3. Filtern einer Liste 2 (mittel)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_numbers.
Die neue Liste darf nur Elemente enthalten, die größer als 5 sind
und kleiner als 100. Die filtered_numbers-Liste muss sortiert ausgegeben
werden.

result = [23, 42, 99]
"""
numbers = [1, 4, 5, 2, 42, 2, 1, 99, 23]
numbers_filtered = []
for n in numbers:
    if n > 5 and n < 100:
        numbers_filtered.append(n)

# 5. das letzte Element (mittel)
"""
Gegeben ist eine Liste, die auch leer sein kann. Prüfe, ob sich mindestens
ein Element in der Liste befindet und printe das letzte Element in der Liste.

Erinnerung: eine Liste ist True, wenn sie mindestens
ein Element enthält.
"""
symbols = ["B", "C"]
if symbols:
    print(symbols[-1])


# 6. erlaubte Werte (mittel)
"""
Gegeben sind zwei Listen:
eine Ausgangsliste a und
eine Liste mit erlaubten Werten allowed_values.

Prüfe für jedes Element in a, ob es in der erlaubten Liste enthalten ist,
und füge es einer neuen Liste c hinzu, wenn das zutrifft.

tip:
Iteriere über a und prüfe für jedes Element, ob es erlaubt ist.
Nutze dazu den Membership-Operator in.

result = [50, 200, 50]
"""
a = [50, 100, 40, 20, 200, 50, 100, 10]
c = []
allowed_values = [50, 200]

for value in a:
    if value in allowed_values:
        c.append(value)
print(f"{c=}")

# 7. Bereiningen der Liste (mittel)
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente von _
(underscore) und speichere sie in einer neuen Liste. Leere Elemente sollen
nicht in die neue Liste aufgenommen werden.

result = [xx, alphabeta]

"""
a = ["x_x", "alpha_beta", "_"]
b = []
for el in a:
    el = el.replace("_", "")
    if el:
        b.append(el)

print(f"{b=}")


# 8. Bereiningen der Liste von Steuerzeichen und x (schwer)
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente
von Whitespace und Steuerzeichen. Entferne alle x aus den Strings.
strip()
replace("x", "y")


result = ["halt", "and", "catch", "fire"]
"""
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]
result = []

for el in a:
    el = el.strip().replace("x", "")
    result.append(el)

print(result)
