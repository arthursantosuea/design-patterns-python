import abc
import Strategy

class ConcreteStrategySubtract(Strategy.Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA - pointB