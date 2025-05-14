"""
Einführung in den Datentyp `tuple` in Python

Ein Tuple (oder Tupel) ist eine geordnete, unveränderliche Sammlung von Elementen.
Im Gegensatz zu Listen können die Werte eines Tuples nach der Erstellung
nicht geändert werden. Tuples eignen sich gut für Daten, die unveränderlich
bleiben sollen.

Themenübersicht:
1. Erstellung und Eigenschaften von Tuples
2. Zugriff und Entpacken von Tuples
3. Verwendung von Tuples in Funktionen
4. Methoden und Anwendungen
"""

# Tupel mit zwei Elementen
x = 1, 2
y = (1, 2)

# Tupel mit einem Element
a = (1,)

# leeres Tuple
_ = ()

# Entpacken eines Rückgabe-Tuples einer Funktion
a, b = divmod(4, 2)

# Entpacken von Sequenzen in Variablen
fruits = ["apple", "cherry", "pineapple"]
a = fruits[0]

# pythonisch
a, b, c = fruits

# apple ist in a, der Rest geht in *rest
a, *rest = fruits
print(rest, type(rest))  # <class 'list'>

# nur vorne und hinten werden in a und b gepackt.
a, *rest, b = fruits

# Entpacken eines Strings in zwei Variablen
x, y = "ab"
