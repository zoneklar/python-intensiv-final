"""
Parametrisierte Decorators erlauben es, einem Decorator Argumente zu
übergeben. Das ist besonders nützlich, wenn das Verhalten des Decorators
abhängig von konfigurierbaren Werten sein soll – etwa bei Validierungen,
Log-Leveln oder bedingtem Ausführen.

Ein parametrisierter Decorator besteht aus drei verschachtelten Funktionen:
1. Eine äußere Funktion, die die Parameter des Decorators entgegennimmt.
2. Eine innere Decorator-Funktion, die die zu dekorierende Funktion annimmt.
3. Ein Wrapper, der die Logik ausführt.

Dieses Skript zeigt reale Anwendungsbeispiele für Decorators mit Parametern,
zum Beispiel zur Wertevalidierung und Zugriffskontrolle.
"""


# Beispiel 1: Validierung von Zahlenwerten mit einem parameterisierten Decorator


# @validate_range(1, 10)
def quadrat(x):
    return x * x
