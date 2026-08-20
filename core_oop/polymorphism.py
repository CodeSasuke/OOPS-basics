"""Polymorphism: one operation, many implementations.

Without polymorphism, ``make_speak`` would need ``if`` statements for every
kind of object. The solution is a shared method name: each object supplies
its own ``speak`` behavior and the caller stays unchanged.
"""


class Dog:
    def speak(self):
        return "Bark"


class Cat:
    def speak(self):
        return "Meow"


class Robot:
    def speak(self):
        return "Beep"


def make_speak(thing):
    print(f"{type(thing).__name__}: {thing.speak()}")


def make_speak_without_polymorphism(thing):
    if isinstance(thing, Dog):
        return "Dog: Bark"
    if isinstance(thing, Cat):
        return "Cat: Meow"
    if isinstance(thing, Robot):
        return "Robot: Beep"
    return "Unknown sound"


def main():
    print("WITHOUT POLYMORPHISM")
    for thing in (Dog(), Cat(), Robot()):
        print(make_speak_without_polymorphism(thing))

    print("\nWITH POLYMORPHISM")
    for thing in (Dog(), Cat(), Robot()):
        make_speak(thing)


if __name__ == "__main__":
    main()
