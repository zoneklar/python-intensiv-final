"""
Vergleich normale Klasse vs Dataclass

Pause bis 10.48
"""

import random
from dataclasses import dataclass, field, asdict


class RegularCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"RegularCard({self.rank!r}, {self.suit!r})"


queen_of_hearts = RegularCard(rank="Q", suit="Hearts")
queen_of_hearts2 = RegularCard(rank="Q", suit="Hearts")

####################


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts_v = DataClassCard(rank="Q", suit="Hearts")
queen_of_hearts2_v = DataClassCard(rank="Q", suit="Hearts")
print(queen_of_hearts_v == queen_of_hearts2_v)


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


@dataclass
class FrenchCardDeck:
    cards: list[DataClassCard] = field(default_factory=list)  # legt eine leere Liste


def generate_french_deck(shuffle: bool = False):
    """Erzeuge ein franz. Kartendeck."""
    result = [DataClassCard(r, s) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(result)

    return result


deck = FrenchCardDeck(cards=generate_french_deck())
print(deck.cards)

# Als dict exportieren
d = asdict(queen_of_hearts2_v)
print(d)

d = asdict(deck)
print(d)
