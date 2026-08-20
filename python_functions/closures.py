"""Closures: preserve data after the outer function returns.

Without a closure, a multiplier would need a global variable or repeated
arguments to remember its factor. The solution returns an inner function
that keeps the needed value in its enclosing scope.
"""


def create_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


def multiply_without_closure(number, factor):
    return number * factor


def main():
    print("WITHOUT A CLOSURE")
    print(multiply_without_closure(5, 2))
    print("The factor must be passed again for every call")

    print("\nWITH A CLOSURE")
    times_two = create_multiplier(2)
    times_three = create_multiplier(3)
    print(times_two(5))
    print(times_three(5))
    print(f"Remembered values: {times_two.__closure__[0].cell_contents}, {times_three.__closure__[0].cell_contents}")


if __name__ == "__main__":
    main()
