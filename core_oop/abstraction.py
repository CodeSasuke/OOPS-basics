"""Abstraction: first the problem, then the solution.

Without abstraction, every caller must know which concrete calculation to
perform. That makes code that works with several shapes grow a new condition
for every shape and makes missing implementations easy to overlook.

The solution is an abstract ``Shape`` contract. Code can ask every shape for
its area without knowing how that area is calculated. ``ABC`` and
``@abstractmethod`` also stop incomplete shapes from being created.
"""

from abc import ABC, abstractmethod


def problem_without_abstraction():
    """Show the repeated type checks the solution removes."""
    shapes = [("square", 4), ("circle", 2)]
    areas = []
    for shape, value in shapes:
        if shape == "square":
            areas.append(value * value)
        elif shape == "circle":
            areas.append(3.14 * value * value)
    print(f"Without abstraction, the caller owns the rules: {areas}")


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the shape's area."""
        raise NotImplementedError

    def describe(self):
        return f"{type(self).__name__} area = {self.area()}"


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius


def main():
    problem_without_abstraction()

    for shape in (Square(4), Circle(2)):
        print(shape.describe())

    try:
        Shape()
    except TypeError as error:
        print(f"Abstract class rejected: {error.__class__.__name__}")


if __name__ == "__main__":
    main()
