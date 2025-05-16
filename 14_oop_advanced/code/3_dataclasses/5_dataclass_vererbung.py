"""
Datenklassen lassen sich einfach erweitern und vererben.
"""

from dataclasses import dataclass, asdict, astuple


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str = "Deutschland"


capital = Capital(name="Berlin", lon=34.343, lat=23, country="Germany")
print(capital)

print(astuple(capital))  # ('Berlin', 34.343, 23, 'Germany')
print(
    asdict(capital)
)  # {'name': 'Berlin', 'lon': 34.343, 'lat': 23, 'country': 'Germany'}
