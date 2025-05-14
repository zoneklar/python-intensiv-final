# 8. Lese die Datei worldcities.csv mit dem CSV - Reader ein,
# sortiere die Einträge nach city_ascii und speichere sie in einer
# neuen Daten worldcities_sorted.csv ab.
# Schreibe dazu die Funktion load_cities, sort_cities_by_ascii_name und
# save_cities mit den dazugehörigen typehints.

# 1.b) Länder-Filter
# Erweitere die Aufgabe um einen Länder-Filter: es sollen nur Einträge
# in die neue Datei kommen, die einem eingegebenen Land entsprechen (zb. India)

# einfache Lösung ohne List-Comprehension und DictReader

import csv
from pathlib import Path


def load_cities(filename: str, country=None) -> tuple[list, list]:
    """Load Cities from CSV File and return list."""
    city_rows = []
    with open(Path(__file__).parent / filename, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)  # Rückt den Iterator eins weiter
        for row in reader:
            # Country Filter
            if country and isinstance(country, str):
                if row[4].lower() == country.lower():
                    city_rows.append(row)
                continue

            city_rows.append(row)
    return city_rows, header


def sort_cities_by_ascii_name(city_rows: list) -> list:
    """Sort cities by column ascii_name."""
    return sorted(city_rows, key=lambda e: e[1])


def save_cities_to_file(filename: str, city_rows: list, header: list) -> None:
    """Save rows to file."""
    with open(Path(__file__).parent / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        writer.writerows(city_rows)


def main():
    FILE_IN = "worldcities.csv"
    FILE_OUT = "worldcities_sorted_germany.csv"
    city_rows, header = load_cities(FILE_IN, country="Germany")
    sorted_cities = sort_cities_by_ascii_name(city_rows)
    print(sorted_cities)
    save_cities_to_file(FILE_OUT, sorted_cities, header)


main()
