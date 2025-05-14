"""
String Splitting in Python

Das Zerlegen von Strings (String Splitting) ist eine häufige Aufgabe in der
Datenverarbeitung. Python bietet verschiedene Methoden, um Strings anhand
von Trennzeichen oder festgelegten Mustern zu zerlegen.

Die Split-Operation erzeugt eine Liste

Themenübersicht:
1. Die Methode `split()`
2. Zerlegen mit benutzerdefinierten Trennzeichen
3. Zerlegen mit maximaler Anzahl von Teilen
5. Erweiterte Splitting-Optionen mit dem Modul `re`
"""

import re

csv_liste = "1,2,3,4,4"
csv = csv_liste.split(",")  # Default Trenner ist Leerzeichen
print(csv)

csv = csv_liste.split(",", maxsplit=1)  # Default Trenner ist Leerzeichen
print(csv)
