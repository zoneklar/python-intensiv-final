"""
schwer

Black Jack (17 und 4)

Vereinfachte Version von 17 und 4, in der der Spieler nur gegen sich selbst
spielt.
Spieler zieht solange Karten, bis er entscheidet, das Spiel zu beenden oder sein Kartenwert > 21 ist.
Wenn der Gesamtwert seiner Karten <= 21 und > 17, hat der Spieler gewonnen.
Anderenfalls hat er verloren.

1. Erstelle dazu ein Karten-Deck (Kreuzprdukt aus values und colors)
2. Nutzde die shuffle - Methode aus dem random Modul, um das dEck zu mischen
3. Das Spiel beginnt, es werden initial zwei Karten gezogen.

Kartenwerte
2, 3, 4, 5, 6, 7, 8, 9, 10
Bube, Dame, König: 10
Ass 11

shuffle methode aus dem random Modul
es werden 4 Kartensätze in einem Spiel genutzt



Beispiel 1:
---------------
Du hast folgende Karte gezogen: Kreuz Fünf
Du hast folgende Karte gezogen: Herz Drei
Aktuelle Punkte: 8
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Herz Acht
Aktuelle Punkte: 16
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Karo Bube
Aktuelle Punkte: 26
Du hast verloren!
Game Over

Beispiel 2:
-----------------
Du hast folgende Karte gezogen: Pik Zwei
Du hast folgende Karte gezogen: Pik Acht
Aktuelle Punkte: 10
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Karo Sieben
Aktuelle Punkte: 17
Willst du eine weitere Karte ziehen? J/N: N
Du hast verloren, GAME OVER!
"""

import random

names = [
    "Zwei",
    "Drei",
    "Vier",
    "Fünf",
    "Sechs",
    "Sieben",
    "Acht",
    "Neun",
    "Zehn",
    "Bube",
    "Dame",
    "König",
]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
colors = ["Pik", "Herz", "Kreuz", "Karo"]

MAX_VALUE = 21

deck = []
for _ in range(4):
    for color in colors:
        for name, number in zip(names, values):
            deck.append((color, number, name))

# Karten mischen
random.shuffle(deck)
print(deck)

# GAME START
player_value = 0

# Spieler zieht zwei Karten
card_1 = deck.pop()
card_2 = deck.pop()

print(f"Du hast folgende Karte gezogen: {card_1[0]}", card_1[2])
print(f"Du hast folgende Karte gezogen: {card_2[0]}", card_2[2])

player_value = card_1[1] + card_2[1]

while True:
    print("Aktuelle Punkte:", player_value)

    if player_value > MAX_VALUE:
        print("Du hast verloren!")
        print("Game Over")
        break

    # user pick game
    user_input = input("Willst du eine weitere Karte ziehen? J/N: ")
    if user_input == "J":
        card = deck.pop()
        print(f"Du hast folgende Karte gezogen: {card[0]} {card[2]}")

        player_value = player_value + card[1]
    else:
        if player_value > 17:
            print("Du hast gewonnen!")
        else:
            print("Du hast verloren, GAME OVER!")
        break
