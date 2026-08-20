"""Live examples for generators and lazy iteration."""


def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


def main():
    numbers = count_up_to(3)
    print(type(numbers).__name__)
    print(next(numbers))
    print(next(numbers))
    print(list(numbers))


if __name__ == "__main__":
    main()
