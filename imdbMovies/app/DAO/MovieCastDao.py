"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""

from app.Models.CastModels import Cast
from app.Models.MovieCastModels import MovieCast


class MovieCastDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addMovieCast(movieID, castID):
        try:
            movieCastResponse = MovieCast.objects.get(movieID=movieID, castID=castID)
            return movieCastResponse

        except Exception as e:
            movieCastResponse = MovieCast(movieID=movieID, castID=castID).save()
            return movieCastResponse

    @staticmethod
    def getMovieCast(castID):
        movieCastResponse = MovieCast.objects.filter(castID=castID).first()
        return movieCastResponse
