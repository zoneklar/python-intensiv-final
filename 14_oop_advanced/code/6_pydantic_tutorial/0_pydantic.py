"""
pip install pydantic
"""

from pathlib import Path
import json
import pydantic
from typing import Literal


class Wizard(pydantic.BaseModel):
    id: int
    name: str
    age: int
    power: pydantic.PositiveInt
    magic: int
    intelligence: int
    origin: str | None = None  # optionale Felder benötigen Default-Wert
    history: list[int]
    type: Literal["wizard", "witcher"]
    super_power: bool | None = pydantic.Field(alias="superPower", default=None)

    model_config = pydantic.ConfigDict(populate_by_name=True)


def read_json(filename) -> list[dict]:
    """Lese Json ein und geb list von dicts zurück."""
    with open(Path(__file__).parent / filename, encoding="utf-8") as f:
        data = json.load(f)
        return data


if __name__ == "__main__":
    try:
        w = Wizard(
            id=3,
            name="Bob",
            age=100,
            power=3,
            magic=3,
            intelligence=34,
            origin=None,
            history=[2, 3],
            type="witcher",
            super_power=True,
        )  # type: ignore
        print(w.model_dump())  # mit model_dump_json() kann man json erstellen

    except Exception as e:
        print("Wizard konnte nicht angelegt werden!")

    data = read_json("wizards.json")
    wizards: list[Wizard] = [Wizard(**w) for w in data]

    print(wizards[0])
