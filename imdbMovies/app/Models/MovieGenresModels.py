"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import UUIDField, ReferenceField
import uuid
from app.Models.MoviesModels import Movies
from app.Models.GenresModels import Genres


class MovieGenre(Document):

    # uuid = UUIDField(binary=False, default=uuid.uuid4(), required=True, unique=True)
    genreID = ReferenceField(Genres)
    movieID = ReferenceField(Movies)

    meta = {"collection": "MovieGenre"}

    def __repr__(self):
        return "Movie Genre Table Id={} Movie ID={}, Genre ID={}".format(
            self.uuid, self.movieID, self.genreID
        )
