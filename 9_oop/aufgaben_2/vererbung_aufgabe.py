"""mittel

Aufgabe: Entwicklung eines Klassifizierungssystems für Medieninhalte

Ziel:
Implementiere ein Programm in Python, das verschiedene Arten von
Medieninhalten wie Bücher, Filme und Podcasts klassifiziert. Das
Programm soll Vererbung verwenden, um eine Hierarchie von Klassen
zu erstellen, die allgemeine und spezifische Eigenschaften von
Medienobjekten darstellen. Es reicht eine Ableitungsklasse.

Anforderungen:
1. Basisklasse:
   - Erstelle eine Basisklasse namens `Media`, die generische
     Eigenschaften wie `title`, `creator` und `publication_year`
     enthält.
   - Definiere eine Methode `display_info()`, die Basisinformationen
     ausgibt.

2. Abgeleitete Klassen:
   - Entwickle eine abgeleitete Klasse: Z.B. `Book`, `Movie`, und `Podcast`.
   - `Book` sollte zusätzliche Attribute wie `number_of_pages` und
     `genre` haben.
   - `Movie` erweitert `Media` mit Attributen wie `duration` und
     `director`.
   - `Podcast` fügt Eigenschaften wie `number_of_episodes` und `host`
     hinzu.
   - Überschreibe die Methode `display_info()` in jeder abgeleiteten
     Klasse, um spezifische Informationen auszugeben.

3. Ausgabe
   - Erstelle eine Funktion, die Instanzen jeder Klasse erstellt
     und die Methode `display_info()` für diese Objekte aufruft, um
     die korrekte Funktionalität zu überprüfen.


Beispiel:
-------------
book = Book(title="1984", creator="George Orwell", year=1949,
    number_of_pages=328,"Dystopian",)
movie = Movie(title="Inception", creator="Christopher Nolan", year=2010,
    duration=148, director="Christopher Nolan")
podcast = Podcast(title=
        "Science Vs", creator="Wendy Zukerman", year=2015,
        number_of_episodes=112, host="Wendy Zukerman"
    )

media_items = [book, movie, podcast]
display_media_info(media_items)

Ausgabe:
Book: 1984, Author: George Orwell,Year: 1949, Pages: 328, Genre: Dystopian
Movie: Inception, Director: Christopher Nolan, Year: 2010, Duration: 148 mins
Podcast: Science Vs, Host: Wendy Zukerman,Year: 2015, Episodes: 112

"""


class Media:
    def __init__(self, title, creator, publication_year):
        self.title = title
        self.creator = creator
        self.publication_year = publication_year

    def display_info(self):
        print(
            f"Title: {self.title}, Creator: {self.creator},"
            f"Year: {self.publication_year}"
        )


# Abgeleitete Klasse für Bücher
class Book(Media):
    def __init__(self, title, creator, publication_year, number_of_pages, genre):
        super().__init__(title, creator, publication_year)
        self.number_of_pages = number_of_pages
        self.genre = genre

    def display_info(self):
        print(
            f"Book: {self.title}, Author: {self.creator},"
            f"Year: {self.publication_year}, Pages: {self.number_of_pages}"
            f"Genre: {self.genre}"
        )


class Movie(Media):
    def __init__(self, title, creator, publication_year, duration, director):
        super().__init__(title, creator, publication_year)
        self.duration = duration
        self.director = director

    def display_info(self):
        print(
            f"Movie: {self.title}, Director: {self.director}, "
            f"Year: {self.publication_year}, Duration: {self.duration} mins"
        )


# Abgeleitete Klasse für Podcasts
class Podcast(Media):
    def __init__(self, title, creator, publication_year, number_of_episodes, host):
        super().__init__(title, creator, publication_year)
        self.number_of_episodes = number_of_episodes
        self.host = host

    def display_info(self):
        print(
            f"Podcast: {self.title}, Host: {self.host},"
            f"Year: {self.publication_year},"
            f"Episodes: {self.number_of_episodes}"
        )


def test():
    book = Book("1984", "George Orwell", 1949, 328, "Dystopian")
    movie = Movie("Inception", "Christopher Nolan", 2010, 148, "Christopher Nolan")
    podcast = Podcast("Science Vs", "Wendy Zukerman", 2015, 112, "Wendy Zukerman")

    media_list = [book, movie, podcast]
    for media in media_list:
        media.display_info()


if __name__ == "__main__":
    test()
