"""
Das Thema dieser Datei ist das `os`-Modul in Python.

- Das `os`-Modul bietet Funktionen zur Interaktion mit dem Betriebssystem.
- Es ermöglicht Dateiverwaltung, Prozesssteuerung und Zugriff auf Systeminformationen.
- In diesem Dokument werden die wichtigsten Funktionen des `os`-Moduls
  detailliert erklärt und durch Beispiele veranschaulicht.
"""

import os
import subprocess


# Subprozess:
cmd = "git --version"

# Kommando auf Shell ausführen
returned_value = subprocess.call(cmd, shell=True)
print("Fehlercode:", returned_value)


# Rückgabewert von date
returned_value = subprocess.check_output("ls")
print(list(returned_value))
x = returned_value.decode(encoding="utf-8")
print("Ergebnis von date:", x)
