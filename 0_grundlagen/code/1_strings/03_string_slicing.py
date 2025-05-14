"""
String Slicing in Python

String Slicing erlaubt es, Teilstrings (Substrings) aus einem String zu
extrahieren.
Mit Hilfe von Start-, End- und Schrittwerten kann flexibel auf bestimmte
Abschnitte eines Strings zugegriffen werden.

Themenübersicht:
1. Grundlagen des Slicings
2. Negative Indizes
3. Slicing mit Schrittwerten
4. Nützliche Anwendungen



Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""

string = "Hamburg"
print(f"{string[0:4]=}")  # Hamb
print(f"{string[:4]=}")  # Hamb

print("Negativer Index:", string[-1])
print(f"{string[0:-1]=}")  # Hambur
print(f"{string[2:]=}")  # mburg

# # Übung
# # Schneide jeweils alle A aus den Strings
# AAAAB => AAAA
# BBAAABBB => AAA
# AAAABBBB => AAAA
# ABBBBB => A
string = "AAAAB"  # AAAA
print(string[0:-1])

string = "BBAAABBB"
print(string[2:5])

string = "AAAABBBB"
print(string[:4])

string = "BBAABBBB"
print(string[2:4])

string = "ABBBBB"
print(string[:1])

numbers = "123456789"
print(numbers[::2])  # 13579
print(numbers[1::2])  # 2468

print(numbers[::-1])  # String umdrehen
