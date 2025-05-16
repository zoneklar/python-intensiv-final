from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select


connection_string = "sqlite:///user.db"


class Base(DeclarativeBase):
    """Baseclass to generate tables."""

    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))  # VARCHAR(30)

    def __repr__(self) -> str:
        return self.name


def create_db(engine):
    """die Datenbank anlegen."""
    Base.metadata.create_all(engine)


def get_user(engine, id_):
    with Session(engine) as session:
        stmt = select(User).where(User.id == id_)
        return session.scalars(stmt).first()


def get_users(engine) -> list[User]:
    """Get Users from Table users."""

    with Session(engine) as session:
        stmt = select(User).where(User.name.in_(["Bob", "alice"]))
        return list(session.scalars(stmt))


if __name__ == "__main__":

    engine = create_engine(connection_string, echo=True)
    create_db(engine)  # Datenbank anlegen

    with Session(engine) as session:
        bob = User(name="Bob")
        session.add(bob)
        session.commit()

        users = get_users(engine)
        print("users:", users)

        user = get_user(engine, 3)
        print("User:", user, type(user))
        print(user.name)
