from app.Models.CastModels import Cast
from app.DAO.CastInterface import CastInterface

class CastDAO(CastInterface):
    """
    A CastDAO to perform crud operations on Cast datamodel
    """

    @staticmethod
    def addCast(castName):
        """
        This function add cast to Cast-datamodel
        ARGS:
            castName(string) : Name of movie cast
        RETURN:
            Cast datamodel object
        """
        try:
            castResponse = Cast.objects.get(castName=castName)
            return castResponse
        except Exception as e:
            castResponse = Cast(castName=castName).save()
            return castResponse

    @staticmethod
    def getCast(castName):
        """
        This function check if castName exists in Cast-datamodel
        ARGS:
            castName : Name of movie cast

        RETURN:
            Cast datamodel object
        """
        castResponse = Cast.objects.filter(castName=castName).first()
        return castResponse
