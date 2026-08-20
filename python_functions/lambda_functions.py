"""Live examples for lambda functions."""


def main():
    add = lambda first, second: first + second
    numbers = [1, 2, 3, 4]
    squares = list(map(lambda number: number * number, numbers))
    ordered = sorted(["python", "is", "fun"], key=lambda word: len(word))

    print(add(2, 3))
    print(squares)
    print(ordered)


if __name__ == "__main__":
    main()
