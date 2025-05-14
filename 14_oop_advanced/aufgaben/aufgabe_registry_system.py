"""
Aufgabe: Automatische Registrierung von Konfigurationsklassen

Implementiere eine Metaklasse, die beim Erzeugen einer Klasse prüft,
ob die Attribute 'name', 'version' und 'settings' vorhanden sind und
die Typen korrekt sind. Die Klassen sollen automatisch in einer
Registry gespeichert werden, ohne dass der Nutzer explizit Code zur
Registrierung schreiben muss. Die Basisklasse 'BaseConfig' kapselt
die Metaklasse und bietet Zugriff auf alle registrierten Klassen
über 'BaseConfig.all()' und 'BaseConfig.get(name)'.

name: str
version: str
settings: dict
"""


class ConfigMeta(type):
    def __init__(cls, name, bases, dct):
        # Wenn die ConfigMeta-Klasse noch keine _registry hat,
        # muss diese als leeres Dict angelegt werden
        # if not hasattr(cls, "_registry"):
        # cls._registry = {}

        # Wenn es sich nicht um die BaseConfig handelt,
        # Prüfung der Attribute vornehmen, falls nicht vorhanden,
        # TypeError werfen
        # elif cls.__name__ != "BaseConfig":
        #    required_fields = ['name', 'version', 'settings']
        #    for field in required_fields:

        # Datentypen der Felder müssen aufgeprüft werden
        # if not isinstance(cls.name, str):
        #     raise TypeError("'name' muss ein str sein.")

        # Wenn Prüfung erfolgreich, Registrierung bei der Basisklasse
        # cls._registry[cls.name] = cls

        # Superklasse initialisieren
        # super(). ...


class BaseConfig(...):
    """BaseConfig muss Metaklasse ConfigMeta verwenden.  

    Zudem müssen die Methoden all() und get() implementiert werden.

    all(): liefert eine Liste aller registrierten Klassen zurück.
    get(classname): liefert die Klasse mit dem angegebenen Namen zurück.
    """


class LoggingConfig(BaseConfig):
    """Verwendet die BaseConfig als Basisklasse und definiert die Attribute."""
    name = "logging"
    version = "2.1"
    settings = {"level": "debug", "output": "stdout"}


class CacheConfig(BaseConfig):
    """Verwendet die BaseConfig als Basisklasse und definiert die Attribute."""
    name = "cache"
    version = "1.0"
    settings = {"size": 128, "eviction": "LRU"}


class WrongConfig(BaseConfig):
    """Verwendet die BaseConfig als Basisklasse. Allerdings fehlen Attribute."""
    name = "wrong"
    # Attriutes missing, must result in Error


# So kann man sich alle Konfiguration-Klassen ausgeben lassen:
for config_cls in BaseConfig.all():
    print(config_cls.name, config_cls.settings)

# So kann man sich die CacheConfig-Klasse holen:
cache = BaseConfig.get("cache")
print(cache.version)
