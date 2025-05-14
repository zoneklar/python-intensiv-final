"""
1. Vokale zählen (MITTEL)
Schreibe eine Funktion count_vowels() die einen String als Parameter erwartet,
und alle Vokale  in diesem String zählt. Der Rückgabewert der Funktion ist die
Anzahl der Vokale (int). Als Vokale zählen im deutschen: aeiouüäö
Beachte Groß- und Kleinschreibung! Auge hat 3 Vokale

Beispiel:
number_of_vowels = count_vowels("teleport").
print(number_of_vowels)
// 3

number_of_vowels = count_vowels("Ööll").
print(number_of_vowels)
// 2
"""


def count_vowels(word: str) -> int:
    """Count german vowels in word."""
    vowels = "aeiouüäö"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1

    return count


number_of_vowels = count_vowels("teleport")
print(number_of_vowels)


number_of_vowels = count_vowels("Ööll")
print(number_of_vowels)


def filter_input(values: list, allowed_values: list) -> list:
    """Filtere eine Liste anhand von einer Vergleichsliste."""
    new_list = []
    for value in values:
        if value in allowed_values:
            new_list.append(value)
    return new_list


r = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
print(r)

r = filter_input([1, 3, 4, 5, 3], [])
print(r)

r = filter_input([1, 3, 4, 5, 3], [3, 4])
print(r)


"""
4. Rückwärts (SCHWER)
Schreibe eine Funktion reverse_cutter(), die einen String entgegennimmt, diesen
zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet und
das Ergebnis umgedreht zurückgibt. Ein Input kleiner gleich Länge zwei gibt
einen leeren String zurück.  Beispiel:
reversed = reverse_cutter("Petersburg")
// rubsrete
"""


def reverse_cutter(word: str):
    return word[-2:0:-1].lower()


reversed = reverse_cutter("Petersburg")
print(reversed)


"""
5. Max (MITTEL)
Implementiere die Funktion max. Diese soll aus einer gegebenen Liste von
Integerwerten den größten Wert zurückgeben. Nutze dazu nicht die Built-In
Funktion max oder max aus dem Numpy-Modul! Die Funktion soll None zurückgeben,
wenn eine leere Liste übergeben wurde.  

Beispiel:
values = [3, 2, 4]
x_max = max(values)
// 4

values = []
x_max = max(values)
// None
"""

"""
6. Median (SCHWER)
Implementiere die Funktion median(), die eine Liste von Integerwerten
entgegennimmt und den Median berechnet. Prüfe die Funktion mit verschiedenen
Input-Werten! Nicht die Funktion median aus dem Numpy Modul o.ä. nutzen.
Ergebnis kann hier geprüft werden:
http://www.alcula.com/calculators/statistics/median/


Beispiel:
values = [1, 2, 4, 8, 2, 19]
x_median = median(values)
// 3.0
"""

""" (LEICHT)
7. Schwellenwertfunktion (Heaviside, Hard Limit)
Eine Funktion, die häufig im Zusammenhang mit neuronalen Netzen 
genutzt wird, ist die Heaviside funktion.
Sie gibt 1 zurück, wenn der Eingangswert größergleich 0 ist, ansonsten,
gibt sie 0 zurück.

Hintergrundwissen:
https://de.wikipedia.org/wiki/Heaviside-Funktion
"""

"""
8. Rectifier (RELU) (MITTEL)
im DeepLearning häufig genutze Funktion, die als Positivteil ihres Arguments
definiert ist.

Hintergrundwissen:
https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html

f(v) = max(0, v)

Führe die Funktion von der Range -10 bis 10 aus, zum Beispiel via einer
List-Comprehension.
"""
