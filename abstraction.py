"""Live examples for abstraction with the abc module."""

from abc import ABC, abstractmethod


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
    for shape in (Square(4), Circle(2)):
        print(shape.describe())

    try:
        Shape()
    except TypeError as error:
        print(f"Abstract class rejected: {error.__class__.__name__}")


if __name__ == "__main__":
    main()
