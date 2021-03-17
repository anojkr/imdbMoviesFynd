from app.Exceptions import Exceptions

# DataParser class to format and  valid input request parameter
class DataParser(object):
    @staticmethod
    def validateParam(popularity, imdb_score):
        """
        1           This functions validate parameters for index-outof-bound error
                    ARGS:
                        popularity : movie popularity number
                        imdb_score : imdb_score of movie
                    RETURN:
                        raise InputOutofBound Exception if data not validated
        """
        if popularity > 100 or popularity < 0:
            raise Exceptions.InputOutOfBounds

        if imdb_score > 10 or imdb_score < 0:
            raise Exceptions.InputOutOfBounds

    @staticmethod
    def validateRequestData(jsonData):
        """
        This function parse the json-data and return value
        ARGS:
            jsonData : contains details of movies

        RETURN:
            popularity(float) : popularity of movie range(1-100)
            director(string) : director of movie
            imdbScore(float) : imdb score of movie
            movieName(string) : movie name
            genreList(List of strings) : generes to which movie belong
        """

        parameter = {
            "99popularity": True,
            "director": True,
            "genre": True,
            "imdb_score": True,
            "name": True,
        }
        if parameter.keys() != jsonData.keys():
            raise Exceptions.ParameterError

        popularity = float(jsonData.get("99popularity", 0))
        director = jsonData.get("director", "").strip()
        genre_list = jsonData.get("genre", [])
        imdb_score = float(jsonData.get("imdb_score", 0))
        name = jsonData.get("name", "").strip()

        DataParser.validateParam(popularity, imdb_score)

        for index, value in enumerate(genre_list):
            genre_list[index] = value.strip()

        return popularity, director, genre_list, imdb_score, name
