# Decorators in Python

A **decorator** is a callable that receives another function or method and returns a replacement callable. It lets us add behavior without editing the original function body.

Common uses include:

- logging and tracing
- authentication and authorization
- validation
- timing and performance measurement
- caching
- retries
- registering functions as commands or routes

## The core idea

Functions are objects in Python. They can be stored in variables, passed into other functions, and returned from functions.

```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())  # Hello
```

A decorator uses this fact:

```python
def make_louder(function):
    def wrapper():
        return function().upper()
    return wrapper
```

The decorator accepts `function` and returns `wrapper`.

## Why are functions objects?

In Python, a function definition creates a function object and binds a name to it. The name is only a reference; the function object is the value stored somewhere in memory.

```python
def greet():
    return "Hello"


print(greet)       # <function greet at ...>
print(type(greet)) # <class 'function'>
```

The exact memory address in the first output changes between runs, but the important part is that `greet` is an object whose type is `function`.

Visual model:

```text
name                         object in memory

greet  --------------------> function object
                              - executable code
                              - name: "greet"
                              - docstring
                              - global-variable context
                              - custom attributes
```

Python gives functions the same object behavior available to other values. A function can be:

1. assigned to another name
2. passed as an argument
3. returned from another function
4. stored in a list, tuple, or dictionary
5. given attributes
6. inspected at runtime

### 1. Assigning a function to another name

Assignment does not copy the function. Both names refer to the same object:

```python
def greet():
    return "Hello"


say_hello = greet

print(greet is say_hello)  # True
print(say_hello())         # Hello
```

The `is` expression checks object identity. Since `greet` and `say_hello` point to the same function object, it returns `True`.

```text
greet     --+
           +----> one function object
say_hello -+
```

This is why renaming a function reference does not create a new function.

### 2. Passing a function as an argument

Because a function is a value, another function can receive it as a parameter. A function passed this way is often called a **callback** or a **higher-order function argument**.

```python
def add(first, second):
    return first + second


def run_operation(operation, first, second):
    return operation(first, second)


print(run_operation(add, 2, 3))  # 5
```

Notice the difference between `add` and `add()`:

```python
run_operation(add, 2, 3)    # passes the function object
run_operation(add(2, 3), 2, 3)  # wrong: passes the result 5
```

Use parentheses when you want to call a function now. Leave them off when you want to pass the function itself.

### 3. Returning a function

A function can create and return another function. The returned function can be called later:

```python
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


times_three = create_multiplier(3)
print(times_three(4))  # 12
```

Visual:

```text
create_multiplier(3)
        |
        +--> creates multiply(number)
        |       remembers factor = 3
        |
        +--> returns multiply function object

times_three(4) -------> 4 * 3 = 12
```

The inner function remembers `factor` even after `create_multiplier` has finished. This combination of a function and remembered surrounding values is called a **closure**. Decorators use the same idea: the wrapper remembers the original function.

### 4. Storing functions in collections

Functions can be selected dynamically from a collection:

```python
def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


operations = {
    "+": add,
    "*": multiply,
}


choice = "*"
print(operations[choice](4, 5))  # 20
```

This avoids a long `if`/`elif` chain. The dictionary maps symbols to behavior, not just to data.

### 5. Functions can have attributes

Function objects can store custom attributes, although this is less common than using a class:

```python
def greet():
    return "Hello"


greet.category = "welcome"
print(greet.category)  # welcome
```

Decorators sometimes attach metadata such as a route, permission, or retry count to a function. For larger amounts of state, a class or a callable object is usually clearer.

### 6. Functions can be inspected

Functions expose useful metadata:

```python
def greet(name: str) -> str:
    """Return a greeting for one person."""
    return f"Hello, {name}"


print(greet.__name__)       # greet
print(greet.__doc__)        # Return a greeting for one person.
print(greet.__annotations__)# {'name': <class 'str'>, 'return': <class 'str'>}
```

The `inspect` module can inspect the signature too:

```python
from inspect import signature


print(signature(greet))  # (name: str) -> str
```

This metadata is useful for debugging, documentation tools, command frameworks, and testing libraries. `functools.wraps` matters because it copies important metadata from a decorated function to its wrapper.

## Why this matters for decorators

The decorator pattern is possible because functions can travel through the program as values:

```text
original function
       |
       v
decorator receives it as an argument
       |
       v
decorator creates a wrapper function
       |
       v
decorator returns the wrapper
       |
       v
name now refers to the wrapper
```

```python
def log_calls(function):
    def wrapper(*args, **kwargs):
        print("Before the call")
        result = function(*args, **kwargs)
        print("After the call")
        return result
    return wrapper


def add(first, second):
    return first + second


add = log_calls(add)
print(add(2, 3))
```

Output:

```text
Before the call
After the call
5
```

The original `add` function is not edited. Its reference is passed into `log_calls`, and the name `add` is rebound to the returned wrapper. That is the central reason decorators can add logging, validation, authentication, caching, or timing around existing behavior.

## Function object versus function call

Keep these two ideas separate:

```python
add       # the function object; can be passed or stored
add(2, 3) # calls the function and produces its return value
```

```text
add       -> function object
add(2, 3) -> 5
```

Many decorator mistakes come from confusing the function object with the result of calling it.

## Visual: decorator call flow

```text
Before decoration:

    greet  ----------------------->  original greet function

Apply decorator:

    greet = make_louder(greet)
             |
             +---- receives original function
             +---- creates wrapper
             +---- returns wrapper

After decoration:

    greet  ----------------------->  wrapper
                                      |
                                      +-- calls original greet
                                      +-- changes the result
```

## Basic example

```python
def make_louder(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper


@make_louder
def greet():
    return "hello"


print(greet())  # HELLO
```

This syntax:

```python
@make_louder
def greet():
    return "hello"
```

means exactly this:

```python
def greet():
    return "hello"


greet = make_louder(greet)
```

The function name now points to the returned wrapper.

## A practical logging decorator

The live file [decorators_methods_functions.py](decorators_methods_functions.py) uses this pattern:

```python
from functools import wraps


def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling: {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@log_calls
def add(first, second):
    return first + second


print(add(2, 3))
```

Output:

```text
Calling: add
5
```

### Why `*args` and `**kwargs`?

A general-purpose decorator should accept any positional and keyword arguments:

```text
add(2, 3)                    -> args = (2, 3), kwargs = {}
add(first=2, second=3)       -> args = (), kwargs = {"first": 2, "second": 3}
```

The wrapper forwards both collections to the original function:

```python
return function(*args, **kwargs)
```

## Decorators and methods

A method is still a function stored on a class. When accessed through an instance, Python binds the instance as the first argument.

```python
from functools import wraps


def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling: {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


class Calculator:
    @log_calls
    def multiply(self, first, second):
        return first * second


calculator = Calculator()
print(calculator.multiply(4, 5))
```

Visual:

```text
calculator.multiply(4, 5)
        |
        v
wrapper(calculator, 4, 5)
        |
        v
multiply(calculator, 4, 5)
        |
        v
        20
```

The wrapper must forward the instance in `args`. A wrapper that accepts only `first, second` would fail because the bound instance is also passed.

## Why use `functools.wraps`?

Without `@wraps`, Python reports the wrapper's metadata instead of the original function's metadata.

```python
from functools import wraps


def explain(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper


@explain
def greet():
    """Greet the learner."""
    return "Hello"


print(greet.__name__)  # greet
print(greet.__doc__)   # Greet the learner.
```

`@wraps(function)` preserves useful attributes such as `__name__`, `__doc__`, `__module__`, and `__wrapped__`. This helps debugging, introspection, documentation tools, and other decorators.

## Adding behavior before and after a function

```python
from functools import wraps


def trace(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Finished {function.__name__}")
        return result
    return wrapper
```

The important rule is to return the original result. Otherwise, a function that used to return a value may unexpectedly return `None`.

## A decorator that validates input

```python
from functools import wraps


def positive_numbers(function):
    @wraps(function)
    def wrapper(first, second):
        if first <= 0 or second <= 0:
            raise ValueError("Both numbers must be positive")
        return function(first, second)
    return wrapper


@positive_numbers
def divide(first, second):
    return first / second


print(divide(10, 2))  # 5.0
```

For reusable decorators, `*args` and `**kwargs` are usually preferable. Explicit parameters can be useful when the decorator is intentionally restricted to one function signature.

## Decorators with their own arguments

A parameterized decorator needs one extra function layer:

```python
from functools import wraps


def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi")


say_hi()
```

Visual:

```text
@repeat(3)
def say_hi(): ...

is evaluated as:

say_hi = repeat(3)(say_hi)
         |       |
         |       +-- original function
         +---------- returns the actual decorator
```

There are three layers:

```text
repeat(times) -> decorator(function) -> wrapper(*args, **kwargs)
```

## Decorator order

When several decorators are stacked, decoration happens from the bottom upward, like nested function calls.

```python
@outer
@inner
def work():
    pass
```

means:

```python
work = outer(inner(work))
```

At runtime, the outer wrapper runs first:

```text
call work()
   |
   v
outer wrapper
   |
   v
inner wrapper
   |
   v
original work
```

Order matters when decorators perform validation, logging, authentication, or caching.

## `classmethod` and `staticmethod`

Decorators can be combined with method descriptors. The order is usually written like this:

```python
from functools import wraps


def require_admin(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Checking permissions...")
        print("Access granted for admin user")
        return function(*args, **kwargs)
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
```

For `delete_user`, the effective expression is:

```python
UserManager.delete_user = classmethod(require_admin(delete_user))
```

For `login`, it is:

```python
UserManager.login = staticmethod(require_admin(login))
```

- `classmethod` supplies `cls`.
- `staticmethod` supplies neither `self` nor `cls`.
- `require_admin` receives the underlying function and forwards all arguments.

## A decorator is not always a function

A class can also implement `__call__` and act as a decorator:

```python
class CountCalls:
    def __init__(self, function):
        self.function = function
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.function(*args, **kwargs)


@CountCalls
def add(first, second):
    return first + second


print(add(1, 2))  # 3
print(add.count)  # 1
```

A callable object is useful when the decorator needs to keep state between calls. If using this style, remember that metadata handling requires extra care because `functools.wraps` is designed for function wrappers.

## Common mistakes

### Forgetting to return the wrapper

```python
def broken(function):
    def wrapper():
        return function()
    # Missing: return wrapper
```

The decorated name becomes `None`.

### Forgetting to return the original result

```python
def also_broken(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        # Missing: return function(...)
    return wrapper
```

The call runs, but the caller receives `None`.

### Forgetting method arguments

This fails for normal instance methods:

```python
def broken_method_decorator(function):
    def wrapper(first, second):
        return function(first, second)
    return wrapper
```

Use `*args, **kwargs` so `self` can pass through.

### Hiding exceptions or side effects

Decorators change behavior around a function. Keep them small, name them clearly, and make logging, authorization, or error handling visible to readers.

## Run the repository example

From this directory:

```bash
python3 decorators_methods_functions.py
```

The script demonstrates:

```text
Calling: add
5
Calling: multiply
20
Checking permissions...
Access granted for admin user
Deleting user: alice
Checking permissions...
Access granted for admin user
User bob logged in
```

## Quick revision

```text
Decorator = callable that receives a callable and returns a callable

@decorator
def function(): ...

is equivalent to:

function = decorator(function)
```

Remember:

1. A decorator wraps or replaces behavior.
2. The wrapper should usually accept `*args, **kwargs`.
3. Forward arguments and return the original result.
4. Use `functools.wraps` for preserved metadata.
5. Stacked decorators are applied bottom to top.
6. Methods need their implicit `self`, `cls`, or neither forwarded correctly.
