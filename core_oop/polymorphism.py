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


def main():
    print("Without polymorphism, the caller would check every concrete type")
    for thing in (Dog(), Cat(), Robot()):
        make_speak(thing)


if __name__ == "__main__":
    main()
