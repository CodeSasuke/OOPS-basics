# Lambda Functions in Python

## Why do we need `lambda`?

Some operations are tiny and used only once, especially when passing behavior to `map`, `sorted`, or another function. Naming every tiny operation can add noise.

## Think first

Predict the squares produced by:

```python
list(map(lambda number: number * number, [1, 2, 3, 4]))
```

Run `python3 lambda_functions.py`.

## The syntax

```python
lambda parameters: expression
```

This:

```python
add = lambda first, second: first + second
```

is similar to:

```python
def add(first, second):
    return first + second
```

A lambda has one expression and returns its result automatically.

## When to use it

```python
sorted(words, key=lambda word: len(word))
```

The lambda tells `sorted` what value to use for comparison.

## When not to use it

Use `def` when the logic needs multiple statements, a meaningful name, a docstring, validation, or debugging. Short is not always clearer.

## Common mistakes

- Trying to put statements in a lambda.
- Using deeply nested lambdas.
- Using lambda when a named function would explain the program better.

## Quick revision

```text
lambda = small anonymous function with one expression
```
