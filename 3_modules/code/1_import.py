import sys
import math
from pprint import pprint
from random import randint as randy  # alias für Funktion
import cmath as dummeszeug  # Alias als Modulname
import dummy
import random

# falls eine random.py im gleichen Verzeichnis liegt,
# wird nicht mehr das random der Standard-bibliothek importiert.
# random.randint(2, 4) erzeugt dann einen Fehler.

# in diesem Path sucht Python nach Modulen
pprint(sys.path)

# Dummy Funktion aus dem Dummy-Funktion nutzen
dummy.dummy("a", "b")

# import numpy as np

x = math.ceil(2.4)

# Alle geladenen Module ausgeben
for key, value in sys.modules.items():
    print(key, value)

print("*" * 50)
# via dem Zugriff auf das Modules-Dict lässt sich ein Modul referenzieren
# in der Praxis unüblich
copy_modul = sys.modules["pprint"]
print(dir(copy_modul))


# Module sind Modul-Objekte:
print(type(sys))  # <class 'module'>
