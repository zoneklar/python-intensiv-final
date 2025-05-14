"""
Lambda-Ausdrücke in Python sind anonyme Funktionen – das heißt,
sie haben keinen Namen. Sie werden mit dem Schlüsselwort `lambda`
definiert und dienen der kompakten Darstellung einfacher Funktionen.

Syntax: lambda argumente: ausdruck

Lambda-Funktionen können beliebig viele Argumente enthalten, aber nur
einen einzigen Ausdruck, dessen Ergebnis automatisch zurückgegeben wird.
Sie sind besonders nützlich, wenn man eine Funktion nur kurzzeitig
und einmalig benötigt, ohne ihr einen Namen zu geben.

Dieses Skript erklärt die Syntax und zeigt grundlegende Beispiele,
ohne den Einsatz in anderen Funktionen wie `map()` oder `sorted()`.
"""

c = 42

f = lambda a, b: a + b  # erstellt ein Funktionsobjekt / Funktionsreferenz
f(2, 4)


# klassisch
def fn(a, b):
    return a + b


fn(3, 2)
