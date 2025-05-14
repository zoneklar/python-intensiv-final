"""
Einführung in den Datentyp `set` in Python

Ein Set (Menge) ist eine ungeordnete Sammlung von einzigartigen Elementen.
In Python wird der Datentyp `set` verwendet, um Mengen zu repräsentieren.
Er eignet sich besonders für Operationen wie Vereinigung, Schnittmenge oder
Unterschied.

Themenübersicht:
1. Erstellung und Eigenschaften von Sets
2. Hinzufügen und Entfernen von Elementen
3. Mengenoperationen: Vereinigung, Schnittmenge, Unterschied
4. Methoden und Anwendungen
"""

# 3. Mengenoperationen
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

leeres_dict = {}  # leeres Dict Literal

# leeres
leeres_set = set()

# Elemente hinzufügen
leeres_set.add("2")
leeres_set.add("32")
leeres_set.add("42")

# pop() nimmt ein willkürliches element aus dem Set
print(leeres_set.pop())
for element in leeres_set:
    print(element)

# von doppelten bereinigen
numbers = [1, 2, 2, 3, 4, 4]
numbers = list(set(numbers))
print(numbers)

set_c = {1, 2}
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Vereinigung (`union()` oder `|`)
menge = set_a | set_b
print("Vereinigungsmenge:", menge)

# Schnittmenge (`intersection()` oder `&`)
print("Schnittmenge: ", set_a & set_b)  # {3, 4}


# 4. Methoden und Anwendungen
# `issubset()`: Prüft, ob ein Set eine Teilmenge eines anderen ist.
if set_c < set_a:
    print("C ist echte Teilmenge von a")

if {1, 2, 3, 4} <= set_a:
    print("C ist Teilmenge von a")

# Set aus Tupeln
tuple_menge = set(
    [
        (
            1,
            2,
        ),
        (34, 53),
    ]
)
print(tuple_menge)

# man kann kein Dict mit einem Set als Key machen
# d = {tuple_menge: [1, 2, 3]}  unhashable type: 'set'

# FROZEN SET
###################################
frozen = frozenset([1, 2, 3])

# ein Frozenset kann man als key eines Dicts nutzen
d = {
    frozen: [1, 2, 3, 4],
}
