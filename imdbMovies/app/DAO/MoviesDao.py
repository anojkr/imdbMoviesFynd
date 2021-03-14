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
# from app.DAO.MovieGenresDao import


class MoviesDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addMovies(popularity, director, imdbScore, movieName, genreList):

        try:
            response = Movies.objects.get(movieName=movieName)
            return response

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

            return movieResponse

    @staticmethod
    def getMovie(limit, offset):
        query = Movies.objects.filter().skip(offset).limit(limit)
        return query

    @staticmethod
    def getmoviesPopularity(popularity, offset, limit):
        query = Movies.objects.filter(popularity__gte = popularity).skip(offset).limit(limit)
        return query

    @staticmethod
    def getmoviesImdbScore(imdbScore, offset, limit):
        query = Movies.objects.filter(imdbScore__gte = imdbScore).skip(offset).limit(limit)
        return query

    @staticmethod
    def getSearchResult(popularity, movieName, director, genre, imdbScore, offset, limit):
        popularityResponse = Movies.objects.filter(popularity__gte = popularity)#.skip(offset).limit(limit)
        imdbscoreResponse = popularityResponse.filter(imdbScore__gte = imdbScore)

        responseResult = imdbscoreResponse
        if movieName!= None:
            movieResponse = imdbscoreResponse.filter(movieName__icontains = movieName)
            responseResult = movieResponse

        if director!= None:
            directorResponse = movieResponse.filter(director__icontains = director)
            responseResult = directorResponse
            
        return responseResult