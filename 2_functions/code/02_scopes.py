"""
Funktionen und Scopes in Python

Der Scope (Gültigkeitsbereich) bestimmt, wo Variablen definiert und verwendet
werden können. Python unterscheidet zwischen lokalem, globalem und
nicht-lokalem Scope. Das Verständnis von Scopes ist wichtig, um Funktionen
effektiv zu nutzen und Fehler durch unerwartete Variablenänderungen zu
vermeiden.

Themenübersicht:
1. Lokaler Scope
2. Globaler Scope
3. Die `global`-Anweisung
"""

from pprint import pprint

# Konstanten sind groß geschrieben, können aber verändert werden
# ist nur eine konvention
MAX_VALUE = 42
x = 3  # liegt im globalen Scope
y = 42
names = ["bob", "grumpy"]


def fn(a):
    """Testfunktion zum Zeigen der Scopes."""
    x = 7  # liegt diese Variable im lokalen Scope
    print(f"{MAX_VALUE=}")
    print(f"Lokals von fn: {locals()}")  # zeigt alle lokalen Variablen von fn

    # UnboundLocalError: cannot access local variable 'y' where it is not associated with a value
    # Bei Zuweisung wird erst eine Varialbe y ohne wert angelegt. MIt dieser kann nicht gerechnet
    # werden.
    # y = y + 1  # 43
    # Lösung, anderen Namen wählen
    my_y = y + 1

    # Verändlichen Datentypen erweitern (Seiteneffenkt)
    names.append("Alice")

    return a


def print_names(names):
    """Eine Liste wird per Referenz übergeben.
    ein unverändlicher Datentype wie int wird per value übergeben.
    """
    for name in names:
        print(name)
    print(names.pop())  # verändert names aus dem globalen Scope


fn(3)
print(f"X aus dem globalen Scope: {x}")  # 3

# Funktion globals(): Zeigt alle globalen Variablen und Bezeichner
# pprint(globals())
print(f"{names=}")
print_names(names)  # Liste names wurde in print_names verändert (Seiteneffekt)
