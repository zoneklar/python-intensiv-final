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


class ExcelExporterMixin:
    def export_csv(self):
        print(self.data)


class JsonExporterMixin:
    def export_json(self):
        print(self.data)


class DataManager(ExcelExporterMixin, JsonExporterMixin):
    def __init__(self):
        self.data = []

    def add_data(self, number):
        self.data = number

    def get_data(self):
        return self.data


d = DataManager()
d.get_data()
d.export_csv()
