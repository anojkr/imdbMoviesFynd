"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField, DateTimeField
import uuid
import datetime

class Cast(Document):

    castName  = StringField(unique=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.datetime.utcnow())
    
    meta = {"collection": "Cast"}

    def __repr__(self):
        return "Cast name={}".format(self.castName)
