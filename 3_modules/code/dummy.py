"""
Modul dummy

Modul für das Arbeiten mit dummy-Funktionen.

Kontakt: Tim Zufall, tel. 23 298392
"""

print("Dummy: ", __name__)  # dunder name


def dummy(a: str, b: str) -> None:
    """Dummy Funktion zur Vorführungszwecken."""
    print(a, b)


if __name__ == "__main__":
    dummy(3, 3)
    print("hallo test")
