class Calculator:
    def add(self, number):
        return number + 10
    
calculator = Calculator()

bound_method = calculator.add
print(bound_method(5))       # self is already attached

unbound_method = Calculator.add
print(unbound_method(calculator, 5))  # self must be supplied manually