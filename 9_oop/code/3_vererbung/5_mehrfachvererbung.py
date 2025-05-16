"""
Thema: Mehrfachvererbung in Python

In Python kann eine Klasse von mehreren Basisklassen gleichzeitig erben.
Das nennt man Mehrfachvererbung.

Syntax:
class Subklasse(BasisA, BasisB):
    ...

Dabei wird die sogenannte MRO (Method Resolution Order) verwendet, um
zu bestimmen, in welcher Reihenfolge nach Attributen und Methoden gesucht
wird. Die Reihenfolge folgt dem C3-Linearization-Algorithmus.

Mehrfachvererbung ist besonders nützlich bei sogenannten Mixins – also
kleinen Klassen, die Zusatzfunktionalität bieten, aber keine eigene
vollständige Hierarchie bilden.

Achtung: Bei unklarer Struktur kann Mehrfachvererbung den Code
unübersichtlich und fehleranfällig machen. Sie sollte gezielt und
strukturiert eingesetzt werden.
"""


class A:
    def __init__(self):
        print("init von A")

    def foo(self):
        print("foo von A")


class B(A):
    def __init__(self):
        print("init von B")
        super().__init__()

    def bar(self):
        print("bar von B")


class C:
    def __init__(self):
        print("init von C")

    def foo(self):
        print("foo von C")


class D(B, C, A):
    def __init__(self):
        print("Init von D")
        super().__init__()


d = D()
d.foo()

# Method Resolution Order: Wo wird nach foo() gesucht (Reihenfolge)
print(D.mro())
