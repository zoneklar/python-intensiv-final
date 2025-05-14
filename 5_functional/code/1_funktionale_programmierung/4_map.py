"""
Die Funktion `map()` ist eine eingebaute Funktion in Python, mit der
man eine Funktion auf jedes Element eines iterierbaren Objekts anwenden
kann. Dabei entsteht ein Iterator mit den Ergebnissen der Anwendung.

Syntax: map(funktion, iterable)

Oft wird `map()` in Kombination mit `lambda` oder einer definierten
Funktion genutzt, um Transformationen effizient durchzuführen.

Wichtig: Der Rückgabewert von `map()` ist ein Iterator, keine Liste.
Will man das Ergebnis als Liste haben, muss man `list()` verwenden.

Reale Anwendungsbeispiele:
- Umrechnung von Einheiten (z. B. Celsius → Fahrenheit)
- Extraktion oder Transformation von Feldern in Datensätzen
- Normalisierung oder Formatierung von Strings

Dieses Skript zeigt den Einsatz von `map()` in mehreren realistischen
Szenarien.
"""

numbers = [1, 3, 4, 5]

# Liste der Quadrate
numbers_quad = [i**2 for i in numbers]

# map estellt ein Map-Objekt, das ist ein Iterator
numbers_map = map(lambda e: e**2, numbers)
print(list(numbers_map))

zahlen_liste = ["1", "34", "34"]
print(list(map(int, zahlen_liste)))


############################################################
# Beispiel mit zwei Iterables
# ##########################################################
def summe(a: int, b: int) -> int:
    return a + b


liste_a = [1, 3, 45, 23]
liste_b = [1, 3, 45, 23]

# Elemente aus a und b werden spaltenweise an summe übergeben
result = list(map(summe, liste_a, liste_b))
print(result)  # [2, 6, 90, 46]


########################################################
# 3 Listen jeweils Elementweise multiplizieren
########################################################
def multiply(a, b, c):
    return a * b * c


liste_a = [1, 3, 45, 23]
liste_b = [1, 3, 45, 23]
liste_c = [1, 3, 45, 23]

# mit map
result = list(map(multiply, liste_a, liste_b, liste_c))
print(result)

# als List Comprehension
result = [multiply(a, b, c) for a, b, c in zip(liste_a, liste_b, liste_c)]
print(result)
