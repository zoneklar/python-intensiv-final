"""
Thema: Observer Pattern – Zustandsänderungen beobachten und reagieren

Das Observer Pattern ist ein Verhaltensmuster, bei dem ein Objekt (das
**Subject**) mehrere **Beobachter (Observer)** registrieren kann. Wenn sich
der Zustand des Subjekts ändert, werden alle registrierten Beobachter
automatisch benachrichtigt.

Dieses Muster ist besonders nützlich in Szenarien, in denen eine
**lose Kopplung** zwischen Komponenten gewünscht ist:

- GUI-Frameworks (z. B. bei Button-Klicks)
- Event-getriebene Systeme
- Benachrichtigung bei Datenänderungen
- Logging, Caching, Messaging

Bestandteile des Patterns:
- `Subject` verwaltet eine Liste von Observern und benachrichtigt sie bei Änderung.
- `Observer` implementiert eine Methode (z. B. `update()`), die aufgerufen wird.

Der Vorteil: Das Subject kennt die Observer nicht im Detail. Sie können zur Laufzeit
hinzugefügt oder entfernt werden – ohne die Logik des Subjects zu ändern.

Hinweis: In Python kann dieses Muster leicht mit Methoden, Callbacks oder auch
Funktionen umgesetzt werden.
"""
