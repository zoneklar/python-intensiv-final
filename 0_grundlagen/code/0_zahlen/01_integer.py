"""
Python Integer und arithmetische Operatoren

In Python werden Ganzzahlen als Integer bezeichnet und durch den Datentyp
`int` repräsentiert. Arithmetische Operatoren erlauben mathematische
Berechnungen wie Addition, Subtraktion, Multiplikation und Division.
Hierbei sind auch fortgeschrittene Operatoren wie Modulo oder
Exponentialrechnung verfügbar.

Besonderheiten:
- Integer in Python haben keine feste Größenbeschränkung, sondern nur
  eine Speichergrenze durch die verfügbare Hardware.
- Division mit `/` erzeugt immer einen Fließkommawert (float), selbst
  wenn das Ergebnis mathematisch eine Ganzzahl ist.

Beispiele für arithmetische Operatoren:
- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
- Abrundsdivion Division: `//`
- Modulo: `%`
- Potenzierung: `**`

Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz zurück.
- `max()`: Gibt den größten Wert einer Sequenz zurück.
"""

x = 42  # dynamische Typsierung

distance_b = 1
distance_a = 3

distance_total = distance_a + distance_b

print(type(distance_total))  # <class 'int'>
print(int("111111101101", 2))  # 4077

# Int hat keine Größenbegrenzung
grenzenlos = 238749832732873273283274098327498327832708327320984798327409832709832740983273287324908732402374823704
print(grenzenlos + 1)

# Division erzeugt immer ein Float
a = 3 / 3  # 1.0
print("a:", a)

# Floor Division
x = 7
y = 3
print(x // y)  # 6

# Modulo
print(x % y)  # 7 / 3

# Potenz
print(x**2)

# Summe erwartet ein Iterable
print("summe", sum([1, 2, 3]))

# min
print(min(1, 42, -2, 5))

# gibt den Tupel von // und %
print(divmod(7, 3))  # (2, 1)
