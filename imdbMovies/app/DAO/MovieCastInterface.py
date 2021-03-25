from abc import ABCMeta, abstractmethod

class MovieCastInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def addMovieCast():
    	pass

    @abstractmethod
    def getMovieCast():
    	pass


