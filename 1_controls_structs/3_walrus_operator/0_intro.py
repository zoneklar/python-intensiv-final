"""
Dieses Modul gibt eine Einführung in den sogenannten "Walrus Operator"
(:=), der mit Python 3.8 eingeführt wurde.

Er erlaubt es, einer Variablen **während** eines Ausdrucks einen Wert
zuzuweisen. Das reduziert doppelte Berechnungen und erlaubt kompaktere,
aber weiterhin lesbare Code-Konstruktionen.

Syntax:
    variable := Ausdruck

Typische Anwendungen:
- While-Schleifen mit Input oder IO
- Bedingungen, die gleichzeitig speichern und prüfen
- List Comprehensions mit Bedingungsspeicherung

Hinweis: Der Operator hat seine Grenzen und sollte nur dort verwendet
werden, wo er wirklich Klarheit schafft.

Hinweis: Der Walrus-Operator (:=) hat eine geringere Priorität als viele
andere Operatoren – daher sollte er in komplexeren Ausdrücken immer in
Klammern gesetzt werden, um unerwartetes Verhalten zu vermeiden.
"""

import re

# ---------------------------------------------
# Beispiel 1: klassische while-Schleife mit input()
# ---------------------------------------------
# so lange input eingeben, bis nichts mehr eingegeben wird.
while (name := input("bitte text eingeben: ")) != "":
    print(name)

# ---------------------------------------------
# Beispiel 2: Zwischenspeichern im If-Ausdruck
# ---------------------------------------------


def pruefe_email(email: str):
    """Prüfe, ob die E-Mail-Adresse gültig ist.

    Hinweis:
    Einfache Prüfung auf das Vorhandensein von '@' und '.'.
    """
    if match := re.match(r".+@.+\..+", email):
        print("gültige Emailadresse:", match[0])
    else:
        print("Keine gültige Addresse")


pruefe_email("user@example.com")
pruefe_email("keine.email")

# ---------------------------------------------
# Beispiel 3: List Comprehension mit Bedingungsergebnis
# ---------------------------------------------
werte = ["Apfel", "Banane", "Kiwi", ""]

# ---------------------------------------------
# Beispiel 4: mehrfach verwendetes Ergebnis vermeiden
# ---------------------------------------------


def quadrat_und_vergleich(x):
    """Vergleiche das Quadrat von x mit 100 und gib das Ergebnis aus."""
    if (q := x * x) > 100:
        print(f"Das Ergebnis ist {q=}")
    else:
        print(f"kleiner gleich 100 {q=}")


quadrat_und_vergleich(5)
quadrat_und_vergleich(11)

# ---------------------------------------------
# Beispiel 5: Stream-Verarbeitung mit Limit
# ---------------------------------------------


def lese_zeilen(dateipfad):
    """Lese Zeilen aus einer Datei und gebe sie aus."""
    pass


# lese_zeilen("beispiel.txt")  # Datei nötig


# ---------------------------------------------
# Beispiel 6: Iterator-Zwischenspeicherung
# ---------------------------------------------
iterator = iter([1, 2, 3, 4, 5])
