"""
Aufgabe-Decorator @timed(repeat=1)

• Misst die Ausführungszeit der Funktion `repeat`‑mal.
• Gibt den Rückgabewert unverändert zurück.
• Druckt: "<name> took X.XXX s (avg of N)".


Vorgaben:  import functools, time, statistics
Nutze functools.wraps, um den Namen der Funktion zu erhalten..

Beispiel:

    @timed(repeat=3)
    def slow(x):
        time.sleep(x)
        return x

    slow(0.1)   # → 0.1  und Meldung auf Stdout
"""
