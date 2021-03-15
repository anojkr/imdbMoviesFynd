"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import UUIDField, ReferenceField, DateTimeField
import uuid
import datetime
from app.Models.MoviesModels import Movies
from app.Models.GenresModels import Genres


class MovieGenre(Document):

    genreID = ReferenceField(Genres)
    movieID = ReferenceField(Movies)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "MovieGenre"}

    def __repr__(self):
        return "Movie Genre Movie ID={}, Genre ID={}".format(
            self.movieID, self.genreID
        )
