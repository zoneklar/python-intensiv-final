"""
Eine Funktion kann in Python wie jede andere
Variable behandelt werden kann. Funktionen sind sogenannte 'First-Class
Citizens'. Man kann sie einer Variablen zuweisen, als Argument
weitergeben oder als Rückgabewert verwenden.

"""

from pprint import pprint
from typing import Callable

x = 3  # Integer-Objekt


def take_function(f: Callable) -> None:
    f()
    return f


def fn():
    # Funktionsobjekt
    print("Hallo, ich bin FN")


pprint(globals())

print(dir(x))

# Eigenschaften des Funktionsobjekts
print(dir(fn))

# Aufruf mit Funktionsobjekt
f = take_function(fn)

# Name der Funktion
print(take_function.__name__)
