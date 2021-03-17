class MoviesSerializer(object):
    def __init__(self, responseObj):
        self.responseObj = responseObj

    def getReponse(self):
        
        resp = {}
        for obj in self.responseObj:
            resp[obj.movieName] = {
                "movieid" : obj.uid,
                "movieName": obj.movieName,
                "popularity": obj.popularity,
                "director": obj.director,
                "imdb_score": obj.imdbScore,
                "genre_list": obj.genreList,
            }
        return resp
