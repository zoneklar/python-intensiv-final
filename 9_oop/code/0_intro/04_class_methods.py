"""
Thema: Klassenmethoden in Python – @classmethod

Klassenmethoden sind Methoden, die auf die Klasse selbst statt auf
eine Instanz zugreifen. Sie werden mit dem Decorator @classmethod
gekennzeichnet und erhalten cls (statt self) als ersten Parameter.

Damit können sie auf Klassendaten zugreifen oder alternative
Konstruktoren bereitstellen.

Typische Anwendungsfälle:
- Factory-Methoden
- Zugriff auf oder Veränderung von Klassenattributen
- Klassenspezifische Initialisierungen

Aufruf: über die Klasse oder eine Instanz möglich (Klasse.methode()).
"""

from __future__ import annotations

# entweder Self aus typing oder from __future__ annotations nutzen
# wenn man den Datentyp der Klasse in der eingenen Klasse verwenden will.
# from typing import Self


class Robot:

    counter = 0  # Klassenvariable

    def __init__(self, id_: int, type_: str):
        self.id_ = id_
        self.type_ = type_
        print(type(id_))

        Robot.counter += 1  # Inkrement von Klassenattribut

    @classmethod
    def from_string(cls, robot_string: str) -> Robot:
        id_, type_ = robot_string.split(";")
        return cls(int(id_), type_)


robot = Robot(id_=23432, type_="MA3")
print(Robot.counter)  # Lesende Zugriff auf Klassenvariable via Klasse
print(robot.counter)  # Lesende Zugriff auf Klassenvariable via Object
robot.counter = 938493  # neues Attribut counter für Objekt counter!!!

# Erzeuge aus einer Liste von Strings eine Liste von Robot-Objects
robots = [
    "234334;T3",
    "242424;T53",
]

robot_objects = [Robot.from_string(robot_string) for robot_string in robots]
print(robot_objects)
