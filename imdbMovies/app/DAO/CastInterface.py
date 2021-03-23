from abc import ABCMeta, abstractmethod

class CastInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def addCast():
    	pass

    @abstractmethod
    def getCast():
    	pass


