# Core OOP Learning Plan

**Navigation:** [Back to main roadmap](../learning_roadmap.md) | [Python functions plan](../python_functions/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

This folder teaches Python's object-oriented foundations. Follow the order below; each step depends on the mental model built by the previous step.

## Teaching convention

For every topic:

```text
1. Ask the learner to predict the behavior.
2. Explain the problem without the concept.
3. Run the live example.
4. Compare prediction with output.
5. Explain the mechanism.
6. Change one line and predict again.
7. Review mistakes and summarize.
```

Do not begin with inheritance or descriptors. First establish what an object is and how `self` selects one object's state.

## Learning order

### 1. Classes and objects

Files:

- [method_example.py](method_example.py)
- [use_of_vehicle_class.py](use_of_vehicle_class.py)

Questions to answer:

- What is a class?
- What is an object?
- Why can two objects from one class hold different values?
- What does `__init__` initialize?

Core visual:

```text
Vehicle class -> blueprint
Vehicle("Honda") -> one object
Vehicle("Toyota") -> another object
```

Run:

```bash
python3 core_oop/method_example.py
python3 core_oop/use_of_vehicle_class.py
```

Checkpoint: create a third `Vehicle` with a different make and print its information.

### 2. `self` and instance methods

Files:

- [method_binding.py](method_binding.py)
- [self_omitted.py](self_omitted.py)

Questions to answer:

- Why is `self` written as the first parameter?
- Is `self` a keyword or a convention?
- Why do two objects produce different output from the same method?

Visual:

```text
student1.introduce() -> introduce(student1)
student2.introduce() -> introduce(student2)
```

Run:

```bash
python3 core_oop/method_binding.py
python3 core_oop/self_omitted.py
```

Checkpoint: call `Student.introduce(student1)` and compare it with `student1.introduce()`.

### 3. Bound and unbound method access

File:

- [bound_vs_unbound.py](bound_vs_unbound.py)

Questions to answer:

- What does `object.method` remember?
- Why does `Class.method(object, ...)` need the object explicitly?
- What error occurs if `self` is missing?

Visual:

```text
calculator.add(5)              -> object supplied automatically
Calculator.add(calculator, 5)  -> object supplied manually
```

Run:

```bash
python3 core_oop/bound_vs_unbound.py
```

Checkpoint: uncomment the missing-`self` call and predict the `TypeError` before running it.

### 4. Encapsulation

Files:

- [encapsulation.py](encapsulation.py)
- [encapsulation_notes.md](encapsulation_notes.md)

Questions to answer:

- What invalid state can a caller create by changing data directly?
- Where should validation rules live?
- What does a leading underscore communicate in Python?

Run:

```bash
python3 core_oop/encapsulation.py
```

Checkpoint: try a negative deposit and explain which object rule rejects it.

### 5. Inheritance

Files:

- [inheritance.py](inheritance.py)
- [inheritance_notes.md](inheritance_notes.md)

Questions to answer:

- What behavior belongs in the parent?
- What behavior is specific to the child?
- Is the child genuinely an "is-a" form of the parent?

Visual:

```text
Vehicle -> Car -> ElectricCar
 common    specialized    more specialized
```

Run:

```bash
python3 core_oop/inheritance.py
```

Checkpoint: add a `Truck(Vehicle)` class with a `load()` method.

### 6. Polymorphism and overriding

Files:

- [polymorphism.py](polymorphism.py)
- [polymorphism_notes.md](polymorphism_notes.md)

Questions to answer:

- Why should the caller use `thing.speak()` instead of checking every type?
- How can unrelated classes support the same operation?
- What is method overriding?

Run:

```bash
python3 core_oop/polymorphism.py
```

Checkpoint: add `Parrot.speak()` without editing `make_speak()`.

### 7. Abstraction

Files:

- [abstraction.py](abstraction.py)
- [abstraction_notes.md](abstraction_notes.md)

Questions to answer:

- What behavior must every shape provide?
- Why should `Shape()` itself be rejected?
- How is abstraction different from encapsulation?

Run:

```bash
python3 core_oop/abstraction.py
```

Checkpoint: create a `Triangle` that implements `area()`.

### 8. Method Resolution Order

Files:

- [method_resolution_order.py](method_resolution_order.py)
- [method_resolution_order.md](method_resolution_order.md)

Questions to answer:

- Where does Python search first?
- What happens when a child does not define a method?
- Why is multiple inheritance ambiguous?
- How does `super()` continue through the MRO?

Visual:

```text
Child -> ParentA -> ParentB -> object
```

Run:

```bash
python3 core_oop/method_resolution_order.py
```

### 9. Descriptors and `__get__`

Files:

- [__get__.py](__get__.py)
- [__get___notes.md](__get___notes.md)
- [important.py](important.py)

Teach this last because it explains the machinery behind method binding.

Questions to answer:

- What does `__get__` receive for class access?
- What does it receive for instance access?
- How does it return a callable with `self` remembered?

Run:

```bash
python3 core_oop/__get__.py
```

Visual:

```text
object.method
     |
     v
__get__(object, Class)
     |
     v
bound method with self attached
```

## Completion checklist

- [ ] I can create a class and instantiate objects.
- [ ] I can explain `self` using an object diagram.
- [ ] I can expand `object.method(...)` into `Class.method(object, ...)`.
- [ ] I can identify a good inheritance relationship.
- [ ] I can explain polymorphism without relying only on inheritance.
- [ ] I can distinguish encapsulation from abstraction.
- [ ] I can read a simple MRO.
- [ ] I can explain why `__get__` is involved in method binding.

**Navigation:** [Back to main roadmap](../learning_roadmap.md) | [Python functions plan](../python_functions/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)
