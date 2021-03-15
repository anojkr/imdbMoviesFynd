"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, ReferenceField, DateTimeField
import uuid
import datetime
from app.Models.CastModels import Cast
from app.Models.MoviesModels import Movies


class MovieCast(Document):

    castID = ReferenceField(Cast)
    movieID = ReferenceField(Movies)
    role = StringField(default="Director")
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "MovieCast"}

    def __repr__(self):
        return "MovieCast ID={}".format(self.castID)
