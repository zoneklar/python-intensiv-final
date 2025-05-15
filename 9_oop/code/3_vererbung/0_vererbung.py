"""
Thema: Vererbung in Python – Klassen erweitern und wiederverwenden

Vererbung erlaubt es, eine Klasse (Basisklasse) zu definieren, deren
Eigenschaften und Methoden von anderen Klassen (Subklassen) übernommen
werden.

Die Syntax lautet: class Unterklasse(Oberklasse):
Dabei kann man geerbte Methoden überschreiben oder erweitern.

Python unterstützt auch Mehrfachvererbung, was vorsichtig verwendet
werden sollte.

Vererbung fördert Code-Wiederverwendung und hilft bei der Modellierung
von „ist-ein“-Beziehungen.
"""


class Hero:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class MarvelHero(Hero):
    def __init__(self, name: str, points: int):
        super().__init__(name)
        self.points = points


superman = MarvelHero(name="Superman", points=34)
print(vars(superman))  # {'name': 'Superman', 'points': 34}
print(superman)  # __str__ von Hero
