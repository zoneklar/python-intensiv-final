"""
Ein Decorator (dt. Dekorierer) ist ein Konstrukt in Python, mit dem
Funktionen oder Methoden um zusätzliche Funktionalität erweitert werden
können, ohne ihren eigentlichen Code zu verändern.

Ein Decorator ist eine Funktion, die eine andere Funktion als Argument
nimmt und eine neue Funktion zurückgibt.

Einsatzmöglichkeiten:
- Logging
- Zeitmessung
- Zugriffskontrolle
- Vor- und Nachbedingungen

Syntax:
@decorator_name
def funktion():
    ...

Dies ist gleichbedeutend mit:
funktion = decorator_name(funktion)

Dieses Skript zeigt den grundlegenden Aufbau eines einfachen Decorators.
"""

import time
from functools import lru_cache


def timer(fn):
    """Ein Timer Decorator."""

    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"Die Ausführung hat {end - start:.2f} Sekunden gedauert.")
        return result

    return inner


def dummy(fn):
    """Ein Decorator, der vor und nach dem Funktionsaufruf printed."""

    def inner(*args, **kwargs):
        print("VOR dem Funktionsaufruf")
        result = fn(*args, **kwargs)
        print("NACH dem Funktionsaufruf")
        return result

    return inner


@dummy
@timer
def fn(a, b):
    time.sleep(2)
    return a + b


# fn = dummy(fn)  in anderen sprachen gibts kein @ symbol
result = fn(3, 3)
print(result)
