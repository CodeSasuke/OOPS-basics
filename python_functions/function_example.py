"""Functions: name a reusable solution instead of repeating an expression.

Without a function, every caller would rewrite ``a + b`` and any later rule
change would need many edits. The final example centralizes that behavior in
``add``.
"""


def add(a: int, b: int) -> int:
    return a + b

def main():
    print("WITHOUT A FUNCTION")
    print(5 + 3)
    print("The addition rule is repeated directly in the caller")

    print("\nWITH A FUNCTION")
    result = add(5, 3)
    print(result)


if __name__ == "__main__":
    main()