"""
Per defualt sind alle Attribute und Methoden public.
Mit einem (oder zwei) Underscores sind die Attribute und Methoden non-public
"""


class Human:
    def __init__(self, name: str, age: int):
        self._name = name  # non - public
        self.age = age  # public
        self._initialize()  # interner Zugriff auf non-public methode

    def __str__(self) -> str:
        return self._name

    def __len__(self) -> int:
        return 42

    def _initialize(self):
        print("init")


bob = Human("bob", 33)
bob._name = "Bobby"
print(vars(bob))

print(bob)  # => str(bob)
print(bob.__str__())  # geht, aber ist nicht empfohlen
bob._initialize()  # Zugriff auf non-public methode wird nicht empfohlen

print(len(bob))  # ruft __len__
