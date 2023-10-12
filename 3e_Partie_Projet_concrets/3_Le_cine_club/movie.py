import logging
import os
import json

DIR = os.path.dirname(__file__)
DATA_file = os.path.join(DIR, "data", "movies.json")


def get_movies():
    movies = []
    with open(DATA_file, "r") as f:
        movies_title = json.load(f)
    # le code si dessous en comprehension de listes
    # movies = [Movie(movie_title) for movie_title in movies_title]
    for movie_title in movies_title:
        movies.append(Movie(movie_title))
    return movies


class Movie:
    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return self.title
    
    def _get_movies(self):
        with open(DATA_file, "r") as f:
            return json.load(f)
    
    def _write_movies(self, movies):
        with open(DATA_file, "w") as f:
            json.dump(movies, f, indent=4)
    
    def add_to_movies(self):
        movies = self._get_movies()
        
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f'Le film {self.title} est déjà enregistré')
            return False
    
    def remove_from_movies(self):
        movies = self._get_movies()
        
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)


if __name__ == '__main__':
    m = Movie("Harry potter")
    m.remove_from_movies()
    m.add_to_movies()
    # m._write_movies(["Green Book", "Mary poppins", "barry lyndon"])
    print(DATA_file)
    movies = get_movies()
    print(movies)
