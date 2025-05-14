"""
Wichtige Dictionary-Methoden in Python

Dictionaries sind eine flexible Datenstruktur in Python und bieten eine Vielzahl
von Methoden, um Schlüssel-Wert-Paare hinzuzufügen, zu entfernen, zu durchsuchen
und zu manipulieren.

Themenübersicht:
1. Zugriffsmethoden: `get()`,
2. Aktualisierung und Zusammenführung: `update()`
3. Entfernen von Einträgen: `pop()`, `popitem()`, `clear()`
4. Schlüssel und Werte: `keys()`, `values()`, `items()`
5. Kopieren und Standardwerte: `copy()`, `fromkeys()`
"""

# 1. Zugriffsmethoden
user = {"name": "Alice", "age": 30}
print(user.get("name"))

user.update({"city": "Köln"})
print(user)

# pop
print(user.pop("name"))

user.update({"permissions": [1, 2, 3, 4]})
print(user)

d = {}
# Liste als Key geht nicht, da eine Liste nicht hashable ist
# d[[1, 2]] = 1
d[(1, 2)] = 134  # als Tuple geht, da unverändlich
