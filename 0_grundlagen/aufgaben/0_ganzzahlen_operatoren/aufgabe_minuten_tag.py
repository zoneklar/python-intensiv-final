"""(MITTEL)
Rechne die angegebnen Minuten in Tage, Stunden und Minuten um
nutze dazu floordiv und modulo

MINUTES_DAY = 24 * 60

Wieviele Tage sind 3434 Minuten?
Wieviele Stunden und Minuten bleiben dann noch übrig?

---------------------------------------------------------------
Beispiel

minuten = 3434

sind 2 Tage, 9 Stunden und 14 Minuten

"""

MINUTES_HOUR = 60
MINUTES_DAY = 24 * MINUTES_HOUR
total_mins = 3434


days = total_mins // MINUTES_DAY
rest_minutes = total_mins % MINUTES_DAY
hours = rest_minutes // MINUTES_HOUR
minutes = rest_minutes % MINUTES_HOUR

print(
    total_mins, "Minuten sind", days, "Tage,", hours, "Stunden und", minutes, "Minuten"
)

# --------------------------------------------------
# Alternative Lösung mit der Funktion divmod
# divmod liefert immer Floordiv und Modulo
# ---------------------------------------------------
days, rest_minutes = divmod(total_mins, MINUTES_DAY)
hours, minutes = divmod(rest_minutes, MINUTES_HOUR)

print(
    total_mins, "Minuten sind", days, "Tage,", hours, "Stunden und", minutes, "Minuten"
)
