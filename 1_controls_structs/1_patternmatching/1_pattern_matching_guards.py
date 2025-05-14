"""
Dieses Modul demonstriert die Verwendung von Pattern Matching
in Python 3.10+ mit sogenannten "Guards" (zusätzliche Bedingungen).

Pattern Matching erlaubt es, strukturierte Daten (wie Dicts, Listen oder Strings)
in Form von "Mustern" auszuwerten – ähnlich wie ein switch/case in anderen
Sprachen, aber deutlich mächtiger.

Guards sind optionale `if`-Klauseln, die nach dem Pattern geprüft werden
und zusätzliche Bedingungen an das Match stellen.

Dieses Modul zeigt:
- Pattern Matching mit einfachen Bedingungen
- Einsatz von Guards in case-Zweigen
- Beispiele mit Listen, Strings und Dictionaries
- Kombination mit APIs (GitHub-Beispiel)
"""

import requests

# ---------------------------------------------
# Beispiel 1: Namensabfrage mit Guard-Bedingungen
# ---------------------------------------------

harrypotter = ["Harry", "Hermione", "Ron"]
hhgtg = ["Arthur", "Ford", "Zaphod", "Trillian"]
name = input("Enter a name: ")

match name:
    case n if n in hhgtg:
        print(f"{n} ist ein Charakter aus Hitchkiker ....")
    case n if n in harrypotter:
        print(f"{n} ist ein Charakter aus Harry Potter ....")
    case _:
        print("unknown charakter")


# ---------------------------------------------
# Beispiel 2: Zugriff auf GitHub-Repositories mit Guards
# pip install requests
# ---------------------------------------------

response = requests.get("https://api.github.com/orgs/python/repos")
repositories = response.json()

for repo in repositories:
    match repo:
        # Dict Entpacken, name und stars raus-extrahieren und prüfen
        # ob stars > 1000.
        case {"name": name, "stargazers_count": stars} if stars > 1000:
            print(name, stars)


# ---------------------------------------------
# Aufgabe: Bücherliste
# ---------------------------------------------
"""
Gegeben ist eine Liste von Dictionaries mit Informationen zu Büchern:

books = [
    {"title": "Dune", "author": "Herbert", "pages": 412},
    {"title": "It", "author": "King", "pages": 1138},
    {"title": "Foundation", "author": "Asimov", "pages": 255},
    {"title": "Pet Sematary", "author": "King", "pages": 374},
    {"title": "Unbekanntes Werk"}  # fehlerhaftes Beispiel, Autor fehlt
]

Ziel:
- Gib alle Bücher von "King" mit mehr als 400 Seiten aus
- Kennzeichne Bücher mit weniger als 300 Seiten als Kurzroman
- Gib alle anderen Bücher mit Titel und Autor aus
- Gib bei unvollständigen Daten eine Warnung aus

Lösung:

Buch: Dune von Herbert
King-Roman mit Überlänge: It (1138 Seiten)
Kurzroman: Foundation von Asimov (255 Seiten)
Buch: Pet Sematary von King
⚠️ Unvollständige Angabe

"""

books = [
    {"title": "Dune", "author": "Herbert", "pages": 412},
    {"title": "It", "author": "King", "pages": 1138},
    {"title": "Foundation", "author": "Asimov", "pages": 255},
    {"title": "Pet Sematary", "author": "King", "pages": 374},
    {"title": "Unbekanntes Werk"},
]
