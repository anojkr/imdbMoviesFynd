from app.Models.CastModels import Cast
from app.Models.MovieCastModels import MovieCast
from app.DAO.MovieCastInterface import MovieCastInterface

class MovieCastDAO(MovieCastInterface):
    """
    MovieCastDAO class is to perform crud operations on MoviesCast datamodel
    """

    @staticmethod
    def addMovieCast(movieID, castID):
        """
        This function add record in MovieCast datamodel
        ARGS:
            movieID : object_id of Movie datamodel
            castID : object_id of Cast datamodel
        RETURN:
            MovieCast datamodel object
        """
        try:
            movieCastResponse = MovieCast.objects.get(movieID=movieID, castID=castID)
            return movieCastResponse

        except Exception as e:
            movieCastResponse = MovieCast(movieID=movieID, castID=castID).save()
            return movieCastResponse

    @staticmethod
    def getMovieCast(castID):
        """
        This function check castID exist in MovieCast datamodel
        ARGS:
            castID : object_id of Cast datamodel
        RETURN:
            Cast datamodel object
        """

        movieCastResponse = MovieCast.objects.filter(castID=castID).first()
        return movieCastResponse
