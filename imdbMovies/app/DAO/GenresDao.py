
from app.Models.GenresModels import Genres

class GenresDAO(object):
    """
    GenresDAO class to perform crud operation on Genres-datamodel
    """

    @staticmethod
    def addGenres(genresName):
        """
            This function add record in Genres-datamodel
            ARGS:
                genresName(string) : genere of movie it belong
            RETURN:
                Genres datamodel object
        """
        try:
            response = Genres.objects.get(genresName=genresName)
            return response
        except Exception as e:
            response = Genres(genresName=genresName).save()
            return response

    @staticmethod
    def getGenres(genresName):
        """
            This function check genresName exists in Genres-datamodel
            ARGS:
                genresName(string) : genere of movie it belong
            RETURN:
                Geners datamodel object
        """
        response = Genres.objects.filter(genresName=genresName).first()
        return response
