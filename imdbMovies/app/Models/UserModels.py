"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, DateTimeField
import uuid
import datetime


class User(Document):

    uid = UUIDField(binary=False, default=uuid.uuid4(), required=True)
    username = StringField(unique=True)
    password = StringField(unique=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())

    meta = {"collection": "User"}

    def __repr__(self):
        return "Cast name={}".format(self.castName)
