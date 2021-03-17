# Exception class to throw internal code error
class InternalServerError(Exception):
    pass


# Exception class to throw duplicate record error
class DuplicateData(Exception):
    pass


# Exception class to throw missing parameter error
class ParameterError(Exception):
    pass


# Exception class to throw outof bound value of parameter
class InputOutOfBounds(Exception):
    pass


# Exception class to throw invalid-operation performed on record
class InvalidOperation(Exception):
    pass


# This function builds reponse for Exceptions
def getReponseMessage(error_type, message):
    """
    ARGS:
        error_type(string) : Types of error occurred
        message(string) : Display the corresponding error message

    RETURN:
        dict object containing response
    """

    resp = dict()
    resp["status"] = "fail"
    resp["message"] = message
    resp["error_type"] = error_type
    return resp
