"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, ReferenceField, DateTimeField
import uuid
import datetime
from app.Models.CastModels import Cast
from app.Models.MoviesModels import Movies
from mongoengine import *

#MoviesCast datamodel save details of casts such as actor, actress, director etc. related to movies
class MovieCast(Document):

    castID = ReferenceField(Cast, reverse_delete_rule=CASCADE)
    movieID = ReferenceField(Movies, reverse_delete_rule=CASCADE)
    role = StringField(default="Director")
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "MovieCast"}

    def __repr__(self):
        return "MovieCast ID={}".format(self.castID)
