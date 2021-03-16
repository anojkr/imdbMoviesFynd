"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import (
    StringField,
    ListField,
    FloatField,
    DateTimeField,
)

import uuid
import datetime
from app.Models.CastModels import Cast


class Movies(Document):

    popularity = FloatField()
    director = StringField()
    imdbScore = FloatField()
    movieName = StringField(unique=True)
    genreList = ListField()
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "Movies"}

    def __repr__(self):
        return (
            "Movies Popularity={} Director {} Imdb Score={} Name={} "
            "Genre ={}".format(
                self.popularity,
                self.director,
                self.imdbScore,
                self.movieName,
                self.genreList,
            )
        )
