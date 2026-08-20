# Python Functions Learning Plan

**Navigation:** [Back to main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

This folder teaches function behavior independently of OOP. Decorators are included here first because they depend on first-class functions, closures, and flexible arguments.

## Teaching convention

For every topic:

```text
predict -> run -> observe -> explain -> modify -> rerun -> summarize
```

Always explain syntax before using it in a larger example. Use named `def` functions first; introduce shorter or more advanced syntax only after the underlying behavior is understood.

## Learning order

### 1. Basic functions

File:

- [function_example.py](function_example.py)

Learn parameters, return values, calls, and the difference between a function object and a function call.

Run:

```bash
python3 python_functions/function_example.py
```

Questions:

- What is passed into a function?
- What is returned?
- What is the difference between `add` and `add()`?

### 2. First-class functions

Start with the function-object section in [decorators_notes.md](decorators_notes.md).

A function can be assigned, passed, returned, stored, and inspected.

```python
def run(operation):
    return operation(2, 3)
```

Visual:

```text
function object -> argument -> another function -> result
```

Checkpoint: pass both `add` and `multiply` into `run()`.

### 3. Positional and keyword arguments

Before decorators, teach:

```python
def show(*args, **kwargs):
    print(args)
    print(kwargs)
```

Explain:

```text
*args   -> tuple of positional values
**kwargs -> dictionary of named values
```

Then teach unpacking:

```python
function(*values)
function(**named_values)
```

The complete lesson is in [decorators_notes.md](decorators_notes.md).

### 4. Closures

Files:

- [closures.py](closures.py)
- [closures_notes.md](closures_notes.md)

Questions:

- What value does the inner function remember?
- How can it remember that value after the outer function returns?

Run:

```bash
python3 python_functions/closures.py
```

Visual:

```text
create_multiplier(3) -> inner function remembers factor = 3
```

### 5. Lambda functions

Files:

- [lambda_functions.py](lambda_functions.py)
- [lambda_notes.md](lambda_notes.md)

Teach lambda as a small anonymous function only after `def` and function objects.

```python
lambda number: number * number
```

Run:

```bash
python3 python_functions/lambda_functions.py
```

Checkpoint: rewrite one lambda as a named `def` and compare readability.

### 6. `map`, `filter`, and `reduce`

Files:

- [functional_tools.py](functional_tools.py)
- [functional_tools_notes.md](functional_tools_notes.md)

Teach the three jobs:

```text
map    -> transform every item
filter -> keep matching items
reduce -> combine many items into one result
```

Run:

```bash
python3 python_functions/functional_tools.py
```

Explain why `map` and `filter` are converted to `list`, and why `reduce` comes from `functools`.

### 7. Decorators

Files:

- [decorators_notes.md](decorators_notes.md)
- [decorators_methods_functions.py](decorators_methods_functions.py)
- [decorators_methods_functions_interview.md](decorators_methods_functions_interview.md)

Teach in this exact order:

```text
motivation
  -> repeated behavior without decorators
  -> function objects
  -> closures
  -> args and kwargs
  -> @decorator syntax
  -> @wraps
  -> method decorators
```

Run:

```bash
python3 python_functions/decorators_methods_functions.py
```

Checkpoint: add a timing or tracing decorator without changing `add()`.

### 8. Generators

Files:

- [generators.py](generators.py)
- [generators_notes.md](generators_notes.md)

Teach `yield`, lazy evaluation, `next()`, pausing, resuming, and exhaustion.

Run:

```bash
python3 python_functions/generators.py
```

Visual:

```text
next() -> produce one value -> pause
next() -> resume -> produce next value -> pause
```

## Completion checklist

- [ ] I can distinguish a function object from its returned value.
- [ ] I can pass a function into another function.
- [ ] I can explain packing and unpacking with `*args` and `**kwargs`.
- [ ] I can explain what a closure remembers.
- [ ] I know when a lambda improves clarity and when `def` is better.
- [ ] I can distinguish map, filter, and reduce.
- [ ] I can explain decorators as reusable wrappers.
- [ ] I can explain why `@wraps` preserves metadata.
- [ ] I can explain how a generator pauses and resumes.

**Navigation:** [Back to main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)
