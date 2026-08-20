# How do decorators affect functions and methods?
# 31. How do decorators affect functions and methods?
# Answer: A decorator receives a function and returns a replacement function or object.
# For methods, the decorator can preserve, change, or remove normal argument binding.
# Use functools.wraps when writing wrappers to preserve function metadata.

from functools import wraps

# Decorator example for a normal function

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


# Decorator example for a method
class Calculator:
    @log_calls
    def multiply(self, a, b):
        return a * b


obj = Calculator()
print(obj.multiply(4, 5))

# Explanation:
# A decorator wraps the original function and returns a new function.
# For methods, Python automatically passes the instance as the first argument.
# @wraps keeps the original function metadata like name and docstring intact.


# Additional example: decorators with @classmethod, @staticmethod, and logging/auth style

def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Checking permissions...")
        print("Access granted for admin user")
        return func(*args, **kwargs)
    return wrapper


class UserManager:
    admin_name = "admin"

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

# Explanation:
# - @classmethod makes the first parameter cls instead of self.
# - @staticmethod does not receive self or cls.
# - A decorator can be used to add behavior such as permission checks or logging.
# - In real projects, decorators are often used for authentication, logging, caching, etc.