# `__get__` and Method Binding in Python

**Navigation:** [Core OOP plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Python functions plan](../python_functions/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

## Where this topic belongs

This is an advanced topic in Core OOP. Learn it after:

```text
classes and objects
        |
        v
self and instance methods
        |
        v
bound and unbound method calls
        |
        v
__get__ and descriptors
```

You do not need to understand `__get__` before using ordinary methods. It explains the mechanism Python uses underneath ordinary method binding.

## Why do we need `__get__`?

Consider these two calls:

```python
calculator.add(5)
Calculator.add(calculator, 5)
```

They produce the same result, even though the first call appears to pass only one argument. Python automatically supplies `calculator` as `self` when the method is accessed through the object.

The question is:

```text
How does Python know when to add self?
```

The answer is the **descriptor protocol**. Functions stored in classes provide a `__get__` method. Python calls that method when the function is accessed through a class or an object.

## Think before running

Open [__get__.py](__get__.py) and predict:

1. What will happen when `Greeter.greet` is accessed through the class?
2. What will happen when `greeter.greet` is accessed through an instance?
3. Which access receives an instance argument?
4. Why can `greeter.greet("Hello")` omit `self`?

Run from the repository root:

```bash
python3 core_oop/__get__.py
```

Expected output:

```text
Normal Python method behavior:
__get__: accessed through Greeter instance
Asha says: Hello
__get__: accessed through Greeter
Asha says: Hello again

Descriptor behavior:
__get__: accessed through Greeter
Class access returns: function
Ravi says: Class call
__get__: accessed through Greeter instance
Instance access returns: function
Ravi says: Instance call
```

## What is a descriptor?

A descriptor is an object that controls what happens when an attribute is read, written, or deleted. A class can define special methods such as:

```text
__get__ -> controls reading an attribute
__set__ -> controls assigning an attribute
__delete__ -> controls deleting an attribute
```

This lesson focuses on `__get__`.

A descriptor is placed in a class. When Python evaluates an attribute access, it can ask the descriptor what value should be returned.

```text
object.attribute
       |
       v
Python finds descriptor in the class
       |
       v
descriptor.__get__(object, class)
       |
       v
returned value
```

## The two forms of access

### Access through the class

```python
Greeter.greet
```

Python calls the descriptor approximately like this:

```python
 descriptor.__get__(None, Greeter)
```

There is no particular object, so `instance` is `None`. Python returns the original function. The caller must provide the object manually:

```python
Greeter.greet(greeter, "Hello")
```

### Access through an instance

```python
greeter.greet
```

Python calls the descriptor approximately like this:

```python
descriptor.__get__(greeter, Greeter)
```

This time, `instance` is the `greeter` object. The descriptor returns a new callable that remembers `greeter` and supplies it as the first argument later:

```python
greeter.greet("Hello")
```

is conceptually similar to:

```python
Greeter.greet(greeter, "Hello")
```

## The `__get__` signature

The live descriptor has this method:

```python
def __get__(self, instance, owner):
    ...
```

The names mean:

| Parameter | Meaning |
| --- | --- |
| `self` | The descriptor object itself |
| `instance` | The object through which the attribute was accessed, or `None` for class access |
| `owner` | The class that owns the attribute lookup |

Visual:

```text
Greeter.greet
      |
      +--> instance = None
      +--> owner = Greeter

ravi.greet
      |
      +--> instance = ravi
      +--> owner = Greeter
```

## Building the descriptor step by step

The descriptor stores the original function:

```python
class MethodDescriptor:
    def __init__(self, function):
        self.function = function
```

For class access, return the original function:

```python
def __get__(self, instance, owner):
    if instance is None:
        return self.function
```

For instance access, return a wrapper that supplies the instance:

```python
def __get__(self, instance, owner):
    if instance is None:
        return self.function

    def bound_method(*args, **kwargs):
        return self.function(instance, *args, **kwargs)

    return bound_method
```

The returned `bound_method` is a closure. It remembers `instance` after `__get__` returns.

```text
ravi.greet
   |
   v
__get__(ravi, Greeter)
   |
   +-- creates bound_method
   |       remembers ravi
   |
   +-- returns bound_method
           |
           v
bound_method("Hello")
   |
   v
original_greet(ravi, "Hello")
```

## How the live class uses it

Inside [__get__.py](__get__.py), the original function is wrapped by `MethodDescriptor` inside the class body:

```python
class Greeter:
    def greet(self, message):
        return f"{self.name} says: {message}"

    greet = MethodDescriptor(greet)
```

The name `greet` first refers to the normal function. Then the class body replaces that name with a `MethodDescriptor` containing the function.

```text
normal greet function
        |
        v
MethodDescriptor(greet)
        |
        v
Greeter.greet stores the descriptor
```

The descriptor then controls future class and instance access.

## Normal functions already behave this way

You normally do not write a descriptor for every method because Python function objects already implement the descriptor behavior. That is why this ordinary class works:

```python
class Calculator:
    def add(self, first, second):
        return first + second
```

Python effectively performs descriptor work when evaluating:

```python
calculator.add
```

The function's descriptor returns a bound method containing `calculator` as `self`.

## Compare all three expressions

```python
calculator.add(2, 3)
Calculator.add(calculator, 2, 3)
```

These are equivalent calls.

But this expression only retrieves a callable:

```python
calculator.add
```

It does not execute the method yet. Attribute access triggers `__get__`; parentheses trigger the returned callable.

```text
calculator.add       -> retrieve bound method
calculator.add(...)  -> retrieve bound method, then call it
```

## Why `instance` can be `None`

The same attribute can be accessed through a class or an object:

```python
Greeter.greet  # no object selected
ravi.greet     # ravi selected
```

The descriptor must distinguish those cases. The standard test is:

```python
if instance is None:
    return self.function
```

Use `is None`, not `== None`, because `None` is a singleton and identity is the correct test.

## Connection to `staticmethod` and `classmethod`

These built-in decorators also use descriptor behavior:

```text
normal method   -> bind instance as self
staticmethod    -> do not bind self or cls
classmethod     -> bind class as cls
```

That is why method binding, `staticmethod`, and `classmethod` belong to the same deeper Python mechanism.

## What happens without the descriptor behavior?

If Python returned the raw function for instance access, this would fail:

```python
calculator.add(2, 3)
```

The raw function expects `self`, `first`, and `second`, but the caller supplied only `2` and `3`. The descriptor creates the bound callable that fills the missing `self`.

```text
without binding:
add(2, 3) -> 2 becomes self, 3 becomes first, second is missing

with binding:
add(calculator, 2, 3) -> every parameter is supplied
```

## Common mistakes

- Thinking `__get__` is called only when a method is executed. It is called during attribute access, before the call.
- Forgetting that class access passes `instance=None`.
- Returning the descriptor itself instead of a useful callable.
- Forgetting to pass the instance to the original function.
- Assuming every descriptor must be a method descriptor. `property`, `classmethod`, and `staticmethod` are also descriptor-based features.
- Starting with descriptors before explaining ordinary method calls and `self`.

## Quick revision

```text
Descriptor = object that controls attribute access

__get__(instance, owner):
    instance is None -> class access -> return original function
    instance exists  -> object access -> return callable with self bound
```

The key equivalence is:

```python
object.method(arguments)

# conceptually becomes

Class.method(object, arguments)
```

The descriptor protocol is the mechanism that makes this automatic binding possible.
