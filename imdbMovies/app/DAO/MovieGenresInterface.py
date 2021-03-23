from abc import ABCMeta, abstractmethod

class MovieGenresInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def addMovieGenres():
    	pass

    @abstractmethod
    def getByGenre():
    	pass

    @abstractmethod
    def getByMovie():
    	pass


