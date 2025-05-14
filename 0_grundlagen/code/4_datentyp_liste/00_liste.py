"""
Einführung in den Datentyp Liste in Python

Listen sind eine grundlegende Datenstruktur in Python. Sie erlauben das
Speichern und Verarbeiten von mehreren Elementen in einer geordneten Sequenz.
Listen sind veränderlich, d. h., ihre Elemente können nach der Erstellung
geändert werden.

Themenübersicht:
1. Erstellung und Initialisierung von Listen
2. Wichtige Operationen und Methoden
3. Vergleich von Listen
4. Überprüfung von Listeninhalten
5. Prüfung auf Leere und Existenz
"""

from copy import deepcopy

names = ["Bob", "Alice", "Grumpy"]  # Liste mit 3 String-Objekten
print(names[0])
print(names[:2])
print(f"{hex(id(names))}")  # ID ist eindeutig

copy_names = names  # Referenz kopieren
copy_names[0] = "Bobby"
print("Names:", names)

# Identitätsoperator (wenn beide die selbe ID haben)
if copy_names is names:
    print("copy_names IS names")


# Listen konkatenieren
new_names = names + ["Waldo"]
print(new_names)


# Liste kopieren
copy_names_2 = names.copy()  # flache Kopie
copy_names_2 = names[::]  # flache Kopie mit Slicing Notation
copy_names_3 = deepcopy(names)  # echte, tiefe Kopie
