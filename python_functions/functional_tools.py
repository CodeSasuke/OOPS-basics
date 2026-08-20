"""Functional tools: transform collections without manual loops.

Without these tools, each transformation needs a separate loop and result
list. ``map``, ``filter``, and ``reduce`` provide reusable operations for
transforming, selecting, and combining values.
"""

from functools import reduce


def main():
    print("Without functional tools, three separate loops would be needed")
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda number: number * 2, numbers))
    evens = list(filter(lambda number: number % 2 == 0, numbers))
    total = reduce(lambda running_total, number: running_total + number, numbers, 0)

    print(f"map: {doubled}")
    print(f"filter: {evens}")
    print(f"reduce: {total}")


if __name__ == "__main__":
    main()
