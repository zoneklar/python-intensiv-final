"""
Liste: Wichtige Methoden in Python

Listen sind eine der flexibelsten und am häufigsten verwendeten Datenstrukturen
in Python. Sie bieten eine Vielzahl von Methoden, um Elemente hinzuzufügen,
zu entfernen, zu suchen oder zu manipulieren.

Themenübersicht:
1. Hinzufügen von Elementen: `append()`, `extend()`, `insert()`
2. Entfernen von Elementen: `remove()`, `pop()`, `clear()`
3. Suchen und Zählen: `index()`, `count()`
4. Sortieren und Umkehren: `sort()`, `reverse()`
5. Kopieren von Listen: `copy()`
"""

# 1. Hinzufügen von Elementen
fruits = ["apple", "banana", "cherry"]
print(id(fruits))

fruits.append("birne")  # hängt ein Element an, inplace Operatrion
print(id(fruits))

print(id(["apple", "banana", "cherry"] + ["ananas"]))

# Extend hängt eine Liste von elemente nan
fruits.extend(["peach", "coconut"])

# hängt vor ein Element an (besser Datentyp dafür wäre die Deque)
fruits.insert(0, "schokolade")

el = fruits.pop()
print(f"{el=}")

# 4. Sortieren und Umkehren
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # inplace operation.
print(numbers)

# hat einen Rückgabewert, mit reverse kann das Ergebnis umgedreht werden.
numbers_sorted = sorted(numbers, reverse=True)
print(numbers_sorted)

# umdrehen mit dem Slicing Operator, erzeugt neue Liste
numbers_reversed = numbers_sorted[::-1]
print(numbers_reversed)
