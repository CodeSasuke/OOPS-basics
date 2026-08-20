# Polymorphism in Python

**Navigation:** [Core OOP plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Python functions plan](../python_functions/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

## Why do we need polymorphism?

Imagine a program that must make many objects speak. Without polymorphism, the caller may need to know every concrete type:

```python
if type(thing) is Dog:
    thing.bark()
elif type(thing) is Cat:
    thing.meow()
elif type(thing) is Robot:
    thing.beep()
```

This grows whenever a new type is added. Polymorphism lets the caller ask every object for the same operation, such as `speak()`, without checking its type.

## Think first

Predict the output before running:

```python
for thing in (Dog(), Cat(), Robot()):
    make_speak(thing)
```

Question: does `make_speak` need three branches?

Run:

```bash
python3 core_oop/polymorphism.py
```

Expected output:

```text
Dog: Bark
Cat: Meow
Robot: Beep
```

## The central idea

```python
def make_speak(thing):
    print(thing.speak())
```

The function depends on the behavior `speak()`, not on one specific class.

```text
make_speak(Dog())   -> Dog.speak()   -> Bark
make_speak(Cat())   -> Cat.speak()   -> Meow
make_speak(Robot()) -> Robot.speak() -> Beep
```

The same call has different results because the object supplies the implementation.

## What happens without polymorphism?

The caller becomes coupled to every class. Adding `Bird` requires editing the caller. With polymorphism, adding a class that supports `speak()` does not require changing `make_speak`.

## Two Python forms

### Method overriding

A child class replaces a parent's method:

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Bark"
```

### Duck typing

Python often cares whether an object supports the requested operation rather than whether it belongs to a particular inheritance tree. `Robot` in the live example does not inherit from `Animal`, but it still works because it has `speak()`.

```text
required interface: speak()

Dog    -> has speak()
Cat    -> has speak()
Robot  -> has speak()
```

## Try a new type

Add this class without changing `make_speak`:

```python
class Parrot:
    def speak(self):
        return "Hello"
```

Then call `make_speak(Parrot())`. This is the test that proves the function depends on behavior, not type names.

## Common mistakes

- Confusing polymorphism with inheritance only. Duck typing can provide polymorphism too.
- Checking every concrete type instead of asking for the shared operation.
- Giving classes methods with inconsistent meaning or incompatible arguments.
- Forgetting that a missing method causes `AttributeError`.

## Quick revision

```text
one interface + many implementations = polymorphism

Caller: thing.speak()
Object: decides which speak() runs
```
