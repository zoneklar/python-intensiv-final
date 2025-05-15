"""
Eine einfache Klasse, die ein Haus beschreibt.
"""


class House:
    def __init__(self, rooms: int, windows: int) -> None:
        """Das ist der Initializer."""
        print(rooms, windows)
        # print(id(self))


house = House(rooms=3, windows=23)  # house Objekt
print(id(house))


print(isinstance(house, House))  # auf eine Klasse prüfen
print(isinstance(2, (int, float)))  # mehrere Klassen prüfen

# Alles Auflisten, was Klasse house kann
print(dir(House))
