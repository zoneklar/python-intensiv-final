"""
Aufgabe:
Erstelle eine Klasse Vector, die eine Klassen-Methode implementiert soll.

# Gegeben:

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y




# Gesucht:

die Klassen-Methode heisst from_dict und erstellt ein Vector-Objekt
auf Basis eines Dict in der Form:

d = {
    "x_point": 2,
    "y_point": 10,
}

oder

d = {
    "y_point": 11,
    "x_point": 3,
}

(Beachte, dass die Reihenfolge der Keys in dem Dict unterschiedlich sein kann!)

Zudem soll die Klasse die __repr__() - Methode implementieren

>>> v2 = Vector.from_dict(d)
>>> print(v2)
Vector(x=3, y=11)
>>> print(type(v2))
<class '__main__.Vector'>

"""

from __future__ import annotations


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_dict(cls, d: dict) -> Vector:
        d = {name.replace("_point", ""): value for name, value in d.items()}
        return cls(**d)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Only Vector instances can be added")

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


if __name__ == "__main__":
    v1 = Vector(x=10, y=30)
    print(v1)

    d = {
        "y_point": 10,
        "x_point": 4,
    }

    v2 = Vector.from_dict(d)
    print(v2)
    print(type(v2))

    d = {
        "x_point": 2,
        "y_point": 10,
    }

    v3 = Vector.from_dict(d)
    print(v3)

    # Vektoraddition
    v4 = v1 + v2
    print(v4)
