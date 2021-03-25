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
    MoviesDAO is class to perform crud operations on Movie datamodel
    """

    @staticmethod
    def addMovies(popularity, director, imdbScore, movieName, genreList):
        """
        This function add record on Movie datamodel
        ARGS:
            popularity(float) : popularity of movie range(1-100)
            director(string) : director of movie
            imdbScore(float) : imdb score of movie
            movieName(string) : movie name
            genreList(List of strings) : generes to which movie belong

        RETURN:
            Movie datamodel object
        """

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
    def updateMovies(movieid, popularity, director, imdbScore, movieName, genreList):
        """
        This function add record on Movie datamodel
        ARGS:
            popularity(float) : popularity of movie range(1-100)
            director(string) : director of movie
            imdbScore(float) : imdb score of movie
            movieName(string) : movie name
            genreList(List of strings) : generes to which movie belong

        RETURN:
            Movie datamodel object
        """

        try:

            movieObject = Movies.objects.get(uid=movieid)
            movieObject.popularity = popularity
            movieObject.director = director
            movieObject.imdbScore = imdbScore
            movieObject.movieName = movieName
            movieObject.genreList = genreList
            movieObject.save()

            return movieObject, True
        
        except Exception as e:
            print(e)
            return None, False



    @staticmethod
    def getMovieList(offset, limit):
        """
        This function Movie datamodel object containing all movies
        """
        query = Movies.objects.filter().skip(offset).limit(limit)
        return query

    @staticmethod
    def getmoviesPopularity(popularity, offset, limit):
        """
        This function return list of movies having popularity greatest than <popularity> parameter
        ARGS:
            popularity(float) : popularity of movie
        RETURN:
            Movies datamodel object
        """
        query = (
            Movies.objects.filter(popularity__gte=popularity).skip(offset).limit(limit)
        )
        return query

    @staticmethod
    def getmoviesImdbScore(imdbScore, offset, limit):
        """
        This function return list of movies having imdbScore greatest than <imdbScore> parameter
        ARGS:
            imdbscore(float) : imdb-score of movie
        RETURN:
            Movies datamodel object
        """
        query = (
            Movies.objects.filter(imdbScore__gte=imdbScore).skip(offset).limit(limit)
        )
        return query

    @staticmethod
    def getSearchResult(
        popularity, movieName, director, genre, imdbScore, offset, limit
    ):

        """
        This function filter result from Movies datamodel based on functional parameters an return Movies datamodel object
        ARGS:
            popularity(float) : popularity of movie range(1-100)
            director(string) : director of movie
            imdbScore(float) : imdb score of movie
            movieName(string) : movie name
            genreList(List of strings) : generes to which movie belong

        RETURN:
            Movie datamodel object
        """
        responseResult = Movies.objects.filter()
        if popularity > 0:
            responseResult = responseResult.filter(popularity__gte=popularity)

        if imdbScore > 0:
            responseResult = responseResult.filter(imdbScore__gte=imdbScore)

        if movieName != None:
            responseResult = responseResult.filter(movieName__icontains=movieName)

        if director != None:
            responseResult = responseResult.filter(director__icontains=director)

        if genre != None:
            responseResult = responseResult.filter(genreList__icontains=genre)

        return responseResult.skip(offset).limit(limit)

    @staticmethod
    def deleteMovie(movieID):

        """
        This function delete record from Movies datamodel for given movieID in parameter
        ARGS:
            movieID : object_id of Movies datamodel
        RETURN:
            True : if delete operation sucessfully
            False: if failed to find movieID on Movies datamodel
        """
        response = Movies.objects(uid=movieID).delete()
        response = True if response == 1 else False
        return response
