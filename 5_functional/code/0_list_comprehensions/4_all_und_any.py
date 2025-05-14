"""
Die Funktionen `all()` und `any()` sind eingebaute Funktionen in Python
zur Auswertung von Wahrheitswerten in iterierbaren Objekten (z. B. Listen,
Tupel oder Generatoren).

- `all(iterierbar)` gibt True zurück, wenn **alle** Elemente True sind.
- `any(iterierbar)` gibt True zurück, wenn **mindestens eines** True ist.

Beide Funktionen arbeiten effizient mit Generator Expressions, da die
Auswertung bei Bedarf abbricht (Short-Circuit Evaluation).

Dieses Skript zeigt die Grundlagen und reale Anwendungsbeispiele für
`all()` und `any()`.
"""

# all(): Sind alle Bedingungen erfüllt?
werte = [2, 4, 6, 8]
symstem_var = 3
long_var_name = 334


# bei längeren Bedingungen, die mit and verbunden werden,
# bietet sich all an. All  ist wahr, wenn alle Elemente von
# all wahr sind
if all(
    [
        symstem_var > 3,
        symstem_var < long_var_name,
        long_var_name == symstem_var,
    ],
):
    print("das ist wahr")


# gleiches gilt für any.
# any(): Ist mindestens eine Bedingung erfüllt?
if any([3 > 1, 3 < 1, symstem_var == 3]):
    print("any ist wahr")
