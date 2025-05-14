"""
Thema: getattr, setattr und delattr in Python

Python erlaubt den dynamischen Zugriff auf Attribute über die
eingebauten Funktionen:
- getattr(obj, "attr", [default]) → Gibt den Wert des Attributs zurück
- setattr(obj, "attr", value) → Setzt ein Attribut zur Laufzeit
- delattr(obj, "attr") → Löscht ein Attribut dynamisch

Diese Funktionen sind besonders hilfreich, wenn Attributnamen zur
Laufzeit als Strings vorliegen – z. B. bei Konfigurationen,
Deserialisierung, automatischer Validierung, usw.

Sie ermöglichen flexible und dynamische Manipulation von Objekten
und stehen im Kontrast zum festen Zugriff per Punktnotation
(obj.attr).
"""


class BananaTree:
    def __init__(self, bananas):
        self.rotten = 0
        self.bananas = bananas

    @property
    def bananas(self):
        return self._bananas

    @bananas.setter
    def bananas(self, amount):
        if amount > 0:
            self._bananas = amount

    @bananas.deleter
    def bananas(self):
        del self._bananas


b = BananaTree(56)
c = BananaTree(11)
