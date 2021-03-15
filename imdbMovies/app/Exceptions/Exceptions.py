
class ValidationError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error

   	def __str__(self):
		return self.message

    def getMessage():
      response = { "status" : "fail"git 
                   , "message" : self.message
                   , "error" : self.error
              }

class MethodNotAllowed(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error

    def __str__(self):
    return self.message

    def getMessage():
      response = { "status" : "fail"
                   , "message" : self.message
                   , "error" : self.error
              }

class AuthorizationError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error

    def __str__(self):
    return self.message

    def getMessage():
      response = { "status" : "fail"
                   , "message" : self.message
                   , "error" : self.error
              }

class ParameterError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error

    def __str__(self):
    return self.message

    def getMessage():
      response = { "status" : "fail"git 
                   , "message" : self.message
                   , "error" : self.error
              }