
from app.Models.GenresModels import Genres
from app.Models.MoviesModels import Movies
from app.Models.MovieGenresModels import MovieGenre


class MovieGenresDAO(object):
    """
        MovieGenresDAO is class to perform crud operations on MovieGenres datamodel
    """

    @staticmethod
    def addMovieGenres(movieID, genreID):
        """
            This function save record on MovieGenres datamodel
            ARGS:
                movieID : object_id of Movie datamodel
                genreID : object_id of Genres datamodel
            RETURN:
                MovieGenres datamodel object 
        """
        try:
            response = MovieGenre.objects.get(genreID=genreID, movieID=movieID)
            return response

        except Exception as e:
            response = MovieGenre(movieID=movieID, genreID=genreID).save()
            return response

    @staticmethod
    def getByGenre(genreID, offset, limit):
        """
            This function get movies list based on genereID
            ARGS:
                genreID : object_id of Genres datamodel
            RETURN:
                MovieGenre datamodel object
        """
        response = MovieGenre.objects.filter(genreID=genreID).skip(offset).limit(limit)
        return response

    @staticmethod
    def getByMovie(movieID, offset, limit):
        """
            This function get genreID list based on movieID
            ARGS:
                movieID : object_id of Movie datamodel
            RETURN:
                MovieGenre datamodel object
        """
        response = MovieGenre.objects.filter(movieID=movieID).skip(offset).limit(limit)
        return response
