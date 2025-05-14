"""
Thema: __str__ und __repr__ in Python (Dunder-Methoden)

In Python gibt es spezielle Methoden, die mit doppelten Unterstrichen
beginnen und enden – sogenannte "dunder"-Methoden. Zwei wichtige davon
sind:

- __str__(self): Wird aufgerufen, wenn ein Objekt in einen String
  umgewandelt oder mit print() ausgegeben wird. Ziel: leserliche
  Darstellung für den Benutzer.

- __repr__(self): Wird aufgerufen, wenn die "repr()" Funktion genutzt
  wird oder ein Objekt in einer interaktiven Konsole angezeigt wird.
  Ziel: eine eindeutige, oft technische Darstellung, die im Idealfall
  wieder zu demselben Objekt führt (eval(repr(obj))).

Diese Datei zeigt den Unterschied beider Methoden mit praktischen
Beispielen.
"""
