import abc
from Strategy import Strategy

class ConcreteStrategySubtract(Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA - pointB