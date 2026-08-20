"""Generators: produce values only when they are requested.

Without a generator, a large sequence would be built fully in memory before
the caller could use its first value. ``yield`` pauses the function and
allows the solution to produce one value at a time.
"""


def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


def main():
    print("Without lazy iteration, all values would be built at once")
    numbers = count_up_to(3)
    print(type(numbers).__name__)
    print(next(numbers))
    print(next(numbers))
    print(list(numbers))


if __name__ == "__main__":
    main()
