# OOP + Python Features Learning Plan

This folder teaches Python features that connect functions, descriptors, and classes. These topics come after the Core OOP and Python function foundations.

## Teaching convention

For each feature:

```text
1. Understand the ordinary class or function first.
2. Predict what the decorator or descriptor changes.
3. Run the live example.
4. Expand the syntax into its equivalent form.
5. Compare it with nearby features.
6. Modify the example and rerun.
```

## Learning order

### 1. `staticmethod`

Files:

- [static_methods.py](static_methods.py)
- [method_example.py](../core_oop/method_example.py)

Prerequisites: classes, methods, `self`, and standalone functions.

Question: what if a function belongs conceptually to a class but does not need an object or class?

```python
class MathTools:
    @staticmethod
    def add(first, second):
        return first + second
```

No `self` or `cls` is supplied.

Run:

```bash
python3 oop_python_features/static_methods.py
```

Compare:

```text
instance method -> self
classmethod     -> cls
staticmethod    -> neither
```

### 2. `classmethod`

Files:

- [cls_.py](cls_.py)
- [cls_notes.md](cls_notes.md)

Prerequisites: classes, `self`, inheritance, class state, and decorators.

Question: how can one method create an object of whichever class called it?

```python
class Student:
    @classmethod
    def from_text(cls, text):
        name, course = text.split(",")
        return cls(name.strip(), course.strip())
```

Run:

```bash
python3 oop_python_features/cls_.py
```

Visual:

```text
Student.from_text(...)       -> cls is Student
OnlineStudent.from_text(...) -> cls is OnlineStudent
```

### 3. `property`

Files:

- [properties.py](properties.py)
- [properties_notes.md](properties_notes.md)

Prerequisites: encapsulation, methods, validation, and controlled state.

Question: how can method logic look like ordinary attribute access?

```python
class Temperature:
    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32
```

Run:

```bash
python3 oop_python_features/properties.py
```

Visual:

```text
temperature.fahrenheit -> property getter -> calculated value
```

Then teach a setter and validation.

### 4. Method decorators

Files:

- [decorators_methods_functions.py](../python_functions/decorators_methods_functions.py)
- [decorators_notes.md](../python_functions/decorators_notes.md)
- [decorators_methods_functions_interview.md](../python_functions/decorators_methods_functions_interview.md)

Prerequisites: decorators, `*args`, `**kwargs`, method binding, `self`, `classmethod`, and `staticmethod`.

Question: why must a method decorator forward the instance as part of `args`?

```text
calculator.multiply(4, 5)
        |
        v
wrapper(calculator, 4, 5)
        |
        v
multiply(calculator, 4, 5)
```

Run:

```bash
python3 python_functions/decorators_methods_functions.py
```

Compare decorator placement around `@classmethod` and `@staticmethod`.

### 5. Class decorators

Files:

- [class_decorators.py](class_decorators.py)
- [class_decorators_notes.md](class_decorators_notes.md)

Prerequisites: classes, callable objects, first-class functions, and decorators.

Question: what does a decorator receive when it is placed above a class?

```python
def add_label(cls):
    cls.category = "model"
    return cls
```

This syntax:

```python
@add_label
class User:
    pass
```

means:

```python
User = add_label(User)
```

Run:

```bash
python3 oop_python_features/class_decorators.py
```

## Comparison table

| Feature | Receives automatically | Main purpose |
| --- | --- | --- |
| Instance method | `self` | Work with one object's state |
| `classmethod` | `cls` | Work with class state or create objects |
| `staticmethod` | Nothing | Group related utility behavior |
| `property` | `self` through attribute access | Controlled calculated read/write |
| Method decorator | Existing method arguments | Add reusable method behavior |
| Class decorator | Class object | Register or modify a class |

## Completion checklist

- [ ] I can explain why a static method does not receive `self`.
- [ ] I can explain why a class method receives `cls`.
- [ ] I can use `cls(...)` for subclass-friendly factories.
- [ ] I can explain a property getter and setter.
- [ ] I can forward method arguments through a decorator.
- [ ] I can expand a class decorator into `Class = decorator(Class)`.
- [ ] I can compare methods, static methods, class methods, and properties.
