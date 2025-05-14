"""
Thema: frozen=True in @dataclass – Unveränderliche Objekte erzeugen

Mit dem Parameter `frozen=True` bei der Dekoration einer Datenklasse
(`@dataclass`) wird die Klasse **unveränderlich** (engl. *immutable*).

Das bedeutet:
- Nach der Instanziierung können keine Attribute mehr verändert werden.
- Jeder Versuch, ein Attribut neu zu setzen oder zu überschreiben,
  führt zu einem `FrozenInstanceError`.

Beispiel:

    @dataclass(frozen=True)
    class Point:
        x: int
        y: int

    p = Point(1, 2)
    p.x = 10  # ❌ ergibt FrozenInstanceError

Dies ist besonders nützlich:
- wenn Objekte als Dictionary-Keys oder in Sets verwendet werden sollen
- zur Fehlervermeidung bei versehentlichen Änderungen
- bei funktionalem Programmierstil

Hinweis: frozen=True erzeugt automatisch eine `__hash__`-Methode,
wenn möglich – z. B. wenn alle Felder selbst hashbar sind.
"""
