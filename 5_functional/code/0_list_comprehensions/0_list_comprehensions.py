"""
List Comprehensions sind eine kompakte Möglichkeit in Python, um
Listen zu erstellen. Sie kombinieren Schleifen und Bedingungen auf
elegante Weise und machen den Code oft kürzer und lesbarer.

Dieses Skript zeigt grundlegende Anwendungen von List Comprehensions.
"""

numbers = [1, 3, 4, 5]

# Aufgabe: neue Liste mit den Quadraten
new_numbers = []
for number in numbers:
    if number > 3:
        new_numbers.append(number**2)

print(new_numbers)

# eine erste List Comprehension
new_numbers = [number**2 for number in numbers if number > 3]
print(new_numbers)

# Aufgabe: Neue liste mit namen, die mit einem großen B anfangen
personen = ["Bernd", "Carsten", "Holger", "Mandy", "Celine", "Bob"]
new_persons = [person for person in personen if person.startswith("B")]
print(new_persons)

# Zwei Iterationen in der List Comprehension
cart_product = []
for i in range(3):
    for j in range(3):
        cart_product.append((i, j))

print(cart_product)

cart_product = [(i, j) for i in range(3) for j in range(3)]
print(cart_product)


# Sum der Quadrate
numbers = [1, 3, 4, 5]
result = sum(number**2 for number in numbers)
print(result)

# Funktionsaufruf ohne Rückgabewert (Bad Practise)
# [None, None, None]
x = [print(i) for i in range(3)]
print(x)
