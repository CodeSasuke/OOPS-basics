# Closures in Python

## Why do we need closures?

Sometimes a function needs a value that should stay private and remembered between the moment it is created and the moment it is called. Passing that value manually every time is repetitive.

## Think first

Predict:

```python
times_two = create_multiplier(2)
print(times_two(5))
```

Where does `times_two` get the value `2` after `create_multiplier` has finished?

Run `python3 closures.py`.

## The idea

A closure is an inner function plus the values from its enclosing scope that it remembers.

```python
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply
```

Visual:

```text
create_multiplier(3)
        |
        +-- factor = 3
        +-- returns multiply
                    |
                    +-- remembers factor = 3

multiply(4) -> 4 * 3 -> 12
```

The outer function has finished, but the returned function still has access to `factor`.

## Why this matters for decorators

A decorator's wrapper remembers the original function:

```text
wrapper closure -> original function
```

That is why the wrapper can call the function later.

## Common mistakes

- Confusing a closure with a global variable.
- Assuming the enclosing value disappears when the outer function returns.
- Creating closures in a loop without understanding late binding.

## Quick revision

```text
closure = inner function + remembered enclosing values
```
