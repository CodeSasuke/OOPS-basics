"""Live examples for map, filter, and reduce."""

from functools import reduce


def main():
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda number: number * 2, numbers))
    evens = list(filter(lambda number: number % 2 == 0, numbers))
    total = reduce(lambda running_total, number: running_total + number, numbers, 0)

    print(f"map: {doubled}")
    print(f"filter: {evens}")
    print(f"reduce: {total}")


if __name__ == "__main__":
    main()
