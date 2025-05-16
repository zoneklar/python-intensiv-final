"""
Ohne Name-Mangling wird die falsche Methode aufgerufen

- public: alles ist public per default
- non-public: _x = 3 bzw. _baz()
- __x = Name Mangling, verhindert, dass in einer geerbten Klasse die falsche Methode aufgerufen wird
"""


class A:
    def foo(self):
        self.__x = 1
        self.__connect()  # __connect von A
        self.bar()  # bar von B

    def __connect(self):
        print("ICH BIN connect von A")

    def bar(self):
        print("bar von a")


class B(A):
    def __connect(self):
        print("ICH BIN connect von B")

    def bar(self):
        print("bar von b")


# a = A()
# a.foo()

b = B()
b.foo()
