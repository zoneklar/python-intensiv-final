"""
Schwer

Erstelle via Usereingabe zwei Vektoren gleicher Länge
und führe im Anschluss eine Vektoraddition aus.

Wie addiert man Vektoren?
https://de.serlo.org/mathe/1759/vektoren-addieren-und-subtrahieren

Die Vektoren sind einfache Python-Listen und der zu
verwendende Datentyp der Vektorwerte ist Integer.

Um eine Vektor-Addition durchzuführen, müssen die Vektoren
die gleiche Länge haben.

Schreibe ein Programm, welches die Vektoren auf gleiche
L#nge prüft und dann einen neuen Vektor erzeugt. Wir gehen bei der Eingabe von
validen Daten aus (also User gibt Integer ein und keine BUchstaben u.ä.)

Nutze dazu split(","), for-loop, append

Beispiel:
Bitte gebe die Werte für den Vektor 1 an: 1,2,3
Bitte gebe die Werte für den Vektor 2 an: 2,3,4
der neue Vektor ist: [3, 5, 7]

Empfehlung Vorgehensweise:
1) Vektordaten vom User erhalten, zum Beispiel als kommaspaprierter String
2) Split durchführen und die Liste mit Zahl-Strings konvertieren nach int
3) das für den 2. Vektor wiederholen
4) Prüfen, ob beide Vektoren (Listen) gleich lang sind
5) Falls ja, die Vektoraddition elementweise durchführen.
"""

vector_1_str = input("Bitte gebe die Werte für den Vektor 1 an: ").split(",")
vector_2_str = input("Bitte gebe die Werte für den Vektor 2 an: ").split(",")

vector_1 = []
vector_2 = []
vector_3 = []

for element in vector_1_str:
    vector_1.append(int(element))

for element in vector_2_str:
    vector_2.append(int(element))

if len(vector_1) != len(vector_2):
    print("Die Vektoren haben nicht die gleiche Länge!")
else:
    for i in range(len(vector_1)):
        v = vector_1[i] + vector_2[i]
        vector_3.append(v)

    print(f"der neue Vektor ist: {vector_3}")
