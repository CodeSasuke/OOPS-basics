"""Functional tools: transform collections without manual loops.

Without these tools, each transformation needs a separate loop and result
list. ``map``, ``filter``, and ``reduce`` provide reusable operations for
transforming, selecting, and combining values.
"""

from functools import reduce


def without_functional_tools(numbers):
    doubled = []
    evens = []
    total = 0
    for number in numbers:
        doubled.append(number * 2)
        if number % 2 == 0:
            evens.append(number)
        total += number
    return doubled, evens, total


def main():
    numbers = [1, 2, 3, 4, 5]
    print("WITHOUT FUNCTIONAL TOOLS")
    print(without_functional_tools(numbers))

    print("\nWITH FUNCTIONAL TOOLS")
    doubled = list(map(lambda number: number * 2, numbers))
    evens = list(filter(lambda number: number % 2 == 0, numbers))
    total = reduce(lambda running_total, number: running_total + number, numbers, 0)

    print(f"map: {doubled}")
    print(f"filter: {evens}")
    print(f"reduce: {total}")


if __name__ == "__main__":
    main()
