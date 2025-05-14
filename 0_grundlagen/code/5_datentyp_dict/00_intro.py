"""
Einführung in den Datentyp Dictionary in Python

Ein Dictionary (oder kurz `dict`) ist eine Sammlung von Schlüssel-Wert-Paaren.
Jeder Schlüssel (Key) ist eindeutig und dient als Index, um einen Wert (Value)
zu speichern und abzurufen. Dictionaries sind veränderlich, d. h.,
Schlüssel-Wert-Paare können hinzugefügt, geändert oder entfernt werden.

Themenübersicht:
1. Erstellung und Initialisierung von Dictionaries
2. Zugriff auf Werte und Schlüssel
3. Hinzufügen, Ändern und Entfernen von Einträgen
4. Iteration über Dictionaries
5. Wichtige Methoden
"""

d = {
    "a": 42,
}

en_de = {
    "cat": "katze",
    "dog": "Hund",
    "horse": "Pferd",
}

# Zugriff via Klammer-Operator
print(en_de["cat"])

# Fehler bei Zugriff KeyError
# print(en_de["fish"])

# prüfen, ob ein Key im Dict vorhanden ist.
if "fish" in en_de:
    print(en_de["fish"])
else:
    print("fish ist nicht enthalten")

# Alternative
animal = en_de.get("fish", "Default-Tier")
print(f"{animal=}")


# Dicts verbinden
a = {"a": 3, "b": 5}
b = {"b": 42}

# ab Python 3.10
c = a | b  # vorsicht, Key b wurde überschrieben
print(c)

# vor Python 3.10
c = {**a, **b}
print(c)

# Iteration über ein Dict: es wird über die keys Iteriert
for key in en_de:
    print(key)


for value in en_de.values():
    print(value)

# items() liefert "Liste" von Key-Value Päärchen
for key, value in en_de.items():
    print(key, value)
