"""
mittel

(Mustererzeugung). Schreiben Sie ein Programm, das mit Hilfe von
Schleifen das folgende Muster erzeugt (mit einem while-loop):

Eingabe: 5

*
**
***
****
*****
****
***
**
*

Eingabe: 3

*
**
***
**
*

"""

max_stars = int(input("Enter the max number of stars: "))

# mit ternäry operator
stars, count = 1, 1
while stars:
    print("*" * stars)
    stars = (stars - 1) if count >= max_stars else (stars + 1)
    count += 1

# Lösung mit zwei for loops
for i in range(1, max_stars + 1):
    print("*" * i)

for i in range(max_stars - 1, 0, -1):
    print("*" * i)
