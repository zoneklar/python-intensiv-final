"""
Thema: Klassenmethoden in Python – @classmethod

Klassenmethoden sind Methoden, die auf die Klasse selbst statt auf
eine Instanz zugreifen. Sie werden mit dem Decorator @classmethod
gekennzeichnet und erhalten cls (statt self) als ersten Parameter.

Damit können sie auf Klassendaten zugreifen oder alternative
Konstruktoren bereitstellen.

Typische Anwendungsfälle:
- Factory-Methoden
- Zugriff auf oder Veränderung von Klassenattributen
- Klassenspezifische Initialisierungen

Aufruf: über die Klasse oder eine Instanz möglich (Klasse.methode()).
"""
