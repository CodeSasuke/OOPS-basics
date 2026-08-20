# `map`, `filter`, and `reduce`

**Navigation:** [Python functions plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

## Why do we need these tools?

Programs often need to transform every item, keep only matching items, or combine many items into one result. These tools express those three jobs directly.

## Think first

For `[1, 2, 3, 4, 5]`, predict:

```text
map    -> double every number
filter -> keep even numbers
reduce -> add all numbers
```

Run `python3 python_functions/functional_tools.py`.

## The three operations

```text
map    : one item in -> one changed item out
filter : one item in -> keep/discard decision
reduce : running result + one item -> one final result
```

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda number: number * 2, numbers))
evens = list(filter(lambda number: number % 2 == 0, numbers))
total = reduce(lambda result, number: result + number, numbers, 0)
```

`map` and `filter` return lazy iterator objects, so `list(...)` makes their values visible immediately. `reduce` needs the `functools` import because it combines values into one result.

## Common mistakes

- Forgetting to consume a `map` or `filter` iterator.
- Using `reduce` when a simple `sum()` is clearer.
- Writing a lambda that is harder to understand than a loop.

## Quick revision

```text
map    = transform
filter = select
reduce = combine
```
