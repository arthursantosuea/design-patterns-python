import abc
import Strategy

class ConcreteStrategyMultiply(Strategy.Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA * pointB