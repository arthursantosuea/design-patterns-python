import ConcreteStrategyAdd
import ConcreteStrategySubtract
import ConcreteStrategyMultiply
from Context import Context

class Application:
    def __init__(self):
        context = Context()
        pointA = int(input("Digite o primeiro número: "))
        pointB = int(input("Digite o segundo número: "))
        action = input("Digite a operação: ")

        if action == "add":
            context.setStrategy(ConcreteStrategyAdd.ConcreteStrategyAdd())
        elif action == "sub":
            context.setStrategy(ConcreteStrategySubtract.ConcreteStrategySubtract())
        elif action == "mul":
            context.setStrategy(ConcreteStrategyMultiply.ConcreteStrategyMultiply())
        
        result = context.executeStrategy(pointA, pointB)
        print("Result: ", result)
if __name__ == "__main__":
    main = Application()