"""
Thema: __getitem__ und __setitem__ – Zugriff wie bei Listen und Dictionaries

Mit den Methoden __getitem__(self, key) und __setitem__(self, key, value)
kann man eigenen Klassen das Verhalten von Index- oder Schlüsselzugriff
verleihen – ähnlich wie bei Listen oder Dictionaries.

Damit lässt sich z. B. obj[key] lesen oder schreiben, anstatt Methoden
wie get(key) oder set(key, value) zu verwenden.

Dieses Konzept wird häufig in containerartigen Klassen, Datenstrukturen
und internen APIs verwendet.
"""
