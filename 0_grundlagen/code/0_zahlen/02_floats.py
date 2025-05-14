"""
Fließkommazahlen in Python: Stellen, Präzision und Probleme

Fließkommazahlen werden in Python mit dem Typ `float` dargestellt. Dieser
ermöglicht die Darstellung von Dezimalzahlen und unterstützt auch die
wissenschaftliche Notation. Allerdings gibt es wichtige Aspekte und
Einschränkungen, die beachtet werden sollten.
Er enstpricht dem C Datentyp double (64 bit), und ist in IEEE 754 spezifiziert.

Themenübersicht:
1. Eigenschaften von Fließkommazahlen
2. Probleme mit der Präzision
3. Rundung und Formatierung
4. Wissenschaftliche Notation
5. Typkonvertierungen: int, float, str
"""

import decimal

x = 1.1  # dynamische Typisierung

y = 1.224232324234324324
y_rounded = round(y, 4)
print(y_rounded)

# Rundung
# half to even (scientific rounding)
print(round(4.5))  # 4
print(round(3.5))  # 4
print(round(2.5))  # 2

# float nach int
x = int(1.9)  # Truncacte
print(x)

# Typ-Konvertierung von String nach float
value = "1"
value = float(value)

print(f"{10 / 3: .20f}")
print(f"{10 / 6: .20f}")
