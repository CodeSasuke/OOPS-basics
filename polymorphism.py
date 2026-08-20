"""Live examples for polymorphism and method overriding."""


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
    for thing in (Dog(), Cat(), Robot()):
        make_speak(thing)


if __name__ == "__main__":
    main()
