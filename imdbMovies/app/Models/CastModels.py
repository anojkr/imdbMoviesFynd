"""
Definition of database Models
"""

from mongoengine import connect, Document
from mongoengine import StringField, UUIDField
import uuid


class Cast(Document):

    # uuid = UUIDField(binary=False, default=uuid.uuid4(), primary_key=True, unique=True)
    castName = StringField(unique=True)

    meta = {"collection": "Cast"}

    def __repr__(self):
        return "Persons table Id={}, name={}".format(self.uuid, self.castName)
