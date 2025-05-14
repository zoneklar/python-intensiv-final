"""
(mittel)

Über eine Usereingabe sind zwei Kreise k1 und k2 einzugeben. Diese Kreise sind
definiert durch Radius und Position im kart. Koordinatensystem.

Eingabe:
Position und Radius der beiden Kreise

Aufgabe:
Schneiden/Überlagern sich die Kreise?
"""

import math

k1 = input("Bitte gebe Kreis 1 ein (x y r): ").split()
k2 = input("Bitte gebe Kreis 2 ein (x y r): ").split()

x1, y1, r1 = float(k1[0]), float(k1[1]), float(k1[2])
x2, y2, r2 = float(k2[0]), float(k2[1]), float(k2[2])

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Alternative mit dist-Funktion des math-Moduls
distance = math.dist(
    (x1, y1),
    (x2, y2),
)

if r1 + r2 > distance:
    print("die Kreise k1 und k2 schneiden/überlagern sich!")
else:
    print("die Kreise k1 und k2 schneiden/überlagern sich nicht!")
