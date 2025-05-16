import pydantic
from typing_extensions import Annotated
from typing import Self


class Person(pydantic.BaseModel):
    id: pydantic.PositiveInt
    name: Annotated[
        str,
        pydantic.StringConstraints(
            strip_whitespace=True, strict=True, min_length=3, max_length=3
        ),
    ]
    age: Annotated[int, pydantic.Field(strict=False, gt=2, le=1130)]  # > 2 && <= 10

    @pydantic.field_validator("age")
    @classmethod
    def validate_age(cls, value: int) -> int:
        """Prüfe Alter auf irgendwas."""
        print("tpye von age:", type(value))
        if value == 1000:
            raise ValueError("Der Wert darf nicht genau Tausend")

        return value

    @pydantic.model_validator(mode="after")
    def validate_age_and_name(self) -> Self:
        """Kreuzfeld-Validierung von Name und Alter."""

        if self.name.lower() == "bob" and self.age == 999:
            raise ValueError("Bob darf nicht 999 jahre alt sein")

        return self

    def say_hello(self):
        print(self.name)


p = Person(id=3, name=" abc", age="1001")
print(p.name)
p.say_hello()
###############################################
p = Person(id=4, name="Bob", age=999)
print(p.name)
p.say_hello()
