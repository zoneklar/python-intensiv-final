"""
Thema: Das Iterator-Protokoll in Python

Das Iterator-Protokoll beschreibt, wie Objekte in Python iterierbar
gemacht werden können. Ein Objekt gilt als Iterator, wenn es:

1. Die Methode __iter__() besitzt, die das Objekt selbst zurückgibt.
2. Die Methode __next__() implementiert, die das nächste Element
   zurückgibt oder StopIteration auslöst, wenn keine Elemente mehr da sind.

Iteratoren ermöglichen die Nutzung in for-Schleifen, Generatoren,
List-Comprehensions und allen anderen iterierbaren Kontexten.

Dieses Protokoll ist zentral für die Arbeit mit Sequenzen und Streams.
"""
