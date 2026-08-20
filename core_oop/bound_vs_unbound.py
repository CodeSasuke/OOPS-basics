"""Beginner notes: bound and unbound methods.

A bound method is connected to a particular object. When it is called,
Python automatically passes that object as ``self``.

When a method is accessed through the class, it is not connected to an
object. We must pass the object ourselves as the first argument.

Without binding, every object call would require manually passing the
instance. Python's descriptor behavior creates a bound method for us.
"""


class Calculator:
    def add(self, number):
        return number + 10

calculator = Calculator()

print("WITHOUT AUTOMATIC BINDING")
try:
    Calculator.add(5)
except TypeError as error:
    print(f"Class access without self fails: {error}")

print("\nWITH AUTOMATIC BINDING")

# Accessing add through the object creates a bound method.
# calculator is already attached as self, so only number is provided.
bound_method = calculator.add
print(bound_method(5))

# Accessing add through the class does not attach self.
# The calculator object must be provided explicitly.
unbound_method = Calculator.add
print(unbound_method(calculator, 5))

# This would raise a TypeError because self is missing:
# print(unbound_method(5))

# These calls are equivalent:
print(calculator.add(5))
print(Calculator.add(calculator, 5))