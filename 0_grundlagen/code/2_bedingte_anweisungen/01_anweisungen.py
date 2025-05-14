"""
Kontrollstrukturen: if, else und elif in Python

Die Kontrollstrukturen `if`, `else` und `elif` ermöglichen in Python
bedingte Anweisungen. Sie erlauben es, Code abhängig von bestimmten
Bedingungen auszuführen.

Themenübersicht:
1. Die if-Anweisung
2. Die else-Anweisung
3. Die elif-Anweisung
4. Verschachtelte Bedingungen
5. Kurzformen (Ternary Operator)
6. Die pass-Anweisung
"""

long_string = """
hallo
welt
"""

a = 3
b = 65

if a > b:
    # pass bedeutet weitergehen, ist nur da, um keinen Einrückungsfehler
    # zu erzeugen
    pass


if b <= a:
    print("b ist kleiner gleich a")
elif b > 3:
    print("Elif Zweig")
else:
    print("else Zweig")


# Ternärer Operator
# a = a > b ? 3 : 78
a = 42 if a > b else 78
print(f"{a=}")
