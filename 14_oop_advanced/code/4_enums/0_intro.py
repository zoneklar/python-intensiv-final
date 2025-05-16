"""
Thema: Enums in Python – Aufzählungstypen definieren

Ein Enum (Abkürzung für *enumeration*) ist ein spezieller Datentyp,
mit dem man symbolische Namen für feste Werte definieren kann.
So entstehen **konstante, benannte Werte**, die sich z. B. besser
lesen, warten und typisieren lassen als einfache Strings oder Zahlen.

Python bietet dafür das Modul `enum` mit der Basisklasse `Enum`.

Vorteile:
- besser lesbarer Code (z. B. Color.RED statt "red")
- feste Wertemengen, z. B. Status, Typen, Kategorien
- Vergleichbarkeit, Iteration, Typsicherheit
- zentrale Definition der erlaubten Werte

Beispiel:

    from enum import Enum

    class Status(Enum):
        PENDING = "pending"
        PAID = "paid"
        CANCELED = "canceled"

    print(Status.PENDING.value)   # "pending"
    print(Status["PAID"])         # Status.PAID

Enums sind unveränderlich, vergleichbar und ideal, um z. B. Zustände,
Rollen, Aktionen oder Konfigurationsmodi konsistent abzubilden.
"""

from enum import Enum, StrEnum, IntEnum, auto


class Role(StrEnum):
    # seit python 3.11
    DEVELOPER = "developer"
    BOSS = "boss"
    HUMAN_RESOURCES = "hr"


class HTTPStatus(IntEnum):
    NOT_FOUND = 404
    REDIRECT = 302


class Status(Enum):
    PENDING = auto()
    PAID = auto()
    CANCELED = auto()


def set_status(status: Status):
    """Enum"""
    print(status.name)  # PAID
    print(status.value)  # 1


set_status(status=Status.PAID)


def check_http_status(status: HTTPStatus):
    """Prüfe anhand von Status den Wert."""
    if status == HTTPStatus.NOT_FOUND:
        print("Wurde nicht gefunden")
        print(HTTPStatus.NOT_FOUND)  # 404


check_http_status(status=HTTPStatus.NOT_FOUND)
