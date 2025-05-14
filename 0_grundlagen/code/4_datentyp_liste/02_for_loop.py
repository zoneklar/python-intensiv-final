"""
For-Schleifen in Python

Die for-Schleife ist eine der am häufigsten verwendeten Kontrollstrukturen
in Python. Sie wird verwendet, um über Sequenzen (wie Listen, Tupel oder Strings)
zu iterieren. Python bietet zusätzliche Funktionen wie `enumerate`, sowie
die Möglichkeit, Schleifen mit `break`, `continue` und `else` zu kontrollieren.

Themenübersicht:
1. Grundlagen der for-Schleife
2. Verwendung von `enumerate`
3. Steuerung der Schleife mit `break` und `continue`
4. Die `for-else`-Konstruktion
5. Filtern von Listen
"""

numbers = [1, 2, 43, 53]

# Iteration über eine Sammlung
for number in numbers:
    print(number)


students = ["Bob", "Alice", "Grumpy"]
grades = [1, 3, 2]

# klassische Variante mit Inkrement
i = 0
for name in students:
    print(grades[i], name)
    i += 1

# enumerate erzeugt einen Iterator von Index und Element
# Iteratoren müssen konsumiert werden, zb. Iteration oder list
print(list(enumerate(students)))

# pythonische Variante für das Iterieren mit Index
for index, namen in enumerate(students):
    print(index, namen)


# break: Schleifeabbruch
numbers = [1, 2, 3, 4, 6]
for number in numbers:
    if number == 3:
        print(3)
        break


# continue: Schleifen-Durchlauf abbrechen
for number in numbers:
    if number % 2 == 0:
        print(number)
        continue
    print(f"{number=}")


# for else

# klassisches Problem: Meldung "nicht gefunden" ausgeben
rabbits = ["fiver", "hazel", "bigwig"]

# Klassisch mit Flag
found = False
for rabbit in rabbits:
    if "fiverx" in rabbit:
        print("Fiver wurde gefunden")
        found = True

if not found:
    print("Fiver wurde nicht gefunden")

# --------------------------------------------------------------------------
# Pythonische Variante mit for-else:
for rabbit in rabbits:
    if "fiverx" in rabbit:
        print("Fiver wurde gefunden")
        break
else:
    # else wird ausgeführt, wenn for-loop nicht mit break
    # abgebrochen wurde
    print("Fiver wurde nicht gefunden")

# --------------------------------------------------------------------------
# Filtern einer Liste
# --------------------------------------------------------------------------
values = [2, 4, 6, 34, 2, 1]
values_new = []

for value in values:
    if value > 2 and value < 6:
        values_new.append(value)

print(values_new)

# --------------------------------------------------------------------------
# Range Funktion
# --------------------------------------------------------------------------

# von Index 2 bis 9 (10 ist exclusive)
for i in range(2, 10):
    print(i)

# mit Angabe von einem Argument beduetet von 0 bis 2
# Underscore: Variable wird nicht weiter genutzt
for _ in range(3):
    print("Hallo Welt")
