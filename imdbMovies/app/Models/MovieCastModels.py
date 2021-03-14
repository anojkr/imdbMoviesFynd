"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, ReferenceField
import uuid
from app.Models.CastModels import Cast
from app.Models.MoviesModels import Movies


class MovieCast(Document):

    # uuid = UUIDField(binary=False, default=uuid.uuid4(), primary_key=True, unique=True)
    castID = ReferenceField(Cast)
    movieID = ReferenceField(Movies)
    role = StringField(default="Director")

    meta = {"collection": "MovieCast"}

    def __repr__(self):
        return "Persons table Id={}, name={}".format(self.uuid, self.castName)
