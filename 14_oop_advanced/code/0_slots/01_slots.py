"""
Thema: __slots__ – Speicher sparen bei vielen Instanzen

Mit dem Attribut __slots__ kann man in Klassen festlegen, welche
Attribute erlaubt sind. Dadurch wird verhindert, dass ein dynamisches
__dict__ für jedes Objekt angelegt wird – was Speicher spart.

Vorteile:
- Weniger Speicherverbrauch bei vielen Instanzen
- Schnellere Attributzuweisungen (leicht messbar)
- Kann unbeabsichtigte Attribut-Erweiterungen verhindern

Einschränkungen:
- Kein __dict__ → keine dynamische Erweiterung zur Laufzeit
- Kein __weakref__ (außer explizit angegeben)

__slots__ ist sinnvoll bei großen Datenklassen oder vielen Objekten,
z. B. in Simulationen, Parsern, oder bei numerischen Datenmodellen.
"""
