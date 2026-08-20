# Abstraction in Python

## Why do we need abstraction?

A caller often needs to know what an object can do, not how it does it. A report can ask a shape for its `area()` without knowing whether the shape is a square or a circle.

Without abstraction, code may depend on implementation details:

```python
if shape.type == "square":
    return shape.side * shape.side
```

Every new shape requires another branch. An abstract interface defines the operation once.

## Think first

Before running [abstraction.py](abstraction.py), predict:

1. Can `Square` and `Circle` both be stored as `Shape` objects?
2. Can you create `Shape()` directly?
3. What must every concrete shape implement?

Run:

```bash
python3 abstraction.py
```

Expected output:

```text
Square area = 16
Circle area = 12.56
Abstract class rejected: TypeError
```

## The central idea

`Shape` defines a required operation, while each concrete class supplies the implementation:

```text
Shape
  |
  +-- required: area()
       |
       +-- Square.area()
       +-- Circle.area()
```

The abstract class is a contract. It is not a complete concrete object.

## The `abc` tools

```python
from abc import ABC, abstractmethod
```

- `ABC` marks a class as an abstract base class.
- `@abstractmethod` marks a method that subclasses must implement.
- A concrete subclass is instantiable only after it implements every abstract method.

The live example uses:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError
```

The `raise` line is a defensive body. Python still prevents direct construction because `area` is abstract.

## Encapsulation versus abstraction

```text
Encapsulation: protect the object's internal state.
Abstraction: define what behavior callers can rely on.
```

They often work together, but they solve different problems.

## Try the contract

Create this class and observe the error:

```python
class Triangle(Shape):
    pass


Triangle()
```

Then implement `area()` and run it again. This experiment shows that an abstract class enforces a required behavior.

## Common mistakes

- Treating an abstract class as a class that can never have useful concrete subclasses.
- Forgetting to implement every abstract method.
- Confusing abstraction with simply hiding data.
- Adding abstract methods that do not represent a real shared contract.

## Quick revision

```text
ABC + abstractmethod = required interface

Abstract base class -> describes the contract
Concrete subclass   -> implements the contract
Caller              -> uses the contract, not the implementation details
```
