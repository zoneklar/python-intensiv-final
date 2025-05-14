"""
*-Operator
"""

# Entpacken von Sequenzen
name = "Alice"

# Entpacken von Sequenzen, *args unbestimmte anzahl
a, *args = name
print(a, args)  # args sind eine Liste


def fn(a, b, *args):
    print(args)  # Tuple


def process_data(id: int, name: str, city: str):
    print(id, name, city)


user_liste = [
    (1, "Bob", "hamburg", 34),
    (2, "Alice", "Köln", 24),
]

d = {"id": 3, "name": "Grumpy", "city": "Berlin"}

for user in user_liste:
    # process_data(id=user[0], name=user[1], city=user[2])
    id, name, city, *args = user
    process_data(id, name, city)

    # Entpacken bei Funktionsaufruf, mit Sternchenoperator
    process_data(*user[:-1])

    # Entpacken eines Dicts bei funktionsaufruf
    process_data(**d)  # process_data(id=3, name="Grumpy", city="Berlin")


# # Iteation über Keys
# for element in d:
#     print("=>", element)
