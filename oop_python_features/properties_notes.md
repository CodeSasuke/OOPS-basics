# `property` in Python

**Navigation:** [OOP + Python features plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [Python functions plan](../python_functions/learning_plan.md)

## Why do we need properties?

A plain public attribute is simple, but sometimes reading or changing it needs calculation or validation. Calling `get_fahrenheit()` feels less natural when the value behaves like an attribute.

Without a property, callers may also assign impossible values directly:

```python
temperature.celsius = -300
```

## Think first

Predict:

1. Does `temperature.fahrenheit` call a method?
2. What happens when Celsius is set to `-300`?
3. Why is the public syntax still `temperature.celsius`?

Run `python3 oop_python_features/properties.py`.

## The idea

`@property` lets a method be read like an attribute while keeping logic behind the access.

```python
@property
def fahrenheit(self):
    return self.celsius * 9 / 5 + 32
```

Visual:

```text
temperature.fahrenheit
          |
          v
@property method runs
          |
          v
calculated Fahrenheit value
```

A setter controls assignment:

```python
@celsius.setter
def celsius(self, value):
    validate(value)
    self._celsius = value
```

## What happens without properties?

The caller must remember which getter and setter methods to call, or can bypass validation. Properties preserve a natural attribute interface while enforcing object rules.

## Encapsulation connection

`property` supports encapsulation:

```text
public interface: temperature.celsius
internal storage: self._celsius
control logic:    celsius.setter
```

## Common mistakes

- Recursively assigning `self.celsius` inside its own setter. Store in `_celsius` instead.
- Forgetting that a read-only property has no setter.
- Putting unrelated side effects inside a property getter.

## Quick revision

```text
@property       -> controlled read access
@property.setter -> controlled write access
```
