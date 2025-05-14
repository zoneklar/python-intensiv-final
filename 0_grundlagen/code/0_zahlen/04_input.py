"""
Benutzereingaben in Python: `input`, Prompts und Konvertierung

Python ermöglicht es, Benutzereingaben über die Funktion `input` zu
verarbeiten. Die Eingabe wird standardmäßig als String zurückgegeben, kann
aber in andere Datentypen umgewandelt werden, um damit zu arbeiten.

Themenübersicht:
1. Grundlagen der Funktion `input`
2. Verwendung eines Prompts für Eingaben
3. Konvertierung von Eingaben in andere Datentypen
4. Validierung und Umgang mit ungültigen Eingaben
"""

values = int(input("Bitte Wert eingeben:"))
print(values, type(values))  # str

# values = int(values)
