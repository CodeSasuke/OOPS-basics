# `cls` in Python

`cls` is the conventional name for the first parameter of a **class method**. It refers to the class itself, just as `self` refers to one particular object.

A class method is created with `@classmethod`:

```python
class Student:
    @classmethod
    def from_text(cls, text):
        name, course = text.split(",")
        return cls(name.strip(), course.strip())
```

## Visual: what gets passed?

```text
                          class method call
                    Student.from_text("Asha, Python")
                                      |
                                      v
                         cls ------------------+
                          |                    |
                          v                    |
                    +-----------+             |
                    |  Student  |             |
                    +-----------+             |
                          |                    |
                          +---- return cls(...) 
                                      |
                                      v
                           +------------------+
                           | Student instance |
                           | name = "Asha"    |
                           | course = "Python"|
                           +------------------+
```

The method can use `cls` to read class data, create an object, or return an object of the class that called it.

## `self` versus `cls`

| Name | Refers to | Used by | Typical purpose |
| --- | --- | --- | --- |
| `self` | One object | Instance method | Read or change object-specific data |
| `cls` | The class | Class method | Read or change shared data, or create objects |

```python
class Student:
    school = "Dhanushya Prep"  # shared by the class and its students

    def __init__(self, name):
        self.name = name         # different for every object

    def describe(self):          # receives self
        return f"{self.name} studies at {self.school}."

    @classmethod
    def change_school(cls, new_school):  # receives cls
        cls.school = new_school
```

## Why use `@classmethod`?

### 1. Alternate constructors

A normal constructor accepts the regular argument format. A class method can provide another readable way to build the same kind of object.

```python
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    @classmethod
    def from_text(cls, text):
        name, course = text.split(",")
        return cls(name.strip(), course.strip())

student = Student.from_text("Ravi, Python")
print(student.name)    # Ravi
print(student.course)  # Python
```

### 2. Shared class state

A class method is a good place to update information shared by all instances.

```python
class Student:
    school = "Dhanushya Prep"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("Dhanushya Advanced Prep")
print(Student.school)
```

### 3. Subclass-friendly factories

Use `cls(...)`, not `Student(...)`, inside a class method. Then a subclass can reuse the method and receive an object of the subclass type.

```python
class OnlineStudent(Student):
    pass

online = OnlineStudent.from_text("Mina, Data Structures")
print(type(online).__name__)  # OnlineStudent
```

This is the important difference:

```python
return cls(name, course)      # respects the class that called the method
# return Student(name, course) # always creates Student, even for subclasses
```

## Run the live examples

The complete runnable examples are in [cls_.py](cls_.py).

```bash
python3 oop_python_features/cls_.py
```

Expected output:

```text
Asha studies Python at Dhanushya Prep.
Ravi studies Object-Oriented Programming at Dhanushya Prep.
Created students: 2
Shared school after change: Dhanushya Advanced Prep
Factory returned: OnlineStudent
Mina studies Data Structures at Dhanushya Advanced Prep.
```

## Important rules

- `cls` is a convention, but use it because it makes the method's purpose immediately clear.
- `@classmethod` automatically passes the class as the first argument.
- Call a class method from either the class or an instance, but class-level calls make the intent clearer.
- Use `self` for per-object state and `cls` for class-level behavior or data.
- A class method is not the same as a static method: a static method receives neither `self` nor `cls` automatically.

## Quick comparison

```python
class Example:
    def instance_method(self):
        return self                 # one object

    @classmethod
    def class_method(cls):
        return cls                  # the class

    @staticmethod
    def static_method():
        return "no automatic object or class"
```
