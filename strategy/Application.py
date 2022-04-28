from ConcreteStrategyAdd import ConcreteStrategyAdd
from ConcreteStrategySubtract import ConcreteStrategySubtract
from ConcreteStrategyMultiply import ConcreteStrategyMultiply
from Context import Context

class Application:
    def __init__(self):
        context = Context()
        pointA = int(input("Digite o primeiro número: "))
        pointB = int(input("Digite o segundo número: "))
        action = input("Digite a operação: ")

        if action == "add":
            context.setStrategy(ConcreteStrategyAdd())
        elif action == "sub":
            context.setStrategy(ConcreteStrategySubtract())
        elif action == "mul":
            context.setStrategy(ConcreteStrategyMultiply())
        
        result = context.executeStrategy(pointA, pointB)
        print("Result: ", result)
if __name__ == "__main__":
    main = Application()