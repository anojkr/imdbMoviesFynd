class ValidationError(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error

    def __str__(self):
        return self.message

    def getMessage(self):
        response = {"status": "fail", "message": self.message, "error": self.error}
        return response

class InputOutOfBounds(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error

    def __str__(self):
        return self.message

    def getMessage(self):
        response = {"status": "fail", "message": self.message, "error": self.error}
        return response

class DuplicateData(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error

    def __str__(self):
        return self.message

    def getMessage(self):
        response = {"status": "fail", "message": self.message, "error": self.error}
        return response