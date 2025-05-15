"""
Thema: __str__ und __repr__ in Python (Dunder-Methoden)

In Python gibt es spezielle Methoden, die mit doppelten Unterstrichen
beginnen und enden – sogenannte "dunder"-Methoden. Zwei wichtige davon
sind:

- __str__(self): Wird aufgerufen, wenn ein Objekt in einen String
  umgewandelt oder mit print() ausgegeben wird. Ziel: leserliche
  Darstellung für den Benutzer.

- __repr__(self): Wird aufgerufen, wenn die "repr()" Funktion genutzt
  wird oder ein Objekt in einer interaktiven Konsole angezeigt wird.
  Ziel: eine eindeutige, oft technische Darstellung, die im Idealfall
  wieder zu demselben Objekt führt (eval(repr(obj))).

Diese Datei zeigt den Unterschied beider Methoden mit praktischen
Beispielen.
"""


class Person:
    """Das hier beschreibt eine Persons."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        """String Repräsentation eines Personen-Objekts."""
        return self.first_name

    def __repr__(self) -> str:
        """Interne Repräsentation für Debugging, Logging, Testing."""
        return f"Person({self.first_name!r}, {self.last_name!r}, {self.age!r})"


bob = Person("bob", "Meyer", 34)
alice = Person("Alice", "Doe", 78)

bob.country = "Deutschland"  # schlechter Stil, Attribute nachträglich zufügen
print(bob.first_name)  # lesend
bob.first_name = "Bobby"  # schreibend

# print bob objekt
print("Bob Objekt: ", bob)  #  String-Repräsentation eines Bob Objekts
# print(dir(bob))
print("test")  # String-Repräsentation eines Strings

persons = [bob, alice]
print(persons)
