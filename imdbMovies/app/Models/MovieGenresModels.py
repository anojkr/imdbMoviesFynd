"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import UUIDField, ReferenceField, DateTimeField
import uuid
import datetime
from app.Models.MoviesModels import Movies
from app.Models.GenresModels import Genres
from mongoengine import *

#MovieGenres datamodel to save relation between movies and genres it belongs
class MovieGenre(Document):

    genreID = ReferenceField(Genres, reverse_delete_rule=CASCADE)
    movieID = ReferenceField(Movies, reverse_delete_rule=CASCADE)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "MovieGenre"}

    def __repr__(self):
        return "Movie Genre Movie ID={}, Genre ID={}".format(self.movieID, self.genreID)
