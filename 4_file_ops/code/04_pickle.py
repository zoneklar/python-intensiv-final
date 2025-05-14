"""
Das Thema dieser Datei ist die Verwendung des `pickle`-Moduls in Python.

- `pickle` ist ein Modul zur Serialisierung und Deserialisierung von Python-Objekten.
- Serialisierung bedeutet, ein Python-Objekt in ein Byte-Format umzuwandeln,
  das gespeichert oder übertragen werden kann.
- Deserialisierung ist der Prozess, dieses Byte-Format wieder in ein Python-Objekt
  zurückzuverwandeln.
"""

import pickle
from pathlib import Path

# 1. Einführung in das `pickle`-Modul
# Beispiel-Daten
data = {
    "name": "Anna",
    "age": 30,
    "languages": ["Deutsch", "Englisch"],
    "is_employed": True,
}

# 2. Serialisierung: Schreiben von Objekten in eine Datei
file_path = Path(__file__).parent / "data.pkl"
