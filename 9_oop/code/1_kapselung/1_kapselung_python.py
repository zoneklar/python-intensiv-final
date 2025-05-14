"""
Thema: Kapselung in Python mit @property

In Python wird Kapselung nicht über strikte Zugriffsmodifikatoren
(gibt es nicht wie in Java), sondern über Konventionen und das
@property-Decorator realisiert.

Mit @property kann man Methoden wie Attribute verwenden. Damit ist
es möglich, den Zugriff auf interne Variablen zu kontrollieren,
ohne die äußere Schnittstelle zu verändern.

Typisches Anwendungsbeispiel:
- Private Variable _name
- Getter mit @property
- Setter mit @<name>.setter

So lässt sich Logik beim Lesen und Schreiben von Attributen
unterbringen, ohne dass der Benutzer eine Methode aufrufen muss.
"""
