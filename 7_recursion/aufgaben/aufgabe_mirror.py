"""
Mini‑Aufgabe – Rekursives Spiegeln einer Zeichenkette

Schreibe die Funktion reverse_rec(text: str) -> str, die mithilfe
reiner Rekursion einen String rückwärts ausgibt.

Vorgaben
--------

1. Basisfall: Ein leerer String oder ein einzelnes Zeichen wird
   unverändert zurückgegeben.
2. Rekursionsschritt: Nimm das erste Zeichen und hänge es
   **hinten** an das Ergebnis des rekursiven Aufrufs mit dem Rest
   der Zeichenkette.

Beispiele
---------

    >>> reverse_rec("abc")
    'cba'

    >>> reverse_rec("Regeneration")
    'noitarenegeR'

Regeln
------

* Keine Schleifen, nur Rekursion
"""


def reverse_rec(text: str):
    """Rekursives Spiegeln eines Strings."""
    if len(text) <= 1:
        return text
    return reverse_rec(text[1:]) + text[0]


print(reverse_rec("hase"))
