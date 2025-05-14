"""
In Python kann die eingebaute Funktion `sorted()` verwendet werden,
um Listen und andere iterierbare Objekte zu sortieren. Dabei kann man
mit dem Parameter `key` eine Funktion übergeben, die bestimmt, nach
welchem Kriterium sortiert werden soll.

Oft wird dafür eine Lambda-Funktion verwendet, da sie es erlaubt,
einfach und direkt ein Sortierkriterium zu definieren, ohne eine
separate Funktion schreiben zu müssen.

Beispiel:
sorted(liste, key=lambda x: x[1])  # Sortiert nach dem zweiten Element

Python verwendet eine stabile Sortierung. Das bedeutet, dass Elemente
mit gleichem Sortierwert ihre ursprüngliche Reihenfolge beibehalten.
Dies ist nützlich, wenn man mehrfach sortieren möchte – z. B. erst
nach Nachnamen, dann nach Vornamen.

Dieses Skript zeigt, wie man `lambda` mit `sorted()` nutzt und erklärt
anhand von Beispielen, was stabile Sortierung bedeutet.
"""

# unsortierte Liste
liste = [3, 5, 1, 9, 1]
print(sorted(liste))  # aufsteigend
print(sorted(liste, reverse=True))  # absteigend

# unsortierte ASCII Buchstaben
chars = ["a", "f", "c", "d", "e"]
print(sorted(chars))


def to_lower(e):
    return e.lower()


# Großbuchstaben kommen vor Kleinbuchsten (A=65, a=97)
chars = ["a", "f", "b", "B", "A", "d", "e", "ü", "u", "z"]
print(sorted(chars, key=lambda e: e.lower()))
print(sorted(chars, key=to_lower))

# AUFGABE
# Sortiere nach der Zahl
# Ergebnis:
# ids sorted:  ['idx1', 'id2', 'id3', 'id4', 'id5', 'idy5']
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
print(sorted(ids, key=lambda e: int(e[-1])))


# SNACKS 1
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}
print(sorted(snacks.items()))


# nach Preis des Produkts aufsteigend sortiert:
# [1.50, 3.30, 5.20]
print(sorted(snacks.items(), key=lambda e: e[1]))

d = dict(sorted(snacks.items(), key=lambda e: e[1]))
print(d)


# SNACKS 2 (nach Preis sortieren)
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}

snacks_sorted = sorted(snacks.items(), key=lambda e: e[1]["price"])
print(snacks_sorted)


# Stabile Sortierung Beispiel
# tuple alice und Eve haben gleiche ordnung. Stabile
# Sortierung sorgt dafür, dass Alice und Eve gleiche Ordnung
# haben nach Sortierung
people = [("Alice", 25), ("Bob", 30), ("Eve", 25), ("David", 28)]
print(sorted(people, key=lambda e: e[1]))
