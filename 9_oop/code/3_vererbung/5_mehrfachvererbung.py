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
