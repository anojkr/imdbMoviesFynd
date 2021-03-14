"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""

from app.Models.CastModels import Cast


class CastDAO(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    @staticmethod
    def addCast(castName):
        try:
            castResponse = Cast.objects.get(castName=castName)
            return castResponse
        except Exception as e:
            castResponse = Cast(castName=castName).save()
            return castResponse

    @staticmethod
    def getCast(castName):
        castResponse = Cast.objects.filter(castName=castName).first()
        return castResponse
