"""
Generator Expressions ähneln List Comprehensions, erzeugen aber keine
vollständige Liste im Speicher. Stattdessen geben sie einen Iterator
zurück, der die Werte bei Bedarf (lazy evaluation) erzeugt.

Ein Iterator ist ein Objekt, das mit der Funktion `next()` den nächsten
Wert liefert. Sobald alle Werte verbraucht sind, ist der Iterator
erschöpft. Generatoren sind besonders speichereffizient bei großen
Datenmengen, da sie nicht alles auf einmal im Speicher halten.

In diesem Skript zeigen wir den Unterschied zwischen Generator Expressions
und List Comprehensions, insbesondere beim Speicherverbrauch.
"""

import os
import sys
import psutil

current_process = psutil.Process(os.getpid())
print("Current Memory:", current_process.memory_info().rss / 1024**2)


# List Comprehension: Erzeugt sofort eine komplette Liste im Speicher
liste = [x**2 for x in range(1_000_000)]

print("Current Memory:", current_process.memory_info().rss / 1024**2)

# Generator Expression erzeugt ein Generator-Objekt
gen_liste = (x**2 for x in range(10_000))

print("Current Memory:", current_process.memory_info().rss / 1024**2)
# print(next(gen_liste))
# print(next(gen_liste))


# Bei Funktionsaufruf ohne [] ist der Inhalt des Aufrufs
# ein Iterator
numbers = [1, 3, 4, 5]
result = sum(number**2 for number in numbers)  # Generator-Objekt
print(result)
