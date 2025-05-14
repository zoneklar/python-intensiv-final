"""
Das Thema dieser Datei ist `*args`, `**kwargs` und Default-Parameter.
- `*args` erlaubt eine unbestimmte Anzahl an positionsbasierten Argumenten.
- `**kwargs` erlaubt eine unbestimmte Anzahl an keywordbasierten Argumenten.
- Default-Parameter können standardisierte Werte festlegen, die verwendet
  werden, wenn kein Argument übergeben wird.
"""


def f(a, b):
    pass


f(1, 2)


##############################
def values(a, b, *args):
    print("Das Ergebnis ist ein Tuple von Werten:", args)
    print("a, b", a, b)


values(1, 2, 43, 24, 134)


############################
# keyword args
def say_hello(name, age):
    pass


say_hello("bob", 22)
say_hello(name="bob", age=22)
say_hello(age=22, name="Alice")  # Reihnfolge spielt bei Keyword-Args keine Rolle!


def introduce_person(**kwargs):
    """Stellt eine Person mit Begrüßung, Namen und Attributen vor.

    kwargs: ein Dict mit den Keyword-Arumgenten
    """
    print("**kwargs:", kwargs)


# Beispielaufruf der Funktion
introduce_person(age=25, city="München")


def configure_device(*args, **kwargs):
    """Konfiguriert ein Gerät mit einem Modus und einer Leistung."""
    print(args)  # ('Sensor Y',)
    print(kwargs)  # {'mode': 'manual', 'power': 75}


# Beispielaufruf der Funktion
configure_device("Sensor X")
configure_device("Sensor Y", mode="manual", power=75)


# Keyword-Argumente erzwingen. Alles rechts von * muss
# per keyword übergeben werden.
def connect_database(*, username, password, database):
    print(username, password, database)


# fehler, übergabe nur per Position:
# connect_database("bob", "supersecret", "system")

# Richtig, Übergaber per Keyword Argumente
connect_database(username="bob", password="supersecret", database="system")
