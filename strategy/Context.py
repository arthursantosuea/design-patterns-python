class Context:
    def setStrategy(self, strategy):
        self.strategy = strategy
    def executeStrategy(self, pointA, pointB):
        return self.strategy.execute(pointA, pointB)