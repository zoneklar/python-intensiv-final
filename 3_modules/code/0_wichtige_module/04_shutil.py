"""
Das Thema dieser Datei ist das `shutil`-Modul in Python.

- Das `shutil`-Modul bietet Funktionen zum Kopieren, Verschieben und Löschen
  von Dateien und Verzeichnissen sowie zum Arbeiten mit Archiven.
- Es wird häufig für Aufgaben im Zusammenhang mit der Dateiverwaltung verwendet.
"""

import shutil
from pathlib import Path

# --- Datei kopieren ---
source_file = Path(__file__).parent / "source.txt"
destination_file = Path(__file__).parent / "neu.txt"

# Verzeichnis kopieren mit copytree
# source_dir = Path(__file__).parent / "data"
# destination_dir = Path(__file__).parent / "backup"
# shutil.copytree(source_dir, destination_dir)

return_value = shutil.copy(source_file, destination_file)
print(return_value)
