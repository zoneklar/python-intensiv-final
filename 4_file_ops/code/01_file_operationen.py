"""
Das Thema dieser Datei ist die Arbeit mit Dateioperationen in Python.

- Python bietet zahlreiche Funktionen, um Dateien zu lesen, zu schreiben
  und zu manipulieren.
- Wir betrachten grundlegende Dateioperationen wie das Erstellen, Lesen,
  Schreiben und Löschen von Dateien.
"""

# 1. Datei erstellen und schreiben
from pathlib import Path


file_name = Path(__file__).parent / "test.txt"

# nicht machen, da nicht garantiert ist, dass das File geschlossen wird
# f = open(file_name, mode="r", encoding="utf-8")
# f.read()   # lädt ganze Datei ein
# f.close()

# besser einen Kontext-Manager. Schließt die Datei garantiert und automatisch
# LeseMmous
with open(file_name, mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# Falls eine Datei nicht existiert, wird sie anglegt im Schreibmodus
# Schreibmodus
with open(Path(__file__).parent / "example.txt", mode="w", encoding="utf-8") as f:
    f.write("hallo test\n")  # f.write macht kein Newline
    f.write("hallo test2")


# Falls eine Datei nicht existiert, wird sie anglegt im append
# Appendmodus
with open(Path(__file__).parent / "example2.txt", mode="w") as f:
    f.write("hallo test\n")
    f.write("hallo test2")


# Zeilenweise Auslesen einer (großen) Datei.
oceans_name = Path(__file__).parent / "data/oceans.txt"
with open(oceans_name, mode="r", encoding="utf-8") as f:
    # über die Datei iterieren
    for line in f:
        print(line, end="")  # Zeilenumbrach nach print verhindern
