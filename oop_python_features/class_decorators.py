"""Class decorators: add class behavior without editing each class.

Without a decorator, metadata and registration code would be repeated after
every class definition. The solution is a callable that receives a class,
changes or records it, and returns the finished class.
"""


def add_model_metadata(cls):
    def describe(self):
        return f"{cls.__name__} belongs to the {self.category} category"

    cls.category = "model"
    cls.describe = describe
    return cls


@add_model_metadata
class User:
    def __init__(self, name: str):
        self.name = name


def register(cls):
    registry.append(cls)
    return cls


registry = []


@register
class Report:
    pass


def main():
    print("Without class decorators, metadata and registration would be manual")
    user = User("Asha")
    print(User.category)
    print(user.describe())
    print([registered.__name__ for registered in registry])


if __name__ == "__main__":
    main()
