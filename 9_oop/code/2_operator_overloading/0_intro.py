"""
Dunder Methoden
"""

from __future__ import annotations


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Addition ist nur zwischen Vektoren erlaubt.")

        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Vector) -> bool:
        if not isinstance(other, Vector):
            raise TypeError("Addition ist nur zwischen Vektoren erlaubt.")

        return self.x == other.x and self.y == other.y


v1 = Vector(2, 4)
v2 = Vector(2, 4)

v3 = v1 + v2
print(v1 == v2)


# IS vs ==
3 == 3
print("3 is 3:", 20**50 is 20**50)
print("3 is 3:", 3 is 3)

print("hallo welt" is "hallo welt")

x = ""

# Prüfen, ob x als falsch evaluiert wird
if not x:
    print("x ist falsch")

# Prüfen, ob ein Objekt expliziti None
if x is None:
    print("x ist None")
