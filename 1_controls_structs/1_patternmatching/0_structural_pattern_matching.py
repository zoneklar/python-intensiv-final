"""
Ab Python 3.10 kann anstelle des fehlenden Switch-Cases
das Structural Pattern Matching verwendet werden.
Pattern Matching ist allerdings sehr viel mächtiger als das herkömmliche
Switch-Case.

Schema:
match expression:
    case pattern1: # do something
    case pattern2: # do something else
"""

# Oldschool: Bedingte Verarbeitung mit if/elif/else
weekday = 1
if weekday == 1:
    weekday_name = "Monday"
elif weekday == 2:
    weekday_name = "Tuesday"
else:
    weekday_name = "undefined"

print(weekday_name)

# Pattern Matching: Vereinfachung durch match/case
match weekday:
    case 1:
        weekday_name = "Monday"
    case 2:
        weekday_name = "Tuesday"
    case _:
        weekday_name = "undefined"


# Pattern Matching mit Listen
name = "Captain Jean Luc"
match name.split():  # ["Captain", "Jean", "Luc"]
    case ["_Captain", "Jean", "Luc"] as captain_name:
        print(captain_name)
    case [a, "Jean", b]:
        print("a, b:", a, b)
    case ["Captain", *args]:
        print("args:", args)
    case first_name, middle_name, last_name:
        print(first_name, middle_name, last_name)


# Pattern Matching mit benutzerdefinierten Zeichenfolgen


# Pattern Matching mit Dictionaries
orders = [
    {"type": "book", "title": "1984", "author": "George Orwell"},
    {"type": "electronics", "product": "smartphone", "brand": "Acme"},
    {"type": "grocery", "items": ["milk", "bread"], "quantities": [3, 4]},
]
for order in orders:
    match order:
        case {"type": "book", "title": title, "author": author}:
            print(title, author)
        case _:
            print("typ nicht gefunden")


command = "get shovel"
command = "go north"

match command.split():
    case ["north"] | ["go", "north"]:
        print("user is going north")
    case ["get", obj] | ["pick", obj] | ["pick", obj, "up"]:
        print("User is picking up", obj)
    case _:
        print("Dieses Kommando ist unbekannt")


# Aufgabe: Gegeben ist ein Punkt (1, 4)
# match auf Nullpunkt (0,0)
# match auf Punkt auf der X-Achse (0, y)
# match auf Punkt auf der y-Achse (x, 0)
# allgemeiner Punkt (x, y)
# kein match: Das ist kein Punkt im Koordinatensystem

point = 0, 0

match point:
    case (0, 0):
        print("nullpunkt")
    case (0, y):
        print(f"auf der x-Achse, y: {y=}")
    case (x, 0):
        print(f"auf der y-Achse, x: {x=}")
    case (x, y):
        print(f"{x=} {y=}")
    case _:
        print("Kein punkt")
