import abc
from Strategy import Strategy
class ConcreteStrategyAdd(Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA + pointB