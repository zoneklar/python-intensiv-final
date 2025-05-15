"""
Thema: Kapselung in Python mit @property

In Python wird Kapselung nicht über strikte Zugriffsmodifikatoren
(gibt es nicht wie in Java), sondern über Konventionen und das
@property-Decorator realisiert.

Mit @property kann man Methoden wie Attribute verwenden. Damit ist
es möglich, den Zugriff auf interne Variablen zu kontrollieren,
ohne die äußere Schnittstelle zu verändern.

Typisches Anwendungsbeispiel:
- Private Variable _name
- Getter mit @property
- Setter mit @<name>.setter

So lässt sich Logik beim Lesen und Schreiben von Attributen
unterbringen, ohne dass der Benutzer eine Methode aufrufen muss.
"""


class Wizard:
    """Beispielklasse für Properties."""

    def __init__(self, name: str, magic_points: int):
        self.name = name
        self.magic_points = magic_points  # hier wird der Setter aufgerufen

    @property
    def magic_points(self) -> int:
        """Magic Points getter"""
        return self._magic_points

    @magic_points.setter
    def magic_points(self, points) -> None:
        """Magic Points setter"""
        if points < 0:
            raise ValueError("Negative Magiepunkte sind nicht erlaubt")

        self._magic_points = points


w = Wizard(name="Gandalf", magic_points=100)
w.magic_points = 343  # regulärer Set Zugriff
print(w.magic_points)  # reguläre Get Zugriff

print(w.__dict__)  # Erzeugt ein Dict mit Attributwerten
print(vars(w))  # Erzeugt ein Dict mit Attributwerten (wie __dict__)
