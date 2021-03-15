"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""

from app.Models.GenresModels import Genres
from app.Models.MoviesModels import Movies
from app.Models.MovieGenresModels import MovieGenre


class MovieGenresDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addMovieGenres(movieID, genreID):
        try:
            response = MovieGenre.objects.get(genreID=genreID, movieID=movieID)
            return response

        except Exception as e:
            response = MovieGenre(movieID=movieID, genreID=genreID).save()
            return response

    @staticmethod
    def getByGenre(genreID, offset, limit):
        # genreID = Genres.objects.get(movieName = genresName)
        response = MovieGenre.objects.filter(genreID=genreID).skip(offset).limit(limit)
        return response

    @staticmethod
    def getByMovie(movieID, offset, limit):
        # movieID = Movies.objects.get(movieName = movieName)
        response = MovieGenre.objects.filter(movieID=movieID).skip(offset).limit(limit)
        return response
