# Python and OOP Learning Roadmap

This roadmap organizes the `OOPS-basics` folder into three connected tracks:

1. **Core OOP:** the object-oriented ideas themselves
2. **Python functions:** function behavior that is useful beyond OOP
3. **OOP + Python features:** Python features that connect functions and classes

Every topic in this roadmap is taught with the repository convention: motivation first, the problem without the concept, a Socratic prediction, runnable code, observed output, visuals, common mistakes, and quick revision.

The order is beginner-first. Each topic should answer this sequence:

```text
Why is this needed?
        |
What problem exists without it?
        |
How does the idea solve that problem?
        |
How does Python implement it?
        |
What code can we run?
        |
What mistakes should we avoid?
```

## Recommended teaching order

### Phase 0: Python foundations

Before OOP, make sure the learner is comfortable with variables, strings, numbers, collections, conditionals, loops, function calls, parameters, return values, and imports.

Existing starting point:

- [function_example.py](function_example.py): a minimal function with parameters, a return value, and a call

### Phase 1: Core OOP

Teach these as the main OOP sequence:

```text
1. Classes and objects
2. __init__ and object state
3. self and instance methods
4. Method binding and descriptors
5. Encapsulation
6. Inheritance
7. Polymorphism and method overriding
8. Abstraction
9. Multiple inheritance and MRO
```

#### 1. Classes and objects

**Goal:** Understand that a class is a design/type and an object is a concrete value created from it.

Start with [method_example.py](method_example.py) and [use_of_vehicle_class.py](use_of_vehicle_class.py).

```python
class Vehicle:
    def __init__(self, make):
        self.make = make


car = Vehicle("Honda")
print(car.make)
```

Visual:

```text
class Vehicle  -----------------> blueprint/type
                                      |
                                      +-- Vehicle("Honda")
                                                  |
                                                  v
                                           car object
                                           make = "Honda"
```

Teach first:

- a class groups data and behavior
- an object is an instance of a class
- `Vehicle("Honda")` creates an object
- `__init__` initializes the object's state

#### 2. `self` and instance state

**Goal:** Understand how each object stores its own data and how methods access that data.

Use [method_binding.py](method_binding.py), then [self_omitted.py](self_omitted.py) as a correction exercise. The current `self_omitted.py` needs repair before it is used: it calls `main()` even though no `main` function exists and creates an object inside the class body.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


first = Student("Asha")
second = Student("Ravi")
print(first.introduce())
print(second.introduce())
```

Visual:

```text
first  ------> Student object: name = "Asha"
second ------> Student object: name = "Ravi"

Student.introduce is shared method code.
self selects which object's name is read.
```

#### 3. Method binding and descriptors

**Goal:** Explain why `object.method()` works and why `Class.method(object)` is the equivalent explicit form.

Use [bound_vs_unbound.py](bound_vs_unbound.py) and [method_binding.py](method_binding.py). Use [important.py](important.py) as an advanced question, not as the first explanation.

```python
calculator.add(5)
Calculator.add(calculator, 5)
```

Both calls provide the same object as `self`:

```text
calculator.add(5)
        |
        v
Calculator.add(calculator, 5)
```

Only after the learner understands this should you introduce that functions stored in classes implement the descriptor protocol and use `__get__` for binding.

#### 4. Encapsulation

**Goal:** Explain why an object should control access to its state instead of allowing every caller to change it freely.

Current status: **missing a dedicated live file and notes**.

Implemented: [encapsulation.py](encapsulation.py) and [encapsulation_notes.md](encapsulation_notes.md).

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def get_balance(self):
        return self._balance
```

The teaching point is not that Python has strict private fields. Explain that `_balance` communicates internal-use intent and methods protect valid state changes.

#### 5. Inheritance

**Goal:** Explain reuse and specialization: a child class receives behavior from a parent class and can add or change behavior.

Current status: **missing a dedicated live file and notes**.

Implemented: [inheritance.py](inheritance.py) and [inheritance_notes.md](inheritance_notes.md).

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    pass


print(Dog().speak())
```

Visual:

```text
Animal
  |
  +---- Dog
          |
          +---- inherits speak()
```

#### 6. Polymorphism and overriding

**Goal:** Show that different objects can respond to the same method call in different ways.

Implemented: [polymorphism.py](polymorphism.py) and [polymorphism_notes.md](polymorphism_notes.md). The idea also appears briefly in [tough_questions.txt](tough_questions.txt).

```python
class Dog:
    def speak(self):
        return "Bark"


class Cat:
    def speak(self):
        return "Meow"


def make_speak(animal):
    print(animal.speak())


make_speak(Dog())
make_speak(Cat())
```

The caller uses one interface, `speak()`, while the object decides the implementation.

#### 7. Abstraction

**Goal:** Explain why callers should depend on required behavior instead of implementation details.

Current status: **missing a dedicated live file and notes**.

Implemented: [abstraction.py](abstraction.py) and [abstraction_notes.md](abstraction_notes.md) using `abc.ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

Explain the difference:

```text
encapsulation -> protect/change how state is accessed
abstraction   -> expose required behavior, hide implementation details
```

#### 8. Method Resolution Order

**Goal:** Explain how Python finds methods through inheritance, especially multiple inheritance.

Teach this after inheritance and overriding. Use [method_resolution_order.md](method_resolution_order.md) and [method_resolution_order.py](method_resolution_order.py).

```text
Child -> ParentA -> ParentB -> object
```

Then teach `super()` as “continue from the next class in the MRO,” not simply “call my direct parent.”

## Phase 2: Python functions

These topics are not inherently OOP. Teach them as Python function concepts before decorators and before advanced method decorators.

```text
1. First-class functions
2. Positional and keyword arguments
3. Closures
4. lambda
5. map, filter, and reduce
6. Decorators
7. Generators
```

### 1. First-class functions

**Goal:** Understand that functions are values that can be stored, passed, and returned.

Use [decorators_notes.md](decorators_notes.md), beginning with its function-object section, and [function_example.py](function_example.py).

```python
def add(first, second):
    return first + second


def run(operation):
    return operation(2, 3)


print(run(add))
```

Visual:

```text
add function object -> passed into run -> called by run -> result 5
```

### 2. Positional and keyword arguments

Teach ordinary arguments first, then `*args` and `**kwargs`:

```python
def show(*args, **kwargs):
    print(args)    # tuple of positional values
    print(kwargs)  # dictionary of named values
```

This prerequisite is already explained in [decorators_notes.md](decorators_notes.md) and must come before the first general wrapper example.

### 3. Closures

**Goal:** Understand how an inner function remembers values from the surrounding function.

Current status: notes exist in [decorators_notes.md](decorators_notes.md), but a dedicated live file would improve the sequence.

Create next: `closures.py`.

```python
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


times_three = create_multiplier(3)
print(times_three(4))  # 12
```

### 4. `lambda`

**Goal:** Teach small anonymous functions only after normal `def` functions and first-class behavior.

Implemented: [closures.py](closures.py) and [closures_notes.md](closures_notes.md).

Implemented: [lambda_functions.py](lambda_functions.py) and [lambda_notes.md](lambda_notes.md).

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda number: number * number, numbers))
print(squares)
```

Explain when not to use `lambda`: if the expression needs a name, multiple steps, or a useful docstring, use `def`.

### 5. `map`, `filter`, and `reduce`

**Goal:** Explain transforming, selecting, and combining data with functions.

Implemented: [functional_tools.py](functional_tools.py) and [functional_tools_notes.md](functional_tools_notes.md).

Create next: `functional_tools.py` and `functional_tools_notes.md`.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
print(list(map(lambda number: number * 2, numbers)))
print(list(filter(lambda number: number % 2 == 0, numbers)))
print(reduce(lambda total, number: total + number, numbers, 0))
```

Teach the roles visually:

```text
map    : every item -> a new item
filter : every item -> keep or discard
reduce : many items -> one result
```

### 6. Decorators

**Goal:** Explain how a reusable wrapper solves repeated cross-cutting behavior.

Use [decorators_notes.md](decorators_notes.md) and [decorators_methods_functions.py](decorators_methods_functions.py).

Teach in this order:

```text
motivation -> function objects -> closures -> args/kwargs -> @decorator
           -> @wraps -> method decorators
```

The notes already cover the motivation, what happens without decorators, `@wraps`, visuals, common mistakes, and expected output.

### 7. Generators

**Goal:** Explain lazy production of values with `yield` and why generators can avoid storing all results at once.

Implemented: [generators.py](generators.py) and [generators_notes.md](generators_notes.md).

Create next: `generators.py` and `generators_notes.md`.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


for number in count_up_to(3):
    print(number)
```

Visual:

```text
next() -> produce one value -> pause
next() -> resume -> produce next value -> pause
```

Teach generators after normal functions and iteration, and before using generator-based pipelines in larger examples.

## Phase 3: OOP + Python features

Teach these only after the learner knows classes, objects, methods, and the relevant function concept.

```text
1. staticmethod
2. classmethod
3. property
4. method decorators
5. class decorators
```

### 1. `staticmethod`

**Prerequisite:** classes, methods, and the difference between a method and an independent function.

Use [static_methods.py](static_methods.py) and [method_example.py](method_example.py).

```python
class MathTools:
    @staticmethod
    def add(first, second):
        return first + second


print(MathTools.add(2, 3))
```

Explain that no `self` or `cls` is supplied. The method is grouped inside the class because it is conceptually related to the class.

### 2. `classmethod`

**Prerequisite:** classes, `self`, class state, inheritance, and decorators.

Use [cls_.py](cls_.py) and [cls_notes.md](cls_notes.md).

```python
class Student:
    @classmethod
    def from_text(cls, text):
        name, course = text.split(",")
        return cls(name.strip(), course.strip())
```

Visual:

```text
Student.from_text(...) -> cls is Student
OnlineStudent.from_text(...) -> cls is OnlineStudent
```

Teach `classmethod` after `staticmethod` so learners can compare:

```text
instance method -> self -> one object
classmethod     -> cls  -> class/subclass
staticmethod    -> neither automatic value
```

### 3. `property`

**Prerequisite:** encapsulation, methods, getters/setters, and validation.

Implemented: [properties.py](properties.py) and [properties_notes.md](properties_notes.md).

Create next: `properties.py` and `properties_notes.md`.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


temperature = Temperature(25)
print(temperature.fahrenheit)
```

Explain that `@property` lets method logic look like attribute access while still controlling calculation or validation.

### 4. Method decorators

**Prerequisite:** decorators, method binding, `self`, `classmethod`, and `staticmethod`.

Use [decorators_methods_functions.py](decorators_methods_functions.py), [decorators_notes.md](decorators_notes.md), and [decorators_methods_functions_interview.md](decorators_methods_functions_interview.md).

```python
class Calculator:
    @log_calls
    def multiply(self, first, second):
        return first * second
```

The key visual is:

```text
calculator.multiply(4, 5)
        |
        v
wrapper(calculator, 4, 5)
        |
        v
multiply(calculator, 4, 5)
```

### 5. Class decorators

**Prerequisite:** classes, callable objects, first-class functions, and decorators.

Current status: **missing a dedicated live file and notes**.

Implemented: [class_decorators.py](class_decorators.py) and [class_decorators_notes.md](class_decorators_notes.md).

```python
def add_label(cls):
    cls.category = "model"
    return cls


@add_label
class User:
    pass


print(User.category)
```

Explain that a class decorator receives a class object and returns the same or a modified class.

## File classification

The folder currently contains one level, `OOPS-basics/`. The files classify as follows.

### Core OOP files

| File | Role | Status | Teach when |
| --- | --- | --- | --- |
| [method_example.py](method_example.py) | Classes, objects, `__init__`, instance state, basic method, static method preview | Live example | Phase 1, topics 1-2 |
| [use_of_vehicle_class.py](use_of_vehicle_class.py) | Importing and using a class from another module | Live example | After classes and objects |
| [method_binding.py](method_binding.py) | `self`, bound calls, explicit class calls | Live example | Phase 1, topics 2-3 |
| [bound_vs_unbound.py](bound_vs_unbound.py) | Bound versus class-accessed methods | Live example | Phase 1, topic 3 |
| [self_omitted.py](self_omitted.py) | Intended `self` omission experiment | Needs repair | Phase 1, topic 2 |
| [important.py](important.py) | Descriptor and `__get__` question | Placeholder/advanced prompt | After method binding |
| [method_resolution_order.py](method_resolution_order.py) | Executable MRO examples | Live example | Phase 1, topic 8 |
| [method_resolution_order.md](method_resolution_order.md) | MRO explanations, multiple inheritance, diamond problem | Notes | Phase 1, topic 8 |
| [tough_questions.txt](tough_questions.txt) | Interview revision for functions, methods, binding, inheritance, MRO, and descriptors | Revision bank | After the relevant phases |

### Python function files

| File | Role | Status | Teach when |
| --- | --- | --- | --- |
| [function_example.py](function_example.py) | Basic function, parameters, return, call | Live example | Phase 0 |
| [decorators_methods_functions.py](decorators_methods_functions.py) | Function decorators and method decorators | Live example | Phase 2, topic 6; Phase 3, topic 4 |
| [decorators_notes.md](decorators_notes.md) | Motivation-first decorator course with function objects, closures, `args/kwargs`, `wraps`, visuals, and mistakes | Notes | Phase 2, topic 6 |
| [decorators_methods_functions_interview.md](decorators_methods_functions_interview.md) | Short interview revision for decorators and methods | Revision notes | After decorators |

### OOP + Python feature files

| File | Role | Status | Teach when |
| --- | --- | --- | --- |
| [static_methods.py](static_methods.py) | `staticmethod` and class access | Live example | Phase 3, topic 1 |
| [cls_.py](cls_.py) | `classmethod`, `cls`, alternate constructors, class state, subclass factory | Live example | Phase 3, topic 2 |
| [cls_notes.md](cls_notes.md) | Detailed `cls` notes and visuals | Notes | Phase 3, topic 2 |
| [decorators_methods_functions.py](decorators_methods_functions.py) | `@classmethod` and `@staticmethod` combined with a decorator | Bridge example | Phase 3, topic 4 |

### Existing supporting material

| File | Role | Recommendation |
| --- | --- | --- |
| [.gitignore](.gitignore) | Ignores Python and local generated files | Keep as repository configuration |
| [learning_roadmap.md](learning_roadmap.md) | This curriculum and file map | Use as the folder index |

## Missing files to create next

Create these in the following order, using the same notes convention:

```text
1. inheritance.py + inheritance_notes.md
2. polymorphism.py + polymorphism_notes.md
3. encapsulation.py + encapsulation_notes.md
4. abstraction.py + abstraction_notes.md
5. closures.py + closures_notes.md
6. lambda_functions.py + lambda_notes.md
7. functional_tools.py + functional_tools_notes.md
8. generators.py + generators_notes.md
9. properties.py + properties_notes.md
10. class_decorators.py + class_decorators_notes.md
```

Every notes file should begin with:

```text
why the topic is needed
what happens without it
what problem that creates
how the topic solves the problem
beginner explanation before code
visuals
runnable examples and expected output
common mistakes
quick revision
link to the live Python file
```

## Final dependency map

```text
functions and calls
        |
        v
classes and objects -> self -> method binding
        |                         |
        v                         v
encapsulation -> inheritance -> polymorphism -> abstraction -> MRO
        |
        +---- property

first-class functions -> args/kwargs -> closures -> lambda -> map/filter/reduce
        |
        v
    decorators
        |
        +---- method decorators
        +---- class decorators
        +---- classmethod / staticmethod comparison
```

## Revision rule

Do not start with decorators just because the current folder contains decorator files. Start with the dependency that makes the topic understandable. Use the existing files as live checkpoints, and use [tough_questions.txt](tough_questions.txt) only after each concept has been explained and run.
