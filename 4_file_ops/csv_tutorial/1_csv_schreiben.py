from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent

persons = [
    [1, "Bob", "Dortmund"],
    [2, "Alice", "Bochum"],
    [3, "Grumpy", "Dublin"],
]

# Old School Reader nutzen
with open(BASE_DIR / "names.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    # Header schreiben
    writer.writerow(["ID", "Name", "Stadt"])

    # Daten schreiben aus Liste von Liste
    writer.writerows(persons)

persons_neu = [
    {"id": 3, "name": "Bob", "age": 3},
    {"id": 13, "name": "Alice", "age": 13},
    {"id": 33, "name": "Grumpy", "age": 23},
]

# Falls die Daten als Liste von Dicts vorliegen, bietet sich der
# Dict-Writer an
with open(BASE_DIR / "names2.csv", mode="w", encoding="utf-8", newline="") as f:
    fieldnames = persons_neu[0].keys()
    # Fieldnames ist eine liste der spalten
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # Auf Basis der fieldnames wird der header erstellt
    writer.writeheader()

    # persons_meu - Liste wegschreiben
    writer.writerows(persons_neu)
