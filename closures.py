"""Live examples for closures."""


def create_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


def main():
    times_two = create_multiplier(2)
    times_three = create_multiplier(3)
    print(times_two(5))
    print(times_three(5))
    print(f"Remembered values: {times_two.__closure__[0].cell_contents}, {times_three.__closure__[0].cell_contents}")


if __name__ == "__main__":
    main()
