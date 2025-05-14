"""
Das pathlib-Modul in Python bietet eine objektorientierte
Möglichkeit, mit Dateipfaden zu arbeiten. Es erleichtert die
Verwaltung und Bearbeitung von Pfaden im Dateisystem.

Wichtige Funktionen und Eigenschaften:
- Path(): Erstellt ein Path-Objekt
- .parent: Gibt das übergeordnete Verzeichnis zurück
- .resolve(): Gibt den absoluten Pfad zurück
- .exists(): Prüft, ob der Pfad existiert
- .is_file(): Prüft, ob es sich um eine Datei handelt
- .is_dir(): Prüft, ob es sich um ein Verzeichnis handelt
- Path.cwd(): Gibt das aktuelle Arbeitsverzeichnis zurück
"""

from pathlib import Path


def is_file(file: Path) -> bool:
    """Prüfen, ob ein File ein File ist."""
    return file.is_file()


# Verzeichnis, in dem die aktuelle Datei liegt
DATA_DIR = Path(__file__).resolve().parent

print("aktuelles Arbeitsverzeichnis:", Path.cwd())

# Pfad zu der aktuellen Datei:
pfad = Path(__file__).resolve().parent
print(pfad)

# Test-Datei öffnen
f = open(DATA_DIR / "test.txt")
print(f.read())
f.close()

# Prüfen, ob es ein Directory ist
print(pfad.is_dir())
