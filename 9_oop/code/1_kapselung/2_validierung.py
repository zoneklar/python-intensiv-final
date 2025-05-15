"""
Beispiel für die Validierung von Attributen in einer Klasse.

Klasse Point, Attribute sind x und y.
Business-Regel sagt: x und y müssen int sein

__str__ und __repr__ einbauen
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("x Muss int sein")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("y Muss int sein")
        self._y = value

    def __str__(self) -> str:
        return f"Punkt an: {self.x}/{self.y}"

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r})"


p = Point(-2, 4)
p2 = Point(3, 3)
print(p)

print([p, p2])
