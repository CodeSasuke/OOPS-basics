"""Lambda functions: small one-use functions where a name adds no value.

Without a lambda, short callbacks for ``map`` and ``sorted`` need several
named functions scattered away from the operation. The solution keeps tiny
expressions close to the call that uses them.
"""


def main():
    print("Without lambdas, every tiny callback would need a separate name")
    add = lambda first, second: first + second
    numbers = [1, 2, 3, 4]
    squares = list(map(lambda number: number * number, numbers))
    ordered = sorted(["python", "is", "fun"], key=lambda word: len(word))

    print(add(2, 3))
    print(squares)
    print(ordered)


if __name__ == "__main__":
    main()
