# Generators in Python

**Navigation:** [Python functions plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

## Why do we need generators?

A normal list stores all results immediately. For a very large sequence, that can consume unnecessary memory. A generator produces one value at a time only when requested.

## Think first

Predict the order:

```python
numbers = count_up_to(3)
print(next(numbers))
print(next(numbers))
print(list(numbers))
```

Run `python3 python_functions/generators.py`.

## The idea

A function containing `yield` becomes a generator function. Calling it creates an iterator; it does not run the whole body immediately.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1
```

Visual:

```text
call generator -> paused before first value
next()         -> produce 1 -> pause
next()         -> resume -> produce 2 -> pause
next()         -> resume -> produce 3 -> pause
```

`yield` remembers the function's local state between calls.

## What happens without a generator?

A list version calculates and stores every number before the caller can use the first one. A generator supports streaming and can represent large or even infinite sequences.

## Common mistakes

- Calling a generator function and expecting a value instead of an iterator.
- Forgetting that a generator is exhausted after its values are consumed.
- Calling `next()` after exhaustion without handling `StopIteration`.

## Quick revision

```text
yield -> produce one value, pause, remember state, continue later
```
