"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an.

- Der Name muss mindestens drei Zeichen lang sein
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock haben".
- Im Fehlerfall raise ValueError.

Implementiere auch __str__ und __repr__.

Teste mit folgenden Produkten:
products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern
    ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
    ("Za", 23.2, "in stock"),  # muss scheitern.
]
Nutze zum testen einen Loop und try-except
"""

class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit

    # Getter-Methode für name

    # Getter-Methode für preis

    # Getter-Methode für verfuegbarkeit

    # Setter-Methode für name

    # Setter-Methode für preis

    # Setter-Methode für verfuegbarkeit


if __name__ == "__main__":

    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
        ("Za", 23.2, "in stock"),  # muss scheitern.
    ]


