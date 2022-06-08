"""
Zadanie: biblioteka filmów
A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący bibliotekę filmów i seriali. 
Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:

Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. 
Każdy film powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Liczba odtworzeń
Umożliwia przechowywanie informacji na temat seriali. 
Każdy serial powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Numer odcinka
Numer sezonu
Liczba odtworzeń
Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, 
np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, 
natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
Przechowuje filmy i seriale w jednej liście.
"""
films_library = []

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        

        #Variables
        self.number_of_plays = 0

    def __str__(self):
        return f"{self.title} ({self.year})"
    def __repr__(self):
        return f"{self.title} {self.year} {self.genre} {self.number_of_plays}"

    def play(self):
        self.number_of_plays += 1

class Serial(Movie):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episode_number = episode_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"
    def __repr__(self):
        return f"{self.title} {self.year} {self.genre} {self.number_of_plays} {self.season_number} {self.episode_number}"


serial_1 = Serial(title="The 100", year ="2014", genre="sci-fi", season_number=1, episode_number=1)
serial_2 = Serial(title="The 100", year ="2014", genre="sci-fi", season_number=5, episode_number=10)
serial_3 = Serial(title="The 100", year ="2014", genre="sci-fi", season_number=10, episode_number=1)
serial_4 = Serial(title="The 100", year ="2014", genre="sci-fi", season_number=10, episode_number=10)
film_1 = Movie(title="Pulp Fiction", year ="1994", genre="drama")
film_2 = Movie(title="Prometheus", year ="2012", genre="sci-fi")
films_library.append(serial_1)
films_library.append(serial_2)
films_library.append(serial_3)
films_library.append(serial_4)
films_library.append(film_1)
films_library.append(film_2)

if __name__ == "__main__":
    serial_1.play()
    serial_1.play()
    serial_1.play()
    print(serial_1)
    print(serial_1.number_of_plays)

    serial_2.play()
    serial_2.play()
    print(serial_2)
    print(serial_2.number_of_plays)

    serial_3.play()
    serial_3.play()
    serial_3.play()
    serial_3.play()
    print(serial_3)
    print(serial_3.number_of_plays)

    serial_4.play()
    print(serial_4)
    print(serial_4.number_of_plays)

    film_1.play()
    print(film_1)
    print(film_1.number_of_plays)

    film_2.play()
    film_2.play()
    film_2.play()
    film_2.play()
    film_2.play()
    print(film_2)
    print(film_2.number_of_plays)
    
    print(films_library)