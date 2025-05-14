"""
Modul-Docstring

Beschreibung des Moduls

Funktions-Docstrings:

- jede nicht selbst erklärende Funktion sollte einen Docstring haben.
- <= 72 Zeichen lang
- Wird genutzt für automatisierte Erstellung von Dokumentationen bzw. im
- python hilfestystem
"""


def fn(a, b):
    """Summary Line: Berechne Summe von a und b."""
    return a + b


def google_fn(a, b):
    """
    Summary Line eines Google Docstring Formats.

    Args:
        a: int Seite a
        b: int Seite b

    Returns:
        int, Summe von a und b

    Raises:
        Value Error if a < 0
    """
    return a + b


help(fn)

google_fn
