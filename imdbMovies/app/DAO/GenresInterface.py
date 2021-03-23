from abc import ABCMeta, abstractmethod

class GenresInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def addGenres():
    	pass

    @abstractmethod
    def getGenres():
    	pass


