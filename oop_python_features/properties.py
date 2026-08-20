"""Properties: validate assignment while keeping simple attribute syntax.

Without a property setter, callers could assign an impossible temperature
directly. The solution validates writes in one place and computes Fahrenheit
when it is read.
"""


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value


def without_property():
    class UnsafeTemperature:
        def __init__(self, celsius: float):
            self.celsius = celsius

    temperature = UnsafeTemperature(25)
    temperature.celsius = -300
    print(f"Invalid value is accepted: {temperature.celsius} C")


def main():
    print("WITHOUT A PROPERTY")
    without_property()

    print("\nWITH A PROPERTY")
    temperature = Temperature(25)
    print(f"Celsius: {temperature.celsius}")
    print(f"Fahrenheit: {temperature.fahrenheit}")

    try:
        temperature.celsius = -300
    except ValueError as error:
        print(f"Rejected invalid temperature: {error}")


if __name__ == "__main__":
    main()
