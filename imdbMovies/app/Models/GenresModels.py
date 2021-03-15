"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, DateTimeField
import uuid
import datetime


class Genres(Document):

    genresName = StringField(unique=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    
    meta = {"collection": "Genres"}

    def __repr__(self):
        return "Genres name={}".format(self.genresName)
