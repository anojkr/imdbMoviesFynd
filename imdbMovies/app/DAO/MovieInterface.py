from abc import ABCMeta, abstractmethod

class MovieInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def addMovies():
    	pass

    @abstractmethod
    def getMovieList():
    	pass

    @abstractmethod
    def deleteMovie():
    	pass