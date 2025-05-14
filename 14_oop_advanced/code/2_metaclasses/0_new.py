"""
Thema: __new__ – Kontrolle über Objekterzeugung in Python

Die Methode __new__(cls, ...) ist ein spezieller Konstruktor, der
verwendet wird, um eine neue Instanz einer Klasse zu erzeugen, bevor
__init__ aufgerufen wird.

Im Gegensatz zu __init__, das nur ein bereits erzeugtes Objekt
initialisiert, ist __new__ dafür zuständig, dieses Objekt überhaupt
erst zu erstellen.

Typische Einsatzgebiete für __new__:
- Erzeugung von Singleton-Objekten
- Veränderung oder Austausch der Instanz beim Erzeugen
- Unterklassen von Immutable-Typen (z. B. int, str, tuple), bei denen
  Änderungen nur beim Erzeugen möglich sind

__new__ wird seltener benötigt, ist aber zentral, wenn man tiefen
Einfluss auf die Objekterzeugung nehmen möchte.
"""
