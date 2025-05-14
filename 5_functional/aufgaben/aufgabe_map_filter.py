# **Aufgabe 2: Verwenden von `filter()`, um gerade Zahlen zu finden**
numbers = [1, 2, 3, 4, 5]
# Verwende map(), um die Zahlen zu quadrieren
squared_numbers = list(map(lambda x: x**2, numbers))

# Gib die ursprüngliche Liste und die quadrierten Zahlen aus
print("Ursprüngliche Liste:", numbers)
print("Quadrierte Zahlen:", squared_numbers)


# 2. Aufgabe Verwenden von `filter()`, um gerade Zahlen zu finden**
numbers = [10, 15, 20, 25, 30]

# Verwende filter(), um gerade Zahlen zu finden
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Gib die ursprüngliche Liste und die geraden Zahlen aus
print("Ursprüngliche Liste:", numbers)
print("Gerade Zahlen:", even_numbers)


numbers = [2, 3, 4, 5, 6]

# Verwende map(), um das Quadrat der geraden Zahlen zu berechnen
squared_even_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Gib die ursprüngliche Liste, die Liste der geraden Zahlen und die quadrierten geraden Zahlen aus
print("Ursprüngliche Liste:", numbers)
print("Quadrierte gerade Zahlen:", squared_even_numbers)
