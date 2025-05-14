"""
Set Comprehensions ermöglichen das Erzeugen von Mengen (Sets) auf
kompakte Weise. Sie ähneln List Comprehensions, liefern aber eine
ungeordnete Sammlung eindeutiger Elemente.

In diesem Beispiel werden Set Comprehensions anhand eines realen
Szenarios verwendet: Duplikate aus Daten entfernen und Filtern
von Zeichen in Texten.
"""

# Liste von Benutzereingaben mit Duplikaten
emails = [
    "max@sensei.com",
    "lara@cthullu.com",
    "max@peaches.com",
    "john@xanadoo.com",
    "lara@firefly.com",
    "laura@firefly.com",
]

# Beispiel: Nur Domains extrahieren und in ein Set speichern
domains = {email.split("@")[1] for email in emails}
print(domains)
