class Context:
    # def __init__(self, strategy):
    #     self.strategy = strategy
    def setStrategy(self, strategy):
        self.strategy = strategy
    def executeStrategy(self, pointA, pointB):
        return self.strategy.execute(pointA, pointB)