"""
In Python lassen sich Funktionen verschachteln (Nested Functions).

global keyword
"""

global_x = 42


def outer():
    outer_x = 3

    # die globale Variable global_x in outer schreibar machen (global machen)
    # bad practise! kein global nutzen,
    global global_x
    global_x += 3

    def better_inner(value):
        value += 1
        return value

    def inner():
        # nonlocal ist das global für den nested Scope
        # bad practise!
        nonlocal outer_x
        outer_x += 1
        print("ich bin inner, outer_x:", outer_x)

    inner()
    # Besser explizit mit Übergabe und Rückgabewert
    outer_x = better_inner(outer_x)
    print(f"Outer x in outer: {outer_x}")


outer()
print(f"{global_x=}")

# Dunder File: absoluter Pfad im Dateisystem. Built in Variable
print(__file__)
