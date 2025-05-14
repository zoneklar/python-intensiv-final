"""
Datentyp `bool` in Python

Der Datentyp `bool` repräsentiert in Python die zwei Wahrheitswerte `True`
und `False`. Er wird häufig in Kontrollstrukturen, Vergleichen und logischen
Operationen verwendet.

Themenübersicht:
1. Grundlagen des Datentyps `bool`
2. Erzeugung von Booleschen Werten
3. Vergleichsoperatoren
4. Logische Operationen
5. Konvertierung in und von `bool`
6. Falsy-Werte in Python
"""

a = False
b = True

# Logische Operatoren
# and or not
print("a and b:", a and b)  # False
print("a or b:", a or b)  # True
print("not b:", not b)  # True

# Arithmetische Vergleichsoperatoren
x = 3
y = 5
print("==:", x == y)
print(">=:", x >= y)
print("<:", x < y)

# In-Operator (Membership-Operator) und der Identitätsoperator
print("a" in "aaaa")
print(1 in [1, 2, 3, 4])

apples = ["green", "red"]
print("Apples:", bool(apples))

# Beispiele für falsy-Werte:
print("Bool von 0:", bool(0))  # False
print("Bool von 0.0:", bool(0.0))  # False
print("Bool von leerem Tuple:", bool(()))  # False
print("Bool von leerer Liste:", bool([]))  # False
print("Bool von leerem Dictionary:", bool({}))  # False
print("Bool von None:", bool(None))  # False
