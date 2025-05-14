"""
Fehler erheben
"""

import math


class EllipseError(Exception):
    pass


def ellipse_area(a: float, b: float) -> float:
    """Berechne die Fläche der Ellipse."""
    if b > a:
        raise EllipseError(
            """
            Kleine Halbachse darf nicht größer
            sein als große Halbachse
            """
        )

    return math.pi * a * b


try:
    ellipse_area(13, 4)
except ValueError:
    pass
except EllipseError as e:
    print(f"print {e}")

######################################################
d = {"a": 3}
try:
    d["b"]
except KeyError as e:
    # Fehler re-raisen
    raise
