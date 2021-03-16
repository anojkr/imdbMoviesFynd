class InternalServerError(Exception):
    pass


class DuplicateData(Exception):
    pass


class ParameterError(Exception):
    pass


class InputOutOfBounds(Exception):
    pass


class InvalidOperation(Exception):
    pass


def getReponseMessage(error_type, message):
    resp = dict()
    resp["status"] = "fail"
    resp["message"] = message
    resp["error_type"] = error_type
    return resp
