"""Inheritance: solve repeated behavior by sharing a parent contract.

Without inheritance, every vehicle class would repeat ``make`` storage and
the ``start`` behavior. The solution is to place common behavior in
``Vehicle`` and let specialized classes add only what they need.
"""


class Vehicle:
    def __init__(self, make: str):
        self.make = make

    def start(self):
        return f"{self.make} vehicle starts"


class Car(Vehicle):
    def drive(self):
        return f"{self.make} car drives"


class ElectricCar(Car):
    def charge(self):
        return f"{self.make} electric car charges"


def main():
    print("Without inheritance, Car and ElectricCar would duplicate start()")
    car = Car("Honda")
    electric_car = ElectricCar("Tesla")

    print(car.start())
    print(car.drive())
    print(electric_car.start())
    print(electric_car.drive())
    print(electric_car.charge())
    print(f"Car is a Vehicle: {isinstance(car, Vehicle)}")


if __name__ == "__main__":
    main()
