# Inheritance in Python

## Why do we need inheritance?

Suppose `Car`, `Truck`, and `Motorcycle` all have a manufacturer and a `start()` operation. Without inheritance, we repeat the same code in every class.

```text
Car        = make + start + car-specific behavior
Truck      = make + start + truck-specific behavior
Motorcycle = make + start + motorcycle-specific behavior

same vehicle code repeated in many classes
```

Inheritance lets a child class reuse a parent's common behavior and add its own behavior.

## Think first

Before running the example, predict:

1. Can `Car` use `start()` even though `Car` does not define it?
2. What will `electric_car.drive()` do?
3. Is an `ElectricCar` also a `Vehicle`?

Run:

```bash
python3 inheritance.py
```

Expected output:

```text
Honda vehicle starts
Honda car drives
Tesla vehicle starts
Tesla car drives
Tesla electric car charges
Car is a Vehicle: True
```

## The basic idea

```python
class Vehicle:
    def start(self):
        return "Vehicle starts"


class Car(Vehicle):
    pass


print(Car().start())
```

`Car(Vehicle)` means `Car` inherits from `Vehicle`. Python searches `Car` first, then `Vehicle` when looking for `start()`.

```text
Vehicle
  |
  +---- Car
          |
          +---- receives start() from Vehicle
```

## What happens without inheritance?

Every child would need to repeat common methods. If the shared behavior changes, every copy must be updated. Inheritance keeps the shared behavior in one parent class.

## The live example

In [inheritance.py](inheritance.py), `Vehicle` owns the common `make` state and `start()` behavior. `Car` adds `drive()`, and `ElectricCar` inherits from both levels and adds `charge()`.

```python
class Vehicle:
    def __init__(self, make):
        self.make = make

    def start(self):
        return f"{self.make} vehicle starts"


class Car(Vehicle):
    def drive(self):
        return f"{self.make} car drives"
```

Notice that `Car` uses `self.make`, which it received through `Vehicle.__init__`.

## Important vocabulary

- **Parent/base/superclass:** the class being inherited from
- **Child/derived/subclass:** the class that inherits
- **Inherited method:** a method found in a parent
- **Specialized method:** behavior added by the child
- **`isinstance(value, Type)`:** checks whether an object belongs to a type or its ancestors

## Inheritance is an "is-a" relationship

```text
An ElectricCar is a Car.
A Car is a Vehicle.
Therefore, an ElectricCar is a Vehicle.
```

Use inheritance when the child genuinely is a specialized form of the parent. Do not use it only to reuse unrelated code.

## Common mistakes

- Forgetting that a child may inherit state only if the parent initializer runs.
- Creating deep hierarchies when composition would be clearer.
- Assuming inheritance means every parent behavior is appropriate for every child.
- Calling something an `is-a` relationship when it is really a `has-a` relationship.

## Quick revision

```text
class Child(Parent):
    ...

Child gets Parent behavior.
Python searches Child before Parent.
A child can add behavior or override inherited behavior.
```
