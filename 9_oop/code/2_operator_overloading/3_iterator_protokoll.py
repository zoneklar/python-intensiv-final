"""
Thema: Das Iterator-Protokoll in Python

Das Iterator-Protokoll beschreibt, wie Objekte in Python iterierbar
gemacht werden können. Ein Objekt gilt als Iterator, wenn es:

1. Die Methode __iter__() besitzt, die das Objekt selbst zurückgibt.
2. Die Methode __next__() implementiert, die das nächste Element
   zurückgibt oder StopIteration auslöst, wenn keine Elemente mehr da sind.

Iteratoren ermöglichen die Nutzung in for-Schleifen, Generatoren,
List-Comprehensions und allen anderen iterierbaren Kontexten.

Dieses Protokoll ist zentral für die Arbeit mit Sequenzen und Streams.
"""

from __future__ import annotations


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Course:
    def __init__(self, name):
        self.name = name
        self.members = []
        self._counter = 0

    def add(self, member: Person) -> None:
        self.members.append(member)

    def __iter__(self) -> Course:
        return self

    def __next__(self) -> Person:
        """Iterator Protokoll."""
        try:
            val = self.members[self._counter]

        except IndexError:
            raise StopIteration()

        self._counter += 1
        return val


if __name__ == "__main__":
    bob = Person("bob")
    alice = Person("Alice")

    course = Course("Python Intensiv")
    course.add(bob)
    course.add(alice)

    for member in course:
        print("=>", member)
