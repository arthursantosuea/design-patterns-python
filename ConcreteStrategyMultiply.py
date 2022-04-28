import abc
from Strategy import Strategy

class ConcreteStrategyMultiply(Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA * pointB