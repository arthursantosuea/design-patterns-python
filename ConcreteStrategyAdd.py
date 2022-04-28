import abc
import Strategy
class ConcreteStrategyAdd(Strategy.Strategy):
    @abc.abstractmethod
    def execute(self, pointA, pointB):
        return pointA + pointB