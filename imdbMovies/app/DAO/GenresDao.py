"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""

from app.Models.GenresModels import Genres


class GenresDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addGenres(genresName):
        try:
            response = Genres.objects.get(genresName=genresName)
            return response
        except Exception as e:
            response = Genres(genresName=genresName).save()
            return response

    @staticmethod
    def getGenres(genresName):
        response = Genres.objects.filter(genresName=genresName).first()
        return response
