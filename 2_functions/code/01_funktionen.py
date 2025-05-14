"""
Einführung in Funktionen in Python

Funktionen sind ein zentrales Konzept in Python, das es ermöglicht, Code
wiederverwendbar und modular zu gestalten. Mit Funktionen können Aufgaben
kapsuliert, Parameter verarbeitet und Ergebnisse zurückgegeben werden.

Themenübersicht:
1. Definition und Aufruf von Funktionen
2. Parameter und Argumente
3. Rückgabewerte
"""


def function_name():
    print("hallo funktion")


def summe(a, b):
    # Best Practice: Funktionsrückgabewert sollte immer
    # der selbe sein.
    # if a > 5:
    #     return "hallo"

    return a + b


print("summe:", summe("43", "3"))


# Default Rückgabewert ist None
x = function_name()


def say_hello(first_name, last_name):
    print(first_name, last_name)


say_hello("bob", "test")
