"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""

from app.Models.CastModels import Cast
from app.Models.MoviesModels import Movies
from app.DAO.CastDao import CastDAO
from app.DAO.GenresDao import GenresDAO
from app.DAO.MovieGenresDao import MovieGenresDAO
from app.DAO.MovieCastDao import MovieCastDAO

from app.Exceptions import Exceptions

# from app.DAO.MovieGenresDao import


class MoviesDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addMovies(popularity, director, imdbScore, movieName, genreList):

        try:
            response = Movies.objects.get(movieName=movieName)
            return response, False

        except Exception as e:

            castResponse = CastDAO.addCast(director)
            movieResponse = Movies(
                popularity=popularity,
                director=director,
                imdbScore=imdbScore,
                movieName=movieName,
                genreList=genreList,
            ).save()

            response = MovieCastDAO.addMovieCast(movieResponse.id, castResponse.id)

            # adding movies genere-list
            for movieGenre in genreList:
                genreResponse = GenresDAO.addGenres(movieGenre)
                MovieGenresDAO.addMovieGenres(movieResponse.id, genreResponse.id)

            return movieResponse, True

    @staticmethod
    def getMovieList(offset, limit):
        query = Movies.objects.filter().skip(offset).limit(limit)
        return query

    @staticmethod
    def getmoviesPopularity(popularity, offset, limit):
        query = (
            Movies.objects.filter(popularity__gte=popularity).skip(offset).limit(limit)
        )
        return query

    @staticmethod
    def getmoviesImdbScore(imdbScore, offset, limit):
        query = (
            Movies.objects.filter(imdbScore__gte=imdbScore).skip(offset).limit(limit)
        )
        return query

    @staticmethod
    def getSearchResult(
        popularity, movieName, director, genre, imdbScore, offset, limit
    ):
        responseResult = Movies.objects.filter()
        if popularity > 0:
            responseResult = responseResult.filter(popularity__gte=popularity)
        
        if imdbScore > 0:
            responseResult = responseResult.filter(imdbScore__gte=imdbScore)

        if movieName != None:
            responseResult = responseResult.filter(movieName__icontains=movieName)

        if director != None:
            responseResult = responseResult.filter(director__icontains=director)

        return responseResult.skip(offset).limit(limit)

    @staticmethod
    def deleteMovie(movieID):
        response = Movies.objects(uid=movieID).delete()
        response = True if response == 1 else False
        return response
