"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import (
    IntField,
    StringField,
    ListField,
    UUIDField,
    FloatField,
    DateTimeField,
    DictField,
    ReferenceField,
)

import uuid
from app.Models.CastModels import Cast


class Movies(Document):

    # uuid = UUIDField(binary=False, default=uuid.uuid4(), required=True, unique=True)
    popularity = FloatField()
    director = StringField()
    imdbScore = FloatField()
    movieName = StringField(unique=True)
    genreList = ListField()

    meta = {"collection": "Movies"}

    def __repr__(self):
        return (
            "Movies table Id={} Popularity={} Director {} Imdb Score={} Name={} "
            "Genre Blob={}".format(
                self.uuid,
                self.popularity,
                self.director,
                self.imdbScore,
                self.movieName,
                self.genreList,
            )
        )
