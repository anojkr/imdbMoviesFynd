from app.Exceptions import Exceptions


class DataParser(object):
    @staticmethod
    def validateParam(popularity, imdb_score):
        if popularity > 100 or popularity < 0:
            raise Exceptions.InputOutOfBounds

        if imdb_score > 10 or imdb_score < 0:
            raise Exceptions.InputOutOfBounds

    @staticmethod
    def validateRequestData(jsonData):
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
