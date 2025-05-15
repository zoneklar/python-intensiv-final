"""
Read only property example
"""


class Wizard:
    """Beispielklasse für Properties."""

    def __init__(self, name: str, magic_points: int):
        self.name = name
        self._magic_points = magic_points  # _name => non public

    @property
    def magic_points(self):
        return self._magic_points


w = Wizard("Gandalf", 200)
print(w.magic_points)
# w.magic_points = 34

# del w.magic_points

print(vars(w))
