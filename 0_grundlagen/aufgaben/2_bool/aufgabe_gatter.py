A = True
B = True

""" (schwer)
Es sollen Logik-Gatter implementiert werden.
nutze dazu die Variablen A und B, wie in Zeile 1-2 definiert.
Verändere die Werte der Variablen A und B, um die verschiedenen
Gatter zu testen.
"""

"""
Beispiel: das UND-Gatter
"""
if A and B:
    print("A and B ist true")


"""
Implementiere das XOR-Gatter
# XOR Gatter: XOR ist wahr, wenn exklusiv A oder B wahr ist
https://de.wikipedia.org/wiki/Exklusiv-Oder-Gatter

#
A   B   A XOR B
0   0   0
0   1   1
1   0   1
1   1   0

"""
print("Exclusive OR: ---------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a=} {b=}")
        if a is not b:
            print(f"{a=} XOR {b=}")
print("---------------------------")

"""
Ein NAND-Gatter gibt am Ausgang 0 aus, wenn alle Eingänge 1 sind.
In allen anderen Fällen, d. h., wenn mindestens ein Eingang 0 ist,
wird eine 1 ausgegeben.
https://de.wikipedia.org/wiki/NAND-Gatter

A   B   A NAND B
0   0   1
0   1   1
1   0   1
1   1   0
"""
print("NAND: ---------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a=} {b=}")
        if not (a and b):
            print(f"{a=} NAND {b=}")
print("---------------------------")

"""
Implementiere das NOR-Gatter mit zwei Eingängen
Ein NOR-Gatter gibt am Ausgang 1 aus, wenn alle Eingänge 0 sind. In allen anderen Fällen,
d. h. wenn mindestens ein Eingang 1 ist, wird eine 0 ausgegeben.
https://de.wikipedia.org/wiki/NOR-Gatter

A   B   A NOR B
0   0   1
0   1   0
1   0   0
1   1   0
"""
print("NOR ---------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a=} {b=}")
        if not (a or b):
            print(f"{a=} NOR {b=}")
print("---------------------------")

"""
Implementiere das XNOR-Gatter (exklusive not or) mit zwei Eingängen
Ein XNOR-Gatter gibt am Ausgang 1 aus, wenn alle Eingänge 0 oder 1 sind.
https://de.wikipedia.org/wiki/XNOR-Gatter

A   B   A XNOR B
0   0   1
0   1   0
1   0   0
1   1   1
"""
print("XNOR ---------------------------")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a=} {b=}")
        if (a and b) or not (a or b):
            print(f"{a=} XNOR {b=}")
print("---------------------------")
