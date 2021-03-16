class MoviesSerializer(object):
    def __init__(self, responseObj):
        self.responseObj = responseObj

    def getReponse(self):
        # count = 1
        resp = {}
        for obj in self.responseObj:
            resp[obj.movieName] = {
                "movieName": obj.movieName,
                "popularity": obj.popularity,
                "director": obj.director,
                "imdb_score": obj.imdbScore,
                "genre_list": obj.genreList,
            }
            # count = count + 1
        return resp
