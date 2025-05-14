"""
Thema: Klassenvariablen in Python

Klassenvariablen sind Variablen, die auf Klassenebene definiert
werden und von allen Instanzen gemeinsam genutzt werden.

Im Gegensatz zu Instanzvariablen (self.var), die nur für ein
bestimmtes Objekt gelten, sind Klassenvariablen für **alle Objekte
der Klasse gleich** – sofern sie nicht auf Instanzebene überschrieben
werden.

Typischerweise werden sie verwendet für:
- Zähler über alle Instanzen
- Konstante Klasseneigenschaften
- Gemeinsame Konfigurationswerte

Klassenvariablen werden direkt in der Klasse definiert, nicht im
__init__-Konstruktor.

Diese Datei zeigt, wie Klassenvariablen definiert, verwendet und
überschrieben werden können.
"""
