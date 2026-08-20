# Interview Question: Decorators and Methods

**Navigation:** [Python functions plan](learning_plan.md) | [Main roadmap](../learning_roadmap.md) | [Core OOP plan](../core_oop/learning_plan.md) | [OOP + Python features plan](../oop_python_features/learning_plan.md)

## Q1. How do decorators affect functions and methods in Python?

### Answer:
A decorator is a function that takes another function as input and returns a new function or callable object. It is used to modify or extend the behavior of a function without changing its original code.

Example:

```python
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add(a, b):
    return a + b


print(add(2, 3))
```

Output:

```python
Calling: add
5
```

For methods, decorators work similarly. Python automatically binds the instance to the method when it is called.

Example:

```python
class Calculator:
    @log_calls
    def multiply(self, a, b):
        return a * b


obj = Calculator()
print(obj.multiply(4, 5))
```

Output:

```python
Calling: multiply
20
```

### Key points:
- A decorator receives a function and returns a replacement function.
- It can add behavior before or after the original function runs.
- For methods, normal binding still works unless the decorator changes it.
- `functools.wraps` preserves the original function name and metadata.

---

## Q2. How does a decorator behave with `@classmethod` and `@staticmethod`?

### Answer:
A decorator can be applied to methods as well. The effect depends on the type of method:

- `@classmethod`: the first argument is `cls`
- `@staticmethod`: no implicit instance or class is passed

Example:

```python
from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Checking permissions...")
        return func(*args, **kwargs)
    return wrapper


class UserManager:
    @classmethod
    @require_admin
    def delete_user(cls, username):
        print(f"Deleting user: {username}")

    @staticmethod
    @require_admin
    def login(username):
        print(f"User {username} logged in")


UserManager.delete_user("alice")
UserManager.login("bob")
```

### Explanation:
- `@classmethod` receives the class as the first argument.
- `@staticmethod` receives neither `self` nor `cls`.
- The decorator can add checks like authentication, authorization, or logging.

---

## Q3. Why do we use `functools.wraps` in decorators?

### Answer:
`functools.wraps` copies the metadata from the original function to the wrapper function. This keeps the function name, docstring, and module information intact.

Without `@wraps`, debugging and documentation may become confusing because the wrapper may appear to have a different name.

Example:

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper


@my_decorator
def greet():
    """Greets the user."""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```python
greet
Greets the user.
```

---

## Short Final Answer:
Decorators modify or extend the behavior of functions and methods by wrapping them in another function. They are especially useful for logging, access control, validation, and caching. For methods, Python handles argument binding automatically, and `functools.wraps` helps preserve the original metadata.
