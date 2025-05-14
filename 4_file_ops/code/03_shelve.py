"""
Das Thema dieser Datei ist die Verwendung des `shelve`-Moduls in Python.

- `shelve` ist ein Modul der Python-Standardbibliothek, das einfache
  persistente Speicherlösungen bietet.
- Es ermöglicht das Speichern von Python-Objekten in einer Datei
  mithilfe eines Dictionary-ähnlichen Interfaces.
- Die gespeicherten Daten werden automatisch serialisiert.
- Keys dürfen nur Strings sein, während die Werte beliebige Python-Objekte
  sein können.

Die gespeicherten Daten werden intern von einem Datenbankmodul (wie dbm)
verwaltet. Dadurch entstehen beim Speichern mehrere Dateien

Die Daten liegen nach Speicherung in drei Dateien vor:
- basename.db: Enthält die Daten.
- basename.dat: Enthält die serialisierten Daten.
- basename.bak: Enthält eine Sicherungskopie der Datenbank.
- basename.dir: Enthält die Indexdatei.

Je nach Betriebssystem und DBM-Backend können auch weniger oder andere Dateien
entstehen. Beispielsweise erzeugt dbm.dumb nur .dat und .dir.

Aufgrund dieser Tatsache ist shelve nicht platformunabhängig und sollte
nur genutzt werden, wenn die Datenbankdateien auf dem gleichen System
genutzt werden.

Alternativen zu `shelve` sind:
- pickle: Einfaches Modul zum Serialisieren von Python-Objekten.
- json: Modul zum Serialisieren von Python-Objekten in JSON-Dateien.
"""

import shelve
from pathlib import Path
