"""
Eine Closure ist ein Konzept aus der funktionalen Programmierung.
Wenn eine Funktion, die freie Variablen verwendet, den Scope verlässt,
in dem diese vereinbart sind (meistens, weil sie selbst von einer Funktion
zurückgegeben wird), und wird dieser Scope abgeräumt, so wären diese
freien Variablen ab diesem Zeitpunkt undefiniert.

Um dem zu begegnen, setzt der Compiler bei der Rückgabe eine neue Struktur
zusammen. Sie besteht aus dieser Funktion und sämtlichen von ihr
verwendeten freien Variablen. Diese Struktur heißt Closure.

Ein Closure entsteht, wenn:
1. Eine Funktion innerhalb einer anderen definiert ist,
2. Die innere Funktion eine Variable der äußeren Funktion verwendet,
3. Die äußere Funktion eine Referenz auf die innere Funktion zurückgibt.

Closures ermöglichen das Erzeugen spezialisierter Funktionen zur
Laufzeit und werden oft für Konfiguration, Kapselung und in
funktionalen Programmiertechniken verwendet.

Real-World-Beispiel: Ein Rabatt-Generator, der je nach eingegebenem
Rabattprozentsatz eine angepasste Preisfunktion erzeugt.
"""

from typing import Callable


def outer(x: int) -> Callable:
    def inner() -> None:
        print(x)

    return inner


fn = outer(3)
# print(fn)
fn()  # 3


##################################################
def rabatt_generator(rabatt: int) -> Callable:
    def berechne_rabatt(preis) -> float:
        return preis * (1 - rabatt / 100)

    return berechne_rabatt


# Rabatt Generator als Funktion erstellen und
# dann die Preise übergeben
zwanzig_prozent_rabatt = rabatt_generator(20)
print(zwanzig_prozent_rabatt(100))
