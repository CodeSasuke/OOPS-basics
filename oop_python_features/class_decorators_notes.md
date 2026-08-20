# Class Decorators in Python

**Navigation:** [OOP + Python features plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [Python functions plan](../python_functions/learning_plan.md)

## Why do we need class decorators?

A class decorator solves the same reuse problem as a function decorator, but it receives a class object. It can register a class, add metadata, or modify the class after its definition.

Without a class decorator, registration is easy to forget:

```python
class Report:
    pass

registry.append(Report)  # repeated manual step
```

## Think first

Predict:

1. What does `@add_model_metadata` receive?
2. Does it create a User object?
3. What will `User.category` print?

Run `python3 oop_python_features/class_decorators.py`.

## The syntax

```python
def add_label(cls):
    cls.category = "model"
    return cls


@add_label
class User:
    pass
```

This means:

```python
class User:
    pass


User = add_label(User)
```

Visual:

```text
class User definition
        |
        v
add_model_metadata(User)
        |
        +-- adds category
        +-- adds describe
        +-- returns User
```

The decorator receives the class itself, not an instance.

## What happens without a class decorator?

Metadata, registration, or setup code must be repeated after every class definition. A decorator centralizes that class-level setup.

## Registration example

The live file also uses:

```python
def register(cls):
    registry.append(cls)
    return cls
```

The `Report` class is added to `registry` when Python creates the decorated class. This is useful for plugin systems, command registries, serializers, and framework discovery.

## Class decorator versus metaclass

Start with class decorators because they are easier to see: a class decorator receives a finished class and returns it. Metaclasses control class creation itself and should be introduced much later, if needed.

## Common mistakes

- Forgetting to return the class, which replaces the class name with `None`.
- Confusing a class decorator with an instance decorator.
- Adding hidden behavior that makes the class difficult to understand.
- Using a class decorator when a normal base class or explicit function is clearer.

## Quick revision

```text
function decorator: receives function -> returns callable
class decorator:    receives class    -> returns class
```
