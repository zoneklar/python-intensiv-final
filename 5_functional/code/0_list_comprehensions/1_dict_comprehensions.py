"""
Dict Comprehensions sind ähnlich wie List Comprehensions, aber sie
werden verwendet, um Dictionaries auf elegante und kompakte Weise zu
erstellen. Dabei werden Schlüssel-Wert-Paare direkt erzeugt.

Dieses Skript zeigt grundlegende Anwendungen von Dict Comprehensions.
"""

# Klassisches Erstellen eines Dictionaries mit einer Schleife
quadrate = {}
for i in range(6):
    quadrate[i] = i**2
print(quadrate)

# im Ausdruck steht ein key-value Paar
quadrate = {i: i**2 for i in range(6)}
