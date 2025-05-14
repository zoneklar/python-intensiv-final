"""
Die Funktion `filter()` in Python wird verwendet, um Elemente aus einem
iterierbaren Objekt zu filtern, basierend auf einer Funktion, die
wahrheitswertige Rückgaben liefert.

Syntax: filter(funktion, iterable)

Dabei wird jedes Element des iterierbaren Objekts an die Funktion
übergeben. Nur jene Elemente, für die die Funktion `True` zurückgibt,
werden im Ergebnis enthalten sein.

Der Rückgabewert ist ein Iterator. Um die Ergebnisse zu sehen,
muss man ihn z. B. in eine Liste umwandeln.

Typische Einsatzgebiete:
- Herausfiltern ungerader/gerader Zahlen
- Entfernen leerer oder ungültiger Werte
- Prüfung auf Bedingungen in Datenreihen

Vergleich:
filter(predicate, seq) ist äquivalent zu:
[el for el in seq if predicate(el)]

Dieses Skript zeigt grundlegende und praxisnahe Anwendungen von `filter()`.
"""


# Funktion, die prüft, ob eine Zahl größer als 100 ist
def greater_than_100(x) -> bool:
    return x > 100


# Liste mit Zahlen
zahlen = [1, 111, 2, 222, 3, 333]

# als Filter
print(list(filter(greater_than_100, zahlen)))

# als List Comprehension
print([el for el in zahlen if greater_than_100(el)])
