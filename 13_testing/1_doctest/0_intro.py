"""
Beispielmodul mit einfacher Summenfunktion und doctest-Beispielen.

Der Zweck von doctest liegt heute vorrangig im dokumentarischen
Nutzen: Die Beispiele im Docstring zeigen, wie die Funktion
verwendet wird, und können automatisch getestet werden.

alternativ: python -m doctest .\0_intro.py
"""

import doctest


def summe(a: float, b: float) -> float:
    """
    Addiere zwei Float-Werte.

    >>> summe(2, 4)
    6
    >>> summe(0, -1)
    -1
    """
    return a + b


if __name__ == "__main__":
    doctest.testmod()
