"""
Thema: Vererbung in der Praxis – Parser-Struktur für Dateiformate

In vielen Anwendungen müssen unterschiedliche Dateiformate analysiert
werden (z. B. JSON, CSV, XML). Dabei folgt die Verarbeitung oft einem
ähnlichen Schema: Datei einlesen, parsen, in ein gemeinsames Format
überführen.

Durch Vererbung kann man eine gemeinsame Basisklasse Parser definieren,
die das Grundgerüst vorgibt, und spezifische Parserklassen für jedes
Format ableiten.
"""

from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).parent
