"""
Dieses Skript erklärt typische Komplexitätsprobleme bei rekursiven Funktionen
in Python – also Laufzeit- und Speicherprobleme, die bei tiefer oder
nicht optimal gesteuerter Rekursion entstehen können.

**Typische Probleme:**

1. **Exponentielles Wachstum:**
   - Wenn rekursive Aufrufe mehrfach verzweigen (z. B. naive Fibonacci-Implementierung),
     wächst die Anzahl der Aufrufe exponentiell.
   - Lösung: Zwischenspeichern mit Memoisierung oder Iteration bevorzugen.

2. **Stack Overflow / RecursionError:**
   - Python hat eine maximale Rekursionstiefe (`sys.getrecursionlimit()`),
     bei tiefer Rekursion (z. B. 10.000+ Schritte) bricht das Programm ab.
   - Lösung: Rekursionstiefe erhöhen oder iterative Umsetzung bevorzugen.

3. **Redundante Berechnungen:**
   - Ohne Caching werden gleiche Teilprobleme mehrfach gelöst.
   - Lösung: `functools.lru_cache` oder explizite Memoisierung verwenden.

4. **Ungeeignete Probleme für Rekursion:**
   - Lineare Abläufe (z. B. einfache Zählschleifen) sind mit Iteration klarer,
     effizienter und leichter zu debuggen.

Dieses Skript demonstriert problematische und effiziente Varianten


Fibonacci-Baum rekursiv:

                    fib(4)
                   /      \
              fib(3)       fib(2)
             /     \       /     \
        fib(2)   fib(1) fib(1)  fib(0)
        /    \     |      |       |
   fib(1)  fib(0)  1      1       0
     |       |
     1       0
"""
