"""
Thema: Mixins in Python – Mehrfachvererbung gezielt nutzen

Ein Mixin ist eine Klasse, die **zusätzliche Funktionalität** liefert,
aber **nicht eigenständig instanziiert** wird. Sie wird verwendet, um
Fähigkeiten per Mehrfachvererbung modular zu anderen Klassen hinzuzufügen.

Eigenschaften von Mixins:
- Kein eigener Konstruktor (normalerweise kein __init__)
- Klein, fokussiert und wiederverwendbar
- Wird zusammen mit einer Hauptklasse geerbt

Typische Anwendungsbeispiele:
- LoggingMixin → bietet Logging-Funktion
- JsonSerializableMixin → bietet to_json()-Methode
- TimestampMixin → fügt Erstellungszeitpunkt hinzu

Mixins fördern saubere, modulare Architekturen – besonders in komplexeren
Systemen wie Web-Frameworks oder Datenmodellen.
"""
