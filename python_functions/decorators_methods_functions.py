"""Decorators: add behavior without editing every function.

Without a decorator, logging and permission checks would be copied into each
function or method. A decorator receives the original callable and returns a
replacement that adds the shared behavior. ``functools.wraps`` preserves the
wrapped callable's metadata.
"""

from functools import wraps


def add_without_decorator(a, b):
    print("Calling: add_without_decorator")
    return a + b


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add(a, b):
    return a + b


class Calculator:
    @log_calls
    def multiply(self, a, b):
        return a * b


obj = Calculator()


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


def main():
    print("WITHOUT A DECORATOR")
    print(add_without_decorator(2, 3))
    print("The logging statement must be copied into every function")

    print("\nWITH A DECORATOR")
    print(add(2, 3))
    print(obj.multiply(4, 5))
    UserManager.delete_user("alice")
    UserManager.login("bob")


if __name__ == "__main__":
    main()