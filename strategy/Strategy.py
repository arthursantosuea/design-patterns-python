import abc

class Strategy:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, pointA, pointB):
        pass