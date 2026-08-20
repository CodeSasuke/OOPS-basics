"""``self``: what breaks when the instance is not supplied.

Calling ``Animal.speak()`` without an object raises ``TypeError`` because
class access does not bind an instance. The solved calls show both normal
object syntax and explicit class syntax.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


def main():
    my_animal = Animal("Dog")
    print("Without self, Animal.speak() cannot know which name to use")
    print(my_animal.speak())

    # Python supplies my_animal as self in this call.
    print(Animal.speak(my_animal))


if __name__ == "__main__":
    main()
