"""Live examples for the property decorator."""


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


def main():
    temperature = Temperature(25)
    print(f"Celsius: {temperature.celsius}")
    print(f"Fahrenheit: {temperature.fahrenheit}")

    try:
        temperature.celsius = -300
    except ValueError as error:
        print(f"Rejected invalid temperature: {error}")


if __name__ == "__main__":
    main()
