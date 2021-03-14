"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField
import uuid


class Genres(Document):

    # uuid = UUIDField(binary=False, default=uuid.uuid4(), primary_key=True, unique=True)
    genresName = StringField(unique=True)

    meta = {"collection": "Genres"}

    def __repr__(self):
        return "Persons table Id={}, name={}".format(self.uuid, self.genresName)
